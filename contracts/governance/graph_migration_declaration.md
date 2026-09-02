<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/graph-migration-declaration
title: GraphMigrationDeclaration — fixture-only pre-execution governance contract
type: semantic-contract
version: v0.1.0
status: proposed-inactive; fixture-only; non-executing; non-release; non-publication
owner: OWNER_TBD — graph steward · governance steward · evidence steward · migration steward · Directory Rules reviewer
created: 2026-08-09
updated: 2026-08-09
policy_label: public; proposed; governance; graph-migration; fail-closed; non-authoritative
source_card: KFM-P30-PROG-0008
source_spec_hash: sha256:517810192f27527381aca4b4ce448b2409f26e47932fddb1954d30ceab7d4b14
related:
  - ../../migrations/graph/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../schemas/contracts/v1/governance/graph_migration_declaration.schema.json
  - ../../fixtures/contracts/v1/governance/graph_migration_declaration/cases.json
[/KFM_META_BLOCK_V2] -->

# GraphMigrationDeclaration

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This contract defines the meaning of a bounded pre-execution graph-migration declaration. It does not select a graph store or runner, execute a migration, approve review, authorize release, or publish graph state.

## Responsibility boundary

`GraphMigrationDeclaration` is a governance object that makes migration intent, invariants, scope, blast radius, telemetry expectations, reversibility, and governance constraints inspectable before any executable packet can be considered. Graph-migration mechanics and review packets remain owned by [`migrations/graph/`](../../migrations/graph/README.md). Machine shape lives in `schemas/contracts/v1/governance/`; validation and fixtures are proof surfaces, not authority.

## Required meaning

| Surface | Meaning | Fail-closed rule |
|---|---|---|
| `migration` | Proposed title, intent, class, and non-executed status. | It cannot claim applied, rehearsed, or approved state. |
| `scope` | Store class and bounded affected graph surfaces. | Empty or non-canonical scope is invalid; `UNRESOLVED` is permitted while the store is unselected. |
| `invariants` | Complete preservation obligations for evidence, identity, topology, scope, provenance, rights, and recovery. | Missing or relaxed required invariants invalidate the declaration. |
| `blast_radius` | Named affected components and a conservative worst-case statement. | Destructive effects are not admissible in this inactive profile. |
| `telemetry` | Precheck, metric, and postcheck references expected from a future runner. | State remains `NOT_RUN`; references are requirements, not observations. |
| `reversibility` | Recovery class and paired recovery design reference. | A missing recovery reference, irreversible effect, or execution claim invalidates the declaration. |
| `governance` | Authority, reason, evidence, policy, and pending-review references. | Review is pending; execution, release, and publication authorization remain false. |
| `assessment` | Mandatory `HOLD` posture. | A declaration cannot promote itself into approval. |

## Identity

`spec_hash` is the repository hashing package's RFC 8785/JCS SHA-256 digest over the entire record after removing `declaration_id` and `spec_hash`. `declaration_id` is `kfm:graph-migration-declaration:` plus the first 24 hexadecimal digest characters. Array ordering is semantic and therefore must be sorted and duplicate-free where the schema declares set-like references.

## Invariant closure

Every declaration carries these ten required invariants: `DETERMINISTIC_IDENTITY`, `DIRECTIONALITY_CARDINALITY`, `ENDPOINT_INTEGRITY`, `EVIDENCE_CLOSURE`, `IDENTITY_LINEAGE`, `NO_AUTHORITY_INFLATION`, `PROVENANCE`, `RECOVERY`, `SENSITIVITY_RIGHTS`, and `TEMPORAL_SPATIAL_SCOPE`. This profile does not waive them.

## Non-effects

A conforming record performs no graph access, query execution, graph write, identity remap, evidence mutation, lifecycle promotion, policy decision, review approval, release, or publication. A validator PASS proves only bounded shape, semantic consistency, fixture polarity, and deterministic identity.

## Adoption and rollback

Activation requires a separately reviewed store and runner decision, executable migration and paired recovery formats, authenticated review evidence, dry-run and postcheck evidence, and policy integration. Until then, all records remain `PROPOSED_INACTIVE`, `FIXTURE_ONLY`, and `HOLD`. Rollback of this proposal is deletion of its contract packet; no graph state exists to reverse.
