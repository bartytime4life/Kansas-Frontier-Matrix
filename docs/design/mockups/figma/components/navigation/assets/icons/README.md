<div align="center">

# 🧭 Kansas Frontier Matrix — Navigation Icons  
`docs/design/mockups/figma/components/navigation/assets/icons/`

**Consistent · Vector · Accessible UI Symbols**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Navigation%20Icons-purple)](../../figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🎯 Purpose

This directory contains all **navigation-related icons** used across the Kansas Frontier Matrix interface — optimized SVG/PNG exports from Figma.  
Icons provide a unified visual language for controls like search, zoom, layers, filters, and timeline actions.

The icons follow the project’s **design system** principles: minimalistic geometry, accessible contrast, and scalability for any device.

---

## 📁 Directory Layout

```text
docs/design/mockups/figma/components/navigation/assets/icons/
├── README.md                # This documentation file
├── icon-search.svg          # Search field magnifier icon
├── icon-layer.svg           # Map layer toggle
├── icon-zoom-in.svg         # Zoom in button
├── icon-zoom-out.svg        # Zoom out button
├── icon-timeline-play.svg   # Timeline play/pause toggle
├── icon-info.svg            # Info/help panel trigger
└── checksums.txt            # SHA256 integrity verification

All SVGs are exported from Figma, cleaned via SVGO, and stored as plain XML (no embedded styles).
Each icon includes an accessible title and aria-label attribute suggestion for assistive technologies.

⸻

🧩 Integration Diagram

flowchart LR
  A["Figma Design Icons"] --> B["Export SVG"]
  B --> C["Optimize\nSVGO • TinyPNG"]
  C --> D["/assets/icons"]
  D --> E["Web UI (React)\nimport { ReactComponent as IconSearch }"]
  E --> F["Documentation (Markdown)\nlinked via <img> or inline SVG"]

<!-- END OF MERMAID -->


Icons are reusable across:
	•	Map Toolbar (zoom, layer toggles, location reset)
	•	Timeline Controls (play/pause, range reset)
	•	Global Header (search, info, language switch)

⸻

🧠 Design Principles

Principle	Description	Implementation
Simplicity	Icons are geometric and minimalist	Stroke-width 2px, uniform grid (24×24)
Scalability	Vector format adapts to all displays	SVG viewBox "0 0 24 24"
Contrast	Minimum contrast ratio 4.5:1	Uses design token --kfm-accent
Consistency	Shared alignment and proportions	Derived from KFM grid + corner radius system
Accessibility	Semantic labeling via ARIA	aria-label="Search" or <title>Search</title>


⸻

🎨 Design Tokens

Token	Example	Usage
--kfm-icon-color	#4F9CF9	Default icon stroke
--kfm-icon-hover	#72B7FF	Hover/focus state
--kfm-icon-disabled	#8a8a8a	Inactive state
--kfm-bg-dark	#0b1020	Background (dark mode)
--kfm-bg-light	#ffffff	Background (light mode)

The color-palette.json in /assets/ defines these tokens globally.

⸻

🔍 Provenance & Integrity

Icon	Type	Figma Node	Export Date	SHA256
icon-search.svg	SVG	figma://node/35:22	2025-09-30	sha256-23cd…
icon-layer.svg	SVG	figma://node/35:28	2025-09-30	sha256-18a1…
icon-zoom-in.svg	SVG	figma://node/35:31	2025-09-30	sha256-7a9e…
icon-timeline-play.svg	SVG	figma://node/35:33	2025-09-30	sha256-9dd2…

All exported assets are logged in checksums.txt for MCP traceability.
CI pipelines validate these SHA256 hashes to prevent drift between design and implementation.

⸻

🧾 Related Documents
	•	Navigation Assets
	•	Navigation Wireframes
	•	Web UI Architecture
	•	System Architecture

⸻

📜 License & Credits

Icons © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Exported and maintained by the KFM Design & Interaction Team for use across the web UI and documentation under MCP reproducibility and accessibility standards.

