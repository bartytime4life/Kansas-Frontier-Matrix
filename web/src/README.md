<div align="center">


🧭 Kansas Frontier Matrix — Web Frontend

web/src/

Purpose: Interactive map + timeline UI for Kansas Frontier Matrix — React + MapLibre + Canvas, driven by a Neo4j-backed API and MCP-quality docs & pipelines.

</div>



⸻


---
title: "KFM • Web Frontend (web/src/)"
version: "v1.6.0"
last_updated: "2025-10-17"
owners: ["@kfm-web", "@kfm-architecture"]
tags: ["react","typescript","maplibre","canvas","timeline","vite","stac","mcp"]
license: "MIT"
semantic_alignment:
  - CIDOC CRM
  - OWL-Time
  - STAC 1.0
  - DCAT 2.0
---


⸻

📚 Table of Contents
	•	🪶 Overview
	•	🏗 Architecture
	•	🗂 Directory Layout
	•	🧩 Components
	•	🚀 Quickstart
	•	🔌 API Contracts
	•	🧠 Data Flow
	•	⚙️ Configuration (generated)
	•	♿ Accessibility & Responsiveness
	•	🛡 Security & Privacy
	•	🛠 DevEx & MCP
	•	⚡ Performance Checklist
	•	🧑‍💻 Developer Cheatsheet
	•	🧰 Troubleshooting
	•	🔗 Related Docs
	•	📜 License

⸻

🪶 Overview

The KFM Web Frontend is a React 18+ SPA that pairs a MapLibre map with a Canvas-driven timeline to explore Kansas’s people–places–events across time. It reads from a FastAPI layer backed by a Neo4j knowledge graph, aligned to CIDOC CRM and OWL-Time, and surfaces AI summaries where helpful. Design goals and UI behavior follow the Web UI Design Document and system docs.

Why this shape? The frontend is the thin, interactive shell; heavy logic (ETL/AI/graph) lives server-side per KFM architecture.

⸻

🏗 Architecture

flowchart TD
  A["React SPA<br/>(web/src/)"] --> B["MapView<br/>(MapLibre GL JS)"]
  A --> C["TimelineView<br/>(HTML5 Canvas)"]
  A --> D["SearchBar<br/>(Graph queries)"]
  A --> E["AI Panel<br/>(summaries, citations)"]
  A --> F["DetailPanel<br/>(entity dossiers)"]
  A --> G["LayerControls<br/>(STAC-driven)"]

  B --> H["FastAPI Backend<br/>REST · GraphQL"]
  C --> H
  D --> H
  E --> H
  F --> H
  G --> H

  H --> I["Neo4j Knowledge Graph<br/>CIDOC CRM · OWL-Time"]
  H --> J["Geodata Assets<br/>COGs · GeoJSON · STAC"]

  I -.-> A
  J -.-> B
%% END OF MERMAID

References: Web UI stack & SPA/API split, knowledge-graph integration, and map/timeline linkage.

⸻

🗂 Directory Layout

web/src/
├─ components/              # UI building blocks
│  ├─ MapView.tsx           # MapLibre instance & layer orchestration
│  ├─ TimelineView.tsx      # Canvas timeline (zoom/pan/brush)
│  ├─ DetailPanel.tsx       # Entity/event dossiers with citations
│  ├─ SearchBar.tsx         # Graph search + autocomplete
│  ├─ AIAssistant.tsx       # Summaries & context
│  ├─ LayerControls.tsx     # STAC-driven layer toggles & legends
│  └─ index.ts
├─ context/                 # App-level state & providers
├─ hooks/                   # useMap/useTimeline/useStac/useSearch
├─ styles/                  # Tailwind/CSS tokens
├─ types/                   # Shared TypeScript types
├─ utils/                   # API client, formatters, geometry, stac helpers
├─ config/                  # generated: layers.json, app.config.json, vite.config.ts
├─ assets/                  # SVGs, icons, manifest
└─ index.tsx                # App entry

Keep this layout consistent with monorepo patterns and docs-first approach.

⸻

🧩 Components

Component	Purpose	Key libs / notes
MapView	Basemap + overlays (historic maps, treaties, hydrology, settlements)	maplibre-gl; STAC-fed COG/GeoJSON; time filtering via style filters.
TimelineView	Canvas timeline (range zoom, brush, playhead sync to map)	HTML5 Canvas; D3 scales/zoom; perf guidance in Canvas notes.
SearchBar	Entity/event/place search with graph-powered facets	FastAPI→Neo4j queries (people/places/events).
AIAssistant	Summaries of places/events with citations to sources	Server-side AI per KFM AI docs.
DetailPanel	Dossiers: attributes, links, map snippets, timeline pins	Knowledge graph joins; provenance visible.
LayerControls	Toggle layers from STAC; legends; opacity/time filters	STAC & file architecture integration.


⸻

🚀 Quickstart

# 1) Install
pnpm install   # or npm/yarn

# 2) Dev server
pnpm dev       # starts Vite dev server on http://localhost:5173 (default)

# 3) Env vars (example)
cp .env.example .env
# FRONTEND_*
# API_BASE_URL=https://localhost:8000
# MAP_STYLE_URL=/tiles/style.json

# 4) Build & preview
pnpm build
pnpm preview

Backends & data are expected per KFM system docs: FastAPI, Neo4j, and STAC-indexed assets (COG/GeoJSON).

⸻

🔌 API Contracts

Minimal, stable endpoints the UI expects (FastAPI):
	•	GET /events?start=YYYY&end=YYYY&bbox=... → time-windowed events with minimal geom.
	•	GET /entity/{id} → entity dossier (fields, relations, citations).
	•	GET /search?q=... → mixed results (people/places/events + facets).
	•	GET /layers.json → generated display config from STAC (raster/vector layers).

The SPA is read-only for general users; admin endpoints are gated.

⸻

🧠 Data Flow
	•	STAC → layers.json: The ETL catalogs COGs/GeoJSON in data/stac/; a build step produces web/src/config/layers.json consumed by MapView.
	•	Graph → API: Neo4j encodes People/Places/Events with CIDOC/OWL-Time semantics; API resolves queries, performs joins, and returns lean payloads.
	•	Timeline sync: Time brush updates both map style filters and API calls to ensure coherent spatio-temporal selection.

⸻

⚙️ Configuration (generated)

web/src/config/layers.json is generated from STAC Items (raster COGs, vector GeoJSON), preserving:
	•	id, title, attribution/license, time range, bbox, tiling metadata (COG), display hints (opacity, z-index, legend).
	•	Do not edit by hand. Update sources in data/sources/*.json and re-run the pipeline.

⸻

♿ Accessibility & Responsiveness
	•	Keyboard & ARIA: Focus states on interactive map controls; trap focus in modals/panels; role semantics on nav and controls. See HTML5/ARIA notes.
	•	Color/contrast: Tokenized colors in styles/ to maintain AA contrast in map UI and timeline.
	•	Responsive layout: Map + timeline coexist on desktop; on mobile, panels collapse/toggle; avoid oversized tables per styling guide.

⸻

🛡 Security & Privacy
	•	Run heavy logic server-side (API); no secrets in client bundle.
	•	Avoid PII; show provenance/citations only; respect source licenses surfaced via STAC/metadata.
	•	General GUI guidance & event-driven patterns: main-thread UI; offload long tasks.

⸻

🛠 DevEx & MCP
	•	Docs-as-code: Every UI change updates docs & READMEs; consistent centered headers, badges, TOC, and emoji headings per KFM Markdown rules.
	•	Monorepo: Co-evolution with src/ (ETL) and data/ (STAC); atomic PRs with CI gates.
	•	Style & mermaid: Use strict Mermaid blocks and close with %% END OF MERMAID.

⸻

⚡ Performance Checklist
	•	Canvas timeline: prefer Canvas over SVG for dense series; avoid per-frame layout thrash; batch draw.
	•	Map layers: use COG for rasters, simplified GeoJSON (or vector tiles) for large vectors; filter by time on-style where possible.
	•	Code-split routes/panels; memoize selectors; throttle window resize & timeline drag.

⸻

🧑‍💻 Developer Cheatsheet

# Lint & type-check
pnpm lint && pnpm typecheck

# Run e2e unit tests (if configured)
pnpm test

# Regenerate layers.json from STAC (example task)
pnpm run gen:layers


⸻

🧰 Troubleshooting
	•	No layers appear: Ensure layers.json exists and STAC Items reference valid COG/GeoJSON URLs.
	•	Time filter empty: Verify events API returns within [start,end]; check bbox filter.
	•	Canvas jitter: Reduce draw frequency; debounce hover; confirm devicePixelRatio handling.

⸻

🔗 Related Docs
	•	Web UI Design Document — interaction flows, layout, and component specs.
	•	System Documentation (Public) — mission, knowledge-graph, storytelling features.
	•	AI System – Developer Docs — ETL, NLP, summarization, graph linking.
	•	STAC & File Architecture — sources, raw/processed, catalogs.
	•	Design Audit & Gaps — enhancements & analysis opportunities.
	•	Markdown Rules / Styling — headers, emojis, TOC, mermaid, badges.

⸻

📜 License

MIT (code) · CC-BY 4.0 (docs/content)
© Kansas Frontier Matrix. See repository LICENSE and data attributions via STAC Items.