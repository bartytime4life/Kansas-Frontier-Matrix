<div align="center">

# 🌐 Kansas Frontier Matrix — **Web Application**  
`/web/`

### *Interactive · Temporal · Spatial · Narrative*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../.github/workflows/site.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../.github/workflows/codeql.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../.github/workflows/stac-validate.yml)
[![Docs · MCP-DL](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../LICENSE)

</div>

---

```yaml
title: "Kansas Frontier Matrix — Web Application"
version: "v1.6.0"
last_updated: "2025-10-14"
authors: ["KFM Web Team"]
status: "Stable"
maturity: "Production"
tags: ["web","react","vite","typescript","maplibre","stac","timeline","mcp"]
license: "MIT (code) | CC-BY 4.0 (docs)"
semantic_alignment:
  - CIDOC CRM
  - OWL-Time
  - DCAT 2.0
  - STAC 1.0


⸻

📚 Table of Contents
	•	🧭 Overview
	•	🏗 Architecture at a Glance
	•	🗂 Directory Layout
	•	🚀 Quickstart
	•	🔧 Environment Configuration
	•	🔌 API Contracts
	•	🧩 Key Components
	•	🗺 Data & Semantics
	•	⚙️ Configuration (Generated)
	•	🏗 UI Architecture
	•	📱 Accessibility & Responsiveness
	•	🛡 Security & Privacy
	•	🛠 Dev Experience & MCP
	•	⚡ Performance Guide
	•	🧑‍💻 Developer Recipes
	•	🧪 Troubleshooting
	•	🧾 Change Log
	•	🔗 References & Links

⸻

🧭 Overview

The Kansas Frontier Matrix (KFM) Web Application is the user-facing portal blending a timeline and interactive map with AI-assisted context. It renders COG rasters and GeoJSON vectors, queries the Neo4j knowledge graph via FastAPI, and discovers map layers from a STAC catalog.
	•	🕰 Timeline (Canvas): Smooth zoom/pan/brush with animated playback
	•	🗺 Map (MapLibre GL): COG rasters + GeoJSON vectors + feature hit-testing
	•	🔎 Search: Graph-powered autocomplete & result navigation
	•	📑 Detail Panels: Summaries, citations, relationships
	•	🤖 AI Assistant: Q&A with source citations

⸻

🏗 Architecture at a Glance

flowchart TD
  A["User"] --> B["React SPA (Vite)"]
  B --> C["TimelineView (Canvas)"]
  B --> D["MapView (MapLibre GL)"]
  B --> F["SearchBar"]
  D --> E["DetailPanel"]

  subgraph Backend
    G["FastAPI /events /entity /search /ask"]
    H["Layers Config /layers-config (derived from STAC)"]
  end

  C <-->|time window| D
  C -->|GET /events| G
  D -->|GET /layers-config| H
  E -->|GET /entity/:id| G
  F -->|GET /search| G

%% END OF MERMAID

⸻

🗂 Directory Layout

/web/
├─ src/
│  ├─ components/   # TimelineView, MapView, LayerControls, DetailPanel, SearchBar, AIAssistant, Legend
│  ├─ hooks/        # useTimelineWindow, useMapLayers, useDebounce, useHotkeys
│  ├─ context/      # AppContext (selection, time, layers), ThemeProvider
│  ├─ utils/        # api.ts, geometry.ts, stac.ts, time.ts, formatters.ts
│  ├─ styles/       # tokens.css (design tokens), global.css
│  └─ types/        # api.d.ts, graph.d.ts, stac.d.ts, layers.d.ts
├─ config/          # generated: layers.json, app.config.json (do not edit manually)
├─ public/          # favicon, manifest, icons
├─ package.json     # scripts & pinned deps
├─ vite.config.ts   # Vite build config
└─ README.md


⸻

🚀 Quickstart

Prerequisites
	•	Node.js 18+ (or 20+)
	•	npm 10+ (or pnpm/yarn)
	•	Backend running (see ../docs/sop.md)

cd web
npm ci
npm run dev         # http://localhost:5173
npm run build       # production build
npm run preview     # preview dist
npm run lint        # eslint + prettier
npm run test        # jest + @testing-library/react


⸻

🔧 Environment Configuration

Create /web/.env (Vite reads VITE_* variables):

VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=https://basemaps.cartocdn.com/gl/positron-gl-style/style.json
VITE_APP_TITLE="Kansas Frontier Matrix"
VITE_ENABLE_AI_ASSISTANT=true

Notes
	•	No secrets in client; only public endpoints (VITE_*).
	•	For self-hosted tiles, point VITE_MAP_STYLE_URL to your MapLibre style JSON.

⸻

🔌 API Contracts

Endpoint	Method	Query/Body	Returns	Used by
/events	GET	start(ISO), end(ISO), bbox?, type?	Event[] (GeoJSON Feature[] or FeatureCollection)	TimelineView, MapView
/entity/{id}	GET	—	EntityDossier (props, relations, summary)	DetailPanel
/layers-config	GET	—	LayerDef[] (derived from STAC)	MapView, LayerControls
/search	GET	q, limit?	EntitySummary[]	SearchBar
/ask	POST	{ “question”: string }	{ “answer”: string, “citations”: Citation[] }	AIAssistant

Type Fragments (TypeScript)

export interface EventFeature {
  type: 'Feature';
  geometry: GeoJSON.Geometry;
  properties: {
    id: string; label: string; type: string; start: string; end?: string; bbox?: number[];
  };
}

export interface EntityDossier {
  id: string; type: string; label: string; summary?: string;
  relations: { predicate: string; targetId: string; targetLabel: string; }[];
  bbox?: number[]; time?: { start: string; end?: string };
}

export interface LayerDef {
  id: string; label: string;
  type: 'raster-cog' | 'vector-geojson';
  source: { url: string; minzoom?: number; maxzoom?: number };
  time?: { start: string; end?: string };
  legend?: { category?: string; ramp?: string[] };
  visible: boolean; opacity: number;
}


⸻

🧩 Key Components
	•	TimelineView (Canvas): Virtualized event rendering; brush sets [start,end]; hotkeys (±, ←, →).
	•	MapView (MapLibre GL): Consumes layers.json; raster COG & vector GeoJSON; click → select → DetailPanel.
	•	LayerControls: Categories, toggles, opacity, legend; persisted in localStorage.
	•	DetailPanel: Dossier (summary, citations, related items); deep-links #/entity/:id.
	•	SearchBar: Async autocomplete; Enter → flyTo + select.
	•	AIAssistant: Q&A with inline citations (sanitized HTML).

⸻

🗺 Data & Semantics
	•	Vectors: GeoJSON (API + static) with properties.start/end/type/id.
	•	Rasters: COG (Cloud-Optimized GeoTIFF) with internal overviews for fast pan/zoom.
	•	STAC: data/stac/ drives web/config/layers.json (Items/Collections → UI layers).
	•	Ontologies: CIDOC-CRM (entities/relations), OWL-Time (instants/intervals), PeriodO (period tags).

⸻

⚙️ Configuration (Generated)

/web/config/layers.json (generated from STAC) configures the map UI.

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


⸻

🏗 UI Architecture

flowchart TD
  A["User"] --> B["React Router"]
  B --> C["TimelineView (Canvas)"]
  B --> D["MapView (MapLibre GL)"]
  C <-->|time window| D
  D --> E["DetailPanel"]
  B --> F["SearchBar"]
  F --> D

  subgraph API
    G["FastAPI · /events /entity /search /ask"]
    H["Layers Config · /layers-config (from STAC)"]
  end

  C -->|GET /events| G
  D -->|GET /layers-config| H
  E -->|GET /entity/:id| G
  F -->|GET /search?q=...| G

%% END OF MERMAID

⸻

📱 Accessibility & Responsiveness
	•	Layouts: Desktop (map + timeline + panel), Tablet (collapsible drawers), Mobile (tabbed Map/Timeline/Details).
	•	A11y: ARIA roles/labels, skip-links, visible focus rings. Keyboard: ←/→ pan, ± zoom, f focus map, s focus search.
	•	Color-blind-safe palettes, respects prefers-reduced-motion, touch targets ≥ 44×44 px.

⸻

🛡 Security & Privacy
	•	HTTPS in production; strict CORS; no secrets in client (VITE_* only).
	•	Sanitize AI output (escape/strip HTML); never eval user content.
	•	No analytics by default; if enabled, anonymize & opt-in.

⸻

🛠 Dev Experience & MCP
	•	CI/CD: GitHub Actions (Build · Lint · Test · Deploy); STAC validation gates.
	•	Static Analysis: CodeQL + Trivy.
	•	Testing: Jest + React Testing Library; Cypress (planned).
	•	Docs-first: Keep ../docs/architecture.md, ../docs/sop.md, and ../docs/model_card.md in sync.
	•	Reproducibility: Pinned deps; deterministic Vite builds; COG/STAC checksums in CI.

⸻

⚡ Performance Guide
	•	Timeline (Canvas): Batch draw · offscreen bands · requestAnimationFrame · debounced state.
	•	Map (MapLibre): COG with overviews · min/max zoom bounds · pre-tile heavy vectors · cull hidden layers.
	•	Network: Cache immutable assets (Cache-Control) · Brotli/Gzip · code-split vendor/app · lazy-load heavy panels.

⸻

🧑‍💻 Developer Recipes

Add a New Map Layer
	1.	Create a STAC Item under data/stac/…
	2.	Regenerate web/config/layers.json (ETL → site build).
	3.	Toggle in LayerControls.

Fetch & Render Events in Timeline

// src/utils/api.ts
export async function getEvents(start:string,end:string,bbox?:number[],type?:string){
  const p = new URLSearchParams({ start,end, ...(bbox?{bbox:bbox.join(',')}:{}), ...(type?{type}:{}) });
  const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/events?${p}`);
  if(!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json() as Promise<EventFeature[]>;
}

Minimal Map Sources

// Vector
map.addSource('trails', { type:'geojson', data:'/layers/trails.geojson' });
map.addLayer({ id:'trails-line', type:'line', source:'trails',
  paint:{ 'line-color':'#1f78b4','line-width':2 }});

// Raster COG
map.addSource('usgs1894', { type:'raster',
  tiles:['/tiles/usgs_topo_larned_1894.tif/{z}/{x}/{y}'], tileSize:256, minzoom:0, maxzoom:14 });
map.addLayer({ id:'usgs1894', type:'raster', source:'usgs1894',
  paint:{ 'raster-opacity':0.8 }});


⸻

🧪 Troubleshooting

Symptom	Check
Timeline empty	/events?start&end valid? UTC? bbox filter correct?
Layer missing	Entry in config/layers.json? URL/CORS ok? zoom range? visible:true?
COG blurry/slow	Internal overviews present? tile URL correct? reduce overdraw
AI answers blank	/ask reachable? sanitize not over-stripping?
Mermaid not rendering	Fenced ```mermaid block closed properly and ends with %% END OF MERMAID


⸻

🧾 Change Log

Version	Date	Author(s)	Summary
v1.6.0	2025-10-14	KFM Web Team	Rebuilt README to KFM house style; added badges & mermaid diagrams
v1.5.0	2025-09-10	KFM Web Team	STAC → layers.json generation; performance guidance
v1.4.0	2025-08-02	KFM Web Team	AI Assistant panel + /ask integration


⸻

🔗 References & Links
	•	web/ARCHITECTURE.md — Component flows & UI wiring
	•	../docs/architecture.md — Full-stack system design
	•	../docs/sop.md — Reproducibility SOPs
	•	../docs/model_card.md — AI model documentation

⸻


<div align="center">


KFM Web UI — Explore Kansas across time & space.
MIT License · MCP-DL v6.2 · Last Updated 2025-10-14

</div>
```
