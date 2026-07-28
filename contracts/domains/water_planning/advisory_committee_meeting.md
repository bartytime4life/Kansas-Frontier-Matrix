<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-advisory-committee-meeting
title: AdvisoryCommitteeMeeting Contract — Water Planning
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
  - ../../../schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json
  - ../../../fixtures/domains/water_planning/advisory_committee_meeting/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

# AdvisoryCommitteeMeeting Contract — Water Planning

> **Status:** `draft` / PROPOSED semantic contract
> **Schema:** `schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json`
> **Fixtures:** `fixtures/domains/water_planning/advisory_committee_meeting/`

## Meaning

A Kansas Regional Advisory Committee (RAC) meeting event. Each advisory committee meeting is linked to exactly one governed PlanningRegion. An advisory meeting is not a public meeting, a planning decision, an approval, or an award.

## Anti-collapse boundaries

- An advisory meeting is not a public meeting.
- An advisory meeting is not a planning decision.
- A meeting is not an award.

## Schema posture

| Schema fact | Status |
|---|---|
| Schema file | `schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json` |
| Schema status | `PROPOSED` |
| `additionalProperties` | `false` |

## Related

- [`README.md`](./README.md) — Domain contract index
- [`docs/sources/catalog/kansas/kwo.md`](../../../docs/sources/catalog/kansas/kwo.md) — KWO source catalog entry
- [`schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json`](../../../schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json) — Schema
- [`fixtures/domains/water_planning/advisory_committee_meeting/`](../../../fixtures/domains/water_planning/advisory_committee_meeting/) — Fixtures
