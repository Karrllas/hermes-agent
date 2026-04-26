# zoho-research

Researches Klaipėdos LEZ client companies using hermes and writes AI descriptions back to Zoho CRM.

## What it does

1. Fetches all FEZ Client accounts from Zoho CRM → `accounts.json`
2. For each account missing `AIShortDesc` or `AILongDesc`:
   - Builds a research prompt from `prompt.md` (fills in `{{COMPANY_NAME}}`)
   - Runs hermes — the agent searches the web and produces a structured dossier
   - Parses the JSON output (short timeline, full report, SWOT, process notes)
   - Saves full report to `reports/<Company>.md`
3. Uploads results to Zoho CRM (`AIShortDesc`, `AILongDesc`, `SWOT` fields)

Stops early if a token/rate limit is detected. Safe to re-run — skips companies already processed.

## Run

```bash
cd ~/.hermes/hermes-agent/workflows/zoho-research
python run.py          # all pending
python run.py -n 2     # cap to 2 companies this run
```

## Schedule

Runs nightly via cron on the VPS (srv889958). Current cap: 2 companies/night.

```
7 2 * * * PATH=/home/me/.local/bin:$PATH /home/me/.hermes/hermes-agent/venv/bin/python /home/me/.hermes/hermes-agent/workflows/zoho-research/run.py -n 2 >> /home/me/.hermes/hermes-agent/workflows/zoho-research/cron.log 2>&1
```

## Credentials

Stored in `.env` (not committed). Required:

```
ZOHO_CLIENT_ID=
ZOHO_CLIENT_SECRET=
ZOHO_REFRESH_TOKEN=
```

## Files

| File | Purpose |
|------|---------|
| `run.py` | Main orchestrator — fetch → research loop → upload |
| `fetch.py` | Pulls accounts from Zoho CRM → `accounts.json` |
| `upload.py` | Pushes results to Zoho CRM |
| `prompt.md` | Research prompt template (Lithuanian, structured JSON output) |
| `accounts.json` | Generated — full account list from last fetch |
| `results.json` | Generated — upload payload from last run |
| `reports/` | One `.md` file per researched company |
| `run.log` | Persistent run log |
| `process.log` | Per-company process notes + token costs |

## Zoho field limits

| Field | Limit | Content |
|-------|-------|---------|
| `AIShortDesc` | 2 000 chars | Timeline section only |
| `AILongDesc` | 30 000 chars | Full dossier |
| `SWOT` | — | SWOT section only |

## Status

49 companies pending as of 2025-04. Processing 2/night → ~25 nights to complete.
