<div align="center">

# 🧭 Kansas Frontier Matrix — Navigation Assets  
`docs/design/mockups/figma/components/navigation/assets/`

**Icons · Thumbnails · Overlays · Brand UI Elements**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Navigation%20Assets-purple)](../figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 🎯 Purpose

This directory stores **visual assets** supporting the Navigation Component wireframes and UI design — including icons, thumbnails, map overlays, and color references.  
All assets are exported from Figma and optimized for web (SVG/PNG) to ensure pixel clarity, accessibility, and reproducibility.

These assets define the **visual identity** for:
- Map and timeline toolbars  
- Layer toggles, legends, and icons  
- Detail panel indicators  
- Search and filter affordances  

Each file includes metadata and checksum verification for version traceability under MCP documentation standards.

---

## 📁 Directory Layout

```text
docs/design/mockups/figma/components/navigation/assets/
├── README.md               # This specification
├── icons/                  # SVG/PNG interface icons (e.g., search, zoom, layer)
│   ├── icon-search.svg
│   ├── icon-layer.svg
│   ├── icon-zoom-in.svg
│   └── icon-zoom-out.svg
├── thumbnails/             # Preview snapshots for UI states
│   ├── timeline-thumb.png
│   └── map-thumb.png
├── overlays/               # Semi-transparent visual overlays (e.g. focus masks)
│   ├── timeline-overlay.png
│   └── map-overlay.jpg
└── color-palette.json      # Design tokens and hex references

Each directory corresponds to a category of reusable assets within the Kansas Frontier Matrix design system.

⸻

🎨 Design Tokens

Token	Example	Usage
--kfm-accent	#4F9CF9	Primary accent (links, highlights)
--kfm-bg-dark	#0b1020	Map and dark UI backgrounds
--kfm-bg-light	#f7f9fb	Light mode panels
--kfm-border	#d1d5db	Divider lines and UI borders
--kfm-radius	8px	Button and panel corner rounding
--kfm-shadow	rgba(0,0,0,0.2)	Subtle elevation for panels

These color and shape constants are synchronized with the global design token registry (web/src/styles/tokens.css).

⸻

🧩 Asset Integration Flow

flowchart LR
  A["Figma Export (SVG/PNG)"] --> B["Optimization\nSVGO · TinyPNG"]
  B --> C["Asset Folder\n/icons · /thumbnails · /overlays"]
  C --> D["Web Integration\nReact + MapLibre UI"]
  D --> E["STAC UI Reference\n(layer-icons.json)"]

<!-- END OF MERMAID -->


This ensures a traceable, reproducible design chain from Figma → optimized export → asset repository → live web implementation.

⸻

🧠 Design Guidelines

Category	Principle	Implementation
Iconography	Flat, geometric, legible at 16–32 px	Optimized SVGs with stroke-width="2"
Contrast	4.5:1 minimum for text and icons	Verified with WCAG contrast checker
Consistency	Shared stroke and corner radius	Derived from design tokens
Scalability	Vector-based	No embedded raster unless for texture overlays
Localization	No text baked into images	Use aria-label for semantic equivalents


⸻

🔍 Provenance & Integrity

Asset	Type	Figma Node	Exported	SHA256
icon-search.svg	Icon	figma://node/23:81	2025-09-28	sha256-f9c2…
timeline-thumb.png	Thumbnail	figma://node/24:11	2025-09-28	sha256-a29b…
color-palette.json	Palette	figma://node/25:63	2025-09-28	sha256-7cde…

Each asset’s checksum is listed in checksums.txt for MCP reproducibility and CI validation.

⸻

🧾 Related Documents
	•	Navigation Wireframes
	•	Navigation Components Overview
	•	Web UI Architecture
	•	Design Tokens & Style Guide

⸻

📜 License & Credits

All design assets © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Designed and maintained by the KFM Design & Interaction Team in alignment with MCP reproducibility and accessibility standards.

