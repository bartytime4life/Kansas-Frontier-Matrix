---
title: "🧪 Kansas Frontier Matrix — Experiment Reproducibility Validation Reports"
path: "docs/self-validation/experiments/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/docs-experiments-validation-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Experiment Reproducibility Validation Reports**
`docs/self-validation/experiments/README.md`

**Purpose:** Index and describe experiment reproducibility and validation reports generated for all scientific, data, or AI experiments conducted within the Kansas Frontier Matrix (KFM).  
These reports document compliance with **Master Coder Protocol (MCP v6.3)** and **FAIR+CARE** reproducibility standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare.md)
[![Status: Automated](https://img.shields.io/badge/Status-Automated-success)]()

</div>

---

## 📘 Overview

The `experiments/` directory houses validation reports verifying that all experiments conducted in the Kansas Frontier Matrix are **reproducible**, **traceable**, and **governance-audited**.  
Each report includes:
- Experimental parameters and inputs
- Validation results and performance metrics
- FAIR+CARE reproducibility scores
- Cross-references to telemetry and governance ledgers

Generated automatically during `make validate-experiments` or CI/CD pipeline execution, these files ensure full transparency of all experimental outcomes documented via `docs/templates/experiment.md`.

---

## 🗂️ Directory Layout

```
docs/self-validation/experiments/
├── README.md                    # This file
├── experiment_summary.json       # Summary of validated experiments and outcomes
└── results.ndjson                # Detailed per-experiment validation logs
```

---

## 🧾 Report Details

### 1. 🧠 `experiment_summary.json`
Aggregated validation results for all documented experiments.

| Field | Description |
|--------|-------------|
| `experiments_total` | Number of experiment documents validated. |
| `passed` | Count of experiments meeting reproducibility criteria. |
| `failed` | Count of experiments requiring revision or additional data. |
| `avg_runtime_sec` | Average runtime for experiment validation. |
| `timestamp` | UTC timestamp of validation session. |

**Example:**
```json
{
  "experiments_total": 7,
  "passed": 6,
  "failed": 1,
  "avg_runtime_sec": 452,
  "timestamp": "2025-11-05T19:30:00Z"
}
```

---

### 2. 📋 `results.ndjson`
Detailed log file capturing validation results for each experiment run.

| Field | Description |
|--------|-------------|
| `experiment_id` | Unique identifier (from YAML front-matter of experiment doc). |
| `ok` | Boolean: true if experiment reproduced successfully. |
| `parameters` | Experiment configuration (learning rate, epochs, etc.). |
| `metrics` | Validation metrics (accuracy, F1 score, etc.). |
| `telemetry_ref` | Link to associated telemetry snapshot. |
| `notes` | Context or improvement recommendations. |

**Example Entry:**
```json
{
  "experiment_id": "ocr_ner_1850s",
  "ok": true,
  "parameters": {
    "epochs": 20,
    "learning_rate": 0.0005,
    "batch_size": 32
  },
  "metrics": {
    "accuracy": 0.946,
    "f1_score": 0.940
  },
  "telemetry_ref": "releases/v9.7.0/focus-telemetry.json",
  "notes": "Reproducible across different compute environments."
}
```

---

## ⚙️ Validation Workflow

**Workflow:** `.github/workflows/faircare-validate.yml` (via experiment submodule)  
**Local Command:** `make validate-experiments`

**Process:**
1. Scan `docs/experiments/*.md` for experiment files.  
2. Parse YAML front-matter and extract parameters.  
3. Validate experiment runtime reproducibility using logs and metadata.  
4. Record outcomes into `results.ndjson`.  
5. Summarize in `experiment_summary.json`.  
6. Append validation results to `reports/audit/experiments-ledger.json`.  
7. Update telemetry metrics in `releases/v9.7.0/focus-telemetry.json`.

---

## 🧮 Governance & Telemetry Integration

All experiment validations are cross-linked to governance and telemetry systems for oversight.

| Record | Description | Path |
|---------|-------------|------|
| **Governance Ledger** | Experiment audit trail | `reports/audit/experiments-ledger.json` |
| **Telemetry Dashboard** | Experiment performance visualization | `docs/reports/telemetry/build_metrics.json` |
| **AI Models Ledger** | Link for experiments involving AI models | `reports/audit/ai_models.json` |

**Governance Ledger Example:**
```json
{
  "event": "experiment_validation",
  "experiment_id": "ocr_ner_1850s",
  "status": "pass",
  "timestamp": "2025-11-05T19:35:00Z",
  "telemetry_ref": "releases/v9.7.0/focus-telemetry.json"
}
```

---

## 🧩 FAIR+CARE Reproducibility Criteria

| Principle | Validation Target |
|------------|-------------------|
| **Findable** | Experiment documentation includes `id`, `title`, `version`, and source path. |
| **Accessible** | Results stored under open license and public GitHub directory. |
| **Interoperable** | Metadata aligns with MCP schema and FAIR+CARE JSON structures. |
| **Reusable** | Fully reproducible workflows with parameter transparency. |
| **CARE** | Ethical compliance confirmed for datasets or AI models used. |

---

## 🧠 Reproducibility Score Metrics

KFM assigns a **Reproducibility Index (RI)** to each experiment based on validation outcomes.

| Metric | Description | Weight |
|---------|-------------|--------|
| **Code Reuse** | Source scripts are versioned and accessible. | 25% |
| **Parameter Disclosure** | All experiment parameters documented. | 20% |
| **Validation Success** | Consistent reproduction of metrics. | 35% |
| **Governance Compliance** | Approved FAIR+CARE audit. | 20% |

**Formula:**
```
RI = (CodeReuse + ParameterDisclosure + ValidationSuccess + GovernanceCompliance)
```

**Example:**
> Experiment `ocr_ner_1850s` scored RI = 95.8 (Excellent)

---

## 🧾 Data Retention & Access Policy

| Policy Element | Specification |
|----------------|----------------|
| **Retention Period** | Permanent archival for all releases. |
| **Format** | NDJSON + JSON summary. |
| **Checksum Validation** | SHA-256 checksum recorded in release manifest. |
| **Access** | Public (CC-BY 4.0) under `/docs/self-validation/experiments/`. |
| **Governance Review** | Quarterly by FAIR+CARE Council. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Added detailed experiment validation index and governance linkage. |
| v9.5.0 | 2025-10-20 | A. Barta | Introduced Reproducibility Index and telemetry metrics. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Created baseline experiment validation documentation. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Self-Validation Index](../README.md) · [Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
