---
title: "🚨 KFM v11.2.3 — NODD Telemetry Alerts Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed alert and SLO-violation specification for the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/telemetry/alerts/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x telemetry-alerts compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Telemetry Alerts Specification"
intent: "nodd-sns-sqs-telemetry-alerts"
category: "Pipelines · Atmospheric · Telemetry · Alerts"

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
sunset_policy: "Superseded by next major NODD telemetry alerts standard"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🚨 NODD Telemetry Alerts Specification  

`docs/pipelines/atmo/nodd-sns-sqs/telemetry/alerts/README.md`

**Governed alert, paging, and SLO-violation model for the NOAA NODD SNS → SQS ingestion pipeline.**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Pipeline-NODD_SNS_%E2%86%92_SQS-skyblue" />
<img src="https://img.shields.io/badge/Telemetry-Alerts_%26_SLOs-red" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

⸻

## 🧭 1. Purpose

This document defines the **canonical alerts and SLO enforcement rules** for the NOAA NODD SNS → SQS ingestion pipeline:

- Which conditions MUST trigger alerts and how they are classified (warning vs critical).  
- How alerts are derived from telemetry metrics defined in `telemetry/README.md` and `telemetry_schema`.  
- Required routing, runbook linkage, and payload fields for alert notifications.  
- CI/governance expectations for keeping alerts in sync with telemetry and SLOs.

Concrete rule details and thresholds are elaborated in `nodd-alert-policies.md`.

⸻

## 🗂 2. Directory Layout (Alerts)

    docs/pipelines/atmo/nodd-sns-sqs/telemetry/alerts/
    │
    ├── 📄 README.md                 # This file (alerts & SLO spec index)
    │
    └── 📄 nodd-alert-policies.md    # Concrete alert rules, thresholds, and routing profiles

Platform-specific alert definitions (Grafana, Alertmanager, PagerDuty, etc.) live in infrastructure repositories and MUST implement these contracts.

⸻

## 🎯 3. Core Alert Categories

NODD alerts are grouped into six governed categories:

1. **Queue Health SLO Alerts**  
   Queue age, queue depth, and watermark lag.

2. **Failure & DLQ Alerts**  
   Validation/gov errors and DLQ spikes.

3. **Replay Determinism Alerts**  
   Replay mismatches and unexpected replay volume.

4. **Ingest Latency Alerts**  
   End-to-end latency vs dataset-specific SLOs.

5. **Telemetry & Coverage Alerts**  
   Missing metrics, stalled ingestion, or silent failure modes.

6. **Energy/Carbon Anomaly Alerts** (optional when enabled)  
   Sudden unexplained jumps in energy or carbon metrics.

Each category maps to one or more rule blocks in `nodd-alert-policies.md`.

⸻

## 📬 4. Queue Health & SLO Alerts

### 4.1 Queue Age SLO Breach (Critical)

**Source metric:** `nodd_sns.queue_age_seconds{queue,env,quantile}`

Condition (primary queue, `env = prod`):

- P90 queue age > 90 seconds for a sustained window (e.g., 5–10 minutes).  

Alert payload MUST include:

- `queue`, `env`, P50/P90/P99 values, SLO threshold, and breach duration.  
- Links to:
  - NODD ingestion dashboard queue panels.  
  - Relevant runbooks if the pattern suggests systemic backlog.

### 4.2 Queue Depth Abnormal (Warning / Critical)

**Source metric:** `nodd_sns.queue_depth{queue,env}`

Conditions (examples, finalized in `nodd-alert-policies.md`):

- Warning: depth above a soft threshold for a sustained period.  
- Critical: depth near configured hard limit, or accelerating growth.

Payload MUST list current depth, rolling trend, and affected `queue`/`env`.

⸻

## 🧪 5. Failure & DLQ Alerts

### 5.1 DLQ Rate Spike (Critical)

**Source metric:** `nodd_sns.dlq_messages_total{queue,env,dataset}` (used as rate/derivative)

Condition (prod):

- DLQ rate > 0.05% of total messages over a rolling window, **or**  
- Absolute DLQ volume above dataset-specific thresholds.

Payload MUST include:

- `queue`, `env`, top contributing `dataset` values, recent DLQ trend, and dominant error types (where available).  
- Direct links to:
  - DLQ panels on the NODD ingestion dashboard.  
  - `replay/runbooks/dlq-drain-runbook.md`.

### 5.2 Validation/Governance Error Surge (Warning / Critical)

**Source metric:** `nodd_sns.validation_errors_total{dataset,env,error_type}` (rate/derivative)

Conditions:

- Warning: sustained elevation for a single `error_type` (e.g., `schema_mismatch`).  
- Critical: large step-change across multiple `datasets` or `error_type`s, indicating widespread schema drift or governance breakage.

Alerts MUST reference:

- Offending `error_type` and `dataset` set.  
- Suggested investigation paths (schema/gov docs, recent deploys).

⸻

## 🔁 6. Replay Determinism & WAL Alerts

### 6.1 Replay Mismatch (Critical, Hard SLO)

**Source metric:** `nodd_sns.replay_mismatch_total{dataset,env}`

Condition (prod):

- Any **increase** in `replay_mismatch_total` over the evaluation window.

Rationale:

- WAL replays must be deterministic; mismatches are treated as P1 reliability incidents.

Payload MUST include:

- Affected `dataset`, count of mismatches, time window, and any available `replay_run_id`.  
- Links to:
  - `replay/runbooks/incident-replay-runbook.md`.  
  - Lineage dashboards (OpenLineage / graph views) for affected runs.

### 6.2 Unexpected Replay Volume (Warning)

**Source metric:** `nodd_sns.replays_total{dataset,env,reason}`

Condition:

- Replay counts significantly above baseline for a given `reason` (e.g., repeated DLQ drains) in `prod`.

Intent:

- Early warning that replays are compensating for a latent issue (schema bugs, unstable upstreams).

⸻

## ⏱ 7. Ingest Latency Alerts

### 7.1 Ingest Latency SLO Breach

**Source metric:** `nodd_sns.ingest_latency_seconds` (P90 per `dataset`/`env`)

Critical condition (priority datasets, prod):

- P90 ingest latency > 300 seconds (5 minutes) for a sustained window.

Warning condition:

- P90 latency trending > 2× recent baseline for multiple datasets.

Alert payload MUST include:

- Affected `dataset(s)`, current vs SLO latency, evaluation window, and related context (queue age, DLQ levels).

⸻

## 📡 8. Telemetry & Coverage Alerts

### 8.1 Telemetry Silence / Coverage Gap

Conditions:

- No `nodd_sns.ingest` spans or equivalent ingest metrics in `prod` for longer than a small grace period while ingestion is expected.  
- Missing series for critical metrics (queue depth, queue age, latency) in `prod`.

Severity:

- Warning for `dev`/`stage` silence with active `prod`.  
- Critical for `prod` silence beyond the configured threshold.

Payload MUST include:

- Affected metric families, `env`, last-seen timestamps.  
- Pointers to infra-level dashboards (e.g., collector health, scraping endpoints).

⸻

## 🌱 9. Energy & Carbon Anomaly Alerts (Optional)

When energy/carbon telemetry is enabled:

**Source metrics:**

- `nodd_sns.energy_kwh_total{env}`  
- `nodd_sns.carbon_gco2e_total{env}`

Conditions (Warning, informational):

- Sudden deviation from baseline energy usage per ingested GB/unit.  
- Abrupt jumps in `carbon_gco2e` not attributable to known changes (e.g., new regions, increased volume).

These alerts are **non-paging** and used to track sustainability regressions over time.

⸻

## 📦 10. Alert Payload & Routing Requirements

All alert notifications (PagerDuty, email, chat, etc.) MUST include:

- **Context fields**:
  - `env`, `dataset` (where applicable), `queue` (where applicable).  
  - Condition summary and breached threshold.

- **Telemetry links**:
  - Stable URLs to:
    - NODD ingestion dashboard.  
    - The most relevant panel group (queue, DLQ, replay, latency).

- **Runbooks**:
  - Direct links to relevant runbooks, for example:
    - `replay/runbooks/dlq-drain-runbook.md`  
    - `replay/runbooks/incident-replay-runbook.md`  

- **Severity & routing**:
  - Severity = `info`, `warning`, or `critical`.  
  - Mapped to paging/notification channels as defined in `nodd-alert-policies.md`.

Routing profiles and platform-specific config are standardized in `nodd-alert-policies.md`.

⸻

## 🧪 11. CI & Governance Validation

CI SHOULD validate that alert rules in infrastructure repositories:

- Reference metric names and labels consistent with `telemetry_schema`.  
- Encode thresholds and patterns consistent with this spec and `nodd-alert-policies.md`.  
- Include required runbook URLs in alert annotations.  

Governance reviews SHOULD periodically confirm that:

- SLOs remain appropriate for dataset volume and criticality.  
- Alert fatigue is reduced (no persistent noisy alerts).  
- New datasets or pipeline modes are covered by appropriate alerts.

Removing or substantially weakening any **core** SLO alert (queue age, DLQ SLO, replay mismatch, ingest latency) without updating this spec and passing Council review is a governance violation.

⸻

## 🕰 12. Version History

| Version  | Date       | Notes                                                                                              |
|---------:|------------|----------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD telemetry alerts spec; defined SLO-driven alert categories, payload, and CI guidance. |

---

<div align="center">

🚨 NODD Telemetry Alerts · KFM v11.2.3  

SLO-Driven · Runbook-Linked · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Telemetry](../README.md) ·  
[📊 Dashboards](../dashboards/README.md) ·  
[📁 Telemetry Samples](../samples/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
