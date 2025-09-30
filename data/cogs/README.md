<div align="center">

# 🛰️ Kansas-Frontier-Matrix — Cloud-Optimized GeoTIFFs (`data/cogs/`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

**Mission:** Hold **validated Cloud-Optimized GeoTIFFs (COGs)** — the canonical raster products  
used for terrain, overlays, and analysis in the Frontier-Matrix stack.  

Every file here must be **reproducible, HTTP-friendly, checksummed, and STAC-registered**.  

</div>

---

## 🔄 Lifecycle

```mermaid
flowchart LR
  A["Raw rasters\n(data/raw/)"] --> B["Processing\n(reproject / clean)"]
  B --> C["COGs\n(data/cogs/**.tif)"]
  C --> D["Checksums\n(.sha256)"]
  C --> E["STAC Items\n(stac/items)"]
  E --> F["Validate\n(stac-validate)"]
  C --> G["Tiles / PMTiles\n(data/tiles)"]
  G --> H["Web Viewer\n(MapLibre)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/cogs/
├── dem/          # canonical DEM rasters
├── hillshade/    # derived hillshade rasters
└── overlays/     # historic maps, scanned overlays

Each raster must have:
	•	✅ Cloud-Optimized layout (internal tiling + overviews)
	•	✅ CRS = EPSG:4326 (unless documented otherwise)
	•	✅ .sha256 sidecar (GNU format)
	•	✅ STAC Item under stac/items/

⸻

🏷️ Naming Convention

<theme_or_region>*<detail>*<temporal>.tif

Examples:
	•	ks_1m_dem_2018_2020.tif
	•	ks_hillshade_2018_2020_multidir.tif
	•	usgs_topo_larned_1894.tif

⸻

⚙️ Conversion to COG

Using Project Script

python scripts/convert.py raster-to-cog \
  data/raw/maps/usgs_topo_larned_1894_raw.tif \
  data/cogs/overlays/usgs_topo_larned_1894.tif

Direct GDAL (DEM example)

gdal_translate -of COG \
  -co COMPRESS=DEFLATE -co PREDICTOR=2 -co BLOCKSIZE=512 \
  -co NUM_THREADS=ALL_CPUS -co BIGTIFF=IF_SAFER \
  input_dem_wgs84.tif data/cogs/dem/ks_1m_dem_2018_2020.tif

Scripts automatically:
	•	reproject to EPSG:4326
	•	build overviews
	•	generate checksums

⸻

🌐 CRS Guidance
	•	Default: EPSG:4326 (WGS84) for web/viewer layers
	•	Kansas DEMs: often UTM Zone 14N (EPSG:26914 / EPSG:6344)
	•	Always document reprojection in STAC proj:epsg

⸻

📑 STAC Registration

Generate STAC Items after conversion:

make stac stac-validate-items

Each item must include:
	•	assets.tiles.href → COG path
	•	checksum:sha256 → from sidecar
	•	proj:epsg → final CRS

⸻

🌍 Web Integration

Example raster layer config:

{
  "id": "usgs_topo_larned_1894",
  "title": "USGS Topo (Larned, 1894)",
  "type": "raster",
  "data": "data/cogs/overlays/usgs_topo_larned_1894.tif",
  "time": { "start": "1894-01-01", "end": "1894-12-31" },
  "opacity": 0.8,
  "visible": false,
  "attribution": "USGS (Public Domain)"
}


⸻

🧪 Validation

# Verify checksums
sha256sum -c data/cogs/**/*.sha256

# Inspect metadata
gdalinfo data/cogs/dem/ks_1m_dem_2018_2020.tif | head -n 40

# Confirm COG compliance
rio cogeo validate data/cogs/overlays/usgs_topo_larned_1894.tif


⸻

📋 Checklist for New Rasters
	1.	Convert to COG under data/cogs/<subdir>/<name>.tif
	2.	Write checksum sidecar <name>.tif.sha256
	3.	Generate STAC Item (make stac)
	4.	Add to web config if needed
	5.	Validate with sha256sum, gdalinfo, and rio cogeo
	6.	Commit → CI enforces STAC + checksum

⸻

✅ Summary

data/cogs/ is the canonical home for rasters:
Cloud-Optimized, checksummed, documented, and STAC-discoverable.

They form the bridge between raw inputs and derivative products/tiles,
ensuring the Frontier-Matrix stack remains mission-grade, reproducible, and auditable.