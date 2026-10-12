# `schemas/contracts/v1/spatial-foundation/` — Spatial Foundation Schemas

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-spatial-foundation-readme
title: schemas/contracts/v1/spatial-foundation/ README
type: readme; schema-family-index; spatial-foundation; machine-shape
version: v0.2.0
status: draft; PROPOSED; fixture-first; mixed-maturity
updated: 2026-08-05
policy_label: public; schemas; contracts-v1; spatial-foundation; non-authoritative
tags: [kfm, schemas, spatial-foundation, survey-control, boundary-derivation, provenance]
related:
  - ../../../../contracts/spatial-foundation/README.md
  - ../../../../contracts/spatial-foundation/boundary_derivation_record.md
  - ../../../../fixtures/contracts/v1/spatial-foundation/boundary_derivation_record/
  - ../../../../tools/validators/validate_boundary_derivation_record.py
  - ../../../../tests/validators/test_validate_boundary_derivation_record.py
notes:
  - "v0.2.0 replaces the former README-only guardrail with one bounded proposed schema profile."
  - "Schema validity grants no title, ownership, parcel, survey certification, legal-boundary, source, evidence, policy, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

## Purpose

This lane owns machine-checkable shape for cross-domain Spatial Foundation objects whose primary responsibility is coordinate/reference grammar, geometry lineage, representation, control, uncertainty, and fitness-for-use rather than the truth of one consuming domain.

It remains a schema responsibility lane only. Semantic meaning belongs under `contracts/spatial-foundation/`; fixtures, validator code, tests, lifecycle records, policy, release decisions, and public behavior remain in their own roots.

## Current proposed schema

| Schema | Contract | Status | Scope |
|---|---|---|---|
| [`boundary_derivation_record.schema.json`](./boundary_derivation_record.schema.json) | [`BoundaryDerivationRecord`](../../../../contracts/spatial-foundation/boundary_derivation_record.md) | `PROPOSED` / fixture-first | Source-role-aware survey-control, adjustment/residual, review, lineage, and analytic-use shape. |

## Authority boundary

A conforming `BoundaryDerivationRecord` is an analytic provenance record. It is not:

- title or ownership evidence;
- parcel authority;
- a certified cadastral or legal boundary;
- source admission or EvidenceBundle closure;
- a PolicyDecision, review approval, PromotionDecision, ReleaseManifest, or publication permission.

Fixtures contain synthetic references and no real survey coordinates.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_boundary_derivation_record.py' \
  --verbose

python tools/validators/validate_boundary_derivation_record.py --fixtures
```

A green result proves only the bounded machine shape and local semantic invariants exercised by the proposed fixture profile.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the dependency-closed contract/schema/fixture/validator/test/workflow/receipt change. No source geometry, lifecycle record, legal record, release, or published artifact requires restoration.
