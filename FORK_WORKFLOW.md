# Fork Workflow

## Setup (already done)
- `upstream` → NousResearch/hermes-agent (the real repo)
- `origin` → karrllas/hermes-agent (your fork)
- `main` — tracks upstream, kept clean
- `my-mods` — your changes live here

## Getting upstream updates

```bash
# 1. hermes update pulls new commits into main automatically
hermes update

# 2. Switch to your branch and rebase onto updated main
git checkout my-mods
git rebase main

# 3. Force-push your rebased branch to your fork
git push origin my-mods --force-with-lease
```

## What rebase does

Before:
```
main      A──B──C──D──E──F──G──H   (new upstream commits)
my-mods   A──B──C──D──E──X──Y      (your commits, old base)
```

After `git rebase main`:
```
main      A──B──C──D──E──F──G──H
my-mods                         X'──Y'  (your commits replayed on top)
```

Your commits get re-applied one by one on top of the latest main.
If upstream changed the same lines you did, you'll get a conflict to resolve.

## Notes
- `--force-with-lease` is a safe force-push — refuses if someone else pushed to your fork branch unexpectedly
- `hermes update` only ever touches `main`, never `my-mods`
- After rebasing, test that your changes still work before using
