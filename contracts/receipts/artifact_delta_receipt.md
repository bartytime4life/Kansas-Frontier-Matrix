<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/receipts/artifact-delta-receipt
title: ArtifactDeltaReceiptCandidate Semantic Contract
type: semantic-contract; receipt; fixture-first; no-network
version: v0.1.0
status: proposed; candidate-only; no-cryptographic-verification; no-release-authority
owners: OWNER_TBD — Receipt steward · Release steward · Evidence steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; receipts; process-memory; delta; no-release-authority
related:
  - ./README.md
  - ../../schemas/contracts/v1/receipts/artifact_delta_receipt.schema.json
  - ../../fixtures/contracts/v1/receipts/artifact_delta_receipt/
  - ../../tools/validators/validate_artifact_delta_receipt.py
  - ../../tests/validators/test_validate_artifact_delta_receipt.py
  - ../release/promotion_receipt.md
  - ../release/rollback_card.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, receipt, artifact-delta, jcs, sha256, cose, dsse, sigstore, rollback]
[/KFM_META_BLOCK_V2] -->

# `ArtifactDeltaReceiptCandidate`

> A fixture-first process-memory candidate that binds one declared artifact revision to
> another and records the associated policy, review, rollback/correction, and attestation
> metadata. A valid candidate is **not** cryptographic proof and does not authorize promotion,
> release, publication, rollback execution, or public use.

## Purpose

The attached *New Ideas 3-11-26* packet proposes tamper-evident delta receipts containing
`before` and `after` run/spec identities, a policy decision, a steward identity, deterministic
JCS/SHA-256 identity, a COSE signature, and an OCI referrer. This contract adopts only the
safe, dependency-closed first step: deterministic shape and local consistency over synthetic
fixtures. It deliberately does not download signing tools, use secrets, contact a registry,
verify a real signature, mutate lifecycle data, or publish from a pull request.

## Responsibility and placement

| Surface | Responsibility root | Role |
|---|---|---|
| Semantic meaning | `contracts/receipts/` | This contract. |
| Machine shape | `schemas/contracts/v1/receipts/` | Closed Draft 2020-12 schema. |
| Synthetic examples | `fixtures/contracts/v1/receipts/` | Positive and negative fixture polarity. |
| Validation | `tools/validators/`, `tests/validators/` | Deterministic, no-network checks. |
| Emitted process memory | `data/receipts/` | Future runtime instances; none created here. |
| Release decisions | `release/` | Separate authority; only referenced here. |

This follows accepted ADR-0029 and Directory Rules v2: a receipt is owned by the receipt
semantic/schema families, while release decisions, rollback cards, policy decisions, proofs,
and published carriers remain separate object families.

## Required semantics

| Field | Meaning |
|---|---|
| `receipt_id` | Stable candidate identity. |
| `change_kind` | `PROMOTION`, `CORRECTION`, `ROLLBACK`, or `SUPERSESSION`. |
| `before` / `after` | Run receipt, artifact, spec-hash, artifact-digest, and optional release references. |
| `decision` | Referenced policy outcome and obligations; metadata only. |
| `review` | Referenced review state and actor metadata; metadata only. |
| `attestation` | Declared format and verification state; no signature bytes are accepted. |
| `rollback_target_ref` | Required for approved changes and all rollback candidates. |
| `correction_notice_ref` | Required for correction candidates. |
| `canonicalization.payload_digest` | SHA-256 over the canonical candidate with this field omitted. |
| `governance` | Fixed false/non-authoritative boundary flags. |

## Deterministic digest profile

The profile name is `RFC8785-JCS-SAFE-SUBSET-v1`.

1. Parse UTF-8 JSON with duplicate-key rejection.
2. Reject floating-point values and non-finite numbers. This profile contains only strings,
   booleans, nulls, arrays, and objects.
3. Remove `canonicalization.payload_digest` from a deep copy.
4. Serialize with UTF-8, lexicographically sorted object keys, and no insignificant
   whitespace.
5. Compute SHA-256 and store the lower-case value as `sha256:<64 hex>`.

The profile is intentionally narrower than a general-purpose RFC 8785 implementation. It is
sufficient for this contract's value domain and must not be cited as proof that arbitrary JSON
numbers were JCS-canonicalized.

## Local consistency rules

- `before` and `after` must differ in artifact/spec identity.
- A run receipt reference cannot be reused across both revisions.
- `APPROVE` requires an approved review record, declared verified attestation metadata,
  attestation/signer/OCI references, and a rollback target.
- `ROLLBACK` requires a rollback target.
- `CORRECTION` requires a correction notice.
- Placeholder zero digests are denied.
- The stored payload digest must recompute exactly.
- Every governance authority flag remains false; the object is process memory only.

## Finite validator outcomes

The CLI emits `PASS` or `FAIL` plus stable finding codes. Important codes include:

- `DELTA_NO_EFFECT`
- `RUN_RECEIPT_REUSED`
- `PAYLOAD_DIGEST_MISMATCH`
- `APPROVAL_REQUIRES_APPROVED_REVIEW`
- `APPROVAL_REQUIRES_VERIFIED_ATTESTATION`
- `APPROVAL_REQUIRES_ROLLBACK_TARGET`
- `ROLLBACK_TARGET_REQUIRED`
- `CORRECTION_NOTICE_REQUIRED`
- `GOVERNANCE_BOUNDARY_VIOLATION`

## Trust boundary

A green validation establishes only that synthetic bytes match this proposed receipt profile.
It does **not**:

- verify COSE, DSSE, Sigstore, Rekor, an OCI referrer, or a signer identity;
- establish that a referenced policy or review decision exists or is valid;
- prove that either artifact exists, is unchanged, or is public-safe;
- authorize a lifecycle transition, promotion, release, correction, rollback, or publication;
- replace `PromotionReceipt`, `ReleaseManifest`, `RollbackCard`, `CorrectionNotice`,
  evidence, policy, human review, or a runtime verifier.

## Rollback

Before merge, close the draft pull request and delete its branch. After merge, revert the
additive commit. No runtime receipts, signatures, OCI referrers, lifecycle records, releases,
public artifacts, caches, or indexes are created by this slice.
