<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/signed-rollback-token
title: SignedRollbackToken Contract
type: semantic-contract; rollback readiness; fixture-only
version: v0.1.0
status: proposed; inactive; fixture-only; non-mutating
owners: OWNER_TBD — Release steward · Correction steward · Integrity steward · Signing steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; release; rollback; signature; receipt; fail-closed
related:
  - ./release_alias_verification.md
  - ./cosign_attestation_verification_plan.md
  - ./promotion_receipt.md
  - ../../schemas/contracts/v1/release/signed_rollback_token.schema.json
[/KFM_META_BLOCK_V2] -->

# SignedRollbackToken

A `SignedRollbackToken` is a deterministic, fixture-only readiness record that binds the current immutable release alias state to one verified prior release target, the evidence and policy closure that justify that target, a detached signature-verification reference, and an append-only revert-receipt template.

This contract implements the bounded repository prerequisite described by Pass 22 card `KFM-P22-PROG-0027`. It does **not** sign bytes, verify cryptography, mutate an alias, execute rollback, write a receipt, authorize release, deploy, or publish.

## Relationship to existing release controls

- `ReleaseAliasVerification` remains the preflight authority for comparing an observed alias with an expected prior state and a proposed immutable transition.
- Cosign/Sigstore verification remains outside this validator. A token only becomes internally `READY` when it carries a declared verification result reference, envelope digest, and exact signing-payload digest.
- The rollback token is evidence for a later steward-controlled `ROLLBACK` transition. It is not a second alias writer or release authority.
- A later rollback must append a new revert receipt and advance alias history; it must never rewrite or delete the original promotion record.

## Required closure

A ready token binds:

1. the currently bound release, manifest digest, `spec_hash`, and alias revision;
2. an immutable, verified prior release with a strictly lower alias revision;
3. `EvidenceBundle`, `RunReceipt`, `PolicyDecision`, `PromotionReceipt`, review, and release-alias-verification references;
4. a passing policy outcome and approved review outcome;
5. a declared verified detached signature over the canonical rollback payload; and
6. an append-only revert-receipt template whose source and target exactly match the token.

## Finite outcomes

| Outcome | Meaning | Validator result |
|---|---|---|
| `READY` | The fixture declaration is internally coherent for later governed execution. | `PASS` |
| `HOLD` | Current state, target verification, policy, review, or signature evidence is not yet knowable. | `ABSTAIN` |
| `DENY` | The target is not prior/verified, evidence or review denies, signature closure fails, or the revert receipt does not bind. | `DENY` |
| `ERROR` | An explicit evaluation, current-state, target, policy, review, or signature error is declared. | `ERROR` |

A `PASS` proves only bounded shape, deterministic identity, cross-field closure, and fixture replay. It grants no rollback or publication authority.

## Deterministic identity and signature binding

`signature.subject_digest` is SHA-256 over the RFC 8785 canonical signing payload containing the object/profile identity, issue time, alias reference, current state, rollback target, closure references, and revert-receipt template. Signature evidence and computed results are not part of that signing payload.

`spec_hash` is SHA-256 over the full token after removing `token_id` and `spec_hash`. `token_id` is `kfm:signed-rollback-token:` plus the first 24 lowercase hexadecimal characters of `spec_hash`.

## Directory Rules basis

Meaning belongs in `contracts/release/`; shape in `schemas/contracts/v1/release/`; synthetic cases in `fixtures/contracts/v1/release/`; validation in `tools/validators/release/`; tests in `tests/validators/`; CI in `.github/workflows/`; source adaptation in `docs/intake/exploratory/`; and generated authoring provenance in `data/receipts/generated/`.

No new root or parallel proof, policy, receipt, signing, rollback, release, or publication authority is created.

## Rollback

Revert this additive fixture-only packet. No alias, release object, signature, receipt store, cache, deployment, or public artifact is changed by the packet.
