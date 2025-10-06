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

The **Navigation Components** define the **core movement and exploration tools** for the Kansas Frontier Matrix (KFM) web interface — the bridge between **space**, **time**, and **knowledge**. These elements synchronize the **map**, **timeline**, and **detail panels** across devices.

Every component originates from the **Figma design library** and corresponds to a React implementation in `/web/src/components/navigation/`.

---

## 🧭 Component Hierarchy

```text
docs/design/mockups/figma/components/navigation/
├── README.md
├── header/                         # Global top navigation bar & search
├── sidebar/                        # Layer controls, filters, legends
├── timeline-controls/              # Time rail, zoom handles, play/pause
├── map-toolbar/                    # Zoom, locate, layers toggle, mode switch
└── panels/                         # Details + context drawers


⸻

🧩 System Integration (GitHub-safe Mermaid)

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



⸻

🧱 Responsive Layout Modes

flowchart TD
  D["Desktop Layout\nFull timeline + map + side panels"] --> T["Tablet\nToggle timeline panel"]
  T --> M["Mobile\nStacked map + slide-up timeline"]

<!-- END OF MERMAID -->



⸻

⚙️ State Lifecycle (deterministic updates)

stateDiagram-v2
  [*] --> Idle
  Idle --> Loading: fetchData()
  Loading --> Ready: setState(data)
  Ready --> Updating: userInteraction()
  Updating --> Ready: render()

<!-- END OF MERMAID -->



⸻

🎨 Design Tokens (extract)

Token	Example	Purpose
--kfm-color-bg	#0b1020 / #ffffff	Background (dark/light)
--kfm-color-fg	#fafafa / #111111	Text
--kfm-accent	#22a7f0	Interactions
--kfm-radius-lg	12px	Corners
--kfm-shadow-md	0 2px 8px rgba(0,0,0,0.25)	Elevation

Tokens live in /web/src/styles/tokens.css and are consumed by all navigation elements.

⸻

🔌 API touchpoints
	•	/api/events?start={t0}&end={t1} → timeline window
	•	/api/layers-config → map layer toggles
	•	/api/entity/{id} → detail panel content

⸻

♿ Accessibility
	•	Keyboard: Tab, Enter, arrows on sliders
	•	ARIA roles on sliders, toggles, menus
	•	AA contrast min; focus-visible styles
	•	Touch gestures on ≤768px

⸻

🧾 Source
	•	Design: Figma (shared KFM lib)
	•	Frontend: React 18 + MapLibre GL
	•	Backend: FastAPI + Neo4j
	•	Maintainer: KFM Design Team
	•	Last Updated: 2025-10
