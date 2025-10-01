<div align="center">

# 🗺 Kansas-Frontier-Matrix — Layer Documentation (`web/docs/LAYERS.md`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy Security Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📖 Purpose

Each **map layer** is defined as JSON under `web/data/*.json` or embedded in `app.config.json`.  
This guide documents the **required fields**, **schema-lite**, and **examples** so contributors can add layers that are consistent, accessible, and performant.

Layers drive the **sidebar grouping**, **legend chips**, and **timeline filtering**.

---

## 📂 Required Fields (Schema-Lite)

| Field              | Type     | Required | Description                                                                          |
|-------------------|----------|----------|--------------------------------------------------------------------------------------|
| `id`              | string   | ✅        | Unique, stable identifier (lower-hyphen preferred)                                   |
| `title`           | string   | ✅        | Human-readable layer title                                                           |
| `type`            | string   | ✅        | One of: `raster`, `raster-dem`, `vector`, `geojson`                                  |
| `data` / `url`    | string   | ✅        | GeoJSON path (`data`) or tile URL template (`url`)                                   |
| `category`        | string   | ✅        | Must match a key in [`categories.json`](CATEGORIES.md)                               |
| `time`            | object   | opt      | `{ "start": <ISO date>, "end": <ISO date|null> }` (layer-level span)                 |
| `timeProperty`    | string   | opt      | Feature-level start property (e.g., `"year"`)                                        |
| `endTimeProperty` | string   | opt      | Feature-level end property                                                           |
| `style`           | object   | opt      | Paint object: `lineColor`, `lineWidth`, `fillOpacity`, `circleColor`, `circleRadius` |
| `visible`         | boolean  | opt      | Default visibility (true/false)                                                      |
| `attribution`     | string   | opt      | Dataset source + license info                                                        |
| `legendKey`       | string   | opt      | Symbol mapping defined in `config/legend.json`                                       |
| `popup`           | array    | opt      | Properties to show in popups                                                         |

---

## 📝 Example: Cultural Points (GeoJSON)

```json
{
  "id": "ks_settlements",
  "title": "Settlements, Forts, Trading Posts",
  "type": "geojson",
  "data": "./data/processed/towns_points.geojson",
  "category": "culture",
  "time": { "start": "1800-01-01", "end": null },
  "timeProperty": "year",
  "style": { "circleColor": "#FF595E", "circleRadius": 4, "circleOpacity": 0.9 },
  "visible": true,
  "attribution": "Compiled / Kansas Frontier Matrix",
  "popup": ["name", "year", "notes"],
  "legendKey": "settlements"
}


⸻

🌳 Example: Environmental Raster Tiles

{
  "id": "nlcd_2019",
  "title": "Land Cover (NLCD 2019)",
  "type": "raster",
  "url": "./tiles/nlcd_2019/{z}/{x}/{y}.png",
  "category": "environment",
  "time": { "start": "2019-01-01", "end": "2019-12-31" },
  "opacity": 0.9,
  "visible": false,
  "attribution": "USGS NLCD 2019 (Public Domain)",
  "legendKey": "landcover"
}


⸻

🎨 Common Styles Reference

Layers support a subset of MapLibre paint properties (camelCase).
Use these consistently in style blocks:

Style Key	Type	Applies to	MapLibre Equivalent	Example Value
lineColor	string	Line	line-color	"#d97706"
lineWidth	number	Line	line-width	1.5
lineOpacity	number	Line	line-opacity	0.8
fillColor	string	Polygon	fill-color	"#3A86FF"
fillOpacity	number	Polygon	fill-opacity	0.6
circleColor	string	Point	circle-color	"#FF595E"
circleRadius	number	Point	circle-radius	4
circleOpacity	number	Point	circle-opacity	0.9

👉 Keep symbolization minimal and readable; colors should align with CATEGORIES.md.

⸻

🧩 Usage Notes
	•	Layers are config-driven — avoid hardcoding in app.js.
	•	category must match config/categories.json.
	•	Always use web-relative paths (./vectors/..., ./tiles/...).
	•	Timeline filtering works if:
	•	time is defined at the layer level, or
	•	features include timeProperty / endTimeProperty.
	•	Performance: GeoJSON > 10 MB → convert to vector tiles (PMTiles/MBTiles).
	•	Accessibility: ensure legend color contrast; use sensible default opacity.
	•	Provenance: always include attribution with source and license.

⸻

✅ Validation

Local checks:

# JSON syntax
jq . web/data/layers/*.json > /dev/null

# Schema validation
ajv validate -s web/config/layers.schema.json -d web/data/layers/*.json

CI will run:
	•	JSON validity
	•	Category + legend consistency
	•	STAC linkage checks (if connected)

⸻

🔄 Layer Lifecycle (Visual)

flowchart LR
  A["Prepare Data\n(GeoJSON or tiles)"] --> B["Add Layer JSON\n(web/data or app.config.json)"]
  B --> C["Set Category & Legend\n(categories.json, legend.json)"]
  C --> D["Add Time Info\n(time or timeProperty)"]
  D --> E["Apply Styles\n(style: line/fill/circle)"]
  E --> F["Validate JSON\n(jq + ajv)"]
  F --> G["Preview Locally\n(static server)"]
  G --> H["Commit & PR\n(with attribution)"]


⸻


<div align="center">


Layers are the building blocks of the Kansas-Frontier-Matrix web viewer.
Keep them consistent, validated, styled, and attributed to ensure reproducibility.

</div>
```
