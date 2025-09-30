<div align="center">

# 🗺️ Kansas-Frontier-Matrix — DEM COGs (`data/cogs/dem/`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)

**Mission:** Store **Cloud-Optimized GeoTIFFs (COGs)** for **Digital Elevation Models (DEMs)**.  
These rasters power terrain visualizations (hillshade, slope, aspect), time-aware overlays,  
and downstream analysis in the Frontier-Matrix web app + Google Earth integration.  

</div>

---

## 🔄 DEM Lifecycle

```mermaid
flowchart LR
  A["Raw DEM tiles\n(data/raw/dem/**)"] --> B["Mosaic / Reproject\n(gdalbuildvrt · gdalwarp)"]
  B --> C["COG (EPSG:4326)\n(data/cogs/dem/**)"]
  C --> D["Checksums\n(.sha256)"]
  C --> E["STAC Items\n(stac/items)"]
  C --> F["Derivatives\n(hillshade · slope · aspect)"]
  F --> G["Web viewer\n(MapLibre / KML)"]
  E --> H["Validate\n(stac-validate)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/cogs/dem/
├── ks_1m_dem_2018_2020.tif         # statewide mosaic (COG)
├── ks_1m_dem_2018_2020.tif.sha256  # checksum (GNU format)
└── README.md

	•	Project-wide metadata lives in STAC items under stac/items/** (source of truth).
	•	A local .meta.json is optional for extra notes.

⸻

🧭 Conventions
	•	COG layout → internal tiles 512×512, overviews down to ~512 px
	•	CRS (web copy) → EPSG:4326 (WGS84); use projected CRS (e.g. EPSG:26914 UTM 14N, EPSG:6344) for analysis
	•	NoData → set to safe value (e.g., -9999) and record in STAC
	•	Compression → DEFLATE + PREDICTOR=2 for continuous rasters
	•	Integrity → every .tif must have a .tif.sha256 sidecar

Naming convention:

<region>_<resolution>_<theme>_<temporal>.tif

Example: ks_1m_dem_2018_2020.tif
For tiled mosaics, suffix with tile keys (e.g. _w98n39).

⸻

🛠️ Reproducible Build

Option A — Project script

python scripts/convert.py raster-to-cog \
  data/raw/dem/ks_1m_dem_2018_2020.tif \
  data/cogs/dem/ks_1m_dem_2018_2020.tif
# → Writes COG + .sha256

Option B — Canonical GDAL flow

# 1. Build VRT
gdalbuildvrt dem.vrt data/raw/dem/*.tif

# 2. Reproject to UTM (analysis CRS)
gdalwarp -t_srs EPSG:26914 -r bilinear -dstnodata -9999 -multi -wo NUM_THREADS=ALL_CPUS \
  dem.vrt dem_utm14.tif

# 3. Create web copy (WGS84 COG)
gdalwarp -t_srs EPSG:4326 -r bilinear -dstnodata -9999 dem_utm14.tif /tmp/dem_wgs84.tif

gdal_translate -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 \
  -co BLOCKSIZE=512 -co OVERVIEW_RESAMPLING=AVERAGE \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  /tmp/dem_wgs84.tif data/cogs/dem/ks_1m_dem_2018_2020.tif

# 4. Checksum
sha256sum data/cogs/dem/ks_1m_dem_2018_2020.tif \
  > data/cogs/dem/ks_1m_dem_2018_2020.tif.sha256


⸻

🏔️ Derivatives (Terrain Products)

Generate from projected CRS, then COG-ify:

# Hillshade
gdaldem hillshade -az 315 -alt 45 -compute_edges dem_utm14.tif hillshade.tif

# Slope / Aspect
gdaldem slope  dem_utm14.tif slope.tif  -s 1.0
gdaldem aspect dem_utm14.tif aspect.tif

# Publish as COGs
gdal_translate -of COG -co COMPRESS=DEFLATE -co PREDICTOR=2 slope.tif  data/cogs/dem/ks_slope_2018_2020.tif
gdal_translate -of COG -co COMPRESS=DEFLATE -co PREDICTOR=2 aspect.tif data/cogs/dem/ks_aspect_2018_2020.tif

Emit checksums + STAC for each derivative.

⸻

📇 STAC Registration

Record in STAC Item:
	•	datetime or start_datetime–end_datetime
	•	proj:* (EPSG, transform, shape), raster:* (bands, nodata)
	•	file:* (size), checksum:sha256
	•	Processing notes (warp, resampling, compression)
	•	Providers + license

Fast path (Python API):

from kansas_geo_timeline.ingest import ingest_raster
out, item = ingest_raster(
    "data/cogs/dem/ks_1m_dem_2018_2020.tif",
    stac_items_dir="stac/items",
    stac_collection="kfm-dem"
)
print(out, item["id"])

CLI:

make stac stac-validate-items


⸻

🌐 Web & Earth Integration

MapLibre (web viewer):

{
  "id": "ks_1m_dem_2018_2020",
  "title": "DEM (1 m, 2018–2020)",
  "type": "raster-dem",
  "data": "data/cogs/dem/ks_1m_dem_2018_2020.tif",
  "maxzoom": 14,
  "attribution": "USGS 3DEP / Kansas DASC (Public Domain)"
}

Google Earth / KML:
	•	Export regionated KML/KMZ for large extents
	•	Publish WGS84 COGs for visualization
	•	Keep projected CRS copies for analysis

⸻

🧪 Validation & QA

# Verify checksums
find data/cogs/dem -name "*.tif.sha256" -print0 | xargs -0 sha256sum -c

# Inspect metadata
gdalinfo -checksum data/cogs/dem/ks_1m_dem_2018_2020.tif | head -n 40

# Optional: validate COG structure
rio cogeo validate data/cogs/dem/ks_1m_dem_2018_2020.tif

Document in STAC (and .meta.json if used):
	•	Resolution, transform, vertical units/datum
	•	Resampling details (warp, overviews)
	•	NoData handling & void fill notes
	•	Georeferencing accuracy (RMS or equivalent)

⸻

⚡ Performance Tips
	•	Use BLOCKSIZE=512 + internal overviews for fast UX
	•	For heavy clients, publish tiled COGs (quad-key or county)
	•	Keep analysis in projected CRS; publish WGS84 copies for web
	•	For distribution, consider PMTiles (raw COGs remain provenance)

⸻

✅ Checklist (New DEM)
	1.	Build/warp DEM to working CRS; set NoData
	2.	Produce web copy as COG (EPSG:4326)
	3.	Write .tif.sha256 sidecar
	4.	Emit STAC Item + validate
	5.	(Optional) Generate derivatives (hillshade, slope, aspect) → COG + STAC
	6.	Wire into web viewer (raster-dem or hillshade)
	7.	Run validation (sha256sum -c, gdalinfo, optional rio cogeo validate)
	8.	Commit → CI validates & publishes

⸻

✅ Summary

Mission-grade principle: DEM COGs must be fast, verifiable, and fully traceable via STAC.
If it doesn’t validate or display, fix the metadata first, then the data.