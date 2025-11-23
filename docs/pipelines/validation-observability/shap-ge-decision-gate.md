---
title: "🔍 KFM v11 — SHAP + Great Expectations Decision Gate Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/shap-ge-decision-gate.md"
version: "v11.0.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/shap-ge-decision-gate-schema-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
status: "Active / Enforced"
---

# 🔍 SHAP + Great Expectations Decision Gate  
### **Unified Explainability and Validation Standard for Autonomous Pipelines**

This document defines the **mandatory explainability-and-validation decision gate** used in all **KFM v11 autonomous pipelines** (hydrology-refresh, climate-refresh, hazards-refresh, etc).  
The standard integrates:

- **SHAP** (feature-level explainability and drift detection)  
- **Great Expectations** (schema, physics, units, cadence, continuity validation)  

This gate ensures that **no AI-generated dataset may enter the KFM Knowledge Graph or be promoted to STAC/DCAT** unless it passes all structural, physical, and semantic checks.

---

## 📘 1. Purpose

The KFM v11 Decision Gate guarantees:

1. **Explainability:** Every model prediction is traceable and interpretable through SHAP.  
2. **Validity:** Inputs and outputs comply with physics, hydrology/climate domain rules, and dataset standards.  
3. **Drift Defense:** SHAP signatures must remain consistent with canonical baselines.  
4. **Autonomous Safety:** Pipelines self-block, self-quarantine, and self-report when anomalies occur.

This is a **hard compliance requirement** for all autonomous ETL pipelines.

---

## 🗂️ 2. Required Directory Layout

```
src/pipelines/autonomous/{domain}-refresh/
    nodes/
        infer.py
        decision_gate.py
    resources/
        ge_suites/
            hydrology_v11.yml
            climate_v11.yml
        shap_baselines/
            <domain>/<feature>.parquet
    tests/
    pipeline.yaml

data/reference/baselines/shap/<domain>/<feature>.parquet

docs/pipelines/validation-observability/shap-ge-decision-gate.md
```

---

## 📏 3. Validation Logic (Great Expectations)

Each prediction batch must pass these checks:

### 3.1 Units & Physical Bounds  
Examples (hydrology domain):

- precipitation_mm: 0 to 500  
- temp_c: -60 to 60  
- discharge_m3s: 0 to 100000  

### 3.2 Temporal Rules

- timestamp must be non-null  
- monotonic increasing  
- cadence consistent (daily/hourly as defined per dataset)  

### 3.3 Structural Rules

- row count within logical bounds  
- no missing values in required columns  
- column types must match declared schema  

Great Expectations suite file lives at:

```
docs/pipelines/validation-observability/ge_suites/<domain>_v11.yml
```

---

## 🧠 4. SHAP Drift & Explainability Rules

### 4.1 Baseline Requirements  
Each feature has a baseline distribution stored at:

```
data/reference/baselines/shap/<domain>/<feature>.parquet
```

### 4.2 Drift Detection  
- Population Stability Index (PSI) threshold: **0.2**  
- SHAP sign rules must hold (e.g., precip should not reduce flow on average)  
- Feature importance ranking stability recommended (but not hard-gated in v11.0.0)  

### 4.3 Sample Strategy  
- Use up to 2000 rows per batch (random sample) to compute SHAP values  
- Must use the same sampling seed for reproducibility: 42  

---

## 🧪 5. Decision Gate Policy

The promotion rule is simple and strict:

```
PROMOTE only if:
    GE_VALIDATION == PASS
    AND
    SHAP_DRIFT == PASS
Else:
    QUARANTINE and block promotion.
```

On failure:

- run is tagged as `blocked-autonomous-run`  
- OpenLineage event is emitted  
- issue is opened or logged in pipeline governance  
- data is stored under `data/work/staging/quarantine/`  

---

## 🧼 6. Telemetry Artifact

Every run must generate a machine-readable decision log:

```
data/work/staging/telemetry/decision_gate_<domain>_v11.json
```

This log includes:

- ge_ok: boolean  
- shap_ok: boolean  
- ge_summary: object  
- shap_summary: object  
- psi scores  
- sign checks  
- policy metadata  

---

## 💻 7. Canonical Implementation (Python)

```
# File: src/pipelines/autonomous/hydrology-refresh/nodes/decision_gate.py
# Purpose: Run Great Expectations + SHAP drift checks before promotion.

from pathlib import Path
import json
import numpy as np
import pandas as pd
import great_expectations as ge
from great_expectations.dataset import PandasDataset
import shap

BASELINE_DIR = Path("data/reference/baselines/shap/hydrology/")
GE_SUITE_PATH = Path("docs/pipelines/validation-observability/ge_suites/hydrology_v11.yml")

def psi(a, b, bins=20):
    qa = np.histogram(a, bins=bins, range=(min(a.min(), b.min()), max(a.max(), b.max())), density=True)[0] + 1e-9
    qb = np.histogram(b, bins=bins, range=(min(a.min(), b.min()), max(a.max(), b.max())), density=True)[0] + 1e-9
    return float(np.sum((qa - qb) * np.log(qa / qb)))

def run_ge_validations(df_pred):
    ds = ge.from_pandas(df_pred)
    ds.expect_column_values_to_be_between("precip_mm", min_value=0, max_value=500)
    ds.expect_column_values_to_be_between("temp_c", min_value=-60, max_value=60)
    ds.expect_column_values_to_be_between("discharge_m3s", min_value=0, max_value=100000)
    ds.expect_column_values_to_not_be_null("timestamp")
    ds.expect_table_row_count_to_be_between(min_value=1, max_value=10000000)
    res = ds.validate(result_format="SUMMARY")
    return res["success"], res

def run_shap_checks(model, X_sample):
    explainer = shap.Explainer(model)
    shap_values = explainer(X_sample)
    shap_df = pd.DataFrame(shap_values.values, columns=model.feature_names_in_)

    psi_scores = {}
    drift_flag = False
    for col in shap_df.columns:
        base = pd.read_parquet(BASELINE_DIR / f"{col}.parquet")["shap"]
        score = psi(shap_df[col].astype(float), base.astype(float))
        psi_scores[col] = score
        if score > 0.2:
            drift_flag = True

    sign_ok = shap_df["precip_mm"].mean() >= -1e-6

    return (not drift_flag) and sign_ok, {"psi": psi_scores, "sign_ok": sign_ok}

def decision_gate(model, X_all, df_pred):
    ge_ok, ge_report = run_ge_validations(df_pred)
    X_sample = X_all.sample(min(2000, len(X_all)), random_state=42)
    shap_ok, shap_report = run_shap_checks(model, X_sample)

    artifact = {
        "ge_ok": ge_ok,
        "shap_ok": shap_ok,
        "ge_summary": ge_report.get("statistics", {}),
        "shap_summary": shap_report,
        "policy": {
            "promotion_rule": "PROMOTE if ge_ok AND shap_ok; else QUARANTINE",
            "shap_psi_threshold": 0.2
        }
    }

    Path("data/work/staging/telemetry").mkdir(parents=True, exist_ok=True)
    with open("data/work/staging/telemetry/decision_gate_hydro_v11.json", "w") as f:
        json.dump(artifact, f, indent=2)

    return ge_ok and shap_ok
```

---

## 🔧 8. Pipeline Integration (YAML)

```
nodes:
  - id: infer
    type: python
    entrypoint: src/pipelines/autonomous/hydrology-refresh/nodes/infer.py:run

  - id: decision_gate
    type: python
    depends_on: [infer]
    entrypoint: src/pipelines/autonomous/hydrology-refresh/nodes/decision_gate.py:decision_gate
    inputs:
      - model: artifacts/models/hydro_focus_transformer_v11.pkl
      - X_all: data/work/staging/hydro/features.parquet
      - df_pred: data/work/staging/hydro/predictions.parquet
    outputs:
      - data/work/staging/telemetry/decision_gate_hydro_v11.json

  - id: promote
    type: python
    depends_on: [decision_gate]
    condition: "upstream.ok"
    entrypoint: src/pipelines/common/promote.py:run
```

---

## 🧭 9. Compliance

This standard is enforced in CI/CD by:

- schema lints  
- explainability drift lints  
- pipeline integrity tests  
- FAIR+CARE Council quarterly review  

Any pipeline missing this decision gate **cannot be executed**.

---

## 🔗 Footer

**• [⬅ Back to Validation & Observability](../README.md)** ·  
**[📚 KFM Documentation Root](../../README.md)** ·  
**[🌐 Project Homepage](../../../README.md)**
