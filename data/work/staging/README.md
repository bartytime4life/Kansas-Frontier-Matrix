<div align="center">

# 🗂️ Kansas-Frontier-Matrix — Staging Workspace (`data/work/staging/`)

**Mission:** Provide a buffer for **intermediate rasters/vectors**  
that are being transformed, clipped, or standardized **before promotion**  
to canonical directories (`processed/`, `cogs/`, or `derivatives/`).  

This folder acts as a **pre-flight zone** where data is assembled,  
checked, and prepared for reproducible use.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)

📌 Subdirectory of `data/work/` (scratch + staging).  
📌 Files here are **ephemeral** until validated and promoted.  
📌 **Promote when analysis-ready** with checksums + STAC entries.  

</div>

---

## 🎯 Purpose

- Hold **clipped subsets** of rasters or vectors.  
- Store **intermediate GeoTIFFs** prior to COG conversion.  
- Stage **trial reprojected layers** before standardization (EPSG:4326).  
- Buffer **temporary exports** from geoprocessing pipelines.  

---

## 📂 Typical Contents

- Clipped county-level DEMs before mosaicking.  
- Unoptimized TIFFs awaiting conversion to COG.  
- Trial reprojected shapefiles/GeoJSONs.  
- Intermediate MBTiles/PMTiles built for inspection.  
- Any spatial artifact pending cleanup and promotion.  

---

## 🚦 Rules

- 🚫 **Not final** — staging files are not analysis-ready.  
- ✅ **Promote if reproducible:**  
  - → `data/processed/` once cleaned and standardized.  
  - → `data/cogs/` if converted to Cloud-Optimized GeoTIFF.  
  - → `data/derivatives/` if finalized as an analysis product.  
  - Always create/update **STAC Item + provenance** when promoted.  
- 🧹 **Safe to delete** — pipelines must regenerate as needed.  

---

## 🔄 Lifecycle Position

```mermaid
flowchart LR
  A["Staging workspace\n(data/work/staging)"] --> B["Processed / COGs\n(data/processed, data/cogs)"]
  B --> C["Derivatives\n(data/derivatives)"]
  C --> D["Catalog\n(stac/items)"]
  D --> E["Web Viewer\n(web/)"]

<!-- END OF MERMAID -->



⸻

🛠️ Usage Examples

Staging DEM tiles

# Clip statewide DEM to Ellis County before COG conversion
gdalwarp -cutline data/raw/counties/ellis.geojson \
  -crop_to_cutline data/raw/dem/ks_1m_2018.tif \
  data/work/staging/ellis_dem_stage.tif

Reprojection trial

# Reproject shapefile to EPSG:4326 for staging
ogr2ogr -t_srs EPSG:4326 \
  data/work/staging/railroads_stage.geojson \
  data/raw/railroads/railroads_1900.shp


⸻

🧹 Cleanup Policy
	•	Wipe staging area with:

clean-staging:
	rm -rf data/work/staging/*

	•	Promote validated outputs before cleanup.
	•	CI/CD may purge this directory automatically.

⸻

✅ Summary:
data/work/staging/ = pre-flight zone for rasters/vectors.
Use it to prep data for standardization;
promote only once reproducible + documented.