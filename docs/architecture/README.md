# Architecture Overview

This directory contains architecture notes for repository subsystems.

## Current structure (verified on 2026-04-26)

- `docs/architecture/governed-ai/` — architecture notes for governed AI surfaces.

## Architecture intent

Repository architecture should keep these boundaries explicit:

1. **Contracts and schemas** define machine-checkable interfaces.
2. **Policy and validation tooling** enforce release/runtime guardrails.
3. **Applications and pipelines** implement behavior behind those contracts.
4. **Runbooks and ADRs** document operational and governance decisions.

## Next move

1. Add one concise subsystem architecture page per major lane (API, UI, pipelines, validators).
2. Link each architecture page to the owning contract/schema and CI checks.
3. Keep architecture docs factual and aligned with checked-in code paths.

## Verification commands

```bash
find docs/architecture -maxdepth 3 -type f | sort
python3 tools/ci/generate_markdown_debt_backlog.py --root . --top 15 --output docs/runbooks/markdown-debt-backlog.md
```
