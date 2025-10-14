<div align="center">

# 🧭 Kansas Frontier Matrix — Web Frontend  
`web/src/`

**Interactive Map · Timeline · Knowledge Graph Interface**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-lightgrey)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Web Frontend (web/src/)"
version: "v1.4.0"
last_updated: "2025-10-13"
owners: ["@kfm-web", "@kfm-architecture"]
tags: ["react","typescript","maplibre","canvas","timeline","vite","mcp"]
license: "MIT"
---

🪶 Overview

The Kansas Frontier Matrix Web Frontend is a React 18+ SPA (TypeScript) that renders Kansas’s historical, environmental, and cultural data through a synchronized Map + Timeline experience. It is the public face of the KFM knowledge graph, backed by FastAPI / GraphQL and Neo4j, and driven by STAC-indexed datasets (COG/GeoJSON).

Core principles
	•	📍 Spatio-Temporal Sync — map and timeline share one time window & selection model
	•	🤖 AI Assistance — summaries & Q&A with citations from the knowledge graph
	•	🗺 Open Data — STAC → layers.json (COG rasters & GeoJSON vectors)
	•	♿ Accessible & Modular — composable React components; WCAG 2.1 AA practices

⸻

⚙️ Architecture

flowchart TD
  A["React SPA<br/>(web/src/)"] --> B["MapView<br/>(MapLibre GL JS)"]
  A --> C["TimelineView<br/>(HTML5 Canvas + D3)"]
  A --> D["SearchBar<br/>(REST/GraphQL queries)"]
  A --> E["AI Assistant Panel<br/>(Q&A + citations)"]
  A --> F["DetailPanel<br/>(Entity & Event dossiers)"]
  A --> G["LayerControls<br/>(STAC-driven config)"]

  B --> H["FastAPI Backend<br/>REST · GraphQL"]
  H --> I["Neo4j Knowledge Graph<br/>CIDOC CRM · OWL-Time"]
  H --> J["GIS Tile Storage<br/>COGs · GeoJSON · STAC"]

  I --> A
  J --> B
%% END OF MERMAID


⸻

🧩 Component Structure

Component	Purpose	Key Libraries
MapView	2D basemap + overlays (historic maps, hydrology, treaties, hazards, etc.)	maplibre-gl, react-map-gl
TimelineView	Zoom/pan/brush timeline with Canvas (high-density rendering)	HTML5 Canvas, d3-scale,d3-zoom
SearchBar	Autocomplete & search, queries /search?q=	fetch/Axios, React Context
AI Panel	Prompt → answer with citations; links to entities & time slices	client call to backend AI route
DetailPanel	Dossier (summary, relations, documents, map links)	react-markdown, internal UI kit
LayerControls	Toggles/legends/opacity; reads generated config/layers.json	React hooks, internal store

Global state (time window, selection, layers) is kept in a lightweight React Context to keep interop predictable.

⸻

🚀 Usage

Prerequisites
	•	Node.js 18+ (or 20+)
	•	npm 10+ (or pnpm/yarn)
	•	Backend API running (see ../docs/sop.md)

Environment

Create /web/.env (Vite reads VITE_ variables):

VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=https://basemaps.cartocdn.com/gl/positron-gl-style/style.json
VITE_APP_TITLE="Kansas Frontier Matrix"
VITE_ENABLE_AI_ASSISTANT=true

Commands

cd web
npm ci               # reproducible install
npm run dev          # local dev: http://localhost:5173
npm run build        # production bundle (dist/)
npm run preview      # preview prod bundle
npm run lint         # ESLint + Prettier
npm run test         # Jest + React Testing Library

Default dev port is 5173 (Vite). Update proxy rules if your backend differs.

⸻

🔌 API Contracts (frontend usage)

Endpoint	Method	Query / Body	Returns	Used by
/events	GET	start ISO, end ISO, bbox?, type?	Event[] (GeoJSON Feature or FC)	TimelineView, MapView
/entity/{id}	GET	—	EntityDossier (props, relations, summary)	DetailPanel
/layers-config	GET	—	LayerDef[] (generated from STAC)	MapView, LayerControls
/search	GET	q, limit?	EntitySummary[]	SearchBar
/ask	POST	{ "question": string }	{ "answer": string, "citations": Citation[] }	AI Panel

Type fragments (TS)

export interface EventFeature {
  type:'Feature'; geometry:any; properties:{
    id:string; label:string; type:string; start:string; end?:string; bbox?:number[];
  };
}
export interface EntityDossier {
  id:string; type:string; label:string; summary?:string;
  relations:{ predicate:string; targetId:string; targetLabel:string; }[];
  bbox?:number[]; time?:{ start:string; end?:string };
}
export interface LayerDef {
  id:string; label:string; type:'raster-cog'|'vector-geojson';
  source:{ url:string; minzoom?:number; maxzoom?:number };
  time?:{ start:string; end?:string };
  legend?:{ category?:string; ramp?:string[] };
  visible:boolean; opacity:number;
}


⸻

🧠 Data Flow

flowchart LR
  U[User] --> UI["React Components"]
  UI --> API["FastAPI / GraphQL"]
  API --> DB["Neo4j Knowledge Graph"]
  API --> STAC["STAC Catalog (data/stac/)"]
  STAC --> UI
%% END OF MERMAID


⸻

🧪 Development Notes
	•	State — React Context for: timeline [start,end], selected entity, layer visibility/opacity
	•	Accessibility — ARIA roles/labels, keyboard navigation, skip-links, color contrast (WCAG 2.1 AA)
	•	Performance — Virtualized timeline drawing; clustered markers; COG internal overviews; rAF + debounced updates
	•	Testing — Unit: Jest + RTL; E2E: Cypress (planned)
	•	Build — Vite (ESM optimized, code-split, cache-friendly)

⸻

🧭 Provenance & Dependencies
	•	Inputs — data/stac/catalog.json, API routes in src/utils/api.ts, generated config/layers.json
	•	Outputs — dist/ (optimized build), can be served with Docker/nginx
	•	Checksums — Build artifacts can be hashed; CI attaches integrity info where defined
	•	Linkage — Consumes data/processed/** layers (COG/GeoJSON) and AI summaries via backend endpoints

⸻

🗂 Data & Semantics
	•	Vectors — GeoJSON features with properties.id/type/start/end for spatio-temporal filtering
	•	Rasters — COG with internal overviews & reasonable {minzoom,maxzoom}
	•	STAC — data/stac/ → generates /web/config/layers.json (do not hand-edit)
	•	Ontologies — CIDOC CRM & OWL-Time inform backend graph queries; PeriodO tags periods in event metadata

⸻

⚙️ Configuration (generated)

/web/config/layers.json (generated from STAC) drives the UI:

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

For vectors use "type":"vector-geojson" and "source":{"url":"…/layer.geojson"}.
The time block powers timeline filtering and visibility.

⸻

♿ Accessibility & Responsiveness
	•	Layouts
	•	Desktop: map + timeline + side panels
	•	Tablet: collapsible drawers
	•	Mobile: tabs (Map / Timeline / Details)
	•	Keyboard
	•	← / → pan time; + / − zoom time; f focus map; s focus search; Esc close panels
	•	Color & Motion
	•	Color-blind-safe palette; High-Contrast toggle; respects prefers-reduced-motion

⸻

🛡 Security & Privacy (frontend)
	•	🔐 No secrets in client code; VITE_ envs must reference public endpoints
	•	🌐 Enforce HTTPS in production; honor CORS carefully (API controlled server-side)
	•	🧼 Sanitize AI output (escape/strip HTML); never eval untrusted strings
	•	📊 Analytics off by default; if enabled, make it opt-in & anonymized

⸻

🛠 DevEx & MCP
	•	CI/CD — build/test/deploy via GitHub Actions (see badges)
	•	Static Analysis — CodeQL & Trivy run repo-wide
	•	Docs-First — keep ../docs/architecture.md, ../docs/sop.md, ../docs/model_card.md in sync
	•	Reproducibility — pinned deps; deterministic builds; integrity checks on data wired into CI

⸻

⚡ Performance Checklist

Timeline (Canvas)
	•	Pre-render static bands (decades/eras) into offscreen buffers
	•	Batch event draws; clamp updates to requestAnimationFrame
	•	Debounce time/viewport changes; avoid layout thrash

MapLibre
	•	Prefer COGs with internal overviews; bound zoom range
	•	Pre-tile dense vectors; reuse sources; throttle hover events
	•	Cull hidden layers; control layer order and opacity blending

Network
	•	Cache immutable tiles (COGs, sprites); gzip/Brotli on static assets
	•	Code-split & lazy-load side panels; leverage HTTP/2 multiplexing

⸻

🧑‍💻 Developer Quick Reference

Common commands

npm run dev       # local dev server (5173)
npm run build     # production bundle
npm run preview   # local preview of dist
npm run lint      # ESLint + Prettier
npm run test      # Jest unit tests

Key files
	•	src/components/TimelineView.tsx — Canvas timeline
	•	src/components/MapView.tsx — MapLibre sources & layers
	•	src/components/DetailPanel.tsx — dossiers + citations
	•	src/utils/api.ts — API client; /events, /entity/:id, /search, /layers-config
	•	config/layers.json — generated from STAC (do not hand-edit)

Add a new map layer
	1.	Create a STAC Item under data/stac/
	2.	Regenerate config/layers.json (ETL/site build step)
	3.	Toggle appears in LayerControls grouped by category

⸻

🧰 Troubleshooting
	•	Timeline empty?
	•	Check /events?start&end; ensure ISO dates & UTC; verify bbox filter
	•	Layer not visible?
	•	Confirm entry in config/layers.json; check URL/CORS; zoom range; visible:true
	•	COG blurry/slow?
	•	Ensure internal overviews; correct tiling scheme; reduce overdraw/opacity stacks
	•	AI panel silent?
	•	Verify /ask route; backend health; sanitizer not stripping content
	•	Mermaid in docs failing?
	•	Avoid class names like end in classDef; use done instead

⸻

🔗 Related Documentation
	•	System Architecture — ../docs/architecture.md
	•	Web UI Architecture (full) — web/ARCHITECTURE.md
	•	Monorepo Design — ../docs/monorepo.md
	•	ETL Pipelines — ../docs/sop.md

⸻

📜 License & Credits

MIT License — © Kansas Frontier Matrix.
Developed under the Master Coder Protocol (MCP).

“Time, terrain, and story — united through data.”