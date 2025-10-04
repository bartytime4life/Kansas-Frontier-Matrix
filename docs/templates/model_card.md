<div align="center">

# 🧮 Kansas Frontier Matrix — Model Card Template  
`docs/templates/model_card.md`

**Purpose:** Provide a **reproducible and transparent template** for documenting any analytical, predictive, or AI/ML model  
within the **Kansas Frontier Matrix (KFM)** — ensuring **traceability**, **accountability**, and **MCP-aligned reproducibility**  
for all scientific and computational models used in data analysis, forecasting, or decision support.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)

</div>

---

## 🧭 Model Metadata

| Field | Description |
|:------|:-------------|
| **Model ID** | Unique identifier (e.g., `MODEL-2025-001-CLIMATE`) |
| **Model Name** | Descriptive title |
| **Author(s)** | Developer(s) or team responsible |
| **Date Created** | YYYY-MM-DD |
| **Last Updated** | YYYY-MM-DD |
| **Version** | v1.0, v1.1, etc. |
| **Domain** | Terrain / Hydrology / Climate / Hazards / Landcover / Tabular / Text |
| **Status** | Development / Validated / Production / Deprecated |
| **Associated Experiment(s)** | `docs/templates/experiment.md` ID or link |
| **License** | CC-BY 4.0 (outputs), MIT (code), or other |
| **Source Repository / Script** | (e.g., `src/models/climate_trend_model.py`) |

---

## 🎯 Model Purpose

Describe what this model is designed to do and its intended application.

> Example:  
> *This model predicts drought severity across Kansas based on precipitation anomalies, temperature indices,  
> and historical hydrologic drought events.*

---

## 🧩 Model Overview

| Category | Description |
|:-----------|:-------------|
| **Type** | Statistical / Machine Learning / Simulation / Rule-based |
| **Algorithm / Framework** | (e.g., Random Forest, XGBoost, CNN, Linear Regression) |
| **Language / Library** | (Python / TensorFlow / Scikit-learn / R / SQL) |
| **Training Method** | (Supervised / Unsupervised / Hybrid / Simulation) |
| **Input Features** | (List variables or input data sources) |
| **Output Targets** | (Describe model outputs or predictions) |

---

## ⚙️ Data Inputs & Dependencies

### Input Datasets
List all datasets, metadata files, and provenance links used by the model.

| Dataset | Description | License | Location |
|:-----------|:-------------|:-----------|:-----------|
| `daymet_1980_2024.nc` | Daily climate data | Public Domain | `data/processed/climate/` |
| `usgs_streamflow_1900_2025.csv` | Historical streamflow records | USGS | `data/processed/hydrology/` |

### Data Provenance
Each dataset must have a corresponding:
- **Source Manifest:** `data/sources/<domain>/*.json`  
- **Checksum:** `data/checksums/<domain>/*.sha256`  
- **STAC Metadata:** `data/stac/<domain>/*.json`

---

## 🧮 Model Architecture

Describe model structure, layers, or key computational components.

```text
Input Data (Climate Variables)
     ↓
Feature Engineering (Normalization, Aggregation)
     ↓
Model Core (Random Forest with 200 trees)
     ↓
Output (Predicted Drought Severity Index)
````

> If applicable, include architecture diagrams in `docs/architecture/diagrams/exported/`.

---

## 🧠 Training Configuration

| Parameter            | Value                               | Description                          |
| :------------------- | :---------------------------------- | :----------------------------------- |
| **Training Period**  | (e.g., 1980–2020)                   | Historical data range                |
| **Test Period**      | (e.g., 2021–2024)                   | Validation data range                |
| **Data Split Ratio** | (e.g., 80% train / 20% test)        | Proportion of data for model fitting |
| **Random Seed**      | (e.g., 42)                          | Ensures reproducibility              |
| **Hardware**         | (e.g., CPU / GPU type)              | Computational environment            |
| **Environment**      | (Python v3.11, Conda env `kfm_env`) | Execution environment                |

---

## 📊 Performance Metrics

Document the evaluation metrics and their values.

| Metric                 | Description                                     | Value       | Evaluation Method           |
| :--------------------- | :---------------------------------------------- | :---------- | :-------------------------- |
| **RMSE**               | Root Mean Square Error                          | 1.23        | Standard model evaluation   |
| **R²**                 | Coefficient of determination                    | 0.94        | Comparison to observed data |
| **Precision / Recall** | Classification accuracy (if applicable)         | 0.89 / 0.91 | Confusion matrix            |
| **AUC**                | Area under ROC curve (for classification tasks) | 0.92        | Scikit-learn                |
| **Checksum Match**     | Model binary and weights integrity              | ✅           | SHA-256                     |

---

## 🔍 Validation & Reproducibility

| Validation Type         | Description                           | Method                                          |
| :---------------------- | :------------------------------------ | :---------------------------------------------- |
| **Checksum Validation** | Ensure data/model integrity           | `make checksums`                                |
| **Cross-validation**    | Multi-fold evaluation                 | k=5 cross-validation                            |
| **STAC Consistency**    | Verify metadata matches input data    | `make stac-validate`                            |
| **CI/CD Validation**    | Automated testing workflow            | `.github/workflows/codeql.yml`, `checksums.yml` |
| **Peer Review**         | Independent verification by reviewers | GitHub PR or Issue discussion                   |

All validation logs should be stored in:

```
data/work/logs/models/<model_id>_validation.log
```

---

## 🧩 Limitations & Assumptions

Describe known constraints or model limitations.

> Example:
>
> * Model accuracy declines in years with missing precipitation data.
> * Does not account for anthropogenic factors (irrigation, dam management).
> * Temporal resolution limited to annual means.

---

## 🧠 Interpretability & Explainability

Provide interpretation aids for understanding model predictions.

| Feature               | Importance (%) | Explanation                          |
| :-------------------- | :------------- | :----------------------------------- |
| Precipitation Anomaly | 45             | Strongest predictor of drought index |
| Soil Moisture         | 30             | Secondary influence on persistence   |
| Temperature           | 15             | Contributes seasonal variability     |
| Vegetation Index      | 10             | Captures surface response            |

> Use `SHAP`, `LIME`, or feature importance plots when applicable.

---

## 🧾 Model Outputs

| Output Type       | Format          | Location                   | Description                   |
| :---------------- | :-------------- | :------------------------- | :---------------------------- |
| **Model Weights** | `.pkl` / `.h5`  | `models/<domain>/`         | Saved model binary            |
| **Predictions**   | `.csv` / `.tif` | `data/processed/<domain>/` | Model output data             |
| **Metadata**      | `.json`         | `data/stac/<domain>/`      | STAC-compliant metadata       |
| **Logs**          | `.log`          | `data/work/logs/models/`   | Execution and validation logs |

---

## 🔐 Ethical & Licensing Considerations

* Data follows **public domain or CC-BY 4.0** licenses.
* Model code released under **MIT License**.
* No personal, sensitive, or confidential data used.
* Attribution required for derivative works.
* Bias and fairness evaluations recommended for all predictive models.

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | Model documented prior to publication and release.               |
| **Reproducibility**     | Data, configuration, and parameters version-controlled.          |
| **Open Standards**      | STAC, JSON, CSV, and COG formats used for interoperability.      |
| **Provenance**          | Linked to dataset manifests, checksums, and STAC items.          |
| **Auditability**        | CI/CD logs and checksum verification ensure reproducible builds. |

---

## 📎 Related Documentation

| File                                   | Description                                            |
| :------------------------------------- | :----------------------------------------------------- |
| `docs/templates/experiment.md`         | Use alongside experiments for training and validation. |
| `docs/templates/sop.md`                | SOP for model deployment and validation.               |
| `docs/architecture/pipelines.md`       | Overview of model integration within ETL pipelines.    |
| `docs/architecture/knowledge-graph.md` | Semantic linkage of models to datasets and provenance. |
| `.github/workflows/codeql.yml`         | Workflow for security and code validation.             |

---

## 🧾 References

1. **STAC Specification v1.0.0** — [https://stacspec.org](https://stacspec.org)
2. **Master Coder Protocol (MCP)** — KFM Documentation Framework
3. **Model Cards for Model Reporting** — Google Research, 2019
4. **FAIR Principles** — Wilkinson et al., 2016 (Findable, Accessible, Interoperable, Reusable)

---

## 📅 Version History

| Version | Date       | Author                 | Summary                                                           |
| :------ | :--------- | :--------------------- | :---------------------------------------------------------------- |
| v1.0    | 2025-10-04 | KFM Documentation Team | Initial model card template for reproducible model documentation. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Model Transparent. Every Prediction Proven.”*
📍 [`docs/templates/model_card.md`](.) · Template for documenting analytical and predictive models under MCP standards.

</div>
