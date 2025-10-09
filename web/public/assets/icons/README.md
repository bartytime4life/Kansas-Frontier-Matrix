<div align="center">

# 🧭 Kansas Frontier Matrix — Public Icons  
`web/public/assets/icons/`

**Vector Icons · UI Symbols · Thematic Graphics**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-blue)](../../../../docs/design/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/public/assets/icons/` directory contains the **vector-based icons**  
used across the Kansas Frontier Matrix web interface — in the navigation,  
map controls, timeline, modals, and AI assistant.

Icons are standardized under the **Kansas Frontier Matrix Design System**  
and exported directly from Figma or Illustrator in **SVG format**.  
Each icon is **accessible, theme-aware**, and designed to maintain  
clarity across light and dark modes.

---

## 🧱 Directory Structure

```text
web/public/assets/icons/
├── ai-bot.svg            # AI Assistant symbol
├── map-marker.svg        # Map location pin icon
├── timeline.svg          # Timeline and temporal UI icon
├── filter.svg            # Filter/Layer control icon
├── info.svg              # Information modal icon
├── settings.svg          # Settings and configuration icon
├── search.svg            # Header search magnifier
├── keyboard.svg          # Keyboard shortcuts help icon
├── contrast.svg          # Accessibility/contrast toggle
└── README.md             # This documentation file


⸻

🎨 Design Specifications

Attribute	Specification
Canvas Size	24 × 24 px (consistent viewBox for UI integration)
Stroke Width	1.5 px (scales cleanly with font size)
Fill	none (stroke-based, inherits CSS color)
Color Tokens	var(--kfm-color-accent) / var(--kfm-color-text)
Export Format	SVG, optimized via SVGO multipass
Usage Context	React <img> or <svg> inline rendering

Each SVG uses CSS variables for stroke/fill color to support
automatic adaptation to the current theme (light/dark).

Example:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke="var(--kfm-color-accent)" fill="none" stroke-width="1.5">
  <circle cx="12" cy="12" r="9" />
</svg>


⸻

🧩 Icon Usage by Component

Icon	Used In	Purpose
ai-bot.svg	AIAssistant	Visual marker for AI interaction
map-marker.svg	MapView	Location or site indicators
timeline.svg	TimelineView	Temporal navigation controls
filter.svg	LayerControls / Sidebar	Toggles filters and overlays
info.svg	Modals / DetailPanel	Opens context help or metadata
settings.svg	Header / SettingsModal	Application preferences
search.svg	Header	Search bar magnifier icon
keyboard.svg	AccessibilityModal / HelpModal	Keyboard shortcut reference
contrast.svg	ThemeToggle	Theme or color contrast switch


⸻

🧠 Design and Development Workflow
	1.	Design – Icons are created or refined in Figma under
docs/design/mockups/icons/ using the shared KFM design grid.
	2.	Export – Exported as SVG using Export > SVG (Outline Text).
	3.	Optimize – Run through svgo --multipass in the CI build pipeline.
	4.	Accessibility Review – Each icon tested for legibility and color contrast.
	5.	Integration – Imported into web components (via inline SVG or <img src>).
	6.	Validation – CI checks file integrity (no embedded raster data, correct viewBox).

⸻

♿ Accessibility Guidelines
	•	All icons used for decoration must include role="presentation"
or empty alt="" attributes when rendered as <img>.
	•	Informative icons must include aria-label or title attributes.
	•	Minimum visible size: 16×16 px for UI buttons; 20×20 px recommended for clarity.
	•	Contrast ratio must meet or exceed 4.5:1 between foreground and background.
	•	Icons scale responsively with CSS em units for accessibility zoom support.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	Figma/Illustrator vector exports, design tokens
Outputs	Optimized SVG icons, versioned with checksums
Dependencies	SVGO, TailwindCSS, Framer Motion (for motion icons)
Integrity	Validated in CI: SVG lint, accessibility contrast test, and checksum generation

All icons include embedded metadata comments in their SVG headers, referencing source and license.

⸻

🔗 Related Documentation
	•	Public Assets Overview
	•	Design Mockups — Icons
	•	Accessibility Guidelines
	•	Web UI Architecture

⸻

📜 License

All icons designed by the Kansas Frontier Matrix Team are licensed under MIT,
with third-party derivative icons attributed under CC-BY 4.0 or compatible licenses.

© 2025 Kansas Frontier Matrix — Developed under the Master Coder Protocol (MCP)
for open design, transparency, and cross-platform accessibility.

“Icons are the symbols of discovery — they guide every click across Kansas’s digital frontier.”

