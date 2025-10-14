<div align="center">


🌐 Kansas Frontier Matrix — Web Application

“Tracing the echoes of time where prairie meets code”

</div>



⸻


---
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
---


⸻

📚 Table of Contents
	•	Overview
	•	Architecture at a Glance
	•	Directory Layout
	•	Quickstart
	•	Environment Configuration
	•	API Contracts
	•	Key Components
	•	Data & Semantics
	•	Development & MCP Practices
	•	Performance Guide
	•	Troubleshooting
	•	Change Log
	•	References & Links

⸻

🧭 Overview

The Kansas Frontier Matrix Web Application fuses an interactive map and timeline with AI-assisted storytelling.
It visualizes Kansas’s history — terrain, people, treaties, climate, and archives — within a single interface powered by the Frontier Matrix Knowledge Graph.

Features
	•	🕰️ Timeline (Canvas) — smooth zoom/pan/playback
	•	🗺️ Map (MapLibre GL) — COG rasters + GeoJSON vectors
	•	🔎 Search — graph-powered entity discovery
	•	📜 Detail Panels — summaries, citations, relationships
	•	🤖 AI Assistant — contextual Q&A with provenance links

⸻

🏗️ Architecture at a Glance

flowchart TD
  A["User"] --> B["React SPA (Vite)"]
  B --> C["TimelineView (Canvas)"]
  B --> D["MapView (MapLibre GL)"]
  B --> F["SearchBar"]
  D --> E["DetailPanel"]

  subgraph Backend
    G["FastAPI /events /entity /search /ask"]
    H["Layers Config /layers-config (from STAC)"]
  end

  C <-->|time window| D
  C -->|GET /events| G
  D -->|GET /layers-config| H
  E -->|GET /entity/:id| G
  F -->|GET /search| G

<!-- END OF MERMAID -->


From data to dialogue — a spatial-temporal web built for Kansas.

⸻

🗂️ Directory Layout

/web/
├── src/
│   ├── components/   # TimelineView, MapView, LayerControls, DetailPanel, SearchBar
│   ├── hooks/        # useTimelineWindow, useMapLayers, useDebounce
│   ├── context/      # AppContext, ThemeProvider
│   ├── utils/        # api.ts, geometry.ts, stac.ts, time.ts
│   ├── styles/       # tokens.css, global.css
│   └── types/        # api.d.ts, graph.d.ts, stac.d.ts
├── config/           # generated: layers.json, app.config.json
├── public/           # favicon, manifest, icons
├── package.json
├── vite.config.ts
└── README.md


⸻

🚀 Quickstart

Prerequisites
	•	Node.js ≥ 18
	•	npm ≥ 10
	•	Running backend (FastAPI service)

cd web
npm ci
npm run dev         # http://localhost:5173
npm run build       # production build
npm run preview     # preview dist
npm run lint        # eslint + prettier
npm run test        # jest + testing-library/react


⸻

🔧 Environment Configuration

Create .env in /web/ (Vite reads VITE_*):

VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=https://basemaps.cartocdn.com/gl/positron-gl-style/style.json
VITE_APP_TITLE="Kansas Frontier Matrix"
VITE_ENABLE_AI_ASSISTANT=true

Notes
	•	Never store secrets in client env
	•	VITE_MAP_STYLE_URL can point to self-hosted tiles for offline use

⸻

🔌 API Contracts

Endpoint	Method	Params	Returns	Used By
/events	GET	start, end, bbox?, type?	Event[]	TimelineView, MapView
/entity/{id}	GET	—	EntityDossier	DetailPanel
/layers-config	GET	—	LayerDef[]	MapView
/search	GET	q, limit?	EntitySummary[]	SearchBar
/ask	POST	{ question }	{ answer, citations[] }	AIAssistant


⸻

🧩 Key Components
	•	🕰️ TimelineView: virtualized event rendering; keyboard hotkeys
	•	🗺️ MapView: interactive MapLibre GL map with layer controls
	•	🧭 LayerControls: toggles, opacity sliders, category filters
	•	📜 DetailPanel: linked entities, AI summaries, document excerpts
	•	🔎 SearchBar: async autocomplete; flyTo location
	•	🤖 AIAssistant: contextual Q&A from knowledge graph

⸻

🗺️ Data & Semantics

Type	Format	Description
Vectors	GeoJSON	Features with time + entity attributes
Rasters	Cloud-Optimized GeoTIFF (COG)	Terrain & historical maps
Metadata	STAC 1.0	Drives /web/config/layers.json
Ontologies	CIDOC CRM · OWL-Time · PeriodO	Semantic & temporal alignment


⸻

🛠️ Development & MCP Practices
	•	Documentation-first (MCP-DL v6.2)
	•	Deterministic Vite builds with pinned dependencies
	•	Continuous Integration (Build · Lint · Test · Deploy)
	•	STAC + CodeQL + Trivy security gates
	•	SHA-256 checksums for reproducibility
	•	Accessibility compliance (WCAG 2.1 AA)

⸻

⚡ Performance Guide
	•	Timeline: batch render via Canvas · debounced updates
	•	Map: COG with overviews · vector simplification
	•	Network: Brotli compression · lazy-load heavy components
	•	Frontend: code-splitting & cache-busting for static assets

⸻

🧪 Troubleshooting

Symptom	Check
Timeline empty	/events?start&end valid? UTC offset?
Layer missing	Listed in layers.json? visible flag true?
COG blurry/slow	Internal overviews present? correct URL?
AI answers blank	/ask endpoint reachable?
Mermaid not rendering	Code fence closed + <!-- END OF MERMAID --> added


⸻

🧾 Change Log

Version	Date	Author(s)	Summary
v1.6.0	2025-10-14	KFM Web Team	Rebuilt README to Root Architecture formatting
v1.5.0	2025-09-10	KFM Web Team	STAC integration & performance tuning
v1.4.0	2025-08-02	KFM Web Team	Added AI Assistant and improved docs


⸻

🔗 References & Links
	•	web/ARCHITECTURE.md
	•	../docs/architecture.md
	•	../docs/sop.md
	•	../docs/model_card.md

⸻


<div align="center">


🌾 Kansas Frontier Matrix — Explore Time, Terrain & Story
“Tracing the echoes of time where prairie meets code.”
MIT License · MCP-DL v6.2 · Updated 2025-10-14

</div>
