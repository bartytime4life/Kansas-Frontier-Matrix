# packages/indexers

This directory currently acts as a **placeholder indexer lane**.

## Current repo state (verified on 2026-04-26)

- The only committed file in `packages/indexers/` is this `README.md`.
- No runnable indexer implementation modules are present yet.
- No dedicated test suite exists under this directory yet.

## Intended role

When implemented, this lane should contain **derived index builders** (search/spatial/tile/temporal) that consume already-governed artifacts and do not redefine canonical truth.

## Next implementation move

1. Add one minimal, deterministic indexer thin slice (input fixture -> output artifact).
2. Add a matching test that validates output structure and checksum stability.
3. Document command-line usage and input/output contract in this README.

## Verification commands

Run from repository root:

```bash
find packages/indexers -maxdepth 3 -type f | sort
python3 tools/ci/generate_markdown_debt_backlog.py --root . --top 15 --output docs/runbooks/markdown-debt-backlog.md
```
