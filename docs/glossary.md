<div align="center">

# 📘 Kansas Frontier Matrix — Glossary  
`docs/glossary.md`

**Mission:** Provide a **canonical reference** for all technical, geospatial, historical, and procedural terms  
used across the **Kansas Frontier Matrix (KFM)** project — ensuring cross-discipline clarity, transparency,  
and interoperability in documentation, datasets, and pipelines.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)

</div>

---

## 📚 Overview

The **Kansas Frontier Matrix Glossary** is a **cross-domain reference** for developers, researchers, historians,  
and data scientists contributing to or using this repository.  

It aligns language across all MCP-compliant documentation and serves as a **knowledge interface**  
linking the project’s data architecture, workflows, ontologies, and CI/CD systems.  

This glossary is organized by category:
- 🧱 **Architecture & Infrastructure**
- 🌎 **Geospatial & Environmental Data**
- 🧩 **Metadata & Interoperability**
- 🧠 **Knowledge Graph & Semantics**
- 📜 **Historical & Archival Concepts**
- ⚙️ **CI/CD & Governance**

---

## 🧩 Core Terminology

| Term | Definition | Context |
|:------|:-------------|:----------|
| **MCP (Master Coder Protocol)** | Documentation-first methodology ensuring reproducibility, provenance, and transparency. | Foundational across all KFM workflows. |
| **STAC (SpatioTemporal Asset Catalog)** | Open metadata schema for describing spatiotemporal assets and datasets. | `data/stac/` collections and items. |
| **ETL (Extract–Transform–Load)** | A structured data workflow to ingest, normalize, and prepare datasets. | `src/pipelines/` directory. |
| **Checksum** | Cryptographic hash (SHA-256) used for data integrity verification. | Generated in `data/checksums/`. |
| **CIDOC CRM** | International ontology for cultural heritage and historical data relationships. | Knowledge Graph schema in `src/graph/`. |
| **OWL-Time** | Temporal ontology representing intervals, durations, and sequencing. | Used for event timelines. |
| **JSON Schema** | A schema standard for validating JSON structures. | Used in STAC and internal schema validation. |
| **GeoTIFF (COG)** | Cloud-Optimized GeoTIFF, a raster format for web-ready imagery. | Terrain data in `data/processed/rasters/`. |
| **GeoJSON** | JSON format encoding geographic vector data structures. | Boundaries, roads, hydrology layers. |
| **CSV / Parquet** | Open tabular data formats for time-series and statistical data. | Census and agricultural datasets. |
| **OCR (Optical Character Recognition)** | Conversion of scanned documents into machine-readable text. | Used in `data/processed/text/`. |
| **Pipeline** | Automated sequence of data tasks — fetch, transform, enrich, and load. | `src/pipelines/<stage>/` scripts. |
| **Provenance** | Tracked lineage of dataset origin, transformation, and verification. | Recorded in STAC metadata and logs. |
| **Auditability** | Ability to verify every dataset, transformation, and model result. | Implemented through CI/CD and checksum tracking. |
| **Documentation-first** | MCP principle requiring documentation before implementation. | Enforced across all new modules. |
| **Reproducibility** | Guarantee that identical results can be regenerated from the same data and code. | CI/CD pipelines and Makefile tasks. |
| **Ontology** | Structured representation of conceptual relationships. | Knowledge Graph modeling. |
| **Knowledge Graph** | Semantic data network linking entities (people, places, events, documents). | Implemented via Neo4j / RDF. |
| **RDF (Resource Description Framework)** | Standard model for representing information as triples. | Data export format for Knowledge Graph. |
| **SPARQL** | Query language for RDF graphs. | Used for semantic data queries. |
| **PROV-O** | W3C Provenance Ontology describing data lineage. | Used in metadata enrichment. |
| **CIDOC Entity** | Node in the cultural ontology (e.g., Person, Event, Place, Object). | Graph schema design. |
| **STAC Item** | Metadata record describing an individual spatiotemporal asset. | GeoTIFF or GeoJSON entry in catalog. |
| **STAC Collection** | Aggregation of multiple related STAC items with shared metadata. | Used in catalog indexing. |
| **Temporal Range** | Start and end times for dataset validity or event occurrence. | Displayed in timeline slider. |
| **Timeline Slider** | Interactive UI component for temporal exploration. | Web app (`web/`). |
| **Web Viewer** | MapLibre-based frontend for geospatial exploration. | `web/` directory. |
| **Mermaid Diagram** | Markdown syntax for rendering system flowcharts. | `docs/architecture/*.md`. |
| **CI/CD** | Continuous integration and deployment pipelines for automation and validation. | `.github/workflows/`. |
| **CodeQL** | Static code analyzer used for vulnerability detection. | `.github/workflows/codeql.yml`. |
| **Trivy** | Container and dependency vulnerability scanner. | `.github/workflows/trivy.yml`. |
| **Pre-Commit Hooks** | Local checks ensuring code formatting and schema validation pre-push. | `.pre-commit-config.yaml`. |
| **Open Standards** | Non-proprietary, interoperable formats (JSON, CSV, GeoTIFF). | Ensures FAIR-compliant data practices. |
| **FAIR Data** | Findable, Accessible, Interoperable, Reusable data principles. | Underpins all KFM datasets. |
| **Audit Trail** | Historical record of CI/CD runs and validation logs. | `data/work/logs/`. |
| **Makefile** | Task automation framework for reproducible data builds. | Root of repository. |

---

## 🌎 Geospatial & Environmental Terms

| Term | Definition | Context |
|:------|:-------------|:----------|
| **DEM (Digital Elevation Model)** | Raster dataset representing elevation values. | Derived from LiDAR or USGS 3DEP. |
| **LiDAR (Light Detection and Ranging)** | Remote sensing method to capture terrain surfaces. | Source for Kansas elevation models. |
| **Raster** | Pixel-based geospatial dataset. | DEMs, hillshades, landcover. |
| **Vector** | Geometry-based geospatial dataset. | Roads, rivers, boundaries. |
| **COG (Cloud-Optimized GeoTIFF)** | GeoTIFF variant optimized for HTTP range requests. | Used for terrain and imagery layers. |
| **Map Tiles** | Tiled raster or vector images rendered for web maps. | MapLibre viewer. |
| **EPSG:4326 (WGS84)** | Common geospatial coordinate system. | Global standard for latitude/longitude. |
| **CRS (Coordinate Reference System)** | Defines how spatial data is projected. | Used in reprojecting datasets. |
| **Bounding Box (BBox)** | Rectangular spatial extent defined by min/max coordinates. | Used for dataset spatial queries. |

---

## 🧠 Knowledge Graph & Semantics

| Term | Definition | Context |
|:------|:-------------|:----------|
| **Entity** | Object in the graph (Person, Place, Event, Document). | Neo4j node type. |
| **Relationship** | Directed link connecting entities (e.g., OCCURRED_AT). | Neo4j relationship. |
| **Cypher** | Query language for Neo4j databases. | Used for event and place queries. |
| **Inference (Reasoning)** | Automated deduction of new relationships from known ones. | Implemented in `src/graph/reasoner.py`. |
| **JSON-LD** | JSON-based serialization for linked data. | Used for Knowledge Graph exports. |
| **Graph Schema** | Structural definition of node labels and relationships. | `src/graph/graph_schema.py`. |
| **Neo4j** | Graph database engine used for KFM semantic storage. | Backend of the knowledge layer. |

---

## ⚙️ CI/CD & Governance

| Term | Definition | Context |
|:------|:-------------|:----------|
| **GitHub Actions** | Workflow automation for build, test, and deploy. | `.github/workflows/`. |
| **Pre-Commit** | Linting and validation hooks run before committing. | Ensures data & schema compliance. |
| **Artifact** | Output produced by a build or validation pipeline. | `_site/`, `data/processed/`. |
| **Containerization** | Packaging app dependencies for consistent runtime. | `Dockerfile` and `compose.yml`. |
| **Trivy Scan** | Automated dependency and container vulnerability scan. | Security workflow. |
| **STAC Validation** | Schema validation ensuring all collections conform to spec. | `make validate`. |

---

## 🧱 Acronyms

| Acronym | Full Form | Description |
|:-----------|:-----------|:-------------|
| **KFM** | Kansas Frontier Matrix | The project repository and system. |
| **MCP** | Master Coder Protocol | Project’s reproducibility and documentation framework. |
| **STAC** | SpatioTemporal Asset Catalog | Open metadata standard for geospatial assets. |
| **ETL** | Extract, Transform, Load | Data ingestion and processing pattern. |
| **CI/CD** | Continuous Integration / Deployment | Automated testing and deployment. |
| **RDF** | Resource Description Framework | Data model for linked semantic data. |
| **COG** | Cloud-Optimized GeoTIFF | Raster format optimized for web delivery. |
| **NHD** | National Hydrography Dataset | Hydrology data (streams, rivers). |
| **WBD** | Watershed Boundary Dataset | Hydrologic boundary polygons. |
| **NOAA** | National Oceanic and Atmospheric Administration | Climate and weather data provider. |
| **USGS** | United States Geological Survey | Primary source of elevation and hydro data. |
| **USDA** | United States Department of Agriculture | Source of soils and landcover datasets. |
| **KSHS** | Kansas State Historical Society | Repository for archival historical materials. |

---

## 🔗 Cross-References

| Document | Description |
|:-----------|:-------------|
| [`docs/architecture/architecture.md`](architecture/architecture.md) | High-level system architecture overview. |
| [`docs/architecture/data-architecture.md`](architecture/data-architecture.md) | Data flow and lineage. |
| [`docs/architecture/knowledge-graph.md`](architecture/knowledge-graph.md) | Semantic and ontology design. |
| [`docs/architecture/pipelines.md`](architecture/pipelines.md) | ETL and AI pipeline documentation. |
| [`docs/standards/metadata-standards.md`](standards/metadata-standards.md) | Metadata and schema compliance guide. |

---

## 🧠 MCP Compliance Summary

| MCP Principle | Implementation |
|:--------------|:----------------|
| **Documentation-first** | All terms defined before implementation in code. |
| **Reproducibility** | Each term directly references reproducible components. |
| **Open Standards** | Terminology grounded in open data and schema standards. |
| **Provenance** | Each definition references a dataset, ontology, or workflow. |
| **Auditability** | Reviewed via CI/CD schema validation for consistency. |

---

## 🕰️ Version History

| Version | Date | Summary |
|:---------|:------|:----------|
| **v1.1** | 2025-10-05 | Expanded glossary with ontology, geospatial, and governance terms; improved formatting for GitHub rendering. |
| **v1.0** | 2025-10-04 | Initial release: MCP-aligned glossary covering architecture, data, and reproducibility concepts. |

---

<div align="center">

**Kansas Frontier Matrix** — *"Every Definition. Every Domain. Linked and Reproducible."*  
📍 [`docs/glossary.md`](.) · Canonical terminology reference for the Kansas Frontier Matrix documentation ecosystem.

</div>
