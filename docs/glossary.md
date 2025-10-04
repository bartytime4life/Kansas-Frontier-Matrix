<div align="center">

# 📘 Kansas Frontier Matrix — Glossary  
`docs/glossary.md`

**Mission:** Provide authoritative definitions for all technical, geospatial, historical, and procedural terms  
used throughout the Kansas Frontier Matrix (KFM) repository — promoting consistency, transparency,  
and interoperability across all documentation, datasets, and pipelines.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

## 📚 Overview

This glossary serves as a **cross-disciplinary reference index** for contributors, researchers,  
and developers working on the Kansas Frontier Matrix.  

It consolidates terminology from:
- 🧱 **Architecture & CI/CD**
- 🌎 **Geospatial data systems**
- 🧩 **STAC & metadata frameworks**
- 🧠 **Knowledge graph ontology**
- 📜 **Historical & archival documentation**

Every entry aligns with the **Master Coder Protocol (MCP)** principles of documentation-first reproducibility  
and provides links to related files or standards.

---

## 🧩 Core Terminology

| Term | Definition | Context |
|:------|:-------------|:----------|
| **MCP (Master Coder Protocol)** | Documentation-first framework ensuring reproducibility, provenance, and auditability. | Used across all KFM docs and pipelines. |
| **STAC (SpatioTemporal Asset Catalog)** | Open geospatial metadata standard for describing datasets, assets, and collections. | Used in `data/stac/`. |
| **ETL (Extract–Transform–Load)** | Data pipeline model for ingestion, cleaning, and standardization. | Implemented in `src/pipelines/`. |
| **Checksum** | Cryptographic hash verifying data integrity and reproducibility (SHA-256). | Stored in `data/checksums/`. |
| **CIDOC CRM** | Cultural heritage ontology modeling events, people, and places. | Used in `docs/architecture/knowledge-graph.md`. |
| **JSON Schema** | Schema validation format for JSON data structures. | Used in metadata validation and STAC items. |
| **GeoTIFF (COG)** | Cloud-Optimized GeoTIFF, a spatial raster format designed for web streaming. | Used in `data/processed/terrain/`. |
| **GeoJSON** | Lightweight open standard for vector spatial data. | Used in `data/processed/hydrology/`. |
| **Tabular Data (CSV/Parquet)** | Structured non-spatial datasets (e.g., census, agriculture). | Used in `data/processed/tabular/`. |
| **OCR (Optical Character Recognition)** | Conversion of scanned text into machine-readable formats. | Used in `data/processed/text/`. |
| **Pipeline** | Scripted data processing module transforming input → output. | `src/pipelines/<domain>_pipeline.py`. |
| **Checksum Manifest** | Collection of all `.sha256` integrity hashes. | `data/checksums/manifest.json`. |
| **Validation Workflow** | Automated CI/CD process testing data, metadata, and schema compliance. | `.github/workflows/stac-validate.yml`. |
| **Makefile** | Task automation script defining reproducible build targets. | Repository root. |
| **Provenance** | Documented origin, lineage, and transformation of a dataset. | Enforced via metadata and checksums. |
| **Auditability** | Capability to trace, verify, and reproduce every result or output. | Core MCP requirement. |
| **Documentation-first** | The practice of writing and validating documentation before code execution. | MCP Principle. |
| **Open Standards** | File and schema formats free from proprietary restrictions. | Includes STAC, GeoTIFF, JSON, CSV, NetCDF. |
| **Reproducibility** | The ability to regenerate identical results from the same sources. | Enforced by CI/CD pipelines. |
| **Provenance Chain** | Linked record of all data transformations and validations. | Described in `data/ARCHITECTURE.md`. |
| **Audit Trail** | Historical log of CI/CD executions, validations, and dataset states. | Stored in `data/work/logs/`. |
| **Web Viewer** | MapLibre-based frontend for visualizing KFM datasets. | `web/` directory. |
| **Timeline Slider** | Interactive control allowing exploration of datasets across time. | Implemented in `web/app.js`. |
| **Knowledge Graph** | Semantic network connecting datasets, people, places, and events. | `docs/architecture/knowledge-graph.md`. |
| **RDF (Resource Description Framework)** | Standard model for linked data representation. | Used for graph storage and querying. |
| **SPARQL** | Query language for RDF datasets. | Used to query KFM knowledge graph. |
| **Ontology** | Structured representation of relationships among entities. | Used in semantic graph design. |
| **CIDOC CRM Entity** | Class used to represent events, documents, or objects in cultural data. | Knowledge graph context. |
| **PROV-O** | W3C Provenance Ontology for tracking data lineage. | Integrated with STAC metadata. |
| **OWL-Time** | Ontology for modeling temporal intervals and events. | Used for historical dataset modeling. |
| **CI/CD (Continuous Integration / Deployment)** | Automation framework validating and deploying code and data changes. | `.github/workflows/` |
| **CodeQL** | Static analysis tool for detecting vulnerabilities in source code. | `.github/workflows/codeql.yml`. |
| **Trivy** | Security scanner for dependencies and container images. | `.github/workflows/trivy.yml`. |
| **Pre-Commit Hooks** | Automatic checks (linting, formatting, validation) before commit. | `.pre-commit-config.yaml`. |
| **Mermaid** | Open-source syntax for diagram rendering in Markdown. | Used in `docs/architecture/diagrams/`. |
| **MapLibre** | Open-source mapping engine used in the KFM web viewer. | `web/index.html`. |
| **Tiles (Raster/Vector)** | Web-optimized map layers generated from processed data. | `data/tiles/`. |
| **CC-BY 4.0** | Creative Commons license permitting reuse with attribution. | All KFM documentation. |
| **MIT License** | Open-source license governing KFM source code. | `LICENSE` file. |

---

## 🧱 Acronyms and Abbreviations

| Acronym | Full Form | Description |
|:-----------|:-----------|:-------------|
| **KFM** | Kansas Frontier Matrix | Project name and repository identifier. |
| **MCP** | Master Coder Protocol | Documentation-first reproducibility framework. |
| **STAC** | SpatioTemporal Asset Catalog | Metadata schema for spatiotemporal assets. |
| **ETL** | Extract, Transform, Load | Pipeline for data ingestion and transformation. |
| **CI/CD** | Continuous Integration / Continuous Deployment | Automated validation and deployment system. |
| **RDF** | Resource Description Framework | Data model for semantic graphs. |
| **CSV** | Comma-Separated Values | Tabular data format. |
| **COG** | Cloud-Optimized GeoTIFF | Efficient raster format for streaming. |
| **NHD** | National Hydrography Dataset | USGS dataset for rivers and streams. |
| **WBD** | Watershed Boundary Dataset | USGS dataset for hydrologic units. |
| **NOAA** | National Oceanic and Atmospheric Administration | Climate and weather data provider. |
| **USGS** | U.S. Geological Survey | Federal mapping and elevation data provider. |
| **USDA** | U.S. Department of Agriculture | Agricultural and landcover data provider. |
| **BEA** | Bureau of Economic Analysis | Source for economic and demographic data. |
| **BLS** | Bureau of Labor Statistics | Workforce and labor economics data source. |
| **KSHS** | Kansas State Historical Society | Provider of archival and oral history materials. |

---

## 🧾 Cross-References

| Related Document | Description |
|:------------------|:-------------|
| [`docs/architecture/architecture.md`](architecture/architecture.md) | Full system overview. |
| [`docs/architecture/data-architecture.md`](architecture/data-architecture.md) | Data flow and lineage architecture. |
| [`docs/architecture/knowledge-graph.md`](architecture/knowledge-graph.md) | Semantic graph integration. |
| [`docs/architecture/pipelines.md`](architecture/pipelines.md) | ETL and processing workflows. |
| [`docs/architecture/ci-cd.md`](architecture/ci-cd.md) | CI/CD system architecture. |
| [`docs/standards/metadata-standards.md`](standards/metadata-standards.md) | Metadata and schema standards. |

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation |
|:--------------|:----------------|
| **Documentation-first** | Every major term defined and cross-referenced. |
| **Reproducibility** | Terms describe reproducible frameworks and workflows. |
| **Open Standards** | Includes definitions for open data and metadata formats. |
| **Provenance** | Definitions link directly to data sources and architecture files. |
| **Auditability** | Glossary reviewed for consistency in CI/CD validation. |

---

## 📅 Version History

| Version | Date | Summary |
|:---------|:------|:----------|
| v1.0 | 2025-10-04 | Initial comprehensive glossary for Kansas Frontier Matrix terminology and MCP compliance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Defining Every Term. Clarifying Every Connection.”*  
📍 [`docs/glossary.md`](.) · The canonical terminology reference for the Kansas Frontier Matrix documentation ecosystem.

</div>
