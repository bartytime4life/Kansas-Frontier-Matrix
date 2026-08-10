# Sensitive-overlay reveal-expiry implementation map

Status: **PROPOSED implementation mapping**

Implementation authority: **NONE**

## Evidence inspected

| Evidence | Truth label | Relevant requirement |
|---|---|---|
| Private research corpus used for candidate discovery | `INTERNAL`; identifiers and content withheld from public provenance | Candidate selection only. It grants no repository, policy, review, release, or publication authority and is not a public citation. |
| `contracts/governance/sensitive_overlay_gatehouse_preflight.md` and its schema, validator, and tests | `CONFIRMED` repository evidence | The existing synthetic preflight already freezes a 24-hour cap, consent and challenge binding, current revocation posture, expiry checks, and no-live-credential boundaries while leaving post-preflight transitions unwired. |
| `docs/doctrine/directory-rules.md` | `CONFIRMED` repository governance | Contracts, schemas, fixtures, validators, workflows, and generated authoring receipts stay in their owning roots. |
| Existing gatehouse profile at base commit `149af17075f7f12d716aa14de439ea22ee6a343e` | `CONFIRMED` repository state | The gatehouse consumes summaries and intentionally leaves post-preflight state transitions, real token/key handling, runtime execution, receipt signing, release, and publication unwired. |

## Implemented mapping

| Source idea | Repository artifact | Boundary |
|---|---|---|
| Reveal-expiry transition semantics | `contracts/governance/sensitive_overlay_reveal_expiry.md` | Defines a pure transition profile, not a live runtime handler. |
| Closed summary shape | `schemas/contracts/v1/governance/sensitive_overlay_reveal_expiry.schema.json` | Accepts hashes and summaries only; raw token/key fields are undeclared. |
| Required negative paths | `fixtures/contracts/v1/governance/sensitive_overlay_reveal_expiry/cases.json` | Covers expired, revoked, stale revocation, stale policy, failed/unknown attestation, consumed/non-single-use token, and TTL overflow. |
| Deterministic transition kernel | `tools/validators/governance/validate_sensitive_overlay_reveal_expiry.py` | Derives `HOLD`, `ABSTAIN`, `DENY`, or input `ERROR`, plus countdown, target view state, and declarative actions without side effects. |
| Regression coverage | `tests/validators/governance/test_sensitive_overlay_reveal_expiry.py` | Freezes case polarity, inclusive expiry, 24-hour cap, cleanup declarations, no-network behavior, and no-secret boundary. |
| CI execution | `.github/workflows/sensitive-overlay-reveal-expiry.yml` | Runs only deterministic local validation and authoring-receipt integrity. |

## Deliberately deferred

- raw token parsing, issuance, storage, rotation, and revocation-ledger access;
- key derivation, retrieval, client storage, cryptographic erasure, and proof of
  erasure;
- live attestation and policy evaluation;
- browser, MapLibre, cache, worker, or HUD integration;
- signed RevealReceipt/AuditReceipt emission;
- live consent or identity service integration;
- job execution, lifecycle mutation, release, deployment, and publication.

The repository follow-on gap is `CONFIRMED`; the exact schema fields, finding
codes, 300-second warning threshold, and pure transition profile are
`PROPOSED` until reviewed. Private discovery materials are neither copied nor
treated as public evidence. Required-action output must not be interpreted as
evidence that any cleanup action occurred.
