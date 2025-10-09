<div align="center">

# 🧭 Kansas Frontier Matrix — Web Frontend  
`web/src/`

**Interactive Map · Timeline · Knowledge Graph Interface**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../.github/workflows/ci.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-lightgrey)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

## 🪶 Overview

The **Kansas Frontier Matrix Web Frontend** is a **React 18+ Single Page Application (SPA)** that visualizes  
Kansas’s historical, environmental, and cultural data through an interactive **Map + Timeline interface**.  
It serves as the public face of the KFM knowledge graph, powered by a Python **FastAPI / GraphQL backend**  
and a **Neo4j** data layer.

**Core principles:**  
- 📍 Spatial–Temporal Synchronization — Explore Kansas history across both map and timeline views.  
- 🤖 AI Assistance — Retrieve AI-generated summaries, insights, and Q&A from the knowledge graph.  
- 🗺️ Open Data — Built on STAC-indexed GeoJSON & COG datasets.  
- 🧩 Modular & Accessible — Component-based React architecture (Map, Timeline, Layers, Search, Detail).  

---

## ⚙️ Architecture

flowchart TD
  A["React SPA\n(web/src/)"] --> B["MapView\n(MapLibre GL JS)"]
  A --> C["TimelineView\n(HTML5 Canvas + D3)"]
  A --> D["SearchBar\nREST/GraphQL queries"]
  A --> E["AI Assistant Panel\nLLM summary/Q&A"]
  A --> F["DetailPanel\nEntity & Event metadata"]
  A --> G["LayerControls\nSTAC-driven config"]
  B --> H["FastAPI Backend\nREST · GraphQL"]
  H --> I["Neo4j Knowledge Graph\nCIDOC CRM · OWL-Time"]
  H --> J["GIS Tile Storage\nCOGs · GeoJSON · STAC"]
  I --> A
  J --> B
%% END OF MERMAID

---

## 🧩 Component Structure

| Component | Purpose | Key Libraries |
|------------|----------|---------------|
| **MapView** | Interactive 2D map showing layers (historical maps, hydrology, treaties, etc.). | `maplibre-gl-js`, `react-map-gl` |
| **TimelineView** | Scrollable/zoomable time bar synchronized with the map. | `HTML5 Canvas`, `D3.js` |
| **SearchBar** | Autocomplete entity search; queries `/search?q=` endpoint. | `Axios`, `React Context` |
| **AI Assistant Panel** | Accepts user prompts, displays AI summaries and citations. | `OpenAI / local NLP API` |
| **DetailPanel** | Displays full entity/event details with linked documents and relationships. | `React Markdown`, `Framer Motion` |
| **LayerControls** | Manages toggles, legends, and transparency of map layers. | `Material UI`, `React Hooks` |

---

## 🚀 Usage

```bash
# 1. Setup dependencies
npm install

# 2. Start local development
npm run dev      # launches on http://localhost:3000

# 3. Build for production
npm run build

# 4. Run tests
npm test

The app fetches configuration from:
/api/layers-config → STAC-based layer definitions
/api/events?start=&end= → events for the visible time range
/api/entity/{id} → details and AI summaries

⸻

🧠 Data Flow

flowchart LR
  User --> UI["React Components"]
  UI --> API["FastAPI / GraphQL"]
  API --> DB["Neo4j Knowledge Graph"]
  API --> STAC["STAC Catalog (data/stac/)"]
  STAC --> UI
%% END OF MERMAID


⸻

🧪 Development Notes
	•	State Management: React Context for global timeline range and active entity.
	•	Accessibility: ARIA roles, keyboard navigation, and color-contrast-tested palette (WCAG 2.1 AA).
	•	Performance: Virtualized rendering for dense event timelines and clustered map markers.
	•	Testing: Jest + React Testing Library for components; Cypress for end-to-end user flows.
	•	Build System: Vite (fast dev server, ES module optimization).

⸻

🧭 Provenance & Dependencies
	•	Inputs: data/stac/catalog.json, API endpoints from src/api/
	•	Outputs: build/ (optimized web assets), served via Docker container
	•	Version Control: SHA256 checksums logged for build artifacts
	•	ETL Linkage: Consumes processed outputs from data/processed/ and AI summaries from src/ai/

⸻

🔗 Related Documentation
	•	Kansas Frontier Matrix — Architecture
	•	Web UI Architecture (Full)
	•	Monorepo Design
	•	ETL Pipelines Overview

⸻

📜 License & Credits

Licensed under MIT.
Developed by the Kansas Frontier Matrix Team under the Master Coder Protocol (MCP).

“Time, terrain, and story—united through data.”

