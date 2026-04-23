import requests
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

headers = {"Authorization": f"Zoho-oauthtoken {get_token()}"}

r = requests.get("https://www.zohoapis.com/crm/v2/Accounts/search",
    headers=headers,
    params={
        "criteria": "(Account_Type:equals:FEZ Client)",
        "fields": "id,Account_Name,AIShortDesc,AILongDesc"
    }
)

data = r.json()
accounts = data.get("data", [])

import json as _json
with open("accounts.json", "w", encoding="utf-8") as f:
    _json.dump(accounts, f, ensure_ascii=False, indent=2)

print(f"Done — {len(accounts)} accounts written to accounts.json")