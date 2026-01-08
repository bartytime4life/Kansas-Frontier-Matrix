---
title: "🧾 KFM REST API Contract"
path: "docs/specs/api/API__REST_CONTRACT.md"
version: "v0.1.0"
last_updated: "2026-01-08"
status: "Draft"
doc_kind: "REST Contract (Human‑Readable) + Implementation Rules"
canonical_contracts:
  - "docs/specs/api/openapi.yaml"
related:
  - "docs/specs/api/README.md"
  - "docs/specs/api/API__REST_CONTRACT.md"
  - "docs/specs/api/API__ERROR_MODEL.md"
license: "CC-BY-4.0"
---

# 🧾 KFM REST API Contract (v1)

<div align="center">

![Status](https://img.shields.io/badge/status-draft-orange)
![API](https://img.shields.io/badge/api-REST%20(OpenAPI)-blue)
![Catalog](https://img.shields.io/badge/catalog-STAC%20%7C%20DCAT-brightgreen)
![Provenance](https://img.shields.io/badge/provenance-PROV--O%20%7C%20OpenLineage-4c1)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-6f42c1)

**Deterministic · Provenanced · Governed · Map‑First**

</div>

---

## 🧭 Purpose & contract layering

This document defines **how the REST API behaves** (semantics, invariants, envelopes, governance rules, determinism rules).  
The machine‑readable path/field definitions live in **📄 `openapi.yaml`** (canonical for tooling).

> [!IMPORTANT]
> If a detail conflicts between this file and `openapi.yaml`, treat it as a **contract bug** and fix the conflict immediately. ⚠️

---

## 🎯 Scope

**In scope** ✅

- 🗂️ Catalog + search (STAC-first; DCAT metadata)
- 🧷 Story Nodes + version locking (reproducible narrative states)
- 🗺️ Map delivery (vector tiles/PMTiles, styles, previews)
- 🕸️ Governed graph navigation (bounded entity traversal via REST)
- 🧠 Focus Mode packets (explainable + citations + provenance pointers)
- 🧪 Async simulation jobs (ABM/DES/etc.) with artifacts & lineage
- 🧬 Provenance retrieval (PROV JSON‑LD, run manifests, SBOM, attestations)
- 📡 Telemetry ingestion (UI + pipelines) with schema enforcement
- 🔔 Automation hooks (idempotent triggers)

**Out of scope (for v1)** ❌

- Direct database access
- Unbounded graph traversal or arbitrary Cypher execution
- OGC WMS/WFS as a primary interface (may exist as compatibility adapters later)

---

## 🧱 Non‑negotiables (governed)

These apply to **every** endpoint.

1. 🧨 **Bounded compute & bounded response size**
   - Default limits MUST exist and be enforced.
   - All list endpoints MUST paginate (cursor pagination preferred).

2. 🧾 **Determinism**
   - Stable ordering + stable pagination.
   - Same inputs + same version locks MUST return the same outputs.

3. 🛡️ **FAIR+CARE governance**
   - Sensitive fields MUST be redacted/generalized before leaving the API.
   - Response MUST explain redaction at a **metadata level** (audit-friendly).

4. 🧬 **Provenance-first**
   - Derived results MUST include provenance pointers (`prov_run_id`, `activity_id`, hashes).

5. 🔐 **Security posture**
   - Parameterized queries only.
   - Input validation everywhere.
   - Rate limiting + backpressure.

---

## 🌐 Base URL & versioning

### Base path

- **Stable:** `/api/v1`
- **Optional beta:** `/api/v1beta` (only for clearly marked experimental endpoints)

### SemVer meaning

- **MAJOR**: breaking change (rename/remove/meaning change)
- **MINOR**: backward‑compatible additions
- **PATCH**: examples/docs/tests only

### Deprecation

- Deprecations MUST include:
  - `Deprecation: true` header
  - `Sunset: <RFC3339 date>` header
  - Replacement endpoint reference in docs

---

## 🔐 Authentication & authorization

### Auth mechanisms

- 🔑 Bearer token (OIDC/OAuth) for users
- 🧾 API keys (scoped) for automation
- 🧷 Signed payloads (HMAC/JWT) for inbound hooks

### Role expectations (logical model)

- 🌍 **Public**: browse public catalogs & generalized map assets
- ✍️ **Contributor**: create/update Story Nodes, submit bounded jobs
- 🧰 **Maintainer**: publish catalogs/datasets, approve governance changes
- 🛡️ **Auditor**: read provenance bundles, release artifacts

> [!NOTE]
> AuthZ MUST be enforceable by a gateway/service boundary (not only inside business logic).

---

## 🧩 Global conventions

### Content types

- JSON: `application/json`
- GeoJSON: `application/geo+json`
- NDJSON streaming: `application/x-ndjson`
- Vector tiles: `application/x-protobuf`
- PMTiles: `application/octet-stream`
- PNG preview: `image/png`
- COG (GeoTIFF): `image/tiff`
- GeoParquet: `application/octet-stream` (or `application/x-parquet` if supported)

### Time

- RFC3339 timestamps (UTC “Z” preferred)
- Ranges use STAC‑style: `start/end` (either may be `..`)

### Geo conventions

- Coordinate reference: WGS84 / EPSG:4326 for API-facing GeoJSON
- `bbox` order: `[minLon, minLat, maxLon, maxLat]`
- `datetime` uses STAC semantics
- Geometry in requests MUST be GeoJSON; server MAY simplify/clip

---

## 🧾 Standard headers

| Header | Dir | Required | Why |
|---|---:|:---:|---|
| `X-Request-Id` | → | SHOULD | Client-side correlation |
| `Idempotency-Key` | → | MUST for POST/PUT job submits | Safe retry semantics |
| `X-KFM-Client` | → | SHOULD | Client name/version |
| `ETag` / `If-None-Match` | ↔ | SHOULD | Cache correctness |
| `Cache-Control` | ← | SHOULD | Tile/asset performance |
| `Retry-After` | ← | MUST on 429/503 | Backpressure |

---

## 📦 Response shapes

### A) KFM Envelope (default)

Most endpoints return an envelope:

```json
{
  "data": {},
  "links": [],
  "meta": {
    "request_id": "req_...",
    "trace_id": "trace_...",
    "generated_at": "2026-01-08T00:00:00Z",
    "paging": { "next_cursor": null, "count": 1 },
    "warnings": []
  },
  "governance": {
    "care_status": "public",
    "generalized": false,
    "redactions": [],
    "policy_version": "CARE-LOC-01@2026-01-01"
  },
  "provenance": {
    "prov_run_id": null,
    "prov_activity_id": null,
    "inputs": [],
    "hashes": {}
  }
}
```

### B) Raw standards (no envelope)

To preserve compatibility, the API MUST return **raw, spec‑compatible documents** (no envelope) for:

- 🗂️ STAC endpoints (`/stac/*`)
- 🧬 PROV JSON‑LD documents (`/prov/*/*.jsonld`)

> [!IMPORTANT]
> If an endpoint returns raw STAC/PROV, governance/redaction info MUST be communicated via **headers** (and/or a sibling metadata endpoint), not by wrapping the payload.

---

## ❌ Error model

Errors use a consistent JSON envelope:

```json
{
  "error": {
    "code": "KFM_BAD_REQUEST",
    "message": "bbox is invalid",
    "details": { "bbox": "must be [minLon,minLat,maxLon,maxLat]" }
  },
  "meta": {
    "request_id": "req_...",
    "trace_id": "trace_..."
  }
}
```

### Common error codes

| Code | Typical status | Meaning |
|---|---:|---|
| `KFM_BAD_REQUEST` | 400 | Validation failed |
| `KFM_UNAUTHORIZED` | 401 | Missing/invalid auth |
| `KFM_FORBIDDEN` | 403 | Not permitted |
| `KFM_NOT_FOUND` | 404 | Missing resource |
| `KFM_CONFLICT` | 409 | Version/lock conflict |
| `KFM_GONE` | 410 | Deprecated removed |
| `KFM_UNSUPPORTED_MEDIA` | 415 | Wrong content type |
| `KFM_UNPROCESSABLE` | 422 | Semantically invalid |
| `KFM_RATE_LIMITED` | 429 | Backpressure |
| `KFM_DEPENDENCY_FAILURE` | 424/502 | External dependency failed |
| `KFM_INTERNAL` | 500 | Unexpected server error |

---

## 📄 Pagination & sorting

### Cursor pagination (preferred)

- Request:
  - `page[limit]=100`
  - `page[cursor]=<opaque>`
- Response:
  - `meta.paging.next_cursor`

### Deterministic ordering

All list endpoints MUST accept `sort=` and default to a stable order.

Example:

- `sort=updated_at:desc,id:asc`

---

## 🚦 Rate limiting & backpressure

- API MUST protect itself with a token‑bucket style limiter.
- On overload or external dependency throttling:
  - return **429** or **503**
  - include `Retry-After`

> [!NOTE]
> If upstream APIs (e.g., hydrology/air) return 429/5xx spikes, the system SHOULD degrade gracefully (serve cached + mark `warnings`).

---

# 🗺️ REST Endpoint Index

> Status legend: ✅ Stable · 🧪 Beta · 🧱 Planned

| Group | Endpoints |
|---|---|
| 🩺 Meta/Health | ✅ `GET /api/v1/healthz` · ✅ `GET /api/v1/readyz` · ✅ `GET /api/v1/meta` |
| 🗂️ Datasets (DCAT-ish) | ✅ `GET /api/v1/datasets` · ✅ `GET /api/v1/datasets/{dataset_id}` |
| 🧭 STAC | ✅ `GET /api/v1/stac` · ✅ `GET /api/v1/stac/collections` · ✅ `GET /api/v1/stac/collections/{collection_id}` · ✅ `GET /api/v1/stac/items/{item_id}` · ✅ `POST /api/v1/stac/search` |
| 🧷 STAC lineage/versioning | 🧪 `GET /api/v1/stac/items/{item_id}/lineage` · 🧪 `GET /api/v1/stac/items/{item_id}/diff?against={other_id}` |
| 🗺️ Tiles & styles | ✅ `GET /api/v1/tilesets` · ✅ `GET /api/v1/tilesets/{tileset_id}` · ✅ `GET /api/v1/tiles/{tileset_id}/{z}/{x}/{y}.pbf` · ✅ `GET /api/v1/styles/{style_id}.json` |
| 📦 Assets | ✅ `GET /api/v1/assets/{asset_id}` · ✅ `GET /api/v1/assets/{asset_id}/download` · ✅ `HEAD /api/v1/assets/{asset_id}/download` |
| 🕸️ Graph (bounded REST) | ✅ `GET /api/v1/graph/entities` · ✅ `GET /api/v1/graph/entities/{entity_id}` · ✅ `GET /api/v1/graph/entities/{entity_id}/neighbors` · 🧪 `POST /api/v1/graph/query` |
| 🎬 Story Nodes | ✅ `GET /api/v1/story-nodes` · ✅ `GET /api/v1/story-nodes/{story_id}` · 🧪 `POST /api/v1/story-nodes` · 🧪 `PATCH /api/v1/story-nodes/{story_id}` |
| 🧠 Focus Mode | ✅ `POST /api/v1/analysis/focus` · ✅ `GET /api/v1/analysis/focus/jobs/{job_id}` · ✅ `GET /api/v1/analysis/focus/jobs/{job_id}/result` |
| 🧪 Simulations | ✅ `POST /api/v1/simulations/abm` · ✅ `GET /api/v1/simulations/jobs/{job_id}` · ✅ `GET /api/v1/simulations/jobs/{job_id}/results` · ✅ `POST /api/v1/simulations/jobs/{job_id}/cancel` |
| 📈 Time Series | ✅ `GET /api/v1/timeseries/stations` · ✅ `GET /api/v1/timeseries/stations/{station_id}` · ✅ `GET /api/v1/timeseries/series` · 🧪 `POST /api/v1/timeseries/query` |
| 🧬 Provenance | ✅ `GET /api/v1/prov/runs/{run_id}` · ✅ `GET /api/v1/prov/runs/{run_id}/prov.jsonld` · ✅ `GET /api/v1/prov/runs/{run_id}/manifest.json` · ✅ `GET /api/v1/prov/runs/{run_id}/sbom.spdx.json` · ✅ `GET /api/v1/prov/runs/{run_id}/attestation.json` |
| 📦 Releases | 🧪 `GET /api/v1/releases` · 🧪 `GET /api/v1/releases/{version}` · 🧪 `GET /api/v1/releases/{version}/manifest.zip` · 🧪 `GET /api/v1/releases/{version}/sbom.spdx.json` · 🧪 `GET /api/v1/releases/{version}/focus-telemetry.json` |
| 📡 Telemetry | ✅ `POST /api/v1/telemetry/events` · 🧪 `GET /api/v1/telemetry/snapshots/latest` |
| 🔔 Hooks | 🧪 `POST /api/v1/hooks/{source}` |

---

# 🧾 Endpoint contracts (REST)

## 🩺 Meta & health

### ✅ GET `/api/v1/healthz`

**Purpose:** Liveness check  
**Auth:** none  
**Response:** `200 OK`

```json
{ "ok": true }
```

---

### ✅ GET `/api/v1/readyz`

**Purpose:** Readiness check (db reachable, cache ok, migrations ok)  
**Auth:** none  
**Response:** `200 OK` or `503 Service Unavailable`

```json
{
  "ok": true,
  "checks": {
    "db": "ok",
    "cache": "ok",
    "object_store": "ok"
  }
}
```

---

### ✅ GET `/api/v1/meta`

**Purpose:** API identity + contract versions  
**Auth:** none  
**Response:** `200 OK` (enveloped)

```json
{
  "data": {
    "service": "kfm-api",
    "api_version": "v1",
    "contract_version": "v0.1.0",
    "commit": "git_sha",
    "build_time": "2026-01-08T00:00:00Z",
    "links": {
      "openapi": "/api/v1/meta/openapi",
      "docs": "/docs/specs/api/README.md"
    }
  },
  "meta": { "request_id": "req_x", "trace_id": "tr_x", "generated_at": "2026-01-08T00:00:00Z" },
  "governance": { "care_status": "public", "generalized": false, "redactions": [], "policy_version": "CARE-LOC-01@2026-01-01" },
  "provenance": { "prov_run_id": null, "prov_activity_id": null, "inputs": [], "hashes": {} },
  "links": []
}
```

---

## 🗂️ Datasets (DCAT-ish)

### ✅ GET `/api/v1/datasets`

**Purpose:** List datasets (high-level catalog records)  
**Auth:** public  
**Query params:**
- `q` (string) — full text search
- `tag` (string|repeatable) — filters
- `license` (string) — e.g., `CC-BY-4.0`
- `page[limit]`, `page[cursor]`

**Response:** `200 OK` (enveloped list)

---

### ✅ GET `/api/v1/datasets/{dataset_id}`

**Purpose:** Dataset descriptor (DCAT-aligned)  
**Auth:** public (governance applies)  
**Response:** `200 OK`

**Minimum fields:**
- `dataset_id`, `title`, `description`
- `publisher`, `license`
- `spatial`, `temporal`
- `distributions[]` (links to STAC collections/items/assets)
- `provenance` pointers (run + activity ids)

---

## 🧭 STAC (raw payloads)

> [!IMPORTANT]
> STAC endpoints return **raw STAC JSON** (no KFM envelope).  
> Governance signals use headers (e.g., `X-KFM-Redactions`, `X-KFM-Policy-Version`).

### ✅ GET `/api/v1/stac`

**Purpose:** STAC landing page  
**Response:** STAC Landing Page JSON

---

### ✅ GET `/api/v1/stac/collections`

**Purpose:** List STAC collections  
**Response:** STAC Collections

---

### ✅ GET `/api/v1/stac/collections/{collection_id}`

**Purpose:** Fetch collection  
**Response:** STAC Collection

---

### ✅ GET `/api/v1/stac/items/{item_id}`

**Purpose:** Fetch STAC item  
**Response:** STAC Item

---

### ✅ POST `/api/v1/stac/search`

**Purpose:** Spatiotemporal search (STAC API style)  
**Request:** STAC Search JSON  
**Response:** STAC ItemCollection (FeatureCollection)

Example request:

```json
{
  "collections": ["ks-hydrology-nwis"],
  "bbox": [-101.5, 36.9, -94.3, 40.0],
  "datetime": "2020-01-01T00:00:00Z/2020-12-31T23:59:59Z",
  "limit": 100
}
```

---

## 🧷 STAC lineage & diffs (KFM extensions)

### 🧪 GET `/api/v1/stac/items/{item_id}/lineage`

**Purpose:** Return predecessor/successor graph for an Item (version chain)  
**Auth:** public (governance applies)  
**Response:** `200 OK` (enveloped)

```json
{
  "data": {
    "current": { "item_id": "stac:item:abc", "version": "2026-01-01" },
    "predecessors": [],
    "successors": [],
    "latest": { "item_id": "stac:item:abc", "version": "2026-01-01" }
  },
  "meta": { "request_id": "req_x", "trace_id": "tr_x", "generated_at": "2026-01-08T00:00:00Z" },
  "governance": { "care_status": "public", "generalized": false, "redactions": [], "policy_version": "CARE-LOC-01@2026-01-01" },
  "provenance": { "prov_run_id": "prov:run:ol_7f3e", "prov_activity_id": "prov:activity:publish@ol_7f3e", "inputs": ["stac:item:abc@2025-12-31"], "hashes": {} },
  "links": [
    { "rel": "stac_item", "href": "/api/v1/stac/items/abc", "type": "application/json" }
  ]
}
```

---

### 🧪 GET `/api/v1/stac/items/{item_id}/diff?against={other_id}`

**Purpose:** Field/asset/geometry diff between two items/versions  
**Response:** `200 OK` (enveloped)

Diff MUST include:
- metadata deltas
- asset adds/removes/changed checksums
- geometry/bbox diffs (if allowed by governance)

---

## 📦 Assets

### ✅ GET `/api/v1/assets/{asset_id}`

**Purpose:** Asset metadata + governed download link info  
**Auth:** public (governance applies)  
**Response:** `200 OK` (enveloped)

Minimum fields:
- `asset_id`
- `type` (mime)
- `roles` (e.g., `data`, `thumbnail`, `tile`, `metadata`)
- `checksum` (sha256 or multihash)
- `size_bytes`
- `href` (logical) and/or `download_href` (signed/redirect)

---

### ✅ GET `/api/v1/assets/{asset_id}/download`

**Purpose:** Download (or redirect) asset bytes  
**Response:** `302 Found` (redirect) OR `200 OK` (stream)  
**Notes:**
- Must support Range requests for large artifacts when streaming.
- Must set caching headers appropriately for public assets.

---

### ✅ HEAD `/api/v1/assets/{asset_id}/download`

**Purpose:** Existence check & metadata headers  
**Response:** `200 OK` or `404 Not Found`

---

## 🗺️ Tiles & styles (MapLibre‑ready)

### ✅ GET `/api/v1/tilesets`

**Purpose:** List available tilesets (layers)  
**Auth:** public (governance applies)  
**Response:** `200 OK` (enveloped list)

Tileset metadata MUST include:
- `tileset_id`, `title`, `description`
- `bounds`, `minzoom`, `maxzoom`
- `format` (`pbf` or `pmtiles`)
- `time_support` (none / discrete / continuous)
- `stac_collection_id` link (if applicable)

---

### ✅ GET `/api/v1/tilesets/{tileset_id}`

**Purpose:** Describe one tileset  
**Response:** `200 OK`

---

### ✅ GET `/api/v1/tiles/{tileset_id}/{z}/{x}/{y}.pbf`

**Purpose:** Serve one vector tile  
**Response:** `200 OK` with `application/x-protobuf`

Query params (recommended):
- `t=` (RFC3339 or version id) — time slice
- `v=` (version lock token) — deterministic story state
- `fields=` — optional field gating

> [!IMPORTANT]
> If a tile is governed/generalized, the server MUST either:
> - serve the generalized tile, or
> - return 404/403 per policy (but never leak raw geometry)

---

### ✅ GET `/api/v1/styles/{style_id}.json`

**Purpose:** Mapbox Style JSON for MapLibre clients  
**Response:** `200 OK` (raw style JSON)

Style MUST reference:
- tile endpoints above
- glyph/sprite endpoints if used (optional)

---

## 🕸️ Graph (bounded REST)

> [!NOTE]
> GraphQL is preferred for flexible UI traversal, but REST provides a bounded, auditable subset.

### ✅ GET `/api/v1/graph/entities`

**Purpose:** Search entities  
**Auth:** public (governance applies)  
**Query params:**
- `type` (e.g., `Place`, `Event`, `Layer`, `Document`, `StoryNode`, `Sensor`)
- `q` (name/title search)
- `bbox` (optional spatial filter)
- `datetime` (optional temporal filter)
- pagination

**Response:** `200 OK` (enveloped list)

---

### ✅ GET `/api/v1/graph/entities/{entity_id}`

**Purpose:** Fetch entity detail  
**Response:** `200 OK`

Entity SHOULD include:
- stable identifiers
- minimal properties
- `links` to related STAC items, datasets, sources
- governance + provenance metadata

---

### ✅ GET `/api/v1/graph/entities/{entity_id}/neighbors`

**Purpose:** Fetch bounded neighbors (typed + depth limited)  
**Query params:**
- `rel` (repeatable) — allow-listed relationship types
- `max_depth` (default 1, max 3)
- `max_nodes` (default 100, max 500)

**Response:** `200 OK`

---

### 🧪 POST `/api/v1/graph/query`

**Purpose:** Run a saved/templated query (NO raw Cypher)  
**Auth:** contributor+  
**Request:**

```json
{
  "query_id": "place_timeline_v1",
  "params": { "place_id": "place:fort-hays", "limit": 50 }
}
```

**Response:** `200 OK`

---

## 🎬 Story Nodes

Story Nodes are **curated narrative states** that bind:
- camera/story config (2D/3D transitions)
- layer toggles + time windows
- citations + provenance pointers
- version locks for reproducibility

### ✅ GET `/api/v1/story-nodes`

**Purpose:** List Story Nodes  
**Query params:**
- `q`, `tag`, `bbox`, `datetime`
- pagination

---

### ✅ GET `/api/v1/story-nodes/{story_id}`

**Purpose:** Fetch Story Node definition  
**Response:** `200 OK`

Recommended fields:
- `story_id`, `title`, `summary`
- `config` (camera, UI state, layer bindings)
- `version_lock` (optional)
- `citations[]`
- `stac_refs[]`, `graph_refs[]`

---

### 🧪 POST `/api/v1/story-nodes`

**Purpose:** Create Story Node (governed write)  
**Auth:** contributor+  
**Idempotency-Key:** MUST  
**Response:** `201 Created`

---

### 🧪 PATCH `/api/v1/story-nodes/{story_id}`

**Purpose:** Update Story Node (controlled)  
**Auth:** contributor+  
**Response:** `200 OK`  
**Notes:** Must preserve audit trail (who/when/why). Prefer append-only revision model.

---

## 🧠 Focus Mode (explainability-first)

Focus Mode returns a **Focus Packet**: summary + citations + provenance, suitable for UI “Focus drawer” and report exports.

### ✅ POST `/api/v1/analysis/focus`

**Purpose:** Generate a Focus Packet  
**Auth:** public or contributor depending on policy  
**Headers:**
- `Prefer: respond-async` (optional; recommended)

**Request:**

```json
{
  "question": "What changed in this region between 1860 and 1880?",
  "bbox": [-100.5, 38.0, -99.0, 39.0],
  "datetime": "1860-01-01/1880-12-31",
  "entities": ["place:fort-hays"],
  "constraints": {
    "max_sources": 12,
    "max_tokens": 1200,
    "citation_required": true
  },
  "version_lock": {
    "stac_item_ids": ["stac:item:abc@2026-01-01"],
    "graph_snapshot": "graph:snapshot:2026-01-01"
  }
}
```

**Response modes:**
- `200 OK` with packet (sync)
- `202 Accepted` with `job_id` (async)

Async response:

```json
{
  "data": { "job_id": "focus_job_123", "status": "queued" },
  "meta": { "request_id": "req_x", "trace_id": "tr_x", "generated_at": "2026-01-08T00:00:00Z" },
  "governance": { "care_status": "public", "generalized": false, "redactions": [], "policy_version": "CARE-LOC-01@2026-01-01" },
  "provenance": { "prov_run_id": null, "prov_activity_id": null, "inputs": [], "hashes": {} },
  "links": [
    { "rel": "status", "href": "/api/v1/analysis/focus/jobs/focus_job_123", "type": "application/json" }
  ]
}
```

---

### ✅ GET `/api/v1/analysis/focus/jobs/{job_id}`

**Purpose:** Poll job status  
**Response:** `200 OK`

Statuses: `queued | running | succeeded | failed | canceled`

---

### ✅ GET `/api/v1/analysis/focus/jobs/{job_id}/result`

**Purpose:** Retrieve final Focus Packet  
**Response:** `200 OK`

Minimum fields:
- `summary_markdown`
- `citations[]` (each must include stable source reference)
- `provenance` pointers to retrieval run
- `governance.redactions[]` if applied

---

## 🧪 Simulations (ABM/DES/etc.)

Simulations are async and MUST be reproducible.

### ✅ POST `/api/v1/simulations/abm`

**Purpose:** Submit simulation job  
**Auth:** contributor+ (or public in sandbox mode)  
**Idempotency-Key:** MUST  
**Request:**

```json
{
  "scenario_id": "scenario:ks-frontier:settlement_pressure_v1",
  "bbox": [-101.0, 37.0, -94.5, 40.0],
  "datetime": "1860-01-01/1880-12-31",
  "seed": 123456,
  "replicates": 10,
  "parameters": {
    "migration_rate": 0.12,
    "resource_weight": 0.8
  },
  "outputs": {
    "publish_stac": true,
    "tileset": true
  }
}
```

**Response:** `202 Accepted`

---

### ✅ GET `/api/v1/simulations/jobs/{job_id}`

**Purpose:** Job state + links  
**Response:** `200 OK`

Job MUST include:
- parameters snapshot hash
- model version
- seed/replicate info
- `links.results`, `links.logs`, `links.prov`

---

### ✅ GET `/api/v1/simulations/jobs/{job_id}/results`

**Purpose:** Results bundle  
**Response:** `200 OK`

Results SHOULD include:
- STAC Items produced (if any)
- asset refs (GeoParquet/COGs/PMTiles)
- summary metrics (with uncertainty where applicable)

---

### ✅ POST `/api/v1/simulations/jobs/{job_id}/cancel`

**Purpose:** Cancel job  
**Response:** `202 Accepted` or `409 Conflict` if already terminal

---

## 📈 Time Series (stations + series)

Designed for hydrology/air/etc. pipelines publishing normalized `timeseries.parquet` + quick JSON slices for UI charts.

### ✅ GET `/api/v1/timeseries/stations`

**Purpose:** List stations/sensors  
**Query params:**
- `provider` (e.g., `usgs_nwis`, `epa_aqs`, `purpleair`)
- `bbox`
- `q`
- pagination

---

### ✅ GET `/api/v1/timeseries/stations/{station_id}`

**Purpose:** Station metadata + series inventory  
**Response:** `200 OK`

---

### ✅ GET `/api/v1/timeseries/series`

**Purpose:** Fetch a time slice (chart-friendly)  
**Query params:**
- `station_id` (required)
- `parameter` (required; provider-specific code, e.g., `00060`, `00065`)
- `datetime` (range; required)
- `aggregate` (optional: `raw|hour|day|month`)
- `format` (optional: `json|ndjson`)

**Response:** `200 OK` (enveloped)

Example response:

```json
{
  "data": {
    "station_id": "usgs:06892350",
    "parameter": "00060",
    "unit": "cfs",
    "datetime": "2025-01-01T00:00:00Z/2025-01-02T00:00:00Z",
    "points": [
      ["2025-01-01T00:00:00Z", 153.2],
      ["2025-01-01T01:00:00Z", 151.9]
    ],
    "assets": [
      {
        "role": "columnar",
        "asset_id": "asset:timeseries:parquet:run123",
        "href": "/api/v1/assets/asset:timeseries:parquet:run123"
      }
    ]
  },
  "meta": { "request_id": "req_x", "trace_id": "tr_x", "generated_at": "2026-01-08T00:00:00Z", "paging": { "next_cursor": null, "count": 2 }, "warnings": [] },
  "governance": { "care_status": "public", "generalized": false, "redactions": [], "policy_version": "CARE-LOC-01@2026-01-01" },
  "provenance": { "prov_run_id": "prov:run:ol_7f3e", "prov_activity_id": "prov:activity:normalize@ol_7f3e", "inputs": ["raw:usgs:nwis:..."], "hashes": { "timeseries.parquet": "sha256:..." } },
  "links": []
}
```

---

### 🧪 POST `/api/v1/timeseries/query`

**Purpose:** Multi-series fetch (batch)  
**Auth:** public (bounded)  
**Request:** list of (station_id, parameter, datetime)

---

## 🧬 Provenance (runs, SBOM, attestations)

Provenance is a first-class API. Runs may be backed by PROV‑O, OpenLineage, or both.

### ✅ GET `/api/v1/prov/runs/{run_id}`

**Purpose:** Run summary (links to artifacts)  
**Response:** `200 OK`

Example:

```json
{
  "data": {
    "run_id": "ol_7f3e",
    "backend": "openlineage",
    "status": "succeeded",
    "started_at": "2026-01-01T06:30:12Z",
    "ended_at": "2026-01-01T06:31:40Z",
    "links": {
      "prov_jsonld": "/api/v1/prov/runs/ol_7f3e/prov.jsonld",
      "attestation": "/api/v1/prov/runs/ol_7f3e/attestation.json",
      "sbom": "/api/v1/prov/runs/ol_7f3e/sbom.spdx.json",
      "manifest": "/api/v1/prov/runs/ol_7f3e/manifest.json",
      "logs": "/api/v1/prov/runs/ol_7f3e/logs"
    }
  },
  "meta": { "request_id": "req_x", "trace_id": "tr_x", "generated_at": "2026-01-08T00:00:00Z" },
  "governance": { "care_status": "public", "generalized": false, "redactions": [], "policy_version": "CARE-LOC-01@2026-01-01" },
  "provenance": { "prov_run_id": "prov:run:ol_7f3e", "prov_activity_id": "prov:activity:run@ol_7f3e", "inputs": [], "hashes": {} },
  "links": []
}
```

---

### ✅ GET `/api/v1/prov/runs/{run_id}/prov.jsonld`

**Purpose:** Raw PROV JSON‑LD document  
**Response:** `200 OK` raw JSON‑LD

---

### ✅ GET `/api/v1/prov/runs/{run_id}/manifest.json`

**Purpose:** Artifact manifest (hashes, paths, sizes)  
**Response:** `200 OK`

---

### ✅ GET `/api/v1/prov/runs/{run_id}/sbom.spdx.json`

**Purpose:** SBOM for the pipeline/runtime used  
**Response:** `200 OK`

---

### ✅ GET `/api/v1/prov/runs/{run_id}/attestation.json`

**Purpose:** Supply chain attestation (signatures, SLSA-ish claims)  
**Response:** `200 OK`

---

## 📦 Releases (mirrored bundles)

Releases bundle **manifests + SBOM + telemetry** for reproducible “as‑shipped” states.

### 🧪 GET `/api/v1/releases`

**Purpose:** List releases  
**Response:** `200 OK`

---

### 🧪 GET `/api/v1/releases/{version}`

**Purpose:** Release descriptor  
**Response:** `200 OK`

Recommended links:
- `sbom_ref`
- `manifest_ref`
- `telemetry_ref`

---

### 🧪 GET `/api/v1/releases/{version}/manifest.zip`

**Purpose:** Download release manifest bundle  
**Response:** `200/302`

---

### 🧪 GET `/api/v1/releases/{version}/sbom.spdx.json`

**Purpose:** Download release SBOM  
**Response:** `200`

---

### 🧪 GET `/api/v1/releases/{version}/focus-telemetry.json`

**Purpose:** Download release telemetry snapshot  
**Response:** `200`

---

## 📡 Telemetry

### ✅ POST `/api/v1/telemetry/events`

**Purpose:** Ingest telemetry events (UI + pipelines)  
**Auth:** public or contributor depending on deployment  
**Idempotency-Key:** SHOULD (for batches)  
**Request:**

```json
{
  "schema": "kfm-telemetry@v3",
  "events": [
    {
      "ts": "2026-01-08T00:00:00Z",
      "type": "focus_opened",
      "actor": { "anon_id": "a_123", "role": "public" },
      "context": { "story_id": "story:ks-from-above", "feature_id": "place:fort-hays" }
    }
  ]
}
```

**Response:** `202 Accepted`

---

### 🧪 GET `/api/v1/telemetry/snapshots/latest`

**Purpose:** Read latest merged dashboard snapshot  
**Auth:** maintainer/auditor (recommended)  
**Response:** `200 OK`

---

## 🔔 Hooks (automation triggers)

### 🧪 POST `/api/v1/hooks/{source}`

**Purpose:** Inbound trigger endpoint (ingest/refresh/build)  
**Auth:** signed payload required  
**Idempotency-Key:** MUST (or derived stable event id)  
**Response:** `202 Accepted`

Hard rules:
- validate signature
- validate schema
- dedupe by idempotency key
- bounded retries + DLQ handling

---

# 🧪 Contract tests & CI expectations

Minimum CI gates for REST contract changes:

- ✅ OpenAPI lint + drift check
- ✅ Example payloads validated against schemas
- ✅ Governance tests (redaction/generalization)
- ✅ Determinism tests (stable sort + pagination replay)
- ✅ Provenance link integrity tests (manifest hashes resolvable)

---

# 📂 Repo layout for REST specs (emoji‑annotated)

~~~text
📂 docs/specs/api/
├── 📄 README.md                          # Index + rules + governance invariants
├── 🧾 openapi.yaml                       # Canonical REST contract (machine‑readable)
├── 🧾 API__REST_CONTRACT.md              # This file (semantics + invariants)
├── 🧬 graphql/
│   ├── 📜 schema.graphql                 # Canonical GraphQL schema
│   └── 🧩 operations/                    # Saved operations (allow‑listed)
├── 🧪 examples/
│   ├── 📤 requests/                      # Example request payloads
│   └── 📥 responses/                     # Example responses (golden files)
├── 🧷 schemas/
│   ├── 🧱 api/                           # JSON Schemas: envelopes, errors, jobs
│   ├── 🛰️ stac/                          # STAC profiles + extensions (kfm‑*)
│   └── 📡 telemetry/                     # Telemetry schemas (focus‑telemetry.json)
└── 🧰 tests/
    ├── ✅ contract/                      # REST/GraphQL contract tests
    └── 🛡️ governance/                    # Redaction + policy gate tests
~~~

---

# 📚 Design reference shelf (project files)

These project files influence the REST contract’s priorities (reproducibility, bounded compute, governance, map delivery, statistical rigor). They are **non‑normative** to the contract (the contract is the API behavior), but they shape the requirements.

<details>
<summary><strong>📚 Expand list</strong></summary>

### 🧠 Architecture & platform behavior
- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx`
- 📄 `Latest Ideas.docx`
- 📄 `Other Ideas.docx`

### 🗺️ Geospatial & mapping delivery
- 📘 `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- 📘 `python-geospatial-analysis-cookbook.pdf`
- 📘 `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- 📘 `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- 📘 `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`

### 🧱 Web delivery & rendering constraints
- 📘 `responsive-web-design-with-html5-and-css3.pdf`
- 📘 `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- 📘 `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 🧪 Modeling, simulation, statistics & uncertainty
- 📘 `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- 📘 `Generalized Topology Optimization for Structural Design.pdf`
- 📘 `Understanding Statistics & Experimental Design.pdf`
- 📘 `regression-analysis-with-python.pdf`
- 📘 `Regression analysis using Python - slides-linear-regression.pdf`
- 📘 `graphical-data-analysis-with-r.pdf`
- 📘 `think-bayes-bayesian-statistics-in-python.pdf`
- 📘 `Spectral Geometry of Graphs.pdf`

### ⚖️ Governance & human-centered constraints
- 📘 `Introduction to Digital Humanism.pdf`
- 📘 `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- 📘 `Principles of Biological Autonomy - book_9780262381833.pdf`

### 🔐 Security, reliability, concurrency
- 📘 `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- 📘 `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`
- 📘 `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`
- 📘 `Scalable Data Management for Future Hardware.pdf`
- 📘 `Data Spaces.pdf`

### 🧰 Programming reference compendia (GoalKicker sets)
- 📘 `A programming Books.pdf`
- 📘 `B-C programming Books.pdf`
- 📘 `D-E programming Books.pdf`
- 📘 `F-H programming Books.pdf`
- 📘 `I-L programming Books.pdf`
- 📘 `M-N programming Books.pdf`
- 📘 `O-R programming Books.pdf`
- 📘 `S-T programming Books.pdf`
- 📘 `U-X programming Books.pdf`

</details>

---

## ✅ Definition of Done for REST contract changes

- [ ] `openapi.yaml` updated and validated
- [ ] This contract updated (semantics/invariants)
- [ ] Examples + schemas updated
- [ ] Contract tests updated
- [ ] Governance tests pass (FAIR+CARE + redaction)
- [ ] Provenance links resolvable (manifest + hashes)
- [ ] Determinism verified (sorting/pagination replay)

---

<div align="center">

🔗 **Next:** Implement `openapi.yaml` tags to mirror the endpoint groups above.

</div>

