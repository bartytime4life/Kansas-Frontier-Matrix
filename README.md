# Kansas Geo Timeline — **Time · Terrain · History**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](pyproject.toml)

A minimal **Google Earth + Web (GitHub Pages)** mapping system for Kansas elevation and historical layers.

- **Earth deliverables**: regionated **KML/KMZ** (progressive loading via NetworkLinks)  
- **Web app**: lightweight **MapLibre** viewer with a **time slider**  
- **Catalog**: **STAC 1.0.0** (Catalog → Collections → Items) for clean provenance  
- **Pipelines**: `Makefile` targets to **fetch → COG → derivatives (slope/aspect/hillshade) → site**  
- **CLI**: `kgt` (Kansas Geo Timeline) for STAC validation, listing, and web-config rendering  

> Start small (one county), then scale out. Keep STAC tight and versioned.

---

## 🌐 Live Demo

- **Web Viewer (MapLibre + Time Slider)** → [View Demo](https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/)  
- **Google Earth KMZ (download)** → [Kansas_Terrain.kmz](https://bartytime4life.github.io/Kansas-Frontier-Matrix/earth/Kansas_Terrain.kmz)

---

## Pipeline Overview

```mermaid
flowchart TD
    A[Data Sources] -->|fetch| B[COGs (DEM, overlays)]
    B -->|terrain| C[Derivatives (slope, aspect, hillshade)]
    C -->|stac| D[STAC Catalog & Items]
    D -->|render-config| E[Web Viewer Config (app.config.json)]
    D -->|kml| F[KML/KMZ for Google Earth]
    E -->|serve| G[MapLibre Web Viewer]
    F --> H[Google Earth 3D]


⸻

Table of Contents
	•	Quickstart
	•	Repository layout
	•	Install
	•	Make targets
	•	Data sources (examples)
	•	STAC structure
	•	CLI (kgt) usage
	•	Web viewer (MapLibre + time)
	•	Google Earth (KML/KMZ)
	•	Checks & reproducibility
	•	CI: GitHub Pages publish
	•	Troubleshooting
	•	Roadmap
	•	Requirements
	•	Status snapshot

⸻

Quickstart

# Python env (3.10+ recommended)
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt

# 1) Configure sources (edit data/sources/*.json)
# 2) Build a tiny slice end-to-end
make fetch
make cogs
make terrain
make stac

# 3) Validate STAC + render viewer config
kgt validate-stac stac/items --no-strict
kgt render-config --stac stac/items --output web/app.config.json --pretty

# 4) Serve the viewer locally
python -m http.server -d web 8080

Tip: prefer make stac-validate if using the repo’s validator scripts.

⸻

Repository layout

data/                        # inputs/outputs (COGs, JSON metadata)
  sources/                   # source descriptors (endpoints, CRS, bounds, license)
  processed/                 # generated COGs/tiles and artifacts
stac/                        # STAC 1.0.0: catalog + collections + items
  catalog.json
  collections/
    elevation.json
    historic_topo.json
  items/
    ks_1m_dem_2018_2020.json
    overlays/
      usgs_topo_larned_1894.json
scripts/                     # small, dependency-light tools (Python/bash)
web/                         # static site (MapLibre) for GitHub Pages
docker/                      # container env (reproducible build)
mcp/                         # SOPs/experiments/model cards (reproducibility)


⸻

Install

pip install -r requirements.txt
# optional extras for CLI features
pip install "jsonschema>=4.0" "jinja2>=3.1"

Expose the CLI (via pyproject.toml):

[project.scripts]
kgt = "kansas_geo_timeline.cli:main"


⸻

Make targets

make help          # show all tasks
make fetch         # download/input prep via data/sources/*.json
make cogs          # convert rasters to Cloud Optimized GeoTIFFs (COGs)
make terrain       # derive hillshade/slope/aspect from DEMs
make stac          # (re)generate stac/{items,collections}
make stac-validate # validate sources + STAC
make site          # write a simple web/layers.json
make site-config   # render web/app.config.json via kgt + Jinja2
make clean         # remove intermediates (keeps ./stac)


⸻

Data sources (examples)

DEM (data/sources/ks_dem.json)

{
  "id": "ks_dem_1m",
  "title": "Kansas DEM (1 m)",
  "type": "raster-dem",
  "endpoint": {
    "type": "arcgis",
    "url": "https://tiles.kansasgis.org/arcgis/rest/services/Elevation/KS_1m_DEM/ImageServer"
  },
  "spatial": { "bbox": [-102.10, 36.99, -94.60, 40.00], "crs": "EPSG:4326" },
  "temporal": { "start": "2018-01-01", "end": "2020-12-31" },
  "license": "CC-BY-4.0",
  "outputs": {
    "cog": "data/cogs/dem/ks_1m_dem_2018_2020.tif",
    "hillshade": "data/cogs/hillshade/ks_hillshade_2018_2020.tif"
  }
}

Historic topo (data/sources/usgs_historic_topo.json)

{
  "id": "usgs_topo_1894_1950",
  "type": "raster",
  "endpoint": {
    "type": "http",
    "urls": [
      "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/USGS_15x15_1894_Larned_Geo.tif"
    ]
  },
  "temporal": { "start": "1894-01-01", "end": "1950-12-31" },
  "spatial": { "bbox": [-100.10, 37.90, -98.80, 38.60], "crs": "EPSG:4326" },
  "license": "USGS-PD",
  "style": { "opacity": 0.8 }
}


⸻

STAC structure
	•	Root catalog → stac/catalog.json
	•	Collections:
	•	elevation.json
	•	historic_topo.json
	•	Items:
	•	DEM → stac/items/ks_1m_dem_2018_2020.json
	•	Overlay → stac/items/overlays/usgs_topo_larned_1894.json

Validate:

kgt validate-stac stac/items --no-strict


⸻

CLI (kgt) usage
	•	Validate STAC:

kgt validate-stac stac/items --report-json build/stac_report.json


	•	Render viewer config:

kgt render-config --stac stac/items --output web/app.config.json --pretty


	•	Summarize items:

kgt list-stac stac/items --format csv --output build/items.csv



⸻

Web viewer (MapLibre + time)

web/app.config.json (generated via kgt render-config) drives the viewer.

Serve locally:

python -m http.server -d web 8080

Or open the live GitHub Pages demo:
👉 Kansas Geo Timeline Viewer

⸻

Google Earth (KML/KMZ)

Regionated overlays export into earth/:

earth/
  Kansas_Terrain.kmz
  networklinks/
    ks_1m_hillshade.kml
    usgs_topo_1894.kml

Download demo KMZ:
👉 Kansas_Terrain.kmz

⸻

Checks & reproducibility
	•	Run make stac-validate before commits
	•	Stamp _meta.json with provenance
	•	Add checksum:sha256 to COG assets

⸻

CI: GitHub Pages publish

See .github/workflows/site.yml → runs STAC validation and deploys web/ automatically.

⸻

Troubleshooting
	•	jinja2 missing → pip install jinja2
	•	JSON schema warnings → pip install jsonschema
	•	Blank map → check web/app.config.json + asset hrefs
	•	ArcGIS reprojection oddities → confirm CRS settings

⸻

Roadmap
	1.	Historic topo, statewide hillshade, treaty/railroad vectors
	2.	Time slider v1 (year filter, opacity controls)
	3.	Google Earth polish (per-decade folders)
	4.	Auto _meta.json + STAC refresh in make stac
	5.	CI validation + GitHub Pages publish
	6.	Story stub (e.g. Santa Fe Trail)
	7.	Stretch goal: CesiumJS 3D terrain

⸻

Requirements
	•	rasterio
	•	rio-cogeo
	•	pyproj
	•	shapely
	•	pystac
	•	jsonschema (optional)
	•	jinja2 (optional)
	•	Pillow

⸻

Status snapshot

Layer	STAC Item	Asset Path
DEM (1 m, 2018–2020)	stac/items/ks_1m_dem_2018_2020.json	data/cogs/dem/ks_1m_dem_2018_2020.tif
Hillshade (derived)	same Item (assets.hillshade)	data/cogs/hillshade/ks_hillshade_2018_2020.tif
Historic Topo (Larned 1894)	stac/items/overlays/usgs_topo_larned_1894.json	data/cogs/overlays/usgs_topo_larned_1894.tif


⸻

PRs welcome! ✅ Stick to STAC 1.0.0, keep links relative, and validate before commit.

---
