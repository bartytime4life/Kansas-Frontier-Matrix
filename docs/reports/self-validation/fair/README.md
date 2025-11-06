---
title: "⚖️ Kansas Frontier Matrix — FAIR+CARE Validation Reports (Automated Summary)"
path: "docs/reports/self-validation/fair/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/docs-reports-fair-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# ⚖️ **Kansas Frontier Matrix — FAIR+CARE Validation Reports (Automated Summary)**
`docs/reports/self-validation/fair/README.md`

**Purpose:** Summarize and describe automated FAIR (Findable, Accessible, Interoperable, Reusable) and CARE (Collective Benefit, Authority, Responsibility, Ethics) compliance reports for Kansas Frontier Matrix (KFM) datasets.  
These reports are generated continuously to ensure all datasets maintain ethical and open science standards under **Master Coder Protocol (MCP v6.3)**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)
[![Status: Automated](https://img.shields.io/badge/Status-Validated-success)]()

</div>

---

## 📘 Overview

This directory contains **FAIR+CARE validation reports** automatically produced by CI/CD workflows.  
Each report documents dataset metadata completeness, licensing, provenance, and ethical governance results.  
These validations guarantee KFM’s datasets remain fully **reproducible**, **machine-actionable**, and **ethically transparent**.

Validation is performed via the workflow:  
`.github/workflows/faircare-validate.yml`

Reports are linked to:
- `reports/audit/governance-ledger.json` (Governance decisions)
- `docs/reports/telemetry/governance_scorecard.json` (FAIR+CARE metrics)
- `releases/v9.7.0/focus-telemetry.json` (Telemetry dashboard)

---

## 🗂️ Directory Layout

```
docs/reports/self-validation/fair/
├── README.md                     # This file
├── faircare_results.ndjson        # Raw per-dataset FAIR+CARE validation logs
└── faircare_summary.json          # Aggregated compliance summary
```

---

## 🧾 Report Details

### 1. 🧠 `faircare_results.ndjson`
Each line represents an individual dataset audit with FAIR and CARE validation results.

| Field | Description | Example |
|--------|-------------|----------|
| `path` | Dataset manifest path. | `"data/sources/noaa_storms_1950_2025.json"` |
| `ok` | Boolean success flag. | `true` |
| `errors` | Array of failed checks. | `[]` |
| `warnings` | Non-critical improvement notes. | `["License not SPDX standard but equivalent accepted."]` |
| `care_required` | Boolean: dataset triggers cultural or Indigenous review. | `false` |
| `timestamp` | UTC timestamp of validation run. | `"2025-11-05T17:45:00Z"` |

---

### 2. 📊 `faircare_summary.json`
Aggregated results from all dataset validations within a release cycle.

| Field | Description | Example |
|--------|-------------|----------|
| `datasets_validated` | Total datasets reviewed. | `243` |
| `passed` | Datasets passing FAIR+CARE validation. | `238` |
| `failed` | Datasets requiring revision. | `5` |
| `care_reviews` | Datasets flagged for cultural/Indigenous governance. | `4` |
| `timestamp` | UTC timestamp of report generation. | `"2025-11-05T18:00:00Z"` |

**Example JSON:**
```json
{
  "datasets_validated": 243,
  "passed": 238,
  "failed": 5,
  "care_reviews": 4,
  "timestamp": "2025-11-05T18:00:00Z"
}
```

---

## ⚙️ FAIR+CARE Validation Workflow

**Workflow:** `.github/workflows/faircare-validate.yml`

**Pipeline Steps:**
1. Scan all dataset manifests (`data/sources/*.json`).  
2. Validate mandatory FAIR fields: `id`, `title`, `license`, `provenance`, `checksum`, `temporal`, `spatial`.  
3. Check for missing or invalid CARE review metadata.  
4. Generate `faircare_results.ndjson` for detailed logs.  
5. Aggregate `faircare_summary.json` for CI/CD telemetry integration.  
6. Append workflow metadata to Governance Ledger (`reports/audit/github-workflows-ledger.json`).  

---

## 🧮 Governance & Telemetry Integration

| System | Function | Output |
|---------|-----------|---------|
| **Governance Ledger** | Stores council decisions and validation runs. | `reports/audit/governance-ledger.json` |
| **Telemetry Dashboard** | Visualizes compliance and review rates. | `docs/reports/telemetry/governance_scorecard.json` |
| **Release Manifest** | Records provenance and validation linkage. | `releases/v9.7.0/manifest.zip` |

**Governance Example Entry:**
```json
{
  "event": "faircare_validation",
  "datasets_validated": 243,
  "passed": 238,
  "failed": 5,
  "care_reviews": 4,
  "timestamp": "2025-11-05T18:10:00Z",
  "telemetry_ref": "releases/v9.7.0/focus-telemetry.json"
}
```

---

## ⚖️ FAIR+CARE Criteria Summary

| Principle | Validation Requirement | Enforced By |
|------------|------------------------|--------------|
| **F1 — Findable** | Dataset includes `id`, `title`, `spatial`, `temporal` metadata. | FAIR Validator |
| **F2 — Accessible** | License provided and accessible; public metadata link. | FAIR Validator |
| **F3 — Interoperable** | Schema aligns with STAC/DCAT standards. | FAIR Validator |
| **F4 — Reusable** | Provenance, checksum, and license completeness. | FAIR Validator |
| **C1 — Collective Benefit** | Dataset promotes shared public or community value. | CARE Validator |
| **C2 — Authority to Control** | Indigenous or local authority approval where applicable. | CARE Governance |
| **C3 — Responsibility** | Ethical use and community accountability. | CARE Governance |
| **C4 — Ethics** | Respect for data sovereignty and cultural privacy. | CARE Governance |

---

## 🧩 FAIR+CARE Scoring Metrics

**Score Formula:**
```
FAIR+CARE Score = (FAIR * 0.7) + (CARE * 0.3)
```

| Range | Rating | Description |
|--------|---------|-------------|
| 95–100 | ✅ Excellent | Fully compliant with FAIR+CARE and MCP. |
| 80–94 | ⚙️ Strong | Minor metadata or review adjustments needed. |
| 65–79 | ⚠️ Review Required | Governance review pending or incomplete fields. |
| <65 | 🚫 Non-Compliant | Fails FAIR or CARE validation checks. |

**Telemetry JSON Example:**
```json
{
  "faircare_score": 98.3,
  "datasets_validated": 243,
  "care_reviews": 4,
  "timestamp": "2025-11-05T18:10:00Z"
}
```

---

## 🧾 Data Retention Policy

| Policy | Description |
|---------|--------------|
| **Retention Period** | Permanent archival per release. |
| **Storage Format** | NDJSON (raw), JSON (summary). |
| **Checksum Integrity** | SHA-256 validated in SBOM (`sbom.spdx.json`). |
| **Access Control** | Public (CC-BY 4.0 license). |
| **Governance Review** | Quarterly FAIR+CARE Council verification. |

---

## 🧠 Use Cases

| Use Case | Description |
|-----------|-------------|
| **Governance Audit** | Verify ethical compliance for datasets prior to publication. |
| **Data Quality Review** | Identify incomplete or inconsistent metadata. |
| **Telemetry Insights** | Populate compliance dashboards with FAIR+CARE metrics. |
| **Public Transparency** | Demonstrate commitment to open, ethical science. |

---

## 🧮 Example Telemetry Snapshot

```json
{
  "faircare_validation": {
    "version": "v9.7.0",
    "datasets_validated": 243,
    "passed": 238,
    "failed": 5,
    "care_reviews": 4,
    "compliance_rate": 97.9,
    "timestamp": "2025-11-05T18:30:00Z"
  }
}
```

Stored in:
```
releases/v9.7.0/focus-telemetry.json
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Added full FAIR+CARE validation summary documentation and telemetry alignment. |
| v9.5.0 | 2025-10-20 | A. Barta | Introduced detailed scoring and governance linkage. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established FAIR+CARE self-validation reporting. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Validated under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Self-Validation Index](../README.md) · [Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
