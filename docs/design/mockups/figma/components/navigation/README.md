# 🧭 Kansas Frontier Matrix — Navigation Components
`docs/design/mockups/figma/components/navigation/`

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../docs/design/)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../.github/workflows/site.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

---

## Overview

This directory defines the **Navigation Layer** for the **Kansas Frontier Matrix** design system: the header, sidebar, map controls, timeline controls, breadcrumbs, and tabs that enable spatial, temporal, and contextual exploration.

Every navigation element is a verified Figma export mapped to a React component, ensuring consistency between mockups and the live app.

---

## Directory Layout

```text
docs/design/mockups/figma/components/navigation/
├── README.md                       # This file
├── header/                         # Site-wide header: logo, title, global nav
├── sidebar/                        # Layer, legend, and filter navigation panels
├── map-controls/                   # Zoom, compass, layer toggles, legend button
├── timeline-controls/              # Temporal slider and playback UI
├── breadcrumbs/                    # Contextual path indicators
└── tabs/                           # Secondary, in-panel navigation

Each subfolder typically includes:
	•	Figma exports (.svg, .png)
	•	Interaction specs (.figspec.md)
	•	Mapping to React (component_map.json)
	•	Visual preview (_preview.png)

⸻

Component Reference

Component	Description	Placement	Primary Function
Header	Fixed top bar with branding, title, and global search	Top viewport	Global navigation and identity
Sidebar	Expandable panel with layers, filters, and legends	Left side	Thematic and layer navigation
Map Controls	Floating tools: zoom, compass, legend, base style toggle	Map overlay	Map manipulation
Timeline Controls	Temporal slider with play/pause and step controls	Bottom timeline area	Chronological navigation
Breadcrumbs	Contextual path indicators for detail/admin views	Above content panels	Orientation and hierarchy
Tabs	Inline secondary navigation for entity or admin sub-sections	Within content	Section switching and organization


⸻

Design Tokens

All navigation components derive from tokens defined in:
/docs/design/tokens/

Token	Description	Default
--color-accent-nav	Accent color for active navigation elements	#2B5D9C
--color-bg-nav	Navigation surface background	#F8F9FB
--font-nav	Typeface and size for labels/controls	Inter, 14px
--radius-nav	Corner radius for buttons/cards	8px
--shadow-nav	Elevation shadow for fixed/floating nav	0 2px 8px rgba(0,0,0,0.15)


⸻

Interaction Principles

Responsiveness
	•	Mobile-first layouts.
	•	Sidebar collapses to a drawer on small screens.
	•	Timeline supports tap-to-scrub gestures on touch devices.

Accessibility
	•	ARIA attributes: role="navigation", aria-label, aria-current.
	•	Fully keyboard navigable: Tab, Enter, Space, arrow keys where applicable.
	•	Contrast adheres to WCAG 2.1 AA minimums.

UX Logic
	•	Time and space are primary axes of wayfinding.
	•	Hover/focus states include concise tooltips.
	•	Icons include text fallbacks using visually-hidden classes (e.g., a .sr-only utility).
	•	Active states use subtle opacity/scale transitions (0.15s ease).

⸻

React Integration

Navigation components are implemented under:

web/src/components/navigation/

Name parity is maintained between Figma and React.

Figma Name	React Component	Example Import
Header_Main	Header.tsx	import Header from "@/components/navigation/Header";
Sidebar_Layers	Sidebar.tsx	import Sidebar from "@/components/navigation/Sidebar";
Timeline_Playbar	TimelineControls.tsx	import TimelineControls from "@/components/navigation/TimelineControls";

Example usage:

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

Development Notes
	•	Testing: interactive flows covered with Cypress at tests/ui/navigation/.
	•	Figma–React sync: compared weekly with automated visual diffs.
	•	Versioning: each asset revision tags the Figma component ID and export timestamp.
	•	CSS tokens: imported globally from web/src/styles/tokens.css.

⸻

Workflow
	1.	Design → Export
	•	Export Figma frames as SVG/PNG with a JSON spec if needed.
	•	Save to the corresponding subdirectory with metadata.
	2.	Versioning
	•	Include:
	•	component_name.svg
	•	_meta.json (width, height, color tokens, date)
	•	_preview.png for docs
	3.	Integration
	•	Sync assets to React via npm run sync:figma (Node script in /tools/).
	4.	Validation
	•	CI verifies parity: the count in /figma/components/navigation/
equals the implemented components in /web/src/components/navigation/.

⸻

Design Guidelines

Rule	Description
Hierarchy Clarity	Primary (header) and secondary (sidebar/tabs) layers look and behave distinct.
Spatial Continuity	Map/timeline transitions preserve orientation and context.
Temporal Awareness	Timeline controls and map states stay synchronized to the same time window.
Consistency	Spacing, typography, and animation timings are standardized across views.


⸻

Related Documentation
	•	docs/design/mockups/figma/components/README.md — Figma component index
	•	web/src/components/navigation/ — React implementation
	•	tests/ui/navigation/ — UI test suite
	•	docs/design/README.md — Design architecture
	•	docs/architecture/README.md — System overview

⸻

Navigation as Knowledge

Guiding exploration through time, terrain, and story.
