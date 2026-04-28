# Correction E2E

`tests/e2e/correction/` contains whole-path checks for stale, missing, superseded, or
withdrawn release state handling where KFM must stay fail-closed and preserve visible
lineage.

## What lives here

- correction-lineage drills that verify unresolved release references are not silently ignored
- cases that assert explicit `DENY` outcomes with reviewable failure reasons

## Current executable coverage

- `test_unresolved_release_artifact_is_visible_and_fail_closed`

The current test ensures unresolved release artifacts are surfaced in failures and that
resolution fails closed instead of proceeding with incomplete release state.

## Boundaries

This folder should test correction and lineage behavior, not:

- publishability assembly checks (`tests/e2e/release_assembly/`)
- request-time evidence/runtime response behavior (`tests/e2e/runtime_proof/`)

## Run

```bash
pytest -q tests/e2e/correction
```
