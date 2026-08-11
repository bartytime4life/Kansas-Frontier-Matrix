<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/api-capability-exposure-assessment
title: ApiCapabilityExposureAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — API steward · Contracts steward · Security steward · Release steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; release; governed-api; capability-exposure; trust-boundary
responsibility: Define a fixture-only assessment that records one proposed API capability's purpose, audience, contract, documentation, lifecycle-state scope, prohibited uses, finite outcomes, trust-boundary posture, review, security, release, correction, and rollback references without exposing or authorizing the capability.
truth_posture: "CONFIRMED source-card traceability and repository gap; PROPOSED inactive contract; UNKNOWN actual API behavior and consumer need; NEEDS VERIFICATION API, security, contracts, and release steward review plus hosted CI"
related:
  - ./api_contract_change_assessment.md
  - ./release_manifest.md
  - ./rollback_card.md
  - ../correction/correction_notice.md
  - ../runtime/runtime_response_envelope.md
  - ../../schemas/contracts/v1/release/api_capability_exposure_assessment.schema.json
  - ../../fixtures/contracts/v1/release/api_capability_exposure_assessment/cases.json
  - ../../tools/validators/release/validate_api_capability_exposure_assessment.py
  - ../../tests/validators/release/test_validate_api_capability_exposure_assessment.py
  - ../../docs/intake/exploratory/pass-18-api-capability-exposure-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# ApiCapabilityExposureAssessmentCandidate

`ApiCapabilityExposureAssessmentCandidate` is an inactive declaration profile
for one proposed API capability exposure. It implements the smallest
dependency-closed portion of Pass 18 card `KFM-P18-INV-274`.

## Boundary

A validator `PASS` proves only that the supplied declaration is internally
coherent under this synthetic profile. It does not discover or inspect a route,
authenticate a contract or review reference, execute authorization, read a
store, resolve evidence, evaluate policy, mutate state, approve a capability,
release, deploy, publish, or authorize public use.

The assessment distinguishes a `PUBLIC_CANDIDATE` from an `INTERNAL_ONLY`
declaration. Both remain proposals. An internal-only `PASS` is not permission to
expose an internal route, and a public-candidate `PASS` is not a release or
publication decision.

## Conservative declaration rules

- every complete assessment declares a non-placeholder business purpose,
  audience, contract, documentation surface, lifecycle-state scope, prohibited
  uses, finite outcomes, risk assessment, security review, and human review;
- every exposure uses a governed API or internal governed-service boundary;
  direct canonical-store exposure is denied;
- the fixed finite outcome vocabulary is `ABSTAIN`, `ANSWER`, `DENY`, and
  `ERROR`;
- the universal prohibited-use set denies governance bypass, direct canonical
  store access, caller-created release/publication authority, and uncited
  evidence-free claims;
- a public candidate is read-only, uses the governed API boundary, exposes only
  `PUBLISHED` state, and retains evidence resolution, policy evaluation, and
  public-payload scrubbing;
- a public candidate also references release, correction, and rollback
  closure; and
- administrative mutation is never a valid ordinary capability exposure in
  this profile.

These are conservative fixture rules, not an adopted API inventory, universal
authorization policy, or statement that every internal API must share this
exact shape.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared exposure packet is locally coherent and reviewable. |
| `ABSTAIN` | Capability details or trust-boundary review remain unresolved. |
| `DENY` | The declaration would bypass required purpose, audience, lifecycle, trust-boundary, review, security, or release constraints. |
| `ERROR` | Shape or bounded input handling prevents safe evaluation, or the assessment records an error. |

These outcomes are assessment results only. They are not API responses,
authorization decisions, policy decisions, review approvals, or release state.

## Directory Rules basis

The source card treats exposure review as a precondition to an API capability
becoming public or semi-public. Existing repository convention places adjacent
API contract-change, ReleaseManifest, and RollbackCard semantics under
`contracts/release/`. Accepted ADR-0029 therefore places this semantic profile
there, with machine shape under `schemas/contracts/v1/release/`, synthetic
replay under `fixtures/contracts/v1/release/`, reusable validation under
`tools/validators/release/`, conformance proof under
`tests/validators/release/`, read-only orchestration under
`.github/workflows/`, source reconciliation under `docs/intake/exploratory/`,
and authoring accountability under `data/receipts/generated/`.

The profile composes existing response-envelope, release, correction, rollback,
and API contract-change families by opaque reference. It creates no API or
route registry, canonical-store access path, authorization policy, review
approval, release record, deployment, or publication surface.

## Validation and rollback

```bash
python -m unittest tests.validators.release.test_validate_api_capability_exposure_assessment -v
python tools/validators/release/validate_api_capability_exposure_assessment.py --fixtures
```

Rollback is one additive commit revert. No API, route, client, data, policy,
review, release, correction, rollback, deployment, cache, or public state
requires operational restoration.
