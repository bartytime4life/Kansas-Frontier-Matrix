<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/hazards/drinking-water-advisory/v1
title: DrinkingWaterAdvisory Contract — Hazards
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-only; not-for-life-safety
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Drinking-water authority steward
  - OWNER_TBD — Contracts and validation stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; hazards; drinking-water; volatile-advisory; false-clear-denial; no-public-authority
owning_root: contracts/
responsibility: Preserve public-water-system identity, issue and rescission authority, service-area scope, volatile source status, and false-clear denial for a synthetic drinking-water advisory profile.
truth_posture: "CONFIRMED repository mechanics and connected-source requirement; PROPOSED inactive domain profile; NEEDS VERIFICATION authority steward review and future source admission"
related:
  - ./README.md
  - ../../common/advisory_event_envelope.md
  - ../../source/source_adapter.md
  - ../../source/source_record_absence_assessment.md
  - ../../../schemas/contracts/v1/domains/hazards/drinking_water_advisory.schema.json
  - ../../../fixtures/domains/hazards/drinking_water_advisory/
  - ../../../tools/validators/domains/hazards/validate_drinking_water_advisory.py
  - ../../../tests/domains/hazards/test_drinking_water_advisory.py
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, hazards, drinking-water, advisory, rescission, authority, service-area, source-absence, fixture-only, no-network]
notes:
  - "Adapts the connected Briefing-to-System Integration Architecture drinking-water backlog item without activating a source or publishing current health guidance."
  - "Reuses AdvisoryEventEnvelope mechanics through an explicit crosswalk; the current HAB-specific common schema is not silently broadened."
[/KFM_META_BLOCK_V2] -->

# DrinkingWaterAdvisory Contract — Hazards

## Purpose

`DrinkingWaterAdvisory` is an inactive Hazards-domain profile for one volatile
public drinking-water advisory record. It keeps five authority-bearing concepts
separate:

1. public water system identity;
2. advisory cause and issue notice;
3. issuing authority;
4. service-area scope; and
5. authoritative rescission evidence.

The profile is synthetic and fixture-only. It is not a current advisory feed,
health determination, public warning, or authorization to issue guidance.

## Status and authority boundary

| Field | Value |
|---|---|
| Profile | `kfm.hazards.drinking-water-advisory.v1` |
| Adoption | `PROPOSED_INACTIVE` |
| Execution | Deterministic, fixture-only, no-network |
| Common mechanics | Crosswalk to `contracts/common/advisory_event_envelope.md` |
| Source access | None |
| Public use / alerts | Fixed false |
| Release | Fixed `UNRELEASED`; release reference fixed null |
| Lifecycle, policy, review, deployment, or publication effects | Fixed false |

A validator `PASS` proves only local schema, identity, crosswalk, temporal,
authority, scope, and false-clear coherence. It does not prove a real advisory
exists, is current, applies to a person or address, or is safe to publish.

## Shared AdvisoryEventEnvelope crosswalk

The common `AdvisoryEventEnvelope` owns shared volatile-event mechanics. Its
current machine profile is deliberately HAB-specific, so this packet references
the common semantic contract and records an explicit domain projection instead
of adding drinking-water-native fields to the common schema.

| Drinking-water field | Shared mechanic |
|---|---|
| `shared_mechanics.event_family = DRINKING_WATER` | volatile event family |
| `shared_mechanics.basis = REGULATORY_ADVISORY` | advisory source role |
| `advisory.normalized_status` | finite advisory status |
| `source_surface.source_check_outcome` | retrieval/currentness posture |
| `scope.scope_role` | advisory area, administrative context, or unresolved |
| `advisory.rescinded_at` and `controls.rescission_notice_ref` | authoritative rescission |
| `controls.prior_advisory_ref` | prior lineage |

This crosswalk is compatibility metadata only. It does not claim that the
current HAB-specific common JSON schema validates this domain payload.

## Required semantics

### Public water system identity

A resolved advisory state requires a resolved `public_water_system_ref` plus a
source-native public-water-system identifier. Identity conflict or unresolved
identity cannot borrow a city, county, utility name, or geometry as a guessed
system identity.

### Issue and rescission authority

Every record names an issuing authority and issue notice. `RESCINDED` additionally
requires:

- a rescission time;
- a rescission notice reference;
- an explicitly confirmed rescission authority;
- prior-advisory lineage; and
- `clears_prior_advisory: true`.

The issuing and rescinding authorities are modeled separately because a
governed source may permit distinct authorities. The validator requires both
roles to be explicit; it does not invent equivalence.

### Service area before municipal boundary

Confirmed issued, active, updated, or rescinded status requires
`scope_role: SERVICE_AREA` and an explicit service-area reference. A municipal
or other administrative boundary may appear only as
`ADMINISTRATIVE_CONTEXT`; it cannot be relabeled as the served population or
advisory area. Unresolved service area remains `UNRESOLVED`.

### Source failure and record absence

`NOT_FOUND`, `ACCESS_DENIED`, `RATE_LIMITED`, `MALFORMED`, and
`STATUS_CHECK_FAILED` cannot clear a previously active advisory. A missing row
from a complete snapshot is also not rescission evidence. Those states require
`STATUS_UNCONFIRMED`, retain the last confirmed status, and keep
`clears_prior_advisory` false unless an authoritative rescission notice is
present and independently validated.

An expiry timestamp is not a rescission. The source-specific authority remains
controlling, and expired-but-unrescinded status must not be silently normalized
to `RESCINDED`.

## Finite validation outcomes

- `PASS` — bounded fixture coherence only;
- `DENY` — schema-valid overclaim, false clear, authority, identity, scope,
  temporal, or source-state violation;
- `ERROR` — unsafe input, invalid JSON, unavailable schema/hashing, or identity
  mismatch.

Diagnostics contain stable code/path pairs and never echo advisory values.

## Directory Rules basis

ADR-0029 adopts Directory Governance Standard v2. Domain meaning belongs under
`contracts/domains/hazards/`; its closed shape under
`schemas/contracts/v1/domains/hazards/`; synthetic cases under
`fixtures/domains/hazards/`; repository enforcement under
`tools/validators/domains/hazards/`; domain proof under
`tests/domains/hazards/`; source reconciliation under
`docs/intake/exploratory/`; orchestration under `.github/workflows/`; and
authoring provenance under `data/receipts/generated/`.

The responsibility signature is one Hazards-domain semantic contract, no
lifecycle stage, repository-tool execution, internal exposure, and versioned
Git retention. No new root, domain, common-envelope authority, source registry,
policy home, release object, or public surface is created.

## Non-effects

This profile does not fetch a regulator or utility source; admit or activate a
source; evaluate currentness, evidence, rights, policy, health, or review;
create a public alert, map, API, dashboard, recommendation, or AI answer; write
lifecycle state; promote; release; deploy; publish; or authorize public use.

## Rollback

Before merge, close the draft and abandon its branch. After an authorized
merge, revert this additive packet. It creates no external source, advisory,
alert, lifecycle, cache, release, deployment, or public state to restore.
