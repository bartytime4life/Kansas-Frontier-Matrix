<div align="center">

# 🗂️ Kansas Frontier Matrix — Archive Interface Wireframes  
`docs/design/mockups/archive/wireframes/`

**Browse · Discover · Filter Historical Datasets**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Archive%20Wireframes-purple)](../figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🎯 Purpose

This directory contains **Figma-exported wireframes** for the Kansas Frontier Matrix **Archive Interface** — the digital library and data discovery view of the KFM platform.  
Wireframes visualize how users browse, search, and preview datasets drawn from the system’s **STAC catalog**, enabling transparent and reproducible exploration of Kansas’s historical geospatial resources.

The Archive Interface supports:
- Browsing by **category**, **era**, or **geographic extent**
- Accessing dataset **metadata** (source, license, spatial/temporal coverage)
- Previewing data thumbnails and summary panels
- Launching datasets into the **Map + Timeline** interface
- Viewing **provenance**, **checksums**, and **version history** per dataset

---

## 📁 Directory Layout

```text
docs/design/mockups/archive/wireframes/
├── README.md                    # This file
├── archive-browser.png           # Dataset grid and filter view
├── dataset-detail.svg            # Expanded dataset metadata view
├── filter-panel.png              # Filter sidebar UI
├── search-results.svg            # Example of keyword-based search
└── figma-refs.json               # Figma node metadata for design reproducibility

Each wireframe corresponds to a Figma component node (referenced in figma-refs.json) and documents a functional portion of the archive workflow.

⸻

🧩 User Flow

sequenceDiagram
  participant User
  participant Archive
  participant API
  participant STAC
  participant Map
  User->>Archive: Browse datasets by category or search term
  Archive->>API: GET /datasets?query=water&type=raster
  API->>STAC: Retrieve STAC Items (metadata + URLs)
  STAC-->>API: JSON collection of datasets
  API-->>Archive: Render dataset cards and filters
  User->>Archive: Click dataset card
  Archive->>Map: Open in interactive viewer (via STAC asset link)

<!-- END OF MERMAID -->


This sequence illustrates the flow from user search → STAC metadata retrieval → visualization handoff.

⸻

🧠 Wireframe Details

File	View	Description
archive-browser.png	Dataset Grid	Displays dataset cards with thumbnail, type, and date range
dataset-detail.svg	Detail Panel	Shows dataset metadata, source URL, and provenance info
filter-panel.png	Filters	Sidebar with filters by format, period, and data domain
search-results.svg	Search View	Result layout for keyword and entity-based searches

All designs adhere to accessibility-first principles and responsive layouts for desktop and tablet use.

⸻

🎨 Design Tokens

Token	Example	Purpose
--kfm-archive-bg	#ffffff / #0b1020	Background color (light/dark modes)
--kfm-card-shadow	rgba(0,0,0,0.1)	Card shadow for dataset previews
--kfm-border	#e5e7eb	Divider and panel borders
--kfm-highlight	#4F9CF9	Accent for hover states and highlights
--kfm-radius	0.75rem	Rounded corners for cards and panels

These values align with the global design tokens defined in web/src/styles/tokens.css.

⸻

🧾 Provenance & Integrity

Asset	Figma Node	Exported	SHA256
archive-browser.png	figma://node/42:15	2025-09-29	sha256-4e91…
dataset-detail.svg	figma://node/42:19	2025-09-29	sha256-83af…
filter-panel.png	figma://node/42:21	2025-09-29	sha256-c7a4…
search-results.svg	figma://node/42:23	2025-09-29	sha256-f5c9…

Checksums are tracked for MCP reproducibility, ensuring all exported assets match documented Figma versions.

⸻

📚 Related Documents
	•	Archive Interface
	•	Archive Thumbnails
	•	Web UI Architecture
	•	System Architecture
	•	Data Format Standards

⸻

📜 License & Credits

Archive wireframes © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Designed and documented by the KFM Design & Interaction Team, following Master Coder Protocol reproducibility and open-science standards for transparent UX development.

