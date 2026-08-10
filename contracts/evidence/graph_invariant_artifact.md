<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/graph-invariant-artifact
title: GraphInvariantArtifactCandidate
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Evidence steward · Graph steward · Migration steward · Schema steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; evidence; graph; migration; invariant; no-network; non-release
source_card: KFM-P31-PROG-0003
source_spec_hash: sha256:48b01f0bed00068e64026d0e1ed3d35071da734e223310244c04b23542cc31d7
related:
  - ../governance/graph_migration_declaration.md
  - ../../schemas/contracts/v1/evidence/graph_invariant_artifact.schema.json
  - ../../fixtures/contracts/v1/evidence/graph_invariant_artifact/cases.json
  - ../../tools/validators/evidence/validate_graph_invariant_artifact.py
  - ../../tests/validators/evidence/test_graph_invariant_artifact.py
tags: [kfm, evidence, graph, migration, invariant, comparison, fixture]
[/KFM_META_BLOCK_V2] -->

# GraphInvariantArtifactCandidate

> **PROPOSED / INACTIVE / FIXTURE-ONLY.** This profile records a deterministic comparison of declared before/after graph-invariant snapshots. It does not contact a graph, run a query or GDS procedure, execute a migration, establish evidence sufficiency, approve review, promote, release, or publish.

## Source-derived gap

Pass 31 card `KFM-P31-PROG-0003` calls for graph-invariant artifacts covering counts, constraints, representative query outputs, and GDS procedure results before and after upgrades. The existing `GraphMigrationDeclaration` owns pre-execution intent and admissibility. This profile remains subordinate to that declaration and owns only a synthetic comparison artifact.

## Directory Rules basis

Semantic evidence meaning belongs under `contracts/evidence/`; machine shape under `schemas/contracts/v1/evidence/`; reusable synthetic cases under `fixtures/contracts/v1/evidence/`; reusable enforcement under `tools/validators/evidence/`; and executable proof under `tests/validators/evidence/`. Migration mechanics remain solely under `migrations/graph/`. No parallel graph store, migration runner, receipt store, policy home, or release lane is created.

## Required meaning

| Surface | Meaning | Fail-closed boundary |
|---|---|---|
| `migration_declaration_ref` | Deterministic reference to one proposed graph-migration declaration. | The artifact does not replace or approve the declaration. |
| `before` and `after` | Declared synthetic node/relationship counts, constraint states, query summaries, and GDS summaries. | Both snapshots must expose the same canonical keys so differences are explicit. |
| `comparison` | Exact reproduced deltas and changed-key lists. | Omitted, stale, reordered, or fabricated comparisons fail. |
| `classification` | `NO_DRIFT` or `REVIEW_REQUIRED`. | Neither value authorizes migration, review, release, or publication. |
| `controls` | Fixed fixture-only and non-authority posture. | Live graph access, execution, evidence sufficiency, policy, review, promotion, release, and publication remain false. |

## Identity

`spec_hash` is RFC 8785/JCS SHA-256 over the complete record after removing `artifact_id` and `spec_hash`. `artifact_id` is `kfm:graph-invariant-artifact:` followed by the first 24 hexadecimal digest characters.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/evidence \
  --pattern 'test_graph_invariant_artifact.py' \
  --verbose

python tools/validators/evidence/validate_graph_invariant_artifact.py --fixtures
```

A pass proves only closed schema shape, exact synthetic comparison arithmetic, canonical ordering, fixed non-effects, and deterministic identity.

## Rollback

Revert this additive packet. No graph, migration, policy result, evidence admission, review state, lifecycle state, release, or publication is created.
