<div align="center">

# 🌍 Kansas Geo Timeline — Earth Context Layers

**Earth observation datasets** and **global reference layers**  
that complement the Kansas-focused datasets under `data/`.  

These provide **basemaps, climate context, and environmental indices**  
for comparative analysis in the **Kansas Frontier Matrix**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

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
	•	🌍 Global context — datasets beyond Kansas: NASA/NOAA satellite products, DEMs, land cover, vegetation indices.
	•	🛰️ Remote sensing — MODIS, Sentinel, Landsat, Daymet, NLCD, GEDI, HydroSHEDS.
	•	🌱 Environmental indices — NDVI, EVI, drought indices, fire perimeters, global soils.
	•	🗺️ Basemaps — Natural Earth, coastlines, political boundaries, rivers, global topo backgrounds.

Kansas is the core. These global layers exist only for context and comparison.

⸻

📂 Structure

data/earth/
├── sources/       # JSON descriptors (STAC-style or source metadata)
├── raw/           # downloaded archives / unprocessed rasters/vectors
├── processed/     # reprojected/cleaned GeoJSON, COGs, vector tiles
├── stac/          # STAC Items & Collections referencing processed assets
└── README.md

	•	sources/ → *.json descriptors used by scripts/fetch.py + make fetch
	•	raw/ → untouched downloads (tar/zip, HDF, NetCDF, GeoTIFF, etc.)
	•	processed/ → converted outputs (COG, GeoJSON, MBTiles/PMTiles)
	•	stac/ → metadata to connect to the hub

⸻

⚙️ Conventions
	•	CRS: EPSG:4326 (WGS84) unless justified otherwise.
	•	Raster: Cloud-Optimized GeoTIFF (.tif) with internal overviews.
	•	Vector: GeoJSON (small/medium) or MBTiles/PMTiles (large).
	•	Metadata: Every dataset has a STAC Item in stac/items/.
	•	Checksums: .sha256 sidecars for raw + processed artifacts.

⸻

🔗 Connections
	•	stac-badges.yml → validates data/earth/stac/** and builds Shields badges.
	•	stac.yml → renders web/app.config.json including earth layers.
	•	site.yml → deploys processed layers into MapLibre viewer.

⸻

📋 Common tasks

Add a new dataset:
	1.	Create data/earth/sources/<dataset>.json (endpoint, license, bbox, temporal).
	2.	Run make fetch → downloads to data/earth/raw/.
	3.	Convert: make cogs (rasters) / make vectors (shapefiles → GeoJSON).
	4.	Write STAC Item in data/earth/stac/items/.
	5.	Validate with make stac-validate.

Update an existing dataset:
	•	Refresh source JSON → make fetch + reprocess.
	•	Re-run validation.

Link to viewer:
	•	Reference STAC Item in scripts/badges/source_map.json.
	•	Regenerate web/app.config.json with make stac.

⸻

📝 Notes
	•	Global datasets can be huge → prefer per-tile or per-year subsets.
	•	Always record license in sources/*.json (e.g., NASA EarthData, Copernicus, CC-BY-4.0).
	•	Use scripts/gen_sha256.sh to hash large files after fetch.

⸻

✅ Mission-grade principle: Kansas remains the focus.
Earth layers add the environmental + global context needed for robust historical + geospatial analysis.

