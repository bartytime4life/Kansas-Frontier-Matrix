<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-geo-src-geo-readme
title: packages/geo/src/geo/ — Governed Geospatial Primitive Helper Module
type: readme
version: v0.2
status: draft; repository-grounded; python-source-module; implementation-placeholder; non-authoritative
owners:
  - OWNER_TBD — Geo package owner
  - OWNER_TBD — Spatial Foundation steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Policy, rights, sensitivity, and geoprivacy steward
  - OWNER_TBD — Map, release, correction, validator, security, and docs stewards
created: NEEDS VERIFICATION — target file existed before this revision
updated: 2026-07-15
supersedes: v1 planning-oriented import-namespace guide (2026-06-14)
policy_label: public; packages; geo; python; CRS; geometry; scale; uncertainty; generalization; no-network-by-default; fail-closed; map-is-carrier; non-authoritative
path: packages/geo/src/geo/README.md
truth_posture: CONFIRMED target and prior blob, kfm-geo 0.0.0 project metadata, Python src layout, empty geo initializer, planning-oriented parent package/source READMEs, bounded absence of selected geo helper modules and package.json, bounded absence of package-specific test/fixture READMEs and dedicated geo.yml workflow, actual packages/maplibre helper lane, Directory Rules v1.4, Spatial Foundation doctrine/object-family guidance, current UI MapContextEnvelope schema location and empty permissive shape, three competing LayerManifest schema homes with an explicit data-contract conflict, empty permissive map/layers LayerManifest schemas, minimal data LayerManifest schema, empty permissive TileArtifactManifest schema, KFMGeoManifest contract plus minimal schema stub, and absent schema-declared KFMGeoManifest validator/fixture README at exact tested paths / PROPOSED future pure geospatial primitive adapters, explicit CRS/profile carriers, bounded geometry inspection, scale/precision issue carriers, transform plan carriers, schema-generated models, public-safe candidate assembly from supplied policy decisions, and package tests / CONFLICTED old README paths versus current schema homes, LayerManifest schema-home split, rich Spatial Foundation and geo-manifest semantics versus permissive/minimal schemas, proposed helper outcomes versus no accepted geo-result contract, maplibre-runtime prose versus verified packages/maplibre lane, and public-safe helper ambitions versus policy authority / UNKNOWN build backend, Python requirement, dependencies, package discovery, exports, consumers, canonical geometry/CRS/scale/uncertainty profiles, transform engine, validator integration, dedicated CI, package publication, runtime/API wiring, and production behavior / NEEDS VERIFICATION owners, ADR/profile decisions, reason-code vocabulary, geoprivacy handoff, transform receipts, correction invalidation, release integration, and rollback integration
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 6a6abd1cfadf181c093f21d0eb36a38f7ca3ed8b
  prior_blob: 9f0038e5bd6e0699cca6b9d4587de0d1a6b8ea07
  pyproject_blob: ad9241a73d73d1c47fe2d29e52594b3961e8b588
  package_readme_blob: ba61bc82ab405ba731bb843c0e9d25b079e6db5b
  source_readme_blob: 420d38941b3e7e8e4767d7e65fdea0e53f2f91c0
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
  geo_manifest_architecture_blob: c6af4e5c002f0ec8caf30f4b751368d5bc4d09af
related:
  - ./__init__.py
  - ../README.md
  - ../../README.md
  - ../../pyproject.toml
  - ../../../maplibre/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/architecture/spatial-foundation.md
  - ../../../../contracts/data/layer_manifest.md
  - ../../../../contracts/evidence/kfm_geo_manifest.md
  - ../../../../schemas/contracts/v1/ui/map_context_envelope.schema.json
  - ../../../../schemas/contracts/v1/map/layer_manifest.schema.json
  - ../../../../schemas/contracts/v1/data/layer_manifest.schema.json
  - ../../../../schemas/contracts/v1/layers/layer_manifest.schema.json
  - ../../../../schemas/contracts/v1/map/tile_artifact_manifest.schema.json
  - ../../../../schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json
tags: [kfm, packages, geo, python, source-module, spatial-foundation, CRS, geometry, bbox, scale, uncertainty, generalization, geoprivacy, schema-profile, deterministic, no-network, fail-closed, rollback]
notes:
  - "v0.2 replaces stale planning language with a commit-pinned description of the current kfm-geo 0.0.0 Python scaffold."
  - "The initializer is empty and selected helper modules are absent; no supported geo API, consumer, validator, transform engine, or production behavior is claimed."
  - "Spatial Foundation object families are doctrinally described, but current map/context/manifest schemas are permissive or minimal and LayerManifest has conflicting schema homes."
  - "Public-safe geometry remains a policy- and release-governed transform; this module may only assemble candidates from explicit supplied decisions and transform context."
  - "Only this Markdown file changes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Geospatial Primitive Helper Module

`packages/geo/src/geo/`

> Python source-module boundary for reusable, deterministic, no-network geospatial primitive helpers. The current repository surface is a **greenfield `0.0.0` scaffold**, not an implemented geometry library: `__init__.py` is empty, selected helper modules are absent, no supported exports or consumers are established, and the contracts and schemas needed to standardize CRS, geometry, scale, uncertainty, transformation, and helper outcomes remain incomplete or conflicted.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![distribution](https://img.shields.io/badge/distribution-kfm--geo-3776ab)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![authority](https://img.shields.io/badge/authority-helper%20only-455a64)
![network](https://img.shields.io/badge/network-none%20by%20default-455a64)
![spatial-truth](https://img.shields.io/badge/map-carrier%20not%20truth-0b7285)

**Quick links:** [Purpose](#purpose-and-audience) · [Authority](#authority-level) · [Status](#current-repository-state) · [Context](#bounded-context-and-ubiquitous-language) · [Placement](#placement-and-responsibility) · [Parent split](#package-source-root-and-module-split) · [Spatial Foundation](#spatial-foundation-boundary) · [Contracts](#contract-and-schema-profile-conflicts) · [CRS](#crs-boundary) · [Geometry](#geometry-boundary) · [Scale](#scale-precision-and-uncertainty-boundary) · [Transforms](#transform-generalization-and-public-safe-boundary) · [Manifests](#manifest-and-map-context-boundary) · [MapLibre](#maplibre-boundary) · [Inputs](#accepted-inputs) · [Outputs](#permitted-outputs) · [Interface](#proposed-module-interface) · [Dependencies](#dependency-and-import-direction) · [Failures](#failure-and-outcome-semantics) · [Trust](#lifecycle-policy-release-and-public-safety) · [Security](#security-privacy-and-sensitive-location-controls) · [Tests](#tests-fixtures-validators-and-ci) · [Admission](#implementation-admission-sequence) · [Compatibility](#compatibility-correction-and-rollback) · [Validation](#validation-commands) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Ledger](#evidence-ledger)

> [!IMPORTANT]
> **Repository snapshot:** `main@6a6abd1cfadf181c093f21d0eb36a38f7ca3ed8b`<br>
> **Distribution:** `kfm-geo`<br>
> **Declared version:** `0.0.0`<br>
> **Verified import package:** `src/geo/`<br>
> **Verified implementation:** empty `__init__.py`; selected helper modules absent<br>
> **Build backend, Python requirement, dependencies, package discovery, exports, consumers, and package publication:** not established<br>
> **Map/context/manifest schemas:** present but permissive or minimal `PROPOSED` scaffolds<br>
> **LayerManifest schema home:** conflicted across `map/`, `data/`, and `layers/` families<br>
> **Public posture:** public clients consume governed APIs and released artifacts; they do not import this module or use local geometry validity as publication authority

> [!CAUTION]
> Geometry validity is not spatial truth. A CRS identifier is not a verified transform. A bbox is not evidence closure. A generalized geometry is not automatically public-safe. A manifest-shaped object is not a release. A map is a carrier of governed claims, not an authority source.

---

## Purpose and audience

`packages/geo/src/geo/` is the proposed import module inside the `kfm-geo` shared package.

A mature implementation may provide pure or side-effect-minimal support for:

- carrying explicitly selected CRS and coordinate-operation profiles;
- checking local geometry representation constraints that are actually defined by an accepted contract;
- detecting missing, malformed, unsupported, ambiguous, empty, non-finite, or inconsistent spatial inputs;
- checking bbox, extent, dimensionality, precision, scale, and uncertainty values against explicit profiles;
- constructing **transform plan candidates** without executing an undeclared or ambient transform;
- preserving source geometry and derived/generalized geometry as separate values;
- attaching explicit transform, uncertainty, evidence, policy, release, correction, and rollback references supplied by governed callers;
- assembling candidate fragments for accepted map, layer, tile, evidence, or runtime contracts;
- producing deterministic issue carriers for downstream validators and finite runtime mapping;
- supporting synthetic, sanitized, public-safe, no-network tests.

The module must remain subordinate to contracts, schemas, source descriptors, EvidenceBundles, policy, review, release, correction, runtime envelopes, and governed API serialization.

### Audience

This README is for:

- Geo package maintainers;
- Spatial Foundation and map stewards;
- domain package and pipeline maintainers;
- contract, schema, validator, policy, release, and correction stewards;
- geoprivacy, rights, sensitivity, security, and privacy reviewers;
- governed API, MapLibre, Evidence Drawer, Focus Mode, and export maintainers;
- reviewers deciding whether a spatial behavior belongs here, in a domain package, in `packages/maplibre/`, in a pipeline, in a validator, in policy, or in release tooling.

[Back to top](#top)

---

## Authority level

**Implementation-support module, currently scaffolded; non-authoritative for spatial meaning, source truth, policy, evidence closure, release, storage, or public maps.**

| Concern | Authority in this module |
|---|---|
| Spatial Foundation meaning | **None.** Cross-domain doctrine and accepted contracts own meaning. |
| CRS profile meaning and allowed transforms | **None.** Accepted CRS/transform contracts and policy own the profile. |
| Geometry machine shape | **None.** Accepted schemas own machine shape. |
| Geometry validity for publication | **None.** Validators, evidence, policy, review, and release gates own admission. |
| Source scale and accuracy | **None.** Source descriptors and evidence records own source limitations. |
| Sensitivity and exact-location disclosure | **None.** Policy and geoprivacy systems own allow, restrict, generalize, withhold, deny, and abstain decisions. |
| Generalization transform approval | **None.** Policy, transform specs, validation, review, and receipts own approval. |
| Evidence closure | **None.** EvidenceRef-to-EvidenceBundle resolution remains outside this module. |
| Layer/tile/map release | **None.** Release manifests and promotion records own publication state. |
| Map rendering | **None.** The verified helper lane is `packages/maplibre/`; app/UI roots own public rendering. |
| Local helper behavior | **Supporting only.** Code may inspect explicit inputs, apply accepted pure calculations, and return candidate values/issues. |

Importing a geometry library, parsing GeoJSON, or computing a coordinate transform does not transfer authority into this module.

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
| Base commit | `6a6abd1cfadf181c093f21d0eb36a38f7ca3ed8b` |
| Prior target blob | `9f0038e5bd6e0699cca6b9d4587de0d1a6b8ea07` |
| Project metadata blob | `ad9241a73d73d1c47fe2d29e52594b3961e8b588` |
| Package README blob | `ba61bc82ab405ba731bb843c0e9d25b079e6db5b` |
| Source-root README blob | `420d38941b3e7e8e4767d7e65fdea0e53f2f91c0` |
| Initializer blob | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` |
| Current revision | documentation-only module v0.2 proposal |

### Verified package and module surface

| Surface | Evidence at snapshot | Status | Consequence |
|---|---|---:|---|
| This README | Existing v1 planning-oriented namespace guide. | **CONFIRMED** | Revised in place; prior safety intent is retained. |
| [`../../pyproject.toml`](../../pyproject.toml) | Declares `[project]`, name `kfm-geo`, and version `0.0.0` only. | **CONFIRMED minimal placeholder** | Distribution identity is known; build/install behavior is not. |
| [`../../README.md`](../../README.md) | Package-level planning guide v1. | **CONFIRMED README / planning-oriented** | Describes intent; does not prove implementation. |
| [`../README.md`](../README.md) | Source-root planning guide v1. | **CONFIRMED README / planning-oriented** | Does not prove package discovery, imports, tests, or consumers. |
| [`__init__.py`](./__init__.py) | Exists and is empty. | **CONFIRMED** | Import-package marker only; no exports are established. |
| `package.json` | Absent at `packages/geo/package.json`. | **CONFIRMED bounded absence** | Do not claim a JavaScript/TypeScript package. |
| `crs.py` | Absent at the exact tested module path. | **CONFIRMED bounded absence** | No CRS helper implementation is established. |
| `geometry.py` | Absent at the exact tested module path. | **CONFIRMED bounded absence** | No geometry helper implementation is established. |
| `public_safe.py` | Absent at the exact tested module path. | **CONFIRMED bounded absence** | No public-safe transform implementation is established. |
| `validation.py` | Absent at the exact tested module path. | **CONFIRMED bounded absence** | No local geo-result or validator implementation is established. |
| Build backend | No `[build-system]` section observed in the project file. | **NOT OBSERVED** | Wheel/editable-install behavior is unproven. |
| Python requirement | No `requires-python` field observed. | **NOT OBSERVED** | Supported interpreter versions are unknown. |
| Dependencies | No dependency list observed. | **NOT OBSERVED** | Do not claim Shapely, PyProj, GDAL, GeoPandas, JSON Schema, or other dependencies. |
| Package discovery | No discovery configuration observed. | **NOT OBSERVED** | Inclusion of the `geo` namespace in a wheel is unproven. |
| Public exports | Empty initializer. | **NOT ESTABLISHED** | No symbol is a supported package API. |
| Consumers | Indexed search did not establish production `from geo` or `import geo` consumers. | **NOT OBSERVED / search-limited** | Do not claim runtime or pipeline integration. |
| Package test README | Absent at `tests/packages/geo/README.md`. | **CONFIRMED bounded absence** | No package-specific test lane is documented there. |
| Package fixture README | Absent at `fixtures/packages/geo/README.md`. | **CONFIRMED bounded absence** | No package-specific fixture lane is documented there. |
| Dedicated workflow | Absent at `.github/workflows/geo.yml`. | **CONFIRMED bounded absence** | No dedicated module CI is established by that conventional path. |

These bounded findings do not prove that no related spatial logic exists elsewhere. They do prove that this module must not claim a supported implementation, transform engine, validator, public API, or production consumer from the inspected package surface.

### Verified neighboring surfaces

| Surface | Current evidence | Status | Module consequence |
|---|---|---:|---|
| Directory Rules | `packages/` is a shared implementation root; contracts, schemas, policy, data, release, tests, and apps remain distinct authority roots. | **CONFIRMED doctrine** | This module cannot become a parallel authority home. |
| Spatial Foundation architecture | Defines cross-domain spatial grammar and named object families, while marking implementation realization largely `PROPOSED`. | **CONFIRMED document / mixed doctrine-realization posture** | Ubiquitous language may guide design; fields and APIs require accepted contracts. |
| `packages/maplibre/README.md` | Existing MapLibre helper package lane. | **CONFIRMED README** | Old references to `packages/maplibre-runtime/` cannot be treated as current repo fact. |
| UI MapContextEnvelope schema | Exists under `schemas/contracts/v1/ui/`; object has no properties and allows additional properties. | **CONFIRMED `PROPOSED` scaffold** | The module cannot claim a typed MapContextEnvelope fragment contract. |
| Map LayerManifest schema | Exists under `schemas/contracts/v1/map/`; empty permissive object. | **CONFIRMED `PROPOSED` scaffold** | It does not enforce layer fields. |
| Data LayerManifest schema | Exists under `schemas/contracts/v1/data/`; requires `id`, permits optional `version`/`spec_hash`, and allows additional properties. | **CONFIRMED `PROPOSED` placeholder** | It does not enforce rich layer semantics. |
| Layers LayerManifest schema | Exists under `schemas/contracts/v1/layers/`; empty permissive object. | **CONFIRMED `PROPOSED` scaffold** | A third competing schema family exists. |
| LayerManifest semantic contract | Explicitly records conflict between `data/` and `layers/` homes and incomplete schema realization. | **CONFIRMED draft contract** | The module must require a named manifest profile. |
| TileArtifactManifest schema | Exists under `schemas/contracts/v1/map/`; empty permissive object. | **CONFIRMED `PROPOSED` scaffold** | It cannot validate tile-manifest fragments. |
| KFMGeoManifest contract | Rich geospatial artifact-manifest semantics, explicitly non-authoritative and release-gated. | **CONFIRMED draft contract** | Candidate assembly must remain profile-pinned and non-release-authoritative. |
| KFMGeoManifest schema | Requires only `id`, permits optional `version`/`spec_hash`, and allows additional properties. | **CONFIRMED `PROPOSED` stub** | Rich fields remain semantic proposals, not enforced shape. |
| KFMGeoManifest validator | Schema declares `tools/validators/evidence/validate_kfm_geo_manifest.py`; exact file is absent. | **CONFLICTED metadata / file state** | Do not claim dedicated validator availability. |
| KFMGeoManifest fixture README | Absent at the exact tested path. | **CONFIRMED bounded absence** | No documented fixture family is established there. |

[Back to top](#top)

---

## Bounded context and ubiquitous language

This module belongs to the **Spatial Foundation implementation-support context**.

It may implement reusable calculations and carriers that are independent of a specific KFM domain. It must not absorb domain meaning or publication authority.

### Ubiquitous language

| Term | Meaning in this module | Must not be confused with |
|---|---|---|
| `CRS profile` | Explicit identifier plus accepted axis, units, datum, epoch, vertical, and operation context. | A bare EPSG integer or assumed WGS84. |
| `coordinate operation` | Explicit source-to-target operation or operation-plan reference. | An ambient reprojection chosen by a library. |
| `source geometry` | Input geometry as admitted or supplied, with provenance and source limitations. | Public geometry or canonical truth. |
| `derived geometry` | Geometry produced by an explicit transform, clip, simplify, aggregate, centroid, or generalization step. | Source geometry. |
| `public geometry candidate` | Derived geometry assembled under an explicit supplied policy decision and transform profile. | An automatically publishable geometry. |
| `bbox` | Explicit extent with axis order, CRS/profile, and wrap semantics. | A generic four-number list with assumed meaning. |
| `scale support` | Range or constraint describing where representation or analysis remains supportable. | Renderer zoom alone. |
| `precision` | Representation/storage precision that must not exceed source support. | Accuracy. |
| `accuracy` | Estimated closeness to the real-world location under a defined method. | Number of decimal places. |
| `uncertainty` | Explicit spatial limitation, distribution, bound, confidence, or qualitative issue. | Missing data hidden by a clean geometry. |
| `validity issue` | Deterministic local issue under a named profile. | A policy or release decision. |
| `transform receipt candidate` | Data needed by another system to persist an auditable transform receipt. | A persisted receipt. |
| `manifest fragment candidate` | Profile-pinned fields prepared for an owning manifest assembler. | A schema-valid or released manifest. |

### Context boundary

The module may answer:

- Is a required input present?
- Does a numeric value use a finite supported representation?
- Does an explicit bbox match a named axis/order profile?
- Is a geometry candidate structurally inspectable under an accepted profile?
- Does requested output precision exceed supplied source support?
- Which explicit issues prevent the next governed gate?
- Which transform metadata must be preserved?

The module must not answer:

- Is this location true?
- Is this geometry authoritative?
- May exact coordinates be shown?
- Is a species, archaeological site, infrastructure asset, or private property location safe to disclose?
- Is this layer released?
- Does this evidence close the claim?
- Which coordinate operation should be silently chosen?
- Should invalid geometry be silently repaired?

[Back to top](#top)

---

## Placement and responsibility

### Directory Rules basis

`packages/` is the implementation root for reusable libraries. The existing path is therefore a plausible home for shared, non-domain, non-authoritative geospatial helper code.

The path does **not** authorize this module to own:

- semantic contracts;
- JSON Schemas;
- policy or geoprivacy decisions;
- source registries;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data;
- EvidenceBundles, proofs, validation reports, or receipts;
- release manifests, promotion decisions, corrections, or rollback records;
- MapLibre rendering or UI components;
- public API routes;
- model-provider calls or generated spatial claims.

### Placement test

A proposed function belongs here only when all are true:

1. it is reusable across more than one domain or application;
2. it operates on explicit inputs;
3. it is deterministic under a named profile;
4. it needs no source, registry, datastore, network, policy engine, release service, UI, or model provider access;
5. it does not define object meaning or machine shape;
6. it returns a value or issue candidate rather than a trust decision;
7. it preserves evidence, source, policy, release, correction, and transform context without persisting them.

Otherwise, place it in the domain package, pipeline, validator, policy, release, map, app, or tool root that owns the behavior.

[Back to top](#top)

---

## Package, source-root, and module split

| Level | Path | Responsibility | Current status |
|---|---|---|---:|
| Package | `packages/geo/` | Distribution identity, packaging, compatibility, consumer, and package-wide dependency posture. | v1 planning README; `0.0.0` metadata scaffold. |
| Source root | `packages/geo/src/` | Source layout, discovery, generated-code placement, import direction, and source-wide controls. | v1 planning README. |
| Import module | `packages/geo/src/geo/` | Concrete reusable helper exports and local implementation rules. | Empty initializer; no selected helper modules. |

This README governs the import module only. It does not establish package build behavior, choose dependencies, or settle parent README drift.

### Module invariant

The source module may become executable only after package-level and source-root decisions are explicit enough to make installation, dependency, schema-profile, and test behavior reproducible.

[Back to top](#top)

---

## Spatial Foundation boundary

Spatial Foundation doctrine names a wider object family than this module currently implements.

Named architecture terms include:

- Coordinate Reference Profile;
- GeographyVersion;
- Projection Transform Receipt;
- Geometry Fingerprint;
- Base Layer Descriptor;
- MapStyleRule;
- Scale Support Profile;
- spatial UncertaintySurface;
- Generalization Transform;
- spatial-grammar LayerManifest responsibilities.

Those terms are useful design vocabulary. They are **not** proof that Python classes, schema fields, registries, validators, or runtime routes exist.

### Module relationship

| Spatial Foundation family | Possible helper role here | Authority retained elsewhere |
|---|---|---|
| Coordinate Reference Profile | Parse or compare an accepted generated carrier. | Contract/schema/profile registry. |
| GeographyVersion | Validate explicit identifier/time carrier shape if contracted. | Geography registry and domain/release records. |
| Projection Transform Receipt | Build receipt **candidate data** from explicit operation metadata. | Receipt schema, validator, and persistence system. |
| Geometry Fingerprint | Coordinate with accepted canonicalization/hashing helper. | Hash contract/schema and proof/receipt records. |
| Base Layer Descriptor | Inspect or assemble accepted primitive fields. | Layer/source contracts, policy, and release. |
| MapStyleRule | No default ownership; style semantics belong with map/style lanes. | MapLibre/style contracts and release. |
| Scale Support Profile | Apply an accepted profile to explicit scale/resolution values. | Contract/schema/source descriptor. |
| UncertaintySurface | Carry or inspect accepted metadata. | Domain evidence and uncertainty contract. |
| Generalization Transform | Apply only an explicitly accepted pure transform profile with policy input. | Policy, transform contract, receipt, validation, review, release. |

> [!WARNING]
> Do not turn architecture vocabulary into ad hoc Python dataclasses and then treat those classes as the canonical contract. Contract and schema acceptance must precede or accompany implementation.

[Back to top](#top)

---

## Contract and schema profile conflicts

The module must select an explicit profile for every structured input and output. It must never infer a canonical profile from a class name.

### Confirmed conflicts

| Topic | Current repository evidence | Required module posture |
|---|---|---|
| MapContextEnvelope path | Actual schema is under `schemas/contracts/v1/ui/`, not the old unsegmented path cited in parent docs. | Pin the verified path and schema identity; do not preserve stale aliases silently. |
| MapContextEnvelope shape | Schema is an empty permissive `PROPOSED` scaffold. | Do not claim typed map-context fragment support. |
| LayerManifest home | `map/`, `data/`, and `layers/` schemas coexist. | Require an explicit profile identifier; no default alias. |
| LayerManifest shape | Two schemas are empty/permissive; the data schema only requires `id`. | Do not claim rich layer-manifest validation. |
| LayerManifest meaning | Data contract describes rich evidence/release semantics not enforced by schemas. | Treat rich fields as semantic proposals until paired machine profile is accepted. |
| TileArtifactManifest shape | Map schema is empty/permissive. | Do not claim tile-manifest validation. |
| KFMGeoManifest shape | Rich contract; schema only requires `id` and permits arbitrary extra fields. | Do not treat schema validity as geo-manifest completeness. |
| KFMGeoManifest validator | Declared by schema metadata but file absent. | Return unsupported/not-configured posture; never claim validator execution. |
| Geo helper outcome vocabulary | `VALID`, `INVALID`, `ABSTAIN_READY`, `DENY_READY`, `GENERALIZED`, `WITHHELD` appears only in planning prose. | Keep outcomes `PROPOSED`; no public enum until contract/schema acceptance. |
| Map helper package path | Verified package is `packages/maplibre/`; planning prose names `packages/maplibre-runtime/`. | Use current verified lane or mark runtime ownership unresolved. |

### Profile descriptor requirement

A future helper call should receive or resolve an explicit immutable profile descriptor containing at least:

```text
profile_id
profile_version
contract_ref
schema_ref
schema_hash_or_spec_hash
crs_profile_ref
geometry_profile_ref
axis_order_policy
dimension_policy
precision_policy
scale_support_ref
uncertainty_profile_ref
transform_profile_ref
reason_code_profile_ref
```

Exact fields are **PROPOSED**. The invariant is explicit profile selection.

### No silent compatibility

The module must not:

- try multiple schema families until one passes;
- equate `data/layer_manifest` and `map/layer_manifest`;
- accept arbitrary extra fields because a scaffold schema permits them;
- translate old unsegmented schema paths into current paths without a versioned adapter;
- promote rich semantic fields into machine guarantees;
- infer outcome mapping from prose;
- drop fields that do not fit a selected schema;
- convert missing profile data into defaults.

[Back to top](#top)

---

## CRS boundary

### Required posture

CRS handling must be explicit, profile-driven, and auditable.

A future CRS carrier may need:

- authority and code or a resolvable CRS identifier;
- WKT/PROJJSON identity where required;
- axis order;
- horizontal datum;
- vertical datum/reference;
- units;
- coordinate epoch;
- area of use;
- source and target CRS references;
- coordinate operation/pipeline identifier;
- grid/resource dependencies;
- expected accuracy;
- transform direction;
- antimeridian and wrap rules.

These fields are **PROPOSED** until accepted contracts and schemas exist.

### Prohibited assumptions

The module must not assume:

- EPSG:4326;
- longitude-latitude order;
- latitude-longitude order;
- Web Mercator;
- meters;
- a missing vertical reference;
- a static datum when epoch matters;
- a best-available transform selected from local installation state;
- network grid downloads;
- equivalence of two CRS strings without an accepted comparison profile.

### Transform selection boundary

Selecting a coordinate operation can be policy- and environment-significant.

The module may:

- inspect an explicit operation supplied by the caller;
- verify declared source/target identifiers;
- report missing grids or unsupported operations;
- execute a pure, pinned operation only when dependency/resource identity is controlled;
- return transform metadata and issues.

It must not:

- search the network for grids;
- pick an operation based on mutable local database ranking without recording it;
- silently fall back to a lower-accuracy operation;
- hide unavailable vertical transformations;
- claim transformed coordinates are more accurate than source support.

### CRS issue examples

```text
geo/crs/missing
geo/crs/ambiguous-axis-order
geo/crs/unsupported
geo/crs/epoch-required
geo/crs/vertical-reference-missing
geo/crs/operation-not-pinned
geo/crs/grid-resource-missing
geo/crs/accuracy-insufficient
```

Reason codes are **PROPOSED** pending registry/contract acceptance.

[Back to top](#top)

---

## Geometry boundary

### Local geometry inspection

A future implementation may inspect explicit geometry candidates for:

- declared type;
- coordinate nesting;
- finite numeric values;
- dimensionality;
- emptiness;
- coordinate count and configured resource limits;
- bbox consistency under a named profile;
- ring closure where applicable;
- duplicate or degenerate structures under a named profile;
- self-intersection or topology issues when a pinned engine/profile is accepted;
- antimeridian/wrap behavior;
- source/public geometry separation.

### Validity is profile-relative

Different geometry ecosystems have different validity and repair semantics. Therefore:

```text
geometry representation + accepted profile + pinned engine/version
    -> local inspection result
```

Not:

```text
geometry
    -> universally valid or invalid
```

A helper result must preserve:

- input digest or stable input reference;
- profile identifier;
- engine and version when used;
- operation performed;
- issues and severity;
- whether geometry was changed;
- output digest/reference;
- precision and dimensionality effects;
- provenance/receipt candidate fields.

### No silent repair

The module must not silently:

- close rings;
- reverse ring orientation;
- remove duplicate vertices;
- snap coordinates;
- buffer by zero;
- dissolve geometry;
- simplify;
- clip;
- centroid;
- repair self-intersections;
- discard Z or M dimensions;
- coerce geometry types;
- normalize across the antimeridian;
- replace invalid geometry with bbox/centroid.

A repair or normalization must be a separate explicit transform candidate with before/after identity and loss disclosure.

### Resource safety

Geometry inspection must enforce configured limits for:

- byte size;
- coordinate count;
- nesting depth;
- collection size;
- ring count;
- transform time;
- memory use;
- output expansion.

Exceeding a limit must return a stable issue, not partial success.

[Back to top](#top)

---

## Scale, precision, and uncertainty boundary

### Distinctions to preserve

| Concept | Meaning | Anti-collapse rule |
|---|---|---|
| Source scale | Scale/resolution at which source data was created or is supportable. | Must not be inferred from current renderer zoom. |
| Representation scale | Scale/resolution of a derived layer or display artifact. | Must not imply improved source accuracy. |
| Coordinate precision | Numeric/storage precision. | Decimal places are not accuracy. |
| Positional accuracy | Estimated closeness to real-world location. | Must carry method and confidence/limit. |
| Spatial resolution | Smallest represented or sampled unit. | Must remain distinct from display scale. |
| Generalization level | Explicit transform/representation state. | Must preserve transform lineage. |
| Uncertainty | Limitation, range, distribution, or qualitative confidence. | Must not be erased by normalization. |
| Topology confidence | Confidence in relationships or validity under a profile. | Must not be converted to geometry truth. |

### Precision checks

A future helper may compare requested precision against explicit source support.

It must not:

- add decimal places and call the result more accurate;
- infer accuracy from CRS;
- infer source scale from bbox size;
- infer uncertainty from geometry type;
- remove uncertainty because a transform succeeded;
- use map zoom as an evidentiary confidence score.

### Uncertainty carrier

A candidate uncertainty carrier may include:

```text
uncertainty_kind
value_or_range
unit
confidence_or_method
source_ref
evidence_ref
spatial_scope
temporal_scope
profile_ref
limitations
```

Shape remains **PROPOSED**.

[Back to top](#top)

---

## Transform, generalization, and public-safe boundary

### Transform classes

Potential explicit transform classes include:

- reprojection;
- axis-order conversion;
- dimensionality conversion;
- clipping;
- simplification;
- aggregation;
- snapping;
- smoothing;
- centroiding;
- convex hull;
- grid/hex binning;
- displacement;
- masking;
- redaction;
- generalization;
- withholding.

Each transform must be separately named and receiptable.

### Public-safe geometry is not a local guess

The module may assemble a public-safe geometry **candidate** only when the caller supplies:

- an accepted policy decision/reference;
- audience and purpose;
- source sensitivity and rights context;
- exact transform profile;
- transformation parameters;
- required caveats;
- evidence/source refs;
- correction and rollback context;
- validation requirements.

The module must not decide that a location is safe because:

- it is already online;
- it is in a public dataset;
- the geometry is coarse;
- the requester supplied it;
- the feature is old;
- the coordinate is approximate;
- a style hides it;
- a map is zoomed out.

### Exact and public geometry separation

Required invariant:

```text
source/internal geometry
    -- explicit governed transform -->
public geometry candidate
```

The public candidate must not overwrite or silently replace the source/internal geometry.

### Sensitive-location controls

Rare species, archaeology, infrastructure, living-person, private-property, cultural/sovereignty, and other protected locations require deny-by-default or explicitly governed disclosure.

Fixtures must not include real protected coordinates.

### Transform receipt candidate

A future helper may return data sufficient for an owning system to persist a receipt:

```text
transform_id
transform_profile_ref
tool_and_version
input_ref_or_digest
output_ref_or_digest
parameters
crs_before
crs_after
precision_before
precision_after
loss_summary
policy_decision_ref
evidence_refs
performed_at_policy
correction_and_rollback_refs
issues
```

This module must not persist the receipt itself.

[Back to top](#top)

---

## Manifest and map-context boundary

### Candidate fragments only

The module may eventually assemble profile-pinned fragments for:

- `KFMGeoManifest`;
- `LayerManifest`;
- `TileArtifactManifest`;
- `MapContextEnvelope`;
- layer descriptors or map-source descriptors owned elsewhere.

It must not call an arbitrary dictionary a manifest.

### Current machine-shape limits

| Object | Current machine posture | What the module can safely claim |
|---|---|---|
| MapContextEnvelope | Empty permissive `PROPOSED` schema. | Only that a scaffold exists; no field contract. |
| Map LayerManifest | Empty permissive `PROPOSED` schema. | No rich validation or typed adapter. |
| Data LayerManifest | Requires `id`; optional `version`/`spec_hash`; permits extras. | Minimal placeholder validation only. |
| Layers LayerManifest | Empty permissive `PROPOSED` schema. | No rich validation or typed adapter. |
| TileArtifactManifest | Empty permissive `PROPOSED` schema. | No typed tile-manifest adapter. |
| KFMGeoManifest | Requires `id`; optional `version`/`spec_hash`; permits extras. | Minimal placeholder validation only; rich semantics remain proposed. |

### Completeness rule

Schema validity against a permissive scaffold must never be interpreted as:

- evidence closure;
- complete provenance;
- valid CRS;
- valid bbox;
- valid geometry;
- policy clearance;
- rights clearance;
- sensitivity clearance;
- review approval;
- release approval;
- renderer readiness.

### Schema-home conflict handling

For LayerManifest, callers must provide an explicit profile such as:

```text
kfm-layer-manifest/data/v1
kfm-layer-manifest/map/v1
kfm-layer-manifest/layers/v1
```

These identifiers are illustrative. The accepted profile names must come from an ADR, registry, or contract decision.

[Back to top](#top)

---

## MapLibre boundary

The verified adjacent package is:

```text
packages/maplibre/
```

That package claims renderer-adapter and source/layer/style descriptor helper responsibilities. This geo module should therefore remain below or beside the renderer adapter boundary.

### Geo module may provide

- CRS and bbox primitives;
- geometry and transform issue carriers;
- source/public geometry candidates;
- scale, precision, and uncertainty carriers;
- manifest primitive fragments under explicit profiles.

### MapLibre package or app surface owns

- MapLibre source/layer/style descriptors;
- renderer-specific validation;
- add-source/add-layer sequencing;
- sprites, glyphs, style expressions, and renderer configuration;
- map shell behavior;
- user interaction and rendering.

### Dependency rule

A future dependency should normally point:

```text
packages/maplibre/ or governed app
    -> accepted geo helper API
```

Not:

```text
packages/geo/src/geo/
    -> renderer or UI package
```

The geo module must not import MapLibre runtime code merely to validate generic geometry.

[Back to top](#top)

---

## Accepted inputs

Inputs must be explicit, immutable or treated as immutable, and bounded.

| Input family | Accepted examples | Required handling |
|---|---|---|
| Profile context | contract/schema/profile ids and hashes | Require explicit selection; reject unknown combinations. |
| CRS context | source/target CRS refs, axis order, epoch, vertical reference, operation ref | Preserve identity; no assumptions. |
| Geometry candidate | GeoJSON-like object, WKB/WKT bytes/string, bbox, extent, geometry ref | Require an accepted representation profile and size limits. |
| Scale context | source scale, representation scale, resolution, zoom range, precision policy | Preserve distinctions and source limitations. |
| Uncertainty context | quantitative or qualitative limitation plus method/source | Carry forward; do not erase. |
| Transform context | explicit transform id/profile, parameters, resource refs, engine/version | No ambient transform selection. |
| Policy context | policy decision ref, audience, obligations, disclosure posture | Consume supplied decision; do not evaluate policy. |
| Evidence context | EvidenceRef, EvidenceBundle ref, source descriptor ref, validation refs | Preserve refs; no evidence fabrication. |
| Manifest context | explicit manifest profile and owner | Produce candidate fragments only. |
| Release context | release/correction/rollback refs supplied by callers | Carry refs; do not approve release. |
| Fixture context | synthetic geometries and expected deterministic outcomes | No real sensitive coordinates. |

### Rejected input patterns

Reject or issue on:

- missing required profile;
- unbounded stream or object;
- non-finite coordinates;
- unknown axis order;
- implicit CRS;
- unpinned transform;
- remote resource dependency;
- mutable hidden global configuration;
- source-system URL intended for fetching;
- policy text instead of a decision/reference;
- public-safe request without policy context;
- sensitive fixture data;
- unsupported geometry collection nesting.

[Back to top](#top)

---

## Permitted outputs

Outputs are **candidates**, not trust decisions.

| Output family | Permitted content | Must not imply |
|---|---|---|
| Parsed carrier | Original value, normalized representation, profile, issues | Authority or closure |
| CRS issue result | Explicit mismatch/missing/unsupported issues | Transform approval |
| Geometry inspection result | Structural observations under a named profile | Publication validity |
| Bbox/extent result | Computed/compared bbox plus CRS/axis/wrap context | Evidence support |
| Scale/precision result | Supported/unsupported range and caveats | Accuracy improvement |
| Uncertainty carrier | Explicit limitation metadata | Truth confidence |
| Transform plan | Named operation and parameters for later execution/review | Operation performed |
| Derived geometry candidate | Output plus before/after refs and loss metadata | Public-safe release |
| Public geometry candidate | Policy-bound transformed candidate plus obligations | Policy or release approval |
| Manifest fragment candidate | Fields for one explicit manifest profile | Complete manifest |
| Receipt candidate fields | Data for owning receipt system | Persisted receipt |
| Issue list | Stable code, severity, path, message, refs | Runtime envelope outcome unless mapped elsewhere |

### Output invariants

Every output must:

- preserve the selected profile;
- preserve original input or a stable input reference/digest;
- identify whether geometry changed;
- preserve before/after CRS and precision where applicable;
- carry issues and limitations;
- avoid hidden network or datastore side effects;
- avoid policy or release claims;
- remain serializable through an accepted owning contract before persistence.

[Back to top](#top)

---

## Proposed module interface

No interface below is implemented or accepted. It is a bounded design candidate.

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class GeoIssue:
    code: str
    severity: str
    path: str | None = None
    message: str | None = None


@dataclass(frozen=True)
class GeoProfile:
    profile_id: str
    profile_version: str
    contract_ref: str | None
    schema_ref: str | None
    crs_profile_ref: str | None
    geometry_profile_ref: str | None
    transform_profile_ref: str | None


@dataclass(frozen=True)
class GeometryInspection:
    profile: GeoProfile
    valid_local_shape: bool
    changed: bool
    normalized_candidate: Mapping[str, Any] | None
    issues: Sequence[GeoIssue]


def inspect_geometry_candidate(
    *,
    geometry: Mapping[str, Any],
    profile: GeoProfile,
    limits: Mapping[str, int],
) -> GeometryInspection:
    ...
```

### Interface rules

1. The profile is required.
2. No function fetches data or CRS resources.
3. No function chooses policy.
4. No function publishes or persists.
5. A function that changes geometry must say so.
6. A transform function is distinct from an inspection function.
7. Unknown fields/profiles are not silently normalized.
8. Exceptions are reserved for programmer/configuration failures; expected invalid data returns typed issues.
9. Public exports remain minimal and intentional.
10. Top-level namespace collision risk for `geo` must be reviewed before publication.

### Proposed module split

```text
packages/geo/src/geo/
├── README.md                 # This contract
├── __init__.py               # Deliberate public export boundary
├── profiles.py               # Accepted profile carriers
├── issues.py                 # Stable local issue carriers
├── crs.py                    # Explicit CRS/operation inspection
├── geometry.py               # Representation/structure inspection
├── bbox.py                   # Bbox/extent calculations under explicit profile
├── scale.py                  # Scale/resolution/precision checks
├── uncertainty.py            # Spatial uncertainty carriers
├── transforms.py             # Explicit pure transform execution, if admitted
├── public_safe.py            # Policy-bound candidate assembly, if admitted
├── manifests.py              # Explicit-profile fragment assembly
└── py.typed                  # Only if typed-package policy is accepted
```

All paths except the existing README and initializer are **PROPOSED**.

[Back to top](#top)

---

## Dependency and import direction

### Allowed dependency direction

```text
contracts/schemas/policy decisions supplied as data
                    ↓
generated or local carriers
                    ↓
geo pure helpers
                    ↓
validators / pipelines / map adapters / governed apps
                    ↓
receipts / proofs / release / governed API
```

### Forbidden dependency direction

The module must not import:

- connectors;
- lifecycle stores;
- registry clients;
- proof or receipt persistence;
- policy engines;
- release writers;
- API routers;
- UI components;
- MapLibre renderer runtime;
- model providers;
- application service containers.

### Third-party dependency admission

Before adding a spatial dependency, record:

- package and version range;
- binary/native requirements;
- license;
- platform support;
- deterministic behavior limits;
- embedded CRS/database version;
- network behavior;
- grid/resource behavior;
- topology/repair semantics;
- thread/process safety;
- security update plan;
- wheel/build availability;
- reproducibility and rollback posture.

Do not casually add GDAL, PROJ, GEOS, Shapely, GeoPandas, Rasterio, PyProj, or similar libraries without package-level review. This README does not recommend or reject any specific dependency; none are declared today.

### Import-time safety

Importing `geo` must not:

- open files;
- read environment secrets;
- inspect local CRS databases;
- download grids;
- initialize network clients;
- scan registries;
- connect to databases;
- load model providers;
- inspect lifecycle stores;
- mutate global precision or axis-order settings;
- emit receipts or logs containing sensitive coordinates.

[Back to top](#top)

---

## Failure and outcome semantics

The old README lists `VALID`, `INVALID`, `ABSTAIN_READY`, `DENY_READY`, `GENERALIZED`, and `WITHHELD`. No accepted geo-result contract or schema was found.

Therefore those terms remain **PROPOSED planning vocabulary**, not a public enum.

### Recommended separation

| Layer | Candidate outcomes | Owner |
|---|---|---|
| Local geo inspection | `valid`, `invalid`, `unsupported`, `indeterminate` plus issues | Geo helper contract, if accepted |
| Transform execution | `not_run`, `succeeded`, `failed`, `lossy`, `unsupported` plus receipt candidate | Transform contract/tool |
| Policy/geoprivacy | allow/restrict/generalize/withhold/deny/abstain posture | Policy system |
| Validation | valid/invalid report with findings | Validator and ValidationReport contract |
| Runtime/public | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Governed runtime envelope |
| Release | candidate/released/degraded/superseded/withdrawn/rolled_back | Release system |

Do not collapse these layers into one enum.

### Fail-closed conditions

The helper should return invalid/unsupported/indeterminate issues when:

- CRS is missing or ambiguous;
- axis order is unresolved;
- operation/profile is unpinned;
- coordinates are non-finite;
- limits are exceeded;
- geometry representation is unsupported;
- source scale or precision support is absent when required;
- sensitivity/public-safe context is missing for a public transform;
- requested profile is conflicted or unknown;
- a declared schema validator is unavailable;
- transform resources are missing;
- information would be lost without an explicit accepted adapter.

### Error hygiene

Errors must not expose:

- precise sensitive coordinates;
- raw protected geometry;
- source credentials;
- private file paths;
- hidden internal URLs;
- unrestricted policy context;
- living-person or private-property details.

[Back to top](#top)

---

## Lifecycle, policy, release, and public safety

### Lifecycle invariant

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Geo helper code may be called within governed flows. It does not own or advance lifecycle state.

### Trust sequence

A consequential public spatial output should follow:

```text
admitted source + source role + rights
    -> lifecycle-controlled geometry
    -> explicit geo profile and transform
    -> validation and transform receipt
    -> EvidenceRef -> EvidenceBundle closure
    -> policy / sensitivity / geoprivacy decision
    -> review and release decision
    -> governed API / released artifact
    -> MapLibre or export surface
```

### Anti-collapse rules

```text
parse success              != spatial truth
schema validity            != geometry validity
geometry validity          != evidence closure
transform success          != improved accuracy
generalization             != policy approval
public geometry candidate  != released geometry
manifest shape             != complete manifest
manifest validity          != release
map rendering              != publication authority
```

### Derived stays derived

A derived, repaired, transformed, generalized, centroided, aggregated, or simplified geometry must retain derived status and provenance. It must not replace canonical/source geometry without a governed state transition and correction path.

### Public client boundary

Public clients must not:

- import this module;
- call it as a network service directly;
- receive internal source geometry because a helper succeeded;
- infer public safety from map zoom or style;
- read canonical/internal stores through package shortcuts.

[Back to top](#top)

---

## Security, privacy, and sensitive-location controls

### Threats

Review for:

- geometry bombs and deeply nested collections;
- excessive coordinate counts;
- decompression or parser bombs;
- non-finite values;
- integer/float overflow;
- malicious WKT/WKB/GeoJSON payloads;
- path or URL injection in resource references;
- untrusted CRS definitions;
- network-triggering grid/resource lookup;
- topology operations with unbounded runtime;
- sensitive-coordinate leakage in logs, exceptions, fixtures, snapshots, or telemetry;
- cache keys that embed private geometry;
- cross-tenant or audience confusion;
- generalization that remains re-identifiable;
- inverse-transform disclosure.

### Required controls

- explicit input size and complexity limits;
- no network by default;
- no ambient filesystem/resource scanning;
- pinned profiles and engines;
- sanitized errors;
- coordinate redaction in logs;
- synthetic fixtures;
- property and adversarial tests;
- time and memory budgets;
- cancellation support where relevant;
- immutable policy and profile inputs;
- no in-place mutation of source geometry;
- explicit output classification;
- correction and rollback hooks.

### Sensitive fixture rule

Never place real precise locations for:

- rare or protected species;
- archaeological/cultural sites;
- critical infrastructure;
- private residences or private-property details;
- living-person events;
- tribal/sovereignty-restricted records;
- restricted environmental hazards;
- security-sensitive facilities.

Use synthetic coordinates or clearly non-sensitive public examples approved for fixture use.

[Back to top](#top)

---

## Tests, fixtures, validators, and CI

### Current status

| Surface | Status |
|---|---:|
| Package-specific test README at `tests/packages/geo/README.md` | **NOT FOUND at exact path** |
| Package-specific fixture README at `fixtures/packages/geo/README.md` | **NOT FOUND at exact path** |
| Dedicated `.github/workflows/geo.yml` | **NOT FOUND at exact path** |
| KFMGeoManifest validator declared by schema | **NOT FOUND at exact path** |
| KFMGeoManifest fixture README | **NOT FOUND at exact path** |
| Map/context/manifest schema enforcement | **Permissive/minimal scaffolds** |

### Required test families before implementation claims

#### Import and packaging

- wheel contains the intended namespace;
- import works in a clean environment;
- import has no side effects;
- exported symbols are intentional;
- namespace collision behavior is understood;
- minimum and maximum supported Python versions are tested.

#### CRS

- missing CRS;
- unsupported CRS;
- axis-order ambiguity;
- coordinate epoch required;
- vertical reference missing;
- operation not pinned;
- missing grid resource;
- lower-accuracy fallback prohibited;
- antimeridian/wrap profile behavior;
- no network lookup.

#### Geometry

- valid examples under each accepted profile;
- malformed nesting;
- empty geometry;
- non-finite coordinates;
- unsupported dimensions;
- excessive nesting and coordinate counts;
- bbox mismatch;
- ring closure/orientation issues;
- self-intersection/topology issues under pinned engine;
- geometry collection limits;
- no silent repair;
- before/after identity for explicit transforms.

#### Scale and uncertainty

- false precision detection;
- source scale versus renderer zoom;
- representation scale versus source accuracy;
- uncertainty preservation;
- missing uncertainty when required;
- unit mismatch;
- temporal/spatial scope mismatch.

#### Public-safe transforms

- policy context required;
- source/internal geometry preserved;
- generalized geometry marked derived;
- transform parameters receiptable;
- denied/withheld context not leaked;
- re-identification risk cases;
- synthetic fixtures only;
- rollback to prior public candidate.

#### Contracts and drift

- explicit schema/profile required;
- three LayerManifest profiles cannot be silently interchanged;
- permissive schema success does not imply completeness;
- generated models match pinned schema hashes;
- missing validator is visible;
- unknown fields are handled per selected profile;
- compatibility adapters preserve information or fail.

### CI admission

A future workflow must execute real tests. A job that only echoes a TODO is not behavioral proof.

Minimum CI should cover:

```text
format/lint
type checks, if adopted
unit tests
property/adversarial geometry tests
no-network test
schema/profile drift test
wheel build and clean install
import-side-effect test
dependency/security scan
sensitive-fixture scan
```

[Back to top](#top)

---

## Implementation admission sequence

The smallest useful reversible path is:

### Stage 0 — settle profiles

1. Assign owners.
2. Resolve or explicitly version the LayerManifest schema-home conflict.
3. Accept canonical profiles for CRS, bbox/extent, geometry representation, scale/precision, uncertainty, transform metadata, and local geo results.
4. Decide the role of KFMGeoManifest versus LayerManifest and TileArtifactManifest.
5. Decide whether the top-level import namespace `geo` is acceptable.
6. Define reason-code ownership and runtime mapping.
7. Define public-safe transform and geoprivacy handoff.

### Stage 1 — package metadata

1. Add build backend.
2. Add supported Python range.
3. Add license and package metadata.
4. Configure source discovery.
5. Declare only reviewed dependencies.
6. Add wheel-build and clean-install tests.

### Stage 2 — non-transforming primitives

Implement only:

- profile carriers;
- issue carriers;
- finite-number and limit checks;
- explicit bbox/extent calculations;
- scale/precision comparisons;
- uncertainty carriers;
- no side effects.

No reprojection, repair, simplification, or public-safe transform yet.

### Stage 3 — geometry inspection

After profiles and engine decisions:

- add representation parsing;
- add structural inspection;
- add pinned topology checks;
- preserve input unchanged;
- add adversarial tests;
- emit deterministic issues.

### Stage 4 — explicit transforms

Only after transform contracts and receipts exist:

- pinned coordinate operations;
- explicit normalization/repair transforms;
- before/after identity;
- loss disclosure;
- transform receipt candidates;
- no ambient fallback.

### Stage 5 — public-safe candidate assembly

Only after policy/geoprivacy contracts and tests exist:

- consume supplied policy decisions;
- execute only accepted transforms;
- preserve exact/internal geometry separately;
- emit public candidate plus obligations;
- integrate correction and rollback.

### Stage 6 — manifest adapters and consumers

After manifest profiles are settled:

- add explicit-profile adapters;
- verify one governed internal consumer;
- keep public clients behind governed APIs;
- add release and rollback integration tests.

Each stage should be independently reviewable and revertible.

[Back to top](#top)

---

## Compatibility, correction, and rollback

### Compatibility rules

- Version every accepted profile.
- Never reinterpret an existing profile silently.
- Keep adapters explicit and directional.
- Record information loss.
- Preserve unknown fields only when the selected profile permits it.
- Do not use permissive schema scaffolds as compatibility catch-alls.
- Keep source and derived/public geometries distinguishable.
- Pin transform engine/resource versions when output identity depends on them.
- Retain old adapters until consumers migrate or a breaking-change record approves removal.

### Correction propagation

When source geometry, CRS profile, transform profile, sensitivity, rights, or evidence changes, owning systems may need to invalidate:

- derived geometry candidates;
- fingerprints/hashes;
- transform receipts;
- layer/tile/geo manifests;
- catalog projections;
- release candidates;
- cached public geometry;
- map/export artifacts.

This module may compute candidate dependency keys or issue notices. It does not perform repository-wide correction or release withdrawal.

### Rollback

Documentation rollback:

```text
restore prior blob: 9f0038e5bd6e0699cca6b9d4587de0d1a6b8ea07
```

Future code rollback must identify:

- package version;
- profile versions;
- dependency/resource versions;
- affected consumers;
- derived outputs;
- release/correction records;
- last known-safe public geometry/artifact;
- cache invalidation steps.

### Conditions requiring rollback

Rollback or disable the module if it:

- silently guesses CRS or axis order;
- repairs or transforms geometry without provenance;
- leaks exact sensitive locations;
- reaches the network unexpectedly;
- treats local validity as policy or release approval;
- bypasses evidence or governed APIs;
- writes lifecycle, proof, receipt, or release state;
- makes schema-family selection ambiguous;
- produces non-deterministic output without recording cause;
- breaks source/public geometry separation.

[Back to top](#top)

---

## Validation commands

### Repository inspection

```bash
git rev-parse HEAD
find packages/geo -maxdepth 5 -type f -print | sort
sed -n '1,220p' packages/geo/pyproject.toml
sed -n '1,260p' packages/geo/README.md
sed -n '1,260p' packages/geo/src/README.md
sed -n '1,260p' packages/geo/src/geo/README.md
git grep -n "from geo\|import geo" -- . ':!packages/geo/**/*.md' || true
```

### Contract and schema inspection

```bash
find contracts schemas/contracts/v1 -type f \
  \( -iname '*geo*' -o -iname '*geometry*' -o -iname '*crs*' \
     -o -iname '*layer_manifest*' -o -iname '*tile_artifact*' \
     -o -iname '*map_context*' \) -print | sort

python -m json.tool schemas/contracts/v1/ui/map_context_envelope.schema.json >/dev/null
python -m json.tool schemas/contracts/v1/map/layer_manifest.schema.json >/dev/null
python -m json.tool schemas/contracts/v1/data/layer_manifest.schema.json >/dev/null
python -m json.tool schemas/contracts/v1/layers/layer_manifest.schema.json >/dev/null
python -m json.tool schemas/contracts/v1/map/tile_artifact_manifest.schema.json >/dev/null
python -m json.tool schemas/contracts/v1/evidence/kfm_geo_manifest.schema.json >/dev/null
```

### README checks

```bash
python - <<'PY'
from pathlib import Path

path = Path("packages/geo/src/geo/README.md")
text = path.read_text(encoding="utf-8")

assert text.count("# Governed Geospatial Primitive Helper Module") == 1
assert "\t" not in text
assert not any(line.rstrip() != line for line in text.splitlines())
assert text.count("```") % 2 == 0

print("basic README checks passed")
PY
```

### Future package checks

After implementation and package metadata exist:

```bash
# PROPOSED examples only
python -m pytest tests/packages/geo
python -m build packages/geo
python -m pip install --no-deps --force-reinstall packages/geo/dist/*.whl
python -c "import geo"
```

Do not copy proposed commands into CI until package metadata, test paths, and namespace are accepted.

[Back to top](#top)

---

## Definition of done

### This README revision

This revision is done when it:

- replaces stale implementation assumptions with current repository evidence;
- records the `kfm-geo` `0.0.0` scaffold and empty initializer;
- records selected absent helper modules and package test/fixture/workflow paths;
- distinguishes architecture vocabulary from implemented APIs;
- identifies actual MapContextEnvelope and MapLibre paths;
- surfaces the LayerManifest schema-home conflict;
- bounds permissive/minimal manifest schemas;
- preserves contracts/schema/policy/release/data authority boundaries;
- separates source, derived, and public geometry;
- forbids silent repair, transform, CRS guessing, and false precision;
- defines security, testing, compatibility, correction, and rollback posture;
- changes only this README.

### Future module implementation

Implementation is not done until:

- [ ] owners are assigned;
- [ ] package and source-root docs are reconciled;
- [ ] build backend and Python range are declared;
- [ ] namespace/package discovery is proven;
- [ ] dependencies are reviewed;
- [ ] canonical CRS, geometry, bbox, scale, uncertainty, transform, and result profiles are accepted;
- [ ] LayerManifest profile conflict is resolved or explicitly versioned;
- [ ] KFMGeoManifest validator/fixtures are established if used;
- [ ] public exports are intentional;
- [ ] package-specific tests and fixtures exist;
- [ ] real CI runs the tests;
- [ ] no-network/import-side-effect behavior is proven;
- [ ] adversarial resource-limit tests pass;
- [ ] sensitive-location tests pass;
- [ ] no silent repair or fallback is proven;
- [ ] one governed internal consumer is verified;
- [ ] public clients remain behind governed APIs and released artifacts;
- [ ] correction and rollback are tested;
- [ ] production and publication claims are evidence-backed.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Closure evidence |
|---|---|---:|---|
| `GEO-MOD-001` | Who owns the `kfm-geo` package and module? | UNKNOWN | CODEOWNERS/steward assignment |
| `GEO-MOD-002` | Is the top-level import namespace `geo` accepted and collision-safe? | NEEDS VERIFICATION | Packaging/namespace decision and clean import test |
| `GEO-MOD-003` | What Python versions are supported? | UNKNOWN | `requires-python` plus CI matrix |
| `GEO-MOD-004` | What build backend and discovery configuration are accepted? | UNKNOWN | `pyproject.toml` and wheel inspection |
| `GEO-MOD-005` | Which dependencies are required? | UNKNOWN | Reviewed dependency decision |
| `GEO-MOD-006` | Which real consumers require this module? | UNKNOWN | Verified import/usage inventory |
| `GEO-MOD-007` | What is the canonical CRS profile contract/schema? | NEEDS VERIFICATION | Accepted contract/schema/registry |
| `GEO-MOD-008` | How are axis order, vertical reference, and coordinate epoch represented? | NEEDS VERIFICATION | Accepted CRS profile |
| `GEO-MOD-009` | What coordinate-operation selection policy applies? | UNKNOWN | ADR/profile and deterministic tests |
| `GEO-MOD-010` | Which CRS grids/resources may be used and how are they pinned? | UNKNOWN | Resource manifest and package tests |
| `GEO-MOD-011` | What geometry representations are accepted? | NEEDS VERIFICATION | Contract/schema profile |
| `GEO-MOD-012` | Which geometry validity engine/profile is canonical? | UNKNOWN | Engine/version decision and fixtures |
| `GEO-MOD-013` | What resource limits apply to geometry inputs? | UNKNOWN | Security profile and adversarial tests |
| `GEO-MOD-014` | What bbox/extent axis and antimeridian semantics apply? | NEEDS VERIFICATION | Accepted bbox profile |
| `GEO-MOD-015` | What scale-support profile is canonical? | NEEDS VERIFICATION | Contract/schema/source-descriptor decision |
| `GEO-MOD-016` | How are precision, accuracy, resolution, and uncertainty represented separately? | NEEDS VERIFICATION | Accepted contracts and tests |
| `GEO-MOD-017` | What transform classes may this module execute? | NEEDS DECISION | Package-boundary/ADR decision |
| `GEO-MOD-018` | What transform receipt contract is accepted? | UNKNOWN | Contract/schema/validator/fixtures |
| `GEO-MOD-019` | Who owns generalization and public-safe geometry transforms? | NEEDS VERIFICATION | Policy/package/pipeline boundary record |
| `GEO-MOD-020` | What geoprivacy policy handoff is required? | UNKNOWN | Policy contract and integration tests |
| `GEO-MOD-021` | How are source/internal and public geometry linked without overwrite? | NEEDS VERIFICATION | Contract/schema and correction tests |
| `GEO-MOD-022` | Which LayerManifest schema family is canonical? | CONFLICTED | ADR or versioned profile registry |
| `GEO-MOD-023` | What fields make a LayerManifest complete? | NEEDS VERIFICATION | Accepted contract/schema pair |
| `GEO-MOD-024` | What is the canonical TileArtifactManifest profile? | NEEDS VERIFICATION | Accepted contract/schema pair |
| `GEO-MOD-025` | What is the canonical MapContextEnvelope profile? | NEEDS VERIFICATION | Accepted UI contract/schema pair |
| `GEO-MOD-026` | What is the canonical KFMGeoManifest profile? | NEEDS VERIFICATION | Contract/schema migration and fixtures |
| `GEO-MOD-027` | Will the missing KFMGeoManifest validator be added or metadata corrected? | CONFLICTED | File addition or schema update |
| `GEO-MOD-028` | Where do KFMGeoManifest fixtures live? | NEEDS VERIFICATION | Verified fixture inventory |
| `GEO-MOD-029` | What local geo-result and issue-code contract is accepted? | UNKNOWN | Contract/schema/reason-code registry |
| `GEO-MOD-030` | How do local issues map to ValidationReport and runtime outcomes? | UNKNOWN | Adapter contract and tests |
| `GEO-MOD-031` | Should `packages/maplibre/` consume this module directly? | NEEDS VERIFICATION | Dependency/consumer decision |
| `GEO-MOD-032` | Where do package behavior tests and fixtures live? | NEEDS VERIFICATION | Accepted paths and inventory |
| `GEO-MOD-033` | Is a dedicated geo workflow required? | NEEDS VERIFICATION | Workflow decision and real steps |
| `GEO-MOD-034` | How are generated schema models versioned and checked for drift? | UNKNOWN | Generator contract and CI |
| `GEO-MOD-035` | How are transform outputs fingerprinted? | UNKNOWN | Hash/canonicalization profile |
| `GEO-MOD-036` | What correction invalidates derived/public geometry and manifests? | UNKNOWN | Correction/supersession dependency contract |
| `GEO-MOD-037` | How are cached public geometries withdrawn? | UNKNOWN | Release/runtime rollback procedure |
| `GEO-MOD-038` | What telemetry is allowed without leaking coordinates? | UNKNOWN | Observability/privacy policy and tests |
| `GEO-MOD-039` | Is package publication intended? | UNKNOWN | Release record and package artifact |
| `GEO-MOD-040` | What is the tested consumer rollback procedure? | UNKNOWN | Rollback test and runbook |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---:|---|---|
| Previous module README | CONFIRMED | Existing planning intent and safety boundaries | Did not prove implementation |
| `packages/geo/pyproject.toml` | CONFIRMED minimal scaffold | Distribution name and `0.0.0` version | No build, dependency, or Python support proof |
| Parent package/source READMEs | CONFIRMED planning docs | Intended geo helper responsibility | Still contain unverified paths and implementation assumptions |
| Empty `geo/__init__.py` | CONFIRMED | Import-package marker | No exports or behavior |
| Exact module-path checks | CONFIRMED bounded absences | Selected helper modules absent | Not a recursive proof of all spatial code elsewhere |
| Exact test/fixture/workflow checks | CONFIRMED bounded absences | Conventional package lanes absent | Does not prove no related tests/workflows elsewhere |
| Directory Rules v1.4 | CONFIRMED doctrine | Authority-root and lifecycle separation | Does not choose geo APIs/profiles |
| Spatial Foundation architecture | CONFIRMED document; mixed doctrine/implementation posture | Ubiquitous language and cross-domain boundary | Field realization and repo wiring remain proposed |
| `packages/maplibre/README.md` | CONFIRMED README | Actual adjacent MapLibre package lane | Implementation maturity remains separately unverified |
| UI MapContextEnvelope schema | CONFIRMED `PROPOSED` scaffold | Actual schema path | Empty permissive shape |
| Map LayerManifest schema | CONFIRMED `PROPOSED` scaffold | One schema family | Empty permissive shape |
| Data LayerManifest schema | CONFIRMED `PROPOSED` placeholder | Current data-family pairing | Requires only `id`; permits extras |
| Layers LayerManifest schema | CONFIRMED `PROPOSED` scaffold | Another schema family | Empty permissive shape |
| LayerManifest semantic contract | CONFIRMED draft contract | Rich meaning and explicit schema-home conflict | Schema does not enforce full semantics |
| TileArtifactManifest schema | CONFIRMED `PROPOSED` scaffold | Actual map-family path | Empty permissive shape |
| KFMGeoManifest contract | CONFIRMED draft contract | Rich geospatial artifact-manifest meaning and authority boundary | Field realization mostly proposed |
| KFMGeoManifest schema | CONFIRMED `PROPOSED` stub | `id`, optional `version`/`spec_hash` | Permissive and incomplete |
| KFMGeoManifest validator exact path | NOT FOUND | Metadata/file conflict | Does not prove no alternate validator exists |
| KFMGeoManifest fixture README exact path | NOT FOUND | Bounded fixture gap | Does not prove no individual fixtures exist elsewhere |
| Current revision workflow | CONFIRMED | One-file documentation update | Does not implement or validate geo behavior |

---

## Maintainer checklist

Before editing this module:

- [ ] Reconfirm current `main`.
- [ ] Recheck package metadata and source tree.
- [ ] Recheck parent package/source READMEs.
- [ ] Recheck accepted ADRs and profile registries.
- [ ] Recheck Spatial Foundation contracts/schemas.
- [ ] Recheck all LayerManifest schema families.
- [ ] Recheck KFMGeoManifest contract/schema/validator/fixtures.
- [ ] Recheck MapContextEnvelope and TileArtifactManifest profiles.
- [ ] Recheck MapLibre package boundary.
- [ ] Recheck consumers, tests, fixtures, and workflows.
- [ ] Mark implementation claims with truth status.
- [ ] Preserve exact versus public geometry separation.
- [ ] Preserve CRS, scale, precision, uncertainty, and transform provenance.
- [ ] Preserve evidence, policy, release, correction, and rollback refs.
- [ ] Keep network and persistence out of imports/helpers.
- [ ] Use synthetic, non-sensitive fixtures.
- [ ] Avoid silent repair, fallback, coercion, or profile translation.
- [ ] Make the smallest reversible change.

[Back to top](#top)
