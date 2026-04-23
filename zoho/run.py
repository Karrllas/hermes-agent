#!/usr/bin/env python3
"""
Hermes CRM research pipeline orchestrator.

Flow:
  1. fetch.py  → accounts.md  (all FEZ Client accounts)
  2. For each account missing AIShortDesc or AILongDesc:
       a. Build prompt from prompt.md template + company name
       b. Run hermes → full dossier markdown
       c. Extract timeline section → AIShortDesc
       d. Full dossier         → AILongDesc
       e. Append to results.json
  3. upload.py → push results to Zoho CRM
"""

import json
import logging
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

# Max companies to process per run. Set to None for no limit (production).
MAX_COMPANIES: int | None = 1

# ── Paths ─────────────────────────────────────────────────────────────────────

BASE_DIR      = Path(__file__).parent
REPORTS_DIR   = BASE_DIR / "reports"
LOG_FILE      = BASE_DIR / "run.log"
RESULTS_JSON  = BASE_DIR / "results.json"
ACCOUNTS_JSON = BASE_DIR / "accounts.json"
PROMPT_TPL    = BASE_DIR / "prompt.md"

REPORTS_DIR.mkdir(exist_ok=True)

# ── Logging ───────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)

# ── Helpers ───────────────────────────────────────────────────────────────────


def run_python(script: Path, cwd: Path | None = None) -> int:
    """Run a Python script and return its exit code."""
    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=str(cwd or script.parent),
    )
    return result.returncode


def parse_accounts(json_path: Path) -> list[dict]:
    """Parse accounts.json into a list of account dicts."""
    raw = json.loads(json_path.read_text(encoding="utf-8"))
    accounts = []
    for a in raw:
        accounts.append({
            "id":          str(a.get("id", "")).strip(),
            "name":        str(a.get("Account_Name", "")).strip(),
            "AIShortDesc": str(a.get("AIShortDesc") or "").strip(),
            "AILongDesc":  str(a.get("AILongDesc") or "").strip(),
        })
    return accounts


def build_prompt(company_name: str) -> str:
    """Return prompt text with {{COMPANY_NAME}} substituted."""
    template = PROMPT_TPL.read_text(encoding="utf-8")
    return template.replace("{{COMPANY_NAME}}", company_name)


# Phrases in hermes stderr that indicate a token/rate limit was hit
_LIMIT_SIGNALS = (
    "rate limit",
    "token limit",
    "context length",
    "max_tokens",
    "429",
    "insufficient_quota",
    "context window",
)


def run_hermes(prompt_text: str) -> tuple[str | None, bool]:
    """Run hermes with the given prompt.

    Returns (output, token_limited).
    output is None on error. token_limited=True means stop processing.
    """
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    ) as f:
        f.write(prompt_text)
        tmp_path = f.name

    try:
        result = subprocess.run(
            f"hermes chat -q \"$(cat '{tmp_path}')\" -Q",
            shell=True,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
        )
        stderr_lower = result.stderr.lower()
        token_limited = any(sig in stderr_lower for sig in _LIMIT_SIGNALS)

        if result.returncode != 0:
            log.error("hermes exited %d: %s", result.returncode, result.stderr[:500])
            return None, token_limited
        return result.stdout.strip(), token_limited
    finally:
        os.unlink(tmp_path)


def get_last_session_tokens() -> dict:
    """Query state.db for the most recent session's token usage."""
    db_path = Path.home() / ".hermes" / "state.db"
    if not db_path.exists():
        return {}
    try:
        con = sqlite3.connect(db_path)
        row = con.execute(
            "SELECT input_tokens, output_tokens, cache_read_tokens FROM sessions "
            "ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
        con.close()
        if row:
            return {"input": row[0], "output": row[1], "cache_read": row[2]}
    except Exception:
        pass
    return {}


def parse_agent_output(raw: str) -> dict:
    """Extract structured fields from the agent's trailing JSON block.

    Returns dict with keys: short, long, swot, log.
    Falls back gracefully if JSON is absent or malformed.
    """
    # Agent outputs only raw JSON — strip hermes noise then parse directly
    try:
        cleaned = re.sub(r"\nsession_id:.*$", "", raw, flags=re.MULTILINE).strip()
        data = json.loads(cleaned)
        short = str(data.get("short", "")).strip()
        if len(short) > 2000:
            short = short[:1997] + "..."
        return {
            "short": short,
            "long":  str(data.get("long", "")).strip(),
            "swot":  str(data.get("swot", "")).strip(),
            "log":   str(data.get("log", "")).strip(),
        }
    except Exception:
        pass

    log.warning("Could not parse JSON from agent output — falling back to raw text.")
    fallback = re.sub(r"\nsession_id:.*$", "", raw, flags=re.MULTILINE).rstrip()
    return {"short": "", "long": fallback, "swot": "", "log": ""}


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    log.info("=== Pipeline run started ===")

    # Step 1: Fetch accounts
    log.info("Fetching accounts from Zoho...")
    rc = run_python(BASE_DIR / "fetch.py")
    if rc != 0:
        log.error("fetch.py failed (exit %d), aborting.", rc)
        sys.exit(1)

    # Step 2: Parse
    accounts = parse_accounts(ACCOUNTS_JSON)
    log.info("Total accounts: %d", len(accounts))

    pending = [a for a in accounts if not (a["AIShortDesc"] and a["AILongDesc"])]
    log.info("Pending (missing short or long desc): %d", len(pending))

    if MAX_COMPANIES is not None:
        pending = pending[:MAX_COMPANIES]
        log.info("Capped to %d company(-ies) for this run.", MAX_COMPANIES)

    if not pending:
        log.info("Nothing to process. Exiting.")
        return

    # Step 3: Research each company
    results: list[dict] = []
    for idx, acct in enumerate(pending, 1):
        name = acct["name"]
        acct_id = acct["id"]
        log.info("[%d/%d] Processing: %s (%s)", idx, len(pending), name, acct_id)

        prompt = build_prompt(name)
        report, token_limited = run_hermes(prompt)

        tokens = get_last_session_tokens()
        if tokens:
            log.info("Tokens — input: %s, output: %s, cache_read: %s",
                     f"{tokens['input']:,}", f"{tokens['output']:,}", f"{tokens['cache_read']:,}")

        if token_limited:
            log.warning("Token/rate limit detected — stopping early after %d companies.", len(results))
            break

        if report is None:
            log.warning("Skipping %s — hermes returned no output.", name)
            continue

        parsed = parse_agent_output(report)
        if not parsed["short"]:
            log.warning("No timeline (short) found in output for %s.", name)
        if not parsed["swot"]:
            log.warning("No SWOT found in output for %s.", name)

        # Save full report to file
        safe_name = re.sub(r"[^\w\-]", "_", name)
        report_path = REPORTS_DIR / f"{safe_name}.md"
        report_path.write_text(parsed["long"], encoding="utf-8")
        log.info("Report saved: %s", report_path.name)

        # Append process notes + token costs to process.log
        with open(BASE_DIR / "process.log", "a", encoding="utf-8") as pf:
            token_str = (f"  tokens: input={tokens.get('input',0):,} "
                         f"output={tokens.get('output',0):,} "
                         f"cache_read={tokens.get('cache_read',0):,}") if tokens else ""
            pf.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {name}{token_str}\n")
            if parsed["log"]:
                pf.write(f"{parsed['log']}\n")

        results.append({
            "id":          acct_id,
            "AIShortDesc": parsed["short"],
            "AILongDesc":  parsed["long"],
            "SWOT":        parsed["swot"],
        })

    if not results:
        log.info("No results to upload.")
        return

    # Step 4: Write results.json for upload.py
    RESULTS_JSON.write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    log.info("results.json written with %d entries.", len(results))

    # Step 5: Upload to Zoho
    log.info("Uploading to Zoho CRM...")
    rc = run_python(BASE_DIR / "upload.py")
    if rc != 0:
        log.error("upload.py failed (exit %d). results.json preserved for retry.", rc)
        sys.exit(1)

    log.info("=== Pipeline run complete. Processed %d companies. ===", len(results))


if __name__ == "__main__":
    main()
