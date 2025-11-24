---
title: "🏗️ Kansas Frontier Matrix — Repository Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "ARCHITECTURE.md"
version: "v11.0.1"
last_updated: "2025-11-23"
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
markdown_protocol_version: "KFM-MDP v11.0.0"
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
doc_uuid: "urn:kfm:doc:architecture:repository:v11.0.1"
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

- **Documentation-first (MCP-DL v6.3):** every feature, pipeline, and dataset has accompanying documentation and metadata.  
- **Semantic-first:** all core entities and relationships live in the knowledge graph, with STAC/DCAT/JSON-LD views as projections.  
- **Deterministic pipelines:** ETL and AI pipelines are reproducible via WAL, configs, and OpenLineage logs.  
- **Governance-by-default:** FAIR+CARE, sovereignty, and data contracts guardrails are built into pipelines and CI/CD.  
- **Monorepo cohesion:** a single repository with clear, modular boundaries and shared standards.  

This document describes how those principles are reflected in the physical repository layout and system components.

---

## 🗂 3. Repository Layout (Option B, v11)

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
````

This layout is designed for **clarity, testability, and governance** while keeping everything in a single monorepo.

---

## 🌊 4. Data Lifecycle & Profiles

KFM data flows through a well-defined lifecycle:

1. **Raw (`data/raw/`)**  
   - External sources (NOAA, USGS, archives, museums, etc.)  
   - Stored via DVC/LFS pointers and not committed as full-size binaries  
   - Described via `data/sources/**` manifests and STAC/DCAT entries  

2. **Work (`data/work/`)**  
   - ETL staging area, ephemeral intermediates  
   - Used by LangGraph pipelines during transformations  
   - Not considered stable for reproducibility beyond pipeline logs  

3. **Processed (`data/processed/`)**  
   - Cleaned, harmonized datasets ready for analysis and visualization  
   - Bound to KFM-PDC v11 data contracts and KFM-STAC/DCAT profiles  

4. **Releases (`data/releases/`)**  
   - Public-facing, versioned data bundles  
   - Associated `manifest.zip`, `sbom.spdx.json`, `focus-telemetry.json` per version  

5. **Provenance (`data/provenance/`)**  
   - PROV-O models and OpenLineage event logs  
   - FAIR+CARE governance annotations, including masking levels and sensitivity tags  

STAC and DCAT profiles:

- `stac_profile: "KFM-STAC v11"` → describes KFM-specific STAC metadata requirements  
- `dcat_profile: "KFM-DCAT v11"` → describes DCAT 3.0 usage for KFM datasets  

These profiles ensure consistent, machine-readable metadata across the entire lifecycle.

---

## 🧬 5. Knowledge Graph & Ontologies

The **knowledge graph** is the semantic backbone:

- **Neo4j Enterprise v5.x cluster** as the runtime graph engine  
- Ontology references in `ontology_ref`:

  - `docs/graph/ontology/core-entities.md`  
  - `docs/graph/ontology/cidoc-crm-mapping.md`  
  - `docs/graph/ontology/spatial-temporal-patterns.md`  

- Ontology alignment fields:

  - `cidoc: "E29 Design or Procedure"`  
  - `schema_org: "TechArticle"`  
  - `owl_time: "ProperInterval"`  
  - `prov_o: "prov:Plan"`  
  - `geosparql: "geo:FeatureCollection"`  

Graph ingestion:

- Implemented in `src/graph/`  
- Pipelines implement bidirectional mapping:

  - STAC/DCAT → graph  
  - Graph → JSON-LD views (for external integration)  

The graph is the authoritative source for **relationships**, while STAC/DCAT provide **catalog** views.

---

## 🧠 6. Pipelines, Agents, and Reliability Engine

The runtime section describes:

- `reliability_engine: "Reliable Pipelines v11 — WAL · Retry · Rollback · Hotfix · Lineage"`  
- `agents: "LangGraph Autonomous Updater v11"`  
- `lineage_bus: "OpenLineage v2.5"`  

This reflects:

- Deterministic ETL with WAL and retries  
- Hotfix and rollback primitives used in pipelines and CI flows  
- OpenLineage events for each task and job, tied into `data/provenance/`  
- Autonomous update agents that can:

  - Refresh STAC/DCAT metadata  
  - Regenerate derived data where safe and approved  
  - Propose Story Node updates (subject to human governance)  

The architecture ensures reliability without sacrificing governance visibility.

---

## 🧰 7. API & Frontend Stacks

The `runtime` block defines:

- `api_stack: "FastAPI + GraphQL Gateway (GovHooks v4)"`  
- `frontend_stack: "React · MapLibre · Cesium · Vite Build"`  

This is implemented as:

- **Server layer (`src/server/`)**:

  - FastAPI endpoints for REST-style interactions  
  - GraphQL gateway for complex graph traversals  
  - Governance hooks for CARE, sovereignty, and audit logging  

- **Frontend (`web/`)**:

  - React components for UI  
  - MapLibre for 2D mapping  
  - Cesium for 3D terrain and time-dynamic scenes  
  - Vite-based build system  

The repository architecture reflects this by separating backend (`src/`) and frontend (`web/`) with shared standards in `docs/` and `schemas/`.

---

## 🔗 8. Provenance, OpenLineage, and Telemetry

The architecture is explicitly tied to:

- `prov_profile: "PROV-O Core + KFM Lineage Extensions"`  
- `openlineage_profile: "OpenLineage v2.5 + KFM Extensions"`  

This means:

- Every pipeline run emits OpenLineage events  
- PROV-O based lineage objects are stored under `data/provenance/`  
- Telemetry schemas in `schemas/telemetry/` define:

  - Energy usage (`energy_schema`)  
  - Carbon emissions (`carbon_schema`)  
  - Architecture-level telemetry (`telemetry_schema`)  

The CI and runtime systems export telemetry to `releases/<version>/focus-telemetry.json`, which in turn drives dashboards and governance reporting.

---

## 🧪 9. Validation, CI/CD, and Governance Integration

The architecture includes validation profiles:

- `docs-lint-v11`  
- `schema-lint-v11`  
- `lineage-audit-v11`  
- `governance-audit-v11`  

Plus CI integration:

```yaml
ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
```

This ensures:

- Documentation compliance with **KFM-MDP v11**  
- Schema validation for STAC/DCAT/JSON-LD/telemetry/Story Node documents  
- Lineage audits across PROV-O + OpenLineage data  
- Governance audits for FAIR+CARE and sovereignty policies  

CI/CD specifics are detailed in `.github/ARCHITECTURE.md` and `.github/README.md`.

---

## 🧾 10. Version History

| Version |       Date | Summary                                                                                              |
|--------:|-----------:|------------------------------------------------------------------------------------------------------|
| v11.0.1 | 2025-11-23 | Upgraded to KFM-MDP v11 structure; clarified repo layout, runtime mapping, profiles, and CI linkage. |
| v11.0.0 | 2025-11-19 | First v11 architecture blueprint; integrated ontology, CI, and runtime metadata.                     |

---

[Root README](README.md) · [Docs Home](docs/README.md) · [Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)
