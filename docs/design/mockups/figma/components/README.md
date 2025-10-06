<div align="center">

# 🧩 Kansas Frontier Matrix — Figma Components  
`docs/design/mockups/figma/components/`

**Mission:** Serve as the **single source of truth** for all modular, reusable Figma components  
and their corresponding React implementations in the **Kansas Frontier Matrix (KFM)** system.  

Each component embodies **clarity, accessibility, and consistency**, following the  
**Master Coder Protocol (MCP)** standards for documentation-first, open-source design.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../.github/workflows/site.yml)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-green)](https://www.w3.org/WAI/WCAG21/quickref/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-yellow)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The `/components/` directory holds all **modular Figma component exports and metadata** —  
the foundational building blocks that define the **visual and functional identity**  
of the Kansas Frontier Matrix.

Each component represents a **verified, reusable unit** — such as buttons, inputs,  
icons, map elements, or panels — and is maintained as part of the larger KFM **design system**  
to ensure complete parity between Figma and live React implementations.

---

## 🧭 Directory Structure

```text
docs/design/mockups/figma/components/
├── README.md                           # Index (this file)
├── buttons/                            # Primary and secondary button sets
├── panels/                             # Side panels, modals, drawers
├── timeline/                           # Timeline markers, slider, scale
├── map/                                # Map markers, tooltips, legend elements
├── inputs/                             # Form fields, toggles, dropdowns
├── icons/                              # Shared icon sets and variants
├── navigation/                         # Header, footer, tab controls
└── archive/                            # Deprecated or replaced components

Each subdirectory contains:
	•	📄 Component visuals (.png, .svg, .pdf)
	•	🧩 Metadata (.yml or .md)
	•	♿ Accessibility reports (if applicable)

⸻

🧱 Component Metadata Schema

Each component includes a metadata.yml file conforming to this schema:

id: button_primary_v2.1
title: Primary Button Component (v2.1)
author: design.system.team
date: 2025-10-06
source_figma: https://www.figma.com/file/ABCDE12345/KFM-Component-Library?node-id=112%3A212
description: >
  Standardized primary action button with accessible color contrast,
  focus outline, and consistent padding for all viewport sizes.
version: v2.1
category: button
status: active
accessibility:
  contrast_ratio: 5.0 : 1
  keyboard_focus: true
  reduced_motion: true
linked_docs:
  - ../../../../ui-guidelines.md
  - ../../../../style-guide.md
  - ../../../../interaction-patterns.md
license: CC-BY-4.0


⸻

🧮 Component Lifecycle Workflow

flowchart TD
    A["Design Component in Figma"] --> B["Accessibility Review\n(WCAG + Contrast)"]
    B --> C["Export + Annotate\n(PNG · SVG · Metadata)"]
    C --> D["Commit to /components/"]
    D --> E["Link to Implementation\n(web/src/components/)"]
    E --> F["Review Board Approval\n(docs/design/reviews/)"]
    F --> G["Archive Older Version"]

<!-- END OF MERMAID -->


Workflow Notes
	•	All new or updated components must pass accessibility review prior to commit.
	•	Superseded versions are archived with full metadata for provenance.
	•	Each approved component is cross-documented in Figma and GitHub for reproducibility.

⸻

♿ Accessibility Requirements

Criterion	WCAG Ref	Description	Validation Tool
Color Contrast	1.4.3	≥ 4.5:1 for text/icons	Stark / Able
Focus Visibility	2.4.7	Clearly visible focus indicators	Manual Review
Keyboard Reachability	2.1.1	Fully operable via keyboard	Manual
Motion Safety	2.3.3	Respects prefers-reduced-motion	Browser Simulation
ARIA Labels	4.1.2	Proper roles & labels documented	Manual Annotation

✅ Accessibility validation is part of every MCP compliance review.

⸻

🧩 Component Categories

Category	Description	Example ID	Related Docs
Buttons	Primary, secondary, icon-only variants	button_primary_v2.1	style-guide.md
Panels	Drawers, modals, sidebars with focus management	panel_drawer_v1.3	interaction-patterns.md
Timeline Elements	Ticks, markers, zoom handles	timeline_marker_v1.5	ui-guidelines.md
Map UI	Markers, legends, layer toggles	map_marker_v1.2	style-guide.md
Inputs	Text, checkbox, select, slider, datepicker	input_text_v2.0	ui-guidelines.md
Navigation	Headers, tabs, breadcrumbs	nav_header_v1.4	storytelling.md
Icons	Scalable system-wide icons	icon_close_v1.0	style-guide.md


⸻

🧾 Example Component Documentation

🟧 Primary Button (v2.1)

File: buttons/button_primary_v2.1.png
Figma Source: KFM Component Library →

The default primary action button for all core interactions.
Includes hover, focus, and disabled states. Tested across light/dark themes.

Accessibility Notes:
	•	Contrast ratio: 5.0:1
	•	Focus outline visible, outline-offset: 3px;
	•	Border radius: 8px
	•	Hover transition ≤ 150 ms

Linked Docs:
	•	../../../../ui-guidelines.md
	•	../../../../style-guide.md

⸻

🧠 Mapping to Frontend Components

Figma Component ID	React Component	Path	Notes
button_primary_v2.1	<ButtonPrimary />	/web/src/components/ButtonPrimary.tsx	Implements theme tokens
panel_drawer_v1.3	<DrawerPanel />	/web/src/components/panels/DrawerPanel.tsx	Includes focus trap
timeline_marker_v1.5	<TimelineMarker />	/web/src/components/timeline/Marker.tsx	Syncs with D3 data
map_marker_v1.2	<MapMarker />	/web/src/components/map/Marker.tsx	Layer toggle integration

🔄 Mappings are validated during design–development sync sessions.

⸻

🧩 Versioning & Archival

Status	Description	Action
Active	Current production version	Stored in /components/
Deprecated	Replaced by new version	Moved to /components/archive/
Experimental	Under testing	Flagged in metadata and reviews

Each update triggers a review entry documenting accessibility, visual, and version deltas.

⸻

🧾 Example Review Log Reference

File: docs/design/reviews/2025-10-06_button_primary_v2.1.md

design_id: button_primary_v2.1
reviewers:
  - ui_researcher
  - frontend_dev
status: approved
notes: >
  Verified contrast ratio 5:1; focus ring alignment consistent.
  Exported and synced with React component.
timestamp: 2025-10-06T21:00:00Z


⸻

🧰 Tools & Validation

Tool	Purpose	Output
Figma	Component design & prototype export	.fig, .png, .svg
Able / Stark	Accessibility + contrast tests	Contrast reports
yamllint / jsonschema	Metadata validation	CI pipeline log
Playwright	UI automation and accessibility testing	HTML report
Pre-commit Hooks	Enforce consistent metadata	Pass/fail before commit


⸻

🧩 Related Files
	•	../README.md — Figma mockups index
	•	../../../../ui-guidelines.md — Accessibility & structure rules
	•	../../../../style-guide.md — Color & typography tokens
	•	../../../../interaction-patterns.md — UI interactions
	•	../../../../reviews/ — Design review logs

⸻


<div align="center">


🧩 “Components are the DNA of design —

document them well, and the system lives forever.”
— Kansas Frontier Matrix Design System Team

</div>
