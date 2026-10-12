<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-30-non-container-provenance-predicate-source-map
title: Pass 30 non-container provenance predicate - source adaptation map
type: exploratory-source-map
status: proposed; non-authoritative; non-trust; non-release; non-publication
created: 2026-08-09
updated: 2026-08-09
source_cards: KFM-P30-PROG-0023; KFM-P30-PROG-0024
source_spec_hashes: sha256:cbeaae3de51ab5dd9da4d281780d4dd12f44a9a03d4ef54b526868b22dcddb55; sha256:0a9b3201ff58e875d52e3944cc972735887f0ca25c6a730cd12cf9a1efbebc6b
[/KFM_META_BLOCK_V2] -->

# Pass 30 non-container provenance predicate - source adaptation map

## Decision

**PROPOSED:** admit one dependency-closed, fixture-only `NonContainerProvenancePredicateCandidate` packet. It records a SLSA-style non-container predicate shape and performs repository-native structural validation before any future OPA adapter. It does not claim full SLSA conformance or activate CUE, signing, transparency, policy, release, or publication behavior.

## Source evidence

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| `KFM-P30-PROG-0023` | CONFIRMED | A non-container provenance predicate carrying build type, pipeline, Git repo/SHA, inputs, outputs, and timing. | The card is proposed and does not define a complete SLSA/in-toto version mapping. |
| Card spec hash `sha256:cbeaae3de51ab5dd9da4d281780d4dd12f44a9a03d4ef54b526868b22dcddb55` | CONFIRMED | Exact predicate-card identity. | Does not hash this implementation. |
| `KFM-P30-PROG-0024` | CONFIRMED | Structural provenance validation before OPA trust logic. | CUE is a proposed tool choice, not an accepted repository dependency or schema authority. |
| Card spec hash `sha256:0a9b3201ff58e875d52e3944cc972735887f0ca25c6a730cd12cf9a1efbebc6b` | CONFIRMED | Exact validator-card identity. | Does not prove CUE availability or parity. |
| Consolidated atlas PDF SHA-256 `020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639` | CONFIRMED | Attachment bytes and rendered card page inspected; both cards remain active and unchanged through Pass 32. | Source material, not repository authority. |
| Repository base `1ab34018d7fb13ad41cfe8a79aed5d4763e58bf8` | CONFIRMED | Exact-ID, semantic, branch, and PR duplicate assay; RunReceipt, provenance, attestation, schema, validator, and Directory Rules surfaces inspected. | Bounded snapshot; later changes require recheck. |

Drive evidence references: `google-drive:1w7Qrf5Na7PSvwdTuplZnFbyueToPtQaa#KFM-P30-PROG-0023` and `#KFM-P30-PROG-0024`.

## Directory Rules placement

| Responsibility | Path | Basis |
|---|---|---|
| Proposed evidence-projection meaning | `contracts/evidence/` | The candidate describes provenance evidence without becoming a receipt or decision. |
| Machine shape | `schemas/contracts/v1/evidence/` | JSON Schema owns the closed shape; no parallel schema root is introduced. |
| Synthetic cases | `fixtures/contracts/v1/evidence/` | All artifact, builder, pipeline, Git, invocation, and receipt references are fictional. |
| Executable validation | `tools/validators/evidence/` | Repository-native offline structure and binding checks only. |
| Proof | `tests/validators/evidence/` and `.github/workflows/` | Exact polarity, parser hardening, identity replay, and receipt integrity. |
| Receipt instances and trust decisions | Existing `data/receipts/`, policy, review, and release authorities | Unchanged; the candidate references but does not replace them. |

## Compatibility and non-duplication

This candidate references the existing shared `RunReceipt`; it is not a new execution receipt. It does not replace PMTiles-specific attestation validation, Cosign verification planning, generated-receipt integrity, signatures, Rekor inclusion, OPA decisions, or release manifests. The predicate's `verification` states remain `NOT_RUN` and every authority-bearing decision remains false.

## Admitted, deferred, rejected

- **Admitted:** versioned build type, pipeline identity/spec hash, fixture Git identity, parameters digest, sorted input/output bindings, builder/invocation/run-receipt refs, ordered timing, deterministic identity, fixed non-effects, and pending governance posture.
- **Deferred:** canonical SLSA/in-toto predicate mapping, CUE schema/toolchain and parity validation, artifact byte resolution, signature verification, transparency lookup, OPA input mapping, authenticated review, release integration, and activation.
- **Rejected:** real artifacts, credentials, network endpoints, mutable refs, self-asserted validation, signature or Rekor claims, policy trust, evidence admission, automatic approval, release, and publication.

## Failure and rollback

Malformed, incomplete, unordered, role-collapsed, temporally invalid, authority-bearing, or identity-inconsistent records fail closed. Rollback is deletion of the eight additive files; no artifact, receipt, trust, release, or public state is altered.
