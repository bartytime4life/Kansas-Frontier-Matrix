<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-award
title: Award Contract — Water Planning
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
  - ../../../schemas/contracts/v1/domains/water_planning/award.schema.json
  - ../../../fixtures/domains/water_planning/award/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# Award Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/award.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/award/`

## Meaning

A grant award event. The awarded_amount is distinct from the requested_amount, the recommended_amount, and the paid_amount. An award is not a payment, a completed project, or an operational benefit.

## Anti-collapse boundaries

- An award is not a payment.
- An award is not a completed project.
- awarded_amount ≠ requested_amount ≠ recommended_amount ≠ paid_amount.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/award.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/award.schema.json`](../../../schemas/contracts/v1/domains/water_planning/award.schema.json) — Schema
- [`fixtures/domains/water_planning/award/`](../../../fixtures/domains/water_planning/award/) — Fixtures
