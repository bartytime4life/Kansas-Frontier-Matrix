<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/verification-state-history
title: VerificationStateHistory Contract
type: contract
version: v0.1.0
status: draft; PROPOSED; bounded-profile
owners: OWNER_TBD - Evidence steward; Correction steward; Contract steward; Schema steward; Validation steward
created: 2026-08-02
updated: 2026-08-02
policy_label: public; evidence; bitemporal; correction-aware; replayable; synthetic-fixtures; no-network; not-release-authority
related:
  - ./README.md
  - ../../schemas/contracts/v1/evidence/verification_state_history.schema.json
  - ../../fixtures/contracts/v1/evidence/verification_state_history/README.md
  - ../../tools/validators/validate_verification_state_history.py
  - ../../tests/schemas/test_verification_state_history.py
  - ../../docs/intake/exploratory/new-ideas-4-14-source-map.md
tags: [kfm, evidence, bitemporal, verification-state, correction, revocation, supersession, replay]
notes:
  - "Implements the bounded offline proof proposed by the New Ideas 4-14 source map; the source PDF is design evidence, not implementation authority."
  - "This profile records verification-state history only. It does not create evidence, policy approval, release authority, publication state, or a public runtime answer."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# VerificationStateHistory Contract

> A bounded, append-ordered, bitemporal history for replaying one subject's verification state as effective at one time and known at another. It prevents late corrections and revocations from silently rewriting what KFM knew earlier.

## Status and authority

| Concern | Posture |
|---|---|
| Semantic contract | **PROPOSED** bounded v1 profile |
| Machine shape | [`verification_state_history.schema.json`](../../schemas/contracts/v1/evidence/verification_state_history.schema.json) |
| Executable behavior | Deterministic fixture validator and replay helper |
| Source evidence | `New Ideas 4-14-26(1).pdf`, pages 374-388, reconciled by the repository source map |
| Data posture | Synthetic fixtures only; no live source, evidence, release, or personal/location data |
| Publication effect | None |

`contracts/evidence/` owns this object's meaning because the record describes the history of a verification judgment. Correction, release, policy, receipts, and proof objects remain references owned by their existing families.

## Purpose

The profile answers a narrow question:

> For subject `S`, what verification state was effective by `effective_as_of`, using only events KFM had recorded by `recorded_as_of`?

Those two time axes must remain separate:

- `effective_at` is when an event applies to the subject.
- `recorded_at` is when KFM recorded the event.

A correction can therefore be effective before it is recorded while remaining invisible to a historical query made before that recording time. Within one transition chain, effective times remain nondecreasing so a successor can never become eligible before the event it replaces.

## Object shape

| Field | Meaning |
|---|---|
| `schema_version` | Closed profile version; v1 is `1.0.0`. |
| `history_id` | Stable identity for this history document. |
| `subject_ref` | The one subject whose verification state is replayed. |
| `profile_id` | Fixed replay profile identity. |
| `spec_hash` | SHA-256 of canonical JSON after removing `spec_hash`. |
| `events` | One bounded append-ordered transition chain. |

Each event contains:

| Field | Meaning |
|---|---|
| `event_id` | Unique event identity inside the document. |
| `event_type` | `VERIFIED`, `REVERIFIED`, `CORRECTED`, `SUPERSEDED`, or `REVOKED`. |
| `state` | `ACTIVE`, `CORRECTED`, `SUPERSEDED`, or `REVOKED`. |
| `effective_at` | UTC instant at which the transition applies. |
| `recorded_at` | UTC instant at which KFM recorded the transition. |
| `reason_code` | Stable, non-narrative reason identifier. |
| `basis_refs` | One or more references supporting why the event was recorded; resolution is outside this profile. |
| `relates_to_event_id` | Prior event replaced or modified by a non-initial transition. |
| `correction_ref` | Required only for `CORRECTED`. |
| `replacement_ref` | Required only for `SUPERSEDED`. |
| `revocation_ref` | Required only for `REVOKED`. |

## Transition rules

The first event must be `VERIFIED` / `ACTIVE`. Every later event points to the immediately preceding event, producing a single reviewable chain rather than an ambiguous graph.

| Prior state | Allowed next event | Resulting state |
|---|---|---|
| `ACTIVE` | `CORRECTED` | `CORRECTED` |
| `ACTIVE` | `SUPERSEDED` | `SUPERSEDED` |
| `ACTIVE` | `REVOKED` | `REVOKED` |
| `CORRECTED` | `REVERIFIED` | `ACTIVE` |
| `CORRECTED` | `SUPERSEDED` | `SUPERSEDED` |
| `CORRECTED` | `REVOKED` | `REVOKED` |
| `REVOKED` | `REVERIFIED` | `ACTIVE` |
| `SUPERSEDED` | none | terminal in this bounded profile |

`effective_at` may precede `recorded_at`, which represents a late-recorded event. It may not follow `recorded_at`; scheduled future transitions are outside this profile.

Effective time is also nondecreasing along the chain. A later recorded transition may describe an earlier point than its own recording time, but it may not become effective before its parent transition. This dependency-closure rule prevents replay from selecting a re-verification while the correction or revocation it claims to remediate is still ineligible.

## Replay rule

For query `(effective_as_of, recorded_as_of)`:

1. Validate the entire document before replay.
2. Keep events where `effective_at <= effective_as_of` and `recorded_at <= recorded_as_of`.
3. Select the last eligible event in append order, ordered by `(recorded_at, event_id)`.
4. Return `UNKNOWN` if no event is eligible.

This rule preserves the distinction between current corrected knowledge and the state that was actually known at an earlier recorded time.

## Runtime boundary

| Replayed state | `ANSWER` posture |
|---|---|
| `ACTIVE` | History does not block `ANSWER`, but evidence, policy, review, release, freshness, and every other applicable gate still may. |
| `CORRECTED` | Blocks `ANSWER` until a later valid `REVERIFIED` event becomes eligible. |
| `SUPERSEDED` | Blocks `ANSWER` for this subject history. Consumers must follow separately governed successor logic. |
| `REVOKED` | Blocks `ANSWER`. |
| `UNKNOWN` | Blocks `ANSWER`; absence of history is not active verification. |

The replay helper exposes `answer_blocked`; it never emits a runtime envelope or upgrades an event into evidence, policy, review, release, or publication authority.

The internal `packages/evidence-resolver/` alpha candidate now consumes this
replay directly. It requires the history subject to equal the candidate
`EvidenceRef` and returns a non-authoritative `UNRESOLVED` result for every
non-`ACTIVE` replay. This is a bounded repository consumer, not a production or
public runtime.

## Determinism and failure behavior

- Event IDs must be unique.
- Events must be ordered by `(recorded_at, event_id)`.
- Effective times must be nondecreasing along the transition chain.
- Every non-initial event must point to the immediately preceding event.
- Event type and state must agree.
- The document is capped at 128 events and the shared bounded JSON parser limits bytes, depth, nodes, duplicate keys, and non-finite numbers.
- Invalid shape, hash, ordering, time, chain, or transition fails closed with stable finding codes.
- Validation and replay require no network access.

## Explicit non-effects

This contract does not:

- resolve `basis_refs` or create an EvidenceBundle;
- define CorrectionNotice, ReleaseManifest, PolicyDecision, ReviewRecord, or receipt semantics;
- infer current truth from a historical event;
- authorize a public `ANSWER`, promotion, release, publication, source activation, or rollback;
- provide a UI timeline; or
- reconstruct history from mutable current rows.

## Validation

```bash
KFM_NO_NETWORK=1 python tools/validators/validate_verification_state_history.py --fixtures
KFM_NO_NETWORK=1 python -m pytest -q tests/schemas/test_verification_state_history.py
```

Expected coverage includes active, corrected, reverified, superseded, revoked, late-recorded, and unknown-history replay plus schema, hash, chain, transition, ordering, timestamp, parser-bound, CLI, and no-network failures.

## Compatibility and rollback

This remains additive and has no production consumer or stored data migration.
Its one bounded internal resolver consumer shares the standard-library replay
implementation with this validator. Rollback is a normal revert of the
resolver integration and shared helper; the contract, schema, and original
history fixtures may remain independently. Historical evidence, release,
correction, and published state are unaffected.

[Back to top](#top)
