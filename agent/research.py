"""Toolkit research agent — standalone, reproducible version of the pipeline.

    pass1  recall-only draft (no tools)          -> data/pass1/
    pass2  web-grounded research (Firecrawl)     -> data/pass2/
    pass3  adversarial verifier (Firecrawl)      -> data/pass3/

Each pass uses the prompt file in prompts/ verbatim, so this script and the
Claude Code run that produced the published data follow the same instructions.

Needs: ANTHROPIC_API_KEY (or `ant auth login`), FIRECRAWL_API_KEY.
    pip install anthropic requests
    python agent/research.py pass2 --ids 1-10
    python agent/research.py pass3 --ids 1-10
    python agent/check_evidence.py data/pass2 data/check_pass2.json
"""
import argparse, json, os, re, sys
import anthropic, requests
from anthropic import beta_tool

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FC = "https://api.firecrawl.dev/v2"
MODEL = os.environ.get("RESEARCH_MODEL", "claude-opus-5-5")
client = anthropic.Anthropic()


def _fc(path, body):
    r = requests.post(f"{FC}/{path}", json=body, timeout=90,
                      headers={"Authorization": f"Bearer {os.environ['FIRECRAWL_API_KEY']}"})
    r.raise_for_status()
    return r.json().get("data", {})


@beta_tool
def web_search(query: str) -> str:
    """Search the web. Returns top results as title, url, description.

    Args:
        query: Search query, e.g. "Pipedrive API authentication OAuth".
    """
    data = _fc("search", {"query": query, "limit": 6})
    hits = data.get("web", data) if isinstance(data, dict) else data
    return json.dumps([{k: h.get(k) for k in ("title", "url", "description")} for h in hits][:6])


@beta_tool
def read_page(url: str) -> str:
    """Fetch a page (JS rendered) and return its main content as markdown, truncated to 12k chars.

    Args:
        url: Absolute URL of the page to read.
    """
    md = _fc("scrape", {"url": url, "formats": ["markdown"], "onlyMainContent": True}).get("markdown", "")
    return md[:12000] or "(empty page)"


def prompt(name):
    return open(os.path.join(ROOT, "prompts", name), encoding="utf-8").read()


def parse_ids(spec, apps):
    if spec == "all":
        return [a["id"] for a in apps]
    out = []
    for part in spec.split(","):
        lo, _, hi = part.partition("-")
        out += range(int(lo), int(hi or lo) + 1)
    return out


def extract_json(text):
    m = re.search(r"\[.*\]", text, re.S)
    if not m:
        raise ValueError("no JSON array in model output")
    return json.loads(m.group(0))


def run_pass(stage, items):
    system = prompt("schema.md") + "\n\n" + prompt({"pass1": "pass1_recall.md", "pass2": "pass2_grounded.md",
                                                    "pass3": "pass3_verify.md"}[stage])
    system += "\n\nReturn the JSON array as your final message, with no other text."
    user = json.dumps(items, indent=1)
    tools = [] if stage == "pass1" else [web_search, read_page]
    if not tools:
        msg = client.messages.create(model=MODEL, max_tokens=16000, system=system,
                                     messages=[{"role": "user", "content": user}])
        return extract_json("".join(b.text for b in msg.content if b.type == "text"))
    runner = client.beta.messages.tool_runner(
        model=MODEL, max_tokens=32000, system=system, tools=tools, max_iterations=60,
        output_config={"effort": "high"},
        messages=[{"role": "user", "content": user}],
    )
    final = runner.until_done()
    return extract_json("".join(b.text for b in final.content if b.type == "text"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["pass1", "pass2", "pass3"])
    ap.add_argument("--ids", default="all")
    ap.add_argument("--batch", type=int, default=5, help="apps per model call")
    a = ap.parse_args()

    apps = json.load(open(os.path.join(ROOT, "data/apps.json")))
    ids = parse_ids(a.ids, apps)
    if a.stage == "pass3":   # verifier consumes pass-2 records
        src = {}
        for f in os.listdir(os.path.join(ROOT, "data/pass2")):
            for r in json.load(open(os.path.join(ROOT, "data/pass2", f), encoding="utf-8")):
                src[r["id"]] = r
        items_all = [src[i] for i in ids if i in src]
    else:
        items_all = [x for x in apps if x["id"] in ids]

    out_dir = os.path.join(ROOT, "data", a.stage)
    os.makedirs(out_dir, exist_ok=True)
    for k in range(0, len(items_all), a.batch):
        chunk = items_all[k:k + a.batch]
        lo, hi = chunk[0]["id"], chunk[-1]["id"]
        path = os.path.join(out_dir, f"run_{lo:03d}_{hi:03d}.json")
        if os.path.exists(path):          # resume: skip finished batches
            continue
        try:
            recs = run_pass(a.stage, chunk)
        except (anthropic.APIError, requests.RequestException, ValueError) as e:
            print(f"[{lo}-{hi}] failed: {e}", file=sys.stderr)   # leave for re-run
            continue
        json.dump(recs, open(path, "w", encoding="utf-8"), indent=1)
        print(f"[{lo}-{hi}] {len(recs)} records -> {path}")


if __name__ == "__main__":
    main()
