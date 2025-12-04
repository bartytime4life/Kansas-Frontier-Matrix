---
title: "⚡ KFM v11.2.3 — Event-Driven Auto-Update Ingestion Pipeline (SNS → SQS · Incremental Refresh · STAC-First)"
description: "Event-driven update detection, incremental deltas, deterministic catalog writing, and reliability primitives for auto-updating KFM datasets using SNS → SQS and STAC-first contracts."
path: "docs/pipelines/auto-update/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/auto-update-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/auto-update-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Specification"
intent: "event-driven-auto-update-ingestion"
category: "Pipelines · Auto-Update · SNS/SQS · STAC"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
immutability_status: "version-pinned"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major auto-update ingestion standard"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# ⚡ KFM v11 — Event-Driven Auto-Update Ingestion Pipeline  

`docs/pipelines/auto-update/README.md`

**Event-driven update detection, incremental deltas, deterministic STAC catalog writing, and reliability primitives for auto-updating KFM datasets.**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Updates-SNS_%E2%86%92_SQS-orange" />
<img src="https://img.shields.io/badge/Metadata-STAC_first-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

The **Auto-Update Ingestion Pipeline** defines a governed pattern for **event-driven, incremental updates** across KFM datasets using **SNS → SQS → Workers → STAC**.

It exists to:

- Eliminate polling by using **push-style notifications** for new or updated assets.  
- Support **idempotent, delta-only refreshes** using content hashes/ETags.  
- Make **STAC the source-of-truth** for updated geospatial assets.  
- Embed **validation, governance, and reliability gates** into every update unit.  
- Provide a reusable, standard contract for hydrology, soils, atmo, archives, and other domains.

---

## 🗂 2. Directory Layout (Emoji-Prefix Standard)

High-level layout under `docs/pipelines/auto-update/`:

    docs/pipelines/auto-update/
    │
    ├── 📄 README.md                       # This file (auto-update pipeline spec)
    │
    ├── 📨 sns-schema/                     # SNS event definitions
    │   └── 📄 message-v1.json
    │
    ├── 📬 sqs-contract/                   # Consumer contract, idempotency keys, retry rules
    │   └── 📄 README.md
    │
    ├── 🔍 validation-gates/               # Schema, QA, CARE/FAIR, provenance checks
    │   ├── 📄 schema-check.md
    │   ├── 📄 qa-rules.md
    │   └── 📄 governance-gate.md
    │
    ├── 📦 processors/                     # Workers: ingestion → transform → STAC write
    │   ├── 📄 parquet-updater.md
    │   ├── 📄 raster-updater.md
    │   └── 📄 vector-updater.md
    │
    ├── 🗺️ stac-writers/                   # Atomic STAC item/collection creation
    │   ├── 📄 item-writer.md
    │   └── 📄 collection-writer.md
    │
    ├── ⏱️ watermarks/                     # Event-time watermarks, lag monitors
    │   └── 📄 watermark-spec.md
    │
    └── 📊 telemetry/                      # OTel spans, metrics, error budgets
        └── 📄 metrics.md

Each subdocument must describe contracts, schemas, and CI checks for its component.

---

## 🚀 3. Pipeline Overview

### 3.1 Hot-Path: SNS → SQS → Worker

1. **Publisher emits** compact update events to SNS.  
2. **SNS fan-out** routes messages based on dataset, product, and priority.  
3. **SQS subscriber** receives structured notifications with ETags, URIs, and time ranges.  
4. **Worker** executes:

   - Idempotency check.  
   - Conditional fetch (skip if no hash/ETag change).  
   - Transform (normalize into KFM-ready structure).  
   - Validation & governance gates (schema, QA, CARE/FAIR).  
   - **Atomic STAC write** (Item/Collection updates).

### 3.2 Batch-Path: Cron / EventBridge Scheduler

- Periodic refresh, backfills, extent recomputes, and QA deep scans.  
- Uses **the same ingestion contract**:
  - Same validation and governance gates.  
  - Same STAC writing rules.  
  - No bypass of hot-path protections.

---

## 📥 4. Event Schema (v1)

Example SNS message payload:

    {
      "event_time": "2025-12-04T03:14:15Z",
      "dataset": "usgs/streamflow",
      "asset_uri": "s3://bucket/path/file.parquet",
      "content_etag": "W/\"a1b2c3\"",
      "granule_start": "2025-12-04T03:00:00Z",
      "granule_end": "2025-12-04T03:59:59Z",
      "priority": "high",
      "schema_version": "1.0"
    }

Design principles:

- **Stable** — schema is additive; older events remain valid.  
- **Minimal** — no heavy payloads; only pointers and metadata.  
- **Deterministic** — full reproducibility from `dataset + asset_uri + content_etag`.

Schema details are documented under `sns-schema/message-v1.json`.

---

## 🔁 5. Incremental Refresh Model

Each dataset supports versioned, idempotent upserts using the following keys:

| Key                                   | Purpose                                 |
|--------------------------------------:|-----------------------------------------|
| `asset_uri`                           | Unique pointer to raw or derived data.  |
| `content_etag`                        | Detects content change; skip if same.   |
| `idempotency_key = sha256(dataset + asset_uri + content_etag)` | Deduplication and safe retries. |
| Checkpoint store                      | Tracks last granule processed.          |

Workers:

- Refresh only **deltas** — no blind reprocessing.  
- Log idempotency decisions (hit/miss) to telemetry and provenance.  
- Maintain per-dataset checkpoint state.

---

## 🛡 6. Validation & Governance Gates

All ingest units must pass three gate families:

### 6.1 Schema Gate

- Structural validity (e.g., JSON schema, Parquet schema).  
- CRS and geospatial consistency.  
- Time monotonicity (no impossible or inverted time ranges).

### 6.2 QA Gate

- Range checks and statistical sanity checks.  
- Geometry validity (no self-intersections where prohibited, valid polygons).  
- Null/NaN severity rules (acceptable levels vs. hard-fail thresholds).

### 6.3 Governance Gate

- CARE restrictions and sovereignty flags.  
- Provenance completeness (who/what/when used + generated).  
- STAC licensing accuracy and usage terms.  
- Sensitivity masking or generalization when required.

**Failures are quarantined** (DLQ or quarantine bucket); workers never publish STAC updates on red.

---

## 📚 7. STAC as Source-of-Truth

### 7.1 Writing Rules

- Always create/update STAC Items **atomically**.  
- Validate against:
  - STAC spec.
  - KFM STAC extensions (e.g., `raster:*`, `proj:*`, `processing:*`).  
- Use a **temporary write → validate → promote** sequence:
  - Write candidate Item.  
  - Validate (schema + business rules).  
  - Promote to canonical catalog only on success.

### 7.2 Collections

- Maintain **stable extent** metadata and **versioned summaries**.  
- Attach processing lineage to each update:
  - References to OpenLineage/PROV-O records.  
  - SLO/QA status when available.

STAC catalogs become the authoritative view of which assets exist and which versions are active.

---

## ⏱ 8. Watermarks & Ordered Backfills

KFM uses **per-dataset and per-partition event-time watermarks**:

- Workers only backfill **≤ watermark**.  
- Watermark advances only when **all partitions converge**.  
- Prevents mixed ordering and race conditions in highly concurrent environments.  
- Enables multi-tenant datasets (hydrology, soils, atmo, archaeology imagery) to share infrastructure while preserving ordering guarantees.

Watermark configuration and invariants are documented in `watermarks/watermark-spec.md`.

---

## 📊 9. Observability (OTel-First)

For each ingest unit, the pipeline records:

- **Traces**:
  - `fetch → transform → validate → stac_write` spans.  
- **Metrics** (per dataset / partition):
  - Latency P50/P95/P99.  
  - Queue depth (SQS).  
  - Watermark lag.  
  - DLQ counts.  
  - Error budget burn rate.  
- **Logs**:
  - Structured success logs (low cardinality).  
  - Detailed error logs tied to run IDs and idempotency keys.

Telemetry **must** conform to `telemetry_schema` and respect cardinality constraints.

---

## 🧱 10. Reliability Model

Reliability primitives baked into the auto-update design:

- **Deterministic idempotency keys** (`sha256(dataset + asset_uri + content_etag)`).  
- **WAL-backed replay model** for reprocessing without duplication.  
- **Safe retries** (SQS visibility timeout tuned to content size and processing time).  
- **Canary mode** for schema or pipeline upgrades:
  - Route a fraction of events through new logic, compare outputs.  
- **Kill-switch flags per dataset**:
  - Immediate disable of auto-updates on governance or reliability incidents.

Checkpointed state tables (conceptual):

| Table         | Shape                                               |
|--------------:|-----------------------------------------------------|
| `ingest_state`| `(dataset, asset_uri) → {etag, version, processed_at}` |
| `checkpoints` | `(dataset, partition) → {watermark, updated_at}`    |
| `qa_findings` | `(run_id, dataset, severity, rule)`                 |

---

## 🚦 11. Rollout Sequence (Recommended)

Stepwise rollout for new auto-update pipelines:

1. Define message schema and DLQs (SNS + SQS + failure queues).  
2. Implement **idempotent consumer** with a persistent state store.  
3. Add **validation + governance gates** (schema, QA, CARE/FAIR).  
4. Integrate **STAC atomic writer** (Items/Collections).  
5. Add **OpenTelemetry** instrumentation and connect to KFM dashboards.  
6. Enable **SNS routing** from upstream publishers.  
7. Scale workers and tune concurrency / visibility timeouts.  
8. Turn on **cron-based backfills** and QA scans using the same contract.

---

## 🧩 12. Version History

| Version  | Date       | Notes                               |
|---------:|------------|-------------------------------------|
| v11.2.3  | 2025-12-04 | Initial governed release of spec.   |

---

<div align="center">

### ⚡ KFM v11 — Event-Driven Auto-Update Ingestion Pipeline

Deterministic · Ethics-Aligned · Provenance-Complete  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Pipelines Index](../README.md) ·  
[📚 STAC & Data Contracts](../../data/README.md) ·  
[⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>