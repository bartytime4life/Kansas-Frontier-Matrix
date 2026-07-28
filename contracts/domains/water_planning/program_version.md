<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-program-version
title: ProgramVersion Contract — Water Planning
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
  - ../../../schemas/contracts/v1/domains/water_planning/program_version.schema.json
  - ../../../fixtures/domains/water_planning/program_version/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# ProgramVersion Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/program_version.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/program_version/`

## Meaning

A versioned instance of a Kansas water-infrastructure grant program. Each statutory or policy change (such as 2026 HB 2462) that alters eligibility, scoring, or administration creates a new ProgramVersion. Prior history must not be overwritten. A ProgramVersion is not a scoring matrix, application, or award.

## Anti-collapse boundaries

- A program version is not a scoring matrix.
- A program version is not an application or award.
- HB 2462 creates a new version; it does not overwrite prior history.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/program_version.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/program_version.schema.json`](../../../schemas/contracts/v1/domains/water_planning/program_version.schema.json) — Schema
- [`fixtures/domains/water_planning/program_version/`](../../../fixtures/domains/water_planning/program_version/) — Fixtures
