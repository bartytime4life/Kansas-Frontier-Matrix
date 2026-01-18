![KFM](https://img.shields.io/badge/KFM-Map%20Overlays-2ea44f) ![Static Assets](https://img.shields.io/badge/assets-static-informational) ![MapLibre](https://img.shields.io/badge/MapLibre-GL%20JS-blue) ![Cesium](https://img.shields.io/badge/CesiumJS-3D%20view-black) ![Provenance](https://img.shields.io/badge/provenance-required-purple)

# 🧩 Map Overlays

**Path:** `web/assets/media/maps/overlays/`

This folder contains **web-shipped** overlay assets that the KFM front-end can load directly (ex: MapLibre 2D overlays, occasional Cesium/3D supporting imagery). Think of an overlay as a **transparent “sheet”** you lay on top of the basemap to show extra context (historic scans, boundaries, thematic rasters, etc.).

> ⚠️ **Keep it lean.** Everything here is shipped with (or alongside) the web app. If it’s huge or “raw,” it likely belongs in `data/` + the pipeline (COGs, vector tiles, STAC), not in this static assets folder.

---

## 🧭 Quick Navigation

- [📦 What goes here vs. not](#-what-goes-here-vs-not)
- [🗂️ Folder layout](#️-folder-layout)
- [🧱 Overlay types](#-overlay-types)
- [🧾 `manifest.json` (required)](#-manifestjson-required)
- [➕ How to add a new overlay](#-how-to-add-a-new-overlay)
- [🛠️ Tiling recipes](#️-tiling-recipes)
- [🧪 QA & quality gates](#-qa--quality-gates)
- [🧯 Troubleshooting](#-troubleshooting)
- [⚖️ Governance, licensing, and ethics](#️-governance-licensing-and-ethics)

---

## 📦 What goes here vs. not

### ✅ Put it here
- **Web-ready overlays** (already optimized/compressed) that should load via a plain URL from the site.
- **Raster XYZ tiles** for scanned historic maps or thematic rasters (with transparency where appropriate).
- **Small** GeoJSON overlays (e.g., a single boundary layer or a curated set of points/lines).
- **Legends & thumbnails** used by the layer catalog UI and Story Nodes (preview images).

### 🚫 Don’t put it here
- Raw GIS exports (gigantic GeoTIFFs, shapefiles, project files, etc.).
- Anything that needs “real” data governance + pipeline lineage but is only being dropped here as a shortcut.
- Large/production datasets that should be served as **COGs / vector tiles / API** and referenced via **STAC/DCAT/PROV**.

> 💡 Rule of thumb: if the overlay will grow, change often, or needs strong lineage → **pipeline + STAC**.  
> If it’s small, stable, and meant as a UI-ready overlay → **this folder**.

---

## 🗂️ Folder layout

Organize overlays by **slug** (kebab-case). One overlay per folder.

```text
📁 web/
└── 📁 assets/
    └── 📁 media/
        └── 📁 maps/
            └── 📁 overlays/
                ├── 📄 README.md
                ├── 📁 railroads-1885/
                │   ├── 📄 manifest.json
                │   ├── 🖼️ legend.png
                │   ├── 🖼️ preview.jpg
                │   └── 📁 tiles/
                │       └── 📁 {z}/{x}/{y}.(png|webp)
                ├── 📁 township-grid/
                │   ├── 📄 manifest.json
                │   ├── 🗺️ data.geojson
                │   └── 🖼️ preview.jpg
                └── 📁 plat-map-1901/
                    ├── 📄 manifest.json
                    ├── 🖼️ image.png
                    ├── 🖼️ legend.png
                    └── 🖼️ preview.jpg
```

### 🏷️ Naming conventions
- **Folder slug:** `kebab-case` (example: `railroads-1885`, `prairie-fires-1930-1950`)
- Prefer `topic-year` or `domain-topic-year` when it helps.
- Avoid spaces and special characters.

---

## 🧱 Overlay types

| Type | Best for | Typical files | Notes |
|---|---|---|---|
| 🧩 **Raster tiles (XYZ)** | scanned maps, thematic rasters | `manifest.json`, `tiles/{z}/{x}/{y}.png|webp` | Recommended for large rasters; supports zoom well |
| 🖼️ **Single image overlay** | small extents, quick prototypes | `manifest.json`, `image.(png|jpg)` | Must include corner coordinates (WGS84) |
| 🗺️ **GeoJSON (small)** | boundaries, points, routes | `manifest.json`, `data.geojson` | Keep small; simplify geometry; WGS84 coords |
| 🧾 **UI assets** | layer UI support | `legend.png`, `preview.jpg` | Legends should be readable; previews should be lightweight |

> ⚠️ Avoid using “full basemap” tiles as overlays (they’ll block the basemap). Overlays should typically be **transparent or sparse** so the basemap still provides context.

---

## 🧾 `manifest.json` (required)

Every overlay folder must include a `manifest.json`.  
This is the **contract** between the asset and the UI: it lets the layer catalog/story system load the overlay, show a human name, define zoom bounds, and (critically) expose provenance.

### ✅ Minimum required fields (recommended)
- `id` (string): stable ID used in UI configs
- `title` (string)
- `type` (enum): `raster-tiles` | `image` | `geojson`
- `spatial.bbox` (WGS84): `[west, south, east, north]`
- `attribution` (object): `text`, `license`, `sourceUrl` (and optional `citation`)
- Display hints (zoom range, opacity defaults)

<details>
<summary>📄 Suggested <code>manifest.json</code> template (copy/paste)</summary>

```json
{
  "id": "railroads-1885",
  "title": "Railroads (1885)",
  "description": "Historic railroad lines & stations compiled from a curated 1885 map scan.",
  "type": "raster-tiles",

  "spatial": {
    "bbox": [-102.051, 36.992, -94.588, 40.003],
    "crs": "EPSG:4326"
  },

  "temporal": {
    "start": "1885-01-01",
    "end": "1885-12-31"
  },

  "display": {
    "defaultOn": false,
    "defaultOpacity": 0.65,
    "minZoom": 5,
    "maxZoom": 12
  },

  "rasterTiles": {
    "tileScheme": "xyz",
    "tileSize": 256,
    "template": "./tiles/{z}/{x}/{y}.webp"
  },

  "attribution": {
    "text": "Kansas Historical Society (example placeholder — replace with real source)",
    "license": "Public Domain (example — verify)",
    "sourceUrl": "https://example.org/source",
    "citation": "See repository CITATION / dataset notes."
  },

  "provenance": {
    "notes": "Describe georeferencing method, control points, transformations, and QA checks.",
    "pipeline": "If generated via scripts, reference the script/path + parameters.",
    "stacItem": "Optional: ../../../../../data/stac/<collection>/<item>.json"
  }
}
```

</details>

### 🧠 Why we’re strict about metadata
KFM is built around **evidence-first** mapping: users should be able to discover “the map behind the map” (source, license, method, limits). The manifest is the first step toward that.

---

## ➕ How to add a new overlay

### 1) Create the overlay folder
```bash
mkdir -p web/assets/media/maps/overlays/<overlay-slug>
```

### 2) Add the overlay asset(s)
Pick one:
- `tiles/{z}/{x}/{y}.(png|webp)`
- `image.(png|jpg)` (georeferenced via corner coords in manifest)
- `data.geojson` (small + simplified)

### 3) Add `manifest.json`
Use the template above and fill in:
- **Attribution + license**
- **BBox**
- **Zoom bounds**
- **Display defaults**

### 4) Add `preview.jpg` and (optionally) `legend.png`
- `preview.jpg`: lightweight screenshot used by the catalog UI
- `legend.png`: for symbology (when applicable)

### 5) Register it with the UI (layer catalog / story nodes)
Depending on how the current web build is wired, overlays are typically “discovered” one of these ways:
- A **Layer Catalog** registry file (JSON) that lists available layers
- A **STAC-driven** catalog that the UI reads
- **Story Node** configs that reference overlay IDs

> 🔍 Practical tip: search the web source for `"layer catalog"`, `"layers"`, `"manifest.json"`, `"overlays/"`, or `addSource(` to find where overlays are registered.

---

## 🧩 Example: loading an overlay in MapLibre (reference snippet)

> ✅ Use **relative** URLs when deploying under a subpath (e.g., GitHub Pages). Prefer `assets/...` (no leading slash) unless your deployment guarantees a root path.

### Raster tiles (XYZ)
```js
map.addSource("railroads-1885", {
  type: "raster",
  tiles: ["assets/media/maps/overlays/railroads-1885/tiles/{z}/{x}/{y}.webp"],
  tileSize: 256,
  minzoom: 5,
  maxzoom: 12
});

map.addLayer({
  id: "railroads-1885",
  type: "raster",
  source: "railroads-1885",
  paint: { "raster-opacity": 0.65 }
});
```

### Single image overlay
```js
map.addSource("plat-map-1901", {
  type: "image",
  url: "assets/media/maps/overlays/plat-map-1901/image.png",
  // order: top-left, top-right, bottom-right, bottom-left
  coordinates: [
    [-102.051, 40.003],
    [-94.588, 40.003],
    [-94.588, 36.992],
    [-102.051, 36.992]
  ]
});

map.addLayer({
  id: "plat-map-1901",
  type: "raster",
  source: "plat-map-1901",
  paint: { "raster-opacity": 0.7 }
});
```

---

## 🛠️ Tiling recipes

### 🗺️ Raster tiles workflow (recommended)
```mermaid
flowchart LR
  A[🧾 Source map scan] --> B[📍 Georeference / rectify]
  B --> C[🧼 Crop + set NoData + add alpha]
  C --> D[🌍 Reproject to EPSG:3857]
  D --> E[🧱 Generate XYZ tiles]
  E --> F[🗜️ Optimize (WebP/PNG) + size checks]
  F --> G[📄 Add manifest + preview/legend]
  G --> H[🧩 Register in UI / Story Node]
```

### Example commands (GDAL-style)
> These are reference commands. Use whichever tooling your pipeline already standardizes on.

```bash
# 1) Reproject and preserve transparency (example)
gdalwarp \
  -t_srs EPSG:3857 \
  -r bilinear \
  -dstalpha \
  -co TILED=YES \
  -co COMPRESS=DEFLATE \
  input_georef.tif warped_3857.tif

# 2) Create XYZ tiles (example)
gdal2tiles.py \
  -p mercator \
  -z 5-12 \
  -w none \
  warped_3857.tif \
  web/assets/media/maps/overlays/<overlay-slug>/tiles
```

### Tile optimization tips 🗜️
- Prefer **WebP** when you can (often much smaller than PNG).
- Limit zoom ranges (`minZoom`, `maxZoom`) to avoid generating millions of tiles.
- Keep overlays **transparent** where possible so the basemap can show through.

---

## 🧪 QA & quality gates

Before you commit an overlay ✅

### Required
- [ ] `manifest.json` exists and is valid JSON
- [ ] Attribution includes **source + license**
- [ ] `spatial.bbox` is correct (WGS84 lon/lat)
- [ ] Overlay loads in the viewer at `minZoom` / `maxZoom`
- [ ] Raster tiles use **XYZ** layout: `{z}/{x}/{y}`

### Strongly recommended
- [ ] `preview.jpg` included (lightweight)
- [ ] `legend.png` included when symbology matters
- [ ] Notes included on georeferencing and processing steps (in `manifest.json` → `provenance.*`)

### Performance sanity checks
- [ ] No accidental “basemap-as-overlay” (opaque tiles that hide the basemap)
- [ ] Tiles/images are compressed and reasonably sized
- [ ] Overlay is cropped to its real extent (don’t ship empty tiles)

---

## 🧯 Troubleshooting

### Overlay is shifted / misaligned
- Common cause: CRS mismatch (EPSG:4326 vs EPSG:3857) or incorrect georeferencing control points.
- Fix: verify the source is correctly georeferenced *before* tiling; ensure the tiler output matches your viewer’s projection expectations.

### Tiles look upside-down / wrong y-axis
- You may have generated **TMS** tiles but the viewer expects **XYZ** (or vice versa).
- Fix: regenerate as XYZ, or configure the viewer accordingly.

### Seams between tiles
- Causes: reprojection artifacts, resampling method, or no padding.
- Fix: try different resampling (`bilinear` vs `cubic`), ensure consistent NoData/alpha, and consider adding a tiny buffer before tiling.

### Overlay works locally but not on GitHub Pages
- Often a base path issue.
- Fix: use **relative** URLs (e.g., `assets/...`) and/or the app’s base-url helper.

---

## ⚖️ Governance, licensing, and ethics

KFM is **provenance-first**:
- Every overlay must have **clear attribution** and a **license**.
- If you’re unsure about usage rights, **do not ship it** here.
- If an overlay intersects with sovereignty/rights concerns (e.g., sensitive cultural locations), follow the project’s governance review gates.

> 🧭 If it’s not explainable, it’s not shippable.  
> (Add sources, methods, limitations, and review notes.)

---

## 🔗 Related docs (repo references)
- 📘 Root project docs: `../../../../..`
- 🌐 Web app root: `../../../..`
- 🧾 Standards & profiles (expected): `../../../../../docs/standards/`
- 🗺️ Data catalogs / STAC (expected): `../../../../../data/stac/`

---

<p align="right"><a href="#-map-overlays">⬆️ Back to top</a></p>
