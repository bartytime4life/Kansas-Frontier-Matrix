<div align="center">


🌐 Kansas Frontier Matrix — Web Application (/web/)

Interactive · Temporal · Spatial · Narrative

</div>


<!--
title: "KFM • Web Application"
version: v1.6.0
last_updated: 2025-10-14
owners: [@kfm-web, @kfm-architecture]
tags: [web, react, maplibre, canvas, timeline, vite, typescript, mcp, stac]
license: MIT
status: Stable
-->


v1.6.0 · Updated 2025-10-14 · MIT License
Owners @kfm-web | @kfm-architecture · Tags web · react · maplibre · vite · mcp

⸻

📖 Overview

The Kansas Frontier Matrix Web App is the public UI for exploring Kansas across time and space.
	•	🕰 Timeline (Canvas): high-FPS zoom/pan/brush with animated playback
	•	🗺 Map (MapLibre GL): COG rasters + GeoJSON vectors + hit-testing
	•	🔎 Search: graph-powered autocomplete & results (entities/events)
	•	📑 Detail Panels: AI summaries, citations, and graph relationships
	•	🤖 AI Assistant: natural-language Q&A with inline source citations

The client calls FastAPI for Neo4j graph queries and uses the STAC catalog to discover map layers.

⸻

🧭 Table of Contents
	•	Directory Layout
	•	Quickstart
	•	Environment Configuration
	•	API Contracts
	•	Key Components
	•	Data & Semantics
	•	Configuration (generated)
	•	UI Architecture
	•	Accessibility & Responsiveness
	•	Security & Privacy
	•	Dev Experience & MCP
	•	Performance Guide
	•	Developer Recipes
	•	Troubleshooting
	•	Change Log
	•	References

⸻

📂 Directory Layout

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
├─ package.json     # scripts & pinned deps
├─ vite.config.ts   # Vite build config
└─ README.md        # this file


⸻

🚀 Quickstart

Prereqs
	•	Node.js 18+ (or 20+)
	•	npm 10+ (or pnpm / yarn)
	•	Backend running (see ../docs/sop.md)

cd web
npm ci              # reproducible install
npm run dev         # http://localhost:5173
npm run build       # production build
npm run preview     # preview dist
npm run lint        # eslint + prettier
npm run test        # jest + @testing-library/react


⸻

🔧 Environment Configuration

Create /web/.env (Vite reads VITE_*):

VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=https://basemaps.cartocdn.com/gl/positron-gl-style/style.json
VITE_APP_TITLE="Kansas Frontier Matrix"
VITE_ENABLE_AI_ASSISTANT=true

Notes
	•	No secrets in the client; only public endpoints here.
	•	For self-hosted tiles/styles, point VITE_MAP_STYLE_URL to your MapLibre style JSON.

⸻

🔌 API Contracts

Endpoint	Method	Query/Body	Returns	Used by
/events	GET	start(ISO), end(ISO), bbox?, type?	Event[] (GeoJSON Feature[]/FeatureCollection)	TimelineView, MapView
/entity/{id}	GET	—	EntityDossier (props, relations, summary)	DetailPanel
/layers-config	GET	—	LayerDef[] (derived from STAC)	MapView, LayerControls
/search	GET	q, limit?	EntitySummary[]	SearchBar
/ask	POST	{ "question": string }	{ "answer": string, "citations": Citation[] }	AIAssistant

Type fragments (TS)

export interface EventFeature {
  type: 'Feature';
  geometry: GeoJSON.Geometry;
  properties: {
    id: string; label: string; type: string;
    start: string; end?: string; bbox?: number[];
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
	•	TimelineView (Canvas) — virtualized event rendering; brush sets [start,end]; hotkeys (±, ←, →).
	•	MapView (MapLibre GL) — layers.json-driven; raster COG & vector GeoJSON; click → select → DetailPanel.
	•	LayerControls — toggles, opacity, categories, legends; persisted in localStorage.
	•	DetailPanel — dossier (summary, citations, related); routes #/entity/:id.
	•	SearchBar — async autocomplete; Enter → flyTo & select.
	•	AIAssistant — citations-first Q&A (sanitized HTML).

⸻

🗂 Data & Semantics
	•	Vectors: GeoJSON (API + static); features carry properties.start/end/type/id.
	•	Rasters: COG (Cloud-Optimized GeoTIFF) with internal overviews.
	•	STAC: data/stac/ (Items/Collections) → generates /web/config/layers.json.
	•	Ontologies: CIDOC-CRM (entities/relations), OWL-Time (instants/intervals), PeriodO tags (period labels).

⸻

⚙️ Configuration (generated)

/web/config/layers.json (generated from STAC) drives the map UI.

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

Vectors use "type": "vector-geojson", "source": {"url": "…/layer.geojson"}.
The time block powers timeline filtering.

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
%%END OF MERMAID%%


⸻

📱 Accessibility & Responsiveness

Layouts
	•	Desktop: map + timeline + side panel(s)
	•	Tablet: collapsible drawers
	•	Mobile: tabs (Map / Timeline / Details)

A11y
	•	Landmark roles, labels, skip-links, visible focus rings
	•	Keyboard: ←/→ pan time, ± zoom, f focus map, s focus search
	•	Color-blind-safe palette; respects prefers-reduced-motion
	•	Touch targets ≥ 44×44px; headings in logical order

⸻

🛡 Security & Privacy
	•	No secrets in client; public env vars only (VITE_*).
	•	Enforce HTTPS (prod); strict CORS for API.
	•	Sanitize AI output (escape/strip HTML); never eval.
	•	No analytics by default; if enabled, anonymize & opt-in.

⸻

🛠 Dev Experience & MCP
	•	CI/CD: GitHub Actions (build/test/deploy).
	•	Static Analysis: CodeQL + Trivy.
	•	Testing:
	•	Unit: Jest + RTL (npm run test)
	•	E2E: Cypress (npm run cypress:open) (planned)
	•	Docs-first: keep ../docs/architecture.md, ../docs/sop.md, ../docs/model_card.md in sync.
	•	Reproducibility: pinned deps; deterministic Vite builds; STAC/COG integrity checks in CI.

⸻

⚡ Performance Guide

Canvas Timeline
	•	Batch draw; pre-render era bands to offscreen buffers.
	•	requestAnimationFrame; debounce updates.
	•	Avoid layout thrash (measure once → render).

MapLibre
	•	Prefer COG with overviews; bind min/max zoom.
	•	Pre-tile heavy vectors; cull hidden categories.
	•	Reuse sources; throttle hover/mousemove.

Network
	•	Cache immutable assets (Cache-Control); Brotli/Gzip.
	•	Code-split vendor/app; lazy-load heavy panels.

⸻

🧑‍💻 Developer Recipes

1) Add a New Map Layer
	1.	Create/extend a STAC Item under data/stac/….
	2.	Regenerate config/layers.json (ETL → site build).
	3.	See it in LayerControls under its category.

2) Fetch & Render Events in Timeline

// src/utils/api.ts
export async function getEvents(start:string,end:string,bbox?:number[],type?:string){
  const p = new URLSearchParams({ start,end, ...(bbox?{bbox:bbox.join(',')}:{}), ...(type?{type}:{}) });
  const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/events?${p}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json() as Promise<EventFeature[]>;
}

3) Minimal Map Source (Vector)

map.addSource('trails', { type:'geojson', data:'/layers/trails.geojson' });
map.addLayer({ id:'trails-line', type:'line', source:'trails', paint:{ 'line-color':'#1f78b4','line-width':2 }});

4) Minimal Raster COG

map.addSource('usgs1894', {
  type:'raster',
  tiles: ['/tiles/usgs_topo_larned_1894.tif/{z}/{x}/{y}'],
  tileSize:256, minzoom:0, maxzoom:14
});
map.addLayer({ id:'usgs1894', type:'raster', source:'usgs1894', paint:{ 'raster-opacity':0.8 }});

5) Hotkeys (example)

useHotkeys({
  '+': zoomInTime,
  '-': zoomOutTime,
  ArrowLeft: panLeft,
  ArrowRight: panRight,
  f: focusMap,
  s: focusSearch
});


⸻

🧪 Troubleshooting
	•	Timeline empty? Check /events?start&end; ensure UTC; verify bbox filter.
	•	Layer missing? Confirm config/layers.json entry; validate URL/CORS; check zoom range; visible:true.
	•	COG blurry/slow? Ensure internal overviews; verify tile pattern; reduce overdraw.
	•	AI answers blank? Check /ask health; backend reachable; sanitize guard not stripping content.
	•	Mermaid not rendering? Keep the diagram outside HTML; fence with ```mermaid; close the fence; end with %%END OF MERMAID%%.

⸻

🧾 Change Log

Version	Date	Author(s)	Summary
v1.6.0	2025-10-14	@kfm-web, @kfm-arch	Rebuilt with compact hybrid metadata; standardized ##
v1.5.0	2025-09-10	@kfm-web	Added STAC → layers.json generation; perf guidance.
v1.4.0	2025-08-02	@kfm-web	Added AI Assistant panel & /ask integration.


⸻

📚 References
	•	web/ARCHITECTURE.md — detailed UI architecture & flows
	•	../docs/architecture.md — system-wide architecture
	•	../docs/sop.md — reproducibility SOPs
	•	../docs/model_card.md — AI model documentation

⸻


<div align="center">


KFM Web UI · MIT License · MCP-DL v6.2 · Last Updated 2025-10-14
✨ Explore Kansas across time & space. ✨

</div>
