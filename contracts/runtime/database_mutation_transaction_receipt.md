<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/database-mutation-transaction-receipt
title: DatabaseMutationTransactionReceiptCandidate Contract
type: semantic-contract; run-receipt-companion-profile
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-mutating; non-authoritative
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; runtime; database; mutation; transaction; receipt
related:
  - ../../schemas/contracts/v1/runtime/database_mutation_transaction_receipt.schema.json
  - ../../fixtures/contracts/v1/runtime/database_mutation_transaction_receipt/cases.json
  - ../../tools/validators/runtime/validate_database_mutation_transaction_receipt.py
  - ./run_receipt.md
  - ./replay_safe_effect_ledger.md
  - ../release/conditional_write_attempt_receipt.md
  - ../../docs/intake/exploratory/pass-18-database-mutation-transaction-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# DatabaseMutationTransactionReceiptCandidate

`DatabaseMutationTransactionReceiptCandidate` is an additive companion profile for an exact `RunReceipt`. It declares one synthetic data-changing relational transaction: its start and end, finite commit/rollback posture, per-statement attempted and affected row counts, and recovery target.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-404`. The source proposes adding transaction outcome fields to database run receipts, while noting that read-only analytical queries should not carry the same burden. This profile therefore embeds the existing `RunReceipt` shape instead of changing or replacing it, and its mutation vocabulary intentionally excludes `SELECT`.

## Status and boundary

| Field | Value |
|---|---|
| Status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY_DECLARATION` |
| Database driver, connection, credentials, SQL text, or query executor | None |
| RunReceipt authentication | None; shape and declared linkage only |
| Policy, review, promotion, release, deployment, publication, or public-use authority | None |

A validator `PASS` proves internal fixture coherence only. It does not prove that a transaction ran, committed, rolled back, affected the declared rows, or can be recovered. Relation references are restricted to a synthetic namespace, SQL text is absent, and every operational and governance authority claim is fixed false.

## Profile surface

| Field | Meaning |
|---|---|
| `profile_spec_hash` | Canonical JSON plus SHA-256 binding over the candidate except this field. |
| `run_receipt` / `run_receipt_digest` | Exact existing `RunReceipt` shape and a digest over that embedded declaration. |
| `transaction` | Transaction ID, `APPLY` or `ROLLBACK_REHEARSAL` mode, UTC boundaries, isolation level, finite outcome, and declared persisted state. |
| `mutations` | Ordered synthetic `INSERT`, `UPDATE`, `DELETE`, or `MERGE` statements with attempted/affected counts and validation refs. |
| `totals` | Replayed statement and row-count totals; no total is trusted merely because it was declared. |
| `recovery_target` | Digest-bound synthetic target with explicit resolution state. The validator does not resolve or authenticate it. |
| `authority_claims` | Fixed declarations that validation is deterministic and no network, database, execution, authentication, lifecycle, or publication effects occurred. |

## Deterministic invariants

- Transaction, receipt-observation, and ordering timestamps use UTC; the transaction must have positive duration and end no later than observation.
- The embedded `RunReceipt` must use stage `database_mutation`, and its outcome must agree with the declared transaction outcome.
- `statement_id` values are contiguous from `statement:0001`; embedded RunReceipt reference arrays are canonical.
- Each affected-row count is no greater than its attempted-row count, and all totals replay from the statement declarations.
- `COMMITTED` requires `APPLY`, `SUCCESS`, and `PERSISTED`.
- `ROLLED_BACK` requires `SUCCESS` and `NOT_PERSISTED`; it is the only valid result for `ROLLBACK_REHEARSAL`.
- `FAILED_BEFORE_COMMIT` requires `FAIL` and `NOT_PERSISTED`.
- `INDETERMINATE` requires `PARTIAL` and `UNKNOWN` and causes validator abstention.
- An unresolved recovery target also causes abstention. Any other coherence failure denies.

These rules validate declaration consistency. They do not authenticate database atomicity, row counts, transaction isolation, logs, backups, snapshots, or restore readiness.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Closed shape, hashes, boundaries, counts, and finite outcome mapping are internally coherent. |
| `ABSTAIN` | The recovery target is unresolved or persisted state is indeterminate. |
| `DENY` | A shape-valid candidate violates hash, time, linkage, count, mode, or outcome invariants. |
| `ERROR` | The candidate fails the closed machine schema. |

These are validator outcomes, not runtime, policy, review, promotion, or release decisions.

## Nearby responsibilities retained

- `RunReceipt` remains the general execution-provenance object.
- `ReplaySafeEffectLedger` remains the event-delivery/idempotent-effect profile; it does not become a relational transaction receipt.
- `ConditionalWriteAttemptReceiptCandidate` remains a release-side HTTP/object-store conditional-write transcript; it does not become a database mutation batch.
- Database migration policy, a production mutation validator, transaction log storage, restore execution, and public auditor projection remain deferred.

## Directory Rules basis

The semantic profile lives under `contracts/runtime/`; machine shape, synthetic fixtures, runtime validator, behavior tests, read-only CI, exploratory source map, and generated authoring receipt stay in their accepted responsibility roots. No new root or database, migration, policy, evidence, release, or publication authority is introduced.

## Validation

```bash
python -m unittest tests.validators.test_validate_database_mutation_transaction_receipt -v
python tools/validators/runtime/validate_database_mutation_transaction_receipt.py --fixtures
```

## Rollback

Close the draft PR and delete its branch before merge, or revert the additive packet after an authorized merge. Because no database is contacted and no transaction is executed, rollback requires no data restore, migration reversal, release withdrawal, cache invalidation, or public correction.
