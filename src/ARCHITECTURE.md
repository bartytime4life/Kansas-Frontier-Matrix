# Kansas Geo Timeline — Architecture

This document explains how the repository fits together from **raw data → contracts → rendered outputs → site → knowledge graph**, and how contributors can extend the system safely and reproducibly.

---

## High-Level Overview

The stack unifies **history, cartography, and geology** in one reproducible pipeline.  
Core ideas:

- **Contracts first** — schemas validate everything (STAC, map configs, MCP docs) before generation [oai_citation:0‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468) [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).  
- **Evidence & time** — sources (maps, diaries, treaties, cores) are linked with provenance and dates for timeline reasoning [oai_citation:2‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv) [oai_citation:3‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).  
- **Knowledge graph ready** — people, places, events, documents are linked and queryable via APIs (time, location, confidence) [oai_citation:4‡Kansas Historical Knowledge Hub – System Design.pdf](file-service://file-P6gGz263QNwmmVYw8LBSvB).  
- **Open & modular** — containerized components; STAC-like catalogs document source, license, processing, and time spans [oai_citation:5‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).

---

## Repository Layers

.
├── data/                   # Source descriptors (YAML/JSON), layer configs, endpoints
├── stac/                   # Rendered STAC catalog/collections/items (validated)
├── web/                    # Static site: MapLibre app, time slider, assets
├── docs/                   # Handbooks, design notes, generated narratives
├── src/kansas_geo_timeline # Core package (CLI, schemas, templates, utils)
└── tests/                  # Contract checks & integration tests

**Roles**

- **data/**: Declarative descriptors for layers and sources (e.g., USGS historic topos, DEM/COG, hydrology, soils, treaties) [oai_citation:6‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv) [oai_citation:7‡Data resource analysis.pdf](file-service://file-GdS9Kcw7Xbfqpy4xwwdqWS).  
- **src/**:  
  - `schemas/` — JSON Schema for STAC, map configs, MCP templates [oai_citation:8‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468)  
  - `templates/` — Jinja2 + HTML to render STAC & `web/app.config.json` [oai_citation:9‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv)  
  - `cli.py (kgt)` — validate → render → list  
- **stac/**: Output STAC 1.0.0 items/collections (machine-readable provenance) [oai_citation:10‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv)  
- **web/**: MapLibre config & UI (HTML/CSS/Canvas, accessible & responsive) [oai_citation:11‡Engineering Guide to GUI Development Across Platforms.pdf](file-service://file-JLg6Ai66jZTgdjtc39RJWp) [oai_citation:12‡HTML5 Notes for Professionals - HTML5NotesForProfessionals.pdf](file-service://file-P9kCBXAKs71PBtGkez665c) [oai_citation:13‡HTML5 Canvas Notes for Professionals - HTML5CanvasNotesForProfessionals.pdf](file-service://file-7fT2zjYCiooDLCcuwUFsr2)  
- **docs/**: Narrative docs (MCP experiment/glossary), data catalogs, architecture [oai_citation:14‡Foundational Templates and Glossary for Scientific Method _ Research _ Master Coder Protocol.pdf](file-service://file-XygDDSfCPa5gz3jmjRV81b)  

---

## Dataflow

```mermaid
flowchart TD
  A[Data descriptors\nYAML/JSON in data/] -->|jsonschema| B[Schemas\n(STAC • Map • MCP)]
  B -->|contracts OK| C[Templates\n(Jinja2)]
  C -->|render| D[Outputs]

  D --> O1[stac/*.json]
  D --> O2[web/app.config.json]
  D --> O3[docs/generated/*.md]

  subgraph "Static Site"
    O1 --> W[MapLibre App + Time Slider]
    O2 --> W
    O3 --> W
  end

  W --> U[Researchers & Public Users]

Why this shape?
	•	STAC establishes machine-readable provenance/time for downstream reasoning ￼.
	•	MapLibre config cleanly separates data contracts from presentation (retained/declarative UI best practices) ￼.
	•	Docs (MCP) ensure scientific rigor & reproducibility for cross-disciplinary work ￼ ￼.

⸻

Knowledge Graph Integration

The Kansas Historical Knowledge Hub ingests site outputs and document extractions into a graph of People, Places, Events, Documents, with edges for mentions/located_in/participated_in/occurred_at and confidence fields ￼.

flowchart LR
  S[STAC Items\n(stac/*.json)] --> G[(Knowledge Graph)]
  M[Map Config\n(web/app.config.json)] --> W[Web UI]
  D[Docs (MCP)\n(docs/generated/*.md)] --> G
  W --> Q[API Queries\n(time, location, entity, confidence)]
  G --> Q

	•	NLP + gazetteers normalize toponyms; graph enables time-bound queries (“people in Dodge City in 1880”) ￼.
	•	Confidence/uncertainty recorded and surfaced in UI/graph ￼.

⸻

Contracts & Validation
	•	STAC 1.0.0 for spatial/temporal provenance (catalog → collections → items) ￼
	•	Map config schema for MapLibre layers, sources, and time metadata
	•	MCP docs schemas for experiment/glossary/story templates (problem → hypothesis → method → results → uncertainty) ￼ ￼

The CLI (kgt) runs:

# Validate STAC
kgt validate stac/items/

# Render map config
kgt render map data/sources/*.yml -o web/app.config.json

# Generate MCP docs
kgt render docs data/experiments/*.yml -o docs/generated/


⸻

CI/CD
	•	Pre-merge: jsonschema + pytest on schemas, configs, and rendered artifacts.
	•	Build: Render site config; bundle static site.
	•	Publish: GitHub Pages deployment.
	•	Artifacts: Upload validation logs & STAC reports.

This mirrors the modular ingestion → validation → graph → visualization architecture in the hub design ￼ ￼.

⸻

Data Sources (Examples)
	•	Historic Maps & ToPOs: USGS historical topographic map collection (georeferenced scans) ￼
	•	Terrain: Kansas DEM (1 m) & hillshade/derivatives; county LiDAR where available ￼
	•	Hydrology/Soils: State GIS endpoints for streams, lakes, soils (add missing endpoints) ￼
	•	Treaties & Tribal Lands: Time-aware treaty boundary layers with narrative context (stories + primary source links) ￼
	•	Climate/Hazards: NOAA GHCN-D (stations), Daymet (1 km), SPC tornado tracks, FEMA disasters, US Drought Monitor ￼

Maintain docs/data_sources.md with API URLs, licenses, and update cadence (design audit recommendation) ￼.

⸻

Uncertainty & Modeling
	•	Add georef precision, dating precision, and confidence scores across schemas/templates ￼.
	•	Hook in predictive modules (erosion/drought/settlement) with NASA-grade V&V mindset (credibility, verification, validation) ￼.
	•	Consider fractal/pattern metrics for rivers/settlements/narratives to discover multi-scale structure ￼ ￼.

⸻

UX & Accessibility
	•	MapLibre + declarative/retained-mode site structure; responsive HTML/CSS; Canvas for overlays when needed ￼ ￼ ￼ ￼.
	•	Plan story-map mode for guided narratives (Santa Fe Trail, hydrology changes, treaty timelines) ￼.

⸻

Contributor Playbook
	1.	Add a layer: Create/update a data/sources/*.yml descriptor.
	2.	Validate: kgt validate to confirm schema compliance.
	3.	Render: kgt render map … and inspect the resulting web/app.config.json.
	4.	STAC: Generate or update stac/*.json for provenance/time.
	5.	Docs: Use MCP templates to document methodology/uncertainty ￼.
	6.	Open a PR: CI runs validation & site build; reviewers check schema adherence and uncertainty annotations.

⸻

Roadmap Highlights
	•	Paleoclimate proxies (tree rings, cores, drought indices) integrated in time series ￼ ￼.
	•	Hydrology modeling hooks and dynamic linking of flood events to timeline ￼.
	•	Public submission portal for oral histories & local materials with review workflow (beyond PRs) ￼.
	•	Dataset coverage expansion (LiDAR, orthophotos, small-patch habitats) and statewide erosion modeling integration ￼.

⸻

Contract-first rule: if something fails to render or visualize, fix the metadata or the schema, not the template.
Templates enforce the contract; contracts preserve truth ￼ ￼.

