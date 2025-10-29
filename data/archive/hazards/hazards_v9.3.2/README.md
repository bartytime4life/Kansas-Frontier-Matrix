---
title: "🌪️ Kansas Frontier Matrix — Hazards Dataset v9.3.2 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/archive/hazards/hazards_v9.3.2/README.md"
version: "v9.3.2"
last_updated: "2025-10-28"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.3.2/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
ontology_alignment: "../../../../ontologies/CIDOC_CRM-HazardExt.owl"
---

<div align="center">

# 🌪️ Kansas Frontier Matrix — **Hazards Dataset v9.3.2**
`data/archive/hazards/hazards_v9.3.2/README.md`

**Purpose:** Immutable archived dataset combining all validated Kansas hazard data layers—tornadoes, floods, droughts, wildfires, and seismic events.  
This version represents the highest-quality, FAIR+CARE-verified integration of environmental hazards available for Kansas Frontier Matrix.

[![STAC Validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-gold)](../../../../docs/standards/faircare-validation.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

**Hazards Dataset v9.3.2** is the official archived release of the **Kansas Frontier Matrix Hazards Data Layer** for 2025.  
It integrates multi-agency hazard information into harmonized, validated GeoJSON datasets representing spatial and temporal hazard extents.

This dataset supports:
- Environmental hazard analysis and visualization.  
- Focus Mode AI reasoning for predictive modeling and historic pattern correlation.  
- Public transparency in environmental risk documentation.  
- FAIR+CARE-aligned data ethics and provenance accountability.

---

## 🗂️ Directory Layout

```plaintext
data/archive/hazards/hazards_v9.3.2/
├── README.md                          # This file — overview of v9.3.2 dataset
│
├── hazards_floods_2025.geojson        # Floodplain and inundation areas (NOAA/FEMA)
├── hazards_tornado_tracks_2025.geojson # Tornado paths and intensity points (NOAA SPC)
├── hazards_drought_zones_2025.geojson # Drought severity polygons (USDA/NOAA)
├── hazards_fire_risk_2025.geojson     # Wildfire occurrence and burn risk (USFS/KS Fire Marshal)
├── hazards_seismic_events_2025.geojson # Earthquake points and magnitudes (USGS)
│
├── metadata.json                      # Metadata and STAC item summary
├── provenance_record.json             # Provenance, lineage, and governance approvals
├── validation_report.json             # Schema, STAC, FAIR+CARE validation summary
├── checksums.sha256                   # Integrity verification hashes
└── governance_approval.md             # FAIR+CARE Council sign-off record
```

---

## ⚙️ Dataset Composition

| Layer | Source Agency | Description | Format |
|--------|----------------|-------------|---------|
| **Floods** | NOAA, FEMA | FEMA-designated flood hazard zones and high-water extents. | GeoJSON |
| **Tornadoes** | NOAA SPC | Tornado tracks, EF intensity ratings, and damage paths. | GeoJSON |
| **Droughts** | NOAA CPC, USDA | Weekly drought intensity and duration zones. | GeoJSON |
| **Wildfires** | USFS, KS Fire Marshal | Burn area polygons and risk intensity grids. | GeoJSON |
| **Seismic** | USGS | Earthquake epicenters with magnitude ≥ 2.5 since 1900. | GeoJSON |

Each file uses **EPSG:4326 (WGS84)** and shares temporal coverage between **1900–2025**.

---

## 🧩 Metadata Summary

```json
{
  "id": "hazards_v9.3.2",
  "title": "Kansas Multi-Hazard Integrated Dataset (v9.3.2)",
  "description": "Comprehensive, FAIR+CARE-validated environmental hazards dataset for Kansas combining flood, tornado, drought, fire, and seismic layers.",
  "version": "v9.3.2",
  "created": "2025-10-28T15:45:00Z",
  "license": "CC-BY 4.0",
  "keywords": ["hazards", "climate", "disaster", "kansas", "fair-care"],
  "providers": [
    {"name": "NOAA", "role": "data-source"},
    {"name": "USGS", "role": "data-source"},
    {"name": "FEMA", "role": "data-source"},
    {"name": "Kansas Geological Survey", "role": "validator"}
  ],
  "extent": {
    "spatial": {"bbox": [-102.05, 36.99, -94.61, 40.00]},
    "temporal": {"interval": ["1900-01-01T00:00:00Z", "2025-12-31T00:00:00Z"]}
  }
}
```

---

## 🧠 FAIR+CARE Compliance

| Principle | Implementation |
|------------|----------------|
| **Findable** | Indexed in STAC and manifest with unique dataset identifier. |
| **Accessible** | Public under CC-BY 4.0, downloadable directly from the repository. |
| **Interoperable** | Data conforms to GeoJSON and STAC metadata schemas. |
| **Reusable** | Rich provenance and FAIR metadata enable reproducibility. |
| **Collective Benefit** | Supports research and hazard mitigation planning for Kansas communities. |
| **Authority to Control** | All contributing agencies retain attribution and acknowledgment. |
| **Responsibility** | Data curated ethically and verified for correctness. |
| **Ethics** | Bias, sensitivity, and misuse prevention checks implemented. |

---

## 🔍 Validation Summary

| Validation Category | Status | Reference |
|----------------------|---------|------------|
| STAC Compliance | ✅ Passed | `validation_report.json` |
| Schema Conformance | ✅ Passed | `schema:hazards_v9.3.2.json` |
| FAIR+CARE Certification | ✅ Approved | `reports/fair/data_care_assessment.json` |
| Governance Approval | ✅ Signed | `governance_approval.md` |

**Checksum Verification:**  
All assets verified via `checksums.sha256` and `releases/v9.3.2/manifest.zip`.

---

## 🧾 Provenance Record (Excerpt)

```json
{
  "dataset_id": "hazards_v9.3.2",
  "etl_scripts": [
    "src/pipelines/etl/hazards/floods_pipeline.py",
    "src/pipelines/etl/hazards/tornado_pipeline.py"
  ],
  "validated_by": "@kfm-data-lab",
  "governance_approved_by": "@bartytime4life",
  "fairstatus": {"fair_score": 99, "care_score": 100},
  "checksum": "7dfb99aa8cc8b1f3b8a1af6e3a5f8879d37a2e94f3e876f3...",
  "archived_on": "2025-10-28T16:20:00Z",
  "linked_reports": {
    "audit_ledger": "data/reports/audit/data_provenance_ledger.json",
    "faircare_assessment": "data/reports/fair/data_care_assessment.json",
    "stac_item": "data/stac/items/hazards_v9.3.2.json"
  }
}
```

---

## ⚙️ Governance & Audit Integration

- **Governance Ledger:** `data/reports/audit/data_provenance_ledger.json`  
- **FAIR+CARE Summary:** `data/reports/fair/data_fair_summary.json`  
- **Validation Logs:** `data/reports/validation/stac_validation_report.json`  
- **STAC Record:** `data/stac/items/hazards_v9.3.2.json`  
- **Checksum Manifest:** `releases/v9.3.2/manifest.zip`

Governance sign-off is recorded under:
`data/reports/audit/archive_integrity_log.json`

---

## 📊 Data Usage & Citation

**How to Use:**
1. Load `.geojson` files in GIS tools such as QGIS or MapLibre.  
2. Overlay multiple hazard layers for correlation analysis.  
3. Use metadata for reproducibility or Focus Mode AI exploration.

**Citation Example:**
```text
Kansas Frontier Matrix (2025). Kansas Hazards Dataset (v9.3.2).
FAIR+CARE-verified multi-hazard archive compiled from NOAA, FEMA, USGS, and KGS data.
Available at: https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/archive/hazards/hazards_v9.3.2
License: CC-BY 4.0
```

---

## 🧾 Version Notes

- **v9.3.2:** Consolidated all 2025 hazard sources into unified GeoJSON files.  
- **Enhancements:** Added drought and wildfire layers; standardized CRS to EPSG:4326.  
- **Governance:** First dataset to achieve **Diamond⁹ Ω / Crown∞Ω Ultimate Certification** under FAIR+CARE validation.  

---

<div align="center">

**Kansas Frontier Matrix** · *Hazard Data × Provenance × FAIR+CARE Ethics*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../../../docs/) • [⚖️ Governance Ledger](../../../../docs/standards/governance/)

</div>
