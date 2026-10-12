<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-catalog-src-readme
title: packages/catalog/src/ — Catalog Package Python Source Boundary
type: readme; package-source-root; python-src-layout; shared-catalog-library-boundary; catalog-matrix-readiness
version: v0.3
status: draft; repository-grounded; source-container-confirmed; scaffold-only; empty-import-package; no-build-backend; no-dependencies; no-package-tests; validator-conflicted; non-authoritative
owners: "NEEDS VERIFICATION — CODEOWNERS routes /packages/ to @bartytime4life; no accepted catalog package owner, catalog steward, compatibility owner, or independent reviewer assignment was verified"
created: 2026-06-13
updated: 2026-07-23
supersedes: v0.2 documentation at the same path; no source code, package metadata, contract, schema, validator, pipeline, lifecycle record, release object, runtime behavior, or public behavior is superseded
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: "public-doc; packages; catalog; python-src-layout; shared-library; scaffold-only; no-truth-authority; no-schema-authority; no-contract-authority; no-policy-authority; no-evidence-authority; no-lifecycle-authority; no-release-authority; governed-interface-only; catalog-carrier-not-proof; deterministic; correction-aware; rollback-aware"
current_path: packages/catalog/src/README.md
owning_root: packages/
parent_package: packages/catalog/
import_package: packages/catalog/src/catalog/
responsibility: define the Python source-container boundary for reusable, non-deployable catalog helpers that operate on already-governed in-memory values without acquiring source, evidence, policy, lifecycle, release, persistence, serving, or publication authority
truth_posture: >
  CONFIRMED target README and prior blob; Directory Rules v1.4 packages placement and
  mandatory README contract; packages root v0.3 shared-library boundary; parent catalog
  README v0.1; pyproject name kfm-catalog and version 0.0.0; src/catalog child README v0.2;
  empty catalog/__init__.py; exact absence at checked paths of stac.py, dcat.py, prov.py,
  tests/packages/catalog/README.md, and fixtures/packages/catalog/README.md; CatalogMatrix
  semantic contract v0.2; paired permissive PROPOSED schema; root-level validator stub;
  ADR-0011 v1.2 proposed separation posture; ADR-0022 v1.1 proposed STAC/DCAT/PROV
  agreement posture; and CODEOWNERS /packages review route / PROPOSED future package
  build configuration, public exports, pure mapping helpers, deterministic serialization,
  validation adapters, generated types, package tests, fixtures, consumer integration, and
  distribution / CONFLICTED CatalogMatrix semantic contract and current schema/validator
  maturity; schema-declared validator path versus root-level stub; ADR-0011 versus ADR-0022
  placement and closure details; parent catalog README v0.1 versus current packages-root
  admission and maturity contract / UNKNOWN complete recursive tree, all imports and consumers,
  package discovery, dependency graph, supported Python versions, package installation, CI,
  runtime behavior, release integration, deployment use, and public effects / NEEDS VERIFICATION
  accepted owners, package admission, standards profiles, namespace and canonicalization rules,
  test and fixture homes, dependency direction, compatibility windows, correction propagation,
  and rollback drill
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: a1570d5bb316d2a55edc95ff3f51413118ddb5ee
  prior_blob: e548a2b78b2e61d585fbf14a61729b8cfa08810b
  packages_root_blob: 154e1c9a8b841397bceb52e6b4933b241906ab9a
  parent_catalog_readme_blob: ac16ca299120d7b03b4c24915e969f6f5610f4ae
  catalog_pyproject_blob: 13e0f5b7763a7ed193955e87a03910a924fde90f
  child_catalog_readme_blob: 14d0462d9dfa0d594df33e9a8da6cc7bc1f8ebf0
  catalog_init_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  catalog_matrix_contract_blob: c67923beb505aa39e7c0c768c16e75a00826ff31
  catalog_matrix_schema_blob: 75a927376066226d8a0f89a630d7bb3693143c41
  catalog_matrix_validator_blob: 91ecf78675cf19672a0e94a3899df3074c36ddc4
  adr_0011_blob: 40b0f47b87d584040803ed76aa6b31f5204b7fca
  adr_0022_blob: b09c1d7aaa39f3030afdcec419c58236fd324f17
  bounded_source_search: "packages/catalog/src catalog_matrix kfm-catalog returned the source-root and child-module READMEs"
  checked_absent_paths:
    - packages/catalog/src/catalog/stac.py
    - packages/catalog/src/catalog/dcat.py
    - packages/catalog/src/catalog/prov.py
    - tests/packages/catalog/README.md
    - fixtures/packages/catalog/README.md
related:
  - ../../README.md
  - ../README.md
  - ../pyproject.toml
  - catalog/README.md
  - catalog/__init__.py
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../../docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - ../../../docs/standards/STAC.md
  - ../../../docs/standards/DCAT.md
  - ../../../docs/standards/PROV.md
  - ../../../contracts/data/catalog_matrix.md
  - ../../../schemas/contracts/v1/data/catalog_matrix.schema.json
  - ../../../tools/validators/validate_catalog_matrix.py
  - ../../../tools/validators/catalog/README.md
  - ../../../pipelines/catalog/README.md
  - ../../../data/catalog/README.md
  - ../../../data/proofs/README.md
  - ../../../data/receipts/README.md
  - ../../../release/README.md
  - ../../../tests/README.md
  - ../../../fixtures/README.md
  - ../../../.github/CODEOWNERS
tags: [kfm, packages, catalog, src-layout, python, scaffold, shared-library, stac, dcat, prov, catalog-matrix, deterministic-serialization, evidence, policy, release, correction, rollback]
notes:
  - "v0.3 is a same-path, repository-grounded documentation modernization; it changes no implementation or authority surface."
  - "The first twelve H2 sections follow Directory Rules section 15 in the required order."
  - "The source root remains scaffold-only: pyproject metadata is minimal, catalog/__init__.py is empty, and checked STAC/DCAT/PROV modules are absent."
  - "CatalogMatrix package work remains held until contract, schema, validator, ADR, fixture, policy, and release-closure expectations are reconciled."
  - "The prior v0.2 content remains recoverable through Git history and the recorded prior blob."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="packages-catalog-src"></a>

# `packages/catalog/src/` — Catalog Package Python Source Boundary

> **One-line purpose.** Define the Python `src`-layout container for reusable, non-deployable catalog-support code while keeping catalog execution, lifecycle records, evidence closure, policy, release, correction, rollback, serving, and publication in their governing responsibility roots.

<p>
  <a href="#status"><img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square"></a>
  <a href="#authority-level"><img alt="Authority: shared source container" src="https://img.shields.io/badge/authority-shared%20source%20container-1f6feb?style=flat-square"></a>
  <a href="#current-bounded-repository-inventory"><img alt="Implementation: scaffold only" src="https://img.shields.io/badge/implementation-scaffold%20only-6e7781?style=flat-square"></a>
  <a href="#current-bounded-repository-inventory"><img alt="Import package initializer: empty" src="https://img.shields.io/badge/catalog%2F__init__-empty-6e7781?style=flat-square"></a>
  <a href="#catalogmatrix-alignment-and-implementation-hold"><img alt="CatalogMatrix alignment: hold" src="https://img.shields.io/badge/CatalogMatrix-alignment%20hold-b42318?style=flat-square"></a>
  <a href="#dependency-side-effect-and-public-path-rules"><img alt="Imports: side-effect free" src="https://img.shields.io/badge/imports-side--effect%20free-2da44e?style=flat-square"></a>
  <a href="#authority-level"><img alt="Catalog records: carriers not truth" src="https://img.shields.io/badge/catalog-carrier%20not%20truth-8250df?style=flat-square"></a>
</p>

> [!IMPORTANT]
> **`packages/catalog/src/` is a source container, not an implemented catalog library.** Current evidence confirms a minimal `kfm-catalog` `0.0.0` project declaration, one `catalog/` import-package directory, and an empty `catalog/__init__.py`. It does not confirm a build backend, package discovery, dependencies, exports, helper modules, tests, fixtures, consumers, distribution, or runtime behavior.

> [!CAUTION]
> **Catalog metadata is a carrier, not sovereign truth.** A STAC Item, DCAT Dataset, PROV record, CatalogMatrix, successful schema check, digest, package import, or green test does not establish evidence closure, rights clearance, policy approval, release readiness, public safety, or KFM publication.

> [!WARNING]
> **CatalogMatrix implementation is held.** The semantic contract is materially richer than the permissive placeholder schema; the schema names a validator path that is absent; the existing root-level validator is a `NotImplementedError` stub; and ADR-0011 and ADR-0022 remain proposed. Do not generate package models or release-grade catalog closure from this surface until those authorities and enforcement paths are reconciled.

**Quick navigation**

| Required source-root contract | Current evidence | Design and change control |
|---|---|---|
| [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) | [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) | [Context](#bounded-context-and-ubiquitous-language) · [Inventory](#current-bounded-repository-inventory) · [Imports](#import-and-export-contract) · [Standards](#standards-profile-and-namespace-boundary) · [CatalogMatrix](#catalogmatrix-alignment-and-implementation-hold) · [Maturity](#package-admission-and-maturity) · [Security](#security-rights-sensitivity-and-public-safety) · [Rollback](#compatibility-correction-and-rollback) · [Open work](#open-verification-register) |

---

## Purpose

`packages/catalog/src/` is the Python source container for the shared catalog-support package declared by [`packages/catalog/pyproject.toml`](../pyproject.toml).

A future admitted package may provide reusable, importable helpers for:

- constructing catalog-shaped values from already-governed in-memory inputs;
- STAC, DCAT, PROV-O, and PAV profile mapping;
- preserving source, evidence, receipt, policy, review, release, correction, and rollback references;
- deterministic ordering, serialization, identifiers, and digests under accepted rules;
- schema/profile validation adapters and safe validation-result models;
- compatibility adapters for explicitly versioned catalog-profile migrations;
- deterministic, no-network fixture builders that cannot be mistaken for production catalog records.

This source root remains **non-deployable and non-publishing**. Executable orchestration, authorized reads and writes, receipts, policy evaluation, release decisions, correction, rollback, and public serving belong to their owning roots.

```text
packages/catalog/              = shared package boundary and project metadata
packages/catalog/src/          = Python source container
packages/catalog/src/catalog/  = import package scaffold
pipelines/catalog/             = executable catalog orchestration
tools/validators/              = repository-wide validator entry points
data/catalog/                  = catalog-stage lifecycle records
data/proofs/                   = evidence and proof support
data/receipts/                 = process receipts
contracts/                     = semantic meaning
schemas/                       = machine-checkable shape
policy/                        = admissibility and obligations
release/                       = release, correction, withdrawal, rollback
apps/governed-api/             = normal dynamic public trust membrane
```

This README defines a source boundary. It does not admit a dependency, configure packaging, create a public API, accept an ADR, validate a release, or publish a claim or artifact.

[Back to top](#top)

---

## Authority level

**Implementation-bearing source-container sublane under the canonical `packages/` root; non-authoritative for source identity, truth, object meaning, machine shape, evidence closure, policy, lifecycle state, release, deployment, serving, and publication.**

| Question | Source-root answer | Evidence posture |
|---|---|---:|
| Why `packages/catalog/src/`? | Its primary responsibility is reusable Python implementation code inside a shared package. | **CONFIRMED** placement and scaffold |
| Is `src/` the import package? | No. `src/` is the container; `src/catalog/` is the current import-package directory. | **CONFIRMED** layout |
| Is this an executable catalog pipeline? | No. Lifecycle orchestration belongs to `pipelines/catalog/` or a verified domain pipeline. | **CONFIRMED** responsibility split |
| May this source define catalog semantics? | No. It consumes semantic contracts from `contracts/`. | **CONFIRMED** authority split |
| May it define canonical schemas? | No. Generated or hand-written models remain subordinate to `schemas/contracts/v1/`. | **CONFIRMED** authority split |
| May it decide policy, evidence closure, or release? | No. It may preserve explicit results and references only. | **CONFIRMED** trust posture |
| May it write lifecycle or release state? | Not as an import or hidden helper side effect. An authorized caller owns I/O, receipts, policy, and release handling. | **CONFIRMED** lifecycle boundary |
| Does package distribution publish KFM knowledge? | No. A wheel, sdist, workspace package, or registry artifact is software distribution, not KFM lifecycle promotion. | **CONFIRMED** packages-root boundary |

### Anti-collapse rule

```text
source container        != import package authority
Python package          != catalog pipeline
catalog helper          != catalog lifecycle writer
catalog candidate       != EvidenceBundle
CatalogMatrix           != proof of its own closure
STAC Item               != release approval
DCAT Dataset            != source truth
PROV fragment           != complete provenance proof
schema success          != policy allow
package build           != KFM publication
```

[Back to top](#top)

---

## Status

### Current bounded repository state

| Surface | Current evidence | Status | Consequence |
|---|---|---:|---|
| This README | Existing v0.2 file read from `main`; blob recorded above. | **CONFIRMED** | Same-path modernization target. |
| Parent [`packages/README.md`](../../README.md) | v0.3 package-root admission, maturity, dependency, compatibility, and distribution contract. | **CONFIRMED** | This source root must follow the current packages-root contract. |
| Parent [`packages/catalog/README.md`](../README.md) | v0.1 catalog-package boundary, older than the current packages-root modernization. | **CONFIRMED / STALE** | Preserve its shared-library boundary; do not treat its proposed tree or ownership as current implementation proof. |
| [`packages/catalog/pyproject.toml`](../pyproject.toml) | Greenfield comment, `[project]`, `name = "kfm-catalog"`, `version = "0.0.0"`. | **CONFIRMED placeholder** | Python intent is visible; build/install/distribution maturity is not. |
| Build metadata | No `[build-system]`, supported Python declaration, dependencies, optional dependencies, package discovery, entry points, or tool configuration. | **CONFIRMED absent from file** | Do not call this an installable package. |
| [`catalog/README.md`](catalog/README.md) | v0.2 child-module boundary and scaffold inventory. | **CONFIRMED** | Child and source-root rules must remain consistent. |
| [`catalog/__init__.py`](catalog/__init__.py) | Empty file. | **CONFIRMED scaffold** | No exports, version, registry, or import-time behavior is established. |
| `catalog/stac.py` | Exact path absent. | **CONFIRMED absent at checked path** | STAC helper implementation is not established. |
| `catalog/dcat.py` | Exact path absent. | **CONFIRMED absent at checked path** | DCAT helper implementation is not established. |
| `catalog/prov.py` | Exact path absent. | **CONFIRMED absent at checked path** | PROV/PAV helper implementation is not established. |
| Bounded source search | Returned this README and the child-module README. | **CONFIRMED search result / incomplete tree proof** | A complete recursive tree still requires local or Git-tree inspection. |
| `tests/packages/catalog/README.md` | Exact path absent. | **CONFIRMED absent at checked path** | No package-test lane is documented there. |
| `fixtures/packages/catalog/README.md` | Exact path absent. | **CONFIRMED absent at checked path** | No package-fixture lane is documented there. |
| [`CatalogMatrix` contract](../../../contracts/data/catalog_matrix.md) | v0.2 semantic contract with a broad governed relationship model. | **CONFIRMED contract / draft** | Package code must not narrow semantics to the current schema stub. |
| [CatalogMatrix schema](../../../schemas/contracts/v1/data/catalog_matrix.schema.json) | `PROPOSED`; requires only `id`; permits additional properties. | **CONFIRMED placeholder schema** | Shape validity is weak and does not prove closure. |
| [Root-level validator](../../../tools/validators/validate_catalog_matrix.py) | Raises `NotImplementedError("Greenfield placeholder")`. | **CONFIRMED stub** | A working CatalogMatrix validator is not established. |
| Schema-declared validator | `tools/validators/data/validate_catalog_matrix.py` absent at the checked path. | **CONFIRMED path mismatch** | Contract/schema/validator wiring remains unresolved. |
| CODEOWNERS | `/packages/` routes to `@bartytime4life`. | **CONFIRMED review route** | Stewardship, independent review, and approval remain unverified. |

### Evidence boundary

```text
Python project placeholder         = CONFIRMED
Python src-layout intent            = CONFIRMED
import package directory            = CONFIRMED
empty initializer                   = CONFIRMED
implemented catalog helpers         = NOT OBSERVED
public exports                      = NOT ESTABLISHED
build backend / discovery           = NOT DECLARED
runtime / test dependencies         = NOT DECLARED
package tests / fixtures            = NOT OBSERVED at checked homes
working CatalogMatrix validator     = NOT ESTABLISHED
consuming imports                   = UNKNOWN
installation / build / distribution = NOT RUN / UNKNOWN
catalog lifecycle write behavior    = UNKNOWN
runtime and public effects          = UNKNOWN
```

> [!NOTE]
> Exact-path absence and indexed search are bounded evidence, not a categorical claim about every branch, generated file, or unindexed path.

[Back to top](#top)

---

## What belongs here

Appropriate source includes reusable implementation code that is import-safe, independently testable, and subordinate to governing contracts and schemas:

- internal Python package organization under `src/catalog/`;
- narrow public exports with explicit compatibility promises;
- pure STAC/DCAT/PROV/PAV mapping helpers;
- profile dispatch using explicit profile identity and version;
- reference-preservation helpers for source, evidence, receipt, policy, review, release, correction, and rollback IDs;
- deterministic serialization and digest helpers under accepted algorithms and canonicalization rules;
- validation adapters that call or normalize canonical validators without becoming validator authority;
- structured, public-safe error and warning types;
- compatibility adapters with explicit semantic-loss, retirement, and rollback behavior;
- generated models only when canonical inputs, generator identity, reproducibility, and drift checks are established.

A placement test:

> If the code transforms already-governed in-memory values into catalog-shaped values or validation results, can be reused by more than one verified caller, and does not own I/O, lifecycle transitions, policy, evidence closure, release, or serving, it may belong here.

[Back to top](#top)

---

## What does not belong here

| Do not place here | Correct home or posture |
|---|---|
| Source acquisition or source-specific clients | `connectors/` |
| Catalog pipeline runners and lifecycle orchestration | [`pipelines/catalog/`](../../../pipelines/catalog/README.md) or a verified domain pipeline |
| Declarative pipeline configuration | `pipeline_specs/` |
| Repository-wide validator or generator commands | `tools/` |
| One-off operational scripts | `scripts/` |
| Catalog-stage records | [`data/catalog/`](../../../data/catalog/README.md) |
| Graph/triplet records | Governed triplet/graph lifecycle home |
| EvidenceBundles, ProofPacks, or proof-side closure | [`data/proofs/`](../../../data/proofs/README.md) |
| Run, transform, or catalog-build receipts | [`data/receipts/`](../../../data/receipts/README.md) |
| Source descriptors and rights metadata | `data/registry/` plus source and policy homes |
| Semantic contracts | `contracts/` |
| Canonical schemas | `schemas/contracts/v1/` |
| Policy rules or authoritative decisions | `policy/` |
| Release manifests, promotion decisions, corrections, withdrawals, or rollback decisions | [`release/`](../../../release/README.md) |
| Public API routes or catalog server | `apps/governed-api/` or an accepted deployable app |
| UI rendering | `apps/explorer-web/` or a verified UI package |
| Package test instances | Canonical `tests/` lane after the home is verified |
| Package fixture instances | Canonical `fixtures/` lane after the home is verified |
| Secrets, credentials, raw prompts, private reasoning, protected locations, or restricted source content | Never commit; use approved controls |
| Generated or mock catalog values represented as truth | Forbidden |
| Parallel catalog schema, contract, policy, proof, receipt, or release authority | Requires accepted ADR or migration; default is **DENY** |

[Back to top](#top)

---

## Inputs

This source may consume only explicit, versioned, reviewable inputs.

| Input family | Authority source | Package posture |
|---|---|---|
| Catalog semantics | Accepted contracts under `contracts/` | Consume meaning; do not redefine it locally. |
| Machine shape | Canonical schemas and accepted standards profiles | Generate or validate subordinate models against pinned identities. |
| STAC/DCAT/PROV/PAV profiles | Accepted standards docs, contexts, schemas, and namespace decisions | Require explicit profile/version; do not silently change defaults. |
| Catalog source values | Already-governed normalized metadata or typed domain projections | Validate declared preconditions; do not acquire sources. |
| References | Source, evidence, receipt, policy, review, release, correction, rollback refs | Preserve exactly; do not invent, authorize, or silently resolve. |
| Artifact metadata | Media type, role, size, digest, spatial/temporal extent | Accept from authorized callers or verified derivation. |
| Validation context | Schema/profile ref, options, known extension policy | Keep explicit and deterministic. |
| Clock or randomness | Injected time or deterministic ID source where required | Never hide ambient nondeterminism. |
| Generated-code inputs | Canonical source digest, generator version, command, and configuration | Require reproducible generation and drift checks. |

### Input rules

- Do not accept caller-created evidence closure, policy approval, release approval, correction state, or public-safety claims as authoritative.
- Do not accept internal filesystem paths, raw object-store handles, model endpoints, database credentials, or canonical-store locators as public references.
- Preserve unknown valid extension fields under an accepted round-trip policy.
- Preserve distinct identities and time kinds.
- Reject or explicitly surface unsupported profile versions and incompatible shapes.
- Keep secret and restricted material outside package fixtures and generated code.

[Back to top](#top)

---

## Outputs

Permitted outputs are implementation values, not authoritative lifecycle or release records.

| Output | Required posture |
|---|---|
| In-memory catalog candidate | Clearly not public or released; includes limitations and unresolved refs. |
| Typed or dictionary representation | Preserves standard and KFM extension semantics. |
| Deterministic serialized bytes or text | Bound to named profile, ordering, canonicalization, and encoding rules. |
| Digest or identifier | Bound to named algorithm and declared input surface; not proof of truth. |
| Validation-result value | Structured, safe, and subordinate to the canonical validator/policy flow. |
| Reference/display model | Preserves opaque IDs, versions, digests, and obligations. |
| Safe error or warning | Redacted, non-secret, and free of restricted payloads or internal paths. |
| Compatibility result | Reports versions, semantic loss, warnings, deprecation, and retirement state. |
| Generated model | Traceable to canonical input digest, generator version, command, and drift check. |
| Synthetic test builder output | Deterministic, no-network, public-safe, and visibly non-authoritative. |

Package output must not:

- write lifecycle or release state as a hidden effect;
- fabricate source, evidence, policy, release, correction, or rollback references;
- turn `ABSTAIN`, `DENY`, unresolved, restricted, or stale state into apparent success;
- silently drop standard predicates, KFM extension fields, rights, sensitivity, or obligations;
- expose stack traces, secrets, private paths, prompts, adapter internals, or blocked content;
- label a parse, schema pass, build, digest match, or test as evidence closure or release approval.

[Back to top](#top)

---

## Validation

### Confirmed current validation surfaces

| Check | Repository command or path | What it supports | Current source-root relevance |
|---|---|---|---|
| CatalogMatrix semantic contract | [`contracts/data/catalog_matrix.md`](../../../contracts/data/catalog_matrix.md) | Object meaning and invariants. | Meaning authority; draft. |
| CatalogMatrix schema | [`schemas/contracts/v1/data/catalog_matrix.schema.json`](../../../schemas/contracts/v1/data/catalog_matrix.schema.json) | Minimal placeholder shape. | Insufficient for package generation or closure proof. |
| Root-level CatalogMatrix validator | [`tools/validators/validate_catalog_matrix.py`](../../../tools/validators/validate_catalog_matrix.py) | File presence only. | Raises `NotImplementedError`; not working validation. |
| Catalog validator lane README | [`tools/validators/catalog/README.md`](../../../tools/validators/catalog/README.md) | Proposed validator responsibility. | Does not prove executables. |
| Parent package metadata | [`packages/catalog/pyproject.toml`](../pyproject.toml) | Project name/version placeholder. | Does not support build or import validation. |
| Import package initializer | [`catalog/__init__.py`](catalog/__init__.py) | Empty scaffold file. | No exports or behavior to test. |
| Package-local test lane | `tests/packages/catalog/` | Would prove package behavior. | **NOT ESTABLISHED at checked README path** |
| Package-local fixture lane | `fixtures/packages/catalog/` | Would support deterministic tests. | **NOT ESTABLISHED at checked README path** |
| Dedicated package CI | Verified workflow/command | Would prove configured checks for a revision. | **NOT OBSERVED** |

### Required first test families

Before helper code is described as usable, deterministic coverage should include:

```text
import is side-effect free
public exports are deliberate
no network, filesystem, database, environment, or model calls
no lifecycle or release writes
STAC mapping preserves standard and KFM extension fields
DCAT mapping preserves dataset/distribution semantics
PROV/PAV mapping preserves predicates and attribution/version relations
source/evidence/receipt/policy/release/correction/rollback refs round-trip
catalog metadata cannot become proof or release approval
deterministic ordering, serialization, and digest vectors
time kinds remain distinct
rights, sensitivity, redaction, generalization, and restricted fields fail safely
unknown valid extensions follow the accepted compatibility rule
unsupported profiles fail visibly
compatibility adapters round-trip or disclose semantic loss
```

### Non-vacuity rule

A passing package check proves only its declared assertion. It does not prove:

- source authority or evidence sufficiency;
- rights or policy approval;
- complete STAC/DCAT/PROV agreement;
- release readiness or publication;
- safe exposure outside tested cases;
- pipeline integration, deployment, monitoring, correction, or rollback execution.

### Documentation validation for this README

A documentation-only change should verify:

- complete-file read and no-loss mapping;
- first twelve H2 sections in Directory Rules order;
- one H1, balanced fences/HTML/alerts, and valid heading hierarchy;
- internal navigation and repository-relative links;
- evidence snapshot and truth-label consistency;
- no invented package capability, owner, test result, release, or public effect;
- exact remote diff scope and rollback target.

[Back to top](#top)

---

## Review burden

`/packages/` currently routes to `@bartytime4life` through CODEOWNERS. That is a GitHub review-request mechanism, not proof of stewardship assignment, independent review, approval, release authority, or separation of duties.

| Change class | Minimum review concern | Additional trigger |
|---|---|---|
| README clarification | Source boundary, current evidence, links, no overclaiming. | Docs/package reviewer. |
| Package build configuration | Python support, build backend, discovery, dependencies, license, distribution. | Package and supply-chain reviewer. |
| New public export | Semantics, compatibility, deterministic tests, dependency direction. | Consumer owners. |
| STAC/DCAT/PROV mapping | Standards conformance, extension preservation, namespace/profile versions. | Standards and catalog reviewers. |
| CatalogMatrix models or helpers | Contract/schema/validator/ADR alignment and release-closure boundary. | Contract, schema, validation, evidence, policy, and release reviewers. |
| Digest/canonicalization code | Algorithm, canonicalization, test vectors, compatibility, security. | Identity/hashing reviewer. |
| Validation adapter | Canonical validator ownership, safe errors, no authority duplication. | Validation and policy reviewers. |
| Generated models | Generator pin, input digest, reproducibility, drift detection, rollback. | Schema and supply-chain reviewers. |
| Sensitive-domain metadata support | Rights, consent, redaction, generalization, exact-location protections. | Applicable domain and sensitivity reviewer. |
| Compatibility adapter | Semantic loss, migration window, deprecation, retirement, correction, rollback. | All affected consumers. |

High-impact changes include any modification that can reinterpret identity, digest, time, source role, evidence, rights, sensitivity, policy, release, correction, or standard predicates—or that introduces I/O, global state, network access, or a new public path.

[Back to top](#top)

---

## Related folders

| Surface | Responsibility | Relationship to `packages/catalog/src/` |
|---|---|---|
| [`packages/`](../../README.md) | Canonical shared-library root. | Parent admission, maturity, dependency, compatibility, distribution, and rollback contract. |
| [`packages/catalog/`](../README.md) | Catalog package boundary and metadata. | Parent package; currently v0.1 and due later convergence. |
| [`packages/catalog/src/catalog/`](catalog/README.md) | Current import-package module boundary. | Child source lane; currently scaffold-only. |
| [`pipelines/catalog/`](../../../pipelines/catalog/README.md) | Executable catalog orchestration. | Owns lifecycle flow and authorized I/O. |
| [`tools/validators/`](../../../tools/validators/README.md) | Repository-wide validation tools. | Owns canonical validator entry points. |
| [`contracts/data/catalog_matrix.md`](../../../contracts/data/catalog_matrix.md) | CatalogMatrix semantic contract. | Meaning authority; richer than current schema. |
| [`schemas/contracts/v1/data/catalog_matrix.schema.json`](../../../schemas/contracts/v1/data/catalog_matrix.schema.json) | CatalogMatrix machine shape. | Current placeholder; package models must not treat it as complete. |
| [`data/catalog/`](../../../data/catalog/README.md) | Catalog-stage lifecycle records. | Package code must not write implicitly. |
| [`data/proofs/`](../../../data/proofs/README.md) | Evidence/proof support. | Catalog values may preserve refs; they are not proof. |
| [`data/receipts/`](../../../data/receipts/README.md) | Process receipts. | Authorized callers emit receipts; pure helpers do not silently write them. |
| [`release/`](../../../release/README.md) | Release, correction, withdrawal, rollback decisions. | Package output cannot approve or publish. |
| [`tests/`](../../../tests/README.md) | Enforceability proof. | Candidate home for package tests after a verified convention decision. |
| [`fixtures/`](../../../fixtures/README.md) | Deterministic valid/invalid samples. | Candidate home for package-specific fixtures; source must not hide them. |
| [`packages/hashing/`](../../hashing/README.md) | Shared hashing boundary. | Potential dependency/overlap; do not duplicate digest authority. |
| [`packages/identity/`](../../identity/README.md) | Shared identity boundary. | Potential dependency/overlap for stable IDs. |
| [`packages/temporal/`](../../temporal/README.md) | Shared temporal boundary. | Potential dependency/overlap for time-kind handling. |
| [`packages/citation/`](../../citation/README.md) | Citation and EvidenceRef helper boundary. | Potential dependency/overlap for evidence reference presentation. |
| [`packages/schema-registry/`](../../schema-registry/README.md) | Schema lookup/registry helper boundary. | Potential dependency/overlap for schema resolution. |

### Dependency-direction rule

Before adding a helper, inspect sibling package responsibilities. Do not duplicate hashing, identity, time, citation, schema resolution, evidence resolution, policy runtime, redaction, or release logic merely because a catalog projection needs it.

[Back to top](#top)

---

## ADRs

| Decision record | Current relevance | Status posture |
|---|---|---|
| [`ADR-0001 — schema home`](../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Keeps machine shape under `schemas/contracts/v1/`. | Consult current status before generated models. |
| [`ADR-0002 — contracts versus schemas`](../../../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | Separates object meaning from machine shape. | Package consumes both and owns neither. |
| [`ADR-0011 — receipts, proofs, manifests, catalog separation`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | Defines proposed cross-family authority boundaries and explicitly defers CatalogMatrix closure proof. | **PROPOSED**, repository-grounded, not accepted. |
| [`ADR-0022 — CatalogMatrix STAC + DCAT + PROV agreement`](../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | Proposes release-level cross-vocabulary agreement and closure object. | **PROPOSED**; path and implementation proposals partly stale. |
| [`ADR-0025 — public clients never read canonical/internal stores`](../../../docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md) | Governs dependency direction and public-path denial. | Package design must make bypass structurally difficult. |

### ADR and coordinated-change triggers

An accepted decision or coordinated contract/schema/policy migration is required before:

- creating a parallel catalog contract, schema, policy, validator, proof, receipt, or release home;
- declaring a canonical CatalogMatrix object family, path, closure proof, or public API;
- changing STAC/DCAT/PROV/PAV profile or namespace rules in a compatibility-breaking way;
- selecting canonical RDF/JSON-LD or JSON canonicalization that changes digests;
- moving package tests or fixtures into a competing canonical home;
- introducing a second catalog server or public path;
- collapsing CatalogMatrix, EvidenceBundle, ProofPack, ReleaseManifest, or PolicyDecision semantics;
- changing lifecycle phases or allowing package code to promote or publish.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| **Last repository-grounded review** | 2026-07-23 |
| **Evidence base** | `main@a1570d5bb316d2a55edc95ff3f51413118ddb5ee` |
| **Prior content blob** | `e548a2b78b2e61d585fbf14a61729b8cfa08810b` |
| **Review route** | `.github/CODEOWNERS` → `/packages/ @bartytime4life` |
| **Next mandatory review** | Before adding build metadata, dependencies, public exports, generated code, CatalogMatrix models, I/O adapters, consumers, or package tests. |

Review this document sooner when contracts, schemas, validators, standards profiles, ADR status, package metadata, sibling-package boundaries, consumers, tests, workflows, release integration, correction behavior, or rollback posture changes.

[Back to top](#top)

---

## Bounded context and ubiquitous language

Within KFM, `packages/catalog/src/` means:

> The source container for reusable, non-deployable Python catalog-support code that transforms already-governed in-memory inputs into catalog-shaped values or validation results without owning acquisition, lifecycle transitions, evidence closure, policy decisions, release approval, persistence, serving, or public exposure.

It does not mean a STAC API, catalog server, pipeline runner, lifecycle writer, source connector, proof builder, release service, RDF store, or public trust membrane.

| Term | Meaning in this source root |
|---|---|
| **Source root** | Filesystem container separating importable code from project and repository metadata. |
| **Import package** | `catalog/`, the directory Python callers may import after packaging is configured. |
| **Public export** | Deliberately supported symbol exposed through `catalog.__init__` or documented import path. None are currently established. |
| **Catalog helper** | Pure or side-effect-minimal function that constructs, normalizes, serializes, validates, or translates catalog-shaped values. |
| **Catalog candidate** | Not-yet-public value awaiting evidence, rights, policy, review, release, correction, and rollback checks. |
| **Catalog record** | Discovery/interchange carrier such as STAC, DCAT, PROV, or a domain catalog projection; not proof or approval. |
| **CatalogMatrix** | Governed cross-record relationship descriptor whose current semantic, shape, validator, path, and closure expectations are not yet reconciled. |
| **Reference preservation** | Carrying stable refs without inventing, resolving, authorizing, or silently dropping them. |
| **Validation adapter** | Package function translating a canonical validator result without becoming schema or policy authority. |
| **Canonical serialization** | Stable representation produced under a named, versioned, accepted rule. |
| **Hidden I/O** | Filesystem, database, network, environment, process, clock, randomness, or global-state behavior not explicit in the function contract. |
| **Generated code** | Source emitted from canonical inputs with generator identity, input digest, command, and regeneration rule. |
| **Compatibility adapter** | Temporary versioned translation with semantic-loss disclosure, retirement condition, tests, and rollback. |

[Back to top](#top)

---

## Current bounded repository inventory

```text
packages/catalog/
├── README.md                       # v0.1 package boundary
├── pyproject.toml                  # name/version-only greenfield placeholder
└── src/
    ├── README.md                   # this v0.3 source-root contract
    └── catalog/
        ├── README.md               # v0.2 child-module contract
        └── __init__.py             # empty
```

Checked candidate modules `stac.py`, `dcat.py`, and `prov.py` are absent. This is a bounded inventory, not a guarantee that no additional branch, generated file, or unindexed path exists.

### Candidate future shape

Do not create this tree until package admission and authority reconciliation are complete.

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
        └── generated/              # only if an accepted generator owns it
```

The filenames are illustrative. Cohesive responsibilities, actual consumers, dependency direction, and accepted standards profiles—not topic symmetry—must determine modules.

### Layout rules

- Keep `src/` a source container, not an import namespace.
- Keep importable code under `src/catalog/` unless an accepted package rename changes the namespace.
- Do not add `src/__init__.py` merely for visual symmetry.
- Separate generated and hand-written code.
- Keep tests, fixtures, lifecycle records, receipts, proofs, and release objects outside package source.
- Keep public exports narrow and documented.
- Do not create parallel Python and TypeScript implementations without an accepted decision.

[Back to top](#top)

---

## Import and export contract

### Current state

`catalog/__init__.py` is empty. Current evidence therefore establishes:

```text
public exports         = none confirmed
import-time behavior   = none present in the empty initializer
package __version__    = not defined
entry points           = not defined
plugin registry        = not defined
installability         = not established
```

### Import safety

Future imports must be:

- side-effect free;
- network, filesystem, database, environment-secret, policy-decision, lifecycle-write, receipt-write, and release-decision free;
- deterministic and testable;
- safe when optional integrations are unavailable;
- explicit about configuration and injected dependencies.

Import-time behavior must not fetch external catalogs, open lifecycle files, connect to services, run migrations, register routes, evaluate policy, emit records or receipts, invoke models, or publish artifacts.

### Public API discipline

Before exposing a symbol from `catalog.__init__`:

1. define its bounded semantic responsibility;
2. identify constraining contracts, schemas, profiles, and accepted ADRs;
3. identify verified consumers and dependency direction;
4. specify input/output types and side effects;
5. define safe errors and limitations;
6. prove deterministic behavior where required;
7. add positive and negative tests;
8. record compatibility, deprecation, correction, and rollback expectations.

[Back to top](#top)

---

## Standards, profile, and namespace boundary

| Standard | Package role | Must not become |
|---|---|---|
| [STAC](../../../docs/standards/STAC.md) | Construct or validate spatiotemporal catalog candidates under an accepted profile. | STAC API, source truth, EvidenceBundle, release decision, or public permission. |
| [DCAT](../../../docs/standards/DCAT.md) | Construct or validate dataset, distribution, data-service, and catalog candidates. | Dataset authority or permission to publish. |
| [PROV-O / PAV](../../../docs/standards/PROV.md) | Preserve activities, entities, agents, derivation, attribution, and version relations. | Complete proof closure or renamed KFM-only provenance semantics. |

Helpers must preserve:

- standard identifiers, contexts, namespaces, predicates, links, and role semantics;
- KFM extension namespace and profile versions once accepted;
- unknown valid extension fields under the compatibility policy;
- source, evidence, rights, policy, review, release, correction, and rollback references;
- limitations, redaction, generalization, and withheld-state indicators.

They must not silently fork standards, rewrite predicates, strip namespace/version context, or make profile changes through package defaults alone.

[Back to top](#top)

---

## CatalogMatrix alignment and implementation hold

### Confirmed surfaces

```text
contracts/data/catalog_matrix.md
schemas/contracts/v1/data/catalog_matrix.schema.json
tools/validators/validate_catalog_matrix.py
```

The current contract describes a governed matrix of source, evidence, lifecycle, policy, review, release, correction, and rollback relationships. The paired schema requires only `id` and permits additional properties. The schema points to `tools/validators/data/validate_catalog_matrix.py`, which is absent at the checked path. The existing root-level validator raises `NotImplementedError`.

ADR-0011 and ADR-0022 both remain proposed:

- ADR-0011 separates catalogs from receipts, proofs, release manifests/decisions, and published artifacts, and states that a CatalogMatrix descriptor is not its own validation proof.
- ADR-0022 proposes release-level STAC/DCAT/PROV agreement on identity, digest, and release reference, but names proposed paths that differ from current repository surfaces.

### Hold conditions

Do not implement or generate CatalogMatrix package models until a coordinated change establishes:

1. accepted object meaning and object-family responsibility;
2. canonical schema path and complete enough shape;
3. canonical validator path and working behavior;
4. valid, invalid, denied, restricted, abstain, stale, corrected, superseded, and rollback fixtures;
5. standards-profile and namespace versions;
6. policy and sensitivity obligations;
7. closure proof versus catalog descriptor separation;
8. release integration and rollback posture;
9. package API and dependency direction;
10. tests and observed CI for the intended revision.

### Forbidden shortcut

Do not bridge the gap inside package code through permissive dictionaries, synthetic defaults, silent field dropping, duplicated schemas, locally invented closure semantics, or a validator that treats `id`-only schema success as release readiness.

[Back to top](#top)

---

## Determinism, identity, and time

### Determinism contract

Pure helpers should satisfy:

```text
same declared inputs
+ same profile/version
+ same canonicalization rule
+ same dependency versions
= same declared output bytes or semantic result
```

Control ordering, namespace compaction, volatile fields, timestamps, randomness, environment locale/timezone, floating-point formatting, Unicode normalization, and dependency-version effects.

### Identity rules

- Preserve upstream stable IDs and namespace/version context.
- Distinguish source identity, artifact identity, catalog-record identity, release identity, and relationship identity.
- Do not substitute display labels or slugs for canonical IDs.
- Do not regenerate IDs on every run without an accepted reason.
- Do not treat equal metadata as proof of equal real-world identity.
- Do not treat a digest as factual or release proof.

### Digest rules

A digest helper must declare algorithm, canonicalization, included/excluded fields, volatile-field handling, encoding, error behavior, and test vectors. Do not invent JSON Canonicalization Scheme, RDF canonicalization, namespace pins, or digest authority inside this package while those decisions remain unsettled.

### Time-kind preservation

Keep materially different times distinct, including source, valid, observed, retrieval, processing, catalog emission, release, correction, withdrawal, and supersession time. Never replace source time with retrieval time, make stale data appear current, or use ambient wall-clock time where a governed input is required.

[Back to top](#top)

---

## Dependency, side-effect, and public-path rules

### Current dependency posture

The current `pyproject.toml` declares no dependencies or build backend. `pystac`, RDF/JSON-LD libraries, JSON Schema libraries, canonicalization packages, and other integrations remain **PROPOSED**.

A dependency requires:

- verified use by a narrow public API;
- current version, license, security, maintenance, and compatibility review;
- deterministic/offline-test posture;
- explicit ownership and update policy;
- failure and fallback behavior;
- supply-chain and lockfile strategy;
- removal and rollback plan.

### Dependency direction

```text
contracts / schemas / standards / accepted policy outputs
        constrain
packages/catalog source
        may depend on narrow admitted sibling packages
        supports
pipelines / tools / governed callers
        own
I/O, receipts, evidence resolution, policy enforcement, release, serving
```

Potential callers include catalog pipelines, domain pipelines, tools, governed API projections, tests, and fixture generators. Actual consuming imports remain **UNKNOWN**.

### Side-effect rules

Package helpers must not silently:

- read/write lifecycle, proof, receipt, registry, or release paths;
- call source systems, public networks, databases, object stores, model runtimes, or internal services;
- read secret-bearing environment values;
- mutate caller inputs or global registries without an explicit contract;
- log restricted values;
- emit public URLs or approval states not supplied by governed callers.

When I/O is required, keep the split explicit:

```text
pure package helper returns candidate / result
  -> authorized pipeline or tool owns I/O
  -> caller emits receipt
  -> evidence, policy, review, release govern exposure
```

[Back to top](#top)

---

## Package admission and maturity

### Admission prerequisites

Before implementation files are added, establish:

- supported Python versions, build backend, package discovery, package name, and installation mode;
- verified consumers and reuse justification;
- dependency direction relative to hashing, identity, temporal, citation, schema-registry, evidence-resolver, redaction, policy-runtime, and release packages;
- accepted STAC/DCAT/PROV/PAV profiles, contexts, namespaces, and canonicalization rules;
- CatalogMatrix authority and enforcement resolution;
- source versus generated-code boundary;
- package-test and fixture homes;
- ownership and review burden;
- versioning, distribution, compatibility, deprecation, correction, and rollback policy.

**Gate:** one Python implementation, one build/discovery configuration, no duplicate authority, no hidden I/O, and no consumer migration before deterministic negative-state tests exist.

### Maturity model

| Level | Required evidence | Current status |
|---|---|---:|
| `M0 — documented scaffold` | README, project name/version placeholder, import-package directory. | **CONFIRMED** |
| `M1 — admitted package` | Build backend, Python support, discovery, owners, consumers, dependency direction. | **NOT ESTABLISHED** |
| `M2 — safe import surface` | Deliberate exports, side-effect-free import, structured errors, unit tests. | **NOT ESTABLISHED** |
| `M3 — one pure standards helper` | One accepted profile mapping, deterministic output, no-network tests. | **NOT ESTABLISHED** |
| `M4 — CatalogMatrix-capable` | Contract/schema/validator/ADR alignment, fixtures, closure boundary, drift checks. | **BLOCKED** |
| `M5 — governed consumer integration` | One authorized caller, explicit I/O/receipt boundary, policy/release tests, rollback. | **UNKNOWN** |
| `M6 — supported distribution` | CI, supply-chain controls, compatibility, release notes, deprecation, rollback drill. | **UNKNOWN** |

No README, `0.0.0` manifest, empty initializer, import, type check, package build, or unrelated green workflow may skip these levels.

### Smallest safe first slice

After admission, prefer one pure, reversible capability:

```text
already-governed metadata
  -> one accepted catalog candidate profile
  -> deterministic serialization
  -> explicit validation result
  -> no filesystem, network, policy, evidence, or release side effects
```

[Back to top](#top)

---

## Security, rights, sensitivity, and public safety

Future source must preserve these controls:

- no credentials, tokens, cookies, keys, signed URLs, DSNs, or secret-bearing examples;
- no raw prompts, private reasoning, stack traces, local paths, or adapter internals in public errors;
- no exact rare-species, archaeology, critical-infrastructure, private-land, living-person, DNA/genomic, or restricted cultural details in fixtures or logs;
- no caller-controlled rights, consent, evidence, policy, review, release, correction, redaction, or generalization authority;
- no automatic downgrade of unknown/restricted rights or sensitivity;
- no geometry generalization without an explicit transform and receipt contract;
- no unsafe deserialization, dynamic code execution, or permissive fallback that hides trust-bearing fields;
- no full restricted-payload logging or telemetry;
- no helper that converts internal paths or object-store handles into public URLs;
- no cache or projection that hides stale, corrected, withdrawn, or rollback state.

Fixtures must be synthetic or explicitly public-safe, deterministic, no-network, small, non-authoritative, and reviewed when they model denial, redaction, generalization, consent, or protected location behavior.

Security success is not evidence success. Schema validity is not authorization. Catalog discoverability is not public permission.

[Back to top](#top)

---

## Compatibility, correction, and rollback

### Compatibility rules

- Prefer additive changes only when semantics remain safe.
- Never silently drop standard predicates, extensions, evidence, rights, policy, review, release, correction, limitation, redaction, or generalization fields.
- Treat identity, digest, profile, namespace, time-kind, evidence, policy, release, and correction changes as high impact.
- Update contracts and schemas in their authority roots before generating package models.
- Record generator, source, profile, schema, and dependency identities.
- Bound compatibility windows and name retirement criteria.
- Preserve the ability to disable or revert each consumer migration independently.

### Correction propagation

A catalog helper must not make corrected, withdrawn, or superseded information appear current. Where inputs provide correction or rollback state, outputs should preserve state, refs, reasons, version/digest identity, and audit-safe identifiers. Authorized consumers—not pure package helpers—own cache invalidation and public correction display.

### Documentation rollback

Revert the README commit through normal Git history and re-run documentation checks. Restore the prior blob recorded in the meta block. No package, data, release, cache, or public correction rollback is required for this documentation-only revision.

### Future code rollback

1. identify the last compatible package, profile, schema, and consumer versions;
2. disable or revert the affected consumer integration;
3. restore the prior package artifact or commit;
4. invalidate incompatible generated outputs and caches;
5. preserve correction, withdrawal, supersession, and rollback refs;
6. rerun contract, schema, package, integration, security, and negative-state tests;
7. record the reason and affected software/release surfaces.

Rollback or hold when a change introduces hidden I/O, import-time work, nondeterministic identity/digests, dropped trust fields, renamed standard predicates, sensitive leakage, unauthorized lifecycle writes, or parallel authority.

[Back to top](#top)

---

## Definition of done

### This README revision

- [x] Preserves `packages/` as the shared-library responsibility root.
- [x] Identifies `src/` as a Python source container and `src/catalog/` as the current import package.
- [x] Follows the current first-twelve-section README contract.
- [x] Grounds the source root at a current commit and records the prior blob.
- [x] Distinguishes scaffold presence from implemented capability.
- [x] Records package metadata, empty initializer, absent checked modules, missing checked test/fixture lanes, contract, schema, validator, ADR, and CODEOWNERS evidence.
- [x] Preserves pipeline, lifecycle, evidence, policy, release, public-path, correction, and rollback boundaries.
- [x] Surfaces CatalogMatrix alignment as a blocker rather than resolving it by convention.
- [x] Preserves standards, determinism, identity, temporal, dependency, security, compatibility, and rollback obligations.
- [x] Creates no source code, manifest change, dependency, test, fixture, workflow, contract, schema, policy, data, release object, runtime behavior, or publication state.

### Future supported source root

- [ ] Build backend, Python support, package discovery, license, owners, and consumers are accepted.
- [ ] Dependency direction and sibling-package overlap are resolved.
- [ ] STAC/DCAT/PROV/PAV profiles, namespaces, contexts, and canonicalization are accepted.
- [ ] CatalogMatrix contract, schema, validator, fixtures, policy, ADRs, and release closure are reconciled.
- [ ] Source and generated-code boundaries are documented.
- [ ] Public exports are explicit and minimal.
- [ ] Imports are side-effect free.
- [ ] Deterministic no-network positive and negative tests exist.
- [ ] Rights, sensitivity, redaction, generalization, correction, and rollback states are preserved.
- [ ] Authorized caller integration proves package code cannot bypass lifecycle or release gates.
- [ ] CI and supply-chain results are observed for the intended revision.
- [ ] Compatibility, deprecation, correction propagation, and rollback are exercised.

[Back to top](#top)

---

## Open verification register

| ID | Question | Current state | Evidence needed |
|---|---|---|---|
| `PKG-CATALOG-SRC-001` | Which Python versions, build backend, and package-discovery configuration own this lane? | **UNKNOWN** | Accepted `pyproject.toml` and installation proof. |
| `PKG-CATALOG-SRC-002` | Which runtime and development dependencies are admitted? | **UNKNOWN** | Dependency review, lock/update policy, and consumer need. |
| `PKG-CATALOG-SRC-003` | Which symbols form the first stable public export surface? | **UNKNOWN** | Narrow API design, tests, and consumers. |
| `PKG-CATALOG-SRC-004` | Which current repository files import or should import `catalog`? | **UNKNOWN** | Complete import graph and consumer-owner confirmation. |
| `PKG-CATALOG-SRC-005` | Who owns the package and should CODEOWNERS gain a narrower route? | **NEEDS VERIFICATION** | Stewardship assignment and reviewer policy. |
| `PKG-CATALOG-SRC-006` | Which canonical test and fixture homes govern package instances? | **NEEDS VERIFICATION** | Repository test/fixture convention decision. |
| `PKG-CATALOG-SRC-007` | Which workflow validates import safety, package tests, generated drift, and consumers? | **UNKNOWN** | Command-bearing CI and observed run. |
| `PKG-CATALOG-SRC-008` | Which STAC profile/version and KFM extension namespace are authoritative? | **NEEDS VERIFICATION** | Accepted standards profile and ADR/registry. |
| `PKG-CATALOG-SRC-009` | Which DCAT profile/context/version is authoritative? | **NEEDS VERIFICATION** | Accepted standard/profile record. |
| `PKG-CATALOG-SRC-010` | Which PROV/PAV serialization, context, and canonicalization rules are authoritative? | **NEEDS VERIFICATION** | Accepted profile and test vectors. |
| `PKG-CATALOG-SRC-011` | Which JSON/RDF canonicalization and digest rules should catalog helpers use? | **NEEDS VERIFICATION** | Accepted identity/hashing decision. |
| `PKG-CATALOG-SRC-012` | How will the CatalogMatrix contract, schema, validator path, fixtures, policy, ADR-0011, and ADR-0022 be reconciled? | **OPEN BLOCKER** | Coordinated multi-root decision and enforcement slice. |
| `PKG-CATALOG-SRC-013` | Is the root-level validator stub retained, moved, replaced, or superseded? | **NEEDS VERIFICATION** | Validator ownership and migration decision. |
| `PKG-CATALOG-SRC-014` | Should generated models live here, in another package, or remain absent? | **NEEDS VERIFICATION** | Generator, dependency, and package-boundary decision. |
| `PKG-CATALOG-SRC-015` | Which sibling packages own hashing, identity, temporal, citation, schema lookup, redaction, policy runtime, and release helpers? | **CONFLICTED / NEEDS VERIFICATION** | Package responsibility crosswalk and dependency graph. |
| `PKG-CATALOG-SRC-016` | What compatibility, deprecation, correction, and support policy governs catalog-profile changes? | **UNKNOWN** | Accepted package/version policy. |
| `PKG-CATALOG-SRC-017` | Which thin-slice pipeline or tool is the first governed consumer? | **UNKNOWN** | Consumer selection and integration tests. |
| `PKG-CATALOG-SRC-018` | Which tests prove the package cannot write lifecycle or release state? | **NOT ESTABLISHED** | No-I/O tests and authorized-caller boundary test. |
| `PKG-CATALOG-SRC-019` | What security, license, and supply-chain review applies to future third-party dependencies? | **NEEDS VERIFICATION** | Dependency admission record. |
| `PKG-CATALOG-SRC-020` | Are there source files or consumers absent from current index and exact checks? | **NEEDS VERIFICATION** | Recursive tree and import inspection at the pinned ref. |
| `PKG-CATALOG-SRC-021` | Has correction and rollback propagation been exercised through a real catalog consumer? | **UNKNOWN** | Integration test, correction record, and rollback evidence. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Repository location | Supports | Does not prove |
|---|---|---|---|
| Target README | `packages/catalog/src/README.md` | Existing source-root boundary and update target. | Implemented helper behavior. |
| Packages root contract | [`packages/README.md`](../../README.md) | Shared-library placement, maturity, dependency, compatibility, and distribution rules. | Catalog package exports or consumers. |
| Parent catalog README | [`packages/catalog/README.md`](../README.md) | Catalog shared-library boundary. | Current package maturity; document is older than parent root. |
| Package metadata | [`packages/catalog/pyproject.toml`](../pyproject.toml) | Name and `0.0.0` placeholder. | Build backend, dependencies, installability, or distribution. |
| Child module README | [`catalog/README.md`](catalog/README.md) | `src/catalog/` bounded-context documentation. | Helper implementation. |
| Empty initializer | [`catalog/__init__.py`](catalog/__init__.py) | Import-package scaffold and no initializer content. | Installability or public API. |
| Exact absent-module probes | `catalog/stac.py`, `catalog/dcat.py`, `catalog/prov.py` | Checked candidate helpers are absent. | All possible helper files or branches. |
| Exact test/fixture probes | `tests/packages/catalog/README.md`, `fixtures/packages/catalog/README.md` | Checked lane READMEs are absent. | No tests or fixtures anywhere. |
| Directory Rules | [`docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) | Placement and required README contract. | Runtime behavior. |
| CODEOWNERS | [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) | `/packages/` GitHub review route. | Accepted stewardship or review completion. |
| CatalogMatrix contract | [`contracts/data/catalog_matrix.md`](../../../contracts/data/catalog_matrix.md) | Semantic meaning, invariants, and placeholder warning. | Complete machine shape or validator. |
| CatalogMatrix schema | [`schemas/contracts/v1/data/catalog_matrix.schema.json`](../../../schemas/contracts/v1/data/catalog_matrix.schema.json) | Current minimal `PROPOSED` shape and metadata. | Semantic closure or release readiness. |
| CatalogMatrix validator | [`tools/validators/validate_catalog_matrix.py`](../../../tools/validators/validate_catalog_matrix.py) | Root-level stub presence. | Working validation. |
| Catalog pipeline README | [`pipelines/catalog/README.md`](../../../pipelines/catalog/README.md) | Executable catalog-orchestration responsibility. | Runtime implementation or successful run. |
| Catalog lifecycle README | [`data/catalog/README.md`](../../../data/catalog/README.md) | Catalog-stage lifecycle and release-gated exposure. | Concrete catalog inventory or public enforcement. |
| ADR-0011 | [`docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`](../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | Proposed artifact-family separation and current CatalogMatrix conflict note. | Accepted decision or enforcement. |
| ADR-0022 | [`docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md`](../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | Proposed release-level STAC/DCAT/PROV agreement. | Current canonical paths, accepted decision, or working closure. |

[Back to top](#top)

---

## No-loss modernization ledger

| v0.2 material | v0.3 disposition |
|---|---|
| Purpose, audience, source-root responsibility | Retained under [Purpose](#purpose), [Bounded context](#bounded-context-and-ubiquitous-language), and [What belongs here](#what-belongs-here). |
| Current repository state and evidence boundary | Refreshed under [Status](#status) and [Current inventory](#current-bounded-repository-inventory). |
| Placement, authority, and anti-collapse rules | Retained and strengthened under [Authority level](#authority-level) and [What does not belong here](#what-does-not-belong-here). |
| Current/proposed layout | Retained under [Current bounded repository inventory](#current-bounded-repository-inventory). |
| Import/export contract | Retained under [Import and export contract](#import-and-export-contract). |
| Inputs, outputs, side effects | Retained under [Inputs](#inputs), [Outputs](#outputs), and [Dependency, side-effect, and public-path rules](#dependency-side-effect-and-public-path-rules). |
| STAC/DCAT/PROV posture | Retained under [Standards, profile, and namespace boundary](#standards-profile-and-namespace-boundary). |
| CatalogMatrix drift | Updated with current ADR-0011 evidence under [CatalogMatrix alignment and implementation hold](#catalogmatrix-alignment-and-implementation-hold). |
| Determinism, identity, digests, and time | Retained under [Determinism, identity, and time](#determinism-identity-and-time). |
| Dependency boundaries and consumers | Retained and expanded with sibling-package overlap under [Dependency rules](#dependency-side-effect-and-public-path-rules). |
| Validation and future tests | Retained under [Validation](#validation). |
| Security, rights, sensitivity, public safety | Retained under [Security, rights, sensitivity, and public safety](#security-rights-sensitivity-and-public-safety). |
| Implementation admission sequence | Converted into the evidence-based maturity model under [Package admission and maturity](#package-admission-and-maturity). |
| Generated code, compatibility, migrations | Retained under [Compatibility, correction, and rollback](#compatibility-correction-and-rollback). |
| Definition of done, open questions, evidence, checklist | Retained and refreshed in their named sections. |

The v0.2 file remains recoverable through Git history and the prior blob recorded above. This revision supersedes its presentation and evidence snapshot, not implementation, authority, release, or public state.

[Back to top](#top)

---

## Maintainer checklist

Before adding or changing source under `packages/catalog/src/`:

- [ ] Confirm the responsibility belongs in reusable package code rather than pipelines, tools, connectors, contracts, schemas, policy, data, release, runtime, or apps.
- [ ] Confirm supported Python, build, discovery, dependency, license, owner, consumer, test, and distribution decisions.
- [ ] Confirm contracts, schemas, standards profiles, namespaces, policy, and ADR status.
- [ ] Resolve CatalogMatrix contract/schema/validator/fixture/policy/release closure before generating package models.
- [ ] Inspect sibling packages and establish dependency direction rather than duplicating helpers.
- [ ] Keep imports side-effect free.
- [ ] Keep network, filesystem, database, environment, clock, randomness, and global state explicit and injected.
- [ ] Do not write lifecycle or release state from pure helpers.
- [ ] Preserve source, evidence, receipt, policy, review, release, correction, and rollback refs.
- [ ] Preserve unknown valid extension fields under the accepted policy.
- [ ] Do not rename standard predicates or fork STAC/DCAT/PROV/PAV semantics.
- [ ] Define deterministic ordering, serialization, identity, time, and digest rules with test vectors.
- [ ] Avoid sensitive values in errors, logs, reprs, fixtures, snapshots, and telemetry.
- [ ] Add positive, negative, no-network, no-hidden-I/O, determinism, compatibility, and sensitive-leak tests.
- [ ] Document public exports, deprecation, correction propagation, and rollback.
- [ ] Record generator provenance and drift checks for generated code.
- [ ] Update parent, source-root, and child-module READMEs when boundaries change.
- [ ] Do not claim installability, implementation, CI, deployment, release, or public availability without current evidence.

---

> **Operating law.** Keep `packages/catalog/src/` boring, import-safe, deterministic, and subordinate to the trust membrane. Make governed catalog construction easier without letting package code acquire authority to admit sources, write lifecycle state, create evidence, decide policy, approve release, serve clients, or publish claims.
