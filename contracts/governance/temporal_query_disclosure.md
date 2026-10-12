# TemporalQueryDisclosure

**Status:** PROPOSED fixture-first companion profile  
**Profile:** `kfm.governance.temporal-query-disclosure.v1`  
**Execution mode:** `FIXTURE_ONLY_NO_EXTERNAL_EFFECT`  
**Authority:** `NONE`

## Purpose

`TemporalQueryDisclosure` gives a query-derived output a small, deterministic explanation of **which temporal question was asked** and **which clock supplied the answer**.

It implements the bounded core of KFM-P9-PROG-0033: when temporal semantics affect a public claim, the system should disclose whether the result represents current state, prior state, a valid-time sequence, a nonsequenced transaction-history query, or a tracking log. The companion also discloses whether the calculation used valid time, transaction time, bitemporal state, or release time.

## Relationship to QueryRunRecord

This object references one existing `QueryRunRecord` through `query_run_ref`. It does not replace that record, execute a query, resolve an `EvidenceRef`, decide source authority, evaluate policy, approve review, promote, release, deploy, publish, or create a public claim.

Production API/UI integration remains **HOLD** until a governed query engine can prove that:

- its temporal operator and clock basis match this disclosure;
- snapshot references resolve to immutable or versioned records;
- EvidenceRefs resolve to admissible EvidenceBundles;
- release, correction, withdrawal, and rollback state are visible;
- the public explanation is rendered without upgrading a derivative into truth.

## Query classes

| `temporal_query_type` | Question represented |
|---|---|
| `CURRENT_STATE` | What state is current at the recorded evaluation time? |
| `PRIOR_STATE` | What valid state applied at a named earlier instant? |
| `SEQUENCED` | How did valid state evolve through a bounded interval? |
| `NONSEQUENCED` | How did the recorded transaction history evolve, independent of valid-state sequence? |
| `TRACKING_LOG` | What append-only record history existed through a named transaction cutoff? |

## Time bases

| `time_basis` | Meaning |
|---|---|
| `VALID_TIME` | When the represented fact was valid in the modeled world. |
| `TRANSACTION_TIME` | When KFM recorded or changed the record. |
| `BITEMPORAL` | Both valid and transaction time materially constrain the result. |
| `RELEASE_TIME` | The current released state at evaluation time. |

## Fixed public explanation codes

The profile permits fixed codes rather than arbitrary generated explanation text:

- `CURRENT_STATE_AT_EVALUATION`;
- `PRIOR_VALID_STATE_AS_OF`;
- `VALID_TIME_SEQUENCE`;
- `TRANSACTION_HISTORY_SEQUENCE`;
- `TRACKING_LOG_HISTORY`.

UI copy may later localize these codes through a governed adapter. The fixture profile does not author public prose.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, time precision, class/basis semantics, snapshot/evidence collections, explanation code, deterministic ID, and spec hash verify. |
| `DENY` | A deterministic semantic or integrity rule fails. |
| `ERROR` | Input cannot be read or evaluated safely enough to decide. |

## Directory Rules basis

- `contracts/governance/` owns semantic meaning.
- `schemas/contracts/v1/governance/` owns machine shape.
- `fixtures/` and `tests/` own synthetic proof.
- `tools/generators/` owns deterministic candidate construction.
- `tools/validators/governance/` owns validation.
- `.github/workflows/` owns hosted orchestration.
- `data/receipts/generated/` records AI-authoring accountability.

No new root or parallel query, temporal, evidence, release, proof, or publication authority is created.

## Rollback

Revert the feature commit. No query engine, database, runtime route, public text, source, release, deployment, or published state is changed.
