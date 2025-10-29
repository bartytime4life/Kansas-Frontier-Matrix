---
title: "🌪️ Kansas Frontier Matrix — Hazards Dataset v9.2.0 (FAIR+CARE Legacy Certified)"
path: "data/archive/hazards/hazards_v9.2.0/README.md"
version: "v9.2.0"
last_updated: "2025-07-31"
review_cycle: "Quarterly / Historical"
commit_sha: "<legacy-commit-hash>"
sbom_ref: "../../../../releases/v9.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.2.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
ontology_alignment: "../../../../ontologies/CIDOC_CRM-HazardExt.owl"
---

<div align="center">

# 🌪️ Kansas Frontier Matrix — **Hazards Dataset v9.2.0**
`data/archive/hazards/hazards_v9.2.0/README.md`

**Purpose:** Archived version of Kansas multi-hazard dataset integrating flood, tornado, and drought data for the 2024 cycle.  
This version predates full AI-layer integration but remains FAIR+CARE certified and validated for geospatial and schema integrity.

[![STAC Validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Legacy%20Certified-gold)](../../../../docs/standards/faircare-validation.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

**Hazards Dataset v9.2.0** was the final 2024 release of Kansas Frontier Matrix’s hazard data integration prior to Focus Mode AI adoption.  
It aggregates verified NOAA, FEMA, and USGS datasets into a unified spatiotemporal dataset covering multiple natural hazard domains across Kansas.

Key Features:
- Combines floodplains, tornado tracks, and drought areas into a single harmonized product.  
- FAIR+CARE compliant and validated through governance workflows.  
- Serves as a baseline dataset for version **v9.3.2** improvements.  

---

## 🗂️ Directory Layout

```plaintext
data/archive/hazards/hazards_v9.2.0/
├── README.md                           # This file — overview of dataset v9.2.0
│
├── hazards_combined_2024.geojson       # Merged hazard dataset (flood, tornado, drought)
├── metadata.json                       # STAC-compatible metadata record
├── provenance_record.json              # Provenance and validation metadata
├── validation_report.json              # Validation results summary
└── checksums.sha256                    # Integrity verification file
```

---

## ⚙️ Dataset Composition

| Hazard Type | Source Agency | Description | Format |
|--------------|----------------|-------------|---------|
| **Flood Zones** | FEMA, NOAA | Floodplain polygons and historical inundation areas. | GeoJSON |
| **Tornado Tracks** | NOAA SPC | Tornado paths and attributes (EF0–EF5). | GeoJSON |
| **Drought Severity** | NOAA CPC | Polygonal drought intensity zones (weekly). | GeoJSON |

Spatial reference: **EPSG:4326 (WGS84)**  
Temporal coverage: **1900–2024**

---

## 🧩 Metadata Summary

```json
{
  "id": "hazards_v9.2.0",
  "title": "Kansas Hazards Dataset (v9.2.0)",
  "description": "Integrated hazard dataset combining flood, tornado, and drought data layers for Kansas.",
  "version": "v9.2.0",
  "created": "2024-07-31T14:00:00Z",
  "license": "CC-BY 4.0",
  "providers": [
    {"name": "NOAA", "role": "data-source"},
    {"name": "FEMA", "role": "data-source"},
    {"name": "USGS", "role": "data-source"}
  ],
  "extent": {
    "spatial": {"bbox": [-102.05, 36.99, -94.61, 40.00]},
    "temporal": {"interval": ["1900-01-01T00:00:00Z", "2024-12-31T00:00:00Z"]}
  }
}
```

---

## 🧠 FAIR+CARE Validation Summary

| Validation Category | Status | Report Reference |
|----------------------|---------|------------------|
| STAC Schema Validation | ✅ Passed | `validation_report.json` |
| FAIR Metadata Compliance | ✅ Approved | `data/reports/fair/data_fair_summary.json` |
| CARE Ethical Review | ✅ Approved | `data/reports/fair/data_care_assessment.json` |
| Governance Review | ✅ Signed | `data/reports/audit/data_provenance_ledger.json` |

---

## 🔍 Provenance Record (Excerpt)

```json
{
  "dataset_id": "hazards_v9.2.0",
  "compiled_by": "@kfm-etl-ops",
  "validated_by": "@kfm-data-lab",
  "archived_on": "2024-08-01T09:00:00Z",
  "checksum": "ed65f7c48eae09c5f09f357abc7b23e45bfe783d34c1987f...",
  "sources": [
    "data/sources/noaa_weather_datasets.json",
    "data/sources/fema_disaster_catalog.json"
  ],
  "lineage": {
    "etl_script": "src/pipelines/etl/hazards/hazards_merge_pipeline.py",
    "validated_in": "data/reports/validation/stac_validation_report.json"
  },
  "governance_decision": "approved"
}
```

---

## ⚙️ Data Integrity and Governance

- **Checksum Validation:** Verified via `checksums.sha256` and recorded in `manifest.zip`.  
- **Audit Ledger:** Registered in `data/reports/audit/data_provenance_ledger.json`.  
- **FAIR+CARE Certification:** Approved and documented in `data/reports/fair/`.  
- **Validation Reports:** STAC validation outcomes stored in `data/reports/validation/`.  

Governance review conducted under the FAIR+CARE Council (2024 Q3).

---

## ⚖️ Ethical Stewardship

This dataset underwent FAIR+CARE Council review and was approved for:
- Public release under CC-BY 4.0.  
- Integration into Focus Mode as a training baseline for AI-driven hazard correlation.  
- Permanent archival under `data/archive/hazards/`.

No sensitive or personal data are contained within this dataset.

---

## 🧾 Usage & Citation

**Access Path:**  
`data/archive/hazards/hazards_v9.2.0/hazards_combined_2024.geojson`

**Citation Example:**
```text
Kansas Frontier Matrix (2024). Kansas Hazards Dataset (v9.2.0).
FAIR+CARE-validated integrated dataset combining flood, tornado, and drought hazards.
Available at: https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/archive/hazards/hazards_v9.2.0
License: CC-BY 4.0
```

---

## 🧾 Version Notes

| Version | Date | Notes |
|----------|------|--------|
| v9.2.0 | 2024-07-31 | Unified hazard dataset integrating flood, tornado, and drought sources; validated and archived under FAIR+CARE governance. |
| v9.1.0 | 2024-04-30 | Added drought polygons; improved spatial joins and metadata compliance. |
| v9.0.0 | 2024-01-15 | Initial release of merged hazards dataset; schema aligned with STAC 1.0. |

---

<div align="center">

**Kansas Frontier Matrix** · *Hazard Science × FAIR+CARE Ethics × Reproducible Archival Data*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../../../docs/) • [⚖️ Governance Ledger](../../../../docs/standards/governance/)

</div>
