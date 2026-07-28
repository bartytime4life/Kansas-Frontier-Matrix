<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-scoring-matrix-version
title: ScoringMatrixVersion Contract — Water Planning
type: semantic-contract
version: v0.1
status: draft; PROPOSED; schema-scaffold; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Water Planning domain steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
created: 2026-07-28
updated: 2026-07-28
policy_label: public-with-gates; semantic-contract; water-planning; deferred-epic; PROPOSED
related:
  - ./README.md
  - ../../../schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json
  - ../../../fixtures/domains/water_planning/scoring_matrix_version/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# ScoringMatrixVersion Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/scoring_matrix_version/`

## Meaning

A versioned scoring matrix used to evaluate grant applications under a given ProgramVersion. Each matrix version must be digest-linked so historical guidance remains traceable. A scoring matrix is not a project outcome, application, award, or ProgramVersion.

## Anti-collapse boundaries

- A scoring matrix is not a project outcome.
- A scoring matrix is not a program version.
- Digest linkage is required to preserve historical traceability.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json`](../../../schemas/contracts/v1/domains/water_planning/scoring_matrix_version.schema.json) — Schema
- [`fixtures/domains/water_planning/scoring_matrix_version/`](../../../fixtures/domains/water_planning/scoring_matrix_version/) — Fixtures
