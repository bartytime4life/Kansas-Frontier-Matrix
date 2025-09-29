Kansas Geo Timeline — Web App

Time · Terrain · History — a tiny, dependency-light MapLibre viewer with a time slider.
It prefers a STAC-derived config and gracefully falls back to simple JSON (for local dev).
Designed to run from web/ (GitHub Pages-friendly), no servers required.

⸻

What’s in web/

web/
├─ index.html              # MapLibre bootstrap + UI (loads config JSON, builds UI)
├─ style.css               # Tokens, layout, legend, toggles, accessibility
├─ app.config.json         # (preferred) generated from STAC (see “Build & Generate”)
├─ layers.json             # (fallback) quick dev/preview catalog
├─ config/                 # optional UI/config overrides (all are optional)
│  ├─ app.config.json      # alt location for generated config (same shape as /app.config.json)
│  ├─ viewer.json          # dev override (super-set of app.config.json)
│  ├─ layers.json          # layers-only dev override (subset)
│  ├─ time_config.json     # overrides { time, defaultYear, timeUI } + adds presets
│  ├─ legend.json          # symbol tokens + layerBindings (id→legendKey)
│  ├─ categories.json      # sidebar groups (id→{ label, order })
│  └─ schema.json          # JSON Schemas (legend/categories/sources) for validation
└─ assets/
   ├─ logo.png
   └─ favicon.svg

Runtime load order (first hit wins):
./app.config.json → ./config/app.config.json → ./config/viewer.json → ./config/layers.json → ./layers.json
If ./config/time_config.json exists it overrides top-level time, defaultYear, and timeUI.

⸻

Quick start

A) One-liner (Python)

cd web
python -m http.server 8080
# open http://localhost:8080

B) Docker (compose profile)

# from repo root
docker compose --profile dev up -d site
# open http://localhost:8080


⸻

Build & Generate (data + configs)

From the repo root (see Makefile targets):

# Discover tools/env
make env

# Produce terrain derivatives (COGs → tiles)
make terrain

# Fallback manifest at web/layers.json
make site

# Preferred: STAC → web/config/app.config.json (+ sync UI assets)
make stac stac-validate site-config

Optional DEM override while building terrain:

make terrain DEM=/path/to/dem.tif


⸻

Configs the web app understands

1) STAC-driven (preferred) — app.config.json

Typically produced by make site-config. Minimal shape:

{
  "version": "1.4.0",
  "title": "Kansas-Frontier-Matrix",
  "style": "https://demotiles.maplibre.org/style.json",
  "center": [-98.3, 38.5],
  "zoom": 6,
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "defaultYear": 1930,
  "timeUI": { "step": 1, "loop": false, "fps": 12 },
  "defaults": {
    "minzoom": 0, "maxzoom": 15, "opacity": 1.0, "visible": true,
    "time": { "start": null, "end": null }
  },
  "layers": [
    {
      "id": "usgs_topo_1894_larned",
      "title": "USGS Historic Topo — Larned (1894)",
      "type": "raster",
      "url": "./tiles/historic/usgs_1894_larned/{z}/{x}/{y}.png",
      "opacity": 0.7,
      "visible": true,
      "category": "historical",
      "legendKey": "historic_topo",
      "time": { "start": "1894-01-01", "end": "1894-12-31" }
    },
    {
      "id": "ks_settlements",
      "title": "Settlements, Forts, Trading Posts",
      "type": "geojson",
      "data": "data/processed/towns_points.json",
      "category": "culture",
      "legendKey": "towns",
      "time": { "start": "1800-01-01", "end": null },
      "timeProperty": "year",
      "style": {
        "circleColor": "#FF595E",
        "circleRadius": 4,
        "circleOpacity": 0.95,
        "circleStrokeColor": "#FFFFFF",
        "circleStrokeWidth": 1
      },
      "popup": ["name", "type", "year", "year_end"]
    }
  ]
}

2) Fallback — viewer.json / layers.json

Use for quick dev. Same keys, but you can be minimal:

{
  "version": "1.3.0",
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "layers": [
    {
      "id": "ks_hillshade_2018",
      "title": "Hillshade (2018–2020)",
      "type": "raster",
      "url": "./tiles/terrain/hillshade/{z}/{x}/{y}.png",
      "opacity": 0.9,
      "visible": true,
      "time": { "start": "2018-01-01", "end": "2020-12-31" }
    },
    {
      "id": "ksriv_channels",
      "title": "Kansas River — Channels",
      "type": "geojson",
      "data": "./data/processed/hydrology/kansas_river/channels.geojson",
      "style": { "lineColor": "#1e88e5", "lineWidth": 1.6, "lineOpacity": 1.0 },
      "visible": true,
      "time": { "start": "1850-01-01", "end": null }
    }
  ]
}

Note: Rasters are tile URLs (…/{z}/{x}/{y}.png). Do not point to raw .tif here.
Vectors use data for GeoJSON; rasters use url or tiles.

⸻

How layers load (at runtime)
	•	Raster → MapLibre raster source from url/tiles (PNG/JPEG tiles).
	•	GeoJSON → MapLibre geojson source from data (or path alias).
	•	Styling (camelCase keys):
	•	Lines: lineColor, lineWidth, lineOpacity, lineDasharray
	•	Fills: fillColor, fillOpacity, fillOutlineColor
	•	Circles: circleColor, circleRadius, circleOpacity, circleStrokeColor, circleStrokeWidth
	•	Legend → auto from layer props or external config/legend.json via legendKey + layerBindings.
	•	Time → either layer‐level (time.start/end) or feature-level (timeProperty, optional endTimeProperty).
Feature-level filtering applies when the layer’s data has per-feature year/date values.
	•	Categories → sidebar groups controlled by config/categories.json.

⸻

URL permalinks & debug options

The viewer accepts simple URL params (all optional):

?year=1930
&layers=ks_hillshade_2018,ksriv_channels
&center=-98.3,38.5
&zoom=7
&debug=1

	•	year sets the time slider.
	•	layers toggles default visibility (comma-separated layer ids).
	•	center and zoom override map initial view.
	•	debug=1 shows layer ids + console diagnostics.

⸻

Accessibility & UX
	•	Keyboard-navigable controls, focus-visible, large hit targets.
	•	System color-scheme aware; ensure contrast in style.css.
	•	Timeline control supports arrow keys (←/→ by year; hold Shift for larger steps if configured).
	•	Popups present meaningful labels; avoid color-only encodings in legends.

⸻

Conventions & schema hints
	•	IDs: snake_case, stable, include vintage when useful (usgs_topo_1894_larned).
	•	Categories (one per layer):
reference, terrain, environment, historical, documents, infrastructure, culture, hazards.
	•	CRS: serve tiles/GeoJSON in EPSG:3857/4326; raw COGs live outside web/ (built into tiles).
	•	Validation: use web/config/schema.json + repo CI to validate changes before publish.

⸻

Publishing (GitHub Pages or static host)
	1.	Ensure web/ has a valid config (app.config.json preferred, or /config/viewer.json / /layers.json).
	2.	CI: run make prebuild to validate STAC + render configs.
	3.	Configure Pages to serve /web (or a build artifact directory).
	4.	(Optional) Link check with a simple .lychee.toml:

base_url = "https://<user>.github.io/<repo>/"
include = ["web/**", "README.md", "site/**"]
fail_if_empty = false


⸻

Troubleshooting
	•	Blank map / 404s → Check devtools console. Paths must be relative to web/. Serve via HTTP, not file://.
	•	Tiles don’t render → Confirm tile path pattern and actual tile existence (…/{z}/{x}/{y}.png).
	•	Slider seems inert → You need either:
	•	top-level time bounds, and layer-level time, or
	•	per-feature properties timeProperty (and optional endTimeProperty) + top-level time.
	•	Legend chip missing → legendKey must match config/legend.json.symbols and be bound in layerBindings.
	•	Slow GeoJSON → Simplify or tile; use raw GeoJSON only for small sets (dev/test).
	•	Mixed content → If hosting over HTTPS, ensure all sources are also HTTPS.

⸻

CI hooks (brief)
	•	Schemas: JSON validation of app.config.json, viewer.json, legend.json, categories.json.
	•	STAC: make stac-validate to keep STAC-→viewer sync consistent.
	•	Prebuild: make prebuild to generate/update app.config.json and ensure linkability.

⸻

Roadmap (web)
	•	Vector tiles (PMTiles/TiTiler) for large layers.
	•	Permalinks with full state (year, center/zoom, active layers).
	•	“Story mode” presets (timeline + layer recipes) for guided narratives.
	•	Light i18n scaffolding for UI strings.
	•	Optional hash-based cache-busting for config updates.

⸻

License

MIT (see repo root). Open a GitHub issue for questions or ideas.
