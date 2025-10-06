<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Wireframes  
`docs/design/mockups/map/wireframes/`

**Interactive · Temporal · Spatial · Intuitive**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains **wireframes and layout blueprints** for the **Map module** of the  
Kansas Frontier Matrix (KFM) web interface. These designs define how spatial and temporal layers  
are presented, toggled, and interacted with by users — uniting **map, timeline, and knowledge graph**  
in one seamless interface.

Wireframes illustrate:

- 🗺️ Map layout and toolbar regions (zoom, legend, layer controls).  
- 🕰️ Timeline integration overlay for temporal filtering.  
- 🔍 Search and filter controls for geographic or thematic queries.  
- 🧩 “Detail Panels” for contextual insights (AI summaries, metadata, imagery).  
- 🎨 Responsive behavior for desktop, tablet, and mobile displays.  
- ♿ Accessibility affordances (color contrast, keyboard navigation, ARIA roles).  

---

## 🧱 Directory Layout

```text
docs/design/mockups/map/wireframes/
├── README.md                     # This file (documentation spec)
├── map_wireframes_v1.fig          # Figma source (editable blueprint)
├── exports/                       # PNG/JPG exports of key wireframes
│   ├── map_ui_default.png         # Default desktop layout
│   ├── map_ui_mobile.png          # Mobile compact view
│   └── timeline_overlay.png       # Combined timeline/map layout
└── thumbnails/                    # Small previews for documentation site
    └── map_wireframe_thumb.png


⸻

🧩 Design System Integration

These wireframes correspond to the MapLibre GL-based viewer defined in
the KFM Web UI Architecture ￼.
Each component in the design has a one-to-one mapping with the React frontend modules:

UI Region	React Component	Description
🗺 Map Canvas	MapView.tsx	Core MapLibreGL instance rendering layers, basemaps, and popups.
🧭 Layer Control Panel	LayerControls.tsx	Toggle visibility of STAC layers (e.g., hydrology, topo, treaties).
🕰 Timeline Overlay	TimelineOverlay.tsx	Synchronizes temporal range with map filters.
📜 Detail Panel	DetailPanel.tsx	Displays entity details and AI-generated summaries.
🔍 Search Bar	SearchBar.tsx	Entity lookup with autosuggest (people, places, events).
💬 AI Assistant	AssistantPanel.tsx	Conversational interface for querying the knowledge graph.

All spatial layers represented in the wireframes correspond to STAC Items
(data/stac/items/*.json) and configured layers in web/config/layers.json.

⸻

🎨 Visual Specification

Element	Purpose	Example Style
Base Map	Neutral grayscale (emphasize overlay layers)	#EAEAEA land, #C4D7E0 water
Active Layer	Highlighted in color per theme	e.g., hydrology = #3A86FF, treaties = #FFADAD
Temporal Filter	Slider bar + year markers	D3-driven Canvas overlay
Popups / Tooltips	Present title + snippet + link	Rounded, semi-transparent white with shadow
Icons	Lucide-react icons for consistent style	MapPin, Layers, Clock, Search


⸻

🕹️ Interaction Flow (GitHub-Safe Mermaid)

flowchart LR
  A["User Loads Web App"] --> B["MapLibreGL Initializes\n(base + STAC layers)"]
  B --> C["Timeline Loads\n(time range: 1850–1950)"]
  C --> D["User Moves Slider\n→ Filters Layers by Time"]
  D --> E["Map Updates Layers\n(show only temporal matches)"]
  E --> F["User Clicks Marker\n→ Detail Panel Opens"]
  F --> G["AI Summary + Metadata Displayed"]
  G --> H["User Adjusts Filters or Queries\n(search or toggle layers)"]
  H --> E
<!-- END OF MERMAID -->


⸻

♿ Accessibility & Responsiveness
	•	Keyboard Navigation: All core interactions accessible via Tab, Enter, and Arrow keys.
	•	Color Contrast: WCAG 2.1 AA-compliant; dark mode included.
	•	ARIA Labels: Descriptive labels for screen reader use (aria-label, role="button").
	•	Responsive Breakpoints:
	•	≥1200px: Full timeline + sidebar.
	•	768–1199px: Collapsible panels.
	•	≤767px: Mobile “map-first” layout (timeline hidden by default).

⸻

🧾 Provenance & Workflow
	•	Wireframes created in Figma and exported to PNG/JPG for documentation.
	•	Linked data (thumbnails, metadata) validated through STAC layer definitions.
	•	Updates tracked in Git; each revision should increment the semver field above.
	•	Review process follows MCP Documentation-First principles:
	•	📖 Document → 🔧 Build → 🧪 Validate → 🔁 Iterate.

⸻

🧰 Related References
	•	Kansas Frontier Matrix Web UI Architecture
	•	docs/design/mockups/map/README.md
	•	docs/design/mockups/map/thumbnails/metadata/README.md
	•	data/stac/catalog.json

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Time · Terrain · History · Knowledge Graphs

</div>
```
