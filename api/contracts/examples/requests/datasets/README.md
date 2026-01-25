# 📦 Datasets — Request Examples (API Contracts)

![Contracts](https://img.shields.io/badge/contracts-OpenAPI%20%2B%20GraphQL-2ea44f)
![Standards](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-blue)
![Geospatial](https://img.shields.io/badge/geospatial-PostGIS%20%2B%20MVT%20%2B%20GeoJSON-8a2be2)
![Governance](https://img.shields.io/badge/governance-OPA%20%2B%20Policy%20Pack-orange)
![Clients](https://img.shields.io/badge/clients-UI%20%7C%20Mobile%20%7C%20AR%20%7C%20Notebooks-lightgrey)

> [!TIP]
> This folder is **copy/paste-ready** request examples for **dataset discovery**, **dataset metadata**, and **dataset access** (downloads, subsets, and tiles).  
> Everything here assumes KFM’s “**contract-first + evidence-first**” stance: if a dataset exists, you can also find its **STAC/DCAT/PROV** trail. 🧾🧭

---

## 📁 Where you are (folder map)

```text
api/
  contracts/
    examples/
      requests/
        datasets/
          README.md   👈 you are here
          # (recommended) 00_list_datasets.http
          # (recommended) 01_get_dataset_metadata.http
          # (recommended) 02_get_dataset_data_subset.http
          # (recommended) 03_list_place_datasets.http
          # (recommended) 04_get_vector_tile.http
          # (recommended) 05_graphql_dataset_query.http
```

---

## 🎯 What these examples are for

KFM is built so that **the UI (2D/3D maps + timeline)**, **Focus Mode**, **mobile/offline**, and future **AR/VR** clients all pull from the **same governed API surface**.

These request examples support common product flows:

- 🗺️ **Layer discovery** for the map layer panel / search
- ⏳ **Temporal filtering** (timeline slider / date range)
- 📌 **Place-driven exploration** (graph-linked datasets for a place)
- 🧾 **Provenance + citations** (Focus Mode / “map behind the map”)
- 🧱 **High-performance rendering** via **vector tiles** (MVT)
- 🧠 **Advanced joins** via **GraphQL** (graph + catalog together)

---

## ⚙️ Quick start (environment variables)

Set these once and reuse in every example:

```bash
export KFM_BASE_URL="http://localhost:8000"

# Many docs use endpoints like /datasets/{id}; some deployments prefix routes with /api or /api/v1.
# Set this to whatever your OpenAPI contract defines:
export KFM_API_PREFIX="/api"   # try: ""  or "/api" or "/api/v1"

# Optional (if your endpoint requires auth)
export KFM_TOKEN="REPLACE_ME"
```

Helper:

```bash
kfm() { curl -sS -H "Authorization: Bearer ${KFM_TOKEN}" "$@"; }
```

---

## 🧾 Common headers (recommended)

| Header | Why |
|---|---|
| `Accept: application/json` | Default metadata responses |
| `Accept: application/geo+json` | Vector feature subsets |
| `Accept: application/vnd.mapbox-vector-tile` | MVT tiles (`.pbf`) |
| `Authorization: Bearer …` | Required for restricted/sensitive datasets |
| `X-Request-Id: <uuid>` | Traceability + audit correlation |
| `If-None-Match: "<etag>"` | Client caching for catalog + metadata |

> [!NOTE]
> KFM is designed so **clients never talk directly to PostGIS/Neo4j**. All access goes through the API boundary so redaction + classification can be enforced. 🔒

---

## 🆔 ID conventions (dataset + place)

### Dataset IDs
You’ll commonly see dataset IDs like:

- `kfm.ks.landcover.2000_2020.v1` (example used throughout)

> [!TIP]
> Treat dataset IDs as **stable public identifiers**. If a dataset changes materially, bump the version suffix (`v1 → v2`) rather than silently rewriting.

### Place IDs
Graph endpoints typically use a stable place identifier (examples):
- `place:ks:topeka`
- `place:ks:wichita`
- `place:county:seward-ks`

(Exact formats depend on your graph ontology + contract.)

---

## 🧭 Example index (most-used requests)

| Use case | Endpoint | Example file (suggested) |
|---|---|---|
| List datasets | `GET {{API}}/datasets` | `00_list_datasets.http` |
| Dataset metadata | `GET {{API}}/datasets/{id}` | `01_get_dataset_metadata.http` |
| Download / subset | `GET {{API}}/datasets/{id}/data` | `02_get_dataset_data_subset.http` |
| Datasets for a place | `GET {{API}}/graph/places/{placeId}/datasets` | `03_list_place_datasets.http` |
| Vector tile | `GET {{API}}/tiles/{layer}/{z}/{x}/{y}.pbf` | `04_get_vector_tile.http` |
| GraphQL dataset query | `POST {{GQL}}/graphql` | `05_graphql_dataset_query.http` |

Where:
- `{{API}} = ${KFM_BASE_URL}${KFM_API_PREFIX}`
- `{{GQL}}` is often the same base, unless GraphQL is hosted separately.

---

# ✅ Request Examples

## 00) List datasets (catalog discovery) 📚

### HTTP (VS Code REST Client style)

```http
@baseUrl = {{KFM_BASE_URL}}{{KFM_API_PREFIX}}

GET {{baseUrl}}/datasets?limit=25
Accept: application/json
Authorization: Bearer {{KFM_TOKEN}}
X-Request-Id: {{$guid}}
```

### cURL

```bash
curl -sS \
  -H "Accept: application/json" \
  -H "Authorization: Bearer ${KFM_TOKEN}" \
  "${KFM_BASE_URL}${KFM_API_PREFIX}/datasets?limit=25"
```

**Notes**
- Prefer cursor pagination if available (`cursor=...`).
- Your OpenAPI contract may expose this as `/api/datasets` instead (same idea). 👍

---

## 01) Get dataset metadata (DCAT + links to STAC/PROV) 🧾

### HTTP

```http
@baseUrl = {{KFM_BASE_URL}}{{KFM_API_PREFIX}}
@datasetId = kfm.ks.landcover.2000_2020.v1

GET {{baseUrl}}/datasets/{{datasetId}}
Accept: application/json
Authorization: Bearer {{KFM_TOKEN}}
X-Request-Id: {{$guid}}
```

### cURL

```bash
curl -sS \
  -H "Accept: application/json" \
  -H "Authorization: Bearer ${KFM_TOKEN}" \
  "${KFM_BASE_URL}${KFM_API_PREFIX}/datasets/kfm.ks.landcover.2000_2020.v1"
```

**What you should expect in the response**
- Enough metadata for UI attribution (“Source: …”, license, description)
- Links/distributions to:
  - 🗂️ STAC Collection / Items
  - 🧬 PROV bundle (lineage)
  - 📦 Distribution(s): download URL, tile URL, query URL, etc.

---

## 02) Get dataset data (download OR subset) ⬇️🧩

### 02a) Download / stream as GeoJSON

```bash
curl -L \
  -H "Accept: application/geo+json" \
  -H "Authorization: Bearer ${KFM_TOKEN}" \
  "${KFM_BASE_URL}${KFM_API_PREFIX}/datasets/kfm.ks.landcover.2000_2020.v1/data?format=geojson"
```

### 02b) Spatial + temporal subset (recommended for UI + notebooks)

```bash
curl -L \
  -H "Accept: application/geo+json" \
  -H "Authorization: Bearer ${KFM_TOKEN}" \
  "${KFM_BASE_URL}${KFM_API_PREFIX}/datasets/kfm.ks.landcover.2000_2020.v1/data?format=geojson&bbox=-100.5,37.0,-99.5,38.0&time=2010-01-01/2010-12-31&limit=5000"
```

### 02c) CSV export (for tabular layers)

```bash
curl -L \
  -H "Accept: text/csv" \
  -H "Authorization: Bearer ${KFM_TOKEN}" \
  "${KFM_BASE_URL}${KFM_API_PREFIX}/datasets/kfm.ks.landcover.2000_2020.v1/data?format=csv&limit=10000"
```

> [!IMPORTANT]
> Subsetting is where governance matters most: redaction/aggregation may apply for sensitive datasets. Always assume the API enforces policy before returning rows/features. 🛡️

---

## 03) List datasets linked to a place (graph + catalog bridge) 🧠📍

```bash
curl -sS \
  -H "Accept: application/json" \
  -H "Authorization: Bearer ${KFM_TOKEN}" \
  "${KFM_BASE_URL}${KFM_API_PREFIX}/graph/places/place:ks:topeka/datasets"
```

**Why this exists**
- The UI can pivot from a place → datasets → layers/stories.
- Focus Mode can pull “what’s relevant here?” via graph relationships.

---

## 04) Get vector tiles (fast map rendering) 🧱🗺️

Example shown in docs as a landcover tile endpoint:

```bash
curl -sS \
  -H "Accept: application/vnd.mapbox-vector-tile" \
  "${KFM_BASE_URL}${KFM_API_PREFIX}/tiles/landcover/6/15/25.pbf?year=1936" \
  -o landcover_z6_x15_y25_1936.pbf
```

**Notes**
- MVT endpoints usually take `{z}/{x}/{y}` plus optional filters like `year=`.
- Tiles are designed for MapLibre GL JS usage (client renders in WebGL).

---

## 05) GraphQL dataset query (one request, richer joins) 🧠🔎

GraphQL is ideal when you want metadata + related nodes + provenance references in one response.

```bash
curl -sS \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${KFM_TOKEN}" \
  "${KFM_BASE_URL}${KFM_API_PREFIX}/graphql" \
  -d '{
    "query": "query DatasetWithEvidence($id: ID!) { dataset(id: $id) { id title description stacCollection { id extent { spatial temporal } } provenance { generatedAtTime } } }",
    "variables": { "id": "kfm.ks.landcover.2000_2020.v1" }
  }'
```

> [!NOTE]
> Expect guardrails: max depth, pagination requirements, and query complexity limits to avoid expensive graph traversals.

---

# 📦 Response Shape Cheat Sheet (what the UI expects)

> [!TIP]
> This is **not** a full schema — just the “shape you’ll usually see” so you can sanity-check results.

```json
{
  "id": "kfm.ks.landcover.2000_2020.v1",
  "title": "Kansas Landcover 2000–2020",
  "description": "Landcover classification across Kansas over time.",
  "keywords": ["landcover", "environment", "classification"],
  "license": "CC-BY-4.0",
  "spatial": { "bbox": [-102.051, 36.993, -94.588, 40.003], "crs": "EPSG:4326" },
  "temporal": { "start": "2000-01-01", "end": "2020-12-31" },

  "links": [
    { "rel": "stac-collection", "href": "/catalog/stac/collections/kfm.ks.landcover.2000_2020.v1" },
    { "rel": "prov", "href": "/catalog/prov/kfm.ks.landcover.2000_2020.v1.jsonld" },
    { "rel": "dcat", "href": "/catalog/dcat/kfm.ks.landcover.2000_2020.v1.json" }
  ],

  "distributions": [
    { "type": "subset", "mediaType": "application/geo+json", "href": "/datasets/kfm.ks.landcover.2000_2020.v1/data?format=geojson" },
    { "type": "tiles", "mediaType": "application/vnd.mapbox-vector-tile", "href": "/tiles/landcover/{z}/{x}/{y}.pbf" }
  ],

  "governance": {
    "classification": "public",
    "notes": "May be generalized for privacy or sovereignty rules when needed."
  }
}
```

---

# ❗ Error Envelope (recommended contract pattern)

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Dataset not found: kfm.ks.landcover.2000_2020.v1",
    "request_id": "7b6b9e5c-5f5d-4b72-9c2c-1f3c4fd62c3a"
  }
}
```

Common HTTP codes:
- `200` OK
- `206` Partial Content (range/streaming)
- `400` Bad Request (invalid bbox/time)
- `401` Unauthorized / missing token
- `403` Forbidden (policy denies)
- `404` Not Found
- `409` Conflict (versioning / state mismatch)
- `422` Validation Error (schema/params)

---

# 🛡️ Governance notes (why some requests “don’t return everything”)

KFM treats governance as a **first-class contract requirement**, not a UI afterthought:

- 🧾 **No dataset without evidence** (STAC/DCAT/PROV aligned)
- 🚫 **No “mystery layers”** (unsourced layers don’t ship)
- 🔒 **Policy enforcement at the API** (redaction happens before data leaves the server)
- 🧪 **Deterministic + logged pipelines** (reproducible outputs)

---

# 🚧 Roadmap / Proposed request examples (optional, but useful)

These are consistent with KFM’s roadmap docs. Add these once the contracts exist in OpenAPI/GraphQL.

## A) Offline “data packs” for field use 📦📴
**Goal:** download a region’s datasets/stories ahead of time (mobile / field work).

```http
POST {{baseUrl}}/packs
Content-Type: application/json
Authorization: Bearer {{KFM_TOKEN}}

{
  "bbox": [-100.5, 37.0, -99.5, 38.0],
  "time": "1930-01-01/1940-12-31",
  "datasets": ["kfm.ks.landcover.2000_2020.v1"],
  "include": ["stac", "prov", "stories"],
  "format": "pmtiles+manifest"
}
```

## B) Dataset snapshot as OCI artifact 🧊📦
**Goal:** immutable dataset bundles with checksums/signatures.

```http
GET {{baseUrl}}/datasets/{{datasetId}}/artifacts
Accept: application/json
Authorization: Bearer {{KFM_TOKEN}}
```

## C) AR “what’s here?” query 👓📍
**Goal:** AR clients query by device position/orientation and get relevant layers + citations.

```http
GET {{baseUrl}}/discover/relevant?lat=39.0558&lon=-95.6890&radius_m=500&time=1935-01-01/1935-12-31
Accept: application/json
Authorization: Bearer {{KFM_TOKEN}}
```

---

# 🧩 Adding a new request example (definition of done)

✅ When you add a new example in this folder:

- [ ] The endpoint exists in **OpenAPI** and/or **GraphQL schema**
- [ ] Example includes **Auth + Accept headers** (when applicable)
- [ ] Example includes **spatial + temporal params** (when applicable)
- [ ] Example mentions **expected provenance hooks** (links or evidence IDs)
- [ ] Any new dataset exposure respects **policy pack** rules
- [ ] Example is runnable with `curl` or `.http` client

---

# 🔗 Related docs (in-repo)

If these paths exist in your repo, they’re your best companions:

- `docs/MASTER_GUIDE_v13.md` 🧭
- `docs/standards/KFM_STAC_PROFILE.md` 🗂️
- `docs/standards/KFM_DCAT_PROFILE.md` 🧾
- `docs/standards/KFM_PROV_PROFILE.md` 🧬
- `api/scripts/policy/README.md` 🛡️
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` 🧩

---

<details>
  <summary><strong>📚 Reference shelf (project library PDFs / portfolios)</strong></summary>

These files live in the project library and are useful when implementing clients, pipelines, or performance work:

- 🤖 **AI Concepts & more** (portfolio) — reference docs for RAG/LLMs/modeling
- 🌍 **Maps / Google Maps / Virtual Worlds / Geospatial WebGL** (portfolio) — WebGL, cartography, 3D/VR concepts
- 🧰 **Various programming languages & resources** (portfolio) — CI/CD, DB performance, geoprocessing, etc.
- 🗄️ **Data Management / Theories / Architectures / Data Science / Bayesian** (portfolio) — architecture patterns + data engineering

Recommended “grab-first” items from the portfolios (examples):
- `geoprocessing-with-python` 🐍🗺️
- `webgl-programming-guide` 🧊🎮
- `Google Earth Engine Applications` 🌎
- `Database Performance at Scale` ⚡
- `Designing Data-Intensive Applications` 🧱

</details>
