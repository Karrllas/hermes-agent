import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID     = os.getenv("ZOHO_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")

def get_token():
    r = requests.post("https://accounts.zoho.com/oauth/v2/token", data={
        "grant_type":    "refresh_token",
        "client_id":     CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
    })
    return r.json()["access_token"]

headers = {
    "Authorization": f"Zoho-oauthtoken {get_token()}",
    "Content-Type": "application/json"
}

_results_path = os.path.join(os.path.dirname(__file__), "results.json")
for item in json.load(open(_results_path)):
    r = requests.put(
        f"https://www.zohoapis.com/crm/v2/Accounts/{item['id']}",
        headers=headers,
        json={"data": [{"AIShortDesc": item["AIShortDesc"], "AILongDesc": item["AILongDesc"], "SWOT": item.get("SWOT", "")}]}
    )
    print(f"{item['id']}: {r.status_code} {r.json()}")