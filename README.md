<div align="center">

# 🌾 Kansas Geo Timeline

### **Time · Terrain · History**

**An interactive, reproducible knowledge hub for Kansas’s layered history**  
Where **terrain, climate, culture, and events** intersect across centuries.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)  
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](.pre-commit-config.yaml)  
[![Coverage](https://img.shields.io/badge/coverage-stac%20catalog-blueviolet)](stac/)  
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg?logo=python)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  
![Last Commit](https://img.shields.io/github/last-commit/bartytime4life/Kansas-Frontier-Matrix)  
![Repo Size](https://img.shields.io/github/repo-size/bartytime4life/Kansas-Frontier-Matrix)  
![Stars](https://img.shields.io/github/stars/bartytime4life/Kansas-Frontier-Matrix?style=social)

</div>

---

## 🚀 Overview

Kansas’s history is **fragmented** — treaties, disasters, railroads, floods, climate, and oral histories are scattered across archives.  
This project rebuilds that story into a **time-aware atlas + knowledge graph**, linking data and narrative.

✨ **Core Deliverables**

* 📂 **STAC Catalogs** → provenance & temporal coverage  
* 🗺️ **COGs & GeoJSON** → terrain + historic rasters  
* 🧩 **Knowledge Graphs** → people ↔ places ↔ events  
* 🖥️ **MapLibre Viewer** → timeline slider + dynamic layers  
* 🌍 **Google Earth KMZ/KML** → immersive 3D exploration  

---

## 🌐 Live Demos & Previews

* 🖥️ **Web Viewer (MapLibre)** → [Interactive Atlas](https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/)  
* 🌍 **Google Earth (KMZ)** → [Download KMZ](https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases/latest)  
* 📊 **STAC Catalog** → [Browse STAC JSON](https://bartytime4life.github.io/Kansas-Frontier-Matrix/stac/)  

---

## 🏗 System Architecture

```mermaid
flowchart TD
  A["Sources\nscans · rasters · vectors · documents"] --> B["ETL Pipeline\nMakefile · Python · checksums"]
  B --> C["COGs & Processed Layers\nraster COGs · GeoJSON"]
  C --> D["STAC Catalog\ncollections · items · assets"]
  D --> E["Config Build\napp.config.json · layers.json"]
  E --> F["Web Viewer (MapLibre)\ntimeline · legend · popups"]
  E --> G["Google Earth Exports\nKML · KMZ"]
  D --> H["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
  H --> F
````

<!-- END OF MERMAID -->

* **ETL pipeline**: Makefile + Python ingestion
* **Validation**: JSON Schema + STAC compliance
* **Knowledge graph**: Neo4j, CIDOC CRM + OWL-Time
* **UI**: MapLibre timeline, legends, popups

---

## ⚡ Quickstart

### 🐍 Local Development

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Build data + site
make fetch cogs terrain stac stac-validate site

# Serve locally
python -m http.server -d web 8080
```

### 🐳 Docker

```bash
docker compose up -d site
```

---

## 📂 Repository Layout

```
data/        # sources, cogs, processed vectors/rasters
stac/        # STAC 1.0.0 catalog, collections, items
web/         # MapLibre viewer, configs, legends
earth/       # Google Earth exports (KML/KMZ)
scripts/     # ETL, STAC tools, validators
docker/      # reproducible containers
.github/     # CI/CD workflows, roadmap, pre-commit
```

---

## 📊 Coverage Status (Root Catalog)

| Domain / Layer            | Sources                         | Status                                                                  |
| ------------------------- | ------------------------------- | ----------------------------------------------------------------------- |
| 🏔 DEM & Terrain          | USGS LiDAR, KGS, 3DEP           | ![Complete](https://img.shields.io/badge/status-complete-brightgreen)   |
| 🗺 Hillshade/Derivatives  | LiDAR COGs → slope, aspect      | ![Complete](https://img.shields.io/badge/status-complete-brightgreen)   |
| 🌊 Hydrology              | NHD, Kansas River floods        | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🌱 Land Cover             | NLCD 1992–2021                  | ![Complete](https://img.shields.io/badge/status-complete-brightgreen)   |
| 🧭 Soils / PLSS / Parcels | NRCS SSURGO, KS GIS Hub         | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🪶 Treaties & Lands       | Boundary polygons, cession maps | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🚂 Railroads & Trails     | 1850–1920 GIS                   | ![Planned](https://img.shields.io/badge/status-planned-lightgrey)       |
| 🗺 Historic Topos         | USGS, UT PCL                    | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🌡 Climate Normals        | NOAA 1991–2020, Daymet          | ![Complete](https://img.shields.io/badge/status-complete-brightgreen)   |
| 🌪 Hazards — Tornado      | NOAA SPC 1950–2024              | ![Complete](https://img.shields.io/badge/status-complete-brightgreen)   |
| 🌊 Hazards — Floods       | FEMA, USGS                      | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🔥 Hazards — Wildfire     | NIFC, KS Forest Service         | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🪨 Paleoclimate / Fire    | NOAA cores, charcoal            | ![Planned](https://img.shields.io/badge/status-planned-lightgrey)       |
| 🪶 Oral Histories & Arch. | Tribal narratives, archaeology  | ![Planned](https://img.shields.io/badge/status-planned-lightgrey)       |
| ⛏ Geology / Core Samples  | KGS drill cores, stratigraphy   | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |

---

## 🎯 Roadmap

| Milestone | Goal                                                 | Status         |
| --------- | ---------------------------------------------------- | -------------- |
| 📌 M1     | Expand sources (treaties, hazards, topographic maps) | ✅              |
| 📌 M2     | Terrain & hydrology modeling (flowdir, floodplains)  | 🟡 in progress |
| 📌 M3     | Storytelling layers (oral histories, archaeology)    | ⏳ planned      |
| 📌 M4     | UI enhancements (story maps, vector tiles)           | ⏳ planned      |
| 📌 M5     | Predictive modeling & NASA-grade simulations         | ⏳ planned      |

```mermaid
gantt
  title "Roadmap Timeline (2025–2026)"
  dateFormat  YYYY-MM-DD
  axisFormat  %b %Y

  section Milestones
  M1 — Sources & Hazards        :done,    m1, 2025-01-01, 2025-03-31
  M2 — Terrain & Hydrology      :active,  m2, 2025-04-01, 2025-07-31
  M3 — Stories & Archaeology    :crit,    m3, 2025-08-01, 2025-10-31
  M4 — UI Enhancements          :         m4, 2025-10-01, 2025-12-31
  M5 — Modeling & Simulation    :         m5, 2025-11-15, 2026-02-28
```

<!-- END OF MERMAID -->

---

## ✅ Reproducibility & CI

* 🔐 **SHA-256 checksums** for all artifacts
* 📏 **STAC + JSON Schema validation** in CI
* 🛠 **Pipelines**:

  * `site.yml` → build & deploy
  * `stac-validate.yml` → dataset health shields
  * `codeql.yml` + `trivy.yml` → security checks

---

## 🤝 Contributing

* ✔️ Validate with STAC + JSON Schema
* ✔️ Follow MCP templates (`experiment.md`, `sop.md`, `model_card.md`)
* ✔️ Submit PRs with clear commits & passing CI

---

## 📚 Citation

```bibtex
@software{kansas_geo_timeline_2025,
  title  = {Kansas Geo Timeline — Frontier Matrix},
  author = {Barta, Andy and contributors},
  year   = {2025},
  url    = {https://github.com/bartytime4life/Kansas-Frontier-Matrix}
}
```

---

## ⚖️ License

MIT © 2025 — Kansas Frontier Matrix
