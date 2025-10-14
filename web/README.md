
⸻

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

The Web Frontend is the interactive exploration layer of the Kansas Frontier Matrix (KFM) — a React + MapLibre single-page application binding time · space · story.
It visualizes treaties, trails, hydrology, climate and archival narratives synchronized with the FastAPI / Neo4j semantic backend aligned to CIDOC CRM and OWL-Time.

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


⸻

🗂️ Directory Layout

web/
├─ src/
│  ├─ components/  # Map · Timeline · Panels · Search · Legends
│  ├─ hooks/     # useMap · useTimeline · useStac · useSearch
│  ├─ pages/     # Home · Explore · Admin
│  ├─ styles/     # Tailwind / SCSS tokens
│  ├─ assets/     # Icons · map styles · images
│  ├─ types/      # Shared TypeScript interfaces
│  ├─ utils/      # API client · formatters · helpers
│  └─ main.tsx     # App entrypoint
│
├─ public/      # Static assets at build
├─ package.json    # Dependencies & scripts
├─ vite.config.ts   # Vite configuration
└─ tsconfig.json   # TypeScript settings


⸻

⚙️ Technology Stack

Layer	Technology	Purpose
Core	React 18 + TypeScript	Modular SPA architecture
Mapping	MapLibre GL JS	Vector/raster rendering
Timeline	HTML5 Canvas + D3	Smooth interactive chronology
API	Fetch / Axios / GraphQL	Connects FastAPI ↔ Neo4j
Tooling	Vite · ESLint · Prettier	Fast builds · lint · format
Testing	Jest · RTL	Unit + integration coverage
UI	Tailwind / shadcn-ui	Accessible design system
A11y	WAI-ARIA · WCAG 2.1 AA	Keyboard-first UX


⸻

🧩 Core Features

🗺️ Map + Layers
	•	Temporal MapLibre viewer with STAC overlays
	•	COG rasters + GeoJSON vectors (trails · treaties · hydrology)
	•	Layer visibility linked to timeline range

🕰️ Timeline
	•	Canvas-based zoom/pan/playback
	•	OWL-Time + PeriodO era labels
	•	Click timeline → map focus; click map → timeline highlight

🔎 Knowledge Graph Search
	•	Queries People · Places · Events
	•	Returns linked context + map centering
	•	Graph-aware facets (role · era · region)

🤖 AI Summaries
	•	NER + Transformers generate site dossiers
	•	Provenance + confidence displayed per MCP

🛠️ Admin Console
	•	Role-based curation · entity validation · source linking
	•	Audit trail ensures chain-of-evidence

⸻

⚡ Quickstart

npm install
npm run dev
npm run build
npm run lint && npm test


⸻

🔧 Environment & Config

VITE_API_URL="http://localhost:8000/api"
VITE_MAP_STYLE="/assets/styles/kfm-style.json"


⸻

🔌 API Integration

const API = import.meta.env.VITE_API_URL || "http://localhost:8000/api";

export async function fetchEvents(start:string,end:string){
 const r = await fetch(`${API}/events?start=${start}&end=${end}`);
 return r.json();
}


⸻

🧪 Testing & CI/CD
	•	Jest + RTL unit/integration tests
	•	CI: lint · test · build · STAC validation · deploy
	•	Security: CodeQL + Trivy
	•	Pre-commit hooks: Markdown · Mermaid · YAML lint

⸻

♿ Accessibility & UX
	•	Full keyboard nav + ARIA landmarks
	•	High-contrast map themes · reduced-motion support

⸻

🎨 Styling & Theming
	•	Tailwind tokens for spacing, type, z-layers
	•	Sepia/terrain basemaps for historic modes

⸻

🧭 Versioning & Governance

Domain	Mechanism	Notes
Code	SemVer	vMAJOR.MINOR.PATCH
Docs	docs/CHANGELOG.md	MCP-DL v6.2
Data	STAC properties.version	Per layer
Releases	Tag + DOI	Citable
Governance	GOVERNANCE.md	Roles · merge rules


⸻

🧾 Change Log

Version	Date	Author	Summary
v1.6.0	2025-10-14	Web Team	Aligned README to MCP-DL v6.2
v1.5.0	2025-10-10	Web Team	Timeline zoom · map legend
v1.4.0	2025-09-15	Web Team	STAC autoload · layer registry
v1.3.0	2025-08-20	Web Team	AI dossiers · curator review
v1.2.0	2025-07-05	Web Team	Stable map/timeline sync
v1.0.0	2025-06-01	Init	Initial release


⸻

📚 References
	•	System Architecture (/docs/architecture.md)
	•	Web UI Design (/docs/)
	•	File & Data STAC (/docs/)
	•	AI/ML Developer Docs (/docs/)
	•	Master Coder Protocol (/docs/)

⸻

Made with ❤️ for Kansas — bridging history, climate and technology.
Automation with Integrity · Every Workflow Proven · Versioned for Future Scholars.

⸻
