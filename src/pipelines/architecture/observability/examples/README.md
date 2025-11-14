---
title: "📡 Kansas Frontier Matrix — Observability Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/observability/examples/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-observability-examples-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📡 **Kansas Frontier Matrix — Observability Examples**  
`src/pipelines/architecture/observability/examples/README.md`

**Purpose:**  
Provide **complete, canonical examples** of logs, metrics, traces, and observability artifacts generated during KFM pipeline execution.  
These examples demonstrate **FAIR+CARE visibility**, **SLSA-level provenance**, **deterministic monitoring**, and **MCP-DL v6.3 compliance** for the entire pipeline lifecycle.

<img alt="Docs" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue"/>
<img alt="License" src="https://img.shields.io/badge/License-MIT-green"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Examples-success"/>

</div>

---

## 📘 Overview

KFM observability includes:

- **Structured logs** (JSON)
- **Metrics** (Prometheus/OpenMetrics)
- **Distributed tracing** (OpenTelemetry)
- **Energy & CO₂ telemetry**
- **Governance-aware signals** (CARE flags, masking events)
- **Validation indicators** (schema/STAC/FAIR+CARE outcomes)

This document provides **validated examples** for each observability domain.

---

## 📁 Directory Layout

~~~~~text
src/pipelines/architecture/observability/examples/
├── README.md                        # This file
├── logs.json                        # Structured log example
├── metrics.prom                    # Prometheus metrics example
├── trace.json                       # OpenTelemetry trace example
└── telemetry_record.json            # Combined telemetry export example
~~~~~

---

## 🧩 Example — Structured Log Entry

~~~~~json
{
  "timestamp": "2025-11-13T18:44:09Z",
  "pipeline_id": "etl_hydrology_2025_v10.3.1",
  "dataset_id": "hydrology_flow_ks",
  "event": "validation_passed",
  "runtime_ms": 9334,
  "records_processed": 23871,
  "attempt": 1,
  "idempotency_key": "sha256:f091aa33...",
  "care_label": "public",
  "sovereignty": null,
  "success": true,
  "message": "Schema + FAIR+CARE validation complete."
}
~~~~~

### Notes:
- MUST be JSON.
- MUST include `care_label` & `idempotency_key`.
- MUST exclude PII.

---

## 📊 Example — Metrics (Prometheus/OpenMetrics)

~~~~~text
# HELP kfm_pipeline_runtime_seconds Total runtime of pipeline in seconds
# TYPE kfm_pipeline_runtime_seconds gauge
kfm_pipeline_runtime_seconds{pipeline_id="etl_hydrology_2025_v10.3.1"} 9.334

# HELP kfm_pipeline_records_processed Number of processed records
# TYPE kfm_pipeline_records_processed gauge
kfm_pipeline_records_processed{dataset_id="hydrology_flow_ks"} 23871

# HELP kfm_pipeline_energy_wh Energy used (watt-hours)
# TYPE kfm_pipeline_energy_wh gauge
kfm_pipeline_energy_wh{pipeline_id="etl_hydrology_2025_v10.3.1"} 14.2

# HELP kfm_pipeline_care_violations CARE governance violations detected
# TYPE kfm_pipeline_care_violations counter
kfm_pipeline_care_violations{dataset_id="hydrology_flow_ks"} 0
~~~~~

### Notes:
- Metrics MUST include dataset/pipeline scoping.
- A11y/CARE metrics are required for governance visibility.

---

## 🛰️ Example — OpenTelemetry Trace

~~~~~json
{
  "trace_id": "d7b813845a3eb32e",
  "span_id": "31cd77a9eaa71255",
  "parent_span_id": null,
  "name": "etl:hydrology_flow",
  "start_time": "2025-11-13T18:44:00Z",
  "end_time": "2025-11-13T18:44:09Z",
  "attributes": {
    "kfm.pipeline_id": "etl_hydrology_2025_v10.3.1",
    "kfm.dataset_id": "hydrology_flow_ks",
    "kfm.care_label": "public",
    "kfm.idempotency_key": "sha256:f091aa33...",
    "kfm.records_processed": 23871,
    "kfm.retry_count": 1,
    "kfm.energy_wh": 14.2,
    "kfm.co2_g": 0.0054
  },
  "events": [
    {
      "name": "masking_check",
      "timestamp": "2025-11-13T18:44:03Z",
      "attributes": {
        "care_masking_applied": false
      }
    },
    {
      "name": "validation",
      "timestamp": "2025-11-13T18:44:08Z",
      "attributes": {
        "schema_valid": true,
        "care_valid": true
      }
    }
  ],
  "status": {
    "code": 1,
    "message": "OK"
  }
}
~~~~~

---

## 📡 Example — Combined Telemetry Record

~~~~~json
{
  "pipeline_id": "etl_hydrology_2025_v10.3.1",
  "dataset_id": "hydrology_flow_ks",
  "idempotency_key": "sha256:f091aa33...",
  "runtime_sec": 9.334,
  "energy_wh": 14.2,
  "co2_g": 0.0054,
  "records_processed": 23871,
  "care_label": "public",
  "care_masking_applied": false,
  "retry_count": 1,
  "checksum": "sha256:9393aa331...",
  "telemetry_timestamp": "2025-11-13T18:44:09Z",
  "governance_ref": "docs/reports/audit/pipeline_observability_ledger.json"
}
~~~~~

Stored in:

~~~~~text
../../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Added validated examples for logs, metrics, traces, and telemetry for KFM v10.3 pipelines. |

---

<div align="center">

**Kansas Frontier Matrix — Observability Examples**  
Full-Stack Insight × FAIR+CARE Transparency × Deterministic Monitoring  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Observability](../README.md)

</div>
