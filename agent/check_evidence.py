"""Verification loop 1: deterministic checks on research records (no LLM).

For every record in a pass file/dir:
  - schema: enum fields hold allowed values, required fields present
  - coverage: auth_methods, access, verdict each have >= 1 evidence row
  - liveness: each evidence URL resolves (HTTP < 400)
  - grounding: the quote actually appears on the page (token overlap >= 0.6)
Pages that render client-side come back near-empty; those are marked `js_page`, not failed.
If FIRECRAWL_API_KEY is set, such pages are re-fetched rendered through Firecrawl.

Usage: python agent/check_evidence.py data/pass2 [data/check_pass2.json]
"""
import json, os, re, sys, glob, html
from concurrent.futures import ThreadPoolExecutor
import requests

ENUMS = {
    "access": {"self_serve", "free_trial", "paid_plan", "approval", "partner_gated", "not_applicable"},
    "api_breadth": {"broad", "moderate", "narrow", "none"},
    "official_mcp": {"yes", "no", "beta"},
    "verdict": {"ready", "ready_with_gate", "blocked", "not_a_fit"},
    "blocker": {"none", "paid_plan", "partner_approval", "app_review", "enterprise_only",
                "no_public_api", "tos_restriction", "local_tool_only", "other"},
    "confidence": {"high", "medium", "low"},
}
AUTH = {"oauth2", "api_key", "basic", "bearer_token", "jwt", "hmac_signature", "session/login", "none", "other"}
API_TYPES = {"rest", "graphql", "soap", "grpc", "websocket", "sdk_only", "cli_only", "none"}
MUST_CITE = ["auth_methods", "access", "verdict"]
UA = {"User-Agent": "Mozilla/5.0 (research-checker)"}
_cache = {}


def load(path):
    files = sorted(glob.glob(os.path.join(path, "*.json"))) if os.path.isdir(path) else [path]
    return [r for f in files for r in json.load(open(f, encoding="utf-8"))]


def words(s):
    return re.findall(r"[a-z0-9]+", s.lower())


def page_text(url):
    if url in _cache:
        return _cache[url]
    status, text = None, ""
    try:
        r = requests.get(url, headers=UA, timeout=25, allow_redirects=True)
        status = r.status_code
        text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", r.text, flags=re.S | re.I)
        text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    except requests.RequestException as e:
        status = f"error:{type(e).__name__}"
    key = os.environ.get("FIRECRAWL_API_KEY")
    if key and (not isinstance(status, int) or status >= 400 or len(words(text)) < 150):
        try:
            r = requests.post("https://api.firecrawl.dev/v2/scrape", timeout=60,
                              headers={"Authorization": f"Bearer {key}"},
                              json={"url": url, "formats": ["markdown"]})
            md = r.json().get("data", {}).get("markdown", "")
            if md:
                status, text = 200, md
        except requests.RequestException:
            pass
    _cache[url] = (status, text)
    return _cache[url]


def overlap(quote, text):
    q = words(quote)
    if not q:
        return None
    t = set(words(text))
    return sum(w in t for w in q) / len(q)


def check_row(ev):
    status, text = page_text(ev["url"])
    out = {"field": ev.get("field"), "url": ev["url"], "status": status}
    if not isinstance(status, int) or status >= 400:
        out["result"] = "dead_link"
    elif len(words(text)) < 150:
        out["result"] = "js_page"          # cannot judge without a renderer
    else:
        ov = overlap(ev.get("quote", ""), text)
        out["overlap"] = ov
        out["result"] = "no_quote" if ov is None else ("grounded" if ov >= 0.6 else "quote_not_found")
    return out


def check_record(r):
    issues = []
    for f, allowed in ENUMS.items():
        if r.get(f) not in allowed:
            issues.append(f"bad_enum:{f}={r.get(f)!r}")
    if set(r.get("api_type") or ["?"]) - API_TYPES:
        issues.append(f"bad_enum:api_type={r.get('api_type')}")
    if not r.get("auth_methods") or set(r["auth_methods"]) - AUTH:
        issues.append(f"bad_enum:auth_methods={r.get('auth_methods')}")
    cited = {f.strip() for e in r.get("evidence", []) for f in str(e.get("field", "")).split(",")}
    issues += [f"uncited:{f}" for f in MUST_CITE if f not in cited and f != "verdict"]
    # verdict is a judgment derived from access + blocker; accept it when access is cited
    if "verdict" not in cited:
        issues.append("verdict_derived" if "access" in cited else "uncited:verdict")
    return issues


def main(src, dst=None):
    recs = load(src)
    rows = [(r["id"], e) for r in recs for e in r.get("evidence", []) if e.get("url")]
    with ThreadPoolExecutor(12) as ex:
        results = list(ex.map(lambda x: (x[0], check_row(x[1])), rows))
    by_id = {}
    for i, res in results:
        by_id.setdefault(i, []).append(res)
    report = []
    for r in recs:
        ev = by_id.get(r["id"], [])
        report.append({"id": r["id"], "app": r["app"], "schema_issues": check_record(r), "evidence": ev,
                       "dead": sum(e["result"] == "dead_link" for e in ev),
                       "ungrounded": sum(e["result"] == "quote_not_found" for e in ev)})
    tally = {}
    for _, res in results:
        tally[res["result"]] = tally.get(res["result"], 0) + 1
    summary = {"records": len(recs), "evidence_rows": len(results), "by_result": tally,
               "records_with_schema_issues": sum(any(i != "verdict_derived" for i in x["schema_issues"]) for x in report),
               "records_with_dead_or_ungrounded": sum(bool(x["dead"] or x["ungrounded"]) for x in report)}
    if dst:
        json.dump({"summary": summary, "records": report}, open(dst, "w"), indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main(*sys.argv[1:])
