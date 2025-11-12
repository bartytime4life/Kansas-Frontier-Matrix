---
title: "🌿 Kansas Frontier Matrix — Raw Landcover Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/landcover/README.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.2.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-landcover-v10.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Public Domain / Open Data Commons"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌿 Kansas Frontier Matrix — **Raw Landcover Data**  
`data/raw/landcover/README.md`

**Purpose:**  
Immutable repository for **unaltered vegetation, soil, and surface classification datasets** from **NASA (MODIS/VIIRS/Landsat), USGS (NLCD), ESA/Copernicus (GLC/CCI)**, and Kansas DASC/KGS partners.  
Provides foundational inputs for NDVI analysis, land-use classification, canopy trends, and vegetation monitoring under **FAIR+CARE** governance with **Streaming STAC** and telemetry v2 bindings.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/README.md)
[![License: Open Data](https://img.shields.io/badge/License-Open%20Data-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Landcover%20Governed-gold.svg)](../../../docs/standards/faircare.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Raw Landcover Data Layer** preserves unmodified geospatial datasets representing Kansas vegetation and surface conditions.  
All sources are maintained with **checksums**, **provenance**, **licensing**, and **FAIR+CARE pre-audit** metadata to ensure reproducibility and ethical reuse.

**v10.2.2 Enhancements**
- **Streaming STAC** updates for near-real-time NDVI feeds (MODIS & VIIRS).  
- Telemetry v2 energy and CO₂ metrics integrated for ingestion validation.  
- Expanded pre-audit schema including sensitivity and attribution metadata.

### Core Objectives

- Store **unaltered** satellite rasters and vector classifications.  
- Provide **provenance & licensing** for FAIR+CARE audits.  
- Maintain **checksum** registry for dataset integrity.  
- Enable downstream ETL, AI classification, and Focus Mode v2.1 analyses.

---

## 🗂️ Directory Layout

```plaintext
data/raw/landcover/
├── README.md
├── nlcd_landcover_2021.tif                # USGS NLCD 2021 landcover (Kansas)
├── modis_ndvi_2025.tif                    # MODIS NDVI composite imagery
├── viirs_ndvi_2025.tif                    # VIIRS NDVI composite imagery
├── landsat_surface_reflectance.tif        # Landsat 8/9 SR raster
├── copernicus_landcover_2025.geojson      # Copernicus GLC vegetation classes
├── soil_moisture_surface_esa_2025.tif     # ESA CCI surface soil moisture
├── metadata.json                          # Checksums, provenance, FAIR+CARE pre-audit refs
└── source_licenses.json                   # Licensing & attribution per provider
```

---

## 🧭 Data Acquisition Summary

| Dataset | Source / Provider | Resolution | Format | License | Integrity |
|---|---|---:|---|---|---:|
| NLCD Landcover 2021 | USGS NLCD | 30 m | GeoTIFF | Public Domain | ✅ |
| MODIS NDVI 2025 | NASA MODIS (MOD13) | 250 m | GeoTIFF | Public Domain | ✅ |
| VIIRS NDVI 2025 | NASA VIIRS (VNP13) | 500 m | GeoTIFF | Public Domain | ✅ |
| Landsat Reflectance | NASA / USGS | 30 m | GeoTIFF | Public Domain | ✅ |
| Copernicus GLC 2025 | ESA Copernicus GLC | 100 m | GeoJSON | Open Data | ✅ |
| ESA Soil Moisture 2025 | ESA CCI | 0.25 ° | GeoTIFF | Open Data | ✅ |

---

## 🧩 Example Source Metadata Record

```json
{
  "id": "modis_ndvi_2025_raw",
  "source": "NASA MODIS MOD13 NDVI Product",
  "data_url": "https://lpdaac.usgs.gov/products/mod13a1v061/",
  "provider": "NASA LP DAAC / USGS EROS",
  "format": "GeoTIFF",
  "license": "Public Domain (NASA)",
  "records_fetched": 1,
  "checksum_sha256": "sha256:7b6e214bb5c5d67ea4db8afc1a2d9bba9f08e276ccf3d0a1d4d8e2e41f59b4af",
  "retrieved_on": "2025-11-12T20:48:00Z",
  "validator": "@kfm-landcover-lab",
  "faircare_preaudit": {
    "sensitivity": "none",
    "license_review": "ok",
    "community_flags": []
  },
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|---|---|---|
| **Findable** | STAC/DCAT metadata for dataset discoverability. | `@kfm-data` |
| **Accessible** | Publicly downloadable data; open formats. | `@kfm-accessibility` |
| **Interoperable** | CRS preserved (EPSG:4326); GeoTIFF/GeoJSON formats. | `@kfm-architecture` |
| **Reusable** | Provenance, checksum, and license metadata included. | `@kfm-design` |
| **Collective Benefit** | Enables ecological and sustainability research. | `@faircare-council` |
| **Authority to Control** | Council approves ingestion and ethics. | `@kfm-governance` |
| **Responsibility** | Validators verify checksums and metadata completeness. | `@kfm-security` |
| **Ethics** | Sensitive/derived data reviewed; attribution enforced. | `@kfm-ethics` |

---

## 🧠 Integrity & Cataloging

| Process | Description | Output |
|---|---|---|
| **Checksum Verify** | SHA-256 hashing; vendor hash comparison. | `data/raw/landcover/metadata.json` |
| **Provenance Log** | Acquisition lineage & reviewer notes. | `data/reports/audit/data_provenance_ledger.json` |
| **License Audit** | FAIR+CARE license & attribution verification. | `data/raw/landcover/source_licenses.json` |
| **Catalog Publish** | STAC/DCAT registration for global discovery. | `data/raw/metadata/stac_catalog.json` |

---

## ⚖️ Retention & Sustainability

| Data Type | Retention | Policy |
|---|---|---|
| Raw Landcover Data | Permanent | Immutable archival under ISO 19115 lineage. |
| Source Metadata | Permanent | Preserved for FAIR+CARE audits. |
| Checksum Records | Permanent | Long-term integrity evidence. |
| FAIR+CARE Pre-Audits | 5 Years | Periodic ethics review archive. |
| Ingestion Logs | 365 Days | Rotated via CI/CD compliance. |

**Telemetry Source:** `../../../releases/v10.2.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Landcover Data (v10.2.2).
Unaltered landcover, vegetation, and soil datasets from NASA, USGS, ESA/Copernicus, and Kansas DASC.
Checksum-verified, FAIR+CARE-aligned, and provenance-governed for transparent environmental analytics.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.2.2 | 2025-11-12 | `@kfm-landcover` | Aligned to v10.2: Streaming STAC, telemetry v2 integration, expanded FAIR+CARE fields. |
| v10.0.0 | 2025-11-09 | `@kfm-landcover` | Initial v10 release with telemetry hooks and licensing audits. |
| v9.7.0 | 2025-11-06 | `@kfm-landcover` | Added STAC/DCAT alignment and checksum registry. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Environmental Intelligence × FAIR+CARE Ethics × Provenance Integrity*  
© 2025 Kansas Frontier Matrix — Public Domain / Open Data Commons · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>