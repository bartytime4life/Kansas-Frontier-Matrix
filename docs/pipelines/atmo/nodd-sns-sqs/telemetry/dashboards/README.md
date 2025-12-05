---
title: "📊 KFM v11.2.3 — NODD Telemetry Dashboards Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed specification for NOAA NODD SNS → SQS observability dashboards: layout, panels, queries, and SLO visualizations."
path: "docs/pipelines/atmo/nodd-sns-sqs/telemetry/dashboards/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x telemetry-dashboard compatible"
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

doc_kind: "Telemetry Dashboard Specification"
intent: "nodd-sns-sqs-telemetry-dashboards"
category: "Pipelines · Atmospheric · Telemetry · Dashboards"

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
sunset_policy: "Superseded by next major NODD telemetry dashboard standard"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 📊 NODD Telemetry Dashboards Specification  

`docs/pipelines/atmo/nodd-sns-sqs/telemetry/dashboards/README.md`

**Governed layout and panel specification for NOAA NODD SNS → SQS observability dashboards (queue health, latency, DLQs, replay determinism, energy/carbon).**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Pipeline-NODD_SNS_%E2%86%92_SQS-skyblue" />
<img src="https://img.shields.io/badge/Telemetry-Dashboards-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

This document defines the **canonical dashboards** for the NOAA NODD SNS → SQS ingestion pipeline:

- Establishes which dashboards MUST exist and their high-level layout.  
- Aligns panels with the **telemetry schema**, SLOs, and error budgets.  
- Ensures dashboards are **reproducible, versioned artifacts**, not ad hoc UI-only creations.  
- Provides a reference for **SREs, engineers, and governance reviewers**.

Concrete dashboard JSON (Grafana or equivalent) may live in infrastructure repos, but MUST conform to this specification.

---

## 🗂 2. Directory Layout (Dashboards)

This directory lives under `docs/pipelines/atmo/nodd-sns-sqs/telemetry/dashboards/` and MUST contain:

    docs/pipelines/atmo/nodd-sns-sqs/telemetry/dashboards/
    │
    ├── 📄 README.md                     # This file (dashboard specification index)
    │
    └── 📄 nodd-ingestion-dashboard.md   # Core pipeline dashboard: layout, panels, queries, SLO overlays

Additional dashboard specs (e.g., per-dataset views or governance dashboards) MUST be added as separate `.md` files and referenced from this README.

---

## 🧱 3. Core Dashboard Set

At minimum, KFM MUST expose a **core ingestion dashboard** documented in:

- `nodd-ingestion-dashboard.md`

That dashboard MUST include panels grouped into four logical sections:

1. **Ingest Health & Throughput**  
2. **Queue Health & SLOs**  
3. **Failures, DLQs & Replay**  
4. **Energy, Carbon & Cost (optional but recommended)**  

Each group is summarized here; precise panel lists and queries belong in `nodd-ingestion-dashboard.md`.

---

## 🚀 4. Ingest Health & Throughput

Required panels:

- **Ingest Latency (Distribution)**  
  - Metric: `nodd_sns.ingest_latency_seconds` (histogram/summary).  
  - Views:
    - P50/P90/P99 latency by `dataset`.  
    - SLO reference line (e.g., P90 < 300s).

- **Ingest Throughput (Per Dataset)**  
  - Metric: count of ingest completions or `nodd_sns.bytes_ingested_total`.  
  - Views:
    - Time-series of items or bytes ingested, grouped by `dataset`.  
    - Ability to filter by `env` (`dev`, `stage`, `prod`).

- **Success vs Failure Rate**  
  - Derived from spans or explicit ingestion outcome metrics.  
  - Stacked bar or line chart of successes vs failures over time.

Panel conventions:

- Only low-cardinality labels (`dataset`, `env`).  
- Preset time ranges: 15m, 1h, 6h, 24h, 7d.

---

## 📬 5. Queue Health & SLOs

Required panels for SQS health:

- **SQS Queue Depth**  
  - Metric: `nodd_sns.queue_depth{queue,env}`.  
  - Display: time-series trajectory for primary queue (and optionally DLQ).

- **Queue Age (P50/P90/P99)**  
  - Metric: `nodd_sns.queue_age_seconds{queue,env,quantile}`.  
  - Display:
    - Multiple lines for P50/P90/P99 with SLO threshold line at 90 seconds.

- **Watermark Lag by Dataset/Partition**  
  - Metric: `nodd_sns.watermark_lag_seconds{dataset,partition,env}` (if implemented).  
  - Display:
    - Max or P95 lag per dataset (table or heatmap).

SLO visuals:

- Clear visual indication (color bands / threshold markers) when:
  - Queue-age SLO is violated.  
  - Watermark lag exceeds configured bounds.

---

## 🧪 6. Failures, DLQs & Replay

Required panels:

- **DLQ Volume Over Time**  
  - Metric: `nodd_sns.dlq_messages_total{queue,env,dataset}` (rate or per-interval).  
  - Display:
    - Stacked by `dataset`.  
    - Highlight spikes to link with incidents and runbooks.

- **Error Breakdown by Reason**  
  - Metric: `nodd_sns.validation_errors_total{dataset,env,error_type}`.  
  - Display:
    - Bar chart or table showing top `error_type` contributors.

- **Replay Activity & Determinism**  
  - Metrics:
    - `nodd_sns.replays_total{dataset,env,reason}`.  
    - `nodd_sns.replay_mismatch_total{dataset,env}`.  
  - Display:
    - Time-series of replay counts.  
    - Single-stat or alert panel for any replay mismatch > 0.

Panels MUST link (via descriptions or annotations) to replay runbooks under `docs/pipelines/atmo/nodd-sns-sqs/replay/runbooks/`.

---

## 🌱 7. Energy, Carbon & Cost

When energy/carbon telemetry is enabled:

- **Energy Usage Over Time**  
  - Metric: `nodd_sns.energy_kwh_total{env}` (displayed as rate/derivative).  
  - View: time-series with environment filter.

- **Carbon Emissions Over Time**  
  - Metric: `nodd_sns.carbon_gco2e_total{env}` (rate/derivative).  
  - View: time-series; optional per-dataset breakdown via variables.

Optional panels:

- Cost proxy panels, if standardized cost-per-unit is defined (e.g., per GB processed).

All such panels MUST:

- Use the schemas in `energy_schema` and `carbon_schema`.  
- Clearly label values as **estimates**.

---

## 🎛 8. Panel Naming & Query Conventions

Panel titles SHOULD:

- Be short and descriptive (e.g., “Queue Age (P90) by Queue”).  
- Use consistent prefixes where useful (e.g., “SLO: …” for SLO panels).

Query conventions:

- Use metric names and labels exactly as defined in `telemetry_schema`.  
- Avoid:
  - Wildcard label matches with unbounded cardinality.  
  - Embedding environment-specific constants in queries (prefer dashboard variables).

Recommended variables:

- `$env` — environment (`dev`, `stage`, `prod`).  
- `$dataset` — dataset selector.  
- `$queue` — queue name where applicable.

---

## 🧪 9. CI & Configuration Management

Dashboards are configuration artifacts:

- Grafana (or equivalent) JSON definitions MUST be:
  - Versioned in git (typically infra repos).  
  - Tagged or labeled with the corresponding KFM version.

CI SHOULD:

- Parse dashboard JSON to ensure it is valid.  
- Optionally:
  - Check that required panels or queries exist (by title/UID).  
  - Lint queries to verify they reference required metric names.

Any change that:

- Removes a required panel,  
- Renames a core metric, or  
- Alters SLO visualizations

MUST:

- Be reflected in this README and/or `nodd-ingestion-dashboard.md`.  
- Be reviewed by the Atmospheric Systems and Provenance & Reliability Council.

---

## 🕰 10. Version History

| Version  | Date       | Notes                                                                                              |
|---------:|------------|----------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD telemetry dashboards spec; defined core dashboard groups and panel/SLO expectations.  |

---

<div align="center">

📊 NODD Telemetry Dashboards · KFM v11.2.3  

Schema-Grounded · SLO-Driven · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Telemetry](../README.md) ·  
[📁 Telemetry Samples](../samples/README.md) ·  
[🧠 Operators](../../operators/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
