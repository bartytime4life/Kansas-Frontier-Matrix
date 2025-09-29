
⸻

Kansas Geo Timeline — Time · Terrain · History


⸻

🌟 What is this?

The Kansas Geo Timeline is an open-source, MCP-aligned knowledge hub to explore
Kansas’s terrain, climate, culture, and history through time.

It combines scientific-grade geospatial data with historical narratives:
	•	🌄 Elevation & Terrain — LiDAR DEM, shaded relief, slope/aspect, contours
	•	🗺 Historic Maps — USGS topo scans, county plats, early soil surveys
	•	🧭 Culture & Sovereignty — treaties, tribal land transfers, railroads, trails, settlements
	•	🌱 Environment & Hazards — land cover, soils, hydrology, wildfires, tornadoes, droughts
	•	📖 Archival Narratives — diaries, newspapers, oral histories, archaeology finds

All datasets are indexed with STAC 1.0.0 for reproducibility, linked into a
Neo4j knowledge graph for reasoning, and rendered via a MapLibre timeline viewer
with optional Google Earth KML/KMZ exports ￼ ￼.

Think of it as a time-aware atlas + historical knowledge graph.

⸻

🚀 Live Access
	•	🌐 Web Viewer: MapLibre + Timeline
	•	🌍 Google Earth: Kansas Terrain KMZ

⸻

📊 System Architecture

flowchart TD
  A["Sources\n(data/sources/*.json)"] -->|fetch| B["COGs\n(data/cogs/**/*.tif)"]
  B -->|derive| C["Derivatives\n(slope, aspect, hillshade, vectors)"]
  C -->|index| D["STAC Catalog\n(stac/catalog.json, items/)"]
  D -->|graph| H["Knowledge Graph\n(Neo4j, CIDOC CRM schema)"]
  D -->|render| E["Configs\n(web/config/*.json)"]
  H -->|serve| E
  E -->|serve| F["MapLibre Viewer"]
  D -->|export| G["KML/KMZ\n(earth/)"]

  classDef src fill:#FFD166,stroke:#333;
  classDef cogs fill:#06D6A0,stroke:#333;
  classDef stac fill:#118AB2,stroke:#fff;
  classDef web fill:#073B4C,stroke:#fff;
  classDef earth fill:#EF476F,stroke:#fff;

  class A src;
  class B cogs;
  class C cogs;
  class D stac;
  class E web;
  class F web;
  class G earth;
  class H stac;

Layers are semantically enriched with ontologies (CIDOC CRM, OWL-Time, PeriodO)
for temporal and cultural reasoning ￼.

⸻

🛠 Quickstart

Option A — Local Python

python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Build pipeline
make fetch           # download raw data
make cogs            # convert GeoTIFF → COG
make terrain         # slope, aspect, hillshade
make stac            # generate STAC catalog/items
make stac-validate   # schema + STAC validation
make site-config     # build web/app.config.json
python -m http.server -d web 8080

Option B — Docker Compose

docker compose build kfm
docker compose --profile dev up -d site   # serve viewer
docker compose --profile docs up -d docs  # serve live docs


⸻

📂 Repository Layout

data/
  sources/       # JSON descriptors (URL, CRS, bounds, license, temporal span)
  cogs/          # Cloud Optimized GeoTIFFs (immutable)
  derivatives/   # terrain, contours, hydrology, change maps
  processed/     # cleaned vectors/rasters (ready-to-use)
stac/            # STAC 1.0.0 catalog, collections, items
web/             # MapLibre web viewer
  config/        # layers.schema.json, categories.json, legends
  data/          # small GeoJSONs mirrored for dev
earth/           # KML/KMZ exports (regionated)
scripts/         # ETL, STAC tools, config renderers
docker/          # reproducible environments
.github/         # CI/CD workflows, roadmap, pre-commit hooks


⸻

📑 Key Data Sources

ID	Title	File/Entry	Notes
ks_dem_1m	Kansas DEM (1 m LiDAR)	ks_dem.json	Statewide LiDAR via ArcGIS
usgs_topo	Historic USGS Topos	usgs_topo.json	1890–1950 georeferenced scans
ks_treaties	Kansas Treaties	treaties_polygons.json	Time-aware polygons
ks_railroads	Railroads (historic)	ks_railroads.json	Digitized expansion by year
hazards	Tornadoes, Floods, Fires	NOAA SPC + FEMA + NIFC	Multi-hazard GIS ￼
oral_hist	Oral Histories	Tribal narratives & interviews ￼	Linked to places & events

See data/sources/ for the full catalog.

⸻

🧰 Make Targets

make fetch            # download raw sources
make cogs             # raw GeoTIFF → COG
make terrain          # gdaldem slope/aspect/hillshade
make stac             # build STAC catalog + items
make stac-validate    # validate catalog/items
make site-config      # render web/app.config.json
make site             # fallback: layers.json + dev mirrors
make prebuild         # validation + configs (CI shortcut)

Extras:

make validate-cogs    # conformance checks
make mosaic-county    # county-level LiDAR mosaics
make dem-checksum     # write/verify .sha256
make regionate        # regionated KML/KMZ tree


⸻

✅ Reproducibility & CI
	•	Sidecars: .sha256 + .meta.json for every artifact
	•	CI pipelines:
	•	site.yml → GitHub Pages
	•	stac-badges.yml → live Shields badges
	•	codeql.yml + trivy.yml → security scans
	•	pre-commit → lint, format, schema validate
	•	MCP protocols: every data operation = experiment step ￼ ￼

make prebuild   # run all validation before pushing


⸻

🗺 Roadmap
	•	M1: Enrich Data Sources (DEM, treaties, railroads, hazards)
	•	M2: Terrain & Hydrology analysis (flowdir, floodplains)
	•	M3: Storytelling & Education layers (oral histories, archaeology)
	•	M4: Technical Enhancements (vector tiles, UI polish, story maps) ￼
	•	M5: MCP Integration (experiment logging, predictive models ￼)

See ROADMAP.md and .github/roadmap/roadmap.yaml.

⸻

📦 Requirements
	•	Python: rasterio, rio-cogeo, pyproj, shapely, pystac, jsonschema
	•	GDAL CLI: gdal_translate, gdalwarp, gdaldem
	•	Node.js: roadmap sync, site build
	•	Docker: reproducible environments
	•	Neo4j (optional): knowledge graph integration ￼

⸻

💡 Troubleshooting
	•	Mermaid doesn’t render → quote labels, use \n
	•	Rasters not showing → serve COGs/tiles, not raw .tif
	•	Timeline inert → ensure time.start/end or timeProperty present
	•	Legends missing → define in legend.json or per-layer
	•	File:// blocked → always serve via HTTP (python -m http.server or Docker)

⸻

🤝 Contributing

We welcome PRs!
Follow MCP experiment templates: state problem, hypothesis, method, data, and conclusion ￼.
See CONTRIBUTING.md.

⸻

📚 References
	•	Kansas GIS Hub
	•	USGS Historical Topos
	•	Kansas Geological Survey
	•	NOAA Climate & Storm Events
	•	PeriodO Gazetteer

⸻

🔗 Summary:
This README now ties together terrain + history + hazards + oral traditions with MCP rigor, CI reproducibility, and semantic integration. It serves both as a public landing page and a developer’s map into the repo.

⸻

Would you like me to also generate a shorter “Public-facing README” (for GitHub Pages visitors) while keeping this one as the developer README in the repo? That way, casual users see an atlas-style intro, while contributors get the full MCP + CI depth.
