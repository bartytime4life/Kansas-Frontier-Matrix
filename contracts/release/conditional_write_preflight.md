<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/conditional-write-preflight
title: ConditionalWritePreflightCandidate Contract
type: semantic-contract; release-preflight-candidate; fixture-first
version: v0.1.0
status: proposed; inactive; no-network; non-mutating
owners: OWNER_TBD — release steward · policy steward · validation steward · storage steward
created: 2026-08-06
updated: 2026-08-06
policy_label: internal; fixture-only; no-authority
related:
  - ../../schemas/contracts/v1/release/conditional_write_preflight.schema.json
  - ../../tools/validators/release/validate_conditional_write_preflight.py
  - ../../fixtures/contracts/v1/release/conditional_write_preflight/
  - ../../docs/intake/exploratory/new-ideas-3-11-26-conditional-write-preflight-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, release, conditional-write, optimistic-concurrency, etag, cas, fixture-only]
[/KFM_META_BLOCK_V2] -->

# ConditionalWritePreflightCandidate

> A `ConditionalWritePreflightCandidate` is a deterministic, fixture-only evaluation of an optimistic create-if-absent or replace-if-match condition. It may propose a later write request, suppress an idempotent replay, identify a concurrency conflict, or hold for incomplete upstream closure. It never contacts the target, resolves external state, emits a request, performs a write, changes lifecycle state, creates a release, deploys, publishes, or authorizes public use.

## Why this is a separate object

The source packet proposes an optimistic conditional publish using HTTP `If-Match`/ETag or object-store compare-and-swap after policy gates. The repository already has source normalization, policy/review objects, promotion decisions, release manifests, rollback records, and release validators. This slice does not collapse those authorities into a network writer.

Instead it models only the decision boundary immediately before a governed storage adapter could be asked to act:

```text
released-candidate declarations
  -> fixture-only conditional-write preflight
  -> PROPOSE_WRITE | NO_ACTION | CONFLICT | HOLD
  -> later adapter and operational receipt (out of scope)
```

A preflight result is process memory, not a storage transaction or release record.

## Status and authority boundary

| Field | Value |
|---|---|
| Status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Supported operations | `CREATE_IF_ABSENT`, `REPLACE_IF_MATCH` |
| External state resolution | None |
| Network or write effect | None |
| Policy/review/promotion authority | None; fixture declarations are not authenticated |
| Release/publication authority | None |

## Directory Rules basis

ADR-0029 adopted Directory Governance Standard v2. The implementation is routed by responsibility:

| Responsibility | Home |
|---|---|
| Release-side preflight meaning | `contracts/release/` |
| Machine shape | `schemas/contracts/v1/release/` |
| Synthetic examples | `fixtures/contracts/v1/release/` |
| Repository validation | `tools/validators/release/` |
| Executable proof | `tests/validators/release/` |
| Read-only CI | `.github/workflows/` |
| Source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root, writer, source registry, policy bundle, lifecycle lane, receipt authority, proof store, release manifest family, or public route is created.

## Input declarations

### Target state

The candidate names one logical `target_ref` and declares one operation:

- `CREATE_IF_ABSENT` models a later `If-None-Match: *` request;
- `REPLACE_IF_MATCH` models a later `If-Match: <etag>` request.

The fixture supplies an observed state of `ABSENT` or `PRESENT`. A present target carries an observed ETag and content digest; an absent target carries neither. The validator does not fetch or authenticate these values.

### Proposed content

The request declaration binds:

- expected ETag when replacement is requested;
- proposed content digest;
- proposed byte length;
- content type; and
- deterministic idempotency key.

No content bytes are stored in the candidate.

### Upstream closure declarations

The candidate carries references and declared states for:

- policy decision;
- review record;
- promotion decision;
- release-manifest candidate; and
- rollback target.

The preflight holds when declared closure is incomplete. It does not resolve, authenticate, or replace any referenced object.

## Deterministic outcomes

### `PROPOSE_WRITE`

Emitted only when declared upstream closure is complete and the declared optimistic condition is satisfied:

- create-if-absent with an absent target; or
- replace-if-match with a present target whose observed ETag equals the expected ETag.

This outcome proposes that a separate governed adapter may construct a request. It does not emit one.

### `NO_ACTION`

Emitted when the target already declares the same content digest as the proposed content. This makes replay idempotent even when an old ETag was supplied. No mutation is needed.

### `CONFLICT`

Emitted when target state does not satisfy the declared operation:

- create-if-absent sees an existing target;
- replace-if-match sees an absent target; or
- replace-if-match sees a different ETag.

The preflight never falls back to an unconditional overwrite.

### `HOLD`

Emitted when policy, review, promotion, release-manifest, or rollback declarations are incomplete or non-approving. Blocking declarations dominate target-state analysis.

## Identity

The candidate uses the repository RFC 8785 JCS plus SHA-256 implementation.

- `idempotency_key` binds target reference, operation, and proposed content digest.
- `condition_fingerprint` binds target reference, operation, observed state, observed ETag, and expected ETag.
- `spec_hash` binds the complete candidate except `intent_id` and `spec_hash`.
- `intent_id` is `kfm:conditional-write-intent:<spec_hash hex>`.

Changing target state, request identity, upstream declarations, derived outcome, or no-authority claims changes the candidate identity.

## Claims and non-effects

The schema fixes these claims:

- deterministic preflight is true;
- network access is false;
- external state resolution is false;
- upstream authority verification is false;
- write request emission is false;
- write and lifecycle mutation are false;
- release creation, publication, and public-use authorization are false.

A green result is not an operational run receipt, proof, policy decision, review approval, promotion authorization, release manifest, or storage response.

## Validation and rollback

The validator checks closed Draft 2020-12 shape, target/condition coherence, exact outcome derivation, blocker dominance, idempotency, deterministic hashes, fixed no-effect claims, and fixture polarity. Diagnostics return stable codes and JSON paths without reflecting candidate values.

Before merge, rollback is branch or pull-request deletion. After an authorized merge, revert the additive implementation commit or merge commit. Because the profile is inactive and non-mutating, no source, storage object, lifecycle record, cache, release, deployment, or public product requires cleanup.
