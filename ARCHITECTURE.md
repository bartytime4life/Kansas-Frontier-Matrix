---
title: "🏗️ Kansas Frontier Matrix — Repository Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "ARCHITECTURE.md"
version: "v11.1.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
backward_compatibility: "Full v10.x → v11.x compatibility"
commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v11.0.0/signature.sig"
attestation_ref: "releases/v11.0.0/slsa-attestation.json"
sbom_ref: "releases/v11.0.0/sbom.spdx.json"
manifest_ref: "releases/v11.0.0/manifest.zip"
telemetry_ref: "releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/root-architecture-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
risk_profile: "High Governance · Requires Full Provenance · Auto-Masked Sensitive Data"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "repository-architecture"
category: "System Architecture · Repository Design · Global Dataflow"
sensitivity: "General (non-sensitive, but applies masking to protected datasets)"
prov_profile: "PROV-O Core + KFM Lineage Extensions"
openlineage_profile: "OpenLineage v2.5 + KFM Extensions"
ontology_ref:
  - "docs/graph/ontology/core-entities.md"
  - "docs/graph/ontology/cidoc-crm-mapping.md"
  - "docs/graph/ontology/spatial-temporal-patterns.md"
metadata_profiles:
  - "schemas/stac/kfm-stac-v11.json"
  - "schemas/dcat/kfm-dcat-v11.json"
  - "schemas/jsonld/kfm-context-v11.json"
validation_profiles:
  - "docs-lint-v11"
  - "schema-lint-v11"
  - "lineage-audit-v11"
  - "governance-audit-v11"
ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
runtime:
  compute: "KFM Multi-Cloud Mesh (AWS + GCP + On-Prem)"
  graph_engine: "Neo4j Enterprise v5.x Cluster"
  api_stack: "FastAPI + GraphQL Gateway (GovHooks v4)"
  frontend_stack: "React · MapLibre · Cesium · Vite Build"
  lineage_bus: "OpenLineage v2.5"
  reliability_engine: "Reliable Pipelines v11 — WAL · Retry · Rollback · Hotfix · Lineage"
  agents: "LangGraph Autonomous Updater v11"
fair_category: "F1-A1-I1-R1"
sensitivity_level: "Low"
public_exposure_risk: "Low to Medium"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
redaction_required: false
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "ProperInterval"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "schemas/json/root-architecture-v11.schema.json"
shape_schema_ref: "schemas/shacl/root-architecture-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:architecture:repository:v11.1.0"
semantic_document_id: "kfm-repository-architecture"
event_source_id: "ledger:ARCHITECTURE.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified architectural claims"
  - "modifying normative requirements"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major architecture and repository redesign"
---

<div align="center">

# 🏗️ **Kansas Frontier Matrix**  
## **Repository Architecture & System Blueprint (v11 LTS)**  
`ARCHITECTURE.md`

[![Docs – MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](#)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](#)
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](#)
[![SBOM](https://img.shields.io/badge/SBOM-SPDX-blueviolet)](#)
[![Sustainability](https://img.shields.io/badge/Telemetry-Energy%20%2F%20Carbon-009688)](#)

</div>

---

## 📘 1. System Overview

The **Kansas Frontier Matrix (KFM v11)** is a unified, multi-layer, multi-epoch knowledge system integrating:

- Geospatial data (2D and 3D)  
- AI pipelines and autonomous ETL  
- Historical archives and cultural records  
- Environmental and hydrological models  
- Archaeology and cultural landscapes  
- Hazards and infrastructure  
- Narrative layers (Story Nodes & Focus Mode)  

It functions as a **FAIR+CARE-governed semantic geospatial operating system** for Kansas, built on:

- 🛰️ Remote sensing  
- 💧 Hydrology & climate chronologies  
- 🗺️ GIS + MapLibre + Cesium  
- 🧬 AI-assisted ETL & LangGraph DAG pipelines  
- 🏺 Archaeology & cultural landscapes  
- 📚 Archives, documents, newspapers, photographs  
- 🔥 Hazards, energy, wildfire, drought, flood  
- 🌿 Ecology & landcover  
- 📦 STAC / DCAT / PROV-O provenance  
- 📖 Story Nodes v3 & Focus Mode v3  
- 🏛️ FAIR+CARE governance and Indigenous data sovereignty  

Underneath everything is a **Neo4j graph** aligned with **CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O, and KFM Ontology v11**, with versioning, lineage, and governance enforced by this architecture.

---

## 🧱 2. Architectural Principles

KFM v11 adheres to several core principles:

- **Documentation-first (MCP-DL v6.3)**  
  Every feature, pipeline, and dataset has accompanying Markdown and metadata that pass KFM-MDP v11.2.2 checks.

- **Semantic-first**  
  All core entities and relationships live in the knowledge graph, with STAC/DCAT/JSON-LD exports acting as views.

- **Deterministic pipelines**  
  ETL and AI flows use WAL, configuration, and OpenLineage events for reproducibility.

- **Governance-by-default**  
  FAIR+CARE, sovereignty, and data contracts are baked into pipelines, CI, and deployment workflows.

- **Monorepo cohesion**  
  A single, cohesive repository with modular subtrees and strict standards, allowing atomic updates across code, data, and docs.

This document is the blueprint describing how those principles map onto the physical layout and runtime structure.

---

## 🗂 3. Repository Layout (v11)

```text
Kansas-Frontier-Matrix/                 # Monorepo root
│
├── README.md                           # Root project overview (KFM v11 system)
├── ARCHITECTURE.md                     # This repository architecture & system blueprint
│
├── data/                               # Data hierarchy
│   ├── raw/                            # Raw external inputs (DVC/LFS pointers; not committed)
│   ├── work/                           # ETL staging workspaces
│   ├── processed/                      # Cleaned and analysis-ready outputs
│   ├── stac/                           # STAC Items/Collections for spatiotemporal assets
│   ├── provenance/                     # PROV-O, OpenLineage, FAIR+CARE records
│   └── releases/                       # Versioned data bundles and public data artifacts
│
├── src/                                # Source code (Python + server)
│   ├── pipelines/                      # LangGraph DAGs and ETL/AI pipelines
│   ├── ai/                             # CrewAI workers, models, prompts, explainers
│   ├── graph/                          # Neo4j ingestion, schema, and graph utilities
│   ├── server/                         # FastAPI + GraphQL services and GovHooks
│   └── telemetry/                      # Energy, IO, carbon, and reliability telemetry
│
├── web/                                # Front-end
│   ├── src/                            # React components, MapLibre, Cesium views
│   ├── public/                         # Static assets
│   └── meta/                           # SEO, manifests, metadata
│
├── docs/                               # Documentation
│   ├── standards/                      # Governance, heritage, H3, FAIR+CARE, etc.
│   ├── architecture/                   # Deep architecture diagrams and design docs
│   ├── analyses/                       # Case studies and analytical reports
│   ├── governance/                     # Governance charters and policy documents
│   └── templates/                      # Documentation templates (MCP, SOPs, Story Nodes)
│
├── schemas/                            # JSON, STAC, DCAT, JSON-LD, SHACL schemas
│   ├── telemetry/                      # Energy, carbon, audit telemetry schemas
│   ├── stac/                           # KFM-STAC v11 schemas
│   ├── dcat/                           # KFM-DCAT v11 schemas
│   └── jsonld/                         # JSON-LD context definitions
│
├── mcp/                                # Master Coder Protocol assets
│   ├── experiments/                    # Experiment logs and reproducibility bundles
│   ├── sops/                           # SOPs for pipelines, AI, governance, etc.
│   ├── model_cards/                    # Model cards for AI/ML systems
│   └── MCP-README.md                   # MCP usage and behavioral guidance
│
└── .github/                            # GitHub CI/CD & governance automation
    ├── README.md                       # GitHub infrastructure overview
    ├── ARCHITECTURE.md                 # CI/CD architecture and governance blueprint
    └── workflows/                      # Actions for CI/CD, FAIR+CARE, security, telemetry
```

This layout is optimized for clarity, modularity, and governance in a single monorepo.

---

## 🌊 4. Data Lifecycle & Profiles

KFM data flows through a consistent lifecycle:

1. **Raw (`data/raw/`)**  
   - Immutable ingests from external providers (e.g., NOAA, USGS, archives).  
   - Typically not checked in fully; managed via DVC/LFS or external storage.  
   - Cataloged via `data/sources/**` manifests + STAC Collections.

2. **Work (`data/work/`)**  
   - ETL staging and intermediate artifacts.  
   - Intended to be ephemeral and reproducible from raw + pipeline configs.  

3. **Processed (`data/processed/`)**  
   - Cleaned, harmonized, contract-compliant outputs.  
   - JSON/GeoJSON/COG GeoTIFF/Parquet and similar.  

4. **Releases (`data/releases/`)**  
   - Versioned data bundles for public or internal release.  
   - Each release includes:
     - `manifest.zip`  
     - `sbom.spdx.json`  
     - `focus-telemetry.json`  

5. **Provenance (`data/provenance/`)**  
   - PROV-O datasets and OpenLineage logs.  
   - FAIR+CARE annotations, and H3-mask metadata for sensitive layers.

STAC and DCAT schemas in `schemas/stac/` and `schemas/dcat/` define how all of this is represented in metadata.

---

## 🧬 5. Ontology, Knowledge Graph, and Alignment

The `ontology_ref` entries:

- `docs/graph/ontology/core-entities.md`  
- `docs/graph/ontology/cidoc-crm-mapping.md`  
- `docs/graph/ontology/spatial-temporal-patterns.md`  

define:

- Core entity types (Place, Event, Dataset, Observation, Story Node, Agent).  
- CIDOC-CRM mappings (e.g., E29 Design or Procedure for standards like this).  
- Spatial and temporal patterns (e.g., H3 generalization rules, OWL-Time intervals).  

`ontology_alignment` captures cross-standard mapping:

- `cidoc: "E29 Design or Procedure"` – this document is a design/procedure instruction.  
- `schema_org: "TechArticle"` – external semantic consumer view.  
- `owl_time: "ProperInterval"` – architecture state valid for a time interval.  
- `prov_o: "prov:Plan"` – it is a plan that guides activities.  
- `geosparql: "geo:FeatureCollection"` – relevant for geospatial architectural components.

The Neo4j schema lives in `src/graph/` and is the canonical implementation of these ontologies.

---

## 🧠 6. Pipelines, Agents, and Reliability Engine

The architecture is explicitly tied to:

- `reliability_engine: "Reliable Pipelines v11 — WAL · Retry · Rollback · Hotfix · Lineage"`  
- `agents: "LangGraph Autonomous Updater v11"`  
- `lineage_bus: "OpenLineage v2.5"`  

This implies:

- All pipelines are structured as **LangGraph DAGs** under `src/pipelines/`.  
- Each node in a DAG:
  - Logs inputs/outputs to `data/work/` or `data/processed/`.  
  - Emits OpenLineage events with PROV-O alignment.  
  - Writes WAL entries enabling replay/rollback.  

- Autonomous Updater agents:
  - Periodically re-run DAGs for data refresh (subject to governance).  
  - Regenerate STAC/DCAT metadata from contracts + graph.  
  - Propose new Story Nodes based on updated data.  

Reliability pipelines are documented in `docs/pipelines/reliable-pipelines.md`.

---

## 🧰 7. API & Frontend Runtime

`runtime.api_stack` and `runtime.frontend_stack` define:

- **Server layer** (`src/server/`):

  - FastAPI services for REST endpoints.  
  - GraphQL gateway for graph-centric queries.  
  - Governance hooks (GovHooks v4) that:
    - Enforce CARE & sovereignty policies.  
    - Filter or generalize responses for sensitive content.  
    - Log all governance decisions to `data/provenance/`.

- **Frontend layer** (`web/`):

  - React-based SPA.  
  - MapLibre for 2D base maps and data overlays.  
  - Cesium for 3D scenes and time-dynamic views.  
  - Vite build for fast dev and optimized bundles.

This separation ensures clean boundaries while enabling shared telemetry and provenance across backend and frontend.

---

## 🔗 8. Provenance, OpenLineage, and Telemetry

`prov_profile` and `openlineage_profile` indicate that:

- PROV-O is the logical model used to describe:
  - Activities (ETL runs, training runs).  
  - Entities (datasets, models, docs).  
  - Agents (users, runners, services).  

- OpenLineage is the implementation used for:
  - Emitting events from pipelines in `src/pipelines/`.  
  - Aggregating lineage in `data/provenance/`.  
  - Powering lineage-aware dashboards and audits.  

Telemetry schemas in `schemas/telemetry/`:

- `root-architecture-v1.json` – architecture-level telemetry.  
- `energy-v2.json` – energy usage modeling for jobs.  
- `carbon-v2.json` – carbon intensity and emissions estimates.

CI pipelines and runtime services use these schemas to produce validated telemetry records, which are then merged into `releases/<version>/focus-telemetry.json`.

---

## 🧪 9. Validation, CI/CD, and Governance Integration

The `validation_profiles` list:

- `docs-lint-v11` – ensures Markdown structure follows KFM-MDP v11.2.2.  
- `schema-lint-v11` – guarantees JSON/YAML/LD syntax and schema conformance.  
- `lineage-audit-v11` – checks that all pipelines emit required lineage events.  
- `governance-audit-v11` – verifies FAIR+CARE and sovereignty compliance.

`ci_integration`:

```yaml
workflow: ".github/workflows/kfm-ci.yml"
environment: "dev → staging → production"
```

This ensures:

- All PRs must pass docs/schema/lineage/governance checks.  
- Deployments are gated on successful validation.  
- Architecture and standards documents like this one are enforced by CI and cannot drift silently.

---

## 🧾 10. Version History

| Version | Date       | Summary                                                                                                                   |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------------|
| v11.1.0 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; clarified ontology alignment, CI integration, telemetry schemas, and reliability/agent runtime. |
| v11.0.1 | 2025-11-23 | Aligned to v11 repo layout; documented runtime stacks, LangGraph & OpenLineage integration, and FAIR+CARE governance.    |
| v11.0.0 | 2025-11-19 | First v11 architecture blueprint; integrated ontology, CI, and runtime metadata.                                          |

---

<div align="center">

[⬅ Root README](README.md) · [📚 Docs Home](docs/README.md) · [⚖ Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
