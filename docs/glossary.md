---
title: "📘 Kansas Frontier Matrix — Glossary & Terminology Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/glossary.md"
version: "v11.0.0"
last_updated: "2025-11-18"

review_cycle: "Annual / FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"

sbom_ref: "../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../releases/v11.0.0/manifest.zip"
telemetry_ref: "../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/docs-glossary-v4.json"

governance_ref: "standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "terminology-index"
role: "glossary"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed Dataset Classification"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Documentation"
redaction_required: false

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "DefinedTermSet"
  owl_time: "Instant"
  prov_o: "prov:Collection"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../schemas/json/docs-glossary-v11.schema.json"
shape_schema_ref: "../schemas/shacl/docs-glossary-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:glossary-v11.0.0"
semantic_document_id: "kfm-docs-glossary"
event_source_id: "ledger:docs/glossary.md"
immutability_status: "mutable-plan"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next glossary-wide terminology update"
---

<div align="center">

# 📘 **Kansas Frontier Matrix — Glossary & Terminology Index**  
`docs/glossary.md`

**Status:** Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

**Purpose**  
Provide a standardized, machine-parseable vocabulary for contributors and researchers working within the Kansas Frontier Matrix (KFM).  
Aligned with **MCP-DL v6.3**, **KFM-MDP v11.0.0**, **FAIR+CARE**, **STAC/DCAT**, **CIDOC-CRM**, **OWL-Time**, and **GeoSPARQL** to ensure consistent terminology across documentation, APIs, pipelines, and Story Nodes.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue)](standards/kfm_markdown_protocol_v11.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY_4.0-green)](../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](standards/faircare.md)  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](#-version-history)

</div>

---

## 📘 Overview

This glossary defines key **technical**, **governance**, **security**, **geospatial**, and **domain-specific** terms used throughout the KFM monorepo.

Each entry aims to include:

- A concise, implementation-ready **definition**  
- **Related components** (directories, modules, or key docs)  
- Links or references to **internal standards** or **external specifications**  

When adding or editing a term:

- Use a **clear, neutral, concise** definition  
- Reference the most relevant **directory or document**  
- Avoid project-internal jargon where an existing standard term exists  
- Respect **FAIR+CARE** and Indigenous data sovereignty in any domain description  

---

## 📚 Core Project Terms

| Term | Definition | Related Components |
|------|-----------|--------------------|
| **KFM (Kansas Frontier Matrix)** | A semantic, FAIR+CARE-aligned geospatial–historical knowledge hub for Kansas, integrating maps, timelines, Story Nodes, and AI-assisted narratives. | Entire monorepo |
| **MCP (Master Coder Protocol)** | Documentation-first engineering protocol that requires design docs, provenance, and validation before code is accepted. | `docs/standards/`, `.github/` |
| **KFM-MDP (Markdown Protocol)** | Project-wide ruleset for YAML front-matter, headings, fences, emoji bars, and CI-safe markdown structure. | `docs/standards/kfm_markdown_protocol_v11.md` |
| **FAIR Principles** | Data principles: Findable, Accessible, Interoperable, Reusable. Used to evaluate datasets and metadata. | Validation pipelines, `docs/standards/faircare.md` |
| **CARE Principles** | Indigenous data governance framework: Collective Benefit, Authority to Control, Responsibility, Ethics. | FAIR+CARE validator, governance council |
| **Focus Mode** | AI-assisted, entity-centric interface that synchronizes map, timeline, and narrative insights while enforcing provenance, explainability, and CARE constraints. | `web/`, `src/ai/`, `docs/architecture/` |
| **Story Node** | A narrative unit representing a curated story with spatial footprint, temporal span, and linked entities/documents, backed by graph data and STAC/DCAT metadata. | `docs/architecture/`, `docs/analyses/`, `schemas/` |

---

## ⚙️ Technical & Pipeline Vocabulary

| Term | Definition | Reference |
|------|------------|-----------|
| **ETL (Extract–Transform–Load)** | Pipeline stages that ingest raw data, normalize and enrich it, then load it into storage or the knowledge graph. | `src/pipelines/etl/` |
| **Knowledge Graph** | Neo4j-backed semantic graph of entities, relationships, and events, modeled with CIDOC-CRM, OWL-Time, GeoSPARQL, and PROV-O. | `src/graph/`, `docs/architecture/` |
| **SBOM (Software Bill of Materials)** | SPDX/CycloneDX list of software components, versions, and licenses used in a build or release. | `releases/*/sbom.spdx.json` |
| **Telemetry** | Structured metrics about builds, pipelines, AI performance, accessibility, energy, and governance exported to JSON. | `releases/*/focus-telemetry.json` |
| **SLSA** | Supply-chain Levels for Software Artifacts; guidance for build provenance and integrity. | `.github/workflows/`, `docs/architecture/` |
| **Checksum (SHA-256)** | Cryptographic hash used to verify integrity of files, datasets, and releases. | `data/checksums/`, `releases/*/manifest.zip` |
| **STAC/DCAT Bridge** | Mapping layer that keeps STAC Items/Collections and DCAT Datasets semantically aligned. | `docs/architecture/data-architecture.md` |
| **LangGraph** | DAG-based orchestration layer for multi-step AI and ETL flows. | `src/agents/`, `src/pipelines/` |
| **MCP Server** | Service exposing internal tools (e.g., Neo4j, STAC, GDAL) to AI frameworks through standardized tool interfaces. | `docs/architecture/api-architecture.md` |
| **Write-Ahead Log (WAL)** | Append-only log of transformations and promotions, used for reproducibility, rollback, and audits. | `docs/pipelines/reliable-pipelines.md` |

---

## 🛡️ Security & Governance Terms

| Term | Definition | Related Components |
|------|------------|--------------------|
| **Prompt Injection Defense** | Controls that prevent user-provided text from overriding system policies (e.g., strict tool allowlists, schema-bound prompts). | `docs/security/prompt-injection-defense.md`, `.github/` |
| **Threat Modeling (STRIDE / LINDDUN)** | Structured methods to identify security (STRIDE) and privacy (LINDDUN) risks for system components. | `docs/security/threat-model.md` |
| **Secrets Policy (ZTA)** | Zero-Trust approach for managing credentials: no secrets in repo, use KMS/Vault, rotation, and audits. | `docs/security/secrets-policy.md` |
| **Supply Chain Security** | Practices to secure build and dependency chain: SLSA, SBOMs, signatures, and pinned versions. | `docs/security/supply-chain.md`, `.github/` |
| **Incident Response (IR)** | Process for detecting, triaging, and resolving security/privacy incidents, aligned with NIST 800-61 / ISO 27035. | `docs/security/incident-response.md` |
| **CARE Tag** | Categorical label applied to datasets or nodes indicating governance status: `public`, `restricted`, or `sensitive`. | Graph properties, STAC/DCAT metadata |
| **Governance Ledger** | Append-only record of governance decisions, reviews, and audits related to datasets, models, and narratives. | `docs/reports/audit/`, `docs/standards/governance/` |
| **Public Document** | A document classified as suitable for general public release, usually licensed CC-BY or MIT. | YAML front-matter `classification` field |

---

## 🧠 AI & Semantic Frameworks

| Term | Definition | Related Component |
|------|------------|-------------------|
| **NER (Named Entity Recognition)** | NLP task that extracts labeled entities (e.g., PERSON, PLACE, ORG) from text. | `src/ai/models/`, `src/pipelines/` |
| **Transformers** | Deep learning architectures used for tasks like summarization, classification, and generation. | `src/ai/models/*` |
| **Embedding Model** | Model that converts text or features into dense vectors for similarity search and clustering. | `src/ai/models/embeddings/` |
| **SHAP** | Explainability method showing feature contributions to model predictions. | `src/ai/explainability/` |
| **LIME** | Local interpretable model-agnostic explanation method for predictions. | `src/ai/explainability/` |
| **Cypher** | Query language used to interact with the Neo4j knowledge graph. | `src/graph/queries/` |
| **Focus Transformer** | Specialized model (or model stack) tuned to generate Focus Mode narratives and summaries from graph context. | `src/ai/models/focus_transformer_v*/` |
| **Hallucination Guardrail** | Set of checks ensuring AI output is grounded in actual data and sources, rejecting unverifiable statements. | `docs/pipelines/validation-observability/`, `src/ai/` |

---

## 🗺 Geospatial & Historical Terms

| Term | Definition | Related Usage |
|------|------------|---------------|
| **BBox (Bounding Box)** | Four-value array `[west, south, east, north]` in WGS84 (EPSG:4326) representing a rectangular spatial extent. | STAC Items, GeoJSON |
| **CRS (Coordinate Reference System)** | Formal description of how spatial coordinates map to positions on Earth; typically an EPSG code. | All geodata, STAC |
| **COG (Cloud-Optimized GeoTIFF)** | GeoTIFF structure optimized for HTTP range requests and web tiling. | `data/processed/rasters/` |
| **GeoJSON / GeoTIFF** | Open formats for vector (GeoJSON) and raster (GeoTIFF) geospatial data. | Processed layers, STAC assets |
| **DEM (Digital Elevation Model)** | Raster dataset representing terrain elevation. | Terrain layers, 3D visualization |
| **Hydrography** | Representation of water features such as rivers, lakes, and basins. | Hydrology analyses, `data/sources/hydrology/` |
| **H3 Index** | Hexagonal hierarchical spatial index used for generalization/masking of sensitive locations. | Sensitive sites, CARE masking |
| **DCAT JSON-LD** | JSON-LD encoding of DCAT dataset metadata, enabling linked data integration. | Catalog exports, `docs/data/` |
| **Temporal Interval** | Time span defined by a start and end instant, aligned with OWL-Time. | Graph events, timeline UI |

---

## 🔗 Cross-Standard References

| Standard       | Governing Body     | KFM Usage                                  |
|----------------|--------------------|--------------------------------------------|
| **STAC 1.x**   | OGC / Radiant Earth | Cataloging geospatial assets            |
| **DCAT 3.0**   | W3C                | Dataset metadata and catalogs             |
| **CIDOC-CRM**  | ICOM / ISO         | Cultural heritage entity & event modeling |
| **OWL-Time**   | W3C                | Temporal instants and intervals           |
| **GeoSPARQL 1.1** | OGC             | Spatial relationships in the knowledge graph |
| **PROV-O**     | W3C                | Provenance modeling for entities and activities |
| **SPDX 2.3**   | Linux Foundation   | Software bill of materials (SBOM)         |
| **CycloneDX**  | OWASP              | Alternative SBOM format for security tools |

---

## 🧩 Controlled Vocabulary (Selected Fields)

Use these controlled values in front-matter and metadata to reduce ambiguity:

| Field        | Allowed Values                                | Notes                                   |
|--------------|-----------------------------------------------|-----------------------------------------|
| `care_label` | `Public` · `Restricted` · `Sensitive`         | High-level CARE classification          |
| `classification` | `Public Document` · `Internal` · `Restricted` | Document exposure status            |
| `lifecycle_stage` | `draft` · `stable` · `deprecated`       | Lifecycle flag for docs and schemas     |
| `stac:stage` | `raw` · `work` · `staging` · `processed` · `archive` | Data lifecycle in KFM pipelines |
| `license`    | `CC-BY-4.0` · `MIT` · `ODbL-1.0` · `Public-Domain` | Prefer standard SPDX-compatible IDs |
| `crs`        | `EPSG:4326` (default)                         | Other CRS require explicit documentation |
| `a11y.level` | `AA` · `AAA`                                  | Target WCAG conformance level           |

---

## 🧭 Usage Guidelines

When you introduce new terminology:

1. **Check first** whether a similar term already exists.  
2. Prefer **existing standards** (e.g., CIDOC-CRM, DCAT, STAC) rather than inventing new labels.  
3. Keep definitions **short, neutral, and implementation-friendly**.  
4. Include at least one **Related Component** or **Reference** so others can find practical usage.  
5. If a term relates to Indigenous knowledge, governance, or sensitive heritage, ensure it is reviewed in line with **CARE** and relevant community guidance.

---

## 🕰️ Version History

| Version  | Date         | Author        | Summary                                                                                           |
|---------:|-------------:|--------------|---------------------------------------------------------------------------------------------------|
| v11.0.0  | 2025-11-18   | KFM Docs Team | Upgraded to KFM-MDP v11; expanded ontology fields, security terms, H3, and controlled vocabulary. |
| v10.3.1  | 2025-11-13   | KFM Docs Team | Updated release paths to v10.3.0; added LangGraph, MCP server, and governance entries.           |
| v10.2.4  | 2025-11-12   | KFM Docs Team | Added controlled vocabulary table; checksum reference path updated.                              |
| v10.2.3  | 2025-11-09   | KFM Docs Team | Added security suite terms, STAC/DCAT bridge entry, telemetry schema v3.                         |
| v9.7.0   | 2025-11-05   | A. Barta      | Comprehensive glossary aligned to MCP v6.3 and FAIR+CARE.                                        |
| v9.5.0   | 2025-10-20   | A. Barta      | Added ontology and governance terminology.                                                       |
| v9.3.0   | 2025-08-12   | KFM Core Team | Expanded technical and pipeline entries.                                                         |
| v9.0.0   | 2025-06-01   | KFM Core Team | Initial glossary framework.                                                                      |

---

<div align="center">

**Kansas Frontier Matrix — Glossary & Terminology Index v11**  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Documentation Hub](README.md) · [Back to Standards](standards/README.md) · [Back to Repository Root](../README.md)

</div>