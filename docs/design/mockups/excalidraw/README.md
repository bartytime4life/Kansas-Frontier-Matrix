<div align="center">

# ✏️ Kansas Frontier Matrix — Excalidraw Mockups  
`docs/design/mockups/excalidraw/`

**Rapid Sketches · Interaction Maps · Concept Flows**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../docs/design/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

This directory stores **Excalidraw-based conceptual mockups** for Kansas Frontier Matrix (KFM) components.  
These sketches visualize early **UX flows, data interactions, and layout explorations** before high-fidelity Figma design.  

Excalidraw diagrams are lightweight, version-controlled `.excalidraw.json` files that integrate seamlessly into GitHub and can be exported to PNG/SVG for documentation.

These files support the MCP principle of **document-before-code**, providing an auditable design history of system evolution.

---

## 📁 Directory Layout

```text
docs/design/mockups/excalidraw/
├── README.md                     # This documentation file
├── exports/                      # Rendered exports for GitHub preview
│   ├── kfm-system-overview.png
│   ├── ui-flow.svg
│   └── ai-assistant-context.png
├── sketches/                     # Raw editable .excalidraw.json files
│   ├── kfm-system-overview.excalidraw.json
│   ├── ui-flow.excalidraw.json
│   └── ai-assistant-context.excalidraw.json
└── checksums.txt                 # File integrity and export validation

Each .excalidraw.json file includes metadata for shapes, positions, and layers,
making them portable and diffable in version control.

⸻

🧩 System Integration Overview

flowchart TD
  A["Excalidraw Sketches\n(.json)"] --> B["Exports\n(PNG/SVG for docs)"]
  B --> C["docs/design/\nMarkdown embedding"]
  C --> D["Architecture & UI Design\n(Figma refinement)"]
  D --> E["Implementation\n(React + MapLibre components)"]

<!-- END OF MERMAID -->


Excalidraw serves as the ideation sandbox in the design-to-development pipeline —
bridging conceptual models and production-ready Figma components.

⸻

🧠 Design Use Cases

Category	Description	Example File
System Flow	Visualizes backend–frontend interactions and ETL stages	kfm-system-overview.excalidraw.json
UI Flow	Drafts transitions between major screens (Map ↔ Timeline ↔ Archive)	ui-flow.excalidraw.json
AI Assistant Context	Shows data retrieval + conversation grounding logic	ai-assistant-context.excalidraw.json
Architecture Diagram	Depicts high-level KFM layers (ETL → STAC → Graph → API → UI)	architecture.excalidraw.json


⸻

🎨 Export Guidelines

Format	Purpose	Export Settings
.png	Static previews for READMEs and GitHub	2× scale, white background
.svg	Scalable, embedded in docs or slides	Transparent background, no fonts embedded
.excalidraw.json	Source of truth; editable design file	JSON version 2, saved with namespaced elements

Export Workflow:
	1.	Open sketch in Excalidraw.
	2.	Export to .png or .svg → save to /exports/.
	3.	Run checksum verification (sha256sum exports/* > checksums.txt).
	4.	Commit both versions for reproducibility.

⸻

🧮 Provenance & Integrity

File	Type	Last Modified	SHA256
kfm-system-overview.excalidraw.json	Source	2025-09-30	sha256-9ac3…
ui-flow.excalidraw.json	Source	2025-09-30	sha256-1fbd…
ai-assistant-context.excalidraw.json	Source	2025-09-30	sha256-47dd…
kfm-system-overview.png	Export	2025-09-30	sha256-2ac9…

CI validation scripts ensure that exports correspond exactly to the .excalidraw.json source files (no untracked edits).

⸻

🧾 Related Documents
	•	Navigation Components
	•	AI Assistant Design
	•	Web UI Architecture
	•	System Architecture
	•	Markdown Standard Kit

⸻

📜 License & Credits

All Excalidraw sketches © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Created by the KFM Design & Interaction Team as part of the Master Coder Protocol’s documentation-first workflow.
Design files maintained in raw JSON for transparency, auditability, and open collaboration.

