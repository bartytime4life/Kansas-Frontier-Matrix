<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-catalog-src-catalog-readme
title: Catalog Package Source Catalog Module README
type: readme
version: v0.3
status: draft; repository-grounded
owners:
  - "@bartytime4life"
owner_status: "GitHub review routing is confirmed through .github/CODEOWNERS; catalog, schema, evidence, release, security, and documentation stewardship remain NEEDS VERIFICATION"
created: 2026-06-13
updated: 2026-07-23
policy_label: public
path: packages/catalog/src/catalog/README.md
owning_root: packages/
responsibility: reusable non-deployable Python helpers for catalog candidate construction, reference preservation, deterministic serialization, and validation adaptation
truth_posture: cite-or-abstain; implementation claims are bounded to the pinned repository evidence snapshot
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 17083bece43284fdb9534332988629bdc2bdd616
  target_prior_blob: 14d0462d9dfa0d594df33e9a8da6cc7bc1f8ebf0
  package_readme_blob: ac16ca299120d7b03b4c24915e969f6f5610f4ae
  source_root_readme_blob: e548a2b78b2e61d585fbf14a61729b8cfa08810b
  pyproject_blob: 13e0f5b7763a7ed193955e87a03910a924fde90f
  init_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  catalog_matrix_contract_blob: c67923beb505aa39e7c0c768c16e75a00826ff31
  catalog_matrix_schema_blob: 75a927376066226d8a0f89a630d7bb3693143c41
  root_validator_blob: 91ecf78675cf19672a0e94a3899df3074c36ddc4
  adr_0011_blob: 40b0f47b87d584040803ed76aa6b31f5204b7fca
  adr_0022_blob: b09c1d7aaa39f3030afdcec419c58236fd324f17
related:
  - ../../README.md
  - ../README.md
  - ../../pyproject.toml
  - __init__.py
  - ../../../../.github/CODEOWNERS
  - ../../../../pipelines/catalog/README.md
  - ../../../../data/catalog/README.md
  - ../../../../contracts/data/catalog_matrix.md
  - ../../../../schemas/contracts/v1/data/catalog_matrix.schema.json
  - ../../../../tools/validators/validate_catalog_matrix.py
  - ../../../../tools/validators/catalog/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../../../docs/standards/STAC.md
  - ../../../../docs/standards/DCAT.md
  - ../../../../docs/standards/PROV.md
tags: [kfm, packages, catalog, python, scaffold, stac, dcat, prov, catalog-matrix, deterministic-serialization, evidence, release, governance]
notes:
  - "v0.3 is a same-path evidence refresh and structural consolidation of v0.2."
  - "Current evidence still shows a name/version-only pyproject.toml, an empty catalog/__init__.py, no observed STAC/DCAT/PROV helper modules, no package-local test or fixture README, a permissive CatalogMatrix schema, a missing schema-declared validator path, and a root NotImplementedError validator stub."
  - "ADR-0011 v1.2 separates the CatalogMatrix descriptor from the proof of its validation and defers coordinated acceptance and migration to ADR-0022."
  - "ADR-0011 and ADR-0022 remain proposed; this README accepts neither and establishes no release-level closure."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Source Module

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b)](#status-and-evidence-boundary)
[![Implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-d97706)](#current-repository-state)
[![Runtime: Python placeholder](https://img.shields.io/badge/runtime-Python%20placeholder-3776ab)](../../pyproject.toml)
[![Catalog: carrier, not truth](https://img.shields.io/badge/catalog-carrier%20not%20truth-b42318)](#authority-boundary)
[![CatalogMatrix: unresolved](https://img.shields.io/badge/CatalogMatrix-ADR%20resolution%20required-8250df)](#catalogmatrix-alignment)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781)](#authority-boundary)

> Reusable Python source lane for constructing catalog **candidates**, preserving governed references, adapting validation results, and producing deterministic representations. The current repository surface remains a scaffold: package metadata declares only a name and version, `catalog/__init__.py` is empty, and no STAC, DCAT, or PROV helper implementation was observed at the tested paths.

> [!IMPORTANT]
> **This module is implementation support, not authority.** It does not own catalog lifecycle records, evidence closure, policy decisions, schemas, contracts, release approval, publication, public serving, source acquisition, or pipeline orchestration.

> [!CAUTION]
> A STAC Item, DCAT Dataset, PROV fragment, `CatalogMatrix`, digest, schema pass, or package test is a carrier or validation signal. None becomes truth, proof, release approval, public-safety clearance, or publication permission by itself.

## Quick navigation

- [Status and evidence boundary](#status-and-evidence-boundary)
- [Purpose and bounded context](#purpose-and-bounded-context)
- [Current repository state](#current-repository-state)
- [Authority boundary](#authority-boundary)
- [Responsibilities and interfaces](#responsibilities-and-interfaces)
- [Standards posture](#standards-posture)
- [CatalogMatrix alignment](#catalogmatrix-alignment)
- [Determinism, time, and side effects](#determinism-time-and-side-effects)
- [Security and public safety](#security-and-public-safety)
- [Directory and implementation contract](#directory-and-implementation-contract)
- [Validation and tests](#validation-and-tests)
- [Compatibility, correction, and rollback](#compatibility-correction-and-rollback)
- [Open verification register](#open-verification-register)
- [Evidence ledger](#evidence-ledger)
- [Maintainer checklist](#maintainer-checklist)

---

## Status and evidence boundary

| Field | Current state |
|---|---|
| Repository snapshot | `main@17083bece43284fdb9534332988629bdc2bdd616` |
| Operation | Same-path modernization of `packages/catalog/src/catalog/README.md` |
| Parent surfaces | [`packages/catalog/`](../../README.md) and [`packages/catalog/src/`](../README.md) |
| Confirmed implementation | Name/version-only [`pyproject.toml`](../../pyproject.toml) plus empty [`__init__.py`](__init__.py) |
| Helper implementation | **NOT OBSERVED** at tested STAC/DCAT/PROV paths |
| Review routing | [`.github/CODEOWNERS`](../../../../.github/CODEOWNERS) routes `packages/` to `@bartytime4life` |
| Stewardship | **NEEDS VERIFICATION**; CODEOWNERS is review routing, not a stewardship assignment |
| Public or release effect | None |

The evidence is bounded to current file reads, exact-path checks, indexed search, and related repository documents. It does not establish a complete recursive inventory, package installation, runtime behavior, successful catalog generation, public routes, or release closure.

```text
Python project placeholder         = CONFIRMED
empty import-package initializer   = CONFIRMED
implemented catalog helpers        = NOT OBSERVED
public package exports             = NOT ESTABLISHED
build backend                      = NOT DECLARED
runtime dependencies               = NOT DECLARED
package-specific tests/fixtures    = NOT OBSERVED
working CatalogMatrix validator    = NOT ESTABLISHED
release-level catalog closure      = NOT ESTABLISHED
catalog write behavior             = UNKNOWN
```

[Back to top](#top)

---

## Purpose and bounded context

Within KFM, `packages/catalog/src/catalog/` means:

> Reusable, non-deployable Python helpers that transform explicit, already-governed in-memory inputs into catalog-shaped candidates or validation results without owning acquisition, lifecycle transitions, evidence closure, policy decisions, persistence, release approval, or public exposure.

A mature module may support:

- STAC Catalog, Collection, Item, Asset, and Link candidate construction;
- DCAT Catalog, Dataset, Distribution, and DataService candidate construction;
- PROV-O/PAV entity, activity, agent, and predicate preservation;
- source, evidence, receipt, policy, review, release, correction, withdrawal, supersession, and rollback reference preservation;
- explicitly selected profile dispatch;
- stable identifiers under an accepted identity grammar;
- canonical serialization and digest calculation under an accepted versioned specification;
- narrow validation adapters that preserve failures and warnings;
- explicitly versioned compatibility adapters with loss and retirement metadata;
- deterministic synthetic fixtures that cannot be mistaken for production records.

It is not a catalog server, STAC API, pipeline runner, lifecycle writer, proof builder, source registry, graph authority, release service, or public-client trust membrane.

### Ubiquitous language

| Term | Meaning here |
|---|---|
| **Catalog candidate** | In-memory or serialized catalog-shaped value awaiting validation, policy, review, and any authorized write. |
| **Catalog record** | Catalog-stage STAC, DCAT, PROV, or KFM metadata under the catalog lifecycle owner. |
| **Catalog carrier** | Discovery/interchange metadata that references governed objects without replacing them. |
| **CatalogMatrix descriptor** | Generic governed relationship descriptor defined by the current contract. |
| **Catalog closure matrix** | Proposed release-level STAC/DCAT/PROV agreement artifact in ADR-0022. |
| **Closure proof** | Separate evidence that a matrix and referenced records passed applicable checks. |
| **Validation adapter** | Helper that invokes or normalizes an established validator without becoming validator authority. |
| **Writer** | Code that mutates lifecycle or release state; not owned here. |

[Back to top](#top)

---

## Current repository state

| Surface | Confirmed state | Consequence |
|---|---|---|
| [`packages/catalog/README.md`](../../README.md) | Shared catalog-support boundary exists. | This module must remain subordinate to the parent package. |
| [`packages/catalog/src/README.md`](../README.md) | Python source-root boundary exists. | This README refines, not replaces, that contract. |
| [`pyproject.toml`](../../pyproject.toml) | Only project name `kfm-catalog` and version `0.0.0`. | No build backend, dependencies, discovery, entry points, or publishability established. |
| [`__init__.py`](__init__.py) | Empty. | No exports, version constant, or import-time behavior established. |
| `stac.py`, `dcat.py`, `prov.py` | Not found at tested flat paths. | Do not claim helper implementation. |
| `tests/packages/catalog/README.md` | Not found at tested path. | No package-test lane documented there. |
| `fixtures/packages/catalog/README.md` | Not found at tested path. | No package-fixture lane documented there. |
| [`CatalogMatrix` contract](../../../../contracts/data/catalog_matrix.md) | Draft semantic descriptor exists. | Meaning authority exists but remains incomplete for release closure. |
| [`CatalogMatrix` schema](../../../../schemas/contracts/v1/data/catalog_matrix.schema.json) | Placeholder; requires only `id` and allows additional properties. | A schema pass cannot prove semantic or release closure. |
| [`tools/validators/validate_catalog_matrix.py`](../../../../tools/validators/validate_catalog_matrix.py) | Raises `NotImplementedError`. | No working root validator. |
| Schema-declared validator | `tools/validators/data/validate_catalog_matrix.py` not found. | Metadata and implementation path remain misaligned. |
| ADR-0011 / ADR-0022 | Both proposed. | No accepted object-family, instance-home, validator, or enforcement decision. |

[Back to top](#top)

---

## Authority boundary

Directory Rules place reusable libraries under `packages/`, executable catalog orchestration under `pipelines/`, lifecycle records under `data/`, semantic meaning under `contracts/`, machine shape under `schemas/`, admissibility under `policy/`, and release decisions under `release/`.

| Concern | Correct owner |
|---|---|
| Reusable value-in/value-out catalog helpers | `packages/catalog/src/catalog/` |
| Executable catalog orchestration and writes | `pipelines/catalog/` or an accepted domain pipeline |
| Declarative pipeline configuration | `pipeline_specs/` |
| Catalog and triplet records | `data/catalog/` and `data/triplets/` |
| Receipts and proofs | `data/receipts/` and `data/proofs/` |
| Source descriptors | accepted source-registry home |
| Semantic contracts and machine schemas | `contracts/` and `schemas/contracts/v1/` |
| Policy evaluation | `policy/` and accepted policy runtime |
| Promotion, release, correction, withdrawal, rollback | `release/` |
| Public routes and rendering | governed application/API/UI surfaces |
| Repo-wide validators | `tools/validators/` |

```text
catalog helper        != lifecycle writer
schema pass           != evidence closure
catalog metadata      != source truth
STAC/DCAT/PROV record != release approval
CatalogMatrix         != closure proof or automatic release
receipt reference     != proof
release reference     != release decision
fixture               != production catalog
empty __init__.py     != implemented package
```

[Back to top](#top)

---

## Responsibilities and interfaces

### Owned behavior

A future implementation may own these narrow, reusable behaviors:

- **construction:** assemble standard-shaped candidates from explicit mappings and reject missing required inputs;
- **dispatch:** select an accepted STAC/DCAT/PROV profile explicitly and expose the decision;
- **reference preservation:** retain identifiers, digests, obligations, and governed references without silently resolving them;
- **determinism:** apply accepted identity, canonicalization, serialization, and digest specifications;
- **validation adaptation:** preserve complete finite validator outcomes without upgrading a shape pass into trust;
- **compatibility:** translate only explicit versions, disclose loss, warn on deprecated fields, and include retirement conditions.

### Accepted inputs

Inputs must be explicit already-governed values or clearly synthetic fixtures, including identity, spatial/temporal metadata, distribution metadata, source/evidence/policy/release state, provenance relations, and profile/version information. Source role, rights, sensitivity, or release state must not be inferred from filenames, URLs, or display labels.

### Bounded outputs

Allowed outputs are in-memory or serialized candidates, deterministic bytes, digest metadata, finite validation results, and explicit compatibility warnings. Catalog lifecycle writes, policy decisions, release outcomes, and publication results are forbidden.

```text
authorized caller
  -> explicit governed inputs
  -> catalog helper
  -> candidate + validation/digest metadata
  -> caller-owned validation and policy gates
  -> authorized pipeline writer
  -> catalog-stage record + receipt
  -> release review
  -> governed public projection
```

Prefer immutable or copy-on-write value-in/value-out functions. Hidden IO is a boundary violation.

[Back to top](#top)

---

## Standards posture

| Family | Primary use | Module obligation | Must not do |
|---|---|---|---|
| STAC | Spatiotemporal assets and collections | Preserve core structure, geometry/time, assets, links, roles, and accepted KFM namespaces. | Treat a STAC object as evidence or release approval. |
| DCAT | Dataset/distribution discovery | Preserve DCAT classes/properties, rights, conformity, provenance, and KFM refs. | Treat a DCAT Dataset as source truth. |
| PROV-O/PAV | Entity/activity/agent lineage and versioning | Preserve standard predicates and qualified relations. | Rename predicates or claim complete proof closure. |
| Combined matrix | Cross-standard comparison | Compare identity, digest, release, evidence, source, and profile references. | Resolve proposed ADR conflicts silently. |

Helpers must extend standards through accepted namespaces, preserve unknown standards-compliant fields unless an accepted contract excludes them, and return `ABSTAIN`/error when profile dispatch is unsafe. Version-sensitive standards claims require re-verification before implementation or dependency pinning.

[Back to top](#top)

---

## CatalogMatrix alignment

`CatalogMatrix` remains the highest-risk unresolved surface for this module.

### Confirmed facts

- the generic contract exists under `contracts/data/`;
- its schema exists under `schemas/contracts/v1/data/` but is permissive and marked `PROPOSED`;
- schema metadata names a validator path that is absent;
- a different root validator exists but is only a stub;
- ADR-0011 v1.2 and ADR-0022 v1.1 are both proposed.

### Corrected interpretation

The current ADR-0011 no longer says that the generic `CatalogMatrix` descriptor is inherently a proof-side object. It separates catalog descriptors from the proof of their validation and defers coordinated object-family and migration decisions to ADR-0022. ADR-0022 proposes a release-level STAC/DCAT/PROV agreement artifact and different catalog-family paths.

Therefore the unresolved questions are whether generic descriptors and release closure matrices are one versioned family or two related families, where instances belong at each lifecycle stage, which contract/schema profile is canonical, and which validator/policy/resolver paths enforce the decision.

Until resolved, this module must not:

- hard-code a canonical matrix instance home;
- treat the placeholder schema as release-grade closure;
- create a parallel contract, schema, validator, policy, or proof family;
- embed policy or release decisions in a matrix;
- rename validator entry points silently;
- describe `CatalogMatrix` as implemented enforcement.

A candidate builder may accept an explicit profile identifier and return a descriptor plus validation status. Release-level closure requires accepted ADRs, complete shapes, fixtures, validators, policy, proof, review, correction, and rollback.

[Back to top](#top)

---

## Determinism, time, and side effects

Identifier derivation and canonical serialization must name the namespace, object family, version, input fields, encoding, Unicode and number normalization, key/array order semantics, geometry precision, JSON-LD/RDF canonicalization where applicable, digest algorithm, and serializer/profile version. `sort_keys=True` alone is not a canonicalization contract. A digest proves byte identity, not truth or admissibility.

Preserve distinct valid, observed, source, retrieval, processing, catalog, release, and correction times. Never rewrite stale source or observation time to build time.

The default execution shape is:

```text
explicit values -> pure validation/normalization/construction -> returned values
```

Helpers must not silently read lifecycle/canonical stores, write any `data/` or `release/` authority surface, perform network calls, resolve credentials, fetch source descriptors, call model runtimes, mutate caller inputs, approve policy/review/release, suppress failures, or log restricted payloads. Concrete IO belongs to a reviewed executable adapter with least privilege, dry-run support, receipts, failure disposition, no-public-bypass tests, and rollback.

[Back to top](#top)

---

## Security and public safety

Catalog metadata can expose protected information even when an asset is access-controlled: exact archaeology or rare-species locations, living-person or DNA metadata, private-land joins, infrastructure exposure, embargoed membership, internal paths, signed URLs, credentials, or policy explanations that reveal protected facts.

Helpers must accept policy and transform obligations explicitly; generalize or omit only under an accepted transform/profile; preserve transform indicators and receipt refs; avoid logging full payloads; sanitize errors; never embed credentials or temporary URLs; never follow URLs as a construction side effect; preserve rights, attribution, embargo, and access metadata; and fail closed when a public-safe projection cannot be determined.

```text
package candidate != catalog-stage record
catalog-stage record != released record
released record != unrestricted record
```

[Back to top](#top)

---

## Directory and implementation contract

### Confirmed scaffold

```text
packages/catalog/
├── README.md
├── pyproject.toml          # name/version-only placeholder
└── src/
    ├── README.md
    └── catalog/
        ├── README.md
        └── __init__.py     # empty
```

This is a bounded confirmed view, not a complete recursive-tree assertion. Future files are **PROPOSED** until a consumer-backed use case, controlling contract/schema/profile, tests, and placement review justify them.

### Safe implementation sequence

1. **Reconcile authority:** track or resolve CatalogMatrix object-family, schema, instance-home, validator, and policy drift; identify accepted standards profiles; assign stewardship.
2. **Make the scaffold testable:** add build/discovery/version/test configuration only under verified package conventions; keep exports minimal.
3. **Implement one pure helper:** use explicit input, deterministic output, no IO, one accepted contract/profile, and positive/negative/determinism tests.
4. **Add standards adapters incrementally:** preserve unknown fields and governed refs; test round trips and profile failures.
5. **Integrate through a pipeline:** the executable caller owns reads, writes, policy, receipts, and failure disposition.
6. **Add release closure only after governance resolution:** require complete shapes, validators, policy, proofs, finite outcomes, review, correction, and rollback.

The safest first slice is a small STAC Asset/Link or catalog-reference builder, not release-level `CatalogMatrix` enforcement.

[Back to top](#top)

---

## Validation and tests

### Current maturity

| Surface | Status |
|---|---|
| Package import/helper tests | **NOT OBSERVED** |
| Package fixtures | **NOT OBSERVED** |
| Generic schema | **CONFIRMED placeholder; insufficient for closure** |
| Schema-declared validator | **CONFIRMED absent at tested path** |
| Root validator | **CONFIRMED stub** |
| Catalog validator lane | **README present; executable maturity unknown** |
| Repository test execution for this documentation change | **NOT RUN locally** |

Before implementation claims, test:

- import and export behavior;
- no hidden filesystem/network/model/lifecycle access;
- required-input failures and unsupported profile versions;
- stable serialization and digest reproducibility;
- unknown-field and governed-reference preservation;
- STAC/DCAT/PROV mapping and round trips;
- cross-record identity/digest/release conflicts;
- sensitive-field withholding/generalization;
- finite validation outcomes that do not imply evidence or release approval;
- correction, compatibility, and retirement behavior.

Proposed test and fixture homes remain `tests/packages/catalog/` and `fixtures/packages/catalog/` until adopted. Do not claim they exist until created and verified.

[Back to top](#top)

---

## Compatibility, correction, and rollback

A compatibility adapter must specify source and target profile versions, every renamed/defaulted/removed field, information loss, warnings, fixtures, retirement conditions, and rollback behavior. Silent coercion is forbidden.

Catalog corrections must preserve prior identifiers and release refs, changed-field summaries, correction/supersession/withdrawal refs, effective correction time, new digest/profile version, public-safe status, and rollback target. This package may shape correction metadata; it cannot authorize correction or withdrawal.

Block or revert changes that introduce hidden IO or writes, create parallel authority, weaken catalog/evidence/release separation, drop governed references, make serialization nondeterministic without a contract, expose restricted metadata, treat schema validity as publication, add compatibility without retirement, or change exports without versioning and consumer review.

Documentation rollback is a same-file revert. Implementation rollback must revert code, exports, tests, fixtures, generated types, and dependent callers as one reviewed change.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---|
| `PKG-CATALOG-MOD-001` | Is this package independently buildable or subordinate to the root build? | **NEEDS VERIFICATION** |
| `PKG-CATALOG-MOD-002` | Which Python versions, dependencies, and exports are supported? | **UNKNOWN** |
| `PKG-CATALOG-MOD-003` | Which STAC, DCAT, PROV/PAV, namespace, and canonicalization profiles are accepted? | **NEEDS VERIFICATION** |
| `PKG-CATALOG-MOD-004` | Are generic descriptors and release closure matrices one family or two related families? | **CONFLICTED / NEEDS VERIFICATION** |
| `PKG-CATALOG-MOD-005` | Which contract/schema, instance homes, validator, policy, and resolver paths are canonical? | **CONFLICTED / NEEDS VERIFICATION** |
| `PKG-CATALOG-MOD-006` | Which pure helper is the first consumer-backed slice? | **PROPOSED** |
| `PKG-CATALOG-MOD-007` | Where will package tests and fixtures live, and which workflows run them? | **NEEDS VERIFICATION** |
| `PKG-CATALOG-MOD-008` | Are there unindexed files or consumers? | **UNKNOWN** |
| `PKG-CATALOG-MOD-009` | Who holds catalog/schema/evidence/release stewardship? | **NEEDS VERIFICATION** |
| `PKG-CATALOG-MOD-010` | Which rights, sensitivity, correction, stale-state, and rollback profiles must builders preserve? | **NEEDS VERIFICATION** |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Prior README blob | **CONFIRMED** | v0.2 identity and preserved guidance | Current implementation |
| [`pyproject.toml`](../../pyproject.toml) | **CONFIRMED placeholder** | Project name/version | Buildability or maturity |
| [`__init__.py`](__init__.py) | **CONFIRMED empty** | Import-package scaffold | Exports or behavior |
| Exact helper/test/fixture checks | **CONFIRMED at tested paths** | Tested paths absent | Complete tree absence |
| Parent/source-root READMEs | **CONFIRMED** | Responsibility boundaries | Runtime behavior |
| `CatalogMatrix` contract/schema | **CONFIRMED draft/placeholder** | Current semantics and machine stub | Accepted release closure |
| Root/missing validator paths | **CONFIRMED stub/drift** | Current validation gap | Intended final location |
| ADR-0011 v1.2 | **CONFIRMED document / PROPOSED decision** | Family separation and descriptor/proof distinction | Accepted migration or enforcement |
| ADR-0022 v1.1 | **CONFIRMED document / PROPOSED decision** | Proposed release agreement invariant | Accepted object family or implementation |
| CODEOWNERS | **CONFIRMED review route** | `@bartytime4life` reviews `packages/` | Stewardship, completed review, or release authority |
| Catalog pipeline/data READMEs | **CONFIRMED documentation** | Executable and lifecycle boundaries | Successful runs or publication |

[Back to top](#top)

---

## Maintainer checklist

Before changing source in this module:

- [ ] Confirm the change is reusable package code, not executable orchestration.
- [ ] Name the controlling contract, schema, profile, identity, and serialization rules.
- [ ] Confirm no hidden filesystem, network, database, registry, object-store, graph, or model access.
- [ ] Confirm no lifecycle or release writes.
- [ ] Preserve source, evidence, policy, review, release, correction, and rollback refs.
- [ ] Preserve or explicitly reject unknown standards-compliant fields.
- [ ] Preserve sensitivity, rights, attribution, embargo, and transform obligations.
- [ ] Keep validation failures visible; never convert schema validity into trust or release approval.
- [ ] Version exports and compatibility behavior.
- [ ] Include negative, determinism, no-IO, unknown-field, and sensitivity tests.
- [ ] Do not silently encode unresolved CatalogMatrix or validator-path decisions.
- [ ] Update docs, ADR/drift notes, migration, correction, and rollback when behavior changes.
- [ ] Observe CI before claiming readiness.

---

## Maintainer note

Keep this module small, deterministic, testable, reviewable, and subordinate to KFM’s evidence, policy, catalog, release, correction, and rollback controls.

The safest first code change remains one pure helper with explicit inputs, no IO, one accepted contract/profile, deterministic fixtures, and negative tests. Do not begin with release-level `CatalogMatrix` enforcement while its object-family, path, schema, validator, policy, migration, and proof decisions remain unresolved.
