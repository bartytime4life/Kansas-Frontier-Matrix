<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/expansion-backlog
title: Soil Dependency-Ordered Expansion Backlog
type: domain-expansion-backlog
version: v1.0.0
status: draft; repository-grounded; non-authoritative; release-held
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - contracts and schemas steward
  - OWNER_TBD - source, rights, and sensitivity steward
  - OWNER_TBD - validation and release steward
created: 2026-05-19
updated: 2026-08-28
policy_label: public
owning_root: docs/
responsibility: Dependency-ordered Soil improvement queue with exact evidence requirements, bounded completion criteria, and held transition states
truth_posture: CONFIRMED current repository gaps and bounded candidate surfaces at the pinned base / PROPOSED prioritization and future slices / NEEDS VERIFICATION ownership, acceptance, source admission, operational maturity, and release state
related:
  - docs/domains/soil/README.md
  - docs/domains/soil/VERIFICATION.md
  - docs/domains/soil/CANONICAL_PATHS.md
  - docs/domains/soil/SOURCE_REGISTRY.md
  - docs/domains/soil/MISSING_OR_PLANNED_FILES.md
  - docs/runbooks/soil/README.md
  - contracts/domains/soil/README.md
  - schemas/contracts/v1/domains/soil/README.md
  - packages/domains/soil/README.md
  - pipelines/domains/soil/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, soil, backlog, dependencies, verification, source-admission, lifecycle, release-hold]
notes:
  - "Repository evidence snapshot: main@249974ba480fd68dc749ad0258c84e09477d523a."
  - "Replaces a two-line greenfield placeholder; it does not authorize implementation or transition state."
  - "Planning lineage: KFM Soil Architecture Extended Pro PDF-Only Planning Report, SHA-256 7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea."
  - "The report's proposed paths and PR order are reconciled against current repository evidence rather than copied as authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil dependency-ordered expansion backlog

This backlog turns the Soil planning report's broad proposal into small,
repository-grounded review boundaries. Each row is a candidate, not an
authorization. Select work only after rechecking current `main`, open pull
requests, accepted Directory Rules, adjacent README contracts, and executable
evidence.

> [!IMPORTANT]
> A backlog row may produce a draft pull request or an exact no-change or blocker
> report. It never requires source activation, promotion, release, deployment, or
> publication to manufacture progress.

## Current state

| Surface | Current repository result |
|---|---|
| Contracts and schemas | Multiple substantive Soil candidate profiles exist under the accepted responsibility roots |
| Fixtures, validators, and tests | Several deterministic no-network profiles are executable; other named tests remain explicit placeholders |
| Package implementation | `identity.py`, `layers.py`, and `observations.py` remain one-line greenfield placeholders |
| Lifecycle pipeline | Mesonet fixture normalizer and station-health evaluator are executable; top-level ingest, normalize, validate, catalog, triplets, publish, and rollback modules remain one-line placeholders |
| Source registry | Canonical subtype-first placeholders coexist with a noncanonical domain-first compatibility lane |
| Catalog and proof | Bounded assessment and documentation surfaces exist; no complete operational Soil catalog or release path is established |
| Public UI and API | Held until governed API, evidence, policy, review, and released public-safe carrier closure exist |

## Selection law

A candidate is dependency-ready only when all of these conditions are true:

1. its owning responsibility root and path are confirmed;
2. no open PR owns or overlaps the target path;
3. the paired meaning, shape, fixtures, validator behavior, and negative outcomes
   are explicit enough to prevent parallel authority or silent semantic drift;
4. the change can be validated deterministically without live source access;
5. documentation, rollback, and non-effects fit in the same review boundary; and
6. the work does not imply source admission, evidence closure, policy approval,
   release, deployment, or publication.

## Active dependency-ordered queue

| ID | Priority | Candidate slice | Dependency | Smallest complete output | Exit evidence | State |
|---|---:|---|---|---|---|---|
| `SOIL-BL-001` | P0 | Assign accountable Soil, source, scientific, evidence, policy, release, and independent-review owners | Human governance decision | Update existing owner fields and review routing only after assignments are confirmed | Named accountable owners and review route in repository authority | `BLOCKED_OWNER_DECISION` |
| `SOIL-BL-002` | P0 | Reconcile Soil support-type maturity across domain, contract, schema, fixture, validator, and test indexes | Existing support-type profile and alias-map candidates | One documentation or status correction that distinguishes candidate implementation from canonical vocabulary adoption | Exact path inventory, focused tests, compatibility status, and unchanged activation or release holds | `READY_FOR_REVIEW` |
| `SOIL-BL-003` | P1 | Replace one package placeholder with a bounded semantic implementation | Accepted meaning and machine shape for exactly one object family; strict fixtures and negative tests | One of `identity.py`, `layers.py`, or `observations.py`, plus the minimum paired tests and documentation | Deterministic unit tests; no network; no new source or public route | `DEPENDENCY_READY_AFTER_PROFILE_SELECTION` |
| `SOIL-BL-004` | P1 | Reconcile source-registry compatibility without activating a source | ADR-0029 and Directory Rules `DIR-SOURCE-001` through `DIR-SOURCE-004`; reviewed source mapping | Mapping, generator, redirect or tombstone, or retirement candidate for one duplicate record family | One canonical writer, retained lineage, consumer checks, rollback target, no activation | `HOLD_MAPPING_AND_REVIEW` |
| `SOIL-BL-005` | P1 | Close one top-level lifecycle placeholder with fixture-only behavior | One admitted candidate profile with contract, schema, source decision, fixtures, validator, and policy posture | One bounded ingest, normalize, or validate module; never start with publish or rollback | Positive and negative fixture tests, deterministic identity, no-network proof, explicit lifecycle output boundary | `BLOCKED_PROFILE_AND_SOURCE_DECISION` |
| `SOIL-BL-006` | P1 | Reconcile documentation-only domain tests with the actual validator suites | Current tests under `tests/validators/domains/soil/` and direct Soil suites | Convert, redirect, or retire one placeholder module without duplicating existing executable proof | Test discovery proves the intended executable is collected once; docs and workflow references resolve | `READY_FOR_REVIEW` |
| `SOIL-BL-007` | P2 | Close one catalog-assessment dimension against current candidate artifacts | Existing catalog-closure contract, schema, fixture cases, validator, and tests | One dimension moves from `HOLD` to `READY_FOR_REVIEW` with exact references | Focused assessment test plus evidence showing no catalog, triplet, or release write | `DEPENDENCY_READY` |
| `SOIL-BL-008` | P2 | Reconcile Soil MapLibre and Evidence Drawer documentation with actual Explorer catalog state | Governed API envelope and released public-safe carrier remain prerequisites | Status and contract correction only, unless runtime prerequisites are independently proven | Map or UI tests plus EvidenceRef resolution and negative states; no direct internal-store path | `HOLD_RUNTIME_PREREQUISITES` |

## Completed bounded candidates retained as evidence

These rows are complete only within their named candidate profile. They are not
canonical Soil truth, source admission, or public release.

| Candidate | Repository evidence | Bounded disposition |
|---|---|---|
| Public-safe Soil fixture profile | Validator, exact positive and negative fixtures, and 16-test direct suite | `CONFIRMED_BOUNDED_EXECUTABLE` |
| Station Soil moisture profile | Validator, fixtures, and 12-test direct suite | `CONFIRMED_BOUNDED_EXECUTABLE` |
| SMAP L4 anti-collapse profile | Separate validator, fixtures, and 14-test direct suite | `CONFIRMED_BOUNDED_EXECUTABLE` |
| Support-type profile and alias map | Contracts, schemas, fixtures, validators, and focused validator tests are present | `CONFIRMED_CANDIDATE_SURFACES`; adoption remains `NEEDS VERIFICATION` |
| Catalog-closure assessment | Contract, schema, fixture cases, validator, tests, and domain status document are present | `READY_FOR_REVIEW`; catalog, proof, and release remain held |
| Mesonet fixture normalizer and station-health evaluator | Fixture-only pipeline executables and focused tests are present | `CONFIRMED_BOUNDED_EXECUTABLE`; live retrieval remains held |

## Explicitly deferred work

Do not select these as an incidental follow-up:

- live SSURGO or SDA, Kansas Mesonet, SCAN, USCRN, SMAP, SoilGrids, gSSURGO,
  or gNATSGO retrieval or activation;
- real farm, parcel, private-station, living-person, infrastructure, or
  culturally controlled location material;
- broad schema-home, contract-home, registry, catalog, triplet, proof, or release
  migrations without accepted authority and a migration packet;
- public map, governed API, Evidence Drawer, Focus Mode, graph, export, or AI
  activation before a released public-safe carrier exists; and
- promotion, rollback execution, release, deployment, or publication.

## Validation requirements for every selected row

At minimum, a review handoff must record:

- exact base and head commits;
- changed paths and responsibility-root placement;
- focused positive and negative tests;
- no-network posture and any skipped or unrun checks;
- hosted check results observed for the exact head;
- introduced, inherited, skipped, and not-run findings as separate classes;
- documentation and compatibility effects;
- mechanical rollback; and
- source, evidence, policy, review, proof, release, deployment, and publication
  states as separate fields.

The [Soil verification guide](VERIFICATION.md) records the current reproducible
fixture baseline. The [Soil runbook index](../../runbooks/soil/README.md) owns
operational assessment procedures; this backlog does not replace it.

## Directory Rules basis

This backlog belongs under `docs/domains/soil/` because it is human-readable
domain planning and coordination. It does not create machine contracts, schemas,
source registry records, fixtures, validators, lifecycle data, proof objects, or
release decisions. Those remain in their accepted responsibility roots.

See the [accepted Directory Rules](../../doctrine/directory-rules.md) and
[`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md).

## Rollback

Rollback is an ordinary Git revert of this documentation change. No executable,
source, lifecycle, evidence, policy, catalog, release, deployment, or publication
state changes with this file.
