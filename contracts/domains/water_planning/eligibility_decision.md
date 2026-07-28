<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-eligibility-decision
title: EligibilityDecision Contract — Water Planning
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
  - ../../../schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json
  - ../../../fixtures/domains/water_planning/eligibility_decision/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# EligibilityDecision Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/eligibility_decision/`

## Meaning

A governed eligibility determination for a grant application. Outcome must be one of eligible, ineligible, or pending. An eligibility decision is not a recommendation, award, or project approval.

## Anti-collapse boundaries

- An eligibility decision is not a recommendation.
- An eligibility decision is not an award.
- Outcome is finite: eligible, ineligible, or pending.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json`](../../../schemas/contracts/v1/domains/water_planning/eligibility_decision.schema.json) — Schema
- [`fixtures/domains/water_planning/eligibility_decision/`](../../../fixtures/domains/water_planning/eligibility_decision/) — Fixtures
