🌾 Kansas Geo Timeline — Time · Terrain · History

Explore the layered story of Kansas across centuries — where terrain, climate, culture, and history intersect.

This project builds an open-source, reproducible system to transform archival maps, LiDAR terrain, treaties, railroads, disasters, and oral histories into an interactive atlas + knowledge graph.

⸻

🚀 Quick Links
	•	🌐 Live Web Viewer
	•	🌍 Google Earth KMZ
	•	📊 STAC Catalog

⸻

🗺 Why It Matters

Kansas’s history is layered in maps, treaties, disasters, geology, and stories.
This project helps researchers, educators, and communities explore:
	•	🚂 How railroads and towns spread across tribal lands
	•	🌪️ How droughts, floods, and Dust Bowl storms reshaped settlement
	•	🪶 How archaeology and oral histories connect to landscapes
	•	🔥 How paleoclimate, fire regimes, and water systems influenced resilience

👉 It’s more than maps — it’s a time-aware knowledge hub for Kansas.

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

✨ Pipeline Highlights
	•	📂 STAC 1.0.0 catalog → provenance + temporal coverage
	•	🗺️ Cloud-Optimized GeoTIFFs (COGs) → terrain + rasters
	•	🧩 Neo4j Knowledge Graph → links people, places, events
	•	🖥️ MapLibre Viewer → timeline slider + dynamic layers
	•	🌍 Google Earth exports → KMZ/KML for immersive 3D

⸻

⚡ Quickstart

🐍 Local Python

python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

make fetch cogs terrain stac stac-validate site-config
python -m http.server -d web 8080

🐳 Docker

docker compose up -d site


⸻

📂 Repository Layout

data/
  sources/       # JSON descriptors (URL, CRS, bounds, license, time)
  cogs/          # Cloud-Optimized GeoTIFFs (immutable)
  derivatives/   # slope, aspect, hydrology, change maps
  processed/     # cleaned + normalized vectors/rasters
stac/            # STAC 1.0.0 catalog, collections, items
web/             # MapLibre viewer, configs, legends
earth/           # Google Earth exports (KML/KMZ)
scripts/         # ETL, STAC tools, validators
docker/          # reproducible containers
.github/         # CI/CD workflows, roadmap, pre-commit


⸻

📊 Data Coverage Matrix (Live Status)

🌐 Domain / Layer	🔗 Source(s) Integrated	📌 Status
DEM / Terrain	USGS LiDAR (1 m), KGS, 3DEP	
Hillshade / Derivatives	LiDAR COGs → slope, aspect, hillshade	
Hydrology	USGS NHD, Kansas River flood layers	
Land Cover	NLCD 1992–2021	
Soils / PLSS / Parcels	NRCS SSURGO, Kansas GIS Hub	
Treaties & Tribal Lands	Treaty polygons, tribal cessions	
Railroads & Trails	Historic railroads 1850–1920	
Topographic Maps	USGS Historic Topo, UT PCL library	
Climate Normals	NOAA 1991–2020, Daymet	
Hazards — Tornado	NOAA SPC Tornado GIS (1950–2024)	
Hazards — Drought	US Drought Monitor shapefiles	
Hazards — Floods	FEMA declarations, USGS flood data	
Hazards — Wildfire	NIFC + KS Wildland Fire perimeters	
Paleoclimate / Fire Regimes	NOAA cores, charcoal records	
Oral Histories & Archaeology	Tribal narratives, excavation sites	
Geology / Core Samples	KGS Drill Core Library	


⸻

🎯 Use Cases
	•	🚂 Animate railroad expansion (1850–1910) alongside treaties
	•	🌪️ Overlay Dust Bowl land cover change with NOAA drought indices
	•	🪶 Link oral histories and diaries to specific places + years
	•	🌊 Compare pre-dam vs post-dam hydrology in Kansas River floodplains
	•	🔥 Integrate fire history, paleoclimate, archaeology into narratives

⸻

✅ Reproducibility & CI
	•	🔐 Checksums: .sha256 sidecars for every artifact
	•	📏 Validation: STAC + JSON Schema in CI
	•	🛠️ Pipelines:
	•	site.yml → build & deploy web viewer
	•	stac-badges.yml → shields for dataset health
	•	codeql.yml + trivy.yml → security scans

make prebuild


⸻

🛠 Roadmap
	•	📌 M1: Expand data sources (treaties, railroads, hazards)
	•	📌 M2: Terrain & hydrology modeling (flowdir, floodplains)
	•	📌 M3: Storytelling layers (oral histories, archaeology)
	•	📌 M4: UI enhancements (story maps, vector tiles)
	•	📌 M5: Predictive modeling & MCP simulation protocols

👉 See ROADMAP.md for details.

⸻

🤝 Contributing

We welcome contributions!
	•	✔️ Keep STAC valid + configs schema-checked
	•	✔️ Use MCP-style experiments: Hypothesis → Method → Data → Results
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

✨ This README now:
	•	Uses dynamic live badges wired to CI → no more manual ✔️/⚠️/❌
	•	Shows up-to-date dataset health synced with STAC validation
	•	Is polished for contributors, researchers, and educators

⸻
