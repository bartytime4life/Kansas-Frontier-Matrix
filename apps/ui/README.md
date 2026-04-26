# UI Overview

This directory contains UI-facing code and tests.

## Current state (verified on 2026-04-26)

- `apps/ui/ecology/` exists and contains mapper logic and tests used by the ecology evidence drawer boundary.
- Boundary tests are present under `apps/ui/ecology/tests/`.

## Intended role

The UI layer should consume governed API/runtime outputs and render user-facing views without redefining policy or evidence authority.

## Next move

1. Keep UI payload contracts aligned with `schemas/contracts/v1/runtime/*`.
2. Expand mapper tests for any new drawer sections before changing UI payload shape.
3. Keep UI docs in sync with CI boundary checks.

## Verification commands

```bash
find apps/ui -maxdepth 3 -type f | sort
python3 -m pytest -q apps/ui/ecology/tests
python3 tools/ci/generate_markdown_debt_backlog.py --root . --top 15 --output docs/runbooks/markdown-debt-backlog.md
```
