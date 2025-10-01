<div align="center">

# 🧬 Kansas-Frontier-Matrix — Web Config Schema (`web/docs/SCHEMA.md`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy Security Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📖 Purpose

The web viewer ingests a **merged config** (`app.config.json`).  
It defines **map defaults**, **timeline bounds**, and the **layers** rendered in the UI.

> 🔗 **Authoritative schemas** live in `web/config/`:
>
> - `appconfig.schema.json` — top-level viewer config  
> - `layer.schema.json` — single layer object  
> - `layers.schema.json` — array of layers

---

## 🧱 Top-Level Structure

```json
{
  "version": "1.4.0",
  "generated": "2025-09-30T21:12:13Z",
  "title": "Kansas-Frontier-Matrix",
  "subtitle": "Time · Terrain · History",
  "style": "https://demotiles.maplibre.org/style.json",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "bounds": [-102.05, 36.99, -94.59, 40.00],
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "timeUI": { "step": 1, "loop": false, "fps": 8 },
  "defaults": {
    "minzoom": 4,
    "maxzoom": 18,
    "opacity": 1.0,
    "visible": false
  },
  "layers": []
}

Fields
	•	version — semantic version of this config format or build artifact
	•	generated — ISO-8601 timestamp for provenance
	•	title, subtitle — UI headings
	•	style — MapLibre style URL (or relative)
	•	center, zoom, bounds — initial view and optional constraint extent
	•	time — global timeline bounds (min/max ISO dates)
	•	defaultYear — initial timeline position
	•	timeUI — slider behavior (step, loop, fps if animating)
	•	defaults — fallback paint/visibility/zoom for layers
	•	layers — array of layer objects (see Layer Schema)

⸻

🧩 Layer Schema (Schema-Lite)

{
  "id": "railroads_1900",
  "title": "Railroads (c. 1900)",
  "category": "infrastructure",
  "type": "geojson",
  "data": "./vectors/infrastructure/railroads_1900.geojson",
  "time": { "start": "1900-01-01", "end": "1900-12-31" },
  "timeProperty": "year_built",
  "style": { "lineColor": "#d97706", "lineWidth": 1.6, "lineOpacity": 0.95 },
  "visible": true,
  "legendKey": "railroads",
  "attribution": "Compiled / KFM",
  "popup": ["name", "operator", "year_built"]
}

Required
	•	id, title, category, type, and one of data (GeoJSON) or url (raster tiles)

Types
	•	raster, raster-dem, image → require url (e.g., ./tiles/.../{z}/{x}/{y}.png)
	•	geojson (or vector) → require data (web-relative path)

Temporal
	•	Layer span: time.start, time.end
	•	Feature span: timeProperty, endTimeProperty

Style (camelCase)
	•	Lines: lineColor, lineWidth, lineOpacity
	•	Fills: fillColor, fillOpacity
	•	Circles: circleColor, circleRadius, circleOpacity

⸻

🧭 Config Anatomy (Visual)

flowchart TD
  A["app.config.json"] --> B["Map defaults\n(style · center · zoom · bounds)"]
  A --> C["Timeline\n(time.min/max · defaultYear · timeUI)"]
  A --> D["Defaults\n(minzoom · maxzoom · opacity · visible)"]
  A --> E["Layers[]\n(raster · geojson · image)"]
  E --> F["Category & Legend\n(category · legendKey)"]
  E --> G["Temporal\n(time or timeProperty)"]
  E --> H["Style\n(line/fill/circle)"]
  E --> I["Attribution & Popup\n(provenance · fields)"]


⸻

🧪 Validation

CLI (local)

# Entire app config against top-level schema
ajv validate -s web/config/appconfig.schema.json -d web/app.config.json

# Validate only the layers array
jq '.layers' web/app.config.json > /tmp/_layers.json
ajv validate -s web/config/layers.schema.json -d /tmp/_layers.json

# Validate a single layer object
ajv validate -s web/config/layer.schema.json -d web/data/layers/railroads_1900.json

Quick syntax check

jq . web/app.config.json > /dev/null

💡 CI should also verify category is one of the keys in config/categories.json, and that legendKey maps to config/legend.json.symbols.

⸻

📌 Conventions & Rules
	•	Paths are web-relative (e.g., ./vectors/..., ./tiles/...) — no ../ (breaks GitHub Pages)
	•	Categories must exist in config/categories.json (CATEGORIES.md)
	•	Legend symbols live in config/legend.json (legendKey → symbols)
	•	Attribution is required for provenance and licensing
	•	Keep GeoJSON ≤ 10 MB (convert large data to tiles/PMTiles)
	•	Accessibility: legend colors should meet contrast needs; set sensible opacity

⸻

🧷 Minimal Example (app.config.json)

{
  "version": "1.4.0",
  "generated": "2025-09-30T13:15:42Z",
  "title": "Kansas-Frontier-Matrix",
  "style": "https://demotiles.maplibre.org/style.json",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "defaults": { "minzoom": 4, "maxzoom": 18, "opacity": 1.0, "visible": false },
  "layers": [
    {
      "id": "nlcd_2019",
      "title": "Land Cover (NLCD 2019)",
      "category": "environment",
      "type": "raster",
      "url": "./tiles/nlcd_2019/{z}/{x}/{y}.png",
      "time": { "start": "2019-01-01", "end": "2019-12-31" },
      "opacity": 0.9,
      "visible": false,
      "legendKey": "landcover",
      "attribution": "USGS NLCD 2019 (Public Domain)"
    }
  ]
}


⸻

🔗 See Also
	•	ARCHITECTURE.md — big-picture flow (load order, UI wiring)
	•	STYLE_GUIDE.md — CSS/JS/JSON conventions and examples
	•	LAYERS.md — layer schema, examples, and style quick reference
	•	CATEGORIES.md — category keys and color taxonomy
	•	CONTRIBUTING.md — PR workflow and checks

⸻


<div align="center">


✅ Keep configs valid, web-relative, and attributed to ensure a reproducible, accessible viewer.

</div>
```
