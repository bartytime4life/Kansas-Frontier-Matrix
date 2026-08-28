<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-water-planning-public-meeting
title: PublicMeeting Contract — Water Planning
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
  - ./advisory_committee_meeting.md
  - ./correction_or_withdrawal.md
  - ../../../schemas/contracts/v1/domains/water_planning/public_meeting.schema.json
  - ../../../fixtures/domains/water_planning/public_meeting/
  - ../../../docs/sources/catalog/kansas/kwo.md
  - ../../../tests/schemas/test_water_planning_contracts.py
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PublicMeeting Contract — Water Planning

[![Contract status: PROPOSED](https://img.shields.io/badge/contract-PROPOSED-d29922?style=flat-square)](#status-and-authority)
[![Schema: Draft 2020-12](https://img.shields.io/badge/schema-Draft%202020--12-0969da?style=flat-square)](../../../schemas/contracts/v1/domains/water_planning/public_meeting.schema.json)

Defines the semantic meaning, event boundary, and fail-closed interpretation of a Kansas Water Office public-meeting record.

> [!IMPORTANT]
> This document and its paired schema are `PROPOSED` scaffolds. They do not prove that a meeting was announced or occurred, admit a source, establish attendance or public access, create a planning decision, authorize policy or promotion, or make a record KFM `PUBLISHED`.

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

A `PublicMeeting` represents one scheduled Kansas Water Office public-meeting event record. At the machine-shape level, every record carries:

- one pattern-constrained `meeting_id`;
- the constant discriminant `meeting_type: public_meeting`;
- a non-empty title and a start-time string;
- explicit access and scheduling states; and
- a non-empty `source_ref`.

The record may also carry an end time, a human-readable location, and a source-publication time. Optional fields may be absent; the current nullable fields may explicitly carry `null`.

This contract describes event meaning. The paired JSON Schema defines accepted document shape. Source admission, field-level evidence, identity resolution, rights and sensitivity decisions, policy, review, release, correction, and publication remain separate responsibilities.

Unlike [`AdvisoryCommitteeMeeting`](./advisory_committee_meeting.md), the current `PublicMeeting` shape has no `planning_region_ref`. A title, venue, or source reference must not be used to infer RAC membership, governed region identity, or geometry.

[Back to top](#top)

## Status and authority

| Surface | Current posture | Authority boundary |
|---|---|---|
| This document | `draft`; `PROPOSED`; v0.1 | Defines semantic meaning and anti-collapse rules. |
| [Paired JSON Schema](../../../schemas/contracts/v1/domains/water_planning/public_meeting.schema.json) | Draft 2020-12; `x-kfm.status: PROPOSED` | Defines machine-checkable shape, not source truth or policy. |
| [Valid and invalid fixtures](../../../fixtures/domains/water_planning/public_meeting/) | Synthetic test inputs | Exercise representative schema behavior; they are not meeting evidence. |
| [Schema tests](../../../tests/schemas/test_water_planning_contracts.py) | Repository test surface | Check representative acceptance and rejection; passing does not prove real-world correctness. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Bounded source-family documentation | Records source role and limitations; it does not activate a connector or authorize release. |
| `policy/domains/water_planning/` | Schema metadata forward pointer; no such path exists at the inspected base | No policy outcome may be inferred from this contract or schema. |

Directory placement follows the adopted responsibility-root split: `contracts/` owns semantic meaning, `schemas/` owns machine shape, and `policy/` owns governed decision rules. The [`water_planning` segment](./README.md) is a domain lane inside the contract authority root, not a separate authority.

[Back to top](#top)

## Contract fields

| Field | Required | Schema constraint | Semantic interpretation |
|---|---:|---|---|
| `meeting_id` | Yes | String matching `^[a-z][a-z0-9_:.-]*$` | Record identity. Generation, deduplication, and reschedule-lineage rules remain unspecified. |
| `meeting_type` | Yes | Constant `public_meeting` | Prevents shape-level collapse into [`AdvisoryCommitteeMeeting`](./advisory_committee_meeting.md). |
| `title` | Yes | Non-empty string | Source-facing meeting label; not proof of announcement, occurrence, sponsorship, or outcome. |
| `starts_at` | Yes | String annotated as `date-time` | Intended meeting start as recorded; distinct from source publication time. |
| `ends_at` | No | `date-time` string or `null` | Recorded end time when available. Ordering relative to `starts_at` is not asserted by this schema. |
| `location_description` | No | String or `null` | Human-readable venue description only; it is not governed geometry or a project-location source. |
| `virtual_access_posture` | Yes | `in_person`, `virtual`, `hybrid`, or `unknown` | Recorded participation mode; it does not prove attendance, availability, or accessibility compliance. |
| `cancellation_state` | Yes | `scheduled`, `cancelled`, or `rescheduled` | Scheduling state only; it does not encode a replacement event or decision. |
| `source_publication_time` | No | `date-time` string or `null` | When the source published the notice, if recorded; distinct from event time and retrieval time. |
| `source_ref` | Yes | Non-empty string | Traceability pointer. It is not, by itself, an `EvidenceBundle`, receipt, proof, or release authorization. |

No additional properties are admitted by the current schema.

[Back to top](#top)

## Anti-collapse boundaries

| Boundary | Required interpretation |
|---|---|
| Public meeting != advisory committee meeting | The event types have separate contracts and constant discriminants; the public-meeting shape carries no RAC reference. |
| Meeting record != occurrence | A scheduled notice, title, or source pointer does not prove that the meeting convened. |
| Meeting != decision or recommendation | Scheduling, attendance, discussion, cancellation, or rescheduling does not establish a planning decision, eligibility result, recommendation, approval, or award. |
| Meeting != delivery outcome | This record carries no payment, construction, completion, or operational-benefit authority. |
| Cancellation or reschedule != new meeting | A state change does not, by itself, define replacement identity or lineage. |
| Venue text != geometry | `location_description` must not be promoted into coordinates, a polygon, a planning region, or inferred project location. |
| Access posture != participation proof | `virtual`, `hybrid`, or `in_person` describes the recorded mode only; it does not prove that access worked or that anyone attended. |
| Source publication time != event or retrieval time | These temporal facts must remain distinct and must not be substituted for one another. |
| Source reference != evidence closure | A non-empty `source_ref` does not prove field-level support, rights clearance, freshness, review, or publication. |
| Schema-valid != true or public-safe | Structural acceptance does not establish occurrence, policy approval, release, or KFM publication. |

These boundaries preserve the domain rule that a meeting is not an approval, an application is not an award, and an award is not a completed project.

[Back to top](#top)

## Schema posture

| Schema fact | Current value | Consequence |
|---|---|---|
| Canonical machine-shape file | [`public_meeting.schema.json`](../../../schemas/contracts/v1/domains/water_planning/public_meeting.schema.json) | Change machine constraints in the schema, not by prose alone. |
| JSON Schema dialect | Draft 2020-12 | Consumers must use compatible tooling. |
| Schema status | `PROPOSED` | No stable, released, or published maturity is claimed. |
| Required fields | 7 of 10 properties | Optional fields may be absent; nullable fields may explicitly carry `null`. |
| Unknown fields | Rejected by `additionalProperties: false` | Widening the record requires coordinated contract, schema, fixture, and test review. |
| Event discriminator | `meeting_type: public_meeting` | An `advisory_committee_meeting` value is invalid for this schema. |
| Date-time validation | `format: date-time` annotations are present | The currently wired validator supplies no format checker, so these annotations and the described UTC-offset requirement are not enforced by that runner. |
| Cross-field validation | None | The schema does not require `ends_at >= starts_at` or constrain states by time. |
| Referential validation | None | `source_ref` is checked only as a non-empty string; no evidence or registry target is resolved. |

The contract and schema must remain synchronized: prose cannot loosen or tighten machine behavior without a coordinated schema change.

[Back to top](#top)

## Synthetic example

The repository fixture below is synthetic and test-only. It must not be cited as evidence that the named meeting, venue, schedule, or source record exists.

```json
{
  "meeting_id": "kwo-pm-2026-09-01",
  "meeting_type": "public_meeting",
  "title": "FY2027 State Water Plan Public Meeting — Topeka",
  "starts_at": "2026-09-01T10:00:00-05:00",
  "ends_at": "2026-09-01T12:00:00-05:00",
  "location_description": "Topeka, KS — KDWPT Conference Room",
  "virtual_access_posture": "hybrid",
  "cancellation_state": "scheduled",
  "source_publication_time": "2026-08-01T00:00:00Z",
  "source_ref": "kwo:events:2026-public-meeting-01"
}
```

The paired invalid fixture adds an undeclared `unexpected_field`; `additionalProperties: false` requires that record to be rejected.

[Back to top](#top)

## Validation

Run the schema suite from the repository root:

```bash
python -m pytest -q tests/schemas/test_water_planning_contracts.py
```

| Validation surface | What it checks | What success does not prove |
|---|---|---|
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema presence, distinct entity titles, and representative valid/invalid fixtures across the 15 water-planning entities | Source accuracy, meeting occurrence, date-time correctness, field-level evidence, rights, policy, release, or publication. |
| [`valid_1.json`](../../../fixtures/domains/water_planning/public_meeting/valid/valid_1.json) | One representative shape accepted by the paired schema | That the example is real, current, complete, or source-supported. |
| [`invalid_1.json`](../../../fixtures/domains/water_planning/public_meeting/invalid/invalid_1.json) | An undeclared property is rejected | Exhaustive negative coverage for identifiers, discriminants, enums, dates, time ordering, or lineage. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Triggers on this contract path and runs no-network water-planning domain tests plus the RAC registry validator | Validation of this schema fixture pair: the workflow does not currently invoke the schema pytest suite. |

> [!NOTE]
> A green test or workflow result is validation evidence only within the tested boundary. It is not a source receipt, policy decision, review record, release manifest, or publication proof.

[Back to top](#top)

## Known limits and verification backlog

| ID | Status | Verification item |
|---|---|---|
| `WP-PM-01` | `NEEDS VERIFICATION` | Decide whether `date-time` and explicit UTC-offset requirements must be enforced with a format checker or stronger schema constraint. |
| `WP-PM-02` | `NEEDS VERIFICATION` | Define temporal coherence, including whether `ends_at` must be at or after `starts_at`. |
| `WP-PM-03` | `NEEDS VERIFICATION` | Define stable identity, deduplication, cancellation, reschedule, and replacement-lineage rules for `meeting_id`. |
| `WP-PM-04` | `NEEDS VERIFICATION` | Define how `source_ref` resolves to field-level evidence and how retrieval, correction, and supersession times are retained. |
| `WP-PM-05` | `NEEDS VERIFICATION` | Establish the absent water-planning policy surface and its finite outcomes before any public or semi-public projection. |
| `WP-PM-06` | `NEEDS VERIFICATION` | Define governed region or geometry associations, if needed, without inferring them from title, venue, access mode, or source text. |
| `WP-PM-07` | `NEEDS VERIFICATION` | Add targeted negative tests for the event discriminator, identifier pattern, blank strings, enums, malformed dates, temporal order, and reschedule lineage. |
| `WP-PM-08` | `NEEDS VERIFICATION` | Decide how a public meeting is classified when a RAC, KWA, grant program, or other body convenes it, without collapsing event type into organizer or outcome. |

Until these items are resolved, narrow claims and preserve explicit unknowns. Do not infer occurrence, participation, accessibility, planning-region membership, geometry, decision, or outcome.

[Back to top](#top)

## Compatibility, correction, and rollback

Treat changes to the following as compatibility-significant:

- `meeting_type`, required fields, enums, identity patterns, or `additionalProperties`;
- start/end-time and source-publication semantics;
- cancellation, reschedule, replacement, and identity-lineage behavior;
- source/evidence reference meaning;
- public-meeting versus advisory-committee classification; and
- any public-safe projection or policy outcome.

A material semantic or shape change should update this contract, the paired schema, representative valid and invalid fixtures, tests, known consumers, and correction lineage within one authorized review boundary. Use [`CorrectionOrWithdrawal`](./correction_or_withdrawal.md) or another governed correction surface when applicable; do not silently rewrite a relied-on historical event.

Before merge, rollback is to close the draft pull request and abandon its scoped branch. After merge, use a focused revert or corrective pull request against the actual merged commit. A revert changes repository bytes; it does not erase source history or create publication authority.

[Back to top](#top)

## Related

| Surface | Role |
|---|---|
| [`README.md`](./README.md) | Water-planning semantic-contract index and cross-entity anti-collapse boundaries. |
| [`advisory_committee_meeting.md`](./advisory_committee_meeting.md) | Separate RAC advisory-meeting event contract. |
| [`correction_or_withdrawal.md`](./correction_or_withdrawal.md) | Domain correction and withdrawal event contract. |
| [`public_meeting.schema.json`](../../../schemas/contracts/v1/domains/water_planning/public_meeting.schema.json) | Canonical machine shape for this record. |
| [Water-planning schema index](../../../schemas/contracts/v1/domains/water_planning/README.md) | Schema-family scope, invariants, validation, and public-safe boundary. |
| [Synthetic fixtures](../../../fixtures/domains/water_planning/public_meeting/) | Representative valid and invalid inputs. |
| [`test_water_planning_contracts.py`](../../../tests/schemas/test_water_planning_contracts.py) | Schema-family regression tests. |
| [KWO source catalog entry](../../../docs/sources/catalog/kansas/kwo.md) | Source role, rights, freshness, and admission limitations. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted responsibility-root and domain-lane placement authority. |
| [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption record for Directory Rules v2. |
| [`briefing-integration.yml`](../../../.github/workflows/briefing-integration.yml) | Read-only path-triggered water-planning validation workflow. |

[Back to top](#top)
