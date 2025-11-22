---
title: "⚙️ KFM Telemetry Schema — Compute Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/schemas/telemetry/compute/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/compute-telemetry-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Telemetry-Schema"
intent: "compute-telemetry"
semantic_document_id: "kfm-telemetry-compute"
doc_uuid: "urn:kfm:telemetry:compute:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Low-Risk / Public"
immutability_status: "version-pinned"
---

<div align="center">

# ⚙️ **KFM Telemetry Schema — Compute Layer**  
`docs/pipelines/validation-observability/dashboards/schemas/telemetry/compute/README.md`

**Purpose:**  
Define the **compute-layer telemetry schema** for KFM v11 — capturing CPU/GPU usage, memory footprint, execution time, energy/carbon emissions, hardware lineage, and PROV-O–aligned process metadata for all ETL, AI/ML, observability, and batch workloads.

</div>

---

# 📘 Overview

The **Compute Telemetry Schema** standardizes how KFM records:

- CPU/GPU utilization  
- Memory pressure  
- Execution durations  
- Energy use (Wh)  
- Carbon footprint (gCO₂e)  
- Node/hardware profile  
- Kernel/runtime metadata  
- Pipeline lineage (PROV-O entities/activities/agents)

This schema is consumed by:

- Validation & Observability Dashboards  
- Model Audit Panels  
- FAIR+CARE Governance Reviews  
- Sustainability Ledger (ISO 50001 / ISO 14064)  
- Story Node v3 Explainability overlays  
- STAC/DCAT dataset metadata enrichment pipelines  

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/dashboards/schemas/telemetry/compute/
│
├── README.md                                   # This file
│
├── compute-telemetry-v11.schema.json            # JSON Schema definition
├── examples/                                    # Canonical examples for CI validation
│   ├── ai_batch_run_example.json
│   ├── etl_job_example.json
│   └── focus_eval_compute_telemetry.json
│
└── validators/                                  # Python/JSON schema validators
    ├── validate_compute_schema.py
    └── run_all_validations.sh
```

---

# 🧩 Schema Requirements (v11)

The **compute telemetry schema** MUST include:

### 🖥 Compute Metrics
- `cpu.percent_avg`  
- `cpu.percent_peak`  
- `gpu.utilization` (per-device)  
- `gpu.vram_used_mb`  
- `memory.used_mb`, `memory.peak_mb`

### ⚡ Energy & Carbon
- `energy_wh` — direct measurement OR modelled  
- `carbon_gco2e` — ISO 14064-aligned conversion  

### ⏱ Runtime Metrics
- `wall_time_s`  
- `kernel_time_s`  
- `io_time_s`  

### 🧬 Provenance (PROV-O)
Associated with:

- `prov:Activity` → pipeline or model run  
- `prov:Agent` → user or automation  
- `prov:Entity` → input datasets or models  
- `prov:wasAssociatedWith`, `prov:used`, `prov:generated`

### 🖧 Hardware Profile
- CPU model  
- GPU model(s)  
- Accelerator flags  
- RAM amount  
- Power profile  
- Virtualization/container metadata  

### 🧭 Metadata Alignment
- **STAC**: `processing:compute_usage` extension  
- **DCAT**: dataset-level `dct:provenance` links to telemetry  
- **ISO 19115**: quality & lineage descriptors  
- **FAIR+CARE**: required license, access, ethical notes  

---

# 🛠 Example Telemetry Blob

```json
{
  "kfm_version": "11.0.0",
  "run_id": "urn:kfm:run:etl:2025-11-21T18:22:00Z",
  "timestamp": "2025-11-21T18:23:55Z",
  "compute": {
    "cpu": {
      "percent_avg": 62.2,
      "percent_peak": 97.4
    },
    "gpu": [
      {
        "id": 0,
        "utilization": 88.1,
        "vram_used_mb": 9123
      }
    ],
    "memory": {
      "used_mb": 14520,
      "peak_mb": 16500
    }
  },
  "runtime": {
    "wall_time_s": 127.4,
    "kernel_time_s": 92.3,
    "io_time_s": 18.1
  },
  "sustainability": {
    "energy_wh": 42.8,
    "carbon_gco2e": 21.5
  },
  "hardware_profile": {
    "cpu_model": "AMD EPYC 7763",
    "gpu_models": ["NVIDIA A100 80GB"],
    "ram_gb": 256,
    "environment": "kubernetes-prod-gpu"
  },
  "prov": {
    "agent": "urn:kfm:agent:automated-etl",
    "activity": "urn:kfm:activity:etl_job_3728",
    "used": [
      "urn:kfm:data:raw:usgs_hydro_2024",
      "urn:kfm:model:focus_transformer_v3"
    ],
    "generated": [
      "urn:kfm:data:processed:hydro_2024_cleaned"
    ]
  }
}
```

---

# 🧪 Validation & CI Requirements

Compute telemetry MUST pass:

- **JSON Schema Validation** (`compute-telemetry-v11.schema.json`)  
- **FAIR+CARE Metadata Completeness**  
- **PROV-O Structural Validation**  
- **Energy/Carbon Bounds Check**  
- **Hardware Profile Integrity Check**  
- **SBOM Consistency Validation**  

GitHub Actions workflows:

- `compute-telemetry-validate.yml`  
- `dashboards-refresh.yml`  
- `sustainability-ledger-update.yml`

All failing validations **block merges**.

---

# 🧾 Version History

| Version | Date | Author | Notes |
|--------:|------|--------|-------|
| v11.0.0 | 2025-11-21 | `@kfm-observability` | Initial release of compute telemetry schema documentation. |

---

<div align="center">

**Kansas Frontier Matrix — Telemetry Compute Schema**  
*Precision · Provenance · Sustainability · Governance*  

[Back to Telemetry Index](../README.md) ·  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

