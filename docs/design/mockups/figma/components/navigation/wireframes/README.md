<div align="center">

# 🧭 Kansas Frontier Matrix — Navigation Wireframes  
`docs/design/mockups/figma/components/navigation/wireframes/`

**Interactive · Temporal · Spatial · Accessible Navigation**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Navigation%20Components-purple)](../figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 🎯 Purpose

This folder contains **exported wireframes** and supporting assets for the Kansas Frontier Matrix **Navigation Components**, as designed in Figma.  
They illustrate the system’s **core interaction model** — synchronizing time (timeline), space (map layers), and discovery (search + detail panel).  

These wireframes define:
- Spatial layout of the **timeline**, **map toolbar**, and **detail drawer**
- Interaction states (hover, focus, selected)
- Accessibility and keyboard navigation regions
- Layer toggles, timeline scrubbing, and search-to-zoom behaviors

---

## 📁 Directory Structure

```text
docs/design/mockups/figma/components/navigation/wireframes/
├── README.md                 # This spec (GitHub-rendered)
├── timeline-wireframe.png    # Timeline and scrub controls
├── map-toolbar.svg           # Layer toggle, zoom, locate
├── detail-panel.png          # Entity/event info panel
├── layout-overview.svg       # Combined layout reference
└── figma-refs.json           # Figma node reference metadata

Each image corresponds to a distinct Figma frame and is referenced in figma-refs.json with its component ID and version hash for design reproducibility.

⸻

🧩 System Integration (GitHub-safe Mermaid)

flowchart LR
  subgraph UI["Navigation UI Layer"]
    A["Header\nSearch · Menus · Tabs"]
    B["Timeline\nRange · Scrub · Zoom"]
    C["Map Toolbar\nZoom · Locate · Layers"]
    D["Detail Panel\nEntity/Event Dossier"]
  end

  subgraph Backend["API / State"]
    E["GET /events?start&end"]
    F["GET /layers-config"]
    G["GET /entity/{id}"]
  end

  subgraph State["React State Store"]
    H["selectedTimeRange"]
    I["activeLayers"]
    J["selectedEntity"]
  end

  A --> B
  A --> C
  B --> E
  C --> F
  D --> G
  E --> H
  F --> I
  G --> J
  H --> B
  H --> C
  J --> D

<!-- END OF MERMAID -->



⸻

🧭 Design Principles

Category	Principle	Implementation
Accessibility	Fully keyboard and screen-reader navigable	tabindex, ARIA roles, visible focus rings
Temporal Sync	Timeline filters map layers by time range	Emits { start, end } event to map component
Spatial Control	Layer toggles, opacity, basemap control	Controlled via STAC-driven layers.json
Detail Context	Clicking map or timeline populates detail panel	Fetches /entity/{id} from API
Consistency	Layout follows 12-column responsive grid	Maintained in all viewport breakpoints


⸻

🧠 Design Tokens (Excerpt)

Token	Example	Purpose
--kfm-color-bg	#0b1020 / #ffffff	Background (dark/light modes)
--kfm-accent	#4F9CF9	Interactive element color
--kfm-spacing-md	1rem	Layout padding consistency
--kfm-font-title	"Inter", sans-serif	Headings and UI text
--kfm-radius-lg	1rem	Panel and button corner radius


⸻

🔍 Provenance & Versioning

Asset	Source Figma Node	Export Date	Hash
timeline-wireframe.png	figma://node/23:118	2025-09-30	sha256-b3a1…
map-toolbar.svg	figma://node/24:44	2025-09-30	sha256-5ddc…
detail-panel.png	figma://node/25:92	2025-09-30	sha256-a712…


⸻

📚 Related Documents
	•	Navigation Components Spec
	•	Web UI Architecture
	•	System Architecture
	•	Monorepo Layout

⸻

🧾 License & Credits

Designs © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC-BY 4.0).
Wireframes produced by the KFM Design & Interaction Team using Figma.
For updates, see figma-refs.json and commit history.