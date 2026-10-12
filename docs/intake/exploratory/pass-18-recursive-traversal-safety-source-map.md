<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-recursive-traversal-safety-source-map
title: Pass 18 Recursive Traversal Safety Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Query steward · Evidence steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; recursive-cte; traversal; safety
responsibility: Reconcile one supplied recursive-query idea with current repository evidence while preserving query, database, evidence, policy, review, release, and publication boundaries.
truth_posture: "CONFIRMED supplied-card and bounded repository gap; PROPOSED inactive implementation profile; UNKNOWN runtime adoption; NEEDS VERIFICATION dialect behavior, human review, and hosted CI"
related:
  - ../../../contracts/common/recursive_traversal_safety_assessment.md
  - ../../../contracts/governance/query_run_record.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Recursive Traversal Safety Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-133` | Recursive CTEs used for hierarchies, networks, route graphs, calendars, or lineage should declare termination criteria, maximum depth, and cycle handling. | `CONFIRMED` source statement |
| Source attribution `SRC-P18-003` | The card cites advanced SQL recursive traversal material, notes that strict caps can hide legitimate deep lineage, and proposes `recursion_depth` and `cycle_detected` fields in query receipts. | `CONFIRMED` source lineage |
| Current `QueryRunRecord` and adjacent common query/metric contracts | Query-run identity and adjacent bounded declarations exist, but no exact recursive-CTE termination, depth, breadth, cycle, observation, or receipt-assessment contract, schema, fixture suite, validator, workflow, branch, or PR was found before authoring. | `CONFIRMED` bounded gap |
| GitHub repository and PR/branch search at `main@fa244eb7bd11d8ff96e91f4925ca8abc5bdaa9fe` | Exact card, title, recursive-CTE, cycle-clause, traversal-depth, path, branch, and PR searches found no competing implementation. | `CONFIRMED` bounded search |

The connected Drive entry (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`) identifies a Pass 18 dossier with the same title and source role. Only Drive metadata was inspected; byte identity with the supplied local copy and Drive card-level content were not asserted. The supplied local PDF SHA-256 is `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`; rendered physical page 230 was visually checked for card and continuation fidelity.

## Adaptation

The implementation is a closed synthetic common-contract profile. It carries field names plus opaque digest-bound query, dialect, termination, justification, evidence, parity-fixture, and receipt references. It contains no SQL text, database connection material, parameter values, query results, node values, edge values, credentials, arbitrary generated prose, or runtime thresholds beyond the declared synthetic guards.

`NOT_RUN` is an admissible declaration state and does not pretend that a database query ran. An executed observation must expose `recursion_depth`, `cycle_detected`, visited counts, and a receipt reference. Reaching a depth cap cannot silently pass as complete. `UNRESOLVED` dialect parity abstains and `MISMATCH` denies; the profile invents no cross-dialect compatibility result.

## Directory Rules basis

Accepted ADR-0029 places reusable query-safety meaning under `contracts/common/`, machine shape under `schemas/contracts/v1/common/`, synthetic replay under `fixtures/contracts/v1/common/`, executable validation under `tools/validators/`, conformance proof under `tests/validators/`, orchestration under `.github/workflows/`, reconciliation under `docs/intake/exploratory/`, and generated authoring provenance under `data/receipts/generated/`.

No database adapter, SQL runner, graph store, lineage store, evidence store, policy rule, review record, release lane, public panel, or new root is created.

## Non-effects and rollback

A local `PASS` is declaration coherence only. It is not proof of recursive termination, query execution, result completeness, graph truth, evidence resolution, policy approval, human review, promotion, release, publication, or public-answer authority. Rollback is an additive commit revert with no external cleanup.
