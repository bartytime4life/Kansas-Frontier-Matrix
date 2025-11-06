---
title: "📘 Kansas Frontier Matrix — Glossary & Terminology Index"
path: "docs/glossary.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../releases/v9.7.0/manifest.zip"
telemetry_ref: "../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/docs-glossary-v1.json"
governance_ref: "standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📘 **Kansas Frontier Matrix — Glossary & Terminology Index**
`docs/glossary.md`

**Purpose:** Provide a standardized vocabulary for contributors and researchers working within the Kansas Frontier Matrix (KFM) project.  
This glossary aligns with **Master Coder Protocol (MCP v6.3)**, **FAIR+CARE**, and **Platinum README Template v7.1**, ensuring consistent use of scientific, technical, and ethical terminology across all documentation.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 🧭 Overview

This glossary defines all major terms, acronyms, and frameworks used throughout the KFM monorepo.  
Each entry includes a concise definition and, where applicable, a reference to related KFM components, international standards, or ethical governance practices.

The glossary serves three main functions:
1. **Standardization:** Ensure consistent technical and academic language across all documents.  
2. **Traceability:** Link definitions to external standards like STAC, DCAT, CIDOC CRM, and OWL-Time.  
3. **Governance:** Provide clear definitions for ethical and Indigenous data stewardship terminology in FAIR+CARE contexts.

---

## 📚 Core Terms

| Term | Definition | Related Components |
|------|-------------|--------------------|
| **KFM (Kansas Frontier Matrix)** | The open-source, FAIR+CARE-certified geospatial–historical knowledge hub integrating Kansas’s environmental, cultural, and historical data. | Entire monorepo |
| **MCP (Master Coder Protocol)** | A documentation-first software development protocol emphasizing reproducibility, transparency, and open standards. | Docs, pipelines, governance |
| **FAIR Principles** | Data management guidelines ensuring information is Findable, Accessible, Interoperable, and Reusable. | Validation pipelines, governance |
| **CARE Principles** | Ethical framework for Indigenous and community data governance emphasizing Collective Benefit, Authority to Control, Responsibility, and Ethics. | FAIR+CARE validator, governance council |
| **STAC (SpatioTemporal Asset Catalog)** | An OGC community standard for describing and indexing geospatial data assets in JSON format. | `data/stac/`, `stac-validate.yml` |
| **DCAT (Data Catalog Vocabulary)** | A W3C standard for dataset metadata and discovery in RDF/JSON-LD. Used for FAIR+CARE catalog interoperability. | Metadata bridge (`stac-dcat-bridge.yml`) |
| **CIDOC CRM (Conceptual Reference Model)** | ISO 21127 ontology for cultural heritage information, providing semantic structure for historical data. | `src/graph/schema/`, Neo4j graph |
| **OWL-Time** | W3C ontology describing temporal intervals and instants for event-based data. | Knowledge graph, temporal metadata |
| **GeoJSON / GeoTIFF** | Open geospatial data formats used for vector and raster assets respectively. | `data/processed/`, `web/MapView` |
| **COG (Cloud-Optimized GeoTIFF)** | A GeoTIFF variant optimized for tiled web access and scalable map serving. | ETL pipeline, `rio-cogeo` processing |
| **STAC Item** | A JSON file describing a single geospatial dataset or asset, including geometry, time, and metadata. | `data/stac/items/` |
| **STAC Collection** | A container grouping related STAC Items with shared properties like temporal extent and license. | `data/stac/collections/` |
| **ETL (Extract, Transform, Load)** | Data pipeline process that retrieves, standardizes, and loads data into structured repositories. | `src/pipelines/etl/` |
| **Knowledge Graph** | A Neo4j-based graph storing relationships between entities (People, Places, Events, Documents). | `src/graph/` |
| **Focus Mode** | AI-assisted system that dynamically filters and summarizes data centered on a specific entity or topic. | `src/ai/models/focus_transformer_v1/` |
| **AI Explainability** | Transparent reporting of AI model decisions using SHAP or LIME techniques. | `src/ai/explainability/` |
| **Telemetry** | Automated system metrics capturing validation, workflow results, and performance data. | `releases/v9.7.0/focus-telemetry.json` |
| **Governance Ledger** | Immutable audit log tracking validation and FAIR+CARE compliance events. | `reports/audit/` |

---

## ⚖ Governance & Ethical Terms

| Term | Definition | Reference |
|------|-------------|------------|
| **Ethical Data Stewardship** | The practice of managing data with transparency, respect, and community benefit in mind. | FAIR+CARE |
| **Data Provenance** | Metadata describing the origin, transformations, and history of a dataset. | `data/sources/*.json` |
| **Indigenous Data Sovereignty** | The right of Indigenous peoples to govern the collection, ownership, and application of their data. | CARE principles |
| **Cultural Sensitivity Review** | A governance process ensuring datasets containing Indigenous or cultural information are ethically shared. | `governance_form.yml` |
| **Open Data License** | A public license permitting use, reuse, and redistribution of datasets, e.g., CC-BY, CC0, or Public Domain. | FAIR compliance |
| **Governance Council** | A group of KFM contributors responsible for ethical review, policy enforcement, and CARE evaluations. | Governance charter |

---

## 🧮 Technical & Pipeline Terms

| Term | Definition | Reference |
|------|-------------|------------|
| **SBOM (Software Bill of Materials)** | SPDX-compliant manifest listing all software dependencies and licenses. | `releases/v9.7.0/sbom.spdx.json` |
| **CI/CD (Continuous Integration/Continuous Deployment)** | Automated validation, testing, and deployment workflows managed by GitHub Actions. | `.github/workflows/` |
| **Pre-Commit Hooks** | Local validation scripts ensuring all commits meet syntax and metadata standards before push. | `.pre-commit-config.yaml` |
| **DVC (Data Version Control)** | Git-compatible system for managing large datasets and versioned data artifacts. | `data/raw/`, `data/processed/` |
| **SPDX (Software Package Data Exchange)** | Open standard for communicating software bill of materials and license data. | `sbom_ref` |
| **SLSA (Supply-chain Levels for Software Artifacts)** | Framework for secure, auditable software supply chain practices. | CI/CD release attestation |
| **Manifest** | JSON or ZIP file summarizing version metadata and checksums for a release. | `manifest_ref` |
| **Checksum (SHA-256)** | Cryptographic hash ensuring data integrity and immutability. | `data/sources/*.json` |
| **FAIR+CARE Validator** | Python-based automated audit ensuring datasets meet FAIR and CARE criteria. | `faircare-validate.yml` |
| **Telemetry Dashboard** | Governance dashboard visualizing validation, compliance, and performance metrics. | Web Admin Console |

---

## 🧠 AI & Semantic Frameworks

| Term | Definition | Related Component |
|------|-------------|-------------------|
| **NER (Named Entity Recognition)** | NLP technique used to identify names of people, places, and organizations in text. | `src/ai/models/` |
| **Embedding Model** | Neural model producing vectorized representations of text for semantic search and entity linking. | `src/ai/models/embeddings/` |
| **Transformers** | Deep learning architecture used for NLP tasks (e.g., summarization, classification). | `focus_transformer_v1` |
| **SHAP (SHapley Additive exPlanations)** | Explainability technique quantifying feature importance in AI models. | `src/ai/explainability/` |
| **LIME (Local Interpretable Model-agnostic Explanations)** | Model-agnostic technique for understanding black-box predictions. | `src/ai/explainability/` |
| **Cypher Query** | Neo4j’s declarative graph query language used for managing entities and relationships. | `src/graph/queries/` |

---

## 🗺 Data & Geospatial Vocabulary

| Term | Definition | Related Usage |
|------|-------------|----------------|
| **Bounding Box (BBox)** | Rectangular coordinates `[west, south, east, north]` defining dataset extent. | STAC Items |
| **Projection (CRS)** | Coordinate reference system used for spatial data (e.g., EPSG:4326 WGS84). | All geospatial data |
| **LiDAR (Light Detection and Ranging)** | Remote sensing method using laser pulses to measure topography. | Elevation datasets |
| **Raster** | Gridded data (e.g., imagery, DEM, heatmaps) represented as pixels. | GeoTIFF, COG |
| **Vector** | Geospatial features represented as points, lines, or polygons. | GeoJSON, shapefiles |
| **DEM (Digital Elevation Model)** | Surface model representing elevation data. | `data/processed/climate/` |
| **Hydrography** | Mapping of surface water features (rivers, lakes, basins). | USGS, NHD datasets |
| **Topology** | Spatial relationships between geospatial entities (e.g., adjacency, containment). | Graph layer, GeoSPARQL |

---

## 🕰 Temporal & Historical Context

| Term | Definition | Reference |
|------|-------------|------------|
| **PeriodO** | Linked data gazetteer of historical periods used for tagging events and datasets with time ranges. | Temporal ontology alignment |
| **Timeline Slider** | Interactive UI element allowing exploration of temporal datasets. | Web UI / React TimelineView |
| **Temporal Extent** | The time range represented by a dataset (start and end dates). | STAC metadata |
| **Event Node** | Knowledge graph entity representing an occurrence with time, place, and participants. | `src/graph/schema/` |
| **Historical Layer** | Map overlay or dataset representing a specific time period (e.g., 1850s, 1930s). | `web/public/maps/` |

---

## 🔗 Cross-Standard References

| Standard | Governing Body | KFM Usage |
|-----------|----------------|-----------|
| **STAC 1.0.0** | OGC / Radiant Earth Foundation | Data cataloging and validation |
| **DCAT 3.0** | W3C | Metadata interoperability |
| **CIDOC CRM ISO 21127** | ICOM / ISO | Knowledge graph ontology |
| **OWL-Time** | W3C | Temporal relationships in event data |
| **GeoSPARQL 1.1** | OGC | Spatial reasoning within graph data |
| **SPDX 2.3** | Linux Foundation | SBOM and license tracking |
| **SLSA 1.0** | OpenSSF | Provenance and supply chain integrity |

---

## 🕰 Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Created comprehensive glossary for technical, ethical, and semantic terms. |
| v9.5.0 | 2025-10-20 | A. Barta | Added FAIR+CARE and ontology-related vocabulary. |
| v9.3.0 | 2025-08-12 | KFM Core Team | Expanded technical and pipeline terminology. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Initial glossary framework created. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Return to Documentation Index](README.md) · [View Governance Charter](standards/governance/ROOT-GOVERNANCE.md)

</div>
