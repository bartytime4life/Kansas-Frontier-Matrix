<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://package/temporal
title: Temporal package README
type: package-readme
version: v0.2
status: draft
owners: OWNER_TBD - Temporal steward · Package steward · Contract steward · Schema steward · Validation steward
created: NEEDS_VERIFICATION
updated: 2026-07-21
policy_label: internal
related:
  - ../README.md
  - ./pyproject.toml
  - ./src/README.md
  - ./src/temporal/README.md
  - ../../contracts/common/temporal_window.md
  - ../../schemas/contracts/v1/common/temporal_window.schema.json
  - ../../tools/validators/validate_temporal_window.py
  - ../../docs/doctrine/time-aware.md
  - ../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md
tags: [kfm, packages, temporal, time-aware, interval, validation, correction, release]
notes:
  - "v0.2 replaces the three-line package stub with a repository-grounded package boundary."
  - "The package is a greenfield Python scaffold at the recorded evidence snapshot and exposes no confirmed runtime API."
  - "The prior six-time-kind model and acceptance-check wording is retained only as proposed intent because the current schema, ADR-0014, and time-awareness doctrine use non-equivalent vocabularies."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Temporal package

Shared implementation package for KFM temporal primitives, currently present as a greenfield Python scaffold.

> [!IMPORTANT]
> - **Document status:** draft
> - **Implementation status:** `CONFIRMED` placeholder; no runtime helper API is implemented
> - **Authority:** implementation support only - not contract, schema, policy, evidence, or release authority
> - **Vocabulary posture:** `PROPOSED / CONFLICTED`
> - **Public path:** none; public clients use governed interfaces and released artifacts

## Quick navigation

- [Purpose](#purpose)
- [Authority and placement](#authority-and-placement)
- [Current implementation](#current-implementation)
- [Temporal vocabulary conflict](#temporal-vocabulary-conflict)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Inputs, outputs, and consumers](#inputs-outputs-and-consumers)
- [Trust boundaries](#trust-boundaries)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Change, correction, and rollback](#change-correction-and-rollback)
- [Evidence basis](#evidence-basis)
- [Open verification items](#open-verification-items)
- [Last reviewed](#last-reviewed)

## Purpose

`packages/temporal/` is the package envelope for reusable temporal implementation code shared by KFM applications, packages, tools, pipelines, validators, and tests.

The package may eventually provide contract-backed parsing, normalization, interval operations, comparison helpers, deterministic serialization, and low-level validation support. It must implement accepted decisions made in the appropriate authority roots; it must not define temporal meaning or become a parallel contract, schema, policy, evidence, or release authority.

The prior README described this directory as a "six-time-kind temporal model and acceptance checks." At the pinned repository snapshot, neither capability is implemented. That phrase is retained as historical intent only and is `PROPOSED / CONFLICTED` until the repository's temporal vocabularies are reconciled and executable behavior is proven.

## Authority and placement

Directory Rules places this package under `packages/` because its primary responsibility is shared reusable implementation code. The existing path is preserved; this revision adds no root, lifecycle phase, schema home, policy home, receipt home, proof home, or release authority.

| Surface | Responsibility | Current posture |
|---|---|---|
| [`packages/`](../README.md) | Canonical root for shared reusable implementation libraries. | `CONFIRMED` repository path and root guidance |
| `packages/temporal/` | Package identity, package-level boundary, and implementation orientation. | `CONFIRMED` scaffold; this README remains draft |
| [`packages/temporal/src/`](./src/README.md) | Source-code envelope. | `CONFIRMED` placeholder |
| [`packages/temporal/src/temporal/`](./src/temporal/README.md) | Python module namespace and module-level boundary. | `CONFIRMED` placeholder; no runtime API |
| [`contracts/common/temporal_window.md`](../../contracts/common/temporal_window.md) | Semantic meaning of the current common temporal-window value object. | `CONFIRMED` draft contract |
| [`temporal_window.schema.json`](../../schemas/contracts/v1/common/temporal_window.schema.json) | Current machine-checkable shape and `time_kind` enum. | `CONFIRMED` file; schema metadata says `PROPOSED` |
| [`validate_temporal_window.py`](../../tools/validators/validate_temporal_window.py) | Repository-wide validator entry point. | `CONFIRMED` placeholder; raises `NotImplementedError` |
| [`ADR-0014`](../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md) | Proposed six-kind vocabulary and migration direction. | `CONFIRMED` file; ADR status is `proposed` |

### Document authority graph

| Document | Relationship to this README | Authority boundary |
|---|---|---|
| [`packages/README.md`](../README.md) | Parent root contract | Governs shared-library placement and public-boundary expectations. |
| This README | Canonical package orientation | Describes the package envelope; does not define temporal semantics. |
| [`src/README.md`](./src/README.md) | Companion source-envelope document | Describes source-tree responsibility and current inventory. |
| [`src/temporal/README.md`](./src/temporal/README.md) | Companion module document | Describes the Python namespace and implementation boundary. |
| [`temporal_window` contract](../../contracts/common/temporal_window.md) | Semantic authority for the current value object | Defines meaning, not executable package behavior. |
| [`temporal_window` schema](../../schemas/contracts/v1/common/temporal_window.schema.json) | Machine-shape authority | Defines shape, not semantic correctness or policy permission. |
| [`ADR-0014`](../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md) | Proposed decision | Does not control implementation until accepted and reconciled. |

No duplicate package README or generated, mirrored, localized, or superseded copy was established in the inspected path set. The source and module READMEs are companions at narrower boundaries, not competing package authorities.

## Current implementation

The repository snapshot establishes this package inventory:

```text
packages/temporal/
|-- README.md
|-- pyproject.toml
`-- src/
    |-- README.md
    `-- temporal/
        |-- README.md
        |-- __init__.py
        `-- core.py
```

| File | Confirmed state | What it does not prove |
|---|---|---|
| [`pyproject.toml`](./pyproject.toml) | Declares project name `kfm-temporal` and version `0.0.0`. | A build backend, supported Python version, dependencies, package discovery, entry points, or test configuration. |
| [`src/temporal/__init__.py`](./src/temporal/__init__.py) | Empty. | Any public or internal import surface. |
| [`src/temporal/core.py`](./src/temporal/core.py) | Contains one greenfield-placeholder comment. | Parsing, normalization, interval, comparison, freshness, or validation behavior. |
| [`src/README.md`](./src/README.md) | Documents the source envelope and bounded implementation state. | Executable behavior or consumer integration. |
| [`src/temporal/README.md`](./src/temporal/README.md) | Documents the module boundary, vocabulary conflict, and validation burden. | A runtime API or accepted temporal decision. |

No package-local test command is declared by the inspected metadata. No implemented temporal symbols, package exports, runtime consumers, or package-local tests were established by direct reads and bounded repository search at the evidence snapshot. Absence claims are limited to those inspected files and searches; they are not a byte-complete proof that no concurrent or unindexed work exists.

> [!WARNING]
> Do not document or import `TemporalInterval`, `TemporalProfile`, `coerce_utc`, `intervals_overlap`, `contains_instant`, `classify_staleness`, `validate_half_open_interval`, or other helper names as current behavior unless code and tests at the selected ref establish them.

## Temporal vocabulary conflict

The repository currently contains non-equivalent temporal vocabularies:

| Surface | Vocabulary at the pinned snapshot | Authority state |
|---|---|---|
| [`temporal_window.schema.json`](../../schemas/contracts/v1/common/temporal_window.schema.json) | `observed`, `published`, `ingested`, `effective`, `corrected`, `superseded` | Checked-in machine shape with `x-kfm.status: PROPOSED` |
| [`ADR-0014`](../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md) | `source_time`, `observed_time`, `ingested_time`, `decision_time`, `published_time`, `retraction_time` | Proposed decision; not accepted |
| [`time-aware.md`](../../docs/doctrine/time-aware.md) | Source, observed, valid, retrieval, release, correction, and transaction time | Draft doctrine |

The sets overlap but are not interchangeable. Until an accepted decision and compatible contract/schema changes reconcile them:

1. Do not hard-code a new canonical enum in this package.
2. Do not silently translate one vocabulary into another.
3. Represent any compatibility crosswalk as explicit, versioned, reviewable data.
4. Preserve original time kind, precision, timezone/calendar context, uncertainty, and lineage when the controlling contract requires them.
5. Keep parsing, schema acceptance, semantic correctness, evidence sufficiency, policy permission, review state, and release state separate.
6. Label examples and proposed APIs `PROPOSED`; do not present them as current package behavior.

The current `temporal_window` schema requires `start`, `end`, and `time_kind`, treats both endpoints as JSON Schema `date-time` strings, and rejects additional top-level properties. That shape alone does not establish endpoint ordering, interval inclusivity, open intervals, timezone normalization, calendar rules, precision, uncertainty, freshness, correction closure, or bitemporal behavior.

## What belongs here

Only shared reusable implementation code belongs in this package, such as:

- value objects and adapters that implement an accepted temporal contract;
- deterministic parsing and serialization helpers;
- interval ordering, overlap, adjacency, and containment operations with contract-backed boundary semantics;
- explicit, versioned vocabulary crosswalks backed by an accepted decision and tests;
- low-level validation helpers reused by repository validators;
- package-private utilities and type definitions;
- package documentation tied to actual exports and behavior.

Every new behavior claim remains `PROPOSED` until the implementation, fixtures, tests, and consuming boundary establish it.

## What does not belong here

| Excluded responsibility | Correct authority or home |
|---|---|
| Temporal object meaning, field intent, and semantic invariants | [`contracts/`](../../contracts/README.md) |
| Machine-readable fields, formats, and enum values | [`schemas/contracts/v1/`](../../schemas/contracts/v1/README.md) |
| Allow, deny, restrict, redact, freshness, or release decisions | [`policy/`](../../policy/README.md) |
| Repository-wide validator entry points | [`tools/validators/`](../../tools/validators/README.md) |
| Valid, invalid, denied, abstained, or quarantined examples | The repository's verified fixture and test lanes |
| Raw, work, quarantine, processed, catalog, triplet, proof, receipt, or published data | The correct lifecycle lane under [`data/`](../../data/README.md) |
| Release manifests, correction notices, withdrawal notices, and rollback decisions | [`release/`](../../release/README.md) |
| Domain-specific temporal rules | The owning domain contract, schema, policy, package, fixtures, and tests |
| Public API routes, UI rendering, or model-runtime responses | The appropriate governed application or runtime boundary |
| Source fetching or admission | The appropriate connector and pipeline boundary |

This package must not mint evidence, infer an unknown date as fact, approve promotion, authorize public exposure, publish data, erase correction history, or present generated language as temporal authority.

## Inputs, outputs, and consumers

### Current interfaces

| Interface | Current status |
|---|---|
| Public imports | None confirmed. |
| Internal imports | None confirmed. |
| Accepted runtime inputs | None implemented. |
| Emitted runtime outputs | None implemented. |
| Declared entry points | None confirmed. |
| Dependencies | None declared by the inspected package metadata. |
| Downstream consumers | `UNKNOWN` beyond documentation references. |

### Future implementation boundary

When implementation begins, inputs should be contract-shaped temporal values plus explicit versioned context required by the accepted vocabulary. Outputs should be deterministic values or finite local validation results.

Future interfaces should preserve, when required:

- the time kind or dimension;
- original value, precision, timezone, and calendar context;
- open, approximate, disputed, unknown, and not-applicable states without magic dates;
- correction, supersession, and retraction lineage;
- the owning record, evidence, receipt, decision, or release identity;
- the vocabulary and contract version used by the operation.

Package output alone must not be represented as proof of temporal truth, evidence closure, a policy decision, review approval, release approval, correction closure, rollback approval, or a public response envelope.

## Trust boundaries

Future code in this package must preserve these invariants:

1. A timestamp's kind is part of its meaning; distinct kinds must not collapse into a generic `date` or `timestamp`.
2. Parsing success proves syntax only. Schema validation proves shape only.
3. Semantic checks, evidence resolution, policy decisions, review, release, correction, and rollback remain separate governed responsibilities.
4. Unknown, approximate, open-ended, disputed, and not-applicable values remain distinguishable when the controlling contract supports them.
5. Corrections and supersessions add auditable facts; they do not erase prior history.
6. Identical inputs, configuration, vocabulary version, and timezone/calendar rules produce deterministic output.
7. Temporal helpers do not bypass the lifecycle spine:

   ```text
   RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
   ```

8. Public clients receive temporal claims through governed interfaces and released artifacts, with EvidenceBundle and policy context appropriate to the claim.
9. Sensitive temporal joins involving living people, genomic data, land, cultural resources, protected species, archaeology, infrastructure, or precise locations fail closed or use reviewed generalization and staged access.

## Validation

### Current validation state

| Check | Outcome | Evidence boundary |
|---|---|---|
| Package identity | `CONFIRMED` | `kfm-temporal`, version `0.0.0`. |
| Namespace export surface | `CONFIRMED empty` | `src/temporal/__init__.py`. |
| Core implementation | `CONFIRMED placeholder` | `src/temporal/core.py` is comment-only. |
| Common temporal-window schema | `CONFIRMED file; PROPOSED status` | File inspection; no runtime schema-validation result is claimed here. |
| Declared temporal-window validator | `CONFIRMED placeholder` | The script raises `NotImplementedError`. |
| Package-local runtime tests | `NOT RUN / not established` | The inspected package metadata declares no test command or test configuration. |
| Ordering, boundary, timezone, calendar, uncertainty, freshness, and bitemporal behavior | `UNKNOWN` | No implementation or proof was established. |
| Downstream integration | `UNKNOWN` | No implemented consumer was confirmed by bounded search. |

### Minimum evidence before calling the package functional

- [ ] An accepted controlling vocabulary or explicit versioned compatibility decision exists.
- [ ] Semantic contracts and machine schemas agree on supported fields and kinds.
- [ ] `pyproject.toml` defines a build backend, supported Python versions, package discovery, and dependencies as needed.
- [ ] `src/temporal/__init__.py` exposes only documented, implemented symbols.
- [ ] Valid and invalid fixtures cover every supported kind and boundary condition.
- [ ] Tests cover ordering, equality, overlap, adjacency, open/unknown states, timezone/calendar behavior, precision, uncertainty, correction, and supersession as applicable.
- [ ] Negative tests prove ambiguous, unsupported, non-monotone, and conflicting inputs fail explicitly.
- [ ] The repository validator is implemented beyond `NotImplementedError` and remains separate from policy.
- [ ] Deterministic serialization and compatibility behavior are proven.
- [ ] Downstream consumers pin the vocabulary and contract versions they expect.
- [ ] Public-boundary tests prove no caller treats package output alone as evidence, policy, release, or publication authority.

Do not invent a package-local installation or test command until repository metadata and tooling define one.

## Review burden

[`CODEOWNERS`](../../.github/CODEOWNERS) routes `packages/` changes to `@bartytime4life`. That entry is review routing only; it does not prove temporal stewardship, independent approval, completed review, policy approval, release approval, or branch-protection enforcement.

Functional changes require the responsible contract, schema, validation, package, policy, security, sensitivity, and release reviewers when they affect:

- vocabulary or field meaning;
- schema shape or compatibility;
- interval and ordering semantics;
- timezone, calendar, precision, or uncertainty rules;
- correction, supersession, retraction, or freshness behavior;
- public labels or governed response payloads;
- sensitive-domain joins or location exposure;
- stored values, migrations, or release rollback.

No accepted ADR authorizing a new package authority was established. ADR-0014 remains proposed, and this README does not accept it by implication.

## Change, correction, and rollback

For a behavior change:

1. Update semantic contracts before or with changes in meaning.
2. Update schemas when machine shape or enum values change.
3. Add deterministic valid, invalid, and negative fixtures.
4. Implement focused tests and the repository validator.
5. Review policy, rights, sensitivity, and public-payload impact separately.
6. Version compatibility and migration behavior for stored values and consumers.
7. Preserve evidence, correction, supersession, and release lineage.
8. Record an explicit rollback target and rerun the same validation after rollback.

For this documentation-only revision, rollback is a transparent revert of the implementation commit or, after merge, a revert pull request. Reverting this README changes no runtime behavior because this revision does not modify code, contracts, schemas, policy, tests, data, or release artifacts.

## Evidence basis

Direct repository evidence is bounded to `bartytime4life/Kansas-Frontier-Matrix@f9c257b8f9ba9479bce69dfa2fd2411b9cdcf566`. Connector code search was indexed at `eac8668ca9786773fcb015f9ba099e0e1dadeb35`; comparison to the pinned base found no intervening workflow changes. Base movement after authoring changed only a Habitat/Fauna proof README and its generated receipt; the temporal target and inspected governing files remained unchanged.

| Evidence | Supports | Does not prove |
|---|---|---|
| Current package README blob `974a7137983aa8d88605fad07fbca2b6e0026e04` | The prior file was a three-line stub and named six-time-kind model/acceptance-check intent. | Implemented behavior. |
| [`pyproject.toml`](./pyproject.toml), [`__init__.py`](./src/temporal/__init__.py), and [`core.py`](./src/temporal/core.py) | Package identity, version, empty export surface, and placeholder implementation. | Buildability, compatibility, or consumers. |
| [`src/README.md`](./src/README.md) and [`src/temporal/README.md`](./src/temporal/README.md) | Narrower source and module boundaries, inventory, and open verification state. | Runtime implementation. |
| [`temporal_window` contract](../../contracts/common/temporal_window.md) | Draft semantic meaning and documented limits of the current value object. | Implemented validation or package integration. |
| [`temporal_window` schema](../../schemas/contracts/v1/common/temporal_window.schema.json) | Current fields, required set, enum, formats, and additional-properties rule. | Chronology, timezone, freshness, evidence, policy, or release behavior. |
| [`validate_temporal_window.py`](../../tools/validators/validate_temporal_window.py) | Declared validator path and placeholder state. | Passing validation behavior. |
| [`ADR-0014`](../../docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md) | Proposed six-kind vocabulary and unresolved migration questions. | An accepted temporal decision. |
| [`time-aware.md`](../../docs/doctrine/time-aware.md) | Draft time-awareness doctrine and seven-dimension posture. | Reconciled fields or implemented behavior. |
| [`Directory Rules`](../../docs/doctrine/directory-rules.md) | `packages/` placement and responsibility-root boundary. | Temporal semantics or runtime maturity. |
| [`DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | Inspected repository drift register. | Resolution of the temporal vocabulary conflict; no temporal-specific resolution was established there. |

## Open verification items

- **NEEDS VERIFICATION:** Which temporal vocabulary will become controlling and how existing values will migrate or crosswalk.
- **NEEDS VERIFICATION:** Interval inclusivity/exclusivity, ordering, adjacency, and open-ended representation.
- **NEEDS VERIFICATION:** Timezone normalization, original-offset preservation, calendars, precision, and uncertainty.
- **NEEDS VERIFICATION:** Whether valid-time and transaction-time support belongs in this package and in which contract version.
- **NEEDS VERIFICATION:** Package build configuration, supported Python versions, dependencies, exports, and import name.
- **NEEDS VERIFICATION:** Package-local fixtures, tests, repository-native commands, CI coverage, and downstream consumers.
- **NEEDS VERIFICATION:** Policy behavior for stale, corrected, superseded, embargoed, or evidence-incomplete temporal claims.
- **NEEDS VERIFICATION:** Accepted package, temporal, contract, schema, validation, policy, and release stewardship.
- **UNKNOWN:** Branch-protection and required-check enforcement for package documentation changes.

## Last reviewed

- Date: 2026-07-21
- Repository: `bartytime4life/Kansas-Frontier-Matrix`
- Evidence snapshot: `main@f9c257b8f9ba9479bce69dfa2fd2411b9cdcf566`
- Target baseline blob: `974a7137983aa8d88605fad07fbca2b6e0026e04`
- Code-search snapshot: `eac8668ca9786773fcb015f9ba099e0e1dadeb35`
- Runtime execution: not performed; repository content was inspected through the GitHub connector
- Human review: pending

<details>
<summary>No-loss preservation note</summary>

The prior README asserted two intended responsibilities: a six-time-kind temporal model and acceptance checks. This revision preserves both as visible future intent while correcting their evidence status:

- the package does not currently implement a temporal model;
- the declared validator is a placeholder;
- the checked-in schema, proposed ADR-0014, and draft doctrine use non-equivalent vocabularies;
- future acceptance checks require contracts, schemas, fixtures, executable validation, tests, policy separation, and consumer evidence.

</details>

<p align="right"><a href="#top">Back to top</a></p>
