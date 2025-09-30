<div align="center">

# 🏔️ Kansas Geo Timeline — Processed DEMs

This folder contains **Digital Elevation Model (DEM) derivatives**  
processed from raw sources (e.g., USGS 3DEP 1-m DEMs, LiDAR tiles, statewide mosaics).  

All outputs are **reproducible** from `data/raw/` using Makefile targets + scripts  
and are referenced in the **STAC catalog** (`data/stac/items/dem/*.json`).  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Raw DEM tiles\n(data/raw/dem/**)"] --> B["Mosaic + Reproject\n(gdalwarp → EPSG:4326)"]
  B --> C["COG Conversion\n(rio cogeo / gdal_translate)"]
  C --> D["Processed DEMs\n(data/processed/dem/**)"]
  D --> E["Derivatives\n(slope · aspect · hillshade)"]
  E --> F["Overlays\n(color relief, blends)"]
  D --> G["Checksums + Meta\n(.sha256 · .meta.json)"]
  G --> H["STAC Items\n(data/stac/items/dem/**)"]
  H --> I["Validate\n(stac-validate)"]
  I --> J["Viewer + KML\n(web configs · data/kml/)"]

<!-- END OF MERMAID -->



⸻

📂 Typical contents

data/processed/dem/
├── ks_1m_dem_2018.tif             # statewide DEM (2018 mosaic, COG)
├── ks_1m_dem_2020.tif             # statewide DEM (2020 update, COG)
├── ks_1m_dem_2018_hillshade.tif   # hillshade derivative
├── ks_1m_dem_2018_slope.tif       # slope raster
├── ks_1m_dem_2018_aspect.tif      # aspect raster
├── overlays/                      # styled blends (color-relief, tinted hillshades)
└── hillshade_color.tif

	•	DEM rasters → Cloud-Optimized GeoTIFFs (COGs) with overviews.
	•	Derivatives → slope, aspect, hillshade, TRI/TPI, roughness.
	•	Overlays → styled rasters (color relief, blends) for web & KMZ exports.

⸻

🔄 Workflow
	1.	Fetch raw DEMs → data/raw/
	•	USGS 3DEP / Kansas GIS Hub.
	•	Mosaicked into county/statewide extents.
	•	Record year, resolution, source CRS.
	2.	Mosaic & reproject → EPSG:4326 (web copy).

gdalwarp -t_srs EPSG:4326 raw_tiles/*.tif /tmp/ks_1m_dem_2018.tif


	3.	Convert to COG

rio cogeo create /tmp/ks_1m_dem_2018.tif \
  data/processed/dem/ks_1m_dem_2018.tif \
  --overview-level=5 --web-optimized


	4.	Generate derivatives

make terrain          # slope, aspect, hillshade
make slope_classes
make aspect_sectors


	5.	Compute checksums

scripts/gen_sha256.sh data/processed/dem/*.tif


	6.	Update STAC items → data/stac/items/dem/
	•	Fill bbox, datetime, license, checksums.
	7.	Validate

make stac-validate
pre-commit run --all-files



⸻

🔗 Integration
	•	STAC — Each DEM & derivative documented as STAC Item (data/stac/items/dem/**).
	•	Web viewer — Hillshade, slope, aspect wired via web/data/*.json, validated against layers.schema.json.
	•	KML exports — Styled outputs (hillshade, color-relief) published under data/kml/.
	•	Experiments — Used in MCP workflows: hydrology modeling, archaeology predictive models, floodplain reconstruction, erosion studies.

⸻

📝 Notes
	•	Store only processed DEMs — raw tiles remain in data/raw/.
	•	Stable naming (ks_1m_dem_<year>.tif) so configs don’t break.
	•	Track large rasters with Git LFS or DVC.
	•	Always link back to authoritative provenance (USGS, Kansas GIS Hub, KGS surveys) in STAC.
	•	If rectified with GCPs, document under data/gcp/.
	•	Follow MCP reproducibility — log every step as an experiment or ETL pipeline action.

⸻

📚 See also
	•	data/raw/ — raw DEM tiles (from USGS/DASC).
	•	data/cogs/ — mission-final authoritative COGs.
	•	data/processed/dem/overlays/ — styled hillshades & blends.
	•	data/processed/dem/vectors/ — contour lines & vectorized terrain.
	•	data/stac/items/dem/ — STAC catalog entries.
	•	data/kml/ — KMZ super-overlays for Google Earth.
	•	experiments/ — MCP logs, configs, notebooks.

⸻

✅ Mission-grade principle: Processed DEMs must be COG-optimized, STAC-registered, and reproducible.
They provide the terrain foundation for analysis, visualization, and historical reconstructions.

