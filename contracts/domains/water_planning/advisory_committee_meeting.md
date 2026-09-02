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
updated: 2026-07-30
policy_label: public-with-gates; semantic-contract; water-planning; deferred-epic; PROPOSED
related:
  - ./README.md
  - ./planning_region.md
  - ./public_meeting.md
  - ../../../schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json
  - ../../../fixtures/domains/water_planning/advisory_committee_meeting/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AdvisoryCommitteeMeeting Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json)

Defines the semantic meaning, identity boundary, and fail-closed interpretation of a Kansas Regional Advisory Committee (RAC) meeting record.

> [!IMPORTANT]
> This document and its paired schema are `PROPOSED` scaffolds. They do not prove that a meeting occurred, admit a source, establish a planning decision, authorize policy or promotion, or make a record KFM `PUBLISHED`.

## Quick navigation

- [Meaning](#meaning)
- [Status and authority](#status-and-authority)
- [Contract fields](#contract-fields)
- [Anti-collapse boundaries](#anti-collapse-boundaries)
- [Schema posture](#schema-posture)
- [Synthetic example](#synthetic-example)
- [Validation](#validation)
- [Known limits and verification backlog](#known-limits-and-verification-backlog)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Related](#related)

## Meaning

An `AdvisoryCommitteeMeeting` represents one scheduled Kansas RAC meeting event. At the machine-shape level, every record carries:

- one pattern-constrained `meeting_id`;
- the constant discriminant `meeting_type: advisory_committee_meeting`;
- one `planning_region_ref`;
- a title and start time;
- explicit access and scheduling states; and
- a non-empty `source_ref`.

The required `planning_region_ref` expresses a one-region relationship in the record shape. It does not, by itself, prove that the referenced `PlanningRegion` exists, that the meeting occurred, or that a source supports every recorded field.

The contract describes event meaning. The paired JSON Schema defines accepted document shape. Source admission, evidence resolution, policy decisions, review, release, correction, and publication remain separate responsibilities.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
|---|---|---|
| This document | `draft`; `PROPOSED`; v0.1 | Defines semantic meaning and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not source truth or policy. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/advisory_committee_meeting/) | Synthetic test inputs | Exercise representative schema behavior; they are not meeting evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check representative acceptance and rejection; passing does not prove real-world correctness. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Records source role and limitations; it does not activate a connector or authorize release. |
| `policy/domains/water_planning/` | Forward pointer in schema metadata; policy behavior remains `NEEDS VERIFICATION` | No policy outcome may be inferred from this contract or schema. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
|---|---:|---|---|
| `meeting_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Record identity. Generation, deduplication, and reschedule identity rules remain unspecified. |
| `meeting_type` | Yes | Constant `advisory_committee_meeting` | Prevents collapse into [`PublicMeeting`](./public_meeting.md). |
| `planning_region_ref` | Yes | String matching `^kwo-rac-[0-9]{2}$` | Reference-shaped RAC identity. Existence and exact 01–14 membership require checks beyond this schema. |
| `title` | Yes | Non-empty string | Source-facing meeting label; not proof of occurrence or outcome. |
| `starts_at` | Yes | String annotated as `date-time` | Meeting start as recorded; distinct from source publication time. |
| `ends_at` | No | `date-time` string or `null` | Recorded end time when available. Ordering relative to `starts_at` is not asserted by this schema. |
| `location_description` | No | String or `null` | Human-readable venue description only; it is not governed geometry or a coordinate source. |
| `virtual_access_posture` | Yes | `in_person`, `virtual`, `hybrid`, or `unknown` | Declares the recorded access mode without implying attendance or accessibility compliance. |
| `cancellation_state` | Yes | `scheduled`, `cancelled`, or `rescheduled` | Scheduling state only; it is not a decision, approval, or replacement-record rule. |
| `source_publication_time` | No | `date-time` string or `null` | When the source published the notice, if recorded; distinct from event time and retrieval time. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not, by itself, an `EvidenceBundle`, receipt, proof, or release authorization. |

No additional properties are admitted by the current schema.

[Back to top](#top)

## Anti-collapse boundaries

| Boundary | Required interpretation |
|---|---|
| Advisory committee meeting != public meeting | `meeting_type` is a constant discriminant, and the two event types have separate contracts and schemas. |
| Meeting != decision | Scheduling, convening, attendance, discussion, cancellation, or rescheduling does not establish a planning decision. |
| Meeting != recommendation or award | A meeting record carries no eligibility, recommendation, award, payment, construction, completion, or benefit authority. |
| Region reference != region proof | A shaped `planning_region_ref` does not prove referential integrity, geometry, county membership, or governance jurisdiction. |
| Venue text != geometry | `location_description` must not be promoted into coordinates, a polygon, or inferred project location. |
| Source reference != evidence closure | A non-empty `source_ref` does not prove field-level support, rights clearance, freshness, review, or publication. |
| Schema-valid != true or public-safe | Structural acceptance does not establish occurrence, policy approval, release, or KFM publication. |

These boundaries preserve the domain index rule that a meeting is not an approval, an application is not an award, and an award is not a completed project.

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
|---|---|---|
| Canonical machine-shape file | [`advisory_committee_meeting.schema.json`](../../../schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Required fields | 8 of 11 properties | Optional fields may be absent; nullable fields may explicitly carry `null`. |
| Unknown fields | Rejected by `additionalProperties: false` | Widening the record requires coordinated contract, schema, fixture, and test review. |
| Event discriminator | `meeting_type: advisory_committee_meeting` | A `public_meeting` value is invalid for this schema. |
| Region-reference pattern | `^kwo-rac-[0-9]{2}$` | Shape validation alone does not restrict references to the intended 01–14 inventory. |

The contract and schema must remain synchronized: prose cannot loosen or tighten machine behavior without a coordinated schema change.

[Back to top](#top)

## Synthetic example

The repository fixture below is synthetic and test-only. It must not be cited as evidence that the named meeting, venue, or schedule exists.

```json
{
  "meeting_id": "kwo-rac-01-mtg-2026-08",
  "meeting_type": "advisory_committee_meeting",
  "planning_region_ref": "kwo-rac-01",
  "title": "RAC 1 Southwestern Kansas — August 2026 Meeting",
  "starts_at": "2026-08-15T09:00:00-05:00",
  "ends_at": "2026-08-15T11:00:00-05:00",
  "location_description": "Garden City, KS",
  "virtual_access_posture": "in_person",
  "cancellation_state": "scheduled",
  "source_publication_time": "2026-07-15T00:00:00Z",
  "source_ref": "kwo:rac:01:meeting:2026-08"
}
```

The paired invalid fixture changes `meeting_type` to `public_meeting`; the schema test expects that record to be rejected.

[Back to top](#top)

## Validation

Run the schema suite from the repository root:

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

| Validation surface | What it checks | What success does not prove |
|---|---|---|
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct entity titles, and representative valid/invalid fixtures across the water-planning family | Source accuracy, meeting occurrence, field-level evidence, rights, policy, release, or publication. |
| [`valid_1.json`](../../../fixtures/domains/water_planning/advisory_committee_meeting/valid/valid_1.json) | One representative shape accepted by the paired schema | That the example is real, current, complete, or source-supported. |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/advisory_committee_meeting/invalid/invalid_1.json) | Wrong event discriminant is rejected | Exhaustive negative coverage for identifiers, dates, region references, or temporal ordering. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only, no-network water-planning semantic and registry checks for affected pull requests | Repository authorization, evidence closure, rights clearance, release, deployment, or publication. |

> [!NOTE]
> A green test or workflow result is validation evidence only within the tested boundary. It is not a source receipt, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
|---|---|---|
| `WP-ACM-01` | `NEEDS VERIFICATION` | Reconcile the intended `kwo-rac-01` through `kwo-rac-14` inventory with the current `^kwo-rac-[0-9]{2}$` pattern, which also admits values such as `kwo-rac-00` and `kwo-rac-99`. |
| `WP-ACM-02` | `NEEDS VERIFICATION` | Add or identify deterministic referential-integrity validation from `planning_region_ref` to the governed `PlanningRegion` inventory. |
| `WP-ACM-03` | `NEEDS VERIFICATION` | Decide whether `date-time` format assertions require an explicit format checker; the shared schema runner currently constructs `Draft202012Validator` without one. |
| `WP-ACM-04` | `NEEDS VERIFICATION` | Define and test temporal coherence, including whether `ends_at` must be at or after `starts_at`. |
| `WP-ACM-05` | `NEEDS VERIFICATION` | Define stable identity, deduplication, cancellation, and reschedule lineage rules for `meeting_id`. |
| `WP-ACM-06` | `NEEDS VERIFICATION` | Define how `source_ref` resolves to field-level evidence and how retrieval, correction, and supersession times are retained. |
| `WP-ACM-07` | `NEEDS VERIFICATION` | Establish the water-planning policy surface and its finite outcomes before any public or semi-public projection. |

Until these items are resolved, narrow claims, preserve explicit unknowns, and avoid inferred region membership, geometry, occurrence, or outcome.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- `meeting_type`, required fields, enums, identity patterns, or `additionalProperties`;
- the relationship between `planning_region_ref` and the governed RAC inventory;
- time and cancellation semantics;
- source/evidence reference meaning; and
- any public-safe projection or policy outcome.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, tests, known consumers, and correction lineage within one authorized review boundary. Use [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) or another governed correction surface when applicable; do not silently rewrite a relied-on historical event.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository bytes; it does not erase source history or create publication authority.

[Back to top](#top)

## Related

| Surface | Role |
|---|---|
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`planning_region.md`](./planning_region.md) | Meaning of the referenced `PlanningRegion` entity. |
| [`public_meeting.md`](./public_meeting.md) | Separate public-meeting event contract. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | Domain correction and withdrawal event contract. |
| [`advisory_committee_meeting.schema.json`](../../../schemas/contracts/v1/domains/water_planning/advisory_committee_meeting.schema.json) | Canonical machine shape for this record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic fixtures](../../../fixtures/domains/water_planning/advisory_committee_meeting/) | Representative valid and invalid inputs. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family regression tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, rights, freshness, and admission limitations. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only path-triggered water-planning validation workflow. |

[Back to top](#top)
