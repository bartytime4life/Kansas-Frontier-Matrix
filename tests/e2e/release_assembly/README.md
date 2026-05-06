# Release Assembly E2E

`tests/e2e/release_assembly/` contains end-to-end checks that prove a release can be
assembled from governed inputs and either:

- be marked publishable when closure is complete, or
- fail closed (`DENY`) when required release references are missing.

## What lives here

- release manifest closure tests
- publish-plan wiring checks that consume closure results
- fixtures that represent valid and invalid release-manifest states

## Current executable coverage

- `test_release_manifest_closure_publishable`
- `test_release_manifest_missing_provenance_is_denied`
- `test_publish_plan_is_built_from_publishable_closure`

All cases use local fixture manifests under `tests/fixtures/release/` and monkeypatch
external validators to keep tests deterministic.

## Boundaries

This folder should test publish-path behavior, not:

- request-time runtime outcome behavior (`tests/e2e/runtime_proof/`)
- correction lineage drills (`tests/e2e/correction/`)
- low-level schema-only checks (`tests/contracts/`)

## Run

```bash
pytest -q tests/e2e/release_assembly
```
