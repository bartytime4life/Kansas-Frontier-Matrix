---
title: "🧪 Kansas Frontier Matrix — Experiment Reproducibility & Validation Reports"
path: "docs/reports/self-validation/experiments/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/docs-reports-experiments-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Experiment Reproducibility & Validation Reports**
`docs/reports/self-validation/experiments/README.md`

**Purpose:** Document and summarize the reproducibility and validation outcomes for all scientific and AI experiments conducted within the Kansas Frontier Matrix (KFM).  
These reports ensure experiment transparency, parameter consistency, and adherence to **Master Coder Protocol (MCP v6.3)** and **FAIR+CARE** standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)
[![Status: Validated](https://img.shields.io/badge/Status-Automated-success)]()

</div>

---

## 📘 Overview

This directory contains validation reports evaluating the **reproducibility, accuracy, and ethical governance** of experimental processes in KFM.  
Each experiment is documented using `docs/templates/experiment.md` and automatically validated via pipelines (`faircare-validate.yml`, `make validate-experiments`).

The reports:
- Verify all experiment parameters and configurations.
- Evaluate output consistency and FAIR+CARE alignment.
- Generate telemetry and governance records for audit traceability.

---

## 🗂️ Directory Layout

```
docs/reports/self-validation/experiments/
├── README.md                     # This file
├── experiment_summary.json        # Aggregated validation results for all experiments
└── results.ndjson                 # Detailed per-experiment validation records
```

---

## 🧾 Report Details

### 1. 📊 `experiment_summary.json`
Summarized results for all experiments validated in the current release.

| Field | Description | Example |
|--------|-------------|----------|
| `experiments_total` | Total number of experiments validated. | `7` |
| `passed` | Count of successfully validated experiments. | `6` |
| `failed` | Count of experiments needing revision. | `1` |
| `avg_runtime_sec` | Mean duration per experiment validation. | `452` |
| `timestamp` | UTC timestamp of validation session. | `"2025-11-05T19:45:00Z"` |

**Example JSON:**
```json
{
  "experiments_total": 7,
  "passed": 6,
  "failed": 1,
  "avg_runtime_sec": 452,
  "timestamp": "2025-11-05T19:45:00Z"
}
```

---

### 2. 🧠 `results.ndjson`
Contains detailed logs for each experiment, including validation parameters, metrics, and governance references.

| Field | Description | Example |
|--------|-------------|----------|
| `experiment_id` | Unique experiment identifier. | `"ocr_ner_1850s"` |
| `ok` | Boolean validation outcome. | `true` |
| `parameters` | Model or process parameters. | `{"epochs": 20, "lr": 0.0005}` |
| `metrics` | Key experimental results or performance metrics. | `{"accuracy": 0.946, "f1_score": 0.940}` |
| `telemetry_ref` | Reference to telemetry JSON. | `"releases/v9.7.0/focus-telemetry.json"` |
| `notes` | Validation commentary or recommended improvements. | `"Reproducible across tested environments."` |

---

## ⚙️ Validation Workflow Integration

**Workflow:** `.github/workflows/faircare-validate.yml` (experiment module)  
**Local Command:** `make validate-experiments`

### Steps:
1. Parse experiment metadata from `docs/experiments/*.md`.  
2. Extract parameters and expected results.  
3. Run verification against logged outputs.  
4. Validate FAIR+CARE compliance (metadata + ethical standards).  
5. Record validation outcome in `results.ndjson`.  
6. Summarize results into `experiment_summary.json`.  
7. Append audit entry to `reports/audit/experiments-ledger.json`.  

---

## 🧮 Governance & Telemetry Integration

| System | Function | Output |
|---------|-----------|---------|
| **Governance Ledger** | Records experiment validation events. | `reports/audit/experiments-ledger.json` |
| **Telemetry Dashboard** | Displays validation outcomes and reproducibility rates. | `docs/reports/telemetry/governance_scorecard.json` |
| **FAIR+CARE Audit** | Confirms ethical compliance of experimental workflows. | `reports/fair/faircare_summary.json` |

**Example Governance Ledger Entry:**
```json
{
  "event": "experiment_validation",
  "experiment_id": "ocr_ner_1850s",
  "status": "pass",
  "timestamp": "2025-11-05T19:50:00Z",
  "telemetry_ref": "releases/v9.7.0/focus-telemetry.json"
}
```

---

## ⚖️ FAIR+CARE Reproducibility Criteria

| Principle | Validation Objective | Implementation |
|------------|----------------------|----------------|
| **Findable** | Experiments uniquely identified with `experiment_id`. | Front-matter & ledger links |
| **Accessible** | Publicly available documentation & metadata. | `docs/experiments/` |
| **Interoperable** | Metadata schema aligns with MCP templates. | `docs/templates/experiment.md` |
| **Reusable** | Full reproducibility from recorded parameters. | `results.ndjson` |
| **CARE** | Ethical review for AI and cultural data experiments. | Governance approval required |

---

## 🧠 Reproducibility Index (RI)

All experiments are assigned a **Reproducibility Index (RI)**, a weighted metric reflecting validation robustness.

| Metric | Description | Weight |
|---------|-------------|--------|
| Code Reuse | Version-controlled and open-sourced code. | 25% |
| Parameter Disclosure | Documented training and configuration parameters. | 20% |
| Validation Consistency | Reproducible outputs across environments. | 35% |
| Governance Compliance | FAIR+CARE and ethical review approved. | 20% |

**Formula:**  
```
RI = (CodeReuse + ParameterDisclosure + ValidationConsistency + GovernanceCompliance)
```

**Telemetry Example:**
```json
{
  "experiment_metrics": {
    "reproducibility_index": 95.8,
    "experiments_validated": 7,
    "compliance_rate": 98.1
  }
}
```

---

## 🧾 Data Retention & Access Policy

| Policy Element | Specification |
|----------------|----------------|
| **Retention Period** | Permanent (per release). |
| **Storage Format** | JSON (summary) / NDJSON (detailed). |
| **Checksum Validation** | SHA-256 recorded in SBOM. |
| **Access** | Public (CC-BY 4.0 license). |
| **Governance Oversight** | FAIR+CARE Council quarterly review. |

---

## 🧩 Example Telemetry Snapshot

Stored in:
```
releases/v9.7.0/focus-telemetry.json
```

```json
{
  "experiment_validation": {
    "version": "v9.7.0",
    "experiments_total": 7,
    "passed": 6,
    "failed": 1,
    "avg_runtime_sec": 452,
    "timestamp": "2025-11-05T20:00:00Z"
  }
}
```

---

## 🧠 Use Cases

| Use Case | Description |
|-----------|-------------|
| **Research Audit** | Validate experimental reproducibility and governance approvals. |
| **Telemetry Analytics** | Track reproducibility rates and runtime metrics. |
| **FAIR+CARE Reporting** | Report experiment-level compliance to governance dashboard. |
| **Data Provenance** | Verify links between experiments and derived datasets. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Created experiment validation report index with telemetry and governance linkage. |
| v9.5.0 | 2025-10-20 | A. Barta | Added Reproducibility Index metrics and FAIR+CARE scoring. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established experiment validation reporting system. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Self-Validation Index](../README.md) · [Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
