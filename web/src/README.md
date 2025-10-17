---
title: "🧭 Kansas Frontier Matrix — Web Frontend"
version: "v1.7.0"
last_updated: "2025-10-17"
owners: ["@kfm-web", "@kfm-architecture"]
maturity: "Production"
tags: ["web","react","typescript","vite","maplibre","timeline","stac","mcp","knowledge-graph"]
license: "MIT (code) | CC-BY 4.0 (docs)"
semantic_alignment:
  - STAC 1.0
  - CIDOC CRM
  - OWL-Time
  - DCAT 2.0
  - FAIR Principles
---

<div align="center">

# 🧭 Kansas Frontier Matrix — **Web Frontend**  
`/web/src/`

### *“Time · Terrain · Story — United through Data.”*

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

## 🪶 Overview

The **Kansas Frontier Matrix Web Frontend** is a **React 18 + TypeScript** single-page application that visualizes Kansas’s historical, ecological, and cultural landscape through an interactive **map**, **timeline**, and **knowledge-graph-driven interface**.  
It connects directly to the **FastAPI / Neo4j backend**, rendering **STAC-indexed data layers** as dynamic stories across space and time.

- 🗺 **Spatio-Temporal Integration** — unified map + timeline window  
- 🧭 **Knowledge Graph Context** — CIDOC CRM / OWL-Time aligned entities  
- 🧠 **AI-Enhanced Summaries** — contextual Q&A with citations  
- ♿ **Accessible Design** — WCAG 2.1 AA-compliant components  
- 🔄 **Provenance-Aware** — transparent data lineage under MCP

---

## ⚙️ Architecture

```mermaid
flowchart TD
  A["React SPA<br/>(web/src)"] --> B["MapView<br/>(MapLibre GL JS)"]
  A --> C["TimelineView<br/>(HTML5 Canvas + D3)"]
  A --> D["SearchBar<br/>(Graph Queries)"]
  A --> E["AI Panel<br/>(Summaries + Citations)"]
  A --> F["DetailPanel<br/>(Entity Dossiers)"]
  A --> G["LayerControls<br/>(STAC-Driven)"]

  B --> H["FastAPI Backend<br/>REST · GraphQL"]
  H --> I["Neo4j Knowledge Graph<br/>CIDOC CRM · OWL-Time"]
  H --> J["STAC Assets<br/>COG · GeoJSON · Tiles"]

  I -.-> A
  J -.-> B
%% END OF MERMAID
```

---

## 🗂 Directory Layout

```text
web/src/
├── components/        # UI modules (Map, Timeline, Search, AI, Detail)
├── context/           # Global state providers
├── hooks/             # useMap · useTimeline · useStac · useSearch
├── styles/            # Tailwind CSS + design tokens
├── types/             # Shared TypeScript types
├── utils/             # API client · formatters · geometry · STAC parser
├── config/            # layers.json · app.config.json · vite.config.ts
├── assets/            # SVGs · icons · manifest.json
└── index.tsx          # SPA entry point
```

---

## 🧩 Core Components

| Component | Purpose | Key Libraries |
|:-----------|:---------|:---------------|
| **MapView** | MapLibre GL base map + STAC overlays | `maplibre-gl`, React |
| **TimelineView** | Temporal brush & playback | Canvas, `d3-scale` |
| **SearchBar** | Knowledge Graph search + autocomplete | REST / GraphQL |
| **DetailPanel** | Entity / Event dossiers + provenance | `react-markdown` |
| **AI Panel** | Q&A assistant with citation links | FastAPI / AI service |
| **LayerControls** | Toggle STAC layers + legends | React Hooks |

---

## 🚀 Quick Start

```bash
# Install dependencies
pnpm install

# Run development server
pnpm dev        # → http://localhost:5173

# Build & preview production
pnpm build
pnpm preview
```

**Environment Variables (`.env`):**

```bash
VITE_API_URL=https://localhost:8000
VITE_MAP_STYLE_URL=/tiles/style.json
```

---

## 🧠 Data Flow

1. **STAC Catalog → layers.json** — built automatically by ETL pipelines.  
2. **FastAPI → Neo4j Graph** — delivers CIDOC CRM / OWL-Time aligned entities & events.  
3. **Timeline Sync** — single temporal state drives map and query filters.  
4. **AI Overlay** — citations & contextual summaries from validated sources.

---

## ♿ Accessibility & Responsiveness

- Tokenized color system · AA contrast verified  
- Full keyboard navigation + ARIA roles  
- Responsive layout for mobile and tablet  
- Reduced-motion preferences honored  
- Focus management within panels and dialogs  

---

## 🛡 Security & Privacy

- Read-only client (no mutations / credentials)  
- HTTPS only requests enforced  
- CORS limited to backend origin  
- No PII or tracking; only provenance metadata  
- STAC licenses and citations visible inline  

---

## 🔗 Related Documentation

- `docs/Kansas Frontier Matrix Web UI Design Document.pdf`  
- `docs/Kansas Frontier Matrix – Monorepo Repository Design.pdf`  
- `docs/File and Data Architecture for KFM.pdf`  
- `docs/Markdown styling guide.pdf`  

---

<div align="center">

**MIT License · © Kansas Frontier Matrix**  
Built under the **Master Coder Protocol (MCP)**  

[![Checksum Verified](https://img.shields.io/badge/Checksum-SHA256 Verified-success)]()  
[![Semantic Alignment](https://img.shields.io/badge/CIDOC CRM · OWL--Time · STAC 1.0-blue)]()

</div>