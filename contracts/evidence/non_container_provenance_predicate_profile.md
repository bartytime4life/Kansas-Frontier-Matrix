<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/non-container-provenance-predicate-profile
title: NonContainerProvenancePredicateCandidate - fixture-only structural profile
type: semantic-contract
version: v0.1.0
status: proposed-inactive; fixture-only; structural-only; non-trust; non-release; non-publication
owner: OWNER_TBD - evidence steward; provenance steward; security steward; policy steward; Directory Rules reviewer
created: 2026-08-09
updated: 2026-08-09
policy_label: public; proposed; evidence; provenance; non-container; fail-closed; non-authoritative
source_cards:
  - KFM-P30-PROG-0023
  - KFM-P30-PROG-0024
source_spec_hashes:
  - sha256:cbeaae3de51ab5dd9da4d281780d4dd12f44a9a03d4ef54b526868b22dcddb55
  - sha256:0a9b3201ff58e875d52e3944cc972735887f0ca25c6a730cd12cf9a1efbebc6b
related:
  - ../runtime/run_receipt.md
  - ../../docs/standards/PROVENANCE.md
  - ../../schemas/contracts/v1/evidence/non_container_provenance_predicate_profile.schema.json
  - ../../fixtures/contracts/v1/evidence/non_container_provenance_predicate_profile/cases.json
[/KFM_META_BLOCK_V2] -->

# NonContainerProvenancePredicateCandidate

> **PROPOSED / INACTIVE / FIXTURE-ONLY / STRUCTURAL-ONLY.** This profile records a SLSA-style provenance candidate for synthetic non-container artifacts. It is not a SLSA conformance claim, signature, transparency proof, `RunReceipt`, policy verdict, review record, release decision, or publication record.

## Responsibility boundary

The candidate is an evidence projection that binds one versioned build type, pipeline specification, Git commit, declared input set, declared output set, timing window, builder identity, invocation identity, and existing run-receipt reference. It does not replace KFM's `RunReceipt`; the run receipt remains the execution-memory authority and this candidate remains separately reviewable evidence.

Machine shape lives in `schemas/contracts/v1/evidence/`. The repository-native validator performs JSON Schema plus bounded semantic checks before any future policy adapter could consume the candidate. The source card's proposed CUE implementation is deferred because no accepted CUE schema home, pinned toolchain, or parity gate was verified at the assayed base.

## Required closure

| Surface | Required meaning | Fail-closed rule |
|---|---|---|
| `build_definition` | Versioned build type, pipeline ID/spec hash, immutable fixture Git ref/SHA, and parameters digest. | An unversioned build type, malformed digest, or unpinned commit is invalid. |
| `declared_inputs` | Sorted, unique, digest-bound synthetic source/config inputs. | Empty, duplicate, unordered, output-role, or mutable bindings are invalid. |
| `declared_outputs` | Sorted, unique, digest-bound synthetic data/metadata/proof candidates. | Empty, duplicate, unordered, input-role, or input/output identity collapse is invalid. |
| `run_details` | Builder, invocation, run-receipt reference, and strictly ordered UTC timing. | A missing receipt reference or non-positive interval is invalid. |
| `verification` | Structural, signature, transparency, and OPA states fixed to `NOT_RUN`. | The candidate cannot claim that its own structure, signature, inclusion, or trust was verified. |
| `governance` | Pending review and false evidence-admission, trust, release, and publication decisions. | Structural validity cannot promote itself into trust or release authority. |

## Identity

`spec_hash` is the repository hashing package's RFC 8785/JCS SHA-256 digest over the record after removing `predicate_id` and `spec_hash`. `predicate_id` is `kfm:non-container-provenance-predicate:` plus the first 24 digest characters. Binding arrays and reference arrays are sorted and duplicate-free.

## Fixed non-effects

A conforming candidate performs no file read or mutation, network access, signing, transparency lookup, policy evaluation, evidence admission, review approval, lifecycle promotion, release, or publication. A validator PASS proves only closed shape, declared binding consistency, exact fixture polarity, and deterministic identity.

## Adoption and rollback

Activation requires an accepted provenance-predicate version, canonical SLSA/in-toto mapping decision, pinned validator toolchain (including any CUE parity lane), resolver rules for the referenced run receipt and artifact bytes, authenticated signature and transparency verification, OPA input mapping, human review, and release integration. Rollback is deletion of this eight-file proposal; no artifact, receipt, trust decision, or public state is changed.
