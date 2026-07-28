<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-application-window
title: ApplicationWindow Contract — Water Planning
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
  - ../../../schemas/contracts/v1/domains/water_planning/application_window.schema.json
  - ../../../fixtures/domains/water_planning/application_window/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# ApplicationWindow Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/application_window.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/application_window/`

## Meaning

The open-to-close window for a grant application cycle. The closes_at field must include a UTC offset and the source_timezone (IANA name) must be stored explicitly. The FY2027 SWIGP window closes at 2026-09-15T23:59:00-05:00 (America/Chicago). An application window is not an application, recommendation, or award.

## Anti-collapse boundaries

- An application window is not an application.
- The FY2027 deadline must be stored with explicit Central Time handling.
- source_timezone is required and must be the IANA timezone name.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/application_window.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/application_window.schema.json`](../../../schemas/contracts/v1/domains/water_planning/application_window.schema.json) — Schema
- [`fixtures/domains/water_planning/application_window/`](../../../fixtures/domains/water_planning/application_window/) — Fixtures
