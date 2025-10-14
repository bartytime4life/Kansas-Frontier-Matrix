<div align="center">


🌐 Kansas Frontier Matrix — Web Application

/web/

Interactive · Temporal · Spatial · Narrative

</div>



⸻


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
Owners @kfm-web | @kfm-architecture
Tags: web · react · maplibre · vite · typescript · mcp

⸻

🧭 Overview

The Kansas Frontier Matrix Web Application is the user interface layer of the KFM system —
a high-performance, open-source SPA that visualizes Kansas’s history, environment, and data
through maps, timelines, and AI-driven insights.

Core Capabilities
	•	🕰 Timeline Canvas: Smooth, animated navigation through time ranges
	•	🗺 MapLibre GL: Vector + raster rendering via Cloud-Optimized GeoTIFFs and GeoJSON
	•	🔍 Semantic Search: Knowledge-graph–powered entity lookup
	•	📑 Detail Panels: Contextual AI summaries and document citations
	•	🤖 AI Assistant: Conversational querying with cited sources

⸻

🗂️ Directory Layout

/web/
├─ src/
│  ├─ components/   # TimelineView, MapView, DetailPanel, AIAssistant, Legend
│  ├─ hooks/        # useTimelineWindow, useMapLayers, useHotkeys
│  ├─ context/      # AppContext (selection, time, layers)
│  ├─ utils/        # api.ts, geometry.ts, stac.ts, formatters.ts
│  ├─ styles/       # tokens.css (design tokens), global.css
│  └─ types/        # api.d.ts, graph.d.ts, stac.d.ts
├─ config/          # auto-generated: layers.json, app.config.json
├─ public/          # static assets
├─ package.json     # pinned dependencies
├─ vite.config.ts   # Vite build configuration
└─ README.md


⸻

⚡ Quickstart

# 1️⃣ Install dependencies
npm ci

# 2️⃣ Start dev server
npm run dev     # → http://localhost:5173

# 3️⃣ Build / preview / test
npm run build
npm run preview
npm run test

Requirements
	•	Node.js 18 + or 20 +
	•	npm 10 + (or pnpm / yarn)
	•	Backend running (FastAPI, see ../docs/sop.md)

⸻

⚙️ Environment Configuration

Create a .env file under /web/:

VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=https://basemaps.cartocdn.com/gl/positron-gl-style/style.json
VITE_APP_TITLE="Kansas Frontier Matrix"
VITE_ENABLE_AI_ASSISTANT=true

⚠️ Note: Never include secrets in the frontend.
Use only public, read-only environment variables prefixed with VITE_.

⸻

🔌 API Contracts

Endpoint	Method	Params / Body	Returns	Used By
/events	GET	start, end, bbox?, type?	Event[] (Feature[])	Timeline / Map
/entity/{id}	GET	—	EntityDossier	Detail Panel
/layers-config	GET	—	LayerDef[]	MapView / LayerControls
/search	GET	q, limit?	EntitySummary[]	SearchBar
/ask	POST	{ question }	{ answer, citations }	AIAssistant


⸻

🧩 Key Components

Component	Description
TimelineView (Canvas)	Virtualized temporal visualization with brush + playback
MapView (MapLibre GL)	Renders COG + GeoJSON layers; click → DetailPanel
LayerControls	Category filters, opacity sliders, layer toggles
DetailPanel	Summaries, citations, relations
SearchBar	Graph-linked autocomplete
AIAssistant	Conversational Q&A with source citations


⸻

🗺️ Data & Semantics
	•	Vectors: GeoJSON features with start, end, and type metadata
	•	Rasters: Cloud-Optimized GeoTIFFs with internal overviews
	•	STAC: data/stac/ → /web/config/layers.json (auto-generated)
	•	Ontologies: CIDOC CRM, OWL-Time, PeriodO for temporal context

⸻

🏗️ UI Architecture

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
    H["Layers Config · /layers-config (STAC)"]
  end

  C -->|GET /events| G
  D -->|GET /layers-config| H
  E -->|GET /entity/:id| G
  F -->|GET /search?q=...| G
%%END OF MERMAID%%


⸻

♿ Accessibility & Responsiveness
	•	Desktop: timeline + map side-by-side
	•	Tablet: collapsible drawers
	•	Mobile: tabbed interface (Map / Timeline / Details)

A11y Features
	•	ARIA roles + labels, keyboard shortcuts, skip-links
	•	← / → = pan time ± = zoom f = focus map s = focus search
	•	High-contrast palette · Color-blind-safe · Respects prefers-reduced-motion

⸻

🛡️ Security & Privacy
	•	HTTPS enforced in production
	•	Strict CORS & sanitized API responses
	•	AI output sanitized (no HTML injection)
	•	No analytics unless explicitly opt-in

⸻

🧠 Dev Experience & MCP
	•	CI/CD: GitHub Actions (Build · Lint · Test · Deploy)
	•	Static Analysis: CodeQL + Trivy
	•	Testing: Jest + React Testing Library ( npm test )
	•	Docs-First: All code linked to ../docs/architecture.md and SOPs
	•	Reproducible: Pinned deps · Deterministic Vite builds · STAC checksum CI

⸻

⚡ Performance Tips

Area	Optimization
Timeline (Canvas)	Batch-draw events · Offscreen buffers · requestAnimationFrame
Map (MapLibre)	Use COG with overviews · Cull hidden layers · Throttle hover
Network	Cache immutable assets · Brotli/Gzip · Code-split vendors


⸻

🧩 Developer Recipes

Add a New Map Layer

# 1️⃣  Create a STAC Item
# 2️⃣  Run ETL to rebuild layers.json
# 3️⃣  Launch dev server and verify LayerControls

Example – Minimal Vector Layer

map.addSource('trails', { type:'geojson', data:'/layers/trails.geojson' });
map.addLayer({ id:'trails-line', type:'line', source:'trails',
  paint:{ 'line-color':'#1f78b4','line-width':2 }});

Example – Raster COG

map.addSource('usgs1894', {
  type:'raster',
  tiles:['/tiles/usgs_topo_larned_1894.tif/{z}/{x}/{y}'],
  tileSize:256
});
map.addLayer({ id:'usgs1894', type:'raster', source:'usgs1894',
  paint:{ 'raster-opacity':0.8 }});


⸻

🧪 Troubleshooting

Issue	Check
Timeline empty	/events?start&end → valid UTC range
Missing layer	Exists in layers.json + correct URL/CORS
COG blurry	Has internal overviews · tile pattern correct
AI blank	/ask endpoint reachable · sanitize not over-stripping
Mermaid broken	Ensure fenced block (````mermaid`) and not inside HTML


⸻

🧾 Change Log

Version	Date	Author(s)	Notes
v1.6.0	2025-10-14	@kfm-web, @kfm-arch	Full rebuild · Unified ## headers · Hybrid metadata · Layout refresh
v1.5.0	2025-09-10	@kfm-web	Added STAC → layers.json build · Perf improvements
v1.4.0	2025-08-02	@kfm-web	Introduced AI Assistant · /ask integration


⸻

📚 References
	•	web/ARCHITECTURE.md — component flow & data links
	•	../docs/architecture.md — full system diagram
	•	../docs/sop.md — reproducibility procedures
	•	../docs/model_card.md — AI model details

⸻


<div align="center">


Kansas Frontier Matrix Web UI
Interactive Atlas of Kansas — Built for Discovery & Reproducibility

MIT License · MCP-DL v6.2 · Last Updated 2025-10-14

</div>
```  



⸻

✅ This version:
	•	Reads like your other premium KFM markdowns: balanced, minimal, and elegant.
	•	Has correct ## hierarchy for everything.
	•	Mermaid renders cleanly.
	•	The hybrid metadata is invisible but still MCP-valid.
	•	Ready to drop straight into web/README.md.
