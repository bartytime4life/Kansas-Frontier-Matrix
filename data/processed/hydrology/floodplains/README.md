<div align="center">

# 🌊 Kansas-Frontier-Matrix — Floodplains  
`data/processed/hydrology/floodplains/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![Docs](https://img.shields.io/badge/docs-MCP%20Standards-blue.svg)](../../../docs/)  
[![Data Provenance](https://img.shields.io/badge/provenance-verified✅-green.svg)](../../../stac/items/hydrology/floodplains/)  

**Mission:** Store **processed floodplain datasets** for Kansas, including authoritative **FEMA maps** and **historic reconstructions** derived from DEMs, hydrologic models, and archival maps (e.g., 1890s Kansas River).  
All datasets must be **reproducible**, **provenance-linked**, and registered in the **STAC catalog** (`stac/items/hydrology/floodplains/`).  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Raw sources\n(FEMA NFHL/FIRM, historic scans, DEM runs)"] --> B["Process & convert\n(reproject EPSG:4326 · clean · generalize)"]
  B --> C["Outputs\n(data/processed/hydrology/floodplains/**)"]
  C --> D["Checksums + metadata\n(.sha256 · .meta.json)"]
  C --> E["STAC Items\n(stac/items/hydrology/floodplains/**)"]
  E --> F["Validate\n(make stac-validate)"]
  F --> G["Integration\n(web/config/layers.json · Knowledge Hub · experiments)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Structure

data/processed/hydrology/floodplains/
├── fema_floodplain_2020.json
├── fema_floodplain_2022.json
├── kansas_river_floodplain_1890s.json
├── statewide_flood_zones.json
└── README.md

	•	FEMA layers → official NFHL/FIRM datasets by year/version
	•	Historic reconstructions → polygons digitized from archival maps (georeferenced with GCPs)
	•	Modeled layers → DEM-based flood extent/depth (rasters as COG; vectors as GeoJSON)

⸻

🧭 File Conventions
	•	Vectors → GeoJSON (.json/.geojson)
	•	Rasters → Cloud-Optimized GeoTIFF (.tif) for depth grids / extents
	•	Tables → CSV (.csv) for per-feature attributes (e.g., community IDs, zone stats)
	•	CRS → EPSG:4326 (WGS84) for all outputs

⸻

🔧 Parameters (reference)

Layer Type	Tool/Method	Recommended Defaults	Notes
FEMA NFHL/FIRM	ogr2ogr / GDB → GeoJSON	-t_srs EPSG:4326 + dissolve by zone	Optionally keep attributes: FLD_ZONE, etc.
Historic scan	Georef + digitize	Ground control points (GCPs), RMSE < map tol.	Store .gcp and scan in STAC as source.
Modeled extent	H&H model (TauDEM/Whitebox/GRASS)	Return period (e.g., 1% AEP / 100-yr)	Export depth/extent; publish as COG/GeoJSON.


⸻

🔄 Workflow
	1.	Acquire raw sources → data/raw/hydrology/
	•	FEMA NFHL/FIRM (FEMA Map Service Center)
	•	Historic scans (USGS / state archives)
	•	DEM-based model outputs (TauDEM, WhiteboxTools, GRASS)
	2.	Process & convert
	•	Reproject → EPSG:4326
	•	Clean/dissolve polygons as needed (by FLD_ZONE, county, year)
	•	Export → GeoJSON (vectors), COG (rasters)
	3.	Checksums

scripts/gen_sha256.sh data/processed/hydrology/floodplains/*

	4.	Register in STAC
	•	Create/update Item JSON in stac/items/hydrology/floodplains/
	•	Link assets with roles:["data"] and checksum:sha256
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
    "kfm:lineage": ["data/raw/hydrology/fema/nfhl_ks_2020.gdb"],
    "qa:status": "verified"
  },
  "links": [
    { "rel": "collection", "href": "../../../../stac/collections/hydrology.json" }
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
    { "rel": "collection", "href": "../../../../stac/collections/historic.json" }
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
	•	Web viewer → floodplain toggles configured in web/config/layers.json
	•	Knowledge Hub → link to Kansas River hydrology, climate episodes, historical flood events
	•	Experiments → flood risk analysis, treaty/settlement overlays, vulnerability & exposure studies

⸻

✅ QA Checklist
	•	Files reprojected to EPSG:4326
	•	COG rasters have internal overviews & compression (LZW/DEFLATE)
	•	GeoJSON properties include essential attributes (FLD_ZONE, SOURCE, YEAR, etc.)
	•	Checksums created (.sha256) and referenced in STAC
	•	STAC items created/updated (correct href, roles, checksum)
	•	web/config/layers.json entries added/updated
	•	Large files tracked via Git LFS or DVC

⸻

📝 Notes
	•	Naming → <source>_<theme>_<year>.json (e.g., fema_floodplain_2020.json, kansas_river_floodplain_1890s.json)
	•	Provenance → cite FEMA, USGS, archives in STAC & experiments/
	•	❌ Never hand-edit processed outputs; regenerate via pipeline/notebooks
	•	Depth grids should include units metadata (e.g., meters) in STAC properties

⸻

📚 See Also
	•	../ → parent hydrology datasets
	•	../../dem/vectors/ → DEM-derived basins and streams
	•	stac/items/hydrology/floodplains/ → STAC Items for floodplain datasets
	•	experiments/ → MCP experiment logs for hydrology & flood modeling

⸻


<div align="center">


✅ Mission Principle
Floodplain datasets must be traceable, reproducible, and STAC-linked, ready for research, visualization, and integration across the Kansas Frontier Matrix.

</div>
```
