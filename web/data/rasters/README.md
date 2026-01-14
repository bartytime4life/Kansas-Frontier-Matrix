# 🧱 `web/data/rasters/` — Web‑Optimized Raster Layers (KFM)

![Raster Tiles](https://img.shields.io/badge/web%20maps-raster%20tiles-0b7285)
![COG](https://img.shields.io/badge/format-COG-2f9e44)
![XYZ](https://img.shields.io/badge/tiles-XYZ%20(z%2Fx%2Fy)-1971c2)
![MapLibre](https://img.shields.io/badge/render-MapLibre%20GL%20JS-3b5bdb)
![Cesium](https://img.shields.io/badge/render-CesiumJS-6741d9)
![Provenance](https://img.shields.io/badge/principle-provenance--first-f59f00)

> **Purpose:** This folder holds **web-facing raster deliverables** for the Kansas Frontier Matrix (KFM) map experience—optimized for *fast loading*, *simple hosting*, and *traceable provenance*.  
> Think: **pre‑tiled imagery overlays**, **hillshades**, **historical scanned maps**, **land cover rasters**, and **small previews** that the UI can load instantly.

---

## 🔎 Quick Links

- [What belongs here](#-what-belongs-here)
- [Recommended folder layout](#-recommended-folder-layout)
- [Raster delivery modes](#-raster-delivery-modes)
- [Naming conventions](#-naming-conventions)
- [Metadata contract](#-metadata-contract)
- [How the web app should reference rasters](#-how-the-web-app-should-reference-rasters)
- [Quality + performance checklist](#-quality--performance-checklist)
- [Project library](#-project-library)

---

## ✅ What belongs here

### ✅ Put these here (web‑ready assets)
- 🧩 **Static XYZ tile pyramids** (`{z}/{x}/{y}.png|jpg|webp`) for *GitHub Pages / CDN‑friendly* hosting.
- 🗺️ **Small “demo” COGs** (Cloud‑Optimized GeoTIFFs) *only if they’re small enough* to ship with the web build.
- 🖼️ **Thumbnails / previews** (for layer picker, hover cards, search results).
- 🎨 **Legends / colormaps** (PNG/SVG) and/or a simple legend JSON.
- 🧾 **Layer metadata JSON** (provenance, attribution, bounds, zoom range, etc.).

### ❌ Don’t put these here (wrong layer of the stack)
> [!IMPORTANT]
> This directory is **web-facing**. Don’t commit giant raw artifacts here.

- 🗃️ Raw scans / unoptimized TIFFs / intermediate processing outputs
- 🔒 Restricted or sensitive rasters
- 🧪 Temporary tiles generated during experimentation
- 🐘 Anything that should live in **`data/raw/`** or **`data/processed/`** (or object storage) instead of `web/`

---

## 🗂️ Recommended folder layout

```text
📁 web/
  └─ 📁 data/
     └─ 📁 rasters/
        ├─ 📄 README.md
        ├─ 📄 layers.index.json          # (optional) UI registry of raster layers
        ├─ 📁 tiles/                     # ✅ static, CDN-friendly XYZ tiles
        │  └─ 📁 <layer_id>/
        │     └─ 📁 {z}/{x}/{y}.(png|jpg|webp)
        ├─ 📁 cogs/                      # ⚠️ only small demo COGs for web builds
        │  └─ 🗺️ <layer_id>.tif
        ├─ 📁 thumbs/                    # previews for UI
        │  └─ 🖼️ <layer_id>.jpg
        ├─ 📁 legends/                   # legend assets (image or svg)
        │  └─ 🎨 <layer_id>.png
        └─ 📁 meta/                      # provenance + display metadata per layer
           └─ 📄 <layer_id>.json
```

> [!TIP]
> If you already have a different registry (e.g., `web/data/layers.json` or a TS config in `web/src/`), keep this folder’s structure **stable** and adapt the registry—not the other way around.

---

## 🚚 Raster delivery modes

KFM supports (and we should design for) **two** delivery paths:

### A) 🧩 Static XYZ tiles (best for GitHub Pages + instant UX)
- ✅ Works on static hosting (no backend needed)
- ✅ Easy to CDN cache (files are immutable and addressable)
- ✅ Smooth performance for “stable” layers (historical topo scans, basemaps, etc.)

**Tile addressing scheme:** `/{z}/{x}/{y}`  
Where `z` is zoom, and `x`,`y` are tile coordinates (a standard slippy-map convention).

### B) 🗺️ COG + dynamic tiles (best for production + huge rasters)
- ✅ Great for multi‑GB imagery when served via a tile endpoint
- ✅ Uses internal tiling + overview pyramids to support partial reads (HTTP range requests)
- ✅ Lets backend generate tiles on demand (and optionally cache)

> [!NOTE]
> The *canonical* COGs should generally live in the data layer (e.g., `data/processed/...` or object storage).  
> `web/data/rasters/cogs/` is for **small demo assets** only.

---

## 🧬 Naming conventions

### Layer IDs
Use **stable**, **URL‑safe** IDs (lowercase, underscores; no spaces):

✅ `historic_topo_usgs_1894`  
✅ `landsat_ndvi_1985_2020`  
✅ `dem_hillshade_30m`  
❌ `USGS Topo (1894)`  
❌ `Topo Map Final FINAL v3`

### Suggested ID schema
`<theme>_<source>_<region?>_<year_or_range?>_<product>_<resolution?>`

Examples:
- `historic_usgs_kansas_1894_scan`
- `landcover_nlcd_kansas_2019_class`
- `climate_prism_kansas_1895_2020_anom`

---

## 🧾 Metadata contract

Every raster layer **must** have a matching metadata file:

📄 `meta/<layer_id>.json`

This is not bureaucracy—this is how we keep KFM **provenance‑first** and prevent “mystery layers”.

<details>
<summary><strong>📌 Minimal JSON template (copy/paste)</strong></summary>

```json
{
  "id": "historic_usgs_kansas_1894_scan",
  "title": "USGS Historical Topo Map (1894)",
  "summary": "Georeferenced scan of a historical topo sheet used as an overlay layer.",
  "type": "raster",
  "delivery": {
    "mode": "xyz",
    "tileUrl": "data/rasters/tiles/historic_usgs_kansas_1894_scan/{z}/{x}/{y}.jpg",
    "tileSize": 256,
    "minZoom": 4,
    "maxZoom": 16
  },
  "spatial": {
    "crs": "EPSG:3857",
    "bbox": [-102.05, 36.99, -94.59, 40.00]
  },
  "temporal": {
    "year": 1894
  },
  "render": {
    "opacityDefault": 0.75,
    "blendMode": "normal"
  },
  "assets": {
    "thumbnail": "data/rasters/thumbs/historic_usgs_kansas_1894_scan.jpg",
    "legend": "data/rasters/legends/historic_usgs_kansas_1894_scan.png"
  },
  "provenance": {
    "sourceName": "USGS",
    "sourceUrl": "",
    "license": "Public Domain (confirm per source)",
    "attribution": "USGS",
    "processing": [
      "Georeferenced + warped to EPSG:3857",
      "Color correction (if applicable)",
      "Generated tile pyramid (z4–z16) + thumbnails"
    ],
    "checksum": {
      "type": "sha256",
      "value": ""
    }
  },
  "tags": ["history", "topo", "basemap", "kansas"]
}
```
</details>

### Metadata rules 🧠
- **Attribution must be UI-ready** (a short string we can display in the layer control).
- **Bounds must be correct** (use the actual data footprint, not “Kansas-ish”).
- **Zoom ranges must be realistic** (don’t ship z0–z22 unless you mean it).
- **Processing must be described** (even if brief) so we can reproduce or audit.

---

## 🧩 How the web app should reference rasters

### MapLibre GL JS (raster tiles)
Example source + layer snippet:

```jsonc
{
  "sources": {
    "historic1894": {
      "type": "raster",
      "tiles": [
        "data/rasters/tiles/historic_usgs_kansas_1894_scan/{z}/{x}/{y}.jpg"
      ],
      "tileSize": 256,
      "attribution": "USGS"
    }
  },
  "layers": [
    {
      "id": "historic1894",
      "type": "raster",
      "source": "historic1894",
      "paint": {
        "raster-opacity": 0.75
      }
    }
  ]
}
```

> [!TIP]
> Prefer **relative paths** (`data/rasters/...`) so the app works on GitHub Pages and local dev without rewriting URLs.

---

## 🧪 Pipeline concept (from raw → web)

```mermaid
flowchart LR
  A[📥 Source raster<br/>scan / remote sensing / model output] --> B[🧭 Georeference / Reproject / QA]
  B --> C[🗺️ Build COG + overviews]
  C --> D{🚚 Delivery}
  D -->|🧩 Static| E[tiles/<layer_id>/{z}/{x}/{y}.*]
  D -->|🧰 Dynamic| F[COG in data/processed or object storage<br/>served via /tiles endpoint]
  E --> G[🗺️ MapLibre raster source]
  F --> G
  G --> H[👤 User loads layer + sees attribution]
```

---

## ⚡ Quality + performance checklist

### 🔍 Raster correctness
- [ ] CRS is known and correct (and recorded in metadata)
- [ ] Data footprint/bounds are correct
- [ ] NODATA is set correctly
- [ ] No “seams” or warping artifacts at common zooms

### 🧊 Speed wins (web UX)
- [ ] Tile size is **256×256** unless there’s a strong reason otherwise
- [ ] Zoom range is intentionally limited (don’t ship unnecessary tiles)
- [ ] Use **JPG/WebP** for photo-like imagery; **PNG** for linework/labels/alpha
- [ ] If using COGs: build an **overview pyramid** (the whole point is fast multiscale)

### 🧾 Provenance + governance
- [ ] `meta/<layer_id>.json` exists
- [ ] Attribution + license fields are filled
- [ ] Processing steps are described
- [ ] Checksums are added for immutable assets (ideal for cache validation + reproducibility)

> [!NOTE]
> For large artifacts, prefer **DVC / LFS** (or store tiles/COGs in object storage + reference them). Keep the repo lean and the web build snappy.

---

## 🔐 Security + privacy notes

- Treat all raster endpoints (even static tiles) like production assets: **no secrets**, no hidden private imagery.
- Avoid committing anything with **restricted licenses** unless explicitly allowed.
- If tiles are served dynamically, ensure inputs are validated (z/x/y bounds, layer IDs) and rate limits are sane.

---

## 📚 Project library

<details>
<summary><strong>📖 Why this folder exists (and what informed it)</strong></summary>

This raster organization aligns with KFM’s documented approach:
- Big rasters are best handled as **COGs** (partial reads + overviews) or **pre-rendered XYZ tiles** (static cache + CDN scale).
- The web front-end is designed to load precomputed artifacts quickly and keep interaction smooth.

</details>

<details>
<summary><strong>📚 PDFs in this repo that are relevant to rasters (browse-friendly reference shelf)</strong></summary>

### 🛰 Remote sensing + raster processing
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `python-geospatial-analysis-cookbook.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`

### 🗺 Cartography + mapping theory
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `Archaeological 3D GIS_26_01_12_17_53_09.pdf`

### 🌐 Web rendering + UX
- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `responsive-web-design-with-html5-and-css3.pdf`

### 🗄 Scale + storage patterns
- `Database Performance at Scale.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`

### 📈 Modeling, statistics, and “raster-as-a-model-output”
- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `graphical-data-analysis-with-r.pdf`

### 🧱 Broader engineering & system references
- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`
- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 🧰 “Programming Books” compendiums (handy quick lookups)
- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

</details>

---

🧭 **Rule of thumb:** If someone can’t answer “Where did this raster come from?” in **30 seconds**, it doesn’t belong in `web/data/rasters/` yet.