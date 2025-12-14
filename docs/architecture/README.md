---
title: "🏗️ Kansas Frontier Matrix — System Architecture & Design Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/architecture/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly / FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
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

classification: "Public"
jurisdiction: "Kansas / United States"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:architecture:readme:v11.2.6"
semantic_document_id: "kfm-doc-architecture-readme"
event_source_id: "ledger:kfm:doc:architecture:readme:v11.2.6"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/system-architecture-v3.json"
data_contract_ref: "../contracts/data-contract-v3.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summarize"
  - "extract_task_checklist"
  - "metadata_extraction"
  - "navigation_generation"

ai_transform_prohibited:
  - "invent_sources_or_citations"
  - "invent_governance_status"
  - "fabricate_provenance_or_dataset_relationships"
  - "include_credentials_or_secrets"
  - "generate_sensitive_locations"

scope:
  domain: "architecture"
  applies_to:
    - "docs/architecture/**"
---

<div align="center">

# 🏗️ Kansas Frontier Matrix — **System Architecture & Design Framework (v11.2.6)**
`docs/architecture/README.md`

**Purpose**  
Define the architectural blueprint and design framework for the Kansas Frontier Matrix (KFM). This document connects geospatial, historical, ecological, and security domains inside a unified, governed architecture that is reproducible, provenance-aware, and safe for Story Node / Focus Mode use.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/License-MIT-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange" />
<img src="https://img.shields.io/badge/Status-Stable%20%2F%20Governed-brightgreen" />

</div>

---

## 📘 Overview

The System Architecture & Design Framework describes the full-stack, ontology-driven, containerized ecosystem that powers KFM. It integrates geospatial, tabular, textual, and streaming data across environmental, cultural, historical, and security domains, with end-to-end governance automation and telemetry.

### 🎯 Strategic objectives

- 🧱 Modular, domain-separated architecture (climate, hazards, hydrology, treaties, archaeology, ecology, historical).
- ⚙️ Reproducible ETL + enrichment pipelines aligned to MCP-DL v6.3.
- 🔐 Verifiable provenance and supply-chain integrity (SBOMs, attestations, checksum policy).
- 🌎 Interoperability-first design (STAC, DCAT, PROV-O, GeoSPARQL, CIDOC-CRM, OWL-Time).
- 🤖 Focus Mode integration for evidence-led narrative and explainable insights across layers.
- 🛡️ Security-by-design (threat modeling, secrets policy, supply-chain controls, IR runbooks).

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 architecture/                              — System architecture and design framework docs
    ├── 📄 README.md                              — System Architecture & Design Framework (this file)
    ├── 📄 data-architecture.md                   — Data model notes (STAC/DCAT/CIDOC/GeoSPARQL/OWL-Time)
    ├── 📄 api-architecture.md                    — API boundary (FastAPI/GraphQL) + graph access patterns
    ├── 📄 web-ui-design.md                       — MapLibre/Cesium UI design + accessibility conventions
    ├── 📄 github-architecture.md                 — CI/CD + governance automation design
    ├── 📄 validation-framework.md                — Validation system (FAIR+CARE, schema gates, quality checks)
    ├── 📄 telemetry-architecture.md              — Sustainability, cost, energy, and operational telemetry model
    ├── 📄 predictive-framework.md                — Predictive scenario modeling + projection asset patterns
    ├── 📄 data-flow-diagrams.md                  — Visual architecture + data flow diagrams
    └── 📄 repo-focus.md                          — Monorepo module boundaries and integration points
~~~

Related entry points:

- Analyses: `../analyses/README.md`
- Security: `../security/README.md`
- Workflows: `../workflows/README.md`
- Standards: `../standards/README.md`

## 🧭 Context

KFM architecture is organized around a strict boundary: the frontend consumes only APIs, and the APIs are the only supported boundary to catalogs and the knowledge graph.

Pipeline placement:

ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode.

### 🧾 Internal reference

~~~text
Kansas Frontier Matrix (2025). System Architecture & Design Framework (v11.2.6).
Governed system design for data, AI, security, and web experiences with provenance and telemetry.
~~~

## 📦 Data & Metadata

Release-pinned architecture artifacts:

- SBOM: `sbom_ref`
- Manifest bundle: `manifest_ref`
- Telemetry export: `telemetry_ref`
- Telemetry schema: `telemetry_schema`
- Data contract: `data_contract_ref`

Documentation must not embed sensitive operational endpoints. Use stable repo paths and release-pinned artifacts instead.

## 🧱 Architecture

### ⚙️ End-to-end architecture workflow

1. **ETL pipelines**: fetch, clean, normalize, and checksum input data.
2. **Catalog registration**: register governed assets in STAC/DCAT, link to distributions.
3. **Validation**: enforce FAIR+CARE, contracts (JSON Schema), and basic ISO-aligned metadata gates.
4. **AI enrichment**: NER, geocoding, summarization, embeddings, explainability (rules-first, ML only when needed).
5. **Graph integration**: incrementally merge into Neo4j (idempotent, version-aware).
6. **API layer**: task-shaped endpoints for time/space filters, entity lookups, traversals, provenance traces.
7. **Frontend & narratives**: map/timeline UI renders API outputs; Story Nodes and Focus Mode compose evidence-led narratives.
8. **Telemetry**: record runtime, energy, CO₂e, and governance outcomes; export to release telemetry.

### 🧩 System blueprint (layered design)

| Layer | Function | Standards (non-exhaustive) |
|---|---|---|
| Data layer | ingest and normalize open/archival/streaming data | FAIR+CARE, ISO 19115 |
| Work layer | staging + validation; contract-aligned transforms | MCP-DL v6.3 |
| AI/Analytics layer | enrichment, predictive models, explainability | FAIR+CARE, PROV-O |
| Knowledge graph | Neo4j semantics, traversal, provenance linking | CIDOC-CRM, GeoSPARQL, OWL-Time |
| Governance layer | ethics, publication gating, audits | FAIR+CARE Council |
| Security layer | threat model, secrets, provenance, IR, prompt defense | STRIDE/LINDDUN, SLSA-style controls |
| Web layer | MapLibre/Cesium UI, a11y-first interaction | WCAG 2.1 AA, WAI-ARIA |

### 🛡️ Integrated security architecture (excerpt)

| Control domain | Primary controls | Where enforced |
|---|---|---|
| Threat modeling | STRIDE/LINDDUN risk register | `docs/security/threat-model.md` |
| Supply chain | SBOMs, provenance attestations, signing | `sbom_ref`, `manifest_ref` |
| Secrets | least privilege, rotation, scanning | `docs/security/secrets-policy.md` |
| IR & recovery | runbooks and evidence trails | `docs/security/incident-response.md` |
| Prompt defense | tool allowlists, sandboxed rendering | `docs/security/prompt-injection-defense.md` |

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[External data sources] --> B[ETL pipelines]
  B --> C[Catalog registration: STAC and DCAT]
  C --> D[Validation: schema, FAIR+CARE, contracts]
  D --> E[AI enrichment and analytics]
  E --> F[Knowledge graph merge: Neo4j]
  F --> G[API layer: task-shaped endpoints]
  G --> H[Frontend: Map, Timeline, Focus Mode]
  D --> I[Governance ledger and audits]
  I --> J[Telemetry export]
  J --> K[Release artifacts]
~~~

## 🧠 Story Node & Focus Mode Integration

Architecture requirements for Story Nodes and Focus Mode:

- UI consumes only APIs; Story Nodes never read raw files directly.
- Story Nodes are structured entities: title, narrative text, spatial extent, temporal extent, linked graph entities, and evidence links.
- Narrative must separate and label facts (source-backed), interpretation (reasoned), and speculation (explicitly hypothetical).
- Sovereignty and safety constraints apply by default: sensitive sites must be generalized or withheld.

## 🧪 Validation & CI/CD

Architecture documentation and its referenced artifacts are expected to pass repo CI profiles.

Workflow documentation (typical set):

| Workflow doc | Purpose | Artifacts |
|---|---|---|
| `docs/workflows/docs-lint.yml.md` | Markdown/front-matter, heading registry, fence rules, footer links | docs lint report |
| `docs/workflows/faircare-validate.yml.md` | FAIR+CARE audits, PII scan, quarantine registry | audit summary |
| `docs/workflows/stac-validate.yml.md` | STAC/DCAT validation + asset/checksum checks | validation report |
| `docs/workflows/site.yml.md` | build/deploy docs and portals with provenance | site artifacts |
| `docs/workflows/ai-train.yml.md` | training, drift/explainability, model artifacts | model reports |
| `docs/workflows/telemetry-export.yml.md` | merge metrics to telemetry release file | `telemetry_ref` |

Quarantine policy (architecture-level):

- Any dataset flagged by FAIR+CARE validation must not flow into AI or publication until remediated and council-approved.

### 📊 Predictive and sustainability telemetry

Telemetry reference: `telemetry_ref`.

Example targets (project-level; enforce per workflow where applicable):

| Metric | Target | Source |
|---|---:|---|
| FAIR+CARE alignment | 100% | FAIR+CARE validation |
| Ethical drift detection | enabled | model cards + audits |
| Energy per build (Wh) | ≤ 25 | telemetry |
| CO₂e reporting | required | telemetry |

## 🌐 STAC, DCAT & PROV Alignment

Interoperability principles:

- **STAC**: catalog geospatial and derived assets; validate and version outputs.
- **DCAT**: dataset discoverability, licensing, and distribution records.
- **PROV-O**: mandatory lineage for inputs, transforms, and outputs.
- **CIDOC-CRM + GeoSPARQL**: unify cultural heritage and spatial semantics.
- **OWL-Time**: anchor temporal reasoning for events and intervals.

Predictive projections:

- Modeled futures must be exported as cataloged assets and linked back to the generating `prov:Activity`.
- Predictive narratives must preserve the fact/interpretation/speculation separation.

## ⚖ FAIR+CARE & Governance

Hard constraints (architecture-level):

- Governance is a hard boundary: no bypass paths around review, masking, or publication gates.
- No secrets in docs: credentials, tokens, private keys, and internal endpoints are prohibited.
- Indigenous data sovereignty: apply default masking/generalization and follow the sovereignty policy for culturally sensitive knowledge.
- Least privilege: each subsystem and pipeline should have only the access it needs.

Primary references:

- Governance: `governance_ref`
- Ethics / FAIR+CARE: `ethics_ref`
- Sovereignty: `sovereignty_policy`

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| **v11.2.6** | 2025-12-14 | Updated to KFM-MDP v11.2.6 formatting; normalized fences to `~~~`; aligned heading registry compliance; fixed footer to include governance, ethics, and sovereignty links; updated release-pinned refs. |
| v10.2.3 | 2025-11-09 | Added integrated Security Layer, updated workflows table, refreshed telemetry refs and interoperability notes. |
| v10.2.2 | 2025-11-09 | Linked analyses and security directories; clarified governance and predictive exports as cataloged assets. |
| v9.9.2 | 2025-11-08 | Added data-flow diagrams and synchronized references to telemetry and predictive architecture. |

---

[⬅ Back to Documentation Index](../README.md) · [📂 Standards Index](../standards/README.md) · [🏛️ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) · [🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) · [🪶 Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)