<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/file-system-plan
title: Soil file placement and change guide
type: domain-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Soil file placement and change guide; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/domains/soil/SOURCE_REGISTRY.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# soil — FILE_SYSTEM_PLAN.md

Use this guide when adding or moving Soil artifacts. Soil is a domain segment
inside established responsibility roots. The adopted
[Directory Rules](../../doctrine/directory-rules.md) and
[ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) control
placement; this plan provides a working navigation map.

## Existing homes

| Artifact responsibility | Existing path | Authoring rule |
|---|---|---|
| Human explanations | `docs/domains/soil/` | Link to owning artifacts; distinguish proposal from behavior |
| Semantic meaning | `contracts/domains/soil/` | Preserve object and support-role meaning |
| Machine shape | `schemas/contracts/v1/domains/soil/` | Pair version changes with fixtures and validation |
| Policy | `policy/domains/soil/` | Keep allow/deny and activation decisions out of prose substitutes |
| Synthetic inputs | `fixtures/domains/soil/` | Include exact negative expectations and no real restricted data |
| Shared contract fixtures | `fixtures/contracts/v1/domains/soil/` | Reuse where the contract already binds this lane |
| Validation | `tools/validators/domains/soil/` | Finite deterministic findings; no implicit lifecycle writes |
| Tests | `tests/domains/soil/`, `tests/validators/domains/soil/` | Prove the actual profile and failure boundary |
| Source descriptors | `data/registry/sources/soil/` | Admission remains separate from file presence |
| Domain helpers | `packages/domains/soil/` | Verify substance before citing behavior |
| Lifecycle transforms | `pipelines/domains/soil/` | Preserve RAW, candidate and publication boundaries |
| Declarative execution | `pipeline_specs/soil/` | An inactive declaration is not an executable pipeline |
| Candidate handoff | `release/candidates/soil/` | Candidate identity and release decision stay distinct |
| Domain proof navigation | `data/proofs/soil/` | Do not create proof merely by writing a README |
| Site implementation | `apps/site/source/` | Follow its scoped instructions and separate hosting review |

The [canonical-path register](CANONICAL_PATHS.md) and
[source registry guide](SOURCE_REGISTRY.md) retain historical path conflicts.
In particular, `data/registry/soil/sources/` also exists. Its presence does not
justify a second writer or a bulk migration during documentation work.

## Change procedure

1. Find existing same-purpose artifacts and their consumers before selecting a
   path. Read the local README and any scoped instructions.
2. Choose the owning responsibility, then the existing Soil lane. Verify the
   path at the intended base; a planning diagram is insufficient.
3. List direct companions: meaning, shape, fixtures, validator, tests, workflow,
   related docs and generated artifacts. Mark genuinely optional companions.
4. For a move, inventory inbound paths and anchors, old schema identifiers,
   scripts and readers. Prepare compatibility and rollback before removing a path.
5. Keep migration decisions and accepted ADR state separate from a proposed path.
6. Validate relative links, metadata, document graph and changed-area behavior.

## Common placement failures

- A new top-level `soil/` creates a parallel responsibility root.
- A schema copied under `docs/` becomes a second writable shape authority.
- A live source payload under `fixtures/` can expose restricted data and make
  tests depend on provider state.
- A new registry alias without a consumer map can silently split source identity.
- A generated receipt edited by hand can detach its digest from its source.

Correct the owning path and consumers together. Do not weaken topology or
receipt checks to accommodate a convenient destination.

## Acceptance and rollback

A placement change is ready for review when its owner, path rationale, consumer
inventory, link results and migration/rollback plan are visible. Revert a
misplaced unmerged patch locally; after an authorized merge use a reviewed revert
or forward correction. Preserve source records and evidence history throughout.
