<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/new-ideas-5-19-26-attested-compute-boundary
title: New Ideas 5-19-26 Attested-Compute Boundary Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Governance steward · Security steward · Privacy steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; source-lineage; attested-compute; tre
responsibility: Preserve the connected-Drive recommendation and repository reconciliation for a decision-only attested-compute boundary without promoting source prose into security, compute, policy, release, or publication authority.
truth_posture: "CONFIRMED connected-Drive source identity and repository source-map recommendation; PROPOSED bounded adaptation; UNKNOWN real TEE need; NEEDS VERIFICATION primary security evidence, human review, and hosted exact-head CI"
related:
  - ../../../docs/adr/ADR-0032-attested-compute-boundary.md
  - ./new-ideas-5-19-26-source-map.md
  - ../../../contracts/governance/attested_compute_boundary_assessment.md
  - ../../../schemas/contracts/v1/governance/attested_compute_boundary_assessment.schema.json
  - ../../../fixtures/contracts/v1/governance/attested_compute_boundary_assessment/cases.json
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# New Ideas 5-19-26 Attested-Compute Boundary Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Connected Google Doc `New Ideas 5-19-26`, file ID `1Gx4pU71Pqk1cG1oKb8l69B8K4yOJK7zy5KNH-Xvl4HQ`, modified `2026-05-20T21:19:45.504Z` | The complete Drive document contains proposals for attested compute-to-data and trusted research environments among many other implementation sketches. | `CONFIRMED` source identity |
| Repository source map `new-ideas-5-19-26-source-map.md`, source-text SHA-256 `246c0f9ab4664543a06a91bd8519b170056001a2b3e2c7a8b9ddd79b0151a8f7` | Its recommended next bounded action is a decision-only attested-compute packet that compares `NO_TRE`, `SIMULATED_ASSESSMENT`, `DEFER_REAL_TEE`, and `DENY_UNVERIFIED_ATTESTATION`; separates eight authority layers; permits only no-data/no-network simulation; and defines invalidation rollback. | `CONFIRMED` repository recommendation |
| Proposed `ADR-0032-attested-compute-boundary.md` | It defaults proposals to `NO_TRE`, permits only a separately reviewed synthetic profile after a concrete control gap is documented, and requires affected owners, supported/unsupported attestation claims, separated execution and evidence/review lanes, a synthetic plan, correction, and rollback. | `CONFIRMED` proposed repository decision; not accepted authority |
| `main@6b1c60d3814548acaedc7a365c90e0010573790e` and pull-request history | Exact searches found adjacent quarantine, PolicyDecision, receipt, review, sensitive-release, verifier-portability, correction, rollback, and proposed ADR-0032 surfaces. Merged PR `#2408` owns the ADR-only proposal; no contract/schema/fixture/validator/workflow implementation profile or competing profile branch/PR was found. | `CONFIRMED` for the inspected snapshot and search time |

The Drive document is proposal evidence, not security guidance or implementation authority. No current vendor, cloud, TEE, trust root, verifier, cryptographic mechanism, service term, threat claim, or portability claim was established in this pass.

## Selected increment

The smallest non-duplicative increment is one inactive assessment profile. It asks whether an asserted residual problem survives the existing quarantine, policy, receipt, and review controls; pins affected responsibility owners; separates the source-map boundaries plus the ADR's execution-receipt and evidence/reviewer seams; declares what attestation cannot authorize; and derives one of the four recommended postures.

The packet deliberately has no real execution path. Its strongest positive result, `SIMULATED_ASSESSMENT`, means only that a synthetic declaration packet is internally complete enough for continued human review.

## Source-to-profile mapping

| Source-map pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Explain what existing controls do not solve. | Four separately reviewed control states plus an exact residual-problem mapping. | No claim that a listed control exists, is sufficient, or was correctly reviewed. |
| Separate workload, input, attestation, execution receipt, policy, disclosure, transform, evidence/reviewer, release, and rollback. | Ten required declaration slots with pinned refs and local resolution state. | No reference resolution, authentication, policy evaluation, or approval. |
| Compare four postures. | Deterministic decision derivation and exact fixtures for all four. | No real TEE selection or execution decision. |
| Permit only bounded simulation. | `NO_DATA_SYNTHETIC_ONLY`, no network, no credentials, no external verification, and a pinned synthetic plan. | No real or sensitive input and no cryptographic simulation claim. |
| Bound what attestation can support. | One narrow claimed-support declaration and an exhaustive fixed list of authorities it cannot supply. | No source, purpose, consent, evidence, disclosure, review, or release authority. |
| Deny unverified attestation. | Any `UNVERIFIED_EXTERNAL` claim derives the deny posture. | No v1 vocabulary for verified external evidence. |
| Correct later-invalidated attestation or verifier claims. | Fixed void-and-review action, unreleasable dependents, and a separate rollback reference. | No correction execution or release withdrawal. |

## Directory Rules basis

The decision semantics remain under `contracts/governance/`. Shape, synthetic inputs, validation, tests, read-only orchestration, source reconciliation, and authoring accountability use their established responsibility roots. No topic-named root, runtime lane, key store, verifier service, sensitive-data store, policy authority, release path, or public surface is added.

## Deferred evidence

- whether a KFM use case actually requires trusted execution after existing controls are applied;
- a reviewed threat model, data owner, purpose, and residual disclosure risk;
- primary specifications for any candidate attestation format, verifier, trust root, revocation model, and portability claim;
- key rotation, verifier compromise, freshness, replay, rollback, and dependent-output invalidation behavior;
- legal, privacy, security, policy, review, release, and operational ownership; and
- an explicitly authorized later decision before any real input, credential, network, cloud, key, external verifier, output, deployment, or publication is introduced.

## Validation and rollback

Focused validation covers closed shape, canonical identity, exact control-to-problem mapping, all eight declaration slots, all four postures, synthetic-only safeguards, unverified-attestation denial, correction/rollback separation, no-network replay, unknown-field rejection, and fixed-false authority effects.

Rollback is a focused revert of this additive packet. No TEE, verifier, key, credential, sensitive input, output, release, deployment, or public artifact exists to restore.
