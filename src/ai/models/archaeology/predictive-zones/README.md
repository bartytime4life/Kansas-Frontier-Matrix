---
title: "🧭 Kansas Frontier Matrix — Predictive Archaeology (Soil Moisture × Elevation × Paleo-Hydrology · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/ai/models/archaeology/predictive-zones/README.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.9.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/src-ai-models-archaeology-predictivezones-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
tags: ["archaeology", "geospatial-ml", "soil-moisture", "paleo-hydrology", "DEM", "Kansas"]
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — Predictive Archaeology: Data → Discovery**
`src/ai/models/archaeology/predictive-zones/README.md`

**Purpose:**  
Reproducible FAIR+CARE-governed machine learning pipeline that fuses **soil moisture**, **elevation**, and **paleo-hydrology** data to estimate the **probability of undiscovered archaeological zones** in Kansas.  
Implements ISO-aligned sustainability telemetry and transparent governance workflows under **MCP-DL v6.3**.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../docs/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governed-orange)](../../../../docs/standards/faircare.md)
[![Status](https://img.shields.io/badge/Status-Operational-brightgreen)](#)

</div>

---

## 📘 Overview

This model predicts plausible ancient settlement or activity areas through the integration of three data domains:

- **Soil Moisture** — NDMI/NDWI indices and seasonal composites that reflect preserved organic matter and field systems.  
- **Elevation & Terrain** — Multi-scale DEM derivatives (slope, aspect, curvature, roughness, TPI) identifying terraces, ridges, and valley systems.  
- **Paleo-Hydrology** — Distances to reconstructed streams, oxbows, and terrace margins based on DEM and archival hydrography.

**Outputs**
- 🗺️ Raster: per-pixel probability (0–1).  
- 🧭 Vector: thresholded high-probability zones with FAIR+CARE governance metadata.  

**Ethics**
- Redact or generalize sensitive coordinates.  
- Mask sacred and culturally sensitive zones via **CARE Tag enforcement**.

---

## 🗂️ Directory Layout

```plaintext
src/ai/models/archaeology/predictive-zones/
├── data/                # STAC pointers to DEM, hydrography, and spectral indices
├── notebooks/           # EDA, model validation, SHAP explainability
├── pipeline/            # ETL, training, inference, and validation scripts
├── configs/             # YAML configs defining CRS, thresholds, redaction rules
├── artifacts/           # Trained models, metrics, explainability, and governance
├── outputs/             # GeoTIFF, GeoJSON, PMTiles, visualization layers
├── governance/          # Reviews, approvals, and cultural consultation records
└── README.md
```

---

## 🧩 Data Inputs (STAC/DCAT)

| Layer | Example ID | CRS | Resolution | Notes |
|-------|-------------|-----|-------------|-------|
| DEM | `usgs-dem-10m` | EPSG:5070 | 10–30 m | Slope, aspect, curvature, TPI |
| Moisture Index | `landsat-smi-annual-2013-2024` | EPSG:5070 | 30 m | NDMI/NDWI composites |
| Hydro (modern) | `nhd-highres` | EPSG:5070 | — | Seed for paleo reconstruction |
| Paleo-Hydro | `kfm-paleo-channels-v1` | EPSG:5070 | — | Derived from DEM + archival maps |
| Known Sites (masked) | `khs-sites-redacted` | EPSG:5070 | — | **Restricted under CARE** |

---

## ⚙️ Feature Engineering

**Derived Variables**

| Group | Features |
|--------|-----------|
| Terrain | slope, aspect_sin, aspect_cos, curvature_plan/profile, TPI (250–1000 m), roughness |
| Moisture | NDMI/NDWI percentiles (P10/P50/P90), seasonal mean/variance, dryspell length |
| Hydrography | distance to paleo-channel, floodplain flag, terrace class, relative elevation to channel |
| Accessibility | terrain-weighted least-cost distance to paleo-water |
| Confounders | modern disturbance distances (roads, urban centers) |

All variables normalized by eco-region. Stratified sampling ensures spatial CV independence.

---

## 🧠 Model Design

| Component | Specification |
|------------|----------------|
| Framework | XGBoost / LightGBM (Gradient-Boosted Trees) |
| Baselines | Logistic Regression, Random Forest |
| Validation | 5-fold spatial block CV |
| Metrics | AUROC, AUPRC, Brier, calibration error |
| Explainability | SHAP global + local feature maps |
| Governance | FAIR+CARE validation and telemetry export integrated |

---

## 🧾 Minimal Configuration Example

```yaml
# configs/predictive-zones.kansas.yml
crs: "EPSG:5070"
cell_size: 30
stac:
  dem: "stac://usgs-dem-10m"
  moisture: "stac://landsat-smi-annual-2013-2024"
  paleo_hydro: "stac://kfm-paleo-channels-v1"
  sites_masked: "stac+secure://khs-sites-redacted"
features:
  terrain: [slope, aspect_sin, aspect_cos, tpi_250, tpi_500, tpi_1000, roughness]
  moisture: [ndmi_p50, ndwi_var, dryspell_len]
  hydro: [dist_paleo_channel_m, floodplain_flag, rel_elev_to_channel_m]
model:
  type: "xgboost"
  params:
    max_depth: 6
    n_estimators: 600
    learning_rate: 0.05
thresholds:
  publish_high: 0.8
redaction:
  generalize_cell_m: 250
outputs:
  raster_cog: "outputs/maps/predictive_zones_prob_cog.tif"
  vector_geojson: "outputs/maps/predictive_zones_high.geojson"
```

---

## 🧮 Pipeline Summary

```python
# pipeline/train_predict.py
cfg = load_cfg("configs/predictive-zones.kansas.yml")
stack = build_feature_stack(cfg)
X, y, blocks = sample_training_points(stack, cfg)
cv = SpatialBlockCV(blocks, n_splits=5)
model = XGBClassifier(**cfg.model.params)
metrics = cross_validate(model, X, y, cv=cv, scoring=["roc_auc","average_precision","brier"])
model.fit(X, y)
save_artifacts(model, metrics, "artifacts/")
proba = predict_raster(model, stack)
cog = write_cog(proba, cfg.outputs.raster_cog, cfg.crs)
hi = vectorize_threshold(proba, cfg.thresholds.publish_high)
hi = redact_and_generalize(hi, cfg.redaction)
hi.to_file(cfg.outputs.vector_geojson)
```

---

## 🧪 Validation & Explainability

| Metric | Target | Notes |
|--------|--------|-------|
| AUROC | ≥ 0.80 | Spatial CV mean |
| AUPRC | ≥ 0.35 | Handles imbalance |
| Brier | ≤ 0.18 | Calibration quality |
| ECE | ≤ 0.05 | Post-hoc isotonic calibration if required |

Artifacts:  
- `artifacts/shap_global.csv` — feature importances  
- `artifacts/calibration_curve.png`  
- `artifacts/confusion_matrix_blocked.png`

---

## ♿ FAIR+CARE & Publication Protocols

- No release of raw or precise coordinates.  
- Polygons generalized and buffered ≥ 250 m.  
- All outputs require FAIR+CARE Council approval recorded in `governance/governance_validation.json`.  
- Include provenance, checksums, and consultation summaries.  
- Community notes document oral histories or cultural sensitivities.

---

## 🔗 Integration in KFM Ecosystem

| System | Integration |
|--------|-------------|
| **Knowledge Graph** | ArchaeologyZone nodes linked to DEM, NDMI, paleo-hydrology entities. |
| **Web (MapLibre)** | Probability tiles rendered with categorical legend (Low / Medium / High). |
| **API** | `/api/archaeology/predictive-zones?bbox=&threshold=0.8` |
| **Telemetry** | Logs model hash, data checksums, redaction masks, and energy metrics. |

---

## 🧾 Citation

```text
Kansas Frontier Matrix (2025). Predictive Archaeology (Soil Moisture × Elevation × Paleo-Hydrology) v9.9.0.
FAIR+CARE and ISO-compliant predictive model integrating terrain, moisture, and paleo-hydrological data to identify plausible archaeological landscapes in Kansas.
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------:|------|--------|----------|
| v9.9.0 | 2025-11-08 | `@kfm-ai` | Upgraded model pipeline with telemetry, FAIR+CARE governance, and reproducibility enhancements. |
| v9.7.0 | 2025-11-06 | `@kfm-ai` | Initial predictive archaeology pipeline specification. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Predictive Heritage Science × FAIR+CARE Ethics × Sustainable AI Discovery*  
© 2025 Kansas Frontier Matrix · MIT · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to AI Models Index](../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
