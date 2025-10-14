🧭 Kansas Frontier Matrix — Web Application

“Time · Terrain · History · Knowledge Graphs”


⸻


title: "Kansas Frontier Matrix — Web Application"
version: "v1.0.0"
last_updated: "2025-10-14"
authors: ["KFM Web Team"]
status: "Alpha"
maturity: "Active Development"
stack: ["React", "TypeScript", "MapLibre GL", "FastAPI", "Neo4j"]
license: "MIT (code) | CC-BY 4.0 (docs)"
alignment:
  - CIDOC CRM
  - OWL-Time
  - DCAT 2.0
  - STAC 1.0


⸻

📚 Table of Contents
	•	Overview
	•	Architecture at a Glance
	•	Directory Layout
	•	Getting Started (Dev)
	•	Running the App
	•	Environment & Secrets
	•	Testing & QA
	•	Accessibility (A11y)
	•	Data & Layers (STAC)
	•	CI/CD & Quality Gates
	•	Contributing

⸻

🧭 Overview

The KFM Web app is the interactive, map-and-timeline front end for the Kansas Frontier Matrix. It renders geotemporal data from the knowledge graph (Neo4j) via a FastAPI backend, lets users explore layers, and surfaces AI summaries (“site dossiers”) in context.  ￼  ￼
	•	MapLibre GL powers the GPU map; Canvas/D3 powers the timeline for high-density event rendering.  ￼
	•	The app emphasizes reproducibility (MCP), clear provenance, and standards-aligned metadata.  ￼  ￼

⸻

🏗️ Architecture at a Glance

Mermaid diagram (GitHub-safe) reflecting the thin-client UI and service boundaries:

flowchart LR
  U["User\nBrowser"] --> R["React SPA\nTimeline (Canvas) · MapLibre GL"]
  R -->|GraphQL/REST| A["FastAPI\nAPI Layer"]
  A --> N["Neo4j\nKnowledge Graph"]
  A --> S["Static Assets\nCOGs · GeoJSON · Tiles"]
  subgraph ETL/AI
    P["ETL Pipelines\nIngest · Normalize · STAC"] --> N
    P --> S
    M["AI/NLP\nNER · Summaries · Linking"] --> N
  end
  style R fill:#eef,stroke:#99f
  style A fill:#efe,stroke:#6c6
  style N fill:#ffe,stroke:#cc9
  style S fill:#f8f8f8,stroke:#bbb
  style P fill:#fff0f0,stroke:#f99
  style M fill:#fff0f0,stroke:#f99

%% END OF MERMAID
	•	UI focuses on visualization & interaction; heavy logic (querying, geospatial IO, AI) runs server-side.  ￼
	•	Data delivery relies on STAC-indexed COG/GeoJSON assets for fast, reproducible map layers.  ￼

⸻

🗂️ Directory Layout

Keep the web app isolated and clean inside the monorepo:

web/
├─ src/
│  ├─ components/         # MapView, Timeline, DetailPanel, LayerControls, Search
│  ├─ maps/               # Map styles, sources, layer defs
│  ├─ timeline/           # Canvas timeline modules
│  ├─ api/                # API client (REST/GraphQL)
│  ├─ state/              # Global state (Context/Redux)
│  ├─ utils/              # formatters, a11y helpers
│  └─ index.tsx
├─ public/                # static assets
├─ package.json
├─ vite.config.ts         # or webpack.config.js
└─ README.md              # this file

This structure aligns with the monorepo’s top-level blueprint and separations of concern.  ￼

⸻

⚡ Getting Started (Dev)

Prereqs
	•	Node 18+ / PNPM or NPM
	•	A running backend (FastAPI) and access to dev Neo4j (see /src backend docs)  ￼
	•	Map assets & STAC catalog available (local or remote)  ￼

Install & Run

# from repo root
cd web
pnpm install   # or npm i

# env: see .env.example below
pnpm dev       # or npm run dev

Environment variables (web/.env.local):

VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=/maps/style.json
VITE_STAC_INDEX_URL=/stac/index.json


⸻

🗺️ Data & Layers (STAC)

The app loads map sources (COG rasters, GeoJSON vectors) by reading the STAC index and attaching layers to MapLibre. Keep layers small and tiled when feasible.  ￼
	•	COG for rasters; GeoJSON/MBTiles for vectors.  ￼
	•	Historical topo sheets, DEM hillshades, soils, treaty polygons, hydrology, etc., are advertised via STAC Items.

⸻

🗺️+🕰️ Map & Timeline Concepts
	•	Map: MapLibre GL layers + hover/click interactions → opens DetailPanel with summary, sources, related entities.  ￼
	•	Timeline: Canvas draws dense events efficiently; zoom scales from decades to months; brushing updates map filters.  ￼
	•	AI Dossiers: Summaries for places/events powered by NER + cross-source linking; surfaced as readable context on selection.  ￼

⸻

🧪 Testing & QA
	•	Unit (Jest/RTL) for components and utilities.
	•	Integration tests for API client and render flows.
	•	Visual/Interaction checks for timeline performance (60fps target on typical data).  ￼
	•	Lint/Format via pre-commit hooks.  ￼

Run:

pnpm test
pnpm lint
pnpm typecheck


⸻

♿ Accessibility (A11y)

Follow WAI-ARIA patterns, keyboard navigation, color-contrast checks; ensure map overlays provide text equivalents / legends, and timeline is keyboard-operable.

⸻

🔐 Environment & Secrets
	•	Only non-sensitive map/style URLs in the frontend .env.
	•	Backend secrets never live in the web app. Reference the API gateway for protected data access.  ￼

⸻

🔁 CI/CD & Quality Gates
	•	Build, type-check, lint, test on PRs; enforce status checks before merge.  ￼
	•	Optionally deploy preview builds for docs/site.
	•	Validate STAC links in PR (fail if broken).  ￼

⸻

🤝 Contributing

Please read the project’s contribution guidelines and MCP-style documentation practice. Add or modify UI with tests, docs, and reproducible demos.  ￼  ￼

⸻

🔗 Cross-References
	•	System Design (Knowledge Hub) – end-to-end pipeline & KG APIs.  ￼
	•	Web UI Design Document – component contracts, UX flows.  ￼
	•	Monorepo Design – repository layout & governance.  ￼
	•	File & Data Architecture (STAC, COG, GeoJSON) – data supply to the web app.  ￼
	•	AI/NLP Developer Doc – summaries, NER, linking.  ￼
	•	Design Audit (Gaps & Enhancements) – uncertainty, storytelling, simulations.  ￼
	•	GUI Engineering Guide (Cross-platform UI principles) – event loops, retained vs immediate mode, declarative UI cues.  ￼

⸻

📜 License

Code © KFM under MIT; documentation under CC-BY 4.0.

⸻

“Make it reproducible. Make it explorable. Make it Kansas.”