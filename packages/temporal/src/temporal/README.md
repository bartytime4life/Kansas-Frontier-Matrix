<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://package/temporal/src/temporal
title: Temporal module README
type: package-readme
version: v0.3
status: draft
owners: OWNER_TBD - Temporal steward · Schema steward · Validation steward
created: 2026-06-15
updated: 2026-07-21
policy_label: internal
related:
  - packages/temporal/README.md
  - packages/temporal/src/README.md
  - contracts/common/temporal_window.md
  - schemas/contracts/v1/common/temporal_window.schema.json
  - tools/validators/validate_temporal_window.py
  - docs/doctrine/time-aware.md
  - docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md
tags: [kfm, temporal, time-aware, interval, correction, release, evidence]
notes:
  - "v0.3 replaces speculative helper and import claims with repository-grounded implementation status."
  - "The module is a greenfield placeholder at the recorded evidence snapshot; it exposes no confirmed runtime API."
  - "Temporal vocabulary is PROPOSED / CONFLICTED across the current schema, ADR-0014, and time-awareness doctrine."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Temporal module

Shared implementation lane for KFM temporal primitives, currently present as a greenfield Python package placeholder.

> [!IMPORTANT]
> - **Document status:** draft
> - **Implementation status:** `CONFIRMED` placeholder; no runtime API is implemented
> - **Authority:** implementation support only - not contract, schema, policy, evidence, or release authority
> - **Vocabulary posture:** `PROPOSED / CONFLICTED`
> - **Public path:** none; normal public clients use governed interfaces and released artifacts

## Quick navigation

- [Purpose](#purpose)
- [Scope and audience](#scope-and-audience)
- [Repository fit](#repository-fit)
- [Current implementation](#current-implementation)
- [Temporal vocabulary and known conflict](#temporal-vocabulary-and-known-conflict)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Inputs, outputs, and interfaces](#inputs-outputs-and-interfaces)
- [Invariants and trust boundaries](#invariants-and-trust-boundaries)
- [Validation and testing](#validation-and-testing)
- [Change, correction, and rollback](#change-correction-and-rollback)
- [Evidence basis](#evidence-basis)
- [Open verification items](#open-verification-items)

## Purpose

`packages/temporal/src/temporal/` is the Python module lane for reusable temporal implementation code shared across KFM packages, tools, pipelines, validators, and governed applications.

The lane may eventually implement parsing, normalization, interval operations, temporal comparison, and validation support after the controlling temporal vocabulary and contracts are reconciled. Its code must implement those decisions; it must not become a second place that defines them.

## Scope and audience

This README is for package maintainers, contract and schema stewards, validator authors, reviewers, and downstream implementers.

It documents:

- the module's current repository state;
- the boundary between implementation and temporal authority;
- the checked-in temporal contract, schema, validator, and proposed ADR that future code must reconcile;
- the minimum validation and review burden before the module can be treated as functional.

It does not claim that temporal helpers, package imports, consumers, fixtures, or runtime behavior already exist.

## Repository fit

| Surface | Responsibility | Current status |
|---|---|---|
| [`packages/`](../../../README.md) | Canonical root for shared reusable implementation libraries. | `CONFIRMED` path and root README |
| [`packages/temporal/`](../../README.md) | Package envelope and package-level orientation. | `CONFIRMED` scaffold |
| [`packages/temporal/src/`](../README.md) | Source-code envelope and proposed package boundary. | `CONFIRMED` path; implementation claims remain mostly `PROPOSED` |
| `packages/temporal/src/temporal/` | Import namespace for temporal implementation code. | `CONFIRMED` placeholder |
| [`contracts/common/temporal_window.md`](../../../../contracts/common/temporal_window.md) | Semantic meaning for the current `temporal_window` value object. | `CONFIRMED` draft contract |
| [`schemas/contracts/v1/common/temporal_window.schema.json`](../../../../schemas/contracts/v1/common/temporal_window.schema.json) | Machine-checkable shape and current six-value `time_kind` enum. | `CONFIRMED` file; schema metadata says `PROPOSED` |
| [`tools/validators/validate_temporal_window.py`](../../../../tools/validators/validate_temporal_window.py) | Declared validator entry point. | `CONFIRMED` placeholder that raises `NotImplementedError` |

Directory Rules places this module under `packages/` because its responsibility is shared implementation code. This edit preserves the existing path and creates no new authority root, domain root, lifecycle phase, or parallel contract/schema/policy home.

## Current implementation

The repository snapshot establishes only the following executable surface:

| File | Confirmed state | What it proves |
|---|---|---|
| [`__init__.py`](./__init__.py) | Empty. | The Python namespace exists; it exports no confirmed symbols. |
| [`core.py`](./core.py) | Contains one greenfield-placeholder comment. | No parser, value object, interval helper, comparison, freshness check, or validator is implemented. |
| [`pyproject.toml`](../../pyproject.toml) | Declares project name `kfm-temporal` and version `0.0.0`. | Package identity is scaffolded; it does not declare a build backend, Python requirement, dependencies, entry points, or package-local test configuration. |

No `packages/temporal/tests/` or `packages/temporal/src/temporal/tests/` directory was present at the pinned snapshot. Bounded repository search found no implemented imports from this module. The connector's code-search results were indexed at `77ee6d6fdfad928d19e45ff667935d80df9fd125`, while direct file and path probes used the newer pinned base. Absence is limited to those inspected paths and indexed searches.

> [!WARNING]
> Do not copy the illustrative import block from earlier revisions of this README. `TemporalInterval`, `TemporalProfile`, `coerce_utc`, `intervals_overlap`, `contains_instant`, `classify_staleness`, and `validate_half_open_interval` are not implemented or exported at the evidence snapshot.

## Temporal vocabulary and known conflict

KFM's temporal vocabulary is not yet reconciled across governing and implementation-adjacent artifacts.

| Surface | Vocabulary at the pinned snapshot | Authority state |
|---|---|---|
| [`temporal_window.schema.json`](../../../../schemas/contracts/v1/common/temporal_window.schema.json) | `observed`, `published`, `ingested`, `effective`, `corrected`, `superseded` | Checked-in machine shape with `x-kfm.status: PROPOSED` |
| [`ADR-0014`](../../../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md) | `source_time`, `observed_time`, `ingested_time`, `decision_time`, `published_time`, `retraction_time` | `proposed`; not an accepted decision |
| [`time-aware.md`](../../../../docs/doctrine/time-aware.md) | Seven dimensions: source, observed, valid, retrieval, release, correction, transaction time | Draft doctrine; schema-level field names remain proposed |

These sets overlap but are not equivalent. Until an accepted decision and compatible contract/schema change reconcile them:

1. Do not hard-code a new canonical enum in this module.
2. Do not silently translate one vocabulary into another.
3. Treat a crosswalk as explicit, versioned, and reviewable data rather than an implicit alias map.
4. Keep schema acceptance separate from semantic correctness and policy permission.
5. Mark examples and proposed APIs as `PROPOSED`, not as current package behavior.

The currently checked-in `temporal_window` shape requires exactly `start`, `end`, and `time_kind`; both times are JSON Schema `date-time` strings, and additional top-level properties are rejected. That shape does not define interval inclusivity, ordering, timezone normalization, open intervals, uncertainty, calendar handling, freshness, or bitemporal behavior.

## What belongs here

Only shared, reusable implementation code belongs in this module, such as:

- value objects or adapters that implement an accepted temporal contract;
- deterministic parsing and serialization helpers;
- interval comparison and ordering helpers whose boundary semantics are contract-backed;
- explicit vocabulary crosswalks backed by an accepted decision and tests;
- low-level validation support used by repository validators;
- package-private utilities and type definitions;
- module documentation tied to actual exports and behavior.

Every implementation claim remains `PROPOSED` until code and tests establish it.

## What does not belong here

| Excluded responsibility | Correct authority or home |
|---|---|
| Temporal object meaning, field intent, and semantic invariants | [`contracts/`](../../../../contracts/README.md) |
| Machine-readable field shape and enum values | [`schemas/contracts/v1/`](../../../../schemas/contracts/v1/README.md) |
| Allow, deny, restrict, redact, freshness, or release decisions | [`policy/`](../../../../policy/README.md) |
| Repository-wide validator entry points | [`tools/validators/`](../../../../tools/validators/README.md) |
| Valid, invalid, denied, abstained, or quarantined fixtures | [`fixtures/`](../../../../fixtures/README.md) and verified test lanes |
| Raw, work, quarantine, processed, catalog, triplet, proof, receipt, or published data | The correct lifecycle lane under [`data/`](../../../../data/README.md) |
| Release manifests, correction notices, and rollback decisions | [`release/`](../../../../release/README.md) |
| Domain-specific temporal rules | The owning domain contract, schema, policy, package, and tests |
| Public API routes or UI rendering | Governed application and UI roots |

The module must not mint evidence, approve a release, write canonical lifecycle data, infer an unknown date as fact, or turn generated language into temporal evidence.

## Inputs, outputs, and interfaces

### Current state

- **Public interface:** none confirmed.
- **Internal interface:** none confirmed.
- **Accepted runtime inputs:** none implemented.
- **Emitted runtime outputs:** none implemented.
- **Dependencies and consumers:** `UNKNOWN` beyond documentation references.

### Future implementation boundary

When implementation begins, inputs should be contract-shaped temporal values plus explicit context required by the accepted vocabulary. Outputs should be deterministic values or finite validation results that preserve:

- the time kind or dimension;
- source precision and timezone/calendar information when the controlling contract requires them;
- open, unknown, and not-applicable states without magic dates;
- correction and supersession lineage;
- the owning record or evidence identity.

This module must not invent policy outcomes or public response envelopes. `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or any review `HOLD` state belong to the governed surface that applies contracts, evidence, policy, and release state.

## Invariants and trust boundaries

Future code in this module must preserve these constraints:

1. A timestamp's kind is part of its meaning; different kinds must not be silently collapsed into a generic `date`.
2. Parsing success proves syntax only. It does not prove chronology, source authority, freshness, evidence closure, policy allowance, correction closure, or release state.
3. Schema validation proves shape only. Semantic and policy checks remain separate.
4. Unknown, approximate, open-ended, and not-applicable values must remain distinguishable when the controlling contract supports them.
5. Corrections and supersessions add auditable facts; they do not erase prior history.
6. Temporal helpers must not bypass the lifecycle spine: `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`.
7. Public clients must receive temporal claims through governed interfaces and released artifacts, with evidence and policy context appropriate to the claim.
8. Deterministic output is required for identical inputs, configuration, vocabulary version, and timezone/calendar rules.

## Validation and testing

### Current validation state

| Check | Status | Evidence boundary |
|---|---|---|
| Module import and export tests | `NOT RUN / no package-local tests found` | No confirmed API exists to test. |
| `temporal_window` schema shape | `CONFIRMED` as a checked-in proposed schema | File inspection only; no schema-validation run is claimed here. |
| `temporal_window` semantic validator | `CONFIRMED` placeholder | The declared script raises `NotImplementedError`. |
| Temporal fixtures | `NOT FOUND` at the schema-declared fixture root | Exact path probe at the pinned snapshot. |
| Ordering, interval boundaries, timezone, calendar, uncertainty, and freshness behavior | `UNKNOWN` | Not implemented or proven by inspected package evidence. |
| Downstream integration | `UNKNOWN` | No implemented consumer was confirmed by bounded search. |

### Minimum evidence before calling the module functional

- [ ] An accepted temporal vocabulary or an explicit versioned compatibility decision exists.
- [ ] `pyproject.toml` declares a build system, supported Python version, package discovery, and dependencies as needed.
- [ ] `__init__.py` exposes only documented symbols.
- [ ] Implemented objects and helpers match the controlling contract and schema.
- [ ] Valid and invalid fixtures cover every supported time kind and boundary condition.
- [ ] Tests cover ordering, equality, overlap, adjacency, open/unknown states, timezone/calendar handling, correction, supersession, and deterministic serialization as applicable.
- [ ] Negative tests prove ambiguous, unsupported, and conflicting inputs fail explicitly.
- [ ] The repository validator is implemented beyond `NotImplementedError` and remains separate from policy.
- [ ] Downstream consumers pin the vocabulary/contract version they expect.
- [ ] Public-boundary tests prove no caller treats package output alone as publication authority.

Do not invent a package-local test command until package metadata or repository tooling defines one.

## Change, correction, and rollback

For behavior changes:

1. Update semantic contracts before or with meaning changes.
2. Update schemas when machine shape or enum values change.
3. Add compatible fixtures, validators, and tests.
4. Review policy and public payload impact separately.
5. Record migration and rollback behavior for existing consumers and stored values.
6. Preserve correction and supersession lineage for any released artifact affected by changed semantics.

For this documentation-only revision, rollback is a transparent revert of the implementation commit on the review branch or, after merge, a revert pull request. Reverting this README does not change temporal runtime behavior because no module behavior is changed here.

## Review burden

[`CODEOWNERS`](../../../../.github/CODEOWNERS) routes `packages/` changes to `@bartytime4life`. CODEOWNERS is review routing only; it does not prove approval, temporal stewardship, policy review, release approval, or separation of duties.

A future functional change should include contract/schema and validation stewards when it changes vocabulary, shape, interval semantics, timezone/calendar rules, correction behavior, public labels, or compatibility.

## Evidence basis

Direct repository evidence is bounded to `bartytime4life/Kansas-Frontier-Matrix@aa8a350980eeac2c8834f1cd89c714878a46a650`; connector code-search results were indexed at `77ee6d6fdfad928d19e45ff667935d80df9fd125`.

| Evidence | Supports | Does not prove |
|---|---|---|
| [`__init__.py`](./__init__.py), [`core.py`](./core.py), and [`pyproject.toml`](../../pyproject.toml) | Current package scaffold, empty export surface, placeholder code, project name, and version. | Runtime behavior, compatibility, or consumers. |
| [`temporal_window` contract](../../../../contracts/common/temporal_window.md) | Draft semantic meaning and documented limits of the common value object. | Implemented validation or module integration. |
| [`temporal_window` schema](../../../../schemas/contracts/v1/common/temporal_window.schema.json) | Exact current fields, required set, enum, formats, and `additionalProperties` rule. | Ordering, timezone, policy, freshness, or release behavior. |
| [`validate_temporal_window.py`](../../../../tools/validators/validate_temporal_window.py) | Declared validator path and placeholder state. | Any passing validation behavior. |
| [`ADR-0014`](../../../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md) | Proposed six-kind vocabulary and unresolved questions. | An accepted temporal decision. |
| [`time-aware.md`](../../../../docs/doctrine/time-aware.md) | Draft time-awareness doctrine and seven-dimension posture. | Reconciled schema fields or implemented package behavior. |
| [`Directory Rules`](../../../../docs/doctrine/directory-rules.md) | `packages/` placement and responsibility-root boundary. | Temporal semantics or runtime maturity. |
| [`DRIFT_REGISTER.md`](../../../../docs/registers/DRIFT_REGISTER.md) | Inspected repository drift register. | Resolution of the temporal vocabulary conflict; no temporal-specific entry was present in the inspected file. |

## Open verification items

- **NEEDS VERIFICATION:** Which temporal vocabulary will become controlling, and how the three current vocabularies will be migrated or crosswalked.
- **NEEDS VERIFICATION:** Interval inclusivity/exclusivity, ordering, adjacency, and open-ended representation.
- **NEEDS VERIFICATION:** Timezone normalization, local-source offset preservation, calendar handling, precision, and uncertainty rules.
- **NEEDS VERIFICATION:** Whether bitemporal valid-time and transaction-time support belongs in this module and in which contract version.
- **NEEDS VERIFICATION:** Package build configuration, supported Python versions, dependencies, public exports, and import name.
- **NEEDS VERIFICATION:** Package-local fixtures, tests, repository-native commands, CI coverage, and downstream consumers.
- **NEEDS VERIFICATION:** Policy behavior for stale, corrected, superseded, embargoed, or evidence-incomplete temporal claims.
- **OWNER_TBD:** Confirm the temporal, schema, validation, and documentation stewards.

## ADRs

- [`ADR-0014`](../../../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md) is `proposed`; it must not be presented as an accepted package contract.
- [`ADR-0001`](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) is also `proposed`; Directory Rules independently establishes the current `schemas/` machine-shape and `packages/` shared-implementation separation used by this README.

## Last reviewed

- Date: 2026-07-21
- Repository: `bartytime4life/Kansas-Frontier-Matrix`
- Evidence snapshot: `main@aa8a350980eeac2c8834f1cd89c714878a46a650`
- Code-search snapshot: `77ee6d6fdfad928d19e45ff667935d80df9fd125`
- Current target blob: `da9a450d48b47fb0132d68237e15232f4ec9ff6a`
- Runtime execution: not performed; repository content was inspected through the GitHub connector
- Human review: pending

<p align="right"><a href="#top">Back to top</a></p>
