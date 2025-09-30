<div align="center">

# 🌊 Kansas Geo Timeline — Kansas River Hydrology

This folder contains **processed hydrological datasets** for the Kansas River and its watershed.  

All data are derived from **authoritative sources** (USGS NHD, FEMA, KGS, NOAA) and/or **DEM-based analyses**.  
Outputs are stored in **open formats** (GeoJSON, CSV, COG) and referenced in the **STAC catalog** (`data/stac/items/`) and web configs.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Raw hydrology sources\n(USGS NHD · FEMA · NOAA NWIS · GIS Hub)"] --> B["Process & clean\n(reproject EPSG:4326 · dissolve)"]
  B --> C["Kansas River datasets\n(data/processed/hydrology/kansas_river/**)"]
  C --> D["Checksums + meta\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(data/stac/items/hydrology/**)"]
  E --> F["Validate\n(stac-validate)"]
  F --> G["Viewer integration\n(web/config/layers.json)"]

<!-- END OF MERMAID -->



⸻

📂 Typical contents

data/processed/hydrology/kansas_river/
├── kansas_river_centerline.json   # mainstem line
├── kansas_river_watershed.json    # drainage basin polygon
├── kansas_river_floodplain_1890s.json
├── kansas_river_gauges.csv        # gauge stations
└── README.md

	•	Centerline → generalized vector line of the Kansas River mainstem.
	•	Watershed → polygon boundary of the Kansas River drainage area.
	•	Historic floodplains → reconstructions from historic maps, surveys, or DEMs (e.g., 1890s).
	•	Gauges & stations → CSV/GeoJSON with USGS/NOAA gauge IDs + metadata.

⸻

🔄 Workflow
	1.	Acquire raw sources
	•	USGS NHDPlus, NOAA NWIS, FEMA floodplain data, Kansas GIS Hub.
	•	Historic reconstructions from topo maps or experiments/*/.
	2.	Process & convert
	•	Reproject to EPSG:4326 (WGS84).
	•	Clean topology (snap/merge, dissolve).
	•	Export → GeoJSON (vectors), CSV (tabular).
	3.	Checksums

scripts/gen_sha256.sh data/processed/hydrology/kansas_river/*


	4.	Register in STAC
Example asset in a STAC Item:

"kansas_river_centerline": {
  "href": "../../../processed/hydrology/kansas_river/kansas_river_centerline.json",
  "title": "Kansas River Centerline",
  "type": "application/geo+json",
  "roles": ["data"],
  "checksum:sha256": "<sha256sum>"
}


	5.	Validate

make stac-validate
pre-commit run --all-files



⸻

🔗 Integration
	•	Web Viewer → layers toggle in web/config/layers.json.
	•	Experiments → used in floodplain reconstruction, treaty overlays, erosion studies, archaeology context.
	•	Knowledge Hub → cross-linked with treaties, settlements, climate & environmental data in the graph.

⸻

📝 Notes
	•	Always regenerate from raw sources or experiment scripts — never hand-edit outputs.
	•	Use stable filenames (kansas_river_<layer>.json) for consistent STAC + web references.
	•	Track large files with Git LFS / DVC.
	•	Document provenance and methods in experiments/<ID>_.../experiment.md.

⸻

✅ Mission-grade principle: Kansas River hydrology datasets must be clean, versioned, STAC-linked, and reproducible,
supporting geospatial visualization and cross-domain scientific analysis.

