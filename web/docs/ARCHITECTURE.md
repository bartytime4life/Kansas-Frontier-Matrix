# Kansas-Frontier-Matrix — Web App Architecture

This document describes the **structure and data flow** of the web-based viewer (`web/`),  
which complements the **Google Earth (KML/KMZ)** deliverables and the **STAC catalog**.

---

## Overview

The **web app** is a **lightweight MapLibre viewer** featuring:

- **Config-driven rendering** (`app.config.json` + fallbacks)
- **Historical + terrain overlays** (`tiles/`, `vectors/`, `data/processed/`)
- **Sidebar UI** for toggling layers and adjusting opacity
- **Timeline slider** for filtering layers by temporal attributes
- **Accessible theming** (dark/light, reduced motion, high-contrast, print-safe)

**Design philosophy:** *minimal dependencies, modular configs, reproducible outputs.*

---

## Directory Layout

```text
web/
├── index.html          # Entry point (loads MapLibre, sidebar, timeline, configs)
├── app.css             # Tokens, layout, components, accessibility
├── app.config.json     # Primary config (preferred by index.html)
├── config/             # Fallback configs (viewer.json, layers.json)
│   └── README.md
├── tiles/              # Raster tiles (/{z}/{x}/{y}.png)
├── vectors/            # GeoJSON overlays (e.g., political, infrastructure)
├── data/processed/     # Processed hydrology & other derived data
├── assets/             # Logos, favicons, icons
└── docs/               # Documentation
    ├── ARCHITECTURE.md ← (this file)
    ├── STYLE_GUIDE.md
    └── README.md

Path rule: All URLs/paths in configs are web-relative (e.g., ./tiles/..., ./vectors/...).
Avoid ../ — it will 404 on GitHub Pages.

⸻

Component Architecture

flowchart TD
    A["Config:\napp.config.json"] --> B["Viewer Logic:\nindex.html/app.js"]
    B --> C["MapLibre Map"]
    B --> D["Sidebar UI (layer list,\nlegend, controls)"]
    B --> E["Timeline Control"]
    C --> F["Raster Layers\n(e.g., hillshade, slope)"]
    C --> G["GeoJSON Layers\n(e.g., treaties, railroads,\nhydrology)"]
    D -- "toggles, opacity" --> C
    E -- "year filter" --> C

Notes
	•	Config-driven: Viewer loads configs in order:
./app.config.json → ./config/app.config.json → ./layers.json
	•	MapLibre: Supports raster tiles, single images, and GeoJSON overlays.
	•	Sidebar: Built dynamically from layers[] in config.
	•	Timeline: Filters by time.start / time.end (year-based).
	•	Legend: Auto-built from optional layer.legend.

⸻

Config Schema

classDiagram
  direction LR

  class AppConfig {
    +string version
    +string title
    +string subtitle
    +string style
    +float[2] center  "[-98.3, 38.5]"
    +number zoom
    +TimeBounds time  "{min,max}"
    +number defaultYear
    +Defaults defaults
    +string[] groups
    +Layer[] layers
  }

  class TimeBounds {
    +string min   "YYYY-MM-DD"
    +string max   "YYYY-MM-DD"
  }

  class Defaults {
    +number minzoom
    +number maxzoom
    +number tileSize
    +boolean visible
    +number opacity
    +float[4] bounds  "[W,S,E,N]"
    +TimeWindow time  "{start,end}"
  }

  class Layer {
    +string id
    +string title
    +string group
    +string type  "raster|geojson|image"
    +string url   "for raster/image"
    +string path  "for geojson"
    +number opacity
    +boolean visible
    +TimeWindow time
    +Paint paint     "geojson only"
    +LegendItem[] legend
    +string attribution
    +number minzoom
    +number maxzoom
    +number tileSize
  }

  class TimeWindow {
    +string start  "YYYY-MM-DD|null"
    +string end    "YYYY-MM-DD|null"
  }

  class Paint {
    +LinePaint line
    +FillPaint fill
    +CirclePaint circle
  }

  class LinePaint {
    +string line-color
    +number line-width
    +number line-opacity
  }

  class FillPaint {
    +string fill-color
    +number fill-opacity
    +string fill-outline-color
  }

  class CirclePaint {
    +string circle-color
    +number circle-radius
    +number circle-opacity
  }

  class LegendItem {
    +string type   "line|fill|circle"
    +string label
    +string color
    +number width     "line only"
    +string outline   "fill only"
    +number radius    "circle only"
  }

  AppConfig --> TimeBounds : "time"
  AppConfig --> Defaults   : "defaults"
  AppConfig --> Layer      : "layers *"
  Defaults  --> TimeWindow : "time"
  Layer     --> TimeWindow : "time"
  Layer     --> Paint      : "paint"
  Layer     --> LegendItem : "legend *"
  Paint     --> LinePaint
  Paint     --> FillPaint
  Paint     --> CirclePaint

Config Load Order

flowchart TD
  A["Try:\n./app.config.json"] -->|if missing| B["Try:\n./config/app.config.json"]
  B -->|if missing| C["Try:\n./layers.json (legacy)"]
  A -->|if found| D["Parse & normalize"]
  B -->|if found| D
  C -->|if found| D
  D --> E["Init MapLibre + UI\n(basemap, layers, legend, timeline)"]


⸻

Data Flow
	1.	Load config → from app.config.json (or fallbacks).
	2.	Normalize layers → ensure id, type, url/path, time, paint, legend.
	3.	Init map → basemap + terrain (hillshade, optional slope, aspect).
	4.	Build UI → grouped layer list, toggles, opacity sliders, legend.
	5.	Bind timeline → year slider sets visibility by time.start/time.end.
	6.	Interact → toggles/opacity/year update MapLibre layers in real time.

⸻

CSS Layering
	•	app.css — single source of truth:
	•	Tokens (--bg, --accent, --shadow, etc.)
	•	Layout (sidebar width, safe areas, mobile drawer)
	•	Components (buttons, sliders, layer list, legend)
	•	Accessibility (focus-visible, reduced motion, forced-colors)
	•	RTL safety & z-index for controls/popups

(Older layout.css / theme.css references are consolidated into app.css.)

⸻

Extensibility

Add datasets
	1.	Place assets in web/tiles/ (raster) or web/vectors/ / web/data/processed/ (GeoJSON).
	2.	Add/update layers[] in app.config.json (use url for raster, path for GeoJSON).
	3.	Include legend and attribution where helpful.
	4.	Validate with jq (syntax) and optional CI tests.

Add UI panels
	•	Extend the sidebar creation in index.html / app.js (e.g., search, bookmarks, inspector).

Add themes
	•	Add CSS overrides (e.g., archival sepia), or rely on prefers-color-scheme.

⸻

Roadmap
	•	Add demo_entities.geojson for styling tests
	•	Extend time filtering to cover more raster cases with open-ended dates
	•	Implement search for treaties, railroads, hydrology features
	•	Improve mobile drawer gestures/resizing
	•	Add alternate themes (archival sepia, night mode)

⸻

See also:
	•	web/docs/STYLE_GUIDE.md — tokens, controls, JSON schema-lite, CI checks
	•	web/docs/README.md — file catalog and contributor notes

