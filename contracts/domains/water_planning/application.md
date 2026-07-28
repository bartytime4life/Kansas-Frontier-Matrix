<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-application
title: Application Contract — Water Planning
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
  - ../../../schemas/contracts/v1/domains/water_planning/application.schema.json
  - ../../../fixtures/domains/water_planning/application/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# Application Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/application.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/application/`

## Meaning

A grant application submitted within a given ApplicationWindow. Missing applicant identity must be stored as applicant_resolution_status: unresolved, never guessed. Missing geometry must be stored as geometry_confidence: unresolved. An application is not a recommendation, award, payment, or project.

## Anti-collapse boundaries

- An application is not an award.
- Missing applicant identity → unresolved, never guessed.
- Missing geometry → unresolved, never guessed.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/application.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/application.schema.json`](../../../schemas/contracts/v1/domains/water_planning/application.schema.json) — Schema
- [`fixtures/domains/water_planning/application/`](../../../fixtures/domains/water_planning/application/) — Fixtures
