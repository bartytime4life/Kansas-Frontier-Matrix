---
title: "KFM Web Sample — Analytics · Regression"
path: "web/assets/samples/analytics/regression/README.md"
version: "v0.1.0"
last_updated: "2026-01-18"
status: "draft"
doc_kind: "Sample"
license: "TBD"

# Profile / protocol versions (project tooling may validate these)
markdown_protocol_version: "1.0"
pipeline_contract_version: "v13"

# Governance & ethics hooks (keep even if TBD; tooling may expect these fields)
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
fair_category: "FAIR+CARE"
care_label: "Public · Synthetic Fixture"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

# Integrity / traceability (fill during commit/release)
doc_uuid: "urn:kfm:doc:web:samples:analytics:regression:v0.1.0"
commit_sha: "<commit-hash>"
doc_integrity_checksum: "sha256:<to-be-filled>"
---

# 📈 Regression (Analytics Sample)

![Sample](https://img.shields.io/badge/sample-analytics%2Fregression-blue)
![KFM](https://img.shields.io/badge/KFM-contract--first%20%26%20evidence--first-5b2cff)
![Status](https://img.shields.io/badge/status-draft-orange)
![Data](https://img.shields.io/badge/data-synthetic%20fixture-brightgreen)

A small, **UI-friendly regression demo** intended for the KFM web app’s sample gallery / fixtures.

> 🧠 Why regression? Linear models are a strong baseline: fast, explainable, and easy to sanity-check with residual diagnostics.  [oai_citation:0‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM)

---

## 📘 Overview

### Purpose
Provide a **synthetic, non-sensitive** regression sample that demonstrates:
- A minimal **contract-first** dataset shape (data + metadata)
- A baseline linear model (coefficients + intercept)
- **Evaluation metrics** and quick diagnostics (e.g., residual checks)
- “Exportable artifacts” that a web UI can display without needing a live training job

KFM emphasizes **contract-first** and **deterministic** pipelines for reproducibility.  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Scope
| ✅ In scope | ❌ Out of scope |
|---|---|
| Simple & multivariate linear regression (baseline) | Shipping real governed datasets inside `web/` |
| Synthetic demo data + lightweight artifacts | “Evidence artifacts” meant for publication |
| R²/MAE/RMSE + residual sanity checks | Any UI bypass of KFM’s API/governance layer |

KFM policy: **evidence artifacts must be exposed through governed APIs**; “direct access or hard-coding such artifacts in the UI is not allowed.”  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### Audience
- 🧑‍💻 Web devs needing stable sample fixtures for UI states
- 📊 Analysts wanting a baseline regression example format
- 🧾 Reviewers checking that sample assets stay non-sensitive & governance-safe

### Definitions
- **Fixture**: synthetic/static sample asset used for UI development/testing.
- **Evidence artifact**: derived/AI output treated as a first-class dataset with full provenance and governance, stored under `data/processed/` and exposed via APIs.  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- **Residuals**: differences between observed and predicted values; useful for diagnosing fit issues.  [oai_citation:4‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM)

---

## 🗂️ Directory Layout

> 🧩 This folder is intentionally self-contained. Keep assets **small**, **synthetic**, and **non-sensitive**.

```text
web/assets/samples/analytics/regression/
├─ README.md                         # ← you are here 📍
├─ data/                             # demo inputs 🧪
│  ├─ sample.csv                     # synthetic regression dataset (X + y)
│  └─ sample.meta.json               # minimal “contract-first” metadata
└─ artifacts/                        # precomputed outputs 📦
   ├─ model.linear.json              # coefficients, intercept, feature list
   ├─ metrics.json                   # R² / MAE / RMSE + splits
   └─ predictions.csv                # y_true, y_pred, residual (+ optional row_id)
```

### File roles (recommended)
| File | Role | Notes |
|---|---|---|
| `data/sample.csv` | Input dataset | Synthetic only. No real coords/PII. |
| `data/sample.meta.json` | Data contract + provenance hints | Keep schema stable (UI fixtures love stability). |
| `artifacts/model.linear.json` | Model parameters | Coeffs/intercept for UI display & debugging. |
| `artifacts/metrics.json` | Model quality | R² is common; include MAE/RMSE for interpretability.  [oai_citation:5‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR) |
| `artifacts/predictions.csv` | Row-level outputs | Useful for scatter plots, residual plots, and table views. |

---

## 🧾 Data Contract & Provenance

KFM’s approach centers on **metadata-first**: sources/manifests and explicit provenance reduce “mystery layers” and support traceability.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

For **web fixtures**, we keep it minimal and clearly labeled as synthetic.

### Minimal `sample.meta.json` (example)
```json
{
  "id": "kfm.sample.analytics.regression.v0",
  "title": "Synthetic Regression Fixture",
  "description": "A tiny synthetic dataset for demonstrating linear regression in the KFM web UI.",
  "data_kind": "tabular",
  "provenance": {
    "source": "synthetic",
    "method": "generated-for-ui-fixture",
    "notes": "No real-world coordinates, persons, or sensitive sites."
  },
  "columns": [
    {"name": "x1", "type": "number", "role": "feature"},
    {"name": "x2", "type": "number", "role": "feature"},
    {"name": "y",  "type": "number", "role": "target"}
  ],
  "governance": {
    "fair_care": "FAIR+CARE",
    "care_label": "Public · Synthetic Fixture",
    "classification": "open"
  }
}
```

✅ If a dataset stops being a fixture and becomes “real,” it should migrate into the canonical pipeline:
**ETL → catalogs (STAC/DCAT/PROV) → graph → APIs → UI**.  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📐 Regression Method (What the sample demonstrates)

### Linear model refresher
Multivariate linear regression uses multiple predictors and fits:

$begin:math:display$
y \= \\beta\_0 \+ \\beta\_1 x\_1 \+ \\beta\_2 x\_2 \+ \.\.\. \+ \\epsilon
$end:math:display$

In Python, common options include **statsmodels** (statistics-first) and **scikit-learn** (ML-first).  [oai_citation:8‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR)

### ⚠️ Correlation isn’t causation
Even a strong fit does **not** imply a causal relationship between predictor(s) and target.  [oai_citation:9‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM)

### Residual sanity checks (what to look for)
Residual plots are a fast diagnostic:
- Residuals should look **random** (no obvious pattern)
- Clear trends or “U-shapes” can indicate **non-linearity**
- Changing spread may indicate **heteroscedasticity**
- Large standardized residuals can indicate **outliers/influential points**  [oai_citation:10‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM)  [oai_citation:11‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR)

<details>
<summary><b>🔎 Quick checklist for a “reasonable” baseline regression</b></summary>

- [ ] **Residual plot looks random** (no structure)  [oai_citation:12‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR)  
- [ ] **No extreme standardized residuals** (e.g., beyond ±3 as a rule of thumb)  [oai_citation:13‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM)  
- [ ] **No single point dominates** coefficients/intercept (high leverage/influence)  [oai_citation:14‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM)  
- [ ] **R² doesn’t replace MAE/RMSE** (report multiple metrics)  [oai_citation:15‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR)  
- [ ] **Interpretation included** (units, feature meaning, limitations)

</details>

---

## 🧪 Generate / Refresh the Fixture (Local)

> This is a **reference snippet** showing the kind of export the UI can consume. Keep outputs deterministic (fixed RNG seeds, stable splits) to match KFM’s reproducibility goals.  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

```python
import json
import pathlib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

ROOT = pathlib.Path("web/assets/samples/analytics/regression")
DATA = ROOT / "data" / "sample.csv"
OUT  = ROOT / "artifacts"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)

# 👉 Adjust these columns to match your fixture schema
feature_cols = [c for c in df.columns if c.startswith("x")]
target_col = "y"

X = df[feature_cols]
y = df[target_col]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42  # deterministic ✅
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
residual = y_test.values - y_pred

metrics = {
    "r2": float(r2_score(y_test, y_pred)),
    "mae": float(mean_absolute_error(y_test, y_pred)),
    "rmse": float(np.sqrt(mean_squared_error(y_test, y_pred))),
    "n_train": int(len(X_train)),
    "n_test": int(len(X_test)),
    "features": feature_cols
}

(OUT / "metrics.json").write_text(json.dumps(metrics, indent=2))
(OUT / "model.linear.json").write_text(json.dumps({
    "intercept": float(model.intercept_),
    "coefficients": {f: float(w) for f, w in zip(feature_cols, model.coef_)},
    "features": feature_cols
}, indent=2))

pred_df = pd.DataFrame({
    "y_true": y_test.values,
    "y_pred": y_pred,
    "residual": residual
})
pred_df.to_csv(OUT / "predictions.csv", index=False)
```

---

## 🌐 Web UI Integration Notes

If the UI renders:
- **Metrics card** → `artifacts/metrics.json`
- **Coefficient table** → `artifacts/model.linear.json`
- **Scatter / residual plots** → `artifacts/predictions.csv`

✅ Keep these stable across refreshes:
- Field names
- Numeric formats (avoid scientific notation in JSON when possible)
- Deterministic split seeds

### ♿ Accessibility
KFM’s web experience emphasizes accessibility (e.g., ARIA and high-contrast considerations). When adding charts, include:
- Clear axis labels
- A text summary (alt description) of what the chart shows
- Non-color-only encodings where possible  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ⚖ Governance & Safety Guardrails

This folder is **web-facing**, so treat it like a public surface area:

- ✅ **ONLY synthetic data** (or heavily redacted, steward-approved fixtures)
- ✅ No PII, no precise sensitive sites/locations
- ✅ No “real evidence artifacts” here

If you need to publish a real model output:
- Store it in `data/processed/...`
- Catalog it (STAC/DCAT)
- Trace it (PROV)
- Serve it via governed APIs (redaction/classification)
- Then display in UI via the API layer (no hard-coding)  [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## ✅ Definition of Done (for this sample README + assets)

Aligned with KFM’s doc discipline and CI expectations.  [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

- [ ] Front-matter complete & valid (no missing required fields)  [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- [ ] Includes required sections (Overview, Directory Layout, etc.)  [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- [ ] All sample data is **synthetic** and clearly labeled
- [ ] No broken internal links / unresolved references  [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- [ ] Artifacts are deterministic (fixed seed, stable schema)  [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- [ ] File sizes kept small (fast load, offline-friendly)
- [ ] Governance notes are explicit (FAIR+CARE + classification)

---

## 🕰️ Version History

| Version | Date | Notes |
|---:|---|---|
| v0.1.0 | 2026-01-18 | Initial regression sample README + recommended fixture contract |

---

## 🔗 References (project files)

- KFM v13 Markdown / pipeline discipline (contract-first, evidence-first, CI gates)  [oai_citation:24‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Evidence artifact pattern + API governance rule (“no hard-coded artifacts in UI”)  [oai_citation:25‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Regression analysis notes: residual diagnostics, outliers/influence, model sanity checks  [oai_citation:26‡regression-analysis-with-python.pdf](file-service://file-NCS6ThhvajwNUm4crVVcGM)  
- Linear regression slides: R² interpretation, residual plot expectations, statsmodels vs scikit-learn  [oai_citation:27‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR)  [oai_citation:28‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR)  
- KFM system overview + accessibility emphasis  [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
