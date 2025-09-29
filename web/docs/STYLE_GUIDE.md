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
	•	Define design tokens in :root:
	•	Colors: --bg, --bg-soft, --panel, --border, --text, --muted, --accent, --accent-2, --danger
	•	Radii/Shadows: --radius, --radius-sm, --radius-xs, --shadow, --shadow-1, --shadow-2
	•	Layout: --sidebar-w, z-stack tokens (--z-map, --z-sidebar, --z-overlay, --z-modal)
	•	Typography: --font, --fs-12, --fs-13, --fs-15, --fs-16
	•	Effects: --focus-ring, safe areas (--safe-*)
	•	Provide dark mode overrides under @media (prefers-color-scheme: dark).

1.2 Naming & structure
	•	Prefer component classes over IDs except for roots: #map, #sidebar, #timeline.
	•	Use a light BEM-like convention with kfm- prefix:
	•	.kfm-legend, .kfm-legend__row, modifiers like .is-active, .is-open.

1.3 Responsiveness & layout
	•	Breakpoint: @media (max-width: 900px) → sidebar becomes a bottom drawer.
	•	Use CSS Grid/Flex; avoid floats.
	•	Sidebar widths: desktop 280px, mobile 220px (--sidebar-w token).

1.4 Accessibility
	•	Always style :focus-visible.
	•	Support:
	•	@media (prefers-reduced-motion: reduce)
	•	@media (forced-colors: active)
	•	Ensure high-contrast readability (--border, --focus-ring overrides).
	•	Include RTL safety ([dir="rtl"] adjustments).

1.5 Controls
	•	Range inputs:
	•	Use .range--fill and set --value (0–100%) via JS for track fill.
	•	Increase touch targets under @media (pointer: coarse).

⸻

2) JavaScript (in app.js)

2.1 Structure & helpers
	•	Wrap in an IIFE or ES module scope.
	•	Helpers:

const $  = (sel, root = document) => root.querySelector(sel);
const el = (tag, attrs = {}, children = []) => { /* minimal h() */ };

	•	Use const/let, never var.

2.2 Config-driven viewer
	•	Load config with priority:
	1.	./app.config.json
	2.	./config/app.config.json
	3.	./config/viewer.json / ./config/layers.json
	4.	./layers.json (legacy)
	•	Do not hardcode layer IDs beyond root UI wiring.

2.3 Map & layers
	•	MapLibre sources derive from each layer object:
	•	Raster → url/tiles
	•	GeoJSON → data
	•	Image → coordinates
	•	Style with camelCase paint keys (lineColor, fillColor, etc.).
	•	Time filtering:
	•	Layer spans: layer.time.start / layer.time.end
	•	Feature spans: timeProperty / endTimeProperty
	•	Opacity:
	•	Raster: raster-opacity
	•	GeoJSON: multiply base opacity by UI slider

2.4 Sidebar & legend
	•	Sidebar built from config.layers, grouped by category (categories.json defines order/labels).
	•	Legend chips are auto-built from legend.json (legendKey → symbol).

⸻

3) JSON Configs

3.1 Formatting & metadata
	•	Indent with 2 spaces.
	•	IDs: lowercase, hyphen-separated ("id": "usgs-1894-larned").
	•	Stable IDs for existing layers; new ones follow pattern.

Minimal top-level keys:

{
  "version": "1.4.0",
  "title": "Kansas-Frontier-Matrix",
  "subtitle": "Time-aware historical GIS for Kansas",
  "style": "https://demotiles.maplibre.org/style.json",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "defaults": { "visible": true, "opacity": 1.0 },
  "layers": []
}

3.2 Layer contract (schema-lite)

Key	Type	Req	Notes
id	string	✅	Unique. Lowercase with hyphens.
title	string	✅	Human label.
category	string	✅	Must match categories.json.
type	string	✅	raster / geojson / image / raster-dem.
url	string	opt	Raster/image tiles.
data	string	opt	GeoJSON file path.
opacity	number	opt	0–1 (default defaults.opacity).
visible	boolean	opt	Default defaults.visible.
time	object	opt	{ "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" }.
timeProperty	string	opt	Feature-level property for start.
endTimeProperty	string	opt	Feature-level property for end.
style	object	opt	See §3.3 (GeoJSON styling).
legendKey	string	opt	Symbol key in legend.json.
attribution	string	opt	Data source/license.
popup	array	opt	Properties to show in popups.

3.3 GeoJSON paint keys

"style": {
  "lineColor": "#d97706",
  "lineWidth": 1.6,
  "lineOpacity": 0.95,
  "fillColor": "#2563eb",
  "fillOpacity": 0.25,
  "fillOutlineColor": "#1d4ed8",
  "circleColor": "#0d47a1",
  "circleRadius": 4,
  "circleOpacity": 1.0,
  "circleStrokeColor": "#FFFFFF",
  "circleStrokeWidth": 1
}

3.4 Legend (external file)

Example legend.json:

{
  "symbols": {
    "railroads": { "line": true, "preview": "#d97706" }
  },
  "layerBindings": {
    "railroads_1900": "railroads"
  }
}


⸻

4) Documentation (Markdown)
	•	Headings: #, ##, ###.
	•	Code fences: always closed, language-hinted (bash, json, js, html, mermaid).
	•	Mermaid: quote labels, use \n for line breaks.

Example:

flowchart TD
  A["Config:\napp.config.json"] --> B["Viewer:\nindex.html/app.js"]
  B --> C["MapLibre:\nsources/layers"]
  C --> D["UI:\nsidebar/time slider"]


⸻

5) Accessibility & UX checklist
	•	Keyboard: all interactive controls are focusable, :focus-visible styled.
	•	ARIA: landmark roles (role="region"), labels (aria-label), status updates (role="status").
	•	Visuals: tabular numerals for year readouts, test light/dark/print.
	•	Motion/contrast: respect prefers-reduced-motion, forced-colors.

⸻

6) Adding a new layer (recipe)
	1.	Put assets in repo (GeoJSON → web/vectors/..., raster tiles → web/tiles/...).
	2.	Add config entry:

{
  "id": "usgs-1902-topeka",
  "title": "USGS Historic Topo — Topeka (1902)",
  "category": "historical",
  "type": "raster",
  "url": "./tiles/historic/usgs_1902_topeka/{z}/{x}/{y}.png",
  "opacity": 0.75,
  "visible": false,
  "time": { "start": "1902-01-01", "end": "1902-12-31" },
  "attribution": "USGS Historical Topographic Maps (Public Domain)"
}

	3.	Add legendKey/legend if needed.
	4.	Validate JSON and preview locally.

⸻

7) Commit guidelines
	•	Prefix commits: css:, js:, config:, docs:, tiles:, vectors:, a11y:, build:
	•	Examples:
	•	css: polish range slider fill + focus-visible ring
	•	js: add legend builder and grouped layer list
	•	config: switch hydrology paths to ./data/processed/
	•	docs: expand STYLE_GUIDE with schema-lite and CI checks

⸻

8) Validation & CI tips
	•	Syntax check:

jq . web/config/app.config.json > /dev/null

	•	Schema validation:

ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json

	•	Local serve:

npx http-server web -p 8080

	•	Cross-browser smoke test:
	•	Toggle layers, adjust opacity, test timeline slider.
	•	Dark/light mode legibility.
	•	Mobile safe areas (iOS notch, Android).

⸻

9) Performance
	•	Heavy rasters → use COG or prerendered tiles.
	•	GeoJSON ≤ 5–10 MB in production; use vector tiles for larger.
	•	Avoid DOM thrash; batch updates when redrawing UI.

⸻

10) Security & provenance
	•	Attribution is mandatory for each dataset.
	•	Only use HTTPS or relative URLs.
	•	Verify license compatibility for third-party tiles.

⸻

✅ Following this guide ensures Kansas-Frontier-Matrix stays consistent, accessible, and reproducible across configs, UI, and docs.

