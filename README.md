# Toolkit research: 100 apps

Can each of 100 apps become an agent toolkit today? For every app, an agent pipeline researches the auth method, whether a developer can get credentials without a gate, the API surface, whether an official MCP server exists, and a buildability verdict, with a vendor-page citation for each claim. Verification loops then check the results, which are scored against a hand-adjudicated gold sample.

**Case study (one page):** https://inward17.github.io/toolkit-research-100/
**Machine-readable:** [`docs/data.json`](docs/data.json) · [`docs/findings.md`](docs/findings.md)

## Results at a glance

| | Pass 1 (memory only) | Pass 2 (web research) | Final (after verifier) |
|---|---|---|---|
| Field accuracy, 30-app gold sample (180 judgments) | 79.4% | 94.4% | **97.2%** |
| Same, against the gold labels as written before any human ruling | 78.9% | 92.2% | 93.3% |

59 of 100 apps are self-serve and 56 are ready to build today. OAuth 2.0 (71 apps) and static keys or tokens (79 apps) cover nearly every app. The most common blocker is a paid plan. 88 vendors now ship an official MCP server. 76 apps already have a Composio toolkit, and 7 of the 24 that don't are buildable today with no gate.

## Pipeline

```
apps.json ─► Stage 0  composio_check.py      catalog coverage (HTTP 200/404 on composio.dev/toolkits/<slug>)
          ─► Pass 1   prompts/pass1_recall    memory-only draft (baseline)
          ─► Pass 2   prompts/pass2_grounded  web research, one agent per category, URL + quote per field
          ─► Loop 1   check_evidence.py       deterministic: link alive? quote on page? schema valid?
          ─► Loop 2   prompts/pass3_verify    adversarial verifier: fix loop-1 flags, re-search access/verdict/MCP
          ─► Gold     prompts/gold            3 blind agents label 30 sampled apps; a human adjudicates every dispute
          ─► score.py, build_site.py          accuracy per pass; single-page case study
```

The published run used Claude Code subagents, with Firecrawl search and scrape for web access. `agent/research.py` runs the same prompt files end to end on the Claude API: the SDK tool runner calls Firecrawl's REST API.

## Run it

```bash
pip install anthropic requests
export ANTHROPIC_API_KEY=...   # or `ant auth login`
export FIRECRAWL_API_KEY=...

python agent/composio_check.py                                   # no key needed
python agent/research.py pass1 --ids all
python agent/research.py pass2 --ids all                         # --ids 1-10 for a smoke test
python agent/check_evidence.py data/pass2 data/check_pass2.json  # loop 1
python agent/research.py pass3 --ids all                         # loop 2
python agent/score.py                                            # vs data/gold.json and data/gold_raw.json
python agent/build_site.py                                       # -> docs/index.html
```

`research.py` resumes from where it stopped: a batch whose output file already exists is skipped. Set `RESEARCH_MODEL` to change the model, which defaults to `claude-opus-5-5`.

## Where a human was needed

- **Defining the schema** (`prompts/schema.md`). Agents mixed up "free dev sandbox", "free trial" and "paid production access" until each was given a testable definition.
- **Adjudicating disputes** (`data/adjudication.json`). A person read the vendor page and ruled on 11 disputes between a pass and the gold labels. 4 of the rulings corrected the gold labels themselves.
- **Reviewer corrections** (`data/human_corrections.json`). 5 field fixes were applied after scoring, so they do not inflate the accuracy numbers.
- **Process QA.** Some verifiers marked records "confirmed" without re-searching them. Firecrawl credits also ran out mid-run, and the records it left unchecked were re-run with WebSearch and WebFetch.

## Layout

```
agent/     research.py, composio_check.py, check_evidence.py, score.py, build_site.py
prompts/   schema.md, pass1_recall.md, pass2_grounded.md, pass3_verify.md, gold.md
data/      apps.json, pass1/ pass2/ pass3/, gold.json, gold_raw.json, gold_sample.json,
           adjudication.json, human_corrections.json, check_*.json, accuracy*.json, composio_catalog.json
docs/      index.html (case study), template.html, data.json, findings.md
```

## Limits

Accuracy comes from a 30-app sample, so read it as an estimate with roughly ±5 points of sampling error. Pricing and MCP availability change monthly, and this is a snapshot from Nov 24, 2026. No vendor accounts were created, so "self-serve" means the docs say so, not that a key was actually obtained.
