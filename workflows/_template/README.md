# workflow-template

Short description of what this workflow does.

## What It Does

1. Fetches or prepares input.
2. Runs Hermes or another processing step.
3. Writes durable output.
4. Optionally uploads or applies results.

## Run

```bash
cd ~/.hermes/hermes-agent/workflows/_template
python run.py
```

## Credentials

Copy `.env.example` to `.env` and fill in real values.

## Side Effects

Document any external writes here. If there are no external writes, say so.

## Generated Files

| File | Purpose |
| --- | --- |
| `outputs/` | Generated workflow output. |
| `run.log` | Persistent run log. |
