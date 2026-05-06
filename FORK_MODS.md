# Fork Mods

This fork follows upstream Hermes and keeps a small set of intentional local
changes on `my-mods`. The normal update path is still git-first:

```bash
git checkout main
hermes update
git checkout my-mods
git rebase main
```

The mod list below is the human source of truth. The helper script at
`scripts/apply_fork_mods.py` is a backup and verification tool for known
mechanical changes:

```bash
python scripts/apply_fork_mods.py --check
python scripts/apply_fork_mods.py --apply MOD-001
```

## MOD-001: Provider Payload Preview Command

Status: active

Files:
- `cli.py`
- `hermes_cli/commands.py`

Why:
Hermes can route, enrich, sanitize, prefill, and tool-wrap a message before it
hits the provider. When debugging model behavior, prompt bloat, routing, or
tool schemas, we need to inspect the exact request payload without making an
LLM call.

Behavior:
- Adds a CLI-only `/preview [next user message]` slash command.
- Builds the same agent route and request kwargs that a normal turn would use.
- Includes the current session history and, when supplied, the simulated next
  user message.
- Writes the full preview JSON to `/tmp/hermes_preview.json`.

Rebase handling:
This should normally be preserved by `git rebase main`. If conflicts or an
upstream overwrite remove it, run:

```bash
python scripts/apply_fork_mods.py --check MOD-001
python scripts/apply_fork_mods.py --apply MOD-001
```

Verification:
- `/help` shows `/preview`.
- `/preview test message` writes `/tmp/hermes_preview.json`.
- The JSON contains top-level provider metadata and a `request` object.

## MOD-002: Skills Whitelist Mode

Status: active

Files:
- `agent/skill_utils.py`
- `tests/hermes_cli/test_skills_config.py`

Why:
Upstream Hermes defaults to showing every compatible bundled skill unless it is
explicitly disabled. This fork follows upstream frequently, so new upstream
skills should not automatically enter the system prompt. We want an allowlist
mode where only explicitly approved skills are visible.

Behavior:
- `skills.enabled` in `config.yaml` acts as a global skill allowlist.
- `skills.platform_enabled.<platform>` acts as a platform-specific allowlist.
- Platform allowlists take priority over the global allowlist.
- If no allowlist is configured, Hermes falls back to upstream blacklist
  behavior via `skills.disabled` and `skills.platform_disabled`.

Example:

```yaml
skills:
  enabled:
    - plan
    - github
  platform_enabled:
    telegram:
      - plan
```

Rebase handling:
This should normally be preserved by `git rebase main`. If conflicts or an
upstream overwrite remove it, run:

```bash
python scripts/apply_fork_mods.py --check MOD-002
python scripts/apply_fork_mods.py --apply MOD-002
```

Verification:
- `python scripts/apply_fork_mods.py --check MOD-002`
- `pytest tests/hermes_cli/test_skills_config.py -k whitelist`

## MOD-003: No-Key Web Fallback via DDGS and Jina

Status: active

Files:
- `tools/web_tools.py`

Why:
Upstream web search/extract requires Firecrawl, Parallel, Tavily, Exa, or a
managed Firecrawl gateway. This fork needs web tools to remain usable when no
API-key-backed web provider is configured.

Behavior:
- Keeps upstream provider priority when keys/config are available:
  Firecrawl/gateway, Parallel, Tavily, then Exa.
- Adds `ddgs` as an explicit `web.backend` value.
- Falls back to `ddgs` only when no keyed/configured upstream backend is
  available.
- Uses the `ddgs` package for search.
- Uses Jina Reader (`https://r.jina.ai/...`) for URL extraction.

Notes:
DDGS and Jina are no-key public services, not guaranteed infrastructure. They
can rate-limit, block, or change behavior. This is a practical free fallback,
not an SLA-backed provider.

Rebase handling:
This should normally be preserved by `git rebase main`. If conflicts or an
upstream overwrite remove it, run:

```bash
python scripts/apply_fork_mods.py --check MOD-003
python scripts/apply_fork_mods.py --apply MOD-003
```

Verification:
- `python scripts/apply_fork_mods.py --check MOD-003`
- With no web API keys configured, `web_search` should choose `ddgs`.
- With `FIRECRAWL_API_KEY`, `FIRECRAWL_API_URL`, or the managed gateway
  available, Firecrawl should still win.

## MOD-004: Fork Workflow Library

Status: active

Files:
- `workflows/`

Why:
Some local automation is larger than a skill. It has scripts, prompts,
credentials, generated state, logs, cron, and external side effects. Keeping
these workflows in the fork makes them reusable and versioned alongside the
Hermes customizations they depend on.

Behavior:
- `workflows/` is a fork-local workflow library.
- Each workflow is a runnable project, not a core Hermes patch.
- Workflow credentials, logs, generated data, reports, and caches stay ignored.
- `workflows/README.md` lists available workflows.
- `workflows/WORKFLOW_GUIDE.md` defines conventions.
- `workflows/_template/` provides a minimal starting point.

Current workflows:
- `zoho-research`: researches Klaipėdos LEZ client companies and writes AI
  fields back to Zoho CRM.

Rebase handling:
Workflow directories should be preserved by `git rebase main`. The helper only
checks that required files exist; it does not reconstruct workflow contents.

Verification:
- `python scripts/apply_fork_mods.py --check MOD-004`
