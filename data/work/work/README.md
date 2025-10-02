<div align="center">

# 🛠️ Kansas-Frontier-Matrix — Work Files  
`data/work/work/`

**Mission:** Provide a **workspace for intermediate artifacts** —  
short-lived but potentially reusable outputs from pipelines and analyses.  
Unlike `data/tmp/`, files here **may be shared, inspected, or staged**,  
but they are **not final products** and must be promotable or discardable.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../../.pre-commit-config.yaml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../../../.github/workflows/automerge.yml)  
[![Docs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/docs.yml/badge.svg)](../../../../.github/workflows/docs.yml)  
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://app.codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)  

📌 **Work files are not versioned long-term**.  
📌 Use for staging or debugging when outputs may be passed around or inspected.  
📌 Promote to `processed/`, `cogs/`, or `derivatives/` if they become canonical.  

</div>

---

## 🎯 Purpose

- Provide a **buffer space** between disposable scratch (`tmp/`) and reproducible data (`processed/`).  
- Hold **intermediate mosaics, clipped rasters, or merged vectors** awaiting QC.  
- Allow analysts to **share work-in-progress** without polluting canonical directories.  
- Facilitate **debugging and pipeline testing**.  

---

## 📂 Typical Contents

- DEM mosaics ready for COG conversion.  
- Clipped vectors for county- or watershed-scale testing.  
- QA/QC outputs for soil, land cover, or hazard layers.  
- OCR text reviewed before final archival.  
- Draft STAC descriptors under peer review.  

---

## 🚦 Rules

- ✅ **Work files may be shared** within the repo if relevant for review.  
- ✅ **Promote when finalized:**  
  - → `data/processed/` if analysis-ready.  
  - → `data/cogs/` for cloud-optimized rasters.  
  - → `data/derivatives/` for long-term artifacts.  
  - Always add provenance + STAC on promotion.  

- 🧹 **Purge stale work files** regularly. CI/CD may run `make clean-work`.  
- 🚫 **Do not treat work files as archival** — they are transient.  

---

## 🔄 Lifecycle Position

```mermaid
flowchart LR
  A["Ephemeral scratch\n(data/tmp/)"] --> B["Work-in-progress\n(data/work/work/)"]
  B --> C["Processed / COGs\n(data/processed, data/cogs)"]
  C --> D["Derivatives\n(data/derivatives)"]
  D --> E["Cataloged STAC Items\n(data/stac/items)"]

<!-- END OF MERMAID -->



⸻

🛠️ Usage Examples

DEM Mosaic QC

# Mosaic DEM tiles and save to work/
gdal_merge.py -o data/work/work/ks_mosaic_qc_2018.tif data/raw/dem/tiles/*.tif
# Inspect visually before promotion to processed/cogs

Vector Clipping

# Clip statewide railroads for a county map
ogr2ogr -clipsrc county_boundary.shp \
  data/work/work/railroads_douglas.json \
  data/processed/vectors/ks_railroads.json


⸻

🧹 Makefile Integration

Add clean target for work directory:

clean-work:
	rm -rf data/work/work/*

.PHONY: clean-work


⸻

📜 Provenance & STAC
	•	❌ No provenance or STAC required for files in data/work/work/.
	•	⏫ On promotion:
	•	Generate .sha256.
	•	Add entry to data/provenance/registry.json.
	•	Create/update STAC Item in stac/items/.

⸻

✦ Summary

data/work/work/ = short-term workspace for intermediate artifacts.
Unlike tmp/, files here may be inspected or reviewed, but they are not final.
Promote & document when stable, ensuring Kansas Frontier Matrix stays organized, reproducible, and audit-ready.