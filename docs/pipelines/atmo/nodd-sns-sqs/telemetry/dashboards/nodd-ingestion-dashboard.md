---
title: "📊 KFM v11.2.3 — NODD Ingestion Dashboard Layout (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Canonical layout, panels, and queries for the NOAA NODD SNS → SQS core ingestion observability dashboard."
path: "docs/pipelines/atmo/nodd-sns-sqs/telemetry/dashboards/nodd-ingestion-dashboard.md"

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

doc_kind: "Telemetry Dashboard Layout"
intent: "nodd-sns-sqs-core-ingestion-dashboard"
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
requires_directory_layout_section: false
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD ingestion dashboard layout"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 📊 NODD Ingestion Dashboard — Core Layout  

`docs/pipelines/atmo/nodd-sns-sqs/telemetry/dashboards/nodd-ingestion-dashboard.md`

**Canonical observability layout for the NOAA NODD SNS → SQS ingestion pipeline: ingest health, queue SLOs, failures/DLQs/replay, and energy/carbon.**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Pipeline-NODD_SNS_%E2%86%92_SQS-skyblue" />
<img src="https://img.shields.io/badge/Dashboard-Core_ingestion-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

This document defines the **canonical layout** and **required panels** for the core NODD ingestion dashboard.

The dashboard:

- Surfaces real-time health of the **NODD SNS → SQS → worker → STAC → provenance** path.  
- Visualizes SLOs for **queue age**, **DLQ rate**, **ingest latency**, and **replay determinism**.  
- Aligns panel queries with the NODD telemetry schema and SLO spec in `telemetry/README.md`.  
- Provides a reproducible reference for dashboard JSON definitions managed in infrastructure repositories.

Any production NODD ingestion dashboard MUST implement, at minimum, the groups and panels defined here.

---

## 🎛 2. Dashboard Metadata & Variables

### 2.1 Dashboard Identity

Recommended:

- Title: `NOAA NODD Ingestion — Core`  
- UID / slug: `kfm-nodd-ingestion-core` (or equivalent)  
- Folder: `KFM / Pipelines / Atmospheric / NODD` (implementation-dependent)

### 2.2 Required Variables

The dashboard MUST define the following variables (names may vary, semantics MUST match):

- `$env`  
  - Values: `dev`, `stage`, `prod` (or KFM-standard environments).  
  - Purpose: filter all panels to a single environment.

- `$dataset`  
  - Values: canonical NODD dataset IDs (e.g., `goes-abi`, `nexrad-l2`, `nexrad-l3`, `hrrr`, `surface-obs`).  
  - Purpose: filter per-dataset panels.

- `$queue`  
  - Values: relevant SQS queues (e.g., `nodd-primary-queue`, `nodd-dlq`).  
  - Purpose: filter queue-health panels.

Variables MUST be wired into queries via label filters, not string concatenation or unbounded regex.

---

## 🧱 3. Layout Overview (Rows / Groups)

The dashboard is organized into four logical groups, each represented by one or more rows or collapsible sections:

1. **Ingest Health & Throughput**  
2. **Queue Health & SLOs**  
3. **Failures, DLQs & Replay**  
4. **Energy, Carbon & Cost** (optional but recommended)

The remaining sections describe the required panels per group.

---

## 🚀 4. Ingest Health & Throughput

### 4.1 Panel: Ingest Latency (P50/P90/P99)

- Title: `Ingest Latency — P50/P90/P99 by Dataset`  
- Type: Time-series line chart.  
- Source metric: `nodd_sns.ingest_latency_seconds` (histogram or summary).  
- Dimensions:
  - `dataset` (color/series).  
  - `env = $env`.

Display requirements:

- P50, P90, P99 curves for each dataset (or aggregated with per-dataset drill-down).  
- SLO line at 300 seconds (5 minutes) for P90 ingestion.

### 4.2 Panel: Ingest Throughput (Items / Bytes)

- Title: `Ingest Throughput — Items/Bytes per Dataset`  
- Type: Time-series bar or step-line.  
- Source metrics:
  - Item count (from span counts or explicit metric).  
  - `nodd_sns.bytes_ingested_total` (rate) for volume.

Dimensions:

- `dataset`, filtered by `$dataset` or showing top N datasets.  
- `env = $env`.

### 4.3 Panel: Ingest Outcome Breakdown

- Title: `Ingest Outcomes — Success vs Failed`  
- Type: Stacked bar or stacked area.  
- Source:
  - Outcome metric derived from spans or explicit counters (e.g., `status` label).  

Requirements:

- Show proportion of successful vs failed ingestion attempts over time.  
- Visual emphasis on failure spikes.

---

## 📬 5. Queue Health & SLOs

### 5.1 Panel: SQS Queue Depth

- Title: `Queue Depth — Primary & DLQ`  
- Type: Time-series line chart.  
- Source metric: `nodd_sns.queue_depth{queue,env}`.  
- Dimensions:
  - `queue`, filtered by `$queue` or displaying primary + DLQ.  
  - `env = $env`.

### 5.2 Panel: Queue Age (P50/P90/P99)

- Title: `Queue Age — P50/P90/P99 with SLO`  
- Type: Time-series multi-line.  
- Source metric: `nodd_sns.queue_age_seconds{queue,env,quantile}`.  

Requirements:

- Lines for P50, P90, and P99 per selected `queue`.  
- SLO line at 90 seconds for P90.  
- Visual emphasis (color/annotation) when P90 exceeds SLO.

### 5.3 Panel: Watermark Lag (if implemented)

- Title: `Event-Time Watermark Lag by Dataset`  
- Type: Table or heatmap.  
- Source metric: `nodd_sns.watermark_lag_seconds{dataset,partition,env}`.  

Display:

- For each `dataset`, max or P95 `watermark_lag_seconds` across partitions.  
- Sorting by worst lag to surface problem datasets.

---

## 🧪 6. Failures, DLQs & Replay

### 6.1 Panel: DLQ Volume

- Title: `DLQ Messages — Rate by Dataset`  
- Type: Stacked time-series (rate).  
- Source metric: `nodd_sns.dlq_messages_total{queue,env,dataset}` (derivative/rate).  

Requirements:

- Use `$env` and `$queue` filters.  
- Show which datasets are sending items into DLQ and when.

### 6.2 Panel: Error Breakdown by Reason

- Title: `Validation & Governance Errors — Top Reasons`  
- Type: Bar chart or table.  
- Source metric: `nodd_sns.validation_errors_total{dataset,env,error_type}`.  

Display:

- Top `error_type` values over a selected window.  
- Optional grouping by `dataset`.

### 6.3 Panel: Replay Activity

- Title: `Replay Activity — Count by Dataset`  
- Type: Time-series line chart.  
- Source metric: `nodd_sns.replays_total{dataset,env,reason}`.  

Requirements:

- Distinguish `reason` (e.g., `incident`, `backfill`, `dlq-drain`) as series or legend entries.  
- Filterable by `$dataset`.

### 6.4 Panel: Replay Determinism Violations

- Title: `Replay Mismatches — Must Be Zero`  
- Type: Single-stat or time-series.  
- Source metric: `nodd_sns.replay_mismatch_total{dataset,env}` (rate or cumulative).  

Display:

- Highlight any non-zero values as **SLO violation**.  
- Panel description MUST reference replay runbooks under `replay/runbooks/incident-replay-runbook.md`.

---

## 🌱 7. Energy, Carbon & Cost

(Enabled only when telemetry for energy and carbon is active.)

### 7.1 Panel: Energy Usage

- Title: `Energy Usage — NODD Ingestion (kWh)`  
- Type: Time-series line chart.  
- Source metric: `nodd_sns.energy_kwh_total{env}` (rate/derivative).  

Display:

- Lines per `env`.  
- Optional annotation for major pipeline changes impacting energy.

### 7.2 Panel: Carbon Emissions

- Title: `Carbon Emissions — NODD Ingestion (gCO₂e)`  
- Type: Time-series line chart.  
- Source metric: `nodd_sns.carbon_gco2e_total{env}` (rate/derivative).  

Both panels MUST:

- Use definitions from `energy_schema` and `carbon_schema`.  
- Clearly label values as **estimates**, not audited totals.

Optional cost proxy panels MAY be defined in infrastructure repos; if they become mandatory, this document MUST be updated.

---

## 🧩 8. Accessibility & Usability

The dashboard MUST:

- Respect **WCAG 2.1 AA** color contrast requirements.  
- Use:
  - Color + shape or line style for critical distinctions (not color alone).  
  - Clear, descriptive panel titles and hover text.  
- Provide:
  - Saved default time ranges (e.g., 6h).  
  - Tooltips that display raw metric values and key labels (`dataset`, `env`, `queue`).

Any structural change impacting accessibility (e.g., color palettes) must be reviewed under KFM accessibility standards.

---

## 🧪 9. Validation & Change Management

Changes to this dashboard MUST:

- Keep metric names and labels aligned with `telemetry_schema`.  
- Preserve required panels and groups unless formally deprecated in a new version of this document.  
- Be reflected in:
  - Infrastructure-managed dashboard JSON.  
  - Telemetry samples in `telemetry/samples/`.

CI SHOULD:

- Validate that deployed dashboard JSON:
  - Parses correctly.  
  - Contains panels with titles matching or equivalent to those defined here.  
  - Uses metric names defined in the telemetry spec.

Removing or renaming required panels without updating this document and passing review is a governance violation.

---

## 🕰 10. Version History

| Version  | Date       | Notes                                                                                                    |
|---------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial canonical layout for the NODD ingestion dashboard; aligned with NODD telemetry + SLO specification. |

---

<div align="center">

📊 NODD Ingestion Dashboard — Core · KFM v11.2.3  

Schema-Grounded · SLO-Driven · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Telemetry Dashboards](README.md) ·  
[📁 Telemetry Samples](../samples/README.md) ·  
[🧠 Operators](../../operators/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
