<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-geo-src-readme
title: packages/geo/src/ — Governed Geo Package Source Root
type: readme
version: v0.2
status: draft; repository-grounded; python-src-root; implementation-placeholder; non-authoritative
owners:
  - OWNER_TBD — Geo package owner
  - OWNER_TBD — Spatial Foundation steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, sensitivity, and geoprivacy steward
  - OWNER_TBD — Map, release, correction, validator, security, packaging, and docs stewards
created: NEEDS VERIFICATION — target file existed before this revision
updated: 2026-07-15
supersedes: v1 planning-oriented source-directory guide (2026-06-14)
policy_label: public; packages; geo; python; src-layout; CRS; geometry; scale; uncertainty; generalization; no-network-by-default; fail-closed; map-is-carrier; non-authoritative
path: packages/geo/src/README.md
truth_posture: CONFIRMED target and prior blob, kfm-geo 0.0.0 project metadata, Python src layout, geo import package, empty initializer, merged child-module v0.2 contract, planning-oriented parent package README, bounded absence of selected geo helper modules and package.json, bounded absence of package-specific test/fixture READMEs and dedicated geo.yml workflow, verified packages/maplibre helper lane, Directory Rules v1.4, Spatial Foundation doctrine/object-family guidance, current UI MapContextEnvelope schema location and empty permissive shape, three competing LayerManifest schema homes with an explicit data-contract conflict, empty permissive map/layers LayerManifest schemas, minimal data LayerManifest schema, empty permissive TileArtifactManifest schema, KFMGeoManifest contract plus minimal schema stub, and absent schema-declared KFMGeoManifest validator/fixture README at exact tested paths / PROPOSED future explicit package discovery, deliberate exports, pure geospatial primitive helpers, profile-pinned adapters, generated schema models, bounded transform-plan carriers, public-safe candidate assembly from supplied decisions, package tests, and typed marker / CONFLICTED parent README paths versus current schema homes, LayerManifest schema-home split, rich Spatial Foundation and geo-manifest semantics versus permissive/minimal schemas, proposed helper outcomes versus no accepted geo-result contract, maplibre-runtime prose versus verified packages/maplibre lane, and public-safe helper ambitions versus policy authority / UNKNOWN build backend, Python requirement, dependencies, package discovery, license metadata, public exports, consumers, canonical CRS/geometry/scale/uncertainty profiles, transform engine, validator integration, dedicated CI, package publication, runtime/API wiring, and production behavior / NEEDS VERIFICATION accepted owners, ADR/profile decisions, reason-code vocabulary, geoprivacy handoff, transform receipts, correction invalidation, release integration, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: ee77864fff2c28994ab8dc07723955d1ece3dbdb
  prior_blob: 420d38941b3e7e8e4767d7e65fdea0e53f2f91c0
  child_module_blob: 70d58bc2c016fe759db77d2f398b8c0e3c37248d
  pyproject_blob: ad9241a73d73d1c47fe2d29e52594b3961e8b588
  package_readme_blob: ba61bc82ab405ba731bb843c0e9d25b079e6db5b
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
  - ./geo/README.md
  - ./geo/__init__.py
  - ../README.md
  - ../pyproject.toml
  - ../../README.md
  - ../../maplibre/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/architecture/spatial-foundation.md
  - ../../../contracts/data/layer_manifest.md
  - ../../../contracts/evidence/kfm_geo_manifest.md
  - ../../../schemas/contracts/v1/ui/map_context_envelope.schema.json
  - ../../../schemas/contracts/v1/map/layer_manifest.schema.json
  - ../../../schemas/contracts/v1/data/layer_manifest.schema.json
  - ../../../schemas/contracts/v1/layers/layer_manifest.schema.json
  - ../../../schemas/contracts/v1/map/tile_artifact_manifest.schema.json
  - ../../../schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json
tags: [kfm, packages, geo, python, src-layout, source-root, import-boundary, spatial-foundation, CRS, geometry, bbox, scale, uncertainty, generalization, geoprivacy, schema-profile, generated-code, deterministic, no-network, fail-closed, rollback]
notes:
  - "v0.2 replaces stale planning language with a commit-pinned description of the current kfm-geo 0.0.0 Python src-layout scaffold."
  - "The merged geo/README.md v0.2 owns geospatial helper semantics; this file owns source-root, discovery, import, dependency, generated-code, packaging, test-placement, and compatibility boundaries."
  - "The import initializer is empty and selected helper modules are absent; no supported API, build behavior, consumer, CRS engine, geometry validator, transform engine, or runtime integration is claimed."
  - "Spatial doctrine and rich contract prose exceed current permissive/minimal schemas, and LayerManifest has competing schema homes; the source root requires explicit profiles and forbids silent normalization."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Geo Package Source Root

`packages/geo/src/`

> Python `src`-layout container for the `kfm-geo` shared package. This directory may organize reusable, deterministic geospatial primitive implementation, but it must not become spatial meaning, source truth, schema or contract authority, policy execution, geoprivacy authority, lifecycle storage, proof or receipt persistence, release authority, MapLibre rendering, public API routing, UI state, or generated spatial truth.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![distribution](https://img.shields.io/badge/distribution-kfm--geo-3776ab)
![layout](https://img.shields.io/badge/layout-Python%20src--layout-3776ab)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![authority](https://img.shields.io/badge/authority-helper%20only-455a64)
![network](https://img.shields.io/badge/network-none%20by%20default-455a64)
![spatial-truth](https://img.shields.io/badge/map-carrier%20not%20truth-0b7285)

**Quick links:** [Purpose](#purpose-and-audience) · [Status](#current-repository-state) · [Context](#source-root-bounded-context) · [Placement](#placement-and-authority) · [Surface](#current-source-tree) · [Root/module split](#source-root-versus-import-module) · [Package](#relationship-to-the-parent-package) · [Spatial Foundation](#relationship-to-spatial-foundation) · [MapLibre](#relationship-to-maplibre) · [Packaging](#packaging-and-discovery-boundary) · [Imports](#import-and-export-contract) · [Import safety](#import-time-safety) · [Dependencies](#dependency-direction) · [Profiles](#spatial-profile-and-drift-boundary) · [Generated code](#generated-code-and-schema-adapters) · [Resources](#package-data-native-libraries-and-grid-resources) · [Inputs/outputs](#source-root-input-and-output-boundary) · [Trust](#lifecycle-evidence-policy-release-and-public-safety) · [Tests](#tests-fixtures-validators-and-ci) · [Security](#security-resource-limits-and-observability) · [Evolution](#proposed-source-tree-evolution) · [Compatibility](#compatibility-correction-and-rollback) · [Validation](#validation-commands) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Repository snapshot:** `main@ee77864fff2c28994ab8dc07723955d1ece3dbdb`<br>
> **Distribution:** `kfm-geo`<br>
> **Declared version:** `0.0.0`<br>
> **Verified source root:** `src/`<br>
> **Verified import package:** `src/geo/`<br>
> **Verified implementation:** empty `geo/__init__.py`; selected helper modules are absent<br>
> **Verified child contract:** [`geo/README.md`](./geo/README.md) v0.2<br>
> **Build backend, Python requirement, dependencies, package discovery, exports, consumers, and package publication:** not established<br>
> **Map/context/manifest schemas:** present but permissive or minimal `PROPOSED` scaffolds<br>
> **LayerManifest schema home:** conflicted across `map/`, `data/`, and `layers/` families<br>
> **Dedicated geo workflow:** not found at the exact checked `.github/workflows/geo.yml` path

> [!CAUTION]
> A `src` directory does not confer authority. Package discovery does not prove semantics. A parsed geometry is not spatial truth. A successful transform is not a release. A generalized geometry is not automatically public-safe. Source code may produce candidates and issues; governed contracts, evidence, policy, review, release, correction, and public interfaces decide what may be used or shown.

---

## Purpose and audience

`packages/geo/src/` is the implementation container for the Python project declared by [`../pyproject.toml`](../pyproject.toml).

Its durable responsibilities are structural:

- contain importable source for the `geo` package;
- make package discovery and import boundaries explicit;
- provide a stable home for reusable, no-network geospatial primitive helper code;
- keep exports deliberate, small, versioned, and reviewable;
- keep import-time behavior deterministic and side-effect-free;
- preserve explicit CRS, geometry, scale, precision, uncertainty, transform, evidence, policy, release, correction, and rollback context supplied by callers;
- keep generated models subordinate to accepted contracts and schemas;
- keep implementation separate from source connectors, lifecycle data, policy engines, geoprivacy decisions, proof/receipt stores, release systems, API routes, UI/MapLibre rendering, and model providers;
- support deterministic, synthetic, sanitized, public-safe tests without storing protected coordinates or production spatial data in source.

This README is for Geo package maintainers, Spatial Foundation and map stewards, contract/schema/policy/release reviewers, geoprivacy and security reviewers, governed API and MapLibre maintainers, validator/test maintainers, packaging reviewers, and maintainers deciding whether proposed code belongs in this source root.

Detailed geospatial helper semantics belong in [`geo/README.md`](./geo/README.md). This source-root README governs the container, discovery, import surface, dependency direction, generated-code boundary, static-resource posture, test placement, packaging posture, compatibility, and enforceability placement.

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
| Base commit | `ee77864fff2c28994ab8dc07723955d1ece3dbdb` |
| Prior target blob | `420d38941b3e7e8e4767d7e65fdea0e53f2f91c0` |
| Child module blob | `70d58bc2c016fe759db77d2f398b8c0e3c37248d` |
| Project metadata blob | `ad9241a73d73d1c47fe2d29e52594b3961e8b588` |
| Import initializer blob | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| Current revision | documentation-only source-root v0.2 proposal |

### Verified source-root surface

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---:|---|
| This README | Existing v1 planning-oriented source guide. | **CONFIRMED** | Revised in place. |
| [`../pyproject.toml`](../pyproject.toml) | Declares `[project]`, name `kfm-geo`, and version `0.0.0` only. | **CONFIRMED minimal placeholder** | Distribution identity is known; build and dependency behavior are not. |
| [`geo/README.md`](./geo/README.md) | Merged repository-grounded source-module contract v0.2. | **CONFIRMED** | Detailed CRS, geometry, transform, manifest, and geoprivacy boundaries live there. |
| `geo/__init__.py` | Exists and is empty. | **CONFIRMED** | Import-package marker only; no supported exports are established. |
| `package.json` | Absent at `packages/geo/package.json` during the bounded package check. | **CONFIRMED bounded absence** | Do not claim a JavaScript/TypeScript package. |
| Selected helper files | `crs.py`, `geometry.py`, `public_safe.py`, and `validation.py` were absent at exact tested paths. | **CONFIRMED bounded absence** | No executable Geo implementation is established. |
| Build backend | No `[build-system]` section was observed. | **NOT OBSERVED** | Build/install behavior remains unknown. |
| Dependencies | No dependency list was observed. | **NOT OBSERVED** | Do not claim `pyproj`, `shapely`, GDAL, PROJ, or other spatial dependencies. |
| Supported Python versions | No `requires-python` field was observed. | **NOT OBSERVED** | Interpreter support is unknown. |
| Package discovery | No explicit discovery configuration was observed. | **NOT OBSERVED** | Do not claim editable install or wheel inclusion works. |
| Public exports | Empty initializer. | **NOT ESTABLISHED** | No symbol is part of a supported package API. |
| Consumers | Indexed checks did not establish production imports of `geo`. | **NOT OBSERVED / search-limited** | Do not claim runtime or API integration. |
| Parent package README | `packages/geo/README.md` exists and remains planning-oriented v1. | **CONFIRMED README / stale implementation posture** | Package-level responsibility is described, but current maturity is not grounded there yet. |
| MapLibre package | `packages/maplibre/README.md` exists. | **CONFIRMED helper lane** | Renderer/source/layer descriptor helpers stay outside this source root. |
| MapContext schema | `schemas/contracts/v1/ui/map_context_envelope.schema.json` exists with empty properties and `additionalProperties: true`. | **CONFIRMED permissive scaffold / `PROPOSED`** | Source code cannot infer a stable MapContext payload contract. |
| Map LayerManifest schema | `schemas/contracts/v1/map/layer_manifest.schema.json` exists with empty properties and `additionalProperties: true`. | **CONFIRMED permissive scaffold / `PROPOSED`** | It does not enforce rich layer semantics. |
| Data LayerManifest schema | `schemas/contracts/v1/data/layer_manifest.schema.json` requires `id`, offers optional `version` and `spec_hash`, and allows additional properties. | **CONFIRMED minimal scaffold / `PROPOSED`** | It is the only current LayerManifest profile paired to a semantic contract. |
| Layers LayerManifest schema | `schemas/contracts/v1/layers/layer_manifest.schema.json` exists with empty properties and `additionalProperties: true`. | **CONFIRMED permissive scaffold / `PROPOSED`** | It competes with other schema homes. |
| LayerManifest contract | `contracts/data/layer_manifest.md` explicitly records the schema-home conflict. | **CONFIRMED conflict register** | Source adapters must pin a selected profile and cannot silently translate. |
| TileArtifactManifest schema | `schemas/contracts/v1/map/tile_artifact_manifest.schema.json` is an empty permissive `PROPOSED` scaffold. | **CONFIRMED** | No stable tile-manifest adapter API is established. |
| KFMGeoManifest contract/schema | Rich draft contract plus minimal schema requiring only `id`, with optional `version`/`spec_hash` and additional properties allowed. | **CONFIRMED semantic/schema gap** | Rich manifest construction remains proposed. |
| KFMGeoManifest validator | Schema declares `tools/validators/evidence/validate_kfm_geo_manifest.py`; exact file was absent. | **CONFLICTED metadata / file state** | Source code must not claim dedicated validator availability. |
| KFMGeoManifest fixture README | Absent at the exact checked `fixtures/evidence/kfm_geo_manifest/README.md` path. | **CONFIRMED bounded absence** | Fixture coverage is not established there. |
| Package test README | `tests/packages/geo/README.md` was absent at the exact checked path. | **CONFIRMED bounded absence** | No package-specific test lane is documented there. |
| Package fixture README | `fixtures/packages/geo/README.md` was absent at the exact checked path. | **CONFIRMED bounded absence** | No package-specific fixture lane is documented there. |
| Dedicated workflow | `.github/workflows/geo.yml` was absent at the exact checked path. | **CONFIRMED bounded absence** | No Geo behavior workflow is established. |
| Runtime/release evidence | No deployed consumer, runtime log, transform receipt, Geo package artifact, or released spatial output was inspected. | **UNKNOWN** | This README is not implementation or deployment proof. |

```text
Python distribution identity          = CONFIRMED
Python src-layout container            = CONFIRMED
geo import package                     = CONFIRMED
empty initializer                      = CONFIRMED
implemented geo modules                = NOT OBSERVED at selected paths
supported public exports               = NOT ESTABLISHED
package consumers                      = NOT OBSERVED
build/install behavior                 = UNKNOWN
package-specific tests/fixtures        = NOT ESTABLISHED
spatial contracts/schemas              = PRESENT, mostly PROPOSED scaffolds
LayerManifest schema home              = CONFLICTED
geo result contract                    = NOT ESTABLISHED
dedicated Geo workflow                 = NOT FOUND at tested path
runtime/API behavior                   = UNKNOWN
release behavior                       = UNKNOWN
```

[Back to top](#top)

---

## Source-root bounded context

The source-root bounded context is:

> The organization and admission boundary for importable, reusable geospatial primitive helper implementation.

It includes:

- source-tree structure;
- package discovery;
- import-module placement;
- supported exports;
- dependency direction;
- import-time safety;
- generated-code placement;
- CRS/geometry/scale/uncertainty profile adapter placement;
- transform-plan and issue-carrier placement;
- static package-data and native dependency posture;
- package tests and fixtures integration;
- packaging, distribution, compatibility, and deprecation posture.

It excludes:

- Spatial Foundation semantic meaning;
- CRS or coordinate-operation policy;
- canonical geometry schema shape;
- source descriptors and source-role authority;
- lifecycle spatial data;
- EvidenceBundle closure;
- geoprivacy, sensitivity, rights, or audience decisions;
- transform approval or transform receipt persistence;
- map/layer/tile release approval;
- MapLibre rendering or app state;
- public API serialization;
- AI-generated place or geometry claims.

[Back to top](#top)

---

## Placement and authority

Directory Rules place reusable implementation under `packages/`. The existing path is therefore appropriate for an importable shared library **if** a stable cross-consumer need is verified.

```text
packages/geo/src/
```

| Concern | Authority here |
|---|---|
| Source-tree organization | **Yes.** This README defines structural expectations. |
| Import package and exports | **Supporting authority**, once implemented and tested. |
| Spatial Foundation meaning | **No.** Cross-domain doctrine and accepted contracts own meaning. |
| CRS/geometry machine shape | **No.** Accepted schemas own shape. |
| Source scale, accuracy, and limitations | **No.** Source descriptors and evidence records own them. |
| Geoprivacy and exact-location disclosure | **No.** Policy and geoprivacy systems own decisions. |
| Evidence closure | **No.** EvidenceBundle and resolver lanes own closure. |
| Transform approval | **No.** Accepted transform specs, policy, validation, review, and receipts own approval. |
| Layer/tile/map release | **No.** Release manifests and promotion records own publication state. |
| Map rendering | **No.** `packages/maplibre/` and app/UI roots own renderer-facing behavior. |
| Spatial storage | **No.** Lifecycle and artifact roots own bytes and records. |

The source root may make implementation importable. It cannot make implementation authoritative.

### Placement test

A proposed file belongs under this source root only when all answers are **yes**:

1. Is it reusable implementation rather than semantic meaning, policy, data, a proof, a receipt, or a release record?
2. Is it generic across more than one domain or consumer?
3. Can it run without hidden network access or lifecycle-store access?
4. Does it consume explicit accepted profiles instead of inventing CRS, geometry, scale, or sensitivity semantics?
5. Can its behavior be tested deterministically with synthetic or sanitized public-safe fixtures?
6. Does it return candidate values or issues rather than policy, release, or truth decisions?
7. Does it preserve source/internal, derived, and public geometry as distinct values?
8. Does it avoid duplicating MapLibre, domain, pipeline, validator, policy, or release responsibility?

A **no** answer means the file belongs elsewhere or requires an ADR/profile decision first.

[Back to top](#top)

---

## Current source tree

### Verified tree

```text
packages/geo/src/
├── README.md
└── geo/
    ├── README.md
    └── __init__.py
```

This is the complete source-root surface established by the bounded exact-path checks used for this revision.

### Not established

The repository evidence used here does not establish:

- a build backend;
- package discovery configuration;
- supported Python versions;
- dependency metadata;
- a typed-package marker;
- generated models;
- CRS, geometry, bbox, scale, uncertainty, transform, issue, manifest, or public-safe modules;
- public exports;
- production consumers;
- package-specific tests or fixtures;
- a dedicated Geo workflow;
- package publication;
- runtime wiring.

Do not turn the proposed future tree later in this README into a claim that these files already exist.

[Back to top](#top)

---

## Source root versus import module

The source-root and import-module READMEs have different responsibilities.

| Surface | Owns | Does not own |
|---|---|---|
| `packages/geo/src/README.md` | Source layout, discovery, import boundaries, dependency direction, generated-code placement, package-data posture, test placement, packaging, compatibility, and admission sequence. | Detailed CRS/geometry/transform helper semantics. |
| `packages/geo/src/geo/README.md` | Module bounded context, geospatial terminology, explicit candidate semantics, CRS/geometry/scale/uncertainty/transform rules, geoprivacy boundary, failure posture, and proposed module interface. | Build metadata, package discovery, release storage, policy, public APIs, or renderer authority. |
| `packages/geo/README.md` | Package-level mission, consumers, package relationships, distribution strategy, and lifecycle/trust posture. | Source-file detail or implementation proof. |

The merged child module contract is the detailed source-behavior reference. This source-root README must not copy every helper rule and then drift independently.

### Required consistency

When one layer changes, reviewers must check the other two:

- changing distribution or source layout affects package and source-root docs;
- changing imports or exports affects all three docs and consumers;
- changing candidate/result semantics affects the module doc, contracts/schemas, tests, and callers;
- changing package responsibility may require an ADR and migration plan;
- changing geoprivacy or release posture requires policy/release review, not only package edits.

[Back to top](#top)

---

## Relationship to the parent package

The parent package README remains planning-oriented and does not yet reflect the merged module v0.2 contract.

Until the parent README is grounded:

- this source root must not claim package-level consumer commitments;
- the module must not publish a supported API by documentation alone;
- distribution/version claims remain limited to `kfm-geo` `0.0.0` metadata;
- package-purpose and dependency decisions remain reviewable proposals;
- source-root changes should be small and reversible.

The package-level boundary should eventually reconcile:

- whether `kfm-geo` is intended for internal monorepo use, publication, or both;
- which consumers justify a shared package;
- whether domain-specific geometry belongs in domain packages;
- where transform execution belongs;
- how geoprivacy and generalization hand off to policy;
- how MapLibre adapters consume released spatial candidates;
- what compatibility and deprecation policy applies.

[Back to top](#top)

---

## Relationship to Spatial Foundation

`docs/architecture/spatial-foundation.md` provides cross-domain vocabulary and doctrine. This source root may implement accepted primitives that support that doctrine; it does not own the doctrine.

### Doctrine versus implementation

| Spatial Foundation concern | Source-root posture |
|---|---|
| Coordinate Reference Profile | May host a profile-bound carrier or adapter after contract/schema acceptance. |
| GeographyVersion | Does not own registry records; may parse or preserve explicit refs. |
| Projection Transform Receipt | Does not persist receipts; may produce deterministic receipt **candidates** after an accepted transform contract. |
| Geometry Fingerprint | May call accepted hashing helpers with explicit canonicalization; does not invent the profile. |
| Base Layer Descriptor | Does not own source/layer registry or MapLibre descriptor semantics. |
| MapStyleRule | Does not belong here; style/MapLibre/UI roots own it. |
| Scale Support Profile | May host pure checks after profile acceptance. |
| Spatial Uncertainty | May carry explicit uncertainty values; domain-specific meaning remains with domain/contracts. |
| Generalization Transform | May represent or execute only an accepted pure transform with policy/receipt context; approval remains outside. |

Rich doctrinal vocabulary is not an executable contract. A Python class must not be added merely because a term appears in architecture prose.

[Back to top](#top)

---

## Relationship to MapLibre

The verified adjacent helper lane is:

```text
packages/maplibre/
```

The Geo source root should provide renderer-neutral spatial primitives. MapLibre-specific source, layer, style, expression, event, camera, and interaction behavior belongs in the MapLibre package or app/UI roots.

### Allowed dependency direction

```text
packages/maplibre or governed app
  -> packages/geo
  -> accepted contracts/schemas and lower-level deterministic helpers
```

Blocked direction:

```text
packages/geo
  -X-> packages/maplibre renderer implementation
  -X-> app/UI components
  -X-> public API routes
  -X-> released tile/layer lookup
```

Geo may produce a bounded geometry, bbox, CRS, transform, scale, uncertainty, or issue candidate. It must not produce MapLibre layers as a hidden renderer adapter.

Parent prose that names `packages/maplibre-runtime/` remains **CONFLICTED / NEEDS VERIFICATION** against the current verified `packages/maplibre/` lane.

[Back to top](#top)

---

## Packaging and discovery boundary

### Confirmed metadata

The current project metadata is only:

```toml
[project]
name = "kfm-geo"
version = "0.0.0"
```

This confirms a proposed Python distribution identity. It does **not** confirm a buildable or installable package.

### Missing packaging decisions

The checked metadata does not establish:

- `[build-system]`;
- build backend;
- `requires-python`;
- runtime dependencies;
- optional dependency groups;
- license metadata;
- authors/maintainers;
- package discovery;
- package data;
- entry points;
- wheel/sdist configuration;
- typed-package declaration;
- publication registry;
- release automation.

### Discovery rule

The physical `src/geo/` directory and `__init__.py` make the import package structurally plausible. They do not prove a built wheel includes it.

Before any install/import claim is accepted, tests must demonstrate:

1. a clean build from the package directory;
2. wheel inspection contains the intended `geo` files and no unintended data;
3. installation into a clean environment;
4. import from outside the repository checkout;
5. no accidental import from the working tree;
6. deterministic version metadata;
7. license and notice inclusion for dependencies and any static resources.

### Name-collision risk

`geo` is a broad import name. Before publication or broad internal adoption, verify:

- collision with existing third-party distributions or local packages;
- import ambiguity in monorepo tooling;
- whether a KFM-prefixed import namespace is preferable;
- migration cost if the namespace changes after consumers appear.

The current README does not decide the namespace migration question.

[Back to top](#top)

---

## Import and export contract

### Current contract

`geo/__init__.py` is empty. Therefore:

```text
supported root exports = none established
```

Consumers must not infer that names proposed in documentation are importable.

### Future export requirements

Any supported export must be:

- backed by an accepted contract/profile;
- implemented in a named module;
- type-annotated;
- deterministic for the same explicit inputs and dependency versions;
- no-network by default;
- side-effect-free at import time;
- covered by positive, negative, ambiguity, resource-limit, and sensitive-location tests;
- documented with failure and compatibility behavior;
- reviewed for dependency and native-library implications;
- added deliberately to `geo/__init__.py` only when root-level convenience is justified.

### No wildcard API

Do not populate `__init__.py` using broad wildcard imports or automatic module scanning.

Prefer explicit exports:

```python
# PROPOSED illustration only; no current API is established.
from .issues import GeoIssue
from .profiles import GeoProfileRef

__all__ = ["GeoIssue", "GeoProfileRef"]
```

Even this minimal illustration requires accepted object profiles and tests before implementation.

### Internal modules

Private or generated modules should not become accidental API through documentation, re-export, reflection, or star imports. Use clear private naming and test the public import surface.

[Back to top](#top)

---

## Import-time safety

Importing `geo` must not:

- access the network;
- download CRS definitions or transformation grids;
- inspect system PROJ/GDAL data directories as authority;
- read environment variables as spatial truth or policy;
- read source, registry, lifecycle, proof, receipt, or release stores;
- open files from the current working directory;
- initialize database or HTTP clients;
- instantiate model providers;
- mutate global CRS or geometry-library configuration;
- suppress warnings globally;
- register logging handlers;
- emit telemetry;
- execute transformations;
- scan plugins dynamically;
- generate schemas or code;
- create directories or cache files.

### Allowed import-time behavior

Import-time behavior should be limited to:

- definitions;
- immutable constants derived from accepted local profiles;
- lightweight type aliases;
- explicit exception and issue classes;
- version metadata that does not require repository or network access.

### Lazy dependency posture

Optional heavy or native dependencies should be imported only inside the functions or adapters that require them, with typed, stable unavailable-dependency issues. Lazy import must not silently change semantics.

[Back to top](#top)

---

## Dependency direction

### Preferred direction

```text
governed apps / packages / pipelines / validators
                     |
                     v
              packages/geo
                     |
                     v
 accepted generated types + identity/hashing helpers + standard library
```

### Allowed dependency characteristics

Dependencies should be:

- necessary for accepted behavior;
- pinned through repository dependency controls;
- license-compatible;
- security-scanned;
- deterministic under supported versions;
- usable without network access for normal helper operations;
- explicit about native libraries and data-resource requirements;
- bounded against adversarial geometry and resource exhaustion;
- isolated behind adapters where implementation-specific behavior can drift.

### Disallowed direction

This source root must not depend on:

- connectors;
- source activation code;
- lifecycle storage clients;
- evidence/proof stores;
- policy engines as hidden global services;
- release writers;
- public API routers;
- UI or MapLibre rendering components;
- model-provider clients;
- mutable runtime singletons;
- domain packages for generic primitive behavior.

### Spatial dependency decisions remain open

No current metadata establishes `pyproj`, `shapely`, GDAL, rasterio, GeoPandas, or other spatial libraries. Do not document their behavior as package behavior until dependency selection, supported versions, native data, security posture, and test matrices are accepted.

### Dependency cycles

The package must remain below domain and renderer packages in the dependency graph. A cycle such as `geo -> maplibre -> geo` or `geo -> domain -> geo` is a design failure requiring refactoring or an ADR.

[Back to top](#top)

---

## Spatial profile and drift boundary

Source code must bind behavior to explicit accepted profiles. Generic names such as `validate_geometry`, `normalize_crs`, or `make_public_safe` are unsafe when the governing profile is implicit.

### Required profile families before mature implementation

| Profile family | Required decisions |
|---|---|
| CRS reference | Identifier grammar, authority/version, axis order, units, datum, vertical reference, epoch, deprecation handling. |
| Coordinate operation | Source/target CRS, operation identifier, grid/resource requirements, area of use, accuracy, ballpark/fallback policy. |
| Geometry representation | Supported encodings, geometry types, dimensions, emptiness, finite coordinates, ring/topology rules, antimeridian behavior. |
| Bbox/extent | Axis order, wrapped extents, dimensionality, containment semantics, empty/unknown behavior. |
| Scale/precision | Source scale, representation scale, resolution, significant precision, tolerance, false-precision rules. |
| Uncertainty | Units, confidence/coverage meaning, propagation rules, source versus derived uncertainty. |
| Transform/generalization | Algorithm, parameters, version, topology behavior, error budget, receipt fields, reversibility/lineage. |
| Public-safe geometry | Policy decision input, audience, obligations, output class, reconstruction risk, denial/withholding behavior. |
| Issue/result | Stable codes, severity, path/location, deterministic ordering, retryability, public-safe detail. |

### Current schema limitations

The current MapContext, map LayerManifest, layers LayerManifest, and TileArtifactManifest schemas have empty property sets with `additionalProperties: true`. The data LayerManifest and KFMGeoManifest schemas are minimal and permissive.

Therefore this source root must not claim those schemas define:

- CRS fields;
- geometry fields;
- bbox semantics;
- scale/uncertainty fields;
- transform records;
- public-safe classes;
- release readiness;
- finite helper outcomes.

### LayerManifest conflict

Three LayerManifest schema homes coexist:

```text
schemas/contracts/v1/map/layer_manifest.schema.json
schemas/contracts/v1/data/layer_manifest.schema.json
schemas/contracts/v1/layers/layer_manifest.schema.json
```

Before generating models or adapters, an ADR, migration note, or explicit compatibility profile must identify:

- the canonical profile;
- whether the others are compatibility shells;
- version identifiers;
- information-loss rules;
- deprecation and rollback plan;
- fixture/validator ownership.

Unknown profile combinations must fail visibly. Silent field copying between permissive schemas is not compatibility.

[Back to top](#top)

---

## Generated code and schema adapters

Generated code may be appropriate after schemas are accepted and stable enough to justify it. Generation must remain subordinate to schema authority.

### Proposed placement

```text
packages/geo/src/geo/_generated/   # PROPOSED only
```

Do not create this directory until the generator, source schemas, ownership, and drift checks are accepted.

### Generated artifact requirements

Each generated file must record or resolve to:

- source schema path and `$id`;
- source schema digest;
- generator name and version;
- generation command/profile;
- generation timestamp policy;
- compatibility version;
- review or receipt reference where required;
- warning that the file is generated;
- regeneration and rollback instructions.

### Generation prohibitions

Generated models must not:

- merge the three LayerManifest profiles silently;
- invent missing spatial fields from prose;
- treat permissive schemas as rich validation;
- embed policy outcomes as defaults;
- convert unknown CRS or axis order into WGS84;
- turn `additionalProperties: true` into an undocumented acceptance policy;
- hide information loss;
- be hand-edited without regeneration.

### Adapter rule

Adapters between accepted versions must be explicit and directional. Each must report:

- source and target profile;
- preserved fields;
- transformed fields;
- dropped or defaulted fields;
- unsupported cases;
- deterministic issues;
- whether round-trip equivalence is expected.

[Back to top](#top)

---

## Package data, native libraries, and grid resources

Spatial tooling can depend on static databases, projection grids, native libraries, and environment-specific resources. None are established for this package.

### Default posture

The source root should contain Python source and small package metadata only. Do not add large CRS databases, transformation grids, sample datasets, tiles, rasters, vector data, protected coordinates, native binaries, or generated artifacts by convenience.

### Admission requirements for static resources

Any proposed package data requires:

- a demonstrated runtime need;
- Directory Rules placement review;
- rights and redistribution review;
- source and version provenance;
- checksums;
- sensitivity review;
- deterministic lookup behavior;
- size and performance assessment;
- offline behavior tests;
- update/correction/rollback plan;
- package manifest and wheel-content tests.

### Network-grid prohibition

A helper must not silently download transformation grids or CRS resources. If an accepted transform requires a missing resource, return a stable unavailable-resource issue. A caller may arrange governed resource provisioning outside this package.

### Native dependency boundary

If native dependencies are adopted, package/release documentation must specify supported platforms, ABI/version constraints, supply-chain scanning, licensing, and reproducible installation. Native-library presence must not alter output silently without profile/version disclosure.

[Back to top](#top)

---

## Source-root input and output boundary

### Accepted implementation inputs

Source modules may consume explicit values such as:

- accepted profile identifiers;
- CRS references and coordinate-operation references;
- geometry candidates represented by accepted types;
- bbox/extent candidates;
- source and representation scale;
- precision, tolerance, and uncertainty values;
- transform-plan inputs;
- supplied policy/geoprivacy decisions and obligations;
- evidence, validation, review, release, correction, and rollback refs;
- deterministic resource and dependency-version context.

They must not fetch missing facts from the network, source systems, canonical stores, registries, UI state, operator memory, or generated language.

### Permitted implementation outputs

Source modules may return:

- immutable or typed candidate values;
- explicit normalized representations under a selected profile;
- deterministic local inspection results;
- issue collections;
- transform-plan candidates;
- derived/generalized geometry candidates kept separate from source geometry;
- manifest/context fragments only for an accepted target profile;
- receipt **candidates** for an owning system to persist;
- public-safe candidate payloads only from supplied policy decisions and obligations.

### Prohibited outputs

Source modules must not emit or persist:

- policy decisions;
- release approval;
- EvidenceBundle closure;
- public API envelopes as authoritative responses;
- MapLibre layers/styles as hidden renderer behavior;
- lifecycle writes;
- proof or receipt records directly;
- source-registry updates;
- public map artifacts;
- uncited spatial claims;
- silently repaired or guessed geometry;
- exact sensitive locations without explicit governed authorization.

[Back to top](#top)

---

## Lifecycle, evidence, policy, release, and public safety

The package participates only as reusable implementation support inside the governed lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

It does not own any lifecycle state transition.

### Lifecycle rules

- Source code must not read RAW, WORK, QUARANTINE, or unpublished stores directly.
- Source code must not write PROCESSED, CATALOG, TRIPLET, or PUBLISHED records.
- Promotion is a governed state transition, not a helper return value.
- Derived geometry remains derived and must preserve lineage.
- Correction and supersession refs must remain visible where outputs can affect downstream artifacts.

### Evidence rules

- Geometry validity does not prove a spatial claim.
- A bbox, CRS, or transform result is not EvidenceBundle closure.
- Derived/generalized geometry must preserve evidence and transform refs supplied by callers.
- Missing evidence context must not be replaced by computation or plausible defaults.
- Public clients resolve evidence through governed interfaces, not package internals.

### Policy and geoprivacy rules

- The package does not decide sensitivity, rights, audience, exact-location access, generalization, redaction, withholding, deny, or abstain.
- Public-safe transformation requires an explicit supplied decision/profile.
- Style filters are not a geoprivacy control.
- Rare species, archaeology, infrastructure, private-property, living-person, and culturally sensitive locations require fail-safe treatment.
- Unknown sensitivity or reconstruction risk must fail closed.

### Release rules

- Local validation is not release approval.
- A manifest-shaped fragment is not a ReleaseManifest.
- Released artifacts and rollback targets remain under release/lifecycle authority.
- Package output must preserve release/correction/rollback refs supplied by callers.

### Public interface rules

Public and normal UI clients must use governed APIs and released artifacts. They must not import `geo`, call package internals as authority, or infer publication permission from local geometry validity.

[Back to top](#top)

---

## Tests, fixtures, validators, and CI

### Current posture

No package-specific Geo test README, fixture README, or dedicated `geo.yml` workflow was established at the exact checked paths. General repository workflows do not prove Geo behavior.

### Required test layers

A mature package should have separate tests for:

1. **Package/distribution behavior**
   - clean build;
   - wheel contents;
   - clean-environment install;
   - import outside checkout;
   - public export snapshot;
   - package-data inventory;
   - version metadata.

2. **Pure module behavior**
   - explicit profiles;
   - valid/invalid representations;
   - ambiguous CRS and axis order;
   - non-finite and empty geometries;
   - bbox wrapping/containment;
   - scale, precision, and uncertainty;
   - deterministic issue ordering;
   - source/derived/public geometry separation.

3. **Transform behavior**
   - explicit operation selection;
   - missing grids/resources;
   - area-of-use violations;
   - accuracy and ballpark restrictions;
   - antimeridian and polar cases;
   - topology and dimensionality;
   - deterministic receipt candidates;
   - no network fallback.

4. **Geoprivacy behavior**
   - supplied allow/generalize/redact/withhold/deny obligations;
   - unknown policy context;
   - reconstruction-risk cases;
   - protected-location fixtures;
   - no exact-coordinate leakage in issues/logs.

5. **Contract/schema adapters**
   - selected schema `$id` and digest;
   - LayerManifest profile conflicts;
   - information-loss reporting;
   - permissive-schema limitations;
   - generated-model drift;
   - unknown profiles fail visibly.

6. **Resource and security limits**
   - coordinate-count limits;
   - nesting/collection limits;
   - pathological topology inputs;
   - oversized strings/properties;
   - timeout/cancellation behavior;
   - bounded issue payloads.

### Fixture safety

Fixtures must be synthetic or sanitized and public-safe. Do not use precise protected coordinates, private-property details, living-person locations, source credentials, restricted datasets, or production proof records.

### Validator separation

Validators under `tools/validators/` may validate contract/schema instances. Package tests validate helper behavior. Neither substitutes for the other.

The schema-declared KFMGeoManifest validator is absent at the exact checked path; do not claim it runs.

### CI acceptance

A green generic workflow is not Geo behavior proof. A future Geo workflow must run real package build/import/tests, no-network checks, dependency/security scans, and profile drift checks. Echo-only jobs do not count.

[Back to top](#top)

---

## Security, resource limits, and observability

### Threats to address

Spatial helpers must be reviewed for:

- denial of service from huge or deeply nested geometries;
- pathological topology or coordinate sequences;
- decompression or parser bombs in adapters;
- native-library vulnerabilities;
- malformed CRS strings or operation definitions;
- unsafe file/URL adapters;
- implicit network grid retrieval;
- environment-dependent transformation behavior;
- coordinate leakage through exceptions or logs;
- reconstruction of protected locations from generalized output;
- false precision or uncertainty suppression;
- dependency confusion caused by the broad `geo` import name.

### Resource bounds

Accepted profiles should define limits for:

- coordinate count;
- geometry collection depth;
- property count and size;
- dimensionality;
- numeric magnitude and finiteness;
- transform operation count;
- output amplification;
- issue count and message size;
- execution time and cancellation.

Exceeding limits should produce deterministic typed issues, not partial or silently truncated trusted output.

### Logging and telemetry

Package code should not configure logging or emit telemetry by default. Callers may log public-safe issue codes and bounded metadata. Logs must avoid exact sensitive coordinates, raw geometry, private source refs, hidden policy context, credentials, and full payloads.

### Error detail

Developer diagnostics and public error payloads are different surfaces. Package issues should support safe projection without forcing sensitive details into public messages.

[Back to top](#top)

---

## Proposed source-tree evolution

The smallest useful evolution is incremental and profile-first.

### Stage 0 — current state

```text
src/
├── README.md
└── geo/
    ├── README.md
    └── __init__.py
```

Status: **CONFIRMED scaffold**.

### Stage 1 — package and issue foundation

After package/discovery and result-profile decisions:

```text
src/geo/
├── __init__.py
├── issues.py        # deterministic issue carrier
└── profiles.py      # accepted profile references, not profile authority
```

Admission requirements:

- accepted package discovery/build configuration;
- stable issue/result contract or documented internal profile;
- public export decision;
- deterministic tests;
- no-network import tests.

### Stage 2 — representation-only primitives

After CRS/geometry/bbox/scale profiles are accepted:

```text
src/geo/
├── crs.py
├── geometry.py
├── bbox.py
├── scale.py
└── uncertainty.py
```

Admission requirements:

- explicit contracts/schemas or accepted internal profiles;
- no transform execution hidden in parsing;
- ambiguity and resource-limit tests;
- source/derived distinction;
- dependency review.

### Stage 3 — transform-plan adapters

After coordinate-operation and receipt profiles are accepted:

```text
src/geo/
├── transforms.py
└── receipts.py      # receipt candidates only
```

Admission requirements:

- operation selection contract;
- grid/resource policy;
- accuracy/area-of-use behavior;
- deterministic dependency/version capture;
- no-network tests;
- correction/rollback propagation.

### Stage 4 — public-safe candidate assembly

After geoprivacy policy handoff and transform profiles are accepted:

```text
src/geo/
└── public_safe.py
```

Admission requirements:

- supplied policy decision contract;
- exact/generalized/redacted/withheld separation;
- reconstruction-risk tests;
- transform receipt candidates;
- no exact-location leak tests;
- downstream release review.

### Stage 5 — manifest/context adapters

Only after schema-home conflicts are resolved:

```text
src/geo/
├── manifests.py
├── map_context.py
└── _generated/      # only with accepted generator workflow
```

Admission requirements:

- canonical LayerManifest profile;
- accepted MapContext and TileArtifact profiles;
- KFMGeoManifest schema expansion or explicit minimal-profile use;
- drift and information-loss tests;
- MapLibre and governed API consumer proof.

### Optional typed marker

Add `py.typed` only after the package is intentionally typed, packaging includes it, and type-check tests verify the installed distribution.

This staged tree is **PROPOSED**, not a claim about current files.

[Back to top](#top)

---

## Compatibility, correction, and rollback

### Compatibility posture

At version `0.0.0` with no established exports, no stable public package API is proven. Even so, avoid casual churn because documentation and future consumers may form expectations.

Any future compatibility policy should define:

- distribution and import versioning;
- profile version pinning;
- deprecation windows;
- public export stability;
- generated-model versioning;
- dependency/native-library version support;
- issue-code stability;
- migration adapters;
- rollback targets.

### Profile compatibility

Compatibility is not “both JSON objects parse.” It requires explicit field and semantic mapping.

For each adapter, document:

- source profile/version/digest;
- target profile/version/digest;
- preserved and transformed fields;
- defaults;
- dropped information;
- unsupported cases;
- round-trip expectation;
- correction behavior.

### Correction propagation

When a CRS profile, geometry rule, transform operation, policy decision, source limitation, or schema is corrected:

1. identify affected package versions and generated models;
2. identify candidate outputs and downstream consumers;
3. invalidate or mark stale affected caches/artifacts through owning systems;
4. preserve prior version and correction lineage;
5. regenerate/revalidate where required;
6. issue release/correction records outside this package;
7. keep rollback to the last known-safe package/profile combination.

The package itself must not mutate release state.

### README rollback

Before merge, close or abandon the review branch. After merge, restore the prior README blob or transparently revert the merge.

Prior target blob:

```text
420d38941b3e7e8e4767d7e65fdea0e53f2f91c0
```

### Implementation rollback

A future implementation change requires:

- prior package artifact/version;
- dependency lock rollback;
- generated-model rollback;
- profile/schema rollback or compatibility adapter;
- consumer compatibility evidence;
- correction/release record where outputs affected published artifacts;
- no deletion of audit receipts or prior evidence.

[Back to top](#top)

---

## Validation commands

### Documentation-only checks

```bash
python - <<'PY'
from pathlib import Path

path = Path("packages/geo/src/README.md")
text = path.read_text(encoding="utf-8")
assert text.endswith("\n")
assert text.count("# Governed Geo Package Source Root") == 1
assert "\t" not in text
assert not any(line.rstrip() != line for line in text.splitlines())
print("basic README checks passed")
PY

git diff --check
git diff -- packages/geo/src/README.md
```

### Repository inspection commands

```bash
find packages/geo -maxdepth 4 -type f | sort
sed -n '1,160p' packages/geo/pyproject.toml
sed -n '1,220p' packages/geo/src/geo/README.md

git grep -n "from geo\|import geo" -- . 2>/dev/null || true
git grep -n "packages/maplibre-runtime\|packages/maplibre/" -- packages docs 2>/dev/null || true
git grep -n "layer_manifest.schema.json" -- contracts schemas docs packages 2>/dev/null || true
```

### Future package checks

After implementation and packaging exist:

```bash
# PROPOSED examples only
python -m pytest tests/packages/geo
python -m build packages/geo
python -m pip install --no-deps --force-reinstall packages/geo/dist/*.whl
python -c "import geo; print(geo.__file__)"
python -c "import geo; print(sorted(getattr(geo, '__all__', ())))"
```

### Future offline check

A real no-network test must block network syscalls or run in an isolated environment. Grepping source for HTTP imports is not sufficient.

Do not copy future commands into CI until package metadata, namespace, dependencies, tests, and supported behavior are accepted.

[Back to top](#top)

---

## Definition of done

### This README revision

This revision is done when it:

- replaces stale planning assumptions with current repository evidence;
- records the `kfm-geo` `0.0.0` scaffold and empty initializer;
- aligns with the merged child-module v0.2 contract;
- separates source-root structure from module semantics;
- records missing build/discovery/dependency/export/test/CI evidence;
- preserves Directory Rules and authority roots;
- surfaces LayerManifest schema-home conflict and permissive schema limits;
- keeps MapLibre, policy, geoprivacy, lifecycle, evidence, release, and public interfaces outside this source root;
- defines import-time, dependency, generated-code, static-resource, security, and test boundaries;
- provides a staged implementation sequence rather than claiming files exist;
- defines compatibility, correction, validation, and rollback;
- changes only this README.

### Future source-root implementation

Implementation is not done until:

- [ ] owners are assigned;
- [ ] package purpose and consumers are accepted;
- [ ] build backend and package discovery are configured;
- [ ] supported Python versions are declared;
- [ ] dependencies and native-resource requirements are reviewed;
- [ ] the import namespace collision question is resolved;
- [ ] public exports are explicit;
- [ ] CRS, geometry, bbox, scale, uncertainty, transform, and issue profiles are accepted;
- [ ] LayerManifest schema-home conflict is resolved;
- [ ] MapContext, TileArtifact, and KFMGeoManifest adapter profiles are accepted;
- [ ] geoprivacy/policy handoff is contractually defined;
- [ ] generated-code provenance and drift checks exist if generation is used;
- [ ] package tests and public-safe fixtures exist;
- [ ] actual CI runs build, install, import, behavior, no-network, security, and drift tests;
- [ ] one governed internal consumer is verified;
- [ ] public clients remain behind governed APIs and released artifacts;
- [ ] compatibility, correction, and rollback are tested;
- [ ] package publication or release claims are evidence-backed.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Closure evidence |
|---|---|---:|---|
| `GEO-SRC-001` | Who owns the Geo package and source root? | UNKNOWN | CODEOWNERS/steward assignment |
| `GEO-SRC-002` | Is `kfm-geo` intended for internal use, publication, or both? | UNKNOWN | Package/release decision |
| `GEO-SRC-003` | What build backend is accepted? | UNKNOWN | `[build-system]` and build test |
| `GEO-SRC-004` | Which Python versions are supported? | UNKNOWN | `requires-python` and CI matrix |
| `GEO-SRC-005` | How is the `src` package discovered? | UNKNOWN | Build configuration and wheel inspection |
| `GEO-SRC-006` | Is `geo` the durable import namespace? | NEEDS VERIFICATION | Namespace/collision decision and import tests |
| `GEO-SRC-007` | What is the supported public export surface? | UNKNOWN | Explicit `__all__`, docs, and tests |
| `GEO-SRC-008` | Which governed consumers require the package? | UNKNOWN | Verified import/usage inventory |
| `GEO-SRC-009` | Which dependencies are accepted? | UNKNOWN | Dependency decision and lock metadata |
| `GEO-SRC-010` | Are native spatial libraries required? | UNKNOWN | Architecture/dependency ADR and build matrix |
| `GEO-SRC-011` | Are projection grids or CRS resources vendored? | UNKNOWN | Resource policy, rights, checksums, package manifest |
| `GEO-SRC-012` | What CRS reference profile is canonical? | NEEDS VERIFICATION | Accepted contract/schema/profile |
| `GEO-SRC-013` | What coordinate-operation profile is canonical? | NEEDS VERIFICATION | Accepted operation/transform contract |
| `GEO-SRC-014` | What geometry representation profile is canonical? | NEEDS VERIFICATION | Accepted contract/schema/profile |
| `GEO-SRC-015` | How are antimeridian and wrapped bboxes represented? | NEEDS VERIFICATION | Bbox/extent contract and fixtures |
| `GEO-SRC-016` | What dimensionality and coordinate-range rules apply? | NEEDS VERIFICATION | Geometry profile and tests |
| `GEO-SRC-017` | What scale and precision profile is canonical? | NEEDS VERIFICATION | Scale support contract/profile |
| `GEO-SRC-018` | What uncertainty representation and propagation rules apply? | NEEDS VERIFICATION | Uncertainty contract/profile |
| `GEO-SRC-019` | What issue/result vocabulary is canonical? | UNKNOWN | Contract/schema/registry and tests |
| `GEO-SRC-020` | Are old `VALID`/`INVALID`/`ABSTAIN_READY`/`DENY_READY` terms retained? | CONFLICTED | Accepted result-profile decision |
| `GEO-SRC-021` | Which LayerManifest schema home is canonical? | CONFLICTED | ADR/migration/compatibility decision |
| `GEO-SRC-022` | What MapContextEnvelope profile should adapters target? | NEEDS VERIFICATION | Expanded schema/contract and fixtures |
| `GEO-SRC-023` | What TileArtifactManifest profile should adapters target? | NEEDS VERIFICATION | Expanded schema/contract and fixtures |
| `GEO-SRC-024` | Will KFMGeoManifest schema be expanded to match its contract? | NEEDS VERIFICATION | Schema/fixture/validator update |
| `GEO-SRC-025` | Will the missing KFMGeoManifest validator be added or metadata corrected? | CONFLICTED | File addition or schema change |
| `GEO-SRC-026` | Where do Geo package behavior tests live? | NEEDS VERIFICATION | Accepted test path and tests |
| `GEO-SRC-027` | Where do Geo package fixtures live? | NEEDS VERIFICATION | Accepted fixture path and inventory |
| `GEO-SRC-028` | Is a dedicated Geo workflow required? | NEEDS VERIFICATION | Workflow decision and real steps |
| `GEO-SRC-029` | How is no-network behavior enforced? | UNKNOWN | Isolated/offline test |
| `GEO-SRC-030` | How are resource and geometry-size limits defined? | UNKNOWN | Security profile and tests |
| `GEO-SRC-031` | How are exact, derived, generalized, redacted, and withheld geometries typed separately? | NEEDS VERIFICATION | Contract/schema/type design |
| `GEO-SRC-032` | What policy decision object drives public-safe transforms? | NEEDS VERIFICATION | Policy handoff contract |
| `GEO-SRC-033` | How is reconstruction risk assessed? | UNKNOWN | Geoprivacy policy and tests |
| `GEO-SRC-034` | What transform receipt fields are required? | NEEDS VERIFICATION | Receipt contract/schema and validator |
| `GEO-SRC-035` | Where does transform execution belong: package, pipeline, tool, or runtime? | NEEDS DECISION | Architecture/ADR decision |
| `GEO-SRC-036` | How are dependency and CRS database versions captured? | UNKNOWN | Receipt/profile fields and tests |
| `GEO-SRC-037` | How are generated models versioned and checked for drift? | UNKNOWN | Generator contract and CI |
| `GEO-SRC-038` | How are profile adapters tested for information loss? | UNKNOWN | Compatibility fixtures/tests |
| `GEO-SRC-039` | How do corrections invalidate dependent candidates and releases? | UNKNOWN | Correction/supersession contract and runbook |
| `GEO-SRC-040` | What package versioning and deprecation policy applies? | UNKNOWN | Package/release policy |
| `GEO-SRC-041` | Is package publication intended? | UNKNOWN | Release record and artifact |
| `GEO-SRC-042` | What is the tested consumer rollback procedure? | UNKNOWN | Rollback plan and drill |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---:|---|---|
| Previous `packages/geo/src/README.md` | CONFIRMED | Existing planning intent and prior source-root boundary | Did not prove implementation maturity |
| `packages/geo/pyproject.toml` | CONFIRMED minimal placeholder | Distribution name/version | Does not prove build, discovery, dependencies, or installation |
| `packages/geo/src/geo/README.md` v0.2 | CONFIRMED merged contract | Detailed module boundary, conflicts, safety, and proposed interface | Does not prove module implementation |
| Empty `geo/__init__.py` | CONFIRMED | Import-package marker | No supported exports or behavior |
| Selected module exact-path checks | CONFIRMED bounded absence | No observed `crs.py`, `geometry.py`, `public_safe.py`, or `validation.py` | Not a recursive proof of every possible implementation elsewhere |
| Parent `packages/geo/README.md` | CONFIRMED planning doc | Package intent | Remains stale relative to module v0.2 |
| `packages/maplibre/README.md` | CONFIRMED helper lane | Renderer-adapter separation | Implementation maturity remains separately verified |
| Spatial Foundation architecture | CONFIRMED authored doctrine/PROPOSED implementation guidance | Cross-domain vocabulary and invariants | Rich prose is not an executable schema |
| UI MapContext schema | CONFIRMED / PROPOSED | Current schema location | Empty permissive shape |
| Map LayerManifest schema | CONFIRMED / PROPOSED | One candidate schema home | Empty permissive shape |
| Data LayerManifest contract/schema | CONFIRMED | Semantic contract and current paired minimal schema | Schema does not enforce rich semantics |
| Layers LayerManifest schema | CONFIRMED / PROPOSED | Competing candidate schema home | Empty permissive shape |
| TileArtifactManifest schema | CONFIRMED / PROPOSED | Current map schema path | Empty permissive shape |
| KFMGeoManifest contract/schema | CONFIRMED | Geo artifact manifest semantics and current minimal schema | Contract/schema gap; validator/fixtures unproven |
| Directory Rules v1.4 | CONFIRMED doctrine | `packages/` implementation responsibility and authority separation | Does not choose spatial profiles or dependencies |
| Compare `6a6abd1c…` to `ee77864f…` | CONFIRMED | Source-root target unchanged while child module and unrelated docs merged | Does not prove unindexed runtime behavior |
| Current revision workflow | CONFIRMED | One-file documentation update | Does not implement or validate Geo behavior |

---

## Maintainer checklist

Before editing this source root:

- [ ] Reconfirm current `main` and target blob.
- [ ] Recheck package metadata and source-tree inventory.
- [ ] Recheck the child module contract.
- [ ] Recheck the parent package README and accepted ADRs.
- [ ] Recheck LayerManifest schema-home status.
- [ ] Recheck MapContext, TileArtifact, and KFMGeoManifest schemas/contracts.
- [ ] Recheck validator, test, fixture, and workflow paths.
- [ ] Recheck package consumers and dependency graph.
- [ ] Recheck native/resource and no-network requirements.
- [ ] Recheck geoprivacy, rights, sensitivity, and protected-location rules.
- [ ] Mark implementation claims with evidence status.
- [ ] Keep public clients behind governed APIs and released artifacts.
- [ ] Keep source, derived, and public geometry separate.
- [ ] Preserve lifecycle, evidence, policy, review, release, correction, and rollback boundaries.
- [ ] Avoid parallel schema, contract, policy, proof, receipt, release, or renderer homes.
- [ ] Make the smallest reversible change.

[Back to top](#top)
