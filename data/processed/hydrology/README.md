<div align="center">

# 💧 Kansas-Frontier-Matrix — Hydrology  
`data/processed/hydrology/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Hold **processed hydrological datasets** derived from DEMs, NHD, FEMA flood maps,  
NOAA/NWIS gauges, and Kansas GIS Hub sources.  

Outputs are stored in **open formats** (GeoJSON, CSV, Cloud-Optimized GeoTIFFs)  
and are **reproducible** from raw inputs in `data/raw/`.  

All datasets must be registered in the **STAC catalog** (`data/stac/items/hydrology/`)  
with metadata, checksums, and provenance.  

</div>

---

## 📈 Lifecycle

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

	•	kansas_river/ → Kansas River–specific hydrology datasets
	•	watersheds/ → statewide or regional HUC-based polygons
	•	floodplains/ → FEMA and reconstructed floodplain layers
	•	Other files → generalized or statewide hydrology vectors

⸻

🧭 File Conventions
	•	Vectors → GeoJSON (.json, .geojson)
	•	Rasters → Cloud-Optimized GeoTIFFs (.tif) for flood models & depth grids
	•	Tables → CSV (.csv) for gauges, time series, metadata
	•	Projection → EPSG:4326 (WGS84 lat/long) required for all outputs

⸻

🔄 Workflow
	1.	Acquire raw sources → data/raw/
	•	Sources: USGS NHD, NOAA NWIS, FEMA, Kansas GIS Hub
	2.	Process
	•	Clean, reproject to EPSG:4326
	•	Simplify/dissolve geometries as needed
	•	Export to GeoJSON / COG / CSV
	3.	Checksums

scripts/gen_sha256.sh data/processed/hydrology/*


	4.	Register in STAC
	•	Add/update Item JSON under data/stac/items/hydrology/
	•	Link assets with roles: ["data"] + checksum:sha256
	5.	Validate

make stac-validate
pre-commit run stac-validate --all-files



⸻

📑 Example STAC Items

Watershed (HUC12, vector)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_watersheds_huc12",
  "properties": {
    "title": "Kansas Watersheds (HUC12)",
    "description": "Hydrologic Unit Code 12 polygons for Kansas watersheds.",
    "datetime": "2020-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "Delineated from USGS NHD & DEM flow accumulation",
    "kfm:lineage": [
      "data/raw/hydrology/nhd/ks_huc12.gpkg"
    ],
    "qa:status": "verified"
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../stac/collections/hydrology.json"
    }
  ],
  "assets": {
    "geojson": {
      "href": "../../../data/processed/hydrology/watersheds/ks_watersheds_huc12.json",
      "title": "Kansas Watersheds (HUC12)",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    }
  }
}

Floodplain (FEMA, raster COG)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_floodplain_100yr",
  "properties": {
    "title": "Kansas 100-Year Floodplain (FEMA)",
    "description": "Derived floodplain extent for Kansas based on FEMA DFIRMs.",
    "datetime": "2021-01-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "Rasterized FEMA DFIRM flood zones to 100-year flood extent",
    "kfm:lineage": [
      "data/raw/hydrology/fema/dfirm_ks_2021.gdb"
    ],
    "qa:status": "provisional"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99],
      [-102.05, 40.00],
      [-94.59, 40.00],
      [-94.59, 36.99],
      [-102.05, 36.99]
    ]]
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../../stac/collections/hydrology.json"
    }
  ],
  "assets": {
    "cog": {
      "href": "../../../data/processed/hydrology/floodplains/ks_floodplain_100yr.tif",
      "title": "Kansas 100-Year Floodplain (FEMA, 2021)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "raster"]
    }
  }
}


⸻

🔗 Integration
	•	Web Viewer → layers referenced in web/config/layers.json for MapLibre visualization
	•	Experiments → floodplain reconstruction, treaty overlays, archaeology + erosion studies
	•	Knowledge Hub → cross-links hydrology with treaties, settlements, geology, environment

⸻

📝 Notes
	•	❌ Do not manually edit processed outputs
	•	✅ Always regenerate from raw + documented scripts or notebooks
	•	Use stable filenames (<theme>_<year>.json) so STAC + web configs remain valid
	•	Track large files with Git LFS / DVC
	•	Document provenance + methods in experiments/<ID>_.../experiment.md

⸻

📚 See Also
	•	data/raw/ → raw hydrology sources
	•	data/processed/dem/vectors/ → DEM-derived stream networks + basins
	•	data/stac/items/hydrology/ → STAC Items for hydrology datasets
	•	experiments/ → MCP-style experiment logs for hydrology modeling

⸻

✅ Mission Principle

Hydrology datasets must be consistent, reproducible, STAC-linked, and ready
for cross-domain analysis in the Kansas Frontier Matrix.