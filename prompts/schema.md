# Research record schema (one JSON object per app)

```json
{
  "id": 1,
  "app": "Salesforce",
  "category": "CRM and Sales",
  "one_liner": "What it does, <= 15 words",
  "auth_methods": ["oauth2"],          // any of: oauth2, api_key, basic, bearer_token, jwt, hmac_signature, session/login, none, other
  "auth_note": "e.g. OAuth2 for public apps; private app token for single store",
  "access": "self_serve",              // self_serve | free_trial | paid_plan | approval | partner_gated | not_applicable
  "access_note": "What exactly a dev must do / pay / request to get working credentials",
  "api_type": ["rest"],                // any of: rest, graphql, soap, grpc, websocket, sdk_only, cli_only, none
  "api_breadth": "broad",              // broad (most product objects, CRUD) | moderate | narrow (a few endpoints) | none
  "api_note": "Main resource families, approx endpoint count if documented",
  "official_mcp": "yes",               // yes | no | beta
  "mcp_note": "URL / name of official MCP server, or notable community one",
  "verdict": "ready",                  // ready | ready_with_gate | blocked | not_a_fit
  "blocker": "none",                   // none | paid_plan | partner_approval | app_review | enterprise_only | no_public_api | tos_restriction | local_tool_only | other
  "blocker_note": "One line, only if verdict != ready",
  "evidence": [ {"field": "auth_methods", "url": "https://...", "quote": "short supporting passage from the page"} ],
  "confidence": "high"                 // high | medium | low
}
```

Definitions (apply consistently):
- **self_serve**: a developer can sign up for free (free tier, free dev account, sandbox, or a dev store) and get working API credentials with no human approval.
- **free_trial**: credentials only via a time-limited trial; API keeps working only on a paid plan after.
- **paid_plan**: API access needs a paid subscription / specific paid tier (no free tier, no usable trial).
- **approval**: self-signup works for dev/test but production or broad scopes need an app review / verification (e.g. Meta App Review, Google Ads developer token approval).
- **partner_gated**: API is only for partners/customers via contact-sales, partner program, or enterprise contract.
- **ready**: an agent toolkit can be built today with self-serve creds.
- **ready_with_gate**: buildable, but a paid plan / app review / approval stands in the way of the end user or of us.
- **blocked**: no public API, or creds unobtainable without a partnership.
- **not_a_fit**: not a SaaS API (e.g. local CLI / OSS script) — would need a hosted wrapper instead of a toolkit.
