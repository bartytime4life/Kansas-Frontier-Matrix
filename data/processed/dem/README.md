# Kansas-Frontier-Matrix — Processed DEMs

This folder contains **Digital Elevation Model (DEM) derivatives** that have been processed from raw sources  
(e.g., USGS 3DEP 1-m DEMs, LiDAR tiles, statewide mosaics).  

All outputs here are reproducible from raw inputs (`data/raw/`) using documented Makefile targets and scripts,  
and are referenced in the STAC catalog (`data/stac/items/dem/*.json`).

---

## Typical Contents

data/processed/dem/
├── ks_1m_dem_2018.tif             # 1m DEM (2018 statewide mosaic, COG)
├── ks_1m_dem_2020.tif             # 1m DEM (2020 update, COG)
├── ks_1m_dem_2018_hillshade.tif   # hillshade derivative
├── ks_1m_dem_2018_slope.tif       # slope raster (degrees or percent rise)
├── ks_1m_dem_2018_aspect.tif      # aspect raster (azimuthal)
└── overlays/                      # styled versions (color relief, blends)
└── hillshade_color.tif

- **DEM rasters** → stored as **Cloud-Optimized GeoTIFFs (COG)** with internal pyramids/overviews.  
- **Derivatives** → slope, aspect, hillshade, TRI/TPI, roughness, etc.  
- **Overlays** → styled derivatives (color-relief, shaded relief blends) for web/KML exports.

---

## Workflow

1. **Fetch raw DEM** from USGS 3DEP / Kansas GIS Hub → `data/raw/`  
   - Single LiDAR tiles are mosaicked into county or statewide extents.  
   - Metadata (year, resolution, source CRS) must be recorded.

2. **Mosaic & reproject** into **EPSG:4326** (WGS84 geographic lat/long) for web compatibility.  
   ```bash
   gdalwarp -t_srs EPSG:4326 raw_tiles/*.tif /tmp/ks_1m_dem_2018.tif

	3.	Convert to COG with overviews:

rio cogeo create /tmp/ks_1m_dem_2018.tif \
  data/processed/dem/ks_1m_dem_2018.tif \
  --overview-level=5 --web-optimized


	4.	Generate derivatives:

make terrain     # slope, aspect, hillshade
make slope_classes
make aspect_sectors


	5.	Compute checksums for provenance:

scripts/gen_sha256.sh data/processed/dem/*.tif


	6.	Update STAC Items in data/stac/items/dem/ with bbox, datetime, license, and checksums.
	7.	Validate with schema + STAC tools:

make stac-validate
pre-commit run --all-files



⸻

Integration
	•	STAC → Each DEM and derivative is documented as a STAC Item (data/stac/items/dem/…json) ￼.
	•	Web layers → Hillshade/slope/aspect are referenced in web/data/*.json configs and validated against web/config/layers.schema.json.
	•	KML exports → Styled DEMs (hillshade, color-relief) are exported to data/kml/ as KMZ overlays ￼.
	•	Experiments → Used in MCP workflows: hydrology modeling, archaeological predictive modeling, floodplain reconstructions, erosion studies.

⸻

Notes
	•	Store processed DEMs as COG only — no raw .tif tiles here.
	•	Use stable filenames (ks_1m_dem_<year>.tif) so STAC/web configs don’t break.
	•	Track large files with Git LFS or DVC.
	•	Always link back to authoritative provenance (USGS metadata, Kansas GIS Hub, KGS surveys) in the STAC item.
	•	Document any GCPs or control points used in rectification under data/gcp/.
	•	MCP reproducibility: each processing step must be logged as an experiment or ETL step ￼.

⸻

See Also
	•	data/raw/ — raw DEM tiles (as delivered by USGS/DASC).
	•	data/cogs/ — mission-final COGs (authoritative rasters).
	•	data/processed/dem/overlays/ — styled hillshades and color blends.
	•	data/processed/dem/vectors/ — contour lines and vectorized terrain derivatives.
	•	data/stac/items/dem/ — STAC items documenting DEMs and derivatives.
	•	data/kml/ — Google Earth–ready KMZ exports.
	•	experiments/ — MCP logs, configs, and notebooks documenting DEM experiments.

⸻

✅ This folder ensures Kansas DEM datasets are processed, optimized, STAC-compliant, and reproducible, ready for research, visualization, and web delivery.

---
