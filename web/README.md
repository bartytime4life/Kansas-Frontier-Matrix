<div align="center">


🌐 Kansas Frontier Matrix — Web Application

/web/

Interactive · Temporal · Spatial · Narrative

</div>


⸻

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

🧭 Overview

The Kansas Frontier Matrix Web Application is the interactive exploration layer of the Frontier-Matrix system — a visualization engine for time-aware, spatially-anchored historical data.
Built with React + MapLibre GL JS, it merges temporal and geospatial narratives into a single interface that lets users traverse Kansas history dynamically through maps, timelines, and AI-generated insights.

It connects directly to the FastAPI / Neo4j knowledge graph backend, rendering historical datasets (treaties, settlements, hydrology, climate records, oral histories) through time-synchronized map layers and entity panels ￼ ￼.

⸻

🏗️ Architecture at a Glance

flowchart TD
  A["FastAPI Backend<br/>REST + GraphQL Endpoints"]
    --> B["React Web Client<br/>TypeScript · Vite · Tailwind"]
  B --> C["Timeline View<br/>Canvas · D3 · OWL-Time"]
  B --> D["Map View<br/>MapLibre GL · COG · GeoJSON"]
  B --> E["Knowledge Graph<br/>Neo4j · CIDOC CRM · SPARQL"]
  D --> F["AI Pipeline<br/>spaCy · Transformers · Summarizer"]
  E --> G["User Interaction Layer<br/>Filters · Queries · Playback"]
  G --> B
%% END OF MERMAID

Every visual component synchronizes in real-time — selecting an event in the timeline highlights its location on the map, while panning the map updates the visible temporal window.

⸻

🗂️ Directory Layout

web/
├── src/
│   ├── components/     # React UI modules — Map, Timeline, Panels, Search
│   ├── hooks/          # Shared React hooks (useMap, useTimeline)
│   ├── pages/          # Route-level views (Home, Explore, Admin)
│   ├── styles/         # Tailwind / SCSS configs
│   ├── assets/         # Icons, images, JSON style sheets
│   ├── types/          # Shared TypeScript definitions
│   ├── utils/          # Helper libs (API clients, formatters)
│   └── main.tsx        # Application entrypoint
│
├── public/             # Static assets served at build time
├── package.json        # Node dependencies
├── vite.config.ts      # Vite build configuration
└── tsconfig.json       # TypeScript settings

⸻

⚙️ Technology Stack

Layer	Framework / Tool	Purpose
Frontend Core	React 18 + TypeScript	Modular component architecture
Mapping Engine	MapLibre GL JS	Interactive vector/raster rendering
Timeline Renderer	HTML5 Canvas + D3.js	Smooth, scalable chronology
API Layer	Axios / GraphQL Client	Connects to FastAPI/Neo4j
UI Framework	Tailwind + ShadCN-UI	Unified, responsive design
Build System	Vite + ESLint + Prettier	Modern development pipeline
Testing	Jest + React Testing Library	Unit & integration coverage
Accessibility	WAI-ARIA · WCAG 2.1 AA	Inclusive, keyboard-first UX

⸻

🧩 Core Features

🗺️ Map Engine
	•	MapLibre GL-based temporal viewer with STAC-registered layers.
	•	Supports COG rasters (DEM, hillshade, historic maps) and GeoJSON vectors (trails, treaties).
	•	Layer visibility bound to timeline range.

🕰️ Timeline
	•	GPU-accelerated HTML5 Canvas timeline with OWL-Time period linking.
	•	Scroll, zoom, and play through Kansas history from 1800 → Present.
	•	PeriodO eras (e.g., Territorial Kansas, Dust Bowl) automatically labeled.

🔍 Knowledge Graph Search
	•	Federated semantic search across People, Places, Events.
	•	Contextual results highlight relationships in map + timeline simultaneously.
	•	Queries resolved via Neo4j GraphQL endpoint.

🤖 AI-Assisted Summaries
	•	spaCy NER + transformer summarizers produce site dossiers and contextual narratives.
	•	Each AI output includes provenance and confidence metadata per MCP standards ￼.

🧰 Admin Console
	•	Secure role-based tools for curators to validate, tag, or correct extracted entities.
	•	Source linking and audit trails preserve full provenance (MCP chain-of-evidence).

⸻

🚀 Development & Build

# Install dependencies
npm install

# Launch development server
npm run dev

# Build production bundle
npm run build

# Lint & test
npm run lint && npm test

Environment variables (in .env) define API and map endpoints:

VITE_API_URL="http://localhost:8000/api"
VITE_MAP_STYLE="/assets/styles/kfm-style.json"

⸻

🧪 Testing & CI Pipeline
	•	✅ Unit Tests — React components and helpers via Jest.
	•	🔁 Integration — Timeline↔Map synchronization & API contract checks.
	•	🧩 CI/CD — GitHub Actions run lint/build/test + deploy to GitHub Pages (site.yml).
	•	🔒 Security — Automated scans: Trivy (Security), CodeQL (SAST).

⸻

📘 Documentation & MCP Compliance

All modules in /web/ follow Master Coder Protocol v6.2:
	•	Inline doc-strings and version headers per component.
	•	Corresponding entries in /docs/web/ with diagrams and usage.
	•	Changes trigger automated doc validation in CI (Docs-MCP badge).

This guarantees provenance, reproducibility, and clarity across all front-end workflows.

⸻

🪪 License
	•	Code: MIT License
	•	Documentation / Content: CC-BY 4.0
	•	See LICENSE and CITATION.cff for citation & reuse details.

⸻

<div align="center">


🧭 “Time · Terrain · History · Knowledge Graphs”

Kansas Frontier Matrix — Open-Source Digital Atlas of Kansas

© 2025 Frontier-Matrix Contributors

</div>


⸻

That’s the fully restored fancy version — with all of your project’s emblematic styling intact (emojis, dividers, centered branding, YAML header, and glyph layout).

Would you like me to now generate matching sub-READMEs for
web/src/components/, web/src/types/, and web/src/utils/ in the same MCP-DL format?