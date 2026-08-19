<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/mvt
title: Mapbox Vector Tile (MVT) — KFM Encoding and Readiness Boundary
type: standard; encoding-guidance; carrier-readiness-boundary
version: v2.0-draft
status: "draft; repository-grounded; upstream-currentness-refreshed; no-adoption; no-conformance-proof; no-release; no-publication"
owners:
  - "@bartytime4life — verified default GitHub review route through the standards-lane boundary"
  - "NEEDS VERIFICATION — map/tile, standards, contract, schema, policy, evidence, release, security, performance, and independent-review stewards"
created: 2026-05-14
updated: 2026-08-18
policy_label: "repository-facing; standards-guidance; map; vector-tiles; public"
owning_root: docs/
current_path: docs/standards/MVT.md
responsibility: >
  Explain the upstream Mapbox Vector Tile encoding, distinguish it from tile
  transport and KFM governance, disclose the exact bounded MVT-related
  implementation currently present in the repository, and define the evidence
  required before KFM may claim conformance, activate a renderer consumer, or
  release a public MVT carrier.
truth_posture: >
  CONFIRMED current path, standards-lane placement, default review route,
  upstream MVT 2.1 identity and encoding semantics, current fixture-only
  LayerManifest profile, current inactive geospatial-carrier metadata preflight,
  current non-canonical PMTiles/MVT compatibility slice, permissive unresolved
  TileArtifactManifest schema, and MapLibre package scaffold / PROPOSED active
  KFM MVT profile, binary validator, producer, consumer, catalog binding,
  release integration, MVT-to-MLT migration policy, performance admission,
  correction, and rollback behavior / UNKNOWN production MVT generation,
  runtime loading, deployed serving, released artifacts, consumer
  interoperability, and accountable specialist stewardship.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: c9cdafedec9e29fa8e9a28834601c1d426dd0e83
  target_prior_blob: f4ebfd0b8ec3b6344d69b430c015108ff9b3ec00
  standards_readme_blob: a8cbe5d183448d5f0de37f8a4eacd6fcaca0d71b
  layer_manifest_contract_blob: 234dca70e768ee744f7d78109afc6e0dc745af1b
  layer_manifest_schema_blob: abca306cb271ed75127a83dd05b73830ba20773b
  tile_artifact_contract_blob: 138e2d97b0d0bd7311c7c36a45ed983bae63b154
  tile_artifact_schema_blob: ed8fb0834c06a6254d6175f9a08b8d17ccc68d71
  carrier_readiness_contract_blob: 17055a680b83a4f83834735e88aeb0569322845b
  carrier_readiness_schema_blob: b6ebec77a6e09c50b89594c4032bd40ec238f6be
  carrier_readiness_validator_blob: 63e4cfac4838d0095b7f05fc6a3507ebe180fd8b
  pmtiles_fixture_readme_blob: a9e8d87db4688c69e88121e15542ac1f3abc7c55
external_currentness_review:
  access_date: 2026-08-18
  upstream_mvt: "Mapbox Vector Tile Specification 2.1"
  upstream_maplibre: "Vector-source encoding distinguishes MVT and MLT; scheme is configured separately"
  currentness_risk: "MVT 2.1 is stable; MapLibre and MLT implementation status remains version-sensitive"
related:
  - ./README.md
  - ./PMTILES.md
  - ./OGC-API-TILES.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../contracts/data/layer_manifest.md
  - ../../schemas/contracts/v1/data/layer_manifest.schema.json
  - ../../tools/validators/data/validate_layer_manifest.py
  - ../../tests/validators/test_validate_layer_manifest.py
  - ../../contracts/release/tile_artifact_manifest.md
  - ../../schemas/contracts/v1/map/tile_artifact_manifest.schema.json
  - ../../contracts/release/geospatial_carrier_readiness.md
  - ../../schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json
  - ../../tools/validators/release/validate_geospatial_carrier_readiness.py
  - ../../fixtures/contracts/v1/release/geospatial_carrier_readiness/cases.json
  - ../../tests/release/test_geospatial_carrier_readiness.py
  - ../../.github/workflows/geospatial-carrier-readiness.yml
  - ../../fixtures/pmtiles/attestation/README.md
  - ../../tools/validators/pmtiles/validate_attestation_bundle.py
  - ../../tests/validators/test_pmtiles_attestation_bundle.py
  - ../../packages/maplibre/README.md
tags: [kfm, standards, mvt, vector-tiles, pmtiles, maplibre, carrier-readiness, evidence, release]
notes:
  - "Same-path documentation modernization only; no contract, schema, policy, fixture, validator, workflow, package, source, tile artifact, release object, runtime, deployment, or public product changes."
  - "The prior page overstated KFM-wide adoption and implementation. This revision separates upstream MVT conformance, inactive metadata checks, binary verification, runtime consumption, release, and publication."
  - "The current repository's MVT readiness validator accepts the 2.x family while its positive fixture declares 2.1; exact-version convergence remains NEEDS VERIFICATION."
  - "The prior MLT pilot-only statement is no longer presented as upstream fact. Upstream MapLibre recognizes MVT and MLT encodings, while KFM adoption and migration remain unverified."
  - "Legacy title and numbered-section anchors are retained for inbound-link compatibility."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="mapbox-vector-tiles-mvt--kfm-conformance-standard"></a>

# Mapbox Vector Tile (MVT) — KFM Encoding and Readiness Boundary

> **Purpose.** Explain what the Mapbox Vector Tile specification governs, what KFM currently checks, what remains inactive or unimplemented, and what must be proven before a vector-tile carrier may participate in a governed release.

![status](https://img.shields.io/badge/status-v2.0--draft-d4a72c?style=flat-square)
![evidence](https://img.shields.io/badge/evidence-repository--grounded-1a7f37?style=flat-square)
![upstream](https://img.shields.io/badge/upstream-MVT--2.1-0969da?style=flat-square)
![profile](https://img.shields.io/badge/KFM_profile-PROPOSED__INACTIVE-b54708?style=flat-square)
![binary](https://img.shields.io/badge/binary__conformance-NOT__ESTABLISHED-6e7781?style=flat-square)
![publication](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)

> [!IMPORTANT]
> **An MVT tile is a derived representation, not evidence, policy, review, release, or public truth.** Successful decoding, a valid source-layer name, a green fixture, a PMTiles archive, or a visible MapLibre layer does not establish that the source is authoritative, the geometry is safe, the attributes are publishable, or the artifact has been released.

> [!CAUTION]
> **Current KFM implementation is bounded and inactive.** The repository contains a fixture-only strict `LayerManifest` profile, an inactive metadata-only geospatial-carrier readiness check, and a non-canonical PMTiles/MVT compatibility slice. These surfaces do not parse arbitrary MVT bytes, emit production tiles, resolve evidence, execute policy, authenticate review, authorize release, or load a public map layer.

> [!WARNING]
> **Do not collapse encoding, tiling, container, transport, and release.** MVT is an encoding for vector-tile payloads. XYZ/TMS is tile addressing. Web Mercator or another coordinate model supplies the tile coordinate context. PMTiles, MBTiles, HTTP templates, or an API are delivery/container choices. KFM policy and release records decide exposure.

| Field | Current bounded result |
|---|---|
| **Evidence snapshot** | `main@c9cdafedec9e29fa8e9a28834601c1d426dd0e83` |
| **Directory result** | `PLACE` at the existing `docs/standards/MVT.md` path; accepted Directory Rules assign human-readable standards guidance to `docs/standards/` |
| **Upstream baseline** | Mapbox Vector Tile Specification `2.1` |
| **KFM adoption** | **NOT ESTABLISHED** as an accepted KFM-wide conformance profile or production-default decision |
| **Current strict metadata check** | `GeospatialCarrierReadinessCheck`, status `PROPOSED_INACTIVE`, metadata-only, no-network, finite `READY` / `HOLD` / `ERROR` |
| **Current layer carrier** | `LayerManifest` strict profile is `PROPOSED_INACTIVE` and `FIXTURE_ONLY`; legacy permissive profile remains |
| **Current PMTiles/MVT proof** | Non-canonical structural compatibility fixtures; no canonical `TileArtifactManifest` schema authority |
| **Binary MVT verification** | **NOT ESTABLISHED** by the inspected repository evidence |
| **Producer / browser consumer** | **NOT ESTABLISHED**; `packages/maplibre/` remains a package scaffold without a functioning adapter or known consumer |
| **Release / public effect** | None |

**Quick navigation:** [Status](#0-status--authority) · [Purpose](#1-purpose--scope) · [Upstream](#2-the-external-standard) · [KFM posture](#3-kfm-conformance-posture) · [Constraints](#4-kfm-specific-constraints-on-top-of-mvt) · [Lifecycle](#5-pipeline--lifecycle-placement) · [Objects](#6-required-object-families--manifests) · [Validation](#7-validation--ci-gates) · [Anti-patterns](#8-anti-patterns) · [MLT](#9-relationship-to-mlt-pilot-posture) · [Catalog](#10-stac--dcat--prov-crosswalk-for-mvt-artifacts) · [Open work](#11-open-questions--needs-verification) · [Glossary](#appendix-a--glossary) · [Example](#appendix-b--illustrative-manifest-fragment) · [Related](#related-docs)

---

## 0. Status & authority

### 0.1 Authority by question

| Question | Owning authority | Role of this page |
|---|---|---|
| What MVT 2.1 means | The official Mapbox Vector Tile specification and protobuf definition | Record the checked baseline; do not redefine it |
| Whether KFM adopts MVT | An accepted KFM decision, active profile, contract/schema set, and reviewed implementation evidence | State that adoption is not established |
| What `LayerManifest` means | [`contracts/data/layer_manifest.md`](../../contracts/data/layer_manifest.md) | Cite the current semantic boundary; do not replace it |
| What a tile artifact manifest means | [`contracts/release/tile_artifact_manifest.md`](../../contracts/release/tile_artifact_manifest.md) | Cite the proposed release-artifact pointer; expose the unresolved schema family |
| What machine shape is valid | Accepted schemas under `schemas/` | Cite exact current schemas and their status; do not promote a scaffold into authority |
| What metadata checks run | Current validator code, fixtures, tests, workflow, and generated evidence | State the checked, inactive boundary only |
| What MVT bytes contain | A binary parser/validator operating against pinned MVT 2.1 semantics | State that this proof is not established |
| What may be rendered or published | Policy, evidence, review, release, correction, rollback, and governed runtime authorities | Explain prerequisites; never approve exposure |
| Whether MVT or MLT is used by a browser | Current package dependencies, accepted adapter, style/source contracts, tests, and observed consumers | Keep runtime claims unknown without those proofs |

### 0.2 Truth labels

- **CONFIRMED** — verified from current repository bytes or authoritative upstream material at the named snapshot.
- **PROPOSED** — a KFM profile, requirement, path, validator, producer, consumer, release rule, migration step, or design not established as active behavior.
- **UNKNOWN** — evidence is insufficient for a stronger current claim.
- **NEEDS VERIFICATION** — a concrete repository, standards, implementation, policy, release, or consumer check can resolve the question.
- **CONFLICTED** — current surfaces disagree in identity, home, version, vocabulary, or authority.
- **HOLD** — a review/readiness posture; it is not equivalent to the public `PolicyDecision` outcome vocabulary.

### 0.3 Current repository evidence

| Surface | CONFIRMED observation | Safe conclusion |
|---|---|---|
| [`docs/standards/README.md`](./README.md) | This lane is human-readable standards guidance only and explicitly separates path, adoption, implementation, validation, release, and publication states | This page may explain MVT but cannot adopt or prove conformance |
| [`LayerManifest` contract](../../contracts/data/layer_manifest.md) | Dual profile: legacy permissive carrier plus closed `PROPOSED_INACTIVE` / `FIXTURE_ONLY` profile with deterministic local checks | A bounded candidate carrier exists; no active loader, reference resolution, policy, review, signing, release, or publication follows |
| [`LayerManifest` schema](../../schemas/contracts/v1/data/layer_manifest.schema.json) | Current strict representation supports `PMTILES`, `XYZ`, `COG`, and `GEOJSON_FIXTURE`; PMTiles/XYZ require a source layer | Current machine shape is a fixture profile, not a KFM-wide MVT conformance profile |
| [`TileArtifactManifest` contract](../../contracts/release/tile_artifact_manifest.md) | Semantic contract is proposed and schema-family ownership remains unresolved | Do not infer canonical tile-manifest shape from prose |
| [`map/tile_artifact_manifest` schema](../../schemas/contracts/v1/map/tile_artifact_manifest.schema.json) | Current schema is an open, property-free proposed scaffold | It cannot prove meaningful MVT artifact conformance |
| [`GeospatialCarrierReadinessCheck`](../../contracts/release/geospatial_carrier_readiness.md) | Inactive metadata preflight includes an MVT lane with finite `READY`, `HOLD`, and `ERROR` outcomes | The repository checks declared metadata only; no binary, source, evidence, policy, release, or publication proof |
| [`carrier readiness` schema and validator](../../schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json) | Closed schema plus deterministic no-network validator check MVT declarations such as version family, extent, scheme, source-layer parity, stable IDs, field closure, tile budget, geometry-drop count, area drift, tiler hash, and PMTiles/range posture | This is the strongest current executable MVT-related slice, but it is explicitly inactive and metadata-only |
| [`carrier readiness` fixtures](../../fixtures/contracts/v1/release/geospatial_carrier_readiness/cases.json) | Positive MVT fixture declares version `2.1`; negative cases cover tile budget and sensitive attributes | Fixture polarity is evidence for the bounded preflight, not production readiness |
| [`PMTiles attestation fixtures`](../../fixtures/pmtiles/attestation/README.md) | Synthetic PMTiles v3/MVT compatibility profile checks declared archive/header/vector-layer metadata and digest binding | Non-canonical structural compatibility only; no canonical schema, cryptographic, policy, or release authority |
| [`packages/maplibre/README.md`](../../packages/maplibre/README.md) | Package is a private `0.0.0` scaffold with placeholder export and no established functional adapter, dependency set, consumer, or active package API | Browser-side MVT loading is **UNKNOWN / not established by this review** |

Absence statements are bounded to indexed repository search and inspected paths. They do not claim that private services, historical branches, unindexed files, or external deployments never existed.

### 0.4 Official upstream checkpoint

The official upstream material checked on 2026-08-18 establishes:

- [MVT 2.1](https://github.com/mapbox/vector-tile-spec/tree/master/2.1) is the current published Mapbox Vector Tile specification in the official repository.
- The encoding uses Protocol Buffers and defines a tile as one or more named layers containing features, tags, and geometry command streams.
- Layer `version`, layer `name`, and feature geometry semantics are part of the encoded payload; a feature ID is optional.
- The protobuf layer extent defaults to `4096`, but the specification does not make `4096` the only permitted extent.
- MVT does not carry its own projection or geographic bounds. A producer and consumer must agree on the tile coordinate context.
- Web Mercator and the familiar slippy-map addressing model are reference conventions, not universal MVT requirements.
- The recommended file suffix is `.mvt`, and the registered media type used by the specification is `application/vnd.mapbox-vector-tile`.
- [MapLibre vector-source configuration](https://maplibre.org/maplibre-style-spec/sources/#vector) treats encoding and tile scheme as separate concerns and recognizes both `mvt` and `mlt` encodings.

### 0.5 Non-effects

This revision does **not**:

- adopt MVT or MLT for KFM;
- declare MVT the production default;
- change `GeospatialCarrierReadinessCheck` or activate its profile;
- select a canonical `TileArtifactManifest` schema family;
- create a binary MVT parser, encoder, tileset generator, style compiler, or MapLibre adapter;
- approve Tippecanoe, Planetiler, Tegola, Martin, t_rex, PMTiles, or another tool/version;
- activate a source, inspect restricted data, generate tiles, release an artifact, or publish a layer;
- accept a catalog, performance, security, correction, rollback, or MVT-to-MLT migration policy.

[Back to top](#top)

---

## 1. Purpose & scope

This page owns human-readable guidance for four distinct questions:

1. What does upstream MVT 2.1 encode?
2. Which additional declarations does KFM's current inactive metadata preflight check?
3. What proof is still missing before KFM may claim binary, tileset, runtime, or release conformance?
4. How should an MVT carrier remain subordinate to evidence, policy, review, correction, and rollback?

### 1.1 In scope

- upstream specification identity and core semantics;
- distinction between payload encoding, tile addressing, projection, container, and delivery;
- current repository MVT-related contracts, schemas, fixtures, validators, tests, and workflow boundaries;
- source-layer, attribute, feature-ID, geometry-loss, tile-budget, and deterministic-build concerns;
- MVT/PMTiles and MVT/MLT relationships;
- catalog, provenance, correction, supersession, withdrawal, and rollback expectations;
- evidence required for future activation.

### 1.2 Out of scope

- a legal or interoperability certification;
- authoring a canonical MVT profile through documentation alone;
- selecting or installing an encoder/runtime dependency;
- migrating current tile artifacts;
- defining source-specific field allowlists;
- selecting public endpoints, caches, CDNs, registries, or object stores;
- releasing or serving any tile bytes.

### 1.3 Four layers that must remain distinct

| Layer | Meaning | What it does not prove |
|---|---|---|
| **MVT payload** | One encoded tile containing named layers, features, tags, and geometry command streams | Tileset completeness, public safety, source authority, or release |
| **Tileset / container** | A pyramid or archive that organizes many tile payloads and delivery metadata | That every payload is MVT-conformant or policy-safe |
| **KFM readiness declaration** | Local metadata describing intended version, extent, source layers, fields, budgets, and bindings | That declarations match bytes, references resolve, or release is allowed |
| **Governed release** | Reviewed artifact binding with evidence, policy, release, correction, and rollback context | Canonical source truth; the release remains a derived carrier |

[Back to top](#top)

---

## 2. The external standard

MVT 2.1 is a compact vector-tile encoding. It defines the payload carried by one tile, not a complete tileset protocol, storage architecture, public API, catalog record, or governance system.

### 2.1 Version and representation

| Upstream concept | MVT 2.1 result | KFM consequence |
|---|---|---|
| Specification version | `2.1`; major and minor versioning are explicit | Future active KFM profiles should pin the exact supported version or an explicit compatible family |
| Payload serialization | Protocol Buffers | Binary validation requires parsing the protobuf payload, not inspecting metadata declarations alone |
| File/media convention | `.mvt`; `application/vnd.mapbox-vector-tile` | Container media type may differ; PMTiles containing MVT uses PMTiles media type for the archive |
| Layer version | Encoded per layer; MVT 2.1 uses major version `2` | A validator should inspect every encoded layer rather than trust one top-level declaration |
| Layer name | Required string inside each tile layer | Name agreement with manifests/styles is a KFM cross-surface requirement, not an upstream release decision |
| Extent | Integer tile-coordinate extent; protobuf default `4096` | `4096` is a valid KFM profile choice, not the only upstream-conformant value |

### 2.2 Feature and geometry semantics

- A feature may carry an unsigned integer ID. The upstream specification does not require KFM-style stability across releases.
- Feature attributes are encoded through layer-level key/value tables and per-feature tag indexes.
- Geometry types are `POINT`, `LINESTRING`, and `POLYGON`; multipart geometry is represented through repeated command sequences rather than separate MultiPoint/MultiLineString/MultiPolygon enum values.
- Geometry collections are not an MVT geometry type.
- Geometry coordinates are integer tile coordinates. The common tile-coordinate origin is the upper-left, with positive `y` downward.
- Polygon ring winding is interpreted in tile coordinates; producers must preserve valid exterior/interior ordering after clipping and quantization.
- The encoded payload does not retain arbitrary source CRS coordinates or a canonical geometry object.

### 2.3 What the standard leaves to profiles and applications

MVT does not decide:

- source authority or evidence support;
- which projection or tile matrix is used;
- XYZ versus TMS addressing;
- archive/container format;
- source-layer naming conventions across a product family;
- feature-ID persistence across releases;
- public attribute allowlists;
- rights, sensitivity, redaction, or generalization;
- tile-size budgets, rendering performance, or cache policy;
- catalog/provenance representation;
- correction, withdrawal, or rollback.

### 2.4 Upstream requirement versus current KFM candidate rule

| Concern | Upstream MVT | Current inactive KFM preflight |
|---|---|---|
| Version | Encoded layer version with current specification `2.1` | Validator currently accepts strings beginning `2.`; positive fixture uses `2.1` |
| Extent | Default `4096`, other positive extents possible | Requires exactly `4096` |
| Tile scheme | Outside payload semantics | Requires `XYZ` |
| Container | Outside payload semantics | Prefers/requires PMTiles for a `READY` public-carrier declaration |
| Feature ID | Optional | Requires declaration of stable feature IDs |
| Evidence reference | Not an MVT concept | Requires declaration that a `source_ref` attribute is present |
| Fields | Arbitrary encoded keys/values permitted by encoding | Requires encoded fields to close under an allowlist and denies declared sensitive fields |
| Tile budget | Not defined | Holds declarations above `65,536` bytes |
| Geometry loss/drift | Not defined | Requires zero declared drops and bounded declared area drift |
| Tiler reproducibility | Not defined | Requires a non-placeholder tiler-parameter digest |

The right-hand column describes a **current inactive KFM metadata profile**, not upstream MVT conformance and not active release policy.

[Back to top](#top)

---

## 3. KFM conformance posture

### 3.1 Current determination

**CONFIRMED:** KFM has executable, no-network MVT-related metadata checks.

**NOT ESTABLISHED:** KFM has not proven a complete active MVT conformance profile, production encoder, binary validator, released artifact family, or browser consumer at the inspected revision.

### 3.2 Current implementation ledger

| Slice | Current status | What a green result proves | What it does not prove |
|---|---|---|---|
| `LayerManifest` strict profile | `PROPOSED_INACTIVE` / `FIXTURE_ONLY` | Closed local shape, deterministic identity, selected semantic relationships and non-effects | MVT bytes, artifact resolution, policy, review, release, runtime load |
| `GeospatialCarrierReadinessCheck` MVT lane | `PROPOSED_INACTIVE`, metadata-only | Declared MVT carrier fields satisfy the current inactive profile | Declarations match bytes, source/evidence refs resolve, artifact is safe or released |
| PMTiles declared-manifest compatibility profile | Opt-in, non-canonical, synthetic-only | Bounded PMTiles v3/MVT structural declarations agree with generated synthetic archive metadata | Canonical TileArtifactManifest conformance, signatures, policy, release, public use |
| `map/tile_artifact_manifest` schema | Proposed open scaffold | JSON objects may pass an essentially unconstrained shape | Meaningful artifact conformance |
| `packages/maplibre` | Package scaffold | Repository contains an intended package boundary | Functional renderer adapter, dependency pin, consumer, MVT/MLT support, runtime health |

### 3.3 No production-default claim

The prior edition described MVT as KFM's practical or production default. Current repository evidence supports a narrower statement:

- the inactive readiness profile contains an MVT lane;
- the positive MVT fixture uses MVT `2.1` inside PMTiles;
- MapLibre's upstream vector source defaults to `mvt` when no encoding is declared;
- the KFM MapLibre package/runtime consumer is not established; and
- no accepted KFM-wide decision, production manifest inventory, or released artifact set was established in this review.

Therefore **MVT is a current KFM candidate and checked fixture surface, not a verified production-default implementation**.

### 3.4 Activation ladder

A future active KFM MVT profile should graduate through separate, reviewable stages:

1. accepted applicability and profile decision;
2. exact upstream version and compatibility policy;
3. semantic contract and canonical machine schema;
4. positive, negative, malformed, sensitive, correction, and rollback fixtures;
5. binary parser and deterministic encoder checks;
6. source-layer/style/manifest consumer parity;
7. evidence, policy, review, and release integration;
8. observed public-safe runtime consumption;
9. correction, withdrawal, cache invalidation, and rollback drill.

No single stage implies the next.

[Back to top](#top)

---

## 4. KFM-specific constraints on top of MVT

This section distinguishes current executable **inactive metadata checks** from future active-profile decisions.

### 4.1 Source-layer identity

**CONFIRMED current inactive check:** `source_layer`, `manifest_source_layer`, and every declared style source layer must agree.

**Upstream relationship:** MapLibre style layers that consume vector sources identify the encoded layer through `source-layer`. This is a consumer binding, not evidence or release authority.

**Future activation requirement:** Renaming a source layer must be treated as a versioned consumer-contract change with style, manifest, test, correction, and rollback impact.

### 4.2 Attribute closure and sensitive data

**CONFIRMED current inactive check:**

- declared encoded attributes must be a subset of the declared allowlist;
- declared sensitive attributes produce an `ERROR` outcome; and
- arrays must be sorted and unique.

> [!CAUTION]
> **Style filters are not redaction.** Once an attribute or precise geometry is encoded into publicly reachable tile bytes, a client may inspect it even when the current style does not display it. Sensitive fields and geometry must be transformed or excluded before public artifact generation.

A future active profile must bind field allowlists to accepted domain policy and transformation receipts rather than one global documentation table.

### 4.3 Feature identity

Upstream MVT IDs are optional. KFM needs an explicit consumer strategy before depending on stable feature state:

- encode deterministic feature IDs directly;
- use MapLibre `promoteId` to promote a stable property; or
- use a separately governed lookup key.

**CONFIRMED current inactive check:** the readiness declaration must state that stable feature IDs exist. It does not inspect the bytes or prove stability across builds.

### 4.4 Evidence lookup attributes

**CONFIRMED current inactive check:** the declaration states that a `source_ref` attribute exists.

**NEEDS VERIFICATION:** whether an active profile should require the literal field `source_ref`, a layer-declared evidence key, a compact stable feature key resolved server-side, or another privacy-preserving pattern.

A public tile must never embed a full `EvidenceBundle`, restricted citation excerpt, internal policy reason, or canonical-store locator merely to satisfy evidence lookup.

### 4.5 Extent and tile scheme

- `4096` is the MVT protobuf default and the current inactive KFM requirement.
- `XYZ` is the current inactive KFM requirement.
- Neither is a universal MVT conformance requirement.
- MapLibre supports a separate source `scheme` configuration, including `xyz` and `tms`.

An active KFM profile should either ratify these choices or define explicit exception and migration rules.

### 4.6 Geometry loss and drift

**CONFIRMED current inactive check:** declarations must report zero geometry drops and area drift no greater than the declared limit.

**NOT ESTABLISHED:** the current validator does not parse tile command streams, compare canonical geometry to encoded geometry, calculate drift, test ring winding, or detect clipping/simplification defects. A producer supplies the declaration.

A future binary/producer test should cover:

- invalid command streams and tag indexes;
- out-of-range layer/feature references;
- clipping and quantization behavior;
- exterior/interior ring validity after tile-coordinate transformation;
- deterministic feature counts and IDs;
- declared versus observed field sets;
- cross-zoom disappearance and duplication;
- expected versus observed geometry loss and metric drift.

### 4.7 Tile budgets

**CONFIRMED current inactive check:** `max_tile_bytes > 65,536` produces `HOLD`.

This value is a profile threshold, not an upstream MVT rule and not proven as a universal KFM production SLO. An active budget should be based on representative layers, devices, networks, interaction patterns, caches, and public consequence. It should distinguish hard safety limits, performance targets, and advisories.

The prior `p95 < 150 ms` claim is not retained as established KFM policy because no current accepted performance authority or observed runtime evidence was established here.

### 4.8 Deterministic build declaration

**CONFIRMED current inactive check:** a non-zero SHA-256 tiler-parameter digest is required.

A future active profile must bind that digest to the actual encoder implementation, version, flags/configuration, input digest, ordering, clipping/simplification rules, layer mapping, and output digest. A metadata value alone does not prove deterministic replay.

[Back to top](#top)

---

## 5. Pipeline & lifecycle placement

MVT is downstream of admitted source material and canonical/reviewed geometry. It must not become a shortcut around lifecycle, evidence, policy, review, or release.

```mermaid
flowchart LR
    SRC["Admitted source + SourceDescriptor"] --> CAN["Canonical / reviewed geometry and attributes"]
    CAN --> BUILD["Deterministic tile build candidate"]
    BUILD --> MVT["MVT payloads"]
    MVT --> SET["Tileset / PMTiles / delivery candidate"]
    SET --> META["Layer + artifact + readiness declarations"]
    META --> GOV["Evidence · policy · review · release · correction · rollback"]
    GOV --> PUB["Governed public-safe carrier"]

    META -. current inactive checks .-> CHECK["Fixture-only metadata validation"]
```

The diagram is a responsibility model, not a claim that every node is implemented.

| Lifecycle point | MVT role | Current evidence |
|---|---|---|
| `RAW` | No public tile authority; source-native bytes or references remain preserved | MVT page creates no intake behavior |
| `WORK` / `QUARANTINE` | Candidate mapping, field filtering, geometry transformation, and unresolved-risk handling | No MVT-specific producer flow established |
| `PROCESSED` | Canonical/reviewed source for deterministic tile generation | No active MVT generator established |
| `CATALOG` / `TRIPLET` | Candidate artifact and relation records may describe a tileset | Inactive readiness check requires a `stac_item_ref` but does not resolve it |
| `PUBLISHED` | Released public-safe carrier referenced by governed release records | No MVT release or publication established |

### 5.1 Lifecycle invariants

- MVT bytes must not be treated as the canonical geometry store.
- A public client must not derive authority from a reachable URL or successful decode.
- Source-native and canonical records must remain recoverable for correction and rebuild.
- Generalization/redaction must occur before public tile encoding, with a transform record where policy requires one.
- A changed encoder, profile, source-layer map, field allowlist, geometry rule, or tile matrix produces a new candidate identity and review event.
- Correction, supersession, withdrawal, and rollback must not rewrite historical released bytes silently.

### 5.2 Static and dynamic serving remain separate decisions

MVT may be delivered through pre-generated tiles, PMTiles, a database-backed tile service, or another governed mechanism. This page does not select one. Static versus dynamic delivery must be decided from source cadence, filtering/access needs, sensitivity mediation, deterministic replay, cache behavior, cost, and correction latency—not from an unsupported universal default.

[Back to top](#top)

---

## 6. Required object families & manifests

### 6.1 Current repository map

| Responsibility | Current path | Current status |
|---|---|---|
| Human-readable MVT guidance | `docs/standards/MVT.md` | This page; documentation authority only |
| Layer semantics | [`contracts/data/layer_manifest.md`](../../contracts/data/layer_manifest.md) | Dual profile; strict profile inactive and fixture-only |
| Layer machine shape | [`schemas/contracts/v1/data/layer_manifest.schema.json`](../../schemas/contracts/v1/data/layer_manifest.schema.json) | Closed strict candidate plus legacy compatibility branch |
| Layer validation | [`tools/validators/data/validate_layer_manifest.py`](../../tools/validators/data/validate_layer_manifest.py) | Deterministic local validation; no reference/artifact/runtime authority |
| Tile artifact semantics | [`contracts/release/tile_artifact_manifest.md`](../../contracts/release/tile_artifact_manifest.md) | Proposed contract; canonical schema family unresolved |
| Tile artifact machine shape | [`schemas/contracts/v1/map/tile_artifact_manifest.schema.json`](../../schemas/contracts/v1/map/tile_artifact_manifest.schema.json) | Open proposed scaffold; not meaningful conformance proof |
| Carrier-readiness semantics | [`contracts/release/geospatial_carrier_readiness.md`](../../contracts/release/geospatial_carrier_readiness.md) | `PROPOSED_INACTIVE`, metadata-only |
| Carrier-readiness machine shape | [`schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json`](../../schemas/contracts/v1/release/geospatial_carrier_readiness.schema.json) | Closed current schema including MVT declarations |
| Carrier-readiness validation | [`tools/validators/release/validate_geospatial_carrier_readiness.py`](../../tools/validators/release/validate_geospatial_carrier_readiness.py) | No-network `READY` / `HOLD` / `ERROR`; declared metadata only |
| Carrier-readiness fixtures/tests/CI | [`cases.json`](../../fixtures/contracts/v1/release/geospatial_carrier_readiness/cases.json), [`test`](../../tests/release/test_geospatial_carrier_readiness.py), [`workflow`](../../.github/workflows/geospatial-carrier-readiness.yml) | Bounded executable proof of fixture polarity |
| PMTiles/MVT compatibility | [`fixtures/pmtiles/attestation/`](../../fixtures/pmtiles/attestation/README.md), [`validator`](../../tools/validators/pmtiles/validate_attestation_bundle.py), [`tests`](../../tests/validators/test_pmtiles_attestation_bundle.py) | Non-canonical structural compatibility; synthetic temporary bytes |
| Browser adapter/package | [`packages/maplibre/README.md`](../../packages/maplibre/README.md) | Package scaffold; active adapter and consumer not established |

### 6.2 Authority separation

A future governed MVT release may reference several object families, but none may substitute for another:

| Object family | Responsibility |
|---|---|
| `SourceDescriptor` | Source identity, role, rights, cadence, and sensitivity posture |
| canonical domain record / dataset version | Source-preserving geometry and attributes before tiling |
| `LayerManifest` | Layer representation and runtime-facing candidate contract |
| `TileArtifactManifest` | Exact artifact identity, format/container, digest, coverage, and release-facing relations |
| readiness / validation report | Bounded result of declared-metadata and binary checks |
| `EvidenceRef` / `EvidenceBundle` | Support for map-visible claims |
| `PolicyDecision` | Finite admissibility decision and obligations |
| review record | Accountable human/steward review evidence |
| release manifest / promotion decision | Governed state transition and released contents |
| correction / withdrawal / rollback records | Public lineage, invalidation, and reversibility |
| representation/run receipts | Process and representation accountability, distinct from truth and release |

### 6.3 Current authority conflict

The repository currently has:

- a proposed semantic `TileArtifactManifest` contract under `contracts/release/`;
- an open scaffold schema under `schemas/contracts/v1/map/`; and
- an executable, closed `GeospatialCarrierReadinessCheck` under the release schema family.

This is **CONFLICTED / NEEDS VERIFICATION** for canonical tile-artifact schema ownership. This documentation update does not select a winner, create a parallel schema, or imply that the readiness declaration is the final artifact manifest.

[Back to top](#top)

---

## 7. Validation & CI gates

### 7.1 Current executable coverage

| Check | Current finite outcomes | What is evaluated | What remains outside |
|---|---|---|---|
| LayerManifest validator | `PASS`, `FAIL`, `ERROR` | Schema plus deterministic local semantic rules for legacy/strict candidate profiles | References, artifact bytes, policy, review, release, runtime |
| Geospatial carrier readiness | `READY`, `HOLD`, `ERROR` | Declared metadata for MVT/COG/GeoParquet | Binary bytes, source/evidence resolution, policy, signing, release, publication |
| PMTiles attestation compatibility | Structural pass/hold/error vocabulary defined by that validator | Synthetic PMTiles v3/MVT declarations and selected digest/header/vector-layer relationships | Canonical schema, production bytes, cryptographic authenticity, policy, release |

These result families are validator-specific. They must not be collapsed into the public `PolicyDecision` outcomes `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` without an accepted adapter contract.

### 7.2 Current MVT readiness rules

The inactive validator currently checks declarations for:

- MVT `2.x` version family;
- extent `4096`;
- `XYZ` scheme;
- PMTiles as the default public-container declaration;
- source-layer agreement among tile, manifest, and styles;
- stable feature IDs;
- a `source_ref` attribute declaration;
- field allowlist closure;
- no declared sensitive attributes;
- maximum tile size of `65,536` bytes;
- zero declared geometry drops;
- area drift within a declared limit;
- non-placeholder tiler-parameter digest; and
- range-read support for PMTiles.

A `READY` result means only that the declaration satisfies these inactive checks.

### 7.3 Missing binary and consumer proof

A future active MVT implementation should add evidence for:

1. protobuf parsing against MVT 2.1;
2. encoded layer version, name, extent, keys, values, tags, IDs, and geometry command validity;
3. observed versus declared source layers and field sets;
4. stable ID/replay behavior across equivalent builds;
5. geometry clipping, quantization, winding, loss, and drift against canonical inputs;
6. malformed/hostile payload complexity limits;
7. container/transport behavior, including correct media type, range handling where applicable, and immutable artifact binding;
8. MapLibre style/source compilation and source-layer parity;
9. positive and negative feature-click/evidence resolution through governed interfaces;
10. sensitive geometry and field non-leakage;
11. release-manifest admission, correction, withdrawal, cache invalidation, and rollback; and
12. exact-head CI plus observed consumer behavior.

### 7.4 Required fixture classes for an active profile

| Fixture class | Expected bounded behavior |
|---|---|
| Valid MVT 2.1 tile with one declared layer | Binary check passes for the named profile only |
| Multiple valid layers with independent extents | Parser preserves per-layer declarations |
| Invalid layer version or malformed protobuf | Error/fail with stable reason code |
| Invalid tag indexes or geometry command sequence | Fail closed without unbounded diagnostics |
| Source-layer mismatch with manifest/style | Hold or deny activation according to accepted policy |
| Encoded field outside allowlist | Fail/deny public candidate |
| Sensitive attribute or precise restricted geometry | Deny public candidate before runtime |
| Missing/unstable feature identity where interaction requires it | Hold runtime activation |
| Geometry drop or drift over accepted limit | Fail producer/readiness check |
| Corrected tileset with new digest and predecessor link | New immutable candidate; prior release preserved |
| Withdrawn artifact | No longer served; history and correction reason remain resolvable |
| MVT/MLT parity candidate | Shared facts, styles, feature IDs, and expected visuals remain within accepted tolerances |

### 7.5 What a green check cannot prove

A green MVT-related check cannot by itself establish:

- truth or completeness of the source data;
- legal sufficiency or redistribution rights;
- safe handling of precise locations or personal data;
- fitness for every map scale or analytical use;
- evidence closure;
- review approval;
- release approval;
- deployed interoperability;
- public availability; or
- successful correction and rollback.

[Back to top](#top)

---

## 8. Anti-patterns

| Anti-pattern | Why it fails | Corrective posture |
|---|---|---|
| **MVT bytes treated as evidence** | Encoding is a carrier, not source authority or claim support | Resolve evidence through governed objects and interfaces |
| **Successful decode treated as release** | Technical readability says nothing about policy/review/release state | Require distinct release and correction authorities |
| **`4096` or `XYZ` described as universal upstream law** | They are profile/reference choices, not exclusive MVT requirements | Label the owning profile and exception rules |
| **`2.x` used indefinitely without exact compatibility policy** | Minor-version assumptions can become invisible drift | Pin `2.1` or define an accepted compatibility range and tests |
| **PMTiles described as MVT** | PMTiles is a container; it may carry vector or raster tiles | Record container and inner encoding separately |
| **One tile described as a tileset** | Payload conformance does not prove coverage, completeness, or addressing | Validate the tileset/container and payloads at separate layers |
| **Style filters used as privacy** | Public bytes remain inspectable regardless of visual styling | Remove/generalize sensitive content before encoding |
| **Feature ID assumed stable because an ID exists** | Upstream ID is optional and local to a feature record; persistence is application policy | Define and test deterministic ID or `promoteId` strategy |
| **Metadata declaration treated as byte verification** | A producer may declare values that do not match encoded bytes | Add binary and producer replay tests |
| **Silent geometry loss accepted as optimization** | Missing or distorted features can alter public meaning | Record and gate loss/drift against accepted thresholds |
| **All domains share one field allowlist** | Sensitivity, rights, and explanatory needs vary by domain | Bind allowlists to accepted layer/domain policy |
| **Direct RAW-to-tile publication** | Bypasses lifecycle, evidence, transformation, review, and rollback | Build only from governed candidates and release through state transition |
| **MLT called unsupported or MVT called permanent by assumption** | Upstream capability and KFM adoption are different, evolving questions | Verify current runtime/tooling and use an explicit migration decision |
| **A documentation badge treated as conformance** | Presentation is not implementation evidence | Cite exact contracts, schemas, validators, fixtures, tests, releases, and consumers |

[Back to top](#top)

---

<a id="9-relationship-to-mlt-pilot-posture"></a>

## 9. Relationship to MLT and encoding migration

The legacy anchor retains “pilot posture” for inbound-link compatibility. The current determination is more precise.

### 9.1 Upstream state

MapLibre's current vector-source specification recognizes both `mvt` and `mlt` encodings, with `mvt` as the source-configuration default. The [MapLibre Tile specification](https://github.com/maplibre/maplibre-tile-spec) remains a separate, evolving upstream standard and implementation ecosystem.

Therefore the former statement that MLT cannot be used by current MapLibre clients is stale as an upstream generalization.

### 9.2 KFM state

**CONFIRMED:** the inspected KFM geospatial-carrier readiness profile has MVT, COG, and GeoParquet lanes; it does not include MLT.

**CONFIRMED:** the inspected MapLibre package is a scaffold without an established dependency/version or functional consumer.

**UNKNOWN / NOT ESTABLISHED:** KFM's active MLT support, production MVT dependency, browser compatibility, encoder availability, style parity, release integration, and rollback behavior.

The safe current statement is:

> MVT is the vector-tile encoding represented by KFM's current inactive readiness fixture. Upstream MapLibre also supports MLT, but KFM has not established an active MVT-to-MLT admission or migration policy.

### 9.3 Proposed migration decision gate

Before KFM activates MLT or changes an MVT release family, require:

- exact MapLibre runtime and package lock;
- accepted encoder/decoder versions and supply-chain review;
- explicit encoding field in source/layer/artifact contracts;
- shared source-layer and feature-identity rules;
- field, geometry, time, evidence, and policy parity;
- representative size/decode/render benchmarks;
- visual and interaction regression tests;
- catalog/media-type and container mapping;
- public-client fallback behavior;
- immutable predecessor/successor relation; and
- rollback to the prior released carrier without rewriting history.

A format benchmark is evidence for a decision. It is not the decision itself.

[Back to top](#top)

---

## 10. STAC / DCAT / PROV crosswalk for MVT artifacts

### 10.1 Current boundary

The current inactive `GeospatialCarrierReadinessCheck` requires a `stac_item_ref`. It does not resolve that reference, require a DCAT or PROV reference, or prove catalog closure.

The current synthetic STAC/DCAT/PROV closure surfaces elsewhere in the repository prove bounded profile agreement for their named fixtures. They do not automatically validate MVT payloads or make this MVT page an accepted catalog profile.

### 10.2 Conceptual mapping

Where an accepted KFM catalog/release profile requires these projections, shared released facts should map without collapsing responsibilities:

| Surface | MVT-related responsibility | Boundary |
|---|---|---|
| STAC Item/asset | Discover the tileset/archive by released identity, extent, time, media type, roles, checksum, and public locator | Does not prove payload semantics, policy, or release by itself |
| DCAT Dataset/Distribution | Describe dataset/distribution/service discovery and access conditions | Does not replace the exact artifact or release manifest |
| PROV entity/activity/agent | Record derivation from source/canonical artifacts through the tile build | Does not replace run receipts, evidence, policy, or review |
| LayerManifest | Bind a map layer candidate to source layer, artifact, fields, temporal/exposure/runtime posture | Fixture profile does not activate the layer |
| TileArtifactManifest | Bind exact tile artifact/container identity and digest to release-facing relations | Canonical schema ownership remains unresolved |
| Release/correction records | Authorize and later correct, supersede, withdraw, invalidate, or roll back the served carrier | Catalog discoverability never substitutes for this authority |

### 10.3 Mapping rules for a future active profile

A future mapping should:

1. distinguish the outer container media type from inner MVT encoding;
2. describe one released tileset/archive, not create one catalog record per individual tile unless a specific profile requires it;
3. bind checksum/digest, byte size, extent, time, zoom range, tile matrix, and source-layer inventory to the exact release;
4. preserve source, evidence, rights, sensitivity, policy, review, build, and correction references in their own authorities;
5. avoid public locators for unreleased/internal artifacts;
6. carry predecessor/successor and withdrawal state without mutating historical catalog bytes; and
7. prove shared identity, digest, extent, rights, release, and correction facts agree across admitted projections.

This page does not make STAC, DCAT, or PROV mandatory for every MVT use. Applicability belongs to accepted catalog and release decisions.

[Back to top](#top)

---

## 11. Open questions & NEEDS VERIFICATION

| ID | Question | Status | Closure evidence |
|---|---|---|---|
| MVT-01 | Has KFM adopted MVT as an active or default vector-tile encoding? | UNKNOWN | Accepted decision plus active contracts, schemas, producer, consumer, tests, and released inventory |
| MVT-02 | Should the active version pin be exactly `2.1`, or may a tested `2.x` compatibility range remain? | NEEDS VERIFICATION | Version policy and compatibility fixtures; reconcile validator with positive fixture |
| MVT-03 | Are extent `4096` and `XYZ` universal KFM requirements or profile defaults with exceptions? | NEEDS VERIFICATION | Accepted profile and exception/migration tests |
| MVT-04 | Which canonical object owns tile-artifact shape: map, release, layers, or another accepted family? | CONFLICTED | ADR/migration decision resolving contract/schema ownership |
| MVT-05 | What binary parser and validator prove MVT command, tag, layer, extent, and geometry correctness? | UNKNOWN | Pinned implementation, hostile/valid fixtures, deterministic tests, registry/CI admission |
| MVT-06 | Which encoder/generator is admitted, and how are parameters, inputs, and replay bound? | UNKNOWN | Dependency/supply-chain decision, run receipt, replay test, output digest |
| MVT-07 | What is the stable feature identity strategy for each interactive layer? | NEEDS VERIFICATION | Contract plus direct-ID/`promoteId` consumer tests |
| MVT-08 | Is the evidence lookup key literally `source_ref`, layer-declared, or server-resolved from another stable ID? | NEEDS VERIFICATION | Privacy-aware contract, fixture matrix, governed resolver test |
| MVT-09 | Which field and geometry transforms apply per domain and sensitivity tier? | NEEDS VERIFICATION | Policy, transform receipts, public-safe negative tests, steward review |
| MVT-10 | Which tile-size, feature-count, decode, render, and fetch budgets apply by device/tier? | UNKNOWN | Benchmarks, runtime probes, accepted release budgets, observed checks |
| MVT-11 | Which static/dynamic container and serving patterns are admitted? | NEEDS VERIFICATION | Source cadence/access analysis, correction latency, range/network tests, rollback plan |
| MVT-12 | What is KFM's MLT admission and MVT-to-MLT migration posture? | UNKNOWN | Runtime lock, parity/benchmark fixtures, accepted decision, fallback and rollback proof |
| MVT-13 | Which STAC/DCAT/PROV profile is required for each MVT artifact family? | NEEDS VERIFICATION | Accepted catalog applicability matrix and consumer tests |
| MVT-14 | Which package/runtime actually loads released vector tiles through the governed interface? | UNKNOWN | Current implementation, dependency, consumer inventory, tests, runtime evidence |
| MVT-15 | Who owns MVT profile stewardship and independent release review? | NEEDS VERIFICATION | Named accountable roles; do not invent people |

Open items belong in the appropriate decision, verification, or drift register. This page does not create an ADR or issue automatically.

[Back to top](#top)

---

## Appendix A — Glossary

| Term | Meaning in this page |
|---|---|
| **MVT** | Mapbox Vector Tile payload encoding governed by the upstream 2.1 specification. |
| **MLT** | MapLibre Tile encoding, separate from MVT and governed by its own upstream specification. |
| **Tile** | One encoded payload for a tile coordinate; not automatically a complete tileset or release. |
| **Tileset** | A collection/pyramid of tiles plus addressing and coverage metadata. |
| **PMTiles** | A single-file tile archive/container that may carry MVT or raster payloads. |
| **MBTiles** | A SQLite tile container; container semantics are separate from MVT payload conformance. |
| **Source layer** | Named MVT layer referenced by a vector-style layer through `source-layer`. |
| **Extent** | Integer coordinate grid for one encoded layer; upstream protobuf default is `4096`. |
| **Feature ID** | Optional unsigned integer feature identifier in MVT; persistence is an application/profile concern. |
| **`promoteId`** | MapLibre source configuration that promotes a feature property to the runtime feature ID. |
| **Readiness declaration** | KFM's current inactive metadata-only carrier preflight input. |
| **LayerManifest** | Candidate map-layer contract; current strict profile is inactive and fixture-only. |
| **TileArtifactManifest** | Proposed exact tile-artifact metadata contract; canonical schema family remains unresolved. |
| **EvidenceBundle** | Evidence support that outranks tile bytes and rendered language. |
| **PolicyDecision** | Finite policy result; distinct from validator readiness outcomes. |
| **Release manifest** | Governed record of released contents and rollback/correction relations. |

[Back to top](#top)

---

## Appendix B — Illustrative manifest fragment

> [!NOTE]
> The legacy appendix anchor is retained. The example below is an **illustrative fixture-only `GeospatialCarrierReadinessCheck`**, shaped after the current closed schema. It is not a canonical `TileArtifactManifest`, production record, release, or public-use authorization.

```json
{
  "object_type": "GeospatialCarrierReadinessCheck",
  "schema_version": "1.1.0",
  "profile": "kfm.geospatial-carrier-readiness.v1.1",
  "network_access": "forbidden",
  "carrier_kind": "MVT",
  "artifact": {
    "artifact_ref": "kfm:artifact:synthetic:mvt-roads",
    "digest": "sha256:2222222222222222222222222222222222222222222222222222222222222222",
    "media_type": "application/vnd.pmtiles",
    "file_name": "synthetic-roads.pmtiles",
    "immutable": true
  },
  "bindings": {
    "source_descriptor_ref": "kfm:source:synthetic:roads",
    "run_receipt_ref": "kfm:run:synthetic:mvt-roads",
    "stac_item_ref": "kfm:stac:synthetic:mvt-roads"
  },
  "carrier": {
    "mvt_version": "2.1",
    "extent": 4096,
    "tile_scheme": "XYZ",
    "container_kind": "PMTILES",
    "source_layer": "roads",
    "manifest_source_layer": "roads",
    "style_source_layers": ["roads"],
    "stable_feature_ids": true,
    "source_ref_attribute": true,
    "attribute_whitelist": ["class", "name", "source_ref"],
    "encoded_attributes": ["class", "name", "source_ref"],
    "sensitive_attributes": [],
    "max_tile_bytes": 64000,
    "geometry_drop_count": 0,
    "area_drift_pct": 0.1,
    "area_drift_limit_pct": 1.0,
    "tiler_parameters_hash": "sha256:2323232323232323232323232323232323232323232323232323232323232323",
    "range_read_supported": true
  },
  "governance": {
    "authority_created": false,
    "evidence_closure_claimed": false,
    "policy_evaluated": false,
    "promotion_authorized": false,
    "release_authorized": false,
    "publication_authorized": false,
    "public_use_allowed": false,
    "release_ref": null
  }
}
```

A `READY` result for this object proves declared-metadata readiness under the inactive profile only.

[Back to top](#top)

---

## Related docs

| Path | Relationship | Current bounded status |
|---|---|---|
| [`README.md`](./README.md) | Standards-lane boundary and state-separation rules | Repository-grounded lane authority |
| [`PMTILES.md`](./PMTILES.md) | Container/archive guidance and current partial structural compatibility | Draft; production profile remains proposed |
| [`OGC-API-TILES.md`](./OGC-API-TILES.md) | Tile-service interoperability guidance | Present; adoption and consumer behavior require separate evidence |
| [`directory-rules.md`](../doctrine/directory-rules.md) | Placement authority | Adopted through ADR-0029 |
| [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Directory Rules adoption | Accepted placement decision |
| [`LayerManifest`](../../contracts/data/layer_manifest.md) | Layer candidate semantics | Strict profile inactive and fixture-only |
| [`TileArtifactManifest`](../../contracts/release/tile_artifact_manifest.md) | Proposed exact tile-artifact semantics | Schema family unresolved |
| [`GeospatialCarrierReadinessCheck`](../../contracts/release/geospatial_carrier_readiness.md) | Current executable MVT declared-metadata preflight | Inactive; no authority or binary proof |
| [`PMTiles compatibility fixtures`](../../fixtures/pmtiles/attestation/README.md) | Synthetic PMTiles v3/MVT structural checks | Non-canonical compatibility evidence |
| [`MapLibre package boundary`](../../packages/maplibre/README.md) | Intended browser renderer-adapter package | Scaffold; functioning adapter/consumer not established |

### Rollback

Restore prior blob `f4ebfd0b8ec3b6344d69b430c015108ff9b3ec00` through normal reviewed history. No contract, schema, policy, fixture, validator, workflow, package, source, tile artifact, release, runtime, deployment, or public-product migration is required.

[Back to top](#top)
