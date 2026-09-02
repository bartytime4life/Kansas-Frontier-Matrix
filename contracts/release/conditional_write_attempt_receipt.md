<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/conditional-write-attempt-receipt
title: ConditionalWriteAttemptReceiptCandidate Contract
type: semantic-contract; release-attempt-receipt-candidate; fixture-first
version: v0.1.0
status: proposed; inactive; no-network; non-authoritative
owners: OWNER_TBD — release steward · storage steward · validation steward · security steward
created: 2026-08-07
updated: 2026-08-07
policy_label: internal; fixture-only; no-authority
related:
  - ./conditional_write_preflight.md
  - ../../schemas/contracts/v1/release/conditional_write_attempt_receipt.schema.json
  - ../../tools/validators/release/validate_conditional_write_attempt_receipt.py
  - ../../fixtures/contracts/v1/release/conditional_write_attempt_receipt/
  - ../../docs/intake/exploratory/new-ideas-3-11-26-conditional-write-attempt-receipt-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, release, conditional-write, attempt-receipt, optimistic-concurrency, etag, cas, fixture-only]
[/KFM_META_BLOCK_V2] -->

# ConditionalWriteAttemptReceiptCandidate

> A `ConditionalWriteAttemptReceiptCandidate` deterministically evaluates one declared conditional-write attempt against an exact, valid `ConditionalWritePreflightCandidate`. It records a fixture transcript and derives `APPLIED`, `NO_ACTION`, `CONFLICT`, `HOLD`, or `ERROR` without contacting a target or authenticating that the declared request, response, or after-state occurred.

## Why this is separate

The existing preflight ends at a non-authoritative proposal:

```text
ConditionalWritePreflightCandidate
  -> PROPOSE_WRITE | NO_ACTION | CONFLICT | HOLD
  -> later adapter and operational receipt
```

The source packet proposes the next mechanics: conditional `PUT` using `If-None-Match: *` or `If-Match`, explicit handling of `409`/`412`, idempotent replay, and a run receipt after the attempt. This profile implements only the deterministic receipt-candidate boundary. It does **not** add a live writer, credential path, external-state resolver, attestation executor, or publication workflow.

## Status and authority

| Field | Value |
|---|---|
| Status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY_DECLARATION` |
| Upstream dependency | exact valid `ConditionalWritePreflightCandidate` |
| Network/request/write effect | none |
| External-state or execution authentication | none |
| Release/publication authority | none |

`APPLIED` means only that the declared transcript is internally consistent with the preflight and the admitted response pattern. The schema fixes `subject_execution_authenticated`, `write_verified`, `lifecycle_write_verified`, `published`, and `public_use_authorized` to `false`.

## Directory Rules basis

ADR-0029 adopted Directory Governance Standard v2. The object remains in existing responsibility roots:

| Responsibility | Home |
|---|---|
| Release-side attempt-receipt meaning | `contracts/release/` |
| Machine shape | `schemas/contracts/v1/release/` |
| Synthetic examples | `fixtures/contracts/v1/release/` |
| Deterministic validation | `tools/validators/release/` |
| Executable proof | `tests/validators/release/` |
| Read-only CI | `.github/workflows/` |
| Source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No writer, transport, source registry, lifecycle lane, policy bundle, proof store, release-manifest family, or public route is created.

## Attempt transcript

The candidate embeds the exact preflight object and declares:

- fixture attempt time and adapter identifier;
- transport class: `NONE`, `HTTP`, or `OBJECT_STORE`;
- whether a request was declared;
- method, exact conditional headers, request digest, and request length;
- response status, ETag, and content digest when present;
- a finite transport-error class when no response was received; and
- declared after-state: `ABSENT`, `PRESENT`, or `UNKNOWN`.

The validator never resolves any of these fields against an external service.

## Finite derivation

| Preflight / transcript | Result | Rule |
|---|---|---|
| `HOLD` | `HOLD` | No attempt is admitted. |
| preflight `CONFLICT` | `CONFLICT` | No attempt is admitted. |
| `NO_ACTION` with matching declared after-content | `NO_ACTION` | Replay is idempotent. |
| `PROPOSE_WRITE` + exact conditional request + admitted success response + matching after-state | `APPLIED` | Transcript is internally consistent only. |
| `PROPOSE_WRITE` + `409` or `412` | `CONFLICT` | No unconditional-overwrite fallback. |
| transport failure, omitted required request, response/after-state disagreement, or header/body drift | `ERROR` | Fail closed. |

Blockers recorded by the preflight always dominate. A receipt candidate cannot upgrade `HOLD`, `CONFLICT`, or `NO_ACTION` into an applied result.

## Deterministic identity

The repository RFC 8785 JCS plus SHA-256 implementation computes:

- `attempt_fingerprint` over the exact preflight identity and complete attempt transcript;
- `spec_hash` over the complete receipt candidate except its self-identifiers; and
- `receipt_id = kfm:conditional-write-attempt-receipt:<spec_hash hex>`.

Changing the preflight, target, request condition, declared response, after-state, result, or no-effect claims changes the identity.

## Non-effects

A passing candidate is not an authenticated storage receipt, `RunReceipt`, proof, signature, policy decision, review approval, promotion authorization, release manifest, deployment record, or publication record. It performs no network, credential, request, write, lifecycle, release, deployment, or public-use action.

## Validation and rollback

The validator composes the existing preflight validator, checks exact transcript/result derivation, canonical ordering, attempt/spec identity, and fixed no-effect claims. Diagnostics expose stable codes and paths without echoing candidate values.

Before merge, rollback is closing the pull request and deleting the branch. After an authorized merge, revert the additive implementation commit or merge commit. No source, target object, lifecycle record, cache, release, deployment, or public product requires cleanup.
