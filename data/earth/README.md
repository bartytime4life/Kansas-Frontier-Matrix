<div align="center">

# 🌍 Kansas-Frontier-Matrix — Earth Context Layers  
`data/earth/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](../../.github/workflows/stac-badges.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.pre-commit-config.yaml)

**Mission:** Curate **Earth observation datasets** and **global reference layers**  
to provide **context, baselines, and environmental indices**  
that complement Kansas-focused datasets in the Frontier Matrix.  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Source Descriptors\n(data/earth/sources/*.json)"] --> B["Fetch\n(make fetch)"]
  B --> C["Raw Downloads\n(data/earth/raw/*)"]
  C --> D["Processing (COG, GeoJSON, PMTiles)\n(data/earth/processed/*)"]
  D --> E["STAC Items\n(data/earth/stac/items/*)"]
  E --> F["Validation\n(make stac-validate)"]
  F --> G["Viewer Integration\n(web/app.config.json)"]

<!-- END OF MERMAID -->



⸻

🧭 Scope
	•	🌍 Global context → datasets beyond Kansas boundaries.
	•	🛰️ Remote sensing → MODIS, Sentinel, Landsat, Daymet, NLCD, GEDI, HydroSHEDS.
	•	🌱 Environmental indices → NDVI, EVI, drought indices, fire perimeters, soils.
	•	🗺️ Basemaps → Natural Earth, coastlines, rivers, political boundaries, global DEM/topo.

Kansas remains the core. Earth datasets exist only for comparison and context.

⸻

📂 Directory Layout

data/earth/
├── sources/       # JSON descriptors (STAC-style metadata)
├── raw/           # Untouched downloads (archives, HDF, NetCDF, GeoTIFF)
├── processed/     # Cleaned/reprojected COGs, GeoJSON, PMTiles
├── stac/          # STAC Items & Collections
└── README.md

	•	sources/ → dataset configs (endpoint, license, bbox, temporal).
	•	raw/ → direct downloads (no modification).
	•	processed/ → converted products (COG, GeoJSON, PMTiles).
	•	stac/ → metadata linking into catalog/collections.

⸻

⚙️ Conventions
	•	CRS → EPSG:4326 (WGS84) unless documented otherwise.
	•	Rasters → Cloud-Optimized GeoTIFF (.tif) with internal overviews.
	•	Vectors → GeoJSON (small/medium) or PMTiles (large).
	•	Metadata → every dataset must have a STAC Item in stac/items/.
	•	Checksums → .sha256 sidecars for all raw + processed artifacts.

⸻

🔗 Repo Connections
	•	stac-badges.yml → validates data/earth/stac/**, builds Shields badges.
	•	stac.yml → generates web/app.config.json (includes Earth layers).
	•	site.yml → deploys processed datasets into MapLibre viewer.

⸻

📋 Common Tasks

➕ Add a new dataset
	1.	Create data/earth/sources/<dataset>.json.
	2.	Run make fetch → saves to data/earth/raw/.
	3.	Convert: make cogs (rasters) or make vectors (shapefiles → GeoJSON).
	4.	Write STAC Item → data/earth/stac/items/.
	5.	Validate → make stac-validate.

♻️ Update an existing dataset
	•	Update source JSON → rerun make fetch + reprocess.
	•	Refresh STAC Item and validate.

🔗 Link to viewer
	•	Reference STAC Item in scripts/badges/source_map.json.
	•	Rebuild config → make stac.

⸻

📑 Example STAC Item (MODIS NDVI, 2020)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "earth_modis_ndvi_2020",
  "properties": {
    "title": "MODIS NDVI (2020)",
    "description": "Global MODIS NDVI annual composite for 2020, subsettable for Kansas context.",
    "start_datetime": "2020-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z",
    "proj:epsg": 4326,
    "kfm:method": "NASA MODIS MOD13A3 v6.1 annual NDVI composite",
    "kfm:lineage": [
      "data/earth/raw/MODIS/MOD13A3.A2020001.hdf"
    ],
    "processing:software": "GDAL 3.9.0 (Docker image ghcr.io/bartytime4life/kfm-gdal:3.9.0)",
    "qa:status": "provisional"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-180.0, -90.0],
      [-180.0, 90.0],
      [180.0, 90.0],
      [180.0, -90.0],
      [-180.0, -90.0]
    ]]
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../stac/collections/earth.json"
    }
  ],
  "assets": {
    "cog": {
      "href": "../../data/earth/processed/modis_ndvi_2020.tif",
      "title": "MODIS NDVI 2020 (COG)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "raster"]
    },
    "pmtiles": {
      "href": "../../data/earth/processed/modis_ndvi_2020.pmtiles",
      "title": "MODIS NDVI 2020 (PMTiles)",
      "type": "application/vnd.pmtiles",
      "roles": ["data", "tiles"]
    }
  }
}


⸻

📝 Notes
	•	Global datasets can be very large → subset by year or tile.
	•	Always record license in sources/*.json (NASA EarthData, Copernicus, CC-BY-4.0).
	•	Use scripts/gen_sha256.sh to hash large files after fetch.

⸻

✅ Mission Principle

Kansas is the focus.
Earth datasets are included only to strengthen Kansas analysis by providing:
	•	climate + environmental baselines,
	•	comparative global indices,
	•	and reference context for geospatial history.