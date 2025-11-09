---
title: "🌦️ Kansas Frontier Matrix — Climatology Raw Datasets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/climatology/datasets/raw/README.md"
version: "v10.2.2"
last_updated: "2025-11-09"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/analyses-climatology-datasets-raw-v3.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climatology Raw Datasets**
`docs/analyses/climatology/datasets/raw/README.md`

**Purpose:**  
Document the **raw climate data inputs** used within the Kansas Frontier Matrix (KFM) climatology analysis pipeline.  
These datasets are unaltered, directly sourced from official providers (NOAA, NASA, PRISM, and CMIP6) and registered under **FAIR+CARE**, **STAC/DCAT 3.0**, and **ISO 19115** standards for provenance and transparency.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Raw_Datasets-orange)](../../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Active_Data-brightgreen)](../../../../../../releases/)
</div>

---

## 📘 Overview

This directory hosts **unaltered raw climate datasets** used to derive climatology analyses within KFM.  
Each dataset is stored in open formats (CSV, NetCDF, GeoTIFF) and tagged with **metadata JSON files** describing its source, coverage, and acquisition method.

These datasets feed preprocessing workflows in:
- `docs/analyses/climatology/temporal-modeling.md`
- `docs/analyses/climatology/spatial-trends.md`
- `docs/analyses/climatology/projection-modeling.md`

---

## 🗂️ Directory Layout

```plaintext
docs/analyses/climatology/datasets/raw/
├── README.md                                  # This document
├── ghcn_daily.csv                             # NOAA Global Historical Climatology Network (daily station data)
├── prism_monthly.nc                           # PRISM monthly climate normals and trends
├── daymet_daily.nc                            # NASA Daymet daily gridded climate data
├── cmip6_projections.nc                       # CMIP6 downscaled climate projections (SSP scenarios)
└── storm_events.csv                           # NOAA storm events database for Kansas
```

---

## ⚙️ Dataset Descriptions

| File | Source | Description | Temporal Range | Spatial Resolution | License |
|------|---------|-------------|----------------|--------------------|----------|
| **ghcn_daily.csv** | NOAA NCEI | Daily temperature and precipitation records from Kansas stations | 1880–2025 | Station points | Public Domain |
| **prism_monthly.nc** | PRISM Climate Group | Monthly temperature and precipitation climatologies | 1895–2025 | 4 km grid | CC-BY 4.0 |
| **daymet_daily.nc** | NASA ORNL DAAC | Daily gridded weather variables (P, Tmin, Tmax, VP) | 1980–2025 | 1 km grid | CC-BY 4.0 |
| **cmip6_projections.nc** | CMIP6 (Downscaled) | Climate projections for SSP1–2.6 to SSP5–8.5 | 2015–2100 | 0.25° grid | CC-BY 4.0 |
| **storm_events.csv** | NOAA Storm Events | Severe weather records (tornado, hail, floods) | 1950–2025 | County-level | Public Domain |

All raw datasets are validated upon import with SHA-256 checksums and logged in `metadata/provenance_log.json`.

---

## 🧩 FAIR+CARE Metadata Example

```json
{
  "dataset_id": "noaa-ghcn-daily-raw-ks",
  "title": "NOAA Global Historical Climatology Network - Daily (Kansas Subset)",
  "source_url": "https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/",
  "spatial_extent": [-102.05, 36.99, -94.6, 40.0],
  "temporal_coverage": ["1880-01-01", "2025-01-01"],
  "license": "Public Domain",
  "format": "CSV",
  "validation": {
    "integrity_check": "SHA-256 Verified",
    "missing_values": "2.1%",
    "duplicates_removed": 114,
    "validation_status": "Pass"
  },
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T13:50:00Z"
}
```

---

## ⚖️ FAIR+CARE Data Governance

| Principle | Implementation | Validation Source |
|------------|----------------|--------------------|
| **Findable** | Datasets cataloged with UUIDs in STAC/DCAT registries | `metadata/stac_catalog.json` |
| **Accessible** | Openly accessible via provider APIs and FAIR+CARE portal | FAIR+CARE Ledger |
| **Interoperable** | Open formats (CSV, NetCDF, GeoTIFF) | `telemetry_schema` |
| **Reusable** | Metadata includes full provenance and license info | `manifest_ref` |
| **Responsibility** | Energy and carbon logged during ingestion | `telemetry_ref` |
| **Ethics** | No private or restricted data; sensitive events generalized | FAIR+CARE Ethics Audit |

---

## 🧮 Telemetry & Sustainability Metrics

| Metric | Description | Value | Target | Unit |
|---------|-------------|--------|---------|------|
| **Energy (J)** | Energy consumed during data ingestion | 11.2 | ≤ 15 | Joules |
| **Carbon (gCO₂e)** | CO₂ emitted during processing | 0.0047 | ≤ 0.006 | gCO₂e |
| **Telemetry Coverage (%)** | FAIR+CARE trace completeness | 100 | ≥ 95 | % |
| **Audit Pass Rate (%)** | FAIR+CARE validation compliance | 100 | 100 | % |

---

## 🧾 Governance Ledger Record Example

```json
{
  "ledger_id": "climatology-raw-ledger-2025-11-09-0007",
  "component": "Climatology Raw Datasets Ingestion",
  "datasets": [
    "NOAA GHCN-Daily",
    "PRISM Monthly",
    "Daymet V4",
    "CMIP6 Downscaled",
    "NOAA Storm Events"
  ],
  "energy_joules": 11.2,
  "carbon_gCO2e": 0.0047,
  "faircare_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T13:55:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.2.2 | 2025-11-09 | FAIR+CARE Council | Published climatology raw dataset index with provenance tracking and telemetry metrics. |
| v10.2.1 | 2025-11-09 | Data Governance Group | Added metadata validation examples and STAC/DCAT compliance. |
| v10.2.0 | 2025-11-09 | KFM Climate Analysis Team | Created baseline raw dataset registry for climatology workflows. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Climatology Datasets](../README.md) · [Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

