<div align="center">

# 🧭 Kansas Frontier Matrix — **Web Frontend**  
`web/src/`

**Interactive Map · Temporal Timeline · Knowledge Graph Interface**

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container--scan-secure-lightgrey)](../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix • Web Frontend (web/src/)"
version: "v1.7.0"
codename: "Interactivity & Provenance Upgrade"
last_updated: "2025-10-17"
owners: ["@kfm-web", "@kfm-architecture", "@kfm-design"]
status: "Stable"
maturity: "Production"
tags: ["react","typescript","vite","maplibre","canvas","timeline","stac","graph","ai","mcp"]
license: "MIT (code) | CC-BY 4.0 (docs)"
semantic_alignment:
  - CIDOC CRM
  - OWL-Time
  - DCAT 2.0
  - STAC 1.0
  - FAIR Principles
x-mcp:
  - Documentation-First
  - Provenance-Aware
  - Accessibility-Certified
  - Open-Standards
  - Audit-Ready
---


⸻

📜 Table of Contents
	•	🪶 Overview
	•	🏗 Mission & Design System
	•	⚙️ Architecture
	•	🗂 Directory Layout
	•	🧩 Components
	•	🚀 Quickstart
	•	🔌 API Contracts
	•	🧠 Data Flow
	•	⚙️ Configuration (Generated)
	•	♿ Accessibility & Responsiveness
	•	🛡 Security & Privacy
	•	🛠 DevEx & MCP Compliance
	•	⚡ Performance Checklist
	•	🧰 Troubleshooting
	•	🔗 Related Documentation
	•	📜 License & Credits

⸻

🪶 Overview

The KFM Web Frontend is a React 18+ single-page application (SPA) designed to visualize Kansas’s
historical, environmental, and cultural data layers via an interactive map, temporal timeline, and
knowledge graph-driven interface.

Key Attributes:
	•	🌍 Spatio-Temporal Synchronization — unified time window across map, timeline, and entities
	•	🧭 Knowledge Graph Context — entities and events drawn from a Neo4j + FastAPI backend
	•	🧠 AI Assistant Integration — contextual summaries and Q&A with citations
	•	🧩 STAC-Driven Configuration — dynamically generated layers.json from catalog metadata
	•	♿ WCAG-Compliant Design System — fully responsive, keyboard-navigable, color-tokenized UI

⸻

🏗 Mission & Design System

Mission:
Deliver an interactive, accessible, and provenance-aware storytelling interface linking Kansas’s geography,
history, ecology, and people into a unified temporal map system.

Design System Highlights:
	•	Tailwind-based token system (styles/variables.scss)
	•	Figma-aligned components and motion primitives
	•	Light/dark mode adaptive theming
	•	Accessible focus states, reduced motion settings
	•	AI-enhanced narrative components (citations, provenance overlays)

⸻

⚙️ Architecture

flowchart TD
  A["React SPA<br/>(web/src/)"] --> B["MapView<br/>(MapLibre GL JS)"]
  A --> C["TimelineView<br/>(HTML5 Canvas + D3)"]
  A --> D["SearchBar<br/>(Graph + REST Queries)"]
  A --> E["AI Panel<br/>(Q&A · Summaries · Citations)"]
  A --> F["DetailPanel<br/>(Entity/Event Dossiers)"]
  A --> G["LayerControls<br/>(STAC-Driven)"]

  B --> H["FastAPI Backend<br/>REST · GraphQL"]
  H --> I["Neo4j Knowledge Graph<br/>CIDOC CRM · OWL-Time"]
  H --> J["GeoAssets<br/>COG · GeoJSON · STAC"]

  I --> A
  J --> B
%% END OF MERMAID


⸻

🗂 Directory Layout

web/src/
├── components/              # Core UI modules
│   ├── MapView.tsx          # MapLibre instance + STAC layer loader
│   ├── TimelineView.tsx     # Temporal visualization via Canvas
│   ├── DetailPanel.tsx      # Entity/event dossiers
│   ├── SearchBar.tsx        # Knowledge graph search/autocomplete
│   ├── AIAssistant.tsx      # Contextual Q&A + provenance
│   ├── LayerControls.tsx    # Layer toggles & legends
│   └── index.ts             # Barrel export
│
├── context/                 # Global app state management
│   ├── AppContext.tsx
│   └── useGlobalState.ts
│
├── hooks/                   # Reusable custom hooks
│   ├── useMap.ts
│   ├── useTimeline.ts
│   ├── useStac.ts
│   └── useSearch.ts
│
├── styles/                  # Design tokens & TailwindCSS
│   ├── tailwind.css
│   ├── variables.scss
│   └── index.css
│
├── types/                   # Shared TypeScript types
│   ├── entities.d.ts
│   ├── api.d.ts
│   └── index.d.ts
│
├── utils/                   # Helper utilities
│   ├── api.ts
│   ├── formatters.ts
│   ├── geometry.ts
│   └── stac.ts
│
├── config/                  # Generated runtime configuration
│   ├── layers.json
│   ├── app.config.json
│   └── vite.config.ts
│
├── assets/                  # SVGs, icons, manifest.json
├── tests/                   # Unit & integration tests
└── index.tsx                # Application entry point


⸻

🧩 Components

Component	Purpose	Key Libraries
MapView	Basemap + STAC overlays (historical maps, hydrology, treaties)	maplibre-gl, react-map-gl
TimelineView	Temporal visualization (zoom, pan, brush)	d3-scale, d3-zoom, Canvas
SearchBar	Entity & event search across knowledge graph	axios, React Context
AI Panel	Summaries + citations from FastAPI/Graph endpoints	react-markdown
DetailPanel	Entity dossier, provenance trail, related nodes	react-markdown + UI Kit
LayerControls	STAC layer management & legends	React Hooks, STAC parser


⸻

🚀 Quickstart

# Clone & Install
git clone https://github.com/bartytime4life/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix/web
pnpm install

# Development
pnpm dev     # http://localhost:5173

# Build & Preview
pnpm build
pnpm preview

Environment Variables (.env):

VITE_API_URL=https://localhost:8000
VITE_MAP_STYLE_URL=/tiles/style.json
VITE_APP_MODE=development


⸻

🔌 API Contracts

Endpoint	Description	Example
/events?start=YYYY&end=YYYY&bbox=...	Retrieve events within time window	/events?start=1850&end=1900
/entity/{id}	Fetch entity dossier with relations	/entity/kansas_river
/search?q=term	Search graph entities and events	/search?q=railroad
/layers.json	STAC-generated config for map layers	/layers.json


⸻

🧠 Data Flow
	1.	STAC → layers.json — Automatically generated from catalog entries.
	2.	API → Knowledge Graph — REST/GraphQL routes query Neo4j using CIDOC CRM alignment.
	3.	Timeline Sync — Unified temporal window drives both map and graph queries.
	4.	AI Layer — Context-aware responses reference primary documents and metadata.

⸻

⚙️ Configuration (Generated)

config/layers.json is auto-generated by the ETL workflow:

{
  "id": "terrain_slope",
  "title": "Kansas Terrain Slope",
  "type": "raster",
  "source": "data/stac/terrain_slope.json",
  "license": "CC-BY 4.0",
  "time_range": ["1890-01-01", "2020-01-01"]
}

⚠️ Do not edit manually. Regenerate using the MCP ETL pipeline for reproducibility.

⸻

♿ Accessibility & Responsiveness
	•	WCAG 2.1 AA compliant colors, tokens, and focus states
	•	Full keyboard navigation and ARIA roles
	•	Responsive breakpoints for tablet and mobile
	•	Reduced motion toggle for timeline animations
	•	Screen-reader accessible tooltips and metadata summaries

⸻

🛡 Security & Privacy
	•	Client-side is read-only: no mutations or credentials
	•	CORS strictly limited to backend API
	•	HTTPS enforced for all network requests
	•	No personal data stored locally
	•	Provenance metadata displayed transparently

⸻

🛠 DevEx & MCP Compliance
	•	Docs-First: Changes require parallel documentation update
	•	Checksums: Artifact integrity verified in CI
	•	Open-Source Data Alignment: STAC + DCAT2.0
	•	Semantic Versioning: MAJOR.MINOR.PATCH structure
	•	Mermaid Enforcement: All diagrams end with %% END OF MERMAID
	•	Badging: CI and documentation badges verified weekly

⸻

⚡ Performance Checklist

✅ COG over GeoTIFF for rasters
✅ Lazy loading via Vite code-splitting
✅ WebGL tile rendering optimization
✅ Debounced timeline rendering (Canvas batch)
✅ Memoized React components
✅ Thread-safe async data fetching

⸻

🧰 Troubleshooting

Issue	Likely Cause	Resolution
Map fails to load	layers.json missing or invalid	Regenerate via pnpm run gen:layers
Timeline empty	API not returning events in time range	Check /events endpoint and console
404 for assets	Incorrect VITE_MAP_STYLE_URL	Update .env configuration
CORS error	Backend origin mismatch	Adjust FastAPI CORS middleware


⸻

🔗 Related Documentation
	•	docs/Kansas Frontier Matrix Documentation.pdf
	•	docs/Kansas Frontier Matrix Web UI Design Document.pdf
	•	docs/Kansas Frontier Matrix – Monorepo Repository Design.pdf
	•	docs/File and Data Architecture for KFM.pdf
	•	docs/Markdown styling guide.pdf

⸻

📜 License & Credits

License: MIT (Code) · CC-BY 4.0 (Docs/Data)
Copyright: © Kansas Frontier Matrix

Built under the Master Coder Protocol (MCP)
and aligned with Open Science & FAIR Principles.

⸻


<div align="center">


Kansas Frontier Matrix — Web Frontend v1.7.0
“Time · Terrain · Story — United Through Data.”

</div>
```
