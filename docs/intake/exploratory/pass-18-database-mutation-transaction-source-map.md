<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-database-mutation-transaction
title: Pass 18 Database Mutation Transaction Receipt Source Map
type: exploratory-intake; implementation-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; source-lineage; runtime; database; mutation
related:
  - ../../../contracts/runtime/database_mutation_transaction_receipt.md
  - ../../../schemas/contracts/v1/runtime/database_mutation_transaction_receipt.schema.json
  - ../../../fixtures/contracts/v1/runtime/database_mutation_transaction_receipt/cases.json
  - ../../../contracts/runtime/run_receipt.md
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Database Mutation Transaction Receipt Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical page 273 / printed page 270 | Card `KFM-P18-INV-404` proposes receipts for database mutation batches that state transaction boundaries, commit/rollback outcome, affected row counts, and recovery target. It names `RunReceipt`, database migration policy, mutation validator, and rollback target as dependencies and distinguishes read-only queries. | `CONFIRMED` |
| Connected Drive copy `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`, modified `2026-05-17T16:04:12Z`) | The connected source preserves the same Pass 18 planning corpus and proposal posture. | `CONFIRMED` for connected source identity and corpus availability; card wording validated from the supplied rendered page |
| `main@149af17075f7f12d716aa14de439ea22ee6a343e` | Exact searches found general `RunReceipt`, replay-safe effect-ledger, release-side conditional-write, and graph-migration surfaces, but no `KFM-P18-INV-404`, `transaction_outcome`, database mutation transaction receipt/profile, matching validator, fixtures, workflow, or PR history. | `CONFIRMED` for the inspected snapshot |

The supplied and Drive artifacts are proposal evidence, not repository instruction authority. The source-attributed `Advanced-SQL-Concepts.pdf` was not supplied or independently verified, so this implementation relies only on the bounded planning statement and established repository contracts. No external database, driver, package, version, rights, or runtime claim is made.

## Reconciliation and selected increment

The repository already owns general execution provenance in `contracts/runtime/run_receipt.md`. It also has nearby but distinct fixture profiles:

- `ReplaySafeEffectLedger` records event delivery, idempotency reservation, and effect history;
- `ConditionalWriteAttemptReceiptCandidate` records a declared HTTP/object-store conditional write on the release side; and
- `GraphMigrationDeclarationCandidate` governs a graph migration declaration.

None records relational transaction boundaries, finite commit/rollback posture, per-statement row counts, and a recovery target while composing the existing `RunReceipt`. The selected increment is therefore a companion profile, not a canonical `RunReceipt` schema change and not a database executor.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| State transaction boundaries. | UTC `began_at` / `ended_at` with positive duration and receipt-observation ordering. | No transaction start, commit, rollback, log read, or clock attestation. |
| Record commit or rollback outcome. | Finite outcome mapped to existing `RunReceipt.outcome` and declared persisted state. | No outcome authentication or database atomicity proof. |
| Record affected row counts. | Ordered synthetic mutation statements and replayed totals. | No SQL text, query plan, table discovery, count query, or production relation reference. |
| Name a recovery target. | Digest-bound synthetic target with explicit resolved/unresolved state. | No backup discovery, restore test, recovery execution, or recovery authority. |
| Avoid burdening read-only analysis. | Closed mutation vocabulary contains only `INSERT`, `UPDATE`, `DELETE`, and `MERGE`; fixtures prove `SELECT` rejection. | No read-only query receipt or analytical query runner. |
| Remain downstream of governance and release. | All operational and authority effects fixed false. | No policy/review decision, promotion, release, deployment, publication, or public-use authorization. |

## Deferred questions

- Which accepted database-migration policy should a future active profile reference?
- Which component may authenticate transaction log position and affected-row counts?
- What recovery-target type is sufficient for each datastore and mutation materiality class?
- Which fields, if any, may be projected to public release auditors without exposing sensitive schema or operational details?
- Should an active implementation extend `RunReceipt` directly or preserve a separately versioned companion profile?

These decisions require separate source, security, runtime, policy, and steward review.

## Validation and rollback

Focused validation covers the embedded RunReceipt schema, canonical hashes, UTC boundaries, statement identity/order, exact count totals, affected-versus-attempted bounds, commit/rollback/failure/indeterminate mapping, recovery-target abstention, read-only rejection, and closed-field rejection.

Rollback is a focused revert of this additive packet. It cannot require data recovery because it contains no database connector, SQL, credentials, mutation command, or live transaction effect.
