<div align="center">

# 🌐 Kansas Frontier Matrix — **Web Application**

### *Interactive · Temporal · Spatial · Narrative*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../.github/workflows/site.yml)
[![Pages Deploy](https://img.shields.io/github/deployments/bartytime4life/Kansas-Frontier-Matrix/github-pages?label=Pages%20Deploy)](https://bartytime4life.github.io/Kansas-Frontier-Matrix/)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy%20Security)](../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../docs/)
[![License: MIT | CC-BY 4.0](https://img.shields.io/badge/License-MIT%20(code)%20%7C%20CC--BY%204.0%20(docs)-blue)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Web Application"
version: "v1.7.2"
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
	•	Quickstart
	•	Core Components
	•	Data Standards
	•	Configuration
	•	Accessibility
	•	Security
	•	Performance
	•	Developer Reference
	•	Troubleshooting
	•	References

⸻

🧭 Overview

The Kansas Frontier Matrix Web Application is the interactive exploration layer of the project — a React + MapLibre GL single-page interface connecting time · terrain · story.
It synchronizes maps, timelines, and documents backed by a FastAPI + Neo4j semantic backend aligned to CIDOC CRM and OWL-Time.

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
├── src/
│   ├── components/   # TimelineView · MapView · LayerControls · DetailPanel · SearchBar · AIAssistant
│   ├── hooks/        # useMap · useTimeline · useStac · useSearch
│   ├── context/      # Global state (timeline window, layer toggles)
│   ├── utils/        # API client · formatters · geometry helpers
│   ├── styles/       # Tailwind / SCSS design tokens
│   └── types/        # Shared TypeScript interfaces
├── public/           # Static assets (icons, manifest)
├── config/           # Auto-generated (layers.json, app.config.json)
├── package.json      # Node project metadata
├── vite.config.ts    # Vite build config
└── README.md         # This file


⸻

⚡ Quickstart

Prerequisites
	•	Node.js 18+
	•	Backend API running → ../docs/sop.md

Environment

VITE_API_BASE_URL=http://localhost:8000
VITE_MAP_STYLE_URL=https://basemaps.cartocdn.com/gl/positron-gl-style/style.json
VITE_APP_TITLE="Kansas Frontier Matrix"

Setup

cd web
npm install
npm run dev
npm run build
npm run preview


⸻

🧩 Core Components

Component	Purpose
TimelineView	High-performance HTML5 Canvas timeline (zoom/pan/filter → emits time window)
MapView	MapLibre GL map; renders GeoJSON & COGs; integrates with timeline filters
LayerControls	Toggles, legends, and opacity; built from config/layers.json
DetailPanel	Entity dossiers + AI summaries + source citations
SearchBar	Graph search autocomplete → highlights on map/timeline
AIAssistant	Conversational Q&A with citation links


⸻

🗺️ Data Standards
	•	GeoJSON → vector features
	•	COG (Cloud-Optimized GeoTIFF) → raster overlays
	•	STAC Catalogs → spatio-temporal asset indexing
	•	CIDOC CRM + OWL-Time → graph semantics for events, entities, and intervals

⸻

⚙️ Configuration

Example layer entry from /config/layers.json:

{
  "id": "usgs_topo_larned_1894",
  "label": "USGS Topographic Map — Larned (1894)",
  "type": "raster-cog",
  "source": { "url": "/tiles/usgs_topo_larned_1894.tif", "minzoom": 0, "maxzoom": 14 },
  "time": { "start": "1894-01-01", "end": "1894-12-31" },
  "legend": { "category": "Historic Topographic Maps" },
  "visible": false,
  "opacity": 0.8
}

Vectors use "type": "vector-geojson" with "source": {"url": ".../layer.geojson"}.
The time block syncs with timeline filters.

⸻

♿ Accessibility
	•	Keyboard navigation (←/→ timeline, f focus map, s focus search)
	•	WAI-ARIA roles/labels, skip-links, and focus rings
	•	High-contrast color mode · reduced-motion animations

⸻

🛡️ Security
	•	No secrets in client (VITE_ = public vars only)
	•	HTTPS enforced in production
	•	AI outputs sanitized; no user data logged
	•	Analytics disabled by default (opt-in only)

⸻

⚡️ Performance
	•	Offscreen canvas buffers; rAF-driven redraw
	•	MapLibre with overviews + vector tiles
	•	Lazy-loaded routes; compressed static assets (Gzip/Brotli)

⸻

🧪 Developer Reference

npm run dev       # start dev server
npm run build     # build production bundle
npm run preview   # serve built site
npm run lint      # lint/format
npm run test      # Jest unit tests

Key Files:
src/components/TimelineView.tsx · MapView.tsx · DetailPanel.tsx · config/layers.json

To add a new layer:
	1.	Add STAC item under data/stac/
	2.	Rebuild config → new toggle auto-appears

⸻

🧰 Troubleshooting

Issue	Solution
Timeline empty	Verify /events returns valid date range (UTC).
Missing layer	Confirm config/layers.json URL & CORS settings.
Blurry raster	Add internal overviews in GeoTIFF (COG).
AI silent	Ensure backend /ask service reachable.
Mermaid fails in docs	Avoid end as class name → rename to done.


⸻

📚 References
	•	web/ARCHITECTURE.md
	•	../docs/architecture.md
	•	../docs/sop.md
	•	../docs/model_card.md

⸻


<div align="center">


✨ Kansas Frontier Matrix — Web Application ✨
Exploring Kansas through Time, Terrain, and Story.

</div>
```