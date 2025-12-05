---
title: "🚨 KFM v11.2.3 — NODD Alert Policies (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Concrete alert rules, thresholds, severities, and routing profiles for the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/telemetry/alerts/nodd-alert-policies.md"

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

doc_kind: "Telemetry Alerts Policy"
intent: "nodd-sns-sqs-alert-policies"
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
requires_directory_layout_section: false
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD telemetry alerts policy"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🚨 NODD Alert Policies  

`docs/pipelines/atmo/nodd-sns-sqs/telemetry/alerts/nodd-alert-policies.md`

**Concrete alert rules, thresholds, severities, and routing profiles for the NOAA NODD SNS → SQS ingestion pipeline.**

</div>

⸻

## 🧭 1. Purpose

This document instantiates the alert categories defined in `README.md` for NODD telemetry alerts into **concrete policies**:

- Assigns **policy IDs**, thresholds, severities, and environments.  
- Describes **routing profiles** and required **runbook links** for each alert.  
- Ensures alerts are **deterministic, reproducible**, and aligned with NODD SLOs.

Platform-specific alert configs (Grafana alerts, Alertmanager, PagerDuty, etc.) MUST implement these policies without weakening thresholds or removing mandatory alerts.

⸻

## 🧱 2. Policy Conventions

Policy fields (conceptual schema):

    id:           Stable policy identifier (e.g., NODD-Q-AGE-CRIT)
    category:     Queue | DLQ | Replay | Latency | Telemetry | EnergyCarbon
    severity:     critical | warning | info
    env:          dev | stage | prod (one or more)
    metric:       Primary telemetry metric name
    condition:    Human-readable threshold and logic
    window:       Evaluation window (lookback)
    cooldown:     Minimum interval between repeated alerts
    routes:       Logical routing profiles (on-call, SRE channel, etc.)
    runbooks:     Paths to one or more runbooks in repo
    notes:        Optional rationale or implementation notes

All conditions are expressed in terms of metrics defined in `telemetry_schema`.

⸻

## 📬 3. Queue Health Policies

### 3.1 Policy: Queue Age SLO Breach (Critical)

    id:        NODD-Q-AGE-CRIT
    category:  Queue
    severity:  critical
    env:       prod
    metric:    nodd_sns.queue_age_seconds{queue,env,quantile}

Condition:

- Target queue: primary ingestion queue (as declared in config).  
- For `quantile = "0.9"` and `env = "prod"`:  
  - P90 queue age > 90 seconds for at least 10 minutes (e.g., 10 × 1-minute evaluations).

Window:

- 10 minutes rolling.

Cooldown:

- 30 minutes.

Routes:

- oncall_primary: "KFM NODD On-Call"  
- notify_channels: "kfm-nodd-sre", "kfm-ops"

Runbooks:

- `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/delayed-queue-runbook.md`  
- `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/capacity-tuning-runbook.md`

Notes:

- This enforces the NODD queue-age SLO (P90 < 90s) for production.

⸻

### 3.2 Policy: Queue Depth High (Warning/Critical)

    id:        NODD-Q-DEPTH-WARN
    category:  Queue
    severity:  warning
    env:       stage, prod
    metric:    nodd_sns.queue_depth{queue,env}

Condition (warning):

- For the primary queue:
  - Depth > 5,000 messages for at least 15 minutes.

Window:

- 15 minutes.

Cooldown:

- 60 minutes.

Routes:

- notify_channels: "kfm-nodd-sre"

Condition (critical; separate rule):

    id:        NODD-Q-DEPTH-CRIT
    severity:  critical

- Depth > 20,000 messages OR  
- Depth increasing > 1,000 messages per 5 minutes over 15 minutes.

Routes (critical):

- oncall_primary: "KFM NODD On-Call"  
- notify_channels: "kfm-nodd-sre", "kfm-ops"

Runbooks:

- `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/delayed-queue-runbook.md`

⸻

## 🧪 4. DLQ & Failure Policies

### 4.1 Policy: DLQ Rate SLO Breach (Critical)

    id:        NODD-DLQ-RATE-CRIT
    category:  DLQ
    severity:  critical
    env:       prod
    metric:    nodd_sns.dlq_messages_total{queue,env,dataset}

Condition:

- For DLQ attached to primary ingestion queue, `env = "prod"`:  
  - DLQ rate (DLQ messages / total messages) > 0.05% over 30 minutes, OR  
  - Absolute DLQ count increase > 1,000 messages over 30 minutes.

Window:

- 30 minutes.

Cooldown:

- 60 minutes.

Routes:

- oncall_primary: "KFM NODD On-Call"  
- notify_channels: "kfm-nodd-sre", "kfm-ops"

Runbooks:

- `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/dlq-drain-runbook.md`  
- `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/validation-error-investigation-runbook.md`

⸻

### 4.2 Policy: Validation / Governance Error Surge (Warning)

    id:        NODD-VAL-ERR-WARN
    category:  DLQ
    severity:  warning
    env:       stage, prod
    metric:    nodd_sns.validation_errors_total{dataset,env,error_type}

Condition:

- For any `dataset`, `env ∈ {stage, prod}`:  
  - Rate of a single `error_type` (e.g., `schema_mismatch`, `governance_violation`) > 10 errors / 5 minutes, and  
  - At least 5× the 24-hour baseline.

Window:

- 15 minutes.

Cooldown:

- 60 minutes.

Routes:

- notify_channels: "kfm-nodd-sre"

Runbooks:

- `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/validation-error-investigation-runbook.md`

Notes:

- Intended to surface schema drift, upstream format changes, or governance misconfiguration.

⸻

## 🔁 5. Replay & Determinism Policies

### 5.1 Policy: Replay Mismatch (Critical, Hard SLO)

    id:        NODD-REPLAY-MISMATCH-CRIT
    category:  Replay
    severity:  critical
    env:       prod
    metric:    nodd_sns.replay_mismatch_total{dataset,env}

Condition:

- Any increase of `replay_mismatch_total` in `env = "prod"` during the last 5 minutes.

Window:

- 5 minutes.

Cooldown:

- 15 minutes.

Routes:

- oncall_primary: "KFM NODD On-Call"  
- notify_channels: "kfm-nodd-sre", "kfm-reliability"

Runbooks:

- `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/incident-replay-runbook.md`  
- `docs/pipelines/lineage/ci-validation/README.md` (for lineage cross-checks)

Notes:

- Any non-zero mismatch is treated as a P1 event because it violates deterministic WAL semantics.

⸻

### 5.2 Policy: Unexpected Replay Volume (Warning)

    id:        NODD-REPLAY-VOLUME-WARN
    category:  Replay
    severity:  warning
    env:       prod
    metric:    nodd_sns.replays_total{dataset,env,reason}

Condition:

- For `reason` = `incident` or `dlq-drain` in `env = "prod"`:  
  - Replays > 500 per hour OR  
  - Replays per hour > 3× 7-day moving average.

Window:

- 60 minutes.

Cooldown:

- 120 minutes.

Routes:

- notify_channels: "kfm-nodd-sre"

Runbooks:

- `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/dlq-drain-runbook.md`  
- `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/incident-replay-runbook.md`

⸻

## ⏱ 6. Ingest Latency Policies

### 6.1 Policy: Ingest Latency SLO Breach (Critical)

    id:        NODD-LAT-P90-CRIT
    category:  Latency
    severity:  critical
    env:       prod
    metric:    nodd_sns.ingest_latency_seconds{dataset,env,quantile}

Condition:

- For priority datasets (e.g., `goes-abi`, `nexrad-l2`, `hrrr`) in `env = "prod"`:  
  - P90 ingest latency > 300 seconds (5 minutes) for at least 20 minutes.

Window:

- 20 minutes.

Cooldown:

- 60 minutes.

Routes:

- oncall_primary: "KFM NODD On-Call"  
- notify_channels: "kfm-nodd-sre"

Runbooks:

- `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/delayed-queue-runbook.md`  
- Infrastructure capacity or networking runbooks (referenced from infra docs).

⸻

### 6.2 Policy: Latency Trend Degradation (Warning)

    id:        NODD-LAT-TREND-WARN
    category:  Latency
    severity:  warning
    env:       stage, prod
    metric:    nodd_sns.ingest_latency_seconds{dataset,env,quantile}

Condition:

- For any dataset, `env ∈ {stage, prod}`:  
  - P90 latency > 2× 24-hour baseline for 30 minutes.

Window:

- 30 minutes.

Cooldown:

- 120 minutes.

Routes:

- notify_channels: "kfm-nodd-sre"

⸻

## 📡 7. Telemetry Coverage Policies

### 7.1 Policy: Telemetry Silence (Critical in Prod)

    id:        NODD-TEL-SILENCE-CRIT
    category:  Telemetry
    severity:  critical
    env:       prod
    metric:    nodd_sns.ingest spans or equivalent ingest metrics

Condition:

- No ingest spans or ingest-completion metrics in `env = "prod"` for > 10 minutes  
  while the pipeline is expected to be active (based on schedule/config).

Window:

- 10 minutes.

Cooldown:

- 30 minutes.

Routes:

- oncall_primary: "KFM NODD On-Call"  
- notify_channels: "kfm-nodd-sre", "kfm-infra"

Runbooks:

- Infra / telemetry collector runbooks (infra repo)  
- `docs/pipelines/atmo/nodd-sns-sqs/telemetry/README.md` for metric expectations

⸻

### 7.2 Policy: Metric Family Missing (Warning)

    id:        NODD-TEL-METRIC-MISS-WARN
    category:  Telemetry
    severity:  warning
    env:       stage, prod
    metric:    queue depth, queue age, latency families

Condition:

- For `env ∈ {stage, prod}`:  
  - Any of the core metric families (queue depth, queue age, ingest latency) absent for > 30 minutes.

Window:

- 30 minutes.

Cooldown:

- 120 minutes.

Routes:

- notify_channels: "kfm-nodd-sre"

⸻

## 🌱 8. Energy & Carbon Policies (Optional)

These policies apply only when energy/carbon telemetry is enabled and validated.

### 8.1 Policy: Energy per Unit Anomaly (Info/Warning)

    id:        NODD-ENERGY-PER-UNIT-WARN
    category:  EnergyCarbon
    severity:  info (or warning if paging is desired)
    env:       prod
    metric:    nodd_sns.energy_kwh_total{env}, nodd_sns.bytes_ingested_total{env}

Condition:

- Derived metric: kWh per GB ingested.  
- > 2× 30-day baseline for at least 24 hours.

Window:

- 24 hours.

Cooldown:

- 24 hours.

Routes:

- notify_channels: "kfm-sustainability", "kfm-nodd-sre"

Notes:

- Intended for sustainability tracking, not immediate paging.

⸻

## 🧪 9. CI & Drift Detection

CI MUST:

- Validate that infrastructure alert rule definitions:
  - Include policies with these `id` values.  
  - Use metrics and label sets consistent with `telemetry_schema`.  
  - Implement thresholds no weaker than those specified here (stricter thresholds are allowed with review).  

- Fail if:
  - A core policy (queue age, DLQ SLO, replay mismatch, ingest latency P90) is missing.  
  - A policy exists with modified thresholds that weaken SLO enforcement without corresponding changes to this document.

Governance reviews MUST:

- Re-confirm policy set and thresholds at least once per review_cycle.  
- Update this document when SLOs or alerting strategies change.

⸻

## 🕰 10. Version History

| Version  | Date       | Notes                                                                                             |
|---------:|------------|---------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD alert policy set; concretized queue, DLQ, replay, latency, telemetry and energy rules.|

---

<div align="center">

🚨 NODD Alert Policies · KFM v11.2.3  

SLO-Driven · Reproducible · Governance-Enforced  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Alerts Spec](README.md) ·  
[📊 Dashboards](../dashboards/README.md) ·  
[📁 Telemetry Samples](../samples/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
