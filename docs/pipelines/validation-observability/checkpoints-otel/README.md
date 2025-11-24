---
title: "📊 KFM v11 — GE Checkpoints + OpenTelemetry Metrics Integration (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/pipelines/validation-observability/checkpoints-otel/README.md"
version: "v11.0.1"
last_updated: "2025-11-24"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/validation-observability-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/validation-observability-v11.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
status: "Active / Enforced"
---

# 📊 GE Checkpoints + OpenTelemetry Metrics  
### **Deterministic Validation · Metric Emissions · SLO Enforcement**

This folder documents how **Great Expectations (GE)** and **OpenTelemetry (OTel)** combine to provide **uniform, cross-pipeline validation and observability** in KFM v11.

Every autonomous update, ETL batch, and AI pipeline is required to wrap data mutation steps with:

1. **GE Checkpoint Execution**  
2. **Metric Emission (OTel Counter + Histogram)**  
3. **Promotion Gating** based on failed expectations  

This subsystem is part of the **Reliable Pipelines v11** strategy and feeds into dashboards, SLOs, error budgets, and the pipeline kill-switch.

---

# 📁 Directory Layout

```text
docs/pipelines/validation-observability/checkpoints-otel/
│
├── README.md
│   # This file — full specification of GE + OTel integration
│
├── examples/
│   # Minimal runnable examples used by CI and developers
│
├── suites/
│   # GE Expectation Suites (KFM structured)
│   # One suite per dataset or pipeline stage
│
├── checkpoints/
│   # GE Checkpoint YAMLs following naming: kfm_<stage>_ckpt.yml
│
└── runners/
    # Python runners for pipeline-level integration
    # Emits OTel metrics after executing Checkpoints
```

---

# 🎯 Purpose

KFM v11 enforces **deterministic, audit-ready validation** for every data-changing operation.

This module ensures:

- ✔ **Schema & value constraints** are validated before promotion  
- ✔ **Freshness, drift, reference integrity** are continuously tested  
- ✔ **Errors are observable** through consistent OTel metric names  
- ✔ **Promotion gates** fail CI/CD when expectations fail  
- ✔ **Dashboards** unify pass/fail counts, latency, and row deltas  
- ✔ **Root-cause analysis** is supported via Checkpoint result stores  

---

# 📦 Required Metric Names (OTel v11 Spec)

Pipelines MUST emit:

- `kfm.update_errors` – number of failed expectations  
- `kfm.rows_ingested` – rows committed during this run  
- `kfm.latency_ms` – full task runtime in milliseconds  

Labels (required):

- `pipeline`  
- `stage`  
- `table`  
- `env`  

Example:

```
kfm.update_errors{pipeline="ingest_v11", stage="validate", table="my_table", env="prod"} = 3
```

---

# 🧩 GE Checkpoint Contract

All KFM checkpoints MUST:

- Use `StoreValidationResultAction`  
- Include `UpdateDataDocsAction`  
- Reference a valid suite under `suites/`  
- Follow naming conventions:  

```
kfm_ingest_ckpt.yml
kfm_harmonize_ckpt.yml
kfm_publish_ckpt.yml
```

---

# 🐍 Python Runner Standard (v11)

Runners in `/runners/` must:

1. Load and run a GE Checkpoint  
2. Parse statistics  
3. Emit metrics via OTel  
4. Exit non-zero if failures occur  
5. Emit row deltas (if available)  
6. Log PROV-O lineage entries to the pipeline ledger  

Runners **must not mutate data** before GE execution.

---

# 📊 Dashboards & SLO Alignment

This module feeds the following dashboards:

- SLO Latency (p50/p95/p99)
- Validation Failures over Time
- Row Drift / Volume Change Detection
- Autonomous Update Safety Checks

Dashboards consuming this module follow the contract defined in:

`docs/pipelines/reliability/slo-error-budgets.md`

---

# 🧪 Testing & CI/CD Enforcement

CI performs:

- Checkpoint syntax validation  
- Expectation suite linting  
- Dry-run of OTel metric emission  
- YAML + schema validation via JSONSchema  

Promotion is **blocked** if:

- Any suite has >0 failed expectations  
- Any OTel metric fails emission schema  
- Runners do not exit deterministically  

---

# 🔒 Provenance, FAIR+CARE, and Ethical Handling

All validation results are:

- Stored with timestamps and commit SHAs  
- Linked to PROV-O lineage records  
- Included in quarterly FAIR+CARE audits  
- Exported as JSON-LD for long-term reproducibility  

---

# 📌 Related Documents

- `reliable-pipelines.md`  
- `slo-error-budgets.md`  
- `validation-observability/README.md`  
- `standards/governance/ROOT-GOVERNANCE.md`  

---

# 🔗 Footer

**[⬅ Back to Validation & Observability](../README.md)** ·  
**[📚 Standards Index](../../../standards/README.md)** ·  
**[🏠 KFM Root](../../../../README.md)**