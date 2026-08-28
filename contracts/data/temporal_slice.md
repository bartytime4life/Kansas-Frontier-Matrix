<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/temporal-slice
title: TemporalSlice Contract
type: semantic-contract; derived-view-metadata; temporal-index-carrier
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Data steward · Temporal steward · Evidence steward · Contract steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; data; temporal-slice; process-memory; non-publisher
related:
  - ./README.md
  - ../common/temporal_window.md
  - ./dataset_version.md
  - ./material_change_assessment.md
  - ../evidence/evidence_bundle.md
  - ../runtime/run_receipt.md
  - ../../schemas/contracts/v1/data/temporal_slice.schema.json
  - ../../tools/validators/validate_temporal_slice.py
notes:
  - "Implements one bounded persistent-observation pattern mined from New Ideas 3-16-26.pdf."
  - "The source's deterministic-ULID suggestion is adapted to a content-derived SHA-256 identity."
  - "This object permits PROCESSED or CATALOG candidates only and creates no release or public-use authority."
[/KFM_META_BLOCK_V2] -->

# TemporalSlice

`TemporalSlice` is deterministic metadata for one time-bounded, spatially supported derived view, such as a tile, coverage cell, feature set, or story section. It supports “what changed here, when, and under which evidence and run?” without treating the view, artifact, or change score as source truth.

## Responsibility and placement

The object belongs in `contracts/data/` because it describes a derived data view and its lineage. `TemporalWindow` remains the shared time value under `contracts/common/`; artifact and release semantics remain under their existing release families. Machine shape, fixtures, validator, tests, CI, source assay, and authoring receipt remain in their existing responsibility roots. No new root, lifecycle stage, database, API route, proof family, or public surface is created.

## Deterministic identity

```text
slice_id = "kfm:temporal-slice:sha256:" + sha256(canonical_json({
  dataset_version_ref,
  temporal_window,
  footprint_hash,
  grid_system,
  grid_key,
  spec_hash
}))
```

Canonical JSON uses UTF-8, sorted object keys, no insignificant whitespace, finite numbers, and preserved array order. The profile name is `kfm-temporal-slice-id-v1`.

## Required meaning

A slice binds one `DatasetVersion` reference; one explicit `TemporalWindow`; spatial support and footprint digest; one or more `EvidenceBundle` references; one `RunReceipt` reference; the governing `spec_hash`; declared checks, policy labels, obligations, and optional policy/gate references; local change lineage; and digest-bound references to materialized map, story, Focus Mode, API, or export artifacts.

A reference is not proof that its target resolves. This fixture-first validator checks local shape and consistency only.

## Invariants

- Timestamps are timezone-aware and `start <= end`.
- Reference and label arrays are sorted and unique.
- Artifact references are sorted, unique, payload-free, and bound to non-placeholder SHA-256 digests.
- `BASELINE` has no previous slice or change support.
- `CHANGED` requires a distinct previous slice, change support, and a declared change signal.
- `UNCHANGED` requires a previous slice and `MaterialChangeAssessment` reference, with no delta details.
- A `CATALOG` candidate records the gate reference that admitted it to that stage.
- Self-lineage, all-zero digest placeholders, governance overclaim, and deterministic-ID mismatch fail closed.
- Validation success creates no evidence, policy, promotion, release, publication, or public-use authority.

## Lifecycle boundary

This profile permits only `PROCESSED` and `CATALOG`. `PUBLISHED` is deliberately absent. A later governed release may reference a reviewed slice only after evidence resolution, policy and sensitivity evaluation, review, proof closure, release-manifest closure, correction support, and a rollback target exist.

## Validation

```bash
PYTHONPATH=. KFM_NO_NETWORK=1 \
  python tools/validators/validate_temporal_slice.py --fixtures

PYTHONPATH=. KFM_NO_NETWORK=1 \
  python -m unittest discover \
    --start-directory tests/validators \
    --pattern 'test_validate_temporal_slice.py' \
    --verbose
```

A green result proves only the proposed schema, deterministic identity profile, exact synthetic fixture polarity, temporal ordering, canonical references, and local change-lineage rules.

## Correction and rollback

Before merge, close the draft pull request and abandon the feature branch. After an authorized merge, revert the dependency-closed contract/schema/fixtures/validator/tests/workflow/source-map/receipt change. If later persisted records rely on stable `slice_id` values, preserve those records and use correction or supersession rather than destructive deletion.
