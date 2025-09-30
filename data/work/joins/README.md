<div align="center">

# 🔗 Kansas-Frontier-Matrix — Joins Workspace (`data/work/joins/`)

**Mission:** Provide a staging area for **temporary merges, overlays, and joins**  
between datasets — exploratory combinations that are **not yet canonical**.  

This folder is where layers meet, intersect, and get stress-tested  
before they are cleaned, documented, and promoted.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)

📌 Subdirectory of `data/work/` (scratch + staging).  
📌 Files here are **ephemeral by default**.  
📌 **Promote if meaningful → otherwise wipe freely.**

</div>

---

## 🎯 Purpose

- Run **trial joins and overlays** of multiple layers.  
- Test **schema integration** before formal normalization.  
- Prototype **geoprocessing operations** (intersects, unions, dissolves).  
- Compare alignment of disparate sources (historic maps vs. modern GIS).  

---

## 📂 Typical Contents

- Temporary GeoJSON/CSV merges from scripts.  
- Unioned shapefiles or clipped subsets for inspection.  
- Dissolved rasters or vectors used for trial analysis.  
- Joins between OCR text entities and geospatial features.  
- Test exports for debugging projection or attribute issues.  

---

## 🚦 Rules

- 🚫 **Not canonical** — never treat these as final.  
- ✅ **Promote if valuable:**  
  - → `data/processed/` once standardized & reproducible.  
  - → `data/derivatives/` if analysis-ready outputs.  
  - Always update **STAC Item + provenance** if promoted.  
- 🧹 Wipe clean with `make clean-joins` (safe to delete anytime).  

---

## 🔄 Lifecycle Position

```mermaid
flowchart LR
  A["Scratch joins\n(data/work/joins)"] --> B["Processed / COGs\n(data/processed, data/cogs)"]
  B --> C["Derivatives\n(data/derivatives)"]
  C --> D["Catalog\n(stac/items)"]
  D --> E["Web Viewer\n(web/)"]

<!-- END OF MERMAID -->



⸻

🛠️ Usage Examples

Trial vector overlay

# Join treaty polygons with modern county boundaries
ogr2ogr -f GeoJSON data/work/joins/treaties_x_counties.geojson \
  -sql "SELECT t.id, c.name, t.geometry
        FROM treaties t
        JOIN counties c
        ON ST_Intersects(t.geometry, c.geometry)" \
  data/raw/

OCR entity ↔ feature join

# Merge OCR text entities with trial geocoded features
python scripts/join_text_to_features.py \
  data/work/ocr/treaty1854_entities.json \
  data/raw/treaties/treaty1854.geojson \
  -o data/work/joins/treaty1854_join_trial.geojson


⸻

🧹 Cleanup Policy
	•	Safe to delete everything here:

clean-joins:
	rm -rf data/work/joins/*

	•	Promote before cleanup if the artifact is meaningful.
	•	CI/CD pipelines may wipe data/work/joins/ automatically.

⸻

✅ Summary:
data/work/joins/ = workspace for exploratory merges/overlays.
Use it to test data integration; promote only if reproducible.
Otherwise, treat it as disposable scratch space.