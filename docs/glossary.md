---
title: "📘 Kansas Frontier Matrix — Glossary & Terminology Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/glossary.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "terminology-index"
role: "glossary"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../releases/v11.2.6/signature.sig"
attestation_ref: "../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../releases/v11.2.6/manifest.zip"
telemetry_ref: "../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/docs-glossary-v4.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed Dataset Classification"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public Document"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
risk_category: "Documentation"
redaction_required: false

data_steward: "KFM FAIR+CARE Council"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next glossary-wide terminology update"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "DefinedTermSet"
  owl_time: "Instant"
  prov_o: "prov:Collection"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/glossary.md@v11.2.6"
  - "docs/glossary.md@v11.0.1"
  - "docs/glossary.md@v11.0.0"
  - "docs/glossary.md@v10.3.1"
  - "docs/glossary.md@v10.2.4"
  - "docs/glossary.md@v10.2.3"
  - "docs/glossary.md@v9.7.0"
  - "docs/glossary.md@v9.5.0"
  - "docs/glossary.md@v9.3.0"
  - "docs/glossary.md@v9.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../schemas/json/docs-glossary-v11.schema.json"
shape_schema_ref: "../schemas/shacl/docs-glossary-v11-shape.ttl"
story_node_refs: []

immutability_status: "mutable-plan"

doc_uuid: "urn:kfm:doc:glossary:v11.2.6"
semantic_document_id: "kfm-docs-glossary-v11.2.6"
event_source_id: "ledger:kfm:doc:glossary:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧭 Context"
    - "📦 Data & Metadata"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: false
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# 📘 **Kansas Frontier Matrix — Glossary & Terminology Index**  
`docs/glossary.md`

**Status:** Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

**Purpose**  
Provide a standardized, machine-parseable vocabulary for contributors and researchers working within the Kansas Frontier Matrix (KFM).  
Aligned with **MCP-DL v6.3**, **KFM-MDP v11.2.6**, **FAIR+CARE**, **STAC/DCAT**, **CIDOC-CRM**, **OWL-Time**, and **GeoSPARQL** to ensure consistent terminology across documentation, APIs, pipelines, and Story Nodes.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue)](standards/kfm_markdown_protocol_v11.2.6.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY_4.0-green)](../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](standards/faircare/FAIRCARE-GUIDE.md)  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](#-version-history)

</div>

---

## 📘 Overview

This glossary defines key **technical**, **governance**, **geospatial**, **heritage**, and **AI/semantic** terms used throughout the KFM monorepo.

Each entry aims to include:

- A concise, implementation-ready **definition**  
- **Related components** (directories, modules, or key docs)  
- Links or references to **internal standards** or **external specifications**

Usage rules:

- Prefer **existing standards** (CIDOC-CRM, DCAT, STAC, PROV-O, OWL-Time, GeoSPARQL) before inventing new terms.  
- Keep definitions **neutral and specific** to implementation or governance behavior.  
- When a term touches Indigenous knowledge or heritage, ensure it is consistent with **FAIR+CARE** and sovereignty policies.  
- Treat this glossary as the **authoritative vocabulary** for new docs, schemas, and APIs.

---

## 🧭 Context

The glossary is:

- The **root terminology index** for all documentation in `docs/`, including:
  - Standards (`docs/standards/`)  
  - Architecture (`docs/architecture/`)  
  - Pipelines (`docs/pipelines/`)  
  - Heritage/H3 masking (`docs/standards/heritage/`)  
  - Story Nodes / Focus Mode (`docs/architecture/story_nodes/`, etc.)  

- A **bridge** between:
  - Internal naming (e.g., “Autonomy Matrix”, “Focus Mode”)  
  - External standards (STAC/DCAT, CIDOC-CRM, OWL-Time, GeoSPARQL, PROV-O)

- A key input to:
  - **KFM-MDP** linting (checking for unknown or inconsistent terms).  
  - **Focus Mode** semantic highlighting and entity linking.  
  - **Schema design** (JSON/SHACL) for new KFM components.

When in doubt about a term’s meaning or allowed variants, check here first.

---

## 📦 Data & Metadata

This section organizes glossary entries into thematic groups (H3+), keeping H2 headings aligned with **KFM‑MDP v11.2.6**.

### 📚 Core Project Terms

| Term | Definition | Related Components |
|------|-----------|--------------------|
| **KFM (Kansas Frontier Matrix)** | A semantic, FAIR+CARE-aligned geospatial–historical knowledge hub for Kansas, integrating maps, timelines, Story Nodes, and AI-assisted narratives under a unified architecture. | Entire monorepo |
| **MCP (Master Coder Protocol)** | Documentation-first engineering protocol that requires design docs, provenance, and validation before code is accepted; governs experiments, model cards, and SOPs. | `docs/standards/`, `mcp/`, `.github/` |
| **KFM-MDP (Markdown Protocol)** | Project-wide ruleset (v11.2.6) for YAML front-matter, headings, diagram profiles, and CI-safe Markdown structure, including heading registries and governance footers. | `docs/standards/kfm_markdown_protocol_v11.2.6.md` |
| **KFM-OP (Ontology Protocol)** | Defines how entities, relationships, time, and space are modeled in the KFM knowledge graph, aligning with CIDOC-CRM, OWL-Time, GeoSPARQL, and PROV-O. | `schemas/`, `docs/architecture/graph_*.md` |
| **KFM-STAC / KFM-DCAT / KFM-PROV** | KFM-specific profiles of STAC, DCAT, and PROV-O used to keep catalogs, datasets, and provenance graphs consistent. | `docs/standards/`, `data/stac/`, `data/sources/` |
| **FAIR Principles** | Data principles: Findable, Accessible, Interoperable, Reusable; used to evaluate datasets, documentation, and APIs. | Validation pipelines, `docs/standards/faircare/` |
| **CARE Principles** | Indigenous data governance framework: Collective Benefit, Authority to Control, Responsibility, Ethics. | Governance council, `docs/standards/faircare/` |
| **Focus Mode** | AI-assisted, entity-centric interface that synchronizes map, timeline, and narrative insights while enforcing provenance, explainability, and CARE constraints. | `src/web/`, `src/api/`, `docs/architecture/focus_mode*.md` |
| **Story Node** | A narrative unit representing a curated story with spatial footprint, temporal span, and linked entities/documents, backed by graph data and STAC/DCAT metadata. | `docs/architecture/story_nodes/`, `schemas/json/*story-node*` |
| **Heritage Standards** | Unified heritage protection specification governing schemas, examples, and assets for sensitive cultural and archaeological data in KFM. | `docs/standards/heritage/HERITAGE_STANDARDS_v11.md` |

### ⚙️ Technical & Pipeline Vocabulary

| Term | Definition | Reference |
|------|------------|-----------|
| **ETL (Extract–Transform–Load)** | Pipeline stages that ingest raw data, normalize and enrich it, then load it into storage or the knowledge graph. | `src/pipelines/etl/` |
| **Knowledge Graph** | Neo4j-backed semantic graph of entities, relationships, and events, modeled with CIDOC-CRM, OWL-Time, GeoSPARQL, and PROV-O. | `src/graph/`, `docs/architecture/graph_*.md` |
| **Autonomy Matrix** | Governed control-plane layer for KFM pipelines that issues `resume / slow / pause / escalate` actions using cost, energy, carbon, freshness, and governance signals. | `docs/pipelines/autonomy-matrix/` |
| **Pipeline Profile** | YAML contract describing SLOs, budgets, CARE labels, and autonomy behaviors for a specific pipeline. | `docs/pipelines/autonomy-matrix/pipeline-profiles/` |
| **Scenario Fixture** | Synthetic JSONL telemetry snapshot used to test and replay Autonomy Matrix decisions under specific scenarios (e.g., P0 storm, P2 batch reporting). | `docs/pipelines/autonomy-matrix/examples/` |
| **Reliability Framework** | Suite of practices and docs defining SLOs, error budgets, and rollback/replay procedures across KFM pipelines. | `docs/pipelines/reliability/` |
| **SBOM (Software Bill of Materials)** | SPDX/CycloneDX list of software components, versions, and licenses used in a build or release. | `releases/*/sbom.spdx.json` |
| **Telemetry** | Structured metrics about builds, pipelines, autonomy decisions, AI performance, accessibility, energy, and governance exported as JSON. | `releases/*/focus-telemetry.json`, `schemas/telemetry/` |
| **SLSA** | Supply-chain Levels for Software Artifacts; guidance and levels for build provenance and integrity. | `.github/workflows/`, `docs/architecture/supply_chain.md` |
| **Checksum (SHA-256)** | Cryptographic hash used to verify integrity of files, datasets, and releases. | `releases/*/manifest.zip`, `data/checksums/` |
| **STAC/DCAT Bridge** | Mapping layer keeping STAC Items/Collections and DCAT Datasets semantically aligned with KFM ontology. | `docs/architecture/data-architecture.md` |
| **LangGraph** | DAG-based orchestration layer for multi-step AI and ETL flows, used to coordinate agents and pipeline steps. | `src/agents/`, `src/pipelines/` |
| **MCP Server** | Service exposing internal tools (Neo4j, STAC, GDAL, etc.) to AI frameworks through standardized MCP tool interfaces. | `docs/architecture/api-architecture.md`, `mcp/` |
| **Write-Ahead Log (WAL)** | Append-only log of transformations and promotions, used for reproducibility, rollback, and audits across datasets and models. | `docs/pipelines/reliable-pipelines.md` |

### 🛡️ Security & Governance Terms

| Term | Definition | Related Components |
|------|------------|--------------------|
| **Prompt Injection Defense** | Controls that prevent user-provided text from overriding system policies (tool allowlists, schema-bound prompts, strict context filters). | `docs/security/prompt-injection-defense.md`, `.github/` |
| **Threat Modeling (STRIDE / LINDDUN)** | Structured methods to identify security (STRIDE) and privacy (LINDDUN) risks for system components and data flows. | `docs/security/threat-model.md` |
| **Secrets Policy (ZTA)** | Zero-Trust approach for managing credentials: no secrets in repo, use KMS/Vault, strict rotation and access logs. | `docs/security/secrets-policy.md` |
| **Supply Chain Security** | Practices to secure build and dependency chain (SLSA levels, SBOMs, signatures, pinned dependencies). | `docs/security/supply-chain.md`, `.github/` |
| **Incident Response (IR)** | Process for detecting, triaging, and resolving security/privacy incidents, aligned with NIST/ISO guidance. | `docs/security/incident-response.md` |
| **CARE Tag** | Categorical label applied to datasets or nodes indicating governance status (e.g., `Public`, `Restricted`, `Sensitive`). | Graph properties, STAC/DCAT metadata |
| **Governance Ledger** | Append-only record of governance decisions, reviews, and audits related to datasets, models, and narratives. | `docs/reports/audit/`, `docs/standards/governance/` |
| **Public Document** | A document classified as suitable for general public release, typically licensed under CC-BY or similar. | YAML front-matter `classification` field |
| **Heritage Protection Tier** | Tiered flag (I–III) indicating how aggressively a heritage resource must be masked or restricted in outputs. | `docs/standards/heritage/`, heritage schemas |

### 🧠 AI & Semantic Frameworks

| Term | Definition | Related Component |
|------|------------|-------------------|
| **NER (Named Entity Recognition)** | NLP task that extracts labeled entities (e.g., PERSON, PLACE, ORG) from text for graph linking. | `src/ai/models/`, `src/pipelines/text/` |
| **Transformer** | Deep learning architecture used for tasks like summarization, classification, and generation. | `src/ai/models/*` |
| **Embedding Model** | Model that converts text or features into dense vectors for similarity search, clustering, and retrieval. | `src/ai/models/embeddings/` |
| **SHAP** | Explainability method showing feature contributions to model predictions. | `src/ai/explainability/` |
| **LIME** | Local interpretable model-agnostic explanation method for black-box predictions. | `src/ai/explainability/` |
| **Cypher** | Query language used to interact with the Neo4j knowledge graph. | `src/graph/queries/` |
| **Focus Transformer** | Model stack tuned to generate Focus Mode narratives and summaries from graph and document context. | `src/ai/models/focus_transformer_v*/` |
| **Hallucination Guardrail** | Set of checks ensuring AI output is grounded in actual data and sources, rejecting unverifiable statements and unknown entities. | `docs/pipelines/validation-observability/`, `src/ai/` |

### 🗺 Geospatial, Heritage & Historical Terms

| Term | Definition | Related Usage |
|------|------------|---------------|
| **BBox (Bounding Box)** | Four-value array `[west, south, east, north]` in WGS84 (EPSG:4326) representing a rectangular spatial extent. | STAC Items, GeoJSON |
| **CRS (Coordinate Reference System)** | Formal description of how spatial coordinates map to Earth positions; typically specified as an EPSG code. | All geodata, STAC assets |
| **COG (Cloud-Optimized GeoTIFF)** | GeoTIFF structure optimized for HTTP range requests and web tiling; used for terrain, imagery, and rasters. | `data/processed/rasters/` |
| **GeoJSON / GeoTIFF** | Open formats for vector (GeoJSON) and raster (GeoTIFF) geospatial data. | Processed layers, STAC assets |
| **DEM (Digital Elevation Model)** | Raster dataset representing terrain elevation, often used for terrain analysis and 3D rendering. | Terrain layers, 3D visualization |
| **Hydrography** | Representation of water features such as rivers, lakes, and basins. | Hydrology analyses, `data/sources/hydrology/` |
| **H3 Index** | Hexagonal hierarchical spatial index used for aggregation and masking of sensitive locations (e.g., heritage sites). | `docs/standards/heritage/`, sensitive layers |
| **Temporal Interval** | Time span defined by start and end instants, modeled using OWL-Time and stored as event extents. | Graph events, timeline UI |
| **Heritage Generalization** | Process of transforming raw heritage locations into generalized H3 cells or regions to protect exact site locations. | Heritage pipelines, `HERITAGE_STANDARDS_v11.md` |

### 🔗 Cross-Standard References

| Standard       | Governing Body       | KFM Usage                                  |
|----------------|----------------------|--------------------------------------------|
| **STAC 1.x**   | OGC / Radiant Earth  | Cataloging geospatial assets               |
| **DCAT 3.0**   | W3C                  | Dataset metadata and catalogs              |
| **CIDOC-CRM**  | ICOM / ISO           | Cultural heritage entity & event modeling  |
| **OWL-Time**   | W3C                  | Temporal instants and intervals            |
| **GeoSPARQL 1.1** | OGC              | Spatial relationships in the knowledge graph |
| **PROV-O**     | W3C                  | Provenance modeling for entities and activities |
| **SPDX 2.3**   | Linux Foundation     | Software bill of materials (SBOM)          |
| **CycloneDX**  | OWASP                | Alternative SBOM format for security tools |

### 🧩 Controlled Vocabulary (Selected Fields)

Use these controlled values in front-matter and metadata to reduce ambiguity:

| Field        | Allowed Values                                | Notes                                   |
|--------------|-----------------------------------------------|-----------------------------------------|
| `care_label` | `Public` · `Restricted` · `Sensitive`         | High-level CARE classification          |
| `classification` | `Public Document` · `Internal` · `Restricted` | Document exposure status            |
| `lifecycle`  | `Draft` · `Long-Term Support (LTS)` · `Deprecated` | Use for doc lifecycle, not just stage |
| `stac:stage` | `raw` · `work` · `staging` · `processed` · `archive` | Data lifecycle in KFM pipelines |
| `license`    | `CC-BY 4.0` · `MIT` · `ODbL-1.0` · `Public-Domain` | Prefer SPDX-compatible identifiers |
| `crs`        | `EPSG:4326` (default)                         | Other CRS require explicit documentation |
| `a11y.level` | `AA` · `AAA`                                  | Target WCAG conformance level           |

---

## 🧠 Story Node & Focus Mode Integration

The glossary supports Story Nodes and Focus Mode by providing:

- A **canonical label set** for:
  - Entity types (e.g., `heritage_site`, `Story Node`, `Autonomy Scenario`).  
  - Governance tags (`care_label`, `heritage_protected`, `indigenous_rights_flag`).  
  - Technical artifacts (`pipeline_profile`, `scenario_fixture`, `telemetry_schema`).

- A **machine-extractable vocabulary** for:
  - Semantic highlighting in Focus Mode.  
  - Entity disambiguation (e.g., “Collection” in STAC vs “Collection” in DCAT).  
  - Glossary popovers in the UI.

Focus Mode usage rules:

- MAY surface glossary definitions inline when users hover or tap terms.  
- SHOULD show the **short, neutral definition** plus links to deeper standards docs.  
- MUST NOT rewrite or reinterpret glossary entries in ways that conflict with governance; any normative redefinition must happen here in the glossary, reviewed via the usual process.

---

## 🧪 Validation & CI/CD

Glossary-specific checks in CI:

- **Schema lint** — this file’s front-matter is validated against `docs-glossary-v11` JSON schema.  
- **Metadata check** — required identity, classification, and governance fields are present and correctly formatted.  
- **Provenance check** — `provenance_chain` entries match the Version History table.  
- **Footer check** — ensures governance and navigation links are present at the end of the document.  
- **Accessibility check** — headings, tables, and link text meet basic accessibility requirements.

Suggested local commands (examples; actual targets may differ):

~~~text
make validate-docs-glossary
make lint-markdown
~~~

Any term added here should ideally appear in at least one:

- Schema (`schemas/json/`, `schemas/shacl/`)  
- Standard (`docs/standards/`)  
- Architecture or pipeline doc (`docs/architecture/`, `docs/pipelines/`)

---

## ⚖ FAIR+CARE & Governance

The glossary is itself a **governed artifact**:

- It encodes **shared understanding** across technical, historical, and governance teams.  
- Changes to sensitive terminology (especially heritage, Indigenous data, and sovereignty terms) require **FAIR+CARE Council review**.  
- It participates in **provenance and audit**:
  - Each version is referenced in `provenance_chain`.  
  - Focus Mode and other AI tools are constrained by the definitions and restrictions here.

Guidance:

- When defining heritage or Indigenous-related terms:
  - Avoid oversimplification; link to the relevant heritage or sovereignty documents for nuance.  
  - Do not introduce new labels for communities or traditions without consultation.  
- When defining AI terms relating to risk:
  - Make explicit whether the term is normative (governance) or descriptive (implementation detail).

---

## 🕰️ Version History

| Version   | Date       | Author        | Summary                                                                                           |
|----------:|------------|---------------|---------------------------------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-11 | KFM Docs Team | Upgraded to KFM-MDP v11.2.6; aligned release paths and schemas; clarified telemetry and Focus Mode usage; kept glossary entries in sync with Autonomy Matrix and heritage standards. |
| v11.0.1  | 2025-12-06 | KFM Docs Team | Realigned with KFM-MDP v11.2.4; added Autonomy Matrix, heritage standards, scenario fixtures, and clarified controlled vocabulary. |
| v11.0.0  | 2025-11-18 | KFM Docs Team | Upgraded to KFM-MDP v11; expanded ontology fields, security terms, H3, and controlled vocabulary. |
| v10.3.1  | 2025-11-13 | KFM Docs Team | Updated release paths to v10.3.0; added LangGraph, MCP server, and governance entries.           |
| v10.2.4  | 2025-11-12 | KFM Docs Team | Added controlled vocabulary table; checksum reference path updated.                              |
| v10.2.3  | 2025-11-09 | KFM Docs Team | Added security suite terms, STAC/DCAT bridge entry, telemetry schema v3.                         |
| v9.7.0   | 2025-11-05 | A. Barta      | Comprehensive glossary aligned to MCP v6.3 and FAIR+CARE.                                        |
| v9.5.0   | 2025-10-20 | A. Barta      | Added ontology and governance terminology.                                                       |
| v9.3.0   | 2025-08-12 | KFM Core Team | Expanded technical and pipeline entries.                                                         |
| v9.0.0   | 2025-06-01 | KFM Core Team | Initial glossary framework.                                                                      |

---

<div align="center">

📘 **Kansas Frontier Matrix — Glossary & Terminology Index v11.2.6**  
Scientific Insight · Documentation-First · FAIR+CARE Ethics  

[📘 Docs Root](.) · [📂 Standards](standards/README.md) · [⚖ Governance](standards/governance/ROOT-GOVERNANCE.md)

</div>