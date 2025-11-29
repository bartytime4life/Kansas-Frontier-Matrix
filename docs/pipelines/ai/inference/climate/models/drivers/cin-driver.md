---
title: "🧲🌡️📉 KFM v11.2.2 — CIN Driver Model (Convective Inhibition · Parcel Suppression · Deterministic · XAI-Ready)"
path: "docs/pipelines/ai/inference/climate/models/drivers/cin-driver.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Component · Hazard Driver · CIN"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-drivers-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-drivers-v11.2.2.json"
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
sensitivity: "Climate-Driver-CIN"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "cin-driver"
  - "convective-inhibition"
  - "parcel-suppression"
  - "thermodynamic-stability"
  - "hazard-drivers"
  - "deterministic-seed"
  - "xai-compatible"
  - "stac-xai"
  - "prov-lineage"

scope:
  domain: "pipelines/ai/inference/climate/models/drivers"
  applies_to:
    - "cin-driver.md"
    - "cape-driver.md"
    - "shear-driver.md"
    - "llj-driver.md"
    - "instability-pack.md"
    - "hazard-driver-core"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🧲🌡️📉 **CIN Driver Model**  
`docs/pipelines/ai/inference/climate/models/drivers/cin-driver.md`

**Purpose**  
Define the **CIN (Convective Inhibition)** driver model that quantifies suppressive energy  
required to lift a parcel to its LFC (Level of Free Convection).  
CIN represents resistance to convection and plays a crucial role in severe weather forecasting,  
hazard-chain modeling, and Focus Mode v3 atmospheric narratives.

</div>

---

## 📘 Overview

CIN measures **negative buoyant energy** preventing surface parcels from freely rising.  
Its magnitude influences:

- Thunderstorm initiation timing  
- Dryline/capping strength  
- Tornado and large hail potential  
- Hazard-chain model branching (CAPE–CIN interaction)  
- Realtime and batch regional severe-weather risk maps  
- Story Node v3 meteorological context  

Properties:

- Deterministic parcel-theory calculation  
- XAI-ready (layer-by-layer suppression attribution)  
- FAIR+CARE-compliant  
- STAC-XAI compatible  

---

## 🧩 Physical Definition (ASCII-safe)

```
CIN = ∫ g * ( (T_parcel - T_environment) / T_environment ) dz
      where buoyancy < 0 before LFC
```

Where:

- `g` = gravitational acceleration  
- `T_parcel` = lifted parcel temperature  
- `T_environment` = environmental temperature  
- Integration over **negative buoyancy** layers until LFC  

---

## 🧬 CIN Driver Pipeline

```mermaid
flowchart TD
    A[Temperature Dewpoint Pressure Profiles] --> B[Parcel Initialization]
    B --> C[Compute LCL]
    C --> D[Lift Parcel Until LFC]
    D --> E[Compute Negative Buoyancy]
    E --> F[Integrate CIN]
    F --> G[Produce CIN Field]
    G --> H[XAI Attribution Optional]
    H --> I[STAC XAI Metadata Packaging]
```

---

## 🧱 Inputs Required

### **Thermodynamic Inputs**
- Temperature profile  
- Dewpoint profile  
- Pressure profile  
- Mixing ratio  
- Soil moisture (optional, for parcel source correction)  

### **Metadata**
- CRS: `EPSG:4326`  
- Vertical axis: `pressure`, `height_agl`, or model-level index  
- Units explicitly declared  
- ISO 8601 timestamp  

### **Optional Wind Conditioning**
CIN can be included in instability packs with shear and LLJ layers.

---

## 📦 Outputs

The CIN driver MUST output:

- `cin_grid.tif` (COG)  
- `cin_metadata.json`  
- `cin_summary.json`  
- STAC Item (CIN driver asset)  
- Checksum (multihash)  
- Optional XAI attribution grids  
- PROV lineage block  

---

## 🔍 XAI Integration

CIN XAI reveals:

- Suppression layers in the vertical profile  
- Sensitivity to dewpoint depressions  
- Inversion strength attribution  
- Pressure-layer contributions  
- Parcel-path explainability  

Must include:

- Seed-lock metadata  
- Model version  
- CARE scope  
- Layer-by-layer attribution arrays  

---

## 🛡️ CARE + Sovereignty Enforcement

CIN outputs MUST:

- Apply H3-based spatial masking for protected regions  
- Avoid conveying hyperlocal suppression gradients in sovereignty zones  
- Attach CARE block:

```json
{
  "care": {
    "masking": "h3-generalized",
    "scope": "public-generalized",
    "notes": ["CIN values generalized within sovereignty-limited domains"]
  }
}
```

---

## 🧮 Deterministic Integration Rules

- No stochastic parcel initialization allowed  
- No perturbation sampling  
- Floating-point summation order fixed  
- Strict reproducibility across runs  

---

## 🧪 CI Validation Requirements

CI MUST ensure:

- CRS + vertical axis consistency  
- Units validity  
- Seed-lock enforced  
- XAI metadata complete  
- STAC-XAI metadata correct  
- Complete PROV lineage  
- Correct enforcement of CARE masking  
- Deterministic integration over negative buoyancy layers  

Failure → ❌ merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                  |
|----------|------------|----------------------------------------|
| v11.2.2  | 2025-11-28 | Initial CIN driver model documentation |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Driver Models](../README.md) ·  
[🌡️ Climate Inference Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

