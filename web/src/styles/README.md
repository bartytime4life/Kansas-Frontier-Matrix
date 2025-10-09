<div align="center">

# 🎨 Kansas Frontier Matrix — Web Frontend Styles  
`web/src/styles/`

**Design System · Theming · Layout Grid · Accessibility Tokens**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../.github/workflows/ci.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../docs/design/reviews/accessibility/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/src/styles/` directory defines the **visual identity and design tokens**  
for the Kansas Frontier Matrix Web Application.  

It implements a **modular styling system** that unifies typography, colors, spacing,  
and responsive layouts across all components — ensuring visual consistency and  
accessibility in line with the **Master Coder Protocol (MCP)** design standards.  

The styles follow a **documentation-first** pattern and reference the broader  
Design System defined under `docs/design/` (typography, mockups, accessibility reviews).

---

## 🧱 Directory Structure

```text
web/src/styles/
├── base.css              # Tailwind base + reset + global rules
├── variables.scss        # CSS custom properties (colors, spacing, z-index)
├── typography.scss       # Font scale, heading hierarchy, readability tweaks
├── layout.scss           # Grid + flex utilities for panels and timeline
├── map.scss              # MapLibre and legend overlays styling
├── timeline.scss         # Canvas timeline colors, markers, transitions
├── theme-dark.scss       # Dark mode color palette
├── theme-light.scss      # Light mode palette
├── animations.scss       # Framer Motion + keyframe definitions
└── index.scss            # Master import, compiled into build CSS

Each file maps to a specific UI domain (global, layout, or feature-specific)
so that changes can be made without side effects elsewhere.

⸻

🎨 Design Tokens

Token	Example	Description
--kfm-color-bg	#0b1020 / #ffffff	Background (dark/light)
--kfm-color-accent	#00b3b3	Primary accent color
--kfm-color-text	#eaeaea / #111	Text color for contrast
--kfm-radius	1rem	Border radius for panels and buttons
--kfm-shadow	0 2px 8px rgba(0,0,0,0.15)	Standard drop shadow
--kfm-spacing	8px, 16px, 24px	Spacing increments
--kfm-z-map, --kfm-z-timeline	100, 200	Layer stacking order

Design tokens are defined in variables.scss and injected globally via
CSS variables. These tokens can also be read by JavaScript for adaptive theming.

⸻

🧩 Layout & Responsive Grid

flowchart LR
  A["Header\n(nav, search, login)"] --> B["Main Area\nMapView + DetailPanel"]
  B --> C["Timeline\n(Canvas/D3 overlay)"]
  B --> D["Sidebar\nLayerControls & Legends"]
  A --> D
%% END OF MERMAID

The layout grid uses a flex-based 3-column structure with adjustable
breakpoints:

Breakpoint	Min Width	Layout Behavior
sm	480px	Collapsed timeline + stacked panels
md	768px	Split map + timeline view
lg	1024px	Full 3-panel layout (map, sidebar, timeline)
xl	1440px	Adds detail panel & AI assistant columns

All spacing and font scaling are responsive using clamp() functions.

⸻

🖼️ Theming System

Dark and light themes are managed through CSS variables and a <html data-theme="light|dark"> attribute.
Users can toggle themes from the header panel; the app remembers preferences via localStorage.

Theme	Base	Accent	Text	Background
Light	#ffffff	#00b3b3	#111111	#f9f9f9
Dark	#0b1020	#00e6e6	#eaeaea	#0b1020

Transitions between themes are animated with Framer Motion for smooth visual shifts.

⸻

✨ Animations

Animations are defined in animations.scss and integrated with Framer Motion.
They emphasize subtle motion, not distraction — e.g.:

Animation	Purpose
fade-in	Smooth load of map layers and panels
slide-up	Timeline events appearing in sequence
pulse	Highlighting selected map markers
sway	Background gradient motion (thematic flourish)

Animations follow WCAG accessibility best practices (respecting prefers-reduced-motion).

⸻

♿ Accessibility (WCAG 2.1 AA)

All colors and contrasts are tested for WCAG AA compliance using the
--kfm-color-text and --kfm-color-bg variables.
	•	Minimum contrast ratio: 4.5:1
	•	Focus states use visible outlines (outline: 2px solid var(--kfm-color-accent);)
	•	Keyboard navigation supported across all panels
	•	Font scaling respects OS accessibility settings

Accessibility audit scripts are maintained in
docs/design/reviews/accessibility/.

⸻

🧩 Example Usage

@import "variables";
@import "theme-dark";
@import "layout";

.app-container {
  background-color: var(--kfm-color-bg);
  color: var(--kfm-color-text);
  transition: background 0.3s ease;
}

This pattern ensures consistent theming and safe composability across components.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	Design tokens from docs/design/mockups/ and accessibility audit reports
Outputs	Compiled CSS bundles (build/static/css/)
Dependencies	TailwindCSS, SCSS, PostCSS, Framer Motion
Integrity	Validated via Stylelint + Prettier in CI; color and contrast audits in GitHub Actions


⸻

🔗 Related Documentation
	•	Web Frontend Overview
	•	Web UI Architecture
	•	Design System Overview
	•	Accessibility Review Templates

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — developed with MCP design standards for
clarity, accessibility, and aesthetic consistency.

“Design is data made visible — and Kansas has stories to tell.”

