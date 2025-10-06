<div align="center">

# 🧭 Navigation Components — Figma Exports  
`docs/design/mockups/figma/components/navigation/`

**Kansas Frontier Matrix — Design System**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../docs/design/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🎯 Purpose

This directory houses the **navigation-related components** exported from Figma for the  
**Kansas Frontier Matrix** web application design system.  
These elements define how users move through the system — including **menus**, **headers**, **tabs**, and **map/timeline controls** — ensuring consistency between Figma mockups and live React components.

All navigation components are version-controlled, documented, and linked to their source in the Figma design file.

---

## 🧩 Directory Structure

```text
docs/design/mockups/figma/components/navigation/
├── README.md                     # Index and documentation (this file)
├── header/                       # Top-level site header & logo placement
├── sidebar/                      # Collapsible sidebar navigation
├── map-controls/                 # Zoom, layer toggles, compass, legends
├── timeline-controls/            # Time slider, play/pause buttons
├── breadcrumbs/                  # Page breadcrumbs & contextual paths
└── tabs/                         # Secondary navigation (tabbed sections)

Each subfolder contains:
	•	Exported SVG/PNG assets from Figma
	•	Optional .json metadata or .figspec.md describing component behavior
	•	Screenshots for documentation and version control comparison

⸻

🧱 Component Overview

Component	Description	Usage Context
Header	Fixed top navigation bar with branding and search.	Appears on all major views (Map, Timeline, Docs).
Sidebar	Expandable vertical menu for layers and filters.	Left side of UI (Map/Terrain view).
Map Controls	Buttons for zoom, compass, legend, and base layer toggles.	Overlay within MapLibre canvas.
Timeline Controls	Interactive slider and temporal filters.	Bottom timeline pane.
Breadcrumbs	Path indicators for detail or admin views.	Appears above content panels.
Tabs	Secondary navigation for sub-sections.	Used in admin, entity, and data panels.


⸻

🎨 Design Tokens

All Figma exports follow the shared Design Token Specification
defined under /docs/design/tokens/.

Token	Description	Example
--color-accent-nav	Primary accent color for navigation elements.	#2B5D9C
--font-nav	Font used for labels and menu items.	Inter / 14px
--radius-nav	Border radius for active buttons.	8px
--shadow-nav	Drop shadow used under fixed nav elements.	0 2px 6px rgba(0,0,0,0.1)


⸻

🧭 Interaction Guidelines
	•	Consistency: Navigation elements must match the Figma prototypes exactly in position, hierarchy, and typography.
	•	Responsiveness: Components adapt to desktop (split map/timeline view) and mobile (drawer navigation).
	•	Accessibility:
	•	All buttons include ARIA roles (aria-label, aria-current).
	•	Keyboard navigation via Tab and Enter supported.
	•	State Management:
	•	Active states shown with accent color highlight.
	•	Disabled states use 40% opacity of default token colors.

⸻

🔄 Figma Integration Workflow
	1.	All navigation components originate in
Figma › Kansas Frontier Matrix / Components / Navigation.
	2.	Components are exported as .svg or .png assets.
	3.	Each export includes metadata (width, height, color tokens).
	4.	Assets are versioned here and referenced in the web app at:
web/src/components/navigation/.

✅ Tip: Keep exported asset names identical to their Figma component names (e.g. header_logo.svg, timeline_play.svg) to ensure synchronization scripts function properly.

⸻

🧰 Developer Notes
	•	React Integration: Navigation elements correspond to components under
web/src/components/navigation/.
Example:

import Header from "@/components/navigation/Header";
import Sidebar from "@/components/navigation/Sidebar";


	•	CSS Tokens are imported globally from /web/src/styles/tokens.css.
	•	Testing: Interactive behaviors are verified via Cypress tests under tests/ui/navigation/.

⸻

📘 Related Documentation
	•	docs/design/README.md — Global design overview
	•	docs/design/mockups/figma/components/README.md — Component index
	•	web/src/components/navigation/ — Implementation
	•	tests/ui/navigation/ — Test suite

⸻


<div align="center">


Kansas Frontier Matrix Design System
🧭 Navigation as Knowledge — Guiding exploration through time and terrain.

</div>
