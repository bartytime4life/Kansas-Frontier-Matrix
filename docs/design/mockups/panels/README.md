<div align="center">

# 🪶 Kansas Frontier Matrix — Panels & Detail Views  
`docs/design/mockups/panels/`

**Contextual · Interactive · Knowledge-Linked**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../docs/design/)
[![Figma Source](https://img.shields.io/badge/Figma-Panel%20System-purple)](./figma-refs.json)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 🎯 Purpose

The **Panel System** provides the Kansas Frontier Matrix (KFM) interface with its **contextual detail views** — dynamic panels that display rich metadata, document excerpts, and AI-generated summaries.  
Panels are the **information bridge** between the map/timeline views and the knowledge graph, surfacing relationships (People ↔ Places ↔ Events ↔ Documents) interactively.

These panels enable users to:
- Explore entity and event details (via `/entity/{id}`)
- Read document excerpts with provenance links  
- View cross-references, sources, and AI summaries  
- Interact with embedded media (images, scanned maps, treaties)  
- Access quick filters or drill-down queries within the same context  

---

## 🧩 Panel Architecture

```mermaid
flowchart LR
  A["User Action\n(click on map/timeline)"] --> B["API Query\n/entity/{id}"]
  B --> C["Panel Renderer\n(React Component)"]
  C --> D["Knowledge Graph Data\n(Neo4j via FastAPI)"]
  C --> E["AI Summary Service\n(BART/T5 Model)"]
  C --> F["STAC Links\nPreviewable Media"]

<!-- END OF MERMAID -->


Panels pull structured information from the knowledge graph, AI layer, and STAC catalog, merging it into a single, interactive display.
Each panel is context-sensitive — e.g., event panels show timelines, place panels show maps, and document panels show transcripts or images.

⸻

📁 Directory Layout

docs/design/mockups/panels/
├── README.md                  # This documentation
├── wireframes/                # Figma exports for panel layouts
│   ├── entity-panel.png
│   ├── document-panel.svg
│   ├── place-panel.png
│   └── timeline-context.svg
├── thumbnails/                # Preview snapshots for GitHub
│   ├── panel-thumb.png
│   └── document-thumb.png
└── figma-refs.json            # Figma node metadata and export hashes

Each wireframe is linked to its design origin in figma-refs.json for reproducibility and auditability.

⸻

🧭 Panel Types

Type	Description	Data Source
Entity Panel	Displays attributes and relationships for people, organizations, or tribes	Neo4j node data (Person, Organization)
Event Panel	Shows event metadata, participants, and time span	Event nodes and relations (OCCURRED_AT, INVOLVED)
Place Panel	Combines map previews, coordinates, and historical boundaries	GeoJSON from STAC + place metadata
Document Panel	Provides text excerpts, scanned pages, and source links	OCR + NLP summaries + document URLs
AI Summary Panel	Condensed insight combining multiple sources	NLP outputs from /ask endpoint

Each panel shares a consistent structure for clarity and user familiarity.

⸻

🎨 Design Tokens

Token	Example	Purpose
--kfm-panel-bg	#ffffff / #0b1020	Light/dark background
--kfm-border-color	#d1d5db	Divider lines
--kfm-accent	#4F9CF9	Link and highlight color
--kfm-shadow	rgba(0,0,0,0.15)	Drop shadow for panel elevation
--kfm-radius	1rem	Rounded corners for panels

All design tokens are synchronized with the global KFM style definitions (web/src/styles/tokens.css).

⸻

🧠 Interaction Flow

sequenceDiagram
  participant User
  participant Map
  participant Timeline
  participant Panel
  participant API
  User->>Map: Click on feature
  Map->>API: GET /entity/{id}
  API-->>Panel: JSON (entity, relationships, citations)
  Panel-->>User: Display metadata, linked items, AI summary
  User->>Panel: Click linked entity
  Panel->>API: Fetch linked entity details

<!-- END OF MERMAID -->


Panels allow recursive exploration of the knowledge graph — users can navigate through linked entities without leaving context.

⸻

🧾 Provenance & Integrity

Asset	Figma Node	Exported	SHA256
entity-panel.png	figma://node/50:10	2025-09-30	sha256-a4b2…
document-panel.svg	figma://node/50:12	2025-09-30	sha256-d8f3…
timeline-context.svg	figma://node/50:15	2025-09-30	sha256-19ef…

Checksums are validated during CI to ensure design integrity under MCP standards.

⸻

📚 Related Documents
	•	Map Interface
	•	Navigation Components
	•	AI Assistant Design
	•	Web UI Architecture
	•	System Architecture

⸻

📜 License & Credits

Panel and detail view designs © 2025 Kansas Frontier Matrix Project.
Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
Designed by the KFM Design & Interaction Team under Master Coder Protocol documentation-first methodology for reproducibility and accessibility.

