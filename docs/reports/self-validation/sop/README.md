---
title: "🧾 Kansas Frontier Matrix — SOP Validation & Governance Reports"
path: "docs/reports/self-validation/sop/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/docs-reports-sop-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — SOP Validation & Governance Reports**
`docs/reports/self-validation/sop/README.md`

**Purpose:** Provide summaries of automated Standard Operating Procedure (SOP) validation reports and governance records.  
These reports verify that all KFM procedural documents comply with **Master Coder Protocol (MCP v6.3)**, **FAIR+CARE** documentation standards, and governance oversight requirements.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)
[![Status: Validated](https://img.shields.io/badge/Status-Automated-success)]()

</div>

---

## 📘 Overview

This directory documents all validation reports related to **Standard Operating Procedures (SOPs)** used across KFM’s pipelines, AI systems, and data workflows.  
Each validation confirms that:
- SOPs are written in MCP-compliant Markdown.  
- YAML front-matter metadata is present and schema-valid.  
- FAIR+CARE governance criteria are met.  
- Documents are reviewed by the FAIR+CARE Council and referenced in telemetry logs.

SOP validations are automatically performed through:
- `.github/workflows/docs-lint.yml`  
- `.github/workflows/faircare-validate.yml`

---

## 🗂️ Directory Layout

```
docs/reports/self-validation/sop/
├── README.md                     # This index file
├── sop_validation_summary.json    # Summary of all SOP validation outcomes
└── sop_results.ndjson             # Detailed validation logs for individual SOPs
```

---

## 🧾 Report Details

### 1. 📊 `sop_validation_summary.json`
Aggregated report summarizing validation outcomes across all SOP documents.

| Field | Description | Example |
|--------|-------------|----------|
| `sop_total` | Number of SOPs validated. | `12` |
| `passed` | Number of SOPs that passed validation. | `12` |
| `failed` | SOPs with validation errors or missing metadata. | `0` |
| `rules_tested` | Total linting and FAIR+CARE validation rules applied. | `18` |
| `timestamp` | UTC timestamp of validation session. | `"2025-11-05T20:30:00Z"` |

**Example JSON:**
```json
{
  "sop_total": 12,
  "passed": 12,
  "failed": 0,
  "rules_tested": 18,
  "timestamp": "2025-11-05T20:30:00Z"
}
```

---

### 2. 🧮 `sop_results.ndjson`
Line-separated validation logs describing compliance for each SOP file.

| Field | Description | Example |
|--------|-------------|----------|
| `path` | File path to the SOP. | `"docs/sop/data_ingestion_procedure.md"` |
| `ok` | Validation result. | `true` |
| `errors` | Array of failed validation checks. | `[]` |
| `warnings` | Minor issues or non-critical notes. | `["Missing optional telemetry_ref field"]` |
| `governance_reviewed` | Indicates if reviewed by FAIR+CARE Council. | `true` |
| `timestamp` | UTC timestamp. | `"2025-11-05T20:31:00Z"` |

**Example:**
```json
{
  "path": "docs/sop/faircare_validation_procedure.md",
  "ok": true,
  "errors": [],
  "warnings": ["Missing optional telemetry_ref field"],
  "governance_reviewed": true,
  "timestamp": "2025-11-05T20:31:00Z"
}
```

---

## ⚙️ Validation Workflow Integration

| Workflow | Function | Output |
|-----------|-----------|---------|
| **`docs-lint.yml`** | Ensures proper structure, formatting, and front-matter compliance. | `sop_results.ndjson` |
| **`faircare-validate.yml`** | Validates FAIR+CARE governance fields and ethical compliance. | `sop_validation_summary.json` |
| **`telemetry-export.yml`** | Integrates validation results with dashboards and governance scorecards. | `releases/v9.7.0/focus-telemetry.json` |

---

## 🧩 Governance & Telemetry Integration

Each SOP validation event is cross-referenced within:
- **Governance Ledger:** `reports/audit/github-workflows-ledger.json`  
- **FAIR+CARE Ledger:** `reports/audit/governance-ledger.json`  
- **Telemetry Dashboard:** `docs/reports/telemetry/governance_scorecard.json`

**Example Ledger Entry:**
```json
{
  "event": "sop_validation",
  "validated_files": 12,
  "failed": 0,
  "workflow": "docs-lint.yml",
  "timestamp": "2025-11-05T20:35:00Z",
  "telemetry_ref": "releases/v9.7.0/focus-telemetry.json"
}
```

---

## ⚖️ FAIR+CARE SOP Compliance

| Principle | SOP Requirement | Implementation |
|------------|-----------------|----------------|
| **Findable** | SOPs versioned and indexed under `docs/sop/`. | YAML front-matter metadata. |
| **Accessible** | Documents open-access under CC-BY 4.0 license. | Public GitHub repository. |
| **Interoperable** | SOP metadata compatible with FAIR schema. | MCP + JSON validation. |
| **Reusable** | SOPs include reproducible procedural steps. | Standardized `sop.md` template. |
| **CARE** | Reviewed by FAIR+CARE Council for ethical oversight. | CARE validation flag in metadata. |

---

## 🧠 Common Validation Rules

| Rule | Description |
|------|-------------|
| `MD041` | First line must be an H1 title with emoji. |
| `MD025` | Only one top-level heading per file. |
| `YAML_SCHEMA_MISSING_FIELD` | Required front-matter key missing. |
| `MCP_HEADER_VALIDATION` | Front-matter fails MCP v6.3 format. |
| `CARE_REVIEW_FLAG` | Missing `governance_reviewed` field or CARE block. |
| `LINK_CHECK_FAILURE` | Invalid or broken internal link reference. |

---

## 🧾 Data Retention & Access Policy

| Policy Item | Specification |
|--------------|---------------|
| **Retention Period** | Permanent per release cycle. |
| **Format** | JSON / NDJSON (UTF-8 encoded). |
| **Checksum Validation** | Recorded in `sbom.spdx.json`. |
| **Access** | Public under CC-BY 4.0. |
| **Governance Oversight** | FAIR+CARE Council quarterly review. |

---

## 🧮 Example Telemetry Snapshot

Stored in:  
`releases/v9.7.0/focus-telemetry.json`

```json
{
  "sop_validation": {
    "version": "v9.7.0",
    "validated": 12,
    "passed": 12,
    "failed": 0,
    "timestamp": "2025-11-05T20:35:00Z"
  }
}
```

---

## 🧩 Use Cases

| Use Case | Description |
|-----------|-------------|
| **Operational Governance** | Ensure all procedures follow reproducible documentation standards. |
| **Audit Readiness** | Validate that SOPs include required metadata and review approvals. |
| **Telemetry Analytics** | Populate dashboard metrics for procedural compliance. |
| **FAIR+CARE Certification** | Demonstrate ethical and transparent workflow management. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Added comprehensive SOP validation summary with governance and telemetry mapping. |
| v9.5.0 | 2025-10-20 | A. Barta | Expanded FAIR+CARE criteria and rule checks. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established SOP validation documentation standard. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Self-Validation Index](../README.md) · [Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
