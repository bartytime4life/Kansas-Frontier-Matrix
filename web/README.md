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
tags: ["web","react","vite","typescript","maplibre","stac","timeline","mcp"]
license: "MIT (code) | CC-BY 4.0 (docs)"
semantic_alignment:
  - CIDOC CRM
  - OWL-Time
  - DCAT 2.0
  - STAC 1.0


⸻

📘 Overview

The Kansas Frontier Matrix Web Application is the user-facing layer of the Frontier-Matrix system — an open-source, temporal–spatial exploration interface that allows users to traverse Kansas history through time, geography, and narrative.
Built with React + MapLibre GL JS, it renders interactive maps, time-linked datasets, and AI-generated story layers connected to the system’s Neo4j Knowledge Graph and FastAPI backend ￼ ￼.

The frontend’s mission is to visualize the project’s integrated data — historical events, places, climate records, and cultural archives — in a cohesive, intuitive web interface that synchronizes map overlays and timelines, allowing users to “time-travel” across Kansas’s frontier past.

⸻

🧩 Architecture at a Glance

flowchart TD
  A["Backend API<br/>FastAPI · GraphQL · STAC Endpoints"]
    --> B["Web Client<br/>React · TypeScript · Vite"]
  B --> C["Timeline View<br/>Canvas · D3 · OWL-Time"]
  B --> D["Map View<br/>MapLibre GL · GeoJSON · COGs"]
  B --> E["Knowledge Graph Queries<br/>Neo4j · CIDOC CRM"]
  D --> F["AI Summaries<br/>LLM · spaCy · Transformers"]
  E --> G["User Interaction Layer<br/>Events · Filters · Queries"]
  G --> B
%% END OF MERMAID

The UI and backend communicate via REST/GraphQL endpoints that expose graph data and geospatial assets (STAC/GeoJSON).
Heavy processing (ETL, AI/ML, NER) occurs server-side, while the web client focuses purely on rendering and interaction ￼.

⸻

🗂️ Directory Layout

web/
├── src/
│   ├── components/        # React components (Map, Timeline, Panels, Search)
│   ├── hooks/             # Custom React hooks (useMap, useTimeline, etc.)
│   ├── pages/             # Route-level views (Home, Explore, Admin)
│   ├── assets/            # Static assets (icons, images, JSON styles)
│   ├── styles/            # CSS/SCSS or Tailwind configurations
│   ├── types/             # Shared TypeScript type definitions
│   ├── utils/             # Helper utilities (API client, formatters)
│   ├── config.ts          # Environment and endpoint configuration
│   └── main.tsx           # React entrypoint
│
├── public/                # Static files served at build time
├── package.json           # Node dependencies
├── vite.config.ts         # Vite build configuration
├── tsconfig.json          # TypeScript compiler settings
└── README.md              # (this file)


⸻

⚙️ Technology Stack

Layer	Framework / Library	Purpose
Frontend Framework	React 18 + TypeScript	Modular UI components
Map Engine	MapLibre GL JS	Vector-tile mapping, temporal overlays
Timeline Renderer	HTML5 Canvas + D3.js	High-performance interactive timeline
State Management	React Context / Zustand	Cross-component state sync
API Client	Axios / GraphQL	Connects to FastAPI + Neo4j endpoints
Build Tools	Vite + ESLint + Prettier	Fast bundling and code linting
UI Library	Tailwind / ShadCN-UI	Themed responsive layout
Testing	Jest + React Testing Library	Component/unit testing
Accessibility	WAI-ARIA, WCAG 2.1 AA	Inclusive design standards


⸻

🧭 Core Features

🗺️ Map & Layer Engine
	•	Interactive MapLibre viewer with STAC-registered layers (GeoJSON / COG).
	•	Time-based map layers toggle dynamically as the timeline moves.
	•	Supports raster (historical maps, DEMs) and vector overlays (railroads, treaties, climate zones).

🕰️ Timeline Visualization
	•	Scrollable & zoomable HTML5 Canvas timeline linked to OWL-Time data structures.
	•	Syncs with the map — clicking a timeline event zooms to its geographic location.
	•	Can display events, eras (PeriodO definitions), or environmental cycles.

🔍 Knowledge Graph Search
	•	Federated search queries across People, Places, Events nodes in Neo4j.
	•	Queries return contextual info: linked entities, related maps, and document snippets.
	•	Supports fuzzy and semantic matching (leveraging CIDOC CRM and OWL-Time tags).

🤖 AI-Assisted Summaries
	•	AI models generate site dossiers and contextual summaries for selected entities.
	•	Combines NLP (spaCy NER) and transformer summarizers to synthesize text across sources.
	•	Provenance and confidence scores are displayed for each AI insight ￼.

🧰 Admin Console
	•	Secure access for curators to review, edit, or flag extracted data.
	•	Includes “source linking” tools to associate entities with documents or maps.
	•	Supports validation of AI-generated content through human review workflows.

⸻

🚀 Development & Build

Prerequisites
	•	Node.js ≥ 20.x
	•	npm or pnpm (recommended)
	•	Backend running at http://localhost:8000 (FastAPI server)

Commands

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Run linter and tests
npm run lint && npm test


⸻

🧩 Integration with Backend

The web client communicates with the FastAPI backend through REST/GraphQL endpoints:

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000/api";

async function fetchEvents(start: string, end: string) {
  const res = await fetch(`${API_BASE}/events?start=${start}&end=${end}`);
  return await res.json();
}

Endpoints are documented automatically via Swagger/OpenAPI in the backend.
The frontend consumes STAC and metadata JSONs for available layers (from /data/stac/) and dynamically registers them as MapLibre sources.

⸻

🧪 Testing & CI/CD
	•	Unit Tests: Run via Jest for React components and utility functions.
	•	Integration Tests: Verify data integrity across API endpoints and timeline/map linking.
	•	Continuous Integration: GitHub Actions run linting, build checks, and deploy to GitHub Pages (site.yml).
	•	Security & Dependency Scanning: Automated via Trivy and CodeQL workflows.

⸻

🧠 Documentation Alignment

All web documentation follows the Master Coder Protocol (MCP):
	•	Every component is documented inline with version and dependency notes.
	•	Changes to UI or logic must include corresponding updates in /docs/web/ or /docs/architecture.md.
	•	MCP compliance ensures provenance, reproducibility, and open-science traceability.

⸻

🪪 License

Code is released under the MIT License, and documentation/content under CC-BY 4.0.
Attribution and citation details are provided in CITATION.cff.

⸻


<div align="center">


Kansas Frontier Matrix — “Time · Terrain · History · Knowledge Graphs”
📍 Open-Source Digital Atlas of Kansas
© 2025 Frontier-Matrix Contributors

</div>



⸻

Would you like me to generate companion files (web/src/README.md for components & types) to maintain consistency with the rest of your repo structure?