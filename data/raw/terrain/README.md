---
title: "🏔️ Kansas Frontier Matrix — Raw Terrain Data (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/terrain/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-raw-terrain-v10.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "Public Domain / Open Data Commons"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🏔️ Kansas Frontier Matrix — **Raw Terrain Data**
`data/raw/terrain/README.md`

**Purpose:**  
Immutable collection of **unaltered elevation, slope, and topographic datasets** from **USGS 3DEP, NASA SRTM, and Kansas DASC/KGS**.  
Provides foundational inputs for terrain analysis, slope mapping, hydrological modeling, and Focus Mode analytics under **FAIR+CARE** and **ISO 19115**, with **Streaming STAC** and telemetry v2 integrations.

[![Docs · MCP](https://img.shields.io/badge/Docs%20·%20MCP-v6.3-blue.svg)](../../../docs/architecture/README.md)
[![Public Domain](https://img.shields.io/badge/License-Open%20Data-brightgreen.svg)](../../../LICENSE)
[![FAIR+CARE Ethics](https://img.shields.io/badge/FAIR%2BCARE-Raw%20Terrain%20Governed-gold.svg)](../../../docs/standards/faircare-validation.md)
[![STAC 1.0](https://img.shields.io/badge/STAC-1.0%20Compliant-0052cc.svg)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Metadata%20Aligned-green.svg)]()

</div>

---

## 📘 Overview
The **Raw Terrain Data Layer** houses unmodified geospatial rasters & vectors capturing Kansas elevation, slope, and terrain morphology.  
Datasets form the baseline for **topographic normalization**, **hydrologic basin modeling**, **hazard analysis**, and **3D visualization** across KFM.

**v10 Enhancements**
- **Streaming STAC** hooks for periodic DEM refresh & derivative updates.  
- Telemetry v2 bindings (energy/CO₂, validation coverage) for ingestion runs.  
- Expanded FAIR+CARE pre-audit fields (license nuances, sensitivity notes).

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
├── slope_raster_usgs_derived.tif          # Slope from USGS DEM (for reference only; still raw as delivered)
├── terrain_units_kansas.geojson           # Terrain unit classification polygons
├── metadata.json                          # Checksums, provenance, FAIR+CARE pre-audit fields
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
  "retrieved_on": "2025-11-09T19:58:00Z",
  "validator": "@kfm-terrain-lab",
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

## ⚖️ Retention & Sustainability
| Category           | Retention | Policy                                                  |
|---|---|---|
| Raw Terrain Data  | Permanent | Immutable archival for lineage & reproducibility.       |
| Source Metadata   | Permanent | ISO 19115 lineage retention.                            |
| Checksum Records  | Permanent | Long-term integrity evidence.                           |
| FAIR+CARE Pre-Audits | 5 Years| Licensing/ethics review archive.                        |
| Ingestion Logs    | 365 Days  | Rotated per governance policy.                          |

**Telemetry reference:** `../../../releases/v10.0.0/focus-telemetry.json`

---

## 🧾 Internal Use Citation
```text
Kansas Frontier Matrix (2025). Raw Terrain Data (v10.0.0).
Unaltered elevation, slope, and contour datasets from USGS, NASA SRTM, and Kansas DASC/KGS.
Checksum-verified and FAIR+CARE-aligned for transparent geospatial modeling, hydrological analysis, and Focus Mode v2 analytics.
```

---

## 🕰️ Version History
| Version | Date       | Author         | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-09 | `@kfm-terrain` | Upgraded to v10: Streaming STAC hooks, telemetry v2 bindings, expanded pre-audit fields. |
| v9.7.0  | 2025-11-06 | `@kfm-terrain` | Telemetry/schema refs aligned; governance & badges clarified. |
| v9.6.0  | 2025-11-03 | `@kfm-terrain` | Added SRTM & contour datasets with checksum validation. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Topography Intelligence × FAIR+CARE Ethics × Provenance Assurance*  
© 2025 Kansas Frontier Matrix — Public Domain / Open Data Commons · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Raw Data Index](../README.md) · [Governance Charter](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>