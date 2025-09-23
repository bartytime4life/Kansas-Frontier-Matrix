# Kansas Geo Timeline — Core Package

This directory contains the **Python source code** for the  
**Kansas Geo Timeline / Kansas-Frontier-Matrix** stack.

The package provides:
- **Schema definitions** (`schemas/`) — JSON Schema contracts for STAC, map configs, and MCP docs [oai_citation:0‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB) [oai_citation:1‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468).
- **Templates** (`templates/`) — Jinja2 + HTML generators for STAC items, map configs, and narrative docs [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).
- **CLI utilities** (`kgt`) — lightweight commands to validate, render, and list datasets.
- **Helpers** — path resolution, schema loading, and JSON/YAML parsers.

---

## Philosophy

The stack integrates **history, cartography, and geology** into one reproducible pipeline [oai_citation:3‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468).  
Core principles:
- **Evidence-driven** — maps, documents, geology, and oral histories are ingested and linked with provenance [oai_citation:4‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN) [oai_citation:5‡Archaeology (MCP Domain Module).pdf](file-service://file-YEVu6bSFdnokatJ563EmVA).
- **Layered architecture** — raw data → schemas → templates → outputs → web app [oai_citation:6‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).
- **Time-aware** — every dataset is tied to a date/range for time-slider and historical reasoning [oai_citation:7‡Historical Dataset Integration for Kansas Frontier Matrix.pdf](file-service://file-EG371w17RJTzXWjXvqgsB6).
- **Uncertainty-ready** — placeholders for confidence and error margins are first-class fields [oai_citation:8‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN).
- **Open & modular** — components are containerized and reproducible from data to site [oai_citation:9‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).

---

## Repository Layout (src/)

src/kansas_geo_timeline/
├── init.py          # version resolver + lightweight helpers
├── cli.py               # entrypoint for kgt CLI
├── schemas/             # JSON Schema definitions
│   └── README.md
├── templates/           # Jinja2 & HTML templates
│   └── README.md
└── utils/               # optional helpers (json/yaml loaders, paths)

---

## System Flow (Mermaid)

> GitHub renders Mermaid inside triple-backtick code fences with `mermaid` as the language.

```mermaid
flowchart TD
  %% Inputs
  A[Data Descriptors\nYAML/JSON in data/] -->|validate| B[Schemas\nSTAC • Map • MCP]
  B -->|contract OK| C[Renderer\nJinja2 via `kgt` CLI]

  %% Template paths
  C --> T1[STAC Templates\nsrc/.../templates/stac/*.j2]
  C --> T2[Map Config Templates\nsrc/.../templates/map/*.j2]
  C --> T3[Doc Templates\nsrc/.../templates/docs/*.j2]
  C --> T4[UI Partials\nsrc/.../templates/ui/*.html.j2]

  %% Outputs
  T1 --> O1[stac/*.json]
  T2 --> O2[web/app.config.json]
  T3 --> O3[docs/generated/*.md]
  T4 --> O4[web/includes/*]

  %% Tests & Publish
  subgraph CI/CD
    V1[jsonschema/pytest] --> P[Build & Publish\nGitHub Actions]
  end
  O1 --> V1
  O2 --> V1
  O3 --> V1
  O4 --> V1

  P --> W[GitHub Pages + MapLibre App]
  W --> U[End Users\nMaps • Timeline • Story Maps]


⸻

CLI Examples

Validate STAC:

kgt validate stac/items/

Render MapLibre config:

kgt render map data/sources/*.yml -o web/app.config.json

Generate docs (MCP experiment/glossary pages):

kgt render docs data/*.yml -o docs/generated/


⸻

Design Notes
	•	Schemas follow STAC 1.0.0 and MCP experiment templates ￼ ￼.
	•	Templates standardize STAC, MapLibre, and MCP experiment/glossary outputs ￼.
	•	Docs integration: Experiments and story maps can embed diagrams, R snippets, and cartographic overlays ￼ ￼.
	•	UI: MapLibre + HTML5/CSS/Canvas snippets support responsive, accessible display ￼ ￼ ￼ ￼.
	•	Modeling hooks: Metadata aligns with NASA-grade modeling & uncertainty practices for future simulation modules ￼.
	•	Archaeology: Compatible with stratigraphy/context and artifact datasets & workflows ￼.
	•	Data gaps: Extensible to paleoclimate, oral histories, fire regimes, and hydrology modeling ￼ ￼ ￼.

⸻

Next Steps
	•	Add uncertainty fields (confidence, georef_error_m, dating_precision) across schemas & templates ￼.
	•	Add predictive modeling hooks (erosion, drought, settlement clustering) with clear validation plans ￼.
	•	Provide story-map templates to sequence treaty layers, oral histories, and environmental change ￼.
	•	Expand data_sources.md documenting USGS/Kansas GIS/NOAA/KGS endpoints & scripts ￼ ￼.

⸻

Reminder: If rendering fails, fix the metadata or schemas — not the templates.
Templates enforce the contract; contracts preserve truth ￼.

