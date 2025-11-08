```
---
title: "🧭 KFM — Predictive Archaeology (Soil Moisture × Elevation × Paleo‑Hydrology)"
path: "src/ai/models/archaeology/predictive-zones/README.md"
version: "v9.7.0"
last_updated: "2025-11-08"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v9.7.0/sbom.spdx.json"
manifest_ref: "releases/v9.7.0/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/ai-archaeology-v1.json"
governance_ref: "docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
tags: ["archaeology", "geospatial-ml", "soil-moisture", "paleo-hydrology", "DEM", "Kansas"]
---

<div align="center">

# 🧭 **Predictive Archaeology: Data → Discovery**
`src/ai/models/archaeology/predictive-zones/README.md`

**Purpose:** A small, reproducible pipeline that combines **soil moisture indices**, **elevation/terrain metrics**, and **proximity to historical waterways** to predict **likely undiscovered archaeological zones** in Kansas.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/README.md)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-orange)](../../../../docs/standards/FAIR-CARE.md)
[![Status](https://img.shields.io/badge/Status-Experimental-brightgreen)](#)

</div>

---

## 📘 Overview

This model estimates locations where past human activity is plausible by fusing:
- **Soil moisture** (static indices from multispectral composites or temporal means; wetter micro‑basins often preserve organic material and correlate with settlement/fields).
- **Elevation & terrain** (DEM‑derived slope, aspect, curvature, Topographic Position Index (TPI), and multi‑scale roughness to capture ridge/terrace/valley forms).
- **Proximity to paleo‑water** (distance‑to reconstructed channels, springs, oxbows, and terrace edges; water access is a first‑order driver of siting).

Outputs:
- **Raster**: per‑pixel likelihood (0–1).
- **Vector**: high‑likelihood polygons with confidence bands and governance metadata.

Ethics & governance:
- Mask **sacred/known sites**; generalize coordinates; apply **CARE** principles and consultation workflows before publication.

---

## 🗂️ Directory Layout

```

src/ai/models/archaeology/predictive-zones/
data/                  # staging pointers to STAC items (DEM, water layers, indices)
notebooks/             # EDA and SHAP summaries
pipeline/              # code: features, train, predict, postprocess
configs/               # YAML: data sources, CRS, thresholds, masks
artifacts/             # trained models, metrics, SHAP, confusion matrices
outputs/               # rasters (GeoTIFF/COG), vectors (GeoJSON), tiles (PMTiles)
governance/            # approvals, redaction logs, stakeholder notes
README.md

````

---

## 🧩 Data Inputs (STAC/DCAT)

| Layer | Example ID | CRS | Resolution | Notes |
|---|---|---|---|---|
| DEM | `usgs-dem-10m` | EPSG:5070 | 10–30 m | For slope/aspect/TPI/curvature |
| Moisture Index | `landsat-smi-annual-2013-2024` | EPSG:5070 | 30 m | e.g., NDMI/NDWI composites & seasonal stats |
| Hydro (modern) | `nhd-highres` | EPSG:5070 | — | Seed for paleo reconstruction |
| Paleo‑Hydro | `kfm-paleo-channels-v1` | EPSG:5070 | — | Derived from DEM + archival maps |
| Known Sites (masked) | `khs-sites-redacted` | EPSG:5070 | — | **Access‑controlled**; never published raw |

---

## ⚙️ Feature Engineering

- **Terrain**: slope, aspect (sin/cos), plan/profile curvature, TPI (r=250/500/1000 m), roughness, relative elevation to nearest channel.
- **Moisture**: NDMI/NDWI percentiles (P10/P50/P90), seasonal mean/variance, dry‑spell length.
- **Hydro Proximity**: distance to paleo‑channel centerline, floodplain membership, terrace class.
- **Accessibility**: least‑cost path to water (terrain‑weighted).
- **Confounders**: distance to modern disturbance (roads/centers) for masking only.

Normalization: robust scaling by eco‑region.  
Balancing: stratified sampling with **spatial block CV** (avoid leakage).

---

## 🧠 Model

- **Primary**: Gradient Boosted Trees (e.g., XGBoost/LightGBM) with class weights.
- **Baselines**: Logistic Regression (interpretable), Random Forest (variance check).
- **CV**: 5‑fold spatial block; AUROC, AUPRC, Brier, calibration curve.
- **Explainability**: SHAP global (top features) + SHAP value maps.

---

## 🧾 Minimal Config (YAML)

```yaml
# configs/predictive-zones.kansas.yml
crs: "EPSG:5070"
cell_size: 30
blocks:
  size_m: 5000
stac:
  dem: "stac://usgs-dem-10m"
  indices: "stac://landsat-smi-annual-2013-2024"
  hydro_modern: "stac://nhd-highres"
  paleo_hydro: "stac://kfm-paleo-channels-v1"
  sites_masked: "stac+secure://khs-sites-redacted"
features:
  terrain: [slope, aspect_sin, aspect_cos, curvature_plan, curvature_profile, tpi_250, tpi_500, tpi_1000, roughness]
  moisture: [ndmi_p10, ndmi_p50, ndmi_p90, ndwi_seasonal_mean, ndwi_seasonal_var, dryspell_len]
  hydro: [dist_paleo_channel_m, floodplain_flag, terrace_class, rel_elev_to_channel_m]
model:
  type: "xgboost"
  params:
    max_depth: 6
    n_estimators: 600
    learning_rate: 0.05
    subsample: 0.8
    colsample_bytree: 0.8
thresholds:
  publish_high: 0.80
  publish_medium: 0.60
redaction:
  generalize_cell_m: 250
  dissolve_min_area_m2: 20000
outputs:
  raster_coG: "outputs/predictive_zones_prob_cog.tif"
  vector_geojson: "outputs/predictive_zones_high.geojson"
````

---

## 🛠️ Pipeline (pseudo‑code)

```python
# pipeline/train_predict.py
cfg = load_cfg("configs/predictive-zones.kansas.yml")
stack = build_feature_stack(cfg)                 # DEM→terrain, indices→moisture, paleo→distances
X, y, blocks = sample_training_points(stack, cfg) # y from masked known sites; negatives from matched terrain strata
cv = SpatialBlockCV(blocks, n_splits=5)
model = XGBClassifier(**cfg.model.params)
metrics = cross_validate(model, X, y, cv=cv, scoring=["roc_auc","average_precision","brier"])
model.fit(X, y)
save_artifacts(model, metrics, "artifacts/")
proba = predict_raster(model, stack)             # apply to full grid
cog = write_cog(proba, cfg.outputs.raster_coG, cfg.crs)
hi = vectorize_threshold(proba, cfg.thresholds.publish_high)
hi = redact_and_generalize(hi, cfg.redaction)
hi.to_file(cfg.outputs.vector_geojson)
```

---

## 🧪 Validation & Explainability

| Metric            | Target | Notes                       |
| ----------------- | ------ | --------------------------- |
| AUROC             | ≥ 0.80 | Spatial CV                  |
| AUPRC             | ≥ 0.35 | Class‑imbalance aware       |
| Brier             | ≤ 0.18 | Calibration                 |
| ECE (calibration) | ≤ 0.05 | Post‑hoc isotonic if needed |

Artifacts:

* `artifacts/shap_global.csv` (feature importance)
* `artifacts/calibration_curve.png`
* `artifacts/confusion_matrix_blocked.png`

---

## ♿ FAIR+CARE & Publishing Rules

* **Do not** release precise coordinates; buffer & generalize polygons.
* Obtain approvals recorded in `governance/approvals.md`.
* Include provenance chain (STAC links, processing logs, checksums).
* Provide community context notes: local knowledge, oral histories, sensitivities.

---

## 🔌 Integration Points (KFM)

* **Graph**: attach polygons as `ArchaeologyZone` nodes with edges to feature provenance (DEM/indices/paleo layers).
* **Web (MapLibre)**: render probability tiles (PMTiles) with a discrete legend: Low/Med/High.
* **API**: `/api/archaeology/predictive-zones?bbox=&threshold=0.8`
* **Telemetry**: log model hash, data hashes, and redaction parameters.

---

## 🕰️ Version History

| Version | Date       | Author | Summary                                                          |
| ------- | ---------- | ------ | ---------------------------------------------------------------- |
| v9.7.0  | 2025-11-08 | KFM AI | Initial predictive archaeology pipeline spec and minimal config. |

---

<div align="center">

© Kansas Frontier Matrix — Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified
[Back to AI Models](../../README.md) · [Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
```
