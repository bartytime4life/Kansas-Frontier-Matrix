<div align="center">

# 🧩 Kansas Frontier Matrix — Panels Wireframes  
`docs/design/mockups/panels/wireframes/`

**Purpose:** Define the structure, behavior, and visual hierarchy of **panel-based components**  
for the Kansas Frontier Matrix (KFM) Web UI — including the **Detail Panel**, **AI Assistant Panel**,  
and **Layer/Filter Control Panels**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains **wireframes and specifications** for interactive **UI panels** that appear  
within the KFM web application alongside the Map and Timeline interfaces.  
These panels act as **contextual views** — displaying entity details, AI-generated summaries,  
data filters, or search results synchronized with the map and timeline.

The design prioritizes:
- 📊 **Information hierarchy** — clear distinction between summaries, metadata, and AI insights.  
- 🔍 **Context sensitivity** — panel contents adapt dynamically to user selections.  
- ⚙️ **Reproducibility** — design metadata and layout blueprints linked to Figma files.  
- ♿ **Accessibility** — keyboard and screen-reader compatible layouts.  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/panels/wireframes/
├── README.md                      # This file
├── panel_wireframes_v1.fig         # Figma master file for all panel wireframes
├── exports/                        # PNG/JPG exports for documentation
│   ├── detail_panel_default.png
│   ├── ai_assistant_panel.png
│   ├── filter_layer_panel.png
│   └── mobile_stack_panel.png
└── metadata/                       # JSON metadata for each panel wireframe
    └── panel_wireframes_metadata.json


⸻

🧱 Panel Types and Design Intent

Panel Type	Description	Key Interactions	Data Sources
🧾 Detail Panel	Displays details of a selected entity (Person, Place, Event).	Scrollable; tabs for sources, timeline, and AI summaries.	Neo4j Knowledge Graph + STAC metadata
🤖 AI Assistant Panel	Conversational UI for querying historical data.	Input field + context suggestions; chat bubbles.	AI/NLP API (FastAPI endpoint /ask)
🧭 Layer/Filter Panel	Controls layer visibility and time-based filters.	Toggles, sliders, and color legends.	web/config/layers.json
🔍 Search/Results Panel	Displays search results for entities or events.	Interactive list with hover highlights on map/timeline.	Search API (/search?q=)
📱 Mobile Stack Panel	Responsive variant combining detail and AI panels.	Swipable, collapsible.	Composite of others, simplified for mobile.


⸻

🧩 Wireframe Interaction Flow (Mermaid)

flowchart LR
  A["User Selects Entity\n(on Map or Timeline)"] --> B["Detail Panel Opens\n(loads entity details)"]
  B --> C["AI Assistant Suggests Related Context\n(e.g. nearby events, similar sites)"]
  C --> D["User Opens AI Assistant Panel"]
  D --> E["User Queries → Backend /ask Endpoint"]
  E --> F["AI Response Rendered in Chat Interface"]
  F --> G["User Toggles Layers or Filters"]
  G --> H["Layer/Filter Panel Updates Map View"]
  H --> A
<!-- END OF MERMAID -->


⸻

🎨 Visual Standards

Element	Font / Size	Color Tokens	Behavior
Header	Inter	18px bold	--kfm-color-fg / --kfm-color-bg
Subsection Tabs	Inter	14px medium	Highlighted on selection
Content Body	Inter	14px regular	Scrollable region
Divider Lines	1px solid	--kfm-color-border	Always visible
Icons	Lucide-react	16px–24px	ARIA-labeled
Scrollbars	Minimal	--kfm-color-scroll	Auto-hide on inactivity

Panels adhere to the Design Token System defined in
web/src/styles/tokens.css, ensuring consistent theming between light/dark modes.

⸻

♿ Accessibility Compliance
	•	Keyboard Navigation: All panel components accessible via Tab, Shift+Tab, and Enter keys.
	•	Screen Reader Support: ARIA roles for tabs, headings, and buttons.
	•	Contrast: Minimum 4.5:1 per WCAG 2.1 AA.
	•	Responsive Layouts: Automatically adjust for viewport breakpoints:
	•	≥1200px: Dual-panel mode (Map + Detail + Assistant)
	•	768–1199px: Collapsible side panels
	•	≤767px: Stacked “sheet” panels for mobile

⸻

🧾 Provenance & Validation
	•	Design Source: Figma file panel_wireframes_v1.fig
	•	Metadata Schema: Validated against schema/panel_wireframe.schema.json
	•	Generated Thumbnails: Stored in ../thumbnails/metadata/
	•	Checksums: SHA-256 hashes for each export to ensure design reproducibility
	•	Validation Pipeline: Included in CI (stac-validate.yml and jsonschema.yml)

Manual validation:

python -m jsonschema -i metadata/panel_wireframes_metadata.json schema/panel_wireframe.schema.json


⸻

📚 Related References
	•	Panels (Main Mockup Directory)
	•	Map Wireframes
	•	AI Assistant Wireframes
	•	Kansas Frontier Matrix Web UI Architecture
	•	Accessibility Standards

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Time · Terrain · History · Knowledge Graphs

</div>
```
