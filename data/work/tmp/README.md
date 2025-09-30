<div align="center">

# 🗑️ Kansas-Frontier-Matrix — Work TMP (`data/work/tmp/`)

**Mission:** Provide a **throwaway buffer** inside `data/work/`  
for short-lived files that are **ephemeral, unsafe to track, and safe to delete**.  

This directory is the lowest rung of the `work/` tier —  
use it as a scratchpad for anything not worth documenting or promoting.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)

📌 Always `.gitignore`d.  
📌 CI/CD ignores this directory completely.  
📌 **If it matters → promote. If not → let it vanish.**

</div>

---

## 🎯 Purpose

- Hold **transient scratch files** created during builds or experiments.  
- Buffer **unzipped archives**, **download caches**, or **debug dumps**.  
- Prevent clutter in `data/work/` subfolders (`scratch/`, `joins/`, `ocr/`, `staging/`).  
- Provide a safe, disposable workspace for iterative development.  

---

## 📂 Typical Contents

- Temporary TIFFs or shapefiles clipped mid-pipeline.  
- API query caches, CSV downloads, or test extracts.  
- Unpacked ZIP/TAR archives awaiting processing.  
- Debug logs, trace files, or sandbox exports.  

---

## 🚦 Rules

- 🚫 **Never commit files in `data/work/tmp/`.**  
- ✅ **Promote if meaningful:**  
  - → `scratch/` if useful for exploratory work.  
  - → `staging/` if preparing for COG/GeoJSON.  
  - → `processed/` or `derivatives/` if analysis-ready.  
  - Always update provenance + STAC if promoted.  
- 🧹 Everything here is **safe to delete** — pipelines must regenerate.  

---

## 🔄 Lifecycle Position

```mermaid
flowchart LR
  A["Ephemeral TMP\n(data/work/tmp)"] --> B["Scratch / Staging\n(data/work/*)"]
  B --> C["Processed / COGs\n(data/processed, data/cogs)"]
  C --> D["Derivatives\n(data/derivatives)"]
  D --> E["Catalog\n(stac/items)"]
  E --> F["Web Viewer\n(web/)"]

<!-- END OF MERMAID -->



⸻

🛠️ Usage Examples

Unpack ZIP for processing

unzip data/raw/soils/kansas_1967.zip -d data/work/tmp/

Cache API pulls

curl -s https://api.noaa.gov/data/ks/weather.csv \
  -o data/work/tmp/noaa_weather_trial.csv


⸻

🧹 Cleanup Policy
	•	Wipe tmp workspace with:

clean-work-tmp:
	rm -rf data/work/tmp/*

	•	CI/CD pipelines may auto-clean this directory after jobs.
	•	Promote before cleanup if anything is valuable.

⸻

✅ Summary:
data/work/tmp/ = throwaway scratchpad inside work/.
Use it for short-lived junk; promote only if reproducible.
Everything else should be wiped without hesitation.