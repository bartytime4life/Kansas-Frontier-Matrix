<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/briefing-governance-event-source-map
title: Briefing GovernanceEvent Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; PROPOSED adaptation; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; governance; no-authority
owning_root: docs/
responsibility: Record the bounded adaptation from the briefing governance lane into an inactive GovernanceEvent profile and preserve the next dependency-ordered queue.
truth_posture: "CONFIRMED current repository overlap check; PROPOSED adaptation; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/governance/governance_event.md
  - ../../../contracts/governance/briefing_signal.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, exploratory, briefing, governance, participation]
[/KFM_META_BLOCK_V2] -->

# Briefing GovernanceEvent Source Map

## Source requirement

The briefing governance lane names an umbrella `GovernanceEvent` plus
`MeetingSession`, `AgendaItem`, `CommentWindow`, `Submission`,
`Recommendation`, `Decision`, `DecisionImplementation`, and
`ParticipationReceipt`. Its controlling requirement is state separation:
announcement is not attendance, attendance is not recommendation,
recommendation is not decision, decision is not implementation, and
implementation is not measured outcome.

## Repository reconciliation

CONFIRMED against the implementation base:

- `BriefingSignal` and common temporal envelopes already exist;
- the governance responsibility roots already exist;
- ADR-0029 accepts Directory Governance Standard v2;
- bounded searches found no existing `governance_event` contract, schema,
  validator, fixture packet, or open pull request for the exact family.

## Adaptation

The smallest coherent implementation is the umbrella event carrier with
explicit linked-stage references, deterministic identity, finite event and
source-lineage states, no-network fixtures, and authority non-effects. It does
not implement the related families in the same review boundary.

## Next sourced ideas

1. `CommentWindow` and `Submission` profiles with privacy/publication posture.
2. `Recommendation` and `Decision` profiles proving advisory versus binding
   authority.
3. `DecisionImplementation` and `OutcomeObservation` chain integrity.
4. Governance role-crosswalk tests showing that event state, recommendation,
   decision, implementation, and outcome cannot substitute for each other.
5. A public participation explorer only after released, public-safe
   projections, correction, and rollback controls exist.

## Deliberate holds

No live calendar, source activation, comment intake, identity disclosure,
decision authority, release, API, map, search, notification, or public product
is introduced.

## Rollback

Discard the branch before merge or revert the additive packet afterward. No
live or public state is affected.
