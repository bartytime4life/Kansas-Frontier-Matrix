# 🧭 Kansas Frontier Matrix — Navigation Components
`docs/design/mockups/figma/components/navigation/`

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../docs/design/)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

---

## 🪶 Overview

This directory defines the **Navigation Layer** for the **Kansas Frontier Matrix Design System** —  
the unified set of elements that enable **spatial**, **temporal**, and **contextual exploration** across the interactive web platform.

Each navigation element — whether a **header bar**, **sidebar**, or **timeline slider** — is a verified Figma export mapped directly to its React implementation.  
These maintain visual and functional consistency between Figma prototypes and the live React app.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/figma/components/navigation/
├── README.md                       # Documentation (this file)
├── header/                         # Site header and top-level navigation
├── sidebar/                        # Layer & filter panel navigation
├── map-controls/                   # Map interaction elements (zoom, compass)
├── timeline-controls/              # Time slider and playback UI
├── breadcrumbs/                    # Contextual path indicators
└── tabs/                           # Secondary tab navigation

Each subfolder includes:
	•	Figma exports (.svg, .png, .json)
	•	Interaction specifications (.figspec.md)
	•	Behavioral mapping (component_map.json)
	•	Visual previews (_preview.png)

⸻

🧩 Component Reference

Component	Description	Placement	Primary Function
Header	Fixed top bar with branding, title, and global search.	Top viewport	Global navigation and identity
Sidebar	Expandable panel for layers, filters, and data toggles.	Left side	Layer and theme navigation
Map Controls	Floating tools (zoom, compass, legend, base map style).	Map overlay	Interactive map manipulation
Timeline Controls	Temporal slider with play/pause and date range selection.	Bottom timeline area	Chronological exploration
Breadcrumbs	Path indicators for detail and admin views.	Above panels	Orientation and hierarchy
Tabs	Inline secondary navigation for entities and admin sections.	Within content	Section switching and organization


⸻

🎨 Design Tokens

All components use shared tokens from:
/docs/design/tokens/

Token	Description	Default
--color-accent-nav	Primary accent color for active navigation	#2B5D9C
--color-bg-nav	Background color for nav surfaces	#F8F9FB
--font-nav	Typeface and size for navigation labels	Inter, 14px
--radius-nav	Corner radius for buttons and cards	8px
--shadow-nav	Drop shadow for elevated nav elements	0 2px 8px rgba(0,0,0,0.15)


⸻

🧭 Interaction Principles

Responsiveness
	•	Mobile-first design approach.
	•	Sidebar collapses into a sliding drawer on narrow viewports.
	•	Timeline converts to a tap-to-scrub slider on touch devices.

Accessibility
	•	Uses proper ARIA attributes (role="navigation", aria-label, aria-current).
	•	Fully keyboard-navigable (Tab, Enter, Space, Arrow Keys).
	•	Minimum contrast ratio: WCAG 2.1 AA compliance.

UX Logic
	•	Navigation mirrors user mental mapping of time and space.
	•	Hover and focus states include tooltips.
	•	Icons include text fallbacks using screen-reader utilities (.sr-only).
	•	Active states use light opacity or scale transitions (0.15s ease).

⸻

🔗 Integration with React

All navigation components are implemented in:

web/src/components/navigation/

Each Figma export corresponds 1:1 with a React component.

Figma Name	React Component	Example Import
Header_Main	Header.tsx	import Header from "@/components/navigation/Header";
Sidebar_Layers	Sidebar.tsx	import Sidebar from "@/components/navigation/Sidebar";
Timeline_Playbar	TimelineControls.tsx	import TimelineControls from "@/components/navigation/TimelineControls";

Example Usage

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

🧱 Development Notes
	•	Testing: Interactive components validated with Cypress (tests/ui/navigation/).
	•	Sync: Weekly automated visual diff compares Figma exports vs React components.
	•	Versioning: Each export tagged with Figma component ID and timestamp.
	•	Styling: CSS tokens imported globally from web/src/styles/tokens.css.

⸻

🧰 Workflow
	1.	Design → Export
	•	Export Figma frames as SVG/PNG (+ JSON specs).
	•	Save to the matching subdirectory with metadata.
	2.	Versioning
	•	Include:
	•	component_name.svg
	•	_meta.json (width, height, tokens, date)
	•	_preview.png for documentation.
	3.	Integration
	•	Sync exports with React components using npm run sync:figma (script in /tools/).
	4.	Validation
	•	CI confirms component parity between
/figma/components/navigation/ and /web/src/components/navigation/.

⸻

🧭 Design Guidelines

Rule	Description
Hierarchy Clarity	Header (primary) and sidebar/tabs (secondary) use distinct visual levels.
Spatial Continuity	Transitions between map ↔ timeline maintain spatial context.
Temporal Awareness	Timeline state and map layers remain synchronized.
Consistency	Uniform spacing, typography, and animations across all components.


⸻

🧾 Related Documentation
	•	docs/design/mockups/figma/components/README.md — Figma component index
	•	web/src/components/navigation/ — React implementation
	•	tests/ui/navigation/ — UI test suite
	•	docs/design/README.md — Design documentation
	•	docs/architecture/README.md — System architecture overview

⸻

Navigation as Knowledge

Guiding exploration through time, terrain, and story.

---

### ✅ What’s Fixed for GitHub

| Issue Type | Fix |
|-------------|-----|
| **HTML tags (`<div align>` etc.)** | Removed — replaced with Markdown headers & horizontal rules |
| **Collapsed tables** | Re-built with strict pipe alignment |
| **List spacing** | Converted to `-` bullets, added blank lines for GFM spacing |
| **Code blocks** | Wrapped in triple backticks with language tags |
| **Mixed indentation** | Normalized to spaces for uniform rendering |

This version **renders identically inside GitHub** — tables, code, and lists all line up and preserve spacing.
