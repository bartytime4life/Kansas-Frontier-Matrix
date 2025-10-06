<div align="center">

# ⏳ Kansas Frontier Matrix — Timeline Interface  
`docs/design/mockups/timeline/`

**Temporal · Interactive · Synchronized with Map**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Timeline%20Design-purple)](./figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The **Timeline Interface** provides the **temporal dimension** of the Kansas Frontier Matrix (KFM) — a dynamic, interactive bar that lets users explore history through time.  
It synchronizes directly with the **map** and **knowledge graph**, allowing users to see how events, entities, and spatial layers evolve chronologically.

Core functions include:
- Navigating historical periods with a **draggable range selector**  
- Filtering map layers and entities by date  
- Visualizing clusters of events or activity density  
- Displaying **event markers** that highlight changes on the map  
- Coordinating with the AI Assistant for time-based queries  

---

## 🧩 Architecture Overview

```mermaid
flowchart LR
  A["User Interaction\n(scrub, zoom, play)"] --> B["Timeline Component\n(Canvas + React Hook)"]
  B --> C["API Request\n/events?start&end"]
  C --> D["Knowledge Graph (Neo4j)\nTemporal Query (OWL-Time)"]
  D --> E["Frontend Update\nMap + Detail Panels"]
  B --> F["Animation Loop\n(time-play)"]

<!-- END OF MERMAID -->


The timeline operates as a React component built on HTML5 Canvas for smooth rendering, with D3.js handling scales and data transformations.
All interactions emit { start, end } time ranges to synchronize the map’s visible layers.

⸻

📁 Directory Layout

docs/design/mockups/timeline/
├── README.md                # This documentation
├── wireframes/              # Figma exports for layout
│   ├── timeline-overview.png
│   ├── scrubber-control.svg
│   ├── event-markers.png
│   └── playback-controls.svg
├── thumbnails/              # Preview images for README
│   ├── timeline-thumb.png
│   └── controls-thumb.png
└── figma-refs.json          # Figma node IDs and export metadata

Each file links to its original Figma source node via figma-refs.json for version traceability.

⸻

🧭 Key Features

Feature	Description	Implementation
Scrubber Handle	Draggable control defining visible time range	Canvas event listeners (mousedown, mousemove)
Event Markers	Visual pins representing historical events or clusters	D3 scales for temporal binning + Canvas draw loop
Playback Control	Play/pause historical animation (auto-advance)	React state + requestAnimationFrame loop
Zoom Levels	Multi-resolution views (decades, years, months)	D3 temporal scale + adaptive tick density
Linked Highlighting	Selecting an event highlights corresponding map feature	Shared context with MapLibre via React hooks


⸻

🎨 Design Tokens

Token	Example	Purpose
--kfm-timeline-bg	#0b1020	Background color (dark mode)
--kfm-timeline-accent	#4F9CF9	Marker and selection color
--kfm-timeline-range	rgba(79,156,249,0.25)	Active selection fill
--kfm-grid-line	#cccccc40	Temporal grid lines
--kfm-font	"Inter", sans-serif	Tick labels and captions

Design tokens mirror those in the global web/src/styles/tokens.css.

⸻

🧠 Interaction Flow

sequenceDiagram
  participant User
  participant Timeline
  participant API
  participant Map
  User->>Timeline: Drag range selector
  Timeline->>API: GET /events?start=1850&end=1870
  API-->>Timeline: JSON (events + metadata)
  Timeline-->>Map: Emit {start, end} range + highlighted events
  Map-->>User: Update visible layers and markers

<!-- END OF MERMAID -->


The timeline acts as the temporal control surface for the entire KFM interface — everything from STAC layers to entity visibility is time-bound by its range.

⸻

🧩 Accessibility & UX Notes

Element	Accessibility Practice
Keyboard Controls	← / → for moving range; space toggles play/pause
ARIA Labels	role="slider" with aria-valuemin, aria-valuemax, aria-valuenow
Color Contrast	All interactive elements meet 4.5:1 ratio
Animation Safety	Smooth playback ≤ 30fps to prevent motion sickness
Responsive Layout	Collapses into simplified scrub bar on mobile


⸻

🔍 Provenance & Integrity

Asset	Figma Node	Exported	SHA256
timeline-overview.png	figma://node/52:17	2025-09-30	sha256-81aa…
scrubber-control.svg	figma://node/52:19	2025-09-30	sha256-3f92…
event-markers.png	figma://node/52:22	2025-09-30	sha256-6aef…
playback-controls.svg	figma://node/52:25	2025-09-30	sha256-b9d3…

All hashes validated in CI to ensure fidelity between design exports and tracked documentation.

⸻

📚 Related Documents
	•	Map Interface
	•	Navigation Components
	•	Panels & Detail Views
	•	AI Assistant Design
	•	Web UI Architecture

⸻

📜 License & Credits

Timeline design © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Designed and documented by the KFM Design & Interaction Team in alignment with Master Coder Protocol principles for reproducibility, accessibility, and open collaboration.

