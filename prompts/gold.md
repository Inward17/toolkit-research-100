# Gold labeling (independent reference for scoring)

You produce reference labels used to grade other agents. You must NOT open anything under
`data/pass1`, `data/pass2`, `data/pass3` — your labels must be independent.

For each app, read the vendor's own docs (auth page, API reference, pricing / API-access page,
MCP page) with firecrawl_search / firecrawl_scrape, and record per `prompts/schema.md` definitions:

```json
{"id": 2, "app": "HubSpot",
 "auth_required": ["oauth2"],               // methods a builder MUST list (the primary ones)
 "auth_allowed":  ["oauth2", "bearer_token"],// every method the docs actually support
 "access":       ["self_serve"],             // accepted value(s); 2 only if docs truly support both readings
 "api_type":     ["rest"],
 "official_mcp": ["yes"],
 "verdict":      ["ready"],
 "blocker":      ["none"],
 "note": "one line on the deciding fact",
 "sources": ["https://exact-vendor-page", "..."]}
```

Rules: vendor pages beat blogs. Be precise about gates (free dev account vs paid plan vs app review
vs partner). "official_mcp" = an MCP server published by the vendor itself (remote or repo under vendor org);
"beta" if labeled beta/preview. Private-app tokens / personal access tokens count as `bearer_token`
unless docs call them API keys. Write the JSON array to the given path and verify it parses.
