"""Score each pass against hand-verified gold labels (data/gold.json).

Gold format per app:
  {"id": 2, "auth_required": ["oauth2"], "auth_allowed": ["oauth2","bearer_token"],
   "access": ["self_serve"], "official_mcp": ["yes","beta"], "verdict": ["ready"],
   "blocker": ["none"], "api_type": ["rest"], "note": "...", "sources": ["https://..."]}
Every non-auth field lists the values a careful reviewer accepts (usually one;
two when the docs genuinely support both readings).
auth_methods is correct when it contains every required method and nothing outside allowed.

Usage: python agent/score.py   -> prints table, writes data/accuracy.json
"""
import json, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIELDS = ["auth_methods", "access", "api_type", "official_mcp", "verdict", "blocker"]


def load_pass(name):
    out = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "data", name, "*.json"))):
        for r in json.load(open(f, encoding="utf-8")):
            out[r["id"]] = r
    return out


def judge(field, rec, g):
    v = rec.get(field)
    if field == "auth_methods":
        s = set(v or [])
        return set(g["auth_required"]) <= s and s <= set(g["auth_allowed"])
    if field == "api_type":   # correct if primary type(s) present and none invented
        s = set(v or [])
        ok_extra = set(g.get("api_type_allowed", g["api_type"])) | {"sdk_only", "cli_only", "websocket"}
        return set(g["api_type"]) <= s and s <= ok_extra
    return v in g[field]


def main(gold_file="data/gold.json", out_file="data/accuracy.json"):
    gold = {g["id"]: g for g in json.load(open(os.path.join(ROOT, gold_file), encoding="utf-8"))}
    report = {}
    for p in ["pass1", "pass2", "pass3"]:
        recs = load_pass(p)
        if not recs:
            continue
        per_field = {f: [0, 0] for f in FIELDS}
        misses = []
        for i, g in gold.items():
            r = recs.get(i)
            for f in FIELDS:
                ok = bool(r) and judge(f, r, g)
                per_field[f][0] += ok
                per_field[f][1] += 1
                if not ok:
                    misses.append({"id": i, "app": g["app"], "field": f,
                                   "got": r.get(f) if r else None,
                                   "gold": g["auth_required"] if f == "auth_methods" else g[f]})
        hit = sum(a for a, _ in per_field.values())
        tot = sum(b for _, b in per_field.values())
        report[p] = {"accuracy": round(hit / tot, 3), "correct": hit, "total": tot,
                     "per_field": {f: round(a / b, 3) for f, (a, b) in per_field.items()},
                     "misses": misses}
        print(f"{p}: {hit}/{tot} = {hit / tot:.1%}  " +
              "  ".join(f"{f}={a}/{b}" for f, (a, b) in per_field.items()))
    json.dump(report, open(os.path.join(ROOT, out_file), "w"), indent=1)


if __name__ == "__main__":
    print("-- vs adjudicated gold --")
    main()
    print("-- vs raw gold (before any human ruling) --")
    main("data/gold_raw.json", "data/accuracy_raw_gold.json")
