<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://package/temporal
title: Temporal package README
type: package-readme; shared-temporal-kernel
version: v0.3.0
status: proposed; fixture-first; no-network; non-authoritative
updated: 2026-09-05
responsibility_root: packages/
related:
  - ./pyproject.toml
  - ./src/README.md
  - ./src/temporal/README.md
  - ../../contracts/common/temporal_view_state.md
  - ../../schemas/contracts/v1/common/temporal_view_state.schema.json
  - ../../tools/validators/validate_temporal_view_state.py
  - ../../tests/validators/test_validate_temporal_view_state.py
  - ../../apps/explorer-web/src/features/temporal/
[/KFM_META_BLOCK_V2] -->

# KFM temporal package

packages/temporal owns reusable, renderer-independent temporal implementation support. Slice A adds deterministic state/query identity, typed-boundary normalization, a generation-guarded frame reducer, and no-network validation support for the proposed kfm.temporal.view-state.v1 profile.

The package is not an authority for temporal meaning, evidence, policy, release, correction, source admission, or publication. It composes the existing TemporalWindow, TemporalSlice, QueryRunRecord, EvidenceResolutionRecord, release, story, and public workspace responsibilities.

## Current Slice A behavior

- Preserves raw boundaries and typed precision; normalizes only timezone-aware instants.
- Returns bounded SUPPORTED, UNSUPPORTED, or ERROR outcomes for query normalization.
- Supports snapshot, moving-window, accumulation, event-step, and comparison configuration checks.
- Keeps requested/loading state separate from the committed frame and ignores stale generations.
- Rejects mixed-date or restricted frame metadata; a withheld layer carries no actual time or evidence reference.
- Derives reproducible state/query identities without credentials, source URLs, prompts, or raw payloads.

The six-kind TemporalWindow.time_kind vocabulary remains unresolved. This package does not silently translate it or widen the closed legacy contract. All production source activation, evidence resolution, policy, release, Site, and public-exposure decisions remain outside this package.

## Placement and lifecycle

Directory Rules and ADR-0029 place shared reusable implementation under packages/; the semantic successor and machine shape remain under contracts/common/ and schemas/contracts/v1/common/. Fixtures stay under fixtures/; repository validator entry points stay under tools/validators/; tests stay under tests/.

The lifecycle boundary remains:

RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED

This Slice A creates no data, release, database, broker, transport, renderer, migration, or publication artifact.

## Validation and rollback

Run:

- python -m unittest discover --start-directory tests/validators --pattern 'test_validate_temporal_view_state.py' --verbose
- python tools/validators/validate_temporal_view_state.py --fixtures
- python -m pytest -q tests/schemas/test_common_contracts.py -k temporal_view_state
- pnpm --dir apps/explorer-web exec vitest run tests/temporal-kernel.test.ts

A green result does not prove Site editing, MapLibre/GPU readiness, production data admission, evidence closure, policy approval, release readiness, or publication.

Before merge, close the draft PR and abandon this branch. After an authorized merge, revert the contract, schema, fixtures, validator, tests, package, adapter, and workflow together. Existing Site version 42 and rollback version 41 remain untouched.
