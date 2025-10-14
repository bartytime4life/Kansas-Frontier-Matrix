🧩 Kansas Frontier Matrix — Web Frontend

“Time · Terrain · History · Knowledge Graphs”


⸻


---
title: "Kansas Frontier Matrix — Web Frontend"
version: "v1.6.0"
last_updated: "2025-10-14"
authors: ["KFM Web Team"]
status: "Stable"
maturity: "Production"
tags: ["web","react","vite","typescript","maplibre","timeline","stac","mcp"]
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
	•	Technology Stack
	•	Core Features
	•	Quickstart
	•	Environment & Config
	•	API Integration
	•	Testing & CI/CD
	•	Accessibility & UX
	•	Styling & Theming
	•	Versioning & Governance
	•	Change Log
	•	References

⸻

🧭 Overview

The Web Frontend is the interactive layer of the Kansas Frontier Matrix (KFM): a React + MapLibre application that binds time (timeline) to space (map) and story (AI-assisted summaries, knowledge graph links). It visualizes treaty polygons, trails, hydrology, climate and archival narratives — synchronized through a semantic backend (Neo4j + FastAPI) aligned to CIDOC CRM and OWL-Time.

⸻

🏗️ Architecture at a Glance

flowchart TD
  A["Sources<br/>maps · rasters · vectors · text archives"]
    --> B["ETL Pipeline<br/>Makefile · GDAL · Checksums"]
  B --> C["Processed Layers<br/>COG · GeoJSON · CSV"]
  B --> I["AI/ML Enrichment<br/>NER · OCR · Geocoding · Summaries"]
  C --> D["STAC Catalog<br/>Collections · Items · Assets"]
  D --> H["Knowledge Graph<br/>Neo4j · CIDOC CRM · OWL-Time"]
  I --> H
  D --> J["API Layer<br/>FastAPI · GraphQL · REST"]
  H --> J
  J --> F["Web Frontend (React + MapLibre)<br/>Map · Timeline · AI Panels"]
%% END OF MERMAID

From raw archives to semantic graphs to interactive storytelling.

⸻

🗂️ Directory Layout

web/
├─ src/
│  ├─ components/      # Map, Timeline, Panels, Search, Legends
│  ├─ hooks/           # useMap, useTimeline, useStac, useSearch
│  ├─ pages/           # Home, Explore, Admin
│  ├─ styles/          # Tailwind / SCSS / tokens
│  ├─ assets/          # Icons, map styles, images
│  ├─ types/           # Shared TypeScript interfaces
│  ├─ utils/           # API client, formatters, helpers
│  └─ main.tsx         # App entry
│
├─ public/             # Static assets served at build
├─ package.json        # Dependencies and scripts
├─ vite.config.ts      # Vite configuration
└─ tsconfig.json       # TypeScript configuration


⸻

⚙️ Technology Stack

Layer	Tech	Purpose
Core	React 18 + TypeScript	Modular SPA architecture
Mapping	MapLibre GL JS	Vector/raster rendering (COG/GeoJSON)
Timeline	HTML5 Canvas + D3	Smooth, scalable chronology
API	Fetch / Axios / GraphQL client	FastAPI + Graph endpoints
Tooling	Vite · ESLint · Prettier	Fast builds, formatting & linting
Testing	Jest · React Testing Library	Unit/integration coverage
UI	Tailwind / shadcn-ui	Aesthetic, accessible components
A11y	WAI-ARIA · WCAG 2.1 AA	Keyboard-first, screen-reader friendly


⸻

🧩 Core Features

🗺️ Map + Layers
	•	Temporal MapLibre viewer with STAC-registered overlays
	•	COG rasters (DEM, hillshade, historic sheets), GeoJSON vectors (trails, treaties, hydrology)
	•	Layer visibility bound to timeline range; legends and semantic filters

🕰️ Timeline
	•	GPU-accelerated Canvas timeline with zoom, pan, and playback
	•	OWL-Time & PeriodO era labels (e.g., Territorial Kansas, Dust Bowl)
	•	Selecting a timeslice updates map; selecting a map feature focuses timeline

🔎 Knowledge Graph Search
	•	Finds People · Places · Events, returns linked context
	•	One-click centering on the map + pin on the timeline
	•	Graph-aware facets (role, era, region)

🤖 AI Summaries (MCP-aligned)
	•	NER + summarization to assemble site dossiers
	•	Provenance + confidence inline; curator review workflows

🛠️ Admin Console
	•	Role-based curation: validate entities, link sources, adjust geometries
	•	Audit trails preserve chain-of-evidence (MCP)

⸻

⚡ Quickstart

# 1) Install dependencies
npm install

# 2) Start dev server
npm run dev

# 3) Build production assets
npm run build

# 4) Lint and test
npm run lint && npm test


⸻

🔧 Environment & Config

Create a .env (or .env.local) with:

VITE_API_URL="http://localhost:8000/api"
VITE_MAP_STYLE="/assets/styles/kfm-style.json"
VITE_MAP_TOKEN=""   # if using a private tiles host (optional)


⸻

🔌 API Integration

Frontend calls FastAPI/Graph endpoints:

const API = import.meta.env.VITE_API_URL ?? "http://localhost:8000/api";

export async function fetchEvents(start: string, end: string) {
  const res = await fetch(`${API}/events?start=${start}&end=${end}`);
  if (!res.ok) throw new Error("Failed to load events");
  return res.json();
}

export async function search(q: string) {
  const res = await fetch(`${API}/search?q=${encodeURIComponent(q)}`);
  return res.json();
}

STAC items for layers are loaded at runtime to auto-register COG/GeoJSON sources in MapLibre.

⸻

🧪 Testing & CI/CD
	•	Unit tests: npm test (Jest + RTL)
	•	Integration: Map↔Timeline sync, API contracts
	•	CI: GitHub Actions — lint, test, build, STAC validation, pages deploy
	•	Security: CodeQL (SAST) + Trivy scans
	•	Pre-commit: formatting, linting, Markdown & Mermaid checks

⸻

♿ Accessibility & UX
	•	Keyboard-navigable map controls and timeline focus rings
	•	Descriptive ARIA roles/labels for markers and event groups
	•	Color-contrast-safe theme; motion reduced when prefers-reduced-motion is set

⸻

🎨 Styling & Theming
	•	Design tokens: spacing, type scale, z-layers, radii
	•	Map theme: neutral terrain, high-contrast overlays, period-aware palettes
	•	Components: shadcn-ui + Tailwind utilities for clean, consistent UI

⸻

🧭 Versioning & Governance

Domain	Mechanism	Notes
Code	SemVer	vMAJOR.MINOR.PATCH
Docs	docs/CHANGELOG.md	Render-safe MCP-DL
Data	STAC properties.version	Per-layer version
Releases	GitHub Tag + DOI	Citable snapshots
Governance	GOVERNANCE.md	Roles, review, merge rules


⸻

🧾 Change Log

Version	Date	Author	Summary
v1.6.0	2025-10-14	Web Team	Align README to MCP-DL v6.2; UX/A11y pass
v1.5.0	2025-10-10	Web Team	Timeline zoom improvements; map legends
v1.4.0	2025-09-15	Web Team	STAC autoload + layer registry
v1.3.0	2025-08-20	Web Team	AI dossiers (curator-review)
v1.2.0	2025-07-05	Web Team	Stable map/timeline sync
v1.0.0	2025-06-01	Project Init	Initial web frontend


⸻

📚 References
	•	System Architecture (/docs/architecture.md)
	•	Web UI Design (/docs/)
	•	File & Data / STAC (/docs/)
	•	AI/ML Developer Docs (/docs/)
	•	MCP — Scientific Method & SOPs (/docs/)

⸻

Made with ❤️ for Kansas — bridging history, climate, and technology.
Automation with Integrity · Every Workflow Proven · Versioned for Future Scholars.