<div align="center">

# 🌊 Kansas Geo Timeline — Floodplains

This folder contains **processed floodplain datasets** for Kansas.  

It includes both **authoritative FEMA maps** and **historic floodplain reconstructions**  
derived from DEMs, hydrological models, and archival maps (e.g., 1890s Kansas River).  

All datasets are **reproducible**, **provenance-linked**, and registered in the  
**STAC catalog** (`data/stac/items/hydrology/floodplains/`).  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Raw sources\n(FEMA NFHL/FIRM, historic scans, DEM runs)"] --> B["Process & convert\n(reproject EPSG:4326, clean)"]
  B --> C["Outputs\n(data/processed/hydrology/floodplains/**)"]
  C --> D["Checksums + meta\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(data/stac/items/hydrology/floodplains/**)"]
  E --> F["Validate\n(stac-validate)"]
  F --> G["Integration\n(web configs, experiments, Knowledge Hub)"]

<!-- END OF MERMAID -->



⸻

📂 Typical contents

data/processed/hydrology/floodplains/
├── fema_floodplain_2020.json
├── fema_floodplain_2022.json
├── kansas_river_floodplain_1890s.json
├── statewide_flood_zones.json
└── README.md

	•	FEMA layers → official datasets by year/version (FIRM, NFHL).
	•	Historic reconstructions → polygons digitized from archival maps.
	•	Modeled layers → DEM-based flood depth/extent grids.

⸻

🔄 Workflow
	1.	Acquire raw sources
	•	FEMA NFHL/FIRM (shapefiles, GDBs) from FEMA Map Service Center.
	•	Historical maps (USGS / Kansas archives, stored under data/raw/).
	•	DEM-based hydrology models (TauDEM, WhiteboxTools, GRASS).
	2.	Process & convert
	•	Reproject → EPSG:4326 (WGS84).
	•	Clean/dissolve polygons if needed.
	•	Export → GeoJSON for vectors, COG for rasters.
	3.	Checksums

scripts/gen_sha256.sh data/processed/hydrology/floodplains/*


	4.	Register in STAC
	•	Create STAC Item in data/stac/items/hydrology/floodplains/.
	•	Example asset entry:

"fema_floodplain_2020": {
  "href": "../../../processed/hydrology/floodplains/fema_floodplain_2020.json",
  "title": "FEMA Floodplain (2020)",
  "type": "application/geo+json",
  "roles": ["data"],
  "checksum:sha256": "<sha256sum>"
}


	5.	Validate

make stac-validate
pre-commit run --all-files



⸻

🔗 Integration
	•	Web viewer → floodplain layers toggle in web/config/layers.json.
	•	Experiments → inputs for flood risk analysis, treaty overlays, vulnerability studies.
	•	Knowledge Hub → linked with Kansas River hydrology, climate datasets, and historical flood events.

⸻

📝 Notes
	•	Naming convention → <source>_<theme>_<year>.json
	•	Example: fema_floodplain_2020.json, kansas_river_floodplain_1890s.json.
	•	Provenance required → document sources (FEMA, USGS, archives) in experiment.md or STAC.
	•	Large rasters → store as COGs, track with Git LFS / DVC.
	•	❌ Never hand-edit; always regenerate via pipeline.

⸻

✅ Mission-grade principle: Floodplain datasets must be traceable, reproducible, and STAC-linked, ready for use in research, visualization, and the Kansas Frontier Matrix web map.

