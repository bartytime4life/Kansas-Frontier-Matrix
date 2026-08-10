<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-31-graph-invariant-artifact-source-map
title: Pass 31 graph invariant artifact source map
type: source-adaptation-map
version: v1.0.0
status: proposed; implementation-support; non-authoritative
owners: OWNER_TBD — Intake steward · Evidence steward · Graph steward · Directory Rules reviewer
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; intake; graph; evidence; provenance
source_card: KFM-P31-PROG-0003
source_spec_hash: sha256:48b01f0bed00068e64026d0e1ed3d35071da734e223310244c04b23542cc31d7
[/KFM_META_BLOCK_V2] -->

# Pass 31 graph invariant artifact source map

## Evidence basis

| Evidence | Confirmed use |
|---|---|
| Drive `KFM_Pass23_Pass32_Consolidated_Deduplicated_Atlas.pdf` (`1w7Qrf5Na7PSvwdTuplZnFbyueToPtQaa`) | Card `KFM-P31-PROG-0003`; specification hash `sha256:48b01f0bed00068e64026d0e1ed3d35071da734e223310244c04b23542cc31d7`. |
| Supplied `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` | Byte digest `sha256:020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639`; extracted card text checked locally. |
| Drive `Directory Rules` (`1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs`) | Responsibility-root placement and contract/schema/fixture/tool/test separation. |
| Repository `main@7335ed9ea0f81342ae0b1c7828a21ac74711c78b` | Gap and collision assay, including merged `GraphMigrationDeclaration`. |

## Adaptation decision

The source asks for before/after graph-invariant artifacts containing counts, constraints, representative query outputs, and GDS procedure results. This packet encodes that comparison deterministically but accepts only prepared synthetic declarations. It does not add a graph client, store, query runner, GDS dependency, migration payload, or execution path.

The existing `GraphMigrationDeclaration` remains the pre-execution governance authority. `GraphInvariantArtifactCandidate` references it and cannot approve or execute it.

## Collision check

Exact card-ID, exact-title, repository-file, and PR searches found no implementation of `KFM-P31-PROG-0003`. Merged PR #2371 implements the distinct declaration card `KFM-P30-PROG-0008`; its intent, scope, and invariants are reused by reference rather than duplicated.

## Truth and authority boundary

`CONFIRMED`: source card, specification hash, Directory Rules authority, repository base, and existing graph declaration were inspected. `PROPOSED`: this profile and every authored path. `UNKNOWN`: live graph compatibility, representative query correctness, GDS availability, migration admissibility, policy, human review, release, and publication.

## Rollback

Delete the eight additive packet files. No migration, graph, policy, evidence, release, or public state requires restoration.
