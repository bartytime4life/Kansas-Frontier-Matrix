<!-- According to a document from 2026-01-14, KFM relies on Cloud-Optimized GeoTIFFs (COGs) and can pre-render XYZ tiles for heavy/stable layers; this README operationalizes that approach for the web front-end.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) -->

# 🧩 Tiles (`web/data/tiles`)

![Tiles](https://img.shields.io/badge/tiles-XYZ%20%7C%20MVT%20%7C%20COG-blue)
![Hosting](https://img.shields.io/badge/hosting-static%20(GitHub%20Pages)%20friendly-success)
![Cache](https://img.shields.io/badge/cache-CDN%20ready%20%7C%20versioned-informational)
![Frontend](https://img.shields.io/badge/frontend-MapLibre%20GL%20JS-orange)
![Data](https://img.shields.io/badge/metadata-STAC%20%2B%20PROV--O%20mindset-purple)

> ⚡ **Goal:** make the KFM web viewer fast + reproducible by shipping **web-ready tiles** as static assets (no custom server required).  
> The platform prototype is designed as a static site (GitHub Pages) using MapLibre/Leaflet, and heavy layers are expected to be delivered as tiles/COGs.  [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA) [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H) [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧠 What this folder is (and isn’t)

### ✅ What belongs here
- **🧱 Extracted XYZ tile pyramids** (raster or vector)
- **📦 Packaged tilesets** (optional): `.pmtiles` / `.mbtiles` (when that’s the best delivery unit)
- **🧾 Tile descriptors** (`tilejson.json`) + lightweight `metadata.json`
- **🎨 Shared map assets** (optional): sprites / glyphs used by the MapLibre style
- **🖼️ Tiny previews** (optional): `preview.png` for docs/UI

### 🚫 What does *not* belong here
- Raw sources (scanned maps, original shapefiles, bulk downloads)
- Intermediate processing outputs (scratch rasters, temp GeoJSON, notebooks)
- Anything without **license + attribution + provenance** recorded

KFM’s data approach treats “web artifacts” (tiles, KML/KMZ) as *products generated* from standardized, traceable pipelines.  [oai_citation:4‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

---

## 🚀 Why tiles live under `web/`

KFM’s mapping stack is designed so the **front-end can be hosted as static files** (HTML/JS/CSS + JSON) and still deliver performant maps.  [oai_citation:5‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA) [oai_citation:6‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

### Performance + scale
- **COGs** enable partial reads over HTTP range requests (fetch *just* what’s needed for the view).  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- For **very frequently accessed layers**, KFM can **pre-render XYZ tiles** and serve them as static files via a server/CDN (storage-for-speed trade).  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- **Level-of-detail management** is essential: don’t draw every feature at every zoom. Serve generalized data (or gate layers by zoom).  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Cartography reality check
Maps are **generalizations**. Design choices depend on **scale** and what users can realistically interpret at each zoom. 

---

## 📦 Recommended folder layout

> This layout is intentionally “static-hosting-first” (works on GitHub Pages/CDN). Adjust as the repo evolves.

```text
web/data/tiles/
├─ 📄 README.md
│
├─ ✅🧾 tilesets.json                 # ✅ single index the app can read (catalog of tilesets)
│
├─ 📁🧭 vector/
│  └─ 🛣️ ks-roads/
│     ├─ 🧾 tilejson.json
│     ├─ 🧾 metadata.json
│     ├─ 🖼️ preview.png              # optional
│     └─ 🧱📦 {z}/{x}/{y}.pbf          # MVT (pbf), usually gzip/brotli in hosting layer
│
├─ 🗺️🧱 raster/
│  └─ 🕰️🗺️ historic-topo-1890/
│     ├─ 🧾 tilejson.json
│     ├─ 🧾 metadata.json
│     └─ 🖼️🧱 {z}/{x}/{y}.webp         # or .png
│
├─ 📦 packages/
│  ├─ 🧰🗺️ ks-landcover_v20260114.pmtiles
│  └─ 🗃️🗺️ ks-hillshade_v20260114.mbtiles
│
├─ 🎨 sprites/                       # optional: MapLibre sprite sheets
│  ├─ 🧾 sprite.json
│  ├─ 🖼️ sprite.png
│  ├─ 🧾 sprite@2x.json
│  └─ 🖼️ sprite@2x.png
│
└─ 🔤 fonts/                         # optional: MapLibre glyphs
   └─ 🔤📦 {fontstack}/{range}.pbf
```

**Why an index file?**  
So the UI can list layers (name, bounds, min/max zoom, attribution) without hardcoding. This aligns with KFM’s “data catalog” mindset (structured metadata, traceability).  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:12‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw)

---

## 🧾 Tileset contract

Each tileset folder (or package) must have **two small JSON files**:

### 1) `tilejson.json` (delivery contract)
A standard TileJSON descriptor that MapLibre can consume.

### 2) `metadata.json` (governance + provenance)
KFM expects rigorous metadata (license, provenance concepts, etc.).  [oai_citation:13‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

#### `metadata.json` minimum fields (recommended)
| Field | Required | Example | Why it matters |
|---|:---:|---|---|
| `id` | ✅ | `"historic-topo-1890"` | stable identifier |
| `title` | ✅ | `"USGS Topo (1890 edition)"` | UI label |
| `type` | ✅ | `"raster"` / `"vector"` | rendering pipeline |
| `format` | ✅ | `"webp"` / `"mvt"` / `"pmtiles"` | client expectations |
| `bounds` | ✅ | `[-102.05,36.99,-94.59,40.00]` | map fit + validation |
| `minzoom` / `maxzoom` | ✅ | `6` / `14` | LOD + performance |
| `attribution` | ✅ | `"USGS …"` | legal + ethical |
| `license` | ✅ | `"Public Domain"` / `"CC-BY-4.0"` | must be explicit |
| `sources` | ✅ | `["data/catalog/…"]` | link to catalog entry |
| `provenance` | ✅ | `{ "prov": … }` | reproducibility |
| `build` | ✅ | `{ "tool": "tippecanoe", "git": "abc123", "date": "2026-01-14" }` | audit trail |

KFM’s metadata approach explicitly calls out STAC, PROV concepts, and enforcing license presence in dataset metadata.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧭 Projection & coordinates

### Display & interchange
- **GeoJSON defaults to WGS84 / EPSG:4326** (lat/lon).  [oai_citation:15‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)
- KFM’s internal standard is **WGS84 (EPSG:4326)** for consistency; datasets are **reprojected on ingest** and original CRS is recorded in provenance/metadata.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### Practical note for tiles
Even if source data is WGS84, **slippy-map tiles** are typically generated into an XYZ grid for web mapping. Treat the XYZ grid as the delivery mechanism, and keep CRS truth in `metadata.json`.

---

## 🗺️ Raster vs Vector (choosing the right tile type)

Use this quick heuristic:

- **Raster tiles** ✅ when the layer is an image (scanned historic maps, hillshade, continuous rasters).  
- **Vector tiles** ✅ when the layer is interactive/semantic (roads, rivers, boundaries, points of interest).

Vector and raster data support different kinds of analysis and interaction; pick based on your intended use and scale. 

---

## 🧱 Versioning, caching, and “don’t break URLs”

### Rule of thumb
> If users might cache it, **version it**.

Examples:
- `ks-landcover_v20260114.pmtiles`
- `historic-topo-1890_v2/{z}/{x}/{y}.webp`
- `ks-roads_sha1-3f9c…/{z}/{x}/{y}.pbf`

Versioned filenames prevent stale caches and make CDN caching safe.  [oai_citation:17‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)

### CI & visual regression
Automated tests can’t catch every cartographic regression, so build pipelines should include **tile sanity checks** and, ideally, **visual diffs** (small sample areas/zooms).  [oai_citation:18‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)

> ⚠️ **Large tiles are large.**  
> If a tileset is too big for regular Git, consider a data-management layer (e.g., DVC/Git LFS) and keep only lightweight pointers/metadata in the main history.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧩 Serving modes

This folder supports 3 common delivery patterns:

### 1) Static XYZ folders (GitHub Pages/CDN) ✅
Best for: stable rasters, smaller vector sets, guaranteed simplicity.

### 2) Packaged tilesets (PMTiles/MBTiles) 📦
Best for: single-file distribution, offline-ish use, simpler artifact management.

The design allows TileJSON/MBTiles “for convenience,” with the MapLibre front-end fetching via HTTP.  [oai_citation:20‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

### 3) COG-first (range requests) 🛰️
Best for: huge rasters where you want partial reads instead of massive tile pyramids.

KFM emphasizes converting large rasters to COGs to enable efficient access and reduce bandwidth.  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧑‍💻 MapLibre integration examples

### Vector (TileJSON)
```json
{
  "id": "ks_roads",
  "type": "vector",
  "url": "/data/tiles/vector/ks-roads/tilejson.json"
}
```

### Raster (direct XYZ template)
```json
{
  "id": "historic_topo_1890",
  "type": "raster",
  "tiles": ["/data/tiles/raster/historic-topo-1890/{z}/{x}/{y}.webp"],
  "tileSize": 256,
  "attribution": "…"
}
```

MapLibre GL JS is explicitly called out as the high-performance browser renderer for vector tiles + raster layers in KFM’s web stack.  [oai_citation:22‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

---

## 🧪 QA & release checklist

Before committing a tileset:

- [ ] **TileJSON loads** and has correct `tiles`, `bounds`, `minzoom`, `maxzoom`
- [ ] **Attribution + license** present in `metadata.json`
- [ ] **Provenance link** points back to catalog/source entry
- [ ] **Zoom gating makes sense** (don’t overload low zooms)
- [ ] **Spot-check alignment** vs a known reference layer
- [ ] **Size sanity** (don’t accidentally ship a 50GB pyramid)
- [ ] **CI sample build** + optional visual diff passes  [oai_citation:23‡I-L programming Books.pdf](file-service://file-T9sYu87k1GPNNKMLddx41a)

Also remember: map layers are models/generalizations with error—track accuracy where possible. 

---

## 🔐 Governance & trust

Tiles are *products*, not just files:
- metadata is a contract
- provenance is non-negotiable
- licenses and lineage enable reuse

This matches a “data trust / governance” framing: clear rules, roles, processes, and quality signals. 

---

## 🧯 Troubleshooting

### “Tiles 404”
- Confirm `tilesets.json` lists the tileset
- Confirm paths are correct relative to the built site root (GitHub Pages-friendly)
- Prefer relative URLs where possible

### “Layer is misaligned”
- Confirm ingest reprojection to WGS84 and record original CRS (don’t silently mix projections).  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- If you’re loading raw GeoJSON, validate it’s in WGS84 bounds (lon/lat).  [oai_citation:25‡python-geospatial-analysis-cookbook.pdf](file-service://file-HT14njz1MhrTZCE7Pwm5Cu)

### “The map is slow”
- Gate the layer by zoom / simplify geometry
- For heavy rasters, prefer COG-first or pre-render tiles for stable base layers.  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 📎 Project docs used to shape this README (clickable)

-  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) — KFM Technical Documentation (COGs, tiling/caching, projections, metadata standards)  
-  [oai_citation:28‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-64djFYQUCmxN1h6L6X7KUw) — KFM Open-Source Mapping Hub Design (static GitHub Pages + MapLibre, tiles/KML)  
-  [oai_citation:29‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP) — Making Maps (scale, generalization, vector vs raster)  
-  [oai_citation:30‡Database Performance at Scale.pdf](file-service://file-36z8qyiVJRtrSs6QG7Epen) — Cloud-Based Remote Sensing with Google Earth Engine (accuracy mindset)  
-  [oai_citation:31‡Data Spaces.pdf](file-service://file-7UnZyJ7eCK1egnsyuYJaFq) — Data Spaces (governance/trust framing)  
-  [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) — B‑C Programming Books (CI + versioned static assets guidance)

---

## 📚 Full project library crosswalk (how everything connects) 🔍

<details>
<summary><strong>Expand: “All project files” → how they inform tiles & web delivery</strong></summary>

### 🗺️ Mapping, geospatial & visualization
- **making-maps-a-visual-guide-to-map-design-for-gis.pdf** → scale, generalization, symbolization, “what belongs at what zoom”
- **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf** → mobile constraints, context-aware mapping UX
- **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf** → GPU/WebGL performance mental model (MapLibre is WebGL-based)
- **Archaeological 3D GIS_26_01_12_17_53_09.pdf** → 3D layer thinking (future: terrain/3D Tiles)
- **python-geospatial-analysis-cookbook.pdf** → reprojection, GeoJSON assumptions, geoprocessing recipes
- **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf** → remote sensing pipelines + accuracy habits
- **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** → raster tile format tradeoffs (PNG/WebP/JPEG)

### 🧱 Data platforms, storage, performance
- **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** → PostGIS-backed queries that may feed tile builds
- **Database Performance at Scale.pdf** → caching/indexing patterns applicable to tile endpoints/CDN behavior
- **Scalable Data Management for Future Hardware.pdf** → “performance is an architecture decision” mindset (batch builds, query costs)
- **Data Spaces.pdf** → governance + trust model for tile products (metadata, lineage, quality signals)

### 🧪 Modeling, statistics, QA, and uncertainty
- **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf** → verification/validation mindset for derived products
- **Understanding Statistics & Experimental Design.pdf** → experiment design for QA sampling + comparisons
- **regression-analysis-with-python.pdf** + **Regression analysis using Python - slides-linear-regression.pdf** → analytics pipeline patterns (not tiles directly)
- **think-bayes-bayesian-statistics-in-python.pdf** → uncertainty communication (future: confidence layers / model outputs)

### 🧠 Algorithms & advanced math (future analysis layers → future tiles)
- **Spectral Geometry of Graphs.pdf** → graph/network layers (roads/rivers) and derived metrics that could be tiled
- **Generalized Topology Optimization for Structural Design.pdf** → optimization mindset for resource-constrained rendering
- **Principles of Biological Autonomy - book_9780262381833.pdf** → systems thinking / autonomy metaphors for “data product” design

### 🌐 Web + engineering + governance
- **responsive-web-design-with-html5-and-css3.pdf** → responsive UI constraints + performance budgets (tiles are payload)
- **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf** → background processing mental model (pipelines/builds)
- **Introduction to Digital Humanism.pdf** → human-centered constraints and ethics for public-facing mapping
- **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf** → governance + transparency expectations
- **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** → secure hosting posture (static is safer; watch supply chain)
- **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf** → security awareness (defensive mindset only)

### 📚 “Programming Books” mega-files (repo-wide engineering practices)
- **A programming Books.pdf**
- **B-C programming Books.pdf**
- **D-E programming Books.pdf**
- **F-H programming Books.pdf**
- **I-L programming Books.pdf**
- **M-N programming Books.pdf**
- **O-R programming Books.pdf**
- **S-T programming Books.pdf**
- **U-X programming Books.pdf**

### 🤖 (Note) Not indexed by file browser
- **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf** → offline ML pipelines that may generate map layers later

</details>
