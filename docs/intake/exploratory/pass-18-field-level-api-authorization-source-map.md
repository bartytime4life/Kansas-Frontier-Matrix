<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-18-field-level-api-authorization-source-map
title: Pass 18 Field-Level API Authorization Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — API steward · Policy steward · Security steward · Release steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: Trace Pass 18 card KFM-P18-INV-151 into a bounded fixture-only field-projection assessment without creating a route, executing authentication or policy, inspecting values, or emitting a response.
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending review / NEEDS VERIFICATION API, policy, security, release, and hosted exact-head execution
related:
  - ../../../contracts/release/field_level_api_authorization_assessment.md
  - ../../../contracts/release/api_capability_exposure_assessment.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/policy/policy_decision.md
  - ../../../contracts/policy/policy_obligation_set.md
  - ../../../contracts/runtime/decision_envelope.md
  - ../../../contracts/ui/evidence_drawer_payload.md
tags: [kfm, pass-18, api, field-authorization, projection, policy, evidence-drawer, source-map]
[/KFM_META_BLOCK_V2] -->

# Pass 18 Field-Level API Authorization Source Map

## Source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, local supplied artifact SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, card `KFM-P18-INV-151`, PDF pages 403–404 (printed pages 400–401) | Endpoint authorization and field-level access are design-time contract requirements. Sensitive, unpublished, or role-inappropriate evidence fields must not be returned merely because a caller is authenticated. The card asks for revoked-grant and downstream Evidence Drawer cases. | Proposal register; it does not define an adopted role model, policy implementation, route, or payload. |
| Google Drive file `KFM Pass 18 Idea Index Category Atlas and Expansion Dossier`, file `1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5` | Drive metadata confirms the matching dossier title used for corpus discovery. | The locally supplied PDF was the inspected evidence. Its byte size differs from the Drive object metadata, so byte identity is not asserted. |
| `contracts/release/api_capability_exposure_assessment.md` | Current repository meaning already assesses whether a capability may be considered for API exposure. | It does not classify or derive individual response-field projections. |
| Existing policy, runtime, and UI contracts | `PolicyDecision`, `PolicyObligationSet`, `DecisionEnvelope`, and `EvidenceDrawerPayload` provide adjacent boundaries and opaque reference roles. | This candidate does not resolve, execute, or supersede them. |
| Adopted Directory Rules v2 | Placement follows responsibility and may not create a parallel policy, runtime, API, or UI authority. | Placement law only; it does not adopt the candidate. |

## Card transcription

`KFM-P18-INV-151` is titled **“Field-level authorization as API
trust-membrane control.”** The card proposes that endpoint authorization and
field-level data access be explicit in the contract surface. It warns that an
authenticated user can still be ineligible to receive sensitive, unpublished,
or role-inappropriate evidence fields.

The card identifies the API contract, `PolicyDecision`, and the role/obligation
model as dependencies. Its expansion prompt specifically asks for fixtures
covering role-specific hidden fields, revoked grants, and downstream Evidence
Drawer payloads. Its open question is the classification of public,
role-scoped, embargoed, and never-returned fields. This packet adopts those four
labels only as a proposed, closed fixture vocabulary.

The cited source attribution inside the dossier is `SRC-P18-006`, source pages
23–24. This packet does not independently verify or reproduce the source book;
the dossier card is the proposal evidence being adapted.

## Repository reconciliation

GitHub `main@bd59127604f3ab7578fe43f30caaeef089c0fffc` already contained
capability-exposure, policy-decision, policy-obligation, runtime-envelope, and
Evidence Drawer meanings. Exact and semantic searches found no
`field_level_api_authorization_assessment`,
`FieldLevelApiAuthorizationAssessmentCandidate`, or equivalent fixture and
validator packet that derives per-field projections from source lifecycle,
policy outcome, grant state, audience role, embargo, and evidence.

The existing capability-exposure assessment remains the broader release
condition. This candidate is an adjacent, narrower pre-exposure check and does
not modify the existing contract.

## Bounded adaptation

| Source pressure | Retained behavior | Deferred authority |
|---|---|---|
| Field classification | Closed labels for public, role-scoped, embargoed, and never-returned fields. | Adopted taxonomy, schema rollout, and production migration. |
| Lifecycle and policy | Only `PUBLISHED` fields under an `ANSWER` policy outcome can qualify. | Store reads, lifecycle resolution, and policy execution. |
| Role and grant | Role-scoped fields require exact role match, active grant, and obligations; revoked grants withhold. | Authentication, identity resolution, grant issuance, and revocation execution. |
| Embargo | The declared evaluation time must be at or beyond the declared embargo time before qualification. | Clock authority, embargo policy, and legal approval. |
| Downstream surfaces | API, AI answer, export, and Evidence Drawer use the same projection boundary. | Payload construction, response delivery, and UI behavior. |
| Evidence | Any projected field requires an opaque EvidenceBundle reference. | Evidence resolution, admission, and truth determination. |

## Path decision

~~~yaml
path_decision:
  artifact: FieldLevelApiAuthorizationAssessmentCandidate
  proposed_path: contracts/release/field_level_api_authorization_assessment.md
  artifact_kind: semantic contract
  authority_owner: bounded pre-exposure field-projection assessment meaning
  lifecycle_stage: pre_release
  execution_role: none
  scope_kind: object_family
  scope_id: field-level-api-authorization-assessment
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - contracts/release/api_capability_exposure_assessment.md
    - contracts/policy/policy_decision.md
    - contracts/policy/policy_obligation_set.md
    - contracts/runtime/decision_envelope.md
    - contracts/ui/evidence_drawer_payload.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
~~~

The release contract lane owns this bounded pre-exposure assessment. Policy
continues to own admissibility decisions, runtime owns execution envelopes, UI
owns Evidence Drawer payload meaning, and any future API implementation remains
outside this packet.

## Non-effects

This packet does not create or inspect a route, authenticate a caller, issue or
revoke a grant, execute policy, read a store or field value, resolve evidence,
construct or emit a response, approve capability exposure, promote, release,
deploy, publish, or authorize public use.
