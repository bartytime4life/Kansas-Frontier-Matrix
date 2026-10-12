<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/spatial-foundation/xy-point-transform-receipt
title: XYPointTransformReceiptCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Spatial Foundation steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; spatial-foundation; coordinate-creation; transform-lineage; auditability
responsibility: Define a fixture-only receipt candidate for table-to-point coordinate creation with explicit fields, CRS binding, precision, range checks, count reconciliation, and non-authority boundaries.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./README.md
  - ../../schemas/contracts/v1/spatial-foundation/xy_point_transform_receipt.schema.json
  - ../../fixtures/contracts/v1/spatial-foundation/xy_point_transform_receipt/cases.json
  - ../../tools/validators/validate_xy_point_transform_receipt.py
  - ../../tests/validators/test_validate_xy_point_transform_receipt.py
  - ../../docs/intake/exploratory/pass-18-xy-point-transform-receipt-source-map.md
[/KFM_META_BLOCK_V2] -->

# XYPointTransformReceiptCandidate

`XYPointTransformReceiptCandidate` is an additive, fixture-only profile for recording how a tabular pair of coordinate fields was interpreted to create a point-set candidate.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-174`: declare the source table, X and Y fields, coordinate reference system, precision, validation checks, output identity, and row-count consequences of an XY-to-point transform.

## Boundary

The profile is `PROPOSED_INACTIVE`, no-network, and non-authoritative. A validator `PASS` means only that:

- the candidate is closed under this schema;
- its deterministic profile hash replays;
- source and output artifacts are pinned by reference and digest;
- X and Y fields are distinct and carry a supported semantic-role pair;
- a CRS binding is explicitly resolved for the fixture profile;
- declared and observed coordinate bounds are ordered and the observed bounds fit within the declared bounds;
- observed decimal precision does not exceed the declared precision;
- source, created-point, rejected-row, and reason counts reconcile;
- the output point-set count and CRS binding match the transform summary; and
- evidence references are canonically ordered.

It does **not** open or inspect the source table, parse a CRS definition, transform coordinates, prove that coordinates are accurate, authenticate an artifact digest, resolve evidence, approve manual review, create a domain observation, promote lifecycle state, release, deploy, publish, or authorize public use.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_spec_hash` | Canonical JSON plus SHA-256 binding of the complete candidate except this field. |
| `transform_ref` | Stable identity of this proposed transform receipt. |
| `source_table` | Pinned source-table candidate, explicit local resolution state, source role, and row count. |
| `axis_mapping` | Distinct X/Y field names and paired semantic roles (`LONGITUDE`/`LATITUDE`, `EASTING`/`NORTHING`, or `X_COORDINATE`/`Y_COORDINATE`). |
| `coordinate_reference_system` | Pinned CRS reference and digest plus explicit resolution state, coordinate-space class, axis order, and unit. The validator does not parse or endorse the referenced CRS. |
| `precision` | Declared maximum and observed decimal-place counts for the two input fields. |
| `declared_valid_bounds` / `observed_coordinate_bounds` | Explicit finite envelopes used only for deterministic range reconciliation. They are not geometry or a coverage claim. |
| `validation_summary` | Total, accepted, rejected, and per-reason row counts plus a declared axis-swap check. |
| `output_point_set` | Pinned synthetic output candidate with `POINT` geometry, count, and exact CRS binding. |
| `evidence_refs` | Canonically ordered references retained for a later resolver. |
| `authority_claims` | Fixed-false declaration preventing observation, evidence, policy, review, promotion, release, publication, or public-use authority. |

No individual coordinates or source rows are carried by this profile. Real transforms need separately governed source access, rights, sensitivity, evidence, review, and lifecycle handling.

## Axis and range interpretation

The validator checks only the declared fixture semantics. A supported X/Y role pair prevents a field labeled `LATITUDE` from silently occupying the X role or a field labeled `LONGITUDE` from silently occupying the Y role. It does not infer axis meaning from a field name or a CRS database.

The declared bounds are part of the candidate. They must be proper, and the observed envelope must fit inside them. Passing that check proves internal agreement only; it does not prove that the declared envelope is suitable for the referenced CRS or real source.

## Count reconciliation

For the fixture profile:

`source rows = created points + rejected rows`

and:

`rejected rows = missing-coordinate rows + out-of-range rows + non-finite rows + other-invalid rows`.

The output point-set count must equal the created-point count. These equations prevent silent row disappearance; they do not establish that rejection reasons were observed correctly in a real table.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, bindings, axis roles, bounds, precision, counts, output lineage, and canonical references are coherent. |
| `ABSTAIN` | The source table or CRS binding is explicitly unresolved. |
| `DENY` | A deterministic identity, UTC, axis, bounds, precision, count, output, or canonicalization invariant fails. |
| `ERROR` | The candidate cannot be evaluated safely under the closed machine schema. |

These are validator outcomes only. They are not evidence findings, review decisions, release states, or runtime answers.

## Directory Rules basis

The accepted responsibility-root model places shared spatial representation and transform-lineage meaning under `contracts/spatial-foundation/`, machine shape under `schemas/`, synthetic cases under `fixtures/`, repository validation under `tools/`, executable checks under `tests/`, CI orchestration under `.github/`, source reconciliation under `docs/`, and authoring accountability under `data/receipts/generated/`.

No new root, CRS registry, source registry, evidence authority, policy authority, runtime transform, or publication path is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_xy_point_transform_receipt -v
python tools/validators/validate_xy_point_transform_receipt.py --fixtures
```

## Rollback

Revert the additive profile packet. It has no consumer and mutates no source table, point layer, observation, evidence record, policy decision, lifecycle record, release, cache, route, deployment, or public artifact.
