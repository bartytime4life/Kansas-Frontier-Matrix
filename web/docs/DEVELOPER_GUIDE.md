<div align="center">

# 🛠 Kansas-Frontier-Matrix — Web Developer Guide (`web/`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy Security Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📖 Purpose

This guide is for **contributors and maintainers** working on the `web/` viewer.  
It explains how **configs, code, and UI connect**, and how to **extend or debug** them.

---

## 1. ⚙️ Config Loading

Order of preference (**first hit wins**):

1. `./app.config.json` → **primary** (generated from STAC)  
2. `./config/app.config.json` → **override/fallback**  
3. `./config/viewer.json` or `./config/layers.json` → **dev-only**  
4. `./layers.json` → **legacy**  

Configs define:

- **Basemap/terrain rasters** (`url` or `tiles`)  
- **GeoJSON overlays** (`data`)  
- **Temporal windows** (`time.start`, `time.end`, or feature `timeProperty`)  
- **Legend info** (`legendKey` → `legend.json`)  
- **Categories** for sidebar grouping (`category`)  

👉 See [`STYLE_GUIDE.md`](STYLE_GUIDE.md) for schema-lite + JSON key conventions.  
👉 See [`ARCHITECTURE.md`](ARCHITECTURE.md) for system-wide flow.

---

## 2. 🧩 How `index.html` + `app.js` Work

1. **Load config** → fetch JSON, merge defaults, normalize `layers[]`.  
2. **Init MapLibre** → apply style, center, zoom, and optional bounds.  
3. **Register sources** → raster tiles, DEMs, or GeoJSON.  
4. **Build UI** → sidebar groups, layer toggles, opacity sliders, legend.  
5. **Bind events**:  
   - Timeline slider → updates `year` and filters layers  
   - Sidebar toggles → show/hide overlays  
   - Opacity sliders → adjust alpha on rasters or GeoJSON  
6. **Update map** → MapLibre refreshes in real time (no reload).

```mermaid
flowchart TD
  A["Config:\napp.config.json"] --> B["Viewer Logic:\nindex.html / app.js"]
  B --> C["MapLibre:\nmap + sources/layers"]
  B --> D["UI:\nsidebar + legend + time slider"]
  D -- "toggles · opacity" --> C
  D -- "year filter" --> C


⸻

3. ➕ Adding a New Layer
	1.	Place assets:
	•	Raster tiles → web/tiles/...
	•	GeoJSON → web/vectors/... or web/data/processed/...
	2.	Add entry in app.config.json (or STAC → config generator). Example:

{
  "id": "railroads_1900",
  "title": "Railroads (c. 1900)",
  "category": "infrastructure",
  "type": "geojson",
  "data": "./vectors/infrastructure/railroads_1900.geojson",
  "opacity": 1.0,
  "visible": true,
  "time": { "start": "1900-01-01", "end": "1900-12-31" },
  "style": {
    "lineColor": "#d97706",
    "lineWidth": 1.6,
    "lineOpacity": 0.95
  },
  "popup": ["name", "year_built", "operator"],
  "legendKey": "railroads"
}

	3.	Add legend mapping (config/legend.json):

{
  "symbols": {
    "railroads": { "line": true, "preview": "#d97706" }
  },
  "layerBindings": {
    "railroads_1900": "railroads"
  }
}

	4.	Rebuild config (if using STAC → config generator):

make site-config


⸻

4. 🐞 Debugging & Testing

Validate JSON

jq . web/config/app.config.json > /dev/null
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json

Serve locally

# Python
cd web && python -m http.server 8080

# Node.js
npx http-server web -p 8080

→ Open http://localhost:8080/

Common pitfalls
	•	❌ ../ in paths → will 404 on GitHub Pages.
	•	❌ Missing id or wrong type → UI silently skips the layer.
	•	❌ Large GeoJSON (>10 MB) → sluggish → convert to tiles (PMTiles, Tippecanoe).
	•	❌ Legend not showing → legendKey must match a symbol in legend.json.

⸻

5. 🔧 Extending the Viewer
	•	New categories → add to config/categories.json for sidebar grouping.
	•	Timeline behavior →
	•	time.start/time.end = layer span
	•	timeProperty/endTimeProperty = feature spans
	•	Paint styles → support line, fill, circle (converted to MapLibre paint).
	•	Legend system → centralized in legend.json, theme-aware.
	•	Plugins → add helpers via window.* (e.g., window.attachPopup, window.LegendControl).

⸻

6. 📌 Contribution Notes
	•	Use commit prefixes from STYLE_GUIDE.md §7.
	•	Keep configs web-relative (./vectors/..., ./tiles/...).
	•	Run make prebuild before pushing (validates configs + STAC).
	•	Test across browsers (Chrome, Firefox, Safari).
	•	Check light/dark mode, reduced motion, keyboard focus.
	•	Update docs (DEVELOPER_GUIDE.md, STYLE_GUIDE.md) if adding new keys/categories.

⸻

7. 🔄 Layer Lifecycle (Visual)

flowchart LR
  A["Add Data Files\n(web/tiles or web/vectors)"] --> B["Update app.config.json"]
  B --> C["Link Legend\n(config/legend.json)"]
  C --> D["Run Validation\n(jq + ajv)"]
  D --> E["Preview in Browser\n(local server)"]
  E --> F["Commit & PR"]


⸻


<div align="center">


✅ Workflow summary → add → validate → preview → commit → PR.
The viewer is fully config-driven — no hardcoding required.

</div>
```
