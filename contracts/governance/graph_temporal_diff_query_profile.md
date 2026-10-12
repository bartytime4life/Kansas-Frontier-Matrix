<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/graph-temporal-diff-query-profile
title: GraphTemporalDiffQueryProfileCandidate - fixture-only read-only query declaration
type: semantic-contract
version: v0.1.0
status: proposed-inactive; fixture-only; non-executing; non-release; non-publication
owner: OWNER_TBD - graph steward; governance steward; migration steward; evidence steward; Directory Rules reviewer
created: 2026-08-09
updated: 2026-08-09
policy_label: public; proposed; governance; graph; temporal-diff; fail-closed; non-authoritative
source_card: KFM-P30-PROG-0010
source_spec_hash: sha256:b40876ab01dbd8f6262288674846060542ee79a7e75d0ac202cd04febb64f5ba
related:
  - ./graph_migration_declaration.md
  - ../evidence/graph_invariant_artifact.md
  - ../../migrations/graph/README.md
  - ../../schemas/contracts/v1/governance/graph_temporal_diff_query_profile.schema.json
  - ../../fixtures/contracts/v1/governance/graph_temporal_diff_query_profile/cases.json
[/KFM_META_BLOCK_V2] -->

# GraphTemporalDiffQueryProfileCandidate

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This profile declares three bounded, parameterized, read-only Cypher templates for comparing synthetic graph snapshots. It does not connect to a graph, execute a query or migration, observe graph state, approve review, authorize release, or publish.

## Responsibility boundary

The profile is subordinate to the existing `GraphMigrationDeclaration`. It makes the intended migration-window, label-scoped, and relationship-scoped comparison shapes reviewable before any executable migration packet exists. Graph migration and rollback mechanics remain owned by [`migrations/graph/`](../../migrations/graph/README.md); before/after evidence remains owned by the `GraphInvariantArtifactCandidate`. This contract owns only the proposed declaration meaning.

## Required query set

| Query ID | Scope | Required parameters | Result meaning |
|---|---|---|---|
| `MIGRATION_WINDOW_NODE_DIFF` | All nodes carrying one declared migration-window ID. | `migration_window_id`, `before_snapshot_ref`, `after_snapshot_ref` | Before/after counts grouped by node labels. |
| `LABEL_SCOPED_NODE_DIFF` | Nodes with one parameterized label in that migration window. | The window parameters plus `label` | Before/after counts for the declared label. |
| `RELATIONSHIP_SCOPED_DIFF` | Relationships of one parameterized type in that migration window. | The window parameters plus `relationship_type` | Before/after counts for the declared relationship type. |

Every template must begin with `MATCH`, use only declared `$parameters`, return deterministic columns, end in an `ORDER BY`, and remain free of write clauses, procedure calls, external loads, dynamic identifier interpolation, and statement chaining. These checks are a conservative fixture profile, not a complete Cypher parser or proof of runtime safety.

## Identity and closure

`spec_hash` is the repository hashing package's RFC 8785/JCS SHA-256 digest over the record after removing `profile_id` and `spec_hash`. `profile_id` is `kfm:graph-temporal-diff-query-profile:` plus the first 24 digest characters. Query IDs, parameter declarations, result columns, references, and non-effects are sorted and duplicate-free.

## Fixed authority posture

A conforming candidate has `review_state: PENDING`, `assessment: HOLD`, no network or graph permission, and no query, migration, policy, lifecycle, release, or publication effect. A validator PASS proves only closed shape, bounded template checks, exact fixture polarity, and deterministic identity.

## Adoption and rollback

Activation requires a separately reviewed graph platform and version matrix, an executable migration packet, authenticated review, parameter-binding implementation, query-plan and timeout evidence, representative before/after graph fixtures, recovery rehearsal, and policy integration. Rollback of this proposal is deletion of its eight additive files; no graph state exists to reverse.
