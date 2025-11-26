---
title: "🏗️ Kansas Frontier Matrix — Repository Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "ARCHITECTURE.md"
version: "v11.1.1"
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
doc_uuid: "urn:kfm:doc:architecture:repository:v11.1.1"
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

[Docs – MCP v6.3](#) · [FAIR+CARE](#) · [License: MIT](LICENSE) · [Status: Active](#-11-version-history) · [SBOM](releases/v11.0.0/sbom.spdx.json) · [Telemetry](releases/v11.0.0/focus-telemetry.json)

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
  FAIR+CARE, sovereignty, and data contracts are embedded into pipelines, CI, and deployment workflows.

- **Monorepo cohesion**  
  A single, cohesive repository with modular subtrees and strict standards, allowing atomic updates across code, data, and docs.

This document is the blueprint describing how those principles map onto the repository layout, runtime stacks, and CI/CD integration.

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
   - Immutable ingests from external providers (NOAA, USGS, archives, etc.).  
   - Managed via DVC/LFS or cloud storage, referenced in `data/sources/**` manifests.  

2. **Work (`data/work/`)**  
   - ETL staging and intermediate artifacts.  
   - Ephemeral and reproducible from raw + pipeline configuration.  

3. **Processed (`data/processed/`)**  
   - Cleaned, harmonized, contract-compliant outputs.  
   - Stored in interoperable formats (GeoJSON, COG GeoTIFF, Parquet, CSV).  

4. **Releases (`data/releases/`)**  
   - Versioned data bundles with SBOM, manifest, and telemetry.  

5. **Provenance (`data/provenance/`)**  
   - PROV-O datasets and OpenLineage logs.  
   - FAIR+CARE annotations and H3-masking metadata for sensitive layers.

STAC and DCAT definitions in `schemas/stac/` and `schemas/dcat/` ensure this lifecycle is reflected in machine-readable catalogs.

---

## 🧬 5. Ontology, Knowledge Graph, and Alignment

Ontology references:

- `docs/graph/ontology/core-entities.md`  
- `docs/graph/ontology/cidoc-crm-mapping.md`  
- `docs/graph/ontology/spatial-temporal-patterns.md`  

define:

- Core entity types (Place, Event, Dataset, Observation, Story Node, Agent).  
- Mappings into CIDOC-CRM, OWL-Time, and PROV-O.  
- Spatial-temporal patterns (e.g., H3 generalization rules, time intervals).

`ontology_alignment` fields describe how this architecture:

- Is a **CIDOC E29 Design or Procedure**.  
- Exposes as a **schema.org TechArticle** to external consumers.  
- Represents a **ProperInterval** in OWL-Time (v11 LTS window).  
- Functions as a **prov:Plan** describing KFM’s infrastructure.  
- References geospatial aspects as a **geo:FeatureCollection**.

The Neo4j schema in `src/graph/` is the concrete implementation of these ontologies.

---

## 🧠 6. Pipelines, Agents, and Reliability Engine

The runtime block encodes:

- `reliability_engine: "Reliable Pipelines v11 — WAL · Retry · Rollback · Hotfix · Lineage"`  
- `agents: "LangGraph Autonomous Updater v11"`  
- `lineage_bus: "OpenLineage v2.5"`  

Implications:

- All ETL and AI pipelines are LangGraph DAGs (`src/pipelines/`).  
- Each DAG node:
  - Emits OpenLineage events.  
  - Writes WAL entries for rollback and replay.  
  - Produces contract-validated outputs.  

- Autonomous agents:
  - Run governed data refresh jobs.  
  - Regenerate STAC/DCAT views.  
  - Propose new Story Nodes and Focus Mode narratives, subject to governance.

Detailed reliability patterns are documented in `docs/pipelines/reliable-pipelines.md`.

---

## 🧰 7. API, Frontend, and Runtime Stacks

From `runtime`:

- **Compute:**  
  - Multi-cloud mesh (AWS+GCP+On-Prem), enabling flexible deployment topologies.

- **Graph Engine:**  
  - Neo4j Enterprise v5.x cluster, backing all knowledge graph operations.

- **API Stack:**  
  - FastAPI + GraphQL Gateway (GovHooks v4) for:
    - Graph-centric queries.  
    - Governance hooks that apply CARE/sovereignty masking and log decisions.

- **Frontend Stack:**  
  - React + MapLibre + Cesium, built via Vite.  
  - Supports 2D and 3D views, timeline integration, Story Nodes, and Focus Mode.

All stacks share:

- Telemetry emission to `data/provenance/` and `releases/<version>/focus-telemetry.json`.  
- Governance integration for sensitive content and routes.

---

## 🔗 8. Provenance, Lineage, and Telemetry

`prov_profile` and `openlineage_profile` specify:

- PROV-O for conceptual lineage and plan/activity/entity modeling.  
- OpenLineage v2.5 + KFM Extensions for implementation detail.

Telemetry schemas:

- `schemas/telemetry/root-architecture-v1.json`  
- `schemas/telemetry/energy-v2.json`  
- `schemas/telemetry/carbon-v2.json`  

are used by pipelines and CI to produce:

- Architecture-level telemetry.  
- Energy and carbon estimates per job.  
- Governance and validation statistics.

Telemetry is consolidated into `releases/<version>/focus-telemetry.json`.

---

## 🧪 9. Validation, CI/CD, and Governance Integration

`validation_profiles`:

- `docs-lint-v11` – enforces KFM-MDP v11.2.2 structure and style.  
- `schema-lint-v11` – validates all JSON/YAML/LD artifacts.  
- `lineage-audit-v11` – ensures pipeline runs emit adequate lineage.  
- `governance-audit-v11` – checks FAIR+CARE, sovereignty, and license compliance.

`ci_integration`:

```yaml
workflow: ".github/workflows/kfm-ci.yml"
environment: "dev → staging → production"
```

ensures:

- All changes are validated before touching protected branches.  
- Architecture and standards documents are kept in sync with code, data, and schemas.  
- Governance audits are part of the normal CI cycle.

---

## 🧾 10. Version History

| Version | Date       | Summary                                                                                                                    |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------------|
| v11.1.1 | 2025-11-27 | Updated badges to single-line layout, aligned metadata with KFM-MDP v11.2.2, clarified runtime and validation profiles.    |
| v11.1.0 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; refreshed ontology references, runtime block, and CI integration metadata.                    |
| v11.0.1 | 2025-11-23 | Aligned to v11 repo layout; documented runtime stacks, LangGraph & OpenLineage integration, and FAIR+CARE governance.     |
| v11.0.0 | 2025-11-19 | Introduced v11 architecture blueprint integrating ontology, CI, data lifecycle, and monorepo design.                        |

---

<div align="center">

[Root README](README.md) · [📚 Docs Home](docs/README.md) · [⚖ Governance Charter](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
