<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/conditional-decision-closure
title: ConditionalDecisionClosure Candidate Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Policy steward · Review steward · Contracts steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/policy/conditional_decision_closure.schema.json
  - ../../fixtures/contracts/v1/policy/conditional_decision_closure/
  - ../../tools/validators/policy/validate_conditional_decision_closure.py
  - ../../tests/validators/test_validate_conditional_decision_closure.py
  - policy_obligation_set.md
  - policy_obligation_reduction.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, policy, conditional-decision, obligation, closure, evidence, waiver, hold]
notes:
  - "This additive profile consumes references to existing obligation candidates; it does not create a competing obligation vocabulary."
  - "CLOSED_FOR_SEPARATE_GATE is not ALLOW and creates no review, promotion, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# ConditionalDecisionClosure Candidate Contract

> **Purpose.** Make the closure state of already-declared conditional obligations explicit and evidence-bound so an open, expired, violated, or unsupported obligation cannot disappear between review and a later governed gate.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Machine shape | `schemas/contracts/v1/policy/conditional_decision_closure.schema.json` |
| Validator | `tools/validators/policy/validate_conditional_decision_closure.py` |
| Policy evaluation or enforcement | None |
| Review, promotion, release, publication, or public-use authority | None |

The strongest passing outcome is `CLOSED_FOR_SEPARATE_GATE`. It means only that the fixture's applicable obligations are recorded in a supported finite closure state. It is never `ALLOW`, review approval, promotion eligibility, release authorization, or publication authorization.

## Source-derived gap and existing-authority integration

Drive Full Atlas `KFM-TRIAD-058` proposes conditional-decision obligation closure. Current repository evidence already includes:

- `PolicyObligationSet`, which carries already-declared duties;
- `PolicyObligationReduction`, which mechanically combines already-issued transform obligations;
- promotion and review fixtures that recognize open obligations as a hold condition.

This slice does not redefine those authorities. It adds one fixture-only closure assessment that references an existing `obligation_set_ref` and a conditional decision. It does not alter the existing schemas, issue obligations, reduce them, or enforce them.

## Directory Rules basis

ADR-0029 adopts responsibility-root placement. This slice uses established homes:

| Responsibility | Path family |
|---|---|
| Policy-object meaning | `contracts/policy/` |
| Machine shape | `schemas/contracts/v1/policy/` |
| Synthetic cases | `fixtures/contracts/v1/policy/` |
| Executable validation | `tools/validators/policy/` |
| Behavior proof | `tests/validators/` |
| Read-only orchestration | `.github/workflows/` |
| Authoring accountability | `data/receipts/generated/` |

No policy bundle, reviewer registry, enforcement engine, source registry, lifecycle store, release home, proof authority, or publication surface is created.

## Obligation closure states

| State | Applicable posture | Closure requirement |
|---|---|---|
| `OPEN` | Blocking | No closure evidence or close time; produces `HOLD`. |
| `SATISFIED` | Closed | Evidence reference and close time required. |
| `WAIVED` | Closed | Evidence reference, close time, and waiver-authority reference required. |
| `EXPIRED` | Blocking | Produces `HOLD`; expiry is not silent satisfaction. |
| `VIOLATED` | Blocking | Produces `HOLD`; violation cannot be upgraded by summary prose. |
| `SUPERSEDED` | Closed | Evidence, close time, and forward supersession reference required. |
| `NOT_APPLICABLE` | Excluded | Allowed only when `applicable=false` with applicability evidence. |

`authority_ref` records the authority asserted by a fixture. This validator checks required presence only; it does not authenticate that authority. A later governed gate must resolve and verify it.

## Deterministic summary

The validator reproduces:

- `blocking_obligation_ids` from applicable `OPEN`, `EXPIRED`, or `VIOLATED` records;
- `closed_obligation_ids` from applicable `SATISFIED`, `WAIVED`, or `SUPERSEDED` records;
- `HOLD` whenever any blocker remains;
- `CLOSED_FOR_SEPARATE_GATE` only when no applicable blocker remains;
- stable reason codes derived from the blocking states;
- RFC 8785 JCS plus SHA-256 identity over all fields except `closure_id` and `spec_hash`.

Arrays are stored sorted and unique. The validator rejects a plausible-looking summary that omits a blocker or upgrades `HOLD`.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, closure evidence, authority-field coherence, deterministic summary, identity, and non-authority checks passed. |
| `DENY` | Shape passed but an obligation-closure or summary invariant failed. |
| `ERROR` | The object or schema could not be evaluated safely. |

These validator outcomes are not policy decisions.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_conditional_decision_closure.py' \
  --verbose

python tools/validators/policy/validate_conditional_decision_closure.py --fixtures
```

## Rollback

Before merge, close the draft PR and delete its branch. After an authorized merge, revert the additive commit. The profile is inactive and has no policy-engine or release consumer, so rollback requires no bundle change, obligation migration, release withdrawal, cache invalidation, or public correction.

## Open verification

- What accepted decision contract issues a conditional approval?
- Which authority registry authenticates a waiver or supersession?
- Which obligation kinds permit waiver, extension, or supersession?
- Which changes reopen downstream assessments and already-built release candidates?
- What receipt proves that an obligation was enforced rather than merely recorded closed?
