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

This directory defines the **Navigation Layer** for the **Kansas Frontier Matrix Design System** —  
all interface elements that enable **spatial**, **temporal**, and **contextual exploration** across the  
interactive web platform.

Each navigation element — whether a **header bar**, **sidebar**, or **timeline slider** — is a verified  
Figma export mapped directly to its React implementation. These components maintain cohesion  
between design prototypes and live deployments, ensuring seamless user experience and historical clarity.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/figma/components/navigation/
├── README.md                       # Documentation & usage guidelines (this file)
├── header/                         # Site-wide header: logo, title, global nav
├── sidebar/                        # Layer, legend, and filter navigation panels
├── map-controls/                   # Zoom, compass, layer toggle buttons
├── timeline-controls/              # Temporal slider & playback UI
├── breadcrumbs/                    # Path context in detail & admin views
└── tabs/                           # Secondary content navigation (tabbed layout)

Each subfolder includes:
	•	Figma exports (.svg, .png, .json)
	•	Interaction specifications (.figspec.md)
	•	Behavioral mapping to React (component_map.json)
	•	Visual previews for documentation (_preview.png)

⸻

🧩 Component Reference

Component	Description	Placement	Primary Function
Header	Fixed top bar with branding, project title, and global search.	Top viewport	Persistent global nav & identity
Sidebar	Expandable panel with map layers, filters, and data toggles.	Left side	Thematic and layer navigation
Map Controls	Floating set of tools (zoom, compass, legend, style toggles).	Map overlay	Interactive map manipulation
Timeline Controls	Horizontal temporal slider with play/pause buttons.	Bottom	Controls chronological visualization
Breadcrumbs	Contextual path indicators for detail and admin views.	Above content panels	Orientation & hierarchy
Tabs	Inline secondary navigation for entity views or admin panels.	Within content	Sectional switching & categorization


⸻

🎨 Design Tokens

All components derive from global tokens defined in
/docs/design/tokens/.
Use of tokens ensures consistent styling across Figma, CSS, and React.

Token	Description	Default
--color-accent-nav	Primary accent for active navigation elements.	#2B5D9C
--color-bg-nav	Background color for nav surfaces.	#F8F9FB
--font-nav	Typeface for menu labels and controls.	Inter, 14px
--radius-nav	Corner radius for nav buttons & cards.	8px
--shadow-nav	Shadow under fixed headers or floating nav.	0 2px 8px rgba(0,0,0,0.15)


⸻

🧭 Interaction Principles

📱 Responsiveness
	•	All navigation components are mobile-first.
	•	Sidebar collapses into a floating drawer on small screens.
	•	Timeline becomes a tap-to-scrub slider with gesture support.

♿ Accessibility
	•	Uses ARIA roles (role="navigation", aria-label, aria-current).
	•	All elements are fully keyboard-navigable (Tab, Enter, Arrow Keys).
	•	Minimum contrast ratio: WCAG 2.1 AA.

🧠 UX Logic
	•	Navigation reflects user cognitive mapping — time and space are primary axes.
	•	Hover states show tooltips for clarity.
	•	Each icon includes text fallback (<span class="sr-only">) for screen readers.
	•	Active states animate subtly with opacity and scale transitions (0.15s ease).

⸻

🔗 Integration with React

All navigation components are implemented under:

web/src/components/navigation/

Each Figma export corresponds to a React component, maintaining name parity:

Figma Name	React Component	Example Import
Header_Main	Header.tsx	import Header from "@/components/navigation/Header";
Sidebar_Layers	Sidebar.tsx	import Sidebar from "@/components/navigation/Sidebar";
Timeline_Playbar	TimelineControls.tsx	import TimelineControls from "@/components/navigation/TimelineControls";


⸻

🧱 Development Notes
	•	Testing: Interactive elements tested via Cypress (tests/ui/navigation/)
	•	Documentation: Figma–React sync verified weekly via automated diff visual tests.
	•	Version Control: Each asset revision tagged with Figma version ID and export timestamp.
	•	CSS Tokens: Imported globally from /web/src/styles/tokens.css

Example Component Usage

import Header from "@/components/navigation/Header";
import Sidebar from "@/components/navigation/Sidebar";
import TimelineControls from "@/components/navigation/TimelineControls";

export default function Layout() {
  return (
    <>
      <Header />
      <Sidebar />
      <TimelineControls />
    </>
  );
}


⸻

🧰 Workflow

1. Design → Export
	•	Figma components exported using Frame → SVG/PNG + JSON spec.
	•	Saved to corresponding subdirectory with metadata.

2. Versioning
	•	Each export includes:
	•	component_name.svg
	•	_meta.json (width, height, color tokens, date)
	•	_preview.png for documentation

3. Integration
	•	Exports synced with React components during npm run sync:figma (Node script under /tools/).

4. Validation
	•	CI verifies parity: component count in /figma/components/navigation/
equals implemented React components in /web/src/components/navigation/.

⸻

🧭 Design Guidelines

Design Rule	Description
Hierarchy Clarity	Primary (header) and secondary (sidebar/tabs) nav layers are visually distinct.
Spatial Continuity	Transitions between map/timeline maintain orientation and user context.
Temporal Awareness	Timeline controls and map states are synchronized to the same temporal domain.
Consistency	Component spacing, typography, and animation timings are standardized across all views.


⸻

🧾 Related Documentation
	•	docs/design/mockups/figma/components/README.md – Figma component index
	•	web/src/components/navigation/ – React implementation
	•	tests/ui/navigation/ – UI test suite
	•	docs/design/README.md – Design architecture
	•	docs/architecture/README.md – System overview

⸻


<div align="center">


🧭 Kansas Frontier Matrix — Navigation as Knowledge

“Guiding exploration through time, terrain, and story.”

</div>
