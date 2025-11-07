---
title: "🏔️ Kansas Frontier Matrix — Raw Terrain Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/terrain/README.md"
version: "v9.7.0"
last_updated: "2025-11-06"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.7.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-terrain-v9.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Public Domain / Open Data Commons"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏔️ Kansas Frontier Matrix — **Raw Terrain Data**
`data/raw/terrain/README.md`

**Purpose:**  
Immutable collection of **unaltered elevation, slope, and topographic datasets** from **USGS, NASA SRTM, and Kansas DASC**.  
Provides foundational inputs for terrain analysis, slope mapping, and hydrological modeling under **FAIR+CARE** and **ISO 19115**.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/architecture/README.md)
[![Public Domain](https://img.shields.io/badge/License-Open%20Data-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Terrain%20Governed-gold.svg)](../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview

The **Raw Terrain Data Layer** houses unmodified geospatial rasters & vectors capturing Kansas elevation, slope, and terrain morphology.  
Datasets form the baseline for **topographic normalization**, **hydrologic basin modeling**, and **hazard analysis** across KFM.

### Core Objectives
- Preserve original terrain datasets from verified geospatial sources.  
- Maintain **checksum & provenance** for integrity assurance.  
- Enable **FAIR+CARE** transparency and **ISO 19115** lineage compliance.  
- Support **AI-assisted** slope modeling, runoff analysis, and elevation regridding.  

---

## 🗂️ Directory Layout

```plaintext
data/raw/terrain/
├── README.md
├── usgs_3dep_dem_10m.tif                  # USGS 3DEP 10 m DEM
├── nasa_srtm_30m.tif                      # NASA SRTM 30 m DEM
├── kansas_contours_10ft.geojson           # Kansas DASC contour lines
├── slope_raster_usgs_derived.tif          # Slope from USGS DEM
├── terrain_units_kansas.geojson           # Terrain unit classification polygons
├── metadata.json                          # Checksums, provenance, FAIR+CARE fields
└── source_licenses.json                   # Licensing & acquisition records
```

---

## 🧭 Data Acquisition Summary

| Dataset            | Source / Provider          | Resolution | Format  | License       | Integrity |
|-------------------|----------------------------|-----------:|---------|---------------|----------:|
| USGS 3DEP DEM     | USGS                       | 10 m       | GeoTIFF | Public Domain | ✅ Verified |
| NASA SRTM DEM     | NASA / JPL                 | 30 m       | GeoTIFF | Public Domain | ✅ Verified |
| KS Contours       | Kansas DASC                | 10 ft      | GeoJSON | Public Domain | ✅ Verified |
| Slope Raster      | Derived (USGS DEM)         | 10 m       | GeoTIFF | Derived (USGS)| ✅ Verified |
| Terrain Units     | Kansas Geological Survey   | vector     | GeoJSON | Public Domain | ✅ Verified |

---

## 🧩 Example Source Metadata Record

```json
{
  "id": "usgs_3dep_dem_10m_raw",
  "source": "USGS 3D Elevation Program (3DEP)",
  "data_url": "https://www.usgs.gov/core-science-systems/ngp/3dep",
  "provider": "United States Geological Survey (USGS)",
  "format": "GeoTIFF",
  "license": "Public Domain (USGS)",
  "records_fetched": 32,
  "checksum_sha256": "sha256:8b2e4c71a32f7b4d8e3c49e4d2e71a8c9e1f2c6b7a2b8a3e4c1d9e5a3f7a1b6d",
  "retrieved_on": "2025-11-06T19:58:00Z",
  "validator": "@kfm-terrain-lab",
  "governance_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚙️ FAIR+CARE Compliance Matrix

| Principle | Implementation | Oversight |
|-----------|----------------|-----------|
| **Findable** | STAC/DCAT catalog entries; governance linkages. | `@kfm-data` |
| **Accessible** | Open access; retrieval guidance documented. | `@kfm-accessibility` |
| **Interoperable** | GeoTIFF/GeoJSON standards; CRS preserved as delivered. | `@kfm-architecture` |
| **Reusable** | Provenance, schema, and checksums embedded in metadata. | `@kfm-design` |
| **Collective Benefit** | Enables open modeling & resilience planning. | `@faircare-council` |
| **Authority to Control** | Council validates ingestion and ethics. | `@kfm-governance` |
| **Responsibility** | Stewards verify integrity and metadata completeness. | `@kfm-security` |

---

## 🧠 Integrity & Cataloging

| Process            | Description                                  | Output                                           |
|-------------------|----------------------------------------------|--------------------------------------------------|
| **Checksum Verify** | SHA-256 hashing; vendor hash comparison.     | `data/raw/terrain/metadata.json`                 |
| **Provenance Log**  | Acquisition lineage & reviewer notes.         | `data/reports/audit/data_provenance_ledger.json` |
| **License Audit**   | FAIR+CARE licensing & attribution review.     | `data/raw/terrain/source_licenses.json`          |
| **Catalog Publish** | STAC/DCAT registration for discoverability.   | `data/raw/metadata/stac_catalog.json`            |

---

## 📊 Example Checksum Record

```json
{
  "file": "nasa_srtm_30m.tif",
  "checksum_sha256": "sha256:d4a3c8e1b2f7a8c9e3e1b4f9d7c6a8b9e4f5c7d2b3a1e8c9d4f3a7e2b9c1f6e4",
  "validated": true,
  "verified_on": "2025-11-06T20:00:00Z",
  "ledger_ref": "data/reports/audit/data_provenance_ledger.json"
}
```

---

## ⚖️ Retention & Sustainability

| Category           | Retention | Policy                                                  |
|-------------------|----------:|---------------------------------------------------------|
| Raw Terrain Data  | Permanent | Immutable archival for lineage & reproducibility.       |
| Source Metadata   | Permanent | ISO 19115 lineage retention.                            |
| Checksum Records  | Permanent | Long-term integrity evidence.                           |
| FAIR+CARE Pre-Audits | 5 Years| Licensing/ethics review archive.                        |
| Ingestion Logs    | 365 Days  | Rotated per governance policy.                          |

**Telemetry reference:** `../../../releases/v9.7.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation

```text
Kansas Frontier Matrix (2025). Raw Terrain Data (v9.7.0).
Unaltered elevation, slope, and contour datasets from USGS, NASA SRTM, and Kansas DASC.
Checksum-verified and FAIR+CARE-aligned for transparent geospatial modeling and Focus Mode analytics.
```

---

## 🕰️ Version History

| Version | Date       | Author         | Summary |
|--------:|------------|----------------|---------|
| v9.7.0  | 2025-11-06 | `@kfm-terrain` | Upgraded to v9.7.0; telemetry/schema refs aligned; governance & badges clarified. |
| v9.6.0  | 2025-11-03 | `@kfm-terrain` | Added SRTM & contour datasets with checksum validation. |
| v9.5.0  | 2025-11-02 | `@kfm-governance` | Integrated FAIR+CARE audit & provenance manifest. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Topography Intelligence × FAIR+CARE Ethics × Provenance Assurance*  
© 2025 Kansas Frontier Matrix — Public Domain / Open Data Commons · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>