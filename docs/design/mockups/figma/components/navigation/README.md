<div align="center">

# 🧭 Kansas Frontier Matrix — Navigation Components  
`docs/design/mockups/figma/components/navigation/`

**Interactive · Temporal · Spatial · Intuitive Navigation**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../docs/design/)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🪶 Overview

The **Navigation Components** define the **core movement and exploration tools** for the  
Kansas Frontier Matrix (KFM) web interface — the bridge between **space**, **time**, and **knowledge**.  
These elements form the **interactive shell** of the platform, synchronizing the **map**, **timeline**,  
and **information panels** across devices.

Every component originates from the **Figma design library** and corresponds to a React implementation  
within the `/web/src/components/navigation/` directory. These mockups ensure **visual consistency**,  
**accessibility**, and **semantic design logic** across KFM.

---

## 🧭 Component Hierarchy

```text
docs/design/mockups/figma/components/navigation/
├── README.md                       # Index (this file)
├── header/                         # Global top navigation bar & search
│   ├── header-primary.fig           # Figma: full-width layout mockup
│   └── header-mobile.fig            # Figma: responsive mobile variant
├── sidebar/                        # Layer controls, filters, legends
│   ├── sidebar-left.fig             # Figma: collapsed + expanded states
│   └── sidebar-mobile.fig           # Compact mobile view (drawer)
├── timeline-controls/              # Time rail, zoom handles, play/pause
│   ├── timeline-rail.fig
│   └── timeline-tooltip.fig
├── map-toolbar/                    # Zoom, locate, layers toggle, mode switch
│   ├── map-toolbar-default.fig
│   └── map-toolbar-darkmode.fig
└── panels/                         # Details + context drawer
    ├── panel-details.fig
    └── panel-ai-summary.fig

Each .fig file corresponds to a Figma component frame, mirrored to a React JSX component in /web/src/.
Developers can reference these mockups for pixel-perfect implementation and interaction mapping.

⸻

🧩 Core Navigation Flow

🗺️ System Integration Diagram

flowchart LR
  A["Header\nsearch · menus · tabs"] --> B["Timeline\nrail · handles · zoom"]
  A --> C["Map Toolbar\nzoom · locate · layers"]
  B --> D["API\nGET /events?start&end"]
  C --> E["API\nGET /layers-config"]
  A --> F["Details Panel\nGET /entity/{id}"]
  D --> G["React State\nselectedTimeRange"]
  E --> H["React State\nactiveLayers"]
  F --> I["React State\nselectedEntity"]
  G --> J["Map View Updates"]
  H --> J
  I --> J
  J --> K["Rendered Output\nTimeline + Map + Panels"]

<!-- END OF MERMAID -->


This flow represents UI synchronization between navigation controls, React state, and backend APIs.
Every navigation input (header, toolbar, or timeline) triggers data fetches or UI updates in real-time.

⸻

🎨 Design Tokens & Standards

Token	Example	Purpose
--kfm-color-bg	#0b1020 / #ffffff	Background colors (dark/light mode)
--kfm-color-fg	#fafafa / #111111	Primary text colors
--kfm-accent	#22a7f0	Highlight & interaction states
--kfm-radius-lg	12px	Rounded corners for buttons and panels
--kfm-shadow-md	0 2px 8px rgba(0,0,0,0.25)	Depth for floating navigation bars
--kfm-font-ui	Inter, sans-serif	Standard interface font
--kfm-font-mono	IBM Plex Mono	Monospace for code or data layers

Note: Tokens are centralized under /web/src/styles/tokens.css and consumed by all navigation elements
to maintain color harmony, accessibility contrast, and visual hierarchy.

⸻

⚙️ Component Interactions

Component	Behavior	Linked System
Header Bar	Global search, menu access, language toggle	/api/search
Timeline Rail	Drag to select time window; scroll/zoom controls	/api/events
Map Toolbar	Zoom, pan, locate, toggle map layers	/api/layers-config
Sidebar (Left)	Filter controls and legends	STAC catalog
Detail Panel (Right)	Contextual info, AI summaries	/api/entity/{id}
AI Summary Panel	Displays GPT-generated site or event overview	/api/ai/summary

Interactions are bi-directional — any selection updates the global React state and triggers
a synchronized change across the timeline and map.

⸻

🧱 Accessibility & Responsiveness
	•	Keyboard Navigation: All interactive components support Tab, Enter, and arrow keys.
	•	ARIA Labels: Descriptive roles for screen readers (e.g., role="slider" for the timeline).
	•	Color Contrast: Minimum AA compliance for text and interface colors.
	•	Responsive Layout: Collapsible panels for ≤768px width, with touch gestures supported.

graph TD
  A["Desktop Layout\n(Full Timeline + Map)"] --> B["Tablet Layout\nTimeline collapses on toggle"]
  B --> C["Mobile Layout\nStacked map + slide-up timeline"]

<!-- END OF MERMAID -->



⸻

🧠 Design System Integration

All navigation mockups comply with the Kansas Frontier Matrix Design System, ensuring:
	•	Unified typography and iconography (via Lucide React icons)
	•	Shared motion patterns (Framer Motion transitions)
	•	Standardized spacing scale (4px base unit)
	•	Reusable interactive states (hover, focus, active)

Developers should use the @/components/ui/ directory for base UI primitives before composing navigation-specific elements.

⸻

🧰 Developer Notes

API Endpoints Referenced
	•	/api/events?start={t0}&end={t1} → Timeline synchronization
	•	/api/layers-config → Map layer controls
	•	/api/entity/{id} → Panel content loading

React State Model (Simplified)

stateDiagram-v2
    [*] --> Idle
    Idle --> Loading : fetchData()
    Loading --> Ready : setState(data)
    Ready --> Updating : userInteraction()
    Updating --> Ready : render()

<!-- END OF MERMAID -->


This ensures deterministic updates across navigation components.

⸻

🧾 Versioning & Source

Field	Description
Design Tool	Figma (shared KFM library)
Frontend Framework	React 18 + MapLibre GL
Data Source	FastAPI (Python) + Neo4j
Document Maintainer	KFM Design Team
Last Updated	October 2025


⸻

📎 References
	•	Kansas Frontier Matrix — Web UI Architecture
	•	Design System Tokens
	•	Frontend Components Directory
	•	Master Coder Protocol Documentation

⸻


<div align="center">


🧭 “Navigate Kansas Through Time.”

Built with MCP precision, open design, and historical empathy.

</div>
