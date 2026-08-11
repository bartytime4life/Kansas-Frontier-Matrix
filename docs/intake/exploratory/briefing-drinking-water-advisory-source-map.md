<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/briefing-drinking-water-advisory
title: Briefing Drinking-Water Advisory Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; PROPOSED adaptation; non-authoritative; not-for-life-safety
owners: ["@bartytime4life"]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; hazards; drinking-water; no-public-authority
owning_root: docs/
responsibility: Reconcile the connected architecture's drinking-water issue/rescission backlog against existing shared advisory and source-absence mechanics.
truth_posture: "CONFIRMED source and repository inspection; PROPOSED inactive Hazards profile; NEEDS VERIFICATION authority review and hosted exact-head CI"
related:
  - ../../../contracts/domains/hazards/drinking_water_advisory.md
  - ../../../contracts/common/advisory_event_envelope.md
  - ../../../contracts/source/source_adapter.md
  - ../../../contracts/source/source_record_absence_assessment.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, exploratory, hazards, drinking-water, advisory, rescission, service-area, false-clear]
[/KFM_META_BLOCK_V2] -->

# Briefing Drinking-Water Advisory Source Map

## Goal

Implement the smallest dependency-closed drinking-water issue/rescission
profile from the connected Briefing-to-System Integration Architecture without
claiming a live source, current public-health status, or public alert authority.

## Connected-source requirement

The source architecture's Lane B backlog calls for a drinking-water advisory
profile that preserves:

- public water system identity;
- advisory cause;
- issue and rescission authority;
- service-area scope in preference to city boundary; and
- authoritative rescission before clearing a volatile event.

Its negative expectations state that a missing rescission must remain
`STATUS_UNCONFIRMED` and a retrieval failure must never false-clear an event.
The connected source is design input. Private locator and connector metadata are
not copied into this repository artifact.

## Current repository inspection

Inspection base:

```text
main@463381703bcd6eada8eea05e95c4a88912ed4b02
```

CONFIRMED at that base:

- `AdvisoryEventEnvelope` owns shared volatile-event identity, status, scope,
  lineage, and false-clear mechanics, but its first machine profile is
  intentionally HAB-specific.
- `SourceAdapter` says `NOT_FOUND` and failed checks preserve uncertainty and
  never infer rescission.
- `SourceRecordAbsenceAssessment` prevents a missing row from becoming an
  unsupported clear, deletion, or rescission.
- the Hazards lane is registered and already owns drought and HAB advisory
  semantics.
- repository and GitHub searches found no drinking-water advisory contract,
  schema, validator, fixture packet, matching branch, or open pull request.

## Reconciliation decision

The smallest non-duplicative packet is:

```text
source requirement
  -> inactive Hazards domain payload
  -> explicit AdvisoryEventEnvelope semantic crosswalk
  -> closed schema and exact synthetic cases
  -> deterministic no-network validator
  -> domain tests and read-only path-scoped workflow
  -> byte-bound generated receipt
```

The packet does not broaden the current HAB-specific common schema. A future
common-schema multi-profile decision can be reviewed separately after more than
one domain profile exists.

## Hard boundaries

1. Only a confirmed rescission authority plus notice, time, and lineage can
   clear a prior advisory.
2. Expiry, row absence, `NOT_FOUND`, access denial, rate limiting, malformed
   content, or a failed status check cannot produce `RESCINDED`.
3. A city or administrative boundary remains context and cannot impersonate a
   public water system service area.
4. Identity conflict cannot borrow a guessed system or scope.
5. Passing fixtures remain unreleased, non-public, non-alerting, and
   not-for-life-safety.

## Directory Rules basis

| Artifact | Owning responsibility root | Placement result |
|---|---|---|
| Domain meaning | `contracts/domains/hazards/` | `PLACE` |
| Closed shape | `schemas/contracts/v1/domains/hazards/` | `PLACE` |
| Synthetic cases | `fixtures/domains/hazards/` | `PLACE` |
| Domain validator | `tools/validators/domains/hazards/` | `PLACE` |
| Domain conformance | `tests/domains/hazards/` | `PLACE` |
| Source reconciliation | `docs/intake/exploratory/` | `PLACE` |
| CI orchestration | `.github/workflows/` | `PLACE` |
| Authoring provenance | `data/receipts/generated/` | `PLACE` |

Applicable rules include `DIR-SIGNATURE-001`, `DIR-PLACE-001`,
`DIR-PLACE-005`, `DIR-AUTHROOT-001`, `DIR-SCOPELANE-003`,
`DIR-SCOPELANE-004`, and `DIR-DEP-001`. No parallel common contract, policy,
source, lifecycle, release, proof, catalog, or public authority is created.

## Validation boundary

The packet can prove closed local shape; finite source/status mapping; required
public-water-system identity; confirmed issue/rescission roles; service-area
anti-collapse; temporal order; only-authoritative-rescission clearing;
deterministic identity; exact fixture polarity; and all-false authority effects.

It cannot prove a real advisory exists, is current, is complete, applies to an
address, has enforceable source terms, is clinically or legally sufficient, or
is safe to release. Live source admission, evidence closure, policy, health and
authority review, public-safe transformation, release, and correction remain
separate work.

## Rollback

Before merge, close the draft and abandon the branch. After an authorized
merge, revert the additive packet. No source, advisory, alert, lifecycle,
release, deployment, cache, or public-state restoration is required.
