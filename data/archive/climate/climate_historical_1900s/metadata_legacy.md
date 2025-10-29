---
title: "🧾 Kansas Frontier Matrix — Legacy Metadata (Climate Historical 1900s)"
path: "data/archive/climate/climate_historical_1900s/metadata_legacy.md"
version: "v8.x-Legacy"
last_updated: "2025-10-28"
review_cycle: "Permanent / Historical"
compiled_by: "@kfm-data-lab"
reviewed_by: "@bartytime4life"
data_sources:
  - "NOAA National Centers for Environmental Information (NCEI)"
  - "U.S. Historical Climatology Network (USHCN)"
  - "Kansas Mesonet"
license: "CC-BY 4.0"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — **Legacy Metadata File**
### Climate Historical 1900s Archive  
`data/archive/climate/climate_historical_1900s/metadata_legacy.md`

**Purpose:** Documents metadata for Kansas historical climate datasets covering 1900–1999, reconstructed and preserved as part of the Kansas Frontier Matrix (KFM) legacy archive.  
This metadata was retroactively generated under FAIR+CARE audit procedures (2025) to ensure transparency, discoverability, and long-term reproducibility.

[![Legacy Status](https://img.shields.io/badge/Status-Legacy%20Preserved-grey)](../../../../docs/standards/governance/DATA-GOVERNANCE.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![FAIR+CARE Alignment](https://img.shields.io/badge/FAIR%2BCARE-Retrospective%20Applied-yellow)](../../../../docs/standards/faircare-validation.md)

</div>

---

## 🧭 Dataset Overview

| Field | Value |
|--------|--------|
| **Dataset ID** | `climate_historical_1900s` |
| **Title** | Kansas Historical Climate Dataset (1900–1999) |
| **Description** | Early Kansas temperature and precipitation datasets digitized from NOAA, USHCN, and NCEI archives. Retrospectively metadata-enhanced and validated under FAIR+CARE review (2025). |
| **Temporal Coverage** | 1900–1999 |
| **Spatial Extent** | Kansas statewide (longitude -102.05 to -94.61, latitude 36.99 to 40.00) |
| **Coordinate System** | EPSG:4326 (WGS84) |
| **License** | CC-BY 4.0 |
| **Data Format** | GeoJSON (converted from CSV/shapefile sources) |
| **Total Files** | 2 primary datasets + 2 governance records |

---

## 🌍 Source Datasets

| Source Agency | Dataset | Original Format | Converted Format | Coverage |
|----------------|----------|------------------|------------------|-----------|
| NOAA NCEI | U.S. Monthly Climate Summary (1900–1999) | CSV | GeoJSON | Kansas statewide |
| USHCN | Temperature and Precipitation Records | Fixed-width text | GeoJSON | Station-based |
| Kansas Mesonet | Precipitation Index (1950–1999) | CSV | GeoJSON | Kansas counties |

---

## 🧩 Provenance Reconstruction

These legacy datasets were manually aligned with the **FAIR+CARE** governance model using retrospective audit documentation.

| Provenance Field | Description | Example |
|------------------|-------------|----------|
| `source_reference` | Original dataset URL or archive name | `"https://www.ncei.noaa.gov/pub/data/cdo/summaries/"` |
| `ingestion_date` | Approximate date of import into KFM | `"2020-07-15"` |
| `conversion_tool` | Software or script used for format conversion | `"ogr2ogr (GDAL 3.1.0)"` |
| `quality_notes` | QA comments from retrospective validation | `"CRS unified to EPSG:4326; missing metadata added manually."` |
| `ethics_review_status` | Result of 2025 FAIR+CARE retrospective review | `"Approved"` |

---

## 🧠 FAIR+CARE Retrospective Notes (2025 Review)

**FAIR Principles Applied:**
- *Findable:* Metadata fields (`id`, `title`, `description`, `extent`, `provider`) added manually.  
- *Accessible:* All datasets released under CC-BY 4.0 license.  
- *Interoperable:* Converted to GeoJSON for universal GIS compatibility.  
- *Reusable:* Provenance reconstructed; checksums generated and validated.

**CARE Principles Applied:**
- *Collective Benefit:* Retained to ensure research transparency and public accessibility.  
- *Authority to Control:* Source institutions fully acknowledged and cited.  
- *Responsibility:* Retro-validation process documented by KFM governance team.  
- *Ethics:* Verified that no personal, restricted, or sensitive data exist.

**Audit File:**  
`data/archive/climate/climate_historical_1900s/retro_audit_notes.json`

---

## 🧾 Dataset File Summary

| File | Description | Size (MB) | CRS | Temporal Range |
|------|--------------|------------|------|----------------|
| `kansas_temp_1900_1999.geojson` | Kansas temperature observations (monthly mean) | 5.8 | EPSG:4326 | 1900–1999 |
| `kansas_precip_1950.geojson` | Annual precipitation dataset for 1950 (county aggregates) | 1.2 | EPSG:4326 | 1950 |

---

## ⚙️ Validation Metadata

```json
{
  "validation": {
    "performed_by": "@kfm-data-lab",
    "review_date": "2025-03-05",
    "stac_compliance": "partial",
    "metadata_added": ["extent", "license", "keywords", "provider"],
    "checksum_verified": true,
    "governance_approval": "retrospective"
  }
}
```

Validation log cross-referenced with:  
`data/reports/validation/schema_validation_summary.json`

---

## ⚖️ Governance & Ethics Summary

> The FAIR+CARE Council retroactively approved this dataset for **historical retention** on *March 10, 2025.*  
> The council found no ethical, attributional, or scientific concerns preventing open access.  
> Future use of this data should acknowledge both its historical limitations and its foundational role in the evolution of Kansas climate analytics.

Governance records:
- `data/reports/audit/archive_integrity_log.json`  
- `data/reports/fair/ethics_review_summary.md`

---

## 🧾 Recommended Citation

```text
Kansas Frontier Matrix (Legacy Archive). Kansas Historical Climate Dataset (1900–1999).
Retrospective FAIR+CARE metadata reconstruction by KFM Data Lab, 2025.
Available at: https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/data/archive/climate/climate_historical_1900s
License: CC-BY 4.0
```

---

<div align="center">

**Kansas Frontier Matrix** · *Legacy Climate Data × FAIR+CARE Retrospective Integrity × Historical Transparency*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../../../docs/) • [⚖️ Governance Ledger](../../../../docs/standards/governance/)

</div>
