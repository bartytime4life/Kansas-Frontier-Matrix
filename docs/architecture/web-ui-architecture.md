<div align="center">

# 🌐 Kansas Frontier Matrix — Web UI Architecture  
`docs/architecture/web-ui-architecture.md`

**Mission:** Define the **frontend and visualization architecture** of the Kansas Frontier Matrix (KFM) —  
explaining how map layers, timelines, datasets, and metadata integrate within the  
web interface to deliver an interactive, provenance-aware exploration of Kansas history, science, and geography.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)

</div>

---

## 📚 Overview

The **Kansas Frontier Matrix Web UI** is a **MapLibre-based, STAC-powered visualization layer**  
that connects processed data, metadata, and temporal filters into an interactive public interface.

It combines:
- 🗺️ **MapLibre GL JS** for rendering raster/vector tiles  
- 🧭 **STAC JSON metadata** for dynamic layer configuration  
- 📆 **Timeline + temporal filtering** for time-aware visualization  
- 🧠 **Semantic metadata integration** for provenance-aware pop-ups  
- ⚙️ **Static site generation (SSG)** via GitHub Actions  

Every element in the UI adheres to **MCP documentation-first principles** and references datasets via **STAC Items** and **data/tiles/** assets.

---

## 🏗️ High-Level Web UI Architecture

```mermaid
graph TD
  A["🧩 STAC Metadata\n(data/stac/)"] --> B["🗺️ Tile Layers\n(data/tiles/)"]
  B --> C["🌐 Web Configs\n(web/config/layers.json)"]
  C --> D["🧭 MapLibre GL Viewer\n(web/index.html, app.js)"]
  D --> E["🧠 User Interaction\n(Map, Timeline, Search)"]
  E --> F["📈 Visual Analytics & Provenance Pop-ups"]

  style A fill:#fffbea,stroke:#e8a500
  style B fill:#eef8ff,stroke:#0077cc
  style C fill:#f5f5f5,stroke:#888
  style D fill:#ecf9f0,stroke:#22aa44
  style E fill:#f0e8ff,stroke:#8844cc
  style F fill:#f7f7f7,stroke:#555
````

<!-- END OF MERMAID -->

---

## 🧩 Web Directory Structure

```bash
web/
├── index.html                # Root HTML file for the MapLibre web viewer
├── app.js                    # Main application logic for UI interactivity
├── style.css                 # Base UI styling and theme tokens
├── config/
│   ├── layers.json           # Layer definitions and display order
│   ├── categories.json       # Domain grouping (terrain, hydrology, etc.)
│   ├── time_config.json      # Timeline and animation settings
│   ├── legend.json           # Color ramps, layer symbology, and labels
│   └── viewer.json           # Global app configuration and theme
└── assets/
    ├── icons/                # UI and map icons
    ├── images/               # Thumbnails and reference images
    └── logos/                # Branding and institutional logos
```

> Each configuration file is JSON-based and **STAC-compatible**,
> ensuring synchronization with `data/stac/` metadata and CI/CD validation.

---

## ⚙️ Key Components

| Component        | Path                          | Description                                               |
| :--------------- | :---------------------------- | :-------------------------------------------------------- |
| **Map Viewer**   | `web/index.html`              | Core entry point loading MapLibre GL JS and UI assets.    |
| **App Logic**    | `web/app.js`                  | Manages layer toggles, time slider, pop-ups, and events.  |
| **Layer Config** | `web/config/layers.json`      | Defines visible datasets, categories, and default styles. |
| **Timeline**     | `web/config/time_config.json` | Controls animation speed, timeline bounds, and FPS.       |
| **Legend**       | `web/config/legend.json`      | Defines color ramps, symbols, and classification labels.  |
| **Theme**        | `web/style.css`               | Implements global UI theme (dark/light modes).            |

---

## 🧱 Layer Configuration Model

Each dataset visible in the UI is defined as a **layer object** in `web/config/layers.json`
and linked directly to a **STAC Item** under `data/stac/`.

### Example Layer Definition

```json
{
  "id": "terrain-hillshade",
  "type": "raster",
  "title": "Kansas Hillshade (1m, 2020)",
  "category": "Terrain",
  "source": {
    "type": "raster",
    "tiles": ["data/tiles/terrain/ks_hillshade/{z}/{x}/{y}.png"],
    "tileSize": 256
  },
  "paint": {"raster-opacity": 0.8},
  "metadata": "data/stac/terrain/ks_hillshade_2018_2020.json",
  "legend": "web/config/legend.json"
}
```

> **Note:**
> This architecture allows **dynamic UI updates** whenever datasets or metadata are updated in STAC —
> no hardcoded map layers are required.

---

## 🧭 Timeline Architecture

The KFM timeline system links temporal metadata in STAC Items to
time-aware visualization filters in the web UI.

| Element                   | File                             | Description                                            |
| :------------------------ | :------------------------------- | :----------------------------------------------------- |
| **Time Config**           | `web/config/time_config.json`    | Sets animation speed, playback modes, and time bounds. |
| **STAC `datetime` Field** | `data/stac/<domain>/<item>.json` | Defines dataset temporal extent.                       |
| **UI Slider**             | `web/app.js`                     | Syncs map layer visibility with selected timestamp.    |
| **CI Validation**         | `stac-validate.yml`              | Ensures correct `datetime` metadata values.            |

The system enables animation or stepping through datasets across historical periods (e.g., landcover change, flood events).

---

## 🧾 Provenance Integration

Each pop-up and info panel within the UI draws its metadata from the linked STAC item.

### Example Pop-Up Template

```html
<h3>{{title}}</h3>
<p><strong>Source:</strong> {{provider}}</p>
<p><strong>Date:</strong> {{datetime}}</p>
<p><strong>Description:</strong> {{description}}</p>
<a href="{{stac_href}}" target="_blank">View Full Metadata</a>
```

Pop-ups render dynamically using data fields defined in STAC Items (`title`, `description`, `providers`, etc.),
ensuring metadata provenance is preserved throughout the visualization layer.

---

## 🧠 CI/CD Integration

Web architecture validation and deployment are automated via GitHub Actions:

| Workflow                | Function                                                        | Trigger             |
| :---------------------- | :-------------------------------------------------------------- | :------------------ |
| **`site.yml`**          | Builds and deploys static web app to GitHub Pages.              | On `push` to `main` |
| **`stac-validate.yml`** | Validates all STAC references used in `web/config/layers.json`. | On PR or commit     |
| **`checksums.yml`**     | Verifies integrity of map tiles and assets.                     | On tile generation  |
| **`pre-commit.yml`**    | Lints and validates JSON config files.                          | On every PR         |

Validation artifacts are stored in `data/work/logs/web_build.log`.

---

## 🧩 Accessibility & Theming

| Feature                  | Implementation                                          |
| :----------------------- | :------------------------------------------------------ |
| **Light/Dark Mode**      | Implemented in `web/style.css` using CSS media queries. |
| **High Contrast Tokens** | Applied to base color palette in `viewer.json`.         |
| **Keyboard Navigation**  | Enabled via `tabindex` and accessible HTML roles.       |
| **Responsive Design**    | Viewport-flexible layout adapting to all screen sizes.  |

Accessibility compliance follows **WCAG 2.1 Level AA** standards.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                                       |
| :---------------------- | :----------------------------------------------------------------------------------- |
| **Documentation-first** | All configs and UI layers include human-readable and machine-readable documentation. |
| **Reproducibility**     | UI dynamically regenerates from STAC and config JSONs.                               |
| **Open Standards**      | Uses MapLibre GL JS, STAC 1.0.0, and JSON-based configs.                             |
| **Provenance**          | Every visible layer links back to a STAC metadata item.                              |
| **Auditability**        | CI/CD validation and build logs trace all published assets.                          |

---

## 📎 Related Documentation

| Path                                     | Description                                               |
| :--------------------------------------- | :-------------------------------------------------------- |
| `docs/architecture/architecture.md`      | Full system architecture overview (ETL + CI/CD + Web).    |
| `docs/architecture/data-architecture.md` | Data subsystem and metadata lineage.                      |
| `web/config/README.md`                   | Configuration reference for map layers and UI components. |
| `.github/workflows/site.yml`             | Automated web build and deployment workflow.              |

---

## 📅 Version History

| Version | Date       | Summary                                                                  |
| :------ | :--------- | :----------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial Web UI architecture documentation (MapLibre + STAC integration). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing Time, Terrain, and Truth — Provenance in Every Pixel.”*
📍 [`docs/architecture/web-ui-architecture.md`](.) · Web visualization and user interface architecture documentation.

</div>
