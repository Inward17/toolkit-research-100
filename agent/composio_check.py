"""Check which apps already have a Composio toolkit.

composio.dev/toolkits/<slug> returns 200 for a published toolkit and 404 otherwise,
so this needs no API key. We try a few slug spellings per app.
Writes data/composio_catalog.json: {app_id: slug | null}.
"""
import json, re, sys
from concurrent.futures import ThreadPoolExecutor
import requests

ROOT = __file__.rsplit("agent", 1)[0]
apps = json.load(open(ROOT + "data/apps.json"))

# Manual slug hints where the obvious spelling differs (found by checking the catalog).
EXTRA = {
    "WhatsApp Business": ["whatsapp"], "Meta Ads": ["metaads", "facebook"],
    "LinkedIn Ads": ["linkedin"], "Google Ads": ["googleads"], "Lark (Larksuite)": ["lark", "larksuite"],
    "Magento (Adobe Commerce)": ["magento"], "Amazon Selling Partner": ["amazon", "amazon_selling_partner"],
    "Salesforce Commerce Cloud": ["salesforce_commerce_cloud"], "Threads (Meta)": ["threads"],
    "Monday.com": ["monday"], "Zoho CRM": ["zoho", "zoho_crm"], "Zoho Cliq": ["zoho_cliq"],
    "MongoDB Atlas": ["mongodb", "mongodb_atlas"], "Otter AI": ["otter", "otter_ai"],
    "YouTube Transcript": ["youtube", "youtube_transcript"], "Mermaid CLI": ["mermaid"],
    "Help Scout": ["helpscout", "help_scout"], "Bright Data": ["brightdata", "bright_data"],
    "Waterfall.io": ["waterfall"], "systeme.io": ["systeme", "systeme_io"],
    "SE Ranking": ["seranking", "se_ranking"], "GoHighLevel": ["highlevel"], "Paygent Connect": ["paygent"],
}


def candidates(name):
    base = re.sub(r"\(.*?\)", "", name).strip().lower()
    out = EXTRA.get(name, []) + [re.sub(r"[^a-z0-9]", "", base), re.sub(r"[^a-z0-9]+", "_", base).strip("_")]
    return list(dict.fromkeys(out))


def check(app):
    for slug in candidates(app["name"]):
        try:
            r = requests.get(f"https://composio.dev/toolkits/{slug}", timeout=20)
            if r.status_code == 200:
                return app["id"], slug
        except requests.RequestException:
            pass
    return app["id"], None


if __name__ == "__main__":
    with ThreadPoolExecutor(8) as ex:
        res = dict(ex.map(check, apps))
    json.dump({str(k): res[k] for k in sorted(res)}, open(ROOT + "data/composio_catalog.json", "w"), indent=1)
    print(sum(v is not None for v in res.values()), "of", len(res), "have a Composio toolkit", file=sys.stderr)
