---
title: "🔁 Kansas Frontier Matrix — Unified Reliable Pipeline Architecture v11 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/reliable-pipelines.md"
version: "v11.0.0"
last_updated: "2025-11-18"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/pipelines-reliable-v2.json"
governance_ref: "../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Architecture · Standard"
intent: "pipelines-reliability"
fair_category: "F1-A1-I1-R1"
care_label: "Collective benefit · Authority to control · Responsibility · Ethics"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Operational Reliability"
redaction_required: false
provenance_chain:
  - "src/pipelines/architecture/reliable-pipelines.md@v1.0.0"
  - "src/pipelines/architecture/reliable-pipelines.md@v10.3.1"
  - "src/pipelines/architecture/reliable-pipelines.md@v10.4.0"
  - "src/pipelines/architecture/reliable-pipelines.md@v10.4.1"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../schemas/json/pipelines-reliable-pipelines-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/pipelines-reliable-pipelines-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:pipelines-reliable-pipelines-v11.0.0"
semantic_document_id: "kfm-doc-pipelines-reliable-pipelines"
event_source_id: "ledger:src/pipelines/architecture/reliable-pipelines.md"
immutability_status: "mutable-plan"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "execution-control-changes"
  - "governance-weakening"
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

# 🔁 **Kansas Frontier Matrix — Unified Reliable Pipeline Architecture v11**  
`src/pipelines/architecture/reliable-pipelines.md`

**Purpose**  
Define the *authoritative, enforceable* reliability standard and architecture for all KFM pipelines and updaters:

> **Triggers → light AI (schema only) → deterministic ETL → validation gates → idempotent upsert → metadata/versioning → blue/green publish → alerts & telemetry**,  
> with **safe retries, rollback, and resume** enforced at the architecture level.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../docs/README.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Operational-orange)](../../docs/standards/faircare.md)  
[![Status: Enforced](https://img.shields.io/badge/Status-Enforced-success)](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

---

## 📘 1. Overview

This document specifies the **Unified Reliable Pipeline Architecture** for Kansas Frontier Matrix (KFM).  
It merges and supersedes all prior “Reliable Updaters” and “Reliable Pipeline Architecture” guides into a single **Diamond⁹ Ω / Crown∞Ω Ultimate Certified** v11 architecture + standard.

Reliable pipelines in KFM are:

- **Deterministic** — same inputs + same config → same outputs.  
- **Idempotent** — safe under at-least-once triggers, with exactly-once effects at the publish boundary.  
- **Rollback-safe** — blue/green pointer flips, never destructive edits.  
- **Observable** — structured logs, metrics, traces, FAIR+CARE telemetry.  
- **Replayable** — checkpoints + immutable artifacts enable safe re-runs.  
- **Governed** — FAIR+CARE + governance gates applied before publish.  

Any pipeline that does not comply with this standard MUST NOT be deployed.

---

## 🎯 2. Purpose

The purposes of this standard are to:

- Provide a **single, enforceable pattern** for all KFM pipelines and updaters.  
- Ensure **idempotent, observable, rollback-safe** behavior across ingestion, ETL, graph updates, and publishing.  
- Align pipeline design with:
  - **Master Coder Protocol (MCP-DL v6.3)**  
  - **Markdown Structural & Formatting Rules v11**  
  - **FAIR+CARE governance**  
  - **STAC/DCAT/PROV-O/OpenLineage**  

**Primary consumers:**

- Pipeline authors (Python, SQL, Neo4j, STAC tooling).  
- Architecture and SRE teams.  
- FAIR+CARE Council and governance bodies verifying reliability posture.  

---

## 📍 3. Scope

### In Scope

All code and configuration under `src/pipelines/**` that:

- Reads from `data/sources/**`, `data/raw/**`, or external APIs/streams.  
- Writes to `data/work/**`, `data/processed/**`, `data/stac/**`, or Neo4j.  

All pipelines that:

- Perform ETL (batch or streaming).  
- Update KFM knowledge graph or STAC/DCAT catalogs.  
- Affect user-facing maps, timelines, Focus Mode, or Story Nodes.

### Out of Scope

- Pure frontend logic that does not depend on pipeline guarantees.  
- Ad-hoc notebooks used solely for one-off analysis (not used in production).  
- External upstream providers’ internal architectures.

**Related documents:**

- `src/ARCHITECTURE.md` — global system architecture.  
- `src/pipelines/architecture/observability/README.md` — observability standard.  
- `docs/standards/markdown_rules.md` — Markdown protocol.  

---

## 📚 4. Definitions

- **Pipeline / Updater** — repeatable process that ingests, transforms, validates, and publishes data or knowledge into KFM.  
- **Trigger** — mechanism that starts a run (cron, event, manual), bundled with a *trigger envelope*.  
- **Idempotency Key (run-level)** — deterministic hash of the trigger envelope used to prevent double-processing of the same run.  
- **Natural Key (record-level)** — minimal, stable business identity for each record (e.g., `(station_id, date)`).  
- **Content Hash** — hash of the **normalized record without runtime fields** (no timestamps, no ephemeral IDs).  
- **Blue/Green** — dual dataset pattern where one version serves (blue) and another is candidate (green).  
- **Checkpoint** — persisted cursor (date/page/offset) for resume.  
- **DLQ (Dead Letter Queue)** — durable storage for work items that failed beyond allowed retries.  
- **Artifact** — any derived dataset (COG, Parquet, CSV, GeoJSON, STAC item, etc.) whose integrity is tracked.  
- **Run ID** — unique identifier of a single pipeline execution derived from content and configuration.

---

## 🏗 5. Architecture / Context

### 5.1 System Context

~~~mermaid
flowchart TD
  subgraph External_Sources[External Sources]
    S1["Archives / APIs"]
    S2["STAC / HTTP"]
    S3["DBs / Files"]
  end

  subgraph Pipelines["Reliable Pipeline (this standard)"]
    T["Trigger<br/>cron · event · manual"]
    AI["Light AI (Optional)<br/>schema hints only"]
    E["Deterministic ETL<br/>pure transforms"]
    V["Validation & QA<br/>schema · spatial · temporal · drift · FAIR+CARE"]
    U["Idempotent Upsert<br/>natural key · content hash"]
    M["Metadata & Versioning<br/>STAC · DCAT · PROV"]
    B["Blue/Green Publish<br/>pointer flip"]
    O["Observability & Telemetry<br/>logs · metrics · traces"]
  end

  subgraph Stores["KFM Stores"]
    G[(Neo4j Graph)]
    D[(data/processed-blue / data/processed-green)]
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
~~~

### 5.2 Repository Context

~~~text
src/pipelines/
├── architecture/
│   └── reliable-pipelines.md
├── <pipeline_name>/
│   ├── run.py
│   ├── idempotency.py
│   ├── stac_io.py
│   ├── staging_writer.py
│   ├── validators/
│   │   ├── gx_checkpoint.yml
│   │   ├── semantic_rules.yml
│   │   └── faircare_rules.yml
│   ├── neo4j_commit.py
│   ├── lineage.py
│   ├── telemetry.py
│   ├── flags.py
│   └── tests/
│       ├── test_idempotency.py
│       ├── test_e2e_small.py
│       └── test_validation_contracts.py
~~~

---

## ⚙️ 6. Trigger & Run Identity

### 6.1 Trigger Envelope

Every run MUST start from a **trigger envelope**:

~~~json
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
~~~

### 6.2 Deterministic Run ID (v11)

~~~text
run_id = sha256(
    STAC_Item.id +
    sorted_asset_checksums +
    pipeline_semver +
    normalized_config +
    code_fingerprint
)[:16]
~~~

Properties:

- Same inputs + same config + same code ⇒ same `run_id`.  
- Used as pipeline-level idempotency key.  
- Used in staging namespaces, telemetry, and lineage.

---

## 🧮 7. Deterministic ETL

- All core transforms MUST be **pure and stateless**.  
- No unseeded randomness; any randomness MUST be seeded and recorded.  
- Inputs are normalized into artifact tables and feature sets with:
  - Explicit unit conversions.  
  - CRS reprojection.  
  - Controlled vocabularies and enumerations.  

---

## ✅ 8. Validation Layer

Validation occurs **after staging**, **before publish**.

### 8.1 Data Quality (e.g., Great Expectations)

Required checks:

- Row counts within tolerance.  
- Geometry validity (no self-intersections; CRS correct).  
- Temporal ranges match STAC Item.  
- Required fields present and typed.  
- Distribution checks against calibration baselines.

### 8.2 Semantic & Ontology Validation

- CIDOC-CRM / GeoSPARQL / OWL-Time mapping validated.  
- Graph topology rules (no illegal relationships).  
- Deduplication semantics enforced.  
- Reference integrity:
  - STAC → graph.  
  - Graph → PROV-O.  

### 8.3 FAIR+CARE / Governance Validation

- CARE labels respected.  
- Sensitive datasets generalized (e.g., via H3 masking).  
- No restricted content flows into public artifacts.  

### 8.4 Validation Gate

A pipeline **cannot promote** unless:

~~~text
VALIDATION_STATUS = PASS
~~~

On failure:

- Emit `FAILED_VALIDATION` lineage event.  
- Persist validation artifacts (e.g., GE Data Docs).  
- Halt execution with no promotion into production graph or processed data.

---

## 🧱 9. Staging Model

All pipelines follow:

~~~text
Extract → Transform → Validate → Stage → Promote → Finalize
~~~

### 9.1 Staging Namespace

Write NOTHING directly to production graph or `data/processed/**`.

All writes are labeled / namespaced:

- Graph labels: `:Staging_<run_id>`  
- Object storage: `.../<pipeline>/<run_id>/<asset>.<ext>`  
- Work tables: `data/work/<pipeline>/<run_id>/...`

Staging must be:

- Fully reconstructable.  
- Self-contained.  
- Free of references to production nodes.

---

## 🔁 10. Idempotency Protocol

### 10.1 Run-Level Idempotency

~~~text
Condition                     → Behavior
------------------------------------------------
Run ID exists & finalized      → Skip entire pipeline
Run ID exists & partial        → Retry from last durable checkpoint
Run ID missing                 → Execute full pipeline
~~~

### 10.2 Record-Level Idempotency

- Use **natural key + content hash** per record.  
- Skip any record where `prev_content_hash == new_content_hash`.  
- Ensure exactly-once behavior at the **publish boundary**.

---

## 🌉 11. Blue/Green Publish & Rollback

### 11.1 Namespaces

- `data/processed-blue/**`  
- `data/processed-green/**`  

### 11.2 Flow

1. Write new artifacts into `processed-green`.  
2. Validate and smoke-test.  
3. Flip pointer so that `blue` ↔ `green` roles swap.  
4. Monitor metrics for the stability window (24h by default).  

### 11.3 Rollback

- Flip pointer back to previous blue.  
- Delete or quarantine green artifacts from the failed attempt.  
- Emit `ROLLBACK` lineage event describing cause and scope.

---

## 🧬 12. Lineage & Metadata

### 12.1 STAC / DCAT

- All inputs declared via STAC Items/Collections.  
- All outputs described in STAC/DCAT with:
  - `kfm:pipeline_id`  
  - `kfm:run_id`  
  - Temporal and spatial extents.  
  - CARE labels and license.  

### 12.2 PROV-O Lineage

Attach to promoted entities:

~~~text
:GeneratedBy {
  run_id,
  job_name,
  pipeline_semver,
  config_hash,
  startedAt,
  endedAt,
  stac_item_id,
  commit_sha
}
~~~

### 12.3 OpenLineage

Send run events:

- `namespace = "kfm"`  
- `job = "pipelines/<pipeline_name>"`  
- `run_id`  
- Inputs: STAC hrefs.  
- Outputs: URIs for graph and storage locations.  

### 12.4 Provenance Persistence

~~~text
provenance/<pipeline>/<run_id>/lineage.json
~~~

---

## 📡 13. Telemetry & Observability

Every run MUST emit:

- Runtime per stage.  
- Memory and CPU profile.  
- Row/node/edge counts changed.  
- Storage footprints (bytes added/removed).  
- Energy + carbon estimates.  
- Retry counts and DLQ entries (if any).  

Telemetry is serialized to:

~~~text
telemetry/<pipeline>/<run_id>/metrics.json
~~~

and validated against:

~~~text
schemas/telemetry/pipelines-reliable-v2.json
~~~

---

## 🔐 14. Security & Privacy

- No secrets in code or plain YAML; use Vault / secret manager.  
- No PII or sensitive cultural data in logs.  
- Pipelines operate within least-privilege roles.  
- Environments are containerized and pinned.  

Logs and DLQ contents must obey retention policies specified in governance.

---

## 💥 15. Failure Modes & Recovery

Three canonical failure categories:

~~~text
Failure Type         → Behavior
------------------------------------------------
Extract failure       → Stop immediately, no staging
Validation failure    → Stop, emit lineage, keep staging for debug
Promotion failure     → Auto-rollback, no partial promotions
~~~

### 15.1 Retriable (Automatic)

- Transient DB failures.  
- Network blips.  
- Storage errors.  
- Short-term resource saturation.  

Controlled via:

~~~text
max_retries: 3
retry_backoff: exponential
retryable_errors: [TransientDBError, NetworkError, StorageTransientError]
~~~

Non-retriable failures must halt and require manual intervention.

---

## 📁 16. Required Repo Structure

~~~text
src/pipelines/
  architecture/
    reliable-pipelines.md   ← this file
  <pipeline_name>/
    run.py
    idempotency.py
    stac_io.py
    staging_writer.py
    validators/
      gx_checkpoint.yml
      semantic_rules.yml
      faircare_rules.yml
    neo4j_commit.py
    lineage.py
    telemetry.py
    flags.py
    tests/
      test_idempotency.py
      test_e2e_small.py
      test_validation_contracts.py

data/
  sources/
  raw/
  work/
  processed/
    blue/
    green/
~~~

---

## ✅ 17. Promotion Checklist

This checklist MUST be attached to run logs and surfaced in dashboards:

~~~text
[ ] Deterministic run_id computed
[ ] Staging written (0 errors)
[ ] Great Expectations / data-quality PASS
[ ] Semantic validators PASS
[ ] FAIR+CARE / governance validators PASS
[ ] STAC/DCAT metadata updated with run_id
[ ] OpenLineage + PROV-O emitted
[ ] Telemetry metrics generated and stored
[ ] Transactional promotion executed successfully
[ ] Blue/green pointer flipped
[ ] Stability window observed
[ ] Rollback executed (if required)
~~~

---

## 🧪 18. Minimal Example Workflow

~~~text
python run.py \
  --stac-item path/to/item.json \
  --config config.yml \
  --commit true \
  --emit-lineage true
~~~

Pipeline actions:

1. Compute `run_id`.  
2. Extract and transform into normalized structures.  
3. Write to staging under `:Staging_<run_id>` and staging storage paths.  
4. Run data-quality, semantic, FAIR+CARE, and metadata validators.  
5. If all PASS → transactional promotion into blue/green namespace.  
6. Emit OpenLineage + PROV-O + STAC/DCAT updates.  
7. Generate telemetry and persist metrics.  
8. Flip pointer and observe stability window.

---

## 🕰️ Version History

| Version | Date       | Author                               | Summary                                                                                     |
|--------:|------------|----------------------------------------|---------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-18 | FAIR+CARE Council · Architecture WG   | Rebuilt Unified Reliable Pipeline Architecture for KFM-MDP v11; merged v1.0.0, v10.3.1, v10.4.x; added OpenLineage/FAIR+CARE/telemetry v2 integration. |
| v10.4.1 | 2025-11-18 | Architecture WG                       | Refined v10.4 architecture; clarified orchestration patterns for Airflow/Dagster/Temporal. |
| v10.4.0 | 2025-11-15 | Pipeline Architecture Team            | Unified reliable pipeline spec; aligned with Markdown MDP v10.4 and ontology mappings.      |
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team            | Previous “Reliable Pipeline Architecture Guide”.                                            |
| v1.0.0  | 2025-11-15 | ETL/Updaters Working Group            | Initial “Reliable Updaters” pattern.                                                        |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Unified Reliable Pipeline Architecture v11 · FAIR+CARE Certified · Sovereignty-Aware  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified · MCP-DL v6.3  

[Back to Pipeline Architecture](../README.md)

</div>