---
title: "📘 Kansas Frontier Matrix — Glossary & Terminology Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/glossary.md"
version: "v10.2.3"
last_updated: "2025-11-09"
review_cycle: "Annual / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../releases/v10.2.0/manifest.zip"
telemetry_ref: "../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/docs-glossary-v3.json"
governance_ref: "standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📘 **Kansas Frontier Matrix — Glossary & Terminology Index**
`docs/glossary.md`

**Purpose:** Provide a standardized, machine-parseable vocabulary for contributors and researchers working within the Kansas Frontier Matrix (KFM).  
Aligned with **MCP v6.3**, **FAIR+CARE**, **Platinum README v7.1**, **STAC/DCAT**, and **CIDOC CRM** to ensure consistent terminology across all documentation and APIs.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()
</div>

---

## 📘 Overview

This glossary defines key **technical**, **governance**, **security**, and **domain** terms used throughout the KFM monorepo.  
Each entry includes a concise definition, cross-references to related docs, and (when relevant) links to external standards.

> When adding a term, include: a clear definition, **related component(s)**, and a reference to an internal doc or external standard.

---

## 📚 Core Terms

| Term | Definition | Related Components |
|------|-----------|--------------------|
| **KFM (Kansas Frontier Matrix)** | FAIR+CARE-certified, open geospatial–historical knowledge hub for Kansas. | Entire monorepo |
| **MCP (Master Coder Protocol)** | Documentation-first protocol enabling reproducibility and auditability across modules. | Docs, pipelines, governance |
| **FAIR Principles** | Findable, Accessible, Interoperable, Reusable data framework. | Validation pipelines, governance |
| **CARE Principles** | Ethical framework: Collective Benefit, Authority, Responsibility, Ethics. | FAIR+CARE validator, governance council |
| **Focus Mode** | AI-assisted, entity-centric view that synchronizes map, timeline, and narrative insights with explainability and governance. | Web/UI, API, AI |

---

## ⚙️ Technical & Pipeline Vocabulary

| Term | Definition | Reference |
|------|------------|-----------|
| **ETL** | Extract, Transform, Load pipeline stages. | `src/pipelines/etl/` |
| **Knowledge Graph** | Neo4j-based semantic graph of entities and relations. | `src/graph/` |
| **SBOM (Software Bill of Materials)** | SPDX/CycloneDX inventory of packages, versions, and licenses. | `../releases/*/sbom.spdx.json` |
| **Telemetry** | Build/validation metrics exported to a unified JSON. | `../releases/*/focus-telemetry.json` |
| **SLSA** | Supply-chain Levels for Software Artifacts provenance attestations. | CI/CD release workflows |
| **Checksum (SHA-256)** | Cryptographic hash verifying integrity of artifacts and datasets. | `data/sources/*.json` |
| **STAC/DCAT Bridge** | Mappings and validators for STAC Items ↔ DCAT Datasets. | `docs/architecture/data-architecture.md` |

---

## 🛡️ Security & Governance Terms

| Term | Definition | Related Components |
|------|------------|--------------------|
| **Prompt Injection Defense** | Controls preventing instruction smuggling and context poisoning (signed prompts, sanitizer, allowlist). | `docs/security/prompt-injection-defense.md` |
| **Threat Modeling (STRIDE/LINDDUN)** | Methodologies for security/privacy risk identification and mitigation. | `docs/security/threat-model.md` |
| **Secrets Policy (ZTA)** | Zero-Trust secrets lifecycle: KMS/Vault, rotation, audit trails. | `docs/security/secrets-policy.md` |
| **Supply Chain Security** | SLSA, SBOMs, and Sigstore/Cosign signatures for provenance. | `docs/security/supply-chain.md` |
| **Incident Response (IR)** | NIST 800-61/ISO 27035-aligned detection, containment, and recovery. | `docs/security/incident-response.md` |
| **CARE Tag** | Dataset governance label: `public`, `restricted`, or `sensitive`. | Graph properties, STAC/DCAT metadata |

---

## 🧠 AI & Semantic Frameworks

| Term | Definition | Related Component |
|------|------------|-------------------|
| **NER** | Named Entity Recognition for People/Places/Orgs. | `src/ai/models/` |
| **Transformers** | Foundation models for NLP tasks (e.g., summarization). | `src/ai/models/*` |
| **Embedding Model** | Vector representations for semantic search and linking. | `src/ai/models/embeddings/` |
| **SHAP** | Explainability method for feature contribution. | `src/ai/explainability/` |
| **LIME** | Local interpretable explanations for model predictions. | `src/ai/explainability/` |
| **Cypher** | Query language for Neo4j graphs. | `src/graph/queries/` |
| **Story Node** | Narrative unit linking text, geospatial footprint, and time; STAC/DCAT/CIDOC-aligned. | `docs/architecture/data-architecture.md` |

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
| **DCAT JSON-LD** | Dataset metadata representation for linked data. | Catalog export |

---

## 🔗 Cross-Standard References

| Standard | Governing Body | KFM Usage |
|----------|----------------|-----------|
| **STAC 1.0.0** | OGC / Radiant Earth | Cataloging geospatial assets |
| **DCAT 3.0** | W3C | Dataset metadata interoperability |
| **CIDOC CRM** | ICOM / ISO | Cultural heritage entity modeling |
| **OWL-Time** | W3C | Temporal intervals and instants |
| **GeoSPARQL 1.1** | OGC | Spatial reasoning in graphs |
| **SPDX 2.3 / CycloneDX** | Linux Foundation / OWASP | Software bill of materials |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.2.3 | 2025-11-09 | KFM Docs Team | Aligned to v10.2: added security suite terms, STAC/DCAT bridge entry, and telemetry schema v3. |
| v9.7.0  | 2025-11-05 | A. Barta | Comprehensive glossary aligned to MCP v6.3 and FAIR+CARE. |
| v9.5.0  | 2025-10-20 | A. Barta | Added ontology and governance terminology. |
| v9.3.0  | 2025-08-12 | KFM Core Team | Expanded technical and pipeline entries. |
| v9.0.0  | 2025-06-01 | KFM Core Team | Initial glossary framework. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Documentation Index](README.md) · [Governance Charter](standards/governance/ROOT-GOVERNANCE.md)

</div>
