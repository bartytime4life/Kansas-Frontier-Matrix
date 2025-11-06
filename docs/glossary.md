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

**Purpose:** Provide a standardized vocabulary for contributors and researchers working within the Kansas Frontier Matrix (KFM).  
This glossary aligns with **MCP v6.3**, **FAIR+CARE**, and **Platinum README v7.1** to ensure consistent, machine-parseable terminology across all documentation.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

This glossary defines key **technical**, **governance**, and **domain** terms used throughout the KFM monorepo.  
Each entry provides a concise definition and cross-references related documentation or standards for traceability.

> When adding new terms, include a clear definition, the **related component** (file or folder), and — when applicable — a reference to an external standard (e.g., STAC, DCAT, CIDOC CRM).

---

## 📚 Core Terms

| Term | Definition | Related Components |
|------|-----------|--------------------|
| **KFM (Kansas Frontier Matrix)** | FAIR+CARE-certified, open geospatial–historical knowledge hub for Kansas. | Entire monorepo |
| **MCP (Master Coder Protocol)** | Documentation-first protocol enabling reproducibility and auditability. | Docs, pipelines, governance |
| **FAIR Principles** | Findable, Accessible, Interoperable, Reusable data framework. | Validation pipelines, governance |
| **CARE Principles** | Ethical framework: Collective Benefit, Authority, Responsibility, Ethics. | FAIR+CARE validator, governance council |
| **STAC (SpatioTemporal Asset Catalog)** | JSON spec for spatio-temporal assets enabling catalog discovery. | `data/stac/`, `stac-validate.yml` |
| **DCAT (Data Catalog Vocabulary)** | W3C vocabulary for dataset metadata & discovery (RDF/JSON-LD). | STAC↔DCAT bridge |

---

## ⚙️ Technical & Pipeline Vocabulary

| Term | Definition | Reference |
|------|------------|-----------|
| **ETL** | Extract, Transform, Load pipeline stages. | `src/pipelines/etl/` |
| **Knowledge Graph** | Neo4j-based semantic graph of entities and relations. | `src/graph/` |
| **SBOM (Software Bill of Materials)** | SPDX inventory of packages, versions, and licenses. | `../releases/v9.7.0/sbom.spdx.json` |
| **Telemetry** | Build/validation metrics exported to a single JSON. | `../releases/v9.7.0/focus-telemetry.json` |
| **DVC** | Data Version Control for large datasets and artifacts. | `data/raw/`, `data/processed/` |
| **SLSA** | Supply-chain Levels for Software Artifacts provenance. | CI/CD release attestation |
| **Checksum (SHA-256)** | Cryptographic hash verifying integrity of artifacts. | `data/sources/*.json` |

---

## 🧠 AI & Semantic Frameworks

| Term | Definition | Related Component |
|------|------------|-------------------|
| **NER** | Named Entity Recognition for People/Places/Orgs. | `src/ai/models/` |
| **Transformers** | Deep learning models for NLP tasks (e.g., summarization). | `src/ai/models/*` |
| **Embedding Model** | Vector representations for semantic search and linking. | `src/ai/models/embeddings/` |
| **SHAP** | Explainability method for feature contribution. | `src/ai/explainability/` |
| **LIME** | Local interpretable explanations for model predictions. | `src/ai/explainability/` |
| **Cypher** | Query language for Neo4j graphs. | `src/graph/queries/` |

---

## 🗺 Geospatial & Historical Terms

| Term | Definition | Related Usage |
|------|------------|---------------|
| **BBox (Bounding Box)** | `[west, south, east, north]` spatial extent (WGS84). | STAC Items |
| **CRS (Projection)** | Coordinate Reference System (e.g., EPSG:4326). | All geodata |
| **COG** | Cloud-Optimized GeoTIFF for tiled web access. | ETL rasters |
| **GeoJSON / GeoTIFF** | Open formats for vector/raster geodata. | Processed layers |
| **DEM** | Digital Elevation Model for terrain. | `data/processed/**` |
| **Hydrography** | Rivers, lakes, basins networks. | USGS/NHD data |

---

## ⚖️ Governance & Ethics

| Term | Definition | Reference |
|------|------------|-----------|
| **Governance Ledger** | Immutable log of FAIR+CARE decisions and events. | `reports/audit/` |
| **Ethical Data Stewardship** | Managing data with transparency and community benefit. | `standards/faircare.md` |
| **Indigenous Data Sovereignty** | Indigenous governance over data use and access. | `standards/faircare.md` |
| **Cultural Sensitivity Review** | Process ensuring ethical sharing of sensitive data. | `.github/ISSUE_TEMPLATE/governance_form.yml` |

---

## 🔗 Cross-Standard References

| Standard | Governing Body | KFM Usage |
|----------|----------------|-----------|
| **STAC 1.0.0** | OGC / Radiant Earth | Cataloging geospatial assets |
| **DCAT 3.0** | W3C | Dataset metadata interoperability |
| **CIDOC CRM** | ICOM / ISO | Cultural heritage entity modeling |
| **OWL-Time** | W3C | Temporal intervals and instants |
| **GeoSPARQL 1.1** | OGC | Spatial reasoning in graphs |
| **SPDX 2.3** | Linux Foundation | Software bill of materials |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Comprehensive glossary created; aligned to MCP v6.3 and FAIR+CARE. |
| v9.5.0 | 2025-10-20 | A. Barta | Added ontology and governance terminology. |
| v9.3.0 | 2025-08-12 | KFM Core Team | Expanded technical and pipeline entries. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Initial glossary framework. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Documentation Index](README.md) · [Governance Charter](standards/governance/ROOT-GOVERNANCE.md)

</div>