# 100-app toolkit research: findings

Access: {'self_serve': 59, 'free_trial': 13, 'partner_gated': 6, 'paid_plan': 9, 'approval': 11, 'not_applicable': 2}
Verdict: {'ready_with_gate': 38, 'ready': 56, 'blocked': 4, 'not_a_fit': 2}
Auth (any): {'oauth2': 71, 'bearer_token': 36, 'api_key': 44, 'basic': 14, 'other': 4, 'jwt': 4, 'none': 2, 'hmac_signature': 1}
Official MCP: {'yes': 77, 'beta': 11, 'no': 12}
Blockers: {'paid_plan': 22, 'enterprise_only': 5, 'partner_approval': 4, 'app_review': 8, 'local_tool_only': 2, 'other': 3}

| # | App | Category | Auth | Access | API | MCP | Verdict | Blocker | Composio toolkit | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Salesforce | CRM and Sales | oauth2 | self_serve | rest, soap, graphql | yes | ready_with_gate | paid_plan | salesforce | https://developer.salesforce.com/docs/platform/api-rest/guide/intro-oauth-and-connected-apps.html |
| 2 | HubSpot | CRM and Sales | oauth2, bearer_token | self_serve | rest | yes | ready | none | hubspot | https://developers.hubspot.com/docs/apps/legacy-apps/authentication/intro-to-auth |
| 3 | Pipedrive | CRM and Sales | oauth2, api_key | self_serve | rest | yes | ready | none | pipedrive | https://pipedrive.readme.io/docs/core-api-concepts-authentication |
| 4 | Attio | CRM and Sales | oauth2, api_key | self_serve | rest | yes | ready | none | attio | https://docs.attio.com/rest-api/guides/authentication |
| 5 | Twenty | CRM and Sales | api_key, oauth2 | self_serve | rest, graphql | yes | ready | none | twenty | https://docs.twenty.com/developers/extend/api |
| 6 | Podio | CRM and Sales | oauth2 | self_serve | rest | beta | ready | none | podio | https://developers.podio.com/authentication |
| 7 | Zoho CRM | CRM and Sales | oauth2 | self_serve | rest | yes | ready | none | zoho | https://www.zoho.com/crm/developer/docs/api/v8/oauth-overview.html |
| 8 | Close | CRM and Sales | api_key, basic, oauth2 | free_trial | rest | yes | ready_with_gate | paid_plan | close | https://developer.close.com/api/overview |
| 9 | Copper | CRM and Sales | api_key, oauth2 | free_trial | rest | beta | ready_with_gate | paid_plan | copper | https://developer.copper.com/introduction/authentication.html |
| 10 | DealCloud | CRM and Sales | oauth2 | partner_gated | rest | yes | blocked | enterprise_only | - | https://api.docs.dealcloud.com/docs/token |
| 11 | Zendesk | Support and Helpdesk | oauth2, api_key, basic | free_trial | rest | beta | ready_with_gate | paid_plan | zendesk | https://developer.zendesk.com/api-reference/introduction/security-and-auth/ |
| 12 | Intercom | Support and Helpdesk | bearer_token, oauth2 | self_serve | rest | yes | ready | none | intercom | https://developers.intercom.com/docs/build-an-integration/learn-more/authentication |
| 13 | Freshdesk | Support and Helpdesk | api_key, basic | free_trial | rest | yes | ready_with_gate | paid_plan | freshdesk | https://developers.freshdesk.com/api/ |
| 14 | Front | Support and Helpdesk | bearer_token, oauth2 | self_serve | rest | yes | ready | none | front | https://dev.frontapp.com/docs/authentication |
| 15 | Pylon | Support and Helpdesk | bearer_token, oauth2 | paid_plan | rest | yes | ready_with_gate | paid_plan | - | https://docs.usepylon.com/pylon-docs/developer/api/authentication |
| 16 | LiveAgent | Support and Helpdesk | api_key, oauth2 | free_trial | rest | yes | ready_with_gate | paid_plan | - | https://support.liveagent.com/802463-REST-API |
| 17 | Plain | Support and Helpdesk | api_key | free_trial | graphql | yes | ready_with_gate | paid_plan | plain | https://www.plain.com/docs/graphql/authentication |
| 18 | Help Scout | Support and Helpdesk | oauth2 | free_trial | rest | yes | ready_with_gate | paid_plan | help_scout | https://developer.helpscout.com/mailbox-api/overview/authentication |
| 19 | Gorgias | Support and Helpdesk | basic, oauth2 | free_trial | rest | beta | ready_with_gate | paid_plan | gorgias | https://docs.gorgias.com/en-US/rest-api-208286 |
| 20 | Gladly | Support and Helpdesk | basic | partner_gated | rest | no | blocked | partner_approval | - | https://developer.gladly.com/rest/ |
| 21 | Slack | Communications and Messaging | oauth2 | self_serve | rest, websocket | yes | ready | none | slack | https://docs.slack.dev/authentication |
| 22 | Twilio | Communications and Messaging | basic, api_key | self_serve | rest | yes | ready | none | twilio | https://www.twilio.com/docs/iam/api-keys |
| 23 | Zoho Cliq | Communications and Messaging | oauth2 | self_serve | rest | yes | ready | none | zoho_cliq | https://www.zoho.com/cliq/help/restapi/v3/introduction/ |
| 24 | Lark (Larksuite) | Communications and Messaging | oauth2, bearer_token, other | self_serve | rest, websocket | beta | ready | none | lark | https://github.com/larksuite/lark-openapi-mcp |
| 25 | Pumble | Communications and Messaging | api_key, other | self_serve | rest | yes | ready | none | pumble | https://pumble.com/help/integrations/automation-workflow-integrations/api-keys-integration/ |
| 26 | Discord | Communications and Messaging | oauth2, bearer_token | self_serve | rest, websocket | no | ready | none | discord | https://docs.discord.com/developers/platform/oauth2-and-permissions |
| 27 | Telegram | Communications and Messaging | api_key | self_serve | rest | no | ready | none | telegram | https://core.telegram.org/bots/api |
| 28 | WhatsApp Business | Communications and Messaging | oauth2, bearer_token | approval | rest | beta | ready_with_gate | app_review | whatsapp | https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started |
| 29 | Aircall | Communications and Messaging | basic, oauth2 | free_trial | rest | beta | ready_with_gate | paid_plan | aircall | https://developers.aircall.io/api-references |
| 30 | Vonage | Communications and Messaging | basic, jwt | self_serve | rest, websocket | yes | ready | none | - | https://developer.vonage.com/en/getting-started/concepts/authentication |
| 31 | Google Ads | Marketing, Ads, Email and Social | oauth2, other | approval | grpc, rest | yes | ready_with_gate | app_review | googleads | https://developers.google.com/google-ads/api/docs/api-policy/developer-token |
| 32 | Meta Ads | Marketing, Ads, Email and Social | oauth2 | approval | rest | yes | ready_with_gate | app_review | metaads | https://developers.facebook.com/docs/marketing-api/overview/authorization |
| 33 | LinkedIn Ads | Marketing, Ads, Email and Social | oauth2 | approval | rest | no | ready_with_gate | partner_approval | linkedin | https://learn.microsoft.com/en-us/linkedin/marketing/getting-started |
| 34 | GoHighLevel | Marketing, Ads, Email and Social | oauth2, bearer_token | self_serve | rest | yes | ready | none | highlevel | https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api-documentation |
| 35 | Mailchimp | Marketing, Ads, Email and Social | oauth2, api_key, basic, bearer_token | self_serve | rest | yes | ready | none | mailchimp | https://mailchimp.com/developer/marketing/api-concepts/authentication |
| 36 | Klaviyo | Marketing, Ads, Email and Social | api_key, oauth2 | self_serve | rest | yes | ready | none | klaviyo | https://developers.klaviyo.com/en/docs/authenticate_ |
| 37 | systeme.io | Marketing, Ads, Email and Social | api_key | self_serve | rest | yes | ready | none | - | https://help.systeme.io/article/2323-how-to-create-a-public-api-key-on-systeme-io |
| 38 | Pinterest | Marketing, Ads, Email and Social | oauth2 | approval | rest | beta | ready_with_gate | app_review | pinterest | https://developers.pinterest.com/docs/key-concepts/access-tiers/ |
| 39 | Threads (Meta) | Marketing, Ads, Email and Social | oauth2 | approval | rest | no | ready_with_gate | app_review | threads | https://developers.facebook.com/documentation/threads/get-started |
| 40 | SendGrid | Marketing, Ads, Email and Social | api_key | free_trial | rest | no | ready_with_gate | paid_plan | sendgrid | https://www.twilio.com/docs/sendgrid/for-developers/sending-email/authentication |
| 41 | Shopify | Ecommerce | oauth2, bearer_token | self_serve | graphql, rest | yes | ready | none | shopify | https://shopify.dev/docs/apps/build/authentication-authorization |
| 42 | WooCommerce | Ecommerce | basic, api_key | self_serve | rest | beta | ready | none | - | https://developer.woocommerce.com/docs/apis/rest-api/ |
| 43 | BigCommerce | Ecommerce | oauth2, bearer_token | free_trial | rest, graphql | yes | ready_with_gate | paid_plan | bigcommerce | https://docs.bigcommerce.com/developer/docs/overview/api-fundamentals/api-accounts |
| 44 | Salesforce Commerce Cloud | Ecommerce | oauth2, jwt | partner_gated | rest | beta | ready_with_gate | enterprise_only | - | https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization.html |
| 45 | Magento (Adobe Commerce) | Ecommerce | oauth2, bearer_token | self_serve | rest, graphql, soap | beta | ready | none | - | https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-oauth |
| 46 | Squarespace | Ecommerce | api_key, oauth2 | paid_plan | rest | yes | ready_with_gate | paid_plan | - | https://developers.squarespace.com/commerce-apis/authentication-and-permissions |
| 47 | Ecwid | Ecommerce | oauth2, bearer_token | paid_plan | rest | no | ready_with_gate | paid_plan | - | https://docs.ecwid.com/get-started/make-your-first-api-request |
| 48 | Gumroad | Ecommerce | oauth2, bearer_token | self_serve | rest | yes | ready | none | gumroad | https://gumroad.com/help/article/280-create-application-api |
| 49 | Amazon Selling Partner | Ecommerce | oauth2 | approval | rest | yes | ready_with_gate | app_review | amazon | https://developer-docs.amazon.com/sp-api/docs/connecting-to-the-selling-partner-api |
| 50 | fanbasis | Ecommerce | api_key | self_serve | rest | yes | ready | none | - | https://commasdocs.com/ |
| 51 | DataForSEO | Data, SEO and Scraping | basic | self_serve | rest | yes | ready | none | dataforseo | https://docs.dataforseo.com/v3/auth/ |
| 52 | SE Ranking | Data, SEO and Scraping | api_key | free_trial | rest | yes | ready_with_gate | paid_plan | - | https://seranking.com/api/data/getting-started/ |
| 53 | Ahrefs | Data, SEO and Scraping | api_key, oauth2 | paid_plan | rest | yes | ready_with_gate | paid_plan | ahrefs | https://docs.ahrefs.com/en/api/docs/introduction |
| 54 | MrScraper | Data, SEO and Scraping | api_key | self_serve | rest | yes | ready | none | mrscraper | https://docs.mrscraper.com/docs/api/overview |
| 55 | Apify | Data, SEO and Scraping | bearer_token, api_key | self_serve | rest, sdk_only | yes | ready | none | apify | https://docs.apify.com/api/v2 |
| 56 | Firecrawl | Data, SEO and Scraping | bearer_token, oauth2 | self_serve | rest, sdk_only | yes | ready | none | firecrawl | https://www.firecrawl.dev/pricing |
| 57 | Bright Data | Data, SEO and Scraping | bearer_token | self_serve | rest, sdk_only, cli_only | yes | ready | none | brightdata | https://docs.brightdata.com/api-reference/account-management-api/Get_total_balance_through_API |
| 58 | Sherlock | Data, SEO and Scraping | none | not_applicable | cli_only | no | not_a_fit | local_tool_only | - | https://github.com/sherlock-project/sherlock |
| 59 | Waterfall.io | Data, SEO and Scraping | api_key | partner_gated | rest | no | ready_with_gate | partner_approval | - | https://docs.waterfall.io/v1/introduction |
| 60 | Clay | Data, SEO and Scraping | api_key, oauth2 | self_serve | rest | yes | ready | none | clay | https://www.scalekit.com/blog/clay-mcp-vs-api |
| 61 | GitHub | Developer, Infra and Data platforms | oauth2, bearer_token, jwt, basic | self_serve | rest, graphql | yes | ready | none | github | https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api |
| 62 | Vercel | Developer, Infra and Data platforms | bearer_token, oauth2 | self_serve | rest | yes | ready | none | vercel | https://vercel.com/docs/rest-api |
| 63 | Netlify | Developer, Infra and Data platforms | oauth2, bearer_token | self_serve | rest | yes | ready | none | - | https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/ |
| 64 | Cloudflare | Developer, Infra and Data platforms | bearer_token, api_key, oauth2 | self_serve | rest | yes | ready | none | cloudflare | https://developers.cloudflare.com/fundamentals/api/get-started/create-token/ |
| 65 | Supabase | Developer, Infra and Data platforms | bearer_token, oauth2, api_key | self_serve | rest | yes | ready | none | supabase | https://supabase.com/docs/reference/api/introduction |
| 66 | Neo4j | Developer, Infra and Data platforms | oauth2, basic | self_serve | rest | yes | ready | none | neo4j | https://neo4j.com/docs/aura/api/authentication/ |
| 67 | Snowflake | Developer, Infra and Data platforms | oauth2, jwt, bearer_token | free_trial | rest | yes | ready_with_gate | paid_plan | snowflake | https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/authentication |
| 68 | MongoDB Atlas | Developer, Infra and Data platforms | oauth2, other | self_serve | rest | yes | ready | none | mongodb | https://www.mongodb.com/docs/atlas/api/api-authentication/ |
| 69 | Datadog | Developer, Infra and Data platforms | api_key | self_serve | rest | yes | ready | none | datadog | https://docs.datadoghq.com/account_management/api-app-keys/ |
| 70 | Sentry | Developer, Infra and Data platforms | bearer_token, oauth2 | self_serve | rest | yes | ready | none | sentry | https://docs.sentry.io/api/auth/ |
| 71 | Notion | Productivity and Project Management | bearer_token, oauth2 | self_serve | rest | yes | ready | none | notion | https://developers.notion.com/guides/connections-and-tokens/overview |
| 72 | Airtable | Productivity and Project Management | bearer_token, oauth2 | self_serve | rest | yes | ready | none | airtable | https://support.airtable.com/articles/6292134965-getting-started-with-airtable-s-web-api |
| 73 | Linear | Productivity and Project Management | api_key, oauth2 | self_serve | graphql | yes | ready | none | linear | https://linear.app/developers |
| 74 | Jira | Productivity and Project Management | basic, oauth2 | self_serve | rest | yes | ready | none | jira | https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/ |
| 75 | Asana | Productivity and Project Management | bearer_token, oauth2 | self_serve | rest | yes | ready | none | asana | https://developers.asana.com/docs/authentication |
| 76 | Monday.com | Productivity and Project Management | api_key, oauth2 | self_serve | graphql | yes | ready | none | monday | https://developer.monday.com/api-reference/docs/authentication |
| 77 | ClickUp | Productivity and Project Management | api_key, oauth2 | self_serve | rest | yes | ready | none | clickup | https://developer.clickup.com/docs/authentication |
| 78 | Coda | Productivity and Project Management | bearer_token | self_serve | rest | yes | ready | none | coda | https://help.superhuman.com/hc/en-us/articles/46210310809613-Generate-API-tokens-for-Docs |
| 79 | Smartsheet | Productivity and Project Management | bearer_token, oauth2 | paid_plan | rest | yes | ready_with_gate | paid_plan | smartsheet | https://developers.smartsheet.com/register |
| 80 | Harvest | Productivity and Project Management | bearer_token, oauth2 | self_serve | rest | yes | ready | none | harvest | https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/ |
| 81 | Stripe | Finance and Fintech | api_key, oauth2 | self_serve | rest | yes | ready | none | stripe | https://docs.stripe.com/keys |
| 82 | Plaid | Finance and Fintech | api_key, oauth2 | approval | rest | yes | ready_with_gate | app_review | plaid | https://plaid.com/docs/quickstart/ |
| 83 | Binance | Finance and Fintech | api_key, hmac_signature | self_serve | rest, websocket | yes | ready_with_gate | other | - | https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md |
| 84 | Paygent Connect | Finance and Fintech | api_key | partner_gated | rest | no | blocked | partner_approval | - | https://www.gopaygent.com/ |
| 85 | iPayX | Finance and Fintech | bearer_token, api_key | paid_plan | rest | yes | ready_with_gate | paid_plan | - | https://www.ipayx.ai/developers |
| 86 | QuickBooks | Finance and Fintech | oauth2 | approval | rest | yes | ready_with_gate | app_review | quickbooks | https://developer.intuit.com/llms.txt |
| 87 | Xero | Finance and Fintech | oauth2 | self_serve | rest | yes | ready_with_gate | paid_plan | xero | https://raw.githubusercontent.com/XeroAPI/xero-mcp-server/main/README.md |
| 88 | Brex | Finance and Fintech | bearer_token, oauth2 | approval | rest | yes | ready_with_gate | other | brex | https://developer.brex.com/docs/authentication |
| 89 | Ramp | Finance and Fintech | oauth2 | approval | rest | yes | ready_with_gate | other | ramp | https://docs.ramp.com/llms-full.txt |
| 90 | PitchBook | Finance and Fintech | api_key | partner_gated | rest | yes | blocked | enterprise_only | pitchbook | https://investordatarooms.com/pitchbook-api/ |
| 91 | NotebookLM | AI, Research and Media-native | oauth2 | paid_plan | rest | no | ready_with_gate | enterprise_only | - | https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks |
| 92 | Otter AI | AI, Research and Media-native | oauth2, api_key | paid_plan | rest | yes | ready_with_gate | enterprise_only | - | https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server |
| 93 | Fathom | AI, Research and Media-native | api_key, oauth2 | self_serve | rest | yes | ready | none | fathom | https://developers.fathom.ai/quickstart |
| 94 | Consensus | AI, Research and Media-native | api_key, oauth2 | self_serve | rest | yes | ready | none | consensus | https://docs.consensus.app/api-get-started |
| 95 | Reducto | AI, Research and Media-native | api_key, bearer_token | self_serve | rest, sdk_only | yes | ready | none | - | https://docs.reducto.ai/quickstart |
| 96 | Devin | AI, Research and Media-native | bearer_token, api_key | paid_plan | rest | yes | ready_with_gate | paid_plan | - | https://docs.devin.ai/api-reference/authentication |
| 97 | higgsfield | AI, Research and Media-native | api_key | self_serve | rest, sdk_only, cli_only | yes | ready | none | higgsfield | https://docs.higgsfield.ai/ |
| 98 | Mermaid CLI | AI, Research and Media-native | none | not_applicable | cli_only | no | not_a_fit | local_tool_only | - | https://github.com/mermaid-js/mermaid-cli |
| 99 | YouTube Transcript | AI, Research and Media-native | bearer_token, api_key | self_serve | rest | yes | ready | none | youtube | https://transcriptapi.com/ |
| 100 | Grain | AI, Research and Media-native | bearer_token, oauth2 | self_serve | rest | yes | ready | none | grain | https://developers.grain.com/authentication.html |
