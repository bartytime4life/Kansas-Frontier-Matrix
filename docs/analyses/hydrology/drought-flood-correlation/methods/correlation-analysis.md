---
title: "💧 Kansas Frontier Matrix — Drought–Flood Correlation Analysis Methods (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/hydrology/drought-flood-correlation/methods/correlation-analysis.md"
version: "v10.1.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.1.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.1.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.1.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/analyses-hydrology-methods-v2.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Drought–Flood Correlation Analysis Methods**
`docs/analyses/hydrology/drought-flood-correlation/methods/correlation-analysis.md`

**Purpose:**  
Document advanced methods for correlating drought and flood events across Kansas using time-series, spatial, and machine learning approaches integrated within the Kansas Frontier Matrix (KFM) hydrology analysis pipeline.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)](../../../../../docs/standards/faircare.md)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen)]()

</div>

---

## 📘 Overview

This module defines the scientific and computational framework for detecting, quantifying, and visualizing relationships between drought and flood conditions in Kansas watersheds.  
It combines hydrologic indices (SPI, SPEI, PDSI) with river discharge, precipitation, and soil-moisture data, building on the **Hydrology ETL pipeline** described in `src/pipelines/etl/hydrology/`.  

Correlation methods operate over spatially explicit time-series from NOAA, USGS, and NASA datasets to uncover lagged and compound relationships between extreme dry and wet events.

---

## 🗂️ Directory Layout
```
docs/
 └─ analyses/
     └─ hydrology/
         └─ drought-flood-correlation/
             └─ methods/
                 ├─ correlation-analysis.md     # This document
                 ├─ visualizations/             # Report figures, charts
                 ├─ data/                       # Reference CSV/NetCDF subsets
                 └─ notebooks/                  # Reproducible Jupyter workflows
```

---

## ⚙️ Methodological Framework

### 1. Data Sources
| Dataset | Variables | Resolution | Notes |
|----------|------------|-------------|-------|
| NOAA NCEI GHCN-Daily | Precipitation (P), Tmin/Tmax | Daily / Station | 1880 – present – used for SPI calculation |
| USGS NWIS Streamflow | Discharge (Q) | Daily / Gage | For peak flow and baseflow analysis |
| NASA Daymet V4 | P, Tmean, Vapor Pressure | 1 km grid 1980 – present | Spatially continuous inputs for SPEI |
| NOAA Climate Normals 1991–2020 | Baseline means | Monthly / Station | Used for standardization |

---

### 2. Hydrologic Indices Calculation

1. **Standardized Precipitation Index (SPI)**  
   Computed at 1-, 3-, 6-, and 12-month scales using Gamma-fit precipitation distributions.

2. **Standardized Precipitation-Evapotranspiration Index (SPEI)**  
   Derived from precipitation and potential evapotranspiration (PET ≈ Thornthwaite) for moisture balance anomalies.

3. **Palmer Drought Severity Index (PDSI)**  
   Monthly drought severity from CPC archives for verification and trend comparison.

4. **Flood Metrics**  
   - Annual Maximum Daily Flow (AMDF)  
   - Peak Over Threshold (POT) events (e.g., >95th percentile Q)  
   - Flood Duration and Volume from hydrograph integration.

Each index is temporally aligned to water-year calendars (Oct–Sep) and spatially resampled to HUC-8 basins.

---

### 3. Correlation Techniques

| Method | Description | Implementation |
|---------|--------------|----------------|
| **Pearson / Spearman Rank Correlation** | Baseline linear & monotonic correlation between drought and flood severity series per basin. | `scipy.stats` |
| **Cross-Correlation Function (CCF)** | Detects lagged relationships (e.g., drought preceding flood after n months). | `statsmodels.tsa.stattools.ccf` |
| **Mutual Information (MI)** | Nonlinear dependency measure for non-Gaussian series. | `sklearn.feature_selection.mutual_info_regression` |
| **Copula Analysis** | Joint probability modeling of extremes (drought index vs streamflow). | `copulas` library / custom MLE fits |
| **Wavelet Coherence** | Time–frequency co-variability using Morlet wavelets. | `pycwt` / `wavelets` |
| **Dynamic Bayesian Networks** | Causal directionality between indices (PDSI → Flood Frequency). | `pgmpy`, Neo4j temporal edges for graph storage |

Each technique logs metadata and provenance for reproducibility under MCP 2.0 standards.

---

### 4. Graph Integration Workflow

1. **ETL Output → GraphDB**  
   ```mermaid
   flowchart TD
     A[Raw Hydrologic Series] --> B[ETL Transform (Indices, Peaks)]
     B --> C[(Neo4j Graph)]
     C -->|:CORRELATES_WITH| D[(Basin Nodes)]
     C -->|:LEADS_TO (lag→n months)| D
   ```
2. Correlation results are stored as relationships:  
   - `(:DroughtIndex)-[:CORRELATES_WITH {r, p, method, lag}]→(:FloodEvent)`  
   - Indexed in Neo4j for query via `MATCH (d)-[r:CORRELATES_WITH]->(f) RETURN …`

3. Outputs are also serialized as GeoJSON + STAC Items under `data/processed/hydrology/correlation/`.

---

### 5. Visualization & Reporting

Interactive and static visualizations are produced via **Matplotlib**, **Plotly**, and **MapLibre layers**.

| Visualization | Description |
|---------------|-------------|
| Time-Series Panels | SPI/SPEI vs Peak Flow with lag overlay |
| Scatter Heatmaps | Drought vs Flood index density per basin |
| Spatial Correlation Map | GeoTIFF grid of correlation coefficients (r) |
| Wavelet Coherence Spectra | Power and phase arrows (lead/lag zones) |
| Interactive Dashboard | Integrated MapLibre + D3 timeline through KFM UI under `/hydrology` |

---

## 🧩 FAIR+CARE Alignment

| Principle | Implementation |
|------------|----------------|
| **Findable** | All correlation products indexed in STAC/DCAT catalogs with DOIs & UUIDs. |
| **Accessible** | Served via KFM API and Open STAC endpoints. |
| **Interoperable** | Uses GeoJSON, NetCDF, and CSV open formats with DCAT 3.0 metadata. |
| **Reusable** | Provenance captured in Neo4j and JSON-LD lineage. |
| **CARE Ethics** | Transparent AI methods and stakeholder review by FAIR+CARE Council. |

---

## 🧾 Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.1.0 | 2025-11-09 | A. Barta / FAIR+CARE Council | Initial publication of correlation methods aligned with KFM v10 architecture. |
| v9.7.0 | 2025-09-22 | KFM Hydrology Team | Prototype correlation workflow and ETL integration. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Hydrology Analyses](../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

