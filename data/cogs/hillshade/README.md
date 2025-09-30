<div align="center">

# 🌄 Kansas Geo Timeline — Hillshade COGs

**Hillshade raster COGs** for the  
**Kansas Frontier Matrix / Kansas Geo Timeline** stack.  

Hillshade rasters are derived from the **Kansas 1-m bare-earth DEM (2018–2020)** and  
published as **Cloud-Optimized GeoTIFFs (COGs)** for fast, range-read streaming in GIS desktops  
and the MapLibre web viewer.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart LR
  A["DEM COGs\n(data/cogs/dem/**)"] --> B["Derive Hillshade\n(gdaldem hillshade)"]
  B --> C["Hillshade COG\n(data/cogs/hillshade/**)"]
  C --> D["Checksums\n(.sha256)"]
  C --> E["STAC Items\n(stac/items)"]
  C --> F["Web Viewer\n(MapLibre layer)"]
  E --> G["Validate\n(stac validate)"]

<!-- END OF MERMAID -->



⸻

📂 Directory layout

data/cogs/hillshade/
├── ks_hillshade_2018_2020.tif         # main COG
├── ks_hillshade_2018_2020.tif.sha256  # checksum (GNU format)
└── README.md

Project-wide, STAC Items live under stac/items/** and are the source of truth
for metadata (bbox, media type, checksums, etc.).
A separate .meta.json here is optional.

⸻

🧭 Source & processing
	•	Source DEM: Kansas 1-m DEM (2018–2020).
	•	Derivation: gdaldem hillshade (default: -az 315 -alt 45), optionally -multidirectional for softer relief.
	•	CRS (web copy): EPSG:4326 (WGS84).
	•	COG layout: Internal tiles 512×512, overviews down to ~512 px min dimension.
	•	Compression: DEFLATE + PREDICTOR=2.
	•	Integrity: each .tif has a .tif.sha256 sidecar.

⸻

🛠️ Reproducible build

Option A — Makefile targets (recommended)

# Inside repo or project Docker image
make terrain
make stac stac-validate

Option B — Manual GDAL commands

# 1) Produce hillshade from an EPSG:4326 DEM
gdaldem hillshade -alt 45 -az 315 -compute_edges \
  data/cogs/dem/ks_1m_dem_2018_2020.tif \
  /tmp/ks_hillshade_2018_2020.tif

# (Optional) softer shading
# gdaldem hillshade -multidirectional -compute_edges ...

# 2) Convert to COG
gdal_translate -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co BLOCKSIZE=512 -co OVERVIEW_RESAMPLING=AVERAGE \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  /tmp/ks_hillshade_2018_2020.tif \
  data/cogs/hillshade/ks_hillshade_2018_2020.tif

# 3) Write checksum
sha256sum data/cogs/hillshade/ks_hillshade_2018_2020.tif \
  > data/cogs/hillshade/ks_hillshade_2018_2020.tif.sha256

If your DEM is not in EPSG:4326, reproject first (gdalwarp -t_srs EPSG:4326 …).

⸻

🗺️ Web viewer wiring (MapLibre)

Add a layer entry (or generate from STAC):

{
  "id": "ks_hillshade_2018_2020",
  "title": "Hillshade (2018–2020)",
  "type": "raster",
  "data": "data/cogs/hillshade/ks_hillshade_2018_2020.tif",
  "category": "terrain",
  "time": { "start": "2018-01-01", "end": "2020-12-31" },
  "opacity": 0.6,
  "visible": false,
  "attribution": "USGS 3DEP / Kansas DASC (Public Domain)"
}

If served via a tiler/PMTiles, point data (or tiles) to that URL instead of the raw COG.

⸻

🧪 QA / validation

# Checksum verification
sha256sum -c data/cogs/hillshade/ks_hillshade_2018_2020.tif.sha256

# Quick gdalinfo spot check
gdalinfo -checksum data/cogs/hillshade/ks_hillshade_2018_2020.tif | head -n 40

# Optional: validate COG structure
rio cogeo validate data/cogs/hillshade/ks_hillshade_2018_2020.tif


⸻

📌 Notes
	•	Resolution: 1-m grid (with overviews for smooth display at smaller scales).
	•	Extent: Statewide Kansas coverage.
	•	What it is not: Hillshade is a visualization of terrain form only — it does not encode vegetation or structures.
	•	Future: County-level LiDAR hillshades can be added as higher-resolution regional products.

⸻

✅ Mission-grade principle: Hillshade COGs must be fast, verifiable, and fully traceable via STAC —
suitable for both analysis and web visualization.

