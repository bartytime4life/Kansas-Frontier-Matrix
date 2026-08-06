<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/temporal-slice
title: TemporalSlice Contract
type: semantic-contract; derived-view-metadata; temporal-index-carrier
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Data steward · Temporal steward · Evidence steward · Contract steward · Validation steward · Release steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; data; temporal-slice; derived-view; process-memory; non-publisher
related:
  - ./README.md
  - ../common/temporal_window.md
  - ./dataset_version.md
  - ./material_change_assessment.md
  - ../evidence/evidence_bundle.md
  - ../runtime/run_receipt.md
  - ../../schemas/contracts/v1/data/temporal_slice.schema.json
  - ../../fixtures/contracts/v1/data/temporal_slice/
  - ../../tools/validators/validate_temporal_slice.py
  - ../../tests/validators/test_validate_temporal_slice.py
  - ../../docs/intake/exploratory/new-ideas-3-16-26-temporal-slice-source-map.md
tags: [kfm, temporal-slice, persistent-observation, time-first, change-index, evidence-bundle, run-receipt, fixture-first]
notes:
  - "Implements one bounded persistent-observation pattern mined from New Ideas 3-16-26.pdf."
  - "The source's deterministic-ULID suggestion is adapted to a content-derived SHA-256 identity so replay does not depend on timestamp entropy."
  - "This first profile describes PROCESSED or CATALOG candidates only and cannot authorize PUBLISHED or public use."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# TemporalSlice

> `TemporalSlice` is a compact, deterministic metadata record for one time-bounded and spatially supported derived view—such as a tile, coverage cell, feature set, or story section. It makes “what changed here, when, and under which evidence and run?” queryable without treating the view, its artifact, or its change score as source truth.

## Purpose

Persistent observation changes the normal lookup from “show this feature” to “show the latest supported view at this place, compare it with the prior supported view, and explain the evidence and processing behind the difference.”

A `TemporalSlice` therefore binds:

- one `DatasetVersion` reference;
- one explicit `TemporalWindow`;
- one spatial support key and footprint digest;
- one or more `EvidenceBundle` references;
- one run-receipt reference and governing `spec_hash`;
- declared checks, policy labels, obligations, and gate references;
- optional prior-slice and change-proof lineage; and
- one or more referenced materializations for map, story, Focus Mode, API, or export use.

The object is process and catalog metadata. It is not the observation payload, a source admission record, a proof pack, a policy decision, a release manifest, a public claim, or permission to render.

## Why this belongs in `contracts/data/`

`TemporalWindow` is the shared temporal value object and remains under `contracts/common/`. A temporal slice is larger: it describes a derived data view, its dataset version, spatial support, provenance, change lineage, and materialized artifact references. That responsibility fits the existing data semantic-contract family.

| Responsibility | Home |
|---|---|
| Temporal interval meaning | `contracts/common/temporal_window.md` |
| Derived slice meaning | `contracts/data/temporal_slice.md` |
| Machine shape | `schemas/contracts/v1/data/temporal_slice.schema.json` |
| Synthetic examples | `fixtures/contracts/v1/data/temporal_slice/` |
| Executable validation | `tools/validators/validate_temporal_slice.py` |
| Focused tests | `tests/validators/test_validate_temporal_slice.py` |
| Release authority | Existing release contract, policy, review, proof, and manifest families—not this object |

No new root, lifecycle stage, catalog authority, proof family, release object, API route, database table, or public surface is created.

## Source adaptation

The source packet proposes a deterministic ULID over dataset, footprint, time window, and `spec_hash`. A ULID normally includes a time component and entropy, which can make a supposedly deterministic replay ambiguous. This profile preserves the source’s identity inputs but uses a content-derived identifier instead:

```text
slice_id =
  "kfm:temporal-slice:sha256:" +
  sha256(canonical_json({
    dataset_version_ref,
    temporal_window,
    footprint_hash,
    grid_system,
    grid_key,
    spec_hash
  }))
```

Canonical JSON uses sorted keys, UTF-8, no insignificant whitespace, and preserved array order. The profile name is `kfm-temporal-slice-id-v1`.

## Object surface

```text
TemporalSlice
├── slice_id + identity_profile
├── dataset_version_ref
├── temporal_window + cadence_hint
├── spatial
│   ├── footprint_hash
│   ├── support_type
│   ├── grid_system + grid_key
│   └── geometry_ref
├── provenance
│   ├── evidence_bundle_refs[]
│   ├── run_receipt_ref
│   ├── spec_hash
│   ├── processing_level
│   └── input_refs[]
├── verification
│   ├── promotion_gate_ref
│   ├── check_refs[]
│   ├── policy_decision_refs[]
│   ├── policy_labels[]
│   └── obligations[]
├── change
│   ├── state
│   ├── previous_slice_ref
│   ├── material_change_assessment_ref
│   ├── delta_proof_ref
│   ├── delta_magnitude
│   └── change_flags[]
├── materialization
│   ├── surfaces[]
│   └── artifacts[]
├── lifecycle_stage
└── governance
```

## Relationship to adjacent objects

| Object | Relationship | Non-collapse rule |
|---|---|---|
| `DatasetVersion` | Names the versioned dataset representation from which the slice was derived. | The slice does not replace dataset version/source/rights semantics. |
| `TemporalWindow` | Provides the explicit supported interval and time kind. | A valid interval is not proof that an observation occurred. |
| `EvidenceBundle` | Declared support for consequential interpretation. | A reference is not evidence closure unless resolution succeeds. |
| `RunReceipt` | Identifies the process that produced or checked the slice. | A run receipt is not a release or proof of truth. |
| `MaterialChangeAssessment` | Optional reproducible classification of baseline-versus-candidate change. | A materiality result is not promotion authority. |
| `TileArtifactManifest` or other artifact manifests | May describe referenced materialized artifacts more fully. | The slice does not become the artifact manifest or payload. |
| `ReleaseManifest` / `PromotionDecision` | Later governed transition may reference the slice. | This first profile fixes release/public-use fields to false/null. |

## Time-first index projections

The source packet recommends two stable lookup shapes. This contract records the keys but does not create a database or choose PostgreSQL, SQLite, DuckDB, Elasticsearch, or another implementation.

```text
slice_time_idx:
  (dataset_version_ref, spatial.grid_key,
   temporal_window.start, temporal_window.end, slice_id)

slice_change_idx:
  (dataset_version_ref, spatial.grid_key,
   temporal_window.start, change.delta_magnitude, slice_id)
```

These support “latest at location,” bounded time-window scans, top-N declared changes, and the trace path:

```text
slice_id
  -> EvidenceBundle
  -> RunReceipt
  -> declared checks / policy references
```

A future storage migration must verify database conventions, reference integrity, retention, correction behavior, and rollback independently.

## Required invariants

- `slice_id`  is derived from the exact identity projection above.
- `TemporalWindow.start` must not follow `TemporalWindow.end`.
- Timestamps must be timezone-aware.
- Evidence-bundle references are non-empty.
- Reference and label arrays are sorted and unique for deterministic replay.
- Materialized artifact references are sorted, unique, digest-bound, and payload-free.
- A baseline slice has no prior slice or change support.
- `CHANGED` `requires a prior slice, change support, and a declared change signal.
- `UNCHANGED` requires a prior slice and a `MaterialChangeAssessment` reference, with no delta details.
- A CATALOG-stage slice records the gate reference that admitted the candidate to that stage.
- SHA-256 placeholder digests are denied.
- Self-lineage is denied.
- Governance flags cannot claim evidence closure, policy evaluation, promotion, release, publication, or public use.
- Validation success creates no authority.

## Lifecycle boundary

This first profile intentionally permits only:

- `PROCESSED`—a validated derived candidate; or
- `CATALOG`—a catalog candidate with a declared gate reference.

It does not admit `PUBLISHED`. The allowed forward path is:

```text
TemporalSlice(PROCESSED or CATALOG)
  -> evidence resolution
  -> policy and sensitivity evaluation
  -> review and promotion decision
  -> proof and release-manifest closure
  -> governed released artifact
```

Public clients and normal UI surfaces must continue to consume released, policy-safe products through governed interfaces. They must not load a TemporalSlice candidate directly.

## Validator outcomes

The no-network validator emits stable, non-echoing findings for:

- deterministic slice-ID mismatch;
- temporal ordering or timezone defects;
- noncanonical reference arrays and artifact order;
- all-zero digest placeholders;
- missing or self-referential prior-slice lineage;
- unsupported changed/unchanged/baseline combinations;
- missing catalog gate reference;
- governance overclaim;
- unsafe files, duplicate keys, non-finite numbers, malformed JSON, bounded-size/depth failures; and
- JSON Schema failure.

## Validation

```bash
PYTHONPATH=. KFM_NO_NETWORK=1   python tools/validators/validate_temporal_slice.py --fixtures

PYTHONPATH=. KFM_NO_NETWORK=1   python -m unittest discover   --start-directory tests/validators   --pattern 'test_validate_temporal_slice.py'   --verbose
```

A green result proves only the proposed schema, deterministic identity profile, exact synthetic fixture polarity, temporal ordering, canonical arrays, and local lineage rules. It does not resolve a real EvidenceBundle or receipt, evaluate policy, create a catalog item, build an index, promote, release, publish, or authorize public use.

## Correction and rollback

Before merge, close the draft pull request and abandon the feature branch. After an authorized merge, revert the dependency-closed contract/schema/fixtures/validator/tests/workflow/source-map/receipt change. If later records rely on stable `slice_id` values, preserve those records and use correction or supersession instead of destructive deletion.

[Back to top](#top)
