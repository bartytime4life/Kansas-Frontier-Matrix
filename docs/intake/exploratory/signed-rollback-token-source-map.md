# SignedRollbackToken source and adaptation map

## Status

**PROPOSED_INACTIVE.** This packet adds fixture-only rollback-token readiness infrastructure. It does not create a live token, execute cryptography, repoint an alias, issue a rollback, write a revert receipt, deploy, or publish.

## Source basis

The attached KFM Pass 22 atlas identifies `KFM-P22-PROG-0027` as a new candidate: each promotion should create a signed rollback token or card that can return the current alias to a verified prior `spec_hash` and write a new revert receipt. The atlas calls for repository-path verification and a small fixture-backed implementation with schema, validator, policy closure, receipt/proof binding, and rollback tests before adoption.

## Current repository fit verified at main `9c080014926e6f3ba4dc630eaf7a615fff46c7fc`

- `contracts/release/release_alias_verification.md` already models non-mutating alias transition preflight, including `ROLLBACK`.
- `contracts/release/cosign_attestation_verification_plan.md` already owns the version-pinned signature-verification planning boundary.
- `contracts/release/promotion_receipt.md` and existing evidence/run/policy references already own promotion provenance.
- Repository search found rollback stores and runbooks, but no first-class `SignedRollbackToken` contract/schema/validator family.

The new family therefore binds existing release controls instead of creating a competing alias writer, signer, policy engine, or receipt authority.

## Adaptation decisions

1. Model the token as a deterministic readiness declaration, not an executable credential.
2. Require an immutable prior target with a lower alias revision than the current binding.
3. Require EvidenceBundle, RunReceipt, PolicyDecision, PromotionReceipt, review, and alias-verification references.
4. Require passing policy and approved review states; map insufficient evidence to `HOLD`, denials to `DENY`, and explicit failures to `ERROR`.
5. Bind a detached declared signature to an exact canonical signing payload without running Cosign or dereferencing external evidence.
6. Require an append-only revert-receipt template that advances alias history and preserves the original promotion record.
7. Keep every governance effect false and retain `authority: NONE` in validator output.

## Acceptance criteria

- Draft 2020-12 schema meta-validation passes.
- Deterministic `spec_hash`, `token_id`, and signing-payload digest replay exactly.
- Positive fixture proves current-to-prior binding and revert-receipt closure.
- Negative fixtures cover non-prior targets, same-target rollback, unverified targets, policy/review denial, missing/invalid signature evidence, subject mismatch, receipt mismatch, identity drift, and authority overreach.
- `PASS`, `ABSTAIN`, `DENY`, and `ERROR` all have fixture polarity.
- Validator contains no host or network client and performs no external verification.
- Generated authoring receipt binds the final artifact bytes.

## Future integration boundary

A separate reviewed change may connect a cryptographically verified signature result, construct a `ReleaseAliasVerification` `ROLLBACK` preflight, perform an authorized conditional alias write, and append the resulting revert receipt. That work must preserve immutable release targets, exact prior-state comparison, review and policy authority, correction lineage, and rollback of the implementation itself.

## Non-effects

No signature is created or verified; no alias is changed; no rollback or promotion is authorized; no receipt is written; no deployment or publication occurs.
