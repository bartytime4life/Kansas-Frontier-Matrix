# 📦 Datasets API — Response Examples (v1)

![API](https://img.shields.io/badge/API-v1-blue)
![Contracts](https://img.shields.io/badge/Contracts-Contract--First-success)
![Provenance](https://img.shields.io/badge/Provenance-STAC%20%7C%20DCAT%20%7C%20PROV-orange)
![Formats](https://img.shields.io/badge/Formats-GeoJSON%20%7C%20GeoParquet%20%7C%20MVT%20%7C%20COG%20%7C%203D%20Tiles-informational)

> 🧭 This folder is the “golden sample set” for **dataset-related API responses** (v1).  
> These examples exist so **UI (MapLibre/Cesium)** + **Focus Mode** + **CI** can rely on stable, provenance-rich payloads — with **no mystery layers** ✅

---

## 🗂️ Folder contents

> 📌 **Tip:** keep filenames boring + predictable. The *schema* defines what is valid; these examples define what “good” looks like.

```text
📁 api/contracts/examples/responses/v1/datasets/
├─ ✅ README.md
├─ ✅ datasets.list.ok.json
├─ ✅ datasets.get.ok.json
├─ ✅ datasets.data.geojson.ok.json
├─ ✅ datasets.data.download.ok.json
├─ ✅ datasets.tilejson.ok.json
└─ ✅ errors.dataset_not_found.json
```

---

## 🎯 Endpoints covered (v1)

| Endpoint | Purpose | Example(s) in this folder |
|---|---|---|
| `GET /v1/datasets` | List datasets (catalog UI, search results grouping, layer panel) | `datasets.list.ok.json` |
| `GET /v1/datasets/{dataset_id}` | Dataset detail (metadata, provenance, access rules, distributions, tile templates) | `datasets.get.ok.json` |
| `GET /v1/datasets/{dataset_id}/data` | Retrieve actual data (GeoJSON or download link when too large) | `datasets.data.geojson.ok.json`, `datasets.data.download.ok.json` |
| `GET /v1/datasets/{dataset_id}/tilejson` | Tile metadata for MapLibre/Cesium clients (URL template, min/max zoom, bounds) | `datasets.tilejson.ok.json` |
| Errors | Contracted error shapes | `errors.dataset_not_found.json` |

> 🧩 Related but **not in this folder**: endpoints like `/v1/features/{dataset_id}`, `/v1/search`, and raw tile paths like `/tiles/{layer}/{z}/{x}/{y}.pbf` (those belong in their own example directories, but **datasets responses must link to them**).

---

## 🧱 Design rules (non-negotiables)

### 1) ✅ Contract-first
- Responses are treated as a **public contract** (Pydantic/OpenAPI + JSON Schemas).
- If you change a response shape, you must:
  - update the schema,
  - update these examples,
  - and pass validation in CI.

### 2) 🧾 Provenance-first (no “mystery layers”)
Every dataset response must include **links** (or IDs) to the provenance triplet:
- 🗺️ **STAC** (spatiotemporal assets & collections)
- 🗃️ **DCAT** (dataset catalog entry: title/license/source/extent)
- 🧬 **PROV** (what happened to produce it: entities/activities/agents)

### 3) 🗺️ Geo truth + catalog truth + graph truth
> “PostGIS stores geo truth (vectors/rasters), Catalogs describe the assets, Graph links the context.”

These examples assume:
- the API serves **queryable geodata** (GeoJSON/MVT/tiles/downloads),
- but **metadata + governance** are anchored in the catalogs and provenance.

---

## 🧩 Shared primitives (what every response should “feel like”)

### 🆔 Dataset IDs
Use stable IDs that are:
- globally unique within KFM
- human-readable
- version-aware

**Recommended pattern:**
`kfm.{region}.{domain}.{dataset_name}.v{major}`  
Example: `kfm.ks.hydro.usgs_stream_gauges.v1`

### 🌍 Spatial reference + bounds
- Default **CRS** for API-facing metadata is **WGS84 (EPSG:4326)**.
- `bbox` uses `[minLon, minLat, maxLon, maxLat]`.

### ⏱ Time as a first-class filter
- Use ISO 8601 / RFC 3339 timestamps.
- Datasets should declare if they support `time` queries and how (range vs slices).

### 🔐 Sensitivity + access controls
- Every dataset must declare sensitivity and any access controls.
- If sensitive:
  - omit entirely (for unauthorized users), **or**
  - return generalized/aggregated geometry (e.g., hex bins instead of points).

### 📦 Distributions (formats you can actually use)
Common KFM-friendly outputs you’ll see linked from dataset responses:
- **GeoJSON** (default interchange)
- **GeoParquet** (big vector / analytics-friendly)
- **PMTiles / MVT** (fast map rendering)
- **COG** (big rasters, range requests)
- **3D Tiles / CZML** (Cesium + 3D/AR use cases)

---

## 🧾 Response envelopes

### ✅ JSON responses (list/detail/download/tilejson)
These examples use a consistent top-level shape:

```json
{
  "meta": { "api_version": "v1", "generated_at": "..." },
  "data": { },
  "links": { }
}
```

### ✅ GeoJSON responses (`/data` when returning features)
GeoJSON is returned as a standard `FeatureCollection`, with a **KFM extension** field for metadata:

```json
{
  "type": "FeatureCollection",
  "features": [],
  "kfm": {
    "api_version": "v1",
    "dataset_id": "kfm.ks.hydro.usgs_stream_gauges.v1",
    "generated_at": "..."
  }
}
```

> ✅ GeoJSON allows extra top-level members; clients that don’t care can ignore `kfm`.

---

## 🧪 Example payloads (inline)

<details>
<summary><strong>✅ Example: GET /v1/datasets</strong> <em>(datasets.list.ok.json)</em></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "generated_at": "2026-01-24T00:00:00Z",
    "pagination": { "page": 1, "page_size": 2, "total": 2 }
  },
  "data": [
    {
      "dataset_id": "kfm.ks.hydro.usgs_stream_gauges.v1",
      "title": "USGS Real-time Stream Gauges (Kansas)",
      "description": "Latest gauge readings served as GeoJSON points; historical time-series available via time filter.",
      "themes": ["hydrology", "realtime", "rivers"],
      "geometry_type": "Point",
      "spatial": { "bbox": [-102.05, 36.99, -94.60, 40.00], "crs": "EPSG:4326" },
      "temporal": { "mode": "realtime", "latest_observation_at": "2026-01-24T00:00:00Z" },
      "update_frequency": "realtime",
      "license": { "spdx": "CC-BY-4.0", "name": "Creative Commons Attribution 4.0" },
      "sensitivity": { "level": "public" },
      "links": {
        "self": "/v1/datasets/kfm.ks.hydro.usgs_stream_gauges.v1",
        "data": "/v1/datasets/kfm.ks.hydro.usgs_stream_gauges.v1/data",
        "dcat": "/v1/catalog/dcat/kfm.ks.hydro.usgs_stream_gauges.v1",
        "stac": "/v1/catalog/stac/collections/kfm.ks.hydro.usgs_stream_gauges.v1",
        "prov": "/v1/prov/activities/kfm.ks.hydro.usgs_stream_gauges.v1/latest"
      }
    },
    {
      "dataset_id": "kfm.ks.landcover.2000_2020.v1",
      "title": "Kansas Land Cover Change (2000–2020)",
      "description": "Time-sliced land cover layers suitable for timeline playback; served as tiles and downloadable artifacts.",
      "themes": ["remote_sensing", "landcover", "timeline"],
      "geometry_type": "Raster",
      "spatial": { "bbox": [-102.05, 36.99, -94.60, 40.00], "crs": "EPSG:4326" },
      "temporal": { "mode": "range", "start": "2000-01-01", "end": "2020-12-31", "granularity": "year" },
      "update_frequency": "static",
      "license": { "spdx": "CC0-1.0", "name": "Creative Commons Zero v1.0 Universal" },
      "sensitivity": { "level": "public" },
      "links": {
        "self": "/v1/datasets/kfm.ks.landcover.2000_2020.v1",
        "tilejson": "/v1/datasets/kfm.ks.landcover.2000_2020.v1/tilejson",
        "dcat": "/v1/catalog/dcat/kfm.ks.landcover.2000_2020.v1",
        "stac": "/v1/catalog/stac/collections/kfm.ks.landcover.2000_2020.v1",
        "prov": "/v1/prov/activities/kfm.ks.landcover.2000_2020.v1"
      }
    }
  ],
  "links": {
    "self": "/v1/datasets?page=1&page_size=2"
  }
}
```

</details>

---

<details>
<summary><strong>✅ Example: GET /v1/datasets/{dataset_id}</strong> <em>(datasets.get.ok.json)</em></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "generated_at": "2026-01-24T00:00:00Z"
  },
  "data": {
    "dataset_id": "kfm.ks.hydro.usgs_stream_gauges.v1",
    "title": "USGS Real-time Stream Gauges (Kansas)",
    "description": "Real-time gauge readings for Kansas rivers and streams. Includes station metadata and latest readings.",
    "themes": ["hydrology", "realtime", "rivers"],
    "spatial": { "bbox": [-102.05, 36.99, -94.60, 40.00], "crs": "EPSG:4326" },
    "temporal": {
      "mode": "realtime",
      "latest_observation_at": "2026-01-24T00:00:00Z",
      "time_filter_supported": true,
      "time_filter_notes": "Use ?time_start=...&time_end=... to retrieve a time window."
    },
    "license": {
      "spdx": "CC-BY-4.0",
      "name": "Creative Commons Attribution 4.0",
      "attribution_text": "USGS National Water Information System (NWIS)"
    },
    "source": {
      "name": "USGS NWIS",
      "kind": "upstream_api",
      "homepage": "https://waterdata.usgs.gov/",
      "retrieved_via": "pipeline"
    },
    "sensitivity": {
      "level": "public",
      "notes": "Individual stations may be restricted; API may omit restricted stations for unauthorized users."
    },
    "access": {
      "visibility": "public",
      "required_roles": []
    },
    "distributions": [
      {
        "kind": "api_geojson",
        "media_type": "application/geo+json",
        "href": "/v1/datasets/kfm.ks.hydro.usgs_stream_gauges.v1/data",
        "supports": ["bbox", "time_range"]
      },
      {
        "kind": "vector_tiles",
        "media_type": "application/x-protobuf",
        "tile_template": "/tiles/usgs_stream_gauges/{z}/{x}/{y}.pbf",
        "notes": "Optional optimization for map rendering when station count grows."
      }
    ],
    "provenance": {
      "dcat_dataset": "kfm.ks.hydro.usgs_stream_gauges.v1",
      "stac_collection": "kfm.ks.hydro.usgs_stream_gauges.v1",
      "prov_activity": "kfm.prov.activity.realtime_ingest.usgs_stream_gauges.latest",
      "run_manifest": "/v1/prov/runs/kfm-run-20260124T000000Z-usgs-stream-gauges"
    },
    "integrity": {
      "policy_pack": "kfm-policy-pack:v1",
      "lineage_required": true,
      "notes": "Streaming data still logs provenance of the specific observation used."
    }
  },
  "links": {
    "self": "/v1/datasets/kfm.ks.hydro.usgs_stream_gauges.v1",
    "data": "/v1/datasets/kfm.ks.hydro.usgs_stream_gauges.v1/data",
    "dcat": "/v1/catalog/dcat/kfm.ks.hydro.usgs_stream_gauges.v1",
    "stac": "/v1/catalog/stac/collections/kfm.ks.hydro.usgs_stream_gauges.v1",
    "prov": "/v1/prov/activities/kfm.ks.hydro.usgs_stream_gauges.v1/latest"
  }
}
```

</details>

---

<details>
<summary><strong>✅ Example: GET /v1/datasets/{dataset_id}/data</strong> (GeoJSON) <em>(datasets.data.geojson.ok.json)</em></summary>

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "station:06889000",
      "geometry": { "type": "Point", "coordinates": [-95.6752, 39.0493] },
      "properties": {
        "station_id": "06889000",
        "name": "Kansas River at Topeka",
        "value": 12.34,
        "unit": "ft",
        "observed_at": "2026-01-24T00:00:00Z",
        "source": "USGS NWIS"
      }
    },
    {
      "type": "Feature",
      "id": "station:06891000",
      "geometry": { "type": "Point", "coordinates": [-95.2355, 39.3271] },
      "properties": {
        "station_id": "06891000",
        "name": "Kansas River near Lecompton",
        "value": 9.87,
        "unit": "ft",
        "observed_at": "2026-01-24T00:00:00Z",
        "source": "USGS NWIS"
      }
    }
  ],
  "kfm": {
    "api_version": "v1",
    "dataset_id": "kfm.ks.hydro.usgs_stream_gauges.v1",
    "generated_at": "2026-01-24T00:00:01Z",
    "query": {
      "bbox": [-96.0, 38.8, -95.0, 39.6],
      "time": { "mode": "latest" }
    },
    "links": {
      "dataset": "/v1/datasets/kfm.ks.hydro.usgs_stream_gauges.v1",
      "dcat": "/v1/catalog/dcat/kfm.ks.hydro.usgs_stream_gauges.v1",
      "stac": "/v1/catalog/stac/collections/kfm.ks.hydro.usgs_stream_gauges.v1",
      "prov": "/v1/prov/activities/kfm.ks.hydro.usgs_stream_gauges.v1/latest"
    },
    "sensitivity": {
      "level": "public",
      "redaction": "none"
    }
  }
}
```

</details>

---

<details>
<summary><strong>✅ Example: GET /v1/datasets/{dataset_id}/data</strong> (Download link) <em>(datasets.data.download.ok.json)</em></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "generated_at": "2026-01-24T00:00:00Z"
  },
  "data": {
    "dataset_id": "kfm.ks.geology.surficial_geology.v1",
    "delivery": {
      "mode": "download_url",
      "media_type": "application/vnd.geo+parquet",
      "href": "https://example.invalid/download/kfm.ks.geology.surficial_geology.v1/surficial_geology.geoparquet?sig=REDACTED",
      "expires_at": "2026-01-24T06:00:00Z",
      "size_bytes": 483920194
    },
    "also_available_as": [
      {
        "media_type": "application/vnd.pmtiles",
        "href": "https://example.invalid/download/kfm.ks.geology.surficial_geology.v1/surficial_geology.pmtiles?sig=REDACTED"
      }
    ],
    "integrity": {
      "sha256": "REDACTED_EXAMPLE_HASH",
      "oci_ref": "ghcr.io/kfm/data/surficial_geology@sha256:REDACTED_EXAMPLE_DIGEST",
      "signature": "cosign://ghcr.io/kfm/data/surficial_geology@sha256:REDACTED_EXAMPLE_DIGEST"
    }
  },
  "links": {
    "dataset": "/v1/datasets/kfm.ks.geology.surficial_geology.v1",
    "dcat": "/v1/catalog/dcat/kfm.ks.geology.surficial_geology.v1",
    "stac": "/v1/catalog/stac/collections/kfm.ks.geology.surficial_geology.v1",
    "prov": "/v1/prov/activities/kfm.ks.geology.surficial_geology.v1"
  }
}
```

</details>

---

<details>
<summary><strong>✅ Example: GET /v1/datasets/{dataset_id}/tilejson</strong> <em>(datasets.tilejson.ok.json)</em></summary>

```json
{
  "meta": {
    "api_version": "v1",
    "generated_at": "2026-01-24T00:00:00Z"
  },
  "data": {
    "tilejson": "3.0.0",
    "name": "Kansas Land Cover Change (2000–2020)",
    "description": "Vector/raster tiles for fast MapLibre rendering; supports time slicing.",
    "scheme": "xyz",
    "tiles": [
      "https://example.invalid/tiles/landcover/{z}/{x}/{y}.pbf?time=2000"
    ],
    "minzoom": 0,
    "maxzoom": 14,
    "bounds": [-102.05, 36.99, -94.60, 40.00]
  },
  "links": {
    "dataset": "/v1/datasets/kfm.ks.landcover.2000_2020.v1"
  }
}
```

</details>

---

<details>
<summary><strong>❌ Example: dataset not found</strong> <em>(errors.dataset_not_found.json)</em></summary>

```json
{
  "error": {
    "code": "DATASET_NOT_FOUND",
    "message": "Dataset 'kfm.ks.unknown.nope.v1' was not found.",
    "hint": "Call GET /v1/datasets to list available dataset IDs.",
    "request_id": "req_01HZZZZZZZZZZZZZZZZZZZZZZZ"
  }
}
```

</details>

---

## ✅ Validation & CI expectations

### 🧪 What gets validated
- Shape matches **schemas** (OpenAPI/JSON Schema/Pydantic)
- Required provenance links exist: **STAC + DCAT + PROV**
- License fields are present
- Sensitivity classification is present (and enforced)

### 🛠 Suggested checks (pick what your repo already uses)
- **Schema validation**: `ajv` (JSON Schema) or `python -m jsonschema`
- **Contract tests**: load example JSON → validate against response models
- **Policy-as-code**: evaluate dataset metadata with OPA/Conftest rules

> 💡 If you’re adding a new dataset response example, treat it like a test fixture: deterministic fields, stable ordering, and minimal “noise”.

---

## 🔐 Privacy, ethics, and inference control (datasets contract hygiene)

If a dataset has sensitive locations/attributes:
- prefer aggregation/generalization (hex bins, coarse bounding boxes)
- consider privacy-preserving publication patterns (e.g., k-anonymity / l-diversity)
- log access + queries for governance/auditability
- ensure UI clearly signals restricted layers (lock icons / warnings)

✅ Your response examples should explicitly demonstrate **what a redacted/generalized dataset looks like** (even if only as a small “toy” example).

---

## 🗺️ UI + Focus Mode consumption notes

### 🗺 Web UI
- Dataset list powers the **Data Catalog** + search facets
- Dataset detail powers:
  - “Layer Provenance” panel
  - timeline capabilities (“time filter supported?”)
  - download buttons (GeoParquet/PMTiles/COG)
  - tile template configuration (MapLibre/Cesium)

### 🤖 Focus Mode
- Focus Mode must be able to:
  - resolve a dataset ID,
  - pull provenance/metadata for citations,
  - and (for live datasets) fetch a latest reading safely & log PROV usage.

---

## 🧩 Extension points (future-proofing without breaking v1)

These are OPTIONAL fields you can add if the v1 schema allows them:

- 📦 **Offline packs**: `offline_pack.href`, `offline_pack.includes[]`
- 🧊 **3D/AR delivery**: `distributions[].kind = "3d_tiles" | "czml"`
- 🔏 **Supply chain**: `integrity.oci_ref`, `integrity.signature`, `integrity.sbom_ref`
- 🧠 **Model outputs**: `model.name`, `model.version`, `model.assumptions`, `model.uncertainty`

> 🚨 If you add fields that clients will depend on, update schemas + examples together.

---

## ✅ Adding a new example (checklist)

- [ ] Add/confirm schema(s) for the response
- [ ] Create example response JSON in this folder
- [ ] Ensure provenance links exist (STAC/DCAT/PROV)
- [ ] Include license + sensitivity
- [ ] If relevant: include tilejson/distributions for MapLibre/Cesium
- [ ] Run contract validation locally
- [ ] Update this README’s index table

---

## 📚 Project references (why these examples look like this)

This README is aligned to the project’s core docs + reference library:

- 📘 *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation* (contract-first + provenance-first)
- 🧱 *KFM – Comprehensive Architecture, Features, and Design* (stack + PostGIS/Neo4j + MapLibre/Cesium)
- 🧭 *KFM – AI System Overview* (Focus Mode + AR/3D roadmap)
- 🖥️ *KFM – Comprehensive UI System Overview* (catalog UI, search, governance, provenance display)
- 📥 *KFM Data Intake – Technical & Design Guide* (real-time datasets, PostGIS tiles, rules of ingestion)
- 🌟 *KFM – Latest Ideas & Future Proposals* (GeoParquet/PMTiles packs, federation, supply-chain)
- 💡 *Innovative Concepts to Evolve KFM* (4D/AR + sensitivity-aware handling)
- 🧪 *Additional Project Ideas* (OCI artifact storage + signatures)
- 🗺️ *Maps / WebGL / Virtual Worlds / GoogleMaps* (vector tiles + web map delivery patterns)
- 🧠 *AI Concepts & more* (portfolio: AI/ML concepts library)
- 🧰 *Various programming languages & resources* (portfolio: multi-language implementation shelf)
- 🗄️ *Data management theories / architectures / Bayesian methods* (portfolio: data engineering shelf)
