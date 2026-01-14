# 🗺️🧊 3D Map Assets (KFM)

![KFM](https://img.shields.io/badge/KFM-3D%20map%20assets-2b6cb0)
![CesiumJS](https://img.shields.io/badge/CesiumJS-integrated-3b82f6)
![3D%20Tiles](https://img.shields.io/badge/3D%20Tiles-streaming-16a34a)
![WebGL](https://img.shields.io/badge/WebGL-runtime-111827)
![Provenance](https://img.shields.io/badge/provenance-first-7c3aed)

**Folder:** `web/assets/maps/3d/`  
**Role:** Frontend-served 3D terrain + tilesets + models used by the KFM Web UI (primarily via **CesiumJS**). 🧭

> [!IMPORTANT]
> This directory is for **runtime-ready** 3D assets (already optimized for the browser).  
> **Raw source data** (LiDAR LAS/LAZ, massive DEMs, full-resolution orthos, etc.) should live in the pipeline/data storage layer — not here.

---

## 📌 Table of contents

- [What this folder is](#-what-this-folder-is)
- [What belongs here](#-what-belongs-here)
- [Folder layout](#-folder-layout)
- [Formats we support](#-formats-we-support)
- [3D layer contract](#-3d-layer-contract)
- [Coordinate + units rules](#-coordinate--units-rules)
- [Asset pipeline](#-asset-pipeline)
- [Performance + size budgets](#-performance--size-budgets)
- [Mobile + responsive notes](#-mobile--responsive-notes)
- [QA checklist](#-qa-checklist)
- [Security + integrity](#-security--integrity)
- [Glossary](#-glossary)
- [Reference shelf](#-reference-shelf)

---

## 🎯 What this folder is

This folder is the **delivery layer** for KFM’s 3D experience:

- 🌎 **Terrain** (Kansas DEM-derived terrain)
- 🧱 **3D Tiles** (streamed geospatial 3D content: point clouds, meshes, buildings, time-sliced story scenes)
- 🧩 **glTF/GLB models** (localized 3D models used in stories or map overlays)
- 🧾 **Metadata** that keeps “the map behind the map” visible: provenance, licensing, processing notes, bounding boxes, time ranges

The goal is: **fast rendering + clear attribution + repeatable provenance**. 🧠🧾

---

## ✅ What belongs here

| Asset | Example | Why it’s here |
|------|---------|---------------|
| Terrain provider | Kansas DEM → terrain tiles | Enables 3D relief + hill/valley context |
| 3D Tiles tileset | LiDAR point cloud tiles / mesh tiles | Streams efficiently as the user zooms |
| Small GLB models | Landmark model / story prop | Lightweight storytelling + annotations |
| Previews | `preview.webp` | Layer thumbnails + QA quick-check |
| Manifests / contracts | `layer.json` | Layer panel + attribution + load config |

> [!TIP]
> If a dataset is “too big to reasonably code review” (or would bloat repo clones), treat it as **external** and store only:
> - a manifest (`layer.json`)  
> - a preview  
> - a pointer URL  
> - checksums + provenance

---

## 🧱 Folder layout

Suggested structure (keep it boring, predictable, and diff-friendly):

```text
web/assets/maps/3d/
├─ README.md
├─ index.json                         # optional: registry of 3D layers exposed to the UI
├─ terrain/
│  └─ kansas_dem_usgs_10m/
│     └─ v1/
│        ├─ layer.json                # contract + provenance + attribution
│        ├─ terrain/                  # terrain tiles (provider root)
│        └─ preview.webp
├─ tilesets/
│  └─ monument_rocks/
│     └─ v1/
│        ├─ layer.json
│        ├─ tileset.json              # Cesium 3D Tiles entry
│        ├─ tiles/                    # tile content
│        └─ preview.webp
├─ models/
│  └─ story_props/
│     └─ v1/
│        ├─ layer.json
│        ├─ model.glb
│        └─ preview.webp
└─ _schemas/
   └─ kfm-3d-layer.schema.json        # optional: JSON schema for validation
```

> [!NOTE]
> The exact folders can evolve, but the **contract file + versioning** should remain stable. Versioned folders make rollbacks and citations much easier. 🔁

---

## 📦 Formats we support

### Terrain
- ✅ Cesium-friendly **terrain tiles** (e.g., quantized mesh terrain provider output)
- ✅ Heightmaps **only** as intermediate artifacts (avoid shipping raw heightmaps unless required)

### 3D geometry
- ✅ **3D Tiles** (`tileset.json` + tile content)
- ✅ **glTF / GLB** for small localized models

### Textures / thumbnails
- ✅ `webp`, `png`, `jpg/jpeg` (choose based on needs — see [Performance + size budgets](#-performance--size-budgets))

---

## 🧾 3D layer contract

Every “shippable” 3D layer MUST have a `layer.json` next to its primary artifact(s).  
This is what makes layers discoverable, auditable, and UI-friendly.

### Minimal example

```json
{
  "id": "kfm.ks.terrain.kansas_dem_usgs_10m.v1",
  "title": "Kansas Terrain (USGS 10m DEM)",
  "kind": "terrain",
  "version": "1.0.0",

  "spatial": {
    "bbox_wgs84": [-102.051, 36.993, -94.588, 40.003],
    "crs_display": "EPSG:4326",
    "crs_original": "EPSG:xxxx",
    "vertical_datum": "NAVD88",
    "units": { "height": "m" }
  },

  "temporal": {
    "start": "2017-01-01",
    "end": "2020-12-31"
  },

  "artifacts": [
    {
      "role": "terrain-provider",
      "href": "./terrain/",
      "format": "terrain",
      "sha256": "REPLACE_ME",
      "size_bytes": 123456789
    },
    {
      "role": "preview",
      "href": "./preview.webp",
      "format": "image/webp"
    }
  ],

  "render": {
    "engine": "cesium",
    "options": {
      "recommendedTerrainExaggeration": 1.5,
      "prefetch": true
    }
  },

  "attribution": {
    "label": "USGS 3DEP (verify exact product + license)",
    "required": true
  },

  "provenance": {
    "sources": [
      {
        "name": "USGS 3DEP",
        "accessed": "2026-01-14",
        "license": "Public domain (verify)",
        "url": "SOURCE_URL_HERE"
      }
    ],
    "processing": [
      "Reproject to display CRS (EPSG:4326)",
      "Standardize vertical units to meters",
      "Generate terrain tiles for Cesium provider",
      "Create preview image for QA/UI"
    ],
    "limitations": [
      "Vertical datum conversion may introduce small errors depending on source metadata."
    ]
  }
}
```

### Contract rules ✅

- `id` is **stable** and **unique**
- `version` changes when bytes change
- `bbox_wgs84` is required (so the UI can zoom-to-layer)
- Every artifact that ships should have:
  - `format`
  - `href`
  - **checksum** (recommended)
- Provenance must include:
  - source name
  - access date
  - license/terms
  - processing notes

---

## 📐 Coordinate + units rules

- **Display standard:** WGS84 (`EPSG:4326`) for web consistency 🧭  
- Always record **original CRS** in metadata (don’t erase history).
- Standardize **vertical units** (prefer **meters**) and store the unit in metadata.
- If using local/state-plane calculations in pipelines, convert outputs for display and record the transform steps.

> [!WARNING]
> “It lines up on my laptop” is not validation.  
> Always check bbox + CRS + vertical datum explicitly before shipping.

---

## 🔧 Asset pipeline

A practical, repeatable flow (tool-agnostic):

### 1) Acquire + document sources
- DEM / LiDAR / ortho imagery / scanned maps / photogrammetry
- Capture **license + access date + URL + citation text**

### 2) Normalize spatial reference
- Reproject / regrid as needed for consistent display
- Ensure height units are consistent

### 3) Generate 3D deliverables
- Terrain → terrain tiles provider output
- Geometry → 3D Tiles tilesets (chunked + LOD)
- Small story models → GLB

### 4) Optimize for WebGL
- Decimate meshes where possible (keep silhouette + key features)
- Build LODs (don’t force mobile devices to render desktop assets)
- Compress textures appropriately

### 5) Package + validate
- Create `layer.json`
- Generate `preview.webp`
- Compute `sha256`
- Run validation checks (see [QA checklist](#-qa-checklist))

---

## 🚀 Performance + size budgets

3D is **opt-in heavy**, so we budget aggressively. 💨

### Geometry 🧱
- Prefer **streaming** formats (3D Tiles) for large content
- Keep GLB models **small + local** (story props, not entire counties)

### Textures 🧵
General guidance:
- `jpg/jpeg` ✅ for satellite/photographic imagery (lossy, compact)
- `png` ✅ for crisp overlays + transparency (borders, masks, UI-like textures)
- Avoid shipping `bmp` ❌ (large/uncompressed)
- Thumbnails: `webp` ✅ (fast, compact)

### Delivery 📡
- Favor “cacheable static files” (CDN-friendly)
- Use content hashing or versioned folders so caching is safe

> [!TIP]
> If a layer needs frequent updates, keep its **identifier stable** but bump `version` and update checksums.  
> This makes time-travel + reproducible citations possible.

---

## 📱 Mobile + responsive notes

Even if the 3D view is “desktop-first”, it must degrade gracefully:

- ✅ Progressive loading (show something fast, refine later)
- ✅ Don’t assume perfect GPS accuracy or stable battery
- ✅ Keep controls thumb-friendly; avoid tiny UI targets
- ✅ Prefer smaller textures + lower LOD on narrow screens

> [!NOTE]
> If you touch HTML templates, ensure the site remains mobile-friendly:
> ```html
> <meta name="viewport" content="width=device-width, initial-scale=1.0">
> ```

---

## 🧪 QA checklist

Use this before merging any new 3D layer:

### Metadata & provenance
- [ ] `layer.json` present and valid JSON
- [ ] `id` is unique + stable
- [ ] License/terms recorded
- [ ] Access date recorded
- [ ] Processing steps listed
- [ ] Known limitations included

### Spatial correctness
- [ ] `bbox_wgs84` matches reality (spot-check in viewer)
- [ ] CRS conversion steps documented
- [ ] Height units + vertical datum documented

### Performance
- [ ] Preview exists and looks sane (no wrong hemisphere, no upside-down terrain)
- [ ] Asset sizes are reasonable for web delivery
- [ ] Tileset loads without console errors
- [ ] LOD behavior feels sane (no “all-at-once” megadownload)

### Visual design (cartography in 3D 🎨)
- [ ] Avoid overly intense colors that overpower the map context
- [ ] Use appropriate color schemes:
  - qualitative = categories
  - sequential = ordered values
  - diverging = above/below baseline
- [ ] Terrain shading supports legibility (not “muddy”)

---

## 🔐 Security & integrity

3D assets are files… and files are attack surfaces. 🛡️

- Treat externally sourced assets as **untrusted**
- Prefer a controlled build pipeline that:
  - validates file types
  - strips unexpected metadata where appropriate
  - computes checksums
- Ensure CORS/hosting is correct (textures/models often need proper origin headers)
- Never embed secrets in `layer.json` (it’s public by design)

---

## 📚 Glossary

- **DEM**: Digital Elevation Model  
- **COG**: Cloud-Optimized GeoTIFF (great for big rasters; partial HTTP reads)  
- **3D Tiles**: A streaming format for large geospatial 3D datasets  
- **glTF/GLB**: Compact 3D model format (GLB is the binary single-file version)  
- **LOD**: Level of Detail (multiple resolutions as you zoom)

---

## 📚 Reference shelf

<details>
<summary><strong>📦 Project reference library used to shape this folder’s standards</strong> (click to expand)</summary>

### Core KFM architecture + mapping
- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf`
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`

### 3D GIS + geospatial context
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`

### Web rendering + UI
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `responsive-web-design-with-html5-and-css3.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### Data infrastructure
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `Database Performance at Scale.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`

### Modeling, stats, and validation discipline
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `graphical-data-analysis-with-r.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`

### Optimization + math foundations
- `Spectral Geometry of Graphs.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`

### Engineering craft + governance + ethics
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### Extra programming reference bundles (project library)
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`
- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf`

</details>

---

### ✨ Next (recommended)
- Add a repo-level validator that:
  - validates `layer.json` shape
  - verifies checksums
  - enforces versioned folders
  - warns on oversized assets
