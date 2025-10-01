<div align="center">

# 🌾 Kansas Geo Timeline  
### **Time · Terrain · History**

**An interactive, reproducible knowledge hub for Kansas’s layered history**  
Where **terrain, climate, culture, and events** intersect across centuries.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

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

✨ **What you get:**
- 📂 **STAC Catalogs** → provenance & temporal coverage  
- 🗺️ **COGs** → terrain + historic rasters  
- 🧩 **Knowledge Graphs** → connect people, places, events  
- 🖥️ **MapLibre Viewer** → timeline slider + dynamic layers  
- 🌍 **Google Earth KMZ/KML** → immersive 3D exploration  

---

## 🌐 Live Demos & Previews

- 🖥️ **Web Viewer (MapLibre)** → [View Interactive Atlas](https://bartytime4life.github.io/Kansas-Frontier-Matrix/web/)  
- 🌍 **Google Earth (KMZ)** → [Download KMZ](https://github.com/bartytime4life/Kansas-Frontier-Matrix/releases/latest)  
- 📊 **STAC Catalog** → [Browse STAC JSON](https://bartytime4life.github.io/Kansas-Frontier-Matrix/stac/)  

> ⚠️ These links are placeholders — update with your actual **GitHub Pages** or **deployment URLs** once the CI/CD site build is live.

---

## 🏗 Architecture

```mermaid
flowchart TD
  A[Sources<br/>scans · rasters · vectors · tables] --> B[ETL Pipeline<br/>scripts · make · checksums]
  B --> C[COGs and Processed Data<br/>raster cogs · geojson]
  C --> D[STAC Catalog<br/>collections · items · assets]
  D --> E[Config Build<br/>app.config.json · layers.json]
  E --> F[Web Viewer (MapLibre)<br/>timeline · legend · popups]
  E --> G[Google Earth Exports<br/>KML · KMZ]
  D --> H[Knowledge Graph (optional)<br/>people · places · events]
  H --> F


⸻

⚡ Quickstart

🐍 Local Development

python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Build core pipeline
make fetch cogs terrain stac stac-validate site

# Serve locally
python -m http.server -d web 8080

🐳 Docker

docker compose up -d site

🔁 Workflow Diagram

flowchart LR
  A[Serve Site<br/>python http.server] --> B[Validate Configs<br/>make stac-validate]
  B --> C[Add Layer<br/>edit layers.json]
  C --> D[Preview in Browser<br/>localhost:8080]


⸻

📂 Repository Layout

data/        # sources, cogs, processed vectors/rasters
stac/        # STAC 1.0.0 catalog, collections, items
web/         # MapLibre viewer, configs, legends
earth/       # Google Earth exports (KML/KMZ)
scripts/     # ETL, STAC tools, validators
docker/      # reproducible containers
.github/     # CI/CD workflows, roadmap, pre-commit


⸻

📊 Coverage Status (Root Catalog)

<!-- ROOT_COVERAGE_START -->


Layer / Domain	Data Sources	Status
🏔 DEM & Terrain	USGS LiDAR, KGS, 3DEP	
🗺 Hillshade/Derivatives	LiDAR COGs → slope, aspect	
🌊 Hydrology	NHD, Kansas River floods	
🌱 Land Cover	NLCD 1992–2021	
🧭 Soils / PLSS / Parcels	NRCS SSURGO, KS GIS Hub	
🪶 Treaties & Lands	Boundary polygons	
🚂 Railroads & Trails	1850–1920 GIS	
🗺 Historic Topos	USGS, UT PCL	
🌡 Climate Normals	NOAA 1991–2020, Daymet	
🌪 Hazards — Tornado	NOAA SPC 1950–2024	
🌊 Hazards — Floods	FEMA, USGS	
🔥 Hazards — Wildfire	NIFC, KS perimeter sets	
🪨 Paleoclimate / Fire	NOAA cores, charcoal	
🪶 Oral Histories & Arch.	Tribal narratives, archaeology	
⛏ Geology / Core Samples	KGS drill cores	

<!-- ROOT_COVERAGE_END -->


Legend:

 Complete ·

 In Progress ·

 Planned

⸻

🎯 Roadmap

Milestone	Goal	Status
📌 M1	Expand sources (treaties, railroads, hazards)	
📌 M2	Terrain & hydrology modeling (flowdir, floodplains)	
📌 M3	Storytelling layers (oral histories, archaeology)	
📌 M4	UI enhancements (story maps, vector tiles)	
📌 M5	Predictive modeling & NASA-grade simulations	

👉 See ROADMAP.md for full details.

📅 Gantt Timeline

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

  %% style mappings
  classDef done fill:#2ecc71,stroke:#2ecc71,stroke-width:2px,color:#fff
  classDef active fill:#f1c40f,stroke:#f1c40f,stroke-width:2px,color:#000
  classDef planned fill:#bdc3c7,stroke:#7f8c8d,stroke-width:1px,color:#000

  class m1 done
  class m2 active
  class m3,m4,m5 planned


⸻

✅ Reproducibility & CI

Every dataset, config, and artifact is versioned, validated, and reproducible:
	•	🔐 .sha256 checksums → all artifacts
	•	📏 STAC + JSON Schema validation → enforced in CI
	•	🛠 Pipelines →
	•	site.yml → build & deploy
	•	stac-badges.yml → dataset health shields
	•	codeql.yml + trivy.yml → security & provenance checks

⸻

🤝 Contributing
	•	✔️ Validate with STAC + JSON Schemas
	•	✔️ Follow MCP templates (experiment.md, sop.md, model_card.md)
	•	✔️ Submit PRs with clear commits & passing CI

⸻

📚 Citation

@software{kansas_geo_timeline_2025,
  title  = {Kansas Geo Timeline — Frontier Matrix},
  author = {Barta, Andy and contributors},
  year   = {2025},
  url    = {https://github.com/bartytime4life/Kansas-Frontier-Matrix}
}


⸻

⚖️ License

MIT © 2025 — Kansas Frontier Matrix

⸻


---

✅ Now your README has:  
- **Live links** for the viewer, KMZ, and STAC previews.  
- Consistent **Mermaid diagrams** (Architecture + Quickstart Workflow + Roadmap Gantt).  
- Coverage + Roadmap with badges for at-a-glance progress.  
