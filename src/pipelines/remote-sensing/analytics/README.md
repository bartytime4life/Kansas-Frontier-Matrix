---
title: "📊 Kansas Frontier Matrix — Remote Sensing Analytics Module (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/analytics/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-analytics-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📊 **Kansas Frontier Matrix — Remote Sensing Analytics Module**  
`src/pipelines/remote-sensing/analytics/README.md`

**Purpose:**  
Define the **analysis layer** for all KFM Remote Sensing pipelines.  
This module computes **vegetation indices**, **hazard layers**, **burn-scar + flood extents**, **thermal metrics**, **SAR-derived analytics**, **cloud-free composites**, and **multi-temporal summaries**, all under **FAIR+CARE governance**, **repeatable ETL**, and **MCP-DL v6.3** documentation-first rules.

<img alt="Analytics" src="https://img.shields.io/badge/Analytics-Indices_·_Hazards_·_SAR-green"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Deterministic" src="https://img.shields.io/badge/Deterministic-Yes-blue"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

Analytics are applied **after preprocessing** and before Neo4j/RDF publishing.

The Analytics Module supports:

- Spectral Indices (NDVI, NDMI, NDWI, SAVI, EVI, NBR)  
- SAR-Based Hazards (flood extent, water dynamics, backscatter anomalies)  
- Burn Severity (NBR2, dNBR, relative differencing)  
- Thermal Metrics (LST, emissivity-adjusted values)  
- Cloud-Free Composites (temporal mosaic over lookback windows)  
- Change Detection (pre/post differencing; multi-temporal trends)  
- Confidence Maps & Valid-Pixel QA  
- FAIR+CARE-sensitive masking (sovereignty zones, ecological sanctuaries)  
- Summary Statistics for Focus Mode (histograms, percentiles, anomaly flags)

All analytics must be:

- Deterministic  
- Reproducible  
- Schema-validated  
- FAIR+CARE-governed  
- Telemetry-instrumented  
- Graph- and RDF-ready  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/analytics/
├── README.md                     # This file
│
├── indices/                      # Vegetation/Spectral Index Algorithms
│   ├── ndvi.py
│   ├── ndmi.py
│   ├── ndwi.py
│   ├── savi.py
│   ├── evi.py
│   ├── nbr.py
│   ├── nbr2.py
│   └── utils.py
│
├── hazards/                      # SAR / Optical Hazard Layers
│   ├── flood_extent.py
│   ├── water_extent.py
│   ├── drought_index.py
│   ├── burn_scar.py
│   └── utils.py
│
├── thermal/                      # Thermal Infrared Analytics
│   ├── lst.py
│   ├── emissivity.py
│   └── utils.py
│
├── composites/                   # Cloud-Free Mosaics & Temporal Composites
│   ├── mosaic.py
│   ├── percentile.py
│   ├── temporal_stats.py
│   └── utils.py
│
├── change/                       # Multi-Temporal Change Detection
│   ├── differencing.py
│   ├── trend.py
│   └── utils.py
│
├── confidence/                   # Valid-Pixel + Confidence Layers
│   ├── qa_mask.py
│   ├── confidence_map.py
│   └── utils.py
│
└── schemas/
    ├── analytics.schema.json     # Master schema for analytics configurations
    ├── index.schema.json         # Per-index schema (NDVI/NDMI/etc.)
    ├── hazard.schema.json        # Flood, burn-scar, drought schemas
    ├── thermal.schema.json       # LST/emissivity schemas
    └── composite.schema.json     # Temporal mosaic schemas
~~~~~

---

## 🧩 Analytics Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Preprocessed Input<br/>cloud_mask · reprojection · harmonize_gsd"] --> B["Spectral Index Algorithms<br/>NDVI · NDMI · NDWI · SAVI · EVI · NBR"]
  A --> C["SAR Analytics<br/>flood_extent · water_dynamics"]
  A --> D["Thermal Analytics<br/>LST · emissivity"]
  A --> E["Composites<br/>mosaics · percentiles"]
  A --> F["Change Detection<br/>differencing · trends"]
  B --> G["Confidence Maps<br/>QA + valid-pixel"]
  C --> G
  D --> G
  E --> G
  F --> G
  G --> H["Telem. + Lineage<br/>metrics · energy · provenance"]
~~~~~

---

## 🍃 Spectral Index Analytics

Supported indices:

- **NDVI**: Vegetation vigor  
- **NDMI**: Moisture index  
- **NDWI**: Water detection  
- **SAVI**: Soil-adjusted vegetation  
- **EVI**: Enhanced vegetation  
- **NBR / NBR2**: Burn severity  

Each index module MUST:

- Use **sensor-correct band mappings**  
- Respect **harmonized GSD**  
- Apply **masking** (cloud, shadow, snow, CARE-sensitive)  
- Compute:
  - Index raster  
  - Percentile stats  
  - Distribution histograms  
  - Classification bins (if configured)  
- Emit telemetry:
  - `index_min`, `index_max`  
  - `pixels_valid`, `pixels_masked`  
  - `energy_wh`, `co2_g`  

---

## 🌊 SAR Hazard Analytics

Supported hazard layers:

- **Flood extent** (Sentinel-1 backscatter anomalies)  
- **Water persistence** (multi-temporal SAR)  
- **Drought index** (SAR+optical hybrid)  
- **Burn-scar detection** (optical + SAR fusion)  

Hazard modules MUST:

- Terrain-correct backscatter (RTC)  
- Apply speckle filters  
- Normalize sigma0 units  
- Apply adaptive thresholds (Otsu/Kittler/bespoke)  
- Respect CARE-masked AOIs  
- Emit telemetry on:
  - `pixels_water`, `pixels_dry`  
  - `speckle_reduced_pct`  
  - `rtc_duration_ms`  

---

## 🔥 Burn Severity Analytics

Burn-related analytics compute:

- NBR / NBR2  
- ΔNBR (pre/post differencing)  
- Classification (USFS severity bins)  
- Potential hazard zones  

Telemetry fields:

- `burn_area_km2`  
- `severity_class_counts`  
- `anomaly_flags`  

---

## 🌡 Thermal Analytics

Thermal modules provide:

- LST (Land Surface Temperature)  
- Emissivity corrections  
- Thermal anomaly detection  

Telemetry:

- `lst_min`, `lst_max`, `lst_quantiles`  
- `emissivity_applied`  

---

## 🧱 Cloud-Free Composites

Composites built over `P7D`, `P14D`, `P30D` windows:

- Mean, median  
- Percentiles  
- Max-Green, Min-SWIR composites  
- Cloud-probability weighted composites  

Telemetry:

- `composite_window_days`  
- `pixels_contributed`  

---

## 🔁 Change Detection

Change modules compute:

- Pre/post differencing  
- Multi-temporal trends  
- Alert regions (sharp change)  

Outputs include:

- Change magnitude raster  
- Trend slope layer  
- Valid-pixel masks  
- Telemetry summaries  

---

## 🛡 FAIR+CARE Enforcement

The Analytics Module MUST:

- Respect `care_label` from config  
- Mask sensitive AOIs using H3 generalization  
- Suppress or anonymize output in sovereignty areas  
- Log:
  - `care_violations`  
  - `masking_applied`  
  - `sovereignty_flags`  

Governance ledger updated via:

~~~~~text
../../../../../docs/reports/audit/data_provenance_ledger.json
~~~~~

---

## 📡 Telemetry Integration

Analytics write NDJSON telemetry:

~~~~~text
data/processed/telemetry/<analytics-pipeline>.ndjson
~~~~~

Telemetry fields include:

- `stage`  
- `duration_ms`  
- `pixels_processed`  
- `pixels_valid`  
- `pixels_masked`  
- `energy_wh`, `co2_g`  
- `care_violations`  
- `index_min`, `index_max`  

Aggregated to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Testing Requirements

All analytics modules MUST include tests for:

- Index correctness (known-scene golden outputs)  
- Valid-pixel logic  
- CARE masking  
- SAR normalization & RTC correctness  
- Telemetry metrics  
- Schema validation (analytics.schema.json)  

CI enforcement:

- `codeql.yml`  
- `trivy.yml`  
- `telemetry-export.yml`  
- `faircare-validate.yml`  
- `docs-lint.yml`  

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Introduced full Remote Sensing Analytics Suite: indices, hazards, SAR, composites, thermal, change detection, telemetry, governance. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Analytics Layer**  
Scientific Analytics × FAIR+CARE Ethics × Provenance × Deterministic Remote Sensing  
© 2025 Kansas Frontier Matrix — MIT License  

</div>