"""Assemble final dataset + stats and render docs/index.html (single self-contained page).

Final record per app = pass-3 (verified) record, falling back to pass 2 if a verifier batch is missing.
Outputs:
  docs/index.html      the case study (data embedded, no external requests)
  docs/data.json       machine-readable: records + stats + accuracy + verification log
  docs/findings.md     plain-text patterns + table for agents / quick reading
"""
import json, os, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda *p: os.path.join(ROOT, "data", *p)


def load_dir(name):
    out = {}
    for f in sorted(glob.glob(D(name, "*.json"))):
        for r in json.load(open(f, encoding="utf-8")):
            out[r["id"]] = r
    return out


def main():
    apps = json.load(open(D("apps.json")))
    p1, p2, p3 = load_dir("pass1"), load_dir("pass2"), load_dir("pass3")
    catalog = json.load(open(D("composio_catalog.json")))
    hc = json.load(open(D("human_corrections.json")))["corrections"]
    final = []
    for a in apps:
        r = dict(p3.get(a["id"]) or p2[a["id"]])
        r["category"] = a["category"]
        r["composio_toolkit"] = catalog.get(str(a["id"]))
        r["source_pass"] = "pass3" if a["id"] in p3 else "pass2"
        r["human_corrected"] = []
        for c in hc:
            if c["id"] == a["id"]:
                r["human_corrected"].append({"field": c["field"], "from": r.get(c["field"]), "to": c["to"],
                                             "why": c["why"], "url": c["url"]})
                r[c["field"]] = c["to"]
        # changes from pass 1 -> final on the headline fields, for the "what the loops changed" view
        r["changed_since_pass1"] = [f for f in ("access", "verdict", "official_mcp", "blocker")
                                    if p1.get(a["id"], {}).get(f) != r.get(f)]
        final.append(r)

    C = collections.Counter
    cats = list(dict.fromkeys(a["category"] for a in apps))
    auth = C(m for r in final for m in r["auth_methods"])
    primary_auth = C(r["auth_methods"][0] for r in final)
    access = C(r["access"] for r in final)
    verdict = C(r["verdict"] for r in final)
    blocker = C(r["blocker"] for r in final if r["blocker"] != "none")
    mcp = C(r["official_mcp"] for r in final)
    by_cat = {c: {"access": C(r["access"] for r in final if r["category"] == c),
                  "verdict": C(r["verdict"] for r in final if r["category"] == c),
                  "mcp": sum(r["official_mcp"] in ("yes", "beta") for r in final if r["category"] == c)}
              for c in cats}
    no_toolkit = [r for r in final if not r["composio_toolkit"]]
    easy_new = [r for r in no_toolkit if r["verdict"] == "ready"]
    outreach = [r for r in final if r["verdict"] in ("blocked",) or r["access"] in ("partner_gated",)]
    changes = [c | {"id": r["id"], "app": r["app"]} for r in p3.values() for c in r.get("changes", [])]
    vstatus = C(r.get("verifier_status", "n/a") for r in p3.values())

    stats = {"n": len(final), "auth": auth, "primary_auth": primary_auth, "access": access, "verdict": verdict,
             "blocker": blocker, "mcp": mcp, "by_category": by_cat,
             "composio_has_toolkit": sum(bool(r["composio_toolkit"]) for r in final),
             "easy_new": [r["app"] for r in easy_new],
             "no_toolkit_gated": [r["app"] for r in no_toolkit if r["verdict"] != "ready"],
             "outreach": [r["app"] for r in outreach],
             "verifier_status": vstatus, "verifier_changes": len(changes)}

    bundle = {
        "generated": "2026-11-24",
        "records": final,
        "stats": stats,
        "accuracy": json.load(open(D("accuracy.json"))),
        "accuracy_raw_gold": json.load(open(D("accuracy_raw_gold.json"))),
        "gold_sample": json.load(open(D("gold_sample.json"))),
        "adjudication": json.load(open(D("adjudication.json"))),
        "check_pass2": json.load(open(D("check_pass2.json")))["summary"],
        "check_final": (json.load(open(D("check_final.json")))["summary"]
                        if os.path.exists(D("check_final.json")) else None),
        "verifier_changes": changes,
        "human_corrections": json.load(open(D("human_corrections.json"))),
        "pass1": {i: {k: r.get(k) for k in ("access", "verdict", "official_mcp", "auth_methods", "blocker")}
                  for i, r in p1.items()},
    }
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    json.dump(bundle, open(os.path.join(ROOT, "docs/data.json"), "w", encoding="utf-8"), indent=1)
    tpl = open(os.path.join(ROOT, "docs/template.html"), encoding="utf-8").read()
    blob = json.dumps(bundle, ensure_ascii=False).replace("</", "<\\/")
    open(os.path.join(ROOT, "docs/index.html"), "w", encoding="utf-8").write(tpl.replace("__DATA__", blob))

    # plain markdown for agents
    lines = ["# 100-app toolkit research: findings", "",
             f"Access: {dict(access)}", f"Verdict: {dict(verdict)}", f"Auth (any): {dict(auth)}",
             f"Official MCP: {dict(mcp)}", f"Blockers: {dict(blocker)}", "",
             "| # | App | Category | Auth | Access | API | MCP | Verdict | Blocker | Composio toolkit | Evidence |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in final:
        ev = r["evidence"][0]["url"] if r.get("evidence") else ""
        lines.append(f"| {r['id']} | {r['app']} | {r['category']} | {', '.join(r['auth_methods'])} | {r['access']} | "
                     f"{', '.join(r['api_type'])} | {r['official_mcp']} | {r['verdict']} | {r['blocker']} | "
                     f"{r['composio_toolkit'] or '-'} | {ev} |")
    open(os.path.join(ROOT, "docs/findings.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(json.dumps({k: v for k, v in stats.items() if k != "by_category"}, indent=1, default=dict))


if __name__ == "__main__":
    main()
