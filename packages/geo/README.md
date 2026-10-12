<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-geo-readme
title: packages/geo/ — Governed Geo Shared Package
type: readme
version: v0.2
status: draft; repository-grounded; python-package-scaffold; implementation-placeholder; non-authoritative
owners:
  - OWNER_TBD — Geo package owner
  - OWNER_TBD — Spatial Foundation steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, sensitivity, and geoprivacy steward
  - OWNER_TBD — Map, release, correction, validator, security, packaging, and docs stewards
created: NEEDS VERIFICATION — target file existed before this revision
updated: 2026-07-15
supersedes: v1 planning-oriented package guide (2026-06-14)
policy_label: public; packages; geo; python; shared-library; CRS; geometry; scale; uncertainty; generalization; no-network-by-default; fail-closed; map-is-carrier; non-authoritative
path: packages/geo/README.md
truth_posture: CONFIRMED target and prior blob, kfm-geo 0.0.0 project metadata, Python src layout, merged source-root v0.2 contract, merged geo-module v0.2 contract, empty geo initializer, bounded absence of selected geo helper modules, package.json, CHANGELOG.md, py.typed, package-specific test/fixture READMEs, and dedicated geo.yml workflow, verified packages/maplibre helper lane, Directory Rules v1.4, Spatial Foundation doctrine/object-family guidance, current UI MapContextEnvelope schema location and empty permissive shape, three competing LayerManifest schema homes with an explicit data-contract conflict, empty permissive map/layers LayerManifest schemas, minimal data LayerManifest schema, empty permissive TileArtifactManifest schema, KFMGeoManifest contract plus minimal schema stub, and absent schema-declared KFMGeoManifest validator/fixture README at exact tested paths / PROPOSED future accepted package metadata, explicit package discovery, deliberate exports, profile-pinned pure geospatial primitive helpers, generated schema models, bounded transform-plan carriers, public-safe candidate assembly from supplied decisions, package tests, typed marker, and versioned distribution / CONFLICTED old package README paths versus current schema homes, LayerManifest schema-home split, rich Spatial Foundation and geo-manifest semantics versus permissive/minimal schemas, proposed helper outcomes versus no accepted geo-result contract, maplibre-runtime prose versus verified packages/maplibre lane, broad geo import name versus unverified compatibility posture, and public-safe helper ambitions versus policy authority / UNKNOWN build backend, Python requirement, dependency graph, package discovery, license metadata, public exports, consumers, canonical CRS/geometry/scale/uncertainty profiles, transform engine, validator integration, dedicated CI, package publication, runtime/API wiring, and production behavior / NEEDS VERIFICATION accepted owners, ADR/profile decisions, package-name/import-name decision, reason-code vocabulary, geoprivacy handoff, transform receipts, correction invalidation, release integration, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 28de9ef2710d978a5c00f3057cc33868cbedd698
  prior_blob: ba61bc82ab405ba731bb843c0e9d25b079e6db5b
  source_root_blob: 6f53a525e9524ac6cc73258d83186e96fe53a6a2
  source_module_blob: 70d58bc2c016fe759db77d2f398b8c0e3c37248d
  pyproject_blob: ad9241a73d73d1c47fe2d29e52594b3961e8b588
  initializer_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  spatial_foundation_blob: 8e6ec163063d465d47ef1576c54755bc41539915
  maplibre_readme_blob: 7aff988e18d5b113d8fb049f2ffd8c9e49bcf422
  map_context_schema_blob: 06a98e4f49e5b9d5487a420e18273160b6ed9efc
  map_layer_schema_blob: a28a6b194ce61dfc25667ebe9f095680b099893a
  data_layer_schema_blob: 2ed967b05a7dacdf0990366820e018dba1adc79b
  layers_layer_schema_blob: 81b6872fa7f9c843adb8432f28aa306ab8d272f6
  tile_artifact_schema_blob: ed8fb0834c06a6254d6175f9a08b8d17ccc68d71
  layer_manifest_contract_blob: d2a575cd9f247cc2649c6e7f0dafd3319e03a25d
  geo_manifest_contract_blob: cf8e467cf32323718e38ad1510da3e5f60bef884
  geo_manifest_schema_blob: 931a0de24e45af4bc237c596c69bcaf305fb811f
related:
  - ./pyproject.toml
  - ./src/README.md
  - ./src/geo/README.md
  - ./src/geo/__init__.py
  - ../README.md
  - ../maplibre/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/spatial-foundation.md
  - ../../contracts/data/layer_manifest.md
  - ../../contracts/evidence/kfm_geo_manifest.md
  - ../../schemas/contracts/v1/ui/map_context_envelope.schema.json
  - ../../schemas/contracts/v1/map/layer_manifest.schema.json
  - ../../schemas/contracts/v1/data/layer_manifest.schema.json
  - ../../schemas/contracts/v1/layers/layer_manifest.schema.json
  - ../../schemas/contracts/v1/map/tile_artifact_manifest.schema.json
  - ../../schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json
tags: [kfm, packages, geo, python, shared-library, package-boundary, src-layout, spatial-foundation, CRS, geometry, bbox, scale, uncertainty, generalization, geoprivacy, schema-profile, generated-code, deterministic, no-network, fail-closed, rollback]
notes:
  - "v0.2 replaces stale planning language with a commit-pinned package contract for the current kfm-geo 0.0.0 scaffold."
  - "The merged src/README.md and src/geo/README.md v0.2 documents own source-root and module-specific boundaries; this file owns package identity, packaging, dependency, compatibility, consumer, versioning, test/CI, and release-admission posture."
  - "The import initializer is empty and selected helper modules are absent; no supported API, build behavior, consumer, CRS engine, geometry validator, transform engine, or runtime integration is claimed."
  - "Spatial doctrine and rich contract prose exceed current permissive/minimal schemas, and LayerManifest has competing schema homes; implementation admission requires accepted profiles and no silent normalization."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Geo Shared Package

`packages/geo/`

> Shared-package boundary for reusable geospatial primitive implementation. The current repository surface is a **greenfield Python `0.0.0` scaffold**, not an implemented or published geometry library: package metadata is minimal, `src/geo/__init__.py` is empty, selected helper modules are absent, package discovery and dependencies are not declared, no dedicated Geo workflow exists, and key spatial contracts and schemas remain incomplete or conflicted.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![distribution](https://img.shields.io/badge/distribution-kfm--geo-3776ab)
![declared-version](https://img.shields.io/badge/declared%20version-0.0.0-lightgrey)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![authority](https://img.shields.io/badge/authority-helper%20only-455a64)
![network](https://img.shields.io/badge/network-none%20by%20default-455a64)
![spatial-truth](https://img.shields.io/badge/map-carrier%20not%20truth-0b7285)

**Quick links:** [Purpose](#purpose-and-audience) · [Authority](#authority-level) · [Status](#current-repository-state) · [Context](#package-bounded-context) · [Placement](#placement-and-responsibility) · [Package split](#package-source-root-and-module-split) · [Spatial Foundation](#relationship-to-spatial-foundation) · [MapLibre](#relationship-to-maplibre) · [Metadata](#distribution-and-package-metadata) · [Imports](#import-name-and-public-api) · [Dependencies](#dependency-and-optional-feature-policy) · [Profiles](#contract-schema-and-profile-boundary) · [CRS/geometry](#crs-geometry-scale-and-uncertainty-boundary) · [Transforms](#transform-generalization-and-public-safe-boundary) · [Inputs/outputs](#package-input-and-output-boundary) · [Consumers](#consumer-and-integration-boundary) · [Trust](#lifecycle-evidence-policy-release-and-public-safety) · [Security](#security-privacy-and-sensitive-location-controls) · [Resources](#resource-limits-native-libraries-and-grid-data) · [Tests](#tests-fixtures-validators-and-ci) · [Versioning](#versioning-compatibility-and-deprecation) · [Admission](#implementation-admission-sequence) · [Evolution](#proposed-package-evolution) · [Docs](#documentation-and-maintenance) · [Validation](#validation-commands) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger) · [Checklist](#maintainer-checklist) · [Rollback](#rollback)

> [!IMPORTANT]
> **Repository snapshot:** `main@28de9ef2710d978a5c00f3057cc33868cbedd698`<br>
> **Distribution name:** `kfm-geo`<br>
> **Declared version:** `0.0.0`<br>
> **Verified source root:** `src/`<br>
> **Verified import package:** `src/geo/`<br>
> **Verified implementation:** empty `src/geo/__init__.py`; selected helper modules are absent<br>
> **Verified child contracts:** [`src/README.md`](./src/README.md) v0.2 and [`src/geo/README.md`](./src/geo/README.md) v0.2<br>
> **Build backend, Python requirement, dependencies, package discovery, exports, consumers, installation, and package publication:** not established<br>
> **Map/context/manifest schemas:** present but permissive or minimal `PROPOSED` scaffolds<br>
> **LayerManifest schema home:** conflicted across `map/`, `data/`, and `layers/` families<br>
> **Dedicated Geo workflow:** not found at the exact checked `.github/workflows/geo.yml` path

> [!CAUTION]
> A package name is not a trust decision. A successful import is not evidence. A parsed geometry is not spatial truth. A coordinate transform is not automatically admissible. A generalized geometry is not automatically public-safe. A schema-shaped object is not a release. Public clients must consume governed APIs and released artifacts, not package internals.

---

## Purpose and audience

`packages/geo/` is the package-level home for a future reusable KFM geospatial primitive library.

At maturity, the package may provide deterministic, bounded, no-network-by-default implementation support for:

- explicit coordinate reference and coordinate-operation profile carriers;
- local geometry representation checks tied to accepted contracts;
- bbox, extent, dimensionality, precision, scale, and uncertainty checks;
- transform-plan construction and, only after explicit dependency/profile decisions, bounded transform execution;
- source/internal, derived, generalized, redacted, and public geometry separation;
- candidate fragments for accepted map, layer, tile, evidence, validation, or runtime contracts;
- deterministic issue carriers for downstream validation and finite runtime mapping;
- generated or handwritten adapters pinned to accepted schema versions;
- synthetic, sanitized, public-safe test helpers.

The package must remain subordinate to:

- source descriptors and source-role decisions;
- semantic contracts and machine schemas;
- EvidenceRef-to-EvidenceBundle resolution;
- rights, sensitivity, geoprivacy, and policy decisions;
- review, promotion, release, correction, supersession, and rollback records;
- governed API serialization;
- MapLibre and UI rendering boundaries;
- lifecycle storage and artifact publication homes.

### Audience

This README is for:

- Geo package maintainers;
- Spatial Foundation and map stewards;
- domain package and pipeline maintainers;
- contract, schema, validator, policy, release, and correction stewards;
- packaging, dependency, security, and supply-chain reviewers;
- geoprivacy, rights, sensitivity, and privacy reviewers;
- governed API, MapLibre, Evidence Drawer, Focus Mode, and export maintainers;
- reviewers deciding whether a proposed spatial behavior belongs in this package, a domain package, a validator, a pipeline, policy, release tooling, or the renderer lane.

[Back to top](#top)

---

## Authority level

**Shared implementation package, currently scaffolded; non-authoritative for spatial meaning, source truth, evidence closure, policy, sensitive-location disclosure, release, storage, or public maps.**

| Concern | Authority in `packages/geo/` |
|---|---|
| Package identity and boundary | **Supporting.** This README and accepted metadata define package scope and compatibility posture. |
| Spatial Foundation meaning | **None.** Architecture doctrine and accepted contracts own meaning. |
| CRS profile meaning and permitted coordinate operations | **None.** Accepted contracts, source context, policy, and transform profiles own the decision. |
| Geometry machine shape | **None.** Accepted schemas own shape. |
| Geometry validity for publication | **None.** Validators, evidence, policy, review, and release gates own admission. |
| Source scale, resolution, and accuracy | **None.** Source descriptors and evidence records own source limitations. |
| Sensitivity and exact-location disclosure | **None.** Policy and geoprivacy systems own allow, restrict, generalize, redact, withhold, deny, and abstain outcomes. |
| Evidence closure | **None.** EvidenceRef-to-EvidenceBundle resolution remains outside this package. |
| Release and publication | **None.** Release manifests, promotion records, correction records, and rollback targets own publication state. |
| Map rendering | **None.** [`../maplibre/`](../maplibre/README.md) is the verified renderer-helper lane; app/UI roots own public rendering. |
| Local implementation behavior | **Supporting only.** Accepted code may inspect explicit inputs, perform accepted pure calculations, and return candidate values or issues. |
| Package distribution | **Not established.** Current metadata does not prove buildability, installability, or publication. |

No geometry library, CRS database, native dependency, or model provider transfers governance authority into this package.

[Back to top](#top)

---

## Current repository state

### Evidence snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Repository ID | `1059091169` |
| Visibility | public |
| Base ref | `main` |
| Base commit | `28de9ef2710d978a5c00f3057cc33868cbedd698` |
| Prior target blob | `ba61bc82ab405ba731bb843c0e9d25b079e6db5b` |
| Source-root README blob | `6f53a525e9524ac6cc73258d83186e96fe53a6a2` |
| Source-module README blob | `70d58bc2c016fe759db77d2f398b8c0e3c37248d` |
| Project metadata blob | `ad9241a73d73d1c47fe2d29e52594b3961e8b588` |
| Import initializer blob | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| Current revision | documentation-only package-level v0.2 proposal |

### Verified package surface

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---:|---|
| This README | Existing v1 planning-oriented package guide. | **CONFIRMED** | Revised in place. |
| [`pyproject.toml`](./pyproject.toml) | Contains only a comment, `[project]`, name `kfm-geo`, and version `0.0.0`. | **CONFIRMED minimal placeholder** | Distribution identity is known; build and dependency behavior are not. |
| [`src/README.md`](./src/README.md) | Repository-grounded source-root contract v0.2. | **CONFIRMED** | Owns source-layout, discovery, import, dependency, generated-code, resource, and test-placement boundaries. |
| [`src/geo/README.md`](./src/geo/README.md) | Repository-grounded source-module contract v0.2. | **CONFIRMED** | Owns detailed CRS, geometry, scale, transform, manifest, and geoprivacy helper semantics. |
| `src/geo/__init__.py` | Exists and is empty. | **CONFIRMED** | Import-package marker only; no supported exports are established. |
| `package.json` | Not found at `packages/geo/package.json`. | **CONFIRMED bounded absence** | Do not claim a JavaScript or TypeScript package. |
| `CHANGELOG.md` | Not found at `packages/geo/CHANGELOG.md`. | **CONFIRMED bounded absence** | No package-specific change ledger is established. |
| `src/geo/py.typed` | Not found at the exact checked path. | **CONFIRMED bounded absence** | PEP 561 typed-package support is not established. |
| Selected helper files | `crs.py`, `geometry.py`, `public_safe.py`, and `validation.py` were absent at exact tested paths during the package inspection. | **CONFIRMED bounded absence** | No executable Geo API is established. |
| Package-specific tests | `tests/packages/geo/README.md` was not found. | **CONFIRMED bounded absence** | No package test lane is documented. |
| Package-specific fixtures | `fixtures/packages/geo/README.md` was not found. | **CONFIRMED bounded absence** | No package fixture lane is documented. |
| Dedicated workflow | `.github/workflows/geo.yml` was not found. | **CONFIRMED bounded absence** | No workflow proves Geo package behavior. |

### Metadata not established

The current `pyproject.toml` does **not** establish any of the following:

- `[build-system]` or a build backend;
- `requires-python`;
- dependencies or optional dependencies;
- package discovery configuration;
- package data inclusion;
- console scripts or entry points;
- README, license, authors, maintainers, classifiers, keywords, or project URLs;
- wheel or source-distribution behavior;
- typed-package declaration;
- publication repository or release automation;
- compatibility guarantees.

The absence of these fields does not prove the package is impossible to import in every development environment. It means build, install, discovery, dependency, and publication behavior are **UNKNOWN / NEEDS VERIFICATION** and must not be represented as supported.

[Back to top](#top)

---

## Package bounded context

### In scope after implementation admission

The package may own reusable implementation mechanics for:

- explicit CRS and coordinate-operation carriers;
- deterministic geometry parsing and local representation checks;
- bbox and extent helpers;
- scale, precision, resolution, and uncertainty carriers;
- transform-plan and transform-result carriers;
- bounded adapters between accepted spatial schemas;
- issue and diagnostic carriers tied to an accepted vocabulary;
- source/internal versus derived/public geometry separation;
- public-safe geometry candidate assembly from supplied policy decisions;
- manifest-fragment assembly against accepted profiles;
- synthetic and sanitized fixture builders;
- package-local compatibility shims with explicit deprecation and rollback.

### Out of scope

The package must not own:

- source data acquisition or connector behavior;
- source identity, source role, rights, or sensitivity registries;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data;
- semantic contract meaning or JSON Schema authority;
- policy evaluation or geoprivacy decisions;
- EvidenceBundle storage or EvidenceRef resolution;
- proof, receipt, review, or release persistence;
- promotion, correction, supersession, withdrawal, or rollback decisions;
- tile, raster, vector, PMTiles, COG, or GeoParquet artifact storage;
- MapLibre rendering, style authority, UI state, or public routes;
- AI-generated geometry, claims, or truth;
- secrets, source credentials, private records, or protected-location fixture data.

### Placement test

A proposed behavior belongs here only when all of the following are true:

1. It is reusable across more than one domain or subsystem.
2. It is implementation support rather than semantic, policy, evidence, release, or renderer authority.
3. Its inputs and outputs can be governed by accepted contracts or explicitly versioned local carriers.
4. It can run deterministically without hidden network access or ambient source-store reads.
5. It preserves provenance, uncertainty, policy, evidence, release, correction, and rollback references supplied by callers.
6. It does not disclose or infer protected locations.
7. Its failure behavior is finite, inspectable, and testable.
8. Its dependencies, licenses, native resources, and offline behavior are reviewed.
9. Its tests and fixtures can remain synthetic, sanitized, and public-safe.
10. Its rollback does not require rewriting canonical data or public release history.

When these conditions are not met, place the behavior in the owning domain package, connector, pipeline, validator, policy, release, runtime, app/UI, or documentation root.

[Back to top](#top)

---

## Placement and responsibility

Directory Rules treats `packages/` as the shared reusable implementation root. It does not make every spatial concern a package concern.

| Concern | Owning home | Package relationship |
|---|---|---|
| Package boundary and overview | `packages/geo/README.md` | This document. |
| Source-layout and packaging internals | [`packages/geo/src/README.md`](./src/README.md) | Defines source-root structure and enforceability placement. |
| Import-module helper semantics | [`packages/geo/src/geo/README.md`](./src/geo/README.md) | Defines detailed future Geo helper behavior. |
| Package metadata | [`packages/geo/pyproject.toml`](./pyproject.toml) | Must become the accepted build/distribution contract before publication. |
| Cross-domain spatial doctrine | [`docs/architecture/spatial-foundation.md`](../../docs/architecture/spatial-foundation.md) | Defines meaning; package code implements accepted mechanics only. |
| Semantic contracts | `contracts/` | Own object meaning and invariants. |
| Machine schemas | `schemas/contracts/v1/` | Own machine shape and profile version. |
| Source descriptors and registries | `data/registry/` and accepted control-plane homes | Own source identity, rights, cadence, role, and limitations. |
| Policy and geoprivacy | `policy/` and accepted domain policy homes | Own disclosure and admissibility decisions. |
| Validators | `tools/validators/` and accepted test lanes | Own independent conformance checks. |
| Lifecycle data | `data/<phase>/` | Own source and derived data by lifecycle state. |
| Proofs and receipts | `data/proofs/`, `data/receipts/` | Own audit and evidentiary records. |
| Release and rollback | `release/`, accepted rollback/correction homes | Own publication state and reversibility. |
| Renderer helpers | [`packages/maplibre/`](../maplibre/README.md) | Own MapLibre descriptor/render-adapter support. |
| Public API/UI | `apps/`, `ui/`, `web/`, or accepted equivalents | Consume released, governed outputs; do not import package internals as authority. |
| Domain-specific spatial semantics | `packages/domains/<domain>/`, domain contracts/docs | Stay with the owning domain. |

> [!WARNING]
> Do not place schemas, contracts, source registries, lifecycle data, proofs, receipts, release manifests, tiles, styles, UI components, public routes, or exact sensitive-location examples under `packages/geo/`.

[Back to top](#top)

---

## Package, source-root, and module split

The three README layers have different responsibilities.

| Layer | Owns | Must not duplicate |
|---|---|---|
| `packages/geo/README.md` | Package identity, bounded context, metadata posture, dependency policy, consumers, versioning, test/CI admission, package release, compatibility, and rollback. | Detailed module API semantics or source-layout mechanics. |
| [`packages/geo/src/README.md`](./src/README.md) | Source-layout, discovery, import/export structure, dependency direction, generated-code placement, package-data/native-resource posture, and test placement. | Package release policy or detailed CRS/geometry semantics. |
| [`packages/geo/src/geo/README.md`](./src/geo/README.md) | CRS, geometry, bbox, scale, uncertainty, transform, public-safe candidate, manifest, issue, and helper behavior boundaries. | Package metadata, release authority, or source-root discovery rules. |
| `packages/geo/src/geo/__init__.py` | Future deliberate import surface. | Hidden side effects, ambient configuration, source access, or broad re-export by accident. |

A change that affects all three layers should update all affected documents in the same governed change or explain why a layer is unchanged.

[Back to top](#top)

---

## Relationship to Spatial Foundation

Spatial Foundation provides the cross-domain grammar for coordinate reference, geometry validity, scale, generalization, uncertainty, basemap context, and cartographic representation.

This package may implement accepted mechanics associated with that grammar. It does not own the grammar itself.

### Package responsibilities

- preserve explicit CRS and coordinate-operation context;
- preserve source scale, representation scale, resolution, precision, and uncertainty;
- distinguish source/internal geometry from derived and public geometry;
- make transforms and information loss inspectable;
- return bounded issues instead of guessing;
- keep domain semantics outside generic helpers;
- keep map rendering outside the package;
- preserve evidence, policy, release, correction, and rollback references supplied by callers.

### Non-responsibilities

- choosing the canonical CRS profile;
- deciding which transform is acceptable for a source or release;
- deciding whether a geometry is evidentially sufficient;
- deciding sensitivity or geoprivacy outcomes;
- deciding whether a derived geometry may be published;
- defining domain truth;
- approving a layer, tile, map, or export release.

[Back to top](#top)

---

## Relationship to MapLibre

The verified adjacent renderer-helper lane is [`packages/maplibre/`](../maplibre/README.md).

| Geo package | MapLibre package |
|---|---|
| CRS, geometry, bbox, scale, precision, uncertainty, transform-plan, and public-safe candidate mechanics. | MapLibre source, layer, style, map-context, and renderer-descriptor adapter mechanics. |
| Produces local candidates or issues under accepted profiles. | Produces renderer-ready descriptor candidates from governed inputs. |
| Does not render or decide release. | Does not decide truth, evidence, policy, or release. |
| Must not import app/UI renderer state as authority. | Must not invent geometry or bypass Geo/evidence/policy gates. |

The old package README referred to `packages/maplibre-runtime/`. The verified current helper lane is `packages/maplibre/`. Any future runtime split or rename requires current repository evidence and an ADR or migration note; this README does not decide it.

[Back to top](#top)

---

## Distribution and package metadata

### Confirmed metadata

```toml
[project]
name = "kfm-geo"
version = "0.0.0"
```

This confirms only the declared distribution name and version.

### Required before build or publication claims

An accepted metadata change should establish, at minimum:

| Metadata concern | Required decision |
|---|---|
| Build backend | Select and pin a supported backend with reproducible build behavior. |
| Python support | Declare `requires-python` and test the supported matrix. |
| Package discovery | Explicitly include the intended `src/geo` package and exclude unintended files. |
| Dependencies | Declare required dependencies with reviewed version bounds and licenses. |
| Optional features | Separate optional native/transform/adapter dependencies behind explicit extras. |
| README and license | Bind package metadata to accepted documentation and license posture. |
| Typed-package support | Add `py.typed` only when annotations and distribution inclusion are verified. |
| Package data | Enumerate any shipped profiles/resources and verify hashes, rights, and offline behavior. |
| Project URLs | Point to accepted repository, documentation, issue, and source locations. |
| Entry points | Add none unless a reviewed CLI or plugin contract exists. |
| Build artifacts | Verify wheel and source-distribution contents. |
| Publication | Define repository, signing, attestations, version policy, and rollback process. |

### Build posture

Until metadata and tests prove otherwise:

- do not publish `kfm-geo`;
- do not promise `pip install` support;
- do not represent editable installs as production support;
- do not infer dependencies from architecture prose;
- do not infer typed-package support;
- do not infer wheel contents;
- do not use package version `0.0.0` as a release or compatibility guarantee.

[Back to top](#top)

---

## Import name and public API

The distribution name is `kfm-geo`; the verified source package is `geo`.

### Import posture

- `src/geo/__init__.py` is empty;
- no supported top-level symbols are established;
- package discovery is not declared;
- installation behavior is not established;
- the broad import name `geo` may collide with external or internal packages;
- no import compatibility guarantee exists.

### Required decisions

Before declaring a public API:

1. Decide whether `geo` remains the accepted import name.
2. Search the repository and supported environments for collisions.
3. Record the decision in an ADR or package contract when material.
4. Define a minimal top-level export list.
5. Keep experimental modules private or explicitly versioned.
6. Add import-surface tests.
7. Define deprecation and compatibility policy.
8. Verify package discovery in built artifacts.
9. Verify no import-time network, filesystem, registry, policy, or source-store access occurs.
10. Publish only after package and repository release gates pass.

### Import safety

Importing the package must not:

- fetch CRS databases, projection grids, or remote schemas;
- inspect connectors, source stores, lifecycle data, or user files;
- initialize native libraries with mutable global policy;
- read secrets or environment credentials;
- configure logging globally;
- mutate locale, timezone, numeric precision, or process-wide environment;
- load unrestricted sensitive-location data;
- register public routes or renderer state;
- call model providers;
- write caches, receipts, proofs, or release records.

[Back to top](#top)

---

## Dependency and optional-feature policy

### Default posture

The package should remain dependency-light and no-network-by-default.

Every proposed dependency must document:

- the exact capability it provides;
- whether the capability belongs in the generic Geo package;
- supported versions and Python platforms;
- license and redistribution posture;
- native-library and binary-wheel implications;
- projection-grid or auxiliary-data requirements;
- offline behavior;
- determinism and numeric-stability implications;
- security and maintenance posture;
- resource and denial-of-service risks;
- fallback behavior;
- tests and rollback.

### Dependency classes

| Class | Examples | Admission rule |
|---|---|---|
| Pure Python utility | Parsing or typed-carrier support | May be admitted when bounded, deterministic, licensed, and tested. |
| Geometry engine | Topology, predicates, repair, simplification | Requires explicit operation/profile contracts; never enables silent repair. |
| CRS/transform engine | Coordinate operations and projection support | Requires explicit source/target CRS, operation selection, grid/resource policy, accuracy reporting, and offline tests. |
| Native geospatial stack | GDAL/PROJ/GEOS-linked features | Requires platform matrix, binary provenance, licensing, security, and rollback review. |
| Schema/model generation | JSON Schema-to-model tooling | Generated output must be reproducible, version-pinned, reviewable, and information-preserving. |
| Network client | Remote registry, grid, or source lookup | **Not admitted by default.** Source activation belongs outside the package. |
| Renderer dependency | MapLibre/UI libraries | Belongs in renderer/app lanes, not this package. |
| Model/AI dependency | Embedding, chat, inference | Belongs behind governed AI adapters, not this package. |

### Optional features

Optional dependencies should be isolated behind explicit extras or adapters only after the package has an accepted build configuration. Core imports must not fail merely because an optional native dependency is absent; callers should receive a stable, documented unsupported-capability result.

[Back to top](#top)

---

## Contract, schema, and profile boundary

Package code must implement accepted profiles; it must not choose among conflicting profiles silently.

### Current confirmed schema posture

| Object family | Confirmed current posture | Package consequence |
|---|---|---|
| MapContextEnvelope | `schemas/contracts/v1/ui/map_context_envelope.schema.json` is an empty permissive `PROPOSED` scaffold. | Do not claim field-level conformance beyond the actual schema. |
| LayerManifest — map | `schemas/contracts/v1/map/layer_manifest.schema.json` is an empty permissive `PROPOSED` scaffold. | Not canonical by package assumption. |
| LayerManifest — data | `schemas/contracts/v1/data/layer_manifest.schema.json` requires only `id`, permits optional `version` and `spec_hash`, and allows additional properties. | Rich layer semantics are not machine-enforced. |
| LayerManifest — layers | `schemas/contracts/v1/layers/layer_manifest.schema.json` is an empty permissive `PROPOSED` scaffold. | Not canonical by package assumption. |
| TileArtifactManifest | `schemas/contracts/v1/map/tile_artifact_manifest.schema.json` is an empty permissive `PROPOSED` scaffold. | Do not claim complete tile-manifest support. |
| KFMGeoManifest | Rich draft semantic contract plus a minimal schema stub requiring only `id`. | Adapters must not imply richer validation than exists. |

### LayerManifest conflict

Three LayerManifest schema homes coexist:

```text
schemas/contracts/v1/map/layer_manifest.schema.json
schemas/contracts/v1/data/layer_manifest.schema.json
schemas/contracts/v1/layers/layer_manifest.schema.json
```

The package must not:

- pick one by convenience;
- translate among them silently;
- merge fields without an accepted profile;
- treat additional properties as semantic approval;
- expose an adapter as canonical before an ADR, migration note, or compatibility rule resolves the split.

### Profile pinning

Each schema adapter must identify:

- contract name and version;
- schema path and `$id`;
- schema content hash or accepted `spec_hash`;
- generation or handwritten adapter version;
- preserved fields;
- unsupported fields;
- loss, coercion, or default behavior;
- issue codes;
- policy and release prerequisites;
- correction and invalidation behavior.

Unknown, conflicted, or unsupported profiles must fail closed with a stable issue carrier. They must not fall through to a “best effort” profile.

[Back to top](#top)

---

## CRS, geometry, scale, and uncertainty boundary

Detailed helper semantics live in [`src/geo/README.md`](./src/geo/README.md). Package-level invariants include the following.

### CRS

The package must not:

- assume WGS84 when CRS is missing;
- infer axis order from coordinate magnitude;
- discard datum, vertical reference, coordinate epoch, units, or area of use;
- choose a coordinate operation only because a library ranks it first;
- fetch missing grids from the network;
- hide ballpark or fallback transforms;
- represent a CRS identifier as proof that a transform was correctly applied.

### Geometry

The package must not:

- silently repair invalid geometry;
- coerce geometry type without an explicit operation;
- drop Z or M dimensions without recording loss;
- normalize ring orientation as if it were source truth;
- discard empty components or invalid coordinates silently;
- flatten collections without an accepted profile;
- erase antimeridian or polar behavior;
- treat local geometric validity as evidentiary or publication validity.

### Scale, precision, and uncertainty

The package must preserve:

- source scale and resolution;
- representation scale and target resolution;
- coordinate precision and uncertainty;
- transform accuracy and area of use;
- topology and simplification tolerance;
- derived/generalized status;
- temporal and spatial scope mismatch;
- information-loss and caveat records.

Numeric formatting, coordinate rounding, simplification, aggregation, or generalization must never create an appearance of greater accuracy than the source supports.

[Back to top](#top)

---

## Transform, generalization, and public-safe boundary

### Transform stages

A governed transform flow separates:

1. source/internal geometry;
2. proposed operation or transform plan;
3. executed derived geometry;
4. validation result;
5. policy/geoprivacy decision;
6. public-safe candidate;
7. release decision;
8. public projection.

The package may support stages 2–4 and bounded assembly at stage 6 when all governing decisions are supplied. It does not own stages 5 or 7.

### Public-safe geometry

A public-safe geometry candidate must preserve or reference:

- source/internal geometry identity;
- transform specification and version;
- source and target CRS;
- tolerance, scale, precision, and uncertainty;
- policy decision and audience class;
- redaction/generalization reason;
- evidence references;
- validation report;
- review and release references;
- correction, supersession, and rollback targets.

The package must not:

- decide that exact geometry is safe;
- convert unknown sensitivity into public;
- use UI style filtering as geoprivacy;
- generate plausible substitute coordinates;
- publish centroids or grids without a supplied decision;
- expose source geometry alongside a generalized public candidate;
- let caller convenience override a deny, restrict, abstain, or review-required posture.

[Back to top](#top)

---

## Package input and output boundary

### Permitted input families

| Input family | Required posture |
|---|---|
| CRS and operation context | Explicit identifiers, axis order, units, datum/vertical/epoch context, source/target role, accepted profile, and operation constraints. |
| Geometry candidate | Explicit representation, geometry role, schema/profile version, source identity, and dimensionality. |
| Bbox or extent | Explicit axis/CRS semantics, antimeridian policy, dimensionality, and derivation status. |
| Scale and uncertainty | Explicit source scale, target representation scale, precision, resolution, tolerance, and uncertainty. |
| Evidence and provenance refs | Preserve as references; do not resolve or fabricate them locally. |
| Policy and geoprivacy decision | Consume an explicit decision and obligations; do not evaluate policy. |
| Release and correction context | Preserve release, correction, supersession, and rollback refs; do not approve release. |
| Fixture input | Synthetic, sanitized, and public-safe only. |

### Permitted output families

After profile acceptance and implementation, package outputs may include:

- parsed or normalized **candidate** carriers;
- geometry inspection reports;
- bbox/extent check results;
- transform plans;
- transform execution results with accuracy and resource metadata;
- scale, precision, and uncertainty issue carriers;
- derived/generalized geometry candidates;
- public-safe geometry candidates assembled from supplied decisions;
- schema adapter results;
- manifest fragment candidates;
- deterministic diagnostics and issue codes.

### Forbidden outputs

The package must not emit:

- release approval;
- policy approval;
- source-role promotion;
- EvidenceBundle closure;
- authoritative public claims;
- public API responses as authority;
- UI components or renderer state;
- lifecycle data writes;
- proof or receipt persistence;
- tile or layer publication;
- uncited or invented geometry.

[Back to top](#top)

---

## Consumer and integration boundary

### Potential consumers

Potential consumers remain **PROPOSED / NEEDS VERIFICATION** until imports and tests are found.

They may include:

- domain packages needing generic spatial primitives;
- pipelines performing governed transforms;
- validators checking spatial candidates;
- map artifact builders;
- governed API assemblers;
- MapLibre descriptor adapters;
- Evidence Drawer or Focus Mode payload assemblers;
- export builders;
- tests and synthetic fixture builders.

### Integration rules

A consumer must:

1. pin an accepted package and profile version;
2. provide explicit source, CRS, geometry role, scale, uncertainty, and policy context;
3. handle all documented issues and unsupported states;
4. keep source/internal and public geometry separate;
5. validate package output independently;
6. resolve evidence through governed interfaces;
7. apply policy, rights, sensitivity, and geoprivacy gates;
8. preserve release, correction, supersession, and rollback context;
9. serialize public results through governed API contracts;
10. never expose package internals directly to public clients.

No consumer may treat a successful helper call as permission to publish.

[Back to top](#top)

---

## Lifecycle, evidence, policy, release, and public safety

KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package may compute or validate candidates inside governed workflows. It does not own lifecycle state or promotion.

### Required separation

| Concern | Package rule |
|---|---|
| Source activation | No source fetching, credential use, or connector behavior. |
| Lifecycle access | No direct reads from RAW, WORK, QUARANTINE, canonical stores, or unpublished candidate stores as package authority. |
| Evidence | Preserve EvidenceRefs; resolution and closure occur through governed evidence systems. |
| Policy | Consume explicit decisions; do not evaluate rights, sensitivity, geoprivacy, or release policy. |
| Review | Preserve review refs; do not self-approve. |
| Release | Preserve release refs; do not promote or publish. |
| Public API | Return candidates/issues to governed assemblers; never become a public trust membrane by itself. |
| Renderer | Hand off governed candidates to MapLibre/app lanes only after required gates. |
| Correction | Preserve correction and invalidation relationships. |
| Rollback | Preserve prior known-safe targets; do not rewrite release history. |

### Fail-safe posture

Missing or conflicted support should produce a finite unsupported, invalid, denied-ready, abstain-ready, or review-required **issue carrier defined by an accepted contract**.

The old README used terms such as `VALID`, `INVALID`, `ABSTAIN_READY`, `DENY_READY`, `GENERALIZED`, and `WITHHELD`. No accepted Geo result contract or schema was verified. These terms must not become public or package API enums by documentation alone.

[Back to top](#top)

---

## Security, privacy, and sensitive-location controls

### Sensitive domains

Exact or reconstructable locations may require deny-by-default or constrained handling for:

- rare, threatened, or culturally sensitive species;
- archaeological and heritage resources;
- critical infrastructure;
- private property and living-person records;
- tribal, sovereign, or culturally restricted knowledge;
- facilities, security assets, and emergency infrastructure;
- other policy-designated protected locations.

### Package rules

The package must:

- operate on the minimum necessary fields;
- keep source/internal geometry separate from public candidates;
- avoid logging coordinates or raw geometry by default;
- support redacted diagnostics;
- avoid storing production examples in source or fixtures;
- avoid returning both exact and generalized geometry in the same public-bound object unless the contract explicitly separates access tiers;
- bound geometry complexity, nesting, coordinate counts, and transform work;
- reject non-finite numbers and malformed structures;
- record lossy operations;
- preserve supplied policy and audience context;
- keep caches private, bounded, and non-authoritative if caches are ever introduced.

The package must not store chain-of-thought, prompts, model traces, credentials, unrestricted source payloads, or sensitive production geometry.

[Back to top](#top)

---

## Resource limits, native libraries, and grid data

### Required limits

Accepted implementations should define configurable limits for:

- input byte size;
- geometry nesting depth;
- coordinate count;
- ring and component count;
- WKT/WKB/GeoJSON parse size;
- transform batch size;
- recursion and iteration count;
- simplification or repair work;
- output size;
- diagnostic count;
- execution time where the runtime supports it.

### Native-library posture

If native geospatial libraries are admitted, review must cover:

- exact library and binary versions;
- build provenance and platform support;
- CVE and patch process;
- ABI compatibility;
- deterministic behavior across platforms;
- thread safety and process-global configuration;
- license and redistribution obligations;
- environment variables and data-directory search paths;
- local grid/database versioning;
- failure when required resources are absent;
- rollback to a prior known-safe dependency set.

### Grid and auxiliary data

Projection grids, EPSG databases, geoid models, and similar resources are not invisible dependencies.

Every shipped or mounted resource must have:

- stable identity and version;
- content digest;
- license and rights posture;
- source and retrieval provenance;
- inclusion or mount strategy;
- offline behavior;
- update and invalidation policy;
- compatibility tests;
- correction and rollback path.

Hidden network download is prohibited.

[Back to top](#top)

---

## Tests, fixtures, validators, and CI

### Test posture

- no package-specific `tests/packages/geo/README.md` was found;
- no package-specific `fixtures/packages/geo/README.md` was found;
- no dedicated `.github/workflows/geo.yml` was found;
- no executable Geo API is established;
- general repository workflows do not prove Geo behavior.

### Required package test families

| Test family | Minimum expectations |
|---|---|
| Packaging | Build wheel/sdist, inspect contents, install in clean environments, verify import package and metadata. |
| Import safety | No network, no writes, no source-store access, no global logging/config mutation, no secret reads. |
| Export surface | Intentional top-level exports only; private symbols remain private. |
| Dependency absence | Core import and supported pure features behave predictably without optional dependencies. |
| CRS | Missing/ambiguous CRS, axis order, units, vertical/epoch context, area-of-use, and unsupported operation. |
| Geometry | Empty, malformed, non-finite, dimensionality, ring, topology, bbox, antimeridian, and complexity-limit cases. |
| Transform | Explicit operation selection, missing grids, ballpark/fallback visibility, accuracy, reproducibility, and offline behavior. |
| Scale/uncertainty | Precision inflation, unsupported scale, loss propagation, and uncertainty preservation. |
| Public-safe candidate | Supplied allow/restrict/generalize/redact/withhold/deny/review posture; no policy inference. |
| Schema adapters | Exact profile pinning, conflict rejection, unknown field preservation or explicit loss, round-trip tests. |
| Native resources | Platform matrix, binary provenance, grid/resource version, absent-resource behavior, and rollback. |
| Sensitive data | No exact protected coordinates in fixtures, logs, errors, snapshots, or public examples. |
| Resource limits | Oversized and adversarial geometry fails predictably without uncontrolled memory/CPU use. |
| Compatibility | Accepted API, serialization, issue-code, and deprecation tests across supported versions. |
| Correction/rollback | Invalidated profiles, resources, or dependency versions cannot remain silently active. |

### Fixture rules

Fixtures must be:

- synthetic or explicitly public-safe;
- deterministic;
- minimal;
- labeled with intended validity and sensitivity posture;
- free of credentials and private source payloads;
- free of exact protected locations;
- paired with negative and boundary cases;
- stored in the accepted fixture root, not embedded as production truth in source.

### Independent validators

Package-local checks do not replace independent validators. When package output is consequential, a validator outside the package should verify:

- schema/profile conformance;
- geometry and bbox constraints;
- transform provenance;
- scale and uncertainty preservation;
- evidence and source refs;
- policy and geoprivacy obligations;
- release, correction, and rollback refs.

[Back to top](#top)

---

## Versioning, compatibility, and deprecation

### Current version

`0.0.0` is a placeholder. It does not establish stability.

### Compatibility dimensions

A mature package must version and test:

- distribution metadata;
- import name;
- top-level exports;
- module paths;
- function and class signatures;
- serialized carriers;
- schema/profile versions;
- issue-code vocabulary;
- numeric behavior and tolerances;
- dependency and native-resource versions;
- package-data formats;
- public-safe candidate semantics;
- correction and invalidation behavior.

### Breaking changes

A breaking change requires:

1. a documented reason and affected contracts;
2. migration or compatibility plan;
3. tests for old and new behavior where overlap is supported;
4. explicit deprecation window when practical;
5. release notes or accepted change ledger;
6. consumer inventory and impact assessment;
7. profile/resource invalidation plan;
8. correction and rollback target;
9. updated package, source-root, and module documentation;
10. governed release approval.

### Import-name change

Changing `geo` to a narrower import name may reduce collision risk but is a breaking change. It requires repository search, consumer evidence, ADR or migration note, compatibility decision, package metadata update, and rollback plan. This README does not select a rename.

[Back to top](#top)

---

## Implementation admission sequence

The smallest safe implementation sequence is:

### Stage 0 — Purpose and profile decisions

- assign owners;
- decide whether the package remains separate and reusable;
- resolve or explicitly profile the LayerManifest schema split;
- accept CRS, geometry, bbox, scale, uncertainty, transform, geoprivacy, and issue contracts;
- decide distribution and import names;
- define public and private API posture.

### Stage 1 — Packaging foundation

- add `[build-system]`;
- declare Python support;
- configure package discovery;
- declare license and README metadata;
- establish dependency and optional-feature policy;
- add clean build/install/import tests;
- add `py.typed` only when verified.

### Stage 2 — Typed carriers and issue model

- implement contract-pinned carriers;
- establish finite issue codes;
- forbid hidden defaults and silent coercion;
- add round-trip and unknown-profile tests.

### Stage 3 — Pure geometry inspection

- add bounded parsing and representation checks;
- add complexity limits;
- add synthetic fixtures;
- keep repair and transformation out until separate admission.

### Stage 4 — CRS and transform planning

- add explicit CRS and operation profiles;
- implement transform-plan carriers;
- record missing resources and unsupported operations;
- keep network retrieval prohibited.

### Stage 5 — Optional transform execution

- admit reviewed dependencies and resources;
- implement explicit operation execution;
- expose accuracy, grids, fallbacks, and loss;
- add platform, offline, reproducibility, and rollback tests.

### Stage 6 — Public-safe candidate assembly

- consume supplied policy/geoprivacy decisions;
- preserve exact/derived/public separation;
- attach transform and evidence refs;
- add deny/restrict/generalize/redact/withhold/review tests;
- do not publish.

### Stage 7 — Schema and manifest adapters

- pin accepted profiles;
- reject conflicts and unknown profiles;
- preserve unknown fields or record loss;
- add independent validator coverage.

### Stage 8 — Governed integration

- inventory consumers;
- integrate through pipelines, validators, governed APIs, and MapLibre adapters;
- verify no public client calls package internals;
- verify release, correction, and rollback paths.

### Stage 9 — Package release

- choose version;
- produce reproducible artifacts;
- generate SBOM and attestations as required;
- run package and repository gates;
- sign and publish only through accepted release process;
- retain rollback target.

Each stage is independently reviewable and reversible. Do not skip from README scaffold to public integration.

[Back to top](#top)

---

## Proposed package evolution

The current verified package surface is minimal:

```text
packages/geo/
├── README.md
├── pyproject.toml
└── src/
    ├── README.md
    └── geo/
        ├── README.md
        └── __init__.py
```

A future tree is **PROPOSED** and must follow accepted profiles rather than topic convenience:

```text
packages/geo/
├── README.md
├── pyproject.toml
├── CHANGELOG.md                 # only after a package change-ledger decision
└── src/
    ├── README.md
    └── geo/
        ├── README.md
        ├── __init__.py          # deliberate, minimal exports
        ├── _profiles/           # accepted profile identifiers/adapters
        ├── _generated/          # reproducible schema-generated models
        ├── crs.py               # explicit CRS carriers/checks
        ├── geometry.py          # bounded representation checks
        ├── bbox.py              # explicit extent semantics
        ├── scale.py             # scale/precision/resolution carriers
        ├── uncertainty.py       # uncertainty and loss carriers
        ├── issues.py            # accepted finite issue vocabulary
        ├── transforms.py        # plans; execution only after admission
        ├── public_safe.py       # supplied-decision candidate assembly
        ├── manifests.py         # profile-pinned candidate adapters
        └── py.typed             # only after typed distribution proof
```

This tree is not implementation evidence. New files require:

- accepted ownership;
- Directory Rules placement check;
- contract/schema/profile support;
- dependency review;
- tests and fixtures;
- documentation updates;
- correction and rollback plan.

[Back to top](#top)

---

## Documentation and maintenance

### Documentation layers

| Document | Update when |
|---|---|
| This README | Package identity, metadata, dependency, consumer, versioning, CI, release, or compatibility posture changes. |
| [`src/README.md`](./src/README.md) | Source-layout, discovery, import, generated-code, package-data, native-resource, or test-placement behavior changes. |
| [`src/geo/README.md`](./src/geo/README.md) | CRS, geometry, bbox, scale, uncertainty, transform, manifest, issue, or public-safe helper semantics change. |
| Contracts and schemas | Meaning or machine shape changes. |
| Policy docs | Rights, sensitivity, geoprivacy, admissibility, or disclosure rules change. |
| Release docs | Version, publication, correction, supersession, withdrawal, or rollback changes. |

### Required maintenance records

Before package release, establish:

- owner and reviewer matrix;
- supported Python/platform matrix;
- dependency and native-resource inventory;
- consumer inventory;
- accepted contract/schema/profile matrix;
- package change ledger;
- security and vulnerability response path;
- deprecation policy;
- release, correction, and rollback runbook.

Documentation must not substitute for tests, build artifacts, runtime evidence, or release receipts.

[Back to top](#top)

---

## Validation commands

These commands are inspection aids. They do not prove behavior by themselves.

### Package inventory

```bash
find packages/geo -maxdepth 5 -type f -print | sort
```

### Metadata

```bash
sed -n '1,240p' packages/geo/pyproject.toml
```

### Import and consumer search

```bash
git grep -nE '(^|[[:space:]])(from geo|import geo)([[:space:].]|$)' -- . 2>/dev/null || true
git grep -n 'packages/geo' -- . 2>/dev/null || true
```

### Spatial profile search

```bash
git grep -nE 'MapContextEnvelope|LayerManifest|TileArtifactManifest|KFMGeoManifest|CRS|bbox|geometry|uncertainty|generalization|geoprivacy' -- \
  packages docs contracts schemas policy tests fixtures apps tools release 2>/dev/null || true
```

### Authority-drift search

```bash
git grep -nE 'publish|approve|release|evaluate_policy|decide_sensitivity|fetch_source|write_receipt|write_proof|render_map' -- \
  packages/geo 2>/dev/null || true
```

### Package checks after metadata exists

```bash
python -m build packages/geo
python -m pip install --force-reinstall packages/geo/dist/*.whl
python -c "import geo; print(geo.__file__)"
```

These build commands are **PROPOSED future checks**. Current metadata does not establish that they succeed.

[Back to top](#top)

---

## Definition of done

This package is not implementation-complete until all applicable criteria pass.

### Ownership and purpose

- [ ] Package owner and required stewards are assigned.
- [ ] Package purpose and boundary are accepted.
- [ ] Distribution and import-name decisions are recorded.
- [ ] Consumer inventory is established.

### Metadata and build

- [ ] Build backend is declared and pinned.
- [ ] Supported Python versions are declared and tested.
- [ ] Package discovery is explicit.
- [ ] Dependencies and optional features are declared and reviewed.
- [ ] License, README, project URLs, and package data are correct.
- [ ] Wheel and source-distribution contents are verified.
- [ ] Clean install and import tests pass.
- [ ] Package publication and rollback process is accepted.

### Contracts and profiles

- [ ] Canonical CRS, geometry, bbox, scale, uncertainty, transform, geoprivacy, and issue profiles are accepted.
- [ ] LayerManifest schema conflict is resolved or explicitly profiled.
- [ ] MapContextEnvelope, TileArtifactManifest, and KFMGeoManifest adapter profiles are version-pinned.
- [ ] Generated code is reproducible and provenance-bearing.
- [ ] Unknown and conflicted profiles fail closed.

### Implementation

- [ ] Top-level exports are deliberate and documented.
- [ ] Import-time side effects are absent.
- [ ] Hidden network and source-store access are absent.
- [ ] Resource limits are enforced.
- [ ] Numeric loss and uncertainty are preserved.
- [ ] Source/internal and public geometry remain separate.
- [ ] Public-safe candidate assembly requires supplied decisions.
- [ ] Native dependencies and grid resources are versioned and offline-capable.

### Tests and governance

- [ ] Package-specific test and fixture lanes are accepted.
- [ ] Dedicated or path-aware CI runs substantive Geo tests.
- [ ] Independent validators cover consequential outputs.
- [ ] Sensitive-location fixtures and logs are safe.
- [ ] Security, dependency, and platform matrices pass.
- [ ] Release, correction, supersession, and rollback paths are tested.
- [ ] Public consumers use governed APIs and released artifacts.

[Back to top](#top)

---

## Open verification register

| ID | Verification item | Status | Required evidence |
|---|---|---|---|
| GEO-PKG-001 | Assign package owner and required reviewers. | **NEEDS VERIFICATION** | CODEOWNERS, ownership record, or accepted governance doc. |
| GEO-PKG-002 | Confirm package remains a distinct shared library. | **NEEDS DECISION** | Architecture decision and consumer evidence. |
| GEO-PKG-003 | Decide whether distribution name `kfm-geo` is final. | **NEEDS DECISION** | Package naming ADR or release decision. |
| GEO-PKG-004 | Decide whether import name `geo` is final. | **NEEDS DECISION** | Collision analysis and compatibility decision. |
| GEO-PKG-005 | Select build backend. | **NEEDS VERIFICATION** | Accepted `[build-system]` configuration and build tests. |
| GEO-PKG-006 | Declare supported Python versions. | **NEEDS VERIFICATION** | `requires-python` plus CI matrix. |
| GEO-PKG-007 | Configure package discovery. | **NEEDS VERIFICATION** | Build configuration and wheel inspection. |
| GEO-PKG-008 | Declare required dependencies. | **NEEDS VERIFICATION** | Dependency proposal, license/security review, tests. |
| GEO-PKG-009 | Define optional dependency groups. | **NEEDS DECISION** | Accepted extras/adapter policy. |
| GEO-PKG-010 | Establish package license and metadata. | **NEEDS VERIFICATION** | Accepted metadata and legal review. |
| GEO-PKG-011 | Decide typed-package posture. | **NEEDS DECISION** | Annotation policy, `py.typed`, packaging tests. |
| GEO-PKG-012 | Establish package change ledger. | **NEEDS DECISION** | `CHANGELOG.md` or accepted alternative. |
| GEO-PKG-013 | Inventory current and intended consumers. | **NEEDS VERIFICATION** | Import search, dependency graph, integration tests. |
| GEO-PKG-014 | Define minimal public export surface. | **NEEDS DECISION** | API contract and import tests. |
| GEO-PKG-015 | Define private/experimental module policy. | **NEEDS DECISION** | Package API/versioning policy. |
| GEO-PKG-016 | Accept CRS profile. | **NEEDS DECISION** | Contract, schema, fixtures, validator, tests. |
| GEO-PKG-017 | Accept coordinate-operation profile. | **NEEDS DECISION** | Operation-selection and resource contract. |
| GEO-PKG-018 | Accept geometry representation profile. | **NEEDS DECISION** | Contract, schema, fixtures, validator, tests. |
| GEO-PKG-019 | Accept bbox/extent profile. | **NEEDS DECISION** | Axis, antimeridian, dimensionality contract. |
| GEO-PKG-020 | Accept scale, precision, and resolution profile. | **NEEDS DECISION** | Contract and tests. |
| GEO-PKG-021 | Accept uncertainty and information-loss profile. | **NEEDS DECISION** | Contract and tests. |
| GEO-PKG-022 | Accept issue/result vocabulary. | **NEEDS DECISION** | Semantic contract, schema, mappings, tests. |
| GEO-PKG-023 | Resolve LayerManifest schema-home conflict. | **CONFLICTED** | ADR, migration note, or compatibility profile. |
| GEO-PKG-024 | Strengthen MapContextEnvelope schema or bound adapter support. | **NEEDS VERIFICATION** | Schema/contract update and tests. |
| GEO-PKG-025 | Strengthen TileArtifactManifest schema or bound adapter support. | **NEEDS VERIFICATION** | Schema/contract update and tests. |
| GEO-PKG-026 | Strengthen KFMGeoManifest schema or bound adapter support. | **NEEDS VERIFICATION** | Schema/validator/fixture update and tests. |
| GEO-PKG-027 | Decide generated-code strategy. | **NEEDS DECISION** | Generator/version/provenance/round-trip plan. |
| GEO-PKG-028 | Select geometry dependency, if any. | **NEEDS DECISION** | Capability, license, security, platform, rollback review. |
| GEO-PKG-029 | Select CRS/transform dependency, if any. | **NEEDS DECISION** | Capability, grid/resource, accuracy, offline, rollback review. |
| GEO-PKG-030 | Define native-library support matrix. | **NEEDS VERIFICATION** | Platform CI and binary provenance. |
| GEO-PKG-031 | Define projection-grid and EPSG database policy. | **NEEDS DECISION** | Resource registry, hashes, rights, offline behavior. |
| GEO-PKG-032 | Define hidden-network prohibition tests. | **NEEDS VERIFICATION** | No-network test harness. |
| GEO-PKG-033 | Define resource and complexity limits. | **NEEDS DECISION** | Limit contract and adversarial tests. |
| GEO-PKG-034 | Define geometry repair posture. | **NEEDS DECISION** | Separate explicit repair contract and provenance rules. |
| GEO-PKG-035 | Define transform receipt/proof handoff. | **NEEDS DECISION** | Contract and receipt integration. |
| GEO-PKG-036 | Define geoprivacy decision handoff. | **NEEDS DECISION** | Policy contract and public-safe tests. |
| GEO-PKG-037 | Define correction invalidation behavior. | **NEEDS DECISION** | Correction contract and tests. |
| GEO-PKG-038 | Define package-specific test root. | **NEEDS DECISION** | Directory Rules check and accepted test README. |
| GEO-PKG-039 | Define package-specific fixture root. | **NEEDS DECISION** | Directory Rules check and accepted fixture README. |
| GEO-PKG-040 | Add substantive Geo CI. | **NEEDS VERIFICATION** | Workflow with build, import, unit, property, no-network, security, and platform checks. |
| GEO-PKG-041 | Add independent validator coverage. | **NEEDS VERIFICATION** | Validator implementations and negative fixtures. |
| GEO-PKG-042 | Define supported package serialization stability. | **NEEDS DECISION** | Compatibility contract and golden tests. |
| GEO-PKG-043 | Define deprecation and breaking-change policy. | **NEEDS DECISION** | Package versioning policy. |
| GEO-PKG-044 | Define reproducible build and SBOM posture. | **NEEDS DECISION** | Release workflow, attestations, artifact checks. |
| GEO-PKG-045 | Define package publication repository and signing. | **NEEDS DECISION** | Release architecture and credentials governance. |
| GEO-PKG-046 | Verify public clients never import package internals. | **NEEDS VERIFICATION** | Dependency graph and runtime/API tests. |
| GEO-PKG-047 | Verify no protected coordinates enter fixtures, logs, or errors. | **NEEDS VERIFICATION** | Security/geoprivacy tests and review. |
| GEO-PKG-048 | Test correction, supersession, withdrawal, and rollback integration. | **NEEDS VERIFICATION** | End-to-end governed flow. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Truth label | Supports | Limits |
|---|---|---|---|
| Current target blob `ba61bc82...` | **CONFIRMED** | Package README existed as a planning-oriented v1 document. | Does not prove implementation. |
| [`pyproject.toml`](./pyproject.toml) blob `ad9241a7...` | **CONFIRMED** | Distribution name `kfm-geo` and version `0.0.0`. | Does not establish build, dependencies, discovery, install, or publication. |
| [`src/README.md`](./src/README.md) blob `6f53a525...` | **CONFIRMED** | Source-root v0.2 structural contract and bounded package inventory. | Documentation is not runtime proof. |
| [`src/geo/README.md`](./src/geo/README.md) blob `70d58bc2...` | **CONFIRMED** | Module v0.2 semantic and governance boundary. | Proposed interfaces are not implemented API proof. |
| `src/geo/__init__.py` blob `e69de29b...` | **CONFIRMED** | Import package marker exists and is empty. | Does not prove build discovery or supported imports. |
| Exact 404 checks | **CONFIRMED bounded absence** | `package.json`, `CHANGELOG.md`, `py.typed`, package test/fixture READMEs, and `geo.yml` were not found at checked paths. | Does not rule out differently named equivalents without a full tree audit. |
| Directory Rules v1.4 blob `2affb080...` | **CONFIRMED doctrine** | `packages/` is shared implementation; authority roots remain separate. | Specific future paths still require verification. |
| Spatial Foundation architecture blob `8e6ec163...` | **CONFIRMED authored doctrine / mixed implementation posture** | Cross-domain spatial grammar and authority separation. | Rich object families are not current package implementation proof. |
| MapLibre package README blob `7aff988e...` | **CONFIRMED repo doc** | Verified adjacent renderer-helper lane is `packages/maplibre/`. | Renderer implementation maturity remains separate. |
| MapContextEnvelope schema blob `06a98e4f...` | **CONFIRMED schema scaffold** | Current path and permissive empty shape. | Does not enforce rich semantics. |
| LayerManifest schemas | **CONFIRMED / CONFLICTED** | Three current schema homes and differing minimal/permissive shapes. | No canonical package adapter profile is accepted. |
| LayerManifest contract blob `d2a575cd...` | **CONFIRMED draft contract** | Explicitly records schema-home conflict and rich semantic intent. | Contract exceeds current schema enforcement. |
| TileArtifactManifest schema blob `ed8fb083...` | **CONFIRMED schema scaffold** | Current map-family path and permissive empty shape. | Does not prove complete adapter support. |
| KFMGeoManifest contract/schema blobs | **CONFIRMED draft contract + minimal schema stub** | Artifact-manifest meaning and current machine-shape limits. | Validator and rich enforcement were not proven. |
| Current documentation update | **PROPOSED until merged** | Package boundary, verification register, and admission plan. | Does not create code, metadata, tests, CI, or release behavior. |

[Back to top](#top)

---

## Maintainer checklist

Before adding or approving package behavior:

- [ ] Confirm the responsibility belongs in a shared package.
- [ ] Identify the accepted contract and schema profile.
- [ ] Identify source, evidence, policy, release, correction, and rollback refs that must be preserved.
- [ ] Confirm no hidden source-store or network access.
- [ ] Confirm no policy, geoprivacy, evidence, or release authority is imported.
- [ ] Review dependency, license, native-library, and resource posture.
- [ ] Define complexity and resource limits.
- [ ] Define finite issue behavior.
- [ ] Add synthetic and public-safe positive, negative, and boundary fixtures.
- [ ] Add package, import, no-network, security, and compatibility tests.
- [ ] Add independent validation where output is consequential.
- [ ] Update package, source-root, and module docs as applicable.
- [ ] Define correction, invalidation, and rollback behavior.
- [ ] Verify public consumers remain behind governed APIs and released artifacts.
- [ ] Keep the change small, reversible, and auditable.

[Back to top](#top)

---

## Rollback

Rollback is required if the package:

- becomes a parallel schema, contract, policy, source-registry, lifecycle-data, evidence/proof, receipt, release, API, UI, tile, layer, style, or renderer authority;
- silently guesses CRS, axis order, operation, scale, precision, sensitivity, or public-safe posture;
- silently repairs, coerces, simplifies, or drops geometry information;
- fetches grids, schemas, source data, or registry state from the network without an accepted boundary;
- exposes exact sensitive geometry or stores protected coordinates in fixtures, logs, or errors;
- publishes or permits public map output without evidence, policy, review, release, correction, and rollback support;
- lets public clients call package internals directly;
- claims build, install, typed, compatibility, or publication support that metadata and tests do not prove.

### Documentation rollback

Before merge, close or abandon the package README PR.

After merge, transparently revert the merge or restore the prior blob:

```text
ba61bc82ab405ba731bb843c0e9d25b079e6db5b
```

### Future implementation rollback

A future implementation rollback should:

1. disable affected consumers or feature flags;
2. restore the last accepted package version and dependency/resource set;
3. invalidate derived candidates affected by the defect;
4. preserve source/internal evidence and prior release history;
5. issue correction or withdrawal records where public output was affected;
6. point release systems to a known-safe artifact;
7. preserve receipts, proofs, diagnostics, and review records;
8. document root cause and profile/resource impact;
9. add a regression test before re-admission.

No code, schema, contract, policy, workflow, fixture, proof, receipt, release, deployment, spatial artifact, native resource, or package-registry rollback is required for this README-only revision.

[Back to top](#top)
