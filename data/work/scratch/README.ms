<div align="center">

# ✏️ Kansas-Frontier-Matrix — Scratchpad (`data/work/scratch/`)

**Mission:** Provide an **ad-hoc sandbox** for exploratory scripts, trial exports,  
and quick experiments that are **not yet reproducible or canonical**.  

This directory is intentionally messy — use it as a working pad  
before promoting valuable outputs to stable directories.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)

📌 Part of the `data/work/` layer (scratch + staging).  
📌 Excluded from canonical lineage until promoted.  
📌 **If it matters → move & document. If not → wipe freely.**

</div>

---

## 🎯 Purpose

- Host **quick one-off tests**: clipping, reprojecting, merging layers.  
- Store **draft exports** (CSV, GeoJSON, TIFF) before standardization.  
- Run **ad-hoc scripts or notebooks** without cluttering canonical dirs.  
- Provide a **low-stakes buffer** where mistakes are safe.  

---

## 📂 Typical Contents

- Trial GeoJSONs from experimental joins.  
- CSVs from uncleaned ETL pulls.  
- Scratch shapefiles, temporary rasters, or unoptimized TIFFs.  
- Jupyter/Colab or QGIS exports used for inspection.  
- Small scripts or notebook outputs under review.  

---

## 🚦 Rules

- 🚫 **Do not commit large binaries** unless needed for review.  
- ✅ **Promote when reproducible:**  
  - → `data/processed/` if cleaned + standardized.  
  - → `data/cogs/` if converted to analysis-ready COG.  
  - → `data/derivatives/` if final product.  
  - Always add **STAC Item + checksum** if promoted.  
- 🧹 **Safe to delete anytime** — treat as ephemeral unless explicitly promoted.  

---

## 🔄 Lifecycle Position

```mermaid
flowchart LR
  A["Scratchpad\n(data/work/scratch)"] --> B["Staging\n(data/work/)"]
  B --> C["Processed / COGs\n(data/processed, data/cogs)"]
  C --> D["Derivatives\n(data/derivatives)"]
  D --> E["Catalog\n(stac/items)"]

<!-- END OF MERMAID -->



⸻

🛠️ Usage Examples

Trial county clip

# Clip DEM to county boundary for inspection
gdalwarp -cutline data/raw/counties/ellis.geojson \
  -crop_to_cutline data/cogs/dem/ks_1m_dem_2018.tif \
  data/work/scratch/ellis_clip_trial.tif

Experimental join

# Merge OCR’d treaty text with trial polygons
ogr2ogr -f GeoJSON data/work/scratch/treaty1854_trial.geojson \
  data/raw/treaties/treaty1854.geojson


⸻

🧹 Cleanup Policy
	•	Wipe scratchpad with:

clean-scratch:
	rm -rf data/work/scratch/*

	•	Promote before cleanup if the file is valuable.
	•	CI jobs may automatically purge this directory.

⸻

✅ Summary:
data/work/scratch/ = low-stakes sandbox.
Use it for quick tests and drafts; promote only if reproducible.
Everything else can — and should — be wiped without regret.