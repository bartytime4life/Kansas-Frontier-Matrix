<div align="center">

# 🌊 Kansas-Frontier-Matrix — Kansas River Hydrology  
`data/processed/hydrology/kansas_river/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![Docs](https://img.shields.io/badge/docs-MCP%20Standards-blue.svg)](../../../docs/)  
[![Data Provenance](https://img.shields.io/badge/provenance-verified✅-green.svg)](../../../stac/items/hydrology/)  

**Mission:** Hold **processed hydrological datasets** for the Kansas River and its watershed.  

All data are derived from **authoritative sources** (USGS NHD, FEMA, KGS, NOAA) and/or **DEM-based analyses**.  
Outputs are stored in **open formats** (GeoJSON, CSV, COG) and registered in the **STAC catalog** (`stac/items/`) and web configs.  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Raw hydrology sources\n(USGS NHD · FEMA · NOAA NWIS · GIS Hub)"] --> B["Process & clean\n(reproject EPSG:4326 · dissolve)"]
  B --> C["Kansas River datasets\n(data/processed/hydrology/kansas_river/**)"]
  C --> D["Checksums + meta\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(stac/items/hydrology/**)"]
  E --> F["Validate\n(make stac-validate)"]
  F --> G["Viewer integration\n(web/config/layers.json)"]
  G --> H["Knowledge Hub integration\n(cross-domain linking)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Structure

data/processed/hydrology/kansas_river/
├── kansas_river_centerline.json   # mainstem line
├── kansas_river_watershed.json    # drainage basin polygon
├── kansas_river_floodplain_1890s.json
├── kansas_river_gauges.csv        # gauge stations
└── README.md

	•	Centerline → generalized vector line of the Kansas River mainstem
	•	Watershed → polygon boundary of the Kansas River drainage area
	•	Historic floodplains → reconstructions from historic maps, surveys, or DEMs (e.g., 1890s)
	•	Gauges & stations → CSV/GeoJSON with USGS/NOAA gauge IDs + metadata

⸻

🧭 File Conventions
	•	Vectors → GeoJSON (.json, .geojson)
	•	Tables → CSV (.csv) for gauges and metadata
	•	Rasters → COG (.tif) if depth grids or flood models are produced
	•	Projection → EPSG:4326 (WGS84 lat/long) for all outputs

⸻

🔄 Workflow
	1.	Acquire raw sources
	•	USGS NHDPlus, NOAA NWIS, FEMA floodplain data, Kansas GIS Hub
	•	Historic reconstructions from topo maps or experiments/*/
	2.	Process & convert
	•	Reproject → EPSG:4326 (WGS84)
	•	Clean topology (snap/merge, dissolve)
	•	Export → GeoJSON (vectors), CSV (tabular)
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

📑 Example STAC Items

Kansas River Centerline (vector)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kansas_river_centerline",
  "properties": {
    "title": "Kansas River Centerline",
    "description": "Generalized line geometry of the Kansas River mainstem.",
    "datetime": "2020-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "Simplified from USGS NHD flowlines",
    "kfm:lineage": ["data/raw/hydrology/nhd/ks_flowlines.gpkg"],
    "qa:status": "verified"
  },
  "links": [
    { "rel": "collection", "href": "../../../../stac/collections/hydrology.json" }
  ],
  "assets": {
    "geojson": {
      "href": "../../../../data/processed/hydrology/kansas_river/kansas_river_centerline.json",
      "title": "Kansas River Centerline",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    }
  }
}

Kansas River Floodplain (1890s reconstruction, vector)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kansas_river_floodplain_1890s",
  "properties": {
    "title": "Kansas River Floodplain (1890s Reconstruction)",
    "description": "Historic floodplain reconstruction digitized from archival 1890s Kansas River maps.",
    "datetime": "1895-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "Digitized polygons from archival maps, georeferenced with GCPs",
    "kfm:lineage": [
      "data/raw/hydrology/historic/kansas_river_1890s_scan.tif",
      "data/gcp/kansas_river_1890s.gcp"
    ],
    "qa:status": "provisional"
  },
  "links": [
    { "rel": "collection", "href": "../../../../stac/collections/historic.json" }
  ],
  "assets": {
    "geojson": {
      "href": "../../../../data/processed/hydrology/kansas_river/kansas_river_floodplain_1890s.json",
      "title": "Kansas River Floodplain (1890s Reconstruction)",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    },
    "scan": {
      "href": "../../../../data/raw/hydrology/historic/kansas_river_1890s_scan.tif",
      "title": "Archival Scan (Kansas River Floodplain, 1890s)",
      "type": "image/tiff",
      "roles": ["source"]
    }
  }
}


⸻

🔗 Integration
	•	Web Viewer → toggleable layers in web/config/layers.json
	•	Knowledge Hub → cross-linked with treaties, settlements, climate & environmental data
	•	Experiments → used in floodplain reconstruction, treaty overlays, erosion studies, archaeology

⸻

✅ QA Checklist
	•	All outputs reprojected to EPSG:4326
	•	Checksums generated and stored (.sha256)
	•	STAC items updated with correct href, roles, and checksums
	•	Web config entries updated for visualization
	•	Large files tracked with Git LFS or DVC
	•	Provenance documented in experiments/

⸻

📝 Notes
	•	Always regenerate from raw sources or experiment scripts → ❌ never hand-edit outputs
	•	Use stable filenames (kansas_river_<layer>.json) for consistency in STAC + web configs
	•	Track large datasets via Git LFS / DVC
	•	Document provenance and methods in experiments/<ID>_*/experiment.md

⸻

📚 See Also
	•	../ → parent hydrology datasets
	•	../../floodplains/ → statewide floodplain datasets
	•	../../dem/vectors/ → DEM-derived stream networks & basins
	•	stac/items/hydrology/ → STAC Items for hydrology datasets
	•	experiments/ → MCP experiment logs for hydrology + floodplain studies

⸻


<div align="center">


✅ Mission Principle
Kansas River hydrology datasets must be clean, versioned, STAC-linked, and reproducible, supporting geospatial visualization and cross-domain scientific analysis.

</div>
```
