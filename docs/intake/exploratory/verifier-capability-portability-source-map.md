<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/verifier-capability-portability-source-map
title: Verifier Capability Portability Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · Evidence steward · Security steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded mapping from Drive and Full Atlas verifier-portability proposals to a bounded repository assessment without treating proposal material as verification evidence or authority
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/evidence/verifier_capability_portability.md
  - ../../kfm_full_atlas_seed_cards.md
  - ./new-ideas-4-14-source-map.md
tags: [kfm, atlas, verifier, capability, portability, source-map]
[/KFM_META_BLOCK_V2] -->

# Verifier Capability Portability Source Map

## Drive source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| `KFM_Full_Atlas_seed_cards`, Google Doc `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho` | Records the verifier profile and capability portability triad, its review surface, and its proposed implementation objects and fixture families. | The Atlas is a candidate register, not implementation or verification evidence. |
| `New Ideas 4-14-26`, Google Doc `1QWheXtSGdXa2_7ZXAQR2vQKXHwn8gqYiFe8it3Y9n4Q` | Supplies browser/offline verification examples and the source lineage reconciled by the existing repository source map. | Example paths, libraries, success labels, and trust inputs are not copied as authority. |

The Drive documents were inspected for idea discovery. No source payload, key, signature, trust root, or executable browser verifier is committed.

## Full Atlas cards

| Card | Retained proposal | Bounded implementation |
|---|---|---|
| `KFM-TRIAD-067` | Verification meaning depends on an explicit verifier profile and environment capabilities. | One combined fixture-only candidate with a reproduced portability assessment. |
| `KFM-CAND-0199` | Bind algorithm, canonicalization, trust/revocation inputs, dependencies, network, time, and resource limits. | Closed profile and capability-claim fields with deterministic comparison. |
| `KFM-CAND-0200` | Expose environment, versions, available/missing capabilities, assumptions, and finite outcome. | Inspectable nested records and sorted finding codes. |
| `KFM-CAND-0201` | Define profile, claim, attempt, and assessment objects with synthetic CI/browser/offline and mismatch fixtures. | Eighteen exact cases covering all named capability families without cryptography. |

## Repository reconciliation

- `VerificationStateHistory` remains authority for bitemporal judgment history; this candidate records environment portability, not state transitions.
- `CosignAttestationVerificationPlan` remains a release-oriented plan for a future Cosign adapter; this packet neither runs nor replaces it.
- Existing trust, signing, evidence, policy, review, release, and publication families remain independent.
- Repository search at base `1ab34018d7fb13ad41cfe8a79aed5d4763e58bf8` found no implemented `VerifierProfile`, `VerificationCapabilityClaim`, `VerificationAttempt`, `PortabilityAssessment`, or equivalent complete portability family outside proposal/source-map material.

## Path decision

~~~yaml
path_decision:
  artifact: VerifierCapabilityPortabilityAssessmentCandidate
  proposed_path: contracts/evidence/verifier_capability_portability.md
  artifact_kind: semantic contract
  authority_owner: context for interpreting one verification judgment
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: object_family
  scope_id: verifier-capability-portability
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/kfm_full_atlas_seed_cards.md
    - docs/intake/exploratory/new-ideas-4-14-source-map.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-AUTHROOT-001
    - DIR-SCOPELANE-004
    - DIR-DEP-001
  outcome: PLACE
~~~

## Non-effects

The packet does not resolve an artifact, perform cryptography, load keys or trust material, check revocation, contact a network service, install a library, establish truth, approve evidence, evaluate policy, approve review, authorize release, publish, or permit public use.
