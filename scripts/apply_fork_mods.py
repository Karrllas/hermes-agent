#!/usr/bin/env python3
"""Check or reapply local Hermes fork modifications.

This script is backup machinery. The primary source of truth is git history on
`my-mods` plus FORK_MODS.md.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

PASS = "PASS"
SKIP = "SKIP"
FAIL = "FAIL"


@dataclass(frozen=True)
class Patch:
    label: str
    path: Path
    old: str
    new: str
    marker: str


@dataclass(frozen=True)
class PresenceCheck:
    label: str
    path: Path


PREVIEW_DISPATCH_OLD = '''\
        elif canonical == "help":
            self.show_help()
        elif canonical == "profile":'''

PREVIEW_DISPATCH_NEW = '''\
        elif canonical == "help":
            self.show_help()
        elif canonical == "preview":
            self._handle_preview_command(cmd_original)
        elif canonical == "profile":'''

PREVIEW_COMMAND_DEF_OLD = '''\
    CommandDef("commands", "Browse all commands and skills (paginated)", "Info",
               gateway_only=True, args_hint="[page]"),
    CommandDef("help", "Show available commands", "Info"),
    CommandDef("restart", "Gracefully restart the gateway after draining active runs", "Session",
               gateway_only=True),'''

PREVIEW_COMMAND_DEF_NEW = '''\
    CommandDef("commands", "Browse all commands and skills (paginated)", "Info",
               gateway_only=True, args_hint="[page]"),
    CommandDef("help", "Show available commands", "Info"),
    CommandDef("preview", "Show the exact provider request payload Hermes would send", "Info",
               cli_only=True, args_hint="[next user message]"),
    CommandDef("restart", "Gracefully restart the gateway after draining active runs", "Session",
               gateway_only=True),'''

PREVIEW_HANDLER_OLD = '''\
    def _handle_background_command(self, cmd: str):'''

PREVIEW_HANDLER_NEW = '''\
    def _handle_preview_command(self, cmd: str):
        """Handle /preview [next user message] - show the exact provider payload."""
        parts = cmd.strip().split(maxsplit=1)
        preview_user_message = parts[1] if len(parts) > 1 else ""

        route = self._resolve_turn_agent_config(preview_user_message or "")
        if not self._init_agent(
            model_override=route["model"],
            runtime_override=route["runtime"],
            request_overrides=route.get("request_overrides"),
        ):
            return

        if not self.agent:
            ChatConsole().print("[bold red]No active agent available for preview[/]")
            return

        try:
            # Reuse the same system-prompt snapshot logic as a normal turn.
            if self.agent._cached_system_prompt is None:
                stored_prompt = None
                if self.conversation_history and self._session_db:
                    try:
                        session_row = self._session_db.get_session(self.session_id)
                        if session_row:
                            stored_prompt = session_row.get("system_prompt") or None
                    except Exception:
                        pass

                if stored_prompt:
                    self.agent._cached_system_prompt = stored_prompt
                else:
                    self.agent._cached_system_prompt = self.agent._build_system_prompt(None)

            messages = list(self.conversation_history or [])
            if preview_user_message:
                messages.append({"role": "user", "content": preview_user_message})

            needs_sanitize = self.agent._should_sanitize_tool_calls()
            api_messages = []
            for msg in messages:
                api_msg = msg.copy()
                for internal_field in ("reasoning", "finish_reason", "_thinking_prefill"):
                    api_msg.pop(internal_field, None)
                if needs_sanitize:
                    self.agent._sanitize_tool_calls_for_strict_api(api_msg)
                api_messages.append(api_msg)

            effective_system = self.agent._cached_system_prompt or ""
            if self.agent.ephemeral_system_prompt:
                effective_system = (effective_system + "\\n\\n" + self.agent.ephemeral_system_prompt).strip()
            if effective_system:
                api_messages = [{"role": "system", "content": effective_system}] + api_messages

            if self.agent.prefill_messages:
                sys_offset = 1 if effective_system else 0
                for idx, pfm in enumerate(self.agent.prefill_messages):
                    api_messages.insert(sys_offset + idx, pfm.copy())

            api_kwargs = self.agent._build_api_kwargs(api_messages)

            preview = {
                "provider": getattr(self.agent, "provider", self.provider),
                "api_mode": getattr(self.agent, "api_mode", self.api_mode),
                "base_url": getattr(self.agent, "base_url", self.base_url),
                "model": getattr(self.agent, "model", self.model),
                "route_label": None,
                "preview_user_message_included": bool(preview_user_message),
                "conversation_history_messages": len(self.conversation_history or []),
                "request": api_kwargs,
            }

            preview_text = json.dumps(preview, indent=2, ensure_ascii=False)
            tmp = Path(tempfile.gettempdir()) / "hermes_preview.json"
            tmp.write_text(preview_text, encoding="utf-8")
            ChatConsole().print(f"[bold {_accent_hex()}]Provider request preview[/]")
            ChatConsole().print(f"[dim]Written to: {tmp}[/]")
            if not preview_user_message:
                ChatConsole().print(
                    "[dim]Tip: use /preview <your next message> to simulate the exact next-turn payload, including that user message.[/]"
                )
        except Exception as e:
            ChatConsole().print(f"[bold red]Preview failed: {e}[/]")

    def _handle_background_command(self, cmd: str):'''


MOD_PATCHES: dict[str, list[Patch]] = {
    "MOD-001": [
        Patch(
            label="cli.py dispatches /preview",
            path=REPO_ROOT / "cli.py",
            old=PREVIEW_DISPATCH_OLD,
            new=PREVIEW_DISPATCH_NEW,
            marker='elif canonical == "preview":',
        ),
        Patch(
            label="commands.py registers /preview",
            path=REPO_ROOT / "hermes_cli" / "commands.py",
            old=PREVIEW_COMMAND_DEF_OLD,
            new=PREVIEW_COMMAND_DEF_NEW,
            marker='CommandDef("preview"',
        ),
        Patch(
            label="cli.py defines _handle_preview_command",
            path=REPO_ROOT / "cli.py",
            old=PREVIEW_HANDLER_OLD,
            new=PREVIEW_HANDLER_NEW,
            marker="def _handle_preview_command",
        ),
    ],
    "MOD-002": [
        Patch(
            label="skill_utils.py supports skills.enabled whitelist mode",
            path=REPO_ROOT / "agent" / "skill_utils.py",
            old='''\
# ── Disabled skills ───────────────────────────────────────────────────────


def get_disabled_skill_names(platform: str | None = None) -> Set[str]:
    """Read disabled skill names from config.yaml.

    Args:
        platform: Explicit platform name (e.g. ``"telegram"``).  When
            *None*, resolves from ``HERMES_PLATFORM`` or
            ``HERMES_SESSION_PLATFORM`` env vars.  Falls back to the
            global disabled list when no platform is determined.

    Reads the config file directly (no CLI config imports) to stay
    lightweight.
    """
    config_path = get_config_path()
    if not config_path.exists():
        return set()
    try:
        parsed = yaml_load(config_path.read_text(encoding="utf-8"))
    except Exception as e:
        logger.debug("Could not read skill config %s: %s", config_path, e)
        return set()
    if not isinstance(parsed, dict):
        return set()

    skills_cfg = parsed.get("skills")
    if not isinstance(skills_cfg, dict):
        return set()

    from gateway.session_context import get_session_env
    resolved_platform = (
        platform
        or os.getenv("HERMES_PLATFORM")
        or get_session_env("HERMES_SESSION_PLATFORM")
    )
    if resolved_platform:
        platform_disabled = (skills_cfg.get("platform_disabled") or {}).get(
            resolved_platform
        )
        if platform_disabled is not None:
            return _normalize_string_set(platform_disabled)
    return _normalize_string_set(skills_cfg.get("disabled"))''',
            new='''\
# ── Disabled skills ───────────────────────────────────────────────────────


class _InvertedSet:
    """A pseudo-set whose __contains__ matches anything NOT in the allowed set.

    Used for whitelist mode: get_disabled_skill_names() returns one of these
    when skills.enabled is configured, so prompt_builder's existing
    ``if name in disabled`` checks work without any modification.
    """

    def __init__(self, allowed: Set[str]):
        self._allowed = allowed

    def __contains__(self, item: object) -> bool:
        return item not in self._allowed


def get_disabled_skill_names(platform: str | None = None) -> Set[str]:
    """Read disabled skill names from config.yaml.

    Args:
        platform: Explicit platform name (e.g. ``"telegram"``).  When
            *None*, resolves from ``HERMES_PLATFORM`` or
            ``HERMES_SESSION_PLATFORM`` env vars.  Falls back to the
            global disabled list when no platform is determined.

    Reads the config file directly (no CLI config imports) to stay
    lightweight.

    When ``skills.enabled`` is set (non-empty list), returns an
    ``_InvertedSet`` so only whitelisted skills appear in the prompt index.
    New upstream skills are excluded automatically until added to the list.
    Falls back to blacklist (``skills.disabled``) when no whitelist is set.
    """
    config_path = get_config_path()
    if not config_path.exists():
        return set()
    try:
        parsed = yaml_load(config_path.read_text(encoding="utf-8"))
    except Exception as e:
        logger.debug("Could not read skill config %s: %s", config_path, e)
        return set()
    if not isinstance(parsed, dict):
        return set()

    skills_cfg = parsed.get("skills")
    if not isinstance(skills_cfg, dict):
        return set()

    from gateway.session_context import get_session_env
    resolved_platform = (
        platform
        or os.getenv("HERMES_PLATFORM")
        or get_session_env("HERMES_SESSION_PLATFORM")
    )

    # Whitelist mode: skills.enabled (or platform_enabled) takes priority
    if resolved_platform:
        platform_enabled = (skills_cfg.get("platform_enabled") or {}).get(resolved_platform)
        if platform_enabled is not None:
            return _InvertedSet(_normalize_string_set(platform_enabled))
    enabled = _normalize_string_set(skills_cfg.get("enabled"))
    if enabled:
        return _InvertedSet(enabled)

    # Blacklist mode (default): skills.disabled
    if resolved_platform:
        platform_disabled = (skills_cfg.get("platform_disabled") or {}).get(resolved_platform)
        if platform_disabled is not None:
            return _normalize_string_set(platform_disabled)
    return _normalize_string_set(skills_cfg.get("disabled"))''',
            marker='skills_cfg.get("enabled")',
        ),
    ],
    "MOD-003": [
        Patch(
            label="web_tools.py accepts web.backend=ddgs",
            path=REPO_ROOT / "tools" / "web_tools.py",
            old='''\
    if configured in ("parallel", "firecrawl", "tavily", "exa"):
        return configured''',
            new='''\
    if configured in ("parallel", "firecrawl", "tavily", "exa", "ddgs"):
        return configured''',
            marker='"exa", "ddgs"',
        ),
        Patch(
            label="web_tools.py falls back to ddgs when no keyed backend is available",
            path=REPO_ROOT / "tools" / "web_tools.py",
            old='''\
    return "firecrawl"  # default (backward compat)''',
            new='''\
    return "ddgs"  # default: free ddgs+jina, no API key needed''',
            marker='return "ddgs"  # default: free ddgs+jina, no API key needed',
        ),
        Patch(
            label="web_tools.py marks ddgs backend available",
            path=REPO_ROOT / "tools" / "web_tools.py",
            old='''\
    if backend == "tavily":
        return _has_env("TAVILY_API_KEY")
    return False''',
            new='''\
    if backend == "tavily":
        return _has_env("TAVILY_API_KEY")
    if backend == "ddgs":
        return True  # always available, no key needed
    return False''',
            marker='if backend == "ddgs":',
        ),
        Patch(
            label="web_tools.py defines ddgs search and Jina extract helpers",
            path=REPO_ROOT / "tools" / "web_tools.py",
            old='''\
# ─── Firecrawl Client ────────────────────────────────────────────────────────''',
            new='''\
# ─── DDGS + Jina Backend (free, no API key) ──────────────────────────────────

def _ddgs_search(query: str, limit: int = 5) -> dict:
    """Search via DuckDuckGo (ddgs lib) — no API key required."""
    try:
        from ddgs import DDGS
    except ImportError:
        return {"success": False, "error": "ddgs not installed — run: uv pip install ddgs"}
    try:
        with DDGS() as d:
            raw = list(d.text(query, max_results=limit))
        results = [
            {"url": r["href"], "title": r["title"], "description": r["body"], "position": i + 1}
            for i, r in enumerate(raw)
        ]
        return {"success": True, "data": {"web": results}}
    except Exception as e:
        return {"success": False, "error": str(e)}


def _jina_extract(urls: list) -> list:
    """Extract clean markdown from URLs via Jina Reader (r.jina.ai) — free."""
    import urllib.request as _ur
    results = []
    for url in urls:
        try:
            req = _ur.Request(
                f"https://r.jina.ai/{url}",
                headers={"Accept": "text/plain", "User-Agent": "Mozilla/5.0"},
            )
            with _ur.urlopen(req, timeout=20) as resp:
                content = resp.read().decode("utf-8")
            results.append({"url": url, "markdown": content, "success": True})
        except Exception as e:
            results.append({"url": url, "markdown": "", "success": False, "error": str(e)})
    return results


# ─── Firecrawl Client ────────────────────────────────────────────────────────''',
            marker="def _ddgs_search",
        ),
        Patch(
            label="web_tools.py dispatches web_search to ddgs",
            path=REPO_ROOT / "tools" / "web_tools.py",
            old='''\
        if backend == "exa":
            response_data = _exa_search(query, limit)
            debug_call_data["results_count"] = len(response_data.get("data", {}).get("web", []))
            result_json = json.dumps(response_data, indent=2, ensure_ascii=False)
            debug_call_data["final_response_size"] = len(result_json)
            _debug.log_call("web_search_tool", debug_call_data)
            _debug.save()
            return result_json''',
            new='''\
        if backend == "ddgs":
            response_data = _ddgs_search(query, limit)
            debug_call_data["results_count"] = len(response_data.get("data", {}).get("web", []))
            result_json = json.dumps(response_data, indent=2, ensure_ascii=False)
            debug_call_data["final_response_size"] = len(result_json)
            _debug.log_call("web_search_tool", debug_call_data)
            _debug.save()
            return result_json

        if backend == "exa":
            response_data = _exa_search(query, limit)
            debug_call_data["results_count"] = len(response_data.get("data", {}).get("web", []))
            result_json = json.dumps(response_data, indent=2, ensure_ascii=False)
            debug_call_data["final_response_size"] = len(result_json)
            _debug.log_call("web_search_tool", debug_call_data)
            _debug.save()
            return result_json''',
            marker='if backend == "ddgs":',
        ),
        Patch(
            label="web_tools.py dispatches web_extract to Jina for ddgs",
            path=REPO_ROOT / "tools" / "web_tools.py",
            old='''\
            if backend == "parallel":
                results = await _parallel_extract(safe_urls)
            elif backend == "exa":''',
            new='''\
            if backend == "parallel":
                results = await _parallel_extract(safe_urls)
            elif backend == "ddgs":
                results = _jina_extract(safe_urls)
            elif backend == "exa":''',
            marker='elif backend == "ddgs":',
        ),
    ],
}

MOD_PRESENCE_CHECKS: dict[str, list[PresenceCheck]] = {
    "MOD-004": [
        PresenceCheck("workflows README exists", REPO_ROOT / "workflows" / "README.md"),
        PresenceCheck("workflow guide exists", REPO_ROOT / "workflows" / "WORKFLOW_GUIDE.md"),
        PresenceCheck("workflow template exists", REPO_ROOT / "workflows" / "_template" / "run.py"),
        PresenceCheck("zoho workflow README exists", REPO_ROOT / "workflows" / "zoho-research" / "README.md"),
        PresenceCheck("zoho workflow runner exists", REPO_ROOT / "workflows" / "zoho-research" / "run.py"),
        PresenceCheck("zoho workflow prompt exists", REPO_ROOT / "workflows" / "zoho-research" / "prompt.md"),
    ],
}


def check_patch(patch: Patch) -> bool:
    text = patch.path.read_text(encoding="utf-8")
    present = patch.marker in text
    status = PASS if present else FAIL
    print(f"{status} {patch.label}")
    return present


def check_presence(check: PresenceCheck) -> bool:
    present = check.path.exists()
    status = PASS if present else FAIL
    print(f"{status} {check.label}")
    return present


def apply_patch(patch: Patch) -> bool:
    text = patch.path.read_text(encoding="utf-8")
    if patch.marker in text:
        print(f"{SKIP} {patch.label}: already present")
        return True
    if patch.old not in text:
        print(f"{FAIL} {patch.label}: anchor not found in {patch.path.relative_to(REPO_ROOT)}")
        return False
    patch.path.write_text(text.replace(patch.old, patch.new, 1), encoding="utf-8")
    print(f"{PASS} {patch.label}: applied")
    return True


def selected_mods(mods: list[str]) -> list[str]:
    known_mods = set(MOD_PATCHES) | set(MOD_PRESENCE_CHECKS)
    if not mods:
        return sorted(known_mods)
    unknown = [mod for mod in mods if mod not in known_mods]
    if unknown:
        known = ", ".join(sorted(known_mods))
        raise SystemExit(f"Unknown mod(s): {', '.join(unknown)}. Known: {known}")
    return mods


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="verify mods are present")
    mode.add_argument("--apply", action="store_true", help="apply missing mechanical patches")
    parser.add_argument("mods", nargs="*", help="optional mod ids, for example MOD-001")
    args = parser.parse_args(argv)

    apply_mode = args.apply
    ok = True
    for mod_id in selected_mods(args.mods):
        print(f"\n{mod_id}")
        for check in MOD_PRESENCE_CHECKS.get(mod_id, []):
            if apply_mode:
                print(f"{SKIP} {check.label}: presence-only check")
                ok = check.path.exists() and ok
            else:
                ok = check_presence(check) and ok
        for patch in MOD_PATCHES.get(mod_id, []):
            ok = (apply_patch(patch) if apply_mode else check_patch(patch)) and ok

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
