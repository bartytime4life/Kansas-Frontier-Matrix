---
title: "📊 Kansas Frontier Matrix — Observability Field Definitions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/observability/fields.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-observability-fields-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Observability Field Definitions**  
`src/pipelines/architecture/observability/fields.md`

**Purpose:**  
Define the **canonical field names, types, and semantics** used across logs, metrics, traces, telemetry records, and governance ledgers for KFM pipelines.  
These definitions ensure **consistent observability**, **FAIR+CARE transparency**, and **MCP-DL v6.3 alignment** for all ETL, geospatial, AI, and metadata workflows.

<img alt="Observability Fields" src="https://img.shields.io/badge/Observability-Field_Spec-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Integrated-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Enforced-success"/>

</div>

---

## 📘 Overview

This document provides a **normalized vocabulary** of observability fields, used by:

- **Structured logs** (JSON)  
- **Metrics** (Prometheus/OpenMetrics)  
- **Traces** (OpenTelemetry attributes)  
- **Telemetry JSONL records**  
- **Governance ledgers**  

All KFM components MUST use these field names and semantics to guarantee:

- Cross-pipeline comparability  
- Governance & CARE visibility  
- Telemetry schema stability  
- Dashboard correctness  

---

## 🧱 Core Identity Fields

These fields uniquely identify pipeline runs and datasets.

| Field | Type | Description | Required In |
|-------|------|-------------|-------------|
| `pipeline_id` | string | Unique ID for a pipeline run (e.g. `etl_hydrology_2025_v10.3.1`) | logs, metrics, traces, telemetry |
| `dataset_id` | string | Primary dataset identifier (e.g. `hydrology_flow_ks`) | logs, metrics, traces, telemetry |
| `run_id` | string | CI/job/infra run identifier (e.g. GitHub run ID) | telemetry, traces |
| `stage` | string (enum) | `extract`, `transform`, `validate`, `publish`, `hydrate_graph`, `telemetry` | logs, traces, metrics |
| `correlation_id` | string | Trace/causation chain ID across services | logs, traces, telemetry |
| `idempotency_key` | string | sha256 key for replay-safe operations | logs, telemetry |

---

## 🕒 Temporal & Runtime Fields

| Field | Type | Description |
|-------|------|-------------|
| `timestamp` | string (ISO8601) | UTC timestamp for the event or log entry |
| `runtime_sec` | number | Total runtime (seconds) for the run or stage |
| `stage_runtime_sec` | number | Runtime for a specific stage |
| `queue_latency_sec` | number | Time spent waiting in queues before execution |

Used in:

- Logs (`timestamp`)  
- Telemetry (`runtime_sec`)  
- Metrics (`pipeline_runtime_seconds`)  

---

## 🚦 Status & Severity Fields

| Field | Type | Description |
|-------|------|-------------|
| `severity` | string (enum) | `debug`, `info`, `warning`, `error`, `critical` |
| `status` | string (enum) | `success`, `failure`, `partial`, `skipped` |
| `validation_passed` | bool | `true` if all validation gates passed |
| `governance_status` | string (enum) | `pass`, `fail`, `escalated`, `blocked` |

These fields are required for:

- Log entries (severity)  
- Telemetry records (status)  
- Governance decisions (governance_status)  

---

## 📦 Data Volume & Throughput Fields

| Field | Type | Description |
|-------|------|-------------|
| `rows_processed` | integer | Number of tabular rows processed |
| `features_processed` | integer | Vector features processed |
| `raster_pixels_processed` | integer | Count of raster pixels processed |
| `items_polled` | integer | STAC Items polled from providers |
| `items_published` | integer | STAC Items successfully published |
| `items_quarantined` | integer | STAC Items sent to quarantine |
| `collections_published` | integer | STAC Collections published |

These fields feed metrics and telemetry dashboards.

---

## ⚖️ FAIR+CARE & Governance Fields

| Field | Type | Description |
|-------|------|-------------|
| `care_label` | string (enum) | `public`, `sensitive`, `restricted` |
| `care_violations` | integer | Number of CARE rule violations detected |
| `sovereignty_conflicts` | integer | Number of sovereignty/tribal intersection issues detected |
| `masking_applied` | bool | Whether masking or generalization was applied |
| `masking_strategy` | string | Strategy used (e.g. `h3_r7`, `bbox_expand_10km`, `centroid_fuzz_500m`) |
| `license_id` | string | SPDX or provider license identifier |
| `governance_ref` | string | Path/URI to governance ledger entry |

These fields MUST be surfaced in:

- Telemetry JSONL  
- Logs where governance is relevant  
- Governance ledgers  

---

## 🔐 Error & Retry Fields

| Field | Type | Description |
|-------|------|-------------|
| `error_class` | string | High-level classification (e.g. `HTTP_503`, `SchemaError`, `CareViolation`) |
| `error_message` | string | Human-readable error description (no secrets/PII) |
| `retry_attempt` | integer | Current retry attempt index (0-based) |
| `retryable` | bool | Whether error was considered retryable |
| `retry_policy` | string | Name of policy (e.g. `exp_full_jitter`) |
| `retry_delay_ms` | integer | Delay before this retry, in milliseconds |
| `circuit_open` | bool | Indicates if circuit breaker is open |

Required in:

- Retry-related logs  
- Telemetry for retries & circuit breakers  

---

## ⚙️ Validation & Schema Fields

| Field | Type | Description |
|-------|------|-------------|
| `schema_valid` | bool | Did the dataset pass all schema checks? |
| `schema_errors` | integer | Count of schema-validation errors |
| `validation_suite` | string | Name of GE or validation suite used |
| `validation_runtime_sec` | number | Time spent in validation stage |

Used in:

- Telemetry  
- Validation logs  
- Metrics (e.g. `validation_failures_total`)  

---

## 🌱 Sustainability & Resource Fields

| Field | Type | Description |
|-------|------|-------------|
| `energy_wh` | number | Estimated energy in watt-hours |
| `co2_g` | number | Estimated CO₂e in grams |
| `cpu_pct` | number | Average CPU utilization (0–100) |
| `memory_mb` | number | Peak memory usage in MB |
| `io_read_mb` | number | Total MB read |
| `io_write_mb` | number | Total MB written |

These fields are essential for:

- Sustainability dashboards  
- Release-level `focus-telemetry.json`  
- ISO-aligned environmental reporting  

---

## 🧬 Provenance & Lineage Fields

| Field | Type | Description |
|-------|------|-------------|
| `source_ids` | array(string) | IDs of input datasets (STAC/DCAT/etc.) |
| `source_checksums` | array(string) | sha256 checksums of inputs |
| `output_checksum` | string | sha256 checksum of primary output |
| `lineage_ref` | string | Path to lineage JSON (PROV-O bundle) |
| `stac_item_ref` | string | Path to related STAC Item |
| `dcat_dataset_ref` | string | Path to DCAT Dataset JSON |

All lineage-aware telemetry and logs must refer to these fields.

---

## 🛰️ Trace Attribute Mapping (OTel)

When encoding observability as **OpenTelemetry attributes**, use:

| OTel Attribute | Source Field |
|----------------|-------------|
| `kfm.pipeline_id` | `pipeline_id` |
| `kfm.dataset_id` | `dataset_id` |
| `kfm.stage` | `stage` |
| `kfm.care_label` | `care_label` |
| `kfm.retry_attempt` | `retry_attempt` |
| `kfm.error_class` | `error_class` |
| `kfm.energy_wh` | `energy_wh` |
| `kfm.co2_g` | `co2_g` |

This ensures consistent attribute naming for traces.

---

## 📡 Telemetry Schema Alignment

All telemetry JSONL records and `focus-telemetry.json` entries MUST:

- Use **exact field names** from this file  
- Use **types** as defined (string, number, bool, array)  
- Conform to `telemetry_schema` referenced in YAML front matter  

Failure to comply:

- Causes CI failures in `telemetry-export.yml`  
- Blocks release gating and governance approval  

---

## 🧪 Local & CI Validation

### Local Checks

- Use `jq` or JSON Schema validators to confirm fields exist and types match  
- Run unit tests around telemetry emitters and log formatters  

### CI Checks

- `telemetry-export.yml` uses JSON Schema to validate telemetry structures  
- `faircare-validate.yml` ensures CARE-related fields are present  
- `docs-lint.yml` verifies this spec stays consistent as a single source of truth  

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Pipeline Architecture Team | Introduced canonical observability field definitions across logs, metrics, traces, telemetry, and governance. |

---

<div align="center">

**Kansas Frontier Matrix — Observability Field Definitions**  
Consistent Signals × FAIR+CARE Visibility × Reproducible Telemetry  
© 2025 Kansas Frontier Matrix — MIT License  

</div>
