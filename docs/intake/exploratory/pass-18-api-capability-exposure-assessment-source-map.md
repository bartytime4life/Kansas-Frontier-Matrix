<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-api-capability-exposure-assessment-source-map
title: Pass 18 API Capability Exposure Assessment Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · API steward · Contracts steward · Security steward · Release steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; api-capability; trust-boundary; release
responsibility: Reconcile the supplied API capability-exposure idea and connected KFM doctrine with current contract, runtime, release, correction, and rollback seams without exposing a route or promoting source prose or fixture declarations into API, authorization, review, release, or publication authority.
truth_posture: "CONFIRMED source card, corroborating doctrine, and repository gap; PROPOSED inactive implementation profile; UNKNOWN actual API behavior, consumer need, and trust-boundary acceptance; NEEDS VERIFICATION API, security, contracts, and release steward review plus hosted CI"
related:
  - ../../../contracts/release/api_capability_exposure_assessment.md
  - ../../../contracts/release/api_contract_change_assessment.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../contracts/release/release_manifest.md
  - ../../../contracts/release/rollback_card.md
  - ../../../contracts/correction/correction_notice.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 API Capability Exposure Assessment Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-274`, physical PDF pages 411–412 (printed pages 408–409) | API capabilities should be exposed only after purpose, audience, contract, documentation, allowed data states, prohibited uses, finite outcomes, and trust-boundary consequences are documented. | `CONFIRMED` source statement |
| Connected Google Drive document `KFM_Full_Atlas_seed_cards` | The wider seed-card corpus repeatedly keeps evidence, policy/review, release, correction, and rollback dependencies explicit. It corroborates the governance boundary but is not asserted to be byte-identical to the supplied Pass 18 card. | `CONFIRMED` corroborating doctrine |
| `contracts/release/api_contract_change_assessment.md` and `contracts/runtime/runtime_response_envelope.md` | Existing seams govern declared contract transitions and response outcomes, but neither records whether a proposed capability has a documented business purpose and reviewed trust-boundary posture. | `CONFIRMED` adjacent contracts and bounded gap |
| `contracts/release/release_manifest.md`, `contracts/correction/correction_notice.md`, and `contracts/release/rollback_card.md` | Existing closure families can be referenced without duplicating their authority. | `CONFIRMED` adjacent contracts |
| Current `main@e2119bcd81d2f34df5a16f729918d12b7d84478e` plus branch, code, and pull-request search | No exact `KFM-P18-INV-274` or `ApiCapabilityExposureAssessmentCandidate` implementation or pull request was found before implementation. | `CONFIRMED` bounded gap |

## Adaptation

The implementation adds one closed synthetic assessment rather than an API
inventory or route. A complete declaration identifies the capability's business
purpose, audience, contract, documentation surface, data-state scope,
prohibited uses, finite outcomes, trust boundary, risk assessment, human review,
security review, and conditional release/correction/rollback closure.

The conservative public profile admits only a read-only governed-API boundary
over `PUBLISHED` state with evidence resolution, policy evaluation, and payload
scrubbing retained. Internal fixture profiles remain non-authorizing, and
administrative mutation or direct canonical-store exposure is denied.

## Directory Rules basis

The source card defines capability exposure as a pre-release/API governance
question. Existing API contract-change and release semantics therefore place
meaning under `contracts/release/`. Shape, fixtures, validation, tests,
orchestration, source reconciliation, and authoring accountability remain in
their established schema, fixture, tool, test, workflow, documentation, and
generated-receipt roots under accepted ADR-0029.

No API inventory, route, authorization policy, canonical-store access path,
review approval, release record, deployment, or publication surface is created.

## Non-effects and rollback

A local `PASS` authenticates no capability, purpose, audience, contract,
documentation, review, security decision, release, correction, rollback, or
public state. Rollback is a single additive commit revert with no external
cleanup.
