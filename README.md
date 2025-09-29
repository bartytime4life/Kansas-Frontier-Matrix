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

## 🗺 Why It Matters

> *“History is layered. To understand Kansas, you need maps, voices, disasters, and memory — all at once.”*

- 🚂 **Railroads & treaties** → how settlement spread  
- 🌪 **Dust Bowl & droughts** → reshaping the plains  
- 🪶 **Oral histories & archaeology** → landscapes of memory  
- 🔥 **Fire regimes & paleoclimate** → resilience over centuries  
- 🌊 **Floods & dams** → shifting rivers and towns  

👉 This is not just a map — it’s a **forensic storytelling engine**.

---

## ⚡ Quickstart

### 🐍 Local Development

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Build core pipeline
make fetch cogs terrain stac stac-validate site

# Serve locally
python -m http.server -d web 8080

🐳 Docker

docker compose up -d site


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

## 📊 Coverage Status (Root Catalog)

<!-- ROOT_COVERAGE_START -->

| Layer / Domain           | Data Sources                     | Status |
|---------------------------|----------------------------------|--------|
| 🏔 DEM & Terrain          | USGS LiDAR, KGS, 3DEP            | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🗺 Hillshade/Derivatives  | LiDAR COGs → slope, aspect       | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🌊 Hydrology              | NHD, Kansas River floods         | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🌱 Land Cover             | NLCD 1992–2021                   | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🧭 Soils / PLSS / Parcels | NRCS SSURGO, KS GIS Hub          | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🪶 Treaties & Lands       | Boundary polygons                | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🚂 Railroads & Trails     | 1850–1920 GIS                    | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🗺 Historic Topos         | USGS, UT PCL                     | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🌡 Climate Normals        | NOAA 1991–2020, Daymet           | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🌪 Hazards — Tornado      | NOAA SPC 1950–2024               | ![Complete](https://img.shields.io/badge/status-complete-brightgreen) |
| 🌊 Hazards — Floods       | FEMA, USGS                       | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🔥 Hazards — Wildfire     | NIFC, KS perimeter sets          | ![In Progress](https://img.shields.io/badge/status-in--progress-yellow) |
| 🪨 Paleoclimate / Fire    | NOAA cores, charcoal             | ![Planned](https://img.shields.io/badge/status-planned-lightgrey) |
| 🪶 Oral Histories & Arch. | Tribal narratives, archaeology   | ![Planned](https://img.shields.io/badge/status-planned-lightgrey) |
| ⛏ Geology / Core Samples  | KGS drill cores                  | ![Planned](https://img.shields.io/badge/status-planned-lightgrey) |

<!-- ROOT_COVERAGE_END -->

**Legend:**  
![Complete](https://img.shields.io/badge/status-complete-brightgreen) Complete ·  
![In Progress](https://img.shields.io/badge/status-in--progress-yellow) In Progress ·  
![Planned](https://img.shields.io/badge/status-planned-lightgrey) Planned

⸻

🎯 Roadmap
	•	📌 M1 — Expand sources (treaties, railroads, hazards)
	•	📌 M2 — Terrain & hydrology modeling (flowdir, floodplains)
	•	📌 M3 — Storytelling layers (oral histories, archaeology)
	•	📌 M4 — UI enhancements (story maps, vector tiles)
	•	📌 M5 — Predictive modeling & NASA-grade simulations

👉 See ROADMAP.md

⸻

✅ Reproducibility & CI

Every dataset, config, and artifact is versioned, validated, and reproducible.
	•	🔐 .sha256 checksums → all artifacts
	•	📏 STAC + JSON Schema validation → enforced in CI
	•	🛠 Pipelines →
	•	site.yml — build & deploy
	•	stac-badges.yml — dataset health shields
	•	codeql.yml + trivy.yml — security & provenance checks

⸻

🤝 Contributing
	•	✔️ Validate with STAC + JSON Schemas
	•	✔️ Follow MCP templates (experiment.md, sop.md, model_card.md)
	•	✔️ PRs → clear commits, passing CI

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

---
