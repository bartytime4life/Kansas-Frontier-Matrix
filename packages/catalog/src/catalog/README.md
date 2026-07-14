<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-catalog-src-catalog-readme
title: Catalog Package Source Catalog Module README
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
path: packages/catalog/src/catalog/README.md
related:
  - ../../../README.md
  - ../../README.md
  - ../README.md
  - ../../../../pipelines/catalog/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/lifecycle-law.md
  - ../../../../docs/doctrine/trust-membrane.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../../../docs/standards/STAC.md
  - ../../../../docs/standards/DCAT.md
  - ../../../../docs/standards/PROV.md
  - ../../../../contracts/data/catalog_matrix.md
  - ../../../../schemas/contracts/v1/data/catalog_matrix.schema.json
  - ../../../../tools/validators/validate_catalog_matrix.py
  - ../../../../tools/validators/catalog/README.md
  - ../../../../data/catalog/README.md
tags: [kfm, packages, catalog, src, python, scaffold, shared-library, catalog-module, stac, dcat, prov, catalog-matrix, deterministic-serialization, evidence, release, governance]
notes:
  - "v0.2 preserves the source-module boundary from v0.1 and adds a commit-pinned repository evidence snapshot, bounded-context vocabulary, current scaffold inventory, catalog-matrix conflict analysis, interface contracts, admission sequence, validation matrix, safe-change guidance, rollback, and evidence ledger."
  - "Remote repository evidence was inspected on main at commit 5049e03434f9b6880464605a5eb31c843bb7e450."
  - "packages/catalog/pyproject.toml exists as a greenfield Python placeholder with project name kfm-catalog and version 0.0.0."
  - "packages/catalog/src/catalog/__init__.py exists and is empty; exact checks for stac.py, dcat.py, and prov.py returned no file."
  - "The global CatalogMatrix semantic contract and placeholder schema exist under contracts/data and schemas/contracts/v1/data; the schema is intentionally permissive and only requires id."
  - "The schema-declared validator path tools/validators/data/validate_catalog_matrix.py was not found, while tools/validators/validate_catalog_matrix.py exists as a NotImplementedError stub. This README records the mismatch but does not resolve it."
  - "ADR-0011 and ADR-0022 remain proposed and express different CatalogMatrix placement/closure emphases. This README does not promote either proposal to accepted authority."
  - "No implemented catalog helper modules, package exports, package build backend, package-specific tests, package fixtures, CI result, lifecycle writes, or runtime behavior is claimed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Source Module

> Python package-source lane for reusable catalog construction, reference-preservation, validation-adapter, and deterministic-serialization helpers. The current repository surface is a **scaffold**, not an implemented catalog library: the package metadata is a greenfield placeholder, `__init__.py` is empty, and the proposed STAC/DCAT/PROV modules were not found at their exact paths.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-packages%2Fcatalog%2Fsrc%2Fcatalog%2F-0a7ea4)
![runtime](https://img.shields.io/badge/runtime-Python%20scaffold-3776ab)
![implementation](https://img.shields.io/badge/helpers-NOT%20IMPLEMENTED-yellow)
![catalog](https://img.shields.io/badge/catalog-carrier%20not%20truth-d62728)
![authority](https://img.shields.io/badge/authority-shared%20module-0a7ea4)

> [!IMPORTANT]
> **Document status:** draft  
> **Repository evidence snapshot:** `main` at `5049e03434f9b6880464605a5eb31c843bb7e450`  
> **Parent package:** `packages/catalog/`  
> **Confirmed scaffold:** `packages/catalog/pyproject.toml` and empty `packages/catalog/src/catalog/__init__.py`  
> **Current helper implementation:** not observed at the tested module paths  
> **Authority boundary:** this module is not catalog data, proof, policy, release, schema, contract, source-registry, pipeline, or public API authority  
> **Public posture:** catalog helpers may shape candidates, but only governed release processes and interfaces may expose released public-safe catalog projections

> [!CAUTION]
> A catalog record is a discovery and interchange carrier. It is not an `EvidenceBundle`, a proof pack, a receipt, a policy decision, a release manifest, a publication decision, or permission to expose sensitive material.

---

## Quick jump

- [1. Purpose and audience](#1-purpose-and-audience)
- [2. Current repository state](#2-current-repository-state)
- [3. Bounded context and ubiquitous language](#3-bounded-context-and-ubiquitous-language)
- [4. Placement and authority](#4-placement-and-authority)
- [5. Owned responsibilities](#5-owned-responsibilities)
- [6. Explicit non-ownership](#6-explicit-non-ownership)
- [7. Inputs, outputs, and interfaces](#7-inputs-outputs-and-interfaces)
- [8. STAC, DCAT, and PROV dispatch](#8-stac-dcat-and-prov-dispatch)
- [9. CatalogMatrix alignment and unresolved drift](#9-catalogmatrix-alignment-and-unresolved-drift)
- [10. Determinism, identity, and temporal handling](#10-determinism-identity-and-temporal-handling)
- [11. Side effects and lifecycle safety](#11-side-effects-and-lifecycle-safety)
- [12. Directory contract](#12-directory-contract)
- [13. Implementation admission sequence](#13-implementation-admission-sequence)
- [14. Validation and test strategy](#14-validation-and-test-strategy)
- [15. Security, rights, sensitivity, and public safety](#15-security-rights-sensitivity-and-public-safety)
- [16. Compatibility, correction, and rollback](#16-compatibility-correction-and-rollback)
- [17. Definition of done](#17-definition-of-done)
- [18. Open verification register](#18-open-verification-register)
- [19. Evidence ledger](#19-evidence-ledger)
- [20. Maintainer checklist](#20-maintainer-checklist)

---

## 1. Purpose and audience

`packages/catalog/src/catalog/` is the internal Python module lane for reusable catalog support inside `packages/catalog/`.

A mature implementation may provide pure or side-effect-minimal helpers for:

- constructing STAC Item, Collection, Catalog, Asset, and Link fragments from already-authorized inputs;
- constructing DCAT Dataset, Distribution, DataService, and Catalog fragments;
- preserving PROV-O and PAV relations without predicate renaming;
- assembling cross-standard catalog-matrix projections;
- preserving `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, receipt, policy, review, release, correction, and rollback references;
- deterministic identifier, canonical serialization, and digest helpers;
- schema-bound validation adapters and safe validation results;
- compatibility adapters for explicitly versioned catalog-profile migrations;
- deterministic no-network test builders that cannot be mistaken for production records.

The module must remain **reusable package code**, not executable lifecycle orchestration. Pipeline runs, authorized writes, receipts, release decisions, and public serving belong to their owning responsibility roots.

**Primary audience**

- catalog package maintainers;
- catalog-pipeline maintainers;
- standards, contract, schema, evidence, policy, and release stewards;
- domain-lane developers building catalog candidates;
- validator and fixture maintainers;
- security and sensitivity reviewers;
- reviewers deciding whether proposed code belongs in a shared package or an executable pipeline.

[Back to top](#top)

---

## 2. Current repository state

This section separates current repository evidence from proposed future implementation.

| Surface | Evidence at inspected ref | Status | Consequence |
|---|---|---|---|
| `packages/catalog/src/catalog/README.md` | Existing v0.1 README was read from `main`. | **CONFIRMED** | This revision updates the source-module contract in place. |
| [`packages/catalog/README.md`](../../README.md) | Parent package README defines shared catalog support subordinate to pipelines, lifecycle data, evidence, policy, and release roots. | **CONFIRMED** | Module rules must remain consistent with the parent package. |
| [`packages/catalog/src/README.md`](../README.md) | Source-root README identifies `src/catalog/` as the current child module. | **CONFIRMED** | This module refines, but must not contradict, the source-root boundary. |
| [`packages/catalog/pyproject.toml`](../../pyproject.toml) | Contains only `[project]`, `name = "kfm-catalog"`, and `version = "0.0.0"`. | **CONFIRMED greenfield placeholder** | Python intent is visible, but build backend, dependencies, package discovery, entry points, and publishability are not established. |
| [`packages/catalog/src/catalog/__init__.py`](__init__.py) | File exists and is empty. | **CONFIRMED scaffold** | No exports, public API, module version, or initialization behavior is established. |
| `packages/catalog/package.json` | Exact path returned no file. | **CONFIRMED absent at tested path** | Do not claim a JavaScript/TypeScript package. |
| `packages/catalog/src/catalog/stac.py` | Exact path returned no file. | **CONFIRMED absent at tested path** | STAC helper implementation is not established. |
| `packages/catalog/src/catalog/dcat.py` | Exact path returned no file. | **CONFIRMED absent at tested path** | DCAT helper implementation is not established. |
| `packages/catalog/src/catalog/prov.py` | Exact path returned no file. | **CONFIRMED absent at tested path** | PROV/PAV helper implementation is not established. |
| Package-local source search | Indexed search returned the source-root and module READMEs; empty or unindexed files require exact checks. | **CONFIRMED search result / incomplete tree proof** | Additional files cannot be categorically excluded without a recursive tree listing. |
| `tests/packages/catalog/README.md` | Exact path returned no file. | **CONFIRMED absent at tested path** | No package-test lane is documented at the expected path. |
| `fixtures/packages/catalog/README.md` | Exact path returned no file. | **CONFIRMED absent at tested path** | No package-fixture lane is documented at the expected path. |
| [`contracts/data/catalog_matrix.md`](../../../../contracts/data/catalog_matrix.md) | Semantic contract exists and explicitly calls the paired schema a placeholder. | **CONFIRMED contract** | Helpers must follow contract meaning without pretending the schema is complete. |
| [`schemas/contracts/v1/data/catalog_matrix.schema.json`](../../../../schemas/contracts/v1/data/catalog_matrix.schema.json) | Schema exists, requires only `id`, and allows additional properties. | **CONFIRMED placeholder schema / status PROPOSED** | Passing this schema is not proof of catalog closure or complete semantics. |
| [`tools/validators/validate_catalog_matrix.py`](../../../../tools/validators/validate_catalog_matrix.py) | File exists and raises `NotImplementedError("Greenfield placeholder")`. | **CONFIRMED stub** | No working repo-wide CatalogMatrix validator is established. |
| `tools/validators/data/validate_catalog_matrix.py` | Schema-declared validator path returned no file. | **CONFIRMED absent at tested path** | Validator metadata and repository path are out of alignment. |
| [`tools/validators/catalog/README.md`](../../../../tools/validators/catalog/README.md) | Proposed catalog-validator lane README exists; it does not confirm executables. | **CONFIRMED README / implementation proposed** | Package validation adapters must not imply validator maturity. |
| [`pipelines/catalog/README.md`](../../../../pipelines/catalog/README.md) | Executable catalog-pipeline boundary README exists. | **CONFIRMED README / execution depth unknown** | Authorized writes and lifecycle transitions remain outside this module. |
| [`data/catalog/README.md`](../../../../data/catalog/README.md) | Catalog-stage lifecycle README exists and marks catalog records release-gated carriers. | **CONFIRMED README** | Package source must not write there as an implicit side effect. |
| [ADR-0011](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | Proposed ADR separates receipts, proofs, catalog, and publication and places CatalogMatrix on the proof side. | **CONFIRMED document / PROPOSED decision** | Do not treat its proposed placement as accepted without ADR resolution. |
| [ADR-0022](../../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | Proposed ADR requires release-level STAC/DCAT/PROV agreement and names a different proposed schema/validator family. | **CONFIRMED document / PROPOSED decision** | Current authority and placement remain conflicted and need reconciliation. |

### Evidence boundary

The repository connector did not provide a complete recursive tree listing for this module. Exact-file checks and indexed search support the current snapshot, but unindexed files remain possible.

```text
Python package placeholder        = CONFIRMED
empty package initializer         = CONFIRMED
implemented STAC helper           = NOT OBSERVED
implemented DCAT helper           = NOT OBSERVED
implemented PROV/PAV helper       = NOT OBSERVED
public exports                    = UNKNOWN
build backend                     = UNKNOWN
dependencies                      = UNKNOWN
package-specific tests            = NOT OBSERVED
package-specific fixtures         = NOT OBSERVED
working CatalogMatrix validator   = NOT ESTABLISHED
catalog pipeline runtime          = UNKNOWN
catalog write behavior            = UNKNOWN
CI pass state                     = UNKNOWN
```

[Back to top](#top)

---

## 3. Bounded context and ubiquitous language

### Bounded context

Within KFM, `packages/catalog/src/catalog/` means:

> Reusable, non-deployable Python helpers that construct, normalize, serialize, validate, or translate catalog-shaped objects from already-governed inputs without owning lifecycle writes, evidence closure, policy decisions, release approval, or public exposure.

It does not mean:

- a catalog server;
- a STAC API;
- a pipeline runner;
- a data writer;
- a proof builder;
- a source registry;
- an RDF/graph authority;
- a release service;
- a public-client trust membrane.

### Ubiquitous language

| Term | Meaning in this module |
|---|---|
| **Catalog candidate** | A not-yet-public catalog-shaped object prepared for validation and release review. |
| **Catalog record** | STAC, DCAT, PROV, or KFM domain catalog metadata stored in the catalog lifecycle lane. |
| **Catalog carrier** | Discovery/interchange metadata that points to evidence, source, policy, and release state without replacing them. |
| **STAC object** | A STAC Catalog, Collection, Item, Asset, or Link structure for spatiotemporal discovery. |
| **DCAT object** | A DCAT Catalog, Dataset, Distribution, or DataService structure for dataset/distribution discovery. |
| **PROV fragment** | PROV-O/PAV entities, activities, agents, and relations preserving lineage; not full proof closure by itself. |
| **CatalogMatrix** | A governed crosswalk or relationship descriptor. Its final release-level meaning and canonical placement remain under proposed-ADR reconciliation. |
| **EvidenceRef** | A resolvable pointer carried by metadata; not evidence closure by itself. |
| **EvidenceBundle** | Admissible evidence support owned outside this package. |
| **Receipt reference** | Pointer to process memory; not proof or release approval. |
| **Release reference** | Pointer to release state; not the release decision itself. |
| **Canonical serialization** | Deterministic byte representation defined by an accepted specification, not ad hoc key sorting. |
| **Validation adapter** | Package helper that invokes or normalizes a validator result without becoming validation authority. |
| **Writer** | Code that mutates lifecycle or release state. Writers do not belong in this module unless placement is changed through reviewed architecture. |

[Back to top](#top)

---

## 4. Placement and authority

Directory Rules place reusable implementation libraries under `packages/`. The `src/catalog/` path is appropriate only as a source module within the Python package scaffold.

| Question | Answer | Status |
|---|---|---|
| Why `packages/`? | It owns shared reusable implementation libraries. | **CONFIRMED root contract** |
| Why `packages/catalog/`? | Catalog helpers may be reused by pipelines, tools, tests, and apps without becoming executable catalog orchestration. | **CONFIRMED parent README / implementation bounded** |
| Why `src/catalog/`? | The Python package scaffold uses a `src` layout and contains an empty `catalog` package initializer. | **CONFIRMED scaffold** |
| Is this executable catalog logic? | No. Executable catalog transitions belong under `pipelines/catalog/` or accepted domain pipeline lanes. | **CONFIRMED boundary** |
| Is this catalog storage? | No. Catalog records belong under `data/catalog/`; triplet/graph projections belong under `data/triplets/`. | **CONFIRMED lifecycle split** |
| Is this proof storage? | No. Evidence and proof artifacts belong under `data/proofs/`. | **CONFIRMED authority split** |
| May this module define object meaning? | No. Contract authority remains under `contracts/`. | **CONFIRMED authority split** |
| May this module define canonical machine shape? | No. Schema authority remains under `schemas/contracts/v1/`. | **CONFIRMED authority split** |
| May this module decide policy? | No. It may preserve policy refs and obligations only. | **CONFIRMED authority split** |
| May this module approve release? | No. It may preserve release/correction/rollback refs only. | **CONFIRMED release separation** |
| May this module publish or grant public access? | No. Public access is release- and policy-gated through governed interfaces. | **CONFIRMED trust posture** |

> [!IMPORTANT]
> Package code can make catalog construction consistent. It cannot make catalog metadata true, admissible, released, public, or safe.

[Back to top](#top)

---

## 5. Owned responsibilities

A future implementation may own reusable behavior in these narrow categories.

### 5.1 Pure construction

- assemble standard-shaped objects from explicit input mappings;
- reject incomplete required inputs rather than inventing values;
- preserve caller-supplied source/evidence/policy/release refs;
- return objects or typed validation results without writing them.

### 5.2 Standards dispatch

- select STAC, DCAT, PROV/PAV, or combined catalog projections from an explicit asset/dataset profile;
- preserve standards-native field names and predicates;
- keep KFM extensions namespaced and versioned;
- expose dispatch decisions for review and testing.

### 5.3 Reference preservation

- preserve identifiers and digests across catalog projections;
- preserve evidence, source, receipt, policy, review, release, correction, withdrawal, and rollback refs;
- distinguish unresolved refs from resolved objects;
- prevent helpers from silently dropping obligations.

### 5.4 Deterministic helpers

- stable identifier derivation under an accepted identity specification;
- canonical serialization under an accepted format and version;
- digest calculation over declared bytes;
- normalized comparison helpers for closure checks;
- explicit version and profile metadata.

### 5.5 Validation adaptation

- invoke an existing validator through a narrow adapter;
- normalize results into a documented, finite result type;
- preserve all failures and warnings;
- avoid turning a schema pass into evidence, policy, or release approval.

### 5.6 Compatibility

- translate explicitly versioned legacy catalog shapes;
- record deprecated fields and migration warnings;
- preserve original identifiers and correction lineage;
- include a removal condition and rollback path.

[Back to top](#top)

---

## 6. Explicit non-ownership

| Concern | Correct owner |
|---|---|
| Catalog pipeline orchestration | `pipelines/catalog/` or accepted domain pipeline lanes |
| Pipeline specifications | `pipeline_specs/` |
| Catalog-stage records | `data/catalog/` |
| Triplet/graph projections | `data/triplets/` |
| Process receipts | `data/receipts/` |
| EvidenceBundles and proof packs | `data/proofs/` |
| Source descriptors | `data/registry/sources/` or accepted registry home |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/contracts/v1/` |
| Policy evaluation | `policy/` and accepted policy runtime |
| Promotion and release decisions | `release/` |
| Correction, withdrawal, and rollback authority | `release/` and their contract families |
| Public API routes | `apps/governed-api/` |
| Public catalog rendering | governed UI/app surfaces |
| Repo-wide validators | `tools/validators/` |
| Package tests | `tests/packages/catalog/` if adopted |
| Package fixtures | `fixtures/packages/catalog/` if adopted |
| Secrets, credentials, private source tokens | approved secret management, never source code |
| Generated summaries as truth | governed interpretive surfaces with evidence and receipts |

### Forbidden collapses

```text
catalog helper        -> lifecycle writer
schema pass           -> evidence closure
catalog metadata      -> source truth
STAC item             -> release approval
DCAT distribution     -> permission to publish
PROV fragment         -> complete proof pack
CatalogMatrix         -> automatic release
receipt reference     -> proof
release reference     -> release decision
fixture               -> production catalog
empty __init__.py     -> implemented package
pyproject placeholder -> installable production library
```

[Back to top](#top)

---

## 7. Inputs, outputs, and interfaces

### 7.1 Accepted inputs

Inputs should be explicit, already-governed values or deterministic synthetic fixtures.

| Input family | Examples | Required posture |
|---|---|---|
| Identity | canonical ID, source ID, dataset/version ID, asset ID, spec hash | Stable, versioned, non-secret |
| Spatial/temporal metadata | geometry/bbox, valid time, observed time, source time, retrieval time | Source and time semantics explicit |
| Asset/distribution metadata | media type, roles, href/ref, digest, byte size, title | Rights and release posture preserved |
| Source state | SourceDescriptor ref, authority role, license/rights, attribution, cadence | Must not be inferred from filename or URL |
| Evidence state | EvidenceRef/EvidenceBundle ref, proof-pack ref, validation-report ref | Refs preserved; resolution not assumed |
| Policy state | sensitivity, rights, access, embargo, redaction/generalization obligations | Policy-derived, not client-overridden |
| Release state | release candidate/ref, ReleaseManifest ref, correction/withdrawal/rollback refs | Required for released/public assertions |
| Provenance state | PROV/PAV relations, run/receipt refs, agents, activities, derived-from refs | Predicate names preserved |
| Profile state | STAC/DCAT/PROV profile/version, KFM extension version | Explicit and testable |
| Synthetic fixture | deterministic test object | Clearly synthetic and non-authoritative |

### 7.2 Bounded outputs

The module may return in-memory or serialized candidate objects and validation results.

| Output | Allowed? | Rule |
|---|---:|---|
| STAC-shaped candidate | Yes | Not public or released by package action alone |
| DCAT-shaped candidate | Yes | Must remain a carrier |
| PROV/PAV fragment | Yes | Must preserve standard predicates |
| CatalogMatrix candidate | Conditional | Must identify contract/profile and unresolved authority state |
| Deterministic serialization bytes | Yes | Algorithm and version must be explicit |
| Digest/result object | Yes | Digest input and algorithm must be recorded |
| Validation result | Yes | Must not imply evidence/policy/release success |
| Compatibility warning | Yes | Must name deprecated field/profile and retirement path |
| Catalog lifecycle write | No | Executable pipeline responsibility |
| Release or publication result | No | Release authority responsibility |

### 7.3 Interface rule

```text
authorized pipeline / tool / test
  -> explicit governed inputs
  -> packages.catalog helper
  -> candidate object + validation/digest metadata
  -> caller-owned validation and policy gates
  -> authorized pipeline writer
  -> catalog-stage record + receipt
  -> release review
  -> governed public projection
```

The module interface should make hidden IO difficult. Prefer value-in/value-out functions and immutable or copy-on-write data structures where practical.

[Back to top](#top)

---

## 8. STAC, DCAT, and PROV dispatch

The standards documents exist, but they are draft adoption references and contain open implementation items. This module must consume accepted profiles rather than inventing them.

### 8.1 Dispatch posture

| Catalog family | Primary use | Module obligation | Must not do |
|---|---|---|---|
| STAC | Spatiotemporal assets and collections | Preserve STAC core structure, assets, links, geometry/time, roles, and namespaced KFM refs | Treat a STAC Item as evidence or release approval |
| DCAT | Dataset/distribution discovery and interoperability | Preserve DCAT v3 classes/properties, distributions, rights, conforms-to, provenance, and KFM refs | Treat a DCAT Dataset as source truth |
| PROV-O/PAV | Activity/entity/agent lineage and authoring/versioning | Preserve standard predicates, qualified relations, agents, activities, entities, and derivation links | Rename predicates or claim complete proof closure |
| Combined matrix | Cross-standard agreement/review | Compare identity, digest, release ref, evidence refs, source refs, and profile versions | Resolve proposed ADR conflicts silently |

### 8.2 No-fork rule

Helpers must:

- extend standards through accepted namespaces;
- avoid free-form top-level STAC fields where profiles require namespaced properties;
- avoid renamed DCAT/PROV predicates;
- retain unknown standards-compliant fields unless an accepted normalization contract explicitly excludes them;
- produce reviewable warnings for unsupported profile versions;
- fail closed or abstain when dispatch cannot be determined safely.

### 8.3 Standards drift

Version-sensitive claims in the standards docs must be rechecked before implementation or dependency pinning. This README confirms repository document presence, not current external-standard versions.

[Back to top](#top)

---

## 9. CatalogMatrix alignment and unresolved drift

`CatalogMatrix` is currently the most important unresolved authority surface for this module.

### 9.1 Confirmed repository facts

- `contracts/data/catalog_matrix.md` exists and defines semantic meaning.
- `schemas/contracts/v1/data/catalog_matrix.schema.json` exists as a greenfield placeholder.
- The schema only requires `id`; `version` and `spec_hash` are optional strings; additional properties are allowed.
- The schema metadata names `tools/validators/data/validate_catalog_matrix.py`.
- That exact validator path was not found.
- `tools/validators/validate_catalog_matrix.py` exists but only raises `NotImplementedError`.
- multiple domain-specific `catalog_matrix.schema.json` files and validator stubs are indexed elsewhere in the repository.
- ADR-0011 and ADR-0022 are both proposed, not accepted.

### 9.2 Conflict surface

| Source | Current emphasis | Status |
|---|---|---|
| Existing contract/schema pair | Generic `CatalogMatrix` under the `data` contract/schema family | **CONFIRMED files; schema placeholder** |
| ADR-0011 | `CatalogMatrix` is a proof-side closure object, canonically under `data/proofs/catalog_matrix/` once accepted | **PROPOSED decision** |
| ADR-0022 | Release-level STAC/DCAT/PROV agreement matrix with proposed catalog-family schema and validator paths | **PROPOSED decision** |
| `pipelines/catalog/README.md` | Catalog matrix/closure report may go to catalog or proofs “per schema decision” | **CONFIRMED documentation of unresolved decision** |
| Validator metadata | Schema points to missing `tools/validators/data/...`; root stub exists elsewhere | **CONFIRMED path mismatch** |

### 9.3 Module rule while unresolved

Until the ADR and path conflicts are resolved, code in this module must not:

- hard-code one canonical `CatalogMatrix` instance home;
- treat the permissive placeholder schema as release-grade closure;
- create a second competing schema or contract;
- embed a release decision in a catalog matrix;
- rename or duplicate the validator entrypoint silently;
- describe `CatalogMatrix` as implemented release enforcement.

A future helper may accept a matrix profile/config explicitly and return a candidate object, but it must expose the contract/schema/profile identifier and validation status.

### 9.4 Required resolution before production implementation

1. Decide whether generic matrix semantics and release-level closure are one object family or two related families.
2. Reconcile `contracts/data` / `schemas/contracts/v1/data` with ADR-0022’s proposed catalog-family paths.
3. Resolve proof-side instance placement versus catalog-stage candidate placement.
4. choose one validator entrypoint and update schema metadata, tests, docs, and drift register together.
5. strengthen schema fields and fixtures before using matrix validation as a release gate.
6. define finite closure outcomes and reason codes.
7. document migration and rollback for any renamed paths or object families.

[Back to top](#top)

---

## 10. Determinism, identity, and temporal handling

### 10.1 Identity

A helper must not invent identifiers from display labels alone.

Identifier derivation should be controlled by an accepted identity specification and should record:

- namespace/profile;
- object family;
- source or dataset identity where applicable;
- version;
- temporal scope where identity depends on time;
- canonicalization algorithm/version;
- digest algorithm;
- inputs included and excluded.

### 10.2 Serialization and hashing

Determinism requires more than `sort_keys=True`.

A production serialization helper should define:

- encoding;
- Unicode normalization;
- number representation;
- date/time normalization;
- key ordering;
- array-order semantics;
- geometry coordinate precision where applicable;
- JSON-LD/RDF canonicalization posture where applicable;
- digest algorithm and prefix;
- profile and serializer version.

A digest proves byte identity, not truth, admissibility, release, or public safety.

### 10.3 Time kinds

Catalog helpers should preserve distinct time meanings when supplied:

| Time kind | Example |
|---|---|
| valid time | period the observation or assertion applies |
| observed time | when an observation occurred |
| source time | timestamp/version supplied by source |
| retrieval time | when KFM acquired the source |
| processing time | when a transform ran |
| catalog time | when a catalog candidate/record was built |
| release time | when an approved release became effective |
| correction time | when a correction, withdrawal, or supersession took effect |

Helpers must not rewrite stale source or observation times to the current build time.

[Back to top](#top)

---

## 11. Side effects and lifecycle safety

### 11.1 Default rule

This module should be pure or side-effect-minimal.

```text
input values -> validation/normalization/construction -> returned values
```

### 11.2 Forbidden hidden side effects

Package helpers must not silently:

- read from RAW, WORK, QUARANTINE, or canonical internal stores;
- write `data/catalog/`, `data/triplets/`, `data/proofs/`, `data/receipts/`, `data/published/`, or `release/`;
- perform network requests;
- fetch source descriptors;
- resolve credentials;
- call model runtimes;
- mutate source inputs;
- approve policy, review, promotion, or release;
- suppress validation failures;
- expose restricted fields through logging.

### 11.3 If IO is ever required

IO must be owned by a reviewed executable surface. A future architecture may define ports/interfaces in this package, but concrete adapters and writers should live under the responsible pipeline, tool, app, or runtime root.

Any approved IO path requires:

- explicit capability and least-privilege scope;
- configuration and secret separation;
- deterministic or idempotent behavior where practical;
- dry-run support;
- receipts and audit references;
- failure disposition;
- tests for no-public-bypass;
- rollback and correction behavior.

[Back to top](#top)

---

## 12. Directory contract

### 12.1 Confirmed current scaffold

```text
packages/catalog/
├── README.md
├── pyproject.toml             # greenfield placeholder: name/version only
└── src/
    ├── README.md
    └── catalog/
        ├── README.md
        └── __init__.py        # empty
```

This is a bounded confirmed view, not a complete recursive-tree assertion.

### 12.2 Proposed future module layout

```text
packages/catalog/
├── pyproject.toml
└── src/
    └── catalog/
        ├── __init__.py
        ├── models.py
        ├── errors.py
        ├── identity.py
        ├── serialization.py
        ├── refs.py
        ├── validation.py
        ├── stac/
        │   ├── __init__.py
        │   ├── builders.py
        │   └── profiles.py
        ├── dcat/
        │   ├── __init__.py
        │   ├── builders.py
        │   └── profiles.py
        ├── prov/
        │   ├── __init__.py
        │   ├── builders.py
        │   └── mapping.py
        └── matrix/
            ├── __init__.py
            ├── builders.py
            └── comparison.py
```

All future paths are **PROPOSED**. Do not create them merely to match this diagram. Add only the smallest module required by an accepted use case and test.

### 12.3 Placement checks for every new source file

A proposed file must answer:

1. Is it reusable package code rather than executable orchestration?
2. Does it avoid lifecycle writes and network access?
3. Which contract and schema constrain it?
4. Which accepted standard/profile constrains it?
5. Which package API exports it?
6. Which tests and fixtures prove behavior?
7. Which evidence/policy/release refs must it preserve?
8. What is the compatibility and rollback plan?
9. Does it create a parallel authority or validator path?
10. Does it require an ADR or drift-register update?

[Back to top](#top)

---

## 13. Implementation admission sequence

The safest first implementation is narrower than a full STAC/DCAT/PROV catalog library.

### Stage 0 — Reconcile authority

- resolve or explicitly track the `CatalogMatrix` contract/schema/validator drift;
- identify accepted STAC/DCAT/PROV profiles and namespace versions;
- assign package ownership;
- choose the package build backend and test tooling.

**Exit condition:** one reviewed package contract and no silent parallel authority.

### Stage 1 — Make the Python scaffold testable

- add a build-system configuration and package discovery only if repository conventions support it;
- add an explicit package version strategy;
- keep `__init__.py` exports empty or minimal;
- add package import and boundary tests.

**Exit condition:** deterministic install/import in the supported development environment.

### Stage 2 — Implement one pure helper

Recommended first slice:

```text
explicit metadata mapping
  -> pure candidate builder
  -> deterministic serialization
  -> schema/profile validation result
  -> no IO
```

Choose one narrowly scoped object, such as a minimal STAC Asset/Link fragment or a catalog-reference bundle, rather than a release-level `CatalogMatrix`.

**Exit condition:** positive, negative, determinism, and no-side-effect tests pass.

### Stage 3 — Add standards/profile adapters

- add STAC/DCAT/PROV adapters one at a time;
- preserve fields and refs losslessly;
- add cross-standard fixture comparisons;
- pin profile/version inputs.

**Exit condition:** round-trip and unknown-field preservation are demonstrated.

### Stage 4 — Integrate with an executable pipeline

- pipeline owns reads, writes, policy checks, receipts, and failure disposition;
- package returns values only;
- pipeline tests prove no hidden write path.

**Exit condition:** fixture-only end-to-end catalog candidate build with receipt and validation report.

### Stage 5 — Release-level closure

Only after ADR/schema/validator reconciliation:

- implement release-level agreement checks;
- emit proof-side closure artifacts where accepted;
- integrate policy and release gates;
- test correction, withdrawal, supersession, and rollback.

**Exit condition:** deterministic finite outcome with inspectable failures and no public bypass.

[Back to top](#top)

---

## 14. Validation and test strategy

### 14.1 Current state

| Validation surface | Current evidence | Status |
|---|---|---|
| Package import test | Not observed | **NOT OBSERVED** |
| Package helper tests | Not observed | **NOT OBSERVED** |
| Package fixtures | Not observed | **NOT OBSERVED** |
| Generic CatalogMatrix schema | Exists but permissive placeholder | **CONFIRMED / insufficient for closure** |
| Schema-declared validator | Missing at named path | **CONFIRMED mismatch** |
| Root CatalogMatrix validator | Exists as `NotImplementedError` stub | **CONFIRMED stub** |
| Catalog validator lane | README only | **CONFIRMED docs / executable unknown** |
| Domain catalog-matrix schemas/validators | Multiple indexed files exist | **CONFIRMED file presence for indexed examples / maturity varies** |
| Repository-native test execution | Not performed in this documentation update | **NOT RUN** |

### 14.2 Required package tests before implementation claims

```text
tests/packages/catalog/
├── README.md
├── test_import.py
├── test_no_hidden_io.py
├── test_no_network.py
├── test_no_lifecycle_writes.py
├── test_unknown_fields_preserved.py
├── test_stable_serialization.py
├── test_digest_reproducibility.py
├── test_refs_preserved.py
├── test_validation_result_does_not_imply_release.py
├── test_stac_builder.py
├── test_dcat_builder.py
├── test_prov_mapping.py
└── test_catalog_matrix_profile_dispatch.py
```

Proposed fixture layout:

```text
fixtures/packages/catalog/
├── valid/
├── invalid/
├── round_trip/
├── determinism/
├── unknown_fields/
├── restricted_metadata/
└── conflict/
```

These paths are **PROPOSED** until adopted.

### 14.3 Minimum negative cases

- missing canonical identifier;
- unsupported profile version;
- invalid or missing digest;
- conflicting identity across STAC/DCAT/PROV;
- missing source descriptor ref;
- missing evidence ref for claim-bearing metadata;
- release assertion without release ref;
- restricted field present without policy obligation;
- PROV predicate rename;
- hidden filesystem/network access;
- catalog candidate passed off as public/released;
- schema pass interpreted as evidence or release approval;
- unknown fields silently dropped;
- temporal fields collapsed or rewritten.

### 14.4 Validation commands to run after implementation exists

```bash
python -m pytest -q tests/packages/catalog
python -m pytest -q tests/validators/catalog
python tools/validators/validate_catalog_matrix.py
```

The current root validator command is expected to raise `NotImplementedError`; it is not a passing validation path today.

[Back to top](#top)

---

## 15. Security, rights, sensitivity, and public safety

Catalog metadata can expose sensitive information even when the underlying asset is protected.

### 15.1 Sensitive metadata examples

- exact archaeology or cultural-site coordinates;
- rare-species or rare-plant locations;
- living-person or DNA-linked metadata;
- private landownership joins;
- critical infrastructure locations or vulnerabilities;
- restricted source URLs, object-store keys, signed URLs, or internal paths;
- embargoed dataset names or collection membership;
- source credentials, tokens, query strings, or access headers;
- internal policy reasons that reveal protected facts.

### 15.2 Module obligations

Helpers must:

- accept policy/redaction obligations as explicit input where material;
- omit or generalize fields only under an accepted transform/profile;
- preserve a redaction/generalization indicator and transform receipt ref;
- avoid logging full payloads by default;
- sanitize safe validation errors;
- never embed credentials or temporary access tokens;
- avoid resolving URLs or following links;
- preserve rights, license, attribution, and embargo metadata;
- fail closed when a public-safe projection cannot be determined.

### 15.3 Public boundary

```text
package candidate != public record
catalog-stage record != released record
released record != unrestricted record
```

Public clients must receive release-aware, policy-safe projections through governed interfaces. Directory placement alone is never publication permission.

[Back to top](#top)

---

## 16. Compatibility, correction, and rollback

### 16.1 Compatibility rules

A compatibility adapter must specify:

- source profile/version;
- target profile/version;
- fields renamed, transformed, defaulted, or removed;
- information-loss status;
- warnings and obligations;
- test fixtures;
- deprecation date or removal condition;
- correction/rollback behavior.

Silent coercion is forbidden.

### 16.2 Correction and supersession

Catalog metadata changes after publication must preserve:

- prior identifier and release references;
- correction or supersession notice refs;
- changed-field summary;
- effective correction time;
- new digest and profile version;
- rollback target;
- public-safe status.

The package may shape correction metadata but cannot authorize correction or withdrawal.

### 16.3 Rollback triggers

Rollback or block the change if it:

- introduces hidden lifecycle or release writes;
- adds network/source access to a pure helper path;
- creates parallel contract, schema, validator, policy, proof, or release authority;
- weakens catalog/evidence/release separation;
- drops source/evidence/policy/release/correction refs;
- makes serialization nondeterministic without an explicit reason;
- exposes restricted metadata;
- treats schema validity as truth or publication;
- adds a compatibility adapter without a retirement path;
- changes public exports without versioning and consumer review.

### 16.4 Documentation rollback

This README-only update can be reverted to the prior blob if its evidence snapshot or boundary guidance is found incorrect. Future implementation rollback must revert code, exports, fixtures, and dependent callers as one reviewed change.

[Back to top](#top)

---

## 17. Definition of done

### README v0.2

This README is complete for the current documentation task when it:

- preserves the parent package and source-root boundaries;
- records the Python placeholder and empty initializer accurately;
- does not claim STAC/DCAT/PROV helper implementation;
- identifies the current CatalogMatrix contract/schema/validator state;
- surfaces the validator path mismatch and proposed-ADR conflict;
- separates package helpers from lifecycle writes, proof, policy, release, and public serving;
- defines bounded inputs, outputs, standards dispatch, determinism, security, tests, safe change, and rollback;
- uses explicit truth labels for incomplete evidence.

### Future module implementation

A source module is ready for production use only when:

- ownership is assigned;
- package build/import configuration is verified;
- contract, schema, standard profile, and identity rules are explicit;
- functions are pure or side effects are separately owned and reviewed;
- tests include positive, negative, determinism, unknown-field, sensitivity, and no-hidden-IO cases;
- package exports are versioned;
- validators are implemented and their paths agree with schema metadata;
- CatalogMatrix conflicts are resolved before closure logic is claimed;
- evidence, source, policy, review, release, correction, and rollback refs are preserved;
- CI results are observed;
- documentation and rollback instructions are updated.

[Back to top](#top)

---

## 18. Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `PKG-CATALOG-MOD-001` | Is the per-package `pyproject.toml` intended to become independently buildable, or is the root project the only build authority? | **NEEDS VERIFICATION** | Root packaging configuration, build workflow, maintainer decision |
| `PKG-CATALOG-MOD-002` | Which Python versions and dependencies are supported? | **UNKNOWN** | Package metadata and CI |
| `PKG-CATALOG-MOD-003` | Which public exports should `catalog.__init__` expose? | **UNKNOWN** | Consumer/use-case inventory |
| `PKG-CATALOG-MOD-004` | Which STAC profile and namespace version are accepted? | **NEEDS VERIFICATION** | Accepted standards/profile decision |
| `PKG-CATALOG-MOD-005` | Which DCAT profile/context and IRI base are accepted? | **NEEDS VERIFICATION** | Accepted standards/profile decision |
| `PKG-CATALOG-MOD-006` | Which PROV/PAV canonicalization and round-trip rules are accepted? | **NEEDS VERIFICATION** | Standards/identity ADR and fixtures |
| `PKG-CATALOG-MOD-007` | Is generic `CatalogMatrix` the same family as release-level STAC/DCAT/PROV closure? | **CONFLICTED / NEEDS VERIFICATION** | ADR-0011/ADR-0022 reconciliation |
| `PKG-CATALOG-MOD-008` | Which contract/schema family is canonical for CatalogMatrix? | **CONFLICTED / NEEDS VERIFICATION** | ADR + migration note |
| `PKG-CATALOG-MOD-009` | Is CatalogMatrix a catalog-stage candidate, proof-side closure artifact, or two related object families? | **CONFLICTED / NEEDS VERIFICATION** | Object-family decision |
| `PKG-CATALOG-MOD-010` | Which validator path is canonical? | **CONFLICTED / NEEDS VERIFICATION** | Schema metadata update, drift resolution, tests |
| `PKG-CATALOG-MOD-011` | Which catalog helper should be the first implemented slice? | **PROPOSED** | Consumer-backed thin-slice decision |
| `PKG-CATALOG-MOD-012` | Where will package-specific tests and fixtures live? | **NEEDS VERIFICATION** | Test/fixture convention |
| `PKG-CATALOG-MOD-013` | Which workflows validate package boundaries and determinism? | **UNKNOWN** | Workflow inspection and successful runs |
| `PKG-CATALOG-MOD-014` | Are there unindexed source files or consumers not found by the connector search? | **UNKNOWN** | Recursive tree and import search |
| `PKG-CATALOG-MOD-015` | Who owns package review and CODEOWNERS coverage? | **UNKNOWN** | Ownership decision and CODEOWNERS update |
| `PKG-CATALOG-MOD-016` | Which source-rights and sensitivity profiles must builders preserve? | **NEEDS VERIFICATION** | Policy and source-registry contracts |
| `PKG-CATALOG-MOD-017` | What is the canonical serializer and digest grammar? | **NEEDS VERIFICATION / ADR** | Identity/canonicalization decision |
| `PKG-CATALOG-MOD-018` | How are corrections, withdrawals, and stale catalog records reflected across STAC/DCAT/PROV? | **NEEDS VERIFICATION** | Correction/release contracts and fixtures |

[Back to top](#top)

---

## 19. Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| This file at the inspected base | **CONFIRMED** | Existing v0.1 module-boundary documentation | Implemented helpers or runtime behavior |
| [`packages/catalog/pyproject.toml`](../../pyproject.toml) | **CONFIRMED** | Python project name `kfm-catalog`, version `0.0.0` | Build backend, dependencies, installability, maturity |
| [`__init__.py`](__init__.py) | **CONFIRMED empty** | Python package scaffold exists | Exports or implemented code |
| Exact missing `stac.py`, `dcat.py`, `prov.py` checks | **CONFIRMED absent at tested paths** | Those proposed flat module paths are not implemented | Absence of every possible helper filename |
| Parent package/source READMEs | **CONFIRMED** | Responsibility and anti-collapse boundaries | Runtime/package implementation |
| [`contracts/data/catalog_matrix.md`](../../../../contracts/data/catalog_matrix.md) | **CONFIRMED** | Current semantic contract and stated limitations | Accepted closure semantics |
| [`catalog_matrix.schema.json`](../../../../schemas/contracts/v1/data/catalog_matrix.schema.json) | **CONFIRMED placeholder** | Current machine shape and metadata | Release-grade validation |
| [`validate_catalog_matrix.py`](../../../../tools/validators/validate_catalog_matrix.py) | **CONFIRMED stub** | A root entrypoint filename exists | Working validator |
| Missing schema-declared validator path | **CONFIRMED absent at tested path** | Metadata/path mismatch | Intended final path |
| [`tools/validators/catalog/README.md`](../../../../tools/validators/catalog/README.md) | **CONFIRMED** | Proposed validator-lane boundary | Executable validators |
| [ADR-0011](../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | **CONFIRMED document / PROPOSED decision** | Artifact-family separation proposal | Accepted placement |
| [ADR-0022](../../../../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | **CONFIRMED document / PROPOSED decision** | Cross-standard agreement proposal | Implemented release gate |
| [STAC](../../../../docs/standards/STAC.md) | **CONFIRMED draft doc** | Repository adoption guidance | Current external version or implemented profile |
| [DCAT](../../../../docs/standards/DCAT.md) | **CONFIRMED draft doc** | Repository adoption guidance | Implemented context/schema |
| [PROV](../../../../docs/standards/PROV.md) | **CONFIRMED draft doc** | Repository provenance guidance | Implemented canonicalization/graph gate |
| [`pipelines/catalog/README.md`](../../../../pipelines/catalog/README.md) | **CONFIRMED README** | Executable/lifecycle boundary | Pipeline code or successful runs |
| [`data/catalog/README.md`](../../../../data/catalog/README.md) | **CONFIRMED README** | Catalog-stage lifecycle and release-gated posture | Concrete catalog inventory or public route enforcement |
| Repository search and exact fetches | **CONFIRMED bounded evidence** | Current indexed files and exact-path outcomes | Complete recursive tree |

[Back to top](#top)

---

## 20. Maintainer checklist

Before adding or changing source in this module:

- [ ] Confirm the change is reusable package code, not pipeline orchestration.
- [ ] Confirm the owning contract and schema.
- [ ] Confirm the external standard/profile/version.
- [ ] Confirm the code does not invent source, evidence, policy, review, or release state.
- [ ] Confirm no hidden filesystem, network, registry, database, graph, object-store, or model access.
- [ ] Confirm no lifecycle or release writes.
- [ ] Confirm deterministic identity and serialization rules where material.
- [ ] Confirm unknown standards-compliant fields are preserved or explicitly rejected.
- [ ] Confirm sensitive metadata and rights obligations are preserved.
- [ ] Confirm validation failures remain failures and are not coerced to success.
- [ ] Confirm schema validity is not described as evidence or release approval.
- [ ] Confirm package exports and compatibility are versioned.
- [ ] Confirm tests include negative, determinism, no-IO, and sensitivity cases.
- [ ] Confirm CatalogMatrix authority/path conflicts are not silently encoded.
- [ ] Confirm docs, drift register, ADRs, and rollback notes are updated when behavior changes.
- [ ] Confirm CI results before claiming readiness.

---

## Maintainer note

Keep this module small, deterministic, reviewable, and subordinate to KFM’s catalog lifecycle, evidence, policy, release, correction, and rollback controls.

The safest first code change is one pure helper with explicit inputs, no IO, a single accepted contract/profile, deterministic fixtures, and negative tests. Do not begin by implementing a release-level CatalogMatrix builder while its object-family, schema-home, instance-home, and validator-path decisions remain unresolved.
