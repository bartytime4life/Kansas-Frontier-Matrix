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
> 💡 Kansas history is **fragmented** — scattered across treaties, disasters, geology, maps, and stories.  
> This project builds a **time-aware knowledge hub** so communities can explore how environment and culture shaped resilience.

**Exploration examples**
- 🚂 Railroads vs. tribal lands → how towns spread  
- 🌪 Dust Bowl storms → reshaping settlement  
- 🪶 Oral histories → tied to rivers, prairies, forts  
- 🔥 Fire regimes → ecological resilience  

👉 Not just maps — a **forensic storytelling engine** for Kansas.

---

## 🔧 How It Works

```mermaid
flowchart TD
  A["📥 Sources<br/>(data/sources/*.json)"] -->|fetch| B["🗺️ COGs<br/>(data/cogs/**/*.tif)"]
  B -->|derive| C["📐 Derivatives<br/>(slope, aspect, hillshade, hydrology)"]
  C -->|index| D["🗂️ STAC Catalog<br/>(stac/catalog.json, items/)"]
  D -->|graph| H["🧩 Knowledge Graph<br/>(Neo4j + Ontologies)"]
  D -->|render| E["⚙️ Configs<br/>(web/config/*.json)"]
  H --> E
  E --> F["🖥️ MapLibre Web Viewer"]
  D --> G["🌍 KML/KMZ (Google Earth)"]

  %% Styles (GitHub Mermaid supports: fill, stroke, color)
  classDef source  fill:#2b6cb0,stroke:#1a365d,color:#ffffff;
  classDef process fill:#38a169,stroke:#22543d,color:#ffffff;
  classDef catalog fill:#d69e2e,stroke:#744210,color:#ffffff;
  classDef graph   fill:#805ad5,stroke:#322659,color:#ffffff;
  classDef viewer  fill:#dd6b20,stroke:#7b341e,color:#ffffff;
  classDef earth   fill:#319795,stroke:#234e52,color:#ffffff;

  %% Apply classes
  class A source;
  class B,C,E process;
  class D catalog;
  class H graph;
  class F viewer;
  class G earth;

<!-- END OF MERMAID -->



⸻

✨ Pipeline Highlights
	•	📂 STAC 1.0.0 catalog → provenance + temporal coverage
	•	🗺️ COGs → terrain & historical rasters
	•	🧩 Neo4j Knowledge Graph → people ↔ places ↔ events
	•	🖥️ MapLibre Viewer → timeline slider + dynamic layers
	•	🌍 Google Earth exports → immersive 3D exploration

⸻

⚡ Quickstart

<details>
<summary>🐍 Local Dev (Python)</summary>


python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

make fetch cogs terrain stac stac-validate site
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

🌐 Domain / Layer	🔗 Sources Integrated	📌 Status
DEM / Terrain	USGS LiDAR 1m, KGS, 3DEP	✅
Hillshade / Derivatives	LiDAR COGs → slope, aspect	✅
Hydrology	USGS NHD, KS River floods	🚧
Land Cover	NLCD 1992–2021	✅
Soils / PLSS / Parcels	NRCS SSURGO, KS GIS Hub	🚧
Treaties & Tribal Lands	Boundary polygons	✅ / Expand
Railroads & Trails	1850–1920 rail GIS	🚧
Topographic Maps	USGS Historic Topo, UT PCL	✅
Climate Normals	NOAA 1991–2020, Daymet	✅
Hazards — Tornado	NOAA SPC 1950–2024	✅
Hazards — Floods	FEMA, USGS flood data	🚧
Hazards — Wildfire	NIFC + KS perimeter sets	🚧
Paleoclimate / Fire	NOAA cores, charcoal	🚧
Oral Histories & Arch.	Tribal narratives, sites	🚧
Geology / Core Samples	KGS drill cores	🚧


⸻

🎯 Use Cases
	•	🚂 Animate railroad expansion (1850–1910) alongside treaties
	•	🌪 Overlay Dust Bowl land-cover change with NOAA drought indices
	•	🪶 Link oral histories to forts, rivers, & counties
	•	🌊 Compare pre-dam vs. post-dam Kansas River floods
	•	🔥 Integrate fire regimes + archaeology into resilience narratives

⸻

✅ Reproducibility & CI

🧪 Following MCP principles: every dataset, config, and artifact is versioned, validated, and reproducible.

	•	🔐 Checksums → .sha256 sidecars for every artifact
	•	📏 Validation → STAC + JSON Schema in CI
	•	🛠 Pipelines
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
	•	🛡 Dynamic badges wired to CI
	•	🗂 Coverage matrix embedded
	•	📜 Anchored in MCP reproducibility standards
	•	🔗 Connects maps, archives, disasters, & oral histories into one forensic timeline
