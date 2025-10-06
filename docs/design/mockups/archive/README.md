<div align="center">

# 🗂️ Kansas Frontier Matrix — Archive Interface  
`docs/design/mockups/archive/`

**Browse · Filter · Discover Historical Datasets**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Archive%20Browser-purple)](./figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The **Archive Interface** is the Kansas Frontier Matrix’s visual gateway to its data backbone — the **STAC catalog and knowledge graph**.  
It allows users to **browse, filter, and preview** datasets, documents, and map layers that make up the project’s historical corpus.

This design defines how users:
- Explore datasets by **category, period, or location**
- Access dataset-level **metadata and provenance**
- Preview map/layer **thumbnails and STAC summaries**
- Filter by **file type (GeoTIFF, GeoJSON, CSV, Text)** or **time period**
- Link from archive items → **interactive map/timeline context**

The archive unifies *data transparency*, *provenance*, and *accessibility* — core principles of the **Master Coder Protocol (MCP)**.

---

## 🧩 Interface Overview

```mermaid
flowchart LR
  A["Archive Browser\n(dataset grid · filters)"] --> B["Dataset Details\nmetadata · preview · provenance"]
  A --> C["Search Bar\nkeyword + entity auto-complete"]
  B --> D["Open in Map/Timeline\nlink to interactive viewer"]
  B --> E["Download / API Access\nCOG · GeoJSON · CSV"]
  B --> F["Citations & Provenance\nsource links + checksums"]
  C --> G["Backend / STAC Catalog\n(data/stac/catalog.json)"]

<!-- END OF MERMAID -->


This interface acts as the “data discovery” layer between users and the underlying ETL + STAC system.
Each item in the Archive corresponds to a STAC Item or Collection, dynamically fetched from data/stac/catalog.json.

⸻

📁 Directory Structure

docs/design/mockups/archive/
├── README.md                 # This document
├── wireframes/               # UI blueprints from Figma
│   ├── archive-browser.png
│   ├── dataset-detail.svg
│   └── filter-panel.png
├── thumbnails/               # Visual samples (optimized PNG)
│   ├── archive-grid-thumb.png
│   └── dataset-preview-thumb.png
└── figma-refs.json           # Figma export metadata

Each wireframe and thumbnail corresponds to a Figma component node referenced in figma-refs.json with its unique ID and export hash.

⸻

🧭 User Flow

Step	Action	Result
1	Open Archive Browser	Loads a grid of datasets from STAC metadata
2	Use filters or search	Filters datasets by theme, period, file type
3	Click a dataset card	Opens detail view (title, abstract, bounding box)
4	Review provenance & license	Displays checksums, source URLs, version
5	Choose Open in Map	Loads the selected layer in MapLibre/Timeline
6	Choose Download	Directs to public file or API endpoint


⸻

🧠 Design Principles

Principle	Implementation
Transparency	Each dataset exposes source, license, and checksum (STAC + MCP fields).
Discoverability	Search and sort across dataset title, period, or keywords.
Semantic Context	Each STAC record links to graph entities (e.g., Places or Events).
Reproducibility	Every dataset view shows provenance, file version, and hash.
Accessibility	WCAG 2.1 AA color contrast, keyboard navigation, focus order.


⸻

📊 Example UI Components

Component	Function
Archive Grid	Displays dataset cards with STAC title, type, thumbnail, and period.
Filter Sidebar	Filters by Category, Time Range, File Type, or Confidence Level.
Search Bar	Autocomplete from STAC keywords and entity names.
Dataset Panel	Expands to show metadata (license, bounding box, source URLs).
Provenance Drawer	Lists checksums, source JSON, and ETL provenance chain.


⸻

🧩 Data Linkage

Each dataset in the Archive connects to the underlying knowledge graph and map layers:

flowchart TD
  A["STAC Item (dataset.json)"] --> B["Knowledge Graph Node\n(type: Dataset)"]
  B --> C["Linked Entities\nPlace · Event · Document"]
  B --> D["Web UI Components\nArchive Card · Map Layer"]

<!-- END OF MERMAID -->


This ensures that data discovery, semantic reasoning, and visualization remain synchronized.

⸻

🔍 Provenance & Integrity

File	Type	Source	Exported	SHA256
archive-browser.png	PNG	figma://node/40:17	2025-09-28	sha256-4f7b…
dataset-detail.svg	SVG	figma://node/40:19	2025-09-28	sha256-67cd…
filter-panel.png	PNG	figma://node/40:23	2025-09-28	sha256-89ae…

All hashes listed in checksums.txt (if present) are validated during CI to preserve design authenticity.

⸻

🧾 Related Documents
	•	Web UI Architecture
	•	System Architecture
	•	STAC Catalog Specification
	•	Design System Tokens
	•	AI Assistant Integration

⸻

📜 License & Credits

Design © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Created by the KFM Design & Interaction Team following MCP documentation-first and open science principles.

