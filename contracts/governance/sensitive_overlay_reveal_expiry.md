# Sensitive-overlay reveal-expiry assessment contract

Status: **PROPOSED fixture profile**

Repository follow-on: `SensitiveOverlayGatehousePreflight`

Profile: `kfm.sensitive-overlay-reveal-expiry.fixture.v1`

## Purpose

`SensitiveOverlayRevealExpiryAssessment` is a pure, deterministic transition
kernel over a synthetic reveal-lease summary. It derives an active, expiring,
expired, revoked, or denied state and declares the actions a runtime handler
would need to perform.

The profile exists to freeze fail-closed behavior before any live token, key,
attestation, revocation ledger, browser storage, map UI, or audit-receipt
integration is authorized.

## State and outcome model

| State | Outcome | Required posture |
|---|---|---|
| `ACTIVE` | `HOLD` | Keep the countdown visible and schedule invalidation; no reveal authority is granted. |
| `EXPIRING` | `HOLD` | Keep the countdown visible, warn, and schedule invalidation. |
| `EXPIRED` | `DENY` | Declare key discard, overlay removal, blurred-view restoration, and audit-receipt emission as required actions. |
| `REVOKED` | `DENY` | Declare the same fail-closed cleanup actions immediately. |
| `ABSTAINED` | `ABSTAIN` | Unknown revocation or attestation evidence cannot support a reveal; declare cleanup and restore blur without asserting a violation. |
| `DENIED` | `DENY` | Apply the cleanup action set for stale revocation, stale policy, failed attestation, consumed or non-single-use token, invalid interval, or TTL over 24 hours. |

Actions are declarative output only. This repository slice does not execute any
action and does not claim cleanup occurred.

## Frozen rules

- Only SHA-256 summaries are accepted for the reveal token, challenge, and
  policy bindings; raw token and key material are denied.
- The lease must be single-use and at most 24 hours from issuance to expiry.
- The revocation summary must be current at the exact assessment time.
- Revocation status and the explicit revoked flag must agree.
- Attestation must be `VERIFIED` and the lease policy hash must match the
  current policy hash. Unknown attestation or revocation evidence abstains;
  explicit failure or stale binding denies.
- Expiry is inclusive: `evaluated_at >= expires_at` is expired.
- The expiring window is the final 300 seconds of a valid lease.
- A consumed single-use token can never return to an active state.

## Responsibility signature

| Responsibility | Owner |
|---|---|
| Transition meaning | `contracts/governance/` |
| Closed machine shape | `schemas/contracts/v1/governance/` |
| Synthetic fixture inputs | `fixtures/contracts/v1/governance/sensitive_overlay_reveal_expiry/` |
| Deterministic validation | `tools/validators/governance/` |
| Regression tests | `tests/validators/governance/` |
| Live consent, tokens, keys, revocation, attestation, UI cleanup, receipts, release, and publication | Their owning services and governed roots; not this profile |

## Non-effects

Validation performs no network access, token parsing, signature verification,
key retrieval, decryption, cache invalidation, UI mutation, audit-receipt write,
policy decision, job execution, release, deployment, or publication. `HOLD`
means only that the synthetic summary is internally eligible to remain in an
already-revealed fixture state pending real authority.

## Relationship to the gatehouse preflight

The existing `SensitiveOverlayGatehousePreflight` checks synthetic consent,
identity, data-use, and tile-egress summaries before a hypothetical reveal.
This profile begins at a later, still synthetic boundary: a hashed lease
summary already exists and must transition safely. Neither profile produces or
accepts a live credential.

Source mapping and deferred dependencies are recorded in
`docs/intake/exploratory/pass-32-sensitive-overlay-reveal-expiry-source-map.md`.
