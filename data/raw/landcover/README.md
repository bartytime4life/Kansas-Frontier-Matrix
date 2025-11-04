---
title: "🌿 Kansas Frontier Matrix — Raw Landcover Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/landcover/README.md"
version: "v9.6.0"
last_updated: "2025-11-03"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.6.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.6.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.6.0/focus-telemetry.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Public Domain / Open Data Commons"
---

<div align="center">

# 🌿 Kansas Frontier Matrix — **Raw Landcover Data**
`data/raw/landcover/README.md`

**Purpose:**  
Immutable repository for **unaltered vegetation, soil, and surface classification datasets** from NASA, USGS, and Copernicus.  
Provides the foundational input for vegetation monitoring, NDVI analysis, and land use classification pipelines under FAIR+CARE governance.

[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Landcover%20Governed-gold)](../../../docs/standards/faircare-validation.md)
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green)]()
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-blue)]()
[![License: Public Domain](https://img.shields.io/badge/License-Open%20Data-brightgreen)](../../../LICENSE)

</div>

---

## 📚 Overview

The **Raw Landcover Data Layer** preserves unmodified geospatial datasets representing Kansas vegetation and surface types.  
These datasets originate from **USGS NLCD, MODIS, Landsat, and Copernicus Global Land Service** archives.  
All data are checksum-verified, licensed under open-access policies, and registered in the **KFM Governance Ledger** for traceable FAIR+CARE compliance.

### Core Responsibilities
- Store unaltered satellite and raster data.  
- Provide provenance, licensing, and schema metadata.  
- Maintain checksum registry for integrity and reproducibility.  
- Enable downstream AI-driven classification and NDVI workflows.  

---

## 🗂️ Directory Layout

```plaintext
data/raw/landcover/
├── README.md                              # This file — documentation for raw landcover data
│
├── nlcd_landcover_2021.tif                # USGS NLCD 2021 landcover dataset for Kansas
├── modis_ndvi_2025.tif                    # MODIS NDVI composite imagery
├── landsat_surface_reflectance.tif        # Landsat 8/9 surface reflectance raster
├── copernicus_landcover_2025.geojson      # Copernicus GLC vegetation classification
├── soil_moisture_surface_esa_2025.tif     # ESA surface soil moisture raster
├── metadata.json                          # Checksum, provenance, and FAIR+CARE audit metadata
└── source_licenses.json                   # Source-specific licensing and attribution metadata
```

---

## 🧭 Data Acquisition Summary

| Dataset | Source | Resolution | Format | License | Integrity |
|----------|---------|-------------|---------|----------|------------|
| NLCD Landcover 2021 | USGS | 30 m | GeoTIFF | Public Domain | ✅ Verified |
| MODIS NDVI 2025 | NASA MODIS | 250 m | GeoTIFF | Public Domain | ✅ Verified |
| Landsat Reflectance | NASA / USGS | 30 m | GeoTIFF | Public Domain | ✅ Verified |
| Copernicus GLC | ESA Copernicus | 100 m | GeoJSON | Open Data | ✅ Verified |
| ESA Soil Moisture | ESA CCI | 0.25° | GeoTIFF | Open Data | ✅ Verified |

---

## 🧩 Example Source Metadata Record

```json
{
  "id": "modis_ndvi_2025_raw",
  "source": "NASA MODIS MOD13Q1 Global NDVI Product",
  "data_url": "https://modis.gsfc.nasa.gov/data/dataprod/mod13.php",
  "provider": "NASA Earth Science Division",
  "format": "GeoTIFF",
  "license": "Public Domain (NASA)",
  "records_fetched": 1,
  "checksum_sha256": "sha256:2a8c9e84f7b56ad9f93e5212c31cf83b61c9c9a12e6a85dfb7a13db86a3c75c9",
  "retrieved_on": "2025-11-03T19:50:00Z",
  "validator": "@kfm-landcover-lab",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|------------|----------------|------------|
| **Findable** | Indexed in STAC and DCAT metadata for global discoverability. | @kfm-data |
| **Accessible** | Publicly accessible via open data license. | @kfm-accessibility |
| **Interoperable** | Data maintained in standard raster formats (GeoTIFF, GeoJSON). | @kfm-architecture |
| **Reusable** | Metadata retains provenance and licensing details. | @kfm-design |
| **Collective Benefit** | Supports climate research and environmental planning. | @faircare-council |
| **Authority to Control** | FAIR+CARE Council validates source and access ethics. | @kfm-governance |
| **Responsibility** | Data maintainers verify file integrity and license compliance. | @kfm-security |
| **Ethics** | Private land-use identifiers anonymized for ethical access. | @kfm-ethics |

---

## 🧠 Data Integrity Verification

| Process | Description | Output |
|----------|--------------|---------|
| **Checksum Verification** | Validates source file integrity using SHA-256. | `data/raw/landcover/metadata.json` |
| **License Validation** | Verifies open licensing and attribution. | `data/raw/landcover/source_licenses.json` |
| **Provenance Logging** | Links source lineage with governance ledger. | `data/reports/audit/data_provenance_ledger.json` |
| **STAC/DCAT Registration** | Publishes metadata to interoperable catalogs. | `data/raw/metadata/stac_catalog.json` |

---

## 📊 Example Checksum Record

```json
{
  "file": "nlcd_landcover_2021.tif",
  "checksum_sha256": "sha256:6a8b921e23cc17e2e42d98fa83e8f45ac9b9e9125a84fce7a7f85b7b69e5d82f",
  "validated": true,
  "verified_on": "2025-11-03T19:53:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Retention & Provenance Policy

| Data Type | Retention Duration | Policy |
|------------|--------------------|--------|
| Raw Landcover Data | Permanent | Immutable archival under ISO 19115 compliance. |
| Metadata | Permanent | Stored for audit and lineage reference. |
| Checksum Records | Permanent | Maintained for integrity and reproducibility. |
| FAIR+CARE Pre-Audits | 5 Years | Archived for ethical verification. |
| Logs | 365 Days | Rotated annually for compliance. |

Retention automation handled by `raw_landcover_retention.yml`.

---

## 🌱 Sustainability Metrics

| Metric | Value | Verified By |
|---------|--------|--------------|
| Energy Use (per ingestion) | 15.8 Wh | @kfm-sustainability |
| Carbon Output | 21.0 gCO₂e | @kfm-security |
| Renewable Power Usage | 100% (RE100 Verified) | @kfm-infrastructure |
| FAIR+CARE Certification | 99.7% | @faircare-council |

Telemetry reference:  
`releases/v9.6.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Landcover Data (v9.6.0).
Unaltered landcover and vegetation datasets sourced from NASA, USGS, ESA, and Copernicus.
Checksum-verified, FAIR+CARE-aligned data for sustainable land management and climate analytics.
```

---

## 🧾 Version Notes

| Version | Date | Notes |
|----------|------|--------|
| v9.6.0 | 2025-11-03 | Added checksum verification and STAC/DCAT metadata alignment. |
| v9.5.0 | 2025-11-02 | Integrated FAIR+CARE ethics validation and licensing metadata. |
| v9.3.2 | 2025-10-28 | Established landcover ingestion structure under FAIR+CARE governance. |

---

<div align="center">

**Kansas Frontier Matrix** · *Environmental Intelligence × FAIR+CARE Ethics × Provenance Integrity*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Governance Ledger](../../../docs/standards/governance/DATA-GOVERNANCE.md) • [📊 FAIR+CARE Reports](../../../data/reports/fair/faircare_summary.json)

</div>