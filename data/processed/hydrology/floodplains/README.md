<div align="center">

# 🌊 Kansas-Frontier-Matrix — Floodplains  
`data/processed/hydrology/floodplains/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Store **processed floodplain datasets** for Kansas,  
including authoritative **FEMA maps** and **historic reconstructions** derived from DEMs,  
hydrological models, and archival maps (e.g., 1890s Kansas River).  

All datasets must be **reproducible**, **provenance-linked**, and registered in the  
**STAC catalog** (`data/stac/items/hydrology/floodplains/`).  

</div>

---

## 📈 Lifecycle

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

📂 Typical Contents

data/processed/hydrology/floodplains/
├── fema_floodplain_2020.json
├── fema_floodplain_2022.json
├── kansas_river_floodplain_1890s.json
├── statewide_flood_zones.json
└── README.md

	•	FEMA layers → official datasets by year/version (FIRM, NFHL)
	•	Historic reconstructions → polygons digitized from archival maps
	•	Modeled layers → DEM-based flood depth/extent grids

⸻

🔄 Workflow
	1.	Acquire raw sources
	•	FEMA NFHL/FIRM shapefiles & geodatabases (FEMA Map Service Center)
	•	Historical maps (USGS / Kansas archives, under data/raw/)
	•	DEM-based hydrology model outputs (TauDEM, WhiteboxTools, GRASS)
	2.	Process & convert
	•	Reproject → EPSG:4326 (WGS84)
	•	Clean / dissolve polygons as needed
	•	Export → GeoJSON (vectors), COG (rasters)
	3.	Checksums

scripts/gen_sha256.sh data/processed/hydrology/floodplains/*


	4.	Register in STAC
	•	Create/update Item JSON in data/stac/items/hydrology/floodplains/
	•	Link all outputs with roles: ["data"] and checksum:sha256
	5.	Validate

make stac-validate
pre-commit run --all-files



⸻

📑 Example STAC Items

FEMA Floodplain (2020, authoritative)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_fema_floodplain_2020",
  "properties": {
    "title": "Kansas FEMA Floodplain (2020)",
    "description": "Official FEMA 2020 floodplain polygons for Kansas.",
    "datetime": "2020-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "Processed from FEMA NFHL shapefiles",
    "kfm:lineage": [
      "data/raw/hydrology/fema/nfhl_ks_2020.gdb"
    ],
    "qa:status": "verified"
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../../stac/collections/hydrology.json"
    }
  ],
  "assets": {
    "geojson": {
      "href": "../../../../data/processed/hydrology/floodplains/fema_floodplain_2020.json",
      "title": "FEMA Floodplain (2020, Kansas)",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    }
  }
}

Historic Floodplain (Kansas River, 1890s reconstruction)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_kansas_river_floodplain_1890s",
  "properties": {
    "title": "Kansas River Floodplain (1890s Reconstruction)",
    "description": "Digitized historic floodplain extent of the Kansas River from archival 1890s maps.",
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
    {
      "rel": "collection",
      "href": "../../../../stac/collections/historic.json"
    }
  ],
  "assets": {
    "geojson": {
      "href": "../../../../data/processed/hydrology/floodplains/kansas_river_floodplain_1890s.json",
      "title": "Kansas River Floodplain (1890s)",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    },
    "scan": {
      "href": "../../../../data/raw/hydrology/historic/kansas_river_1890s_scan.tif",
      "title": "Archival Scan (Kansas River floodplain, 1890s)",
      "type": "image/tiff",
      "roles": ["source"]
    }
  }
}


⸻

🔗 Integration
	•	Web viewer → floodplain layers toggle in web/config/layers.json
	•	Experiments → used in flood risk analysis, treaty overlays, vulnerability studies
	•	Knowledge Hub → linked with Kansas River hydrology, climate datasets, and historical flood events

⸻

📝 Notes
	•	Naming convention → <source>_<theme>_<year>.json
	•	Examples: fema_floodplain_2020.json, kansas_river_floodplain_1890s.json
	•	Provenance required → cite FEMA, USGS, archives in STAC & experiments
	•	Large rasters stored as COGs → tracked with Git LFS or DVC
	•	❌ Never hand-edit → always regenerate via pipeline

⸻

📚 See Also
	•	../ → parent hydrology datasets
	•	../../dem/vectors/ → DEM-derived basins and streams
	•	data/stac/items/hydrology/floodplains/ → STAC Items for floodplain datasets
	•	experiments/ → MCP experiment logs for hydrology and flood modeling

⸻

✅ Mission Principle

Floodplain datasets must be traceable, reproducible, and STAC-linked,
ready for use in research, visualization, and the Kansas Frontier Matrix web map.