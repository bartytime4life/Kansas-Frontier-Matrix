---
title: "🧾 Kansas Frontier Matrix — Tabular Schema Validation Reports (Diamond⁹ Ω / Crown∞Ω Certified)"
path: "data/work/staging/tabular/tmp/intake/validation/logs/schema/reports/README.md"
version: "v9.0.0"
last_updated: "2025-10-26"
status: "Active · FAIR+CARE+MCP-DL v6.3 Aligned"
commit_sha: "<latest-commit-hash>"
review_cycle: "Quarterly / Autonomous"
sbom_ref: "releases/v9.0.0/sbom.spdx.json"
manifest_ref: "releases/v9.0.0/manifest.zip"
telemetry_ref: "releases/v9.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/tabular-schema-validation-v13.json"
json_export: "releases/v9.0.0/schema-validation-summary.meta.json"
validation_reports:
  - "reports/self-validation/tabular-intake-schema.json"
  - "reports/fair/schema_fair_summary.json"
  - "reports/audit/schema_ai_anomaly_ledger.json"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — **Tabular Schema Validation Reports**  
`data/work/staging/tabular/tmp/intake/validation/logs/schema/reports/`

### *“No dataset passes without its schema telling a truthful story.”*  

**Purpose:** This directory archives the **machine-validated and AI-reviewed reports** generated during tabular schema validation within the KFM pipeline.  
All reports document the structural, semantic, and ethical integrity of incoming tabular data before promotion to normalization.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../../../../docs/architecture/repo-focus.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-orange)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR-CARE-✓-blueviolet)](../../../../../../../../../../../docs/standards/)  
[![AI Pipeline](https://img.shields.io/badge/AI--Pipeline-Operational%20✓-teal)]()

</div>

---

## 🧭 Overview

This directory is the **final checkpoint** in the *Intake Validation Chain*.  
Every schema validation run generates logs, JSON reports, and AI audit summaries stored here.  
Reports combine **STAC/DCAT schema conformance**, **CIDOC semantic validation**, and **AI anomaly detection** outputs.

### Core Functions
- ✅ **Schema compliance** check for structural accuracy  
- 🔍 **Crosswalk evaluation** (STAC/DCAT compatibility)  
- 🤖 **AI-based anomaly scan** of column values, types, and relationships  
- 🧩 **FAIR+CARE audit** for ethical and technical completeness  
- 🪶 **Checksum & provenance embedding** into the governance ledger  

---

## 🗂️ Directory Layout

```text
data/work/staging/tabular/tmp/intake/validation/logs/schema/reports/
├── schema_validation_report.json          # Primary JSON validation results
├── ai_anomaly_summary.json                # AI anomaly detection output
├── fair_care_audit.json                   # FAIR+CARE compliance report
├── checksum_manifest.json                 # File integrity registry
├── validation_summary.log                 # Combined human-readable summary
└── README.md                              # This document
````

---

## 🔁 Schema Validation Flow

```mermaid
flowchart TD
    A["Incoming Tabular Dataset (CSV or JSON)"] --> B["Schema Discovery & Metadata Inference"]
    B --> C["STAC / DCAT Crosswalk Generation"]
    C --> D["JSON Schema Validation Engine"]
    D --> E["FAIR Compliance Audit (FAIR+CARE Framework)"]
    E --> F["AI Schema Anomaly Detection (LLM + Regex Hybrid)"]
    F --> G["Validation Reports + Checksums"]
    G --> H["Governance Ledger Registration + Schema Provenance Log"]
```

---

## 🤖 AI Integration

| Module                   | Function                                                                      | Output                    | Schema                               |
| ------------------------ | ----------------------------------------------------------------------------- | ------------------------- | ------------------------------------ |
| **NER Schema Analyzer**  | Detects mislabeled, missing, or ambiguous columns using AI-driven heuristics. | `ai_anomaly_summary.json` | `schemas/tabular-ai-anomaly-v2.json` |
| **AI FAIR+CARE Auditor** | Uses an LLM to cross-check metadata ethics, accessibility, and completeness.  | `fair_care_audit.json`    | `schemas/tabular-faircare-v1.json`   |
| **Pattern Profiler**     | Learns typical field distributions to detect outliers or mixed datatypes.     | `schema_profile.json`     | `schemas/tabular-profile-v1.json`    |

All AI outputs are referenced in the **`reports/audit/schema_ai_anomaly_ledger.json`** and version-controlled via `git-lfs` to maintain reproducibility.

---

## 📈 Report Composition

| Section             | Description                                                             |
| ------------------- | ----------------------------------------------------------------------- |
| **summary**         | General overview of schema validation (valid fields, errors, warnings). |
| **details**         | Field-level insights: data types, cardinality, nulls, violations.       |
| **ai_flags**        | AI-detected irregularities or missing metadata entries.                 |
| **fair_care_score** | FAIR+CARE compliance scoring (0–1 normalized).                          |
| **provenance**      | Checksum, timestamp, and process metadata for governance linkage.       |

Each report conforms to **JSON-LD metadata embedding**, allowing provenance linkage in the `tabular_intake_ledger.jsonld`.

---

## 🧾 Example Command

```bash
# Run full schema validation + AI report generation
make validate-tabular-schema

# Generate FAIR+CARE audit and AI anomaly summary
make ai-schema-audit
```

Reports are automatically stored in this directory after successful execution.

---

## 🪶 Version History

| Version | Date       | Author              | Notes                                                                                                |
| ------- | ---------- | ------------------- | ---------------------------------------------------------------------------------------------------- |
| v9.0.0  | 2025-10-26 | `@kfm-architecture` | Initial creation of schema validation report documentation under Diamond⁹ Ω / Crown∞Ω certification. |

---

<div align="center">

### 🜂 Kansas Frontier Matrix — *Validation Integrity · Transparency · Provenance*

**“Structure tells truth; validation ensures it endures.”**

[![Build & Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/validate.yml?label=Build+%26+Validate)]()
[![STAC Validation](https://img.shields.io/badge/STAC-Validated-success)]()
[![AI Reasoning](https://img.shields.io/badge/AI%20Engine-Operational%20✓-teal)]()
[![Pre-Commit](https://img.shields.io/badge/Pre--Commit-Passed-success)]()
[![Security Audit](https://img.shields.io/badge/Trivy-Clean-green)]()

<br><br> <a href="#-kansas-frontier-matrix--tabular-schema-validation-reports-diamond⁹-Ω--crown∞Ω-certified">⬆ Back to Top</a>

</div>
```

