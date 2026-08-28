<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/governance-event/v1
title: GovernanceEvent Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-only
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; no-public-authority
owning_root: contracts/
responsibility: Define a meeting/hearing/workshop/consultation/rulemaking event without collapsing announcement, attendance, recommendation, decision, implementation, or outcome into one state.
truth_posture: "CONFIRMED source/repository boundary; PROPOSED candidate semantics; NEEDS VERIFICATION governance-steward review and operational adoption"
related:
  - ../../schemas/contracts/v1/governance/governance_event.schema.json
  - ../../fixtures/contracts/v1/governance/governance_event/
  - ../../tools/validators/validate_governance_event.py
  - ../../tests/validators/test_validate_governance_event.py
  - ./briefing_signal.md
  - ../../contracts/common/temporal_authority_envelope.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, meeting, participation, recommendation, decision, implementation, outcome, fixture-only, no-network]
notes:
  - "Implements the GovernanceEvent umbrella object named by the briefing-to-system governance lane."
  - "Downstream recommendation, decision, implementation, and outcome objects remain references to separate families."
[/KFM_META_BLOCK_V2] -->

# GovernanceEvent

## Purpose

`GovernanceEvent` is a release-neutral identity for a meeting, hearing,
workshop, consultation, or rulemaking session. It may describe that an event was
announced, scheduled, held, or cancelled. It may link to later public-input,
recommendation, decision, implementation, and outcome objects, but it does not
turn those stages into one mutable progress record.

## Anti-collapse spine

| Object or state | Must not imply |
|---|---|
| Event announcement | That the event was held |
| Held event | Recommendation, decision, funding, or implementation |
| Agenda item | That the topic was discussed or adopted |
| Comment window | That a submission was accepted or acted upon |
| Submission | Endorsement or decision |
| Recommendation | Binding adoption or implementation |
| Decision | Execution or completion |
| Decision implementation | Measured outcome |
| Participation receipt | Policy approval or truth |

This first slice implements the `GovernanceEvent` carrier only. Related object
families remain explicit references.

## Status and authority boundary

| Field | Value |
|---|---|
| Profile | `kfm.governance.governance-event.v1` |
| Adoption | `PROPOSED_INACTIVE` |
| Execution | Fixture-only, deterministic, no-network |
| Schema | `schemas/contracts/v1/governance/governance_event.schema.json` |
| Validator | `tools/validators/validate_governance_event.py` |
| Calendar or source access | None |
| Release state | Semantically fixed to `UNRELEASED` |
| Public use | Semantically fixed to `false` |
| Lifecycle writes | None |

## Event state

Finite event states are:

- `ANNOUNCED`;
- `SCHEDULED`;
- `HELD`;
- `CANCELLED`.

A held event requires an explicit held time and at least one
`ParticipationReceipt` reference. A cancelled event requires a cancellation
time and cannot carry a held time or participation receipt. Scheduled times,
retrieval time, correction time, and supersession time remain distinct.

## Linked stages

The contract has separate reference arrays for:

- agenda and materials;
- comment windows and submissions;
- recommendations;
- decisions;
- decision implementations;
- outcome observations;
- participation receipts.

An implementation reference requires a decision reference. An outcome
observation reference requires an implementation reference. The validator does
not infer a recommendation, decision, implementation, or measured outcome from
the presence or state of the event itself.

## Geometry and conflict

Resolved geometry requires a geography reference and digest. Unresolved
geometry cannot carry resolved coordinates or confidence. A conflicted event
requires at least two conflict references and unresolved-safe geometry.

## Identity and lineage

`spec_hash` uses the repository RFC 8785 JCS plus SHA-256 package.
`governance_event_id` is content-derived. Finite source-lineage states are
`CURRENT`, `CORRECTED`, `SUPERSEDED`, and `CONFLICTED`; they do not substitute
for KFM lifecycle or release state.

## Finite outcomes

- `PASS` — bounded candidate accepted;
- `DENY` — semantic or authority boundary violated;
- `ERROR` — unsafe input, unavailable dependency, or identity corruption.

Diagnostics expose stable code/path pairs without source values.

## Authority non-effects

All source, evidence, policy, promotion, release, and publication effects remain
false. The profile never issues a decision, approves a recommendation, creates
a participation result, or authorizes public use.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. Meaning lives under
`contracts/governance/`; machine shape under
`schemas/contracts/v1/governance/`; fixtures under
`fixtures/contracts/v1/governance/`; executable validation under
`tools/validators/`; behavior under `tests/validators/`; read-only CI under
`.github/workflows/`; exploratory adaptation under
`docs/intake/exploratory/`; and authoring accountability under
`data/receipts/generated/`.

No new root, calendar/source connector, policy home, decision authority,
evidence authority, release home, or public route is created.

## Non-effects

This profile does not access a calendar, fetch a meeting notice, accept public
comments, assert participation, create a recommendation or decision, write
lifecycle data, issue funding, promote, release, publish, render a map, or
answer with AI.

## Rollback

Close the draft pull request or abandon the branch before merge. After an
authorized merge, revert the additive packet. No live calendar, workflow,
release, or public artifact requires restoration.
