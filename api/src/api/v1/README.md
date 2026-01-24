# 🧭 KFM API v1 — Contracts, Conventions, & Endpoint Map

![API](https://img.shields.io/badge/API-v1-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-ready-009688?logo=fastapi&logoColor=white)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.x-6BA539?logo=openapiinitiative&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-supported-E10098?logo=graphql&logoColor=white)
![PostGIS](https://img.shields.io/badge/PostGIS-spatial-336791?logo=postgresql&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-graph-008CC1?logo=neo4j&logoColor=white)
![Evidence](https://img.shields.io/badge/Evidence-STAC%20%2B%20DCAT%20%2B%20PROV-4C1?logo=files&logoColor=white)
![FAIR+CARE](https://img.shields.io/badge/Governance-FAIR%20%2B%20CARE-7A4?logo=leaflet&logoColor=white)

> [!IMPORTANT]
> **This folder defines the versioned HTTP surface for KFM.**  
> Everything the UI does (maps, search, graph traversal, Story Nodes, Focus Mode) should flow through `/api/v1/*`, where we can **validate**, **authorize**, and **attach provenance** consistently.

---

## 📌 What lives here

This `api/src/api/v1/` layer is the **stable interface contract** for the Kansas Frontier Matrix (KFM) platform.

It is designed to:
- Serve a **React/TypeScript UI** (2D/3D maps, timeline, storytelling, Focus Mode) without direct DB access 🧩
- Provide **REST + OpenAPI** for interoperability and scripting ✅
- Provide **GraphQL** for relationship-heavy “graph-shaped” queries 🕸️
- Enforce **policy gates** (schema, license, sensitivity, provenance, citations) 🔒
- Remain **stateless + container-friendly** so it scales horizontally 🧱
- Make all outputs **evidence-first** (STAC/DCAT/PROV + source links) 🧾

---

## 🗺️ Table of contents

- [Base URL & versioning](#base-url--versioning)
- [Design goals](#design-goals)
- [Standards & media types](#standards--media-types)
- [Auth, roles, and policy gates](#auth-roles-and-policy-gates)
- [Response envelope](#response-envelope)
- [Errors](#errors)
- [Endpoint index](#endpoint-index)
- [Query conventions](#query-conventions)
- [Caching & performance](#caching--performance)
- [Adding new v1 endpoints](#adding-new-v1-endpoints)
- [References](#references)

---

## Base URL & versioning

**Prefix:** ` /api/v1 `

**Versioning rules (v1 is stable):**
- ✅ Additive changes are OK (new fields, new endpoints, new query params)
- 🚫 Breaking changes require `/api/v2` (or a feature-flagged experimental namespace)
- 🧯 Deprecations must include: a header + a migration note in docs

Recommended headers:
- `X-KFM-API-Version: 1`
- `X-KFM-Deprecated: true` (when applicable)
- `X-Request-Id: <uuid>` (always)

> [!NOTE]
> Some older diagrams/docs may show `/api/...` examples. In **code**, we version under `/api/v1` so clients can rely on stability.

---

## Design goals

### 1) Evidence-first publishing 🧾
Every “published” dataset must have the **evidence triplet**:
- **STAC** (spatiotemporal footprint + assets)
- **DCAT** (catalog record + license/distributions)
- **PROV** (lineage + transformations)

### 2) Governed access (UI never touches DB) 🔐
- UI must never run direct SQL/Cypher.
- Sensitive or restricted info is handled here (redaction/generalization/deny).

### 3) Map-first performance 🗺️⚡
- Tiles and spatial subsets are first-class
- Prefer server-side filtering (bbox/time/property) over shipping giant payloads

### 4) Graph-aware discovery 🕸️
Use Neo4j as contextual glue; PostGIS as authoritative spatial store.

### 5) AI-safe interactions 🤖🧭
Focus Mode must return **citations** or refuse. No unsourced outputs.

### 6) Federation-ready 🌎
The API shape should support multi-instance “Frontier Matrix” federation via open standards.

---

## Standards & media types

Common payloads and formats:
- **GeoJSON** (`application/geo+json`)
- **JSON / JSON-LD** (`application/json`, `application/ld+json`)
- **STAC API**-style responses (Collections/Items/Search)
- **DCAT** feeds/records
- **PROV-O** lineage documents (JSON-LD)
- **Vector tiles (MVT)**: `application/vnd.mapbox-vector-tile`
- **Raster tiles** (PNG/JPEG) or links to **COGs**
- Optional: **PMTiles**, **GeoParquet**, **MBTiles** as exports/distributions

---

## Auth, roles, and policy gates

### Roles (typical)
- 👀 `viewer` — public read
- ✍️ `contributor` — propose Story Nodes / annotations / submissions
- 🧑‍⚖️ `curator` — review + publish content
- 🛠️ `admin` — run pipelines, manage policies, system operations

### Policy gates (fail-closed) 🚧
At minimum, expect gates for:
- ✅ schema validation
- ✅ license presence
- ✅ STAC/DCAT/PROV completeness
- ✅ sensitivity classification + handling
- ✅ provenance completeness
- ✅ AI citation requirement (Focus Mode must cite or refuse)

> [!TIP]
> Treat this layer as **the governance boundary**. If it isn’t enforced here, it isn’t enforced.

---

## Response envelope

Where possible, v1 responses follow a consistent “KFM envelope”:

```json
{
  "data": {},
  "meta": {
    "request_id": "b2a7d3f1-0b3e-4c0b-9f6b-9c2d2a1d9f63",
    "generated_at": "2026-01-23T00:00:00Z",
    "paging": { "limit": 50, "cursor": null },
    "warnings": []
  },
  "provenance": {
    "stac": ["stac:item-or-collection-id"],
    "dcat": ["dcat:dataset-id"],
    "prov": ["prov:activity-id-or-doc-id"],
    "evidence": [
      { "type": "dataset", "id": "kfm.ks.example.v1", "href": "/api/v1/datasets/kfm.ks.example.v1" }
    ],
    "redactions": []
  },
  "links": {
    "self": "/api/v1/...",
    "next": null
  }
}
```

---

## Errors

Prefer **RFC 7807 Problem Details** (`application/problem+json`) for non-2xx:

```json
{
  "type": "https://kfm.dev/problems/policy-violation",
  "title": "Policy violation",
  "status": 403,
  "detail": "AI outputs must include citations to source material.",
  "instance": "/api/v1/focus",
  "request_id": "b2a7d3f1-0b3e-4c0b-9f6b-9c2d2a1d9f63",
  "code": "POLICY_CITATION_REQUIRED"
}
```

---

## Endpoint index

> [!NOTE]
> The **authoritative** list is the generated **OpenAPI spec** (Swagger).  
> This section documents the **intended v1 surface** and conventions.

| Group | Example endpoints | Notes |
|---|---|---|
| 🩺 System | `GET /healthz`, `GET /readyz`, `GET /version` | k8s-friendly |
| 📚 Catalog/Datasets | `GET /datasets`, `GET /datasets/{id}`, `GET /datasets/{id}/prov` | evidence-first |
| 🧭 Search | `GET /search?q=...`, `POST /search` | unified, filterable |
| 🗺️ Layers/Tiles | `GET /layers`, `GET /tiles/{layer}/{z}/{x}/{y}.pbf` | MapLibre/Cesium |
| 🕸️ Graph | `GET /graph/places/{id}/datasets`, `POST /graph/query` | governed traversal |
| 🧠 Focus Mode | `POST /focus`, `POST /focus/stream` | citations required |
| 📖 Story Nodes | `GET /stories`, `GET /stories/{id}`, `POST /stories` | narrative + manifest |
| 🧵 Pulse Threads | `GET /pulse`, `POST /pulse`, `GET /pulse/{id}` | geotagged updates |
| 🧩 Concepts | `GET /concepts`, `GET /concepts/{id}/neighbors` | “attention” lens |
| 🧰 Ingest/Jobs | `POST /ingest`, `GET /ingest/runs/{run_id}` | admin-only gates |
| 📦 Exports/Artifacts | `POST /exports`, `GET /artifacts/{digest}` | OCI + provenance |
| 🧪 Future | `GET /offline-packs`, `GET /realtime/feeds` | planned/experimental |

---

## Core endpoint groups (details)

<details>
<summary><strong>🩺 System endpoints</strong></summary>

- `GET /api/v1/healthz` → process health
- `GET /api/v1/readyz` → dependencies ready (DB, graph, cache)
- `GET /api/v1/version` → build + git SHA + API version
- `GET /api/v1/metrics` → Prometheus (if enabled)

</details>

<details>
<summary><strong>📚 Catalog & datasets</strong></summary>

Typical resources:
- `GET /api/v1/datasets`  
  List datasets with key metadata (license, bbox, time range, tags, distributions).
- `GET /api/v1/datasets/{dataset_id}`  
  Dataset details + links to STAC/DCAT/PROV.
- `GET /api/v1/datasets/{dataset_id}/stac`
- `GET /api/v1/datasets/{dataset_id}/dcat`
- `GET /api/v1/datasets/{dataset_id}/prov`
- `GET /api/v1/datasets/{dataset_id}/data`  
  Returns:
  - a subset (GeoJSON/CSV) if small, or
  - a signed URL / distribution link if large

</details>

<details>
<summary><strong>🧭 Search & discovery</strong></summary>

- `GET /api/v1/search?q=...&bbox=...&datetime=...&types=datasets,stories,places`
- `POST /api/v1/search` (preferred for complex queries)

Common filters:
- `q` — full-text search
- `bbox` — `minLon,minLat,maxLon,maxLat`
- `datetime` — ISO8601 interval (`start/end`) and STAC-style open intervals
- `limit`, `cursor` — pagination

</details>

<details>
<summary><strong>🗺️ Layers, styles, and tiles</strong></summary>

For map UX (MapLibre/Cesium), endpoints commonly include:

- `GET /api/v1/layers`  
  Returns “renderable layers” derived from catalogs + config.
- `GET /api/v1/layers/{layer_id}`  
  Includes style hints, attribution, time coverage, and tile templates.
- `GET /api/v1/tiles/{layer_id}/{z}/{x}/{y}.pbf`  
  Vector tiles (**MVT**).  
  `Content-Type: application/vnd.mapbox-vector-tile`
- `GET /api/v1/raster/{layer_id}/{z}/{x}/{y}.png`  
  Raster tiles (when applicable).
- `GET /api/v1/styles/{style_id}.json`  
  MapLibre style JSON (optional).
- `GET /api/v1/legend/{layer_id}`  
  Legend assets (optional).
- `GET /api/v1/assets/{asset_id}`  
  Resolve to distribution URLs (COG/PMTiles/etc).

Caching expectations:
- `ETag` and `Cache-Control` on tiles/styles
- stable URLs for immutable artifacts

</details>

<details>
<summary><strong>🕸️ Graph (Neo4j-backed) + GraphQL</strong></summary>

REST examples:
- `GET /api/v1/graph/places/{place_id}`
- `GET /api/v1/graph/places/{place_id}/datasets`
- `GET /api/v1/graph/events?bbox=...&datetime=...`
- `POST /api/v1/graph/query` (curated query shapes only; no arbitrary Cypher from clients)

GraphQL:
- `POST /api/v1/graphql`

GraphQL should enforce:
- query depth / complexity limits
- pagination on lists
- allowlist patterns for public usage

</details>

<details>
<summary><strong>📖 Story Nodes (interactive narratives)</strong></summary>

Core idea: story content is **not just markdown** — it is evidence-linked and queryable.

- `GET /api/v1/stories`  
- `GET /api/v1/stories/{story_id}`  
- `GET /api/v1/stories/{story_id}/manifest`  
  Evidence manifest (YAML/JSON) with checksums + references.
- `GET /api/v1/stories/{story_id}/prov`  
  PROV linkage for “which datasets support this story?”
- `POST /api/v1/stories` (auth required)  
  Create/submit new Story Node (typically as draft).
- `PUT /api/v1/stories/{story_id}` (auth + policy)

> [!IMPORTANT]
> Story Nodes must maintain **source attribution** and **structured evidence** so the UI can show “the map behind the map.”

</details>

<details>
<summary><strong>🧵 Pulse Threads + 🧩 Concepts (thematic lenses)</strong></summary>

Pulse Threads (geotagged micro-narratives / updates):
- `GET /api/v1/pulse?bbox=...&datetime=...&concept=drought`
- `POST /api/v1/pulse` (auth)
- `GET /api/v1/pulse/{pulse_id}`

Conceptual Attention Nodes (theme-based navigation + AI transparency):
- `GET /api/v1/concepts`
- `GET /api/v1/concepts/{concept_id}`
- `GET /api/v1/concepts/{concept_id}/neighbors`
- Optional: `POST /api/v1/concepts/{concept_id}/attend`  
  Creates a user/session “attention” state for UI + Focus Mode.

Expected behavior:
- Concepts link datasets + stories + pulse threads
- Focus Mode can disclose which concepts guided retrieval (“attention transparency”)

</details>

<details>
<summary><strong>🧠 Focus Mode (AI)</strong></summary>

- `POST /api/v1/focus`  
  Ask a question with map context.
- `POST /api/v1/focus/stream`  
  SSE/WebSocket streaming (implementation choice).

Example request:
```json
{
  "question": "What happened here during the Dust Bowl era?",
  "context": {
    "bbox": [-102.05, 36.99, -94.60, 40.00],
    "datetime": "1930-01-01/1940-12-31",
    "selected_layers": ["kfm.ks.landcover.1930s.v1"],
    "selected_feature": null
  }
}
```

Key contract requirements:
- ✅ Always return citations (datasets, documents, Story Nodes, provenance docs)
- 🚫 If citations can’t be produced, return a policy violation error
- 🧾 Include provenance IDs so answers are audit-friendly

</details>

<details>
<summary><strong>🧰 Ingest, pipelines, and jobs</strong></summary>

Admin & contributor tooling (guarded by policy):
- `POST /api/v1/ingest` — trigger pipeline run / upload submission
- `GET /api/v1/ingest/runs`
- `GET /api/v1/ingest/runs/{run_id}`
- `GET /api/v1/jobs/{job_id}`

Operational expectations:
- raw inputs are immutable (first trust boundary)
- transformations are deterministic/config-driven
- every run yields STAC/DCAT/PROV outputs before publish

</details>

<details>
<summary><strong>📦 Exports & artifacts</strong></summary>

Exports (user-facing):
- `POST /api/v1/exports` → create export job (GeoJSON, CSV, GeoPackage, MBTiles…)
- `GET /api/v1/exports/{export_id}` → status + signed download URL

Artifacts (platform-facing, OCI-oriented):
- `GET /api/v1/artifacts/{digest}`  
  Resolve to OCI registry refs / download links and attach provenance references.

Nice-to-have:
- cosign verification metadata
- SBOM / provenance attestations

</details>

---

## Query conventions

### Spatial
- `bbox=minLon,minLat,maxLon,maxLat` (WGS84 / EPSG:4326 default)
- GeoJSON coordinates are always `[lon, lat]`

### Temporal
- `datetime=YYYY-MM-DD/YYYY-MM-DD`
- Support open intervals (`../2020-01-01`, `2020-01-01/..`) where feasible

### Paging
- Prefer cursor paging for heavy endpoints:
  - `limit=50`
  - `cursor=<opaque>`

### Sorting
- `sort=-created_at` (descending)
- `sort=title` (ascending)

---

## Caching & performance

- Tiles/styles should be cacheable:
  - `ETag`, `Cache-Control`, optional `stale-while-revalidate`
- Prefer **links to immutable artifacts** (COGs/PMTiles/GeoParquet) over giant JSON payloads
- Guard GraphQL complexity
- Prefer async + streaming for heavy AI calls

---

## Adding new v1 endpoints

✅ **PR checklist**
- [ ] Add/extend **Pydantic schemas** (requests + responses)
- [ ] Add router under `/api/v1/*` with a clear tag
- [ ] Add/extend **OpenAPI docs** (examples + descriptions)
- [ ] Add policy checks (authz + sensitivity + provenance requirements)
- [ ] Add tests:
  - [ ] unit tests (schema + business rules)
  - [ ] contract tests (OpenAPI snapshots/golden)
  - [ ] integration tests (DB/graph behind a test container)
- [ ] Ensure provenance is attached (STAC/DCAT/PROV IDs or links)
- [ ] Ensure errors use `application/problem+json`

> [!TIP]
> If you’re adding a “new kind of thing”, also add:
> - a glossary entry 🧾
> - an ADR (why this exists) 🏛️
> - a policy note (how it’s governed) ⚖️

---

## References

### 📘 Core project docs (source of truth)

- **UI System Overview** (map UI, story nodes, Focus Mode, offline/mobile, AR) :contentReference[oaicite:0]{index=0}
- **Data Intake Guide** (immutability, deterministic ETL, evidence triplet, governed API boundary) :contentReference[oaicite:1]{index=1}
- **Innovative Concepts** (future-facing features: AR, simulation/scenario, dashboards, expansion patterns) :contentReference[oaicite:2]{index=2}
- **Pulse / Refinement Notes** (pulse threads, concepts, evidence-linked narratives, artifact ideas) :contentReference[oaicite:3]{index=3}

### 📚 Supporting docs (design alignment)
- Comprehensive Architecture / Technical Documentation
- AI System Overview (Focus Mode safety + research integration)
- Latest Ideas & Future Proposals (offline packs, reproducible research, education tooling)
- Additional Project Ideas (OCI artifacts, concept nodes, evidence-first story manifests)
- Open-Source Mapping Hub Design (STAC-like catalogs, document KB, 4D space+time vision)

---

## 🧾 Glossary (tiny but useful)

- **Evidence triplet**: STAC + DCAT + PROV required to publish a dataset
- **Story Node**: interactive narrative that binds text + layers + time + citations
- **Pulse Thread**: geotagged, time-stamped “micro-story” update linked to evidence
- **Concept node**: thematic tag/entity used to drive UI filtering + AI attention
- **Focus Mode**: AI assistant that must cite KFM evidence or refuse

