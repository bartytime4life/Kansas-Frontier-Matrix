---
title: "🏗️ Kansas Frontier Matrix — Repository Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "ARCHITECTURE.md"
version: "v11.2.4"
last_updated: "2025-12-07"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
backward_compatibility: "Full v10.x → v11.x compatibility"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v11.2.4/signature.sig"
attestation_ref: "releases/v11.2.4/slsa-attestation.json"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/root-architecture-v11.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
openlineage_profile: "OpenLineage v2.5 + KFM Extensions"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "repository-architecture"
category: "System Architecture · Repository Design · Global Dataflow"

fair_category: "F1-A1-I1-R1"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
sensitivity: "General (non-sensitive; applies masking to protected datasets)"
sensitivity_level: "Low"
public_exposure_risk: "Low to Medium"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_profile: "High Governance · Requires Full Provenance · Auto-Masked Sensitive Data"
redaction_required: false

ontology_ref:
  - "docs/graph/ontology/core-entities.md"
  - "docs/graph/ontology/cidoc-crm-mapping.md"
  - "docs/graph/ontology/spatial-temporal-patterns.md"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "ARCHITECTURE.md@v11.2.2"
  - "ARCHITECTURE.md@v11.1.1"
  - "ARCHITECTURE.md@v11.1.0"
  - "ARCHITECTURE.md@v11.0.1"
  - "ARCHITECTURE.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/root-architecture-v11.schema.json"
shape_schema_ref: "schemas/shacl/root-architecture-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:architecture:repository:v11.2.4"
semantic_document_id: "kfm-repository-architecture"
event_source_id: "ledger:ARCHITECTURE.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
  - "lineage-audit-v11"
  - "governance-audit-v11"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_architecture_doc_v10.4"
---

<div align="center">

# 🏗️ **Kansas Frontier Matrix**  
## **Repository Architecture & System Blueprint (v11 LTS)**  
`ARCHITECTURE.md`  

**Purpose:**  
Describe the **canonical repository structure and runtime architecture** for the Kansas Frontier Matrix (KFM v11), in a way that is:  

- deterministic and provenance-aware (PROV-O, OpenLineage),  [oai_citation:0‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- geospatially interoperable (GeoSPARQL, STAC),  [oai_citation:1‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
- documentation-first and CI-safe under **KFM-MDP v11.2.4**.  [oai_citation:2‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  

[📘 Docs – MCP v6.3](docs/README.md) · [⚖️ FAIR+CARE](docs/standards/faircare/FAIRCARE-GUIDE.md) · [📜 License: MIT](LICENSE) · [📦 SBOM](releases/v11.2.4/sbom.spdx.json) · [📊 Telemetry](releases/v11.2.4/focus-telemetry.json)

</div>

---

## 📘 Overview

KFM v11 is a **state-scale, FAIR+CARE-governed knowledge system for Kansas**, spanning:

- 🗺️ Geospatial layers (2D/3D maps, rasters, vectors, DGGS/H3 tiles)  
- 💧 Environmental & hydrological chronologies  
- 🌿 Ecology, land systems, and soil/terrain  
- 🏺 Archaeology & cultural landscapes (generalized for sovereignty and safety)  
- 📜 Historical archives, documents, and newspapers  
- ⚡ Hazards & infrastructure (storms, floods, drought, wildfire, energy)  
- 🧠 AI-assisted ETL, modeling, and narrative generation  
- 📖 Story Nodes & Focus Mode overlays tied to the knowledge graph  

This architecture document is treated as a **prov:Plan** (design/specification) and a **CIDOC-CRM E29 Design or Procedure**, providing the blueprint that all code, data, and docs must conform to.  [oai_citation:3‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

### Goals of this document

- Provide a **single, canonical directory layout** for the monorepo.  [oai_citation:4‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
- Explain how **data, pipelines, graph, APIs, and web UI** compose into one system.  
- Show how **STAC, DCAT, PROV-O, GeoSPARQL, OWL-Time** are wired in from the start.  [oai_citation:5‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
- Describe how **Story Nodes & Focus Mode** depend on this structure for safe, grounded narratives.  
- Anchor CI/CD, governance, and FAIR+CARE checks directly into the repo layout.

All evolution of the repository MUST preserve this high-level shape; deviations (e.g., new top-level directories, alternate layouts) require architecture/governance review and a version bump to this document.

---

## 🗂️ Directory Layout

The directory tree below is the **authoritative layout** for the KFM monorepo. It follows the emoji + comment conventions from **KFM-MDP v11.2.4** and MUST be kept in sync with reality.  [oai_citation:6‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  

~~~text
KansasFrontierMatrix/
├── 📂 docs/                                  # All documentation
│   ├── 📂 standards/                         # Standards & policies (Markdown, FAIR+CARE, governance, etc.)
│   ├── 📂 architecture/                      # System & subsystem designs (ETL, graph, API, UI, Focus Mode)
│   ├── 📂 guides/                            # How-to guides, tutorials, SOP-style walkthroughs
│   ├── 📂 data/                              # Data contracts, source registries, schema notes
│   ├── 📂 analyses/                          # Domain analyses & case studies (archaeology, hydrology, etc.)
│   └── 📄 glossary.md                        # Shared glossary for KFM-wide terminology
├── 📂 src/                                   # Backend & service code
│   ├── 📂 pipelines/                         # ETL, AI/ML, orchestration (batch, streaming, LangGraph, Airflow)
│   ├── 📂 graph/                             # Neo4j schema, loaders, queries, lineage helpers
│   ├── 📂 api/                               # FastAPI / GraphQL services (gateway, auth, routing)
│   └── 📂 tools/                             # Backend utilities, CLIs, migrations
├── 📂 data/                                  # Data lifecycle: raw → work → processed → releases
│   ├── 📂 sources/                           # External dataset manifests (STAC/DCAT-aligned)
│   ├── 📂 raw/                               # Raw ingested data (LFS/DVC; not committed directly)
│   ├── 📂 work/                              # Intermediate normalized / enriched data
│   ├── 📂 processed/                         # Production-ready GeoJSON, COGs, CSVs, graph exports
│   └── 📂 stac/                              # STAC Collections & Items indexing processed assets
├── 📂 schemas/                               # JSON, JSON-LD, STAC, DCAT, SHACL, telemetry schemas
│   ├── 📂 json/                              # JSON schemas (docs, pipelines, Story Nodes, Focus telemetry)
│   └── 📂 telemetry/                         # Energy, carbon, lineage, metrics schemas
├── 📂 mcp/                                   # Master Coder Protocol artifacts
│   ├── 📂 experiments/                       # Experiment logs (timestamped, domain-tagged)
│   ├── 📂 model_cards/                       # Model documentation & evaluation cards
│   └── 📂 sops/                              # SOPs for repeatable processes (ETL, modeling, deployment)
├── 📂 tests/                                 # Automated test suites (unit, integration, UI)
├── 📂 tools/                                 # Repo-level tools, dev utilities, maintenance scripts
└── 📂 .github/                               # CI/CD workflows & GitHub configuration
    └── 📂 workflows/                         # CI pipelines (kfm-ci, docs-lint, lineage-audit, energy/carbon)
~~~

**Directory rules**

- Every directory shown above MUST have a `README.md` explaining purpose, substructure, and governance.  
- New top-level directories are **forbidden** without updating this document and passing architecture/governance review.  
- Directory trees in docs MUST use `~~~text` fences and canonical `├──` / `└──` glyphs and emoji labels, per KFM-MDP v11.2.4.  [oai_citation:7‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  

---

## 🧭 Context

This architecture sits at the intersection of several KFM standards and external vocabularies:

- **Markdown Protocol – KFM-MDP v11.2.4**  
  Enforces front-matter, heading registry, and footer patterns for all Markdown in `docs/`, `ARCHITECTURE.md` included.  [oai_citation:8‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  

- **Provenance – PROV-O + KFM-PROV v11**  
  All design choices here are modeled as a **prov:Plan** and operationalized via Entities–Activities–Agents, enabling lineage of code, data, and docs.  [oai_citation:9‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

- **Geospatial Semantics – GeoSPARQL + KFM-STAC v11**  
  Spatial things in KFM are treated as `geo:Feature` with linked geometries (`geo:Geometry`) using WKT/GeoJSON literals, aligning 2D/3D map views with the graph and catalogs.  [oai_citation:10‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

- **Catalogs – DCAT 3.0 + STAC 1.x**  
  Datasets in `data/` and their metadata in `docs/data/` and `data/stac/` follow DCAT and STAC profiles so they can be discovered, filtered, and linked to PROV graphs.

- **Story Nodes & Focus Mode**  
  Narrative overlays are backed by the graph and catalogs; they rely on this repository’s predictable structure to safely answer “what, where, when, how, and who”.

This document is the **entry point** for new contributors and automated agents: if a change cannot be located in this architecture, it is probably not aligned with KFM governance yet.

---

## 🗺️ Diagrams

### 1. End-to-End System View

~~~mermaid
flowchart LR
    subgraph Repo[Monorepo]
        A[docs/ standards & guides] --> B[src/ pipelines]
        B --> C[data/ processed & stac/]
        C --> D[src/ graph · Neo4j]
        D --> E[src/ api · GraphQL/FastAPI]
        E --> F[web clients · Map/3D/Focus Mode]
    end

    subgraph Lineage[Lineage & Provenance]
        B -. OpenLineage .-> G[Runtime Lineage Bus]
        B --> H[PROV-O Export]
        H --> I[Lineage Store (RDF/Graph)]
        I --> F
    end
~~~

- **Docs** define contracts and standards.  
- **Pipelines** implement those contracts and emit catalog + PROV-O lineage.  [oai_citation:11‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- **Graph & APIs** expose a governed, queryable knowledge graph.  
- **Web** renders maps, timelines, and Focus Mode overlays backed by those layers.  [oai_citation:12‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

### 2. Architecture Evolution (Example)

~~~mermaid
timeline
    title Repository Architecture Evolution (v11)
    2025-11-19 : v11.0.0 : "Initial v11 LTS repository architecture"
    2025-11-23 : v11.0.1 : "Expanded runtime/lineage description"
    2025-11-27 : v11.2.2 : "Aligned with KFM-MDP v11.2.2, CI hardening"
    2025-12-07 : v11.2.4 : "Full KFM-MDP v11.2.4 alignment, STAC/DCAT/PROV/GeoSPARQL integration"
~~~

Diagrams are **illustrative only**; all normative requirements live in text, schemas, and tests.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode are first-class citizens in this architecture:

- **Story Nodes**  
  - Live as JSON (schema in `schemas/json/`) and are indexed by the graph.  
  - Bind narrative text to:
    - Place (`geo:Feature`), via GeoSPARQL-aligned geometry references.  [oai_citation:13‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
    - Time (`time:Instant` / `time:Interval`), using OWL-Time patterns.  
    - Datasets and documents (`prov:Entity`, `dcat:Dataset`).  [oai_citation:14‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

- **Focus Mode v3**  
  - Accepts a focus target: graph node ID, dataset ID, Story Node ID.  
  - Pulls a controlled subgraph (2–3 hops), plus STAC/DCAT records and PROV-O lineage.  
  - Generates explanations using only allowed transforms (`summary`, `semantic-highlighting`, etc.), never modifying source docs or inventing provenance.

**Repo responsibilities**

- `docs/architecture/` describes Story Node schemas, Focus Mode behaviors, and UI contracts.  
- `src/graph/` defines labels and relationships that Story Nodes and Focus Mode target.  
- `src/api/` exposes:
  - “focus target → subgraph + docs + catalogs + lineage” APIs.  
- `web/` (when present under `src/` or a dedicated app) is *only* a consumer of these APIs; it does not invent lineage or narrative on its own.

---

## 🧪 Validation & CI/CD

The repository is wired so that **docs, code, data, and lineage** are validated together before merging.

### 1. CI Workflows

`.github/workflows/kfm-ci.yml` orchestrates:

- **Docs & Markdown**
  - `markdown-lint` and `accessibility-check` for all `.md` (including this file).  [oai_citation:15‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
  - `footer-check` to ensure version history + governance footers are present.  

- **Schemas & Contracts**
  - `schema-lint` for JSON/JSON-LD/STAC/DCAT/Story Node/telemetry schemas.  
  - Data-contract checks (KFM-PDC v11) against sample data in `data/`.  

- **Lineage & Governance**
  - `lineage-audit-v11` verifies that pipelines emit PROV-O/OpenLineage events.  [oai_citation:16‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
  - `governance-audit-v11` ensures FAIR+CARE and sovereignty rules are respected.

### 2. Architecture-Specific Expectations

For any PR that changes **repository structure or architecture**:

- Update **this file** (`ARCHITECTURE.md`) and any relevant `docs/architecture/*.md`.  
- Update schemas (`schemas/json/`, `schemas/shacl/`) if contracts change.  
- Add or update tests under `tests/` and, where appropriate, fixtures under `data/` or `mcp/experiments/`.  
- Include lineage expectations (PROV-O/OpenLineage) for new pipelines.  

No structural change is considered valid until **CI is green and this architecture doc remains consistent with the repo**.

---

## 📦 Data & Metadata

The data and metadata stack is designed to be:

- **Graph-friendly** — everything is representable as nodes and relationships.  
- **Catalog-first** — datasets surface via DCAT and STAC records.  
- **Provenance-rich** — every important entity has a PROV-O lineage chain.  [oai_citation:17‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

### 1. Data Lifecycle

- `data/raw/` — raw ingests, never edited in place; referenced as PROV-O Entities.  
- `data/work/` — normalized and enriched intermediates; often used in iterative analyses.  
- `data/processed/` — canonical outputs for publication and graph loading.  
- `data/stac/` — STAC Collections & Items referencing processed assets (COGs, GeoJSON, etc.).  

### 2. Metadata Artifacts

- **Schemas** in `schemas/json/` and `schemas/shacl/` define:
  - data contracts,
  - Story Node formats,
  - telemetry and energy/carbon measurements.  

- **Catalogs**:
  - DCAT records (KFM-DCAT v11) describe datasets and their distributions.  
  - STAC records (KFM-STAC v11) describe geospatial items and collections.  

- **Lineage**:
  - PROV-O graphs represent Entities–Activities–Agents, including datasets, ETL runs, and review processes.  [oai_citation:18‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

All of these are referenced from the graph, letting Focus Mode “walk” from a narrative to the underlying data and back.

---

## 🌐 STAC, DCAT & PROV Alignment

This repo architecture is explicitly tuned to make **STAC, DCAT, PROV-O, and GeoSPARQL** work together cleanly.   

### 1. High-Level Alignment

- **DCAT 3.0**  
  - `dcat:Dataset` ↔ logical dataset (e.g., “Kansas Wells 2025”).  
  - `dcat:Distribution` ↔ actual files/APIs in `data/processed/`.  
  - Provenance uses `prov:wasGeneratedBy` and related properties.  [oai_citation:19‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

- **STAC 1.x**  
  - STAC Collections/Items in `data/stac/` describe spatial assets linked to processed datasets.  
  - Geometry is expressed via GeoJSON or WKT, in line with GeoSPARQL’s geometry model.  [oai_citation:20‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

- **PROV-O**  
  - Entities = datasets, files, docs, configs.  
  - Activities = ETL runs, analyses, reviews, exports.  
  - Agents = people, orgs, software systems.  [oai_citation:21‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

- **GeoSPARQL**  
  - `geo:Feature` ↔ places, sites, grid cells, etc.  
  - `geo:Geometry` ↔ geometry nodes with `geo:asWKT` / `geo:asGeoJSON` serializations.  [oai_citation:22‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  

### 2. Concrete Repo Mappings

- `data/processed/` → PROV-O Entities + DCAT Distributions; STAC Assets for geospatial outputs.  
- `data/stac/` → STAC Collections/Items; each Item’s geometry is a **GeoSPARQL geometry** in the lineage graph.  
- `src/pipelines/` → PROV-O Activities + OpenLineage jobs, capturing how entities were produced.  [oai_citation:23‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- `docs/` → PROV-O Plans (designs, protocols) and DCAT/TechArticle-style documentation records.  

The architecture ensures every major artifact has **an ID, a catalog record, lineage, and—if spatial—a geometry**.

---

## 🧱 Architecture

Conceptually, KFM v11 is organized into the following layers:

### 1. Data Layer (`data/`, `schemas/`)

- Encodes data lifecycle, contracts, and catalogs.  
- Anchors STAC/DCAT/GeoSPARQL/PROV-O integration.   

### 2. Pipeline & AI Layer (`src/pipelines/`, `src/ai/`, `tools/`)

- Implements ETL, ingestion, and transformation jobs.  
- Emits lineage events (OpenLineage + PROV-O exports).  [oai_citation:24‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- Hosts AI-assisted flows (e.g., summarization, extraction, quality checks) under strict governance.

### 3. Knowledge Graph Layer (`src/graph/`, `docs/graph/`)

- Neo4j schema aligns KFM-OP v11 with:
  - PROV-O for provenance,  [oai_citation:25‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
  - GeoSPARQL for spatial semantics,  [oai_citation:26‡GeoSPARQL: Geospatial SPARQL for the Semantic Web.pdf](file-service://file-Gcko4NCD4BXhFG42Sh7Z1o)  
  - OWL-Time for temporal ranges.  
- Story Nodes are linked into the graph as narrative overlays.

### 4. API & Service Layer (`src/api/`)

- FastAPI/GraphQL gateway adds:
  - access control and authentication,  
  - FAIR+CARE masking and sovereignty enforcement,  
  - lineage-aware query logging and telemetry.

### 5. Presentation Layer (`web/` or frontend apps)

- React + MapLibre + Cesium (where implemented) render:
  - maps, 3D scenes, and timelines,  
  - Focus Mode panels on top of graph + catalogs.  

The repo keeps a **clean separation**: frontends are stateless view clients; governance, semantics, and provenance live one layer down.

---

## ⚖ FAIR+CARE & Governance

This architecture is explicitly engineered to make **FAIR+CARE + sovereignty** enforceable:

- **FAIR**
  - *Findable*: stable IDs, cataloged datasets, discoverable docs.  
  - *Accessible*: open formats (Markdown, JSON, RDF) and public schemas.  
  - *Interoperable*: DCAT, STAC, PROV-O, GeoSPARQL, OWL-Time as shared vocabularies.   
  - *Reusable*: clear licensing, version history, and provenance.

- **CARE**
  - *Collective Benefit*: architecture targets long-term benefit for Kansas communities, not just internal users.  
  - *Authority to Control*: sovereignty policies are wired into:
    - ETL masking and generalization,  
    - graph-level access controls,  
    - Focus Mode transform restrictions.  
  - *Responsibility & Ethics*: docs, pipelines, and UI flows are reviewed where sensitive cultural or ecological data are involved.

- **Governance Hooks**
  - Governance & FAIR+CARE docs in `docs/standards/` are normative references for this file.  [oai_citation:27‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.4.pdf](file-service://file-57iDMaU6FoN7pZ8e5HbsPp)  
  - Changes to architecture, lineage, or exposure pathways MUST go through council review when flagged as high-risk.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                                                               |
|----------:|------------|-----------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-07 | Aligned with **KFM-MDP v11.2.4**; harmonized heading registry, directory layout emojis, and STAC/DCAT/PROV/GeoSPARQL wiring; clarified Story Node & Focus Mode dependencies. |
| v11.2.2  | 2025-11-27 | Synced with v11.2.2 CI/governance setup; described OpenLineage integration and strengthened lineage/governance audits. |
| v11.1.1  | 2025-11-27 | Refined runtime/lineage descriptions; clarified FAIR+CARE hooks in CI and data lifecycle.                              |
| v11.1.0  | 2025-11-27 | Updated for KFM-STAC/DCAT v11 and ontology alignment; documented responsibilities per repo layer.                       |
| v11.0.1  | 2025-11-23 | Expanded runtime description (LangGraph, lineage bus, reliability engine); clarified monorepo layout philosophy.       |
| v11.0.0  | 2025-11-19 | Established v11 LTS architecture; defined dataflow, graph role, and governance integration for the modern KFM stack.   |

---

<div align="center">

🏗️ **Kansas Frontier Matrix — Repository Architecture (v11.2.4)**  
Documentation-First · FAIR+CARE · Provenance-Aware · Spatially Interoperable  

[⬅️ Root Overview](README.md) · [📚 Docs Home](docs/README.md) · [🛡️ Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
