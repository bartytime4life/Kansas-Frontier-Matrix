<div align="center">

# 🌐 Kansas Geo Timeline — Earth Data Sources

Catalog of **Earth-observation and global reference datasets**  
that provide the **planetary context** for Kansas history.  

These include DEMs, climate normals, satellite imagery, basemaps, and global hazard layers.  
They **complement Kansas-specific sources** in `data/sources/` and are referenced via STAC metadata.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Global Earth sources\n(data/earth/sources/*.json)"] --> B["Fetch\n(make fetch)"]
  B --> C["Raw archives\n(data/earth/raw/**)"]
  C --> D["Processed outputs\n(COG, GeoJSON, MBTiles)\n(data/earth/processed/**)"]
  D --> E["STAC Items\n(data/earth/stac/items/**)"]
  E --> F["Validate\n(make stac-validate)"]
  F --> G["Viewer integration\n(web/app.config.json)"]

<!-- END OF MERMAID -->



⸻

🎯 Purpose
	•	Anchor Kansas datasets within a global geospatial framework.
	•	Provide baseline Earth data (terrain, imagery, climate, hazards).
	•	Enable Kansas vs. Plains vs. World comparisons.
	•	Integrate NASA/NOAA/USGS reference products.
	•	Maintain provenance for scientific reproducibility (MCP).

⸻

📂 Directory layout

data/earth/sources/
├── dem_global.json       # SRTM, NASADEM, Copernicus DEMs
├── landsat.json          # Landsat scenes/collections
├── modis.json            # MODIS time series (NDVI, fire, snow)
├── sentinel2.json        # Sentinel-2 MSI imagery (10–20 m)
├── climate_global.json   # WorldClim / ERA5 / Daymet / NOAA GHCN
├── hazards_global.json   # EM-DAT, FIRMS, GFDRR hazard maps
├── tectonics.json        # Global faults, seismic hazard
└── README.md


⸻

🌍 Data domains

Terrain & DEM
	•	SRTM — 30 m global DEM.
	•	NASADEM / Copernicus DEM — improved 30 m products.
	•	Used for comparison with Kansas LiDAR DEMs.

Satellite imagery
	•	Landsat (1972–present) — long-term Earth record.
	•	MODIS (2000–present) — daily to 8-day composites.
	•	Sentinel-2 (2015–present) — 10–20 m resolution, vegetation change.
	•	Global holdings give context baselines for Kansas subsets.

Climate & environment
	•	WorldClim — historical and projected normals.
	•	ERA5 (ECMWF) — hourly global reanalysis.
	•	Daymet — 1 km daily climate (North America).
	•	NOAA GHCN — global station datasets.

Hazards
	•	NASA FIRMS — global fire detections.
	•	EM-DAT — disaster database.
	•	USGS ShakeMap / GEM Seismic Hazard — earthquake context.
	•	GFDRR — global hazard layers (floods, cyclones, landslides).

Geology & tectonics
	•	USGS Global Faults & Folds.
	•	OneGeology / CGMW tectonic maps.
	•	Provides geologic backdrop for Kansas seismicity.

⸻

🛠️ Integration
	•	Each .json conforms to sources_catalog.schema.json.
	•	Metadata includes:
	•	id, title, urls or API endpoints
	•	spatial (bbox, CRS)
	•	temporal (coverage)
	•	license, attribution

Processing:
	•	Convert to COGs (rasters) or GeoJSON/PMTiles (vectors).
	•	Register in STAC Items under stac/items/earth/.

⸻

📝 Notes
	•	Kansas-centric datasets live under data/sources/.
	•	data/earth/sources/ is for global context layers only.
	•	All datasets must include checksums (.sha256) and provenance sidecars.
	•	Follow MCP reproducibility principles: every source must be documented, validated, and traceable.

⸻

📚 See also
	•	data/sources/topo/README.md — Kansas DEM & topo sources.
	•	data/stac/ — STAC catalog and item registry.
	•	docs/ — MCP templates and glossary.

⸻

✅ Mission-grade principle: Earth data sources must be standardized, reproducible, and globally contextual,
anchoring Kansas datasets within the planetary geospatial fabric.

