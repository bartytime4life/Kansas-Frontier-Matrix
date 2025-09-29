# Kansas-Frontier-Matrix — Web Style Guide

This guide defines conventions for CSS, JavaScript, JSON configs, and docs in `web/`.  
Follow it to keep the viewer consistent, accessible, and easy to maintain.

---

## 0) Directory expectations

```text
web/
├─ index.html           # Viewer entry (loads MapLibre + builds sidebar UI)
├─ style.css            # Tokens, layout, components, a11y (single source of truth)
├─ app.config.json      # Primary config (fallbacks allowed; see §3)
├─ config/              # Overrides (viewer.json, layers.json, time_config.json, legend.json)
├─ tiles/               # Raster tiles (/{z}/{x}/{y}.png)
├─ vectors/             # GeoJSON overlays (relative ./vectors/... .geojson)
├─ data/processed/...   # Alt. GeoJSON roots (use ./ relative paths)
└─ docs/
   └─ STYLE_GUIDE.md

Rule: All URLs/paths in configs are web-relative (e.g., ./tiles/..., ./vectors/...).
Avoid ../ — it will 404 on GitHub Pages.

⸻

1) CSS (in style.css)

1.1 Tokens & theming
	•	Define tokens in :root: colors, radii, shadows, z-index, typography, safe areas.
	•	Provide dark mode overrides under @media (prefers-color-scheme: dark).

1.2 Naming & structure
	•	Component classes preferred; IDs only for roots.
	•	BEM-lite with kfm- prefix (e.g., .kfm-legend__row, .is-active).

1.3 Responsiveness & layout
	•	Breakpoint: @media (max-width: 900px) → sidebar becomes bottom drawer.
	•	Use Flex/Grid. Avoid floats.

1.4 Accessibility
	•	Style :focus-visible.
	•	Support prefers-reduced-motion, forced-colors.
	•	Ensure high contrast.
	•	RTL safety with [dir="rtl"].

1.5 Controls
	•	Range sliders: .range--fill, update --value via JS.
	•	Larger touch targets under coarse pointer media query.

⸻

2) JavaScript (in app.js)

2.1 Helpers

const $  = (sel, root = document) => root.querySelector(sel);
const el = (tag, attrs = {}, children = []) => { /* minimal h() */ };

	•	Use const/let, not var.

2.2 Config-driven

Priority:
	1.	./app.config.json
	2.	./config/app.config.json
	3.	./config/viewer.json / ./config/layers.json
	4.	./layers.json (legacy)

2.3 Map & layers
	•	Raster → url, GeoJSON → data.
	•	Styles via camelCase paint keys.
	•	Timeline uses time or timeProperty.
	•	Opacity adjusted live via UI.

2.4 Sidebar & legend
	•	Sidebar = layers[] grouped by category.
	•	Legend built from legend.json via legendKey.

⸻

3) JSON Configs
	•	2-space indent, stable IDs (lower-hyphen).
	•	Minimal top-level shape:

{
  "version": "1.4.0",
  "title": "Kansas-Frontier-Matrix",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "layers": []
}

3.2 Layer schema-lite

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
popup	array	opt	Properties in popup


⸻

4) Documentation (Markdown)
	•	Headings: #, ##, ###
	•	Code fences: always closed, language-hinted
	•	Mermaid diagrams: quote labels + \n for line breaks

Example:

flowchart TD
  A["Config:\napp.config.json"] --> B["Viewer:\nindex.html/app.js"]
  B --> C["MapLibre:\nsources/layers"]
  C --> D["UI:\nsidebar/time slider"]

<!-- END OF MERMAID -->



⸻

5) Accessibility & UX
	•	Keyboard focus visible.
	•	ARIA roles for regions + live status.
	•	Tabular numerals for years.
	•	Respect reduced-motion and forced-colors.

⸻

6) New Layer Recipe
	1.	Put assets in web/vectors/ or web/tiles/.
	2.	Add config entry (with id, title, category, type, url/data).
	3.	Add legendKey if needed.
	4.	Validate JSON (jq, ajv) and preview locally.

⸻

7) Commits

Prefixes: css:, js:, config:, docs:, a11y:, tiles:, vectors:, build:

⸻

8) Validation & CI

jq . web/config/app.config.json > /dev/null
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json
npx http-server web -p 8080

Test across Chrome/Firefox/Safari. Verify dark mode, timeline slider, safe-area insets.

⸻

9) Performance
	•	Rasters → COGs or prerendered tiles.
	•	GeoJSON ≤ 10MB. Tile if larger.
	•	Batch DOM updates for sidebar/legend.

⸻

10) Security & provenance
	•	Attribution mandatory.
	•	HTTPS or relative paths only.
	•	Respect dataset licenses.

⸻

✅ Following this guide keeps the Kansas-Frontier-Matrix web viewer clean, accessible, and reproducible.

---

Would you like me to also make a **`.markdownlint.json` rule pack** just for `web/docs/` so Mermaid blocks always require `<!-- END OF MERMAID -->` after them (to enforce hard stops)?
