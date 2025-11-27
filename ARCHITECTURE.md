---
title: "🏗️ Kansas Frontier Matrix — Repository Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "ARCHITECTURE.md"
version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
backward_compatibility: "Full v10.x → v11.x compatibility"
commit_sha: "<latest-commit-hash>"

signature_ref: "releases/v11.2.2/signature.sig"
attestation_ref: "releases/v11.2.2/slsa-attestation.json"
sbom_ref: "releases/v11.2.2/sbom.spdx.json"
manifest_ref: "releases/v11.2.2/manifest.zip"
telemetry_ref: "releases/v11.2.2/focus-telemetry.json"
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

[📘 Docs – MCP v6.3](docs/README.md) · [⚖️ FAIR+CARE](docs/standards/faircare/FAIRCARE-GUIDE.md) · [📜 License: MIT](LICENSE) · [📦 SBOM](releases/v11.2.2/sbom.spdx.json) · [📊 Telemetry](releases/v11.2.2/focus-telemetry.json)

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

- 🛰️ Remote sensing & EO  
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

Underneath is a **Neo4j graph** aligned with **CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O, and KFM Ontology v11**, with versioning, lineage, and governance enforced by this architecture.

---

## 🧱 2. Architectural Principles

KFM v11 is guided by:

- **Documentation-first (MCP-DL v6.3)**  
  All features, pipelines, and datasets have docs that satisfy KFM-MDP v11.2.2 and are checked in CI.

- **Semantic-first**  
  The graph and ontology are the system of record; other representations are views.

- **Deterministic Pipelines**  
  Pipelines use WAL, configs, and OpenLineage to ensure reproducible runs.

- **Governance-by-default**  
  FAIR+CARE, sovereignty, and data contracts are embedded into schemas, CI, and runtime policies—not bolted on.

- **Monorepo Cohesion**  
  Single repository, modular subtrees, shared governance, allowing atomic cross-layer updates.

This document describes how those principles are realized in the repo layout, data lifecycle, CI/CD, and runtime stacks.

---

## 🗂 3. Repository Layout (v11 · Emoji View)

~~~text
Kansas-Frontier-Matrix/
├── 📄 README.md                         # Root project overview (KFM v11)
├── 🏗️ ARCHITECTURE.md                   # This repository architecture & system blueprint
│
├── 📂 data/                             # Data hierarchy
│   ├── 📂 raw/                          # Raw external inputs (DVC/LFS pointers)
│   ├── 📂 work/                         # Staging + intermediates (reproducible)
│   ├── 📂 processed/                    # Cleaned, contract-compliant outputs
│   ├── 📂 stac/                         # STAC Items/Collections
│   ├── 📂 provenance/                   # PROV-O + OpenLineage logs
│   └── 📂 releases/                     # Versioned data bundles & artifacts
│
├── 📂 src/                              # Backend/ETL/AI code
│   ├── 📂 pipelines/                    # LangGraph DAGs, ETL/AI pipelines
│   ├── 🤖 ai/                           # Agents, models, prompts, explainers
│   ├── 🧠 graph/                        # Neo4j ingestion & schema tools
│   ├── 🌐 server/                       # FastAPI + GraphQL + GovHooks
│   └── 📊 telemetry/                    # Energy, IO, carbon, reliability telemetry
│
├── 🌍 web/                              # Front-end web app
│   ├── 🧩 src/                          # React, MapLibre, Cesium
│   ├── 📦 public/                       # Static assets
│   └── 🧾 meta/                         # SEO, manifests, extra metadata
│
├── 📚 docs/                             # Documentation
│   ├── ⚖️ standards/                    # Governance, heritage, H3, FAIR+CARE, etc.
│   ├── 🧱 architecture/                 # Deep architecture docs
│   ├── 📊 analyses/                     # Analyses & case studies
│   ├── 🛡️ governance/                   # Governance charters, policies
│   └── 🧩 templates/                    # MCP, SOP, Story Node templates
│
├── 🧾 schemas/                          # JSON, STAC, DCAT, JSON-LD, SHACL schemas
│   ├── 📊 telemetry/                    # Telemetry schema definitions
│   ├── 🛰️ stac/                         # KFM-STAC v11 profiles
│   ├── 📂 dcat/                         # KFM-DCAT v11 profiles
│   └── 🧩 jsonld/                       # JSON-LD contexts
│
├── 🧪 mcp/                              # Master Coder Protocol artifacts
│   ├── 🔬 experiments/                  # Experiment logs
│   ├── 📜 sops/                         # SOPs for pipelines, AI, governance, etc.
│   ├── 🧾 model_cards/                  # Model cards for AI/ML components
│   └── 📄 MCP-README.md                 # MCP usage and behavioral guidance
│
└── ⚙️ .github/                          # GitHub CI/CD & governance automation
    ├── 📄 README.md                     # GitHub infra overview
    ├── 🏗️ ARCHITECTURE.md               # CI/CD architecture blueprint
    └── 🤖 workflows/                    # Actions for CI/CD, audits, telemetry
~~~

This structure is canonical for v11; changes must go through architecture + governance review.

---

## 🌊 4. Data Lifecycle & Profiles

KFM defines a strict data lifecycle:

1. **Raw (`data/raw/`)**  
   - Immutable external inputs (NOAA, USGS, KHS, KGS, etc.).  
   - Managed via DVC/LFS or cloud storage; referenced via manifests.  

2. **Work (`data/work/`)**  
   - Pipeline staging area.  
   - Intermediate artifacts considered disposable and regenerable.  

3. **Processed (`data/processed/`)**  
   - Contract-compliant, harmonized datasets.  
   - Open formats (GeoJSON, COG, Parquet, CSV) for interoperability.  

4. **Releases (`data/releases/`)**  
   - Version-tagged output bundles with SBOM, manifest, telemetry.  

5. **Provenance (`data/provenance/`)**  
   - PROV-O graphs and OpenLineage events.  
   - CARE annotations and masking metadata.

STAC/DCAT schemas in `metadata_profiles` ensure data is:

- Findable and structured for external consumers.  
- Mappable into JSON-LD and graph-based serializations.

---

## 🧬 5. Ontology & Knowledge Graph Alignment

References in `ontology_ref` define:

- **Core Entities:** Place, Event, Dataset, Observation, Story Node, Agent.  
- **CIDOC-CRM Mapping:** For cultural heritage and provenance.  
- **Spatial-Temporal Patterns:** For OWL-Time and GeoSPARQL use.

`ontology_alignment` + `ontology_ref` state that:

- This doc is a **design/plan** (E29, prov:Plan) describing KFM’s infrastructure.  
- It advertises itself as a **TechArticle** to external knowledge graphs (schema.org).  
- It’s associated with a **ProperInterval** in time (the v11 LTS window).  
- It is geospatially relevant (FeatureCollection for covered datasets).

The Neo4j schema and ingestion code in `src/graph/` is the concrete implementation of this alignment.

---

## 🧠 6. Pipelines, Agents & Reliability Engine

From `runtime`:

- `reliability_engine: "Reliable Pipelines v11 — WAL · Retry · Rollback · Hotfix · Lineage"`  
- `agents: "LangGraph Autonomous Updater v11"`  
- `lineage_bus: "OpenLineage v2.5"`  

**Implications:**

- All ETL/AI pipelines are expressed as LangGraph DAGs (`src/pipelines/`).  
- Every DAG node:
  - Writes WAL entries to support rollback and replay  
  - Emits OpenLineage events for lineage observability  
  - Outputs data that adhere to KFM-PDC v11.0 contracts  

- Agents:
  - Manage scheduled and event-driven refreshes  
  - Provide governed, autonomous updates to STAC/DCAT catalogs and graph data  
  - Must obey `ai_transform_prohibited` (no modifying normative requirements in code or schemas)

Detailed behavior is further documented in `docs/architecture/pipelines/` and `docs/pipelines/reliable-pipelines.md`.

---

## 🧰 7. Runtime Stacks

### 7.1 Compute & Graph Engine

- **Compute:** `KFM Multi-Cloud Mesh (AWS + GCP + On-Prem)`  
  - Enables hybrid, region-aware, and cost-aware deployments.  

- **Graph Engine:** `Neo4j Enterprise v5.x Cluster`  
  - Backbone for all knowledge representation and queries.  

### 7.2 API Stack

- `FastAPI + GraphQL Gateway (GovHooks v4)`  
  - REST endpoints and GraphQL schema for queries and mutations.  
  - GovHooks enforce authorization, CARE masking, and logging.

### 7.3 Frontend Stack

- `React · MapLibre · Cesium · Vite Build`  
  - User-facing map, timeline, Story Node, Focus Mode UIs.  
  - Architecture defined in `web/README.md` and `web/ARCHITECTURE.md`.

### 7.4 Lineage & Reliability

- `OpenLineage v2.5` as the lineage bus.  
- Reliable pipelines (Retry, Rollback, Hotfix) ensure that:
  - Failures are detected and surfaced.  
  - Recovery paths are well defined.  
  - Governance logs are kept up to date.

---

## 🔗 8. Provenance, Lineage & Telemetry

`prov_profile: "PROV-O Core + KFM Lineage Extensions"` and `openlineage_profile: "OpenLineage v2.5 + KFM Extensions"` indicate:

- Conceptual lineage is modeled with PROV-O.  
- Operational lineage is recorded via OpenLineage, with KFM-specific extensions.  

Telemetry schemas (`telemetry_schema`, `energy_schema`, `carbon_schema`) are used to:

- Log architectural-level events and decisions.  
- Record energy/carbon usage for pipelines and services.  
- Support sustainability reporting and optimization.

Telemetry is published into `releases/<version>/focus-telemetry.json` and referenced by SBOM and manifest.

---

## 🧪 9. Validation, CI/CD & Governance Integration

`validation_profiles` specify:

- **docs-lint-v11** — KFM-MDP v11.2.2 style and structural checks.  
- **schema-lint-v11** — JSON, YAML, STAC, DCAT, JSON-LD, and SHACL validation.  
- **lineage-audit-v11** — Ensures pipelines emit adequate, interpretable lineage.  
- **governance-audit-v11** — Enforces FAIR+CARE, sovereignty, and license constraints.

`ci_integration` ensures these profiles are enforced in:

```yaml
workflow: ".github/workflows/kfm-ci.yml"
environment: "dev → staging → production"
```

Any violation in these profiles blocks merges to protected branches, preserving architectural integrity.

---

## 🧾 10. Version History

| Version | Date       | Summary                                                                                                              |
|--------:|------------|----------------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Applied full KFM-MDP v11.2.2 styling; kept all metadata; added emoji directory layout and upgraded release links.   |
| v11.1.1 | 2025-11-27 | Refined runtime and validation profiles; clarified governance integration with CI/CD and telemetry.                 |
| v11.1.0 | 2025-11-27 | Upgraded to v11.2.2 Markdown Protocol; aligned ontology and dataset lifecycles with KFM-STAC/DCAT v11.              |
| v11.0.1 | 2025-11-23 | Expanded runtime description; documented LangGraph + OpenLineage integration; clarified monorepo layout.            |
| v11.0.0 | 2025-11-19 | Established v11 LTS repository architecture; integrated ontology, CI, and multi-layer dataflow blueprint.           |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](README.md) · [📚 Docs Home](docs/README.md) · [🛡️ Governance](docs/standards/governance/ROOT-GOVERNANCE.md)

</div>