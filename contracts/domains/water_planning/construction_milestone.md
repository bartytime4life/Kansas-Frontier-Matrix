<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-construction-milestone
title: ConstructionMilestone Contract — Water Planning
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
  - ../../../schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json
  - ../../../fixtures/domains/water_planning/construction_milestone/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# ConstructionMilestone Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/construction_milestone/`

## Meaning

A construction progress milestone for a water infrastructure Project. A milestone is not a completion event, an award, or an operational benefit claim.

## Anti-collapse boundaries

- A milestone is not a completion.
- A milestone is not an award.
- No operational benefit may be inferred from a milestone alone.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json`](../../../schemas/contracts/v1/domains/water_planning/construction_milestone.schema.json) — Schema
- [`fixtures/domains/water_planning/construction_milestone/`](../../../fixtures/domains/water_planning/construction_milestone/) — Fixtures
