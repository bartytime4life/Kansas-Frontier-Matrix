<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/replay-safe-effect-ledger
title: ReplaySafeEffectLedger Candidate Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Runtime steward · Pipeline steward · Contracts steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/runtime/replay_safe_effect_ledger.schema.json
  - ../../fixtures/contracts/v1/runtime/replay_safe_effect_ledger/
  - ../../tools/validators/runtime/validate_replay_safe_effect_ledger.py
  - ../../tests/validators/test_validate_replay_safe_effect_ledger.py
  - ../source/source_event_envelope.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, runtime, event, replay, idempotency, side-effect, ledger, fixture]
notes:
  - "The profile records a synthetic event-to-effect history; it never executes or authorizes an effect."
  - "Exactly-once transport is not claimed. The bounded claim is at-least-once delivery with one recorded idempotent effect."
[/KFM_META_BLOCK_V2] -->

# ReplaySafeEffectLedger Candidate Contract

> **Purpose.** Preserve deterministic event identity, delivery attempts, effect intent, reservation state, and effect history so duplicate delivery cannot be mistaken for duplicate completed work.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Machine shape | `schemas/contracts/v1/runtime/replay_safe_effect_ledger.schema.json` |
| Validator | `tools/validators/runtime/validate_replay_safe_effect_ledger.py` |
| Queue, broker, worker, database, or effect executor | None |
| Lifecycle, review, release, deployment, publication, or public-use authority | None |

A conforming record proves only that one synthetic event/effect history satisfies this bounded contract. It does not prove that a transport provides exactly-once delivery, that an effect ran in production, that its payload is true or admissible, or that any governed transition is authorized.

## Source-derived gap

The Drive-backed Full Atlas identifies `KFM-TRIAD-057` as an open replay-safety seam. Existing repository contracts define source-event identity and require idempotence in several lanes, but the reviewed base contains no common `SideEffectLedger` or equivalent event-to-effect record. This slice implements the smallest fixture-only connective profile from candidates `KFM-CAND-0169` through `KFM-CAND-0171`.

## Directory Rules basis

ADR-0029 adopts responsibility-root placement. This slice uses only existing homes:

| Responsibility | Path family |
|---|---|
| Runtime semantic meaning | `contracts/runtime/` |
| Machine shape | `schemas/contracts/v1/runtime/` |
| Synthetic examples | `fixtures/contracts/v1/runtime/` |
| Executable validation | `tools/validators/runtime/` |
| Behavior proof | `tests/validators/` |
| Read-only orchestration | `.github/workflows/` |
| Authoring accountability | `data/receipts/generated/` |

No root, queue, broker, runtime service, lifecycle store, source registry, release home, receipt authority, proof authority, or publication surface is created.

## Bound object family

The candidate binds four source-proposed concepts in one reviewable fixture profile:

1. `event` — deterministic identity over event type, subject, time, and payload digest;
2. `deliveries` — ordered attempts with predecessor linkage and finite delivery outcomes;
3. `effect_intent` and `reservation` — deterministic idempotency key plus recorded reservation state;
4. `ledger_entries` and `result` — append-ordered effect states and one finite summary.

The profile does not claim that one JSON object is the eventual storage model. Splitting these nested records into separate services or stores requires a reviewed interface and replay design.

## Deterministic identity

- `event_id` is RFC 8785 JCS plus SHA-256 over the event type, subject, occurrence time, and payload digest.
- `effect_key` is the same hash profile over event identity, subject, effect type, and idempotency scope.
- `intent_id` is `kfm:effect-intent:` plus `effect_key`.
- `spec_hash` covers the complete record except `ledger_id` and `spec_hash`.
- `ledger_id` is the first 24 hexadecimal characters of `spec_hash` under `kfm://runtime/replay-safe-effect-ledger/`.

These identities prove reproducible fixture semantics, not authenticity, authorization, or effect completion.

## Replay and effect invariants

A conforming candidate must preserve all of the following:

- delivery attempts are contiguous from 1 and each attempt points to its immediate predecessor;
- delivery and ledger arrays are chronologically ordered;
- every ledger entry references a declared delivery and is recorded no earlier than that delivery's receipt time;
- ledger entry IDs are contiguous from `ledger-entry:0001`, and reason-code arrays are canonical and unique;
- no more than one `COMPLETED` entry exists;
- every `DUPLICATE` delivery has exactly one `DUPLICATE_SUPPRESSED` entry bound to that same delivery, and no suppression is borrowed from another attempt;
- compensation follows exactly one prior completion and is followed by a recorded reservation release;
- the reservation snapshot is reconstructed from the latest `RESERVED`, `COMPLETED`, or `RELEASED` ledger transition rather than inferred from the result label;
- `requested_at <= reserved_at <= effect_completed_at` whenever the corresponding states exist, and snapshot timestamps equal their ledger transition timestamps;
- recorded duplicate and completion counts reproduce the ledger;
- the finite result reproduces the observed history;
- all governance flags remain `false`.

A completed effect may later release its reservation without changing the finite result from `EXECUTED_ONCE` or `DUPLICATE_SUPPRESSED`. A compensated effect must end in a recorded `RELEASED` state. The profile deliberately reports at-least-once delivery with an idempotent effect; it does not make a broader exactly-once claim.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, attempt lineage, per-delivery suppression, causal ordering, effect cardinality, state reconstruction, and non-authority checks passed. |
| `DENY` | The object was shape-valid but a replay/effect invariant failed. |
| `ERROR` | The object or schema could not be evaluated safely. |

These outcomes cannot execute an effect or authorize a lifecycle transition.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_replay_safe_effect_ledger.py' \
  --verbose

python tools/validators/runtime/validate_replay_safe_effect_ledger.py --fixtures
```

The focused workflow also watches `packages/hashing/**` and `pyproject.toml`, because the validator imports the shared RFC 8785 JCS plus SHA-256 implementation and installs declared validation dependencies.

## Rollback

Before merge, close the draft PR and delete its branch. After an authorized merge, revert the additive commit. The profile is inactive, fixture-only, and has no runtime consumer, so rollback requires no queue drain, data migration, release withdrawal, cache invalidation, or public correction.

## Open verification

- Which accepted runtime component, if any, owns effect reservation?
- Which stores support compare-and-set semantics and recovery proof?
- Which effect types require compensation rather than retry?
- How are poison events, partition ordering, and retention governed?
- What evidence would justify a stronger exactly-once claim for any bounded effect?
