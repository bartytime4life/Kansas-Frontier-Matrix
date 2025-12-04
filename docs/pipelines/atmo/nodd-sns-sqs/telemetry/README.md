---
title: "📊 KFM v11.2.3 — NOAA NODD SNS → SQS Telemetry & SLO Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "OpenTelemetry spans, metrics, logs, and SLO/error-budget model for the NOAA NODD SNS → SQS ingestion pipeline in KFM."
path: "docs/pipelines/atmo/nodd-sns-sqs/telemetry/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x telemetry-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Telemetry Specification"
intent: "nodd-sns-sqs-telemetry-spec"
category: "Pipelines · Atmospheric · Telemetry · OpenTelemetry"

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
sunset_policy: "Superseded by next major NODD telemetry standard"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 📊 NOAA NODD SNS → SQS Telemetry & SLO Specification  

`docs/pipelines/atmo/nodd-sns-sqs/telemetry/README.md`

**OpenTelemetry-first metrics, spans, logs, and SLO/error-budget contracts for the NOAA NODD SNS → SQS event-driven ingestion pipeline.**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Pipeline-NODD_SNS_%E2%86%92_SQS-skyblue" />
<img src="https://img.shields.io/badge/Telemetry-OTel_first-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

This document defines the **telemetry, SLOs, and error-budget model** for the KFM v11 NOAA NODD SNS → SQS ingestion pipeline.

It ensures that:

- All key stages (SNS → SQS → worker → QC → STAC → provenance) are observable.  
- Metrics and spans are **stable, low-cardinality, and OTel-aligned**.  
- SLOs for **queue age, DLQ rate, replay determinism, and ingest latency** are clearly defined.  
- Telemetry supports FAIR+CARE governance, energy/carbon reporting, and provenance audits.

This spec is binding for implementation, CI checks, and dashboards.

---

## 🗂 2. Directory Layout (Emoji-Prefix Standard)

Telemetry documentation and references for the NODD pipeline live here:

    docs/pipelines/atmo/nodd-sns-sqs/telemetry/
    │
    ├── 📄 README.md                          # This file (telemetry & SLO spec)
    │
    ├── 📁 dashboards/                        # Dashboard definitions or references
    │   └── 📄 nodd-ingestion-dashboard.md    # Panels, queries, and layout description
    │
    ├── 📁 alerts/                            # Alert and SLO configuration docs
    │   └── 📄 nodd-alert-policies.md         # Queue age, DLQ, latency, determinism alerts
    │
    └── 📁 samples/                           # Example traces, metrics, and log records
        ├── 📄 example-trace.json             # Redacted sample OTel trace
        ├── 📄 example-metrics.json           # Aggregated metric export
        └── 📄 example-log.json               # Structured log example

Additional files (e.g., Grafana JSON, alertmanager rules) may be referenced from this directory but stored in infrastructure repos.

---

## 🌐 3. Telemetry Overview

The NODD SNS → SQS pipeline emits:

- **Spans (traces)** for:
  - SNS notification handling.
  - SQS message processing.
  - Object fetch and integrity checks.
  - STAC Item creation and registration.
  - Provenance emission and WAL updates.

- **Metrics** for:
  - Queue health (depth, age, DLQ volume).
  - Ingestion latency and throughput.
  - Validation and error rates.
  - Replay determinism and WAL behavior.
  - Energy and carbon estimates (where enabled).

- **Logs** for:
  - Structured event summaries (info-level).
  - Validation and ingest errors (warn/error).
  - Governance/CARE decisions (audit trail).

All telemetry MUST conform to `telemetry_schema`.

---

## 📏 4. Metrics Catalog

The following metrics are REQUIRED at minimum. Names are illustrative; exact names and label sets are defined by `telemetry_schema`.

| Metric Name                               | Type      | Labels (Low-Cardinality)                  | Description                                                  |
|------------------------------------------:|----------:|-------------------------------------------|--------------------------------------------------------------|
| `nodd_sns.queue_depth`                   | gauge     | `queue`, `env`                             | Current SQS approximate number of messages.                  |
| `nodd_sns.queue_age_seconds`            | summary   | `queue`, `env`, `quantile`                | Message age distribution (P50/P90/P99) at receive time.      |
| `nodd_sns.ingest_latency_seconds`       | histogram | `dataset`, `env`                           | End-to-end latency (SNS publish → STAC Item registered).     |
| `nodd_sns.dlq_messages_total`           | counter   | `queue`, `env`, `dataset`                  | Total messages sent to DLQ.                                  |
| `nodd_sns.validation_errors_total`      | counter   | `dataset`, `env`, `error_type`             | Count of schema/QA/gov failures.                             |
| `nodd_sns.replays_total`                | counter   | `dataset`, `env`, `reason`                 | Number of WAL-backed replays executed.                       |
| `nodd_sns.replay_mismatch_total`        | counter   | `dataset`, `env`                           | Replays that did **not** produce identical outputs.          |
| `nodd_sns.bytes_ingested_total`         | counter   | `dataset`, `env`                           | Total bytes successfully ingested (granules processed).      |
| `nodd_sns.energy_kwh_total`             | counter   | `env`                                      | Estimated cumulative energy usage for NODD ingestion.        |
| `nodd_sns.carbon_gco2e_total`           | counter   | `env`                                      | Estimated cumulative carbon emissions for NODD ingestion.    |

Constraints:

- Labels must be **bounded** and low-cardinality (no per-object IDs).  
- High-cardinality identifiers (e.g., object keys) belong in spans or logs, not metric labels.

---

## 🧵 5. Span Model (Traces)

Each ingest unit should be represented as a linked set of OTel spans forming a trace:

Top-level span:

- `nodd_sns.ingest`  
  - Attributes:
    - `nodd.dataset` (e.g., `goes-abi`, `nexrad-l2`, `hrrr`).  
    - `nodd.object_uri` (may be truncated/redacted in UI).  
    - `nodd.bucket_provider` (`aws`, `azure`, `gcp`).  
    - `nodd.run_mode` (`hot-path`, `backfill`).

Child spans (examples):

- `nodd_sns.sqs_receive`  
- `nodd_sns.object_fetch`  
- `nodd_sns.integrity_check`  
- `nodd_sns.metadata_extract`  
- `nodd_sns.stac_register`  
- `nodd_sns.provenance_emit`

Each span must:

- Include error status on failures.  
- Link to WAL ID and PROV/lineage IDs via attributes:
  - `nodd.wal_id`  
  - `nodd.prov_activity_id`

Sample traces (redacted) are documented in `samples/example-trace.json`.

---

## 📜 6. Logs & Audit Trail

Logging requirements:

- **Info-level logs**:
  - One summary log per ingest unit (e.g., per STAC Item) containing:
    - Dataset, object URI (possibly hashed), outcome (`success`/`quarantined`), bytes processed, latency bucket.
- **Error logs**:
  - Detailed context for failed validation, STAC writes, provenance, or network operations.
  - Include correlation IDs:
    - `trace_id`, `span_id`, `wal_id`, `prov_activity_id`.

- **Governance logs**:
  - CARE/sovereignty decisions:
    - Whether generalization or redaction occurred.
    - Which rules triggered (`rule_id`).

Logs must be structured (JSON or equivalent) and avoid embedding large payloads.

---

## 🎯 7. SLOs & Error Budgets

Recommended SLOs for the NODD SNS → SQS pipeline:

1. **Queue Age SLO**

   - Objective: P90 SQS message age `< 90 seconds` for production datasets.  
   - Error budget burn evaluated over rolling 30-day windows.

2. **DLQ Rate SLO**

   - Objective: `< 0.05%` of messages routed to DLQ.  
   - DLQ events must have clear cause codes (`validation`, `provenance`, `infra`, etc.).

3. **Replay Determinism SLO**

   - Objective: `100%` WAL replays produce identical STAC + provenance outputs for non-mutating code changes.  
   - Any replay mismatch is a **P1 reliability incident**.

4. **Ingest Latency SLO**

   - Objective: P90 ingest latency `< 5 minutes` SNS publish → STAC Item registered for configured priority datasets.

Violations:

- Must trigger alerts (see `alerts/nodd-alert-policies.md`).  
- Feed into reliability reviews and, when related to governance, FAIR+CARE oversight.

---

## 📊 8. Dashboards & Alerts

Dashboards (e.g., Grafana) SHOULD include panels for:

- SQS queue depth and age.  
- Ingest latency distributions by dataset.  
- DLQ rate over time.  
- Replay counts and mismatches.  
- STAC Item throughput and bytes ingested.  
- Energy and carbon trends (if telemetry is enabled).

Alert policies (documented in `alerts/nodd-alert-policies.md`) MUST cover:

- Queue age SLO violations.  
- DLQ rate spikes.  
- Replay mismatch > 0.  
- Telemetry gaps (e.g., missing metrics from specific workers or environments).

---

## 🧩 9. FAIR+CARE & Sovereignty Signals

Telemetry must support:

- Identification of datasets that involve **Indigenous, cultural, or otherwise sensitive content**.  
- Flags for:
  - Generalization (e.g., dynamic H3-level used).  
  - Redaction applied.  
  - Restricted-access collections updated.

These signals help:

- Governance and sovereignty boards audit pipeline behavior.  
- Ensure that auto-updates do not silently erode privacy or sovereignty protections.

Telemetry for sensitive datasets MUST NOT expose sensitive identifiers in metrics or logs.

---

## 🕰 10. Version History

| Version  | Date       | Notes                                                                                      |
|---------:|------------|--------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NOAA NODD SNS → SQS telemetry spec; metrics catalog, span model, SLOs, and alerts. |

---

<div align="center">

### 📊 NOAA NODD SNS → SQS Telemetry · KFM v11.2.3

OTel-First · Reliability-Aware · FAIR+CARE Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Pipeline](../README.md) ·  
[📡 Lineage & CI Validation](../../../lineage/README.md) ·  
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>