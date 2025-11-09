---
title: "🌦️ Kansas Frontier Matrix — Climatology Datasets Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/climatology/datasets/README.md"
version: "v10.2.2"
last_updated: "2025-11-09"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/analyses-climatology-datasets-v3.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌦️ **Kansas Frontier Matrix — Climatology Datasets Registry**
`docs/analyses/climatology/datasets/README.md`

**Purpose:**  
Catalog and describe all **climate data sources**, **metadata standards**, and **validation frameworks** used for climatology analyses in the Kansas Frontier Matrix (KFM).  
This registry defines how raw, processed, and derived datasets align with **FAIR+CARE**, **STAC/DCAT 3.0**, and **ISO 19115** metadata schemas to ensure reproducibility and ethical governance.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Climatology_Datasets-orange)](../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Active_Build-brightgreen)](../../../../../releases/)
</div>

---

## 📘 Overview

The **Climatology Datasets Registry** provides a structured inventory of climate observations, reanalyses, and projections integrated into KFM analyses.  
Each dataset includes provenance, spatial–temporal coverage, processing methods, validation results, and governance metadata.

All data follow open formats (**NetCDF**, **CSV**, **GeoTIFF**) and contain **JSON-LD metadata** to ensure alignment with FAIR+CARE and ISO documentation standards.

---

## 🗂️ Directory Layout

```plaintext
docs/analyses/climatology/datasets/
├── README.md                                  # This document
├── raw/                                       # Original downloaded data (NOAA, PRISM, NASA, CMIP6)
│   ├── ghcn_daily.csv
│   ├── prism_monthly.nc
│   ├── daymet_daily.nc
│   ├── cmip6_projections.nc
│   └── storm_events.csv
├── processed/                                 # Bias-corrected, cleaned, and harmonized datasets
│   ├── temperature_trends.csv
│   ├── precipitation_anomalies.nc
│   ├── seasonal_means.nc
│   └── climate_extremes.csv
├── derived/                                   # Analytical outputs and derived indices
│   ├── spei_indices.csv
│   ├── trend_slopes.nc
│   └── anomaly_surfaces.tif
└── metadata/                                  # STAC / DCAT / FAIR+CARE metadata registry
    ├── README.md
    ├── stac_catalog.json
    ├── dcat_metadata.json
    ├── faircare_validation.json
    └── provenance_log.json
```

---

## ⚙️ Primary Climate Datasets

| Source | Dataset | Variables | Coverage | Format | FAIR+CARE Status |
|--------|----------|------------|-----------|---------|------------------|
| **NOAA NCEI** | GHCN-Daily | Tmin, Tmax, Precip | 1880–present | CSV / JSON | ✅ Certified |
| **PRISM Climate Group** | Monthly Averages | Tmean, Precip | 1895–present | NetCDF | ✅ Certified |
| **NASA Daymet V4** | Daily Weather Parameters | Tmin, Tmax, Precip, VP | 1980–present | NetCDF | ✅ Certified |
| **CMIP6 (Downscaled)** | SSP Projections | Tmean, Precip, PET | 2015–2100 | NetCDF | ✅ Certified |
| **NOAA Storm Events** | Severe Weather | Event Type, Location, Date | 1950–present | CSV | ✅ Certified |

---

## 🧩 Metadata & Governance Standards

All climate datasets are registered using interoperable metadata following:
- **STAC 1.0** for spatiotemporal cataloging  
- **DCAT 3.0** for dataset and distribution linking  
- **FAIR+CARE Metadata Schema v3** for ethical and sustainability documentation  

Example entry from `metadata/stac_catalog.json`:
```json
{
  "stac_version": "1.0.0",
  "type": "Collection",
  "id": "noaa-ghcn-daily",
  "title": "NOAA Global Historical Climatology Network - Daily",
  "extent": {
    "spatial": {"bbox": [[-102.05, 36.99, -94.6, 40.0]]},
    "temporal": {"interval": [["1880-01-01T00:00:00Z", "2025-01-01T00:00:00Z"]]}
  },
  "license": "Public Domain",
  "keywords": ["climate", "temperature", "precipitation", "Kansas"],
  "providers": [{"name": "NOAA NCEI", "roles": ["producer", "licensor"]}],
  "links": [{"rel": "self", "href": "stac_catalog.json"}]
}
```

---

## 🌡️ Processing and Quality Control

1. **Bias Correction** — Align CMIP6 and PRISM means using quantile mapping.  
2. **Gap Filling** — Interpolate missing records via climatological mean substitution.  
3. **Outlier Filtering** — Z-score thresholding (>3σ) followed by manual verification.  
4. **Reprojection** — All rasters standardized to **EPSG:4326 (WGS84)**.  
5. **Temporal Normalization** — Monthly and seasonal aggregates (DJF, MAM, JJA, SON).

Validation metrics logged to `metadata/faircare_validation.json`.

---

## 🧮 FAIR+CARE Validation Example

```json
{
  "validation_id": "climatology-datasets-2025-11-09-002",
  "datasets": [
    "NOAA GHCN-Daily",
    "PRISM Monthly",
    "NASA Daymet V4",
    "CMIP6 SSP Projections"
  ],
  "integrity_score": 100,
  "bias_correction": "Quantile Mapping (95th percentile fit)",
  "missing_value_rate": 0.2,
  "telemetry": {
    "energy_joules": 13.1,
    "carbon_gCO2e": 0.0054
  },
  "validation_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T13:45:00Z"
}
```

---

## ⚖️ FAIR+CARE Dataset Governance Matrix

| Principle | Implementation | Verification Source |
|------------|----------------|--------------------|
| **Findable** | STAC/DCAT 3.0 metadata and UUID assignment | `metadata/stac_catalog.json` |
| **Accessible** | Public FAIR+CARE release on GitHub + API | FAIR+CARE Ledger |
| **Interoperable** | NetCDF, GeoTIFF, CSV, JSON-LD formats | `telemetry_schema` |
| **Reusable** | Provenance and licensing metadata embedded | `manifest_ref` |
| **Collective Benefit** | Supports resilience and climate adaptation policy | FAIR+CARE Audit |
| **Responsibility** | Energy/carbon telemetry monitored via ISO 50001 | `telemetry_ref` |
| **Ethics** | Sensitive grid cells generalized at county scale | FAIR+CARE Council Review |

---

## 🧾 Governance Ledger Record Example

```json
{
  "ledger_id": "climatology-datasets-ledger-2025-11-09-0021",
  "component": "Climatology Datasets Registry",
  "datasets": [
    "NOAA GHCN-Daily",
    "PRISM Monthly",
    "Daymet V4",
    "CMIP6 Projections"
  ],
  "energy_joules": 13.1,
  "carbon_gCO2e": 0.0054,
  "faircare_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T13:47:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.2.2 | 2025-11-09 | FAIR+CARE Council | Published climatology dataset registry with FAIR+CARE and STAC/DCAT 3.0 metadata. |
| v10.2.1 | 2025-11-09 | KFM Climate Analysis Team | Added bias-correction, quality control, and telemetry schema integration. |
| v10.2.0 | 2025-11-09 | Data Governance Group | Created initial climatology dataset documentation aligned with hydrology standards. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Climatology Overview](../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

