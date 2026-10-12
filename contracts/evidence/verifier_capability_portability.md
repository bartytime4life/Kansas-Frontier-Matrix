<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/verifier-capability-portability
title: VerifierCapabilityPortabilityAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Evidence steward · Security steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; evidence; verifier-portability; fail-safe
owning_root: contracts/
responsibility: fixture-only declaration of whether one verifier environment has the pinned capabilities needed for semantically comparable verification
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ./verification_state_history.md
  - ../release/cosign_attestation_verification_plan.md
  - ../../schemas/contracts/v1/evidence/verifier_capability_portability.schema.json
  - ../../fixtures/contracts/v1/evidence/verifier_capability_portability/cases.json
  - ../../tools/validators/validate_verifier_capability_portability.py
  - ../../tests/validators/test_validate_verifier_capability_portability.py
  - ../../docs/intake/exploratory/verifier-capability-portability-source-map.md
tags: [kfm, evidence, verifier, capability, portability, fixture]
notes:
  - "Adapts Full Atlas KFM-TRIAD-067 / KFM-CAND-0199..0201 as one bounded assessment candidate."
  - "A portability result is not cryptographic verification, evidence support, trust, review, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# VerifierCapabilityPortabilityAssessment Candidate Contract

`VerifierCapabilityPortabilityAssessmentCandidate` records whether a synthetic CI, server, desktop, browser, or offline verifier capability claim satisfies one pinned verifier profile. It keeps algorithm, canonicalization, trust and revocation inputs, dependency versions, network posture, time source, and resource limits visible instead of reducing different environments to the same green label.

## Source-derived gap

Full Atlas triad `KFM-TRIAD-067` identifies a portability gap: library availability or environmental success can silently change verification meaning. Candidates `KFM-CAND-0199` through `KFM-CAND-0201` propose `VerifierProfile`, `VerificationCapabilityClaim`, `VerificationAttempt`, and `PortabilityAssessment` records plus synthetic environment and failure fixtures. The reconciled `New Ideas 4-14-26` source map independently marks verifier-profile portability as a repository gap.

## Authority boundary

This profile compares declarations only. It does not resolve an artifact, load trust material, perform cryptography, contact a transparency or revocation service, install a dependency, use a key, or make a verification result authoritative.

The nested records have distinct responsibilities:

- `verifier_profile` pins the semantics and minimum capabilities required for comparison;
- `capability_claim` describes one synthetic environment without proving the claim;
- `verification_attempt` describes a bounded synthetic attempt and resource observation; and
- `portability_assessment` is reproduced from those declarations.

## Finite portability outcomes

| Outcome | Meaning |
|---|---|
| `PORTABLE` | The declared environment matches every pinned capability in this bounded profile. |
| `QUALIFIED` | The capabilities match, but trust material is stale and the result cannot be treated as current. |
| `UNSUPPORTED` | A required algorithm, revocation input, clock, network capability, or resource capacity is unavailable. |
| `INCOMPARABLE` | Canonicalization, trust identity, dependency identity, or time-source semantics differ. |

Hard unsupported capability outranks incomparability, which outranks stale-trust qualification. Every outcome remains non-authoritative and requires separate security review before any real verifier integration.

## Deterministic comparison

The validator reproduces a sorted finding inventory from exact fields:

- required algorithm must be in the claimed supported set;
- canonicalization profile must match exactly;
- trust and revocation digests must match the pinned inputs;
- dependency name, version, and digest inventories must be identical and canonical;
- required network and time capabilities must be available;
- claimed capacity must meet the profile, and observed usage must remain within the claim; and
- the attempt must bind the exact profile, algorithm, and canonicalization identifiers.

`spec_hash` is RFC 8785 JCS plus SHA-256 over the candidate excluding only `assessment_id` and `spec_hash`. `assessment_id` uses the first 24 digest characters. All arrays used as sets are sorted and unique.

## Validator meaning

Validator `PASS` means the declaration, reproduced portability assessment, deterministic identity, and non-authority fields agree. It can therefore accompany any of the four portability outcomes. `DENY` identifies an incoherent declaration, report, or identity. `ERROR` identifies unsafe JSON input. None means that verification occurred.

## Directory Rules basis

The object records context for interpreting a verification judgment, so semantic meaning belongs in `contracts/evidence/`. Machine shape belongs in `schemas/contracts/v1/evidence/`; synthetic cases, executable validation, tests, CI, source mapping, and AI authoring accountability remain in their established roots. No signing, trust-root, release, runtime, policy, or publication authority is added.

## Non-effects and rollback

This packet cannot verify a subject, authenticate an identity, approve a dependency, refresh trust, authorize network use, approve review, promote, release, deploy, publish, or permit public use. Before merge, close the draft PR and retire its branch. After an authorized merge, revert the additive packet; it has no live consumer or external state.
