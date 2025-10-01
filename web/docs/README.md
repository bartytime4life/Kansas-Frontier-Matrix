<div align="center">

# 📚 Kansas-Frontier-Matrix — Web Documentation  
`web/docs/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

**Mission:** keep **architecture, design, and extension guides** close to the viewer so the UI stays  
**consistent, reproducible, and contributor-friendly.**

---

[![Serve Site](https://img.shields.io/badge/QuickStart-Serve_Site-2ea44f?logo=python&logoColor=white)](#quick-start)  
[![Validate Config](https://img.shields.io/badge/QuickStart-Validate_Config-007ec6?logo=json&logoColor=white)](#local-preview)  
[![Add Layer](https://img.shields.io/badge/QuickStart-Add_Layer-orange?logo=mapbox&logoColor=white)](#runtime-contract)

</div>

---

## 🚀 Quick Start {#quick-start}

```bash
# 1. Serve the site locally
cd web && python -m http.server 8080

# 2. Generate configs from STAC + sources, then validate
make stac stac-validate site-config

# 3. Add a new layer (example: GeoJSON points)
# → Update web/config/layers.json
# → Document in DEVELOPER_GUIDE.md

flowchart LR
  A["Serve\n<code>python -m http.server</code>"] --> B["Generate/Validate\n<code>make stac stac-validate site-config</code>"]
  B --> C["Add Layer\nedit <code>web/config/layers.json</code>"]
  C --> D["Preview\nrefresh browser & test"]

<!-- END OF MERMAID -->


🛠️ Troubleshooting
	•	Port already in use (8080): run python -m http.server 8081.
	•	Mermaid not rendering: ensure fenced block starts with ```mermaid and is closed.
	•	JSON parse / schema errors:

jq . web/config/app.config.json
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json


	•	CORS errors: always load via http://localhost:PORT, not file://.
	•	404s for tiles/data: check relative paths from /web/.
	•	Mixed content blocked: avoid http assets when serving over https.
	•	Timeline not updating: ensure ISO-8601 dates and proper timeProperty.
	•	Cache issues: hard refresh (Ctrl+Shift+R / Cmd+Shift+R).

⸻

💡 Dev Tips
	•	Inspect layers live:
In browser console:

map.getStyle().layers


	•	MapLibre inspector: press Alt + I (if enabled) to inspect sources/layers.
	•	Force reload config: append ?t=123 to index.html to bypass cache.
	•	Chrome DevTools shortcuts:
	•	Ctrl+Shift+I / Cmd+Opt+I → open DevTools
	•	Ctrl+Shift+P → quick command palette
	•	Check network paths: DevTools → Network tab shows missing tiles/GeoJSON.
	•	Style tweaks: use map.setPaintProperty('layer-id', 'circle-color', '#FF0000') to test colors live.
	•	Timeline debugging: log events from slider:

document.addEventListener("yearchange", e => console.log(e.detail))



⸻

🗂️ Index {#index}

File / Section	Status	Purpose
ARCHITECTURE.md	✅ current	App flow, runtime data paths, container layout, API boundary
STYLE_GUIDE.md	✅ current	CSS tokens, responsive rules, JS/TS patterns, JSON schema conventions
DEVELOPER_GUIDE.md	✅ current	Loading configs, time filtering, adding layer types, popup hooks
UI_DESIGN.md	✅ current	Sidebar/timeline patterns, detail panel, legends/search
CONTRIBUTING.md	✅ current	PRs, CI checks, style/lint, doc updates
CHANGELOG.md	✅ current	User-visible changes to web app + docs
How the docs connect	📖 section	Diagram of STAC → config → runtime → MapLibre → UI
Runtime contract	📖 section	JSON config excerpt + raster & GeoJSON layer snippets
Local preview & validation	📖 section	Commands for serving site, generating configs, schema validation
UI behaviors	📖 section	Sidebar, timeline, map, popups, detail panel
Contribution workflow	📖 section	Branching, checks, CI, PR docs
Authoring standards	📖 section	Writing rules for docs, fences, headings
See also	📖 section	Links into configs, app.js, CSS, and STAC


⸻

🔌 How the docs connect to the app {#how-these-docs-connect}

flowchart TD
  A["STAC & Sources\n(stac/items/**)"] --> B["Config Build\n(make site-config)"]
  B --> C["Viewer Config\n(web/config/app.config.json)"]
  C --> D["Runtime\n(web/index.html + app.js)"]
  D --> E["MapLibre\n(sources/layers)"]
  D --> F["UI\n(sidebar · legend · timeline)"]

<!-- END OF MERMAID -->



⸻

🧩 Runtime contract {#runtime-contract}

Viewer config excerpt (web/config/app.config.json)

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

Raster layer

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

GeoJSON layer

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


⸻

🧪 Local preview & validation {#local-preview}

# Serve the site
cd web && python -m http.server 8080

# Generate config from STAC + sources, then validate
make stac stac-validate site-config

# Lint/validate JSON configs
jq . web/config/app.config.json > /dev/null
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json
ajv validate -s web/config/layers.schema.json      -d web/config/layers.json


⸻

🧭 UI behaviors {#ui-behaviors}
	•	Sidebar: toggles layers, grouped by category.
	•	Timeline: filters features by year; supports step, loop, fps.
	•	Map: MapLibre GL; clusters dense points, popups for features.
	•	Detail panel & search: graph/API integration for related entities.

⸻

🔁 Contribution workflow {#contribution-workflow}
	1.	Branch with small, focused changes.
	2.	Run local checks (Mermaid, JSON, configs).
	3.	Open a PR with screenshots (if UI).
	4.	CI must pass (schema + link checks).
	5.	Update CHANGELOG.md for user-visible changes.

⸻

✍️ Authoring standards {#authoring-standards}
	•	Headings start at #.
	•	Close fences & type them (bash, json, mermaid).
	•	Use lists/tables for structure.
	•	Relative links inside repo.
	•	Docs must be updated with code changes.

⸻

🔗 See also {#see-also}
	•	../config/ — viewer configs & schemas
	•	../app.js — config loading, popup hooks
	•	../css/ — layout & theme tokens
	•	../../stac/ — STAC catalog powering configs

⸻

✅ Principle: these docs keep the web UI maintainable, accessible, and extendable for Kansas’s time-aware layers and stories.
