<div align="center">

# 🌐 Kansas Frontier Matrix — Web Application (`/web/`)

**Interactive · Temporal · Spatial · Narrative**

[![React](https://img.shields.io/badge/React-18%2B-61DAFB?logo=react&logoColor=white)](https://react.dev/)  
[![MapLibre GL](https://img.shields.io/badge/MapLibre%20GL-JS-brightgreen)](https://maplibre.org/)  
[![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)  
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009485?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)  
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)  
[![Docs: MCP](https://img.shields.io/badge/docs-MCP-blue.svg)](../docs/)  

</div>

---

## 📖 Overview

The **Kansas Frontier Matrix Web App** is the **user-facing portal** of the system.  
It merges:

- 🕰 **Timeline** (Canvas): scroll, zoom, animate history.  
- 🗺 **Map** (MapLibre GL): toggle layers, treaties, trails, hazards, and historical maps.  
- 🔎 **Search**: full-text graph search across people, places, events, and documents.  
- 📑 **Detail Panels**: AI summaries, dossiers, and related entity navigation.  
- 🤖 **AI Assistant**: natural-language Q&A with citations.  

---

## 📂 Directory Layout

```plaintext
/web/
├── src/              # React source code
│   ├── components/   # TimelineView, MapView, DetailPanel, etc.
│   ├── hooks/        # Shared React hooks
│   ├── context/      # App state management (timeline, map, selection)
│   ├── utils/        # API client, formatting helpers
│   └── styles/       # CSS/SCSS, design tokens
├── public/           # Static assets (favicon, icons, manifest)
├── config/           # Generated configs (layers.json, app.config.json)
├── package.json      # Node project dependencies
├── vite.config.js    # Build config (Vite/Webpack)
└── README.md         # This file
````

---

## 🚀 Quickstart

### Prerequisites

* Node.js **18+**
* Yarn or npm
* Backend API running (see [`docs/sop.md`](../docs/sop.md))

### Setup & Run

```bash
cd web
npm install          # or yarn install
npm run dev          # start local dev server
npm run build        # build production bundle
```

Local app → [http://localhost:5173](http://localhost:5173)

---

## 🔌 Core API Endpoints

* `GET /events?start={t1}&end={t2}&bbox=...` → events for timeline + map
* `GET /entity/{id}` → entity details, AI summary, relations
* `GET /layers-config` → STAC-derived layer config
* `GET /search?q=term` → autocomplete search results
* `POST /ask` → AI Assistant answers with citations

📖 See **[architecture flow & sequence diagram](./ARCHITECTURE.md#-high-level-architecture)**

---

## 🧩 Key Components

* **TimelineView** → performant Canvas timeline
* **MapView** → MapLibre GL with raster (COG) + vector (GeoJSON) overlays
* **LayerControls** → config-driven toggle panel + legends
* **DetailPanel** → entity details & dossiers
* **SearchBar** → knowledge graph autocomplete
* **AI Assistant** → conversational Q&A panel

---

## 🗂 Data Standards

* **GeoJSON** → vector features & API responses
* **COG (Cloud-Optimized GeoTIFF)** → raster overlays
* **STAC Catalog** → spatio-temporal metadata in `data/stac/`
* **CIDOC CRM + OWL-Time** → backend semantics for events & time

---

## 📱 Accessibility & Responsiveness

* **Desktop:** map + timeline + side panels
* **Tablet:** collapsible panels
* **Mobile:** tabbed/stacked layout
* **ARIA roles:** live regions for timeline/map, accessible labels
* **Color:** color-blind safe palette, high-contrast toggle
* **Keyboard:** tab order, focus management, shortcuts

---

## 🛠 DevOps & MCP

* **CI/CD:** GitHub Actions build/test/deploy
* **CodeQL + Trivy:** static analysis & vulnerability scans
* **Tests:** Jest + React Testing Library; Cypress for E2E (planned)
* **Docs-first (MCP):** update [`docs/architecture.md`](../docs/architecture.md), [`docs/sop.md`](../docs/sop.md), [`docs/model_card.md`](../docs/model_card.md)
* **Reproducibility:** pinned deps, containerized builds, integrity checksums

---

## ⚡ Developer Quick Reference

### Common Commands

```bash
npm run dev      # Run local dev server
npm run build    # Production build
npm run lint     # Run ESLint + Prettier
npm run test     # Run Jest tests
```

### Important Files

* `src/components/TimelineView.tsx` → Timeline rendering
* `src/components/MapView.tsx` → MapLibre GL integration
* `src/components/DetailPanel.tsx` → Entity info & dossiers
* `config/layers.json` → Map/timeline layer definitions (STAC-driven)
* `public/` → Static assets (icons, manifest, favicon)

### Adding a New Map Layer

1. Create a STAC Item in `data/stac/`.
2. Regenerate `config/layers.json`.
3. Toggle appears automatically in LayerControls.

### Debug Checklist

* **Timeline empty?** → Check `/events` API call + date filters.
* **Map missing layer?** → Confirm layer entry exists in `layers.json` with valid URL.
* **AI Assistant silent?** → Verify `/ask` endpoint responds + backend ML pipeline is running.

---

## 📚 References

* [`web/ARCHITECTURE.md`](./ARCHITECTURE.md) — detailed architecture + sequence diagram
* [`../docs/architecture.md`](../docs/architecture.md) — system-wide architecture
* [`../docs/sop.md`](../docs/sop.md) — reproducibility SOPs
* [`../docs/model_card.md`](../docs/model_card.md) — AI model documentation

---

<div align="center">

✨ *Kansas Frontier Matrix Web UI — explore Kansas across time & space.* ✨

</div>
```
