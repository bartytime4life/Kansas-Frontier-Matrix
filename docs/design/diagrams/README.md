<div align="center">

# 🧩 Kansas Frontier Matrix — Design Diagrams  
`docs/design/diagrams/`

**Purpose:** Contain architecture, workflow, and UI component diagrams for the  
Kansas Frontier Matrix (KFM) design system. These visual models describe how the system’s  
technical, spatial, and narrative layers interact from data ingestion to user interface.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../..)  
[![Architecture](https://img.shields.io/badge/Diagrams-Mermaid-blue)](https://mermaid-js.github.io/mermaid/#/)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains **Mermaid and visual diagrams** illustrating how  
the Kansas Frontier Matrix integrates its various components — ETL pipelines,  
AI/ML enrichment, knowledge graph architecture, and the React + MapLibre web interface.

All diagrams are written in Markdown-friendly **Mermaid syntax** for GitHub rendering and  
are linked to documentation pages across the design and engineering directories.

---

## 🗂️ Directory Layout

```text
docs/design/diagrams/
├── README.md                     # This file
├── system_architecture.mmd        # High-level architecture diagram (ETL → Graph → UI)
├── ui_component_flow.mmd          # React + FastAPI data flow diagram
├── data_pipeline_overview.mmd     # Data ingestion and STAC validation process
├── timeline_map_sync.mmd          # Map & timeline synchronization flow
├── knowledge_graph_schema.mmd     # Neo4j node and relation model overview
└── exports/                       # Rendered PNG/SVG exports of diagrams
    ├── system_architecture.png
    ├── ui_component_flow.png
    └── knowledge_graph_schema.png


⸻

🧱 Diagram Standards

Type	File Extension	Description	Rendered Format
Mermaid	.mmd	Text-based, GitHub-rendered architecture diagrams	PNG, SVG (exported)
PlantUML (optional)	.puml	Complex entity relationships (used for graph schema)	SVG
Exports	.png .svg	Pre-rendered diagrams for use in docs and reports	Static image


⸻

📊 Core Diagrams

1️⃣ System Architecture (Mermaid)

Shows how data sources flow through the ETL pipeline into the Knowledge Graph,
and how results are exposed to the web UI.

flowchart TD
  A["Data Sources\n(USGS · NOAA · FEMA · KGS)"] --> B["ETL Pipeline\n(Python + Makefile)"]
  B --> C["Processed Layers\nGeoJSON · COG · CSV"]
  C --> D["STAC Catalog\n(Spatial + Temporal Index)"]
  D --> E["Knowledge Graph\nNeo4j · CIDOC CRM · OWL-Time"]
  E --> F["API Layer\nFastAPI · GraphQL"]
  F --> G["Web Frontend\nReact + MapLibreGL"]
  G --> H["Users\nResearchers · Educators · Public"]
  style A fill:#E6EFFF,stroke:#0074D9,stroke-width:2px
  style G fill:#E0FFE0,stroke:#2ECC40,stroke-width:2px
  style H fill:#FFF3C4,stroke:#FFB700,stroke-width:2px
<!-- END OF MERMAID -->


⸻

2️⃣ UI Component Flow (React + FastAPI)

Depicts the frontend data flow between major components:
Map, Timeline, Search, Panels, and API endpoints.

flowchart LR
  subgraph Frontend [Frontend (React + MapLibre)]
    A["SearchBar.tsx"]
    B["Timeline.tsx"]
    C["MapView.tsx"]
    D["DetailPanel.tsx"]
  end

  subgraph Backend [Backend (FastAPI + Neo4j)]
    E["/search API"]
    F["/events API"]
    G["/entity/{id} API"]
    H["Graph Database\n(Neo4j Knowledge Graph)"]
  end

  A --> E
  B --> F
  C --> F
  D --> G
  E --> H
  F --> H
  G --> H
  H --> D
  D --> C
  C --> B

  style Frontend fill:#f9f9f9,stroke:#888
  style Backend fill:#e8f0fe,stroke:#0074D9
<!-- END OF MERMAID -->


⸻

3️⃣ Knowledge Graph Schema (Conceptual Model)

Outlines the key entity classes (People, Places, Events, Documents) and relationships
within the KFM Knowledge Graph (CIDOC CRM + STAC-compatible).

erDiagram
  PERSON ||--o{ EVENT : "participated_in"
  PLACE  ||--o{ EVENT : "occurred_at"
  DOCUMENT ||--o{ EVENT : "mentions"
  EVENT {
    string id
    date start_date
    date end_date
    string type
  }
  PERSON {
    string name
    string role
  }
  PLACE {
    string name
    float latitude
    float longitude
  }
  DOCUMENT {
    string title
    string source
  }
<!-- END OF MERMAID -->


⸻

🧮 Validation & Automation

All diagrams are validated and exported through GitHub Actions as part of CI:
	•	.mmd → .png and .svg via Mermaid CLI
	•	Linting ensures valid Mermaid syntax before commit
	•	Checksums (.sha256) are generated for export integrity

Manual Export Example:

npx @mermaid-js/mermaid-cli -i system_architecture.mmd -o exports/system_architecture.png


⸻

♿ Accessibility & Design Standards
	•	All diagrams include text-based equivalents (Mermaid code is directly viewable).
	•	Colors meet WCAG 2.1 AA contrast guidelines.
	•	Logical reading order verified for screen readers (via alt text metadata).
	•	All image exports include accessible filenames and alt text entries in metadata JSON.

⸻

🧾 Provenance & Integrity
	•	Generated From: Core architecture files (Kansas Frontier Matrix Architecture.pdf)
	•	Created Using: Mermaid.js and Figma diagram exports
	•	Validated By: GitHub Actions CI (diagram-validate.yml)
	•	Checksum Tracking: Stored alongside .png and .svg files
	•	License: CC-BY-4.0 (Creative Commons Attribution 4.0 International)
	•	MCP Workflow: Documented → Visualized → Validated → Published

⸻

📚 Related References
	•	Kansas Frontier Matrix Architecture (System Overview)
	•	Kansas Frontier Matrix Web UI Architecture
	•	Panels Wireframes
	•	Map Wireframes
	•	Typography Wireframes

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Architecture
Spatial · Temporal · Narrative Integration

</div>
```
