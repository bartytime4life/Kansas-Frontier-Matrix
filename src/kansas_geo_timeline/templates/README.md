# Kansas Geo Timeline — Templates

This directory contains **Jinja2 and HTML templates** used across the  
Kansas Geo Timeline / Kansas-Frontier-Matrix stack.

Templates act as **generators** for:
- **STAC JSON** (Catalogs, Collections, Items)
- **Map configuration JSON** (MapLibre layers, time slider)
- **HTML pages** (GitHub Pages site, reports, story maps)
- **MCP-style docs** (experiments, glossary, narratives)

By using templates, we ensure outputs are:
- **Consistent & reproducible** — shared structure, provenance fields, and schema validation are applied by design [oai_citation:0‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-AJeFJoUqFfFcKmtpGMVUA4) [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).
- **Interoperable** — history, cartography, geology, archaeology, and environmental layers render from the same metadata contracts [oai_citation:2‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468) [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).
- **Extensible** — new layers/entities/narratives can be added without rewriting core code [oai_citation:4‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv) [oai_citation:5‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN).

---

## Contents

- **`stac/`**  
  Templates for **STAC 1.0.0** Catalogs, Collections, and Items (e.g., COG rasters & vectors), including
  spatial/temporal extents and checksums for traceability [oai_citation:6‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).

- **`map/`**  
  Templates for **MapLibre/Leaflet configs** (e.g., `app.config.json.j2`) that wire layers, sources,
  and time-slider metadata from declarative descriptors [oai_citation:7‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).

- **`docs/`**  
  Markdown templates for **MCP** artifacts:
  - **Experiments** (Problem → Hypothesis → Method → Variables → Data → Results → Conclusion) [oai_citation:8‡Foundational Templates and Glossary for Scientific Method _ Research _ Master Coder Protocol.pdf](file-service://file-XygDDSfCPa5gz3jmjRV81b) [oai_citation:9‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468)
  - **Glossary** (cross-disciplinary terms: projection, stratigraphy, treaty, etc.) [oai_citation:10‡Integrating Historical, Cartographic, and Geological Research (MCP Reference).pdf](file-service://file-HTPyrF5na2BY7mrNRai468)
  - **Story maps** (guided narratives that sequence maps/timelines/quotes) [oai_citation:11‡Kansas-Frontier-Matrix Design Audit – Gaps and Enhancement Opportunities.pdf](file-service://file-BgUSuffTiRq4qidye2sPwN)

- **`ui/`**  
  HTML5/CSS/Canvas snippets (legends, tooltips, panels) built with accessible, responsive patterns [oai_citation:12‡HTML5 Notes for Professionals - HTML5NotesForProfessionals.pdf](file-service://file-P9kCBXAKs71PBtGkez665c) [oai_citation:13‡CSS Notes for Professionals - CSSNotesForProfessionals.pdf](file-service://file-G8bTkTVm7aYDcDbHF8kVcy) and Canvas add-ons where useful [oai_citation:14‡HTML5 Canvas Notes for Professionals - HTML5CanvasNotesForProfessionals.pdf](file-service://file-7fT2zjYCiooDLCcuwUFsr2).

---

## Workflow Integration

1. **Ingestion** — YAML/JSON descriptors in `data/` (sources, layers, entities) are parsed; metadata is validated against schemas (see `../schemas`) [oai_citation:15‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).  
2. **Template rendering** — Jinja2 fills placeholders (e.g., `{{ id }}`, `{{ bbox }}`, `{{ start_date }}`) from the validated metadata.  
3. **Output generation** —  
   - STAC → `stac/*.json`  
   - Map configs → `web/app.config.json`  
   - Docs → `docs/generated/*.md`  
4. **Validation** — Outputs are checked via JSON Schema/pytest; CI enforces validity on PRs and site builds [oai_citation:16‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-CrPP4mcnyNq5sGJotXDwSv).

---

## System Flow (Mermaid)

> GitHub renders Mermaid inside triple-backtick code fences with `mermaid` as the language.

```mermaid
flowchart TD
  %% Sources & Data
  A[Data Descriptors\n(YAML/JSON in data/)] -->|load| B[Renderer\n(Jinja2 CLI)]
  subgraph Schemas & Tests
    S1[Schemas: STAC/Entities\n../schemas/*]
    S2[Unit/Schema Tests\npytest, jsonschema]
  end

  %% Rendering paths
  B --> C1[STAC Templates\nstac/*.j2]
  B --> C2[Map Config Templates\nmap/*.j2]
  B --> C3[Doc Templates\ndocs/*.j2]
  B --> C4[UI Snippets\nui/*.html.j2]

  %% Outputs
  C1 --> O1[Rendered STAC JSON\nstac/*.json]
  C2 --> O2[Rendered Map Config\nweb/app.config.json]
  C3 --> O3[Generated Docs\ndocs/generated/*.md]
  C4 --> O4[HTML Partials\nweb/includes/*]

  %% Validation & Site
  O1 -->|validate| S2
  O2 -->|validate| S2
  O3 -->|lint/build| S2
  O4 -->|lint| S2

  %% Publish / Visualize
  S2 --> P[CI/CD\n(GitHub Actions)]
  P --> W[GitHub Pages Site\n+ MapLibre App]
  W --> U[End Users\nMaps • Timeline • Story Maps]


⸻

Example

Template: stac/item.json.j2

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "{{ id }}",
  "bbox": {{ bbox }},
  "properties": {
    "datetime": "{{ datetime }}",
    "title": "{{ title }}",
    "description": "{{ description }}"
  },
  "assets": {
    "image": {
      "href": "{{ image_href }}",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}

Rendered Output: stac/items/LAWRENCE_1885.json (excerpt)

{
  "type": "Feature",
  "id": "LAWRENCE_1885",
  "bbox": [-95.28, 38.95, -95.22, 39.02],
  "properties": {
    "datetime": "1885-01-01T00:00:00Z",
    "title": "Lawrence, Kansas — 1885"
  },
  "assets": {
    "image": {
      "href": "data/cogs/LAWRENCE_1885.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized"
    }
  }
}


⸻

Design Notes
	•	Documentation-first & MCP-aligned — templates for experiments and glossary make research steps repeatable and auditable ￼ ￼ ￼.
	•	Time + Space native — map templates expose time attributes and spatial metadata for animated eras and overlays ￼.
	•	Uncertainty-ready — placeholders for confidence/error fields can be added (e.g., {{ confidence }}, {{ georef_error_m }}) to surface uncertainty as recommended in the design audit ￼.
	•	Accessible & responsive UI — HTML/CSS/Canvas snippets follow event-driven and declarative UI best practices, enabling performant, adaptive layouts ￼ ￼ ￼ ￼.
	•	Analysis handoff — doc templates can embed R code blocks or link to reproducible scripts/notebooks for maps and stats ￼.

⸻

Next Steps
	•	Add uncertainty placeholders across STAC/Map/Doc templates and surface them in legends/tooltips ￼.
	•	Provide Mermaid partials for auto-generated diagrams in docs (pipelines, lineage, layer stacks).
	•	Expand R analysis templates (ggplot/tmap stubs) for quick-start spatial stats and cartography ￼.
	•	Add story map templates that sequence treaty layers, oral histories, and environmental change over time ￼.
	•	Include environmental modeling config templates (erosion, drought, fire-regime scenarios) to support predictive workstreams ￼ ￼.

⸻

Reminder: fix metadata or schemas first—not the template—if rendering fails. Templates enforce the contract; contracts preserve truth ￼.

