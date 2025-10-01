<div align="center">


📚 Kansas-Frontier-Matrix — Web Documentation

web/docs/

Mission: keep architecture, design, and extension guides close to the viewer so the UI stays consistent, reproducible, and contributor-friendly. The web app renders knowledge-graph data on a timeline + map backed by an ETL/AI pipeline and a graph DB.  ￼

</div>



⸻

🗂️ Index

File	Status	Purpose
ARCHITECTURE.md	✅ current	App flow, runtime data paths, container layout, API boundary
STYLE_GUIDE.md	✅ current	CSS tokens, responsive rules, JS/TS patterns, JSON schema conventions
DEVELOPER_GUIDE.md	✅ current	Loading configs, time filtering, adding layer types, popup hooks
UI_DESIGN.md	✅ current	Sidebar/timeline patterns, detail panel, legends/search
CONTRIBUTING.md	✅ current	PRs, CI checks, style/lint, doc updates
CHANGELOG.md	✅ current	User-visible changes to web app + docs

Cross-link with relative paths into web/ (e.g., ../index.html, ../config/, ../app.js, ../css/). Keep docs in lock-step with the code (“living docs”).  ￼

⸻

🔌 How the docs connect to the running app

flowchart TD
  A["STAC & Sources\n(stac/items/**)"] --> B["Config Build\n(make site-config)"]
  B --> C["Viewer Config\n(web/config/app.config.json)"]
  C --> D["Runtime\n(web/index.html + app.js)"]
  D --> E["MapLibre\n(sources/layers)"]
  D --> F["UI\n(sidebar · legend · timeline)"]

<!-- END OF MERMAID -->


Reality check (stack): ETL ➜ Knowledge Graph (Neo4j) ➜ API ➜ Web (timeline+map). The viewer consumes the time-aware JSON configs produced from STAC + sources; the API serves graph data (people, places, events, documents) the UI can fetch for popups, search, and the detail panel.  ￼  ￼

⸻

🧩 Runtime contract (minimal yet strict)

1) Viewer config excerpt (web/config/app.config.json)

{
  "version": "1.4.0",
  "title": "Kansas-Frontier-Matrix",
  "style": "https://demotiles.maplibre.org/style.json",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "timeUI": { "step": 1, "loop": false, "fps": 12 },
  "layers": []
}

Behavior: the timeline drives layer visibility via time/defaultYear; the sidebar lists layers by category; the detail panel shows linked graph content (people, places, docs) for clicked events/layers.  ￼  ￼

2) Raster layer (tiles)

{
  "id": "usgs_topo_1894_larned",
  "title": "USGS Historic Topo — Larned (1894)",
  "type": "raster",
  "url": "./tiles/historic/usgs_1894_larned/{z}/{x}/{y}.png",
  "category": "historical",
  "visible": true,
  "opacity": 0.7,
  "time": { "start": "1894-01-01", "end": "1894-12-31" }
}

3) GeoJSON layer (features + popup)

{
  "id": "ks_settlements",
  "title": "Settlements, Forts, Trading Posts",
  "type": "geojson",
  "data": "data/processed/towns_points.json",
  "category": "culture",
  "timeProperty": "year",
  "popup": ["name", "type", "year", "year_end"],
  "style": {
    "circleColor": "#FF595E",
    "circleRadius": 4,
    "circleOpacity": 0.95,
    "circleStrokeColor": "#FFFFFF",
    "circleStrokeWidth": 1
  }
}

Hook: implement window.attachPopup to display feature properties and/or to reach into the graph via API for richer details.  ￼

⸻

🧪 Local preview & validation

# Serve the site
cd web && python -m http.server 8080

# Generate config from STAC + sources, then validate
make stac stac-validate site-config

# Lint/validate JSON configs (examples)
jq . web/config/app.config.json > /dev/null
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json
ajv validate -s web/config/layers.schema.json      -d web/config/layers.json

The site consumes time-aware configs produced by the ETL/STAC pipeline; the API can be stood up in parallel to power search/detail panes if enabled in your environment.  ￼  ￼

⸻

🧭 UI behaviors (what contributors rely on)
	•	Sidebar: toggles layers, grouped logically (e.g., “Historic Maps”, “Environmental Layers”). Clear names with year/source help users.  ￼
	•	Timeline: canvas-based, pan/zoom, hundreds of events; it filters the map to the active year(s).  ￼
	•	Map: MapLibre GL, clustered points where dense; click opens popup → focus in timeline + detail panel.  ￼
	•	Detail panel & search: entity traverse (event → people/places → related events/docs), global search hits API.  ￼  ￼

⸻

🔁 Contribution workflow (web scope)
	1.	Branch with small, focused changes (UI, config, docs).
	2.	Run local checks: Mermaid renders, JSON valid, layer URLs reachable, popups working.
	3.	Open a PR with screenshots and doc updates in the same PR (living docs).  ￼
	4.	CI must pass (schema + link checks).
	5.	Update CHANGELOG.md for user-visible changes.

Doc discipline is MCP-style: documentation-first, reproducibility, provenance (keep configs + docs versioned; include what changed & why).  ￼  ￼

⸻

🧱 Adding layers the “right” way
	•	Prefer COG GeoTIFF (rasters) and GeoJSON (vectors), WGS84 (EPSG:4326) for web alignment; name layers with year(s) for timeline clarity.  ￼
	•	Build from STAC items + data/sources/*.json, then run make site-config to emit viewer configs.
	•	For archival layers (historic topo, soils, parcels), follow the GIS Archive/Deeds guide (conversion, grouping, and optional graph linkage for parcels/PLSS).  ￼  ￼

⸻

🔗 App ↔ Graph API (optional but supported)

If your deployment includes the API/graph:
	•	The UI can call REST (or GraphQL) endpoints for event/person/place lookup and global search.  ￼  ￼
	•	Popups may resolve feature IDs (e.g., a parcel key) to graph nodes for deed chains or related documents.  ￼

This wiring matches the project’s layered design (ETL ➜ graph ➜ API ➜ web).  ￼

⸻

✍️ Authoring standards for these docs
	•	Headings start at #; don’t skip levels.
	•	Close fences & type them (bash, json, mermaid).
	•	Prefer short paragraphs; use lists/tables where clearer.
	•	Internal links are relative; external sources are cited or mirrored where possible.
	•	Update docs with code/config changes; keep this README the entry point.  ￼

⸻

🧭 See also
	•	../config/ — viewer config & schemas; categories/legend
	•	../app.js — layer loading, popup hooks (attachPopup) and event wiring  ￼
	•	../css/ — layout, theme tokens, map/timeline styling
	•	../../stac/ — STAC catalog powering config builds
	•	System/stack details: Developer Docs (ETL, Graph, API, UI modules).  ￼  ￼

⸻

Why this layout works

It mirrors the true architecture (sources → STAC → configs → UI + optional API/graph), it’s reproducible and contributor-friendly, and it aligns with the project’s documentation-first/MCP principles so newcomers can confidently ship UI changes without breaking the viewer or the time slider.  ￼  ￼

⸻
