<div align="center">

# 🧭 Kansas Frontier Matrix — Navigation Overlays  
`docs/design/mockups/figma/components/navigation/assets/overlays/`

**UI Mask Layers · Interactive Highlights · Focus Overlays**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Navigation%20Overlays-purple)](../../figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🎯 Purpose

This folder contains **overlay assets** for the Kansas Frontier Matrix Navigation Components.  
These are semi-transparent visual masks, guides, and focus overlays used in mockups, demos, and accessibility visualization.  

Overlays illustrate user interactions and temporal focus regions (e.g., when scrubbing the timeline, zooming on the map, or selecting entities).  
They support both **design communication** (in documentation) and **runtime effects** (in web UI hover states).

---

## 📁 Directory Layout

```text
docs/design/mockups/figma/components/navigation/assets/overlays/
├── README.md               # This specification
├── timeline-overlay.png    # Semi-transparent overlay for timeline focus
├── map-overlay.jpg         # Map dimming/focus overlay
└── checksums.txt           # SHA256 integrity log

All files are optimized raster images (PNG/JPG) exported from Figma at 2× resolution and reduced in size using TinyPNG or ImageOptim.

⸻

🧩 Overlay Integration Diagram

flowchart LR
  A["Figma Export (mask layers)"] --> B["Optimization\nTinyPNG/ImageOptim"]
  B --> C["/assets/overlays"]
  C --> D["Documentation\n(mockup visuals, user flow diagrams)"]
  C --> E["Web UI\nReact Components (focus state overlays)"]

<!-- END OF MERMAID -->


These overlays serve dual purposes:
	1.	As documentation aids in design and architecture markdowns.
	2.	As visual focus layers in web UI (for hover/selection effects on timeline and map panels).

⸻

🎨 Design & Accessibility

Category	Principle	Implementation
Opacity	Provide subtle emphasis without obscuring underlying content	Use opacity: 0.35–0.45
Color	Match KFM theme tokens (--kfm-accent and --kfm-bg-dark)	Overlay color: rgba(79,156,249,0.4)
Contrast	Maintain 4.5:1 contrast for text and icon overlays	Verified with WCAG contrast tools
Responsiveness	Scale proportionally with viewport	Implemented with object-fit: cover in UI
Animation	Fade in/out within 200–300ms for accessibility	CSS transition: opacity 0.25s ease-in-out


⸻

🧠 Use Cases

Overlay	Context	Purpose
timeline-overlay.png	Timeline focus and scrub regions	Shows selected time interval on hover/drag
map-overlay.jpg	Map hover or inactive background mask	Dims inactive map regions to guide attention

Overlays can be used directly in documentation or imported into React components as static assets for UI transitions.

⸻

🔍 Provenance & Integrity

Asset	Type	Figma Node	Export Date	SHA256
timeline-overlay.png	PNG	figma://node/32:12	2025-09-30	sha256-91df…
map-overlay.jpg	JPG	figma://node/32:14	2025-09-30	sha256-6abf…

These hashes are listed in checksums.txt and validated in CI to ensure no drift between design exports and repo copies.

⸻

🧾 Related Documents
	•	Navigation Assets
	•	Navigation Thumbnails
	•	Navigation Wireframes
	•	Web UI Architecture
	•	System Architecture

⸻

📜 License & Credits

Design overlays © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Prepared by the KFM Design & Interaction Team for documentation and UI implementation under MCP reproducibility standards.

