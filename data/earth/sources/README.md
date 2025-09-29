# Kansas-Frontier-Matrix — Earth Data Sources

This directory catalogs **Earth-observation and global reference datasets**  
that underpin the Kansas Frontier Matrix. These sources provide the  
**planetary context** for Kansas history — from DEMs and climate normals  
to satellite basemaps and global hazards. They complement Kansas-specific  
layers in `data/sources/` and are referenced by STAC metadata.

---

## Purpose

- Anchor Kansas datasets within a **global geospatial framework**.  
- Provide **baseline Earth data** (terrain, imagery, hazards, climate).  
- Support **comparisons across scales** (Kansas vs. Plains vs. World).  
- Enable **integration of NASA/NOAA/USGS reference products**.  
- Document provenance for **scientific reproducibility (MCP style)** [oai_citation:0‡Foundational Templates and Glossary for Scientific Method _ Research _ Master Coder Protocol.pdf](file-service://file-XygDDSfCPa5gz3jmjRV81b).  

---

## Directory Layout

data/earth/sources/
├── dem_global.json           # SRTM, Copernicus, or NASADEM global DEMs
├── landsat.json              # Landsat scenes/collections (surface reflectance)
├── modis.json                # MODIS time series (NDVI, fire, snow)
├── sentinel2.json            # Sentinel-2 MSI imagery (10–20 m)
├── climate_global.json       # WorldClim / ERA5 / Daymet / NOAA GHCN gridded
├── hazards_global.json       # EM-DAT, NASA FIRMS fire, GFDRR hazard maps
├── tectonics.json            # Global faults, seismic hazard maps (USGS GEM)
└── README.md                 # This file

---

## Data Domains

### 🌍 Global Terrain & DEM
- **SRTM (Shuttle Radar Topography Mission)** — 30 m global DEM.  
- **NASADEM / Copernicus DEM** — improved versions, ~30 m.  
- Used to compare with Kansas 1-m LiDAR [oai_citation:1‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS).

### 🛰️ Satellite Imagery
- **Landsat (USGS/NASA, 1972–present)** — long-term Earth record.  
- **MODIS (NASA, 2000–present)** — daily to 8-day composites.  
- **Sentinel-2 (ESA, 2015–present)** — higher resolution, vegetation change.  
- All can be subset to Kansas, but global holdings provide **baselines**.

### 🌡️ Climate & Environmental
- **WorldClim** — historical and projected climate normals.  
- **ERA5 (ECMWF)** — hourly reanalysis, global.  
- **Daymet** (NASA ORNL DAAC) — 1-km daily climate for North America [oai_citation:2‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).  
- **NOAA GHCN** — global station datasets [oai_citation:3‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).

### ⚠️ Hazards
- **NASA FIRMS** — global fire detections.  
- **EM-DAT (CRED)** — global disaster database.  
- **USGS ShakeMap / GEM Global Seismic Hazard** — earthquake context.  
- **GFDRR hazard layers** — floods, cyclones, landslides.

### 🌐 Geology & Tectonics
- **USGS Global Faults & Folds**.  
- **OneGeology / CGMW tectonic maps**.  
- Provides backdrop for Kansas seismicity [oai_citation:4‡Data Resources for Kansas.pdf](file-service://file-3VZh97sQTEG1TSo7jN7w8p).

---

## Integration

- Each `.json` file conforms to `sources_catalog.schema.json`.  
- Metadata includes:  
  - `id`, `title`, `url(s)` or API endpoints  
  - `spatial` (bbox, CRS)  
  - `temporal` (coverage dates)  
  - `license` and `attribution`  
- Datasets are converted into **COGs (for rasters)** and **GeoJSON/PMTiles (for vectors)** [oai_citation:5‡Kansas Frontier Matrix – GIS Archive & Deeds Data Integration Guide.pdf](file-service://file-A8GiBPZM1dWsKG68SXPHjE).  
- Linked to **STAC items** under `stac/items/earth/`.

---

## Notes

- Kansas-centric sources live under `data/sources/` (e.g. `topo/`, `hydro/`).  
- This directory holds **global reference data**, useful for context and comparisons.  
- All data must have **checksums** (`.sha256`) and provenance sidecars, per MCP reproducibility guidelines [oai_citation:6‡Foundational Templates and Glossary for Scientific Method _ Research _ Master Coder Protocol.pdf](file-service://file-XygDDSfCPa5gz3jmjRV81b) [oai_citation:7‡Kansas Data Resources for Frontier-Matrix Project.pdf](file-service://file-Q9AC5RwLTeV6QgadxHDf5P).  

---

## See Also

- `data/sources/topo/README.md` — Kansas DEM and topo sources.  
- `data/stac/` — STAC catalog and items for all datasets.  
- `docs/` — MCP protocols, experiment templates, glossary.