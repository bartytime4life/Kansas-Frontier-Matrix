---
title: "📊🛠️🌡️ KFM v11.2.2 — Distribution-Based Bias Correction Model (Multi-Moment · Statistical Alignment · Deterministic)"
path: "docs/pipelines/ai/inference/climate/models/bias-correction/distribution-correction.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Component · Bias Correction · Distribution Alignment"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
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
sensitivity: "Climate-BiasCorrection-Distribution"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "distribution-correction"
  - "bias-correction"
  - "statistical-alignment"
  - "multi-moment-correction"
  - "variance-skew-adjustment"
  - "hazard-input-stabilization"
  - "deterministic-climate-modeling"
  - "xai-compatible"
  - "faircare-governance"
  - "prov-lineage"

scope:
  domain: "pipelines/ai/inference/climate/models/bias-correction"
  applies_to:
    - "distribution-correction.md"
    - "quantile-mapping.md"
    - "regression-correction.md"
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

# 📊🛠️🌡️ **Distribution-Based Bias Correction Model**  
`docs/pipelines/ai/inference/climate/models/bias-correction/distribution-correction.md`

**Purpose**  
Define the **multi-moment distribution-based bias correction model** used to align realtime or  
downscaled climate fields to observed statistical distributions.  
Corrects mean, variance, skew, kurtosis, and higher-order biases to stabilize hazard-chain models,  
ensure XAI interpretability, and deliver FAIR+CARE-compliant, provenance-rich outputs.

</div>

---

## 📘 Overview

Distribution-based correction adjusts **entire statistical moments** rather than only pointwise values.  
It is essential for:

- Stabilizing extreme-value tails (heat extremes, wind gust tendencies, humidity outliers)  
- Improving anomaly and driver accuracy (CAPE, CIN, SRH depend on variance-sensitive fields)  
- Matching climatological distributions (NOAA NCEI normals, PRISM climatology, ERA5-History)  
- Supporting statewide, tile-level, and streaming inference  
- Ensuring deterministic reproducibility and XAI consistency  
- Preparing STAC-XAI-compliant climatological metadata  

It differs from regression or quantile-mapping by directly manipulating **statistical structure**:

```
Corrected = (Realtime - μ_r) * (σ_o / σ_r) + μ_o
```

And optionally:

- Adjust skewness  
- Adjust kurtosis  
- Adjust percentile shape  
- Apply CARE filters to sensitive distributions  

---

## 🧬 Model Architecture

```mermaid
flowchart TD
    A[Realtime Field] --> B[Stats Extraction]
    B --> C[Baseline Distribution Stats]
    C --> D[Deterministic Multi Moment Correction]
    D --> E[XAI Compatible Adjustment Log]
    E --> F[CARE Filtering And Sovereignty Masking]
    F --> G[Assemble Corrected Field]
    G --> H[STAC XAI Metadata Packaging]
```

---

## 🧪 Supported Variables (Distribution-Sensitive)

- Temperature (`t2m`, `t850`, `t700`)  
- Dewpoint (`td2m`)  
- Wind (`u10`, `v10`, upper-level wind fields)  
- Relative humidity  
- Precipitation climatological tendency  
- Soil moisture (optional)  
- Surface pressure distributions  

Each variable must include baseline + realtime moments:

```
mean
stddev
variance
skew
kurtosis
percentile_curves (optional)
```

---

## 🧱 Input Requirements

### **Realtime Field**
- CRS: MUST match baseline  
- Vertical axis: explicit & compatible  
- Units: identical  
- Metadata: spatial extent, timestamp  

### **Baseline Distribution**
- Multi-moment stats (at least mean + stddev)  
- Source provenance  
- Time window (e.g., 1991–2020)  

### **Optional Reference Curves**
- Percentile metrics  
- Tail-shape curves  

---

## 🔍 Correction Formula (Expanded)

```
z = (realtime - mean_realtime) / std_realtime

corrected =
    z * std_obs
  + mean_obs
  + skew_adj
  + kurtosis_adj
  + tail_shape_adj(optional)
```

All steps MUST be deterministic under seed-lock.

---

## 🎛 Outputs

- `distribution_corrected_grid.tif` (COG)  
- `distribution_correction_metadata.json`  
- `distribution_correction_summary.json`  
- XAI correction log (moment adjustments, location sensitivities)  
- STAC Item with correction lineage  
- Provenance chain (`prov:used`, `prov:wasGeneratedBy`)  

---

## 🛡️ CARE & Sovereignty Logic

Distribution correction MUST:

- Mask sensitive spatial domains using H3 generalization  
- Avoid revealing protected local climate features  
- Include CARE scope tags in metadata  

Example:

```json
{
  "care": {
    "masking": "h3-generalized",
    "scope": "public-generalized",
    "notes": ["Distribution adjustments performed under sovereignty filters"]
  }
}
```

---

## 🧪 CI Validation Requirements

CI MUST check:

- All moments available for selected variable  
- CRS + vertical consistency  
- Baseline & realtime units identical  
- Deterministic results under fixed seeds  
- Correct field-level metadata  
- Required STAC-XAI metadata blocks  
- PROV lineage validity  
- Integrity of distribution correction logs  

---

## 🕰 Version History

| Version  | Date       | Notes                                                          |
|----------|------------|----------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial distribution-based bias-correction model documentation |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Bias Correction Models](../README.md) ·  
[🌡️ Climate Inference Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

