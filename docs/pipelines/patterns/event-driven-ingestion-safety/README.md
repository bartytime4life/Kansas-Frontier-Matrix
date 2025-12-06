---
title: "📨 KFM v11.2.4 — Event-Driven Ingestion Safety Pattern (Duplicates, Retries, DLQs, Watermarks)"
path: "docs/pipelines/patterns/event-driven-ingestion-safety/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Eng · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x"
status: "Active / Enforced"

doc_kind: "Pattern"
intent: "event-driven-ingestion-safety-pattern"
role: "event-ingestion-safety-contract"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "messaging"
  applies_to:
    - "etl"
    - "streaming"
    - "backfill"
    - "ai-workloads"
    - "observability"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "KFM-Open"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false
risk_category: "Event-Driven Ingestion Safety"
redaction_required: false

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/patterns-telemetry.json"
telemetry_schema: "schemas/telemetry/patterns-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/patterns/event-driven-ingestion-safety/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-patterns-event-driven-ingestion-safety-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-patterns-event-driven-ingestion-safety-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:pipelines:patterns:event-driven-ingestion-safety:v11.2.4"
semantic_document_id: "kfm-pipelines-patterns-event-driven-ingestion-safety-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:patterns:event-driven-ingestion-safety:v11.2.4"

ingestion_contract:
  event_source: "Amazon S3 Event Notifications (ObjectCreated/*)"
  transport:
    - "SNS"
    - "SQS (STD or FIFO)"
  delivery_semantics: "at-least-once (duplicates & out-of-order possible)"
  consumer_requirements:
    - "idempotent reprocessing"
    - "deduplication keys"
    - "deterministic watermarking for backfills"
    - "exponential backoff with jitter"
    - "DLQ attachment + redrive SOP"

observability:
  metrics:
    - "messages_received_total{queue}"
    - "messages_duplicate_total{queue}"
    - "processing_latency_seconds{stage}"
    - "retry_attempts_total{reason}"
    - "dead_letter_count{queue}"
    - "watermark_event_time_seconds{stream}"
  logs: "structured JSON, correlate by message_id, object_key, run_id"
  traces: "OpenTelemetry spans: source→queue→consumer→storage"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "footer-check"
  - "accessibility-check"
  - "provenance-check"
  - "pattern-contract-check"

ci_integration:
  workflow: ".github/workflows/event-driven-ingestion-safety.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Event-Driven Safety × Deterministic Replays × Sustainable Pipelines"
  architecture: "Idempotency · Retries · DLQs · Watermarks"
  analysis: "Evidence-Led · Reliability-First · FAIR+CARE Grounded"
  data-spec: "S3 Events × SNS/SQS × STAC/DCAT/PROV"
  telemetry: "Duplicates · Retries · DLQs · Watermarks"
  graph: "Events · Activities · Datasets"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# 📨 **KFM v11.2.4 — Event-Driven Ingestion Safety Pattern**  
`docs/pipelines/patterns/event-driven-ingestion-safety/README.md`

**Purpose:**  
Define the **governed safety pattern** for **event-driven ingestion** (S3 → SNS → SQS → consumer) in KFM so that:

- **Duplicates** and **out-of-order delivery** are safe,  
- **Retries** are bounded and jittered,  
- **DLQs** are attached with clear redrive flows, and  
- **Backfills** and **late data** are deterministic and auditable.

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

</div>

---

## 📘 Overview

S3 event notifications are **at-least-once**: duplicates and out-of-order delivery are expected, not exceptional.

This pattern ensures that:

- Reprocessing the same event is **safe** (idempotent side effects).  
- Bursts and transient failures are handled with **exponential backoff + jitter**, not thundering herds.  
- Poison messages are isolated in **DLQs** with clear **redrive SOPs**.  
- Historical replays and late arrivals are **deterministic**, with event-time **watermarks** and fully versioned inputs/outputs.

It applies to:

- S3 → SNS → SQS → consumer flows (STD or FIFO queues).  
- Event-driven **ETL, streaming, backfill, AI workloads**, and **observability** pipelines built on top.

---

## 🗂️ Directory Layout

Canonical layout for this pattern in the KFM monorepo:

~~~text
KansasFrontierMatrix/
├── 📂 docs/
│   └── 📂 pipelines/
│       └── 📂 patterns/
│           └── 📂 event-driven-ingestion-safety/
│               ├── 📄 README.md                 # This file (pattern spec)
│               ├── 📂 examples/
│               │   ├── 📂 sqs-standard/         # STD queue wiring examples
│               │   └── 📂 sqs-fifo/             # FIFO queue + dedupe examples
│               └── 📂 runbooks/
│                   ├── 📄 duplicate-spike.md    # Duplicate rate spike response
│                   ├── 📄 dlq-redrive.md        # DLQ triage + redrive SOP
│                   └── 📄 late-data-lane.md     # Late-data handling & replays
│
├── 📂 src/
│   └── 📂 pipelines/
│       └── 📂 patterns/
│           └── 📂 event_driven_ingestion_safety/
│               ├── 📄 __init__.py
│               ├── 📄 idempotency.py            # Idempotency key & WAL helpers
│               ├── 📄 retry_policy.py           # Exponential backoff + jitter
│               ├── 📄 dlq_handler.py            # DLQ handlers & redrive helpers
│               ├── 📄 watermarking.py           # Event-time watermarks & late-data lanes
│               └── 📄 contract.py               # Envelope/schema contract helpers
│
├── 📂 infra/
│   └── 📂 terraform/
│       └── 📂 messaging/
│           ├── 📄 s3_sns_sqs_events.tf          # Event sources, topics, queues, DLQs
│           └── 📄 event_ingestion_safety.tf     # IAM, retries, visibility, alarms
│
└── 📂 .github/
    └── 📂 workflows/
        └── 📄 event-driven-ingestion-safety-checks.yml
            # CI: contract tests, WAL/idempotency tests, DLQ wiring checks
~~~

**Author rules:**

- New pattern docs must live under this directory and follow this layout.  
- Example and runbook paths should be updated here whenever new files are added.  
- Terraform and code modules must reference this pattern doc in comments or module-level docstrings.

---

## 🧭 Context

Event-driven ingestion in KFM typically looks like:

- **Source**: S3 `ObjectCreated/*` notifications (data files, manifests, tiles).  
- **Transport**: SNS topic fanning out to SQS queues (STD or FIFO) and/or Lambdas.  
- **Consumers**: ETL workers, streaming processors, AI inference pipelines.

Key realities:

- S3/SNS/SQS provide **at-least-once** delivery:  
  - **Duplicates** may occur (retries, fanout, internal retries).  
  - **Out-of-order** messages can occur, especially across partitions.  
- KFM must treat these as **normal conditions**, not exceptional ones.

This pattern standardizes **how** KFM pipelines:

- Declare **ingestion contracts**,  
- Implement **idempotency** and **deduplication**,  
- Handle **retries**, **DLQs**, and **late data**, and  
- Make all of this **observable** and **provenance-aware**.

---

## 🧱 Architecture

### 1. Idempotency & Deduplication

**Why:** S3 and SNS can fan out duplicates; consumers must not double-apply side effects.

**Contract**

- **Idempotency key** = stable hash over:  
  `{bucket, key, etag?, version_id?, size}`  
- **Write-Ahead Log (WAL)** entry is created **before** side effects:
  - `wal_id` = deterministic hash over the idempotency key.  
  - `status ∈ {received, started, succeeded, failed}`.  
- **Exactly-once upsert semantics**:
  - Downstream storage (lakeFS, Parquet tables, Neo4j) performs **idempotent upsert** keyed by dataset primary keys + `content_hash`.  
- **SQS FIFO (optional)**:
  - Use **content-based deduplication** or explicit `MessageDeduplicationId` when per-key ordering strictly matters.  
- **Standard queues (common)**:
  - Treat ordering as **best-effort**; consumers must **not rely** on strict ordering.

**Implementation sketch**

- Maintain a `processed_events` store keyed by `idempotency_key` with TTL ≥ backfill window.  
- On receive:

  1. Check `processed_events`. If present with `succeeded`, **ack** and **skip work**.  
  2. Append WAL entry with `status="started"`.  
  3. Perform deterministic transforms and upserts.  
  4. Append WAL entry with `status="succeeded"`.  
  5. Mark key in `processed_events`.

### 2. Retries with Exponential Backoff + Jitter

**Why:** Avoid thundering herds and repeated hammering of downstream systems.

**Contract**

- Base backoff:  

  ~~~text
  backoff = base * 2^attempt
  sleep   = random_uniform(0, min(backoff, backoff_cap))
  ~~~

- Classify errors:

  - **Retryable**: transient network failures, 5xx errors, throttling.  
  - **Non-retryable**: invalid schema, missing object, permanent permission error.

- **SQS visibility timeout** must exceed:

  ~~~text
  max_processing_time + max_backoff
  ~~~

**Guardrails**

- Cap attempts (e.g., 7). After cap, send to **DLQ**.  
- Emit metrics: `retry_attempts_total{reason}` and log final error cause.

### 3. Dead-Letter Queues (DLQs) & Redrive

**Why:** Isolate poison messages and keep hot paths healthy.

**Contract**

- Attach a **DLQ** to each SQS queue with `maxReceiveCount` (e.g., 5–10).  
- **Redrive SOP** (documented in runbooks):

  - Triage by error class:
    - Schema/validation errors.  
    - Permission/identity errors.  
    - Missing object.  
    - PII or CARE-strike.  
  - Fix upstream data or patch transformer deterministically.  
  - Redrive via controlled batch size with **backpressure** and **same idempotency keys**.

**Telemetry**

- `dead_letter_count{queue}` metrics with alerts and runbook links.  
- Retain last N failure payloads (with CARE masking applied) for forensics.

### 4. Deterministic Backfills & Late Data

**Why:** Replays must yield the **same result** for the **same inputs/config**; late arrivals must be handled consistently.

**Contract**

- **Event-time watermarks**:

  - Track `max_event_time_seen` per stream.  
  - Process only items with `event_time ≤ watermark`.  
  - Treat items later than the watermark as **late data**; route to a **late-data lane** with deterministic rules (e.g., apply patch or queue for scheduled replay).

- **Replay windows**:

  - Define `window_start` / `window_end` by **event time**, not arrival time.  
  - Freeze configs for the replay:

    - Schemas, lookup refs, model versions, seeds.  

- **Versioned inputs/outputs**:

  - Record STAC/DCAT Items, PROV-O lineage, and code artifact digests.  
  - Emit a `run_manifest.json` capturing inputs, commits, parameters, and seeds.

### 5. Ordering & Concurrency

- Use **per-key serialization** only when strictly required (e.g., object chunk assembly).  
- Prefer consumers that tolerate **out-of-order** by:

  - Reading current state (merge-on-read tables).  
  - Applying **idempotent** writes keyed by content hash.

- Use **concurrency limits** per partition key (e.g., `bucket/key-prefix`, H3 bucket) to avoid hotspotting.

---

## 📦 Data & Metadata

### Event Envelope Schema (JSON)

~~~json
{
  "event_id": "<uuid>",
  "source": "s3:ObjectCreated:Put",
  "bucket": "kfm-ingest",
  "key": "datasets/soil/2025/12/06/file.parquet",
  "etag": "abc123",
  "version_id": "3Lg..",
  "size": 1048576,
  "event_time": "2025-12-06T02:15:00Z",
  "idempotency_key": "<sha256(bucket,key,etag,version_id,size)>",
  "trace_id": "<otel-trace-id>"
}
~~~

**Rules**

- `event_time` = canonical **object last modified** time or producer-defined event time.  
- `idempotency_key` **must** be stable for the same content.  
- `trace_id` links to OpenTelemetry spans for end-to-end tracing.  

### Lineage & Catalog Integration

- Each run should produce:

  - **PROV-O Activity** for the consumer run, referencing:

    - S3 object entity (by URI + `etag`/`version_id`).  
    - Queue message entity (by `event_id`).  
    - Output dataset entity (STAC asset, parquet file, or graph nodes).

  - **DCAT/STAC** metadata for the outputs, linking to:

    - Source dataset or snapshots.  
    - Event-based provenance (`prov:used` relationships).

- A `run_manifest.json` per run:

  - Inputs (URIs, versions, hashes).  
  - Environment and config digests.  
  - Seeds and model versions (for AI workloads).

---

## 🧪 Validation & CI/CD

### Metrics & SLOs

Minimum metrics:

- `messages_received_total{queue}`  
- `messages_duplicate_total{queue}`  
- `processing_latency_seconds{stage}`  
- `retry_attempts_total{reason}`  
- `dead_letter_count{queue}`  
- `watermark_event_time_seconds{stream}`  

Suggested SLOs:

- **Duplicate rate**: ≤ 1% observed; **0 double-apply incidents**.  
- **p95 end-to-end latency**: ≤ 5 minutes under nominal load.  
- **DLQ rate**: stable and low; spikes trigger Sev2 with runbook links.

### Checklists

**Idempotency**

- [ ] Stable `idempotency_key` implemented.  
- [ ] WAL persisted before side effects.  
- [ ] Atomic / merge-on-read upsert semantics enforced.

**Retries**

- [ ] Exponential backoff **with jitter** implemented.  
- [ ] Attempts capped; visibility timeout sized accordingly.  
- [ ] Clear retryable vs. non-retryable error taxonomy.

**DLQ**

- [ ] DLQ attached with sane `maxReceiveCount`.  
- [ ] Redrive SOP documented and tools available.  
- [ ] DLQ metrics & alerts wired to dashboards and on-call.

**Backfills & Late Data**

- [ ] Event-time watermarking implemented.  
- [ ] Replay runs use frozen configs and seeds.  
- [ ] `run_manifest.json` and PROV-O lineage recorded.

**Observability**

- [ ] Metrics, logs, traces correlated by `idempotency_key` and `trace_id`.  
- [ ] SLOs defined and surfaced in dashboards.  
- [ ] Runbooks linked from alerts.

### Reference Implementation (Pseudo-Code)

~~~python
# receive → dedupe → WAL → process → commit → mark
msg = receive()
key = stable_hash(msg.bucket, msg.key, msg.etag, msg.version_id, msg.size)

if processed_events.exists(key):
    emit_metric("messages_duplicate_total", labels={"queue": msg.queue})
    ack()
    return

wal.start(key=key, msg=msg)

try:
    deterministic_transform(msg, config=frozen_run_config)
    atomic_upsert(outputs, key=content_hash(outputs))
    wal.succeeded(key=key)
    processed_events.put(key, ttl=backfill_window_days)
    ack()

except Retryable as e:
    emit_metric("retry_attempts_total", labels={"reason": e.reason})
    backoff_with_full_jitter(e.attempt, cfg=retry_cfg)
    raise  # return to queue

except NonRetryable as e:
    send_to_dlq(msg, reason=str(e))
    wal.failed(key=key, reason=str(e))
    ack()
~~~

---

## ⚖ FAIR+CARE & Governance

This pattern contributes to FAIR+CARE by:

- **FAIR**

  - Ensuring event-driven pipelines are **reproducible** and **traceable**, with clear provenance and replay manifests.  
  - Providing consistent envelope schemas and telemetry that can be cataloged as DCAT datasets and STAC assets.

- **CARE**

  - Payloads and logs must respect **CARE masking rules** for any sensitive fields (e.g., if events reference sensitive sites or identities).  
  - Late-data and replay operations must respect the same **governance constraints** as real-time flows (no bypassing of CARE/sovereignty checks).  

Governance expectations:

- IAM policies must enforce **least privilege** (e.g., `GetObject` only on needed prefixes).  
- Consumer containers must be **pinned by digest** with SBOM and SLSA attestations.  
- Any change to envelope schema or ingestion contract must be reviewed under:

  - Reliability Eng, and  
  - FAIR+CARE Oversight (if data could intersect heritage/sensitive overlays).

---

## 🕰️ Version History

| Version   | Date         | Changes                                                                      |
|----------:|--------------|-------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06   | Initial KFM-governed pattern: duplicates, idempotency, jitter, DLQs, watermarks. |

---

<div align="center">

📨 **KFM v11.2.4 — Event-Driven Ingestion Safety Pattern**  
Idempotent Events · Deterministic Replays · DLQ + Watermarks  

[📘 Patterns Index](../README.md) · [📡 SNS Filtering](../../messaging/sns-filtering/README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>