<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-recommendation
title: Recommendation Contract — Water Planning
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
  - ../../../schemas/contracts/v1/domains/water_planning/recommendation.schema.json
  - ../../../fixtures/domains/water_planning/recommendation/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# Recommendation Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/recommendation.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/recommendation/`

## Meaning

A grant recommendation produced by the advisory or administrative process. The recommended_amount is distinct from the requested_amount and the awarded_amount. A recommendation is not an award, payment, or project.

## Anti-collapse boundaries

- A recommendation is not an award.
- recommended_amount ≠ requested_amount ≠ awarded_amount.
- A recommendation is not a project or payment.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/recommendation.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/recommendation.schema.json`](../../../schemas/contracts/v1/domains/water_planning/recommendation.schema.json) — Schema
- [`fixtures/domains/water_planning/recommendation/`](../../../fixtures/domains/water_planning/recommendation/) — Fixtures
