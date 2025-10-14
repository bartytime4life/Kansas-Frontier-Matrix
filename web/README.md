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
stack: ["React + Vite", "TypeScript", "MapLibre GL", "FastAPI", "Neo4j"]
license: "MIT (code) | CC-BY 4.0 (docs)"
alignment:
  - CIDOC CRM
  - OWL-Time
  - DCAT 2.0
  - STAC 1.0


⸻

📚 Table of Contents
	•	🧭 Overview
	•	🏗️ Architecture at a Glance
	•	🗂️ Directory Layout
	•	⚡ Quickstart
	•	🧩 Map & Timeline Core
	•	📡 API & Knowledge Graph
	•	🧪 Testing & QA
	•	♿ Accessibility (A11y)
	•	🔁 CI/CD Pipelines
	•	🤝 Contributing
	•	📎 References

⸻

🧭 Overview

The Kansas Frontier Matrix Web App provides the interactive user interface—a fusion of map, timeline, and knowledge-graph exploration.
It connects historical, ecological, and cultural layers of Kansas through reproducible, STAC-driven geospatial assets and AI-assisted narrative discovery.
	•	Framework: React + Vite (TypeScript)
	•	Mapping: MapLibre GL + COG raster overlays
	•	Data: STAC catalog → FastAPI → Neo4j Knowledge Graph
	•	AI: Natural-language summaries + entity linking
	•	Compliance: Master Coder Protocol (MCP) v6.2 for provenance and reproducibility

⸻

🏗️ Architecture at a Glance

flowchart TD
  A["Sources<br/>maps · rasters · vectors · text archives"]
    --> B["ETL Pipeline<br/>Python Makefile · GDAL · Checksums"]
  B --> C["Processed Layers<br/>COG · GeoJSON · CSV"]
  B --> I["AI/ML Enrichment<br/>NER · OCR · Geocoding · Summaries"]
  C --> D["STAC Catalog<br/>Collections · Items · Assets"]
  D --> H["Knowledge Graph<br/>Neo4j · CIDOC CRM · OWL-Time"]
  I --> H
  D --> J["API Layer<br/>FastAPI · GraphQL"]
  J --> W["Web Frontend<br/>React · MapLibre · Timeline"]
  W --> U["User Interface<br/>Exploration · AI Summaries · Downloads"]
%% END OF MERMAID


⸻

🗂️ Directory Layout

web/
├── src/
│   ├── components/         # UI elements (MapView, Timeline, Panels)
│   ├── maps/               # MapLibre styles & layer definitions
│   ├── timeline/           # Temporal visualization (Canvas/D3)
│   ├── api/                # FastAPI/GraphQL clients
│   ├── state/              # Zustand or Redux store
│   ├── utils/              # Shared helpers and formatters
│   ├── types/              # TypeScript interfaces (MCP-DL)
│   └── index.tsx
├── public/                 # Static assets (favicons, logos)
├── vite.config.ts
├── package.json
└── README.md


⸻

⚡ Quickstart

🧩 Prerequisites
	•	Node 18 + PNPM or NPM
	•	Running backend (API + Neo4j)
	•	Valid STAC catalog (data/stac/)

🚀 Run in Dev Mode

cd web
pnpm install
pnpm dev

Environment (.env.local):

VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=/maps/style.json
VITE_STAC_INDEX_URL=/stac/index.json


⸻

🧩 Map & Timeline Core
	•	MapLibre GL: renders STAC-linked layers (COG, GeoJSON)
	•	Timeline Canvas: scrollable multi-scale event plot
	•	Detail Panels: pull entity metadata & AI summaries
	•	Brushing Sync: timeline filters map time window

⸻

📡 API & Knowledge Graph
	•	FastAPI serves layer metadata and entity search
	•	Neo4j stores People ↔ Places ↔ Events ↔ Documents
	•	Graph aligns with CIDOC CRM and OWL-Time ontologies
	•	All responses include provenance and uncertainty scores

⸻

🧪 Testing & QA

pnpm test
pnpm lint
pnpm typecheck

✅ Unit Tests (Jest) ✅ Integration (Mock API) ✅ A11y Audits ✅ Visual Diffs

⸻

♿ Accessibility (A11y)
	•	WCAG 2.1 AA compliance
	•	Keyboard navigation for map/timeline
	•	ARIA labels for dynamic components
	•	Color contrast tokens from KFM Design System

⸻

🔁 CI/CD Pipelines
	•	Build & Deploy: Vite → GitHub Pages
	•	STAC Validate: schema checks on PRs
	•	CodeQL / Trivy: security scans
	•	Pre-Commit: lint, format, typecheck
	•	Docs: auto-sync to GitHub Pages / docs/

⸻

🤝 Contributing

Follow Master Coder Protocol (MCP) standards:
	•	Document before code
	•	Include README, diagram, and CHANGELOG for each module
	•	Validate STAC links and checksums
	•	Commit with semantic version labels

⸻

📎 References
	•	🧩 Monorepo Design
	•	🧠 System Design (Developer Docs)
	•	🎨 Web UI Design
	•	🗺️ GIS Archive Integration
	•	📚 Data Resources

⸻


<div align="center">


“Make it Reproducible · Make it Explorable · Make it Kansas”

</div>



⸻
