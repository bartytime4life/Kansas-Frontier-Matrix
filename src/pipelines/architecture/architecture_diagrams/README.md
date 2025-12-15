---
title: "🖼️ Kansas Frontier Matrix — Pipeline Architecture Diagrams (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/architecture_diagrams/README.md"
version: "v11.0.0"
last_updated: "2025-12-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
release_stage: "Stable / Governed"

commit_sha: "<latest-commit-hash>"

sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/pipeline-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-diagrams-v1.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

doc_kind: "Architecture"
intent: "pipeline-architecture-diagrams-index"
role: "architecture-diagrams-registry"
category: "Pipelines · Architecture · Diagrams"

classification: "Public Architecture Documentation"
sensitivity: "Low"
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false
indigenous_data_flag: false

fair_category: "F1-A1-I2-R2"
care_label: "Public · Low-Risk"

doc_uuid: "urn:kfm:doc:pipelines:architecture:diagrams:v11.0.0"
semantic_document_id: "kfm-pipeline-architecture-diagrams"
event_source_id: "ledger:src/pipelines/architecture/architecture_diagrams/README.md"
immutability_status: "mutable-plan"

provenance_chain:
  - "src/pipelines/architecture/architecture_diagrams/README.md@v10.3.1"

ai_training_allowed: false
ai_training_guidance: "Do not use architecture diagrams or pipeline documentation as model training data."
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: false
ai_transform_permissions:
  - "summarize"
  - "extract-diagram-index"
  - "generate-navigation-aids"
ai_transform_prohibited:
  - "modify-normative-requirements"
  - "invent-nonexistent-diagrams"
  - "fabricate-governance-status"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States · Kansas"
lifecycle_stage: "operational"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next pipeline-architecture redesign"
---

<div align="center">

# 🖼️ **Kansas Frontier Matrix — Pipeline Architecture Diagrams**
`src/pipelines/architecture/architecture_diagrams/README.md`

**Purpose**  
Provide the **canonical, governed index** of Mermaid diagrams that describe KFM’s pipeline architecture:
ETL → validation → STAC/DCAT/PROV → Neo4j graph → APIs → UI → Story Nodes / Focus Mode, with
reliability (WAL · retries · idempotency) and observability (telemetry · sustainability) baked in.

</div>

---

## 📘 Overview

This directory contains **one-diagram-per-file** Mermaid sources (`.mmd`) used as canonical references for:

- Pipeline onboarding and architecture reviews
- Reliability design (retry, idempotency, outbox/WAL replay)
- Governance gates (FAIR+CARE + sovereignty-by-default)
- Telemetry and sustainability wiring (latency, energy, carbon)

These diagrams are intentionally **high-signal**:
they document “how the system should work” and must remain consistent with the surrounding
architecture specifications under `src/pipelines/architecture/`.

---

## 🗂️ Directory Layout

~~~text
📁 src/
└── 📁 pipelines/
    └── 📁 architecture/
        └── 📁 architecture_diagrams/
            ├── 📄 README.md                   — This index (canonical diagram registry)
            ├── 📄 ai_pipeline.mmd             — Focus Mode / AI pipeline flow (explainability + audit hooks)
            ├── 📄 etl_architecture.mmd        — ETL flow (extract → transform → validate → publish)
            ├── 📄 geospatial_processing.mmd   — Geospatial processing + asset packaging (COG/GeoParquet/etc.)
            ├── 📄 governance_flow.mmd         — Governance gates (CARE + sovereignty + promotion blocking)
            ├── 📄 idempotency_flow.mmd        — Deterministic replay (idempotency keys + outbox/WAL model)
            ├── 📄 lineage_flow.mmd            — Lineage chain (PROV-O / OpenLineage event model)
            ├── 📄 retries_flow.mmd            — Retry/backoff/circuit-breaker semantics
            └── 📄 telemetry_flow.mmd          — Observability (OTel metrics + energy/carbon signals)
~~~

---

## 🧭 Context

### How this folder fits into `src/pipelines/architecture/`

- This folder is the **visual companion** to the pipeline architecture specifications.
- Diagrams are referenced by architecture and governance documents and should not drift from:
  - contracts (KFM-PDC),
  - validation + promotion rules,
  - telemetry expectations,
  - sovereignty constraints.

### File conventions

- Each `.mmd` file MUST contain exactly **one** Mermaid diagram.
- Prefer **flowcharts** (`flowchart TD` or `flowchart LR`) for consistent rendering and linting.
- Keep labels short, stable, and governance-safe (no secrets, no sensitive coordinates, no PII).

---

## 🗺️ Diagrams

### Canonical diagram index

| Diagram file | Primary focus | Why it exists |
|---|---|---|
| `etl_architecture.mmd` | ETL pipeline shape | Makes extraction/transform/validation/publish ordering explicit |
| `geospatial_processing.mmd` | Raster/vector processing | Documents geospatial transforms and publishable asset generation |
| `ai_pipeline.mmd` | Focus Mode / AI flow | Shows explainability + audit checkpoints and data dependencies |
| `governance_flow.mmd` | Governance gates | Visualizes CARE + sovereignty enforcement and “fail closed” promotion rules |
| `lineage_flow.mmd` | Provenance | Documents PROV-O/OpenLineage semantics for traceability |
| `telemetry_flow.mmd` | Observability | Establishes required metrics and sustainability fields (energy/carbon) |
| `retries_flow.mmd` | Reliability | Standardizes retry/backoff/circuit-breaker semantics |
| `idempotency_flow.mmd` | Determinism | Standardizes replay safety via idempotency + WAL/outbox model |

### Mermaid guardrails

Diagrams MUST:

- Use Mermaid syntax only.
- Use `flowchart TD` or `flowchart LR`.
- Use quoted node labels (example: `A["Label text"]`) when any punctuation could be ambiguous.
- Avoid HTML in labels (no `<br/>`, no inline tags).
- Avoid styling/theming directives (keep diagrams CI-stable and renderer-agnostic).

### Minimal example

Plain-language: This example shows the canonical pipeline stages at a high level, without embedding
implementation details or sensitive information.

~~~mermaid
flowchart TD
  A["Raw inputs"] --> B["ETL pipeline"]
  B --> C["Validation: schema, CARE, integrity"]
  C --> D["Cataloging: STAC, DCAT, PROV"]
  D --> E["Graph load: Neo4j"]
  E --> F["APIs"]
  F --> G["UI: MapLibre, Story Nodes, Focus Mode"]
  G --> H["Telemetry + governance ledger"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

These diagrams support Story Node and Focus Mode by:

- providing consistent “system explanation” anchors for narrative summaries,
- clarifying where governance gates and provenance checks happen,
- enabling evidence-led explanations of pipeline behavior (without exposing sensitive details).

Diagrams MUST remain conceptual: they should explain **architecture and controls**, not embed
private data, operational secrets, or user-specific content.

---

## 🧪 Validation & CI/CD

### What is enforced

KFM-MDP requires consistent headings, fencing, directory layout formatting, and Mermaid safety rules.
Where enforced in CI depends on workflow scope, but current governed workflows include:

- `.github/workflows/docs_validate.yml` — Markdown + front-matter governance validation
- `.github/workflows/telemetry_export.yml` — telemetry aggregation/validation for governed workflows

### Author responsibilities when changing diagrams

When you modify any `.mmd` in this directory:

1. Update this index (keep descriptions accurate and governance-safe).
2. Ensure the diagram follows Mermaid guardrails and renders consistently.
3. Add a Version History entry (what changed and why).

---

## 📦 Data & Metadata

This README is the authoritative, human-readable diagram registry.

A machine-readable diagram registry file (e.g., JSON) is **not a hard dependency** here.
If a registry is added in the future, it MUST be backed by a repo schema under `schemas/**`
and reviewed under governance standards before becoming CI-required.

---

## 🌐 STAC, DCAT & PROV Alignment

- **DCAT**: This README can be modeled as a documentation `dcat:Dataset` / `dcat:CatalogRecord` with
  `semantic_document_id` as a stable identifier.
- **STAC**: If represented as a STAC Item, it should be non-spatial (`geometry: null`) with
  `properties.datetime = last_updated` and a markdown asset reference.
- **PROV-O**: This index functions as a `prov:Plan`; diagram updates are `prov:Activity` instances
  linked to a commit SHA and governance review when required.

---

## 🧱 Architecture

These diagrams collectively document the KFM pipeline contract:

- deterministic execution (idempotency + replay),
- reliable recovery (retries + compensation),
- governance enforcement (CARE + sovereignty gates),
- provenance by default (PROV/OpenLineage),
- observability and sustainability (telemetry + energy/carbon metrics).

---

## ⚖ FAIR+CARE & Governance

All diagrams in this directory MUST:

- remain compatible with FAIR+CARE governance requirements,
- avoid encoding sensitive locations, raw PII, credentials, or private infrastructure details,
- clearly represent where sovereignty protections and promotion blocks occur (at the architecture level).

If a diagram needs to reference Indigenous-data protections, keep it at the policy/control level and
avoid any location-specific representation.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---:|---|
| v11.0.0 | 2025-12-15 | Updated diagram index for KFM v11; corrected relative refs; removed stale metadata file dependency; aligned Mermaid guardrails and fencing rules with KFM-MDP v11.2.6; refreshed diagram descriptions for Focus Mode v3 + OTel-aligned telemetry. |
| v10.3.1 | 2025-11-13 | Introduced diagram index; established Mermaid-only, one-diagram-per-file structure and baseline governance expectations. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Visual Clarity × Ethical Transparency × Provenance by Design

[⬅️ Back to Pipeline Architecture](../README.md) ·
[📑 KFM-MDP Standard](../../../../docs/standards/kfm_markdown_protocol_v11.2.6.md) ·
[🛡 Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[⚖ FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Sovereignty Policy](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
