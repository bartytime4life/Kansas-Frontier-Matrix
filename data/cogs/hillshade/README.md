<div align="center">

# 🌄 Kansas-Frontier-Matrix — Hillshade COGs (`data/cogs/hillshade/`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)

**Mission:** Publish **hillshade raster COGs** derived from the **Kansas 1-m bare-earth DEM (2018–2020)**.  
These COGs enable fast range-read streaming in GIS, MapLibre, and Google Earth,  
powering intuitive terrain visualization across the Frontier-Matrix stack.  

</div>

---

## 🔄 Hillshade Lifecycle

```mermaid
flowchart LR
  A["DEM COGs\n(data/cogs/dem/**)"] --> B["Derive hillshade\n(gdaldem hillshade)"]
  B --> C["Hillshade COG\n(data/cogs/hillshade/**)"]
  C --> D["Checksums\n(.sha256)"]
  C --> E["STAC Items\n(stac/items)"]
  C --> F["Web viewer\n(MapLibre layer)"]
  E --> G["Validate\n(stac-validate)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/cogs/hillshade/
├── ks_hillshade_2018_2020.tif         # statewide hillshade COG
├── ks_hillshade_2018_2020.tif.sha256  # checksum (GNU format)
└── README.md

	•	STAC Items in stac/items/** are the authoritative metadata.
	•	A local .meta.json may be used for extra notes.

⸻

🧭 Source & Processing
	•	Source DEM → Kansas 1-m DEM (2018–2020)
	•	Derivation → gdaldem hillshade (default: -az 315 -alt 45), with optional -multidirectional for softer relief
	•	CRS (web copy) → EPSG:4326 (WGS84)
	•	COG layout → internal tiles 512×512, overviews down to ~512 px
	•	Compression → DEFLATE + PREDICTOR=2
	•	Integrity → every .tif has a .tif.sha256 sidecar

⸻

🛠️ Reproducible Build

Option A — Makefile targets (recommended)

# Inside repo or project Docker image
make terrain
make stac stac-validate

Option B — Manual GDAL commands

# 1. Produce hillshade from an EPSG:4326 DEM
gdaldem hillshade -alt 45 -az 315 -compute_edges \
  data/cogs/dem/ks_1m_dem_2018_2020.tif \
  /tmp/ks_hillshade_2018_2020.tif

# Optional: multidirectional for softer shading
# gdaldem hillshade -multidirectional -compute_edges ...

# 2. Convert to COG
gdal_translate -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co BLOCKSIZE=512 -co OVERVIEW_RESAMPLING=AVERAGE \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  /tmp/ks_hillshade_2018_2020.tif \
  data/cogs/hillshade/ks_hillshade_2018_2020.tif

# 3. Write checksum
sha256sum data/cogs/hillshade/ks_hillshade_2018_2020.tif \
  > data/cogs/hillshade/ks_hillshade_2018_2020.tif.sha256

⚠️ If your DEM is not in EPSG:4326, reproject first (gdalwarp -t_srs EPSG:4326 …).

⸻

🗺️ Web Viewer Integration (MapLibre)

Add as a raster layer (or generate dynamically from STAC):

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

If served via a tiler/PMTiles, point data to that URL instead of the raw COG.

⸻

🧪 QA / Validation

# Checksum verification
sha256sum -c data/cogs/hillshade/ks_hillshade_2018_2020.tif.sha256

# Quick gdalinfo spot check
gdalinfo -checksum data/cogs/hillshade/ks_hillshade_2018_2020.tif | head -n 40

# Optional: validate COG structure
rio cogeo validate data/cogs/hillshade/ks_hillshade_2018_2020.tif


⸻

📌 Notes
	•	Resolution → 1-m grid (overviews smooth display at smaller scales)
	•	Extent → Statewide Kansas coverage
	•	Limitations → Hillshade shows terrain form only (not vegetation/structures)
	•	Future → County-level LiDAR hillshades may be added as higher-resolution regional products

⸻

✅ Summary

Mission-grade principle: Hillshade COGs must be fast, verifiable, and fully traceable via STAC —
suitable for both analysis and web visualization.