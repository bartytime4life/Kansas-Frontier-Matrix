# 🗺️ Sample Map Data (`web/src/assets/map/data/sample/`)

![Scope](https://img.shields.io/badge/scope-sample%20map%20data-lightgrey)
![Format](https://img.shields.io/badge/format-GeoJSON-2ea44f)
![Viewer](https://img.shields.io/badge/viewer-MapLibre%20%7C%20Leaflet-blue)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT-orange)

> **Goal:** keep the Web UI moving ⚡ — even when the backend, database, or pipelines aren’t running.

This folder contains **tiny, commit-friendly** datasets (and optional metadata) used by the Web map for:
- 🧪 UI development & tests
- 🎛️ layer styling experiments
- 🧭 “offline-ish” demos
- 🧵 story/timeline prototypes

In the broader KFM architecture, the **full** datasets are served via the API (dataset metadata + streaming GeoJSON) and/or via **tile endpoints** for raster + vector layers.  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

<details>
  <summary><strong>📚 Table of contents</strong></summary>

- [Why this folder exists](#-why-this-folder-exists)
- [What belongs here](#-what-belongs-here)
- [Recommended layout](#-recommended-layout)
- [Data contract](#-data-contract)
- [Temporal support (timeline-ready)](#-temporal-support-timeline-ready)
- [Optional metadata sidecar](#-optional-metadata-sidecar)
- [How to create a new sample layer](#-how-to-create-a-new-sample-layer)
- [Validation checklist](#-validation-checklist)
- [Licensing & attribution](#-licensing--attribution)
- [Project anchors](#-project-anchors)
</details>

---

## 🧭 Why this folder exists

KFM’s web viewer is designed around a browser-based interactive map + timeline UI (MapLibre GL JS or Leaflet) where users can toggle layers and move through time.  [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

In the same architecture:
- **Vector layers** are typically stored/served as **GeoJSON or shapefiles**, and **raster layers** as **COGs**, with tiles generated for interactive use.  [oai_citation:4‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)
- The API can expose **dataset metadata (DCAT) + STAC assets**, stream GeoJSON by bbox, and serve **vector/raster tiles**.  [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

➡️ This `sample/` directory is the **front-end-friendly shortcut**: small “just enough data” slices that match those formats and UI needs—without requiring the full serving stack.

> [!NOTE]
> The repository design also calls out that the `web/` area may include **precomputed JSON** needed by the app (e.g., document indexes or timeline configuration). This folder can act as one place to keep those “small + essential” map examples alongside such configs.  [oai_citation:7‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## 📦 What belongs here

✅ **Good fits**
- 🧩 Small **GeoJSON FeatureCollections** (points/lines/polygons)
- 🧾 Minimal **layer manifests** / **metadata sidecars** (JSON)
- 🎨 Sample style snippets / paint rules (if your map stack needs them)
- 🧪 Test fixtures that represent real-world geometry + properties

🚫 **Not for**
- 🐘 Huge GeoJSON dumps (use vector tiles / API streaming)
- 🛰️ Full-resolution rasters (use COGs + tile services)
- 📥 Raw vendor/source downloads (belong in `data/sources/` / `data/raw/` etc.)
- 🔒 Unlicensed / unclear-attribution datasets

> [!IMPORTANT]
> Keep this folder **tiny**. The KFM repo structure anticipates large data being handled via dedicated `data/` areas (and optionally DVC for large artifacts), with CI validating catalog integrity.  [oai_citation:8‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H) [oai_citation:9‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

---

## 🗂️ Recommended layout

> You can adapt this to your actual loader/registry code — the key is consistency. 🧱

```text
web/src/assets/map/data/sample/               📁
├─ README.md                                  📘 (you are here)
├─ manifest.sample.json                       🧾 (optional “what’s available” index)
├─ layers/                                    🗺️
│  ├─ ks_counties.sample.geojson              🟦
│  ├─ historic_trails.sample.geojson          🐎
│  └─ places_of_interest.sample.geojson       📍
└─ meta/                                      🏷️ (optional per-layer metadata)
   ├─ ks_counties.sample.meta.json            🧾
   ├─ historic_trails.sample.meta.json        🧾
   └─ places_of_interest.sample.meta.json     🧾
```

---

## 📐 Data contract

### 1) Format
- **GeoJSON** `FeatureCollection` (preferred for sample layers)

### 2) Coordinates / CRS
- Use **WGS84 / EPSG:4326** and standard GeoJSON coordinate order: **`[lon, lat]`**.
- If exporting from PostGIS, transform to EPSG:4326 before GeoJSON output (example uses `ST_Transform(..., 4326)` and `ST_AsGeoJSON`).  [oai_citation:10‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

### 3) Size budget
Keep samples **fast to load**:
- ✅ target: **< 1–2 MB per file**
- ✅ target: **< 5,000 features**
- ✅ simplify geometry where it doesn’t change the story (especially polygons)

> [!TIP]
> If a layer is too big as GeoJSON, it’s a strong signal it should become a **tile layer** (vector MVT or raster tiles) in the “real” pipeline/serving path.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:12‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## ⏳ Temporal support (timeline-ready)

The front-end architecture is described as keeping a shared timeline state (e.g., `currentYear`) so that when a user changes the year, the map can filter by year and the story panel can react in sync.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

To make a **sample layer timeline-friendly**, include *one* of these patterns:

### Option A — per-feature year
```json
"properties": {
  "name": "Fort Example",
  "year": 1854
}
```

### Option B — per-feature start/end
```json
"properties": {
  "name": "Trail Segment A",
  "startYear": 1840,
  "endYear": 1862
}
```

### Option C — per-layer time range in metadata
Keep features “timeless” but store the timeframe in `*.meta.json` (see below).

> [!NOTE]
> MapLibre-based designs explicitly call out timeline controls / time sliders for animating across time slices.  [oai_citation:14‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

---

## 🏷️ Optional metadata sidecar

KFM’s API design describes dataset metadata as a **DCAT summary** with links to assets like **STAC items**.  [oai_citation:15‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

For samples, you don’t need full DCAT/STAC—just enough fields to:
- render a human-friendly layer list 🧾
- include license/attribution ✅
- optionally link to the “real” dataset id / tiles 🔗

### Minimal `*.meta.json` example
```json
{
  "id": "historic_trails_sample",
  "title": "Historic Trails (Sample)",
  "description": "Small subset of historic trails for UI development & styling.",
  "license": "Public Domain / CC0 (verify source before using)",
  "attribution": "Source: <add agency/collection here>",
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "time": { "startYear": 1840, "endYear": 1880 },
  "links": {
    "apiDataset": "/api/v1/datasets/historic_trails",
    "apiData": "/api/v1/datasets/historic_trails/data?format=geojson&bbox={bbox}",
    "tilesVector": "/tiles/historic_trails/{z}/{x}/{y}.pbf"
  }
}
```

---

## ➕ How to create a new sample layer

### 1) Start from the “real” serving path (preferred)
If the backend is available, grab a **bbox-restricted** sample from the dataset endpoint described in the docs.  [oai_citation:16‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

```bash
# Example (adjust host, dataset id, bbox)
curl "http://localhost:8000/api/v1/datasets/ks_hydrology_1880/data?format=geojson&bbox=-102,37,-94,40" \
  -o web/src/assets/map/data/sample/layers/ks_hydrology_1880.sample.geojson
```

### 2) If your layer is large → prefer tiles
For big vectors/raster, the documented approach is to serve standard tile endpoints:
- `GET /tiles/{layer}/{z}/{x}/{y}.pbf` (vector MVT)
- `GET /tiles/{layer}/{z}/{x}/{y}.png` or `.webp` (raster)  [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

Sample data can still include:
- a tiny GeoJSON preview (few features), and/or
- metadata pointing to the tile URL templates.

### 3) Clip + simplify (so it stays “sample-sized”)
Use any open tooling (QGIS, scripts, etc.) to:
- clip to a bbox or county boundary
- simplify geometry
- reduce attributes to what the UI needs

### 4) Add/Update `manifest.sample.json` (optional)
A single index makes it easy to show “Sample Layers” in the UI:

```json
{
  "layers": [
    {
      "id": "historic_trails_sample",
      "path": "./layers/historic_trails.sample.geojson",
      "meta": "./meta/historic_trails.sample.meta.json",
      "geometryType": "LineString"
    }
  ]
}
```

---

## ✅ Validation checklist

Before committing a new sample dataset:

- [ ] GeoJSON parses as valid JSON (no trailing commas)
- [ ] Root is a `FeatureCollection`
- [ ] CRS is WGS84 / EPSG:4326 and coordinates are `[lon, lat]`  [oai_citation:18‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- [ ] File is small enough for instant load (see size budget)
- [ ] `id` values are stable (don’t rely on array index)
- [ ] Temporal fields exist if layer is timeline-filtered  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- [ ] License + attribution are included (in meta or README)
- [ ] Any catalog/manifest JSON stays valid (CI should be able to validate it)  [oai_citation:20‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

---

## ⚖️ Licensing & attribution

KFM’s design emphasizes open, reproducible workflows with public/open data sources and browser-based access (no proprietary requirement).  [oai_citation:21‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

For every sample layer, include:
- **license** (e.g., CC0, Public Domain, CC-BY, etc.)
- **attribution/source** (agency, archive, dataset name, year)
- **notes on modifications** (clip/simplify/normalize fields)

---

## 📚 Project anchors

These references are the “why” behind the conventions above:

- API dataset metadata + GeoJSON streaming and tile endpoints (vector/raster)  [oai_citation:22‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695) [oai_citation:23‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Web viewer design: MapLibre/Leaflet, time slider/timeline concepts  [oai_citation:24‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) [oai_citation:25‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- Front-end map layer loading: tile layers for large datasets vs GeoJSON overlays for small data  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Repo structure: `data/processed/`, `stac/`, `web/` w/ precomputed JSON; large data via DVC; CI validates catalogs  [oai_citation:27‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H) [oai_citation:28‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)
- GeoJSON export sanity (transform to EPSG:4326 before output)  [oai_citation:29‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
