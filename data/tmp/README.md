<div align="center">

# 🗂️ Kansas-Frontier-Matrix — Temporary Files (`data/tmp/`)

**Mission:** Provide a **scratch space for ephemeral artifacts** —  
build leftovers, test outputs, or transient pipeline files —  
that **never belong in version control** and may be wiped at any time.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)

📌 Excluded via `.gitignore`.  
📌 CI/CD ignores this directory completely.  
📌 **If it matters → promote & document. If not → let it vanish.**

</div>

---

## 🎯 Purpose

- Sandbox for **build pipelines** and **scripts**.  
- Buffer for **unzipped archives**, **API caches**, or **intermediate exports**.  
- Prevent clutter in canonical directories (`raw/`, `processed/`, `cogs/`, `derivatives/`).  
- Safe space for testing, prototyping, and debugging.  

---

## 📂 Typical Contents

- Temporary mosaics before COG conversion.  
- Clipped shapefiles or reprojection scratch layers.  
- Unpacked ZIP/TAR archives awaiting processing.  
- Intermediate OCR text dumps.  
- Test thumbnails, draft exports, or inspection files.  

---

## 🚦 Rules

- 🚫 **Never commit files in `data/tmp/`.**  
  - This path is `.gitignore`d and excluded from CI/CD.  

- ✅ **Promote if useful:**  
  - → `data/work/` for short-term intermediates.  
  - → `data/processed/` or `data/cogs/` if analysis-ready.  
  - → `data/raw/` if canonical input.  
  - Always update **STAC Items** + **checksums** if promoted.  

- 🧹 **Safe to delete anytime** — pipelines must regenerate outputs.  

---

## 🔄 Lifecycle Position

```mermaid
flowchart LR
  A["Ephemeral scratch\n(data/tmp/)"] --> B["Work-in-progress\n(data/work/)"]
  B --> C["Processed / COGs\n(data/processed, data/cogs)"]
  C --> D["Derivatives\n(data/derivatives)"]
  D --> E["Catalog\n(stac/items)"]

<!-- END OF MERMAID -->



⸻

🛠️ Usage Examples

DEM pipeline scratch

# Mosaic raw DEM tiles before COG conversion
gdal_merge.py -o data/tmp/ks_mosaic_2018.tif data/raw/elevation/tiles/*.tif
rio cogeo create data/tmp/ks_mosaic_2018.tif data/cogs/dem/ks_1m_dem_2018.tif

OCR scratch

# Write intermediate OCR text here (not in processed/)
tesseract data/raw/docs/treaty_osage_1825.pdf data/tmp/treaty_osage_1825 -l eng


⸻

🧹 Makefile Integration

Add a clean target to wipe scratch files:

clean-tmp:
	rm -rf data/tmp/*

.PHONY: clean-tmp

CI/CD pipelines can run make clean-tmp after jobs to prevent buildup.

⸻

📜 Provenance & STAC
	•	❌ No provenance or STAC entries required for files in data/tmp/.
	•	⏫ On promotion:
	•	Generate SHA-256 checksum.
	•	Add provenance entry (data/provenance/registry.json).
	•	Create/update STAC Item under stac/items/.

⸻

✅ Summary:
data/tmp/ = ephemeral scratchpad.
Use it for anything transient; promote & document only if the file becomes important.