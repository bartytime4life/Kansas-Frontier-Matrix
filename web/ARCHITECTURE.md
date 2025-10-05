<div align="center">

# 🌐 Kansas Frontier Matrix — Web Application (`/web/`)

**Interactive · Temporal · Spatial · Narrative**

[![React](https://img.shields.io/badge/React-18%2B-61DAFB?logo=react&logoColor=white)](https://react.dev/)
[![MapLibre GL](https://img.shields.io/badge/MapLibre%20GL-JS-brightgreen)](https://maplibre.org/)
[![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009485?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![Pages Deploy](https://img.shields.io/github/deployments/bartytime4life/Kansas-Frontier-Matrix/github-pages?label=Pages%20Deploy)](https://bartytime4life.github.io/Kansas-Frontier-Matrix/)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Docs: MCP](https://img.shields.io/badge/docs-MCP-blue.svg)](../docs/)

</div>

---

## 📖 Overview

The **Kansas Frontier Matrix Web App** is the **user-facing portal** of the system.  
It merges:

- 🕰 **Timeline (Canvas):** scroll, zoom, animate history  
- 🗺 **Map (MapLibre GL):** toggle layers (treaties, trails, hazards, historic maps)  
- 🔎 **Search:** full-text graph search across people, places, events, docs  
- 📑 **Detail Panels:** AI summaries, dossiers, related entity navigation  
- 🤖 **AI Assistant:** natural-language Q&A with citations  

> Data arrives via the FastAPI backend from the **Neo4j knowledge graph** and the **STAC catalog** (COG/GeoJSON).

---

## 📂 Directory Layout

```plaintext
/web/
├── src/                  # React source
│   ├── components/       # TimelineView, MapView, LayerControls, DetailPanel, SearchBar, AIAssistant, ...
│   ├── hooks/            # Shared React hooks
│   ├── context/          # App state (timeline window, selection, layer toggles)
│   ├── utils/            # API client, formatting, geometry helpers
│   ├── styles/           # CSS/SCSS, design tokens (CSS vars)
│   └── types/            # TS types/interfaces (API/graph/config)
├── public/               # Static assets (favicon, icons, manifest)
├── config/               # Generated configs (layers.json, app.config.json)
├── package.json          # Node project
├── vite.config.ts        # Build config (Vite)
└── README.md             # This file
````

---

## 🚀 Quickstart

### Prerequisites

* Node.js **18+** (or 20+)
* npm or yarn
* Backend API running (see [`../docs/sop.md`](../docs/sop.md))

### Environment

Create `/web/.env` (Vite reads `VITE_` prefixed vars):

```bash
VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=https://basemaps.cartocdn.com/gl/positron-gl-style/style.json
VITE_APP_TITLE="Kansas Frontier Matrix"
```

### Setup & Run

```bash
cd web
npm install          # or: yarn install
npm run dev          # start local dev server (http://localhost:5173)
npm run build        # build production bundle
npm run preview      # preview production build locally
```

---

## 🔌 Core API Endpoints (contract)

| Endpoint         | Method | Params                           | Returns                                    | Used by                |
| ---------------- | ------ | -------------------------------- | ------------------------------------------ | ---------------------- |
| `/events`        | GET    | `start`, `end`, `bbox?`, `type?` | `Event[]` (GeoJSON + props)                | TimelineView, MapView  |
| `/entity/{id}`   | GET    | —                                | Entity dossier (props, relations, summary) | DetailPanel            |
| `/layers-config` | GET    | —                                | Layer defs (from STAC → layers.json)       | MapView, LayerControls |
| `/search`        | GET    | `q`, `limit?`                    | `Entity[]` (id, label, type, bbox?)        | SearchBar              |
| `/ask`           | POST   | JSON `{question}`                | `{ answer, citations[] }`                  | AIAssistant            |

> See backend spec in [`../docs/architecture.md`](../docs/architecture.md) for response shapes.

---

## 🧩 Key Components

* **TimelineView** — performant **HTML5 Canvas** timeline (zoom/pan/brush filter → emits time window)
* **MapView** — **MapLibre GL** map; consumes `layers.json`; supports raster COG + vector GeoJSON + click hit-testing
* **LayerControls** — config-driven toggles, opacity, legends; remembers user selection
* **DetailPanel** — entity dossier w/ AI summary + citations; linked entities (people ↔ events ↔ places)
* **SearchBar** — knowledge graph autocomplete; Enter → flyTo + select
* **AIAssistant** — conversational Q&A with inline citations, links to map/timeline highlights

---

## 🗂 Data Standards

* **GeoJSON** — vector features (and many API responses)
* **COG (Cloud-Optimized GeoTIFF)** — raster overlays (historic maps, hillshade, etc.)
* **STAC Catalog** — spatio-temporal metadata in `data/stac/` → drives `config/layers.json`
* **CIDOC CRM + OWL-Time** — backend semantics for events/actors/time (graph queries honor intervals)

---

## ⚙️ Configuration (generated)

`/web/config/layers.json` (generated from STAC) drives the UI. A **minimal** entry looks like:

```json
{
  "id": "usgs_topo_larned_1894",
  "label": "USGS Topo — Larned (1894)",
  "type": "raster-cog",
  "source": {
    "url": "/tiles/usgs_topo_larned_1894.tif", 
    "minzoom": 0,
    "maxzoom": 14
  },
  "time": { "start": "1894-01-01", "end": "1894-12-31" },
  "legend": { "category": "Historic Topographic Maps" },
  "visible": false,
  "opacity": 0.8
}
```

> Vectors use `"type": "vector-geojson"` and `"source": {"url": ".../layer.geojson"}`.
> The time block powers the timeline filter.

---

## 📱 Accessibility & Responsiveness

* **Layouts:**

  * Desktop: map + timeline + side panel(s)
  * Tablet: collapsible panels, stacked drawers
  * Mobile: tabs for Map / Timeline / Details
* **A11y:** WAI-ARIA roles/labels, focus rings, skip-links, keyboard navigation (←/→ zoom time; `f` focus map; `s` focus search)
* **Color:** color-blind-safe palette, high-contrast toggle
* **Motion:** reduced-motion guardrails for animations

---

## 🛡️ Security & Privacy (frontend)

* Never embed secrets in the client; use `VITE_` config for **public** endpoints only
* Respect CORS and same-origin policies; assert `https` on production
* Sanitize HTML in AI answers (escape/strip)
* Avoid leaking bounding boxes/IDs in analytics (opt-in only)

---

## 🛠 DevEx & MCP

* **CI/CD:** GitHub Actions build/test/deploy (see badges)
* **Static Analysis:** CodeQL + Trivy on the repo (frontend deps covered)
* **Tests:**

  * **Unit:** Jest + React Testing Library (`npm run test`)
  * **E2E:** Cypress (`npm run cypress:open`) *(planned)*
* **Docs-first (MCP):** keep [`../docs/architecture.md`](../docs/architecture.md), [`../docs/sop.md`](../docs/sop.md), [`../docs/model_card.md`](../docs/model_card.md) in sync with changes
* **Reproducibility:** pinned deps, deterministic builds, integrity checksums on data wired into CI

---

## ⚡ Performance Checklist

* Canvas Timeline

  * Use **offscreen buffers** for static bands (decades/eras); paint events as batches
  * Avoid layout thrash: read DOM once, then draw on Canvas
  * Clamp redraws to rAF; debounce window/time changes
* MapLibre

  * Prefer **COGs with internal overviews**; set sensible min/maxzoom
  * Use tippecanoe/geojson-vt (or pre-tiled vector sources) for dense vectors
  * Cull hidden layers; reuse sources; throttle hover events
* Network

  * Cache immutable assets (COGs, sprites); set `Cache-Control` on tiles/static
  * Gzip/Brotli enabled; split vendor/app chunks, lazy-load panels

---

## 🧪 Developer Quick Reference

### Common Commands

```bash
npm run dev       # local dev server
npm run build     # production build
npm run preview   # preview prod build
npm run lint      # ESLint + Prettier
npm run test      # Jest unit tests
```

### Important Files

* `src/components/TimelineView.tsx` — timeline rendering
* `src/components/MapView.tsx` — MapLibre integration & layer sources
* `src/components/DetailPanel.tsx` — dossiers + citations
* `config/layers.json` — STAC-driven layer definitions
* `public/` — icons, manifest, favicon

### Add a New Map Layer

1. Create a **STAC Item** in `data/stac/`
2. Regenerate `config/layers.json` (via ETL/site build)
3. Toggle appears automatically in **LayerControls**

---

## 🧰 Troubleshooting

* **Timeline empty?**

  * Verify `/events?start&end` returns data; check date range and timezone (UTC).
* **Layer missing on map?**

  * Confirm entry exists in `config/layers.json`; validate URL (CORS), zoom range, and visibility.
* **COG draws blurry / slow?**

  * Ensure **internal overviews** present; check tile server range; reduce opacity blending.
* **AI Assistant silent?**

  * Check backend `/ask` health; ensure model service reachable; sanitize user prompt.
* **Mermaid fails in docs?**

  * Avoid class names like `end`; rename to `done` in `classDef`.

---

## 📚 References

* [`web/ARCHITECTURE.md`](./ARCHITECTURE.md) — detailed UI architecture & sequences
* [`../docs/architecture.md`](../docs/architecture.md) — system-wide architecture
* [`../docs/sop.md`](../docs/sop.md) — reproducibility SOPs
* [`../docs/model_card.md`](../docs/model_card.md) — AI model documentation

---

<div align="center">

✨ *Kansas Frontier Matrix Web UI — explore Kansas across time & space.* ✨

</div>

