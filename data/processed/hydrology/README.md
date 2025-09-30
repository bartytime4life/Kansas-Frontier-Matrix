<div align="center">

# 💧 Kansas Geo Timeline — Hydrology

This folder contains **processed hydrological datasets**  
derived from DEMs, USGS/NHD, FEMA flood maps, and Kansas GIS Hub sources.  

Outputs are stored in **open formats** (GeoJSON, CSV, Cloud-Optimized GeoTIFFs) and are  
**reproducible** from raw inputs in `data/raw/`.  

All datasets must be registered in the **STAC catalog** (`data/stac/items/hydrology/`)  
with metadata, checksums, and provenance.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Raw hydrology sources\n(data/raw/hydrology/**)"] --> B["Process\n(clean · reproject · simplify)"]
  B --> C["Processed outputs\n(data/processed/hydrology/**)"]
  C --> D["Checksums + meta\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(data/stac/items/hydrology/**)"]
  E --> F["Validate\n(stac-validate)"]
  F --> G["Viewer integration\n(web/config/layers.json)"]

<!-- END OF MERMAID -->



⸻

📂 Structure

data/processed/hydrology/
├── kansas_river/        # Kansas River centerlines, watershed, floodplains, gauges
├── watersheds/          # HUC-based watershed polygons (HUC8, HUC12)
├── floodplains/         # FEMA + historic floodplain extents
├── stream_networks.json # generalized statewide stream network
├── lakes_wetlands.json  # major lakes & wetlands polygons
└── README.md

	•	kansas_river/ → Kansas River–specific hydrology datasets.
	•	watersheds/ → statewide or regional HUC-based polygons.
	•	floodplains/ → FEMA and reconstructed floodplain layers.
	•	Other files → generalized or statewide hydrology vectors.

⸻

🧭 File conventions
	•	Vectors → GeoJSON (*.json, *.geojson)
	•	Rasters → Cloud-Optimized GeoTIFFs (*.tif) for flood models, depth grids
	•	Tables → CSV for gauges, time series, metadata
	•	Projection → EPSG:4326 (WGS84 lat/long) required for all outputs

⸻

🔄 Workflow
	1.	Acquire raw sources → data/raw/
	•	Sources: USGS NHD, NOAA NWIS, FEMA, Kansas GIS Hub.
	2.	Process
	•	Clean, reproject to EPSG:4326
	•	Simplify/dissolve geometries as needed
	•	Export to GeoJSON/COG/CSV
	3.	Checksums

scripts/gen_sha256.sh data/processed/hydrology/*


	4.	Register in STAC
	•	Add/update Item JSON under data/stac/items/hydrology/
	•	Link assets with roles: ["data"] + checksum:sha256
	5.	Validate

pre-commit run stac-validate --all-files



⸻

🔗 Integration
	•	Web Viewer → layers referenced in web/config/layers.json for MapLibre visualization.
	•	Experiments → used in floodplain reconstruction, treaty overlays, archaeological + erosion studies.
	•	Knowledge Hub → cross-links hydrology with treaties, settlements, geology, environment.

⸻

📝 Notes
	•	❌ Do not manually edit processed outputs.
	•	✅ Always regenerate from raw + documented scripts or notebooks.
	•	Use stable filenames (<theme>_<year>.json) so STAC + web configs remain valid.
	•	Track large files with Git LFS / DVC.
	•	Document provenance and methods in experiments/<ID>_.../experiment.md.

⸻

✅ Mission-grade principle: Hydrology datasets must be consistent, reproducible, STAC-linked, and ready for cross-domain analysis in the Kansas Frontier Matrix.

