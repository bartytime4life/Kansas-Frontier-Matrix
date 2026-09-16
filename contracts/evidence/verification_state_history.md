<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/verification-state-history
title: VerificationStateHistory Contract
type: contract
version: v0.2.0
status: draft; PROPOSED; bounded-profile
owners: OWNER_TBD - Evidence steward; Correction steward; Contract steward; Schema steward; Validation steward
created: 2026-08-02
updated: 2026-09-16
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
| `schema_version` | Closed profile version; legacy is `1.0.0`, proposed synthetic Atlas is `1.1.0`. |
| `history_id` | Stable identity for this history document. |
| `subject_ref` | The one subject whose verification state is replayed. |
| `profile_id` | Fixed replay profile identity. |
| `spec_hash` | SHA-256 of canonical JSON after removing `spec_hash`. |
| `events` | One bounded append-ordered transition chain. |

## Explicit subject profiles

The schema and standard-library parser admit exactly these combinations:

| `schema_version` | `profile_id` | `subject_ref` |
|---|---|---|
| `1.0.0` | `kfm://profile/verification-state-replay/v1` | Existing `kfm://` grammar, unchanged. |
| `1.1.0` | `kfm://profile/verification-state-replay/atlas-fixture/v1alpha1` | Literal `overlay:synthetic-kansas-promotion-proof` only. |

The second combination is **PROPOSED / SYNTHETIC FIXTURE REVIEW ONLY**. Its
implementation allows a compatibility proposal to be tested; it does not record
an accepted verification judgment. Version/profile mixing, unknown versions,
other `overlay:` subjects, case changes, URI encoding, whitespace, aliases and
normalization are rejected. Existing v1 histories continue to reject `overlay:`.
All event IDs, supporting references, correction/replacement/revocation
references, event limits, hashes, ordering and replay rules remain unchanged.

The literal subject is already the original synthetic Atlas carrier's candidate
identity and the full EvidenceBundle's member reference. This profile preserves
those bytes and exact EvidenceRef equality. It does not create a general alias
registry or widen the shared `kfm_ref` definition. The opaque Atlas lookup
selector, EvidenceBundle ID and verification-history subject remain distinct.

The [synthetic profile fixture](../../fixtures/contracts/v1/evidence/verification_state_history/valid/valid_atlas_fixture_profile.json)
contains invented, visibly synthetic events and basis references solely to test
replay. It is not operational evidence, a review decision, a signed verification
record, or authority to render the Atlas. The fixed lookup does not load this
history, select this profile, construct a candidate request or evaluate policy.
Its diagnostic remains a HOLD, now named
`atlas-lookup/verification-profile-review-required`.

Review acceptance must confirm this closed profile/version pair, original byte
and identity preservation, schema/parser parity, negative collision cases,
unchanged v1 semantics, same-subject correction/revocation replay and the absence
of public-answer authority. The [profile tests](../../tests/schemas/test_atlas_verification_profile.py)
exercise the original bundle through the pure candidate evaluator using only
test-supplied context. Internal `RESOLVED` still projects to non-renderable
`CONTINUE_GOVERNED_CHECKS`; it does not establish server-owned policy, rights,
review, release, citation or correction context.

After independent contract review, the next implementation boundary is the
server-owned selection and integrity binding of those records to the same
subject, with missing/stale/revoked cases failing closed, followed by positive
real API/browser and operational recovery proof. Passing the profile tests does
not satisfy those later gates. No new policy outcome, source admission or
production history store is introduced here.

## Event shape

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
KFM_NO_NETWORK=1 python -m pytest -q tests/schemas/test_atlas_verification_profile.py
```

Expected coverage includes active, corrected, reverified, superseded, revoked, late-recorded, and unknown-history replay plus schema, hash, chain, transition, ordering, timestamp, parser-bound, CLI, and no-network failures.

## Compatibility and rollback

This remains additive and has no production consumer or stored data migration.
Its one bounded internal resolver consumer shares the standard-library replay
implementation with this validator. Rollback is a normal revert of the
resolver integration and shared helper; the contract, schema, and original
history fixtures may remain independently. Historical evidence, release,
correction, and published state are unaffected.

The proposed `1.1.0` profile is opt-in, not a migration or default upgrade.
The canonical schema home and existing validator entrypoint stay the same;
there is no new registry or parallel schema. Legacy histories and the original
Atlas carrier, reference and bundle are preserved. The profile has no production
consumer and no operational history is issued. Reverting its schema/parser,
synthetic fixtures, tests and documentation returns to the legacy-only behavior.
Do not coerce a `1.1.0` record into `1.0.0` on rollback: unsupported profiles must
fail closed, and any previously retained record remains historical.

[Back to top](#top)
