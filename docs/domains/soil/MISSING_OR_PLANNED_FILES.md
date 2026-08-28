<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/missing-or-planned-files
title: Soil - Missing or Planned Files
type: domain-planning-register
version: v1.0
status: active; repository-grounded; planning-only
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-05-19
updated: 2026-08-28
policy_label: public
owning_root: docs/
responsibility: Record verified Soil path presence, placeholder debt, and dependency-gated future responsibilities without creating paths or authority
truth_posture: CONFIRMED current-session paths and inspected placeholder bytes / PROPOSED dependency-gated capabilities / UNKNOWN implementation and operational state unless explicitly verified
evidence_snapshot: "repository=bartytime4life/Kansas-Frontier-Matrix; base_commit=813ef14b1dbe5bd236fc902ce8fc3bb2e8ae7e80"
related:
  - docs/domains/soil/README.md
  - docs/domains/soil/VERIFICATION_BACKLOG.md
  - docs/domains/soil/EXPANSION_BACKLOG.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - data/registry/soil/missing_or_planned_files.yaml
tags: [kfm, soil, path-inventory, planned-files, placeholders, directory-rules]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil missing or planned files

This register replaces a greenfield placeholder with a current-session path
inventory. It distinguishes four states:

- `IMPLEMENTED_PROFILE` - bounded executable behavior exists with fixtures and
  tests;
- `PRESENT_MIXED` - a path exists, but maturity varies within the family;
- `PLACEHOLDER` - tracked bytes reserve or describe behavior but do not
  implement it;
- `ABSENT_CAPABILITY` - the required responsibility is not established; this
  does not authorize a guessed filename.

## Directory Rules basis

Soil is a domain segment under existing responsibility roots. Human planning
belongs here under `docs/`; semantic meaning belongs in `contracts/`; machine
shape in `schemas/`; policy in `policy/`; reusable code in `packages/`;
lifecycle transformations in `pipelines/`; tests in `tests/`; validators in
`tools/`; registry instances in `data/registry/`; and release decisions in
`release/`. This register must not create a parallel root or make a proposed
path canonical.

## Current inventory

| Responsibility | Confirmed path or family | State | Notes |
|---|---|---|---|
| Domain navigation | `docs/domains/soil/README.md` | `PRESENT_MIXED` | Repository-grounded entry point; its snapshot and some maturity statements now need refresh |
| Architecture and path guidance | `ARCHITECTURE.md`, `CANONICAL_PATHS.md`, `DATA_LIFECYCLE.md`, `CONTINUITY_INVENTORY.md` | `PRESENT_MIXED` | Substantial documents retain proposal-era or old-snapshot statements |
| Planning control | this file, `VERIFICATION_BACKLOG.md`, `EXPANSION_BACKLOG.md`, `CHANGELOG.md` | `PRESENT_MIXED` | Populated in the bounded planning-register repair; other short Soil docs remain placeholders |
| Semantic contracts | `contracts/domains/soil/` | `PRESENT_MIXED` | Multiple reviewed profiles coexist with proposal-era contract surfaces |
| Canonical domain schemas | `schemas/contracts/v1/domains/soil/` | `PRESENT_MIXED` | 38 JSON schema files; strict profiles coexist with permissive or compatibility shapes |
| Synthetic fixtures | `fixtures/domains/soil/` | `PRESENT_MIXED` | Several closed fixture profiles plus placeholder and compatibility material |
| Repository validators | `tools/validators/domains/soil/` | `PRESENT_MIXED` | 23 Python files; substantive validators coexist with four-line wrappers and documentation-only lanes |
| Tests | Soil-related files under `tests/` | `PRESENT_MIXED` | 41 Python files discovered; executable status and CI binding vary by profile |
| Domain CI | `.github/workflows/domain-soil.yml` | `IMPLEMENTED_PROFILE` | Three fixture suites plus SSURGO package-drift proof; proof and release jobs remain held |
| Source registry | `data/registry/sources/soil/` | `PRESENT_MIXED` | Ten direct files; presence does not activate a source |
| Source watch | `tools/ingest/ssurgo_watch/` and paired tests | `IMPLEMENTED_PROFILE` | Fixture-only package-drift comparison, no live admission authority |
| Package behavior | `packages/domains/soil/src/soil/` | `PLACEHOLDER` | Identity, layer, and observation modules still identify as greenfield placeholders |
| Lifecycle stages | `pipelines/domains/soil/*.py` | `PLACEHOLDER` | Stage modules do not establish an end-to-end Soil lifecycle path |
| Proof records | `data/proofs/soil/` | `PLACEHOLDER` | No material proof artifact found |
| Release candidates | `release/candidates/soil/` | `PLACEHOLDER` | No material candidate record found |
| Human-to-machine planning projection | `data/registry/soil/*.yaml` | `PLACEHOLDER` | File, planned-file, and verification registers are empty templates |

## Absent or dependency-gated capabilities

The responsibilities below are not established at the evidence snapshot. Their
future file names stay `HOLD` until the adjacent root contract and dependency
closure are verified.

| ID | Capability | Owning root | Dependency gate before creating files |
|---|---|---|---|
| `SOIL-MP-001` | Accepted owner and reviewer bindings | `docs/` / repository governance | Named accountable roles and review route |
| `SOIL-MP-002` | Canonical support-type vocabulary and compatibility projection | `contracts/`, `schemas/`, `fixtures/`, `tools/`, `tests/` | Consumer inventory and accepted semantic decision |
| `SOIL-MP-003` | One fully reviewed source-admission packet | `data/registry/`, policy and decision roots | Current rights, role, sensitivity, cadence, terms, fixture proof, review, and rollback |
| `SOIL-MP-004` | One implemented offline lifecycle transformation | `pipelines/` with reusable logic under `packages/` as needed | Contract, schema, source decision, policy, fixtures, validator, identity, and no-network proof |
| `SOIL-MP-005` | Bound policy evaluation and decision output | `policy/` plus owning decision surface | Pinned evaluator, policy input/output contracts, deny fixtures, and review |
| `SOIL-MP-006` | Accepted Soil EvidenceBundle/proof producer | evidence/proof responsibility roots | EvidenceRef resolution, validation report, source/rights/sensitivity closure, immutable bindings |
| `SOIL-MP-007` | Candidate-specific release dry run | `release/` | Accepted manifest contract, independent review, correction, withdrawal, rollback, and readback |
| `SOIL-MP-008` | Governed Soil API and Explorer integration | `apps/` with reusable packages as needed | Released public-safe carrier, governed resolver, Evidence Drawer payload, policy and rollback tests |
| `SOIL-MP-009` | Machine projection of these human registers | accepted registry/control-plane home | Schema, single writer, digest/parity validator, lifecycle, and correction path |

## Do not create from this register

- a top-level `soil/` root;
- a second writable contract, schema, policy, source-registry, proof, release, or
  published-data home;
- live connectors before source admission;
- production payloads in fixtures;
- public map or AI routes backed by RAW, WORK, QUARANTINE, unresolved, or
  unreleased state;
- proof, release, deployment, or publication records inferred from CI success.

## Next update rule

When a planned capability becomes concrete, first verify the owning root,
adjacent README, accepted decisions, producer and consumer paths, tests,
rollback, and overlap. Then replace the row with its exact path and evidence;
do not append speculative path trees.

[Back to top](#top)
