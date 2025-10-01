<div align="center">

# 🎨 Kansas-Frontier-Matrix — Web Style Guide (`web/`)

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.github/workflows/pre-commit.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy Security Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📂 0) Directory Expectations

```text
web/
├─ index.html           # Viewer entry (loads MapLibre + builds sidebar UI)
├─ style.css            # Tokens, layout, components, accessibility
├─ app.config.json      # Primary config (fallbacks allowed; see §3)
├─ config/              # Overrides (viewer.json, layers.json, time_config.json, legend.json)
├─ tiles/               # Raster tiles (/{z}/{x}/{y}.png)
├─ vectors/             # GeoJSON overlays (relative ./vectors/... .geojson)
├─ data/processed/...   # Derived GeoJSON (./ relative paths)
└─ docs/
   └─ STYLE_GUIDE.md

👉 Rule: All URLs/paths are web-relative (./tiles/..., ./vectors/...).
❌ Avoid ../ — it will 404 on GitHub Pages.

⸻

🎨 1) CSS (style.css)

1.1 Tokens & Theming
	•	Define tokens in :root: colors, radii, shadows, z-index, typography, safe areas.
	•	Provide dark mode overrides under @media (prefers-color-scheme: dark).

1.2 Naming & Structure
	•	Prefer component classes; use IDs only for root containers.
	•	BEM-lite with kfm- prefix (e.g., .kfm-legend__row, .is-active).

1.3 Responsiveness & Layout
	•	Breakpoint: @media (max-width: 900px) → sidebar becomes bottom drawer.
	•	Use Flexbox/Grid. ❌ Avoid floats.

1.4 Accessibility
	•	Always style :focus-visible.
	•	Support prefers-reduced-motion, forced-colors.
	•	Ensure high contrast.
	•	Test RTL ([dir="rtl"]).

1.5 Controls
	•	Range sliders: .range--fill, update --value via JS.
	•	Larger touch targets under @media (pointer: coarse).

⸻

⚡ 2) JavaScript (app.js)

2.1 Helpers

const $  = (sel, root = document) => root.querySelector(sel);
const el = (tag, attrs = {}, children = []) => { /* minimal h() */ };

	•	Use const/let, never var.

2.2 Config Priority
	1.	./app.config.json
	2.	./config/app.config.json
	3.	./config/viewer.json / ./config/layers.json
	4.	./layers.json (legacy)

2.3 Map & Layers
	•	Rasters → url, GeoJSON → data.
	•	Styles via camelCase paint keys.
	•	Timeline → time or timeProperty.
	•	Opacity adjusted live from UI.

2.4 Sidebar & Legend
	•	Sidebar = layers[] grouped by category.
	•	Legend built from legend.json via legendKey.

⸻

🗂 3) JSON Configs
	•	2-space indent.
	•	Stable IDs = lower-hyphen.

3.1 Minimal Top-Level

{
  "version": "1.4.0",
  "title": "Kansas-Frontier-Matrix",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "layers": []
}

3.2 Layer Schema-Lite

Key	Type	Req	Notes
id	string	✅	Lower-hyphen, stable
title	string	✅	Human label
category	string	✅	Must match categories.json
type	string	✅	raster / geojson / image
url	string	opt	Raster tiles
data	string	opt	GeoJSON path
time	object	opt	Start/end ISO dates
timeProperty	string	opt	Feature-level start
endTimeProperty	string	opt	Feature-level end
style	object	opt	Paint (line/fill/circle)
legendKey	string	opt	Link to legend.json symbols
attribution	string	opt	Data source/license
popup	array	opt	Properties for popups


⸻

📝 4) Documentation (Markdown)
	•	Use GitHub-flavored Markdown.
	•	Headings: #, ##, ###.
	•	Code fences: always closed + language hint.
	•	Mermaid diagrams: quote labels + \n for line breaks.

Example:

flowchart TD
  A["Config:\napp.config.json"] --> B["Viewer:\nindex.html/app.js"]
  B --> C["MapLibre:\nsources/layers"]
  C --> D["UI:\nsidebar/time slider"]


⸻

♿ 5) Accessibility & UX
	•	Keyboard focus always visible.
	•	Use ARIA roles for regions + live status.
	•	Tabular numerals for years.
	•	Respect prefers-reduced-motion and forced-colors.

⸻

🗺 6) New Layer Recipe
	1.	Put assets in web/vectors/ or web/tiles/.
	2.	Add config entry (id, title, category, type, url/data).
	3.	Add legendKey if needed.
	4.	Validate JSON (jq, ajv) and preview locally.

⸻

📝 7) Commits

Use conventional prefixes:
css:, js:, config:, docs:, a11y:, tiles:, vectors:, build:

⸻

🔍 8) Validation & CI

jq . web/config/app.config.json > /dev/null
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json
npx http-server web -p 8080

	•	Test across Chrome, Firefox, Safari.
	•	Verify dark mode, timeline slider, safe-area insets.

⸻

⚡ 9) Performance
	•	Rasters → COGs or prerendered tiles.
	•	GeoJSON ≤ 10 MB → tile if larger.
	•	Batch DOM updates for sidebar & legend.

⸻

🔒 10) Security & Provenance
	•	Attribution is mandatory.
	•	Use HTTPS or relative paths only.
	•	Respect dataset licenses.

⸻


<div align="center">


✅ Following this guide keeps the Kansas-Frontier-Matrix web viewer clean, accessible, and reproducible.

</div>
```
