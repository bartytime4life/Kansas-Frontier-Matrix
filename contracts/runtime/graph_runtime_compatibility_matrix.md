<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/graph-runtime-compatibility-matrix
title: Graph Runtime Compatibility Matrix Contract
type: semantic-contract; runtime-readiness; fixture-first; no-network
version: v0.1.0
status: proposed; inactive; readiness-evidence-only; non-release
owners: OWNER_TBD — Graph steward · Runtime steward · Validation steward · Security reviewer
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; graph; runtime; compatibility; fail-closed; non-authoritative
related:
  - ../../schemas/contracts/v1/runtime/graph_runtime_compatibility_matrix.schema.json
  - ../../control_plane/graph_runtime_compatibility_matrix.json
  - ../../tools/validators/runtime/validate_graph_runtime_compatibility_matrix.py
  - ../../migrations/graph/README.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, graph, runtime, neo4j, gds, driver, jvm, readiness, compatibility]
[/KFM_META_BLOCK_V2] -->

# Graph Runtime Compatibility Matrix Contract

> `GraphRuntimeCompatibilityMatrix` is a machine-checkable, inactive readiness evidence index. It records candidate runtime/JVM/GDS/driver tuples and cluster-rehearsal state without selecting a runtime, connecting to a graph, authorizing a migration, or claiming vendor support.

## Source-derived requirement

Pass 31 proposes a data-driven Neo4j/GDS/driver compatibility matrix and fail-closed runtime/JVM/cluster gates. This slice implements only the bounded contract, inactive control-plane projection, deterministic validator, synthetic fixtures, and CI evidence.

## Responsibility split

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/runtime/graph_runtime_compatibility_matrix.md` |
| Machine shape | `schemas/contracts/v1/runtime/graph_runtime_compatibility_matrix.schema.json` |
| Inactive projection | `control_plane/graph_runtime_compatibility_matrix.json` |
| Validator | `tools/validators/runtime/validate_graph_runtime_compatibility_matrix.py` |
| Synthetic fixtures | `fixtures/contracts/v1/runtime/graph_runtime_compatibility_matrix/` |
| Focused tests | `tests/validators/test_validate_graph_runtime_compatibility_matrix.py` |

Directory Rules place semantic meaning under `contracts/`, machine shape under `schemas/`, cross-system indexes under `control_plane/`, executable validation under `tools/validators/`, and enforceability under `fixtures/` and `tests/`.

## Finite interpretation

- A structurally and semantically valid matrix returns `PASS`.
- `PASS` proves only that the candidate matrix is closed, canonical, digest-bound, and non-authoritative.
- A tuple may be treated as `SUPPORTED` only when exact versions, JVM major, and evidence references are present.
- A clustered `SUPPORTED` tuple additionally requires a passed discovery/configuration rehearsal and a rehearsal reference.
- `NEEDS_VERIFICATION` rows are valid records but cannot authorize runtime readiness.

## Invariants

1. Rows are sorted by `row_id`; IDs and compatibility tuples are unique.
2. Evidence and reason-code arrays are canonical, unique, and bounded.
3. Single-node rows use `NOT_APPLICABLE` for discovery rehearsal.
4. Clustered supported rows require `PASSED` rehearsal state and a non-null reference.
5. Supported rows cannot use unresolved versions or omit evidence.
6. Every authority-bearing flag remains false.
7. `spec_hash` binds the exact matrix content with only `spec_hash` omitted.

## Non-effects

A valid matrix does not install Java, Neo4j, GDS, or a driver; inspect a live cluster; execute a query; authorize migration; admit data; promote; release; or publish.

## Rollback

Before merge, close the draft PR and delete the branch. After an authorized merge, revert the additive contract/schema/projection/validator/fixture/test/workflow/receipt packet. No graph store, migration, release, or public artifact requires rollback.
