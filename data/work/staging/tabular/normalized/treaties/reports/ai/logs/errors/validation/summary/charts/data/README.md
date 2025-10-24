---
title: "📊 Kansas Frontier Matrix — AI Error Validation Chart Data"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/summary/charts/data/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Continuous / Automated"
status: "Active · FAIR+CARE+ISO Certified"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-validation", "@kfm-ai", "@kfm-data"]
approvers: ["@kfm-architecture", "@kfm-governance"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - STAC / DCAT
  - CIDOC CRM / PROV-O / OWL-Time
  - ISO 9001 / 19115 / 27001 / 50001
tags: ["ai","data","charts","validation","errors","csv","metrics","fair","provenance","governance","stac"]
---

<div align="center">

# 📊 Kansas Frontier Matrix — **AI Error Validation Chart Data**
`data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/summary/charts/data/`

**Purpose:** Provide **structured datasets (CSV/JSON)** powering AI error validation charts and dashboards.  
This directory contains **aggregated statistics** and **derived metrics** used for visualizations, FAIR reporting, and governance telemetry.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![Data](https://img.shields.io/badge/Data-Validated%20%26%20Structured-6f42c1)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%201915%20%7C%202701-229954)]()

</div>

---

## 📚 Overview

The **AI Error Validation Chart Data** directory contains **processed metric exports** used to render validation charts and summary visuals.  
All data is:
- Derived from validation summaries (`../summary/*.json`)  
- Checked for **schema and checksum integrity**  
- Structured for use in analytics and FAIR ledger ingestion  

> 📈 *Each dataset must correspond to one or more chart specs under `../specs/` and one visualization under `../images/`.*

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/summary/charts/data/
├── error_trend_2025-10.csv
├── severity_breakdown_2025-10.csv
├── validation_success_rate.csv
├── metadata.json
└── checksums.sha256
```

---

## 🧩 Dataset Schema Overview

| Field | Type | Description |
| :------ | :------ | :----------- |
| `date` | string (YYYY-MM-DD) | Timestamp of record |
| `validations` | integer | Count of validation attempts |
| `errors` | integer | Count of failed validations |
| `critical` | integer | Count of critical errors |
| `major` | integer | Count of major issues |
| `minor` | integer | Count of minor issues |
| `pass_rate_pct` | float | Overall success rate |
| `fair_score_avg` | float | Average FAIR+CARE compliance score |
| `checksum_sha256` | string | Integrity hash of dataset file |

---

## 🧠 Example Datasets

**`error_trend_2025-10.csv`**
```csv
date,validations,errors,critical,major,minor
2025-10-01,218,3,1,1,1
2025-10-08,231,2,0,1,1
2025-10-15,244,2,0,1,1
2025-10-22,260,1,0,0,1
```

**`severity_breakdown_2025-10.csv`**
```csv
severity,count
critical,2
major,5
minor,8
```

**`validation_success_rate.csv`**
```csv
date,pass_rate_pct,fair_score_avg
2025-10-01,98.7,0.95
2025-10-08,99.2,0.96
2025-10-15,99.5,0.97
2025-10-22,99.6,0.97
```

---

## 🧾 Metadata Record Example

```json
{
  "dataset_id": "validation_error_trends_oct2025",
  "created_at": "2025-10-24T13:00:00Z",
  "source": "../summary/validation_summary_2025-10-24.json",
  "checksum_sha256": "9d3a5f28b7c1...",
  "linked_charts": [
    "../images/error_trend_2025-10.png",
    "../specs/error_trend.spec.json"
  ],
  "provenance_ref": "../provenance/error_trend_2025-10_prov.jsonld",
  "governance_ledger_hash": "abc93f7e12f..."
}
```

---

## 🧪 Data Validation Rules

| Rule | Description | Tool | Output |
| :------ | :------------ | :---------- | :---------- |
| Schema Validation | Conform to `chart_data.schema.json` | `jsonschema-cli` | `schema_validation.json` |
| Integrity Check | Verify SHA-256 per file | `sha256sum` | `checksums.sha256` |
| Provenance Linkage | Validate JSON-LD linkage | `pyshacl` | `provenance_validation.jsonld` |
| FAIR+CARE Scoring | Validate metadata completeness | `fair-checker` | `fair_audit.json` |

---

## 📊 Key Metrics

| Metric | Target | Description |
| :------ | :------ | :----------- |
| `checksum_integrity` | 100% | Hash consistency verified |
| `schema_pass_rate` | ≥ 99% | Schema compliance success rate |
| `provenance_link_rate` | 100% | Provenance and ledger linkage |
| `fair_metadata_score` | ≥ 0.9 | FAIR+CARE metadata audit score |

---

## 🔐 Governance & Provenance Integration

| Ledger | Purpose | Artifact |
| :------ | :----------- | :------------ |
| **FAIR Ledger** | Open data catalog entry for validation datasets | `fair_chart_data_manifest.json` |
| **Governance Chain** | Immutable dataset registry | `ledger_data_manifest.json` |
| **Audit Ledger** | Tracks schema and checksum validation results | `data_audit_summary.json` |
| **Ethics Ledger** | Ensures data neutrality and transparency | `ethics_data_audit.json` |

---

## ✅ Compliance Matrix

| Standard | Domain | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | Data ethics and openness | ✅ |
| **MCP-DL v6.4.3** | Documentation and metadata structure | ✅ |
| **CIDOC CRM / PROV-O / OWL-Time** | Provenance and linkage | ✅ |
| **ISO 9001 / 19115 / 27001** | Data quality + security | ✅ |
| **ISO 50001 / 14064** | Energy & sustainability reporting | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Created chart data module with FAIR+CARE and governance ledger integration. | @kfm-validation |

---

<div align="center">

[![Chart Data](https://img.shields.io/badge/Chart%20Data-Validated%20%26%20Structured-6f42c1?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%201915%20%7C%202701-229954?style=flat-square)]()
[![Provenance](https://img.shields.io/badge/Provenance-CIDOC%20CRM%20%7C%20PROV--O-8a2be2?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · Chart Data
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/summary/charts/data/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
ISO-ALIGNED: true
DATA-VALIDATED: true
PROVENANCE-LINKED: true
STAC-COMPLIANT: true
GOVERNANCE-LEDGER-LINKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->