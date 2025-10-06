<div align="center">

# 🧭 Kansas Frontier Matrix — Navigation Thumbnails  
`docs/design/mockups/figma/components/navigation/assets/thumbnails/`

**Visual Previews · Timeline · Map · Detail Panel**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Navigation%20Thumbnails-purple)](../../figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🎯 Purpose

This folder contains **thumbnail images** representing key UI states and layout previews for the Kansas Frontier Matrix **Navigation System**.  
Thumbnails are small static visuals derived from the main Figma frames used in documentation, design reviews, and as references in architecture and component READMEs.

These are **not** interactive prototypes but **design snapshots** showing:
- Timeline scrubber and time selection interface  
- Map toolbar layout (zoom, layer, search)  
- Detail panel preview (entity/event view)  

Each image follows the MCP reproducibility chain — versioned, referenced, and verified by checksum.

---

## 📁 Directory Layout

```text
docs/design/mockups/figma/components/navigation/assets/thumbnails/
├── README.md               # This specification
├── timeline-thumb.png      # Timeline view preview
├── map-thumb.png           # Map view preview
├── detail-thumb.png        # Detail panel preview
└── checksums.txt           # SHA256 checksums for integrity verification

All images are exported from Figma at 2× resolution for clarity and web-readiness (max width 1600 px).

⸻

🧩 Integration Map

flowchart LR
  A["Figma Frame Export"] --> B["Thumbnail Optimization\n(TinyPNG/OptiPNG)"]
  B --> C["/assets/thumbnails"]
  C --> D["Documentation\n(README, Architecture Diagrams)"]
  D --> E["Web UI Reference\n(tooltips, preview cards)"]

<!-- END OF MERMAID -->


Thumbnails are reused across documentation and UI to maintain visual consistency between design references and production components.

⸻

🧠 Design Guidelines

Category	Principle	Implementation
Clarity	Use high-contrast backgrounds and legible annotations	White or dark neutral background with 4.5:1 contrast
Scale	Maintain consistent aspect ratio across views	16:9 ratio; width ≤ 1600 px
Context	Represent UI in realistic composition	Include representative controls and layers
Compression	Optimize without visible artifacting	≤ 400 KB PNG (TinyPNG pass)
Accessibility	Alt-text and descriptive captions in docs	Example: “Timeline with active range 1850–1870 selected”


⸻

🧾 Provenance & Integrity

Thumbnail	Figma Node	Exported	SHA256
timeline-thumb.png	figma://node/28:40	2025-09-30	sha256-18b3…
map-thumb.png	figma://node/28:42	2025-09-30	sha256-27ac…
detail-thumb.png	figma://node/28:44	2025-09-30	sha256-9fd1…

These hashes are also listed in checksums.txt and validated in CI workflows to ensure design fidelity and traceability per MCP standards.

⸻

🧾 Related Documents
	•	Navigation Assets
	•	Navigation Wireframes
	•	Web UI Architecture
	•	System Architecture

⸻

📜 License & Credits

Design assets © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Exports prepared by the KFM Design & Interaction Team, following MCP documentation-first reproducibility standards.

