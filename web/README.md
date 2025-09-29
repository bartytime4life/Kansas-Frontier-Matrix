# Kansas Geo Timeline — Web App

**Time · Terrain · History** — a tiny, dependency-light MapLibre viewer with a time slider.  
It prefers a **STAC-derived config** and gracefully falls back to simple JSON (for local dev).  
Designed to run from **`web/`** (GitHub Pages-friendly), no servers required.

---

## What’s in `web/`

```text
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

Produced by make site-config. Minimal shape:

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

Use for quick dev. Same keys, but minimal:

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

Note: Rasters are tile URLs (…/{z}/{x}/{y}.png). Do not point to raw .tif.
Vectors use data for GeoJSON; rasters use url or tiles.

⸻

How layers load
	•	Raster → MapLibre raster source from url/tiles (PNG/JPEG tiles)
	•	GeoJSON → MapLibre geojson source from data (or path)
	•	Styling (camelCase):
	•	Lines: lineColor, lineWidth, lineOpacity, lineDasharray
	•	Fills: fillColor, fillOpacity, fillOutlineColor
	•	Circles: circleColor, circleRadius, circleOpacity, circleStrokeColor, circleStrokeWidth
	•	Legend → auto from layer props or external config/legend.json via legendKey + layerBindings
	•	Time → layer-level (time.start/end) or feature-level (timeProperty, endTimeProperty)

⸻

URL parameters

?year=1930
&layers=ks_hillshade_2018,ksriv_channels
&center=-98.3,38.5
&zoom=7
&debug=1

	•	year → sets slider
	•	layers → initial visibility
	•	center + zoom → map view override
	•	debug=1 → console + overlay diagnostics

⸻

Publishing
	1.	Ensure web/ has a valid config (app.config.json preferred)
	2.	Run make prebuild before pushing (validates + generates configs)
	3.	GitHub Pages: set /web or /site as publish dir
	4.	(Optional) Add .lychee.toml for link checks

base_url = "https://<user>.github.io/<repo>/"
include = ["web/**", "README.md", "site/**"]
fail_if_empty = false


⸻

Troubleshooting
	•	Blank map / 404s → check devtools console, paths must be relative to web/
	•	Tiles don’t render → confirm {z}/{x}/{y}.png tiles exist
	•	Slider inert → missing time/timeProperty
	•	Legend missing → legendKey not bound in legend.json
	•	Slow vectors → simplify or tile; use raw GeoJSON only for small sets

⸻

Roadmap (web)
	•	Vector tiles (PMTiles/TiTiler)
	•	Permalinks (year + layers + view state)
	•	Story mode (config/story_layers.json)
	•	I18n scaffolding for UI strings

⸻

License: MIT (see repo root)
Issues / ideas: open a GitHub issue

---
