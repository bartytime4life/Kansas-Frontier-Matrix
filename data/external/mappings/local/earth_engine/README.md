# 🌍 Google Earth Engine — Local Mapping Exports (KFM)

![Google Earth Engine](https://img.shields.io/badge/Google%20Earth%20Engine-GEE-4285F4?logo=google&logoColor=white)
![Remote Sensing](https://img.shields.io/badge/Remote%20Sensing-Rasters%20%2B%20Time%20Series-2ea44f)
![Metadata](https://img.shields.io/badge/Metadata-STAC%20%7C%20DCAT%20%7C%20PROV-orange)
![KFM Pipeline](https://img.shields.io/badge/KFM-Pipeline%20Aligned-6f42c1)

> 🧭 **Purpose:** Use **Google Earth Engine (GEE)** for cloud-scale remote sensing analysis, then export curated layers into the **Kansas Frontier Matrix** data lifecycle (raw → processed → catalog/prov → database → API → UI).

---

## 🗺️ What this directory is

This folder is the **local landing pad** for:
- 🧪 **Earth Engine scripts** (JS + Python) used to generate map layers
- 📤 **Exported outputs** pulled down from GEE (GeoTIFF / GeoJSON / CSV)
- 🧾 **Manifests + run notes** so exports can be ingested reproducibly into KFM
- 🧰 **Local post-processing artifacts** (COG conversion, tiling, reprojection logs)

> ✅ Think of this as the “GEE staging zone” **before** data becomes a first-class KFM dataset.

---

## 📦 Recommended layout

> If some of these folders don’t exist yet, create them as-needed.

```text
📁 data/external/mappings/local/earth_engine/
├─ 📄 README.md                      👈 you are here
├─ 📁 scripts/                       🧠 GEE scripts (JS + Python)
│  ├─ 📁 js/                          (Code Editor scripts)
│  └─ 📁 py/                          (earthengine-api workflows)
├─ 📁 aoi/                           🧭 AOI boundaries (Kansas, counties, watersheds, etc.)
├─ 📁 exports_raw/                   📤 downloads exactly as exported from GEE
├─ 📁 exports_cog/                   🧱 Cloud-Optimized GeoTIFF outputs (ready for ingest)
├─ 📁 manifests/                     🧾 dataset manifests → drives catalog/prov creation
└─ 📁 logs/                          🗒️ task IDs, export settings, QA notes
```

---

## 🧱 How this plugs into the KFM pipeline

KFM treats mapping layers as **evidence artifacts**: they must be reproducible, traceable, and properly cataloged.

### 🔁 Pipeline flow (Earth Engine → KFM)

```mermaid
flowchart LR
  A["🧠 GEE Script (JS/Python)"] --> B["📤 Export (GeoTIFF / GeoJSON / CSV)"]
  B --> C["📁 data/external/.../earth_engine (this folder)"]
  C --> D["📁 data/raw/<domain>/... (canonical raw ingest)"]
  D --> E["📁 data/work/<domain>/... (intermediate)"]
  E --> F["📁 data/processed/<domain>/... (final outputs)"]
  F --> G["🧾 STAC + DCAT + PROV boundary artifacts"]
  G --> H["🗄️ Database / Graph"]
  H --> I["🧩 API"]
  I --> J["🗺️ Map UI"]
```

### ✅ “Done means…” checklist
A layer isn’t “published” until it has:

- [ ] A reproducible GEE script (inputs + params recorded)
- [ ] Exported dataset(s) stored at the correct lifecycle stage
- [ ] Post-processed outputs standardized (COG/GeoJSON/etc.)
- [ ] Metadata + provenance artifacts (STAC + DCAT + PROV)
- [ ] Optional: DB ingestion + UI registration (layer config)

---

## 🚦 When to use Earth Engine (vs. local GIS)

Use Earth Engine when you need:

- 🌐 **Global / national-scale datasets** without downloading petabytes
- 🛰️ **Time series** (e.g., annual composites, trend lines, change detection)
- ☁️ **Cloud masking + compositing** at scale
- 📊 **Zonal stats** and reducer-based summaries over regions
- 🧩 Fast prototyping of derived indices (NDVI/NDWI/etc.) before “productizing”

Use local GIS tools when you need:

- 🗂️ Tight control over file formats + reprojection
- 🧱 Building COG pyramids / tilesets / MBTiles
- 🧾 Catalog/provenance generation + KFM integration steps
- 🧰 QA workflows (visual inspection in QGIS, pixel checks, etc.)

---

## 🚀 Quickstart

### 1) 🧭 Define your AOI (Area of Interest)
Store AOI files under:

- `aoi/` (GeoJSON, Shapefile, GPKG)
- Keep a simple naming standard like:
  - `ks_state_boundary.geojson`
  - `ks_counties_YYYY.geojson`
  - `kfm_study_area_v1.geojson`

### 2) 🧠 Choose your authoring mode

#### Option A — 🖥️ Earth Engine Code Editor (JavaScript)
Recommended for:
- interactive iteration
- visualization debugging
- quick exports

Suggested script naming:
- `scripts/js/gee_<layer>_<aoi>_<start>_<end>_v001.js`

#### Option B — 🐍 Python API (earthengine-api)
Recommended for:
- automation
- repeatable pipelines
- integration into KFM ETL scripts

Suggested script naming:
- `scripts/py/gee_<layer>_<aoi>_<start>_<end>_v001.py`

---

## 📤 Export patterns

### 🟦 Raster exports (GeoTIFF)
Typical use:
- annual composites (Landsat/Sentinel)
- derived indices (NDVI, drought indices)
- DEM-derived products (slope/aspect from SRTM-like sources)

**Best practice:**
- Export **only what you need**: AOI clipped, scale chosen intentionally, time range explicit.
- Write parameters into your manifest (see below).

### 🟩 Vector exports (GeoJSON / Shapefile)
Typical use:
- boundaries derived from classification
- digitized features (polygons/lines/points)
- simplified masks as features

### 🟨 Table exports (CSV)
Typical use:
- zonal stats by county / watershed
- time-series summaries
- per-feature metrics that will join onto vector datasets later

---

## 🧰 Local post-processing

Earth Engine exports are rarely “web-ready” out of the box. Common steps:

### 🧱 Convert GeoTIFF → COG
Store results in:
- `exports_cog/`

Recommended conventions:
- reproject to a KFM-standard CRS (if applicable)
- add overviews
- compress appropriately (lossless unless explicitly needed)

> 🧠 Tip: Keep both the original export (`exports_raw/`) and the optimized derivative (`exports_cog/`) so provenance stays clean.

---

## 🧾 Manifests

Every export should have a manifest in:

- `manifests/<dataset_id>.yml` (or `.json`)

### ✅ Minimal manifest template (YAML)

```yaml
id: gee_landcover_kansas_2010_2020_v001
title: "Kansas Landcover (GEE-derived) 2010–2020"
type: raster  # raster | vector | table
aoi:
  name: kansas
  path: aoi/ks_state_boundary.geojson

source:
  platform: google_earth_engine
  script:
    path: scripts/js/gee_landcover_kansas_2010_2020_v001.js
    entrypoint: CodeEditor
  datasets:
    - id: "<GEE_DATASET_ID_HERE>"
  license: "<license/terms from dataset provider>"

export:
  exported_at: "YYYY-MM-DD"
  region: "AOI clipped"
  scale_m: 30
  crs: "EPSG:4326"
  output:
    raw:
      - exports_raw/gee_landcover_kansas_2010_2020_v001.tif
    cog:
      - exports_cog/gee_landcover_kansas_2010_2020_v001.cog.tif

processing:
  steps:
    - "cloud mask: <method>"
    - "composite: <method>"
    - "index/classification: <method>"
  notes: "Anything that impacts reproducibility goes here."

qa:
  checks:
    - "visual spot check in QGIS"
    - "histogram sanity check"
  status: "draft"  # draft | reviewed | published
```

---

## 🧬 Metadata + provenance expectations

When a layer graduates into KFM’s “published” zone, it should emit:

- 🗂️ **STAC** collection + item records  
- 🧾 **DCAT** dataset entry  
- 🔗 **PROV** lineage bundle (inputs → steps → outputs)

> 🔍 If you’re adding a new domain/module, also create a concise domain runbook under `docs/data/<domain>/` (link it here once it exists).

---

## 🧠 Best practices

### ☁️ Cloud masking & compositing
Clouds and cloud shadows can create **false change signals** in indices and classifications. Always:
- apply cloud masks
- prefer compositing strategies when appropriate
- record your cloud mask method + thresholds in the manifest

### 🧮 Avoid timeouts (GEE coding style)
Earth Engine is server-side; write code that:
- uses `ee.*` functions
- maps functions over `ImageCollection`s
- reduces only what you need
- clips early, filters early, summarizes intentionally

### 🧩 Export metadata matters
Record:
- AOI version
- dataset IDs
- band scaling factors (if used)
- time range
- export scale & CRS
- any special pyramiding policy settings (especially for multi-band outputs)

---

## 🧯 Troubleshooting (common pain points)

<details>
<summary><b>🧱 My export is huge / takes forever</b></summary>

- Reduce AOI size (start with a small tile)
- Increase scale (e.g., 10m → 30m if acceptable)
- Export fewer bands
- Export a single time slice first, then scale up
</details>

<details>
<summary><b>☁️ My output has stripes / weird gaps</b></summary>

- Check cloud mask (too aggressive can “erase” valid pixels)
- Verify compositing window & thresholds
- Inspect raw scenes for known sensor artifacts
</details>

<details>
<summary><b>🧪 My results aren’t reproducible</b></summary>

- Confirm your script pins:
  - dataset IDs
  - date ranges
  - AOI geometry
  - scale & CRS
- Store manifests alongside exports
- Don’t rely on “current map view” states (always encode params)
</details>

---

## 🔒 Credentials + compliance

- 🚫 **Never** commit credentials, tokens, or private keys.
- 📜 Respect dataset licenses and Google Earth Engine terms.
- 🧑‍🤝‍🧑 If a workflow depends on user credentials, document that clearly in the manifest and runbook.

---

## 📚 References (project-local)

- 📄 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint**
- 📄 **Cloud-Based Remote Sensing with Google Earth Engine — Fundamentals and Applications**
- 📄 **MARKDOWN_GUIDE_v13** (KFM pipeline, data lifecycle, STAC/DCAT/PROV conventions)
- 📄 **Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design**

---

## ✅ Next actions (good starter tasks)

- [ ] Add a first AOI boundary to `aoi/`
- [ ] Commit a “hello world” GEE script that exports a small raster
- [ ] Add one manifest that fully documents the export
- [ ] Post-process the raster into a COG
- [ ] Promote the dataset into `data/raw/` → `data/processed/` with STAC/DCAT/PROV artifacts

