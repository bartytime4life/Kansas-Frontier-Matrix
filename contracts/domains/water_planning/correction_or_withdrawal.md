<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-correction-or-withdrawal
title: CorrectionOrWithdrawal Contract — Water Planning
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
  - ../../../schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json
  - ../../../fixtures/domains/water_planning/correction_or_withdrawal/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# CorrectionOrWithdrawal Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/correction_or_withdrawal/`

## Meaning

A correction or withdrawal record for any water-planning entity. Prior state is preserved via optional digest linkage. A correction does not constitute a new award, decision, or project record.

## Anti-collapse boundaries

- A correction is not a new award.
- A correction is not a new project.
- Prior digest linkage preserves historical lineage.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json`](../../../schemas/contracts/v1/domains/water_planning/correction_or_withdrawal.schema.json) — Schema
- [`fixtures/domains/water_planning/correction_or_withdrawal/`](../../../fixtures/domains/water_planning/correction_or_withdrawal/) — Fixtures
