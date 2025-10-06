<div align="center">

# 🗂️ Kansas Frontier Matrix — Archive Interface Thumbnails  
`docs/design/mockups/archive/thumbnails/`

**Preview Images · Dataset Cards · Archive Browser Grid**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Archive%20Thumbnails-purple)](../../figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🎯 Purpose

This folder contains **thumbnail images** used to visually preview the Kansas Frontier Matrix **Archive Interface**.  
Thumbnails represent snapshots of dataset cards, grid layouts, and metadata previews from the archive browser wireframes.  

They provide:
- Quick visual references for documentation and architecture diagrams  
- Standardized small-format previews for UI documentation  
- Visual consistency across GitHub and published docs  

These files are **non-functional assets** for design documentation and not used in the live application.

---

## 📁 Directory Layout

```text
docs/design/mockups/archive/thumbnails/
├── README.md                     # This file
├── archive-grid-thumb.png        # Overview of dataset grid layout
├── dataset-preview-thumb.png     # Example of dataset metadata card
└── checksums.txt                 # SHA256 integrity log

Each image is derived from its respective Figma frame and versioned using a checksum for MCP reproducibility.

⸻

🧩 Integration Diagram

flowchart LR
  A["Figma Wireframes\n(Archive Browser)"] --> B["Export PNG (2× scale)"]
  B --> C["Optimize\nTinyPNG / OptiPNG"]
  C --> D["/thumbnails/"]
  D --> E["Documentation\n(README.md, design overviews)"]

<!-- END OF MERMAID -->


This process ensures all thumbnail assets are traceable, optimized, and compliant with the KFM documentation workflow.

⸻

🎨 Design Guidelines

Category	Requirement	Implementation
Resolution	2× standard UI scale	Max width: 1600px
Format	PNG preferred for clarity	Transparent background where possible
Compression	TinyPNG or OptiPNG optimization	< 400KB each
Accessibility	Include descriptive alt text in docs	Example: “Archive grid showing datasets by period”
Consistency	Use uniform aspect ratio and padding	16:9 layout with 32px internal margin


⸻

🧠 Example Usage in Documentation

![Archive Grid Overview](archive-grid-thumb.png "Archive browser showing dataset cards by theme and date")

These thumbnails are embedded in documentation (like archive/README.md) for visual clarity and quick navigation.

⸻

🔍 Provenance & Integrity

Thumbnail	Figma Node	Export Date	SHA256
archive-grid-thumb.png	figma://node/42:15	2025-09-29	sha256-bf19…
dataset-preview-thumb.png	figma://node/42:19	2025-09-29	sha256-ef3a…

Checksums are verified during CI/CD builds using automated integrity validation scripts per MCP reproducibility standards.

⸻

📚 Related Documents
	•	Archive Interface
	•	Archive Wireframes
	•	Web UI Architecture
	•	System Architecture

⸻

📜 License & Credits

Archive thumbnails © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Created and maintained by the KFM Design & Interaction Team, following Master Coder Protocol principles for documentation-first and reproducible design workflows.

