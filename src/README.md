---
title: "🧠 Kansas Frontier Matrix — Source Code & ETL Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"
backward_compatibility: "v11.0.0 → v11.2.x"

status: "Active / Canonical"
doc_kind: "Source Index"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:src:readme:v11.2.6"
semantic_document_id: "kfm-doc-src-readme"
event_source_id: "ledger:kfm:doc:src:readme:v11.2.6"
provenance_chain:
  - "src/README.md@v11.2.4"
  - "src/README.md@v11.0.0"

sbom_ref: "../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../releases/v11.2.6/manifest.zip"
signature_ref: "../releases/v11.2.6/signature.sig"
attestation_ref: "../releases/v11.2.6/slsa-attestation.json"

data_contract_ref: "../docs/contracts/data-contract-v3.json"

telemetry_ref: "../releases/v11.2.6/src-telemetry.json"
telemetry_schema: "../schemas/telemetry/src-etl-v11.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

validation_reports:
  - "../reports/self-validation/work-src-validation.json"
  - "../reports/fair/src_summary.json"
  - "../reports/audit/ai_src_ledger.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

intent: "src-etl-overview"
accessibility_compliance: "WCAG 2.1 AA+"
machine_extractable: true

classification: "Public"
jurisdiction: "Kansas / United States"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: true
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summarize"
  - "extract_task_checklist"
  - "metadata_extraction"
  - "navigation_generation"
  - "diagram_extraction"

ai_transform_prohibited:
  - "invent_sources_or_citations"
  - "invent_governance_status"
  - "fabricate_provenance_or_dataset_relationships"
  - "include_credentials_or_secrets"
  - "generate_sensitive_locations"

scope:
  domain: "src"
  applies_to:
    - "src/**"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"
  - "secret-scan"
  - "pii-scan"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  graph: "Semantics × Provenance × Spatial Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

fencing_profile: "outer-backticks-inner-tildes-v1"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Source Code & ETL Pipelines (v11.2.6 LTS)**
`src/README.md`

**Purpose**  
Describe the canonical source tree for the Kansas Frontier Matrix (KFM) — including ETL and AI pipelines, orchestration agents, validation engines, governance synchronization, telemetry collectors, graph + API services, and theming — aligned with FAIR+CARE, MCP-DL v6.3, and Diamond⁹ Ω / Crown∞Ω governance.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/License-MIT-green" />
<img src="https://img.shields.io/badge/Status-Stable%20%2F%20Governed-brightgreen" />

</div>

---

## 📘 Overview

The `src/` directory houses KFM’s automation and intelligence core:

- deterministic ETL and harmonization pipelines
- validation and governance gates (contracts, FAIR+CARE, sovereignty)
- Neo4j knowledge graph schema and ingest jobs
- API services for UI and narrative tooling
- orchestration agents (event-driven and scheduled)
- telemetry collectors for runtime, energy, carbon, and ethics events
- theming and UI token utilities used by frontends

All code under `src/` is expected to:

- respect governance and sovereignty constraints
- be reproducible (MCP-DL v6.3; config-driven execution)
- emit provenance and telemetry artifacts suitable for audit and replay

## 🗂️ Directory Layout

This is the intended (canonical) `src/` layout for v11.2.x. Individual modules may evolve, but new work should preserve these boundaries.

~~~text
📁 src/
├── 📄 README.md                                  — Source code and ETL overview (this document)
├── 📄 ARCHITECTURE.md                            — Source-layer architecture notes
│
├── 📁 pipelines/                                 — Automation pipelines (ETL, AI, validation, governance, telemetry)
│   ├── 📁 etl/                                   — Ingestion + transformation (batch and streaming)
│   ├── 📁 ai/                                    — Focus Mode tooling and model runners (rules-first; ML when justified)
│   ├── 📁 validation/                            — Schema, checksum, contracts, FAIR+CARE, sovereignty audits
│   ├── 📁 governance/                            — Ledger sync, provenance emitters, manifest synchronization
│   ├── 📁 telemetry/                             — Runtime, energy, carbon, and ethics event collectors
│   ├── 📁 remote-sensing/                        — Satellite and aerial processing + STAC publishing helpers
│   ├── 📁 updater/                               — Idempotent schedulers, webhooks, dry-run safe updaters
│   └── 📁 utils/                                 — Shared STAC/DCAT/JSON/metadata utilities
│
├── 📁 graph/                                     — Knowledge graph integration (Neo4j + semantic alignment)
│   ├── 📁 schema/                                — Constraints, ontology mappings (CIDOC, GeoSPARQL, OWL-Time)
│   ├── 📁 ingest/                                — Incremental, idempotent ingest + provenance sync jobs
│   ├── 📁 queries/                               — Cypher templates for Focus Mode and analytics
│   └── 📁 utils/                                 — Graph helpers and metadata bridges
│
├── 📁 server/                                    — API boundary (frontend must not query the graph directly)
│   ├── 📁 api/                                   — REST endpoints (search, focus, story nodes, datasets)
│   ├── 📁 graphql/                               — GraphQL schema and resolvers (when used)
│   └── 📁 middleware/                            — Auth, governance gates, telemetry middleware
│
├── 📁 agents/                                    — Orchestration agents (see `src/agents/README.md`)
│   ├── 📄 README.md                              — Agents and orchestration index
│   └── 📁 langgraph/                             — LangGraph-based agents and graphs
│
├── 📁 theming/                                   — Theming and adaptive UI utilities (tokens → CSS/JS)
│   ├── 📄 base.css
│   ├── 📄 light.css
│   ├── 📄 dark.css
│   ├── 📄 high-contrast.css
│   └── 📄 theme.js
│
├── 📁 design-tokens/                             — Design tokens used across frontends
│   └── 📁 tokens/
│
├── 🧾 metadata.json                              — Source registry (generated; checksums + provenance for critical files)
└── 📁 tests/                                     — Unit and integration tests for pipelines, graph, server, agents, theming
~~~

## 🧭 Context

The `src/` layer is the implementation side of the pipeline contract:

ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode.

Operational boundaries:

- frontend code must consume APIs and must not read raw data artifacts directly
- transformations must be deterministic, config-driven, and replayable
- derived data belongs under `data/processed/` (not under `src/`)
- provenance and rights must remain queryable and portable across catalogs and graph

## 🧱 Architecture

### Core responsibilities

`src/` is responsible for:

- ETL orchestration (multi-source ingestion, normalization, harmonization)
- AI enrichment and analysis helpers (Focus Mode components, explainability hooks)
- validation and governance gating (contracts, FAIR+CARE, sovereignty checks)
- knowledge graph construction (schema, ingest, query templates)
- telemetry and sustainability metrics (runtime, energy, carbon, ethics events)
- theming and UI utilities (tokens and accessible theme support)

### Determinism and configuration

Implementation expectations:

- no “magic constants” in pipeline code; tuneables live in config
- every run emits a config snapshot and a provenance trace
- ingestion and graph merges are incremental, idempotent, and version-aware
- validation failures must be explicit (no silent success paths)

## 🗺️ Diagrams

### End-to-end automation flow

~~~mermaid
flowchart LR
  A[Raw data sources] --> B[ETL pipelines: src/pipelines/etl]
  B --> C[Validation: src/pipelines/validation]
  C --> D[Governance sync: src/pipelines/governance]
  D --> E[Graph ingest: src/graph]
  E --> F[AI pipelines: src/pipelines/ai]
  F --> G[Telemetry: src/pipelines/telemetry]
  G --> H[API services: src/server]
  H --> I[Frontend and narratives]
~~~

Notes:

- agents under `src/agents/` may hook into any stage through events and schedules
- validations and governance checks must occur before publication or model training

## 🧠 Story Node & Focus Mode Integration

`src/` enables Story Node and Focus Mode features by providing:

- governed data access patterns (catalog-first, provenance-aware)
- narrative-safe transformations (no fabricated relationships, no policy overrides)
- explainability hooks for ML-assisted outputs (where model work is justified)
- safeguards for sovereignty and sensitivity constraints

Focus Mode behavior constraints (non-exhaustive):

- allowed: summarization, metadata extraction, navigation aids
- prohibited: invented sources, invented governance status, fabricated provenance links

## 🧪 Validation & CI/CD

Validation is CI-enforced via `test_profiles` and is expected to block merges on failure.

Typical coverage areas:

- ETL invariants (schema, CRS, units, and data contract validation)
- AI explainability and bias metrics (when applicable)
- governance sync and provenance integrity
- telemetry schema correctness and thresholds
- accessibility checks for theming utilities

`validation_reports` in front matter point to expected outputs used in audits and governance review.

## 📦 Data & Metadata

### `src/metadata.json` registry

`src/metadata.json` acts as the source-layer registry for:

- module inventory and stable identifiers
- checksums for critical artifacts (pipelines, manifests, agents)
- data contract and schema references
- provenance relationships across ETL, AI, governance, and graph integrations
- telemetry bundle references (`telemetry_ref`)

Example (documentation-safe):

~~~json
{
  "id": "src_registry_v11.2.6",
  "pipelines_registered": [
    "pipelines/etl/climate_stream_etl.py",
    "pipelines/ai/focus_transformer_v3.py",
    "pipelines/governance/governance_sync.py",
    "pipelines/telemetry/telemetry_reporter.py"
  ],
  "checksum_verified": true,
  "faircare_status": "certified",
  "governance_registered": true,
  "telemetry_ref": "../releases/v11.2.6/src-telemetry.json",
  "created": "2025-12-14T00:00:00Z",
  "validator": "@kfm-src-core"
}
~~~

Registry updates should be CI-controlled, not manual.

### Telemetry

Aggregated telemetry is release-pinned at:

~~~text
../releases/v11.2.6/src-telemetry.json
~~~

Telemetry expectations:

- runtime and throughput metrics (latency, I/O, memory)
- energy and carbon reporting aligned to the repo telemetry schemas
- governance and ethics events (masking, quarantine, approvals)

## 🌐 STAC, DCAT & PROV Alignment

`src/` produces and consumes assets in catalog-ready forms:

- STAC: publish derived geospatial assets as Items in stable Collections
- DCAT: ensure dataset discoverability, licensing, and distribution records
- PROV-O: attach lineage to runs, inputs, and outputs (Activities, Entities, Agents)

The graph ingest layer should preserve these links so users can trace:

source → transform → derived asset → narrative usage.

## ⚖ FAIR+CARE & Governance

### Enforcement matrix (implementation view)

| Principle | Implementation | Oversight |
|---|---|---|
| Findable | inventories and IDs in registries; catalog links | data stewardship |
| Accessible | public source licensing; documented APIs | accessibility and governance |
| Interoperable | STAC/DCAT + ontology alignment | architecture review |
| Reusable | deterministic pipelines; versioning and manifests | maintainers and CI |
| Collective Benefit | outputs designed for communities and research | FAIR+CARE Council |
| Authority to Control | sovereignty flags and publication gates | governance |
| Responsibility | telemetry, audits, and remediation workflow | sustainability |
| Ethics | bias and context checks for AI-assisted outputs | ethics review |

Sovereignty-sensitive modules must:

- propagate sovereignty and sensitivity flags into derived assets and graph nodes
- apply masking or generalization for restricted locations by default
- require explicit approval before publication when policies demand it

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| **v11.2.6** | 2025-12-14 | Updated to KFM-MDP v11.2.6; added heading registry and test profiles; normalized internal fences to `~~~`; removed Mermaid HTML labels; standardized footer links and governance references. |
| v11.2.4 | 2025-12-08 | Aligned `src/` overview with KFM-MDP v11.2.4; integrated agents index and patterns; updated telemetry paths and references. |
| v11.0.0 | 2025-11-24 | Upgraded to v11; integrated agents, reliability patterns, sovereignty rules, and expanded telemetry coverage. |
| v10.3.2 | 2025-11-16 | v10.x overview; Focus v2.x; STAC/DCAT ETL; telemetry v3; governance-ledger sync. |
| v10.1.0 | 2025-11-10 | Refactored streaming ETL; improved sustainability metrics and catalog bridge. |
| v10.0.0 | 2025-11-08 | Added AI reasoning and telemetry; baseline FAIR+CARE certification. |
| v9.7.0 | 2025-11-05 | Expanded telemetry and governance pipeline coverage. |

---

<div align="center">

🧠 **Kansas Frontier Matrix — Source Code & ETL Pipelines (v11.2.6 LTS)**  
Deterministic ETL → STAC/DCAT/PROV → Neo4j Graph → API → Web UI → Story Nodes → Focus Mode

[📚 Docs Portal](../docs/README.md) · [📂 Standards Index](../docs/standards/README.md) · [⚙ CI/CD Workflows](../docs/workflows/README.md) · [📊 Telemetry Docs](../docs/telemetry/README.md) · [🏛️ Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md) · [🤝 FAIR+CARE Guide](../docs/standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>