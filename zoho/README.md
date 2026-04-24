# CRM Research Pipeline

Runs AI research on Klaipėdos LEZ client companies and writes results back to Zoho CRM.

## How it works

1. `fetch.py` — pulls all FEZ Client accounts from Zoho → `accounts.json`
2. `run.py` — for each account missing `AIShortDesc` or `AILongDesc`:
   - fills `{{COMPANY_NAME}}` in `prompt.md` and runs hermes
   - parses the JSON block the agent emits at the end
   - saves full report to `reports/<Company>.md`
   - writes `results.json` and calls `upload.py`
3. `upload.py` — pushes `AIShortDesc` (timeline) and `AILongDesc` (full report) to Zoho

## Run

```bash
cd ~/.hermes/hermes-agent/zoho
python run.py
```

## Config

- `MAX_COMPANIES` in `run.py` — limit companies per run (`None` = all pending)
- `.env` — Zoho OAuth credentials (`ZOHO_CLIENT_ID`, `ZOHO_CLIENT_SECRET`, `ZOHO_REFRESH_TOKEN`)

## Files

| File | Purpose |
|------|---------|
| `run.py` | Main orchestrator |
| `fetch.py` | Fetch accounts from Zoho |
| `upload.py` | Push results to Zoho |
| `prompt.md` | Research prompt template |
| `accounts.json` | Generated — account list from last fetch |
| `results.json` | Generated — upload payload from last run |
| `run.log` | Persistent run log |
| `JOBLOG.md` | Agent process notes (overwritten each run) |
| `reports/` | Full report per company |

## Zoho field limits

| Field | Limit |
|-------|-------|
| `AIShortDesc` | 2000 chars (timeline only) |
| `AILongDesc` | 30000 chars (full report) |



----
Cron

Prompt improvments