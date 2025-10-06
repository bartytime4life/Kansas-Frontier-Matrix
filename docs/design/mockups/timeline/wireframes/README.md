<div align="center">

# 🕰️ Kansas Frontier Matrix — Timeline Wireframes  
`docs/design/mockups/timeline/wireframes/`

**Purpose:** Define and document wireframe layouts for the **Timeline UI module** of the  
Kansas Frontier Matrix (KFM) — visualizing how time and story synchronize with map,  
knowledge graph, and AI assistant panels.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

The **Timeline component** is a core feature of the Kansas Frontier Matrix web interface.  
It allows users to traverse history dynamically — exploring **events, periods, and entities**  
through an interactive time slider synchronized with the map and detail panels.

This directory contains **Figma wireframes**, **exported previews**, and **metadata** describing  
timeline design variations (e.g., horizontal scroll, condensed mode, and mobile view).

---

## 🗂️ Directory Layout

```text
docs/design/mockups/timeline/wireframes/
├── README.md                      # This file
├── timeline_wireframes_v1.fig      # Master Figma source for timeline layouts
├── exports/                        # Image exports of wireframes
│   ├── timeline_default.png
│   ├── timeline_condensed.png
│   ├── timeline_mobile.png
│   └── timeline_overlay_map.png
└── metadata/                       # JSON metadata for each wireframe
    └── timeline_wireframes_metadata.json


⸻

🧱 Design Goals

Objective	Description
🕰️ Temporal Navigation	Users should scroll or zoom across years, decades, or centuries smoothly.
🗺️ Map Synchronization	The timeline’s range filters data shown on the map (via STAC layer temporal metadata).
📑 Event Representation	Each event node or span should link to a KFM Knowledge Graph entity (with type, date, and source).
🎞️ Storytelling Mode	Support playback of events through animation or scrubber-based “story mode.”
⚙️ Flexibility	Adaptable to different datasets (historical periods, environmental data, etc.).
♿ Accessibility	Fully keyboard navigable and color-contrast compliant (WCAG 2.1 AA).


⸻

🧩 Key Components (UI Regions)

Component	Function	React Module
TimelineCanvas	Renders years, tick marks, and event nodes via Canvas or D3.js.	TimelineCanvas.tsx
TimelineRangeSelector	Allows range selection and zooming (drag handles).	RangeSelector.tsx
TimelinePlayControls	Playback, step, and pause controls for dynamic visualization.	TimelineControls.tsx
EventTooltip / Popup	Displays summary info for hovered or selected events.	EventTooltip.tsx
PeriodBands	Colored overlays denoting historical eras (linked to PeriodO).	PeriodBands.tsx


⸻

🕹️ Interaction Flow (GitHub-safe Mermaid)

flowchart LR
  A["User Loads Page"] --> B["Timeline Initializes\n(loads events from API)"]
  B --> C["Map Syncs to Initial Time Range"]
  C --> D["User Scrolls or Zooms Timeline"]
  D --> E["Visible Range Updates"]
  E --> F["Map and Panels Refresh with Filtered Events"]
  F --> G["User Clicks Event Node"]
  G --> H["Detail Panel Opens → Linked Data Loaded"]
  H --> I["User Activates Play Controls"]
  I --> J["Timeline Animates Over Period\n(showing evolving data layers)"]
  J --> C
<!-- END OF MERMAID -->


⸻

🎨 Visual Design Standards

Element	Font / Size	Color Tokens	Notes
Year Labels	Inter 12–14px	--kfm-color-fg-muted	Visible at varying zoom levels
Event Nodes	Circle / 6–10px	Thematic colors by type (e.g. --kfm-color-accent-war, --kfm-color-accent-climate)	Tooltip-enabled
Era Bands	Semi-transparent rectangles	Light tints by PeriodO ID	Denote broader historical context
Background	Neutral gray gradient	#F5F6F7	Maintains clarity in light/dark modes
Playback Buttons	Icon-only, 20–24px	--kfm-color-primary	ARIA-labeled for screen readers


⸻

♿ Accessibility & Responsiveness
	•	Keyboard Support:
	•	← / → — step backward/forward
	•	+ / - — zoom in/out
	•	Space — play/pause animation
	•	ARIA Labels:
All interactive elements labeled (role="slider", aria-valuenow for handles).
	•	Contrast:
Minimum 4.5:1 contrast verified for all text and icons.
	•	Responsive Layouts:
	•	≥1200px: Full-width timeline + play controls
	•	768–1199px: Collapsible controls
	•	≤767px: Compact vertical timeline for mobile

⸻

🧾 Provenance & Validation
	•	Design Source: timeline_wireframes_v1.fig
	•	Metadata Schema: Validated via schema/timeline_wireframe.schema.json
	•	Exports: Linked in ../thumbnails/metadata/ with SHA-256 checksums
	•	Validation Pipelines:
	•	jsonschema.yml — schema validation
	•	stac-validate.yml — linkage to STAC temporal fields

Manual Validation Example:

python -m jsonschema -i metadata/timeline_wireframes_metadata.json schema/timeline_wireframe.schema.json


⸻

🧮 Linked Standards
	•	Temporal Ontology: W3C OWL-Time
	•	Historical Periods: PeriodO
	•	Cultural Heritage Context: CIDOC CRM
	•	Geospatial Alignment: STAC 1.0.0

⸻

📚 Related References
	•	Timeline Module (Design Overview)
	•	Panels Wireframes
	•	Map Wireframes
	•	Kansas Frontier Matrix Web UI Architecture
	•	Accessibility Standards

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Time · Terrain · History · Knowledge Graphs

</div>
```
