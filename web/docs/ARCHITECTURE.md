<div align="center">

# 🌐 Kansas-Frontier-Matrix — Web App Architecture (`web/`)

**Mission:** Deliver a **lightweight, config-driven MapLibre viewer** that integrates  
Kansas’s geospatial history into an interactive **timeline + map interface**,  
mirroring Google Earth deliverables and STAC catalogs.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📖 Overview

The **web app** is a modular MapLibre-based viewer with:

- **Config-driven rendering** (`app.config.json` + fallbacks)  
- **Historical & terrain overlays** (tiles, vectors, processed datasets)  
- **Sidebar UI** (layer toggles, legends, opacity sliders)  
- **Timeline slider** (filter features by year or interval)  
- **Accessible theming** (light/dark, reduced motion, high contrast)

> 🔑 **Design principle:** *Minimal dependencies, modular configs, reproducible outputs.*

---

## 📂 Directory Layout

```text
web/
├── index.html          # Entry point (bootstraps viewer)
├── app.js              # Core module (config load, map init, UI wiring)
├── style.css           # Design tokens, responsive layout, accessibility
├── app.config.json     # Preferred config (auto-generated from STAC)
├── config/             # Overrides & fallbacks (viewer.json, layers.json, legend.json, etc.)
│   └── README.md
├── tiles/              # Raster tiles (/{z}/{x}/{y}.png or .jpg)
├── vectors/            # Vector overlays (GeoJSON for dev/testing)
├── data/processed/     # Derived GeoJSON (heavier artifacts linked via config)
├── assets/             # Logos, icons, favicons
└── docs/               # Contributor documentation
    ├── ARCHITECTURE.md
    ├── STYLE_GUIDE.md
    ├── DEVELOPER_GUIDE.md
    ├── UI_DESIGN.md
    └── README.md

👉 Rule: Use ./relative/paths in configs. Avoid ../ (breaks GitHub Pages).

⸻

🏗 Component Architecture

flowchart TD
  A["Config:\napp.config.json"] --> B["Viewer Logic:\nindex.html / app.js"]
  B --> C["MapLibre Map"]
  B --> D["Sidebar UI\n(layer list · legend · controls)"]
  B --> E["Timeline Control"]

  C --> F["Raster Layers\n(hillshade · topo · imagery)"]
  C --> G["GeoJSON Layers\n(treaties · railroads · hydrology)"]

  D -- "toggles · opacity" --> C
  E -- "year filter" --> C


⸻

🔄 Runtime Lifecycle (Sequence)

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
  H->>A: Load module (app.js)
  A->>L: Resolve config
  alt Preferred config
    L-->>A: ./app.config.json
  else Fallback chain
    L-->>A: ./config/app.config.json → viewer.json → layers.json
  end
  A->>M: Init map
  A->>S: Register sources
  A->>S: Add layers
  A->>UI: Build sidebar + legend
  A->>T: Init timeline

  U->>UI: Toggle/opacity
  UI->>S: Update map
  U->>T: Move year slider
  T->>S: Apply time filter
  S->>M: Re-render map


⸻

📜 Config Resolution (Load Order)

flowchart TD
  A["Try: ./app.config.json"] -->|if missing| B["Try: ./config/app.config.json"]
  B -->|if missing| C["Try: ./config/viewer.json"]
  C -->|if missing| D["Try: ./config/layers.json"]
  D -->|if missing| E["Try: ./layers.json (legacy)"]

  A -->|if found| Z["Parse & normalize"]
  B -->|if found| Z
  C -->|if found| Z
  D -->|if found| Z
  E -->|if found| Z

  Z --> M["Init MapLibre + UI\n(basemap · layers · legend · timeline)"]

Overrides
	•	config/time_config.json → time bounds & slider settings
	•	config/legend.json / config/categories.json → legend chips & sidebar grouping

⸻

🎨 CSS & Theming
	•	Tokens: --bg, --text, --accent, --focus-ring, --z-*
	•	Components: sidebar, buttons, timeline slider, legend
	•	Accessibility: :focus-visible, forced-colors, prefers-reduced-motion
	•	Themes: light/dark (system or .theme-* overrides)

⸻

➕ Extensibility
	•	Add datasets:
	1.	Place files in web/tiles/, web/vectors/, or web/data/processed/
	2.	Update app.config.json (id, type, url/data, category, legendKey, attribution)
	3.	Validate JSON (jq + schema)
	•	Add UI panels: Extend app.js modular sidebar builder (keep keyboard accessible).
	•	Add themes: Add CSS overrides or sepia/high-contrast modes.

⸻

🛠 Validation & Troubleshooting

# Local server
cd web && python -m http.server 8080

# Generate configs & validate
make stac stac-validate site-config

# JSON schema lint
jq . web/config/app.config.json > /dev/null
ajv validate -s web/config/app.config.schema.json -d web/config/app.config.json

Common issues
	•	Blank map → wrong relative paths (avoid file://)
	•	Tiles missing → must be {z}/{x}/{y}.png, not .tif
	•	Timeline inert → missing time or timeProperty keys
	•	Legend missing → legendKey must match legend.json

⸻

🗺 Roadmap
	•	PMTiles/TiTiler support for large vector/raster datasets
	•	Full permalink state (year, zoom, layers)
	•	Treaty/railroad/hydrology search & index
	•	Mobile drawer UI + gesture controls
	•	Alternate themes (sepia archival, high contrast)

⸻

📎 See Also
	•	STYLE_GUIDE.md — tokens, controls, schema-lite
	•	DEVELOPER_GUIDE.md — config loading, debugging
	•	README.md — doc index & contributor notes

⸻

📑 Appendix: Conceptual Schema

⚠️ Reference only — actual JSON Schemas live in web/config/*.schema.json.

classDiagram
  direction LR

  class AppConfig {
    +version: string
    +title: string
    +subtitle: string
    +style: string
    +center: float[]
    +zoom: number
    +bounds: float[]
    +time: TimeBounds
    +defaultYear: number
    +timeUI: TimeUI
    +defaults: Defaults
    +layers: Layer[]
  }

  class TimeBounds {
    +min: string
    +max: string
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
    +bounds: float[]
    +time: TimeWindow
  }

  class Layer {
    +id: string
    +title: string
    +category: string
    +type: string
    +url: string
    +data: string
    +opacity: number
    +visible: boolean
    +minzoom: number
    +maxzoom: number
    +legendKey: string
    +attribution: string
    +time: TimeWindow
    +timeProperty: string
    +endTimeProperty: string
    +style: Paint
    +popup: string[]
    +coordinates: float[][]
  }

  class TimeWindow {
    +start: string
    +end: string
  }

  class Paint {
    +lineColor: string
    +lineWidth: number
    +fillColor: string
    +fillOpacity: number
    +circleColor: string
    +circleRadius: number
    +circleOpacity: number
  }

  AppConfig --> TimeBounds
  AppConfig --> TimeUI
  AppConfig --> Defaults
  AppConfig --> Layer
  Defaults --> TimeWindow
  Layer --> TimeWindow
  Layer --> Paint

