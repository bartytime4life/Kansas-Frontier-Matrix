# Kansas-Frontier-Matrix — Web App Architecture

This document describes the **structure and data flow** of the web-based viewer (`web/`),  
which complements the **Google Earth (KML/KMZ)** deliverables and the **STAC catalog**.

---

## Overview

The **web app** is a **lightweight MapLibre viewer** with:

- **Config-driven rendering** (`config/`)
- **Historical + terrain overlays** (`data/`)
- **Sidebar UI** for toggling layers and adjusting opacity
- **Timeline slider** for filtering by temporal attributes
- **Accessible theming** (dark/light, reduced motion, print-safe)

The design philosophy: **minimal dependencies, modular configs, and NASA-grade reproducibility**.

---

## Directory Layout

```

web/
├── app.js            # Main viewer logic
├── css/              # Layout, theme, responsive rules
│   ├── layout.css
│   ├── theme.css
│   └── README.md
├── config/           # Viewer configs (JSON)
│   ├── viewer.json
│   ├── layers.json
│   └── README.md
├── data/             # Demo JSON/GeoJSON entities
│   ├── demo\_entities.json
│   └── README.md
├── docs/             # Documentation
│   └── ARCHITECTURE.md   ← (this file)
├── assets/           # Logos, favicons, icons
└── index.html        # Entry point (loads app.js + configs)

````

---

## Component Architecture

```mermaid
flowchart TD
    A["Config:\nviewer.json"] --> B["App JS:\ninit()"]
    B --> C["MapLibre Map"]
    B --> D["Sidebar UI"]
    B --> E["Timeline Control"]
    C --> F["Raster / Vector Layers"]
    C --> G["GeoJSON Entities"]
    D -- "user toggles" --> B
    E -- "time filter" --> G
````

* **Config-driven:**
  The app looks for configs in this order:
  `config/app.config.json → viewer.json → layers.json` → fallback.

* **MapLibre Map:**
  Handles raster tiles (DEM, overlays), vector tiles, and GeoJSON entities.

* **Sidebar UI:**
  Dynamically built from config and data. Toggles visibility and opacity.

* **Timeline Control:**
  Global slider filtering layers/entities by `[start, end]` attributes.

---

## Data Flow

1. **Configs loaded** → `viewer.json` defines sources/layers.
2. **Entities fetched** → from `web/data/demo_entities.json` (or GeoJSON).
3. **Map initialized** → with basemap + optional DEM derivatives.
4. **UI bound** → sidebar + timeline wired to map layers.
5. **User interactions** → toggle, filter, adjust → updates map in real time.

---

## CSS Layering

* **`layout.css`** = structural grid, sidebar, timeline placement
* **`theme.css`** = skinning (colors, shadows, typography)
* **Optional** `theme-alt.css` = historical/sepia mode

---

## Extensibility

* Add new datasets by:

  * Creating **STAC Items** under `stac/items/`
  * Adding config entries under `web/config/layers.json`
  * Linking provenance + sources
* Add new UI panels by extending `sidebar` rendering in `app.js`.

---

## Roadmap

* [ ] Add **demo\_entities.geojson** for direct MapLibre rendering
* [ ] Extend **time filtering** to raster overlays
* [ ] Implement **search bar** for entities
* [ ] Mobile-first drawer improvements
* [ ] Alternate **themes** (sepia archival view)

---

🚀 This architecture enables a **scalable, reproducible, and interactive viewer**
for Kansas terrain + historical research layers.

```
