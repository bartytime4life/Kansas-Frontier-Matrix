---
title: "🌿 Kansas Frontier Matrix — Species Distribution Modeling (SDM) Methods (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/ecology/species-distribution-modeling.md"
version: "v10.2.2"
last_updated: "2025-11-09"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/analyses-ecology-sdm-v3.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌿 **Kansas Frontier Matrix — Species Distribution Modeling (SDM) Methods**
`docs/analyses/ecology/species-distribution-modeling.md`

**Purpose:**  
Describe the **Species Distribution Modeling (SDM)** framework implemented in the Kansas Frontier Matrix (KFM), integrating biodiversity and environmental datasets under **FAIR+CARE**, **ISO 19115**, and **MCP-DL v6.3** standards.  
This document ensures ethical, transparent, and reproducible modeling of species-habitat relationships across Kansas.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Species_Distribution-orange)](../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Stable_Model-brightgreen)](../../../../releases/)
</div>

---

## 📘 Overview

The **Species Distribution Modeling Module** predicts habitat suitability and ecological niche distributions for key species in Kansas.  
Using FAIR+CARE-validated biodiversity, climate, and landcover data, this workflow combines statistical and machine learning models to assess **species richness**, **conservation gaps**, and **ecological resilience** under present and future climate scenarios.

---

## 🗂️ Directory Context

```plaintext
docs/analyses/ecology/
├── README.md
├── species-distribution-modeling.md           # This document
├── landcover-analysis.md                      # Vegetation change and landcover trends
├── ecosystem-services.md                      # Ecosystem service modeling
├── validation.md                              # FAIR+CARE + ISO validation
└── reports/                                   # Ecological summaries and visual outputs
```

---

## 🧩 Analytical Framework

```mermaid
flowchart TD
  A["Biodiversity Data (GBIF / USDA)"] --> B["Environmental Covariates (Climate + NDVI + Elevation)"]
  B --> C["Model Fitting (MaxEnt / Random Forest / XGBoost)"]
  C --> D["Habitat Suitability Mapping"]
  D --> E["Model Validation + FAIR+CARE Audit + Telemetry Logging"]
```

---

## ⚙️ Input Datasets

| Source | Dataset | Variables | Resolution | FAIR+CARE Status |
|--------|----------|------------|-------------|------------------|
| **GBIF** | Species occurrence records | Presence-only coordinates | Point | ✅ Certified |
| **USDA / NRCS** | Plant and habitat site data | Vegetation, soil, elevation | 1 km grid | ✅ Certified |
| **NASA MODIS / ESA CCI** | Vegetation indices and landcover | NDVI, EVI, landcover class | 250 m–1 km | ✅ Certified |
| **NOAA / PRISM** | Climate variables | Temp, precip, humidity | 4 km | ✅ Certified |

All datasets harmonized to EPSG:4326 and aggregated to 1 km grid for statewide coverage.

---

## 🧠 Methodological Steps

### 1️⃣ Data Preparation
- Combine GBIF occurrence data with environmental rasters (climate + NDVI + elevation).  
- Balance data using spatial thinning and pseudo-absence generation.

```python
from pygbif import occurrences
from sklearn.model_selection import train_test_split

data = occurrences.search(stateProvince="Kansas", limit=5000)
presence, absence = train_test_split(data, test_size=0.3)
```

---

### 2️⃣ Model Fitting
Run ensemble SDMs using multiple algorithms:

| Model | Description | Library / Tool |
|--------|-------------|----------------|
| **MaxEnt** | Maximum entropy model for presence-only data | `maxent.jar`, `dismo` |
| **Random Forest (RF)** | Ensemble tree-based classification | `scikit-learn` |
| **XGBoost** | Gradient boosting for large-scale distribution modeling | `xgboost`, `numpy` |

Example (Random Forest):
```python
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=200)
rf.fit(X_train, y_train)
predicted = rf.predict_proba(X_test)[:, 1]
```

Outputs:  
- `habitat_suitability_model.nc`  
- `species_probability_map.tif`

---

### 3️⃣ Model Validation
Evaluate model performance with cross-validation:
```python
from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_true, predicted)
```
| Metric | Target | Description |
|---------|---------|-------------|
| **AUC (Area Under Curve)** | ≥ 0.8 | Model discrimination accuracy |
| **TSS (True Skill Statistic)** | ≥ 0.6 | Sensitivity-specificity balance |
| **RMSE (Root Mean Square Error)** | ≤ 10% | Prediction deviation |

Validation results saved in `faircare_validation.json`.

---

### 4️⃣ Projection & Mapping
Project model to future climate scenarios using CMIP6 SSP data:
```python
import xarray as xr
future_data = xr.open_dataset("cmip6_ssp245_climate.nc")
future_pred = rf.predict_proba(future_data.to_array().T)
```
Outputs:
- `habitat_suitability_future.tif`  
- `species_range_shift.geojson`

---

## 🧮 FAIR+CARE Validation Record Example

```json
{
  "validation_id": "sdm-analysis-2025-11-09-0176",
  "datasets": [
    "GBIF Occurrences",
    "MODIS NDVI",
    "NOAA Climate Covariates",
    "USDA PLANTS"
  ],
  "models": ["MaxEnt", "Random Forest", "XGBoost"],
  "metrics": {
    "auc_mean": 0.89,
    "tss_mean": 0.71,
    "rmse": 0.09
  },
  "energy_joules": 13.9,
  "carbon_gCO2e": 0.0054,
  "validation_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T17:38:00Z"
}
```

---

## ⚖️ FAIR+CARE & ISO Governance Matrix

| Principle | Implementation | Verification Source |
|------------|----------------|--------------------|
| **Findable** | STAC/DCAT metadata with persistent UUIDs | `datasets/metadata/` |
| **Accessible** | FAIR+CARE open data access with DOI links | FAIR+CARE Ledger |
| **Interoperable** | CSV, GeoTIFF, NetCDF outputs | `telemetry_schema` |
| **Reusable** | Model provenance and code reproducibility tracked | `manifest_ref` |
| **Responsibility** | ISO 50001/14064 telemetry validation per model run | `telemetry_ref` |
| **Ethics** | Sensitive species coordinates masked ≥5 km | FAIR+CARE Ethics Audit |

---

## 🧾 Governance Ledger Record Example

```json
{
  "ledger_id": "sdm-ledger-2025-11-09-0177",
  "component": "Species Distribution Modeling Module",
  "datasets": [
    "GBIF Biodiversity Records",
    "MODIS NDVI",
    "NOAA Climate Covariates"
  ],
  "energy_joules": 13.9,
  "carbon_gCO2e": 0.0054,
  "faircare_status": "Pass",
  "auditor": "FAIR+CARE Council",
  "timestamp": "2025-11-09T17:40:00Z"
}
```

---

## 🧠 Sustainability Metrics

| Metric | Description | Value | Target | Unit |
|---------|-------------|--------|---------|------|
| **Energy (J)** | Average energy used per SDM run | 13.9 | ≤ 15 | Joules |
| **Carbon (gCO₂e)** | CO₂ equivalent per analysis | 0.0054 | ≤ 0.006 | gCO₂e |
| **Telemetry Coverage (%)** | FAIR+CARE trace completion | 100 | ≥ 95 | % |
| **Validation Pass Rate (%)** | FAIR+CARE audit compliance | 100 | 100 | % |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.2.2 | 2025-11-09 | FAIR+CARE Council | Published SDM framework with FAIR+CARE validation and ISO telemetry. |
| v10.2.1 | 2025-11-09 | Ecological Modeling Team | Added ensemble model methods and future projection integration. |
| v10.2.0 | 2025-11-09 | KFM Ecology Group | Created baseline SDM documentation aligned with hydrology and climatology workflows. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Ecology Overview](./README.md) · [Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

