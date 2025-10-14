<div align="center">

# 🌐 Kansas Frontier Matrix — Web Application (`/web/`)

**Interactive · Temporal · Spatial · Narrative**

[![React](https://img.shields.io/badge/React-18%2B-61DAFB?logo=react&logoColor=white)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5%2B-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![MapLibre GL](https://img.shields.io/badge/MapLibre%20GL-JS-brightgreen)](https://maplibre.org/)
[![Vite](https://img.shields.io/badge/Vite-5%2B-646CFF?logo=vite&logoColor=white)](https://vitejs.dev/)
[![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009485?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![Pages Deploy](https://img.shields.io/github/deployments/bartytime4life/Kansas-Frontier-Matrix/github-pages?label=Pages%20Deploy)](https://bartytime4life.github.io/Kansas-Frontier-Matrix/)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Docs: MCP](https://img.shields.io/badge/docs-MCP--DL%20v6.2-blue.svg)](../docs/)

</div>

---

```yaml
---
title: "KFM • Web Application"
version: "v1.6.0"
last_updated: "2025-10-13"
owners: ["@kfm-web", "@kfm-architecture"]
tags: ["web","react","maplibre","canvas","timeline","vite","typescript","mcp"]
license: "MIT"
---
````

## 📖 Overview

The **Kansas Frontier Matrix Web App** is the **user-facing portal**. It merges:

* 🕰 **Timeline (Canvas):** performant zoom/pan/brush with animated playback
* 🗺 **Map (MapLibre GL):** COG rasters + GeoJSON vectors + hit-testing
* 🔎 **Search:** Graph-powered autocomplete & results (entities/events)
* 📑 **Detail Panels:** AI summaries, citations, and graph relationships
* 🤖 **AI Assistant:** natural-language Q&A with source citations

The app talks to **FastAPI** for **Neo4j** knowledge-graph queries and to the **STAC catalog** for layer metadata.

---

## 🧭 Table of Contents

* [Directory Layout](#-directory-layout)
* [Quickstart](#-quickstart)
* [Environment Configuration](#-environment-configuration)
* [API Contracts](#-api-contracts)
* [Key Components](#-key-components)
* [Data & Semantics](#-data--semantics)
* [Configuration (generated)](#-configuration-generated)
* [Accessibility & Responsiveness](#-accessibility--responsiveness)
* [Security & Privacy](#-security--privacy)
* [Dev Experience & MCP](#-dev-experience--mcp)
* [Performance Guide](#-performance-guide)
* [Developer Recipes](#-developer-recipes)
* [Troubleshooting](#-troubleshooting)
* [References](#-references)

---

## 📂 Directory Layout

```text
/web/
├─ src/
│  ├─ components/   # TimelineView, MapView, LayerControls, DetailPanel, SearchBar, AIAssistant, Legend, …
│  ├─ hooks/        # useTimelineWindow, useMapLayers, useDebounce, useHotkeys, …
│  ├─ context/      # AppContext (selection, time, layers), ThemeProvider
│  ├─ utils/        # api.ts, geometry.ts, stac.ts, time.ts, formatters.ts
│  ├─ styles/       # tokens.css (design tokens), global.css, component styles
│  └─ types/        # api.d.ts, graph.d.ts, stac.d.ts, layers.d.ts
├─ public/          # favicon, manifest, icons
├─ config/          # generated: layers.json, app.config.json (do not edit by hand)
├─ package.json     # scripts & deps (pinned)
├─ vite.config.ts   # Vite build config
└─ README.md        # this file
```

---

## 🚀 Quickstart

**Prereqs**

* Node.js **18+** (or 20+)
* npm **10+** (or pnpm/yarn)
* Backend running (see `../docs/sop.md`)

```bash
cd web
npm ci              # reproducible install
npm run dev         # http://localhost:5173
npm run build       # production build
npm run preview     # preview dist
npm run lint        # eslint + prettier
npm run test        # jest unit tests
```

---

## 🔧 Environment Configuration

Create `/web/.env` (Vite uses `VITE_` prefix):

```bash
VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=https://basemaps.cartocdn.com/gl/positron-gl-style/style.json
VITE_APP_TITLE="Kansas Frontier Matrix"
VITE_ENABLE_AI_ASSISTANT=true
```

**Notes**

* No secrets in the client; only **public** endpoints here.
* For self-hosted tiles, point `VITE_MAP_STYLE_URL` to your style JSON.

---

## 🔌 API Contracts

| Endpoint         | Method | Query/Body                                   | Returns                                         | Used by                |
| ---------------- | ------ | -------------------------------------------- | ----------------------------------------------- | ---------------------- |
| `/events`        | GET    | `start` (ISO), `end` (ISO), `bbox?`, `type?` | `Event[]` (GeoJSON FeatureCollection or array)  | TimelineView, MapView  |
| `/entity/{id}`   | GET    | —                                            | `EntityDossier` (props, relations, summary)     | DetailPanel            |
| `/layers-config` | GET    | —                                            | `LayerDef[]` (derived from STAC)                | MapView, LayerControls |
| `/search`        | GET    | `q`, `limit?`                                | `EntitySummary[]`                               | SearchBar              |
| `/ask`           | POST   | `{ "question": string }`                     | `{ "answer": string, "citations": Citation[] }` | AIAssistant            |

**Type fragments (TS)**

```ts
export interface EventFeature { type:'Feature'; geometry:any; properties:{
  id:string; label:string; type:string; start:string; end?:string; bbox?:number[];
}}
export interface EntityDossier { id:string; type:string; label:string; summary?:string;
  relations:{ predicate:string; targetId:string; targetLabel:string; }[];
  bbox?:number[]; time?:{ start:string; end?:string };
}
export interface LayerDef { id:string; label:string; type:'raster-cog'|'vector-geojson';
  source:{ url:string; minzoom?:number; maxzoom?:number }; time?:{ start:string; end?:string };
  legend?:{ category?:string; ramp?:string[] }; visible:boolean; opacity:number;
}
```

---

## 🧩 Key Components

* **TimelineView (Canvas)** — virtualized event rendering; brush sets `[start,end]`; keyboard zoom (±), pan (← →).
* **MapView (MapLibre GL)** — consumes `layers.json`; supports raster COG & vector sources; click → select → DetailPanel.
* **LayerControls** — config-driven toggles, opacity, categories, legends; persisted in `localStorage`.
* **DetailPanel** — dossier (summary, citations, related); deep-links to entity routes (`#/entity/:id`).
* **SearchBar** — async autocomplete; `Enter` → flyTo & select.
* **AIAssistant** — Q&A with citations inline (sanitized HTML).

---

## 🗂 Data & Semantics

* **Vectors**: **GeoJSON** (API + static); features carry `properties.start/end/type/id`.
* **Rasters**: **COG** (Cloud-Optimized GeoTIFF) with **internal overviews** for fast pan/zoom.
* **STAC**: `data/stac/` drives UI layers (collection/item → `config/layers.json`).
* **Ontologies**: CIDOC CRM & OWL-Time align events/actors/time; PeriodO tags period names.

---

## ⚙️ Configuration (generated)

`/web/config/layers.json` (generated from STAC) drives the map UI.

```json
{
  "id": "usgs_topo_larned_1894",
  "label": "USGS Topo — Larned (1894)",
  "type": "raster-cog",
  "source": { "url": "/tiles/usgs_topo_larned_1894.tif", "minzoom": 0, "maxzoom": 14 },
  "time": { "start": "1894-01-01", "end": "1894-12-31" },
  "legend": { "category": "Historic Topographic Maps" },
  "visible": false,
  "opacity": 0.8
}
```

> Vectors: `"type": "vector-geojson"`, `"source": {"url": "…/layer.geojson"}`.
> The `time` block powers timeline filtering.

---

## 📱 Accessibility & Responsiveness

* **Layouts**

  * Desktop: map + timeline + side panel(s)
  * Tablet: collapsible drawers
  * Mobile: tabs (Map / Timeline / Details)
* **A11y**

  * Roles/labels, focus rings, skip-links
  * Keyboard: **←/→** pan time, **±** zoom, **f** focus map, **s** focus search
  * High-contrast & color-blind-safe palette
  * Respects `prefers-reduced-motion`

---

## 🛡 Security & Privacy

* No secrets in client; **public** env vars only (`VITE_*`).
* Enforce HTTPS in production; strict CORS for API.
* Sanitize AI output (escape/strip HTML); never eval user content.
* No analytics by default; if enabled, anonymize & opt-in.

---

## 🛠 Dev Experience & MCP

* **CI/CD**: Actions build/test/deploy; status badges above.
* **Static Analysis**: CodeQL + Trivy run repo-wide.
* **Testing**

  * Unit: **Jest + RTL** (`npm run test`)
  * E2E: **Cypress** (`npm run cypress:open`) *(planned)*
* **Docs-first**: keep `../docs/architecture.md`, `../docs/sop.md`, `../docs/model_card.md` in sync.
* **Reproducibility**: pinned deps, deterministic Vite builds; STAC/COG integrity enforced in CI.

---

## ⚡ Performance Guide

**Canvas Timeline**

* Batch draw events; pre-render static bands (decades/eras) to offscreen buffers.
* Use `requestAnimationFrame` and debounced state updates.
* Avoid layout thrash (measure once → render).

**MapLibre**

* Prefer **COG** with internal overviews; bound min/max zoom.
* Pre-tile heavy vectors; layer culling for hidden categories.
* Reuse sources; throttle hover events.

**Network**

* Cache immutable assets (COGs, sprites); `Cache-Control` headers.
* Enable Brotli/Gzip; code-split vendor/app; lazy-load heavy panels.

---

## 🧑‍💻 Developer Recipes

**1) Add a New Map Layer**

1. Create a **STAC Item** under `data/stac/…`.
2. Regenerate `config/layers.json` (ETL → site build).
3. Layer appears in **LayerControls** grouped by category.

**2) Fetch & Render Events in Timeline**

```ts
// src/utils/api.ts
export async function getEvents(start:string,end:string,bbox?:number[],type?:string){
  const p = new URLSearchParams({ start,end, ...(bbox?{bbox:bbox.join(',')}:{}), ...(type?{type}:{}) });
  const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/events?`+p);
  return res.json() as Promise<EventFeature[]>;
}
```

**3) Minimal Map Source (Vector)**

```ts
map.addSource('trails', { type:'geojson', data:'/layers/trails.geojson' });
map.addLayer({ id:'trails-line', type:'line', source:'trails', paint:{ 'line-color':'#1f78b4','line-width':2 }});
```

**4) Minimal Raster COG**

```ts
map.addSource('usgs1894', { type:'raster', tiles:[
  '/tiles/usgs_topo_larned_1894.tif/{z}/{x}/{y}'
], tileSize:256, minzoom:0, maxzoom:14 });
map.addLayer({ id:'usgs1894', type:'raster', source:'usgs1894', paint:{ 'raster-opacity':0.8 }});
```

**5) Hotkeys (example)**

```ts
useHotkeys({ '+': zoomInTime, '-': zoomOutTime, ArrowLeft: panLeft, ArrowRight: panRight, f: focusMap, s: focusSearch });
```

---

## 🧪 Troubleshooting

* **Timeline empty?** Check `/events?start&end`; ensure UTC dates; verify bbox filter.
* **Layer missing?** Confirm entry exists in `config/layers.json`; validate URL & CORS; check zoom range; `visible:true`.
* **COG blurry/slow?** Ensure internal overviews; verify tile URL pattern; reduce opacity layers overdraw.
* **AI answers blank?** Check `/ask` health; backend reachable; sanitize guard not stripping content.
* **Mermaid fails in docs?** Avoid `classDef … end` (rename to `done`).

---

## 📚 References

* `web/ARCHITECTURE.md` — detailed UI architecture & flows
* `../docs/architecture.md` — system-wide architecture
* `../docs/sop.md` — reproducibility SOPs
* `../docs/model_card.md` — AI model documentation

---

<div align="center">

✨ *Kansas Frontier Matrix Web UI — explore Kansas across time & space.* ✨

</div>
