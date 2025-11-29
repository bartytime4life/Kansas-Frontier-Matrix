---
title: "🌪️🧲⚡ KFM v11.2.2 — Tornado Risk Hazard Model (STP-Style ⚡ · SRH 🌀 · CAPE 🌡️ · LCL 📉 · Shear 🌬️ · XAI 💡 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/inference/hazards/tornado-risk.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazards Working Group 🌪️ · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hazards · Tornado Risk Model 🌪️"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/hazards-inference-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-hazards-inference-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../contracts/data-contract-v3.json"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · High-Risk"
sensitivity: "Hazards-TornadoRisk"
sensitivity_level: "High"
public_exposure_risk: "High"
immutability_status: "version-pinned"

semantic_intent:
  - "tornado-risk"
  - "tornado-parameter"
  - "srh"
  - "cape-cin"
  - "lcl"
  - "shear"
  - "supercell-potential"
  - "storm-environment"
  - "xai-hazards"
  - "stac-xai"
  - "prov-lineage"
  - "seed-locked"

scope:
  domain: "pipelines/ai/inference/hazards"
  applies_to:
    - "tornado-risk.md"
    - "severe-storms.md"
    - "hail-risk.md"
    - "hazard-composite.md"
    - "xai-hazards.md"
    - "telemetry/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true
requires_directory_layout_section: false

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌪️🧲⚡ **Tornado Risk Hazard Model — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/inference/hazards/tornado-risk.md`

**Purpose**  
Define the deterministic, XAI-enhanced, sovereignty-protected **Tornado Risk Model** for KFM.  
Integrates **SRH 🌀**, **CAPE 🌡️**, **LCL height 📉**, **deep-layer shear 🌬️**, **LLJ strength 🌀**,  
**dryline forcing 🌵**, and **storm-relative winds 🔄** into a unified tornado potential index  
for realtime mapping, hazard chains, and Story Node v3 meteorological narratives.

</div>

---

## 🌪️📘⚡ **Overview — Tornado Potential in KFM**

The Tornado Risk Model incorporates:

- 🌀 **Storm-Relative Helicity (SRH)** — 0–1 km / 0–3 km  
- 🌡️ **Instability (CAPE / CIN)**  
- 📉 **Low-Level LCL height** (lower = higher tornado probability)  
- 🌬️ **Deep-Layer Shear** (supercell organization)  
- 🌀 **LLJ strength** (inflow + helicity enhancement)  
- 🌵 **Dryline forcing** & moisture gradient  
- 🔄 **Storm motion vectors**  
- 🧠 **Tornado XAI** (CAM overlays + feature weights)  
- 🛡️ **FAIR+CARE masking**  
- 📜 **PROV-O lineage**  
- 🗂️ **STAC-XAI hazard catalog entry**

This model is a **deterministic analogue** of STP-like tornado parameters.

---

## 🧬🌪️⚙️ **Tornado Risk Pipeline (Mermaid-Safe)**

```mermaid
flowchart TD
    A[🌀 Storm Relative Helicity] --> D[📏 Normalize Inputs]
    B[🌡️ Instability CAPE CIN] --> D
    C[📉 Low LCL Height] --> D
    E[🌬️ Deep Layer Shear] --> D
    F[🌀 LLJ Strength] --> D
    G[🌵 Dryline Convergence] --> D
    D --> H[🌪️ Deterministic Tornado Risk Calculation]
    H --> I[💡 XAI Attribution Layer]
    I --> J[🗂️ STAC XAI Metadata Packaging]
    J --> K[📊 Tornado Risk Outputs]
```

---

## 🌀🌡️🌬️ **Inputs Required**

### 1️⃣ 🌀 Storm Relative Helicity (SRH)  
- 0–1 km, 0–3 km  
- Derived storm motion  

### 2️⃣ 🌡️ Instability  
- CAPE (surface / mixed-layer / effective)  
- CIN to assess inhibition  

### 3️⃣ 📉 LCL Height  
- Lower LCL → larger tornado potential  
- Derived from temp/dewpoint  

### 4️⃣ 🌬️ Shear  
- Deep-layer shear (0–6 km)  
- Shear vectors for storm mode  

### 5️⃣ 🌀 LLJ  
- 850/925 mb wind maxima  
- Nocturnal inflow  

### 6️⃣ 🌵 Dryline Parameters  
- Moisture gradient  
- Surface convergence  

### Metadata  
All MUST include: CRS, units, timestamp, STAC references.

---

## ⚡🧮🌪️ **Tornado Risk Formula (ASCII-Safe)**

```
TornadoRisk =
    w1 * srh_norm
  + w2 * cape_norm
  + w3 * shear_norm
  + w4 * llj_norm
  + w5 * (1 - lcl_norm)
  + w6 * dryline_norm
```

### Deterministic Requirements  
- No probabilistic components  
- Seed-locked  
- Version-pinned weights  
- Stable floating-point order  

---

## 📦🌪️📊 **Outputs**

- `tornado_risk_grid.tif`  
- `tornado_risk_metadata.json`  
- `tornado_risk_summary.json`  
- Optional CAM layers  
- STAC-XAI Item  
- Deterministic seeds  
- Full PROV lineage  
- CARE metadata block  

---

## 💡🧠🌪️ **XAI Integration**

XAI MUST reveal:

- SRH contribution  
- CAPE impact  
- LCL sensitivity  
- Shear & LLJ effects  
- Dryline gradient influence  
- CAM overlays of tornado-favorable regions  
- Variable importance vectors  
- Seed-lock metadata  
- STAC-XAI linkage  

Example:

```json
{
  "xai": {
    "importance": {
      "srh": 0.38,
      "cape": 0.24,
      "shear": 0.18,
      "llj": 0.12,
      "lcl": 0.05,
      "dryline": 0.03
    },
    "seed": 42
  }
}
```

---

## 🛡️⚖️🌪️ **CARE + Sovereignty Enforcement**

Tornado risk fields MUST:

- Avoid revealing hyperlocal tornado-initiation zones in tribal areas  
- Generalize narrow corridors of high STP-like fields  
- Remove sensitive hotspots near protected lands  
- Include:

```json
{
  "care": {
    "masking": "h3-hazard-generalized",
    "scope": "public-generalized",
    "notes": ["Tornado risk generalized in sovereignty-protected regions"]
  }
}
```

---

## 🔒⚙️🧪 **Determinism Requirements**

- No stochastic updraft predictors  
- No random sampling of storm environments  
- Deterministic SRH computations  
- Fixed shear/lapse/CAPE evaluation order  
- CI-reproducible risk maps  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST verify:

- CRS/units  
- Deterministic tornado risk output  
- Complete XAI metadata  
- STAC-XAI conformity  
- Full PROV-O lineage  
- CARE enforcement  
- Telemetry generation  
- All parent hazard drivers present  

Failure → ❌ CI BLOCKED.

---

## 🕰️📜 **Version History**

| Version  | Date       | Notes                                           |
|----------|------------|-------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Tornado Risk Hazard Model (MAX MODE)    |

---

<div align="center">

### 🔗 Footer  
[🌪️ Back to Hazards Pipeline](./README.md) ·  
[⚡ Severe Storms](./severe-storms.md) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

