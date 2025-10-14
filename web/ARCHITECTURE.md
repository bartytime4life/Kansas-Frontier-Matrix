<div align="center">

# 🧭 Kansas Frontier Matrix — **Web Application (`/web/`)**

### *Interactive · Temporal · Spatial · Narrative*

[![React 18+](https://img.shields.io/badge/React-18%2B-61DAFB?logo=react&logoColor=white)](https://react.dev/)
[![MapLibre GL](https://img.shields.io/badge/MapLibre%20GL-JS-brightgreen)](https://maplibre.org/)
[![HTML5 Canvas](https://img.shields.io/badge/HTML5-Canvas-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009485?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)
[![Pages Deploy](https://img.shields.io/github/deployments/bartytime4life/Kansas-Frontier-Matrix/github-pages?label=Pages%20Deploy)](https://bartytime4life.github.io/Kansas-Frontier-Matrix/)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../docs/)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Web Application"
version: "v1.7.1"
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

🧭 Overview

The Kansas Frontier Matrix Web App is the interactive exploration layer of the system — a React + MapLibre single-page application connecting time · terrain · story.
It visualizes treaties, trails, hydrology, climate, and archival narratives synchronized with a FastAPI / Neo4j semantic backend built on CIDOC CRM + OWL-Time ontologies.

⸻

🏗️ Architecture Snapshot

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
│  ├─ components/      # TimelineView · MapView · LayerControls · DetailPanel · SearchBar · AIAssistant
│  ├─ hooks/           # useMap · useTimeline · useStac · useSearch
│  ├─ context/         # Global state providers (timeline window, layer toggles)
│  ├─ utils/           # API client · formatters · geometry helpers
│  ├─ styles/          # Tailwind / SCSS tokens
│  └─ types/           # TypeScript interfaces (API/graph/config)
├─ public/             # Static assets (manifest, icons)
├─ config/             # Generated configs (layers.json, app.config.json)
├─ package.json        # Node project metadata
├─ vite.config.ts      # Vite build config
└─ README.md           # This file


⸻

⚡ Quickstart

Prereqs
	•	Node.js 18 or 20 + npm/yarn
	•	Backend API running → ../docs/sop.md

Environment

VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=https://basemaps.cartocdn.com/gl/positron-gl-style/style.json
VITE_APP_TITLE="Kansas Frontier Matrix"

Run

cd web
npm install
npm run dev       # local dev http://localhost:5173
npm run build     # production bundle
npm run preview   # serve build


⸻

🔌 Core API Endpoints

Endpoint	Method	Params	Returns	Used By
/events	GET	start,end,bbox?,type?	Event[] (GeoJSON)	Timeline · Map
/entity/{id}	GET	—	Entity dossier (summary, relations)	Detail Panel
/layers-config	GET	—	Layer defs (from STAC)	Map · Controls
/search	GET	q,limit?	Entity matches	Search Bar
/ask	POST	{question}	{answer, citations[]}	AI Assistant


⸻

🧩 Key Components
	•	TimelineView — Canvas timeline (zoom/pan/filter → time window emit)
	•	MapView — MapLibre map (GeoJSON + COG layers · hit testing)
	•	LayerControls — Toggle/opacity UI (auto-generated from STAC)
	•	DetailPanel — Entity dossier + AI summary + citations
	•	SearchBar — Autocomplete graph search → flyTo + select
	•	AIAssistant — Conversational Q&A with inline citations

⸻

🗂 Data Standards
	•	GeoJSON · COG · STAC 1.0 for map layers
	•	CIDOC CRM + OWL-Time for semantic events & intervals
	•	Temporal metadata drives timeline visibility

⸻

⚙️ Config Example

{
  "id": "usgs_topo_larned_1894",
  "label": "USGS Topo Larned (1894)",
  "type": "raster-cog",
  "source": { "url": "/tiles/usgs_topo_larned_1894.tif", "minzoom": 0, "maxzoom": 14 },
  "time": { "start": "1894-01-01", "end": "1894-12-31" },
  "legend": { "category": "Historic Topographic Maps" },
  "visible": false,
  "opacity": 0.8
}


⸻

♿ Accessibility & Responsiveness
	•	Keyboard navigation (← → zoom time, f focus map, s search)
	•	ARIA roles/labels · focus rings · skip-links
	•	Color-blind-safe palette · high-contrast toggle
	•	Reduced-motion compliant animations

⸻

🛡️ Security & Privacy
	•	No secrets in client code (VITE_ = public vars)
	•	HTTPS required in production
	•	Escape/sanitize AI HTML output
	•	Analytics opt-in only (no ID/BBox leaks)

⸻

🧠 MCP & DevEx
	•	CI/CD: GitHub Actions (build · lint · test · deploy)
	•	Security: CodeQL + Trivy
	•	Tests: Jest (unit) · Cypress (E2E planned)
	•	Docs-first: update ../docs/{architecture,sop,model_card}.md with changes
	•	Reproducibility: pinned deps · checksums · deterministic builds

⸻

⚡ Performance Notes
	•	Canvas timeline off-screen buffers · rAF render · batched paints
	•	MapLibre COGs with overviews · vector-tile sources for density
	•	Network gzip/Brotli · lazy-load non-critical chunks

⸻

🧪 Developer Cheat-Sheet

npm run dev      # local dev
npm run build    # prod bundle
npm run preview  # serve build
npm run lint     # lint/format
npm run test     # Jest

Key files:
src/components/TimelineView.tsx, MapView.tsx, DetailPanel.tsx, config/layers.json

Add layer → create STAC item → regenerate config → toggle appears.

⸻

🧰 Troubleshooting

Issue	Check
Timeline empty	API /events range/UTC
Layer missing	config/layers.json path & CORS
COG blurry	Internal overviews present
AI silent	Backend /ask reachable
Mermaid fails	Rename class end → done


⸻

📚 References
	•	web/ARCHITECTURE.md
	•	../docs/architecture.md
	•	../docs/sop.md
	•	../docs/model_card.md

⸻


<div align="center">


✨ Kansas Frontier Matrix Web UI — Explore Kansas across Time and Space ✨

</div>
```