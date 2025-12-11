---
title: "📡 Kansas Frontier Matrix — ETL Governance Events Telemetry Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/etl-governance-events/specs/README.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/etl-governance-events-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/etl-governance-events-v11.2.6.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "telemetry-etl-governance-events"
  applies_to:
    - "docs/telemetry/etl-governance-events/**"
    - "schemas/telemetry/etl-governance-events/**"
    - "releases/*/etl-governance-events-telemetry.json"
    - "data/logs/etl-governance-events/**"
    - ".github/workflows/telemetry-export.yml"
    - "src/pipelines/**"
    - "tools/telemetry/emit_etl_governance_events.py"
    - "tools/telemetry/aggregate_etl_governance_events.py"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Operational telemetry; low-risk when aggregated"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by ETL Governance Events Telemetry Specification v12"

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
  - "docs/telemetry/etl-governance-events/specs/README.md@v11.2.4"
  - "docs/telemetry/etl-governance-events/specs/README.md@v10.2.2"
  - "docs/telemetry/etl-governance-events/specs/README.md@v10.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:etl-governance-events:specs:v11.2.6"
semantic_document_id: "kfm-telemetry-etl-governance-events-specs-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:etl-governance-events:specs:v11.2.6"
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
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "3d-context-render"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

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
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/telemetry-export.yml"
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
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 📡 **Kansas Frontier Matrix — ETL Governance Events Telemetry Specification**  
`docs/telemetry/etl-governance-events/specs/README.md`

**Purpose**  
Define the **canonical, governed JSON telemetry specification** for **ETL governance events** in the Kansas Frontier Matrix (KFM).  
This standard normatively specifies event types, required fields, schemas, lifecycle semantics, and governance hooks so that ETL pipelines emit **FAIR+CARE‑aligned**, **PROV‑traceable**, and **sustainability‑aware** telemetry.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![KFM‑MDP v11.2.6](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.6-purple)]()  
[![License · CC‑BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange)]()  
[![Status · Stable](https://img.shields.io/badge/Status-Stable%20%2F%20Enforced-brightgreen)]()

</div>

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 etl-governance-events/
        📄 README.md                      # High-level overview of ETL governance telemetry
        📁 specs/
        │   📄 README.md                  # ← This specification (normative)
        └── 📁 examples/
            📄 README.md                  # Example payload catalog (non-normative)
            📄 minimal_ingest_success.json
            📄 ingest_failure_retry.json
            📄 lineage_openlineage.json
            📄 focus_story_node.json

📁 schemas/
└── 📁 telemetry/
    └── 📁 etl-governance-events/
        📄 etl-governance-event-v11.2.6.json  # Single-event JSON Schema
        📄 etl-governance-batch-v11.2.6.json  # Batch (JSONL) wrapper schema

📁 data/
└── 📁 logs/
    └── 📁 etl-governance-events/
        └── 📁 2025/
            └── 📁 12/
                📄 etl-governance-events-2025-12-11.jsonl  # Production-style JSONL log

📁 tools/
└── 📁 telemetry/
    📄 emit_etl_governance_events.py      # CLI / library to emit events
    📄 aggregate_etl_governance_events.py # Aggregates logs → release telemetry

📁 releases/
└── 📁 v11.2.6/
    📄 etl-governance-events-telemetry.json # Aggregated ETL governance telemetry
    📄 sbom.spdx.json                       # SBOM for telemetry + ETL governance tooling
    📄 manifest.zip                         # Manifest (hashes, versions, references)
~~~

Any new schema or example added under `etl-governance-events` MUST be reflected in this layout and conform to the v11.2.6 schemas.

---

## 📘 Overview

This specification defines:

- **Event taxonomy** for ETL governance telemetry, including:
  - `run_started`, `ingest_succeeded`, `ingest_failed`, `governance_override`, `quarantined`, and related types.  
- **Canonical JSON shape** for individual events and JSONL batches.  
- **Normative semantics** for:
  - `governance_decision`, `faircare` block, `sustainability` block, and lineage fields.  
- **Integration expectations** with:
  - OpenLineage, DCAT/STAC, PROV-O, FAIR+CARE, and KFM sustainability telemetry.

This document is **normative** for:

- Schema evolution of `etl-governance-event-v11.2.6.json` and `etl-governance-batch-v11.2.6.json`.  
- How ETL pipelines under `src/pipelines/**` and CI workflows (e.g., `telemetry-export.yml`) emit and process events.  

Concrete JSON payloads in `docs/telemetry/etl-governance-events/examples/` are **illustrative**, not normative; if they disagree with this spec, **this spec wins**.

---

## 🧭 Context

Within the KFM pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

ETL governance events are the **operational memory** of ETL:

- Capture **what happened** (success/failure, retries, overrides).  
- Capture **why** (schema mismatch, FAIR+CARE violation, sovereignty rule).  
- Capture **cost** (energy, carbon, runtime).  
- Capture **impact** (datasets touched, Story Nodes created, governance decisions made).

They are:

- Produced by **pipelines and workflow runners**.  
- Validated and aggregated by **telemetry workflows**.  
- Consumed by **dashboards, graph, and Focus Mode** for observability and governance.

---

## 🗺️ Diagrams

### ETL Governance Events — Lifecycle

~~~mermaid
flowchart LR
  A[ETL pipeline run] --> B[Emit ETL governance events]
  B --> C[Append JSON events to log]
  C --> D[Validate against telemetry schemas]
  D --> E[Aggregate into release telemetry]
  E --> F[Update graph and catalogs]
  F --> G[Dashboards and Focus Mode]
~~~

---

## 🧠 Story Node & Focus Mode Integration

ETL governance events are designed to be **Story Node-aware**:

- Every event **MAY** include:
  - `story_node_ref`: stable Story Node URN, e.g.  
    `urn:kfm:story-node:etl:<pipeline_id>:<run_id>`  
  - `story_node_kind`: e.g. `"etl-run"`, `"etl-governance-decision"`.

- Focus Mode **MAY**:
  - Aggregate events over a `pipeline_id` or `dataset_ref` to narrate:
    - Reliability (success vs failure rate).  
    - Governance strictness (quarantines, overrides).  
    - Sustainability (energy and carbon per run).  
  - Link from other Story Nodes (e.g., model training) back to ETL provenance.

- Focus Mode **MUST NOT**:
  - Change `governance_decision`, `faircare` labels, or sovereignty flags.  
  - Invent events or interpolate missing history.  
  - Treat examples as production data.

This spec ensures events include enough **IDs and references** for Story Node graphs to be assembled without guesswork.

---

## 🧪 Validation & CI/CD

### 1. Schema & Telemetry Validation

The following workflows enforce this spec:

- `schema-lint.yml`  
  - Validates `etl-governance-event-v11.2.6.json` and `etl-governance-batch-v11.2.6.json` as JSON Schemas.  

- `telemetry-export.yml`  
  - Validates that:
    - `data/logs/etl-governance-events/*.jsonl` entries conform to the event schemas.  
    - Aggregated `etl-governance-events-telemetry.json` conforms to `etl-governance-events-v11.2.6.json`.

### 2. Normative CI Rules

- Any ETL pipeline that claims **governed status** MUST:
  - Emit events following this spec at key lifecycle points.  
  - Fail CI if events fail schema validation.  

- Telemetry aggregation MUST:
  - Reject logs containing unknown `event_type` values.  
  - Aggregate only events whose `schema_version` matches or is compatible with `v11.2.6` (per schema versioning rules).  

---

## 📦 Data & Metadata

### 1. Event Taxonomy (Normative)

`event_type` MUST be one of the registered values. Core types include:

- `run_started`  
- `ingest_succeeded`  
- `ingest_failed`  
- `transform_succeeded`  
- `transform_failed`  
- `governance_override`  
- `quarantined`  
- `abandonment_registered`  
- `abandonment_resolved`

Additional values MAY be registered via governance, but MUST be added to:

- This spec,  
- The JSON Schema enumeration,  
- The examples catalog (non-normative).

### 2. Core Event Fields (Single Event Schema)

At minimum, each event MUST include:

| Field                | Type      | Required | Description                                                       |
|---------------------:|-----------|----------|-------------------------------------------------------------------|
| `schema_version`     | string    | yes      | Telemetry schema identifier, e.g. `etl-governance-event-v11.2.6` |
| `event_id`           | string    | yes      | Globally unique identifier (URN recommended)                      |
| `event_type`         | string    | yes      | One of the registered event taxonomy values                      |
| `pipeline_id`        | string    | yes      | Stable pipeline identifier                                        |
| `run_id`             | string    | yes      | Identifies a single ETL run (unique per pipeline)                |
| `status`             | string    | yes      | `success`, `failed`, `partial`, or `skipped`                     |
| `governance_decision`| string    | yes      | `passed`, `failed`, `quarantined`, or `override-approved`        |
| `dataset_ref`        | string    | no       | STAC/DCAT identifier or URI                                      |
| `inputs`             | array     | no       | Input URIs or IDs                                                 |
| `outputs`            | array     | no       | Output URIs or IDs                                                |
| `faircare`           | object    | no       | FAIR+CARE policy version and issues                               |
| `sustainability`     | object    | no       | `energy_wh` and `carbon_gco2e`                                   |
| `timestamps`         | object    | yes      | `started_at`, `ended_at`, optionally `queued_at`                  |

#### 2.1 FAIR+CARE Block

The `faircare` object SHOULD contain:

- `policy_version` — e.g. `faircare@2025.4`.  
- `score` — numeric summary metric (0–1 or 0–100, defined in schema).  
- `issues` — list of short codes (`missing_care_tag`, `pii_unmasked`, etc.).

#### 2.2 Sustainability Block

The `sustainability` object SHOULD align with `energy-v2.json` and `carbon-v2.json`:

- `energy_wh` — numeric watt-hours for the run.  
- `carbon_gco2e` — grams CO₂ equivalent.  

### 3. Batch Schema (JSONL)

- The `etl-governance-batch-v11.2.6.json` schema governs:
  - Arrays of events in JSON, and  
  - Line-delimited JSONL files with one event per line.

- Batch-level metadata MAY include:
  - `file_id`, `source_system`, `ingested_at`, and hash-based checksums.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC

Aggregated ETL governance telemetry is exposed as STAC Items in a `kfm-telemetry-etl` Collection:

- `id` — e.g. `etl-governance-events-2025-12-11`.  
- `properties.datetime` — end of aggregation window.  
- `assets.etl-governance` — link to `etl-governance-events-telemetry.json` with `type: application/json`.  

Individual events are **not** STAC Items; they are:

- Optional per-run assets or  
- Referenced via links from domain collections (e.g. `kfm-lidar-glo`) to governance telemetry.

### 2. DCAT

At the DCAT layer:

- This spec → `dcat:Dataset` describing the telemetry standard.  
- Aggregated telemetry → separate `dcat:Dataset` with distributions:
  - `etl-governance-events-telemetry.json` (aggregated view).  
  - Compressed JSONL logs for raw events.

Each distribution SHOULD declare:

- `dcat:mediaType` (`application/json`, `application/x-ndjson`, etc.).  
- `spdx:checksum` referencing `manifest.zip`.  

### 3. PROV-O

This specification defines the shape of data used to represent:

- **Activities** — ETL runs (`prov:Activity`).  
- **Entities** — input/output datasets and governance reports (`prov:Entity`).  
- **Agents** — pipelines, CI runners, and governance councils (`prov:Agent`).  

Event fields map to PROV as follows (conceptual):

- `pipeline_id` + `run_id` → `prov:Activity` (`ex:ETLRun_<pipeline_id>_<run_id>`).  
- `inputs` → `prov:used` relations.  
- `outputs` → `prov:wasGeneratedBy` relations.  
- `governance_decision` → attributes on the Activity and/or associated governance Entity.

---

## 🧱 Architecture

ETL governance events fit into KFM’s architecture as:

- **Specification layer**  
  - This document + JSON Schemas define the contract.  

- **Emission layer**  
  - `emit_etl_governance_events.py` implements the contract for pipelines.  

- **Storage layer**  
  - Logs under `data/logs/etl-governance-events/**` store events as JSONL.  

- **Aggregation layer**  
  - `aggregate_etl_governance_events.py` produces release telemetry.  
  - `telemetry-export.yml` validates and uploads aggregated files.  

- **Analysis layer**  
  - Dashboards, graph, and Focus Mode use telemetry and provenance to analyze:
    - Reliability,
    - Governance decisions,
    - Sustainability.

All changes to:

- Event fields,  
- Event types,  
- Semantics of `governance_decision` and `faircare` blocks  

MUST be reflected here **before** schema evolution or code changes.

---

## ⚖ FAIR+CARE & Governance

This specification ensures ETL governance events:

- **FAIR**
  - Findable: stable `event_id`, `run_id`, and `pipeline_id`.  
  - Accessible: logs and telemetry in predictable storage paths.  
  - Interoperable: JSON Schema, DCAT/STAC, PROV, and OpenLineage mapping.  
  - Reusable: versioned schemas and documented semantics.

- **CARE**
  - Collective Benefit: governance decisions and sustainability costs are visible for community oversight.  
  - Authority to Control: sovereignty and FAIR+CARE violations are explicitly logged and can be audited.  
  - Responsibility: pipelines that repeatedly violate FAIR+CARE or sovereignty expectations are identifiable.  
  - Ethics: telemetry avoids embedding PII or sensitive coordinates; instead, it references governed dataset IDs and registry entries.

Events MUST NOT:

- Include raw PII.  
- Include precise coordinates for sensitive or sovereign sites (use generalized or redacted identifiers instead).  
- Misrepresent governance outcomes (e.g., log `"passed"` when FAIR+CARE failed).

---

## 🕰️ Version History

| Version   | Date       | Author             | Summary                                                                                                                      |
|----------:|-----------:|--------------------|------------------------------------------------------------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-telemetry`   | Aligned with KFM‑MDP v11.2.6; expanded normative field and event taxonomy definitions; added STAC/DCAT/PROV alignment details and Story Node integration; wired to v11.2.6 telemetry schemas. |
| v11.2.4   | 2025-12-06 | `@kfm-telemetry`   | Introduced governance_decision semantics and FAIR+CARE block; aligned sustainability fields with energy-v2/carbon-v2.       |
| v10.2.2   | 2025-11-12 | `@kfm-ops`         | Added OpenLineage alignment and batch schema; defined minimal ETL event set.                                                |
| v10.0.0   | 2025-11-10 | `@kfm-core`        | Established baseline ETL governance event schema and logging conventions.                                                   |

---

<div align="center">

📡 **Kansas Frontier Matrix — ETL Governance Events Telemetry Specification (v11.2.6)**  
Operational Observability · FAIR+CARE Governance · Focus-Ready ETL Narratives  

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-ETL_Governance_v11.2.6-informational" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Back to Telemetry Index](../README.md) ·  
[📄 ETL Governance Events Examples](../etl-governance-events/examples/README.md) ·  
[📘 Documentation Templates](../../templates/README.md) ·  
[⚙ CI/CD & Governance Workflows](../../workflows/README.md) ·  
[⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · FAIR+CARE Aligned · Diamond⁹ Ω / Crown∞Ω  

</div>