---
title: "📉📐🌡️ KFM v11.2.2 — Regression-Based Bias Correction Model (Linear/Nonlinear · Deterministic · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/models/bias-correction/regression-correction.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Component · Bias Correction · Regression-Based"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-biascorr-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-biascorr-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-BiasCorrection-Regression"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "regression-bias-correction"
  - "linear-correction"
  - "nonlinear-correction"
  - "distribution-stabilization"
  - "hazard-driver-support"
  - "deterministic"
  - "xai-compatible"
  - "prov-lineage"
  - "faircare-governance"

scope:
  domain: "pipelines/ai/inference/climate/models/bias-correction"
  applies_to:
    - "regression-correction.md"
    - "quantile-mapping.md"
    - "distribution-correction.md"
    - "bias-correction-core"
    - "climatology-baselines"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 📉📐🌡️ **Regression-Based Bias Correction Model**  
`docs/pipelines/ai/inference/climate/models/bias-correction/regression-correction.md`

**Purpose**  
Define the **regression-based climate bias correction model** used to remove systematic offsets  
and structural error in climate fields prior to anomaly generation, downscaling, and hazard driver computation.  
Supports linear, nonlinear, and multivariate regressors with deterministic, reproducible outputs.

</div>

---

## 📘 Overview

Regression bias correction is a **relationship-based adjustment** technique that models bias as a  
function of one or more predictor variables. Useful for:

- Temperature drift removal  
- Dewpoint nonlinear error  
- Wind component structural biases  
- Predictor-driven corrections (paired variables like u10/v10)  
- Simple and robust behavior for realtime inference  
- Compatible with XAI (weights/coefficients explainability)  
- Integrates seamlessly with anomaly and hazard-driver pipelines  

Compared to quantile mapping or distribution correction, regression is best for correcting  
**systematic and smooth spatial patterns**.

---

## 🧩 Regression Models Supported

- **Univariate linear regression**  
- **Polynomial regression**  
- **Piecewise regression**  
- **Multivariate linear regression** (e.g., correcting t2m using t2m + td2m + u10 + v10)  
- **Generalized additive models** (optional)  
- **Deterministic regressors** only  

All regressors MUST include:

- Coefficients  
- Intercept  
- Variables used  
- Units  
- CRS/vertical axis compatibility  
- Seed-lock configuration  

---

## 🧬 Regression Correction Pipeline

```mermaid
flowchart TD
    A[Realtime Field] --> B[Load Regression Model]
    B --> C[Predict Bias]
    C --> D[Subtract Bias From Realtime]
    D --> E[XAI Explain Weights]
    E --> F[CARE And Sovereignty Filters]
    F --> G[Assemble Corrected Field]
    G --> H[STAC XAI Metadata Packaging]
```

---

## 🔍 Input Requirements

### **Realtime Field**
- Units match correction model  
- Full metadata attached (CRS, time, vertical axis, bbox)  
- Complete variable set if multivariate regression is used  

### **Regression Model**
- MUST include deterministic coefficients  
- MUST specify training dataset + licensing  
- MUST include baseline period if seasonal regression used  
- SHOULD include residuals summary  

---

## 📦 Formula

For univariate linear regression:

```
bias = a * x + b
corrected = x - bias
```

For multivariate:

```
bias = a1*x1 + a2*x2 + ... + an*xn + b
corrected = x_target - bias
```

All regressors MUST be deterministic + seeded.

---

## 🎛 Outputs

- `regression_corrected_grid.tif` (COG)  
- `regression_correction_metadata.json`  
- `regression_weights.json` (for XAI)  
- STAC Item metadata  
- PROV lineage block  
- CARE masking if required  
- XAI attribution summary  

---

## 🛡️ CARE + Sovereignty Enforcement

Regression outputs MUST respect:

- Indigenous sovereignty boundaries  
- Spatial generalization for sensitive zones  
- Variable-level access restrictions  
- CARE scoping annotations in all metadata:

```json
{
  "care": {
    "masking": "h3-generalized",
    "scope": "public-generalized"
  }
}
```

---

## 🧪 CI Validation Requirements

CI MUST verify:

- Deterministic coefficient values  
- Regression model contains no prohibited randomness  
- CRS + vertical axis values match realtime field  
- Required metadata fields exist  
- XAI weights explain graph (feature coefficients) present  
- Distribution of residuals validated  
- PROV lineage included  
- STAC-XAI metadata valid  

CI failure → ❌ merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                        |
|----------|------------|--------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial regression-based bias correction model documentation |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Bias Correction Models](../README.md) ·  
[🌡️ Climate Inference Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

