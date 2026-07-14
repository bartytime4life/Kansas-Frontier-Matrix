<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-catalog-src-readme
title: Catalog Package Source Root README
type: readme
version: v0.2
status: draft
owners:
  - <package-owner>
  - <catalog-steward>
  - <schema-steward>
  - <evidence-steward>
  - <release-steward>
  - <security-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-07-14
policy_label: public
path: packages/catalog/src/README.md
related:
  - ../../README.md
  - ../README.md
  - ../pyproject.toml
  - catalog/README.md
  - catalog/__init__.py
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../../docs/standards/STAC.md
  - ../../../docs/standards/DCAT.md
  - ../../../docs/standards/PROV.md
  - ../../../contracts/data/catalog_matrix.md
  - ../../../schemas/contracts/v1/data/catalog_matrix.schema.json
  - ../../../tools/validators/validate_catalog_matrix.py
  - ../../../tools/validators/catalog/README.md
  - ../../../pipelines/catalog/README.md
  - ../../../data/catalog/README.md
  - ../../../.github/CODEOWNERS
tags: [kfm, packages, catalog, src-layout, python, scaffold, shared-library, source-root, stac, dcat, prov, catalog-matrix, deterministic-serialization, lifecycle-boundary, governance]
notes:
  - "v0.2 preserves the source-root boundary from v0.1 and adds a commit-pinned repository snapshot, Python src-layout guidance, current scaffold inventory, import/export rules, interface contracts, dependency boundaries, validation strategy, safe-change sequence, rollback guidance, and evidence ledger."
  - "Remote repository evidence was inspected on main at commit 03e92d65ad07188dea60cafb7a26ae3919268d41."
  - "packages/catalog/pyproject.toml confirms a greenfield Python project placeholder named kfm-catalog at version 0.0.0; it does not define a build backend, dependencies, package discovery, entry points, or publishable artifact."
  - "packages/catalog/src/catalog/__init__.py exists and is empty. No package exports or import-time behavior are established."
  - "The child catalog module README is v0.2 and records exact-path absence of proposed STAC, DCAT, and PROV modules plus unresolved CatalogMatrix contract/schema/validator drift."
  - "Exact checks for tests/packages/catalog/README.md, fixtures/packages/catalog/README.md, and packages/catalog/src/__init__.py returned no file."
  - "No catalog helper implementation, package build, dependency lock, package-specific tests, package fixtures, dedicated CI workflow, consuming imports, lifecycle writes, release behavior, or runtime maturity is claimed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Package Source Root

> Python `src`-layout root for the `packages/catalog/` shared catalog support package. The current repository surface is a **greenfield scaffold**, not an implemented catalog library: package metadata names `kfm-catalog` version `0.0.0`, the import package initializer is empty, and package-local tests, fixtures, exports, dependencies, and working catalog helpers are not established.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fcatalog%2Fsrc%2F-0a7ea4)
![runtime](https://img.shields.io/badge/runtime-Python%20src--layout-3776ab)
![implementation](https://img.shields.io/badge/implementation-SCAFFOLD-yellow)
![authority](https://img.shields.io/badge/authority-shared%20source%20root-0a7ea4)
![catalog](https://img.shields.io/badge/catalog-carrier%20not%20truth-d62728)

> [!IMPORTANT]
> **Document status:** draft  
> **Repository evidence snapshot:** `main` at `03e92d65ad07188dea60cafb7a26ae3919268d41`  
> **Parent package:** `packages/catalog/`  
> **Confirmed Python scaffold:** [`../pyproject.toml`](../pyproject.toml), [`catalog/`](catalog/README.md), and empty [`catalog/__init__.py`](catalog/__init__.py)  
> **Current source implementation:** no exported helpers or implemented STAC/DCAT/PROV modules are established by the inspected evidence  
> **Authority boundary:** source code here is not catalog data, proof, policy, release, schema, contract, source-registry, pipeline, or public API authority  
> **Public posture:** ordinary public clients consume governed, release-aware catalog projections—not package internals or lifecycle candidates

> [!CAUTION]
> Importing this package must never trigger catalog generation, network access, lifecycle reads or writes, policy evaluation, release decisions, model calls, source acquisition, or publication. A package import is not a governed state transition.

---

## Quick jump

- [1. Purpose and audience](#1-purpose-and-audience)
- [2. Current repository state](#2-current-repository-state)
- [3. Bounded context and ubiquitous language](#3-bounded-context-and-ubiquitous-language)
- [4. Placement and authority](#4-placement-and-authority)
- [5. Source-root responsibilities](#5-source-root-responsibilities)
- [6. Explicit non-ownership](#6-explicit-non-ownership)
- [7. Current and proposed layout](#7-current-and-proposed-layout)
- [8. Import and export contract](#8-import-and-export-contract)
- [9. Inputs, outputs, and side effects](#9-inputs-outputs-and-side-effects)
- [10. Standards and CatalogMatrix alignment](#10-standards-and-catalogmatrix-alignment)
- [11. Determinism, identity, and temporal handling](#11-determinism-identity-and-temporal-handling)
- [12. Dependency and integration boundaries](#12-dependency-and-integration-boundaries)
- [13. Validation and test strategy](#13-validation-and-test-strategy)
- [14. Security, rights, sensitivity, and public safety](#14-security-rights-sensitivity-and-public-safety)
- [15. Implementation admission sequence](#15-implementation-admission-sequence)
- [16. Generated code, compatibility, and migrations](#16-generated-code-compatibility-and-migrations)
- [17. Correction and rollback](#17-correction-and-rollback)
- [18. Definition of done](#18-definition-of-done)
- [19. Open verification register](#19-open-verification-register)
- [20. Evidence ledger](#20-evidence-ledger)
- [21. Maintainer checklist](#21-maintainer-checklist)

---

## 1. Purpose and audience

`packages/catalog/src/` is the Python source root for the shared catalog-support package declared by [`packages/catalog/pyproject.toml`](../pyproject.toml).

Its intended purpose is to host importable, reusable, non-deployable implementation code that may eventually support:

- catalog-shaped object construction from already-governed inputs;
- STAC, DCAT, PROV-O, and PAV mapping helpers;
- catalog-profile dispatch;
- reference preservation across source, evidence, receipt, policy, review, release, correction, and rollback objects;
- deterministic identifiers, canonical serialization, and digest calculation;
- schema-bound validation adapters and safe validation results;
- compatibility adapters for explicitly versioned profile migrations;
- package-local types generated from canonical schemas with generation provenance;
- pure fixture builders used by tests, provided they cannot be mistaken for production catalog records.

This root does **not** own executable catalog orchestration. Catalog transitions, authorized writes, receipts, release handoffs, and publication gates belong to [`pipelines/catalog/`](../../../pipelines/catalog/README.md), lifecycle roots, tools, policy, and release surfaces.

**Primary audience**

- catalog package maintainers;
- catalog-pipeline and domain-pipeline maintainers;
- standards, contracts, schemas, evidence, policy, release, and correction stewards;
- validator and fixture maintainers;
- security, privacy, rights, and sensitivity reviewers;
- reviewers deciding whether proposed code belongs in a reusable package, a repository-wide tool, or an executable pipeline.

[Back to top](#top)

---

## 2. Current repository state

The table below separates current repository evidence from proposed implementation.

| Surface | Evidence at inspected ref | Status | Consequence |
|---|---|---|---|
| `packages/catalog/src/README.md` | Existing v0.1 README was read from `main`. | **CONFIRMED** | This revision updates the source-root contract in place. |
| [`packages/catalog/README.md`](../README.md) | Defines `packages/catalog/` as shared support subordinate to catalog pipelines, lifecycle data, evidence, policy, and release authority. | **CONFIRMED README** | This source root refines but must not contradict the package boundary. |
| [`packages/catalog/pyproject.toml`](../pyproject.toml) | Contains a greenfield comment, `[project]`, `name = "kfm-catalog"`, and `version = "0.0.0"`. | **CONFIRMED Python placeholder** | Python intent and project identity are visible; packaging maturity is not. |
| `pyproject.toml` build metadata | No `[build-system]`, dependency list, optional dependency group, package discovery, entry point, or tool configuration appears in the inspected file. | **CONFIRMED absent from inspected content** | Do not claim an installable or publishable package. |
| [`catalog/README.md`](catalog/README.md) | Child module README is v0.2 and documents the module as a Python scaffold. | **CONFIRMED** | Source-root guidance must remain consistent with the child module. |
| [`catalog/__init__.py`](catalog/__init__.py) | File exists and is empty. | **CONFIRMED scaffold** | No exports, public API, version constant, or import-time behavior is established. |
| `packages/catalog/src/__init__.py` | Exact path returned no file. | **CONFIRMED absent at tested path** | This is consistent with a normal Python `src` layout; `src/` is a source container, not the import package. |
| `packages/catalog/package.json` | Exact path returned no file in the prior package inspection. | **CONFIRMED absent at tested path** | Do not claim a JavaScript or TypeScript implementation. |
| `catalog/stac.py` | Child-module inspection returned no file at the exact path. | **CONFIRMED absent at tested path** | STAC helper implementation is not established. |
| `catalog/dcat.py` | Child-module inspection returned no file at the exact path. | **CONFIRMED absent at tested path** | DCAT helper implementation is not established. |
| `catalog/prov.py` | Child-module inspection returned no file at the exact path. | **CONFIRMED absent at tested path** | PROV/PAV helper implementation is not established. |
| Indexed `packages/catalog` search | Search returns the package README, `pyproject.toml`, this README, and the child README; empty or unindexed files require exact checks. | **CONFIRMED search result / incomplete tree proof** | A full recursive tree remains unavailable through the current connector evidence. |
| `tests/packages/catalog/README.md` | Exact path returned no file. | **CONFIRMED absent at tested path** | A package-specific test lane is not documented at the expected home. |
| `fixtures/packages/catalog/README.md` | Exact path returned no file. | **CONFIRMED absent at tested path** | A package-specific fixture lane is not documented at the expected home. |
| Package-specific CODEOWNERS | [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) contains a repository-wide default but no `packages/catalog/` rule. | **CONFIRMED** | Catalog package ownership remains unresolved. |
| Dedicated catalog-package workflow | Repository search for `packages/catalog` did not surface a workflow file. | **NOT OBSERVED / search-limited** | Do not claim dedicated package CI. |
| [`contracts/data/catalog_matrix.md`](../../../contracts/data/catalog_matrix.md) | Semantic contract exists and explicitly says its schema is a placeholder. | **CONFIRMED contract** | Source code must follow meaning authority without treating the schema as semantically complete. |
| [`schemas/contracts/v1/data/catalog_matrix.schema.json`](../../../schemas/contracts/v1/data/catalog_matrix.schema.json) | Requires only `id` and allows additional properties. | **CONFIRMED placeholder schema / status PROPOSED** | Schema validity alone does not establish closure, evidence, policy, or release readiness. |
| [`tools/validators/validate_catalog_matrix.py`](../../../tools/validators/validate_catalog_matrix.py) | Exists but raises `NotImplementedError("Greenfield placeholder")`. | **CONFIRMED stub** | A working repo-wide CatalogMatrix validator is not established. |
| Schema-declared validator path | `tools/validators/data/validate_catalog_matrix.py` was not found in the child-module evidence pass. | **CONFIRMED absent at tested path** | Schema metadata and repository implementation are misaligned. |
| [`tools/validators/catalog/README.md`](../../../tools/validators/catalog/README.md) | Documents a proposed validator lane and explicitly does not confirm executables. | **CONFIRMED README / implementation proposed** | Package adapters must not imply validator maturity. |
| [`pipelines/catalog/README.md`](../../../pipelines/catalog/README.md) | Documents executable `PROCESSED -> CATALOG / TRIPLET` responsibility. | **CONFIRMED README / execution depth unknown** | Lifecycle transitions and writes stay outside this source root. |
| [`data/catalog/README.md`](../../../data/catalog/README.md) | Documents the catalog-stage lifecycle lane and release-gated exposure. | **CONFIRMED README** | Package code must not write there implicitly or equate location with publication. |

### Evidence boundary

The connector did not expose a complete recursive tree listing. Exact-file checks and indexed search support the snapshot, but unindexed files remain possible.

```text
Python project placeholder         = CONFIRMED
Python src-layout intent           = CONFIRMED
import package directory           = CONFIRMED
empty package initializer          = CONFIRMED
implemented catalog helpers        = NOT OBSERVED
public package exports             = UNKNOWN
build backend                      = NOT DECLARED
runtime dependencies               = NOT DECLARED
development/test dependencies      = NOT DECLARED
package-specific tests             = NOT OBSERVED
package-specific fixtures          = NOT OBSERVED
dedicated package CI               = NOT OBSERVED
consuming imports                  = UNKNOWN
working CatalogMatrix validator    = NOT ESTABLISHED
catalog lifecycle write behavior   = UNKNOWN
package installation/build result  = NOT RUN
```

[Back to top](#top)

---

## 3. Bounded context and ubiquitous language

### Bounded context

Within KFM, `packages/catalog/src/` means:

> The source container for reusable, non-deployable Python catalog-support code that transforms already-governed in-memory inputs into catalog-shaped values or validation results without owning acquisition, lifecycle transitions, evidence closure, policy decisions, release approval, persistence, or public exposure.

It does not mean:

- an executable catalog pipeline;
- a STAC API or catalog server;
- a source connector;
- a repository-wide validator command;
- a data-access layer;
- a lifecycle writer;
- an EvidenceBundle or ProofPack builder;
- a policy engine;
- a release service;
- a public-client trust membrane.

### Ubiquitous language

| Term | Meaning in this source root |
|---|---|
| **Source root** | Filesystem container used by Python packaging to separate importable code from project metadata and repository files. |
| **Import package** | `catalog/`, the directory Python callers would import after packaging is configured. |
| **Public export** | A deliberately supported symbol exposed through `catalog.__init__` or documented import paths. No public exports are currently established. |
| **Catalog helper** | Pure or side-effect-minimal reusable code that constructs, normalizes, serializes, validates, or translates catalog-shaped values. |
| **Catalog candidate** | Not-yet-public catalog-shaped data awaiting validation, policy, evidence, review, and release checks. |
| **Catalog record** | Discovery/interchange carrier such as STAC, DCAT, PROV, or a domain catalog projection. It is not proof or publication approval. |
| **CatalogMatrix** | Governed cross-record or catalog/evidence relationship descriptor whose authority and placement remain partly conflicted in current proposed ADRs. |
| **Reference preservation** | Carrying identifiers and refs without inventing, resolving, authorizing, or silently dropping them. |
| **Validation adapter** | Package-level function that invokes or translates a canonical validator result without becoming schema or policy authority. |
| **Canonical serialization** | Stable byte or text representation produced under a named, versioned rule. |
| **Hidden I/O** | Filesystem, database, network, environment, clock, randomness, or process behavior not explicit in the function contract. |
| **Generated code** | Source emitted from canonical schemas or profiles with generator version, input digest, and regeneration instructions. |
| **Compatibility adapter** | Temporary, documented translation between versioned shapes with a removal condition and rollback path. |

[Back to top](#top)

---

## 4. Placement and authority

Directory Rules place a shared library used by multiple deployables under `packages/`. This source root is appropriate because its primary responsibility is reusable implementation code.

```text
packages/catalog/              = shared package boundary and project metadata
packages/catalog/src/          = Python source container
packages/catalog/src/catalog/  = import package / catalog helper module
pipelines/catalog/             = executable catalog lifecycle orchestration
tools/validators/              = repository-wide validator entrypoints
data/catalog/                  = catalog-stage lifecycle records
data/triplets/                 = graph/triplet projection
data/proofs/                   = evidence and proof support
data/receipts/                 = process memory
contracts/                     = object meaning
schemas/                       = machine-checkable shape
policy/                        = admissibility and exposure decisions
release/                       = promotion, correction, withdrawal, rollback
apps/governed-api/             = governed public/semi-public interface
```

| Question | Answer | Status |
|---|---|---|
| Why `packages/catalog/src/`? | It is the source container for the shared catalog package. | **CONFIRMED path and Python scaffold** |
| Why not `pipelines/catalog/`? | Shared functions may be reused, but executable lifecycle transitions belong to pipelines. | **CONFIRMED responsibility split** |
| Why not `tools/validators/`? | Package adapters may support validation, but repository-wide validator commands belong under tools. | **CONFIRMED Directory Rules split** |
| May this root define object meaning? | No. Meaning remains in `contracts/`. | **CONFIRMED authority separation** |
| May this root define canonical machine shape? | No. Shape remains in `schemas/`. | **CONFIRMED authority separation** |
| May this root decide policy? | No. It may preserve policy state or translate results only. | **CONFIRMED authority separation** |
| May this root create evidence closure? | No. It may carry refs; proof creation and resolution remain outside. | **CONFIRMED trust posture** |
| May this root approve publication or rollback? | No. Release authority remains in `release/`. | **CONFIRMED release separation** |
| May this root write catalog records? | Not as a hidden package side effect. Authorized pipeline/tool callers own writes and receipts. | **CONFIRMED lifecycle boundary** |

> [!IMPORTANT]
> The existence of a Python package does not grant it authority. Code location makes reusable implementation ownership visible; it does not transfer semantic, schema, policy, evidence, data, or release authority into the package.

[Back to top](#top)

---

## 5. Source-root responsibilities

This root may eventually own implementation support for:

### 5.1 Package organization

- import package layout;
- internal module boundaries;
- deliberate public export surface;
- package version exposure when tied to project metadata;
- package-local typing protocols and implementation-only types;
- optional generated-code namespace when governance is established.

### 5.2 Pure catalog transformations

- mapping already-governed values into STAC/DCAT/PROV-shaped dictionaries or typed objects;
- namespaced extension-field handling;
- non-lossy reference preservation;
- profile dispatch based on explicit input type and profile version;
- deterministic ordering and canonicalization;
- safe validation-result normalization;
- versioned compatibility translation.

### 5.3 Validation support

- adapters that call canonical validators;
- validation error normalization that does not leak internals or restricted values;
- shared precondition checks that do not become policy decisions;
- deterministic helper-level checks suitable for unit tests.

### 5.4 Test support

- pure builders for synthetic objects;
- deterministic expected values;
- no-network mocks clearly marked non-authoritative;
- golden serialization helpers when fixture placement is accepted.

[Back to top](#top)

---

## 6. Explicit non-ownership

| This source root does not own | Correct responsibility home |
|---|---|
| Source acquisition or source-specific clients | `connectors/` |
| Catalog pipeline runners and lifecycle orchestration | [`pipelines/catalog/`](../../../pipelines/catalog/README.md) or accepted domain pipeline lane |
| Declarative pipeline configuration | `pipeline_specs/` |
| Repository-wide validators or generator CLIs | `tools/` |
| One-off operational scripts | `scripts/` |
| Catalog-stage data instances | [`data/catalog/`](../../../data/catalog/README.md) |
| Graph/triplet records | `data/triplets/` |
| EvidenceBundles, ProofPacks, and proof-side closure | `data/proofs/` |
| Run and catalog-build receipts | `data/receipts/` |
| Source descriptors and rights metadata | `data/registry/` and source documentation/policy homes |
| Semantic contracts | `contracts/` |
| Canonical JSON Schemas | `schemas/contracts/v1/` |
| Policy rules or policy decisions | `policy/` |
| Release manifests, promotion decisions, corrections, withdrawals, rollback cards | `release/` |
| Public API routes or direct public serving | `apps/governed-api/` |
| UI rendering | `apps/explorer-web/` or a verified UI package |
| Package tests as the canonical test home | `tests/packages/catalog/` when created |
| Package fixtures as the canonical fixture home | `fixtures/packages/catalog/` when created |
| Secrets, credentials, raw prompts, or private source payloads | approved secret/data controls; never package source |

[Back to top](#top)

---

## 7. Current and proposed layout

### 7.1 Confirmed scaffold

The evidence supports this minimal layout:

```text
packages/catalog/
├── README.md
├── pyproject.toml                  # greenfield placeholder
└── src/
    ├── README.md                   # this file
    └── catalog/
        ├── README.md
        └── __init__.py             # empty
```

This is a **scaffold inventory**, not a guarantee that no additional unindexed file exists.

### 7.2 Proposed implementation layout

A future implementation might use:

```text
packages/catalog/
├── pyproject.toml
└── src/
    └── catalog/
        ├── __init__.py
        ├── models.py
        ├── dispatch.py
        ├── stac.py
        ├── dcat.py
        ├── prov.py
        ├── refs.py
        ├── serialization.py
        ├── validation.py
        ├── errors.py
        └── _internal/
```

Every proposed file remains **PROPOSED**. Module names should follow actual cohesive responsibilities, not this illustrative tree by default.

### 7.3 Layout rules

- `src/` should remain a source container, not an import namespace.
- Importable code should live under `src/catalog/`.
- `src/__init__.py` is not required for a conventional `src` layout and should not be added merely for symmetry.
- Public imports should be deliberate and documented.
- Internal modules should use a clear private convention where appropriate.
- Generated code should not be mixed with hand-written source without a generation boundary.
- Tests and fixtures should not be hidden under source solely for convenience.
- Data files, catalogs, receipts, proofs, or release artifacts must not be committed inside the package source tree.

[Back to top](#top)

---

## 8. Import and export contract

### 8.1 Current state

`catalog/__init__.py` is empty. Therefore current evidence establishes:

```text
public exports         = none confirmed
import-time behavior   = none observed in the empty initializer
package __version__    = not defined
entry points           = not defined
plugin registry        = not defined
```

### 8.2 Import safety

Future imports must be:

- side-effect free;
- network free;
- lifecycle-storage free;
- policy-decision free;
- release-decision free;
- deterministic;
- fast enough for tests and tools;
- safe when optional integrations are unavailable.

Disallowed import-time behavior includes:

```text
read environment secrets
open lifecycle files
connect to databases or object stores
fetch external STAC/DCAT/PROV resources
register public routes
run migrations
emit catalog records
write receipts
evaluate policy
invoke model runtimes
publish artifacts
```

### 8.3 Public API discipline

Before exposing a symbol from `catalog.__init__`:

1. define its semantic responsibility;
2. identify constraining contracts/schemas/profiles;
3. specify input and output types;
4. define error behavior;
5. prove deterministic behavior where required;
6. add tests;
7. record compatibility posture;
8. document deprecation and rollback expectations.

Avoid exporting implementation details merely because another module needs them. Prefer narrow, stable interfaces over a broad re-export surface.

[Back to top](#top)

---

## 9. Inputs, outputs, and side effects

### 9.1 Accepted inputs

Helpers may accept already-governed, in-memory values such as:

| Input family | Examples | Required posture |
|---|---|---|
| Catalog source values | normalized metadata dictionaries, typed domain projections | Already validated to the helper's declared preconditions |
| Standard profiles | explicit STAC/DCAT/PROV profile identifiers and versions | Versioned; no ambient default that changes silently |
| References | source, evidence, receipt, policy, review, release, correction, rollback refs | Preserve exactly; do not invent or silently resolve |
| Artifact metadata | media type, roles, size, digest, spatial/temporal extent | Derived from authorized inputs or caller-provided evidence |
| Validation context | schema/profile ref, validation options | Explicit; no hidden global mutable configuration |
| Clock/randomness | injected timestamp or deterministic identifier source where needed | Injectable and testable; no uncontrolled wall clock/randomness |

### 9.2 Allowed outputs

Helpers may return:

- in-memory catalog candidate objects;
- typed or dictionary representations;
- deterministic serialized bytes/text;
- validation-result values;
- safe, structured errors;
- explicit warnings and limitations;
- versioned compatibility results;
- digest/identifier values under a named algorithm and profile.

### 9.3 Forbidden hidden outputs

Package helpers must not silently:

- write `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/receipts/`, or `release/`;
- mutate caller objects unless the contract explicitly says so;
- read or write network resources;
- use process-global mutable registries without explicit initialization;
- log restricted values;
- emit public URLs or release states that were not provided or resolved by governed callers;
- convert `ABSTAIN`, `DENY`, or unresolved state into an apparently successful catalog object.

### 9.4 Authorized I/O boundary

When I/O is required, prefer a split:

```text
pure package helper
  -> returns candidate / validation result
  -> executable pipeline or tool owns I/O
  -> caller emits receipt
  -> policy/release process governs exposure
```

Any future package-level I/O adapter must be explicit, narrow, dependency-injected, reviewed, testable, and prohibited from becoming the normal public path.

[Back to top](#top)

---

## 10. Standards and CatalogMatrix alignment

### 10.1 Standards dispatch

This source root may eventually implement adapters for:

| Standard | Package role | Must not become |
|---|---|---|
| [STAC](../../../docs/standards/STAC.md) | Construct or validate spatiotemporal catalog-shaped values. | A STAC API, source of truth, release decision, or proof. |
| [DCAT](../../../docs/standards/DCAT.md) | Construct or validate dataset/distribution metadata. | Dataset authority or permission to publish. |
| [PROV-O / PAV](../../../docs/standards/PROV.md) | Preserve activities, entities, agents, derivation, attribution, and version relations. | Full proof closure or a renamed KFM-only provenance vocabulary. |

Rules:

- extend standards through accepted profiles and namespaces; do not fork them;
- preserve standard predicates and field meanings;
- preserve KFM governance refs without placing unknown top-level fields where standards prohibit them;
- keep profile version explicit;
- retain unknown-but-valid extension fields unless an accepted transform says otherwise;
- avoid lossy round trips;
- treat validation success as shape/profile evidence, not claim truth or release approval.

### 10.2 CatalogMatrix unresolved drift

Current evidence shows:

1. [`contracts/data/catalog_matrix.md`](../../../contracts/data/catalog_matrix.md) exists as semantic authority.
2. [`schemas/contracts/v1/data/catalog_matrix.schema.json`](../../../schemas/contracts/v1/data/catalog_matrix.schema.json) exists as a permissive placeholder.
3. The schema declares `tools/validators/data/validate_catalog_matrix.py`.
4. That exact validator path was not found.
5. [`tools/validators/validate_catalog_matrix.py`](../../../tools/validators/validate_catalog_matrix.py) exists but is a `NotImplementedError` stub.
6. [ADR-0011](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) and [ADR-0022](../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) are proposed and express different placement/closure emphases.

This source root must not resolve that conflict through code convention.

Until authority is reconciled:

- do not create a duplicate CatalogMatrix schema in the package;
- do not hard-code a canonical instance home;
- do not claim a working validator;
- do not present the placeholder schema as complete;
- do not name a package helper `validate_catalog_matrix` in a way that implies canonical enforcement without a clear adapter boundary;
- mark CatalogMatrix builders/adapters **PROPOSED / CONFLICTED / NEEDS VERIFICATION**;
- require an accepted ADR or documented migration decision before making authority-bearing assumptions.

[Back to top](#top)

---

## 11. Determinism, identity, and temporal handling

### 11.1 Determinism

Where practical, the same inputs, profile versions, configuration, and injected time values should yield the same:

- field mapping;
- ordering;
- identifier;
- serialized representation;
- digest;
- validation result;
- warning set.

Determinism must be bounded to a named algorithm and version. Do not claim generic reproducibility without specifying:

```text
input normalization rule
profile/schema versions
serialization algorithm
ordering rules
numeric precision
time handling
digest algorithm
dependency versions
```

### 11.2 Identity

Helpers may compute identifiers only under a declared identity rule.

They must not:

- replace upstream source identifiers;
- conflate display labels with stable IDs;
- strip namespace or version context;
- regenerate IDs on every run without reason;
- treat a digest as proof of truth;
- equate equal metadata with equal real-world entities.

### 11.3 Digests and canonicalization

A digest helper must declare:

- algorithm, normally SHA-256 where KFM policy chooses it;
- canonicalization/serialization rule;
- included and excluded fields;
- handling of timestamps and volatile fields;
- input encoding;
- error behavior;
- test vectors.

Do not invent a JCS, RDF canonicalization, or KFM namespace decision inside package code while those choices remain unsettled.

### 11.4 Time-kind preservation

Catalog helpers must keep materially different times distinct, including where applicable:

- source time;
- valid time;
- observed time;
- retrieval time;
- processing time;
- catalog emission time;
- release time;
- correction/supersession time.

A helper must not rewrite old observations to appear current, copy retrieval time into valid time, or use the local clock as a substitute for source-supported time.

[Back to top](#top)

---

## 12. Dependency and integration boundaries

### 12.1 Current dependency posture

The inspected `pyproject.toml` declares no dependencies or build backend. Therefore no library dependency is currently authoritative for this package.

Potential future dependencies—such as `pystac`, RDF/JSON-LD libraries, JSON Schema libraries, or canonicalization packages—remain **PROPOSED** and require:

- a documented need;
- current version/security/license verification;
- deterministic and offline-test posture;
- dependency ownership;
- lock/update policy;
- failure and fallback behavior;
- no-network tests;
- compatibility and removal plan.

### 12.2 Inbound consumers

Potential callers may include:

- `pipelines/catalog/`;
- domain catalog pipelines;
- repository tools;
- governed API projection code;
- tests and fixture generators.

Actual consuming imports are **UNKNOWN** and must be verified before declaring an API stable.

### 12.3 Outbound dependencies

Package source may depend on:

- Python standard library;
- accepted third-party packages;
- generated types from canonical schemas;
- narrow internal package interfaces.

It must not directly depend on:

- lifecycle filesystem layout as an implicit API;
- production databases or object stores;
- source-specific connector implementations;
- public UI frameworks;
- model runtimes;
- release credentials;
- mutable global policy state.

### 12.4 Dependency direction

```text
contracts / schemas / standards / policy outputs
        constrain
packages/catalog source
        supports
pipelines / tools / governed callers
        own
I/O, receipts, policy enforcement, release, publication
```

[Back to top](#top)

---

## 13. Validation and test strategy

### 13.1 Current test posture

No `tests/packages/catalog/README.md` or `fixtures/packages/catalog/README.md` was found at the expected paths. The package initializer is empty and no catalog helper implementation is established.

Therefore:

```text
package unit tests       = NOT OBSERVED
package fixtures         = NOT OBSERVED
coverage                 = UNKNOWN
package CI               = NOT OBSERVED
installation test        = NOT RUN
import smoke test         = NOT RUN
```

### 13.2 Required future test families

```text
tests/packages/catalog/
├── test_import_is_side_effect_free.py
├── test_public_exports.py
├── test_no_hidden_lifecycle_io.py
├── test_no_network_calls.py
├── test_stac_mapping.py
├── test_dcat_mapping.py
├── test_prov_predicate_preservation.py
├── test_reference_preservation.py
├── test_catalog_metadata_not_evidence.py
├── test_catalog_metadata_not_release.py
├── test_deterministic_serialization.py
├── test_digest_vectors.py
├── test_time_kind_preservation.py
├── test_safe_errors.py
└── test_compatibility_adapters.py
```

This tree is **PROPOSED**.

### 13.3 Fixture expectations

Future fixtures should include:

- minimal valid STAC/DCAT/PROV-shaped inputs;
- unknown extension preservation;
- missing evidence/source/release refs;
- mismatched digest/identifier/release refs;
- sensitive geometry and restricted metadata;
- invalid time combinations;
- non-deterministic ordering traps;
- unsupported profile versions;
- correction/supersession cases;
- catalog-as-proof and catalog-as-release anti-patterns;
- no-network and no-filesystem assertions.

Fixtures must remain synthetic, deterministic, public-safe, and clearly non-authoritative.

### 13.4 Validation layers

| Validation layer | What it proves | What it does not prove |
|---|---|---|
| Import smoke test | Package imports without immediate failure or side effects. | Semantic correctness or safe publication. |
| Unit tests | Helper behavior under known inputs. | Pipeline integration, policy correctness, or release readiness. |
| Schema/profile tests | Output conforms to selected machine/profile shape. | Evidence closure or truth. |
| Determinism tests | Same declared inputs produce same declared output. | Input authority or factual correctness. |
| Integration tests | Caller/package boundary behaves as designed. | Production deployment or complete governance. |
| Policy/release tests | Governed caller blocks unsafe promotion/exposure. | Package authority—the package still does not decide release. |

### 13.5 Proposed commands

Once implementation and test homes exist:

```bash
python -m compileall packages/catalog/src
python -m pytest -q tests/packages/catalog
```

These commands were **NOT RUN** for this documentation-only update and may require package/test configuration before they work.

[Back to top](#top)

---

## 14. Security, rights, sensitivity, and public safety

Package helpers must fail safely when inputs are incomplete or unsafe.

### 14.1 Prohibited leakage

Errors, logs, reprs, fixtures, and serialized candidates must not expose:

- secrets or credentials;
- raw prompts or chain-of-thought;
- private filesystem paths;
- database DSNs;
- source access tokens;
- restricted exact locations;
- living-person sensitive data;
- DNA/genomic details;
- archaeology site locations;
- rare-species or rare-plant exact occurrences;
- critical-infrastructure details;
- embargoed or rights-restricted metadata.

### 14.2 Rights and sensitivity preservation

Helpers may carry or validate rights/sensitivity fields. They must not:

- downgrade classifications;
- replace unknown rights with permissive defaults;
- remove obligations;
- infer consent;
- generalize geometry without a transform/receipt contract;
- treat redacted metadata as if it were the canonical unredacted record;
- expose restricted fields through debug strings or validation errors.

### 14.3 Public-safe posture

A catalog-shaped value is not public merely because:

- it validates;
- it has a URL;
- it is stored under `data/catalog/`;
- it has a STAC or DCAT record;
- it includes a release ref;
- it was produced by a package test.

Public exposure still requires governed evidence, policy, review, release, correction, and rollback posture through the appropriate interface.

[Back to top](#top)

---

## 15. Implementation admission sequence

Use the smallest reversible sequence.

### Stage 0 — reconcile authority

- resolve or formally track CatalogMatrix contract/schema/validator drift;
- identify accepted profile and namespace decisions;
- confirm ownership;
- identify consuming caller and thin-slice use case.

### Stage 1 — make packaging explicit

- add a build backend;
- configure `src` package discovery;
- declare supported Python version;
- define runtime and test dependencies;
- document installation and licensing;
- add package ownership.

### Stage 2 — define the first public API

- choose one narrow helper family;
- define inputs, outputs, errors, determinism, and side effects;
- document public exports;
- avoid broad framework or registry design.

### Stage 3 — add one pure implementation slice

Recommended first slice:

```text
already-governed metadata mapping
  -> one catalog candidate shape
  -> deterministic serialization
  -> no filesystem/network writes
```

### Stage 4 — add tests and fixtures

- import-safety test;
- positive/negative unit tests;
- deterministic test vectors;
- no-network/no-filesystem tests;
- reference-preservation tests;
- sensitive-field negative tests.

### Stage 5 — integrate through an authorized caller

- pipeline/tool owns I/O;
- caller emits receipts;
- policy/release gates remain external;
- integration test proves package does not bypass lifecycle.

### Stage 6 — wire CI and documentation

- dedicated package checks;
- dependency/security scanning;
- consuming import tests;
- update package/source/module READMEs;
- record rollback and compatibility policy.

No stage may collapse catalog metadata into proof or publication authority.

[Back to top](#top)

---

## 16. Generated code, compatibility, and migrations

### 16.1 Generated code

Generated source is allowed only when:

- canonical input schemas/profiles are identified;
- generator name and version are pinned;
- input hashes and generation command are recorded;
- output is reproducible;
- generated files are clearly marked;
- hand edits are prohibited or controlled;
- CI detects drift;
- rollback regenerates from the prior input/tool version.

A proposed generated-code home under `src/catalog/generated/` remains **NEEDS VERIFICATION**.

### 16.2 Compatibility adapters

A compatibility adapter must state:

- old shape/version;
- new shape/version;
- lossless/lossy behavior;
- preserved and dropped fields;
- warning or failure conditions;
- removal milestone;
- tests;
- rollback path.

Do not normalize incompatible shapes silently.

### 16.3 Migrations

Breaking catalog-profile changes should include:

- accepted decision record where authority changes;
- schema/profile version update;
- migration or adapter;
- fixture updates;
- consuming caller updates;
- catalog candidate recompile plan;
- correction/supersession handling for released records;
- rollback target.

Source-code migration is not publication migration. Released catalog records require their own governed correction and release process.

[Back to top](#top)

---

## 17. Correction and rollback

### 17.1 Documentation rollback

This README update is reversible by reverting its commit or closing the review branch without merge.

### 17.2 Future code rollback

Every trust-bearing code change should identify:

- prior package version or commit;
- affected public exports;
- affected profile/schema versions;
- consuming callers;
- generated outputs requiring recompile;
- release/catalog records requiring correction or supersession;
- dependency downgrade constraints;
- rollback validation.

### 17.3 Rollback triggers

Rollback or hold promotion when a package change:

- introduces hidden I/O;
- causes imports to perform work;
- changes identifiers or digests unexpectedly;
- drops evidence, policy, release, or correction refs;
- renames PROV predicates or forks standards;
- exposes sensitive/restricted fields;
- turns schema success into release approval;
- writes lifecycle records without an authorized caller and receipt;
- creates parallel schema, contract, policy, proof, receipt, or release authority;
- changes output nondeterministically without an explicit accepted reason.

[Back to top](#top)

---

## 18. Definition of done

### 18.1 README v0.2

This README is complete for the present documentation task when it:

- preserves `packages/` as the shared-library responsibility root;
- identifies `src/` as a Python source container and `src/catalog/` as the import package;
- records the current greenfield `pyproject.toml` and empty initializer;
- distinguishes scaffold presence from implemented helpers;
- preserves pipeline, lifecycle, evidence, policy, release, and public-interface boundaries;
- documents import safety and no-hidden-I/O rules;
- surfaces CatalogMatrix authority drift without resolving it by convention;
- defines deterministic, temporal, security, test, compatibility, and rollback expectations;
- labels unknown implementation maturity honestly.

### 18.2 Future source-root maturity

The source root is implementation-ready only when:

- package build/discovery is configured;
- ownership is assigned;
- one narrow public API is documented;
- implemented modules exist;
- imports are side-effect free;
- dependencies are reviewed and pinned appropriately;
- tests and fixtures exist;
- no-network and no-hidden-I/O behavior is proven;
- deterministic behavior is tested;
- consuming integration is verified;
- CI is wired and observed;
- authority conflicts are resolved or explicitly gated;
- correction and rollback paths are documented.

[Back to top](#top)

---

## 19. Open verification register

| ID | Question | Status |
|---|---|---|
| `PKG-CATALOG-SRC-ROOT-001` | Which Python versions are supported? | UNKNOWN |
| `PKG-CATALOG-SRC-ROOT-002` | Which build backend and `src` package-discovery configuration will be used? | NEEDS VERIFICATION |
| `PKG-CATALOG-SRC-ROOT-003` | Which runtime and development dependencies are accepted? | UNKNOWN |
| `PKG-CATALOG-SRC-ROOT-004` | Which symbols will form the first stable public export surface? | UNKNOWN |
| `PKG-CATALOG-SRC-ROOT-005` | Which repository files import or will import `catalog`? | UNKNOWN |
| `PKG-CATALOG-SRC-ROOT-006` | Who owns `packages/catalog/` and should CODEOWNERS gain a specific rule? | NEEDS VERIFICATION |
| `PKG-CATALOG-SRC-ROOT-007` | Which dedicated workflow validates this package? | NOT OBSERVED |
| `PKG-CATALOG-SRC-ROOT-008` | Where should package tests and fixtures be created, and which conventions govern them? | NEEDS VERIFICATION |
| `PKG-CATALOG-SRC-ROOT-009` | Which STAC profile/version and KFM namespace are authoritative? | NEEDS VERIFICATION / ADR |
| `PKG-CATALOG-SRC-ROOT-010` | Which DCAT profile/context and version are authoritative? | NEEDS VERIFICATION |
| `PKG-CATALOG-SRC-ROOT-011` | Which PROV/PAV serialization and RDF canonicalization rules are authoritative? | NEEDS VERIFICATION / ADR |
| `PKG-CATALOG-SRC-ROOT-012` | Which canonical serialization and digest rule should shared helpers implement? | NEEDS VERIFICATION / ADR |
| `PKG-CATALOG-SRC-ROOT-013` | How will CatalogMatrix contract, schema, validator, and proposed ADR conflicts be reconciled? | CONFLICTED / ADR REQUIRED |
| `PKG-CATALOG-SRC-ROOT-014` | Is the root-level `validate_catalog_matrix.py` stub retained, moved, replaced, or superseded? | NEEDS VERIFICATION |
| `PKG-CATALOG-SRC-ROOT-015` | Should generated code live inside this package, another package, or remain absent? | NEEDS VERIFICATION |
| `PKG-CATALOG-SRC-ROOT-016` | What compatibility and deprecation policy governs catalog-profile changes? | UNKNOWN |
| `PKG-CATALOG-SRC-ROOT-017` | Which thin-slice pipeline will first consume the package? | UNKNOWN |
| `PKG-CATALOG-SRC-ROOT-018` | Which tests prove package code cannot write lifecycle or release state? | NOT OBSERVED |
| `PKG-CATALOG-SRC-ROOT-019` | Which security/license review applies to future third-party dependencies? | NEEDS VERIFICATION |
| `PKG-CATALOG-SRC-ROOT-020` | Which emitted receipts or build metadata prove generated-code and package-build reproducibility? | UNKNOWN |

[Back to top](#top)

---

## 20. Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| This target file on `main` | **CONFIRMED** | Existing v0.1 source-root boundary and target blob. | Implemented package behavior. |
| [`../pyproject.toml`](../pyproject.toml) | **CONFIRMED** | Python project name and version placeholder. | Build backend, dependencies, installability, or publishability. |
| [`catalog/__init__.py`](catalog/__init__.py) | **CONFIRMED empty file** | Import package scaffold. | Exports or implementation. |
| [`catalog/README.md`](catalog/README.md) | **CONFIRMED v0.2** | Current child-module evidence and boundaries. | Working helpers or runtime. |
| Exact check for `src/__init__.py` | **CONFIRMED absent** | `src/` is not currently a Python package. | Full recursive tree. |
| Exact checks for package tests/fixtures READMEs | **CONFIRMED absent** | Expected package test/fixture docs are missing. | No test/fixture files anywhere under all possible paths. |
| Repository search for `packages/catalog` | **CONFIRMED search result** | Indexed package surfaces and no dedicated workflow result. | Complete recursive inventory. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | **CONFIRMED doctrine** | `packages/` owns shared libraries; other responsibilities remain separate. | Current implementation maturity. |
| [`../README.md`](../README.md) | **CONFIRMED package README** | Parent catalog-package boundary. | Implemented helpers or pipeline behavior. |
| [`../../../pipelines/catalog/README.md`](../../../pipelines/catalog/README.md) | **CONFIRMED README** | Executable catalog pipeline responsibility. | Executable pipeline implementation or pass state. |
| [`../../../data/catalog/README.md`](../../../data/catalog/README.md) | **CONFIRMED README** | Catalog lifecycle and release-gated exposure. | Concrete catalog inventory or public route enforcement. |
| [`../../../contracts/data/catalog_matrix.md`](../../../contracts/data/catalog_matrix.md) | **CONFIRMED contract** | CatalogMatrix semantic meaning and schema-placeholder warning. | Complete machine shape or validator. |
| [`../../../schemas/contracts/v1/data/catalog_matrix.schema.json`](../../../schemas/contracts/v1/data/catalog_matrix.schema.json) | **CONFIRMED placeholder schema** | Current minimal shape and declared metadata. | Full CatalogMatrix semantics or release closure. |
| [`../../../tools/validators/validate_catalog_matrix.py`](../../../tools/validators/validate_catalog_matrix.py) | **CONFIRMED stub** | Current root-level file exists but is not implemented. | Working validation. |
| [ADR-0011](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | **CONFIRMED proposed ADR** | Proposed artifact-family separation. | Accepted authority. |
| [ADR-0022](../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | **CONFIRMED proposed ADR** | Proposed STAC/DCAT/PROV agreement rule. | Accepted placement or working enforcement. |
| [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) | **CONFIRMED** | Repository-wide default ownership and no catalog-package-specific rule. | Actual team availability or review completion. |

[Back to top](#top)

---

## 21. Maintainer checklist

Before adding or changing source under `packages/catalog/src/`:

- [ ] Confirm the file belongs in reusable package source rather than `pipelines/`, `tools/`, `connectors/`, `contracts/`, `schemas/`, `policy/`, `data/`, `release/`, or an app.
- [ ] Confirm the relevant contract, schema, standard/profile, and policy posture.
- [ ] Keep imports side-effect free.
- [ ] Keep network, filesystem, database, and environment access explicit and dependency-injected.
- [ ] Do not write lifecycle or release state from pure helpers.
- [ ] Preserve source, evidence, receipt, policy, review, release, correction, and rollback refs.
- [ ] Preserve unknown valid extension fields when round-tripping.
- [ ] Do not rename standard predicates or fork STAC/DCAT/PROV semantics.
- [ ] Define deterministic ordering, serialization, identity, time, and digest behavior.
- [ ] Inject clock/randomness where needed.
- [ ] Avoid sensitive values in errors, logs, reprs, fixtures, and snapshots.
- [ ] Add positive, negative, no-network, no-hidden-I/O, determinism, and sensitive-leak tests.
- [ ] Document public exports and compatibility posture.
- [ ] Record generator provenance for generated code.
- [ ] Update this README, the child module README, and the parent package README when the boundary changes.
- [ ] Identify rollback triggers and prior compatible version.
- [ ] Do not claim implementation, CI, deployment, release, or public availability without current evidence.

---

## Maintainer note

Keep `packages/catalog/src/` boring, import-safe, deterministic, and subordinate to the trust membrane. A good shared package makes governed catalog work easier without acquiring the authority to ingest sources, move lifecycle state, create evidence, decide policy, approve release, or publish claims.
