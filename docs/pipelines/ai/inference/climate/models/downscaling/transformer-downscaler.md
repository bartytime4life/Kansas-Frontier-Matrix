---
title: "🔮⬇️🌡️ KFM v11.2.2 — Transformer Downscaler Model (Context-Aware · Multivariate · Deterministic · XAI-Ready)"
path: "docs/pipelines/ai/inference/climate/models/downscaling/transformer-downscaler.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Component · Climate Downscaling · Transformer"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
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
sensitivity: "Climate-Downscaler-Transformer"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "transformer-downscaling"
  - "context-aware-downscaling"
  - "multivariate-downscaling"
  - "sequence-spatial-model"
  - "deterministic-seed"
  - "xai-friendly"
  - "long-range-context"
  - "temporal-conditioning"
  - "hazard-driver-support"
  - "stac-xai"

scope:
  domain: "pipelines/ai/inference/climate/models/downscaling"
  applies_to:
    - "transformer-downscaler.md"
    - "unet-downscaler.md"
    - "downscaling-core"
    - "climate-high-resolution"
    - "multivariate-grid-modeling"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🔮⬇️🌡️ **Transformer Downscaler Model**  
`docs/pipelines/ai/inference/climate/models/downscaling/transformer-downscaler.md`

**Purpose**  
Define the **Transformer-based climate downscaling model** used to produce  
high-resolution climate fields from coarse-resolution inputs.  
Supports multivariate conditioning, sequence-aware temporal embeddings, XAI interpretability,  
hazard-driver consistency, and deterministic reproducibility with full FAIR+CARE metadata.

</div>

---

## 📘 Overview

The transformer downscaler provides **context-rich**, **nonlocal**, **multivariate** refinement of coarse  
climate grids.

Capabilities include:

- Multivariate conditioning (temp, dewpoint, wind, humidity, pressure)  
- Long-range spatial dependencies  
- Optional temporal embedding (previous frames)  
- Stable generalization for regional extremes  
- Reproducible inference under strict seed-lock  
- Explainability support (SHAP, IG)  
- Integration with hazard-driver pipelines (CAPE/CIN/SRH/LLJ)  
- STAC-XAI compliant metadata  

Downscaled outputs must feed seamlessly into anomaly, bias-correction, and driver models.

---

## 🧬 Architecture Overview

```mermaid
flowchart TD
    A[Coarse Input Grid] --> B[Embed Variables]
    B --> C[Multi Head Attention Blocks]
    C --> D[Feedforward Refinement Blocks]
    D --> E[Spatial Upscaling Head]
    E --> F[High Resolution Output Grid]
    F --> G[Optional XAI Projections]
    G --> H[STAC XAI Metadata Assembly]
```

---

## 🧱 Model Components

### **1. Embedding Layer**
- Per-variable linear projections  
- Positional encodings (2D or learned)  
- Optional temporal token embeddings  

### **2. Attention Layers**
- Multi-head self-attention  
- Cross-variable attention  
- Regional attention windows (optional)  

### **3. Feedforward Blocks**
- Residual structure  
- Layer normalization  
- GELU activation (preferred)  

### **4. Upscaling Head**
- Pixel shuffle  
- Learned interpolation  
- Local convolution refinement  

Outputs MUST match:

```
target_resolution
target_crs
target_vertical_axis
```

---

## 🧪 Input Requirements

### **Coarse Input**
- Source: ERA5, HRRR, NLDAS, NCEP, or downscaled pre-model  
- CRS: Any transformable to EPSG:4326  
- Units: MUST match fine-resolution targets  
- Variables: Declared in metadata  

### **Training Data**
- Clean multi-year paired datasets  
- Downscaled high-resolution truth (e.g., HRRR → 1 km)  
- Licensing and provenance required  

---

## 📦 Output Specification

Model MUST output:

- `downscaled_grid.tif` (COG)  
- `downscaler_metadata.json`  
- `downscaler_summary.json`  
- STAC Item with XAI & lineage metadata  
- Multihash checksums  
- XAI feature attribution maps (optional)

---

## 🛡️ CARE & Sovereignty Enforcement

Transformer downscalers MUST:

- Apply H3-based generalization over protected areas  
- Remove sensitive high-resolution gradients when restricted  
- Include CARE metadata in outputs:

```json
{
  "care": {
    "masking": "h3-generalized",
    "scope": "public-generalized",
    "notes": ["High resolution downscaling masked in protected zones"]
  }
}
```

---

## 🎛 XAI Integration

Transformer attention maps support:

- SHAP  
- Integrated Gradients  
- Attention rollout  
- CAM-like maps for spatial interpretation  

XAI logs MUST include:

- Input variable contributions  
- Attention-weight summaries  
- Deterministic seeds  
- Model version metadata  

---

## 🧪 CI Validation Requirements

CI MUST validate:

- CRS/units consistency  
- Deterministic inference  
- STAC-XAI blocks present  
- PROV lineage correct  
- XAI metadata complete  
- No missing variables  
- No unseeded randomness in model head  
- CARE filters applied  

Failure → ❌ merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                             |
|----------|------------|---------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial transformer downscaler model documentation |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Downscaling Models](../README.md) ·  
[🌡️ Climate Pipeline Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

