---
title: "✅ Kansas Frontier Matrix — Data Validation Reports (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/reports/validation/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-reports-validation-v10.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# ✅ Kansas Frontier Matrix — **Data Validation Reports**
`data/reports/validation/README.md`

**Purpose:**  
Central repository for **schema conformance, STAC validation, and ETL quality assurance** reports generated during the KFM data lifecycle.  
Ensures reproducibility, transparency, and **FAIR+CARE** compliance for all validated datasets, with **telemetry v2** bindings.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/architecture/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Verified](https://img.shields.io/badge/FAIR%2BCARE-Verified-gold.svg)](../../../docs/standards/faircare-validation.md)
[![STAC Validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)

</div>

---

## 📘 Overview
`data/reports/validation/` stores all **validation artifacts** created during ingestion, ETL transformation, and governance review.  
These reports verify that each dataset adheres to metadata schemas, spatial standards, and **FAIR+CARE** requirements.

**v10 Enhancements**
- Telemetry v2 fields (energy/CO₂, coverage) embedded in validation outputs.  
- Streaming STAC aware checks for continuously updated catalogs.  
- Unified error taxonomy for Focus Mode v2 dashboards.

Each report provides:
- Structural & semantic validation (GeoJSON, GeoTIFF, CSV).  
- **STAC 1.0 / DCAT 3.0** schema verification.  
- Error, warning, and success logs from automated validators.  
- Cross-checks between dataset metadata and governance manifests.

---

## 🗂️ Directory Layout
```plaintext
data/reports/validation/
├── README.md
├── stac_validation_report.json        # STAC compliance report (all datasets)
├── schema_validation_summary.json     # Schema validation summary (GeoJSON/CSV/etc.)
├── geojson_schema_validation.log      # GDAL/ogrinfo geometry + CRS logs
├── ai_validation_metrics.csv          # AI dataset validation metrics (accuracy/drift)
└── validation_summary.md              # Human-friendly overview of outcomes
```

---

## ⚙️ Validation Workflow
```mermaid
flowchart TD
    "ETL Data Processing Completed" --> "STAC Validation (Schema & Metadata)"
    "STAC Validation (Schema & Metadata)" --> "Schema Validation (GeoJSON · CSV · GeoTIFF)"
    "Schema Validation (GeoJSON · CSV · GeoTIFF)" --> "AI & Derived Data Validation"
    "AI & Derived Data Validation" --> "FAIR+CARE Cross-Validation"
    "FAIR+CARE Cross-Validation" --> "Report Generation & Governance Review"
```

### Steps
1. **STAC Validation** — Checks required fields, valid geometries, and metadata structure.  
2. **Schema Validation** — Verifies attributes, CRS consistency, and schema conformance.  
3. **AI Validation** — Assesses drift, bias, and accuracy for derived models.  
4. **FAIR+CARE Validation** — Cross-links ethics standards prior to publishing.  
5. **Governance Review** — Council audit + archival in provenance ledgers.

---

## 🧩 Validation Tools & Standards
| Tool / Standard    | Purpose                                       | Output                             |
|---|---|---|
| **stac-validator** | STAC 1.0 conformance                           | `stac_validation_report.json`      |
| **jsonschema**     | JSON metadata & schema validation              | `schema_validation_summary.json`   |
| **GDAL / ogrinfo** | Geometry validity & CRS checks                  | `geojson_schema_validation.log`    |
| **AI Drift Monitor** | Data/model drift + bias checks               | `ai_validation_metrics.csv`        |

---

## 🔍 Example — STAC Validation Report
```json
{
  "dataset": "hazards_v10.0.0",
  "status": "passed",
  "validator_version": "1.1.0",
  "errors": [],
  "warnings": ["Recommended field 'keywords' missing"],
  "metadata_completeness": 0.98,
  "linked_items": [
    "data/stac/items/hazards_v10.0.0.json",
    "data/reports/audit/data_provenance_ledger.json"
  ],
  "telemetry": {
    "energy_wh": 0.7,
    "co2_g": 1.0
  }
}
```

> ✅ Each report references the dataset’s provenance record and manifest for traceability.

---

## 🧠 FAIR+CARE Validation Criteria
| Validation Type  | FAIR Principle | CARE Principle        | Description                                  |
|---|---|---|---|
| Metadata Schema  | Findable       | Responsibility        | Ensures complete, searchable metadata.       |
| File Format      | Accessible     | Collective Benefit    | Verifies open, non-proprietary formats.      |
| CRS / Geometry   | Interoperable  | Authority to Control  | Checks coordinate system & feature validity. |
| Provenance Chain | Reusable       | Ethics                | Links derived data to verified origins.      |

Results are aggregated into the **FAIR+CARE dashboard**:  
`data/reports/fair/faircare_scorecard.csv`

---

## 🧾 Validation Metrics Example (AI)
```csv
dataset_id,accuracy,f1_score,drift_index,validation_status
hazards_v10.0.0,0.93,0.92,0.02,passed
climate_v10.0.0,0.90,0.88,0.04,passed
treaties_v10.0.0,0.99,0.99,0.00,passed
```

Metrics are appended to the **AI governance ledger**:  
`data/reports/audit/ai_hazards_ledger.json`

---

## 🔗 Governance Integration
Validation outputs feed into:
- `data/reports/audit/data_provenance_ledger.json` — Governance approvals & signatures.  
- `data/reports/fair/data_fair_summary.json` — FAIR scoring aggregation.  
- `releases/v10.0.0/manifest.zip` — Release-packaged validation summaries.  
- `.github/workflows/stac-validate.yml` — Automated validation workflow.

---

## 🧩 Cross-Linkages
| Linked Component               | Purpose                                     |
|---|---|---|
| `data/stac/`                   | Primary dataset metadata for validation     |
| `data/work/processed/`         | Staging source for datasets under review    |
| `docs/standards/governance/`   | Validation protocols and standards          |
| `schemas/telemetry/work-data-governance-v14.json` | Telemetry schema for validation metadata |
| `reports/fair/`                | FAIR+CARE aggregation & ethics reports      |

---

## 🕰️ Version History
| Version | Date       | Author            | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-09 | `@kfm-validation` | Upgraded to v10: telemetry v2 bindings, Streaming STAC awareness, unified error taxonomy, expanded examples & linkages. |
| v9.7.0  | 2025-11-06 | `@kfm-validation` | Telemetry/schema refs added; examples & linkage updated; badges aligned. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Validation × Transparency × Ethical Data Governance*  
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Reports Index](../README.md) · [Docs Portal](../../../docs/) · [Governance Charter](../../../docs/standards/governance/)
</div>