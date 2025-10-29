---
title: "🌦️ Kansas Frontier Matrix — Climate Dataset v9.2.0 (FAIR+CARE Legacy Certified)"
path: "data/archive/climate/climate_v9.2.0/README.md"
version: "v9.2.0"
last_updated: "2024-08-01"
review_cycle: "Quarterly / Historical"
commit_sha: "<legacy-commit-hash>"
sbom_ref: "../../../../releases/v9.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.2.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
ontology_alignment: "../../../../ontologies/CIDOC_CRM-ClimateExt.owl"
---

<div align="center">

# 🌦️ Kansas Frontier Matrix — **Climate Dataset v9.2.0**
`data/archive/climate/climate_v9.2.0/README.md`

**Purpose:** Archived version of Kansas Frontier Matrix’s integrated climate dataset, combining NOAA and NCEI historical data for the 1900–2024 period.  
FAIR+CARE-certified for reproducibility, transparency, and responsible open data stewardship.

[![STAC Validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Legacy%20Certified-gold)](../../../../docs/standards/faircare-validation.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

**Climate Dataset v9.2.0** provides an integrated view of temperature, precipitation, and drought indices for Kansas through 2024.  
It serves as the immediate predecessor to version **v9.3.2**, providing validated historical context and supporting Focus Mode model training.

Key Notes:
- Aggregated NOAA/NCEI/NIDIS data harmonized by the KFM ETL pipelines.  
- FAIR+CARE validated for accessibility, metadata completeness, and ethical compliance.  
- Schema-aligned with STAC 1.0 and DCAT 3.0 standards.  
- Focuses on baseline climatology metrics preceding anomaly integration in v9.3.2.  

---

## 🗂️ Directory Layout

```plaintext
data/archive/climate/climate_v9.2.0/
├── README.md                         # This file — overview of dataset v9.2.0
│
├── climate_indices_2024.geojson      # Annual drought and climate index layers
├── climate_summary_2024.geojson      # Annual temperature and precipitation summary
├── metadata.json                     # Dataset-level metadata (STAC-compliant)
├── validation_report.json            # Schema and FAIR+CARE validation summary
├── provenance_record.json            # Provenance, lineage, and governance details
└── checksums.sha256                  # Integrity verification file
```

---

## ⚙️ Dataset Composition

| Layer | Description | Source | Format |
|--------|--------------|--------|--------|
| `climate_indices_2024.geojson` | Palmer Drought Severity Index (PDSI) and SPI composites for 2024. | NOAA NIDIS | GeoJSON |
| `climate_summary_2024.geojson` | Temperature and precipitation summary by county. | NOAA NCEI | GeoJSON |

Spatial Reference: **EPSG:4326 (WGS84)**  
Temporal Coverage: **1900–2024**

---

## 🧩 Metadata Summary

```json
{
  "id": "climate_v9.2.0",
  "title": "Kansas Climate Dataset (v9.2.0)",
  "description": "Historical temperature, precipitation, and drought data compiled from NOAA and NCEI sources for Kansas, 1900–2024.",
  "version": "v9.2.0",
  "created": "2024-08-01T10:30:00Z",
  "license": "CC-BY 4.0",
  "providers": [
    {"name": "NOAA NCEI", "role": "data-source"},
    {"name": "NIDIS", "role": "data-source"}
  ],
  "extent": {
    "spatial": {"bbox": [-102.05, 36.99, -94.61, 40.00]},
    "temporal": {"interval": ["1900-01-01T00:00:00Z", "2024-12-31T00:00:00Z"]}
  }
}
```

---

## 🧠 FAIR+CARE Validation Summary

| Validation Type | Status | Reference |
|------------------|---------|------------|
| STAC Schema Validation | ✅ Passed | `validation_report.json` |
| FAIR Metadata Assessment | ✅ Passed | `data/reports/fair/data_fair_summary.json` |
| CARE Ethical Review | ✅ Approved | `data/reports/fair/data_care_assessment.json` |
| Governance Review | ✅ Signed | `data/reports/audit/data_provenance_ledger.json` |

---

## 🔍 Provenance Record (Excerpt)

```json
{
  "dataset_id": "climate_v9.2.0",
  "compiled_by": "@kfm-etl-ops",
  "validated_by": "@kfm-data-lab",
  "checksum": "dbcf0f8b9b7eaf09a844e35edb4dcfba43918c8f...",
  "archived_on": "2024-08-01T15:00:00Z",
  "governance_status": "approved",
  "etl_pipeline": "src/pipelines/etl/climate/climate_merge_pipeline.py",
  "validation_report": "data/reports/validation/stac_validation_report.json"
}
```

---

## ⚙️ Governance & Integrity Verification

All components of **v9.2.0** were validated and recorded under:
- `data/reports/audit/data_provenance_ledger.json` — Provenance ledger entry.  
- `data/reports/fair/data_fair_summary.json` — FAIR metadata score (97/100).  
- `data/reports/validation/stac_validation_report.json` — STAC validation record.  
- `releases/v9.2.0/manifest.zip` — Global checksum manifest.  

Governance approvals granted by the FAIR+CARE Council (Q3 2024).

---

## 🧭 FAIR+CARE Governance Summary

| Principle | Result | Notes |
|------------|---------|-------|
| **Findable** | ✅ | Indexed in STAC and public manifest. |
| **Accessible** | ✅ | Openly accessible via GitHub and Focus Mode API. |
| **Interoperable** | ✅ | Complies with GeoJSON and STAC schemas. |
| **Reusable** | ✅ | Includes full provenance and licensing. |
| **Collective Benefit** | ✅ | Promotes transparent climate research. |
| **Authority to Control** | ✅ | Data ownership attributed to NOAA and NIDIS. |
| **Responsibility** | ✅ | All values cross-verified against NCEI records. |
| **Ethics** | ✅ | No privacy or misuse concerns identified. |

---

## 🧾 Usage & Citation

**Access Path:**  
`data/archive/climate/climate_v9.2.0/`

**Citation Example:**
```text
Kansas Frontier Matrix (2024). Kansas Climate Dataset (v9.2.0).
FAIR+CARE-certified dataset integrating NOAA and NCEI historical climate data.
Available at: https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/archive/climate/climate_v9.2.0
License: CC-BY 4.0
```

---

## 🧾 Version Notes

- **Release v9.2.0:** Added Palmer Drought Severity and SPI indices.  
- **Enhancements:** Improved metadata structure and validation automation.  
- **Status:** Superseded by v9.3.2 (added anomaly layers and expanded temporal coverage).  

---

<div align="center">

**Kansas Frontier Matrix** · *Climate Intelligence × FAIR+CARE Stewardship × Provenance Integrity*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../../../docs/) • [⚖️ Governance Ledger](../../../../docs/standards/governance/)

</div>
