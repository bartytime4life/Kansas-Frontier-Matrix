<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/briefing-implementation-campaign-20260806
title: Briefing Implementation Campaign — Temporal, Trace, MapLibre, and USDM
type: implementation-note
version: v0.1.0
status: draft; PROPOSED; synthetic-only; no-network
owners: ["@bartytime4life"]
created: 2026-08-06
updated: 2026-08-06
policy_label: public; architecture; validation; geospatial; non-authoritative
[/KFM_META_BLOCK_V2] -->

# Briefing implementation campaign — August 6, 2026

This bounded campaign implements the still-actionable engineering items from the August 6 KFM briefing. The earlier `AIChangeProposal` fixture-classification correction was already present in later repository history, so this slice does not duplicate it.

## Components

### TemporalSlice SQL storage experiment

`tools/experiments/temporal_slice_store.py` provides a standard-library SQL experiment with two explicit indexes:

```text
(dataset_version_ref, grid_key, temporal_start, temporal_end, slice_id)
(dataset_version_ref, grid_key, temporal_start, delta_magnitude, slice_id)
```

The reference executor is SQLite, using a conservative SQL subset intended to remain portable to DuckDB. It models half-open windows, explicit supersession, deterministic change ordering, and a fail-closed `AMBIGUOUS` result when overlapping unsuperseded slices compete for the same dataset, grid key, and instant. It does not create or migrate a production database.

### Trace-to-temporal closure

`tools/validators/validate_trace_temporal_closure.py` checks a synthetic chain:

```text
RunReceipt digest
  -> EvidenceBundle run-receipt binding
  -> TraceReceiptLink run/evidence anchors
  -> TemporalSlice provenance references
  -> materialized artifact SHA-256
```

Each cross-reference is mutated independently in the negative lane. The validator reads only committed local files, rejects path escape and symlink traversal, recomputes artifact bytes, and keeps every authority, policy, promotion, release, publication, and public-use flag false.

### MapLibre GL JS v6 readiness

`tools/validators/maplibre/validate_v6_readiness.py` does not select or install MapLibre. It inspects repository manifests and source boundaries, then combines that static evidence with an optional finite browser-probe record. `READY` requires:

- an exact `6.x.y` `maplibre-gl` dependency;
- ESM mode and an ES2022 TypeScript target;
- no direct MapLibre imports outside `packages/maplibre/`;
- no use of internal `map.transform` state; and
- passing WebGL2 fallback, worker/CSP, style-spec v25, `GeoJSONSource.setData`, `queryRenderedFeatures`, and visual-diff probes.

The current repository is expected to remain `HOLD` because no exact MapLibre dependency or browser-probe result record is present. A hold is not a workflow failure; it is the truthful pre-upgrade state.

### USDM material-change profile

`tools/validators/domains/hazards/validate_usdm_materiality.py` compares immutable synthetic weekly U.S. Drought Monitor snapshots. It distinguishes:

- `UNCHANGED -> NON_EVENT`;
- `SEMANTIC_NON_MATERIAL -> NON_EVENT`;
- `MATERIAL -> PROMOTION_CANDIDATE`; and
- `UNDETERMINED -> HOLD`.

The profile checks severity-area nesting, weekly time order, geometry and population changes, governed thresholds, and declared-versus-computed outcomes. Administrative drought stages and other legal-declaration fields are rejected from the observation snapshot so physical classification and government action remain separate object families.

## Trust boundary

All data are synthetic and committed. No USDM, Kansas, MapLibre, telemetry, database, registry, OCI, or other external service is contacted. Passing tests do not authenticate evidence, activate a source, resolve a receipt, evaluate policy, authorize a dependency upgrade, promote data, release artifacts, deploy software, publish content, or permit public use.

## Validation

```bash
python -m unittest discover -s tests/experiments -p 'test_temporal_slice_store.py' -v
python -m unittest discover -s tests/validators -p 'test_validate_trace_temporal_closure.py' -v
python -m unittest discover -s tests/maplibre -p 'test_validate_v6_readiness.py' -v
python -m unittest discover -s tests/domains/hazards -p 'test_validate_usdm_materiality.py' -v
python tools/experiments/temporal_slice_store.py --self-test
python tools/validators/validate_trace_temporal_closure.py --fixtures
python tools/validators/maplibre/validate_v6_readiness.py --fixtures
python tools/validators/domains/hazards/validate_usdm_materiality.py --fixtures
```

## Rollback

Before merge, close the draft pull request and delete its branch. After merge, use a focused revert of this campaign commit. No external source, database, dependency selection, release, deployment, or publication state must be rolled back because none is created here.
