---
title: "📊 Kansas Frontier Matrix — Processed Tabular Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/tabular/README.md"
version: "v9.6.0"
last_updated: "2025-11-03"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.6.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.6.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.6.0/focus-telemetry.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "CC-BY 4.0 / FAIR+CARE Certified"
---

<div align="center">

# 📊 Kansas Frontier Matrix — **Processed Tabular Data**
`data/processed/tabular/README.md`

**Purpose:**  
Official repository for **FAIR+CARE-certified tabular datasets** processed from census, treaty, economic, and archival data.  
This layer consolidates normalized, validated, and governance-aligned structured data used across the Kansas Frontier Matrix (KFM) platform.

[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Tabular%20Certified-gold)](../../../docs/standards/faircare-validation.md)
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Aligned-green)]()
[![DCAT 3.0](https://img.shields.io/badge/DCAT-3.0%20Compliant-blue)]()
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-brightgreen)](../../../LICENSE)

</div>

---

## 📚 Overview

The **Processed Tabular Layer** contains **finalized, schema-aligned datasets** that have passed FAIR+CARE governance validation and checksum verification.  
Each dataset in this repository has completed full lineage registration, ethical compliance, and reproducibility certification.

### Core Objectives
- Maintain canonical tabular datasets for research and open publication.  
- Enforce schema validation and FAIR+CARE ethical certification.  
- Integrate tabular data into metadata catalogs (DCAT / STAC).  
- Support AI-assisted tabular reasoning and Focus Mode analytical models.  

---

## 🗂️ Directory Layout

```plaintext
data/processed/tabular/
├── README.md                               # This file — overview of processed tabular datasets
│
├── treaties_aggregated_v9.6.0.csv          # Historical treaty data (normalized and validated)
├── economic_indicators_kansas_2025.csv     # Kansas economic indicator summary table
├── census_population_1900_2020.csv         # U.S. Census data for Kansas (population by county)
├── environmental_statistics.parquet        # Environmental summary and derived statistics
├── metadata.json                           # Provenance, checksum, and FAIR+CARE certification metadata
└── dcat_dataset.json                       # DCAT 3.0-compliant dataset catalog record
```

---

## 🧭 Data Summary

| Dataset | Records | Source | Schema | Status | License |
|----------|----------|---------|---------|----------|----------|
| Treaty Data (Aggregated) | 9,120 | NARA / Kansas Historical Society | `treaty_metadata_v3.0.2` | ✅ Certified | CC-BY 4.0 |
| Economic Indicators | 3,750 | BEA / Kansas Dept. of Commerce | `economic_indicators_v3.0.0` | ✅ Certified | CC-BY 4.0 |
| Census Population | 21,125 | U.S. Census Bureau | `census_population_v3.0.1` | ✅ Certified | CC-BY 4.0 |
| Environmental Statistics | 8,450 | EPA / KDHE | `environmental_stats_v3.0.3` | ✅ Certified | CC-BY 4.0 |

---

## 🧩 Example Processed Metadata Record

```json
{
  "id": "processed_tabular_treaties_v9.6.0",
  "source_stage": "data/work/staging/tabular/",
  "records_total": 9120,
  "schema_version": "v3.0.2",
  "fairstatus": "certified",
  "checksum": "sha256:c4d8b3a6e7a2d9c1b4e3f7a8d6c9e1f3b2a4f7d8c9e3b7a1f5c4e9b6d2f7c8a9",
  "validator": "@kfm-tabular-lab",
  "license": "CC-BY 4.0",
  "created": "2025-11-03T22:10:00Z",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Certification Matrix

| Principle | Implementation | Oversight |
|------------|----------------|------------|
| **Findable** | Indexed in DCAT 3.0 metadata catalogs. | @kfm-data |
| **Accessible** | Available in open CSV and Parquet formats. | @kfm-accessibility |
| **Interoperable** | Schema aligned with JSON Schema and FAIR+CARE contracts. | @kfm-architecture |
| **Reusable** | Metadata includes lineage, checksum, and schema documentation. | @kfm-design |
| **Collective Benefit** | Enables public understanding of Kansas history and economy. | @faircare-council |
| **Authority to Control** | FAIR+CARE Council verifies all dataset ethics audits. | @kfm-governance |
| **Responsibility** | Tabular maintainers perform QA and schema compliance checks. | @kfm-security |
| **Ethics** | Personally identifiable data redacted or anonymized. | @kfm-ethics |

All certification reports and FAIR+CARE validations logged in:  
`data/reports/audit/data_provenance_ledger.json` and `data/reports/fair/data_care_assessment.json`

---

## ⚙️ Validation & Governance Workflow

| Step | Description | Output |
|------|--------------|---------|
| **Schema Validation** | Validates dataset structure using JSON schemas. | `schema_validation_summary.json` |
| **Checksum Verification** | Confirms dataset integrity and lineage tracking. | `checksums.json` |
| **FAIR+CARE Ethics Certification** | Reviews ethics, accessibility, and attribution compliance. | `faircare_certification_report.json` |
| **Governance Ledger Registration** | Records provenance, schema version, and certification results. | `data_provenance_ledger.json` |
| **Catalog Registration** | Adds datasets to DCAT and STAC repositories. | `dcat_dataset.json` |

Governance tasks automated via `tabular_processed_sync.yml`.

---

## 📊 Example Checksum Record

```json
{
  "file": "economic_indicators_kansas_2025.csv",
  "checksum_sha256": "sha256:9b2f6c8e7a3d1f5b4e9c7d3a2f8b6e1a5d9c3b8e4a2d7c1f9b4a6c5e3d7f8b9a",
  "validated": true,
  "verified_on": "2025-11-03T22:15:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Retention & Provenance Policy

| Data Type | Retention Duration | Policy |
|------------|--------------------|--------|
| Processed Tabular Data | Permanent | Retained as canonical FAIR+CARE open data. |
| FAIR+CARE Reports | Permanent | Archived for reproducibility and certification review. |
| Metadata | Permanent | Maintained for transparency and audit traceability. |
| Checksum Records | Permanent | Stored under governance manifest. |
| Logs | 365 Days | Rotated under FAIR+CARE compliance retention policy. |

Retention governed by `processed_tabular_retention.yml`.

---

## 🌱 Sustainability Metrics

| Metric | Value | Verified By |
|---------|--------|--------------|
| Energy Use (per certification cycle) | 10.6 Wh | @kfm-sustainability |
| Carbon Output | 15.4 gCO₂e | @kfm-security |
| Renewable Power | 100% (RE100 Verified) | @kfm-infrastructure |
| FAIR+CARE Certification | 100% | @faircare-council |

Telemetry data recorded in:  
`releases/v9.6.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Processed Tabular Data (v9.6.0).
Final FAIR+CARE-certified tabular datasets including census, treaty, and economic indicators.
Checksum-verified and schema-aligned under governance-certified open data workflows.
```

---

## 🧾 Version Notes

| Version | Date | Notes |
|----------|------|--------|
| v9.6.0 | 2025-11-03 | Added DCAT catalog integration and checksum manifest automation. |
| v9.5.0 | 2025-11-02 | Introduced expanded schema validation and FAIR+CARE certification. |
| v9.3.2 | 2025-10-28 | Established processed tabular directory under FAIR+CARE governance. |

---

<div align="center">

**Kansas Frontier Matrix** · *Structured Intelligence × FAIR+CARE Governance × Provenance Transparency*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../../docs/) • [⚖️ Governance Ledger](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>
