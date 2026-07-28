<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-planning-region
title: PlanningRegion Contract — Water Planning
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
  - ../../../schemas/contracts/v1/domains/water_planning/planning_region.schema.json
  - ../../../fixtures/domains/water_planning/planning_region/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# PlanningRegion Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/planning_region.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/planning_region/`

## Meaning

A Kansas Regional Advisory Committee (RAC) planning area identity. Kansas has exactly 14 RAC planning areas numbered 1–14. Missing or unresolvable geometry must be represented as geometry_confidence: unresolved, never guessed. A PlanningRegion is not a meeting, award, or project.

## Anti-collapse boundaries

- A planning region is not a meeting.
- A planning region is not a grant award.
- Geometry_confidence must be stored explicitly; 'guessed' is not a valid state.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/planning_region.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/planning_region.schema.json`](../../../schemas/contracts/v1/domains/water_planning/planning_region.schema.json) — Schema
- [`fixtures/domains/water_planning/planning_region/`](../../../fixtures/domains/water_planning/planning_region/) — Fixtures
