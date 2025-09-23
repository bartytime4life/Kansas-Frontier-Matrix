# Kansas Geo Timeline — Source Code Overview

This folder contains the **core source code** for the  
**Kansas Geo Timeline / Kansas-Frontier-Matrix** stack.

It unifies **history, cartography, and geology** into a reproducible pipeline [oai_citation:0‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468) [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).  
The code here drives schema validation, template rendering, CLI tools, and integration with  
the Kansas Historical Knowledge Hub [oai_citation:2‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).

---

## Structure

src/
├── kansas_geo_timeline/     # Core Python package
│   ├── init.py          # Version resolver & helpers
│   ├── cli.py               # kgt CLI entrypoint
│   ├── schemas/             # JSON Schema contracts
│   │   └── README.md
│   ├── templates/           # Jinja2 & HTML templates
│   │   └── README.md
│   └── utils/               # Loaders, path resolvers, misc helpers
└── README.md                # (this file)

---

## Responsibilities

- **Schemas**: JSON Schema definitions for  
  - STAC 1.0.0 catalog/collections/items  
  - MapLibre config validation  
  - MCP experiment/glossary templates [oai_citation:3‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468) [oai_citation:4‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN)

- **Templates**: Jinja2 & HTML templates for  
  - STAC metadata generation  
  - MapLibre configs (`web/app.config.json`)  
  - Narrative docs (e.g. experiment reports, glossaries) [oai_citation:5‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv)

- **CLI (`kgt`)**: Lightweight commands to  
  - Validate STAC/catalog JSON  
  - Render map configs  
  - Generate docs (experiments, glossaries, story maps)

- **Utils**: JSON/YAML loaders, schema fetchers, and path helpers.  
  Designed to be **dependency-light**, so tests and CI can run without GIS/ML stacks.

---

## Principles

- **Cross-disciplinary integration**:  
  Connect historical docs, cartography, and geology into one knowledge base [oai_citation:6‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468) [oai_citation:7‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).

- **Evidence-first**:  
  All ingested facts are tied to source docs (maps, diaries, treaties, surveys) for traceability [oai_citation:8‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).

- **Time-aware**:  
  Every dataset carries explicit or inferred time ranges (supporting time-slider visualization) [oai_citation:9‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).

- **Uncertainty-ready**:  
  Gaps, georeferencing errors, and extraction ambiguities are recorded and surfaced [oai_citation:10‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN).

- **Open-source & modular**:  
  Containerized, STAC-driven, and reproducible from raw data to interactive site [oai_citation:11‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv) [oai_citation:12‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).

---

## Visualization Flow

```mermaid
flowchart TD
  A[Data Sources\n(maps, DEMs, treaties, diaries)] -->|ingest| B[Schemas & Validation]
  B -->|contracts| C[Templates (Jinja2/HTML)]
  C -->|render| D[Outputs]
  D --> O1[stac/*.json]
  D --> O2[web/app.config.json]
  D --> O3[docs/generated/*.md]

  subgraph Site
    O2 --> W[MapLibre Web App + Time Slider]
    O1 --> W
    O3 --> W
  end

  W --> U[Researchers & Public Users]


⸻

Integration with Knowledge Hub

This repo’s outputs connect with the Kansas Historical Knowledge Hub ￼:
	•	Documents ingested into a knowledge graph (people, places, events).
	•	Cross-source corroboration assigns confidence scores.
	•	Exposed via APIs for timeline & map exploration.

The schemas/ and templates/ here ensure consistent, valid, reproducible data across the pipeline.

⸻

Next Steps
	•	Expand data sources: Kansas DEM, historic maps, hydrology, soils, tribal treaties ￼ ￼.
	•	Add uncertainty & error fields (georef precision, confidence scores).
	•	Build story-map templates: treaty changes, migrations, fire regimes ￼.
	•	Incorporate paleoclimate & proxy data (tree rings, cores, drought indices) ￼ ￼.
	•	Extend simulation hooks for erosion, drought, and settlement predictive models ￼.

⸻

📌 Reminder: This src/ tree is dependency-light.
Heavy GIS/ML stacks run in pipelines or notebooks, not in this package.

---
