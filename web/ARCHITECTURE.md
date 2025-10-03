<div align="center">

# 🌐 Kansas Frontier Matrix — **Web UI Architecture**  
`web/ARCHITECTURE.md`

**⏳ Timeline · 🗺 Map · 🔎 Search · 🤖 AI Assistant**

<!-- Badges -->
<a href="https://react.dev/"><img alt="React" src="https://img.shields.io/badge/React-18%2B-61DAFB?logo=react&logoColor=white"></a>
<a href="https://maplibre.org/"><img alt="MapLibre GL JS" src="https://img.shields.io/badge/MapLibre%20GL-JS-brightgreen"></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API"><img alt="HTML5 Canvas" src="https://img.shields.io/badge/HTML5-Canvas-E34F26?logo=html5&logoColor=white"></a>
<a href="https://fastapi.tiangolo.com/"><img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-Backend-009485?logo=fastapi&logoColor=white"></a>  
<a href="../.github/workflows/site.yml"><img alt="Build & Deploy" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg"></a>
<a href="../.github/workflows/codeql.yml"><img alt="CodeQL" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg"></a>
<a href="../.github/workflows/trivy.yml"><img alt="Trivy Security" src="https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg"></a>
<a href="../docs/"><img alt="Docs: MCP" src="https://img.shields.io/badge/docs-MCP-blue.svg"></a>
<a href="../LICENSE"><img alt="License: MIT/CC-BY" src="https://img.shields.io/badge/license-MIT%20%7C%20CC--BY-green"></a>

</div>

---

## 📚 Table of Contents

1. [🔭 Overview](#-overview)  
2. [🗺️ High-Level Frontend Architecture](#️-high-level-frontend-architecture)  
3. [🧩 Key Frontend Components](#-key-frontend-components)  
   - TimelineView (Canvas Timeline)  
   - MapView (Interactive Map)  
   - DetailPanel (Entity Details)  
   - LayerControls (Layers & Legends)  
   - SearchBar (Knowledge Graph Search)  
   - AI Assistant (Q&A Interface)  
4. [🔌 Frontend-Backend Integration & Data Flow](#-frontend-backend-integration--data-flow)  
5. [🔄 Timeline & Map Synchronization](#-timeline--map-synchronization)  
6. [🗂 Open Standards & Layer Data](#-open-standards--layer-data)  
7. [📱 Responsive Design & Accessibility](#-responsive-design--accessibility)  
8. [🛠 CI/CD & Master Coder Protocol](#-cicd--master-coder-protocol)  

---

## 🔭 Overview

The **KFM** Web UI is a **React 18+** SPA that links a **Canvas timeline** and a **MapLibre GL** map to explore Kansas’s frontier history through space and time. It talks to a **FastAPI** backend (with optional GraphQL) backed by **Neo4j**. Heavy work (ETL, AI, geospatial queries) runs server-side; the browser focuses on **interactive visualization** and **storytelling**.

> **Docs-first (MCP):** Architecture & SOPs live in repo:  
> • [`docs/architecture.md`](../docs/architecture.md) · [`docs/sop.md`](../docs/sop.md) · [`docs/model_card.md`](../docs/model_card.md)

---

## 🗺️ High-Level Frontend Architecture

```mermaid
sequenceDiagram
    participant U as User
    participant W as "Web UI\n(React SPA)"
    participant A as "API\n(FastAPI)"
    participant G as "Graph DB\n(Neo4j)"
    participant S as "Geo Data\n(STAC Catalog)"
    participant ML as "AI Pipeline\n(NLP/Summary)"

    U->>W: Interact (scroll, click, search, ask)
    W->>A: GET /events?start={t1}&end={t2}&bbox=...
    A->>G: Cypher (time/space filtered)
    G-->>A: Events (GeoJSON + meta)
    A-->>W: FeatureCollection JSON
    W->>S: Load layer assets (COG tiles / GeoJSON)
    S-->>W: Raster/Vector tiles & files
    W-->>U: Render Map + Timeline (synced)
    U->>W: Select entity
    W->>A: GET /entity/{id}
    A-->>W: Entity details + AI summary
    W-->>U: Show DetailPanel
    U->>W: Ask question
    W->>A: POST /ask  { "q": "..." }
    A->>ML: Generate answer + refs
    ML-->>A: Answer (with citations)
    A-->>W: JSON (answer + refs)
    W-->>U: AI chat response
````

<!-- END OF MERMAID -->

---

## 🧩 Key Frontend Components

### TimelineView (Canvas Timeline)

* **Why Canvas?** Smooth panning/zooming at 60fps with hundreds/thousands of events.
* **Features:** time ruler, zoom, scroll, hover & select events, category colors, “importance” labeling by zoom level.
* **Sync:** selecting an event highlights it on the map and opens the DetailPanel; changing time window filters map & events.

### MapView (Interactive Map)

* **MapLibre GL JS:** WebGL vector tiles + raster overlays; base map (e.g., OSM) + **STAC-derived layers**.
* **Layers:** raster **COG** (scanned maps, DEM/hillshade), **GeoJSON** (trails, boundaries), vector tiles.
* **UX:** markers & clustering for events, popups, symbology legend; filters tie to timeline.

### DetailPanel (Entity Details)

* **What:** Entity detail (Event/Person/Place/Document) with properties, **AI summary**, and **related entities**.
* **Graph navigation:** traverse relationships via links (event → person → place → …).
* **Dossiers:** rich narrative pages for important places/topics (images, mini-timeline, media).

### LayerControls (Layers & Legends)

* **Config-driven:** reads `web/config/layers.json` (generated from STAC) for layer list, types, time spans, URLs, styling.
* **Controls:** checkboxes, opacity sliders (raster), grouped categories, legend toggles.
* **Temporal logic:** auto-show/hide per current timeline.

### SearchBar (Knowledge Graph Search)

* **Typeahead:** `GET /search?q=...` returns entity matches (id, name, type, snippet).
* **Actions:** jump timeline, pan map, open DetailPanel.

### AI Assistant (Q&A)

* **Natural Language:** `POST /ask` → LLM answer + citations.
* **Integration:** optional highlight of relevant events/entities on map/timeline.
* **Transparency:** “AI” badge, links to sources, feedback hook.

---

## 🔌 Frontend-Backend Integration & Data Flow

**Core Endpoints**

| Endpoint                                                     | Purpose                                                   | UI Consumer                          |
| ------------------------------------------------------------ | --------------------------------------------------------- | ------------------------------------ |
| `GET /events?start={t1}&end={t2}&bbox={xmin,ymin,xmax,ymax}` | Time/space-filtered events (GeoJSON FeatureCollection).   | TimelineView, MapView                |
| `GET /entity/{id}`                                           | Entity details (attrs, summary, related).                 | DetailPanel                          |
| `GET /layers-config`                                         | Layer list (name, type, time, source URL, style, legend). | LayerControls, MapView, TimelineView |
| `GET /search?q={term}`                                       | Typeahead results (id, name, type, snippet).              | SearchBar                            |
| `POST /ask`                                                  | AI answer (text + references).                            | AI Assistant                         |

**Fetch & Render Pseudocode**

```ts
// Timeline fetch:
const url = `/events?start=${startISO}&end=${endISO}&bbox=${bbox}`;
const eventsFC = await fetch(url).then(r => r.json());
timeline.draw(eventsFC.features);

// Entity details:
const entity = await fetch(`/entity/${id}`).then(r => r.json());
setDetailPanel(entity);

// Layers config:
const layers = await fetch('/layers-config').then(r => r.json());
initLayerControls(layers);
map.addConfiguredLayers(layers);

// Search:
const results = await fetch(`/search?q=${encodeURIComponent(q)}`).then(r => r.json());
showTypeahead(results);

// AI:
const answer = await fetch('/ask', {method:'POST', body: JSON.stringify({ q })}).then(r => r.json());
aiPanel.show(answer);
```

---

## 🔄 Timeline & Map Synchronization

* **Shared state:** `{ timeRange, bbox, selectedEntity, activeLayers }` in React Context.
* **Bi-directional sync:**

  * Timeline → Map: time filters map layers & visible events; selecting event centers map.
  * Map → Timeline: bbox filters events; popups select event & scroll timeline.
* **Highlighting:** selected event marked in both views; related entities emphasized.
* **Playback (optional):** animate time window; update layers and events per step.
* **Layer time extents:** layers auto-enable only during their active dates.

---

## 🗂 Open Standards & Layer Data

* **STAC**: `data/stac/` catalogs raster/vector assets with `bbox`, `datetime`, `assets`.
* **GeoJSON**: vectors & API responses (events, boundaries, trails).
* **COG**: Cloud-Optimized GeoTIFFs for rasters (scanned maps, DEM, hillshade).
* **CIDOC CRM / OWL-Time**: backend semantics for consistent entity/temporal modeling.

**Example STAC → Layer Config**

```json
// STAC Item (simplified)
{
  "id": "ks_rr_map_1878",
  "properties": { "start_datetime": "1878-01-01T00:00:00Z", "end_datetime": "1878-12-31T23:59:59Z" },
  "bbox": [-102.0, 36.0, -94.5, 40.0],
  "assets": {
    "map": {
      "href": "https://cdn.example.org/maps/ks_railroads_1878.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}
```

```json
// Generated web/config/layers.json entry (simplified)
{
  "id": "ks_rr_map_1878",
  "name": "1878 Railroad Map",
  "category": "Historic Maps",
  "type": "raster",
  "start_year": 1878,
  "end_year": 1878,
  "source": { "tileUrl": "https://tiles.example.org/ks_rr_1878/{z}/{x}/{y}.png" },
  "opacity": 0.7,
  "legend": "legends/rr_1878.png"
}
```

---

## 📱 Responsive Design & Accessibility

* **Responsive:** CSS Grid/Flex; desktop = map+timeline+panels; tablet = collapsible panels; mobile = tabbed/stacked views.
* **Touch-friendly:** larger hit targets, simplified controls.
* **ARIA & keyboard:** semantic roles, labeled controls, focus management, `aria-live` updates for Canvas/timeline, accessible alternative lists.
* **Contrast & color:** color-blind friendly palette; optional high-contrast mode.

---

## 🛠 CI/CD & Master Coder Protocol

* **GitHub Actions:** build (`site.yml`), **CodeQL**, **Trivy**.
* **Tests:** Jest + React Testing Library (UI), end-to-end where relevant.
* **Pre-commit:** ESLint/Prettier; consistent code style & formatting.
* **Docs-first (MCP):** keep architecture & SOPs current.

  * [`docs/architecture.md`](../docs/architecture.md) – end-to-end stack
  * [`docs/sop.md`](../docs/sop.md) – reproducible procedures
  * [`docs/model_card.md`](../docs/model_card.md) – AI models & constraints
* **Releases:** semantic versioning; `CHANGELOG`; tagged builds.

---

## 📂 Project Paths (Monorepo)

* `web/src/` — React components (TimelineView, MapView, DetailPanel, LayerControls, SearchBar, AI)
* `web/config/` — generated `layers.json` / `app.config.json`
* `data/stac/` — STAC catalog (items, collections)
* `docs/` — architecture, SOPs, model cards, contributor docs
* `tools/` — scripts for config renderers, validations, tiles; dev utilities
* `.github/workflows/` — CI/CD workflows (build, test, security)

---

## ✍️ Notes for Contributors

* **Add a map layer:** add STAC item → run pipeline to render `web/config/layers.json` → test in UI.
* **Add UI feature:** create isolated component; wire via Context; include tests; update docs.
* **Testing:** add/extend Jest & RTL tests; CI must pass.
* **Docs:** update this file + relevant docs per MCP.

> **Questions?** Open an issue or PR with your proposed change & checklist: tests, docs, config, screenshots (if UI).
