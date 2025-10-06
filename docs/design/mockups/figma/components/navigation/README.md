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

This directory defines the **Navigation Components** designed in Figma and used in the Kansas Frontier Matrix web UI.  
They provide the interactive structure that lets users move through **space (map)** and **time (timeline)** in an intuitive,  
accessible way — mirroring the same component hierarchy implemented in the React/MapLibre frontend.

All components are exported as **Figma design assets** and mapped to their corresponding **React functional components**  
in the `/web/src/components/navigation/` directory.  

---

## 🧭 Directory Structure

```text
docs/design/mockups/figma/components/navigation/
├── README.md                 # Index (this file)
├── export/                   # Exported design assets (SVG/PNG)
│   ├── header/
│   ├── sidebar/
│   ├── menus/
│   ├── timeline/
│   └── controls/
└── specs/                    # Component specifications
    ├── header.spec.md
    ├── sidebar.spec.md
    ├── timeline.spec.md
    └── menus.spec.md


⸻

🎨 Design Tokens

Token	Example	Purpose
--kfm-color-bg	#0b1020 / #ffffff	Background colors (dark/light mode)
--kfm-color-fg	#e9edf3 / #0f1216	Text and icons
--kfm-color-accent	#4ea1ff	Focus, highlight, interaction
--kfm-radius-xl	16px	Corners for panels and buttons
--kfm-gap-sm..xl	8, 12, 16, 24	Spacing scale
--kfm-z-nav	1000	Layer ordering priority
--kfm-tap-target	44px	Minimum touch target size (accessibility)


⸻

🧩 Component Inventory

Component	Purpose	Figma Frame	React Mapping	Status
App Header	Primary navigation, brand, search	nav/header/default	<Header />	✅
Sidebar (Left)	Layer toggles, filters, legends	nav/sidebar/layers	<LayerSidebar />	✅
Detail Panel (Right)	Entity & event details	nav/sidebar/details	<DetailsPanel />	✅
Menus (Overflow)	Secondary actions	nav/menus/kebab	<OverflowMenu />	✅
Breadcrumbs	Hierarchical navigation	nav/breadcrumbs	<Breadcrumbs />	✅
Tabs	Section switcher (Map / Timeline / Docs)	nav/tabs/primary	<Tabs />	✅
Timeline Rail + Controls	Time navigation	nav/timeline/rail	<Timeline />	✅
Map Toolbar	Zoom, locate, measure	nav/controls/map	<MapToolbar />	✅
Command Palette	Global quick actions (⌘K)	nav/command	<CommandPalette />	🔄


⸻

🧭 Figma → Repo Workflow
	1.	Frame Naming Convention
Use nav/<region>/<component>/<state> — e.g., nav/timeline/rail/compact.
	2.	Export Process
	•	Export SVG for icons and PNG (2x) for previews.
	•	Store in export/<component>/.
	3.	Spec Documentation
	•	For each component, create or update specs/<component>.spec.md.
	•	Include: anatomy, spacing, states, ARIA roles, and React mapping.
	4.	Pull Request Checklist
	•	Add before/after thumbnails (use <details> collapsible blocks).
	•	Reference related design tickets or architecture docs.
	•	Verify proper rendering in GitHub preview.

⸻

♿ Accessibility Guidelines
	•	Keyboard — Tab/Shift+Tab navigates components logically.
	•	Focus — Visible ring using accent color, 3:1 contrast minimum.
	•	Touch — Controls ≥ 44 × 44 px.
	•	ARIA Roles — Each component annotated (role="tablist", aria-expanded, etc.).
	•	Color Contrast — Text and icon states meet WCAG AA.
	•	Timeline Text Alternative — Provide verbal equivalents (e.g., “Showing 1850–1875”).

⸻

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

<!-- END OF MERMAID -->



⸻

✅ Do & Don’t

Do
	•	Use design tokens consistently.
	•	Provide ARIA labels and keyboard navigation.
	•	Keep SVGs optimized (no hidden layers or groups).
	•	Update specs when UI or Figma assets change.

Don’t
	•	Hardcode pixel positions.
	•	Mix inconsistent icon sizes.
	•	Commit unoptimized or redundant image exports.

⸻

🧾 Contributing Checklist
	•	Figma frame follows nav/ naming pattern.
	•	Assets exported and placed correctly.
	•	Spec file created/updated.
	•	Screenshots added to PR.
	•	Verified GitHub rendering (Markdown + Mermaid).
	•	Linked to Web UI Design Document and Architecture.

⸻

📚 References
	•	Kansas Frontier Matrix — Web UI Design Document
	•	Kansas Frontier Matrix — Web UI Architecture
	•	Generate Architecture File
	•	Advanced GitHub Formatting Guide

⸻


<div align="center">


“Design for clarity. Build for reproducibility. Navigate through time.”
— Kansas Frontier Matrix Design System

</div>
