<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/ogc-api-tiles
title: OGC API — Tiles — KFM Standards Boundary and Graduation Plan
type: standard; external-api-reference; tiled-geospatial-interoperability-boundary
version: v2.0-draft
status: "draft; repository-grounded; upstream-currentness-refreshed; no-KFM-profile-adoption; no-conformance-proof; no-release; no-publication"
owners:
  - "@bartytime4life — verified GitHub review route through CODEOWNERS"
  - "NEEDS VERIFICATION — map/runtime, governed API, layer, source, security, policy, validation, release, and interoperability stewards"
created: 2026-05-14
updated: 2026-08-18
policy_label: repository-facing; standards-guidance; tiles; network-boundary; rights-and-sensitivity-aware
owning_root: docs/
current_path: docs/standards/OGC-API-TILES.md
responsibility: >
  Explain the published OGC API — Tiles Part 1 and Tile Matrix Set 2.0 baseline,
  disclose KFM's current repository boundary, define a non-authoritative candidate
  integration profile, and state the evidence required before KFM may claim
  conformance, operate an endpoint, admit an external service, or release tiles.
truth_posture: >
  CONFIRMED current path, standards-lane placement, review route, published OGC
  API — Tiles Part 1 version 1.0 and TMS 2.0 identities, current strict
  LayerManifest protocol enumeration, current governed-api scaffold routes, and
  proposal status of the MapLibre seam decisions / PROPOSED KFM profile,
  protocol identifier, semantic and machine-shape changes, source-admission
  record, validators, producers, consumers, endpoint, and graduation sequence /
  UNKNOWN adopted KFM OGC API — Tiles profile, executable client or server,
  released tileset, production interoperability, external certification, and
  accountable specialist stewardship.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 6e45646702022513fa0777b294d09ea90d73cf58
  target_prior_blob: a9337842473846d05d14dbbc1a52cbca7199ea63
  standards_readme_blob: a8cbe5d183448d5f0de37f8a4eacd6fcaca0d71b
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  lifecycle_law_blob: 4eb1f0a38a31130bb9928867450709724bd4cacb
  trust_membrane_doctrine_blob: ded8c3b9b273b3fba41f800f54bcc75c2a35ca6f
  trust_membrane_architecture_blob: e260a1dbe20ec011901fbe8fb752cd3bb66a9eeb
  governed_api_architecture_blob: 06c5fd269fb8a326269f7f8ba98c6b8a75e0fd1a
  layer_manifest_contract_blob: 234dca70e768ee744f7d78109afc6e0dc745af1b
  layer_manifest_schema_blob: abca306cb271ed75127a83dd05b73830ba20773b
  layer_contract_lane_blob: b340d48ba17b7d303b0863f1574bbacbad2c17ea
external_currentness_review:
  access_date: 2026-08-18
  issuer_scope: "Official Open Geospatial Consortium standard pages, published specifications, schemas, and working repositories"
  tiles_standard: "OGC API — Tiles — Part 1: Core, version 1.0, OGC 20-057, International Standard"
  tile_matrix_standard: "OGC Two Dimensional Tile Matrix Set and Tile Set Metadata, version 2.0, OGC 17-083r4, International Standard"
  published_parts: "The official OGC standards page lists Part 1: Core version 1.0; working-repository extensions are not treated as published KFM baselines"
related:
  - ./README.md
  - ./WMTS.md
  - ./MVT.md
  - ./PMTILES.md
  - ./STAC.md
  - ./MAP_TRUST_STATES.md
  - ../doctrine/directory-rules.md
  - ../doctrine/lifecycle-law.md
  - ../doctrine/trust-membrane.md
  - ../architecture/TRUST_MEMBRANE.md
  - ../architecture/governed-api.md
  - ../architecture/map-shell.md
  - ../architecture/contract-schema-policy-split.md
  - "../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md"
  - "../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md"
  - ../../contracts/data/layer_manifest.md
  - ../../contracts/layers/README.md
  - ../../schemas/contracts/v1/data/layer_manifest.schema.json
tags: [kfm, standards, ogc-api, tiles, tms, tile-matrix-set, map, vector, coverage, interoperability, trust-membrane]
notes:
  - "Same-path documentation modernization only; no contract, schema, policy, source, fixture, validator, workflow, runtime, lifecycle object, release, deployment, or public artifact changes."
  - "The current strict LayerManifest protocol enumeration does not include OGC API — Tiles; this document does not add or imply that capability."
  - "The current governed-api scaffold exposes only /bootstrap, /layers, and /evidence as fail-closed ABSTAIN routes; this document does not create a tile endpoint."
  - "Common OGC resource paths are documented as examples or class-specific requirements, not as one universal hard-coded route layout."
  - "All prior major-section anchors are retained for inbound-link compatibility."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="ogc-api--tiles-kfm-standards-reference"></a>

# OGC API — Tiles — KFM Standards Boundary and Graduation Plan

> **Purpose.** Explain the published OGC API — Tiles and Tile Matrix Set baseline, show where current KFM repository evidence stops, and define the gates that must close before KFM claims conformance, admits an external tiles service, operates a tiles endpoint, or releases a tiled product.

![status](https://img.shields.io/badge/status-v2.0--draft-yellow)
![evidence](https://img.shields.io/badge/evidence-repository--grounded-success)
![upstream](https://img.shields.io/badge/OGC%20API%20Tiles-Part%201%20v1.0-blue)
![TMS](https://img.shields.io/badge/TMS-v2.0-blueviolet)
![adoption](https://img.shields.io/badge/KFM%20profile-NOT%20ESTABLISHED-orange)
![runtime](https://img.shields.io/badge/runtime-NOT%20IMPLEMENTED-critical)
![publication](https://img.shields.io/badge/publication-none-critical)

> [!IMPORTANT]
> **A standards page is not conformance proof.** This document does not adopt OGC API — Tiles for KFM, add a protocol value to `LayerManifest`, define a machine schema, admit a source, create a route, certify a client or server, approve a release, or prove interoperability.

> [!CAUTION]
> **Current KFM machine shape does not admit this protocol.** The strict fixture-only `LayerManifest` profile currently enumerates `PMTILES`, `XYZ`, `COG`, and `GEOJSON_FIXTURE`; it does not enumerate an OGC API — Tiles protocol. Adding one would require coordinated contract, schema, fixture, validator, policy, producer, consumer, and migration work.

> [!WARNING]
> **Current KFM runtime evidence does not establish a tiles API.** The governed-api scaffold has three fail-closed GET routes—`/bootstrap`, `/layers`, and `/evidence`—that return `ABSTAIN / NOT_IMPLEMENTED`. No OGC API — Tiles route, resolver, client adapter, server implementation, deployed service, or released tileset is established by the evidence reviewed here.

| Field | Current bounded result |
|---|---|
| **Directory result** | `PLACE` at the existing `docs/standards/OGC-API-TILES.md` path; human-readable external-standard guidance belongs in the standards lane |
| **Published upstream baseline** | OGC API — Tiles — Part 1: Core, version **1.0**, OGC document **20-057**, International Standard |
| **Tiling model baseline** | OGC Two Dimensional Tile Matrix Set and Tile Set Metadata, version **2.0**, OGC document **17-083r4**, International Standard |
| **Published-part boundary** | The official OGC standards page lists Part 1: Core 1.0; working-repository extensions are not treated here as published requirements |
| **KFM profile/adoption state** | **NOT ESTABLISHED** |
| **Current semantic/machine support** | Current `LayerManifest` has a proposed-inactive fixture profile, but its strict protocol enum does not include OGC API — Tiles |
| **Current API support** | No tiles route; current governed-api routes remain fail-closed scaffolds |
| **Current map-runtime decision state** | Relevant MapLibre seam and sole-renderer ADRs remain effectively **PROPOSED**, with runtime readiness held |
| **Release/publication effect** | None |

**Quick navigation:** [Scope](#1-purpose-and-scope) · [Why track it](#2-why-kfm-tracks-this-standard) · [Published model](#3-the-standard-in-brief) · [Conformance](#4-conformance-classes) · [Resources](#5-resources-and-url-templates) · [TMS](#6-tilematrixset-20-reference) · [Current KFM state](#7-kfm-positioning-and-trust-posture) · [Integration](#8-kfm-integration-model) · [Candidate profile](#9-required-kfm-objects-and-contracts) · [Validation](#10-validation-expectations) · [Security and anti-patterns](#11-anti-patterns) · [Open questions](#12-open-questions-and-needs-verification) · [Sources](#13-references) · [Related](#14-related-docs)

---

<a id="1-purpose-and-scope"></a>

## 1. Purpose, authority, and scope

### 1.1 What this page owns

This page owns human-readable guidance for:

- the identity and current published status of OGC API — Tiles Part 1 and TMS 2.0;
- the standard's modular resource, link, URI-template, conformance, encoding, and tile-matrix concepts;
- the difference between upstream conformance and KFM adoption;
- the current repository gap between documentation and executable support;
- a bounded candidate KFM profile for future review;
- validation, security, rights, sensitivity, correction, and rollback expectations; and
- graduation evidence required before stronger claims are made.

### 1.2 What this page does not own

| Question | Owning authority |
|---|---|
| Where this guidance belongs | Adopted Directory Rules, accepted ADRs, and [`docs/standards/README.md`](./README.md) |
| What a KFM source, layer, tileset, release, or runtime envelope means | `contracts/` |
| What machine shape or protocol enumeration is valid | `schemas/` and accepted schema-home decisions |
| What is allowed, denied, held, generalized, cached, proxied, or exposed | `policy/`, source terms, security controls, and governed review |
| Whether an external endpoint may be used | Source admission, rights review, `SourceDescriptor`, and source registry |
| Whether a KFM endpoint or client conforms | Exact-revision code, fixtures, validators, tests, generated reports, and observed interoperability |
| Whether evidence supports a tile-carried claim | `EvidenceRef` resolution to `EvidenceBundle` |
| Whether an artifact may release or publish | Review, proof, release, correction, withdrawal, and rollback authorities |
| What OGC API — Tiles normatively requires | OGC 20-057 and its normative dependencies |

### 1.3 Non-effects

This revision does **not**:

- accept OGC API — Tiles as a KFM application profile;
- create a KFM protocol identifier, conformance URI, route family, source adapter, server, proxy, cache, or catalog record;
- modify `LayerManifest`, `SourceDescriptor`, `RuntimeResponseEnvelope`, or another contract;
- modify a JSON Schema, policy bundle, fixture, validator, test, workflow, package, or application;
- choose a server framework, renderer version, cache topology, authorization model, or deployment;
- activate, crawl, proxy, cache, or expose an external endpoint;
- claim that advertised conformance has been independently tested;
- authorize direct browser access to an arbitrary external tile service;
- approve a release, deployment, publication, correction, or rollback; or
- supersede WMTS, PMTiles, MVT, COG, GeoParquet, STAC, DCAT, PROV, or a domain-specific contract.

### 1.4 KFM operating boundary

OGC API — Tiles is an interoperability and delivery standard. It does not replace KFM's trust membrane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A protocol-valid tile can still be unsupported by evidence, rights-restricted, sensitive, stale, unreleased, corrected, withdrawn, unsafe for a particular audience, or inconsistent with the requested time and geography. Conversely, a released KFM tile carrier can be valid for KFM without KFM claiming OGC API — Tiles conformance.

[Back to top](#top)

---

<a id="2-why-kfm-tracks-this-standard"></a>

## 2. Why KFM tracks this standard

OGC API — Tiles matters to KFM because it provides a standards-based way to discover and retrieve tiled geospatial information while remaining composable with other OGC API building blocks.

| KFM concern | Relevance | Current KFM status |
|---|---|---|
| External-service discovery | A source may advertise tilesets, tile-set metadata, formats, and tile templates through OGC links and conformance declarations | Candidate source-admission use only; no adapter established |
| Dynamic or server-mediated delivery | A reviewed KFM service could eventually expose released map, vector, or coverage tiles through this interface | No route or server implementation established |
| Client interoperability | A reviewed client could consume conforming released services without hard-coding one vendor API | No KFM OGC API — Tiles client established |
| Tile-matrix precision | TMS 2.0 gives a shared model for CRS, matrices, rows, columns, limits, and metadata | Candidate mapping; no protocol binding in current strict `LayerManifest` |
| Catalog and release closure | Tileset links may be projected from released catalog and layer records | No adopted projection or profile established |
| Trust-visible UI | A tile layer can carry attribution, freshness, sensitivity, release, correction, and evidence references at point of use | Doctrine applies; runtime implementation remains held |
| Cross-format delivery | The standard can carry map, vector, coverage, or other tiled information using advertised encodings | Media types and data type must remain explicit; no blanket support claim |

The standard is **not** a replacement for KFM evidence, policy, source admission, layer semantics, release manifests, or rollback. It is also not automatically preferable to static carriers such as PMTiles or to external WMTS services. The appropriate carrier depends on source role, audience, update behavior, policy, performance, hosting, and release evidence.

[Back to top](#top)

---

<a id="3-the-standard-in-brief"></a>

## 3. Published upstream baseline and conceptual model

### 3.1 Standard identity

| Surface | Published identity | Bounded use here |
|---|---|---|
| OGC API — Tiles | Part 1: Core, version 1.0, OGC 20-057 | Published normative baseline |
| OGC Two Dimensional Tile Matrix Set and Tile Set Metadata | Version 2.0, OGC 17-083r4 | Normative tiling and tileset-metadata model used by Part 1 |
| OGC Tile Matrix Set Register | OGC Naming Authority register | Preferred source of reusable TMS identifiers where appropriate |
| OGC API working repository | Public SWG working source | Forward-looking context only; not a substitute for the published standard |

The published standard supports tiled vector features, coverages, maps or imagery, and other forms of geospatial information. It is a successor or alternative to WMTS, but the two can interoperate when they use the same TMS definition.

### 3.2 Core resource concepts

| Concept | Meaning |
|---|---|
| **Geospatial data resource** | The underlying dataset, collection, map, coverage, or other resource represented as tiles |
| **Tileset** | Tiles representing one data resource or composition under one tile matrix set and declared metadata |
| **Tilesets list** | A discoverable collection of available tilesets |
| **Tileset metadata** | Data type, CRS, bounding information, links, TMS identity or definition, limits, and layer metadata as applicable |
| **Tile matrix set** | An ordered set of tile matrices covering a domain at defined scales in a CRS |
| **Tile matrix** | One grid level in the set; its identifier is not required to be a numeric zoom |
| **Tile** | The spatial fragment addressed by tile-matrix, row, and column coordinates |
| **URI template** | A discoverable template whose variables are bound to tile-matrix, row, and column semantics |
| **Conformance declaration** | The set of conformance-class URIs the implementation advertises |
| **Link relation** | The typed relationship used to navigate among landing, data, tileset-list, tileset, TMS, style, and tile resources |

### 3.3 What the standard does not decide for KFM

OGC API — Tiles does not decide:

- source authority, rights, attribution sufficiency, or redistribution permission;
- KFM evidence closure or whether a tile supports a consequential claim;
- sensitivity transforms, field allowlists, geometry generalization, or audience;
- release, correction, withdrawal, or rollback state;
- KFM identity, digest, receipt, proof, or catalog authority;
- authentication, authorization, rate limits, quotas, egress policy, or audit retention;
- cache ownership, service-level objectives, or operational incident response;
- which tile encoding KFM must support;
- which TMS KFM must use globally; or
- whether a KFM client fetches a released endpoint directly, through a gateway, or from a cached artifact.

[Back to top](#top)

---

<a id="4-conformance-classes"></a>

## 4. Conformance classes and claim discipline

OGC API — Tiles is modular. A server advertises supported conformance-class URIs; a conformance claim must be bounded to the relevant classes and tested against the applicable normative tests.

### 4.1 Published Part 1 conformance classes

| Class | Conformance URI | What it covers |
|---|---|---|
| Core | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/core` | Retrieval of individual tiles through a discoverable URI template bound to tile-matrix, row, and column |
| TileSet | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/tileset` | Metadata for one tileset and a mechanism to obtain tile links/templates |
| Tilesets list | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/tilesets-list` | A list of available tilesets |
| Dataset tilesets | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/dataset-tilesets` | Association of tilesets with an API-level dataset |
| Geodata tilesets | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/geodata-tilesets` | Association of tilesets with a specific geospatial data resource |
| Collections selection | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/collections-selection` | Selection of collections for dynamically generated tilesets |
| DateTime | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/datetime` | Generic time-dimension selection |
| OpenAPI 3.0 | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/oas30` | Additional OpenAPI 3.0 definition requirements |
| XML | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/xml` | XML tileset-list and tileset-metadata representations |
| PNG | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/png` | PNG tile encoding |
| JPEG | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/jpeg` | JPEG tile encoding |
| TIFF | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/tiff` | TIFF / GeoTIFF-oriented tile encoding requirements |
| netCDF | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/netcdf` | netCDF tile encoding |
| GeoJSON | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/geojson` | GeoJSON tile encoding |
| Mapbox Vector Tiles | `http://www.opengis.net/spec/ogcapi-tiles-1/1.0/conf/mvt` | MVT encoding |

No tile encoding class is universally mandatory. An implementation may support other encodings, but it must still describe and negotiate them accurately.

### 4.2 Four independent KFM states

Do not collapse these:

| State | Evidence |
|---|---|
| **Advertised** | The service lists a conformance URI |
| **Observed** | A controlled probe retrieved and checked the relevant resources |
| **Validated** | Applicable normative and KFM negative tests passed at a pinned version |
| **Adopted/released** | KFM review, policy, release, correction, and rollback records authorize a bounded use |

An advertised `conformsTo` entry is source evidence about a claim made by the service. It is not independent proof, KFM adoption, security review, rights clearance, or release approval.

### 4.3 KFM claim wording

Until stronger evidence exists, use wording such as:

- “the service advertises the Core and TileSet conformance URIs”;
- “the controlled profile probe passed the named KFM checks”;
- “the KFM client supports the following bounded classes and encodings at revision X”; or
- “the released endpoint is profiled for these classes.”

Do not write “KFM is OGC API — Tiles compliant” without a named implementation, exact version, class set, test evidence, producer/consumer scope, and release record.

[Back to top](#top)

---

<a id="5-resources-and-url-templates"></a>

## 5. Resources, links, and URI templates

### 5.1 Link-driven discovery

A robust client follows typed links and advertised templates. It must not infer the whole service from one guessed route.

Typical discovery flow:

```text
landing or known data resource
  -> conformance declaration
  -> tilesets-list link
  -> selected tileset metadata
  -> TileMatrixSet URI or embedded definition
  -> tile URI template
  -> bounded tile requests
```

### 5.2 Common paths are not one universal route contract

The published model commonly uses resources resembling:

| Resource | Common example |
|---|---|
| Dataset tilesets list | `/tiles` |
| Collection tilesets list | `/collections/{collectionId}/tiles` |
| Tileset metadata | `/tiles/{tileMatrixSetId}` |
| Tile | `/tiles/{tileMatrixSetId}/{tileMatrix}/{tileRow}/{tileCol}` |
| Dataset map tilesets | `/map/tiles` |
| Collection map tilesets | `/collections/{collectionId}/map/tiles` |

These examples are useful, but the Core class does not prescribe one fixed path or variable naming scheme. A conforming client must use the API definition, links, and templates supplied by the implementation. Some higher-level classes prescribe path suffixes for their specific resources; that does not justify hard-coding every deployment from one table.

### 5.3 Template rules a KFM implementation must preserve

A candidate client or source-admission validator should verify that:

- the template is obtained through an allowed discovery mechanism;
- template variables map unambiguously to tile matrix, row, and column;
- all required variables are present for the advertised matrix range;
- no unrecognized variable is silently substituted;
- the scheme is HTTPS unless an explicitly reviewed exception applies;
- the template host and redirect targets satisfy egress policy;
- matrix, row, and column values are validated against the selected TMS and limits before request construction;
- query parameters cannot inject a new host, path, header, or credential;
- media types are negotiated and checked against the response;
- links are resolved according to their base URI and relation, not string-concatenated blindly; and
- cached representations retain the effective URL, headers relevant to identity, response digest, and retrieval time.

### 5.4 Representation and content negotiation

The same logical tileset may offer multiple representations. KFM must keep these separate:

- tileset metadata representation;
- tile encoding and media type;
- data type carried by the tiles;
- style or portrayal relationship;
- language and profile parameters where applicable;
- compression or transfer encoding;
- cached versus live retrieval; and
- public-safe versus restricted variants.

A successful `200` response with bytes is not enough. Content type, declared encoding, tile structure, bounds, limits, and policy posture must agree.

[Back to top](#top)

---

<a id="6-tilematrixset-20-reference"></a>

## 6. Tile Matrix Set 2.0 boundary

TMS 2.0 provides the tiling model used by OGC API — Tiles. It defines regular grids at a bounded sequence of scales in a CRS and a service-independent tileset-metadata model.

### 6.1 Facts that must remain explicit

| Concern | Required KFM posture |
|---|---|
| TMS identity | Record the authoritative URI when available; do not rely only on a short label |
| Custom TMS | Resolve and preserve the complete definition; bind it by digest for deterministic replay |
| CRS | Record the CRS reference and axis semantics used by the TMS |
| Tile matrices | Preserve matrix identifiers; do not assume they are consecutive integer zooms |
| Origin/corner | Respect the declared corner of origin and coordinate direction |
| Matrix width/height | Validate row and column bounds for each matrix |
| Tile width/height | Validate pixel dimensions and reject unreasonable values |
| Scale/cell size | Preserve declared scale denominator and cell size where used |
| Variable-width matrices | Support only when the client and validator explicitly implement them; otherwise abstain |
| TileMatrixSet limits | Respect per-tileset limits rather than requesting the full theoretical grid |
| Bounding information | Keep tileset bounds distinct from data-resource bounds and from one tile's bounds |
| Registered definitions | Prefer stable registered definitions when fit for purpose; no specific TMS is mandated by Part 1 |

### 6.2 WebMercatorQuad is not a universal KFM default by documentation fiat

`WebMercatorQuad` is widely interoperable and may be a sensible profile choice for some public map products. This page does not adopt it as KFM's universal TMS. A profile decision must consider:

- the source CRS and transformation error;
- geometry and measurement fidelity;
- polar or geographic-CRS behavior;
- target client support;
- scale and resolution requirements;
- domain-specific accuracy;
- public-safety transforms;
- tile build reproducibility; and
- rollback compatibility.

### 6.3 Candidate identity binding

A future KFM tileset profile should bind at least:

```text
published OGC API — Tiles version
+ declared conformance-class set
+ tileset self identity
+ data-resource identity
+ TileMatrixSet URI or canonical definition digest
+ TileMatrixSet limits
+ tile media type and data type
+ source/release identity
+ policy and audience
```

The exact field names and hash projection belong in contracts and schemas, not in this standards page.

[Back to top](#top)

---

<a id="7-kfm-positioning-and-trust-posture"></a>

## 7. Current KFM repository state

The observations in this section are pinned to `main@6e45646702022513fa0777b294d09ea90d73cf58`. They establish repository bytes, not deployed behavior.

### 7.1 Confirmed surfaces

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Standards lane | [`docs/standards/README.md`](./README.md) lists this file and defines the lane as human-readable guidance only | Same-path modernization is correctly placed |
| `LayerManifest` semantic contract | [`contracts/data/layer_manifest.md`](../../contracts/data/layer_manifest.md) has a strict, proposed-inactive, fixture-only candidate profile plus a permissive legacy profile | A bounded layer carrier exists; it is not a release or runtime implementation |
| `LayerManifest` schema | [`schemas/contracts/v1/data/layer_manifest.schema.json`](../../schemas/contracts/v1/data/layer_manifest.schema.json) enumerates `PMTILES`, `XYZ`, `COG`, and `GEOJSON_FIXTURE` | OGC API — Tiles is not admitted by the strict protocol enum |
| Layer contract lane | [`contracts/layers/README.md`](../../contracts/layers/README.md) marks `TileArtifactManifest` and `StyleManifest` as proposed and preserves a layer/data placement conflict | This page must not present those objects as implemented authority |
| Governed API | [`docs/architecture/governed-api.md`](../architecture/governed-api.md) records `/bootstrap`, `/layers`, and `/evidence` scaffold routes returning `ABSTAIN / NOT_IMPLEMENTED` | No tiles API or evidence-backed answer path is established |
| Trust membrane | [`docs/architecture/TRUST_MEMBRANE.md`](../architecture/TRUST_MEMBRANE.md) records a bounded fail-closed scaffold and unresolved operational seams | Architecture exists in parts; complete enforcement is unproven |
| MapLibre seam decisions | ADR-0006 and ADR-0007 exist but remain effectively proposed; current package/adapter evidence is scaffold-level and readiness is held | Do not make renderer or adapter implementation claims from this page |

### 7.2 Bounded repository search result

At the reviewed revision:

- the exact indexed token `ogcapi-tiles` was found only in this standards page;
- the exact property token `tileMatrixSetURI` was found only in this standards page; and
- broader “OGC API Tiles” references occur in related documentation such as WMTS, map architecture, and domain/API guidance.

This is a bounded code-search result, not an exhaustive proof of absence. Generated files, unindexed content, alternate names, external systems, branches, and runtime behavior were not established.

### 7.3 Current state summary

| Capability | Status |
|---|---|
| Human-readable standard reference | **CONFIRMED**, being modernized here |
| Adopted KFM application profile | **UNKNOWN / NOT ESTABLISHED** |
| Contract semantics for OGC API — Tiles | **PROPOSED** |
| Strict schema protocol value | **ABSENT from current enum** |
| Positive/negative protocol fixtures | **NOT ESTABLISHED** |
| Executable conformance validator | **NOT ESTABLISHED** |
| Source-admission adapter | **NOT ESTABLISHED** |
| Governed API server route | **NOT ESTABLISHED** |
| Map client adapter | **NOT ESTABLISHED** |
| Released tileset or endpoint | **NOT ESTABLISHED** |
| External interoperability observation | **NOT ESTABLISHED** |
| Production deployment and operations | **UNKNOWN** |

[Back to top](#top)

---

<a id="8-kfm-integration-model"></a>

## 8. Candidate KFM integration model

The following model is **PROPOSED**. It is a graduation path, not current architecture proof.

### 8.1 Two distinct roles

#### Role A — admit an external OGC API — Tiles service

```text
external service
  -> source discovery and immutable metadata snapshot
  -> rights / terms / attribution / security review
  -> conformance and TMS profile validation
  -> WORK or QUARANTINE
  -> approved SourceDescriptor and candidate LayerManifest
  -> evidence / policy / review / release closure
  -> released, manifest-bound client or gateway access
  -> correction / withdrawal / rollback
```

#### Role B — expose a KFM OGC API — Tiles service

```text
released KFM dataset or layer
  -> accepted semantic and machine profile
  -> deterministic tileset and TMS metadata projection
  -> route and content negotiation implementation
  -> conformance and negative tests
  -> security / authorization / cache / operations review
  -> release manifest and rollback target
  -> governed endpoint
```

The two roles must not share an ambiguous authority record. An external source-admission record and a KFM outbound release record have different owners, risks, and correction paths.

### 8.2 Public-client boundary

A KFM public client may use only:

- a released KFM endpoint;
- a released immutable artifact;
- or an external endpoint whose exact use is admitted, policy-approved, review-complete, and bound by a released layer/source manifest.

Whether bytes are same-origin, proxied, cached, or fetched directly is a deployment decision. This page does not force a universal proxy and does not permit arbitrary endpoint access. In every case the client must avoid canonical/internal stores, unreleased candidates, unreviewed URLs, and hidden policy decisions.

### 8.3 No authority collapse

| Do not collapse | Into |
|---|---|
| `SourceDescriptor` | `LayerManifest` |
| Advertised conformance | Validated conformance |
| Tileset metadata | Source truth |
| Tile bytes | `EvidenceBundle` |
| Tile matrix identifier | Complete TMS definition |
| Client rendering success | Rights, security, or release approval |
| Cache entry | Immutable release artifact |
| `LayerManifest` | `ReleaseManifest` |
| Documentation profile | Contract or schema |
| Pull request or validator pass | Publication |

[Back to top](#top)

---

<a id="9-required-kfm-objects-and-contracts"></a>

## 9. Candidate KFM profile and required authority changes

Everything in this section is **PROPOSED** and intentionally avoids declaring field-level wire authority.

### 9.1 Candidate profile record

A future reviewed profile should state:

| Dimension | Candidate content |
|---|---|
| Profile identity | Stable KFM profile ID, version, status, digest, and supersession |
| Upstream baseline | OGC 20-057 version 1.0 and OGC 17-083r4 version 2.0 |
| Required classes | Exact minimum conformance-class set by KFM use case |
| Optional classes | Classes supported but not required |
| Encodings | Allowed media types, data types, compression, and profile parameters |
| Discovery | Allowed landing/data-resource entry points and required link relations |
| Tileset metadata | Required JSON/XML representations and validation level |
| TMS policy | Registered/custom rules, URI/definition digest, limits, variable-width support |
| Time | Required DateTime semantics, valid-time/source-time separation, stale behavior |
| Identity | Source, data resource, tileset, release, and artifact identities kept distinct |
| Rights and attribution | Terms snapshot, attribution text, redistribution/cache posture |
| Sensitivity | Audience, field allowlist, geometry transform, tile-build redaction proof |
| Security | Scheme/host/redirect policy, authentication, egress, size and rate limits |
| Operations | Cache, retry, timeout, circuit breaker, health, audit, incident, withdrawal |
| Evidence and release | Evidence, policy, review, release, correction, and rollback references |
| Validation | Offline fixtures, normative-class tests, KFM negative tests, producer/consumer proof |

### 9.2 Candidate source-admission snapshot

For an external service, preserve at least:

- requested and effective discovery URLs;
- retrieval time, status, selected headers, and content digest;
- redirect chain after policy checks;
- advertised `conformsTo` array;
- selected tilesets-list and tileset links;
- tileset self identity;
- data-resource identity and declared data type;
- tile template and variable bindings;
- advertised media types;
- TMS URI or complete definition and digest;
- tile-matrix limits;
- bounding and temporal metadata;
- authentication class without secret values;
- terms, rights, attribution, cache, and freshness posture;
- probe/validator version and outcome;
- unresolved conflicts, warnings, and abstentions; and
- correction or source-drift lineage.

This is a candidate evidence record, not a schema defined by this page.

### 9.3 Dependency-closed changes required for adoption

An implementation slice that introduces OGC API — Tiles must close all directly affected surfaces:

| Responsibility | Required change |
|---|---|
| Semantic meaning | Accepted contract additions or a dedicated profile contract |
| Machine shape | Schema changes, including an explicit protocol/profile representation |
| Source admission | SourceDescriptor semantics and safe snapshot/reference handling |
| Policy | Egress, rights, attribution, sensitivity, audience, caching, and release rules |
| Fixtures | Synthetic no-network positive and negative service snapshots |
| Validation | Deterministic profile, link, TMS, encoding, and security checks |
| Runtime | Server or client implementation behind the accepted boundary |
| Catalog/layer | Profile and release references without authority collapse |
| Tests | Unit, contract, negative, integration, and interoperability tests |
| Workflows | Read-only CI invocation with stable finite outcomes |
| Release | Manifest, proof, correction, withdrawal, and rollback treatment |
| Documentation | Profile, runbook, security, consumer, and operations updates |

A documentation-only pull request cannot close those requirements by implication.

[Back to top](#top)

---

<a id="10-validation-expectations"></a>

## 10. Validation expectations and graduation gates

### 10.1 Validation layers

| Layer | What it proves | What it does not prove |
|---|---|---|
| Documentation validation | Links, anchors, upstream identity, bounded claims | Machine conformance or runtime behavior |
| Schema validation | Local carrier shape | Correct links, tiles, policy, or release |
| Offline profile validation | Deterministic behavior against synthetic snapshots | Live endpoint health or external interoperability |
| Controlled endpoint probe | Observed discovery, links, TMS, headers, and sample tiles at a time | Continuous correctness, rights, security, or release |
| Producer test | A named KFM server emits the selected profile | Independent consumer compatibility |
| Consumer test | A named KFM client interprets a selected profile | Complete server conformance |
| Normative conformance suite | Applicable OGC test assertions pass | KFM rights, sensitivity, evidence, or release |
| Release validation | Approved profile, proofs, policy/review, correction, and rollback bind to a release | Future uptime or external-source stability |
| Interoperability observation | Independent exchange works for a recorded case | Universal compatibility |

### 10.2 Required no-network negative cases

A future fixture suite should fail closed when:

- the expected Core conformance URI is absent;
- an advertised class conflicts with the resources returned;
- a tilesets list has no usable tileset link;
- tileset metadata has no usable tile template;
- the template is missing a required matrix, row, or column variable;
- variables are duplicated, ambiguous, or substituted outside their intended component;
- a link uses an unapproved scheme, host, port, or user-info component;
- redirects leave the allowlisted origin or enter a private/network-metadata range;
- a custom TMS cannot be resolved or its digest changes;
- TMS identifiers, limits, matrix dimensions, or row/column bounds conflict;
- variable-width matrices are present but unsupported;
- a declared media type conflicts with the response;
- a vector tile contains a forbidden field or harmful precision;
- a raster or coverage tile exceeds size, dimension, or decompression limits;
- an error response is cached or interpreted as a valid empty tile;
- credentials or signed query parameters would be logged or persisted;
- attribution or terms are missing, stale, or changed;
- the source is corrected, withdrawn, or superseded without propagation;
- evidence, policy, review, release, correction, or rollback references are missing; or
- a validator or resolver crashes or cannot safely classify the input.

### 10.3 Graduation gates

| Gate | Required evidence | Hold result when missing |
|---|---|---|
| **G0 — Scope and authority** | Named client/server/source role, owner roles, non-goals, accepted placement | `HOLD` |
| **G1 — Upstream pin** | Published standard, TMS version, required classes, encodings, errata/currentness record | `HOLD` |
| **G2 — Semantic profile** | Reviewed KFM meaning and anti-collapse rules | `HOLD` |
| **G3 — Machine profile** | Closed schema changes and compatibility/migration plan | `HOLD` |
| **G4 — Offline proof** | Synthetic fixtures, deterministic validator, negative cases, no-network tests | `HOLD` |
| **G5 — Discovery and links** | Link-relation, URI-template, conformance, representation, and identity checks | `HOLD` |
| **G6 — TMS correctness** | TMS resolution/digest, limits, matrix math, row/column bounds, supported capabilities | `HOLD` |
| **G7 — Security and operations** | Egress, redirect, authentication, limits, cache, audit, health, incident, and removal plan | `DENY` or `HOLD` |
| **G8 — Rights and public safety** | Terms, attribution, redistribution, sensitivity, transform, audience, review | `DENY` or `HOLD` |
| **G9 — Producer/consumer proof** | Bounded server or client implementation plus integration and interoperability evidence | `HOLD` |
| **G10 — Release closure** | Evidence, policy, review, proof, release manifest, correction, withdrawal, rollback, cache invalidation | `DENY` or `HOLD` |
| **G11 — Post-release review** | Observed metrics, drift detection, correction rehearsal, independent review | Remain pilot |

Passing G0–G9 does not itself publish. G10 is a separate authorized state transition.

### 10.4 Controlled network testing

Unit and contract tests should remain no-network. Live probes, when authorized, should be:

- manually invoked or scheduled under a reviewed source descriptor;
- read-only and rate-limited;
- isolated from private networks and cloud metadata endpoints;
- credential-safe;
- bounded by time, response size, redirect count, matrix range, and tile count;
- recorded with exact effective URL, timestamp, digest, and result;
- unable to promote or publish; and
- safe to replay from immutable snapshots.

[Back to top](#top)

---

<a id="11-anti-patterns"></a>

## 11. Security, rights, sensitivity, and anti-patterns

### 11.1 Security boundary

A tile template is executable network input. Treat it as untrusted until admitted.

| Risk | Required control |
|---|---|
| SSRF and private-network access | Scheme/host/port allowlist, DNS and IP-range checks, redirect revalidation, network isolation |
| DNS rebinding | Resolve and validate at connection time; pin policy to effective destination |
| Redirect escape | Bound count; reapply policy at every hop; deny credential forwarding across origins |
| Template injection | Parse templates structurally; bind only declared variables; reject host/path/query injection |
| Credential leakage | Secrets in approved headers or credential stores only; redact logs; avoid signed URLs in durable public records |
| Cache poisoning | Partition cache by effective URL, representation, authorization/audience, and relevant request headers |
| Content-type confusion | Verify declared and actual media type; reject HTML/login/error bodies as tiles |
| Tile/decompression bomb | Bound compressed and decoded size, dimensions, feature count, property count, and processing time |
| Parser vulnerability | Pin and admit libraries; sandbox or isolate high-risk decoding; keep fixtures for malformed inputs |
| Excessive enumeration | Validate TMS limits; rate-limit and budget matrix/row/column requests |
| Stale or false-clear cache | Preserve validators, expiry, correction/withdrawal state, and negative-cache policy |
| Browser exposure | Review CORS, CSP, credentials, referrer policy, URL logging, and public field/geometry exposure |
| Supply-chain drift | Pin server/client dependencies and record admission, SBOM, vulnerability, update, and removal evidence |

### 11.2 Rights and sensitivity boundary

OGC conformance does not grant use rights. Before public or semi-public use, verify:

- service and data owner identity;
- license or terms and whether caching, transformation, redistribution, and public display are allowed;
- required attribution and display placement;
- rate, quota, and acceptable-use obligations;
- personal, sovereign, tribal, cultural, archaeological, biodiversity, infrastructure, land/title, or other sensitivity;
- whether the tile payload reveals more fields or precision than the public layer declares;
- whether client-side filtering could be bypassed;
- whether a generalized tile was built before delivery and has a transform receipt;
- whether withdrawal or correction can invalidate caches and derived products; and
- whether the endpoint's source role is observation, regulatory, reference, interpretation, modeled, forecast, synthetic, or another explicitly defined role.

### 11.3 Anti-pattern register

| Anti-pattern | Why it fails |
|---|---|
| Hard-code one guessed `/tiles/...` path for every server | The standard is link/template-driven and does not prescribe one universal path |
| Treat `z/x/y` as proof of TMS semantics | Variable names and matrix identifiers do not establish CRS, origin, limits, or definition |
| Assume `WebMercatorQuad` globally | Part 1 mandates no specific TMS and KFM domains may require another CRS/scale model |
| Trust `conformsTo` without tests | Advertisement is not independent validation |
| Treat a `200` response as a valid tile | Error/login/HTML or wrong-format bodies can return `200` |
| Add an external URL directly to MapLibre | Bypasses source, rights, security, policy, release, correction, and rollback checks |
| Use style filters as redaction | Hidden client data remains exposed; transforms must occur before delivery |
| Treat tiles as evidence | Tiles are carriers; consequential claims resolve through `EvidenceBundle` |
| Put field-level profile shape in this Markdown | Creates a parallel schema authority |
| Make a documentation PR add runtime capability by implication | Current contracts, schemas, routes, validators, and adapters remain unchanged |
| Use one cache across audiences | Can leak restricted tiles or credentials |
| Infer empty/clear state from missing or failed tiles | Creates false-clear public-safety risk |
| Regenerate corrected tiles without release lineage | Breaks identity, cache invalidation, correction, and rollback |
| Log full signed URLs or authorization headers | Exposes credentials and may create durable access bypasses |
| Call working-repository extensions “Part 2” requirements | The official published baseline reviewed here is Part 1: Core 1.0 |

[Back to top](#top)

---

<a id="12-open-questions-and-needs-verification"></a>

## 12. Open questions and verification backlog

| ID | Question | Resolution mode |
|---|---|---|
| `OAT-001` | Does KFM want an external-service client profile, an outbound server profile, or both? | Architecture decision |
| `OAT-002` | Which minimum Part 1 conformance classes are required for each use case? | Standards/profile decision |
| `OAT-003` | Which tile encodings and media types are admitted? | Contract, schema, security, and consumer evidence |
| `OAT-004` | What canonical KFM protocol value and semantic object own the binding? | Contract/schema decision |
| `OAT-005` | Does the profile extend current `LayerManifest`, define a companion profile, or use another family? | ADR or accepted migration |
| `OAT-006` | How are TMS URI, custom-definition bytes, canonicalization, digest, limits, and aliases bound? | Identity/schema decision |
| `OAT-007` | Which TMS capabilities must the first client support, including variable-width matrices? | Measured client decision |
| `OAT-008` | Which application owns any outbound endpoint and which package owns shared parsing/validation? | Directory/architecture decision |
| `OAT-009` | What is the public-client fetch topology: same-origin, gateway, cache, direct admitted origin, or a bounded combination? | Security/deployment decision |
| `OAT-010` | What egress, redirect, DNS, authentication, CORS, CSP, timeout, size, and rate policies apply? | Security/policy review |
| `OAT-011` | How are rights, attribution, source role, cache permission, sensitivity, and redistribution represented? | Source/policy/steward review |
| `OAT-012` | What normative OGC test tooling is used and how is its version pinned? | Validation/tooling decision |
| `OAT-013` | Which independent producer and consumer will provide interoperability evidence? | Pilot plan |
| `OAT-014` | How do corrections, withdrawals, source drift, cache purge, and rollback propagate? | Release/operations design |
| `OAT-015` | Which working-repository extensions, if any, should be monitored without treating them as published requirements? | Standards-currentness review |
| `OAT-016` | Who are the accountable map, API, security, source, policy, validation, and release stewards? | Human governance decision |

Until these questions are resolved, operational use remains on `HOLD`.

[Back to top](#top)

---

<a id="13-references"></a>

## 13. Evidence basis and official references

### 13.1 Official upstream sources

| Source | Role |
|---|---|
| [OGC API — Tiles standard page](https://www.ogc.org/standards/ogcapi-tiles/) | Published identity, version, document number, status, overview |
| [OGC API — Tiles — Part 1: Core](https://docs.ogc.org/is/20-057/20-057.html) | Normative published requirements and conformance tests |
| [OGC Two Dimensional Tile Matrix Set standard page](https://www.ogc.org/standards/tms/) | TMS version, document identity, status, schemas |
| [OGC TMS 2.0 published specification](https://docs.ogc.org/is/17-083r4/17-083r4.html) | Normative TMS and tileset-metadata model |
| [OGC Tile Matrix Set Register](https://www.opengis.net/def/tms) | Registered reusable TMS identifiers |
| [OGC API — Tiles working repository](https://github.com/opengeospatial/ogcapi-tiles) | Public working source and extension watch only; not the published KFM baseline |
| [OGC 2D TMS working repository](https://github.com/opengeospatial/2D-Tile-Matrix-Set) | Official schemas, register source, examples, and future-work context |
| [OGC compliance program](https://www.ogc.org/how-our-compliance-program-works/) | Conformance testing program and policy context |

### 13.2 Current repository evidence

| Evidence | What it supports |
|---|---|
| [`docs/standards/README.md`](./README.md) | Standards-lane authority, evidence levels, currentness and conformance boundaries |
| [`contracts/data/layer_manifest.md`](../../contracts/data/layer_manifest.md) | Current semantic profile status and non-effects |
| [`schemas/contracts/v1/data/layer_manifest.schema.json`](../../schemas/contracts/v1/data/layer_manifest.schema.json) | Current strict protocol enumeration and fixture-only machine shape |
| [`contracts/layers/README.md`](../../contracts/layers/README.md) | Current layer-family placement conflict and proposed object status |
| [`docs/architecture/governed-api.md`](../architecture/governed-api.md) | Current route scaffold and fail-closed behavior |
| [`docs/architecture/TRUST_MEMBRANE.md`](../architecture/TRUST_MEMBRANE.md) | Current cross-root membrane evidence and limitations |
| [`docs/adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md`](../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md) | Proposed adapter seam and current scaffold/HOLD evidence |
| [`docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md`](<../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>) | Proposed renderer-family decision and current readiness limits |

External sources establish what the standards say. Repository sources establish what KFM currently contains. Neither alone proves KFM operational conformance or publication.

### 13.3 Currentness triggers

Re-review this page when:

- OGC publishes a new Part 1 revision, corrigendum, or additional normative part;
- OGC publishes or materially changes a TMS revision or register entry used by KFM;
- KFM accepts an OGC API — Tiles profile or related ADR;
- `LayerManifest` gains or changes a protocol/profile representation;
- a client, server, source adapter, validator, or route is implemented;
- an endpoint is admitted, released, corrected, withdrawn, or retired;
- security guidance changes for URL templates, SSRF, caching, or parsers; or
- a working-repository extension becomes a published standard.

[Back to top](#top)

---

<a id="14-related-docs"></a>

## 14. Related KFM documentation and no-loss ledger

### 14.1 Related documents

- [`docs/standards/README.md`](./README.md) — standards-lane authority and evidence model.
- [`WMTS.md`](./WMTS.md) — predecessor/external-service guidance; not interchangeable with OGC API — Tiles.
- [`MVT.md`](./MVT.md) — one tile encoding family.
- [`PMTILES.md`](./PMTILES.md) — static archive carrier guidance.
- [`STAC.md`](./STAC.md) — catalog guidance.
- [`MAP_TRUST_STATES.md`](./MAP_TRUST_STATES.md) — trust-visible map-state vocabulary.
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — adopted placement authority.
- [`docs/doctrine/lifecycle-law.md`](../doctrine/lifecycle-law.md) — lifecycle doctrine.
- [`docs/doctrine/trust-membrane.md`](../doctrine/trust-membrane.md) — trust-membrane doctrine.
- [`docs/architecture/TRUST_MEMBRANE.md`](../architecture/TRUST_MEMBRANE.md) — current architecture/enforcement map.
- [`docs/architecture/governed-api.md`](../architecture/governed-api.md) — current API scaffold.
- [`docs/architecture/map-shell.md`](../architecture/map-shell.md) — map-shell boundary.
- [`docs/architecture/contract-schema-policy-split.md`](../architecture/contract-schema-policy-split.md) — authority separation.
- [`contracts/data/layer_manifest.md`](../../contracts/data/layer_manifest.md) — current layer semantic contract.
- [`schemas/contracts/v1/data/layer_manifest.schema.json`](../../schemas/contracts/v1/data/layer_manifest.schema.json) — current machine shape.

### 14.2 No-loss modernization ledger

| Prior material | Disposition |
|---|---|
| Purpose and scope | Retained and made authority-explicit |
| Why KFM tracks the standard | Retained; removed obsolete category-atlas authority claims |
| Standard overview | Refreshed against official OGC sources |
| Conformance classes | Expanded to the published Part 1 class set and exact URIs |
| Resources and URL templates | Corrected to distinguish common examples, class-specific paths, links, and non-prescribed templates |
| TMS 2.0 reference | Retained; removed universal-default implications and added identity/limits/digest boundaries |
| KFM trust posture | Retained and grounded in current repository evidence |
| Integration model | Retained as a clearly proposed external-client and outbound-server graduation path |
| KFM objects/contracts | Recast as candidate authority changes; current proposed/inactive state is explicit |
| Validation expectations | Expanded into offline negatives, controlled probes, and graduation gates |
| Anti-patterns | Retained and expanded for SSRF, redirects, caching, content confusion, and false-clear risk |
| Open questions | Retained as stable `OAT-*` backlog items |
| References and related docs | Replaced malformed citation-image artifacts with direct authoritative and repository sources |
| Legacy anchors | All prior major-section anchors retained |

### 14.3 Rollback

Before merge, close or abandon the draft pull request.

After an authorized merge, revert the documentation commit or restore prior blob `a9337842473846d05d14dbbc1a52cbca7199ea63` through normal review. Because this change creates no profile, route, source admission, runtime, cache, release, deployment, or public artifact, rollback requires no data migration, source deactivation, cache purge, endpoint withdrawal, or public correction.

<p align="right"><a href="#top">Back to top</a></p>
