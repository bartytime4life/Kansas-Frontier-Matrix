<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/spatial-foundation/boundary-derivation-record
title: BoundaryDerivationRecord Contract
type: semantic-contract; spatial-foundation; survey-control; geometry-provenance
version: v0.1.0
status: draft; PROPOSED; fixture-first; non-title; non-legal-boundary
owners: OWNER_TBD — Spatial foundation steward · Survey-data steward · Contracts steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; spatial-foundation; survey-control; provenance; non-authoritative
related:
  - ./README.md
  - ../../schemas/contracts/v1/spatial-foundation/boundary_derivation_record.schema.json
  - ../../fixtures/contracts/v1/spatial-foundation/boundary_derivation_record/
  - ../../tools/validators/validate_boundary_derivation_record.py
  - ../../tests/validators/test_validate_boundary_derivation_record.py
  - ../../docs/sources/catalog/blm/plss-cadnsdi.md
  - ../../docs/sources/catalog/blm/glo-survey-plats.md
  - ../../docs/sources/catalog/blm/glo-field-notes.md
  - ../../docs/intake/exploratory/new-ideas-4-25-source-map.md
notes:
  - "Implements the bounded KFM-TRIAD-062 gap."
  - "No fixture contains a real coordinate or asserts a legal boundary, title, parcel, or ownership fact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `BoundaryDerivationRecord`

> A source-role-aware provenance record for deriving analytic geometry from survey controls, historical survey material, adjustments, and georeferencing—without treating the derivative as title, ownership, parcel, or certified legal-boundary authority.

## Purpose

KFM source documentation distinguishes present-day PLSS/CadNSDI control geometry from historical GLO survey plats and field notes. The missing seam is a reusable record that explains how a derived line or polygon was produced:

- which source records and source roles were used;
- which control observations participated;
- control status, method, time, uncertainty, and evidence references;
- adjustment or georeferencing method and version;
- parameter digest;
- residual statistics;
- input/output geometry lineage;
- review outcome and fitness for analytic use; and
- non-title, non-parcel, and non-legal-boundary limitations.

The record prevents a rendered line, georeferenced plat, or derived polygon from silently masquerading as source geometry or legal authority.

## Directory Rules basis

The artifact has one semantic owner: spatial-foundation contract meaning. It therefore lives under `contracts/spatial-foundation/`. Companion machine shape uses the existing `schemas/contracts/v1/spatial-foundation/` lane. Synthetic cases, validator, tests, workflow, and authoring receipt remain under their respective responsibility roots. No new repository root or lifecycle store is created.

## Source-role anti-collapse

`source_roles` preserves the distinction among:

- `CONTROL_GEOMETRY`;
- `HISTORICAL_SURVEY`;
- `FIELD_NOTE`;
- `ADJUSTMENT`; and
- `CONTEXT`.

A historical plat is not automatically present-day control geometry. A field note is not a polygon. A georeferencing transform is not an observation. The derivative may cite all of them but may not collapse their authority roles.

## Survey controls

Each control entry binds:

- a stable control ID;
- an observation reference;
- control status;
- a coordinate reference rather than inline sensitive/real coordinates;
- observation or reconstruction method;
- observation time;
- uncertainty in meters; and
- evidence references.

The synthetic profile uses references only. It does not include or expose actual survey coordinates.

## Derivation and residuals

The record binds the method, version, parameters digest, adjustment type, input control IDs, residual summary, and output geometry digest. `point_count` must match the listed input controls, and maximum residual cannot be less than RMSE.

The contract deliberately defines no universal residual threshold. Fitness depends on source scale, intended use, method, jurisdiction, and review. The review object makes the bounded outcome explicit instead of hiding it inside one score.

## Review outcomes

| Outcome | Meaning |
|---|---|
| `ACCEPTED_FOR_ANALYSIS` | Reviewed, not unresolved, and permitted only for the declared analytic use. |
| `HOLD` | Unresolved support or control status remains; analysis use is denied. |
| `REJECTED` | Reviewed and not fit for analytic use. |

Even an accepted record remains `ANALYTIC_DERIVATION_ONLY`.

## Required limitations

Every conforming record fixes these claims to `false`:

- `legal_boundary_authority`;
- `title_or_ownership_authority`;
- `parcel_authority`;
- `source_geometry_overwritten`; and
- all governance/release/public-use authority flags.

The derivative does not overwrite source geometry. Consumers must retain and inspect the source records, transform receipt, residuals, review state, and limitation codes.

## Deterministic fixture hash

`kfm-fixture-json-v1` removes top-level `spec_hash`, serializes sorted-key UTF-8 JSON without insignificant whitespace, preserves array order, and computes SHA-256. This is a local fixture replay profile, not a repository-wide hash-policy decision.

## Validation boundary

The validator enforces bounded JSON safety, schema shape, canonical arrays, control closure, residual arithmetic, review-state consistency, time ordering, non-authority limitations, and governance non-effects.

A green result does not certify surveying quality, cadastral correctness, legal boundaries, title, ownership, source admission, evidence closure, policy, release, or public use.

## Correction and rollback

The slice is additive. Rollback removes only the new contract family README, contract, schema, synthetic fixtures, validator, tests, workflow, and generated authoring receipt. No source document, source geometry, lifecycle record, map layer, legal record, or release state changes.
