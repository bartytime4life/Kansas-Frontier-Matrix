<div align="center">

# 🧩 Kansas Frontier Matrix — Web Frontend Components  
`web/src/components/`

**Modular React Components · Map + Timeline UI · Storytelling Panels**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../.github/workflows/ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/src/components/` directory contains all **React components** that make up  
the interactive Kansas Frontier Matrix Web Application — including the **Map**,  
**Timeline**, **Layer Controls**, **AI Assistant**, and **Detail Panels**.

Components are **modular, typed, and documented** for maintainability and reproducibility.  
Each is designed under the **Master Coder Protocol (MCP)** design ethos:  
> _Document first → Implement → Validate → Reproduce._

Every visual element (map layers, event markers, modals, AI summaries) connects  
to data from the backend FastAPI/GraphQL API and the Neo4j Knowledge Graph.

---

## 🧱 Directory Structure

```text
web/src/components/
├── AppShell/             # Root layout + context providers
├── Header/               # Top navigation, project title, search bar
├── MapView/              # MapLibre-based map, overlays, popups
├── TimelineView/         # HTML5 Canvas/D3 timeline visualization
├── LayerControls/        # STAC-driven layer toggles + opacity sliders
├── DetailPanel/          # Entity/Event info, AI summaries, source links
├── AIAssistant/          # Natural-language Q&A + chat history
├── Sidebar/              # Filter and layer legend container
├── Modals/               # Global modals (about, settings, accessibility)
├── Accessibility/        # Keyboard focus indicators, skip links
└── index.ts              # Export all components

Each subfolder typically includes:
	•	index.tsx — main component implementation
	•	styles.scss — scoped styling rules
	•	test.tsx — Jest + React Testing Library tests
	•	README.md — (optional) sub-component documentation

⸻

🎨 Component Map

flowchart LR
  H["Header\nSearch · Branding · Theme"] --> A["AppShell"]
  A --> M["MapView\n(MapLibre GL + Layers)"]
  A --> T["TimelineView\n(Canvas + D3)"]
  A --> L["LayerControls\nSTAC-driven"]
  A --> D["DetailPanel\nEntity/Event Details"]
  A --> AI["AIAssistant\nSummaries · Q&A"]
  A --> S["Sidebar\nLegends · Filters"]
  A --> MOD["Modals\nSettings · About"]
  A --> ACC["Accessibility\nFocus Rings · Skip Links"]
%% END OF MERMAID

All major UI elements are rendered inside the AppShell component,
which orchestrates layout, context providers, and responsive scaling.

⸻

🧩 Core Components

Component	Purpose	Key Technologies
AppShell	Entry point; wraps global providers (context, theme, AI).	React Context, Framer Motion
Header	Global navigation bar with project title, search, theme toggle.	React Router, useDebounce
MapView	MapLibre map rendering layers (GeoJSON, COGs) from STAC catalog.	MapLibre GL JS
TimelineView	Scrollable/zoomable timeline showing events chronologically.	HTML5 Canvas, D3.js
LayerControls	Dynamic layer toggles, opacity sliders, legend display.	STAC metadata parser
DetailPanel	Displays metadata, AI summaries, and citations for selected entities.	Markdown renderer
AIAssistant	Q&A chat using backend AI endpoints (/api/ask).	OpenAI API / LLM integration
Sidebar	Houses filters, data layers, and legends beside the map.	Framer Motion, Tailwind
Modals	Reusable overlay for About, Accessibility, and Settings panels.	Portal API
Accessibility	Ensures WCAG compliance and keyboard navigation.	ARIA roles, hooks


⸻

⚙️ Component Example — MapView

import React, { useEffect, useRef } from "react";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";

export function MapView({ layers }) {
  const mapContainer = useRef(null);

  useEffect(() => {
    const map = new maplibregl.Map({
      container: mapContainer.current,
      style: "https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json",
      center: [-98.3, 38.5],
      zoom: 6,
    });

    layers.forEach(layer =>
      map.addSource(layer.id, { type: "geojson", data: layer.url })
    );

    return () => map.remove();
  }, [layers]);

  return <div ref={mapContainer} className="map-view"></div>;
}

Purpose: renders the spatial layer stack (treaty maps, hydrology, elevation)
and connects map interactions to the SelectionContext for syncing with the timeline.

⸻

🧠 Data Flow

flowchart TD
  API["FastAPI / GraphQL"] --> E["Events Data"]
  API --> LAYERS["STAC Layer Config"]
  E --> TL["TimelineView"]
  LAYERS --> MAP["MapView"]
  MAP --> DP["DetailPanel"]
  DP --> AI["AIAssistant"]
  TL --> DP
  DP --> MAP
%% END OF MERMAID

This structure ensures the UI reacts dynamically to user interactions —
timeline scrubbing, map panning, or AI queries automatically update the view state.

⸻

🧩 Development Notes
	•	Styling: Each component imports styles from web/src/styles/ (theme variables + layout grid).
	•	Accessibility: Components use ARIA roles and keyboard handlers from AccessibilityContext.
	•	Performance: Timeline and map components use requestAnimationFrame and throttled updates.
	•	Testing: Jest + React Testing Library simulate user interactions; snapshots stored under __tests__/.
	•	Storybook (optional): UI components can be previewed in isolation for visual QA.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	Context and hooks (state, API data, AI results)
Outputs	React-rendered DOM and canvas/map visualizations
Dependencies	React 18+, D3.js, MapLibre GL, Tailwind, Framer Motion
Integrity	Validated via CI — lint, unit tests, accessibility checks (axe-core)


⸻

🔗 Related Documentation
	•	Web Frontend Overview
	•	Context
	•	Hooks
	•	Types
	•	Utilities
	•	Web UI Architecture

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — designed with MCP design and reproducibility standards.

“Components are the storytellers — each renders a fragment of Kansas history into view.”

