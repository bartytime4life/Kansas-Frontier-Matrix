
<div align="center">

# 🌐 Kansas Geo Timeline — Web App  
### **Time · Terrain · History**

A **dependency-light MapLibre viewer** with a time slider.  
It prefers a **STAC-derived config** and gracefully falls back to JSON for dev/preview.  
Runs directly from **`web/`** — Pages-ready, no servers required.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml)

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg?logo=python)
![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix)
![Last Commit](https://img.shields.io/github/last-commit/bartytime4life/Kansas-Frontier-Matrix)
![Repo Size](https://img.shields.io/github/repo-size/bartytime4life/Kansas-Frontier-Matrix)
![Stars](https://img.shields.io/github/stars/bartytime4life/Kansas-Frontier-Matrix?style=social)

</div>

---

## 📦 What’s in `web/`

```text
web/
├─ index.html              # MapLibre bootstrap + UI
├─ style.css               # Tokens, layout, legend, toggles, accessibility
├─ app.config.json         # (preferred) generated from STAC
├─ layers.json             # (fallback) dev/preview catalog
├─ config/                 # optional overrides
│  ├─ app.config.json      # alt generated config
│  ├─ viewer.json          # dev override (superset)
│  ├─ layers.json          # layers-only override
│  ├─ time_config.json     # time overrides + presets
│  ├─ legend.json          # symbol tokens + layer bindings
│  ├─ categories.json      # sidebar groups
│  └─ schema.json          # JSON Schemas for validation
└─ assets/
   ├─ logo.png
   └─ favicon.svg

Runtime load order (first hit wins):
./app.config.json → ./config/app.config.json → ./config/viewer.json → ./config/layers.json → ./layers.json
If ./config/time_config.json exists, it overrides { time, defaultYear, timeUI }.

⸻

⚡ Quick Start

A) One-liner (Python)

cd web
python -m http.server 8080
# open http://localhost:8080

B) Docker (compose profile)

# from repo root
docker compose --profile dev up -d site
# open http://localhost:8080


⸻

🛠 Build & Generate (data + configs)

From repo root (Makefile targets):

# Discover tools/env
make env

# Produce terrain derivatives (COGs → tiles)
make terrain

# Fallback manifest at web/layers.json
make site

# Preferred: STAC → web/config/app.config.json (+ sync UI assets)
make stac stac-validate site-config

Optional DEM override:

make terrain DEM=/path/to/dem.tif


⸻

📑 Configs the Web App Understands

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
  "layers": [...]
}

2) Fallback — viewer.json / layers.json

For quick dev. Same keys, minimal:

{
  "version": "1.3.0",
  "time": { "min": "1850-01-01", "max": "2025-12-31" },
  "layers": [...]
}


⸻

🧩 Layer Handling
	•	Raster → MapLibre raster source from url/tiles
	•	GeoJSON → MapLibre geojson source from data
	•	Styling → lineColor, fillColor, circleColor, etc.
	•	Legend → from props or bound via legend.json
	•	Time → time.start/end or feature-level timeProperty

⸻

📊 Coverage Status (Web Viewer)

<!-- WEB_COVERAGE_START -->


Layer Type / Domain	Example Source	Web Support
🏔 DEM / Terrain	USGS LiDAR → hillshade tiles	
🗺 Historic Topos	USGS Historic Topo maps	
🌊 Hydrology	Kansas River channels (GeoJSON)	
🌱 Land Cover	NLCD slices (vectorized / COG)	
🧭 Soils / Parcels	NRCS SSURGO (vector, simplified)	
🪶 Treaties & Lands	Boundary polygons (GeoJSON)	
🚂 Railroads & Trails	1850–1920 GIS (line GeoJSON)	
🌡 Climate Normals	NOAA NCEI 1991–2020 (station points)	
🌪 Hazards — Tornado	SPC Tornado Paths (polylines)	
🌊 Hazards — Floods	FEMA / USGS flood zones	
🔥 Hazards — Wildfire	NIFC perimeters	
🪶 Oral Histories & Arch.	Tribal narratives (points)	

<!-- WEB_COVERAGE_END -->


Legend:

 Complete ·

 Partial ·

 Planned

⸻

🔗 URL Parameters

?year=1930
&layers=ks_hillshade_2018,ksriv_channels
&center=-98.3,38.5
&zoom=7
&debug=1


⸻

🚀 Publishing
	1.	Ensure web/ has a valid config (app.config.json preferred).
	2.	Run make prebuild before pushing.
	3.	GitHub Pages → set /web or /site as publish dir.
	4.	(Optional) Add .lychee.toml for link checks:

base_url = "https://<user>.github.io/<repo>/"
include = ["web/**", "README.md", "site/**"]
fail_if_empty = false


⸻

🧯 Troubleshooting
	•	Blank map / 404s → check console, paths must be relative to web/
	•	Tiles don’t render → confirm {z}/{x}/{y}.png exist
	•	Slider inert → missing time/timeProperty
	•	Legend missing → legendKey not bound in legend.json
	•	Slow vectors → simplify/tile; raw GeoJSON only for small sets

⸻

🎯 Roadmap (Web)
	•	Vector tiles (PMTiles / TiTiler)
	•	Permalinks (year + layers + view state)
	•	Story mode (config/story_layers.json)
	•	I18n scaffolding for UI strings

⸻

⚖️ License

MIT © 2025 — Kansas Frontier Matrix

💡 Issues & ideas → open a GitHub issue

---

### 🔑 What’s included
- ✅ Color-coded **support badges** (green = complete, yellow = partial, grey = planned).  
- ✅ **Markers (`WEB_COVERAGE_START/END`)** for auto-updating via CI.  
- ✅ Aligned with **root README.md** + `.github/README.md`.  
- ✅ Sections polished for GitHub rendering.  

---
