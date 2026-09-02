<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/field-level-api-authorization-assessment
title: Field-Level API Authorization Assessment Candidate
type: semantic-contract
version: v0.1.0
status: proposed; experimental; fixture-only; non-authoritative
owners: OWNER_TBD — API steward · Policy steward · Security steward · Release steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; release; governed-api; field-authorization; trust-membrane; fixture-only
owning_root: contracts/
responsibility: Define a bounded synthetic assessment that binds per-field response projection to policy outcome, grant state, audience role, source lifecycle, embargo, evidence, and downstream surface without creating a route, executing authentication or policy, inspecting values, or emitting a response.
truth_posture: PROPOSED source-grounded adaptation / CONFIRMED deterministic synthetic implementation / NEEDS VERIFICATION API, policy, security, release, and Evidence Drawer steward review
related:
  - ./api_capability_exposure_assessment.md
  - ../../schemas/contracts/v1/release/field_level_api_authorization_assessment.schema.json
  - ../../fixtures/contracts/v1/release/field_level_api_authorization_assessment/cases.json
  - ../../tools/validators/release/validate_field_level_api_authorization_assessment.py
  - ../../tests/validators/release/test_validate_field_level_api_authorization_assessment.py
  - ../../docs/intake/exploratory/pass-18-field-level-api-authorization-source-map.md
  - ../policy/policy_decision.md
  - ../policy/policy_obligation_set.md
  - ../runtime/decision_envelope.md
  - ../ui/evidence_drawer_payload.md
tags: [kfm, api, field-level-authorization, projection, policy, release, evidence-drawer, fixture-only]
notes:
  - "Implements the smallest dependency-closed slice of Pass 18 card KFM-P18-INV-151."
  - "The candidate assesses field names and control metadata only; it carries no field values or response payload."
[/KFM_META_BLOCK_V2] -->

# Field-Level API Authorization Assessment Candidate

## Status and purpose

`FieldLevelApiAuthorizationAssessmentCandidate` is a **PROPOSED**,
experimental, fixture-only pre-exposure assessment for one governed API
projection. It adapts Pass 18 card `KFM-P18-INV-151`: endpoint authorization
and field-level access are design-time contract requirements, not a runtime
middleware afterthought.

The candidate proves a narrow proposition: given declared request and decision
contexts, every requested field must be projected or withheld for the exact
reason derived by the profile. It records field names and control metadata but
contains no field values. A validator `PASS` cannot disclose data because the
validator never reads a canonical store or emits a response.

## Classification vocabulary

| Classification | Passing projection rule |
|---|---|
| `PUBLIC` | Requested, `PUBLISHED`, policy outcome `ANSWER`, and an EvidenceBundle reference. |
| `ROLE_SCOPED` | Public prerequisites plus an `ACTIVE` grant, exact audience-role match, and at least one obligation reference. |
| `EMBARGOED` | Public prerequisites plus an expired embargo; when a role is declared, the grant must be active and the audience must match. |
| `NEVER_RETURN` | Never projected, regardless of authentication, role, grant, policy outcome, source state, evidence, or downstream surface. |

Only `PUBLISHED` source state can project. `PROCESSED`, `WORK`, `QUARANTINE`,
and `RAW` remain withheld even when a user is authenticated and the declared
policy outcome is `ANSWER`.

## Deterministic decision order

For each requested field, the profile applies the following fail-closed order:

1. an unrequested field remains absent;
2. a non-published source state remains absent;
3. `NEVER_RETURN` remains absent;
4. an active embargo remains absent;
5. `ABSTAIN`, `DENY`, or `ERROR` policy outcomes remain absent;
6. role and active-grant requirements must match;
7. a field that otherwise qualifies still requires an EvidenceBundle
   reference; and
8. only then may the declaration mark the field projected.

The declared boolean and reason code must exactly match that derivation.
Fields and obligation references are canonically ordered, identity is
content-bound, and the summary is deterministically replayed.

## Surfaces and composition

The operation and downstream surface are paired:

| Operation | Surface |
|---|---|
| `READ` | `API_RESPONSE` |
| `ANSWER` | `AI_ANSWER` |
| `EXPORT` | `EXPORT` |
| `DRAWER` | `EVIDENCE_DRAWER` |

The same field boundary applies to every surface. In particular, an Evidence
Drawer is not a side channel for a hidden, embargoed, unpublished, revoked, or
never-returned field.

`PolicyDecision`, `PolicyObligationSet`, the API contract, the capability, and
any EvidenceBundle remain opaque references with distinct roles. Their
existing owners retain semantic and execution authority; this candidate does
not resolve or execute them.

## Finite outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | Field decisions, reason codes, ordering, identity, summary, and boundary flags are internally coherent. | Still `REVIEW_REQUIRED`; no route or response is authorized. |
| `DENY` | Shape, classification, lifecycle, policy, grant, embargo, evidence, projection, surface, identity, or summary invariants fail. | No fallback projection and no partial response. |
| `ERROR` | Input or schema cannot be boundedly read. | No field decision is trusted. |

## Directory Rules basis

This object determines whether a proposed field projection is coherent before
API exposure, so it is adjacent to
`ApiCapabilityExposureAssessmentCandidate` in `contracts/release/`. It does not
own policy meaning, runtime execution, UI payload meaning, or API
implementation. Machine shape, fixtures, deterministic validation, executable
proof, source adaptation, hosted orchestration, and authoring provenance remain
in their adopted responsibility lanes.

## Non-effects

A green result does not:

- create, discover, bind, or modify an API route or schema;
- authenticate a caller, issue or revoke a grant, or execute a policy decision
  or obligation;
- read a database, graph, object store, lifecycle store, evidence bundle, or
  actual field value;
- construct an API, export, AI-answer, or Evidence Drawer payload;
- approve a capability, security review, human review, promotion, release,
  deployment, publication, or public use.

## Rollback

Before merge, close the draft pull request and remove its branch. After an
authorized merge, revert this additive packet and rerun its dedicated
workflow. No route, grant, policy, payload, release, deployment, or public state
requires restoration.
