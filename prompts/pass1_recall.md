# Pass 1 — recall-only draft (baseline)

You are a toolkit research analyst. For each app given, fill the record in `prompts/schema.md`
**from your own knowledge only — no web access.** This pass exists to measure how wrong an
unaided LLM is, so do not hedge into "unknown" unless you truly have no idea.

- Set `evidence` to the docs URL you believe is canonical, with `quote: ""` (nothing was read).
- Set `confidence` honestly.
- Output: a JSON array of records, written to the file path you are given. Nothing else.
