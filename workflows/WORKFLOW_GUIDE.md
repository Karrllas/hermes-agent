# Workflow Guide

Use a workflow when the job is more than a prompt:

- It has multiple steps such as fetch, prompt, parse, upload.
- It touches external systems or business APIs.
- It needs local state, generated files, or logs.
- It should run from cron or be safely resumed.
- It would be awkward as a single Hermes skill.

Use a skill when the main deliverable is agent behavior or instructions.

## Design Rules

Make workflows restartable. A rerun should skip completed work or safely retry
from the last durable output.

Keep side effects explicit. The README must say when a workflow uploads,
modifies CRM data, sends messages, deletes files, or calls paid APIs.

Keep secrets out of git. Store real credentials in `.env` or the environment.
Commit only `.env.example`.

Keep generated data out of git. Ignore logs, reports, API exports, caches,
temporary files, and raw customer data unless a file is intentionally committed
as a fixture or example.

Prefer dry runs for risky operations. Upload or mutation steps should have a
clear way to test without writing to the external system when practical.

Log enough to recover. Persistent logs should show what was processed, what was
skipped, what failed, and where durable output was written.

## README Checklist

Each workflow README should answer:

- What does it do?
- What systems does it read from?
- What systems does it write to?
- What credentials/settings are required?
- How do I run one item or a capped batch?
- What files are generated?
- What is safe to delete?
- How is it scheduled, if at all?
- How do I recover after a partial failure?

## Suggested Layout

```text
workflows/<name>/
├── README.md
├── .env.example
├── .gitignore
├── prompt.md
├── run.py
└── tests/              # optional
```
