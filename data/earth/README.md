<div align="center">

# 🌍 Kansas Geo Timeline — Earth Context Layers  
`data/earth/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../../.github/workflows/stac-badges.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.pre-commit-config.yaml)

**Mission:** Provide **Earth observation datasets** and **global reference layers**  
that complement Kansas-focused data under `data/`.  
These layers give **basemaps, climate context, and environmental indices**  
for comparative analysis in the **Kansas Frontier Matrix**.  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Sources JSON\n(data/earth/sources/**)"] --> B["Fetch\n(make fetch)"]
  B --> C["Raw downloads\n(data/earth/raw/**)"]
  C --> D["Process (COG, GeoJSON, MBTiles)\n(data/earth/processed/**)"]
  D --> E["STAC Items\n(data/earth/stac/items/**)"]
  E --> F["Validate\n(stac-validate)"]
  F --> G["Viewer integration\n(web/app.config.json)"]

<!-- END OF MERMAID -->



⸻

🧭 Scope
	•	🌍 Global context → datasets beyond Kansas (NASA/NOAA satellite products, DEMs, global land cover, vegetation indices).
	•	🛰️ Remote sensing → MODIS, Sentinel, Landsat, Daymet, NLCD, GEDI, HydroSHEDS.
	•	🌱 Environmental indices → NDVI, EVI, drought indices, fire perimeters, global soils.
	•	🗺️ Basemaps → Natural Earth, coastlines, political boundaries, rivers, topo backgrounds.

Kansas remains the core. Global layers exist only for context and comparison.

⸻

📂 Directory Structure

data/earth/
├── sources/       # JSON descriptors (STAC-style metadata)
├── raw/           # Downloads (tar/zip, HDF, NetCDF, GeoTIFF, etc.)
├── processed/     # Reprojected/cleaned GeoJSON, COGs, PMTiles
├── stac/          # STAC Items & Collections for Earth datasets
└── README.md

	•	sources/ → *.json descriptors used by scripts/fetch.py + make fetch.
	•	raw/ → untouched downloads (archives or native formats).
	•	processed/ → converted outputs (COG, GeoJSON, PMTiles).
	•	stac/ → metadata linking assets into the STAC catalog.

⸻

⚙️ Conventions
	•	CRS → EPSG:4326 (WGS84) unless otherwise justified.
	•	Rasters → Cloud-Optimized GeoTIFF (.tif) with internal overviews.
	•	Vectors → GeoJSON (small/medium) or PMTiles (large).
	•	Metadata → every dataset must have a STAC Item in stac/items/.
	•	Checksums → .sha256 sidecars for all raw + processed artifacts.

⸻

🔗 Connections
	•	stac-badges.yml → validates data/earth/stac/** and generates Shields badges.
	•	stac.yml → renders web/app.config.json including Earth layers.
	•	site.yml → deploys processed Earth layers to the MapLibre viewer.

⸻

📋 Common Tasks

Add a new dataset
	1.	Create data/earth/sources/<dataset>.json (endpoint, license, bbox, temporal coverage).
	2.	Run make fetch → downloads into data/earth/raw/.
	3.	Convert: make cogs (rasters) / make vectors (shapefiles → GeoJSON).
	4.	Write a STAC Item in data/earth/stac/items/.
	5.	Validate with make stac-validate.

Update an existing dataset
	•	Refresh source JSON → make fetch + reprocess.
	•	Re-run validation and update STAC Items.

Link to viewer
	•	Reference STAC Item in scripts/badges/source_map.json.
	•	Regenerate web/app.config.json with make stac.

⸻

📝 Notes
	•	Global datasets can be very large → prefer per-tile or per-year subsets.
	•	Always record license in sources/*.json (e.g., NASA EarthData, Copernicus, CC-BY-4.0).
	•	Use scripts/gen_sha256.sh to hash large files after fetch.

⸻

✅ Mission Principle

Kansas is the focus.
Earth datasets are added only to provide context, baselines, and comparative layers
that strengthen Kansas historical and geospatial analysis.