# 🌄 Terrain Assets (3D)

![Terrain](https://img.shields.io/badge/3D-Terrain-%23007ACC)
![Cesium](https://img.shields.io/badge/Viewer-CesiumJS-%2300A3E0)
![WebGL](https://img.shields.io/badge/Runtime-WebGL-%23FF6F00)
![CRS](https://img.shields.io/badge/CRS-EPSG%3A4326-%2334A853)
![Provenance](https://img.shields.io/badge/Principle-Provenance--First-%238A2BE2)

This folder holds **web-ready 3D terrain assets** used by the KFM front-end for **2D/3D map experiences** (e.g., MapLibre for 2D + Cesium for 3D). Think of it as the place where “heavy geospatial truth” becomes **streamable, cacheable, and visual** 🧭

---

## ✨ What lives here (and what doesn’t)

### ✅ Belongs here
- **Tilesets** intended to be fetched directly by the browser (or via CDN).
- **Derived terrain products**: hillshade textures, color-relief textures, normal maps, low/med-res heightfields.
- **3D streaming formats** (e.g., **3D Tiles**, quantized mesh terrain) plus minimal metadata.
- **Small sample regions** for local dev/test (kept intentionally tiny).

### 🚫 Does NOT belong here
- Raw source DEMs/LiDAR (multi-GB GeoTIFF/LAZ) ❌  
- “Mystery layers” with no source/license/provenance ❌  
- Anything that can’t be rebuilt or verified ❌  
- Personally sensitive or restricted datasets ❌

> 🔎 Rule of thumb: **If the browser can’t stream it efficiently, it doesn’t belong here.**  
> Put raw + heavy stuff in the data/pipeline side, and publish only the web-friendly outputs here.

---

## 🧠 Design principles (KFM style)

- **Provenance-first** 🧾: every tileset should be traceable to a source + processing steps.
- **Contract-first** 📜: terrain assets ship with metadata that is “validation-friendly”.
- **Streamable by default** ⚡: favor tiling schemes & formats that support partial reads and LOD.
- **CRS consistency** 🧭: serve web layers consistently to avoid alignment drift.
- **Performance budgets** 🧊: a beautiful terrain that tanks FPS is… not beautiful.

---

## 🗂️ Folder layout (recommended)

> Your repo may vary—this is the **target contract** for how terrain packs should look.

```text
web/assets/3d/terrain/
├── 📘📄 README.md                         # 📘 you are here 📌
├── 🧾🗂️ manifest.json                     # 🧾 index of available terrain packs
├── 🖼️ previews/                          # 🖼️ thumbnails / quicklook PNG/JPG
│   └── 🖼️ kansas-dem-10m.jpg
├── 📦 packs/                             # 📦 versioned terrain “products”
│   ├── 🌾 kansas-dem-10m_v1/             # 🌾 statewide baseline terrain
│   │   ├── 🧱🧾 tileset.json              # 🧱 (3D Tiles entrypoint) OR terrain.json
│   │   ├── 🧩 tiles/                     # 🧩 tile payloads (batched or per-tile)
│   │   ├── 🎨 textures/                  # 🎨 drape/hillshade/color-relief
│   │   └── 🧾📜 meta.json                 # 🧾 provenance + CRS + units + bounds
│   └── 🦬 flint-hills-lidar-1m_v1/       # 🦬 high-res focused region
│       ├── 🧱🧾 tileset.json
│       ├── 🧩 tiles/
│       ├── 🎨 textures/
│       └── 🧾📜 meta.json
└── 🧪 schema/                            # 🧪 optional JSON schemas (if enforced)
    ├── 📐🧾 manifest.schema.json
    └── 📐🧾 meta.schema.json
```

---

## 🧱 Terrain Pack Contract

Every terrain pack **must** have:

1. **Entrypoint**
   - `tileset.json` (3D Tiles) **or**
   - `terrain.json` / equivalent (quantized-mesh terrain provider)

2. **Metadata**
   - `meta.json` with (at minimum):
     - `id`, `title`, `version`
     - `source` (who/where it came from)
     - `license`
     - `crs` (horizontal CRS) + `vertical_units`
     - `bbox` (WGS84) + `min_elev` / `max_elev`
     - `processing` (pipeline summary + parameters)

3. **Preview**
   - `previews/<id>.jpg` (fast sanity check for humans)

---

## 🌐 CRS, units, and “why my terrain is floating”

### ✅ Preferred serving standard
- **Horizontal CRS**: **WGS84 (EPSG:4326)** for web consistency.
- **Vertical units**: **meters** (unless explicitly declared otherwise).

### Required metadata fields (minimum)
- `crs`: `"EPSG:4326"` (or clearly declare otherwise)
- `vertical_units`: `"m"` or `"ft"`
- `vertical_datum`: e.g., `"NAVD88"` / `"EGM96"` / `"unknown"`
- `source_crs`: what it originally came in as (for traceability)

> 🧨 Most “broken terrain” bugs are actually CRS/unit bugs.

---

## 🧩 Formats we support

### 3D geometry / streaming
- **3D Tiles** (`tileset.json` + tile payloads) 🧱
- **Quantized-mesh terrain** (Cesium terrain providers) 🗻
- **glTF** (only when you truly need explicit meshes) 🧊

### Raster textures
- **JPG** for drape + hillshade (small + fast) 🖼️
- **PNG** when you need alpha (labels, masks) 🧼
- Optional: **normal maps** for lighting polish 💡

### Metadata
- `manifest.json`, `meta.json` (JSON, validated) ✅

---

## 🏗️ Build pipeline (source ➜ web terrain)

Below is a **repeatable mental model** for building terrain products. Your actual tooling may vary (GDAL/rasterio/GEE/etc.)—the important part is the **stages**.

### 1) Ingest & normalize
- Validate input DEM/DSM/DTM
- Reproject (if needed) to serving CRS
- Clip to region of interest
- Decide your nodata strategy (mask vs fill)

### 2) Produce visualization textures (optional but recommended)
Common terrain derivatives:
- **Hillshade** (lighting relief) 💡
- **Color relief / hypsometric tint** 🎨
- **Slope / aspect** (analysis + styling) 📐

Example commands (illustrative):
```bash
# Reproject + clip
gdalwarp -t_srs EPSG:4326 -cutline region.geojson -crop_to_cutline input_dem.tif dem_wgs84.tif

# Hillshade
gdaldem hillshade dem_wgs84.tif hillshade.tif -z 2 -az 315 -alt 45

# Color relief
gdaldem color-relief dem_wgs84.tif color_ramp.txt color_relief.tif

# Web texture
gdal_translate -of JPEG -co QUALITY=90 hillshade.tif hillshade.jpg
```

### 3) Build streaming terrain
Choose one:
- **Quantized mesh terrain** for globe-style terrain providers 🌍
- **3D Tiles** when you want unified streaming for terrain + other 3D layers 🧱

Then:
- Generate LOD pyramid / tiling
- Compress payloads (where appropriate)
- Emit `tileset.json` (or terrain provider JSON)
- Emit `meta.json`

### 4) QA gate (non-negotiable)
Before committing:
- Validate metadata schema ✅
- Confirm bbox + min/max elevation ✅
- Visual smoke test (2D + 3D) ✅
- Performance sanity: tile sizes + FPS ✅

---

## ✅ QA checklist (PR-ready)

- [ ] `meta.json` present and complete  
- [ ] Source + license explicitly stated  
- [ ] CRS + units correct (and match rendering)  
- [ ] No obvious seams between tiles  
- [ ] No “striping” artifacts from resampling  
- [ ] Preview image added (`previews/`)  
- [ ] Tile payload sizes reasonable (avoid giant single-tile blobs)  
- [ ] Works in both:
  - [ ] local dev (no CDN required)
  - [ ] production path (cache-friendly URLs)

---

## ⚡ Serving & performance notes

- Prefer **static-file hosting** + CDN caching for stable terrain packs 🧊
- Use **versioned folder names** (`*_v1`, `*_v2`) to make cache invalidation painless
- Keep textures optimized:
  - JPG for photographic drape/hillshade
  - PNG only when you need alpha
- LOD matters: use lower-res terrain when zoomed out; load higher-res only when needed 🔍

---

## 🔒 Security, privacy, and licensing

Terrain is “just elevation”… until it isn’t.

- **License clarity** is mandatory (datasets can be public, restricted, non-commercial, etc.)
- If terrain is derived from sensitive inputs, do not publish derived outputs here
- Avoid unnecessary server fingerprinting in production hosting (keep the static server boring 😴)
- Treat metadata as user-facing truth: don’t overclaim accuracy you can’t justify

> 🌱 Digital Humanism lens: prioritize human values, privacy, and responsible use—especially when terrain layers are combined with other datasets that can infer sensitive information.

---

## 🧩 Integration hints (front-end)

### Cesium (3D)
Typical patterns:
- Terrain as a **terrain provider** (globe elevation)
- Terrain as a **3D Tiles tileset** (streamed 3D content)

Pseudo-example:
```ts
// NOTE: adapt to your actual viewer setup
const tilesetUrl = "/assets/3d/terrain/packs/kansas-dem-10m_v1/tileset.json";
viewer.scene.primitives.add(new Cesium.Cesium3DTileset({ url: tilesetUrl }));
```

### MapLibre (2D)
Terrain derivatives like hillshade/color relief can be added as raster layers, and used for:
- context relief
- storytelling overlays
- QA previews of your DEM pipeline

---

## 🧯 Troubleshooting

### “Terrain doesn’t line up with my vector layers”
- CRS mismatch (source CRS not reprojected)
- Bounding box/extent mismatch
- Axis order confusion (lat/lon vs lon/lat)

### “Terrain looks spiky / noisy”
- Wrong nodata handling
- Resampling artifacts (nearest vs bilinear vs cubic)
- Vertical exaggeration too high

### “Seams between tiles”
- Inconsistent resampling at tile edges
- Missing overlap / skirt strategy
- LOD mismatch or incorrect tile bounds

---

## 🧭 Roadmap (nice upgrades)

- 🗺️ Standardize `meta.json` against project-wide dataset contracts
- 🧱 Add optional `schema/` folder + CI validation for terrain metadata
- 🧊 Introduce modern GPU texture compression for large drape layers (where supported)
- 🧪 Add automated visual regression tests (snapshot camera positions)
- 🧬 Expand analysis products (slope/aspect/curvature) for modeling & research workflows

---

## 📚 Reference shelf (project library map)

<details>
<summary><b>Open the library map 📚</b></summary>

### 🛰️ GIS / Remote sensing / Terrain processing
- *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation*
- *Cloud-Based Remote Sensing with Google Earth Engine – Fundamentals and Applications*
- *Python Geospatial Analysis Cookbook*
- *Making Maps: A Visual Guide to Map Design for GIS*
- *Mobile Mapping: Space, Cartography and the Digital*
- *Archaeological 3D GIS*

### 🧱 Web 3D / Rendering / Geometry
- *WebGL Programming Guide: Interactive 3D Graphics Programming with WebGL*
- *Responsive Web Design with HTML5 and CSS3*
- Programming bundles (*A*, *B–C*, *D–E*, *F–H*, *I–L*, *M–N*, *O–R*, *S–T*, *U–X*)

### ⚙️ Modeling / Simulation / Scientific rigor
- *Scientific Modeling and Simulation: A Comprehensive NASA-Grade Guide*
- *The Scientific Method and Protocol Design: Reproducible Science for the Experimental Sciences*

### 📊 Statistics / ML / Analysis (terrain as a feature space)
- *Understanding Statistics & Experimental Design*
- *Regression Analysis with Python*
- *Think Bayes: Bayesian Statistics in Python*
- *Understanding Machine Learning*
- *Graphical Data Analysis with R*

### 🗃️ Data architecture / scale / storage
- *Database Performance at Scale*
- *Scalable Data Management for Future Hardware*
- *Data Spaces*
- *PostgreSQL Notes for Professionals*

### 🔐 Security / governance / ethics
- *Introduction to Digital Humanism*
- *On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age*
- *Ethical Hacking and Countermeasures: Secure Network Infrastructures*

### 🧠 Bonus theory & future-facing tools
- *Spectral Geometry of Graphs*
- *Generalized Topology Optimization for Structural Design*
- *Principles of Biological Autonomy*

</details>

---

**Owner:** `web/` front-end + GIS pipeline contributors  
**Scope:** web-ready terrain products only ✅  
**Golden rule:** _If it ships to the browser, it needs provenance + performance + predictable structure._ 🌾
