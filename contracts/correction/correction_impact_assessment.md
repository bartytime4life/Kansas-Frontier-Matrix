<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/correction/correction-impact-assessment
title: CorrectionImpactAssessment Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — correction steward · release steward · validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; fixture-only; non-authoritative
related:
  - ./correction_notice.md
  - ../../schemas/contracts/v1/correction/correction_impact_assessment.schema.json
  - ../../fixtures/contracts/v1/correction/correction_impact_assessment/
  - ../../tools/validators/correction/validate_correction_impact_assessment.py
  - ../../tests/validators/correction/test_correction_impact_assessment.py
tags: [kfm, correction, propagation, cache, map, search, ai, rollback]
[/KFM_META_BLOCK_V2] -->

# CorrectionImpactAssessment Contract

`CorrectionImpactAssessment` is a deterministic, fixture-only inventory of the downstream carriers that may need correction, withdrawal, supersession, rebuilding, revalidation, or cache invalidation after a `CorrectionNotice`.

It does not perform the correction. It makes the propagation burden explicit before a correction can be represented as complete.

## Status and non-authority boundary

| Field | Value |
|---|---|
| Profile | `kfm.correction.impact-assessment.v1` |
| Execution | `FIXTURE_ONLY_NO_NETWORK` |
| Outcomes | `COMPLETE`, `HOLD`, `ERROR` |
| Authority | `NONE` |

A `COMPLETE` assessment proves only that the declared carrier inventory is structurally and semantically closed, approved for review purposes, bound to a policy decision, and linked to a rollback target. It does not mutate a catalog, API, map, tile, index, graph, export, AI answer, cache, document, release, or public state.

## Required carrier inventory

Every assessment contains exactly one row, in canonical order, for:

1. `CATALOG`
2. `API`
3. `MAP`
4. `TILE`
5. `SEARCH`
6. `GRAPH`
7. `EXPORT`
8. `AI`
9. `CACHE`
10. `DOCUMENTATION`

Each row states whether the carrier is affected, the required action, stable reason codes, and affected artifact references.

## Anti-collapse and fail-closed rules

- Affected carriers require a non-`NO_ACTION` action, at least one reason code, and at least one artifact reference.
- Unaffected carriers require `NO_ACTION`, no artifact references, and `NOT_APPLICABLE_CONFIRMED`.
- An affected `CACHE` carrier requires `INVALIDATE` and `CACHE_INVALIDATION_REQUIRED`.
- An affected `AI` carrier requires `REVALIDATE`, `WITHDRAW`, or `SUPERSEDE` and `CITATIONS_REVALIDATE`.
- `COMPLETE` requires `review_state=APPROVED`, a `policy_decision_ref`, and a `rollback_target_ref`.
- Missing carriers, duplicate carriers, invalid action semantics, digest drift, or identity drift return `ERROR`.
- Unresolved review, policy, or rollback support returns `HOLD`.
- All authority, repository-mutation, release, publication, and public-use flags remain false.

## Directory Rules basis

Semantic meaning belongs in `contracts/correction/`; machine shape in `schemas/contracts/v1/correction/`; synthetic examples in `fixtures/contracts/v1/correction/`; executable validation in `tools/validators/correction/`; enforceability in `tests/validators/correction/`; source adaptation in `docs/intake/exploratory/`; and AI authoring provenance in `data/receipts/generated/`.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q tests/validators/correction/test_correction_impact_assessment.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/correction/validate_correction_impact_assessment.py \
  fixtures/contracts/v1/correction/correction_impact_assessment/valid/*.json
```

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the bounded feature commit. This inactive profile creates no external or lifecycle state requiring operational cleanup.
