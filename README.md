# Kansas Geo Timeline — **Time · Terrain · History**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](.github/.pre-commit-config.yaml)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](pyproject.toml)
[![Node](https://img.shields.io/badge/node-18+-green.svg)](package.json)
[![STAC](https://img.shields.io/badge/STAC-1.0.0-0A7BBB.svg)](stac/catalog.json)
[![MapLibre](https://img.shields.io/badge/MapLibre-Web%20Viewer-1f6feb.svg)](web/index.html)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 🌟 What is this?

The **Kansas Geo Timeline** is an open-source system to explore **Kansas’s terrain and history through time**.  
It combines **scientific-grade geospatial data** with **storytelling layers**:

- Elevation (LiDAR DEM, shaded relief, slope, aspect)  
- Historic maps (USGS topo scans, overlays)  
- Cultural & historical layers (treaties, railroads, towns, trails)  
- Environmental layers (land cover, soils, hydrology, wildfires, tornadoes)  

All datasets are tracked, validated, and published using **STAC 1.0.0**, then rendered via a **MapLibre web viewer** with a **timeline slider** and optional **Google Earth KML/KMZ exports**.

Think of it as a **time-aware atlas + knowledge hub**.

---

## 🚀 Live Access

- 🌐 **Web Viewer**: [MapLibre + Timeline](https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/)  
- 🌍 **Google Earth**: [Kansas Terrain KMZ](https://bartytime4life.github.io/Kansas-Frontier-Matrix/earth/Kansas_Terrain.kmz)  

---

## 📊 How the System Works

```mermaid
flowchart TD
  A["Sources\n(data/sources/*.json)"] -->|fetch| B["COGs\n(data/cogs/**/*.tif)"]
  B -->|derive| C["Terrain & Overlays\n(data/derivatives/*)"]
  C -->|index| D["STAC\n(stac/catalog.json, items/)"]
  D -->|render| E["Configs\n(web/app.config.json)"]
  E -->|serve| F["MapLibre Viewer"]
  D -->|export| G["KML/KMZ\n(earth/)"]

classDef src fill=#FFD166,stroke=#333;
classDef cogs fill=#06D6A0,stroke=#333;
classDef stac fill=#118AB2,stroke=#fff;
classDef web fill=#073B4C,stroke=#fff;
classDef earth fill=#EF476F,stroke=#fff;

class A src; class B cogs; class C cogs; class D stac; class E web; class F web; class G earth;
````

---

## 🛠 Quickstart

### Option A — Local Python

```bash
# Setup
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Build pipeline
make fetch           # download raw data
make cogs            # convert GeoTIFF → COG
make terrain         # slope, aspect, hillshade
make stac            # generate STAC catalog/items
make stac-validate   # validate
make site-config     # build web/app.config.json
python -m http.server -d web 8080
```

### Option B — Docker Compose

```bash
docker compose build kfm
docker compose --profile dev up -d site   # serve viewer
docker compose --profile docs up -d docs  # serve live docs
```

---

## 📂 Repository Layout

```
data/
  sources/       # JSON descriptors (URL, CRS, bounds, license)
  cogs/          # Cloud Optimized GeoTIFFs (immutable)
  derivatives/   # terrain, contours, hydrology, etc.
  processed/     # vectors/rasters post-cleanup
stac/            # STAC 1.0.0 catalog, collections, items
web/             # static site for GitHub Pages
  config/        # legend.json, categories.json, sources.json, schema
  data/          # small vectors (mirrored for dev)
  tiles/         # optional raster tiles {z}/{x}/{y}.png
earth/           # KMZ/KML exports
scripts/         # ETL, STAC tools, config renderers
docker/          # reproducible environments
.github/         # CI/CD workflows
```

---

## 📑 Data Sources (examples)

| ID             | Title                  | File                                                  | Notes                   |
| -------------- | ---------------------- | ----------------------------------------------------- | ----------------------- |
| `ks_dem_1m`    | Kansas DEM (1 m LiDAR) | [`ks_dem.json`](data/sources/ks_dem.json)             | ArcGIS ImageServer      |
| `usgs_topo`    | Historic USGS Topos    | [`usgs_topo.json`](data/sources/usgs_topo.json)       | 1894–1950 GeoTIFF scans |
| `ks_treaties`  | Kansas Treaties        | [`ks_treaties.json`](data/sources/ks_treaties.json)   | Time-aware polygons     |
| `ks_railroads` | Railroads (historic)   | [`ks_railroads.json`](data/sources/ks_railroads.json) | Digitized vectors       |

---

## 🧰 Make Targets

```bash
make fetch           # download raw sources
make cogs            # raw GeoTIFF → COG
make terrain         # gdaldem slope/aspect/hillshade
make stac            # build STAC catalog + items
make stac-validate   # validate catalog/items
make site-config     # render web/app.config.json
make site            # fallback: write web/layers.json + mirror small vectors
make prebuild        # validation + configs (CI shortcut)
```

Optional:

```bash
make validate-cogs   # conformance checks
make mosaic-county   # county-level LiDAR mosaics
make dem-checksum    # write/verify .sha256
make regionate       # regionated KML/KMZ tree
```

---

## ✅ Reproducibility & CI

* `.sha256` and `.meta.json` sidecars for every major artifact
* CI builds:

  * `site.yml` → GitHub Pages
  * `stac-badges.yml` → Shields endpoint badges
  * `codeql.yml` + `trivy.yml` → security
* Pre-commit hooks: lint, format, STAC/config validate

Run before pushing:

```bash
make prebuild
```

---

## 🗺 Roadmap

* **Milestone 1**: Enrich Data Sources (DEM, treaties, railroads)
* **Milestone 2**: Terrain + Hydrology analysis
* **Milestone 3**: Storytelling & Education layers
* **Milestone 4**: Technical enhancements (tiles, UI)
* **Milestone 5**: MCP integration (scientific method protocols)

See [`ROADMAP.md`](ROADMAP.md) for details.

---

## 📦 Requirements

* Python: `rasterio`, `rio-cogeo`, `pyproj`, `shapely`, `pystac`, `jsonschema`
* GDAL CLI: `gdal_translate`, `gdalwarp`, `gdaldem`, `gdalinfo`
* Node: build utilities + roadmap sync
* Docker: reproducible builds

---

## 💡 Troubleshooting

* **Mermaid fails to render** → quote labels, use `\n` for line breaks
* **Rasters don’t show** → serve tiles or COGs, not raw `.tif`
* **Timeline inert** → layer must have `time.start/end` or `timeProperty`
* **Legend chips missing** → set `legendKey` or define in `legend.json`
* **File:// blocked** → serve via HTTP (`python -m http.server` or Docker dev site)

---

**PRs welcome.**
Keep STAC 1.0.0 valid, configs schema-checked, and provenance intact.

```

---

### Why this rebuild is cleaner

- **Narrative-first**: starts with *what/why*, then flows into tech.  
- **Modern repo map**: directory tree matches your actual structure.  
- **Mermaid-safe**: chart quotes + line breaks.  
- **Quickstart split**: Python (venv) vs Docker Compose.  
- **CI + reproducibility** section consolidated (checksums, badges, workflows).  
- **Troubleshooting** distilled to common gotchas.  
- **Roadmap** simplified into milestones, pointing to `ROADMAP.md`.

---
