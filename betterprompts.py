#!/usr/bin/env python3
"""
betterprompts.py — re-apply prompt patches after hermes update.

Run this after `hermes update` to restore all prompt customizations.
Each patch is idempotent: safe to run multiple times.
"""
import os
import sys
from pathlib import Path

HERMES_AGENT = Path(__file__).parent
HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))

PASS = "\033[32m✓\033[0m"
SKIP = "\033[33m~\033[0m"
FAIL = "\033[31m✗\033[0m"


def patch(label: str, path: Path, old: str, new: str, dry_run: bool = False) -> bool:
    """Replace old with new in path. Returns True if changed, False if already applied."""
    text = path.read_text(encoding="utf-8")
    if new in text:
        print(f"  {SKIP} {label} — already applied")
        return False
    if old not in text:
        print(f"  {FAIL} {label} — PATTERN NOT FOUND (upstream changed?)")
        print(f"      file: {path}")
        return False
    if dry_run:
        print(f"  {PASS} {label} — would apply")
    else:
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        print(f"  {PASS} {label} — applied")
    return True


# ── Patch 1: skill_utils.py — whitelist mode via _InvertedSet ────────────────

SKILL_UTILS = HERMES_AGENT / "agent" / "skill_utils.py"

SKILL_UTILS_OLD = '''\
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
    return _normalize_string_set(skills_cfg.get("disabled"))'''

SKILL_UTILS_NEW = '''\
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
    return _normalize_string_set(skills_cfg.get("disabled"))'''


# ── Patch 2: prompt_builder.py — slim down skills section preamble ───────────

PROMPT_BUILDER = HERMES_AGENT / "agent" / "prompt_builder.py"

PROMPT_BUILDER_OLD = '''\
        result = (
            "## Skills (mandatory)\\n"
            "Before replying, scan the skills below. If a skill matches or is even partially relevant "
            "to your task, you MUST load it with skill_view(name) and follow its instructions. "
            "Err on the side of loading — it is always better to have context you don't need "
            "than to miss critical steps, pitfalls, or established workflows. "
            "Skills contain specialized knowledge — API endpoints, tool-specific commands, "
            "and proven workflows that outperform general-purpose approaches. Load the skill "
            "even if you think you could handle the task with basic tools like web_search or terminal. "
            "Skills also encode the user's preferred approach, conventions, and quality standards "
            "for tasks like code review, planning, and testing — load them even for tasks you "
            "already know how to do, because the skill defines how it should be done here.\\n"
            "If a skill has issues, fix it with skill_manage(action='patch').\\n"
            "After difficult/iterative tasks, offer to save as a skill. "
            "If a skill you loaded was missing steps, had wrong commands, or needed "
            "pitfalls you discovered, update it before finishing.\\n"
            "\\n"
            "<available_skills>\\n"
            + "\\n".join(index_lines) + "\\n"
            "</available_skills>\\n"
            "\\n"
            "Only proceed without loading a skill if genuinely none are relevant to the task."
        )'''

PROMPT_BUILDER_NEW = '''\
        result = (
            "## Skills — load with skill_view(name) if relevant.\\n"
            "\\n"
            "<available_skills>\\n"
            + "\\n".join(index_lines) + "\\n"
            "</available_skills>"
        )'''


# ── Patch 3: prompt_builder.py — strip /preview command from help ─────────────
# (cli.py and commands.py changes are committed on my-mods branch, not patched here)


def bust_skills_cache():
    """Clear the skills prompt snapshot so changes take effect immediately."""
    try:
        os.environ.setdefault("HERMES_HOME", str(HERMES_HOME))
        sys.path.insert(0, str(HERMES_AGENT))
        from agent.prompt_builder import clear_skills_system_prompt_cache
        clear_skills_system_prompt_cache(clear_snapshot=True)
        print(f"  {PASS} skills cache busted")
    except Exception as e:
        print(f"  {FAIL} cache bust failed: {e}")


def main():
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv
    if dry_run:
        print("betterprompts — DRY RUN (no files will be changed)\n")
    else:
        print("betterprompts — applying patches\n")

    changed = False
    changed |= patch("skill_utils.py — whitelist (_InvertedSet)", SKILL_UTILS, SKILL_UTILS_OLD, SKILL_UTILS_NEW, dry_run)
    changed |= patch("prompt_builder.py — slim skills preamble", PROMPT_BUILDER, PROMPT_BUILDER_OLD, PROMPT_BUILDER_NEW, dry_run)

    print()
    if not dry_run:
        if changed:
            bust_skills_cache()
        else:
            print(f"  {SKIP} cache bust skipped — nothing changed")

    print("\ndone.")


if __name__ == "__main__":
    main()
