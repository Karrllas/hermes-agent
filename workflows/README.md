# Workflows

This directory is a fork-local library of runnable Hermes-powered workflows.

Workflows are different from skills:

- A skill is instruction context loaded into an agent.
- A workflow is an executable process around Hermes. It may call external APIs,
  read/write local state, run on cron, upload data, or produce reports.

Keep workflow code here when it is useful to version alongside this Hermes fork.
Generated data, credentials, logs, customer exports, and reports should stay
ignored unless they are deliberately small examples.

## Current Workflows

| Workflow | Purpose |
| --- | --- |
| `zoho-research` | Research Klaipėdos LEZ client companies and write AI fields back to Zoho CRM. |
| `_template` | Minimal starting point for a new workflow. |

## Required Per-Workflow Files

Each workflow should include:

- `README.md` with purpose, run commands, credentials, side effects, generated
  files, scheduling, and recovery notes.
- `.gitignore` for local credentials, logs, caches, generated data, and reports.
- `.env.example` when credentials or settings are needed.
- `run.py` or equivalent entry point.

See `WORKFLOW_GUIDE.md` for conventions.
