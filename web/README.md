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
	•	⚙️ Configuration (generated)
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

The KFM Web Application combines an interactive timeline and map with AI-assisted context.
It renders COG rasters, GeoJSON vectors, and queries the Neo4j Knowledge Graph via FastAPI — dynamically discovering layers from a STAC catalog.

Features include:
	•	🕰 Timeline (Canvas): smooth zoom/pan/brush with animated playback
	•	🗺 Map (MapLibre GL): raster + vector rendering, hit-testing
	•	🔎 Search: graph-powered autocomplete & navigation
	•	📑 Detail Panels: AI summaries, citations, relationships
	•	🤖 AI Assistant: contextual Q&A with source links

⸻

🏗 Architecture at a Glance

flowchart TD
  A["User"] --> B["React SPA (Vite)"]
  B --> C["TimelineView (Canvas)"]
  B --> D["MapView (MapLibre GL)"]
  B --> F["SearchBar"]
  D --> E["DetailPanel"]

  subgraph Backend
    G["FastAPI · /events /entity /search /ask"]
    H["Layers Config · /layers-config (from STAC)"]
  end

  C <-->|time window| D
  C -->|GET /events| G
  D -->|GET /layers-config| H
  E -->|GET /entity/:id| G
  F -->|GET /search| G

<!-- END OF MERMAID -->



⸻

🗂 Directory Layout

/web/
├── src/
│   ├── components/   # TimelineView, MapView, LayerControls, DetailPanel, SearchBar, AIAssistant
│   ├── hooks/        # useTimelineWindow, useMapLayers, useDebounce, useHotkeys
│   ├── context/      # AppContext, ThemeProvider
│   ├── utils/        # api.ts, geometry.ts, stac.ts, time.ts
│   ├── styles/       # tokens.css, global.css
│   └── types/        # api.d.ts, graph.d.ts, stac.d.ts
├── config/           # generated layers.json, app.config.json
├── public/           # favicon, manifest, icons
├── package.json
├── vite.config.ts
└── README.md


⸻

🚀 Quickstart

Prerequisites
	•	Node.js 18+ (or 20+)
	•	npm 10+ (or pnpm/yarn)
	•	Running backend (see ../docs/sop.md)

cd web
npm ci
npm run dev        # http://localhost:5173
npm run build      # production build
npm run preview    # preview dist
npm run lint       # eslint + prettier
npm run test       # jest + testing-library


⸻

🔧 Environment Configuration

.env example (Vite uses VITE_* vars):

VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=https://basemaps.cartocdn.com/gl/positron-gl-style/style.json
VITE_APP_TITLE="Kansas Frontier Matrix"
VITE_ENABLE_AI_ASSISTANT=true

Notes:
	•	Never embed secrets — only public VITE_* variables
	•	For self-hosted tiles, update VITE_MAP_STYLE_URL

⸻

🔌 API Contracts

Endpoint	Method	Query / Body	Returns	Used By
/events	GET	start, end, bbox?, type?	Event[]	TimelineView, MapView
/entity/{id}	GET	—	EntityDossier	DetailPanel
/layers-config	GET	—	LayerDef[]	MapView
/search	GET	q, limit?	EntitySummary[]	SearchBar
/ask	POST	{ “question”: string }	{ “answer”: string, “citations”: [] }	AIAssistant


⸻

🧩 Key Components
	•	TimelineView: Canvas rendering, keyboard navigation, brush select
	•	MapView: Raster + vector GeoJSON layers, click → select → DetailPanel
	•	LayerControls: Toggles, opacity sliders, category filters
	•	DetailPanel: Dossier view (summary, relations, citations)
	•	SearchBar: Async autocomplete + flyTo on Enter
	•	AIAssistant: Embedded Q&A panel with citations

⸻

🗺 Data & Semantics
	•	Vectors: GeoJSON (with time attributes)
	•	Rasters: COGs (Cloud-Optimized GeoTIFFs)
	•	STAC 1.0: drives /web/config/layers.json
	•	Ontologies: CIDOC-CRM, OWL-Time, PeriodO

⸻

🧪 Troubleshooting

Symptom	Check
Timeline empty	/events params valid? UTC? bbox correct?
Layer missing	Exists in layers.json? CORS? zoom range?
COG blurry/slow	Has internal overviews? correct tiles URL?
AI answers blank	/ask reachable? sanitization too strict?
Mermaid not rendering	Ensure fenced ```mermaid + closing comment 


⸻

🧾 Change Log

Version	Date	Author(s)	Summary
v1.6.0	2025-10-14	KFM Web Team	Rebuilt README to MCP-DL v6.2, fixed Mermaid rendering
v1.5.0	2025-09-10	KFM Web Team	Added STAC → layers.json pipeline
v1.4.0	2025-08-02	KFM Web Team	Integrated AI Assistant panel


⸻

🔗 References & Links
	•	web/ARCHITECTURE.md
	•	../docs/architecture.md
	•	../docs/sop.md
	•	../docs/model_card.md

⸻


<div align="center">


KFM Web UI — Explore Kansas across time & space
MIT License · MCP-DL v6.2 · Last Updated 2025-10-14

</div>
```

