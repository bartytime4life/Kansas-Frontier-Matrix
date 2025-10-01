<div align="center">

# 🧩 Kansas-Frontier-Matrix — Viewer Configuration  
`web/config/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** Hold the **declarative JSON** that drives the MapLibre viewer (`web/index.html` + `app.js`).  
Configs define **what** to load (layers), **how** to render (legend/categories/styles), and **when** to show it (time).  
**Design goal:** *zero hand-tuning in code* — the viewer is driven by **STAC → `app.config.json`** plus these overrides.

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["STAC Items & Collections\n(stac/items/**)"] --> B["Render config from STAC\n(kgt render-config)"]
  B --> C["Viewer config\n(web/config/app.config.json)"]
  C --> D["MapLibre app\n(web/app.js)"]
  D --> E["UI modules\n(timeline · legend · sidebar · popup)"]

<!-- END OF MERMAID -->



⸻

📦 Contents (and purpose)

File	Req?	Purpose	Edited by	Source of truth
app.config.json	✅	Final merged viewer config (defaults + layers + time)	Generated from STAC	Yes
viewer.json	➖	Hand-edited local/dev override	Devs	No (fallback)
layers.json	➖	Layers-only catalog for quick tests/dev	Devs	No (fallback)
time_config.json	➖	Override time, defaultYear, timeUI, presets	Devs	Merges over active
legend.json	➖	Global symbology tokens; optional layer bindings	Devs/Cartography	Referenced by UI
categories.json	➖	Sidebar grouping (labels + order)	Devs/Cartography	Referenced by UI
sources.json	➖	Provenance/audit registry for layers → data sources	Devs/Data	Helpful
story_layers.json	➖	Curated themes (layersOn/off, opacity, flyTo)	Editors/Outreach	Story UI
schema.json	➖	Packed schemas (legend/categories/sources)	Devs	CI/Local
app.config.schema.json	➖	Schema for app.config.json	Devs	CI/Local
layers.schema.json	➖	Schema for layers.json	Devs	CI/Local

Rule of thumb: Keep app.config.json generated. Use viewer.json/layers.json only for experiments.

⸻

🔁 Runtime resolution (load order)

The viewer loads the first available file (top → bottom):
	1.	./app.config.json (repo web/ root)
	2.	./config/app.config.json
	3.	./config/viewer.json
	4.	./config/layers.json
	5.	./layers.json (legacy root fallback)

Overrides (if present):
	•	time_config.json → overrides time, defaultYear, timeUI.
	•	legend.json / categories.json → legend chips + sidebar grouping.

⸻

⚙️ Generate app.config.json from STAC

# 1) Build or refresh STAC (items/collections)
make stac

# 2) Render viewer config (STAC → app.config.json)
kgt render-config \
  --stac stac/items \
  --output web/config/app.config.json \
  --pretty

# 3) Validate the result
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json

Re-run after adding/removing/changing any STAC items.

⸻

📑 Contract: top-level shape

Top-level (for app.config.json / viewer.json)

{
  "version": "1.4.0",
  "generated": "2025-09-27T10:00:00Z",
  "title": "Kansas-Frontier-Matrix",
  "subtitle": "Time-aware historical GIS for Kansas",
  "style": "https://demotiles.maplibre.org/style.json",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "bounds": [-102.051, 36.993, -94.588, 40.003],
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "timeUI": { "step": 1, "loop": false, "fps": 12 },
  "defaults": {
    "minzoom": 0,
    "maxzoom": 15,
    "opacity": 1.0,
    "visible": true,
    "bounds": [-102.051, 36.993, -94.588, 40.003],
    "time": { "start": null, "end": null }
  },
  "layers": []
}

Layer schema (common keys)

{
  "id": "unique_id",
  "title": "Display Title",
  "type": "raster",
  "url": "https://tiles/{z}/{x}/{y}.png",
  "data": "data/processed/small.geojson",
  "visible": false,
  "opacity": 0.8,
  "minzoom": 0,
  "maxzoom": 19,
  "category": "reference",
  "legendKey": "symbol_id_in_legend",
  "attribution": "Source / license",
  "time": { "start": null, "end": null },
  "style": {
    "fillColor": "#A0C4FF",
    "fillOpacity": 0.6,
    "lineColor": "#3A86FF",
    "lineWidth": 1,
    "lineOpacity": 0.9,
    "lineDasharray": [2, 2],
    "circleColor": "#FF595E",
    "circleRadius": 4,
    "circleOpacity": 0.95,
    "circleStrokeColor": "#FFFFFF",
    "circleStrokeWidth": 1
  },
  "popup": ["name", "type", "year", "year_end"],
  "timeProperty": "year",
  "endTimeProperty": "year_end",
  "coordinates": [[-102.0,40.0],[-94.6,40.0],[-94.6,37.0],[-102.0,37.0]]
}

Type specifics
	•	raster → tile servers only (/{z}/{x}/{y}.png). Do not point at raw .tif.
	•	raster-dem → terrain sources (tile-based).
	•	vector → vector tiles (TileJSON/PMTiles).
	•	geojson → inline/URL GeoJSON (tile or simplify when large).
	•	image → single image overlay; must include coordinates (four corners lon/lat).

⸻

🕰️ Time overrides & presets (time_config.json)

{
  "version": "1.2.0",
  "generated": "2025-09-27T15:00:00Z",
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "timeUI": { "step": 1, "loop": false, "fps": 12 },
  "presets": [
    { "label": "Bleeding Kansas", "start": "1854-01-01", "end": "1861-12-31" },
    { "label": "Railroad Era",    "start": "1865-01-01", "end": "1900-12-31" },
    { "label": "Dust Bowl",       "start": "1930-01-01", "end": "1940-12-31" },
    { "label": "Modern Kansas",   "start": "1990-01-01", "end": "2025-12-31" }
  ]
}

Filtering uses layer time spans or feature timeProperty/endTimeProperty.

⸻

🎨 Legend & Categories (UI contracts)

legend.json

{
  "version": "1.2.0",
  "generated": "2025-09-27T00:00:00Z",
  "symbols": {
    "basemap":       { "raster": true, "preview": "#BFC7CF" },
    "historic_topo": { "raster": true, "preview": "#C7B8A0" },
    "towns":         { "circle": true, "preview": "#FF595E" }
  },
  "layerBindings": {
    "basemap_osm": "basemap",
    "usgs_topo_1894_larned": "historic_topo",
    "ks_settlements": "towns"
  }
}

categories.json

{
  "version": "1.1.0",
  "generated": "2025-09-27T00:00:00Z",
  "categories": {
    "reference":      { "label": "Reference",      "order": 0 },
    "terrain":        { "label": "Terrain",        "order": 1 },
    "environment":    { "label": "Environment",    "order": 2 },
    "historical":     { "label": "Historical",     "order": 3 },
    "documents":      { "label": "Documents",      "order": 4 },
    "infrastructure": { "label": "Infrastructure", "order": 5 },
    "culture":        { "label": "Culture",        "order": 6 },
    "hazards":        { "label": "Hazards",        "order": 7 }
  }
}


⸻

✅ Examples (correct patterns)

Historical raster (tiled)

{
  "id": "usgs_topo_1894_larned",
  "title": "USGS Historic Topo — Larned (1894)",
  "type": "raster",
  "url": "./tiles/historic/usgs_1894_larned/{z}/{x}/{y}.png",
  "opacity": 0.7,
  "visible": true,
  "category": "historical",
  "legendKey": "historic_topo",
  "attribution": "USGS Historical Topographic Map Collection",
  "time": { "start": "1894-01-01", "end": "1894-12-31" },
  "minzoom": 0,
  "maxzoom": 16
}

Time-aware GeoJSON points

{
  "id": "ks_settlements",
  "title": "Settlements, Forts, Trading Posts",
  "type": "geojson",
  "data": "data/processed/towns_points.json",
  "category": "culture",
  "legendKey": "towns",
  "time": { "start": "1800-01-01", "end": null },
  "timeProperty": "year",
  "popup": ["name", "type", "year", "year_end"],
  "style": {
    "circleColor": "#FF595E",
    "circleRadius": 4,
    "circleOpacity": 0.95,
    "circleStrokeColor": "#FFFFFF",
    "circleStrokeWidth": 1
  },
  "visible": true,
  "attribution": "Compiled / KFM"
}


⸻

🧪 Validation & CI

Local quick checks

# Lint JSON
jq . web/config/app.config.json > /dev/null

# Schema validation (viewer/app/layers)
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json
ajv validate -s web/config/layers.schema.json      -d web/config/layers.json

# Schema pack (legend/categories/sources)
ajv validate -s web/config/schema.json -d web/config/legend.json     -r web/config/schema.json
ajv validate -s web/config/schema.json -d web/config/categories.json -r web/config/schema.json
ajv validate -s web/config/schema.json -d web/config/sources.json    -r web/config/schema.json

CI guarantees
	•	STAC → app.config.json generation is checked; broken STAC = failed build.
	•	Tests assert: structure, categories, legend bindings, time ranges (layer time vs feature timeProperty), and file existence.

⸻

🧰 Troubleshooting
	•	Layer not visible → Check type, url vs data, minzoom/maxzoom, and file paths.
	•	Timeline inert → Provide layer time span or feature timeProperty/endTimeProperty (ISO dates).
	•	Legend chip missing → legendKey must match legend.json.symbols (or add layerBindings[id]).
	•	Wrong sidebar group → Ensure category exists in categories.json.
	•	Slow vectors → Tile or simplify statewide/dense GeoJSON; reserve raw GeoJSON for small sets.
	•	Raster DEM → Serve as tiles; don’t point at raw .tif (use /{z}/{x}/{y}.png).

⸻

🧭 Conventions
	•	IDs: snake_case, stable, optionally include vintage (usgs_topo_1894_larned).
	•	Categories: pick exactly one; keep in sync with categories.json.
	•	Legend: keep legendKey (or layerBindings) aligned with legend.json.symbols.
	•	Time: layer-level spans in time; heterogeneous features via timeProperty/endTimeProperty.
	•	CRS & rasters: store/serve COGs in pipelines; tile to PNG for web rendering (EPSG:4326/3857).
	•	Schemas: bump *.schema.json when adding keys; CI enforces.

⸻

🔭 Minimal data-flow

flowchart TD
  A["STAC Items\n(stac/items/*.json)"] --> B["Config Renderer\n(kgt render-config)"]
  B --> C["Viewer Config\n(web/config/app.config.json)"]
  C --> D["MapLibre App\n(web/app.js)"]
  D --> E["UI\n(Timeline · Legend · Sidebar · Popup)"]

<!-- END OF MERMAID -->



⸻

TL;DR

Generate app.config.json from STAC → tweak UX with
time_config.json, legend.json, categories.json, story_layers.json → validate → ship.

⸻


