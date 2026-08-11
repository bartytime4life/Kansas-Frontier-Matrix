<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/attested-compute-boundary-assessment
title: AttestedComputeBoundaryAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; decision-only; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Governance steward · Security steward · Privacy steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; governance; attested-compute; tre; decision-boundary
responsibility: Define a decision-only assessment that separates an attested-compute proposal into reviewable authority boundaries without selecting or executing a TEE, verifying an external attestation, processing sensitive data, or authorizing release.
truth_posture: "CONFIRMED connected-Drive source-map recommendation and repository gap; PROPOSED inactive assessment; UNKNOWN runtime need; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../docs/adr/ADR-0032-attested-compute-boundary.md
  - ../../docs/intake/exploratory/new-ideas-5-19-26-source-map.md
  - ../../docs/intake/exploratory/new-ideas-5-19-26-attested-compute-boundary-source-map.md
  - ../../schemas/contracts/v1/governance/attested_compute_boundary_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/attested_compute_boundary_assessment/cases.json
  - ../../tools/validators/governance/validate_attested_compute_boundary_assessment.py
  - ../../tests/validators/governance/test_validate_attested_compute_boundary_assessment.py
tags: [kfm, governance, attestation, tre, decision-only, fixture-only, no-network]
notes:
  - "A coherent SIMULATED_ASSESSMENT posture authorizes only continued human review of synthetic declarations; it does not authorize compute."
  - "The v1 vocabulary intentionally has no verified-external-attestation state because this validator performs no external verification."
[/KFM_META_BLOCK_V2] -->

# AttestedComputeBoundaryAssessment Candidate

`AttestedComputeBoundaryAssessmentCandidate` is a fixture-only decision profile for deciding whether KFM should stop at existing controls, review a synthetic boundary, defer real trusted-execution-environment work, or deny an unverified attestation claim.

It implements the bounded next action selected by the connected-Drive `New Ideas 5-19-26` source map and the separate synthetic profile contemplated by proposed ADR-0032. It does not accept that ADR, implement a TRE or TEE, or authorize simulation by file presence.

## Problem boundary

An assessment must first say which residual problem is not solved by the existing quarantine, policy, receipt, and human-review surfaces. The four controls are recorded separately as:

- `REVIEWED_SUFFICIENT`;
- `REVIEWED_INSUFFICIENT`; or
- `NOT_REVIEWED`.

For a defined residual problem, `unsolved_by_existing_controls` must exactly match the controls marked insufficient and at least one affected responsibility owner must be pinned. A `NO_TRE` posture is coherent only when the controls have been reviewed and no residual problem remains. The validator does not prove that a control or owner exists or that its review was correct.

## Separated declarations

The profile keeps these responsibilities distinct:

1. workload identity;
2. input authority;
3. attestation evidence;
4. execution receipt;
5. policy obligations;
6. disclosure review;
7. output transformation;
8. evidence and reviewer decision;
9. release approval; and
10. rollback.

Each slot contains only a pinned local reference and a declaration state. `RESOLVED` means the declaration is locally complete under the fixture; it does not authenticate or resolve the referenced object.

## Finite postures

| Posture | Coherent use in this profile | Validator outcome |
|---|---|---|
| `NO_TRE` | Existing controls were reviewed, no residual problem remains, no execution is requested, and all eight declarations are explicitly not required. | `PASS` |
| `SIMULATED_ASSESSMENT` | A residual gap is defined, existing controls were reviewed, all eight declaration slots are complete, the attestation is synthetic-only, and the request is synthetic simulation. | `PASS` |
| `DEFER_REAL_TEE` | The problem or controls are unresolved, required declaration slots are incomplete, or real TEE work is requested. | `ABSTAIN` |
| `DENY_UNVERIFIED_ATTESTATION` | An external attestation claim is declared but has not been verified. | `DENY` |

An assessment-state error produces validator `ERROR`. These outcomes are local decision-profile results, not policy decisions, security findings, release approvals, or runtime authorizations.

## Synthetic-only boundary

The schema fixes the following safeguards and requires a pinned synthetic fixture-plan reference before the simulated posture can be coherent:

- no real or sensitive data;
- no credentials or keys;
- no network or external verifier call;
- no cloud or TEE selection;
- no compute execution;
- no released output;
- no deployment or publication.

`SIMULATED_ASSESSMENT` permits only a no-data, no-network synthetic fixture for reviewing the boundary declarations. The candidate must also declare the narrow claim the synthetic attestation could represent and explicitly retain source admissibility, purpose authority, consent validity, evidence sufficiency, disclosure safety, review approval, and release fitness outside attestation authority. It does not mean a simulated attestation is genuine or that a real verifier is portable, trustworthy, current, or acceptable.

## Correction and rollback

Every candidate declares that later invalidation of an attestation claim or verifier profile must void the assessment and route dependent candidates back to review. Dependent outputs remain unreleasable. The rollback declaration is separate from release approval so either cannot stand in for the other.

## Deterministic identity

`profile_spec_hash` is SHA-256 over canonical JSON for the complete candidate after removing only that field. Canonical arrays, UTC observation time, exact control-to-problem mapping, attestation-reference coherence, derived decision posture, and fixed-false authority effects are replayed locally.

## Directory Rules basis

Cross-cutting decision meaning belongs under `contracts/governance/`; machine shape under `schemas/contracts/v1/governance/`; synthetic cases under `fixtures/contracts/v1/governance/`; reusable validation under `tools/validators/governance/`; conformance evidence under `tests/validators/governance/`; read-only orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

No `tre/`, `tee/`, security-runtime, secret, key, verifier, data, policy, release, deployment, or publication root is created.

## Validation

```bash
python -m unittest tests.validators.governance.test_validate_attested_compute_boundary_assessment -v
python tools/validators/governance/validate_attested_compute_boundary_assessment.py --fixtures
```

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the additive packet. It creates no runtime, credential, sensitive-data copy, external attestation, release, deployment, or public artifact that requires operational rollback.
