🌾 Kansas Geo Timeline — Time · Terrain · History

Mission: Build an open-source, reproducible system to uncover Kansas’s layered history — where terrain, climate, culture, and events intersect.
The Frontier-Matrix integrates maps, LiDAR terrain, treaties, railroads, disasters, archaeology, and oral histories into an interactive atlas + knowledge graph, with both a MapLibre viewer and Google Earth (KMZ/KML).


⸻

🚀 Quick Links
	•	🌐 Live Web Viewer
	•	🌍 Google Earth KMZ
	•	📊 STAC Catalog

⸻

🗺 Why It Matters

Kansas history is fragmented — scattered across treaties, disasters, geology, maps, and stories.
This project builds a time-aware knowledge hub so communities can explore:
	•	🚂 Railroads vs. tribal lands — how towns spread along rights-of-way.
	•	🌪 Droughts, floods, and Dust Bowl storms reshaping settlement.
	•	🪶 Archaeology & oral histories tied to rivers, prairies, and forts.
	•	🔥 Paleoclimate & fire regimes shaping resilience and ecology.

👉 It’s more than maps — it’s a forensic storytelling engine for Kansas.

⸻

🔧 How It Works

flowchart TD
  A["📥 Sources\n(data/sources/*.json)"] -->|fetch| B["🗺️ COGs\n(data/cogs/**/*.tif)"]
  B -->|derive| C["📐 Derivatives\n(slope, aspect, hillshade, hydrology)"]
  C -->|index| D["🗂️ STAC Catalog\n(stac/catalog.json, items/)"]
  D -->|graph| H["🧩 Knowledge Graph\n(Neo4j + Ontologies)"]
  D -->|render| E["⚙️ Configs\n(web/config/*.json)"]
  H --> E
  E --> F["🖥️ MapLibre Web Viewer"]
  D --> G["🌍 KML/KMZ (Google Earth)"]

<!-- END OF MERMAID -->


✨ Pipeline Highlights
	•	📂 STAC 1.0.0 catalog → provenance + temporal coverage ￼
	•	🗺️ COGs → terrain & historical rasters ￼
	•	🧩 Neo4j Knowledge Graph → people ↔ places ↔ events ￼
	•	🖥️ MapLibre Viewer → timeline slider + dynamic layers
	•	🌍 Google Earth exports → immersive 3D exploration

⸻

⚡ Quickstart

🐍 Python (local dev)

python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

make fetch cogs terrain stac stac-validate site
python -m http.server -d web 8080

🐳 Docker

docker compose up -d site


⸻

📂 Repository Layout

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


⸻

📊 Data Coverage Matrix

🌐 Domain / Layer	🔗 Sources Integrated	📌 Status
DEM / Terrain	USGS LiDAR 1 m, KGS, 3DEP	✅
Hillshade / Derivatives	LiDAR COGs → slope, aspect, hydrology	✅
Hydrology	USGS NHD, KS River floods ￼	🚧
Land Cover	NLCD 1992–2021 ￼	✅
Soils / PLSS / Parcels	NRCS SSURGO, KS GIS Hub ￼	🚧
Treaties & Tribal Lands	Boundary polygons ￼	✅ / Expand
Railroads & Trails	1850–1920 rail GIS ￼	🚧
Topographic Maps	USGS Historic Topo, UT PCL ￼	✅
Climate Normals	NOAA 1991–2020, Daymet ￼	✅
Hazards — Tornado	NOAA SPC 1950–2024 ￼	✅
Hazards — Floods	FEMA, USGS flood data ￼	🚧
Hazards — Wildfire	NIFC + KS perimeter sets ￼	🚧
Paleoclimate / Fire	NOAA cores, charcoal ￼	🚧
Oral Histories & Archaeology	Tribal narratives, sites ￼	🚧
Geology / Core Samples	KGS drill cores ￼	🚧


⸻

🎯 Use Cases
	•	🚂 Animate railroad expansion (1850–1910) alongside treaties.
	•	🌪 Overlay Dust Bowl land-cover change with NOAA drought indices.
	•	🪶 Link oral histories to forts, rivers, & counties.
	•	🌊 Compare pre-dam vs post-dam Kansas River floods.
	•	🔥 Integrate fire regimes + archaeology into resilience narratives.

⸻

✅ Reproducibility & CI
	•	🔐 Checksums: .sha256 sidecars for every artifact ￼
	•	📏 Validation: STAC + JSON Schema in CI ￼
	•	🛠️ Pipelines:
	•	site.yml → build & deploy
	•	stac-badges.yml → dataset health shields
	•	codeql.yml + trivy.yml → security & provenance checks

Run:

make prebuild


⸻

🛠 Roadmap
	•	📌 M1: Expand sources (treaties, railroads, hazards)
	•	📌 M2: Terrain & hydrology modeling (flowdir, floodplains)
	•	📌 M3: Storytelling layers (oral histories, archaeology)
	•	📌 M4: UI enhancements (story maps, vector tiles)
	•	📌 M5: Predictive modeling & NASA-grade simulations ￼

👉 See ROADMAP.md

⸻

🤝 Contributing

We welcome contributions!
	•	✔️ Keep STAC valid + configs schema-checked
	•	✔️ Use MCP templates (experiment.md, sop.md, model_card.md) ￼
	•	✔️ Follow CI hooks + submit PRs with clear commits

⸻

📚 Citation

@software{kansas_geo_timeline_2025,
  title = {Kansas Geo Timeline — Frontier Matrix},
  author = {Barta, Andy and contributors},
  year = {2025},
  url = {https://github.com/bartytime4life/Kansas-Frontier-Matrix}
}


⸻

⚖️ License

MIT © 2025 — Kansas Frontier Matrix

⸻

✨ This README:
	•	Uses dynamic badges wired to CI
	•	Embeds live data coverage matrix
	•	Anchors content in MCP reproducibility standards
	•	Connects maps, archives, disasters, & oral histories into one forensic timeline

⸻
