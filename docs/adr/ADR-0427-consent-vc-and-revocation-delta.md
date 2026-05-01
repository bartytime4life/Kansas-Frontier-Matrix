# ADR-0427: Consent VC + Revocation Delta v1

## KFM Meta Block v2
- status: draft
- verification: PROPOSED
- owners: governance/policy/runtime
- date: 2026-05-01
- scope: consent issuance placeholder, deterministic revocation delta, downstream suppression/recompute signaling

## Context
KFM needs a fail-closed governance slice that can issue consent as a verifiable-credential placeholder, carry consent obligations into evidence and receipts, and deterministically derive revocation deltas without any live network or Sigstore dependency.

## Decision
Define and implement a local-only Consent VC + Revocation Delta v1 posture with deterministic stubs:

- `consent_vc_id`: stable issued credential identifier (`consent_vc_<hex>`).
- `obligations_snapshot_hash`: sha256 of canonical JSON obligations snapshot.
- `revoke_delta_id`: deterministic HMAC identifier from token-derived key and revocation inputs.

Deterministic revocation derivation:
1. derive key using HKDF-like HMAC:
   - `prk = HMAC("kfm:revoke:v1", revocation_token)`
   - `k = HMAC(prk, "kfm:revoke:v1:id")`
2. message = `prior_spec_hash + "|" + delta_timestamp`
3. `revoke_delta_id = "rvk_" + HMAC(k, message).hex()`

No-network posture:
- issuance/revocation use local deterministic signing stub only.
- no remote identity, Sigstore, OIDC, DID, or VC status-list calls.
- all tests run from local fixtures.

## Consequences
- preserves proof/receipt/evidence/revoke-manifest separation.
- enables deterministic testability and replay.
- keeps `revocation_token` private (never serialized in public outputs).

## Privacy and rollback notes
- Revocation tokens are treated as secrets and are excluded from EvidenceBundle, run_receipt, and RevokeDelta artifacts.
- rollback is performed by replaying prior non-revoked specs and emitting a new receipt that references the applicable `revoke_delta_id` and suppression/recompute action.

## NEEDS_VERIFICATION
- Canonical schema authority for generic `EvidenceBundle.v1.json` and `run_receipt.v1.json` in this repo appears absent/ambiguous; this ADR introduces v1 canonical files under `schemas/evidence` and `schemas/receipts` as PROPOSED pending cross-lane ratification.
