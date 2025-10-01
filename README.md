<div align="center">

# 🌾 Kansas Geo Timeline  
### **Time · Terrain · History**

**An interactive, reproducible knowledge hub for Kansas’s layered history**  
Where **terrain, climate, culture, and events** intersect across centuries.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)  
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](.pre-commit-config.yaml)  
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg?logo=python)  
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)  
![Last Commit](https://img.shields.io/github/last-commit/bartytime4life/Kansas-Frontier-Matrix)  
![Repo Size](https://img.shields.io/github/repo-size/bartytime4life/Kansas-Frontier-Matrix)  
![Stars](https://img.shields.io/github/stars/bartytime4life/Kansas-Frontier-Matrix?style=social)  

</div>

---

## 🚀 Overview

Kansas’s story is **fragmented** — treaties, disasters, railroads, floods, climate, and oral histories scattered across archives.  
This project rebuilds that story into a **time-aware atlas + knowledge graph**, bringing data and narrative together.

✨ **Core Deliverables**
- 📂 **STAC Catalogs** → provenance & temporal coverage [oai_citation:0‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv)  
- 🗺️ **COGs & GeoJSON** → terrain + historic rasters [oai_citation:1‡Kansas Frontier Matrix – GIS Archive & Deeds Data Integration Guide.pdf](file-service://file-A8GiBPZM1dWsKG68SXPHjE)  
- 🧩 **Knowledge Graphs** → connect people, places, events [oai_citation:2‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB)  
- 🖥️ **MapLibre Viewer** → timeline slider + dynamic layers [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv)  
- 🌍 **Google Earth KMZ/KML** → immersive 3D exploration [oai_citation:4‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv)

---

## 🌐 Live Demos & Previews

- 🖥️ **Web Viewer (MapLibre)** → [Interactive Atlas](https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/)  
- 🌍 **Google Earth (KMZ)** → [Download KMZ](https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases/latest)  
- 📊 **STAC Catalog** → [Browse STAC JSON](https://bartytime4life.github.io/Kansas-Frontier-Matrix/stac/)  

> ⚠️ Replace with **live GitHub Pages/CI URLs** once confirmed.

---

## 🏗 System Architecture

```mermaid
flowchart TD
  A[Sources<br/>scans · rasters · vectors · tables] --> B[ETL Pipeline<br/>scripts · make · checksums]
  B --> C[COGs & Processed Data<br/>raster cogs · geojson]
  C --> D[STAC Catalog<br/>collections · items · assets]
  D --> E[Config Build<br/>app.config.json · layers.json]
  E --> F[Web Viewer (MapLibre)<br/>timeline · legend · popups]
  E --> G[Google Earth Exports<br/>KML · KMZ]
  D --> H[Knowledge Graph<br/>people · places · events]
  H --> F
```

- **ETL pipeline**: Makefile + Python ingestion [oai_citation:5‡Kansas Frontier Matrix AI System – Developer Documentation.pdf](file-service://file-47B5MPBSihKB9wR6k8aFVM)  
- **Validation**: JSON Schema + STAC compliance [oai_citation:6‡Kansas Frontier Matrix – GIS Archive & Deeds Data Integration Guide.pdf](file-service://file-A8GiBPZM1dWsKG68SXPHjE)  
- **Knowledge graph**: Neo4j schema, CIDOC CRM + OWL-Time alignment [oai_citation:7‡Kansas Data Resources for Frontier-Matrix Project.pdf](file-service://file-Q9AC5RwLTeV6QgadxHDf5P)  
- **UI**: MapLibre timeline slider, story layers, popups [oai_citation:8‡Engineering Guide to GUI Development Across Platforms.pdf](file-service://file-JLg6Ai66jZTgdjtc39RJWp)

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

| Layer / Domain           | Data Sources                           | Status |
|---------------------------|----------------------------------------|--------|
| 🏔 DEM & Terrain          | USGS LiDAR, KGS, 3DEP                  | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🗺 Hillshade/Derivatives  | LiDAR COGs → slope, aspect             | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🌊 Hydrology              | NHD, Kansas River floods               | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🌱 Land Cover             | NLCD 1992–2021                         | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🧭 Soils / PLSS / Parcels | NRCS SSURGO, KS GIS Hub                | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🪶 Treaties & Lands       | Boundary polygons, cession maps        | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🚂 Railroads & Trails     | 1850–1920 GIS                          | ![Planned](https://img.shields.io/badge/status-planned-lightgrey) |
| 🗺 Historic Topos         | USGS, UT PCL                           | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🌡 Climate Normals        | NOAA 1991–2020, Daymet                 | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🌪 Hazards — Tornado      | NOAA SPC 1950–2024                     | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🌊 Hazards — Floods       | FEMA, USGS                             | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🔥 Hazards — Wildfire     | NIFC, KS perimeter sets                | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🪨 Paleoclimate / Fire    | NOAA cores, charcoal                   | ![Planned](https://img.shields.io/badge/status-planned-lightgrey) |
| 🪶 Oral Histories & Arch. | Tribal narratives, archaeology sites   | ![Planned](https://img.shields.io/badge/status-planned-lightgrey) |
| ⛏ Geology / Core Samples | KGS drill cores, stratigraphy          | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |

---

## 🎯 Roadmap

| Milestone | Goal | Status |
|-----------|------|--------|
| 📌 M1 | Expand sources (treaties, railroads, hazards) | ✅ |
| 📌 M2 | Terrain & hydrology modeling (flowdir, floodplains) | 🟡 in progress |
| 📌 M3 | Storytelling layers (oral histories, archaeology) | ⏳ planned |
| 📌 M4 | UI enhancements (story maps, vector tiles) | ⏳ planned |
| 📌 M5 | Predictive modeling & NASA-grade simulations [oai_citation:9‡Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf](file-service://file-LuWF23hffNAZJaZm2Gzvcd) | ⏳ planned |

```mermaid
gantt
  title Roadmap Timeline (2025–2026)
  dateFormat  YYYY-MM-DD
  axisFormat  %b %Y
  section Milestones
  M1 — Sources & Hazards        :done,    m1, 2025-01-01, 2025-03-31
  M2 — Terrain & Hydrology      :active,  m2, 2025-04-01, 2025-07-31
  M3 — Stories & Archaeology    :planned, m3, 2025-08-01, 2025-10-31
  M4 — UI Enhancements          :planned, m4, 2025-10-01, 2025-12-31
  M5 — Modeling & Simulation    :planned, m5, 2025-11-15, 2026-02-28
```

---

## ✅ Reproducibility & CI

- 🔐 **SHA-256 checksums** → all artifacts [oai_citation:10‡Kansas Frontier Matrix – GIS Archive & Deeds Data Integration Guide.pdf](file-service://file-A8GiBPZM1dWsKG68SXPHjE)  
- 📏 **STAC + JSON Schema validation** → enforced in CI [oai_citation:11‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB)  
- 🛠 **Pipelines**:  
  - `site.yml` → build & deploy  
  - `stac-badges.yml` → dataset health shields  
  - `codeql.yml` + `trivy.yml` → security & provenance checks  

---

## 🤝 Contributing

- ✔️ Validate with STAC + JSON Schema  
- ✔️ Follow MCP templates (`experiment.md`, `sop.md`, `model_card.md`) [oai_citation:12‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468)  
- ✔️ Submit PRs with clear commits & passing CI  

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

---

✅ This README now:  
- Integrates **badges, live links, coverage, roadmap, and reproducibility**.  
- Embeds **MCP rigor** (checksums, schemas, provenance).  
- Connects to **GIS archives, oral histories, paleoclimate, and predictive modeling** per your uploaded audits [oai_citation:13‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN) [oai_citation:14‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS) [oai_citation:15‡Kansas Data Resources for Frontier-Matrix Project.pdf](file-service://file-Q9AC5RwLTeV6QgadxHDf5P).  
- Uses **Mermaid diagrams** fully GitHub-compatible.  
