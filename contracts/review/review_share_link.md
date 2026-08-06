# ReviewShareLink Contract

**Status:** PROPOSED fixture profile  
**Object family:** `ReviewShareLink`  
**Source basis:** *New Ideas 4-10-26.pdf* — time-bounded review sharing, expiration, revocation, schema validation, and append-only share receipts  
**Directory Rules basis:** review meaning belongs under `contracts/review/`; machine shape belongs under `schemas/contracts/v1/review/`; enforcement belongs under `tools/validators/review/`.

## Purpose

Define a deterministic, no-network record for a bounded review-context share link without storing the bearer token itself. The record binds a SHA-256 token digest to a released or review-authorized context, an audience class, expiration/revocation timestamps, a finite state, and an exact decision.

This contract is a prerequisite for a later role-gated API or review-shell feature. It does **not** create a public link service, authorize access, persist a live secret, prove review, approve release, or publish any KFM artifact.

## Required semantics

- `token_hash` stores only `sha256:<hex>`; a plaintext bearer token is outside this object and must not be committed.
- `context` identifies at least one governed locator: `release_id`, `decision_envelope_ref`, or `manifest_ref`.
- Context references are limited to governed relative routes (`/api/`, `/release/`, `/reports/`) or `kfm://` identifiers.
- Direct references to `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, canonical data stores, or proof internals are denied.
- `evaluated_at` makes expiration and revocation evaluation deterministic and replayable.
- State precedence is `REVOKED` over `EXPIRED` over `ACTIVE`.
- `decision.reasons` is the exact sorted reason set derived by the validator.
- `decision.outcome` is `ALLOW` only for an active link with no reason; all other states are `DENY`.
- `spec_hash` is SHA-256 over canonical JSON with the top-level `spec_hash` member omitted.

## Finite reasons

| Reason | Meaning |
|---|---|
| `LINK_EXPIRED` | `evaluated_at` is at or after `expires_at`. |
| `LINK_REVOKED` | `revoked_at` is at or before `evaluated_at`. |
| `UNSAFE_CONTEXT_REF` | A context reference bypasses governed routes or targets an internal lifecycle/proof path. |

## Governance boundary

The fixture profile requires:

```json
{
  "fixture_only": true,
  "plaintext_token_stored": false,
  "public_access": false,
  "lifecycle_write": false,
  "release_authority": false
}
```

A schema-valid object remains a candidate record. A production service still requires authentication, authorization, secret handling, persistence, audit receipts, policy review, rate limits, correction behavior, and release-specific review.

## Validation and rollback

Run:

```bash
python -m pytest tests/validators/review/review_share_link/test_validate_review_share_link.py -q
python tools/validators/review/review_share_link/validate_review_share_link.py \
  fixtures/review/review_share_link/valid/active.json
```

Rollback is ordinary Git reversion of this fixture-only family. No runtime, stored token, release, deployment, or public route is introduced.
