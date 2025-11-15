---
title: "🛠️ Kansas Frontier Matrix — Unified Reliable Pipeline Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/reliable-pipelines.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v10.4.0/sbom.spdx.json"
manifest_ref: "releases/v10.4.0/manifest.zip"
telemetry_ref: "releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/pipelines-reliable-updaters-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "architecture"
fair_category: "F1-A1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "src/pipelines/architecture/reliable-pipelines.md@v1.0.0"
  - "src/pipelines/architecture/reliable-pipelines.md@v10.3.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "schemas/json/pipelines-reliable-pipelines.schema.json"
shape_schema_ref: "schemas/shacl/pipelines-reliable-pipelines-shape.ttl"
doc_uuid: "urn:kfm:doc:pipelines-reliable-pipelines-v10.4.0"
semantic_document_id: "kfm-doc-pipelines-reliable-pipelines"
event_source_id: "ledger:src/pipelines/architecture/reliable-pipelines.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "architecture"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon new protocol release"
---

<div align="center">

# 🛠️ **Kansas Frontier Matrix — Unified Reliable Pipeline Architecture**  
`src/pipelines/architecture/reliable-pipelines.md`

**Purpose:**  
Define the *authoritative, enforceable* reliability standard for all KFM pipelines and updaters:  

> **Triggers → light AI (schema only) → deterministic ETL → validation gates → idempotent upsert → metadata/versioning → blue/green publish → alerts & telemetry**,  
> with **safe retries, rollback, and resume** enforced at the architecture level.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../docs/README.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Low%20Risk-orange)](../../docs/standards/faircare.md)  
[![Status: Enforced](https://img.shields.io/badge/Status-Enforced-success)](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

---

## 📘 Overview

This document specifies the **Unified Reliable Pipeline Architecture** for Kansas Frontier Matrix (KFM). It merges and supersedes all prior “Reliable Updaters” and “Reliable Pipeline Architecture” guides into a single **Diamond⁹ Ω / Crown∞Ω Ultimate Certified** standard.

Reliable pipelines in KFM are:

- **Deterministic:** same inputs + same config → same outputs.  
- **Idempotent:** safe under at-least-once delivery, with exactly-once effects at the boundary.  
- **Rollback-safe:** blue/green pointer flips, never destructive edits.  
- **Observable:** structured logs, metrics, traces, FAIR+CARE telemetry.  
- **Replayable:** checkpoints and immutable artifacts enable safe re-runs.  

Any pipeline that does not comply with this standard MUST NOT be deployed.

---

## 🎯 Purpose

The purposes of this standard are to:

- Provide a **single, enforceable pattern** for all KFM pipelines and updaters.  
- Ensure **idempotent, observable, rollback-safe** behavior across ingestion, ETL, graph updates, and publishing.  
- Align pipeline design with:
  - **Master Coder Protocol (MCP-DL v6.3)**  
  - **Markdown Structural & Formatting Rules v10.4**  
  - **FAIR+CARE governance**  

**Primary consumers:**

- Pipeline authors (Python, SQL, Neo4j, STAC tooling).  
- Architecture and SRE teams.  
- FAIR+CARE Council and governance bodies verifying reliability posture.

---

## 📍 Scope

### In Scope

- All code and configuration under `src/pipelines/**` that:
  - Reads from `data/sources/**`, `data/raw/**`, or external APIs/streams.  
  - Writes to `data/work/**`, `data/processed/**`, `data/stac/**`, or Neo4j.  
- All pipelines that:
  - Perform ETL (batch or streaming).  
  - Update KFM knowledge graph or STAC/DCAT catalogs.  
  - Affect user-facing maps, timelines, Focus Mode, or Story Nodes.

### Out of Scope

- Pure frontend logic that does not depend on pipeline guarantees.  
- Ad-hoc notebooks used solely for one-off analysis.  
- External upstream providers’ internal architectures.

**Related documents:**

- `src/ARCHITECTURE.md` — global system architecture.  
- `src/pipelines/architecture/observability/README.md` — observability standard.  
- `docs/standards/markdown_rules.md` — Markdown protocol.  

---

## 📚 Definitions

- **Pipeline / Updater:** A repeatable process that ingests, transforms, validates, and publishes data or knowledge into KFM.  
- **Trigger:** The mechanism that starts a run (cron, event, manual), bundled with a *trigger envelope*.  
- **Idempotency Key (run-level):** A hash of the trigger envelope used to prevent double-processing of the same run.  
- **Natural Key (record-level):** Minimal, stable business identity for each record (e.g., `(station_id, date)`).  
- **Content Hash:** Hash of the **normalized record without runtime fields** (no timestamps, no ephemeral IDs).  
- **Blue/Green:** Dual dataset pattern where one version serves (blue) and another is candidate (green).  
- **Checkpoint:** Persisted cursor (date/page/offset) for resume.  
- **DLQ (Dead Letter Queue):** Durable storage for work items that failed beyond allowed retries.  
- **Artifact:** Any derived dataset (COG, Parquet, CSV, GeoJSON, STAC item, etc.) whose integrity is tracked.  
- **Run ID:** Unique identifier of a single pipeline execution.

---

## 🏗 Architecture / Context

### System Context

~~~~~mermaid
flowchart TD
  subgraph External Sources
    S1["Archives / APIs"]
    S2["STAC / HTTP"]
    S3["DBs / Files"]
  end

  subgraph Pipelines
    T["Trigger<br/>cron · event · manual"]
    AI["Light AI (Optional)<br/>schema · mapping hints"]
    E["Deterministic ETL<br/>pure transforms"]
    V["Validation & QA<br/>schema · spatial · temporal · drift"]
    U["Idempotent Upsert<br/>natural key · content hash · outbox"]
    M["Metadata & Versioning<br/>STAC · DCAT"]
    B["Blue/Green Publish<br/>pointer flip"]
    O["Observability & Telemetry<br/>logs · metrics · traces"]
  end

  subgraph Stores
    G[(Neo4j Graph)]
    D[(data/processed-blue / -green)]
    C[(data/stac/ STAC Catalog)]
  end

  S1 --> T
  S2 --> T
  S3 --> T
  T --> AI
  AI --> E
  E --> V
  V -->|pass| U
  V -->|fail| O
  U --> M
  M --> B
  B --> G
  B --> D
  B --> C
  Pipelines --> O
~~~~~

### Repository Context

~~~~~text
src/pipelines/
├── architecture/
│   └── reliable-pipelines.md
├── etl/
│   ├── batch/
│   └── streaming/
└── common/
    ├── idempotency/
    ├── validation/
    ├── observability/
    ├── versioning/
    └── governance/

data/
├── sources/
├── raw/
├── work/
└── processed/
    ├── blue/
    └── green/
~~~~~

Pipelines sit between external sources and internal stores (Neo4j, STAC, `data/processed/**`), and must conform to the reliability rules below.

---

## ⚙️ Procedures / Implementation

### 1. Trigger & Envelope

Every run MUST start from a **trigger envelope**:

~~~~~json
{
  "trigger_id": "cron-2025-11-15T00:00Z-kgs-wells",
  "trigger_kind": "cron",
  "dataset_id": "kgs_wells",
  "source_uri": "https://example.org/kgs/wells",
  "requested_range": {
    "start": "1900-01-01",
    "end": "2025-11-01"
  },
  "idempotency_key": "sha256(dataset_id|requested_range|source_uri)"
}
~~~~~

### 2. Light AI (Optional)

- AI is permitted only for schema sniffing, unit detection, and mapping hints.  
- All AI-derived outputs MUST be turned into static config (JSON/YAML) and versioned.  

### 3. Deterministic ETL

- Transforms MUST be pure and stateless.  
- Inputs → normalized tables and feature sets with:
  - Explicit unit conversions.  
  - CRS reprojection.  
  - Controlled vocabularies.  
- No unpinned randomness.

### 4. Validation & QA

- Apply schema, spatial, temporal, domain, and drift checks.  
- On failure:
  - Write only to `data/work/**`.  
  - Emit `qa_gate_failed` events.  
  - Abort promotion.

### 5. Idempotent Upsert

- Compute natural key + content hash.  
- Skip records where `prev.hash == new.hash`.  
- Use transactional upsert patterns for graph and tables.  

### 6. Metadata & Versioning

- Update STAC/DCAT metadata for artifacts.  
- Assign semantic version per dataset.  
- Record provenance and FAIR+CARE metadata.

### 7. Blue/Green Publish

- Write candidate to `data/processed-green/**`.  
- Run health checks (UI/API).  
- Flip pointer to `data/processed-blue/**` on success.  

### 8. Alerts & Telemetry

- Emit structured events:
  - `stage_started`, `stage_succeeded`, `qa_gate_failed`, `publish_promoted`.  
- Integrate with telemetry stack as per observability standard.

### 9. Rollback & Resume

- **Rollback:** pointer flip to previous blue; no destructive edits.  
- **Resume:** checkpoints (date/page/offset) plus idempotent logic for safe re-runs.

---

## 📑 Data Contracts & Schemas

Every dataset controlled by this standard MUST have a **source descriptor**:

- Location: `data/sources/<dataset>.json`  
- Required content:
  - Dataset ID, title, description.  
  - Source URLs / endpoints and auth.  
  - Field-level schema:
    - Name, type, unit, nullable flag.  
  - Temporal and spatial coverage.  
  - License + CARE labels.  
  - Expected artifact shapes (tables, COGs, STAC collections, graph updates).  

Example (simplified):

~~~~~text
contract_version: "v3"
fields:
  - name: dataset_id
    type: string
    required: true
  - name: timestamp
    type: datetime
    required: true
~~~~~

Validation (e.g., GX, JSONSchema) MUST be wired to this contract.

---

## 🧬 Ontology Alignment

This architecture aligns with external ontologies:

- **CIDOC-CRM**
  - Pipelines / updaters → `E7 Activity`
  - Artifacts → `E73 Information Object`
- **OWL-Time**
  - Run intervals → `time:TemporalEntity`, `time:hasBeginning`, `time:hasEnd`
- **GeoSPARQL**
  - Dataset footprints → `geo:FeatureCollection`, `geo:hasGeometry`
- **PROV-O**
  - Pipeline → `prov:Activity`
  - Artifacts → `prov:Entity`
  - Operators / automation → `prov:Agent`
  - Links → `prov:wasGeneratedBy`, `prov:used`
- **schema.org**
  - This document → `TechArticle`

These mappings inform metadata exports and knowledge graph enrichment.

---

## 🛰 STAC/DCAT Metadata

Any pipeline that produces geospatial assets MUST emit STAC/DCAT metadata.

Example STAC collection snippet:

~~~~~json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "kfm-kgs-wells-v10-4-0",
  "description": "KFM processed Kansas Geological Survey well dataset.",
  "license": "MIT",
  "extent": {
    "spatial": { "bbox": [[-102.1, 36.99, -94.6, 40.0]] },
    "temporal": { "interval": [["1900-01-01T00:00:00Z", "2025-11-01T00:00:00Z"]] }
  },
  "links": [],
  "assets": {}
}
~~~~~

DCAT 3.0 MUST describe the same dataset and link distributions (`data/processed/**`, STAC items).

---

## 📖 Story Node Integration

This document is **not** a Story Node, but:

- Story Node ETL pipelines MUST comply with:
  - Idempotent upsert patterns.  
  - Validation gates.  
  - Blue/green publish.  

Story Node–specific docs MUST:

- Reference this architecture.  
- Define `story_node_id`, narrative content, temporal/spatial grounding, and relations.  

---

## 🧠 Focus Mode Integration

Focus Mode v2 MAY:

- Summarize this document’s role for developers and operators.  
- Use its content to explain why pipelines are idempotent and rollback-safe.

Boundaries:

- **Allowed:** neutral summaries of procedures, patterns, and error classes.  
- **Prohibited:** speculative commentary on operator intent or unverified claims about upstream data.

Focus Mode should link to this doc as a **policy reference** for any pipeline-related focus view.

---

## 🔐 Ethics & CARE

- This document is classified **Public / Low-Risk**.  
- Pipelines governed by it may handle:
  - CARE-labeled datasets (public/restricted/sensitive).  
  - Potentially culturally significant or Indigenous data.

Requirements:

- Pipelines MUST respect CARE labels declared in `data/sources/**`.  
- Restricted/sensitive data MUST NOT be emitted into public artifacts.  
- Governance docs MUST be referenced for pipelines that process Indigenous or culturally sensitive content.

---

## 🛡 Privacy & Security

- This architecture doc contains no PII and is public.  
- Pipelines MUST:
  - Avoid logging PII or sensitive cultural data in plaintext.  
  - Secure credentials and secrets (not in source descriptors or logs).  
  - Follow security guidelines in:
    - `docs/security/*`
    - `docs/standards/governance/ROOT-GOVERNANCE.md`  

Retention & destruction:

- Logs, telemetry, and DLQ contents must adhere to retention policies defined by governance (e.g., 90-day retention for raw logs, longer for aggregated metrics).

---

## 🧪 Validation & Reproducibility

Pipelines under this standard MUST:

- Provide **unit tests** for:
  - Natural key and content hash derivation.  
  - Transform behavior.  
- Provide **integration tests** for:
  - Full runs on sample data.  
  - Validation failures and expected behavior.  
  - Blue/green pointer flips and rollback.

Example commands:

~~~~~text
$ make docs-validate
$ pytest tests/pipelines/test_reliable_patterns.py
~~~~~

Reproducibility requires:

- Pinned container images.  
- Documented runtime versions (Python, Node, Neo4j).  
- Clear description of any external dependencies.

---

## 📈 Telemetry

Pipelines MUST specify:

- Events they emit (`stage_started`, `qa_gate_failed`, `publish_promoted`, etc.).  
- Metrics tracked (runtime, throughput, retries, DLQ entries, etc.).  
- Sampling strategy (if any) and privacy-preserving transformations.

Telemetry is exported according to:

- `src/pipelines/architecture/observability/README.md`  
- Telemetry schema referenced in `telemetry_schema`.

---

## 🎧 Accessibility (WCAG 2.1 AA)

Plain-language summary:

> This document explains how to make KFM pipelines safe, repeatable, and easy to fix when something goes wrong. It describes a single pattern that all pipelines must follow so they can be rolled back, retried, and monitored without breaking the system.

Accessibility requirements:

- Headings are nested properly and descriptive.  
- Lists and tables are well-structured.  
- Any future images must include alt text.  
- Color is not the only channel of information (Mermaid diagrams use text labels).

---

## 🤖 Machine Extractability

This document is designed to be machine-parsable:

- Heading hierarchy is predictable and complete.  
- Tables are syntactically valid and aligned.  
- Code blocks:
  - Use fenced notation with explicit languages (`json`, `text`, `mermaid`, `python`).  
  - Contain valid JSON/YAML where applicable (enforced by CI).  
- YAML front-matter is complete and conforms to `docs-markdown-rules.schema.json`.

---

## ♻️ Dataset Evolution / Deltas

Compared to prior versions:

- **v1.0.0:**  
  - Basic reliable updaters concept (triggers → ETL → upsert → rollback/resume).  
- **v10.3.1:**  
  - Added detailed trigger mesh, outbox, observability, and retry patterns.  
- **v10.4.0:**  
  - Aligned with Markdown MDP v10.4.  
  - Added FAIR+CARE and ontology alignment.  
  - Formalized error taxonomy, governance, and CI expectations.  

Migration notes:

- Older pipelines MUST be updated to:
  - Use explicit natural keys + content hashes.  
  - Implement blue/green patterns if they previously used in-place updates.  
  - Emit required telemetry events.

---

## 🧩 Error Taxonomy

Pipelines MUST classify errors into:

- **ConfigurationError:** bad or missing config, schema mismatch.  
- **ValidationError:** data fails schema/spatial/temporal/domain/drift checks.  
- **TransientIOError:** temporary network or storage issues.  
- **PermanentIOError:** persistent upstream failures (e.g., dataset removed).  
- **UpsertConflictError:** violations of natural key constraints.  
- **PointerFlipError:** failures during blue/green pointer update.  

Mitigations and safeguards for each class MUST be documented in pipeline-specific docs.

---

## 📁 Directory Layout

~~~~~text
src/pipelines/
├── architecture/
│   └── reliable-pipelines.md
├── etl/
│   ├── batch/
│   └── streaming/
└── common/
    ├── idempotency/
    ├── validation/
    ├── observability/
    ├── versioning/
    └── governance/

data/
├── sources/
├── raw/
├── work/
└── processed/
    ├── blue/
    └── green/
~~~~~

---

## 🕰 Version History

| Version | Date       | Author / Team              | Summary                                                                                 |
|--------:|------------|----------------------------|-----------------------------------------------------------------------------------------|
| v10.4.0 | 2025-11-15 | Pipeline Architecture Team | Unified reliable pipeline spec; aligned with Markdown MDP v10.4 and missing standards.  |
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Previous “Reliable Pipeline Architecture Guide”.                                        |
| v1.0.0  | 2025-11-15 | ETL/Updaters Working Group | Initial “Reliable Updaters” pattern.                                                    |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**  
Validated under **Master Coder Protocol v6.3**  
FAIR+CARE Aligned · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Pipeline Architecture](../README.md) · [Root Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
```
