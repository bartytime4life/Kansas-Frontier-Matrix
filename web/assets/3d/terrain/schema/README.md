---
title: "🌄 3D Terrain Schema"
description: "JSON Schemas + conventions for terrain datasets consumed by the KFM web viewer (CesiumJS / 3D Tiles)."
status: "draft"
version: "0.1.0"
owners:
  - "web/assets/3d/terrain"
tags:
  - kfm
  - terrain
  - 3d
  - cesium
  - schemas
  - json-schema
  - provenance
---

# 🌄 3D Terrain Schema (`web/assets/3d/terrain/schema`)

![JSON Schema](https://img.shields.io/badge/JSON%20Schema-2020--12-blue)
![Contract First](https://img.shields.io/badge/Contract--First-✅-success)
![Provenance](https://img.shields.io/badge/Provenance--First-🧾-informational)
![CesiumJS](https://img.shields.io/badge/CesiumJS-🌍%20Terrain-black)
![3D Tiles](https://img.shields.io/badge/3D%20Tiles-🧱%20Streaming-orange)

This folder defines the **data contracts (schemas) and conventions** for **3D terrain assets** used by the KFM front-end. KFM’s web viewer stack includes **CesiumJS for 3D globe/terrain visualization**, with **3D Tiles** used for streaming 3D geospatial content.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

> **Guiding rule 🧠:** anything that shows up in the UI must be traceable back to cataloged sources and provable processing — no “mystery layers.”  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 Overview

KFM often includes a **Digital Elevation Model (DEM)** for Kansas (e.g., ~10m USGS 3DEP) for:
- **2D**: hillshade/contours
- **3D**: terrain rendering
- **analysis**: hydrology workflows (watershed delineation, etc.)

Because DEMs are large, the system favors **tiling/LOD** strategies: DEMs are commonly converted to **quantized-mesh terrain** or **3D Tiles** for Cesium-based streaming.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Also: performance matters. KFM’s LOD approach explicitly extends to 3D terrain (lower-res until zoomed in).  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🎯 Goals

✅ **Contract-first**: terrain datasets ship with a **self-described JSON manifest** validated by JSON Schema.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
✅ **Provenance-first**: every terrain dataset includes **sources + processing steps**, suitable for attributions and method tracing.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
✅ **Cesium-friendly**: supports Cesium terrain providers (quantized-mesh) and Cesium 3D Tiles tilesets.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
✅ **CI-friendly**: schemas are intended for automated validation gates (structured outputs validated; CI fails on schema errors).  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
✅ **Portable**: works for static hosting (e.g., GitHub Pages) **and** API-served tiles.

---

## 🚫 Non-goals

- This folder does **not** define the full KFM catalog (STAC/DCAT/PROV) — it defines the **web-facing “terrain loading contract.”**  
- This folder does **not** prescribe the exact terrain tiling pipeline/tooling (we only capture **what must be documented**).

---

## 🧱 How terrain typically ships in KFM

```mermaid
flowchart LR
  A[🗺️ Source DEM (COG/GeoTIFF)] --> B[⚙️ Processing & QA]
  B --> C[🧱 Terrain Tiles<br/>(quantized-mesh or 3D Tiles)]
  C --> D[📄 Dataset Manifest JSON<br/>(validated)]
  D --> E[🌐 React App + CesiumJS Viewer]
  D --> F[✅ CI Schema Validation]
  B --> G[🧾 Provenance + License + Attribution]
  G --> D
```

---

## 📁 Directory layout

> The files below are the **intended** layout for schema + examples.

```text
📦 web/assets/3d/terrain/
 ├─ 📂 schema/
 │   ├─ 📄 README.md                      👈 you are here
 │   ├─ 📄 terrain.dataset.schema.json    ✅ top-level dataset manifest
 │   ├─ 📄 terrain.provider.schema.json   ✅ how to load in Cesium
 │   ├─ 📄 terrain.provenance.schema.json ✅ sources + processing steps
 │   ├─ 📄 terrain.lod.schema.json        ✅ LOD/perf knobs
 │   └─ 📂 examples/
 │       ├─ 📄 kfm.ks.terrain.dem_usgs_10m.v1.dataset.json
 │       └─ 📄 kfm.ks.terrain.county_hi_res_lidar.v1.dataset.json
 └─ 📂 datasets/
     └─ 📂 kfm.ks.terrain.dem_usgs_10m.v1/
         ├─ 📄 dataset.json               (matches terrain.dataset.schema.json)
         ├─ 📂 tiles/                     (quantized-mesh or 3D Tiles)
         └─ 🖼️ thumbnail.png
```

---

## 🧩 Schema set

### 1) `terrain.dataset.schema.json` 🧾
**What it describes:** the **dataset manifest** the web app consumes.

**Must answer:**
- What is this terrain dataset?
- Where are the tiles?
- What are the bounds and height range?
- What’s the license + attribution?
- Where did it come from and how was it processed?

### 2) `terrain.provider.schema.json` 🌍
**What it describes:** how the front-end loads terrain in Cesium.

Supported provider “kinds” (recommended):
- `cesium-quantized-mesh` → terrain tiles + `layer.json`
- `cesium-3d-tiles` → a `tileset.json`
- `heightmap-grid` → a heightmap/mesh pipeline (fallback/offline use)

> KFM’s 3D visualization path explicitly includes CesiumJS for globe/terrain, and 3D Tiles for streaming 3D content.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 3) `terrain.provenance.schema.json` 🔎
**What it describes:** minimal provenance that’s usable in:
- credits/attribution
- “how was this made?” UI
- story references / citations

KFM uses provenance as a first-class requirement (“no mystery layers”).  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 4) `terrain.lod.schema.json` 🪜
**What it describes:** tuning knobs for LOD + performance.

KFM’s LOD strategy explicitly extends to 3D terrain (lower res until the user zooms in).  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🗂️ Core object model (recommended)

### `TerrainDataset` (manifest) ✅
These are the recommended top-level fields (schema should enforce required ones):

| Field | Type | Required | Why it exists |
|------|------|----------|---------------|
| `id` | string | ✅ | Stable identifier (used in UI + caching) |
| `version` | string | ✅ | SemVer-ish version for change control |
| `title` | string | ✅ | Human-friendly name |
| `description` | string | ✅ | What’s included / limitations |
| `provider` | object | ✅ | How to load tiles in Cesium |
| `extents` | object | ✅ | Spatial bbox + vertical range |
| `crs` | object | ✅ | Distribution CRS + original CRS notes |
| `license` | string | ✅ | Legal reuse clarity (required in KFM metadata)  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) |
| `attribution` | object | ✅ | Required credits for UI display |
| `provenance` | object | ✅ | Sources + processing steps (no mystery layers)  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) |
| `assets` | object | ⭕ | Thumbnails, style presets, etc. |
| `lod` | object | ⭕ | LOD/performance knobs |

---

## 🧾 Provenance & “no mystery layers” rule

KFM’s policy is straightforward: **if it appears in the UI, it must be traceable**.  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
So provenance for terrain should include at minimum:

### `sources[]` 📚
Each source entry should capture:
- `name` (e.g., “USGS 3DEP 1/3 arc-second DEM”)
- `publisher` / `organization`
- `license`
- `retrieved_at` (ISO date)
- `url` (if public)
- `checksum` (if you downloaded a file)

### `processing[]` ⚙️
Each step should capture:
- `name` (e.g., “Reproject to EPSG:4326”, “Generate quantized-mesh tiles”)
- `tool` + `tool_version`
- `params` (record the “human choices” that matter)
- `run_at`
- `inputs[]` + `outputs[]` (paths, IDs, checksums)

> DEMs are commonly used in 2D + 3D in KFM, and often converted to tiled forms for Cesium streaming.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🪜 LOD & tiling notes (practical)

Terrain is *big*. KFM’s LOD management means:
- low zoom: coarser terrain (fewer vertices / smaller tiles)
- high zoom: progressively higher detail
- keep the app responsive by not over-fetching

This is aligned with KFM’s stated approach for 3D terrain: **use lower resolution until zoomed in**.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✅ Validation (local + CI)

KFM’s CI gates include JSON Schema validation for structured outputs (and fails on schema errors).  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Local validation options 🧪

<details>
<summary><strong>Option A: Node + AJV (recommended for web)</strong></summary>

```bash
npm i -D ajv ajv-formats
node ./scripts/validate-json.mjs \
  --schema web/assets/3d/terrain/schema/terrain.dataset.schema.json \
  --data   web/assets/3d/terrain/datasets/<dataset-id>/dataset.json
```

</details>

<details>
<summary><strong>Option B: Python jsonschema (quick check)</strong></summary>

```bash
python -m pip install jsonschema
python -m jsonschema \
  -i web/assets/3d/terrain/datasets/<dataset-id>/dataset.json \
  web/assets/3d/terrain/schema/terrain.dataset.schema.json
```

</details>

---

## 🏷️ Naming & versioning conventions

KFM uses descriptive dataset IDs like `kfm.ks.landcover.2000_2020.v1`.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
For terrain, follow the same spirit:

✅ **Dataset ID pattern (recommended):**
- `kfm.<region>.<theme>.<detail>.<vN>`
- Examples:
  - `kfm.ks.terrain.dem_usgs_10m.v1`
  - `kfm.ks.terrain.lidar_dtm_flint_hills_1m.v1`

✅ **Folder names**
- `lower_case_with_underscores`
- avoid spaces

✅ **Schema versioning**
- schemas should have a top-level `$id` and `version`
- breaking change → bump major version

---

## 🧪 Examples

### Example A — Quantized-mesh terrain (`cesium-quantized-mesh`)

```json
{
  "id": "kfm.ks.terrain.dem_usgs_10m.v1",
  "version": "1.0.0",
  "title": "Kansas DEM (USGS ~10m) — Terrain Tiles",
  "description": "Statewide DEM for Kansas. Used for 3D terrain visualization and derived analyses. Converted to streaming terrain tiles for Cesium.",
  "provider": {
    "kind": "cesium-quantized-mesh",
    "url": "/assets/3d/terrain/datasets/kfm.ks.terrain.dem_usgs_10m.v1/tiles/",
    "layerJson": "layer.json"
  },
  "extents": {
    "spatial": {
      "bbox": [-102.05, 36.99, -94.59, 40.00],
      "units": "degrees"
    },
    "vertical": {
      "datum": "NAVD88",
      "units": "m",
      "min": 200,
      "max": 1250
    }
  },
  "crs": {
    "distribution": "EPSG:4326",
    "original": "EPSG:xxxx",
    "notes": "Original CRS is preserved in provenance; distribution normalized for web alignment."
  },
  "lod": {
    "minZoom": 0,
    "maxZoom": 14,
    "maxScreenSpaceError": 2.0,
    "notes": "Use coarser terrain until zoomed in to keep UX responsive."
  },
  "license": "Public-Domain",
  "attribution": {
    "requiredText": "Contains data from USGS 3DEP (public domain).",
    "links": [
      { "label": "USGS 3DEP", "href": "https://www.usgs.gov/3d-elevation-program" }
    ]
  },
  "provenance": {
    "sources": [
      {
        "name": "USGS 3DEP 1/3 arc-second DEM",
        "publisher": "USGS",
        "license": "Public-Domain",
        "retrieved_at": "2026-01-15"
      }
    ],
    "processing": [
      {
        "name": "Reproject + resample for distribution",
        "tool": "gdalwarp",
        "tool_version": "x.y.z",
        "run_at": "2026-01-15",
        "params": { "target_crs": "EPSG:4326" }
      },
      {
        "name": "Generate quantized-mesh tiles",
        "tool": "terrain-tiler",
        "tool_version": "x.y.z",
        "run_at": "2026-01-15",
        "params": { "format": "quantized-mesh", "maxZoom": 14 }
      }
    ]
  },
  "assets": {
    "thumbnail": "thumbnail.png"
  }
}
```

### Example B — 3D Tiles terrain/relief (`cesium-3d-tiles`)

```json
{
  "id": "kfm.ks.terrain.relief_3dtiles.v1",
  "version": "1.0.0",
  "title": "Kansas Relief — 3D Tiles",
  "description": "Terrain/relief published as a 3D Tiles tileset for Cesium streaming.",
  "provider": {
    "kind": "cesium-3d-tiles",
    "tilesetUrl": "/assets/3d/terrain/datasets/kfm.ks.terrain.relief_3dtiles.v1/tileset.json"
  },
  "extents": { "spatial": { "bbox": [-102.05, 36.99, -94.59, 40.00] } },
  "crs": { "distribution": "EPSG:4326" },
  "license": "Public-Domain",
  "attribution": { "requiredText": "Derived from public elevation sources." },
  "provenance": { "sources": [], "processing": [] }
}
```

---

## 🧰 Cesium integration notes (front-end)

> The web stack includes CesiumJS for 3D globe/terrain visualization, and uses 3D Tiles for streaming 3D geospatial content.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

Typical loading patterns:
- `cesium-quantized-mesh`: set `viewer.terrainProvider` from a URL to the terrain layer endpoint.
- `cesium-3d-tiles`: load a `Cesium3DTileset` from `tileset.json` and add to the scene.

Keep UI responsive by respecting LOD constraints (don’t request max detail until zoomed in).  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📚 Sources (project files) 🔗

- **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** (CesiumJS integration, 3D Tiles streaming, contract-first + provenance-first, DEM tiling guidance).  [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- **MARKDOWN_GUIDE_v13.md.gdoc** (validation & CI gates; JSON Schema validation expectations).  [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- **Kansas-Frontier-Matrix: Open-Source Geospatial Historical Mapping Hub Design** (3D expansion notes; streaming terrain + 3D tiles via Cesium).  [oai_citation:22‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  
- **python-geospatial-analysis-cookbook** (example pipeline concepts: DEM conversion + web 3D visualization patterns).  [oai_citation:23‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)

---

## ✅ Checklist for adding a new terrain dataset

- [ ] Create dataset folder: `web/assets/3d/terrain/datasets/<dataset-id>/`
- [ ] Place tiles (`tiles/` or `tileset.json`)
- [ ] Write `dataset.json` manifest (fills license + attribution + provenance)
- [ ] Validate against schema locally
- [ ] Ensure CI passes (schema + doc rules)
- [ ] Confirm LOD settings won’t overload the browser
