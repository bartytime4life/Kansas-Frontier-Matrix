<div align="center">

# 🌐 Kansas-Frontier-Matrix — Earth Data Sources  
`data/earth/sources/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Catalog **Earth-observation and global reference datasets**  
that provide the **planetary context** for Kansas history.  

These include DEMs, climate normals, satellite imagery, basemaps, and global hazard layers.  
They **complement Kansas-specific sources** in `data/sources/` and are referenced via **STAC metadata**.  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Global Earth sources\n(data/earth/sources/*.json)"] --> B["Fetch\n(make fetch)"]
  B --> C["Raw archives\n(data/earth/raw/**)"]
  C --> D["Processed outputs\n(COG, GeoJSON, PMTiles)\n(data/earth/processed/**)"]
  D --> E["STAC Items\n(data/earth/stac/items/**)"]
  E --> F["Validate\n(make stac-validate)"]
  F --> G["Viewer integration\n(web/app.config.json)"]

<!-- END OF MERMAID -->



⸻

🎯 Purpose
	•	Anchor Kansas datasets within a global geospatial framework.
	•	Provide baseline Earth data (terrain, imagery, climate, hazards).
	•	Enable Kansas ↔ Plains ↔ World comparisons.
	•	Integrate NASA / NOAA / USGS reference products.
	•	Maintain provenance and scientific reproducibility (MCP principles).

⸻

📂 Directory Layout

data/earth/sources/
├── dem_global.json       # SRTM, NASADEM, Copernicus DEMs
├── landsat.json          # Landsat scenes/collections
├── modis.json            # MODIS time series (NDVI, fire, snow)
├── sentinel2.json        # Sentinel-2 MSI imagery (10–20 m)
├── climate_global.json   # WorldClim / ERA5 / Daymet / NOAA GHCN
├── hazards_global.json   # EM-DAT, FIRMS, GFDRR hazard maps
├── tectonics.json        # Global faults, seismic hazard
└── README.md

	•	Each *.json conforms to sources_catalog.schema.json.
	•	Metadata fields include:
	•	id, title, urls or API endpoints
	•	spatial (bbox, CRS)
	•	temporal coverage
	•	license & attribution

⸻

🌍 Data Domains

Terrain & DEM
	•	SRTM — 30 m global DEM.
	•	NASADEM / Copernicus DEM — improved global DEMs.
	•	Provides comparison with Kansas LiDAR DEMs.

Satellite Imagery
	•	Landsat (1972–present) — long-term record.
	•	MODIS (2000–present) — daily to 8-day composites.
	•	Sentinel-2 (2015–present) — 10–20 m resolution.
	•	Context baselines for Kansas subsets.

Climate & Environment
	•	WorldClim — historical & projected normals.
	•	ERA5 (ECMWF) — hourly reanalysis.
	•	Daymet — 1 km daily climate (North America).
	•	NOAA GHCN — station datasets.

Hazards
	•	NASA FIRMS — global fire detections.
	•	EM-DAT — disaster database.
	•	USGS ShakeMap / GEM — seismic hazard and events.
	•	GFDRR — floods, cyclones, landslides.

Geology & Tectonics
	•	USGS Global Faults & Folds.
	•	OneGeology / CGMW tectonic maps.
	•	Provides seismic & geologic backdrop for Kansas.

⸻

🛠️ Integration
	•	Each JSON source descriptor → fetchable + reproducible.
	•	Processing outputs:
	•	Rasters → COGs
	•	Vectors → GeoJSON / PMTiles
	•	Register in STAC Items under stac/items/earth/.
	•	Validate with CI (make stac-validate).

⸻

📑 Example Source Descriptor (modis.json)

{
  "id": "earth_modis",
  "title": "MODIS Global NDVI (MOD13A3)",
  "description": "Global MODIS NDVI monthly composites for environmental monitoring, subsettable for Kansas.",
  "type": "raster",
  "format": "HDF",
  "providers": [
    {
      "name": "NASA LP DAAC",
      "roles": ["producer", "licensor"],
      "url": "https://lpdaac.usgs.gov/"
    }
  ],
  "license": "NASA Data Policy (free & open)",
  "temporal": {
    "start": "2000-02-18",
    "end": null,
    "resolution": "monthly"
  },
  "spatial": {
    "bbox": [-180, -90, 180, 90],
    "crs": "EPSG:4326"
  },
  "assets": {
    "source": {
      "href": "https://e4ftl01.cr.usgs.gov/MOLT/MOD13A3.061/",
      "type": "application/x-hdf"
    }
  },
  "provenance": {
    "created": "2025-10-01",
    "commit": "abc123def456",
    "checksum:sha256": "placeholder_for_sha256_hash"
  }
}


⸻

📝 Notes
	•	Kansas-centric datasets → data/sources/.
	•	data/earth/sources/ → global context layers only.
	•	All datasets must include .sha256 checksums + provenance sidecars.
	•	Follow MCP: every source must be documented, validated, and reproducible.

⸻

📚 See Also
	•	data/sources/topo/README.md → Kansas DEM & topo sources.
	•	data/stac/ → STAC catalog & registry.
	•	docs/ → MCP templates & glossary.

⸻

✅ Mission Principle

Earth data sources must be standardized, reproducible, and globally contextual,
anchoring Kansas datasets within the planetary geospatial fabric.