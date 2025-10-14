<div align="center">

# 🌾 Kansas Frontier Matrix  
### _An Open-Source Geospatial-Historical Knowledge System for Kansas_

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../actions/workflows/stac-validate.yml)
[![CodeQL Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../actions/workflows/codeql.yml)
[![Trivy Container Scan](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../actions/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](./docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](./LICENSE)
[![Version](https://img.shields.io/badge/Version-MCP-DL v6.2-green)](./docs/standards/)

</div>

---

## 📚 Overview

**Kansas Frontier Matrix (KFM)** is an open, reproducible **geospatial-historical knowledge hub** that unites Kansas’s
fragmented environmental, cartographic, and cultural records into an interactive **map-and-timeline interface**.  
The system links **people ↔ places ↔ events ↔ documents** through a semantically enriched **knowledge graph**,  
combining AI/ML pipelines, GIS data, and public archives under the **Master Coder Protocol (MCP)**.

KFM follows **FAIR** principles — *Findable, Accessible, Interoperable, Reusable* — and all documentation is written in
**MCP-DL v6.2**, ensuring clarity, provenance, and machine-readability.

---

## 🧭 Mission

> _Reconstruct Kansas’s historical, ecological, and cultural frontier as an auditable, reproducible digital atlas._  
> Every dataset, model, and document is traceable — from raw sources to processed layers — through standardized
README and STAC metadata.

---

## 🏗 System Architecture

```mermaid
flowchart LR
    A["External Sources<br>(NOAA · USGS · FEMA · KHS · Treaties)"]
    --> B["Python ETL + AI Pipeline<br>(NER · OCR · Geocoding · Summarization)"]
    --> C["Neo4j Knowledge Graph<br>(People · Places · Events · Documents)"]
    --> D["FastAPI / GraphQL API"]
    --> E["React + MapLibre Web UI<br>(Map · Timeline · AI Panels)"]
````

<!-- END OF MERMAID -->

**Layers**

| Layer                | Technology                            | Function                                                         |
| :------------------- | :------------------------------------ | :--------------------------------------------------------------- |
| **Data Extraction**  | Python ETL scripts (`src/pipelines/`) | Fetch and normalize raw data from APIs and archives.             |
| **AI/ML Processing** | spaCy, Transformers                   | NER, OCR, summarization, entity linking to graph.                |
| **Knowledge Graph**  | Neo4j (+ GeoSPARQL extension)         | Stores entities and relations with spatial and temporal indexes. |
| **API Layer**        | FastAPI (REST/GraphQL)                | Serves queries to frontend and external clients.                 |
| **Frontend**         | React + MapLibre GL JS + D3           | Interactive map and timeline visualization.                      |
| **Docs & CI/CD**     | GitHub Actions · MkDocs               | Continuous validation and site generation.                       |

---

## 🗂 Repository Layout (Monorepo)

```text
Kansas-Frontier-Matrix/
├─ src/          # Python ETL & AI pipelines (ingest, NER, graph integration)
├─ web/          # React frontend (MapLibre GL + timeline UI)
├─ data/
│  ├─ sources/   # JSON source manifests (pointers to external data)
│  ├─ raw/       # immutable original data (DVC/LFS tracked)
│  ├─ processed/ # standardized outputs (COG, GeoJSON, CSV)
│  └─ stac/      # SpatioTemporal Asset Catalog metadata
├─ docs/         # Architecture, SOPs, model cards, MCP standards
├─ tools/        # utility scripts (data converters, build/deploy)
├─ tests/        # automated unit & integration tests
└─ .github/      # CI/CD workflows, issue/PR templates, governance
```

Each directory contains its own **README.md** per [MCP-DL v6.2](./docs/standards/) — no black boxes.

---

## 🧮 Core Data Domains

| Domain                 | Example Datasets                             | Format / Standard                              |
| :--------------------- | :------------------------------------------- | :--------------------------------------------- |
| Terrain & Elevation    | USGS 3DEP LiDAR, KS DEM 1 m                  | Cloud-Optimized GeoTIFF (COG) · STAC Item JSON |
| Hydrology              | NHD flowlines, Kansas rivers                 | GeoJSON / Shapefile · GeoSPARQL                |
| Climate & Hazards      | NOAA Daymet, Storm Events, FEMA Disasters    | CSV / NetCDF / JSON · DCAT metadata            |
| Historical Records     | Kansas Memory, Chronicling America, Treaties | Text + OCR JSON · CIDOC CRM E73 docs           |
| Cultural & Archaeology | Site Inventories, Oral Histories             | GeoJSON + transcripts · CRM E5 Events          |

All datasets include provenance fields, license, bounding box, temporal extent, and SHA-256 checksum.

---

## 💠 Documentation Standards

* **MCP-DL v6.2** – Markdown Documentation Language spec for structure & semantics.
* **STAC 1.0 / DCAT 2.0** – dataset metadata standards.
* **CIDOC CRM · OWL-Time · GeoSPARQL** – semantic ontology alignment.
* **YAML Front-Matter + JSON-LD** in each doc for machine readability.
* **Docs Validation CI** – automated Markdown/STAC linting in GitHub Actions.

See [`docs/standards/`](./docs/standards/) for full rules and templates.

---

## 🤖 AI and Analytics Modules

* **Entity Extraction (NER):** Custom spaCy model for frontier-era names and places.
* **Summarization:** Hugging Face BART/T5 models for document synopses.
* **Pattern Recognition:** Temporal + spatial clustering (Fractal & Bayesian methods).
* **Symbolic Reasoning:** Ontology-driven inference over graph relations.

Each model is documented with a [Model Card](./docs/templates/model_card.md) per MCP-DL.

---

## 🧩 Contributing

We welcome historians, developers, and citizens to expand Kansas Frontier Matrix.
Please see [`CONTRIBUTING.md`](./CONTRIBUTING.md) for branch workflow, semantic commit rules, and MCP checklist.
Every PR must include:

1. Updated README or dataset metadata (STAC Item + checksum).
2. Passing tests and docs lint (`make test`, `make docs-validate`).
3. License confirmation for new data (CC-BY or Public Domain preferred).

---

## 📜 License & Attribution

* **Code:** MIT License – free for reuse with attribution.
* **Data & Docs:** Creative Commons BY 4.0 (CC-BY-4.0).
  Cite as:

> *Barta, A. et al. (2025). Kansas Frontier Matrix v6.2 — An Open Geospatial-Historical Knowledge System.*
> DOI: *pending (see `CITATION.cff`)*.

---

## 🧾 Version History

| Version | Date       | Notes                                                                    |
| :------ | :--------- | :----------------------------------------------------------------------- |
| v6.2    | 2025-10-13 | Adopt MCP-DL v6.2 framework; add semantic ontologies and STAC alignment. |
| v6.1    | 2025-09    | Initial repository standardization under MCP-DL v6 series.               |

---

<div align="center">

### 🏛 “Document the Frontier · Reconstruct the Past · Illuminate Connections.”

© 2025 Kansas Frontier Matrix · MIT / CC-BY 4.0

</div>
```
