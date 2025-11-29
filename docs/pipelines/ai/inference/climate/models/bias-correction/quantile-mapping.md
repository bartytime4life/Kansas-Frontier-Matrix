---
title: "📈📊🌡️ KFM v11.2.2 — Quantile Mapping Bias Correction Model (Distribution Alignment · Extremes-Ready · Deterministic)"
path: "docs/pipelines/ai/inference/climate/models/bias-correction/quantile-mapping.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Component · Bias Correction · Quantile Mapping"

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
sensitivity: "Climate-BiasCorrection-QuantileMapping"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "quantile-mapping"
  - "bias-correction"
  - "distribution-alignment"
  - "cdf-adjustment"
  - "extremes-correction"
  - "hazard-stability"
  - "deterministic-seed"
  - "xai-compatible"
  - "faircare-governance"
  - "stac-xai"
  - "prov-lineage"

scope:
  domain: "pipelines/ai/inference/climate/models/bias-correction"
  applies_to:
    - "quantile-mapping.md"
    - "regression-correction.md"
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

# 📈📊🌡️ **Quantile Mapping Bias Correction Model**  
`docs/pipelines/ai/inference/climate/models/bias-correction/quantile-mapping.md`

**Purpose**  
Define the **quantile mapping (QM) bias correction model** used to align realtime or downscaled  
climate variables with reference climatological distributions.  
Corrects entire cumulative distribution functions (CDFs), preserves extremes, and stabilizes  
hazard-sensitive variables for AI inference, anomaly generation, and statewide climate analysis.

</div>

---

## 📘 Overview

Quantile mapping (QM) is a **distribution-level correction technique**:

- Adjusts full CDF of a variable  
- Corrects mean, variance, higher-order structure implicitly  
- Preserves distribution shape while removing bias  
- Handles nonlinear distortions  
- Excellent for **precipitation**, **humidity**, and **dewpoint**  
- Performs well in **extremes** (upper/lower tails)  
- Robust for multi-decade climate baselines  

The method uses:

```
corrected = F_obs^{-1}( F_model(x) )
```

Where:

- `F_model` = empirical CDF of model/realtime data  
- `F_obs` = empirical CDF of observations  
- `F_obs^{-1}` = quantile function of observed distribution  

---

## 🧬 Model Architecture

```mermaid
flowchart TD
    A[Realtime Field] --> B[Compute Model CDF]
    B --> C[Baseline CDF]
    C --> D[Apply Quantile Mapping]
    D --> E[XAI Correction Log]
    E --> F[CARE Sovereignty Filters]
    F --> G[Assemble Corrected Field]
    G --> H[STAC XAI Metadata Packaging]
```

---

## 🗂 Supported Variables

Ideal for variables with **non-Gaussian** distributions:

- Precipitation  
- Dewpoint  
- Relative humidity  
- Soil moisture  
- Temperature extremes  
- Wind gust fields  
- CAPE/CIN preconditioning variables  

Not ideal for:  
- Variables with strict deterministic relationships (e.g., geostrophic wind)  
- Categorical/weather-type variables

---

## 🧱 Inputs Required

### **Realtime Field**
- Temporal metadata  
- CRS: MUST match baseline  
- Vertical axis defined  
- Units consistent  
- Grid resolution stable  

### **Baseline CDF**
- Derived from standardized climatology (e.g., NOAA NCEI, PRISM, ERA5-Historical)  
- Must include:  
  - Sorted sample arrays  
  - Quantile table  
  - Probability mapping LUT  
  - Metadata: license, provenance, CARE tags  

### **Optional Enhancements**
- Tail inflation/deflation  
- Percentile bounding  
- Seasonal quantile tuning (monthly, DOY windows)

---

## 🔍 Correction Formula (ASCII-safe)

```
p = F_model(x)
corrected = F_obs_inverse(p)
```

Where:

- `p` ∈ [0, 1]  
- All CDFs must be monotonic and validated  

---

## 📦 Outputs

Artifacts MUST include:

- `qm_corrected_grid.tif` (COG)  
- `qm_metadata.json`  
- `qm_summary.json`  
- XAI correction log (CDF adjustments)  
- STAC Item with quantile mapping metadata  
- Checksum (multihash)  
- PROV lineage block  

---

## 🛡️ CARE + Sovereignty Constraints

QM MUST:

- Apply H3 masking to sensitive areas  
- Avoid revealing hidden climatological patterns in protected zones  
- Include explicit CARE metadata:

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

CI MUST check:

- Monotonic CDF arrays  
- No missing quantiles  
- CRS/vertical consistency  
- Deterministic LUT application  
- FAIR+CARE metadata present  
- STAC-XAI fields correct  
- Provenance chain complete  
- Seed-lock stability  

CI failure → ❌ merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                     |
|----------|------------|-----------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial quantile-mapping model documentation.             |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Bias Correction Models](../README.md) ·  
[🌡️ Climate Inference Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

