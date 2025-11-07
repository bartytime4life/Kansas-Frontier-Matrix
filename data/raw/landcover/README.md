---
title: "🌿 Kansas Frontier Matrix — Raw Landcover Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/landcover/README.md"
version: "v9.7.0"
last_updated: "2025-11-06"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.7.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-landcover-v9.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Public Domain / Open Data Commons"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌿 Kansas Frontier Matrix — **Raw Landcover Data**
`data/raw/landcover/README.md`

**Purpose:**  
Immutable repository for **unaltered vegetation, soil, and surface classification datasets** from **NASA, USGS, ESA/Copernicus**, and state partners.  
Provides foundational inputs for NDVI analysis, land-use classification, and vegetation monitoring under **FAIR+CARE** governance.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/architecture/README.md)
[![Public Domain / ODC](https://img.shields.io/badge/License-Open%20Data-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Landcover%20Governed-gold.svg)](../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Raw Landcover Data Layer** preserves unmodified geospatial datasets representing Kansas vegetation and surface types.  
Data originate from **USGS NLCD, MODIS, Landsat, and Copernicus Global Land Service** archives and are stored with **checksums, provenance, and licensing** for complete reproducibility.

### Core Responsibilities
- Store **unaltered** satellite rasters and vector classifications.  
- Provide **provenance & licensing** for FAIR+CARE audits.  
- Maintain **checksum** registry for integrity.  
- Enable downstream ETL, AI classification, and NDVI pipelines.  

---

## 🗂️ Directory Layout

```plaintext
data/raw/landcover/
├── README.md
├── nlcd_landcover_2021.tif                # USGS NLCD 2021 landcover (Kansas)
├── modis_ndvi_2025.tif                    # MODIS NDVI composite imagery
├── landsat_surface_reflectance.tif        # Landsat 8/9 SR raster
├── copernicus_landcover_2025.geojson      # Copernicus GLC vegetation classes
├── soil_moisture_surface_esa_2025.tif     # ESA CCI surface soil moisture
├── metadata.json                          # Checksums, provenance, FAIR+CARE audit refs
└── source_licenses.json                   # Licensing & attribution per provider
```

---

## 🧭 Data Acquisition Summary

| Dataset                 | Source / Provider       | Resolution | Format  | License      | Integrity |
|------------------------|-------------------------|-----------:|---------|--------------|----------:|
| NLCD Landcover 2021    | USGS NLCD               |       30 m | GeoTIFF | Public Domain| ✅ Verified |
| MODIS NDVI 2025        | NASA MODIS (MOD13)      |      250 m | GeoTIFF | Public Domain| ✅ Verified |
| Landsat Reflectance    | NASA / USGS             |       30 m | GeoTIFF | Public Domain| ✅ Verified |
| Copernicus GLC 2025    | ESA Copernicus GLC      |      100 m | GeoJSON | Open Data    | ✅ Verified |
| ESA Soil Moisture 2025 | ESA CCI                 |     0.25 ° | GeoTIFF | Open Data    | ✅ Verified |

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
  "retrieved_on": "2025-11-06T19:50:00Z",
  "validator": "@kfm-landcover-lab",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|-----------|----------------|-----------|
| **Findable** | STAC/DCAT metadata for global discoverability. | `@kfm-data` |
| **Accessible** | Open data access with clear attribution. | `@kfm-accessibility` |
| **Interoperable** | Standard formats (GeoTIFF/GeoJSON) retained. | `@kfm-architecture` |
| **Reusable** | Provenance, license, and checksum metadata included. | `@kfm-design` |
| **Collective Benefit** | Supports sustainable land management & research. | `@faircare-council` |
| **Authority to Control** | Council validates source/ethics. | `@kfm-governance` |
| **Responsibility** | Stewards verify integrity and compliance. | `@kfm-security` |

---

## 🧠 Data Integrity & Cataloging

| Process            | Description                                  | Output                                           |
|-------------------|----------------------------------------------|--------------------------------------------------|
| **Checksum Verify** | SHA-256 per file; vendor hash comparison.     | `data/raw/landcover/metadata.json`               |
| **Provenance Log**  | Acquisition lineage & reviewer notes.         | `data/reports/audit/data_provenance_ledger.json` |
| **License Audit**   | FAIR+CARE licensing & attribution review.     | `data/raw/landcover/source_licenses.json`        |
| **Catalog Publish** | STAC/DCAT registration for discoverability.   | `data/raw/metadata/stac_catalog.json`            |

---

## 📊 Example Checksum Record

```json
{
  "file": "nlcd_landcover_2021.tif",
  "checksum_sha256": "sha256:6a8b921e23cc17e2e42d98fa83e8f45ac9b9e9125a84fce7a7f85b7b69e5d82f",
  "validated": true,
  "verified_on": "2025-11-06T19:53:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Retention & Sustainability

| Data Type             | Retention | Policy                                                  |
|----------------------|----------:|---------------------------------------------------------|
| Raw Landcover Data   | Permanent | Immutable archival under ISO 19115 lineage.            |
| Source Metadata      | Permanent | Preserved for audit and reuse.                          |
| Checksum Records     | Permanent | Long-term integrity evidence.                           |
| FAIR+CARE Pre-Audits | 5 Years   | Licensing/ethics review archive.                        |
| Ingestion Logs       | 365 Days  | Rotated per governance compliance.                      |

**Telemetry reference:** `../../../releases/v9.7.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Landcover Data (v9.7.0).
Unaltered landcover & vegetation datasets from NASA, USGS, ESA/Copernicus.
Checksum-verified, FAIR+CARE-aligned inputs enabling ethical open science and Focus Mode land systems analytics.
```

---

## 🕰️ Version History

| Version | Date       | Author          | Summary |
|--------:|------------|-----------------|---------|
| v9.7.0  | 2025-11-06 | `@kfm-landcover`| Upgraded to v9.7.0; telemetry/schema refs aligned; badges hardened; expanded acquisition summary. |
| v9.6.0  | 2025-11-03 | `@kfm-landcover`| Added checksum verification and STAC/DCAT metadata alignment. |
| v9.5.0  | 2025-11-02 | `@kfm-governance` | Integrated FAIR+CARE audit and licensing records. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Environmental Intelligence × FAIR+CARE Ethics × Provenance Integrity*  
© 2025 Kansas Frontier Matrix — Public Domain / Open Data Commons · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>