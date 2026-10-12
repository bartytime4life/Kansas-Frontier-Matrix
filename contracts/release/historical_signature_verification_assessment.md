<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/historical-signature-verification-assessment
title: Historical Signature Verification Assessment Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Security steward · Release steward · Contract steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; release; security; signature; trust-lifecycle; no-cryptography
owning_root: contracts/
responsibility: Define a bounded assessment that distinguishes trust at signing time from trust at verification time across rotation, expiry, revocation, compromise, supersession, offline material, and trust-policy change without verifying a real signature or authorizing release.
truth_posture: CONFIRMED synthetic validator behavior / PROPOSED inactive historical-verification profile / NEEDS VERIFICATION steward adoption, cryptographic verifier integration, trust policy, and hosted exact-head execution
related:
  - ./release_manifest.md
  - ../../docs/security/KEY_ROTATION.md
  - ../../docs/standards/SIGNING.md
  - ../../schemas/contracts/v1/release/historical_signature_verification_assessment.schema.json
  - ../../fixtures/contracts/v1/release/historical_signature_verification_assessment/cases.json
  - ../../tools/validators/release/validate_historical_signature_verification_assessment.py
  - ../../tests/validators/test_validate_historical_signature_verification_assessment.py
  - ../../docs/intake/exploratory/historical-signature-verification-assessment-source-map.md
tags: [kfm, release, trust-root, signature, rotation, revocation, historical-verification, fixture-only]
notes:
  - "Implements the bounded KFM-TRIAD-056 and KFM-CAND-0166 through KFM-CAND-0168 gap from the Full Atlas."
  - "Fixtures contain synthetic identifiers and verification summaries only; no key, certificate, signature, transparency proof, credential, or production artifact is included."
[/KFM_META_BLOCK_V2] -->

# Historical Signature Verification Assessment Candidate

> A deterministic, fixture-only profile for asking whether a declared signature-verification result is coherent with the trust status recorded at signing time and at later verification time. It performs no cryptography, trust lookup, network request, signing, release, or publication.

## Purpose

Current key status and historical signature validity answer different questions. A key can be active when an artifact is signed and later become verify-only, expired, revoked, compromised, or superseded. Re-evaluating history only against today's status can erase valid lineage; accepting every formerly valid signature can ignore compromise or a changed trust policy.

`HistoricalSignatureVerificationAssessment` binds one artifact digest and signature reference to a signer identity, key identity, signing and verification clocks, trust-profile versions, ordered key-status events, a declared cryptographic-verification summary, offline-material posture, and a mechanically derived review decision.

## Finite decisions

| Decision | Validator result | Meaning |
|---|---|---|
| `VERIFIED_CURRENT` | `PASS` | The declared verification succeeded and the key is active at signing and verification under one profile version. |
| `VERIFIED_HISTORICAL` | `PASS` | The key was active at signing and is now verify-only, expired, or superseded. |
| `REVIEW_REVOKED_AFTER_SIGNING` | `ABSTAIN` | A non-retroactive revocation occurred after signing; owning policy and reviewers must decide treatment. |
| `REVIEW_COMPROMISE` | `ABSTAIN` | A compromise event requires incident-specific review and possible correction or withdrawal. |
| `PROFILE_REEVALUATION_REQUIRED` | `ABSTAIN` | Signing and current verification use different trust-profile versions. |
| `UNKNOWN_TRUST` | `ABSTAIN` | Verification or required offline trust evidence is incomplete. |
| `INVALID_SIGNATURE` | `DENY` | The declared cryptographic-verification summary is failed. |
| `UNAUTHORIZED_AT_SIGNING` | `DENY` | The signer was not authorized or the key was not active at signing. |
| malformed or contradictory packet | `DENY` | Shape, identity, time, event, status, offline-material, decision, or authority invariants failed. |
| `ERROR` or unreadable input | `ERROR` | The bounded assessment could not complete safely. |

`PASS` proves only internal coherence of synthetic declarations. It does not prove a signature, signer identity, trust root, transparency record, claim truth, rights, review sufficiency, release fitness, or publication authority.

## Invariants

1. Artifact digest, signature reference, signer identity, key identity, and trust-profile version remain distinct.
2. Key-status event sequence and effective time are strictly increasing.
3. Status at signing and verification is derived from the latest event effective at each clock and must match the stored snapshots.
4. Signing precedes verification; every event used by a snapshot exists at or before that clock.
5. Only an `ACTIVE` key plus an authorized signer can be authorized at signing.
6. Revoked, compromised, expired, and superseded events retain explicit reasons; supersession names a different key.
7. Offline mode requires a bounded offline-material reference; incomplete evidence cannot pass.
8. Trust-profile version mismatch always requires reevaluation.
9. No raw key, certificate, signature bytes, token, or credential is accepted by the schema.
10. No result authorizes signing, trust mutation, correction, withdrawal, release, deployment, publication, or public use.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the complete candidate after removing only `assessment_id` and `spec_hash`.

```text
spec_hash      = SHA-256(JCS(identity subject))
assessment_id  = kfm:historical-signature:<first 24 digest hex>
```

## Existing-family boundary

- `docs/security/KEY_ROTATION.md` remains draft guidance for custody, rotation, and revocation.
- `docs/standards/SIGNING.md` remains the signing-standard documentation surface.
- `ReleaseManifest` remains the release binding and does not become valid because this assessment passes.
- Real verifier profiles, trust stores, keys, certificates, signatures, transparency proofs, policy, and incident decisions remain outside this fixture.

This contract owns only the missing historical-status reconciliation candidate. It creates no trust-root registry or signing service.

## Directory Rules basis

Release-facing semantic meaning belongs under `contracts/release/`; machine shape under `schemas/contracts/v1/release/`; synthetic cases under `fixtures/contracts/v1/release/`; reusable validation under `tools/validators/release/`; executable evidence under `tests/validators/`; orchestration under `.github/workflows/`; exploratory adaptation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`. No new root or parallel key, identity, policy, proof, release, or publication authority is created.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_historical_signature_verification_assessment
python tools/validators/release/validate_historical_signature_verification_assessment.py --fixtures
```

## Rollback

Before merge, close the draft pull request and remove its branch. After an authorized merge, revert this additive packet. No key, trust store, signature, artifact, release, correction, withdrawal, or publication state requires operational rollback.
