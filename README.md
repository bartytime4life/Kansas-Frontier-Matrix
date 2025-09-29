
<div align="center">

# 🌾 Kansas Geo Timeline  
### **Time · Terrain · History**

**An open-source, reproducible knowledge hub for Kansas’s layered history**  
Where **terrain, climate, culture, and events** intersect.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

</div>

---

<details>
<summary>📑 Table of Contents</summary>

- [🚀 Quick Links](#-quick-links)
- [🗺 Why It Matters](#-why-it-matters)
- [🔧 How It Works](#-how-it-works)
- [✨ Pipeline Highlights](#-pipeline-highlights)
- [⚡ Quickstart](#-quickstart)
- [📂 Repository Layout](#-repository-layout)
- [📊 Data Coverage Matrix](#-data-coverage-matrix)
- [🎯 Use Cases](#-use-cases)
- [✅ Reproducibility & CI](#-reproducibility--ci)
- [🛠 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📚 Citation](#-citation)
- [⚖️ License](#-license)
- [✨ Notes](#-notes)

</details>

---

## 🚀 Quick Links

- 🌐 **[Live Web Viewer](#)**
- 🌍 **[Google Earth KMZ](#)**
- 📊 **[STAC Catalog](stac/catalog.json)**

---

## 🗺 Why It Matters

> Kansas history is **fragmented** — scattered across treaties, disasters, geology, maps, and stories.  
> This project builds a **time-aware knowledge hub** so communities can explore how environment and culture shaped resilience.

Examples:
- 🚂 Railroads vs. tribal lands → how towns spread  
- 🌪 Dust Bowl storms → reshaping settlement  
- 🪶 Oral histories → tied to rivers, prairies, forts  
- 🔥 Fire regimes → ecological resilience  

👉 Not just maps — a **forensic storytelling engine** for Kansas.

---

## 🔧 How It Works

```mermaid
flowchart TD
  A["📥 Sources\ndata/sources/*.json"] -->|fetch| B["🗺️ COGs\ndata/cogs/**/*.tif"]
  B -->|derive| C["📐 Derivatives\nslope, aspect, hillshade, hydrology"]
  C -->|index| D["🗂️ STAC Catalog\nstac/catalog.json + items/"]
  D -->|graph| H["🧩 Knowledge Graph\nNeo4j + ontologies"]
  D -->|render| E["⚙️ Configs\nweb/config/*.json"]
  H --> E
  E --> F["🖥️ MapLibre Web Viewer"]
  D --> G["🌍 KML/KMZ\nGoogle Earth"]

  %% Styles
  classDef source  fill:#2b6cb0,stroke:#1a365d,color:#fff;
  classDef process fill:#38a169,stroke:#22543d,color:#fff;
  classDef catalog fill:#d69e2e,stroke:#744210,color:#fff;
  classDef graph   fill:#805ad5,stroke:#322659,color:#fff;
  classDef viewer  fill:#dd6b20,stroke:#7b341e,color:#fff;
  classDef earth   fill:#319795,stroke:#234e52,color:#fff;

  %% Assignments
  class A source;
  class B,C,E process;
  class D catalog;
  class H graph;
  class F viewer;
  class G earth;

⸻

✨ Pipeline Highlights
	•	📂 STAC 1.0.0 → provenance + temporal coverage
	•	🗺️ COGs → terrain & historical rasters
	•	🧩 Neo4j → people ↔ places ↔ events
	•	🖥️ MapLibre Viewer → timeline slider + dynamic layers
	•	🌍 Google Earth exports → immersive 3D exploration

⸻

⚡ Quickstart

<details>
<summary>🐍 Local Dev (Python)</summary>


python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Build core artifacts + site
make fetch cogs terrain stac stac-validate site

# Serve locally
python -m http.server -d web 8080

</details>


<details>
<summary>🐳 Docker</summary>


docker compose up -d site

</details>



⸻

📂 Repository Layout

<details>
<summary>Directory tree</summary>


data/
  sources/       # JSON descriptors (URLs, CRS, bounds, license, time)
  cogs/          # Cloud-Optimized GeoTIFFs
  derivatives/   # slope, aspect, hydrology, change maps
  processed/     # cleaned + normalized vectors/rasters
stac/            # STAC 1.0.0 catalog, collections, items
web/             # MapLibre viewer, configs, legends
earth/           # Google Earth exports (KML/KMZ)
scripts/         # ETL, STAC tools, validators
docker/          # reproducible containers
.github/         # CI/CD workflows, roadmap, pre-commit

</details>



⸻

📊 Data Coverage Matrix

Domain / Layer	Sources Integrated	Status
DEM / Terrain	USGS LiDAR 1m, KGS, 3DEP	✅ Complete
Hillshade / Derivatives	LiDAR COGs → slope, aspect	✅ Complete
Hydrology	USGS NHD, KS River floods	🚧 In Progress
Land Cover	NLCD 1992–2021	✅ Complete
Soils / PLSS / Parcels	NRCS SSURGO, KS GIS Hub	🚧 In Progress
Treaties & Tribal Lands	Boundary polygons	✅ Complete (expanding)
Railroads & Trails	1850–1920 rail GIS	🚧 In Progress
Topographic Maps	USGS Historic Topo, UT PCL	✅ Complete
Climate Normals	NOAA 1991–2020, Daymet	✅ Complete
Hazards — Tornado	NOAA SPC 1950–2024	✅ Complete
Hazards — Floods	FEMA, USGS flood data	🚧 In Progress
Hazards — Wildfire	NIFC + KS perimeter sets	🚧 In Progress
Paleoclimate / Fire	NOAA cores, charcoal	🚧 In Progress
Oral Histories & Arch.	Tribal narratives, archaeology	🚧 In Progress
Geology / Core Samples	KGS drill cores	🚧 In Progress


⸻

🎯 Use Cases
	•	🚂 Animate railroad expansion (1850–1910) with treaties
	•	🌪 Overlay Dust Bowl land-cover with drought indices
	•	🪶 Link oral histories to forts, rivers, & counties
	•	🌊 Compare pre-dam vs. post-dam Kansas River floods
	•	🔥 Integrate fire regimes + archaeology into resilience narratives

⸻

✅ Reproducibility & CI

Every dataset, config, and artifact is versioned, validated, and reproducible.
	•	🔐 .sha256 checksums for every artifact
	•	📏 STAC + JSON Schema validation in CI
	•	🛠 Pipelines:
	•	site.yml → build & deploy
	•	stac-badges.yml → dataset health shields
	•	codeql.yml + trivy.yml → security & provenance checks

make prebuild


⸻

🛠 Roadmap
	•	📌 M1: Expand sources (treaties, railroads, hazards)
	•	📌 M2: Terrain & hydrology modeling (flowdir, floodplains)
	•	📌 M3: Storytelling layers (oral histories, archaeology)
	•	📌 M4: UI enhancements (story maps, vector tiles)
	•	📌 M5: Predictive modeling & NASA-grade simulations

👉 See ROADMAP.md

⸻

🤝 Contributing
	•	✔️ Keep STAC valid + configs schema-checked
	•	✔️ Use MCP templates (experiment.md, sop.md, model_card.md)
	•	✔️ Follow CI hooks + submit PRs with clear commits

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

✨ Notes
	•	🛡 CI badges wired to workflows
	•	🗂 Coverage matrix embedded
	•	📜 Anchored in MCP reproducibility standards
	•	🔗 Connects maps, archives, disasters, & oral histories into one forensic timeline

---
