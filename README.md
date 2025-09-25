# Kansas Geo Timeline — **Time · Terrain · History**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate & Badges](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](.pre-commit-config.yaml)
[![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](pyproject.toml)
[![Node](https://img.shields.io/badge/node-18%2B-brightgreen.svg)](package.json)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg?logo=docker&logoColor=white)](docker/Dockerfile)
[![STAC](https://img.shields.io/badge/STAC-1.0.0-0A7BBB.svg)](stac/catalog.json)
[![MapLibre](https://img.shields.io/badge/MapLibre-Web%20Viewer-1f6feb.svg)](web/index.html)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 📋 Project Metadata

| Component  | Minimum / Spec | Key Files | Notes |
|---|---|---|---|
| Python | **3.10+** | [`pyproject.toml`](pyproject.toml) · [`requirements.txt`](requirements.txt) | CLI `kgt`, STAC tools, raster pipeline |
| Node | **18+** | [`package.json`](package.json) | Optional: docs/dev tooling; web is static |
| Docker | Multi-stage | [`docker/Dockerfile`](docker/Dockerfile) · [`docker/compose.yaml`](docker/compose.yaml) | Reproducible builds; mount data at runtime |
| STAC | **1.0.0** | [`stac/catalog.json`](stac/catalog.json) · [`stac/collections/`](stac/collections) · [`stac/items/`](stac/items) | Catalog → Collections → Items |
| Web | MapLibre viewer | [`web/index.html`](web/index.html) · [`web/app.config.json`](web/app.config.json) | Time slider; STAC-driven config |
| CI | GitHub Actions | [`site.yml`](.github/workflows/site.yml) · [`stac-badges.yml`](.github/workflows/stac-badges.yml) | Build & deploy Pages; STAC checks; badge JSONs |
| Quality | Hooks & lint | [`.pre-commit-config.yaml`](.pre-commit-config.yaml) | Ruff, yamllint, prettier, actionlint, etc. |
| License | MIT | [`LICENSE`](LICENSE) | SPDX-compatible |

---

## 🛠 Tech Stack

[![Rasterio](https://img.shields.io/badge/Rasterio-1.3+-yellow.svg)](https://rasterio.readthedocs.io/)
[![rio-cogeo](https://img.shields.io/badge/rio--cogeo-5+-orange.svg)](https://cogeotiff.github.io/rio-cogeo/)
[![GDAL](https://img.shields.io/badge/GDAL-3.6+-informational.svg)](https://gdal.org/)
[![Shapely](https://img.shields.io/badge/Shapely-2.0+-blueviolet.svg)](https://shapely.readthedocs.io/)
[![PySTAC](https://img.shields.io/badge/PySTAC-1.10+-0A7BBB.svg)](https://pystac.readthedocs.io/)
[![MapLibre](https://img.shields.io/badge/MapLibre-GL--JS-1f6feb.svg)](https://maplibre.org/)

---

## 📑 Data Sources (tracked in `data/sources/`)

| Status | ID | Title | File | Notes |
|:-----:|----|-------|------|------|
| ![ks_dem_1m](https://img.shields.io/endpoint?url=https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/badges/ks_dem_1m.json) | `ks_dem_1m` | Kansas DEM (1 m) | [`ks_dem.json`](data/sources/ks_dem.json) | ArcGIS ImageServer |
| ![usgs_topo_1894_1950](https://img.shields.io/endpoint?url=https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/badges/usgs_topo_1894_1950.json) | `usgs_topo_1894_1950` | USGS Historical Topos (KS subset) | [`usgs_historic_topo.json`](data/sources/usgs_historic_topo.json) | HTMC GeoTIFFs |
| ![ks_treaties](https://img.shields.io/endpoint?url=https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/badges/ks_treaties.json) | `ks_treaties` | Kansas Treaties (vectors) | [`ks_treaties.json`](data/sources/ks_treaties.json) | Geoparsed treaties |
| ![ks_railroads](https://img.shields.io/endpoint?url=https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/badges/ks_railroads.json) | `ks_railroads` | Kansas Railroads | [`ks_railroads.json`](data/sources/ks_railroads.json) | Historical rail vectors |
| ![schema.source](https://img.shields.io/endpoint?url=https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/badges/schema.source.json) | `schema.source` | Schema for source descriptors | [`schema.source.json`](data/sources/schema.source.json) | JSON schema |

✔ = clean STAC validation · ⚠ = warnings · ❌ = failed/missing

---

A minimal **Google Earth + Web (GitHub Pages)** mapping system for Kansas elevation and historical layers.

* **Earth deliverables**: regionated **KML/KMZ** (progressive loading via NetworkLinks)  
* **Web app**: lightweight **MapLibre** viewer with a **time slider**  
* **Catalog**: **STAC 1.0.0** (Catalog → Collections → Items) for clean provenance  
* **Pipelines**: `Makefile` targets to **fetch → COG → derivatives (slope/aspect/hillshade) → site**  
* **CLI**: `kgt` (Kansas Geo Timeline) for STAC validation, listing, and web-config rendering  

> Start small (one county), then scale out. Keep STAC tight and versioned.

---

## 🌐 Live Demo

- **Web Viewer (MapLibre + Time Slider)** → [Demo Site](https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/)  
- **Google Earth KMZ (download)** → [Kansas_Terrain.kmz](https://bartytime4life.github.io/Kansas-Frontier-Matrix/earth/Kansas_Terrain.kmz)

---

## 📊 Pipeline Overview

```mermaid
flowchart TD
    A["Data Sources"] -->|fetch| B["COGs\nDEM + overlays"]
    B -->|terrain| C["Derivatives\nslope, aspect, hillshade"]
    C -->|stac| D["STAC Catalog and Items"]
    D -->|render-config| E["Web Viewer Config\nweb/app.config.json"]
    D -->|kml| F["KML / KMZ for Google Earth"]
    E -->|serve| G["MapLibre Web Viewer"]
    F --> H["Google Earth 3D"]
````

---

## 📖 Table of Contents

* [Quickstart](#quickstart)
* [Repository layout](#repository-layout)
* [Install](#install)
* [Make targets](#make-targets)
* [Data sources (examples)](#data-sources-examples)
* [STAC structure](#stac-structure)
* [CLI (kgt) usage](#cli-kgt-usage)
* [Web viewer (MapLibre + time)](#web-viewer-maplibre--time)
* [Google Earth (KML/KMZ)](#google-earth-kmlkmz)
* [Checks & reproducibility](#checks--reproducibility)
* [CI: GitHub Pages publish](#ci-github-pages-publish)
* [Troubleshooting](#troubleshooting)
* [Roadmap](#roadmap)
* [Requirements](#requirements)
* [Status snapshot](#status-snapshot)

---

## ⚡ Quickstart

```bash
# Python env (3.10+)
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# 1) Configure sources under data/sources/*.json
make fetch

# 2) Build DEM → COG → terrain
make cogs
make terrain

# 3) Generate and validate STAC
make stac
make stac-validate

# 4) Render viewer config + serve
kgt render-config --stac stac/items --output web/app.config.json --pretty
python -m http.server -d web 8080
```

---

## 📂 Repository Layout

```
data/                        # inputs/outputs (COGs, JSON metadata)
  sources/                   # source descriptors (endpoints, CRS, bounds, license)
  processed/                 # generated COGs/tiles and artifacts
stac/                        # STAC 1.0.0: catalog + collections + items
scripts/                     # small, dependency-light tools (Python/bash)
web/                         # static site (MapLibre) for GitHub Pages
earth/                       # KML/KMZ export and NetworkLinks
docker/                      # container env (reproducible build)
mcp/                         # SOPs/experiments/model cards (reproducibility)
```

---

## 📚 STAC Structure

* **Root catalog** → `stac/catalog.json`
* **Collections** → `stac/collections/*.json`
* **Items** → `stac/items/**/*.json`

Validate:

```bash
kgt validate-stac stac/items --report-json build/stac_report.json
```

---

## 🖥 Web Viewer (MapLibre + Time)

* Driven by `web/app.config.json`
* Serve locally or via GitHub Pages
* [Live Viewer](https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/)

---

## 🌍 Google Earth (KML/KMZ)

Exports under `earth/`:

```
earth/
  Kansas_Terrain.kmz
  networklinks/
    ks_1m_hillshade.kml
    usgs_topo_1894.kml
```

---

## ✅ Checks & Reproducibility

* Run `make stac-validate` before commits
* CI writes `web/badges/*.json` → live ✔/⚠/❌ badges
* Stamp `_meta.json` with provenance
* Add `checksum:sha256` to COG assets when possible

---

## 🗺 Roadmap

1. Expand topo statewide + treaty/rail vectors
2. Time slider v1 (year filter + opacity controls)
3. Google Earth polish (per-decade folders)
4. Auto `_meta.json` + STAC refresh
5. CI validation + Pages publish + badges
6. Story stubs (e.g., Santa Fe Trail)
7. Stretch goal: CesiumJS 3D terrain

---

## 📦 Requirements

* `rasterio`
* `rio-cogeo`
* `pyproj`
* `shapely`
* `pystac`
* `jsonschema` (optional)
* `jinja2` (optional)
* `Pillow`

---

## 📊 Status Snapshot

| Layer                       | STAC Item                                        | Asset Path                                       |
| --------------------------- | ------------------------------------------------ | ------------------------------------------------ |
| DEM (1 m, 2018–2020)        | `stac/items/ks_1m_dem_2018_2020.json`            | `data/cogs/dem/ks_1m_dem_2018_2020.tif`          |
| Hillshade (derived)         | same Item (`assets.hillshade`)                   | `data/cogs/hillshade/ks_hillshade_2018_2020.tif` |
| Historic Topo (Larned 1894) | `stac/items/overlays/usgs_topo_larned_1894.json` | `data/cogs/overlays/usgs_topo_larned_1894.tif`   |

---

**PRs welcome!** ✅ Stick to STAC 1.0.0, keep links relative, validate before commit.

```
