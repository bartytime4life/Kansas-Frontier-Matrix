---
title: "🔁 KFM v11.2.4 — Queue-Centric Pipeline Architecture (Deterministic · Ordered · Observable)"
path: "docs/pipelines/core/queue-architecture/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Systems & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x protocol-safe"
status: "Active · Enforced"

doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "pipelines/core"
  applies_to:
    - "etl"
    - "queues"
    - "backfill"
    - "replay"
    - "telemetry"
    - "provenance"
    - "story-nodes"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/queue-architecture-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/queue-architecture-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:doc:pipelines:core:queue-architecture:v11.2.4"
semantic_document_id: "kfm-pipeline-core-queue-architecture-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:core:queue-architecture:v11.2.4"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🔁 Queue-Centric Pipeline Architecture  
**Deterministic ETL → Ordered Execution → Observability → Replay-Safety**  

`docs/pipelines/core/queue-architecture/README.md`

**Purpose:**  
Define the canonical **queue-driven pipeline architecture** used across all KFM pipelines (Atmospheric, Soil, Hydrology, Archaeology AI, Vector ETL, Catalog Generation, etc.), providing deterministic ingestion, reproducible ordering, backpressure tolerance, and replay-correct behavior aligned with KFM governance, telemetry, and provenance standards.

</div>

---

## 🗂️ Directory Layout

```text
📂 docs/pipelines/core/queue-architecture/
├── 📄 README.md                 # 🔁 Queue-Centric Pipeline Architecture (this file)
├── 📂 examples/                 # 📚 Pattern examples & reference snippets
│   ├── 📄 fifo-groups.md        # FIFO queues & message-group patterns
│   ├── 📄 idempotency-patterns.md
│   └── 📄 otel-attributes.md    # Required/standard OpenTelemetry attributes
├── 📂 runbooks/                 # 📒 Operational guides
│   ├── 📄 backlog-investigation.md
│   ├── 📄 replay-procedures.md
│   └── 📄 slo-burn-analysis.md
└── 📂 diagrams/
    └── 🖼️ queue-architecture.png  # Visual architecture diagram (optional)
```

All queue-based pipelines must reference this document in their own READMEs and follow these patterns unless an exception is documented and governed.

---

## 📘 Overview

KFM pipelines must guarantee:

- **Deterministic behavior** — same input → same output, given the same config and code version.  
- **Idempotency** — handlers can safely be retried or replayed without double effects.  
- **Ordering where required** — particularly for dataset partitions and time-series sequences.  
- **Replay-safe WAL boundaries** — every mutation is reconstructable from logs and messages.  
- **Full OpenTelemetry coverage** — traces, metrics, and logs for every node and queue.  
- **Provable lineage** — STAC, DCAT, and PROV-O-compatible provenance for all outputs.  
- **Energy / cost / carbon tracking** at node and pipeline boundaries.

This queue-centric architecture is the **baseline** for all KFM ETL and streaming workflows. Any pipeline deviating from these rules must document the deviation and obtain governance approval.

---

## 🧭 Context

In the KFM stack:

> Source Systems → Queue-Centric Pipelines → STAC/DCAT/PROV Catalogs → Neo4j Graph → API Layer → Frontend → Story Nodes & Focus Mode

The queue architecture:

- Provides a **common execution and reliability substrate** for domain pipelines (soil, hydrology, atmospheric, archaeology AI, catalog generation).  
- Defines how **backpressure, retries, and replays** are handled across services.  
- Connects telemetry (OpenTelemetry), provenance (PROV-O), and catalogs (STAC/DCAT) to each pipeline step.  

It is a critical foundation for:

- **Deterministic ETL** and backfill.  
- **Event-time–aware processing** (watermarks and late data handling).  
- **Story Node & Focus Mode** stability (so derived narratives are reproducible from underlying data and queues).

---

## 🧱 Architecture

### 1. Deterministic DAG nodes

Each node behaves like a pure function:

```text
input_message + config(seed) → output_message
```

Rules:

- Fixed random seeds for any stochastic operations.  
- No external nondeterministic calls (e.g., `now()`, remote RNG) without explicit, logged injection.  
- Transforms are version-pinned (code version + config version).  
- Schemas are validated on ingress/egress for every node.

Determinism must be testable by rerunning nodes with the same inputs and verifying identical outputs (within defined numeric tolerances).

### 2. Idempotent handlers

Handlers must be safe to run **any number of times**:

- Use a **content hash** (or equivalent) as an **idempotency key**.  
- Writes use **idempotent upserts** keyed by this ID (no blind inserts).  
- WAL (Write-Ahead Log) capture happens **before** external mutations.  
- No side-effects (DB writes, file writes, external calls) occur without WAL confirmation.

Idempotency keys and related metadata must appear in logs and traces.

### 3. Queue ordering & throughput control

Where ordering matters, pipelines must use **FIFO queues with message groups**:

- Message group = business key, examples:
  - `gnatsgo:<county_fips>`  
  - `nexrad:<station_id>`  
  - `archaeo-inference:<site_cluster_id>`  

Concurrency is controlled via:

- Global semaphores (pipeline-wide concurrency caps).  
- Domain-specific semaphores (e.g., “DB writes: max 8”, “external API calls: max 4”).

Ordering guarantees must be documented:

- Per pipeline (e.g., “per station” or “per MUKEY”).  
- In `examples/fifo-groups.md`.

### 4. Dedupe strategy

Use **content-based deduplication** at the queue boundary:

- Normalize JSON payloads (canonical ordering, whitespace rules).  
- Compute SHA-256 (or equivalent) as the **dedupe key**.  
- Queue layer **drops duplicates** based on this key.  
- Pipelines log “duplicate-collapsed” events for observability.

Dedupe logic must not break idempotency: a collapsed duplicate is treated as “already successfully processed”.

### 5. Failure & replay logic

On failure:

1. Handler retries with exponential backoff (bounded).  
2. After N failures → message moves to a **Dead Letter Queue (DLQ)**.  
3. Replay engine pulls from DLQ or WAL.  
4. Messages are reprocessed in deterministic mode (same code and config unless explicitly overridden).  
5. Output events are **re-linked** to original PROV-O lineage using shared identifiers.

Replay procedures and operational steps must be documented in `runbooks/replay-procedures.md`.

### 6. Backfill & event-time watermarks

Backfill is treated as a **first-class operating mode**:

- Uses separate capacity pools to avoid starving live traffic.  
- Employs **event-time watermarks** to ensure consistency between backfill and live flow.  
- Prevents late-arriving historical data from disrupting real-time operations.  
- Emissions from backfill are tagged in PROV-O as `prov:wasDerivedFrom` with additional backfill qualifiers.

Backfill policies (e.g., max lookback, allowed skew) must be documented per pipeline.

---

## 🧪 Validation & CI/CD

### 1. Observability specification

Every pipeline using this architecture must integrate with **OpenTelemetry**:

**Traces**

- One span per DAG node execution.  
- `message_group` (or equivalent) added as an attribute.  
- Link spans when replays occur (using `link` or `parent` semantics).  

**Metrics**

Minimum standard metrics:

- `queue.backlog` (per-queue or per-group).  
- `queue.oldest_age_seconds`.  
- `handler.retry_count`.  
- `latency.p50`, `latency.p95`, `latency.p99` (per handler).  
- `energy.kwh` and `carbon.co2e` per node (using energy standards).  
- SLO burn rate: `error_budget.consumption` for key SLOs.

**Logs (structured)**

Log records must include:

- `trace_id` and (when applicable) `span_id`.  
- `dataset_id` or equivalent domain identifier.  
- `message_group`.  
- `pipeline_version` (code + config).  
- `idempotency_key`.  
- Error details for DLQ transitions.

### 2. CI/CD enforcement

CI workflows must:

- Validate that queue-based pipelines:
  - Emit required OpenTelemetry attributes (see `examples/otel-attributes.md`).  
  - Implement idempotency keys and log them.  
  - Use WAL boundaries before side effects.  
- Include **determinism checks**:
  - Re-running a subset of messages must yield identical outputs.  
- Include **replay tests**:
  - Simulate DLQ-based replays and validate final state and provenance.  

Acceptance criteria are summarized as a checklist:

- [ ] Deterministic node execution verified.  
- [ ] Ordered delivery validated by group keys.  
- [ ] Dedupe keys stable across retries.  
- [ ] WAL replay passes reproducibility tests.  
- [ ] Telemetry bundle generated and schema-valid for each run.  
- [ ] SLO burn rate within governance thresholds.

---

## 📦 Data & Metadata

Key metadata tied to this architecture includes:

- **Message metadata**
  - `message_id`, `message_group`, `idempotency_key`, `attempt_count`, `event_time`.  
- **Handler metadata**
  - `handler_name`, `handler_version`, `pipeline_version`.  
- **WAL records**
  - Encapsulate:
    - Input message snapshot.  
    - Handler version and config hash.  
    - Resulting side-effect descriptors (e.g., DB upsert keys, STAC/DCAT identifiers).  

Telemetry exports (per `queue-architecture-v1.json`) must include:

- Node-level summary metrics (latency, error counts, retries).  
- Queue-level metrics (backlog, age).  
- Energy and carbon for each handler.

All these metadata fields must be designed for **machine readability** and **graph/catal​​og ingestion**.

---

## 🌐 STAC, DCAT & PROV Alignment

The queue architecture itself is **provenance-aware**:

- **PROV-O**
  - Each handler execution is a `prov:Activity`.  
  - Input and output messages are `prov:Entity` instances.  
  - The pipeline or service is a `prov:Agent`.  
  - Replays are modeled as new `prov:Activity` instances **linked** to the original via shared entities and metadata.

- **STAC / DCAT**
  - Outputs that materialize datasets (raster, vector, tables) are:
    - STAC Items/Collections or DCAT Datasets.  
    - Linked to queue activities via PROV fields and foreign members (e.g., `kfm:queue_activity_id`).  

This alignment ensures auditors can:

- Trace a STAC/DCAT asset back through the queue activities that produced it.  
- Understand where retries, replays, or backfills affected a dataset.

---

## ⚖ FAIR+CARE & Governance

Queue architecture is a **technical** standard with **ethical implications** when processing sensitive or sovereignty-related data:

- For pipelines handling **cultural or sensitive datasets**:
  - Use generalized **H3 grids** and enforced minimum resolutions in any spatial derivatives.  
  - Insert sovereignty-review gates before publishing derived layers or Story Nodes.  
  - Apply CARE labels in metadata enrichment nodes.  
  - Use sanitizer nodes to prevent raw geometry or sensitive attributes from leaking downstream.

Governance responsibilities:

- Systems & Reliability Council owns **architecture conformance**.  
- FAIR+CARE Council reviews **pipelines that handle sensitive data** to ensure queue behavior (ordering, replays, backfill) does not undermine sovereignty or privacy.  
- Any deviation from this architecture must be:
  - Documented in an exception record.  
  - Reviewed and approved by relevant governance bodies.

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                        |
|--------:|------------|-------------------|--------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active · Enforced | Initial architecture spec aligned with global KFM queue protocol. |

Future revisions must:

- Document changes to required telemetry, WAL semantics, or idempotency rules.  
- Update examples and runbooks when new queue patterns are adopted.  
- Keep alignment with energy, provenance, and governance standards.

---

<div align="center">

🔁 **KFM v11.2.4 — Queue-Centric Pipeline Architecture**  
Deterministic Pipelines · Ordered Execution · Observable & Replay-Safe  

[📘 Docs Root](../../..) · [⚙ Pipelines Index](../README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>