# Kansas-Frontier-Matrix — Web App Architecture

This document describes the **structure and data flow** of the web viewer (`web/`),  
which complements the **Google Earth (KML/KMZ)** deliverables and the **STAC catalog**.

**Design philosophy:** *minimal dependencies, modular configs, reproducible outputs.*

---

## Overview

The **web app** is a **lightweight MapLibre viewer** featuring:

- **Config-driven rendering** (`app.config.json` + fallbacks)  
- **Historical + terrain overlays** (`tiles/`, `vectors/`, `data/processed/`)  
- **Sidebar UI** for toggles, legend, and opacity  
- **Timeline slider** for time filtering (layer or feature level)  
- **Accessible theming** (light/dark, reduced motion, high-contrast)

---

## Directory Layout

```text
web/
├── index.html          # Entry (loads MapLibre and the viewer module)
├── app.js              # Viewer module (fetch config, build UI, wire timeline)
├── style.css           # Tokens, layout, components, accessibility
├── app.config.json     # Preferred, generated from STAC (see web/config/README.md)
├── config/             # Overrides & fallbacks (viewer.json, layers.json, time_config.json, legend.json)
│   └── README.md
├── tiles/              # Raster tiles (/{z}/{x}/{y}.png or .jpg)
├── vectors/            # GeoJSON overlays (small dev/test sets)
├── data/processed/     # Heavier GeoJSON derived artifacts (ingested via config)
├── assets/             # Logos, favicons, icons
└── docs/               # Developer & contributor documentation
    ├── ARCHITECTURE.md
    ├── STYLE_GUIDE.md
    ├── DEVELOPER_GUIDE.md
    ├── UI_DESIGN.md
    └── README.md

Path rule: Use web-relative paths in configs (e.g., ./tiles/..., ./data/processed/...).
Avoid ../ — it will 404 on GitHub Pages.

⸻

Component Architecture

flowchart TD
  A["Config:\napp.config.json"] --> B["Viewer Logic:\nindex.html / app.js"]
  B --> C["MapLibre Map"]
  B --> D["Sidebar UI\n(layer list · legend · controls)"]
  B --> E["Timeline Control"]
  C --> F["Raster Layers\n(hillshade · topo · imagery)"]
  C --> G["GeoJSON Layers\n(treaties · railroads · hydrology)"]
  D -- "toggles · opacity" --> C
  E -- "year filter" --> C

Key connections
	•	Config-driven load order (first hit wins):
./app.config.json → ./config/app.config.json → ./config/viewer.json → ./config/layers.json → ./layers.json
	•	Legend & categories: optional config/legend.json and config/categories.json drive UI chips/groups via legendKey/category.
	•	Time: layer-level spans via time.start/end, or feature-level via timeProperty (and optional endTimeProperty).
	•	Rasters: tiles only (e.g., …/{z}/{x}/{y}.png). Do not point at raw .tif.

⸻

Runtime Lifecycle (Sequence Diagram)

sequenceDiagram
  autonumber
  participant U as User
  participant H as index.html
  participant A as app.js
  participant L as ConfigLoader
  participant M as MapLibre
  participant UI as Sidebar/Legend
  participant T as Timeline
  participant S as Sources/Layers

  U->>H: Open /web/
  H->>A: load module (app.js)
  A->>L: resolve config (prefer app.config.json)
  alt app.config.json present
    L-->>A: ./app.config.json
  else fallback chain
    L-->>A: ./config/app.config.json → ./config/viewer.json → ./config/layers.json → ./layers.json
  end
  A->>A: normalize (defaults · legend bindings · categories)
  A->>M: init map (style · center · zoom)
  A->>S: register sources (raster tiles / geojson)
  A->>S: add layers (paint/layout · visibility · opacity)
  A->>UI: build sidebar (groups · toggles · sliders)
  A->>UI: build legend (legendKey → legend.json)
  A->>T: init time slider (bounds · defaultYear)

  U->>UI: toggle/opacity
  UI->>S: set visibility/paint
  U->>T: change year
  T->>S: filter by time window (layer.time or feature timeProperty)
  S->>M: update rendered map

  Note over A,M,UI,T: Config-driven; ISO dates; camelCase style keys


⸻

Config Schema (Conceptual)

Actual JSON Schemas live in web/config/*.schema.json.
Keys below mirror the viewer’s expectations (camelCase, ISO dates).

classDiagram
  direction LR

  class AppConfig {
    +version: string
    +title: string
    +subtitle: string
    +style: string
    +center: float[]       // [-98.3, 38.5]
    +zoom: number
    +bounds: float[]       // [W,S,E,N] (optional)
    +time: TimeBounds
    +defaultYear: number
    +timeUI: TimeUI
    +defaults: Defaults
    +layers: Layer[]
  }

  class TimeBounds {
    +min: string           // YYYY-MM-DD
    +max: string           // YYYY-MM-DD
  }

  class TimeUI {
    +step: number
    +loop: boolean
    +fps: number
  }

  class Defaults {
    +minzoom: number
    +maxzoom: number
    +opacity: number
    +visible: boolean
    +bounds: float[]       // optional
    +time: TimeWindow
  }

  class Layer {
    +id: string
    +title: string
    +category: string      // reference|terrain|environment|historical|documents|infrastructure|culture|hazards
    +type: string          // raster|geojson|image|raster-dem
    +url: string           // raster/image tiles
    +data: string          // GeoJSON path (or inline data)
    +opacity: number
    +visible: boolean
    +minzoom: number
    +maxzoom: number
    +legendKey: string
    +attribution: string
    +time: TimeWindow
    +timeProperty: string
    +endTimeProperty: string
    +style: Paint          // camelCase
    +popup: string[]
    +coordinates: float[][] // image overlays (four corners)
  }

  class TimeWindow {
    +start: string | null
    +end: string | null
  }

  class Paint {
    +lineColor: string
    +lineWidth: number
    +lineOpacity: number
    +lineDasharray: number[]
    +fillColor: string
    +fillOpacity: number
    +fillOutlineColor: string
    +circleColor: string
    +circleRadius: number
    +circleOpacity: number
    +circleStrokeColor: string
    +circleStrokeWidth: number
  }

  AppConfig --> TimeBounds : time
  AppConfig --> TimeUI     : timeUI
  AppConfig --> Defaults   : defaults
  AppConfig --> Layer      : layers
  Defaults  --> TimeWindow : time
  Layer     --> TimeWindow : time
  Layer     --> Paint      : style


⸻

Config Resolution (Load Order)

flowchart TD
  A["Try:\n./app.config.json"] -->|if missing| B["Try:\n./config/app.config.json"]
  B -->|if missing| C["Try:\n./config/viewer.json"]
  C -->|if missing| D["Try:\n./config/layers.json"]
  D -->|if missing| E["Try:\n./layers.json (legacy)"]
  A -->|if found| Z["Parse & normalize"]
  B -->|if found| Z
  C -->|if found| Z
  D -->|if found| Z
  E -->|if found| Z
  Z --> M["Init MapLibre + UI\n(basemap · layers · legend · timeline)"]

Optional overrides
	•	config/time_config.json → overrides top-level time, defaultYear, timeUI
	•	config/legend.json / config/categories.json → drive legend chips and sidebar grouping

⸻

Data Flow (Runtime)
	1.	Load config → from preferred file (see load order).
	2.	Normalize layers → ensure id, type, url/data, time, style, category, legendKey.
	3.	Init map → basemap/style, center/zoom, optional bounds.
	4.	Register sources → raster tiles / GeoJSON.
	5.	Add layers → apply style, opacity, default visible.
	6.	Build UI → groups, toggles, opacity sliders, legend.
	7.	Bind timeline → filter by time or timeProperty.
	8.	Interact → UI changes update MapLibre sources/layers in real time.

⸻

CSS & Theming
	•	style.css is authoritative for:
	•	Design tokens (--bg, --text, --accent, --focus-ring, --z-*)
	•	Layout (sidebar widths, safe areas, responsive rules)
	•	Components (buttons, popups, sliders, timeline, legend)
	•	Accessibility (:focus-visible, forced-colors, reduced motion)
	•	Theming (light/dark via prefers-color-scheme or .theme-* classes)

⸻

Extensibility

Add datasets
	1.	Place raster tiles in web/tiles/ or GeoJSON in web/vectors/ / web/data/processed/.
	2.	Add a layers[] entry in app.config.json (raster → url, vector → data).
	3.	Include category, legendKey, attribution.
	4.	Validate JSON (jq) and schema (see Validation).

Add UI panels
	•	Extend app.js sidebar composition (e.g., search, bookmarks, inspectors).
	•	Keep controls modular and keyboard-accessible.

Add themes
	•	Add CSS overrides (e.g., archival/sepia) or rely on system prefers-color-scheme.
	•	Use CSS variables so map styling adapts across themes.

⸻

Validation & Troubleshooting

Local checks

# Serve
cd web && python -m http.server 8080

# Generate from STAC (preferred) and validate
make stac stac-validate site-config

# Lint/validate configs
jq . web/config/app.config.json > /dev/null
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json
ajv validate -s web/config/layers.schema.json      -d web/config/layers.json

Common issues
	•	Blank map / 404s → Wrong relative paths; must be from web/. Avoid file://.
	•	Tiles not rendering → Ensure {z}/{x}/{y}.png exists; don’t reference .tif.
	•	Timeline inert → Provide layer time or feature timeProperty; use ISO dates.
	•	Legend missing → legendKey must match legend.json.symbols (or bind via layerBindings).
	•	Slow vectors → Simplify or tile; keep raw GeoJSON small.

⸻

Roadmap
	•	PMTiles/TiTiler vector/raster tile support for large datasets
	•	Full permalink state (year, center/zoom, layers)
	•	Search/index for treaties, railroads, hydrology features
	•	Mobile drawer gestures and layout refinements
	•	Alternate themes (archival sepia, high-contrast)

⸻

See also
	•	STYLE_GUIDE.md — tokens, controls, schema-lite, CI checks
	•	DEVELOPER_GUIDE.md — config loading, adding layers, debugging
	•	README.md — documentation index and contributor notes

