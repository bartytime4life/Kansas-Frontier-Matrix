---
title: "⛈️🌪️⚡ KFM v11.2.2 — Severe Storms Hazard Model (CAPE 🌡️ · CIN 📉 · Shear 🌬️ · LLJ 🌀 · Lapse Rates 📈 · XAI 💡 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/inference/hazards/severe-storms.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazards Working Group 🌪️ · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hazards · Severe Storms Model ⛈️"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
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
sensitivity: "Hazards-SevereStorms"
sensitivity_level: "High"
public_exposure_risk: "High"
immutability_status: "version-pinned"

semantic_intent:
  - "severe-storms"
  - "instability-drivers"
  - "kinematic-drivers"
  - "dryline-dynamics"
  - "supercell-environment"
  - "updraft-potential"
  - "storm-relative-winds"
  - "shear-profile"
  - "llj-influence"
  - "hazard-driver"
  - "xai-hazards"
  - "stac-xai"
  - "prov-lineage"
  - "seed-locked"

scope:
  domain: "pipelines/ai/inference/hazards"
  applies_to:
    - "severe-storms.md"
    - "hail-risk.md"
    - "tornado-risk.md"
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

# ⛈️🌪️⚡ **Severe Storms Hazard Model — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/inference/hazards/severe-storms.md`

**Purpose**  
Define the deterministic, XAI-ready, FAIR+CARE-governed **Severe Storms Hazard Model**,  
combining **CAPE 🌡️**, **CIN 📉**, **deep-layer shear 🌬️**, **low-level jet 🌀**,  
**lapse rates 📈**, and **dryline dynamics 🌵🌀**, to produce statewide severe-thunderstorm  
hazard fields used in realtime maps, hazard pipelines, and Story Node v3 narrative overlays.

</div>

---

## ⚡⛈️🌪️ **Overview — Severe Thunderstorm Hazard Science**

The Severe Storms Hazard Model blends:

- 🌡️ **Instability:** CAPE, lifted indices, theta-e  
- 📉 **CIN:** capping strength & storm initiation inhibition  
- 🌬️ **Shear:** 0–1km, 0–3km, 0–6km bulk shear  
- 🌀 **LLJ:** overnight inflow strength  
- 📈 **Lapse Rates:** mid-level / low-level lapse rate steepness  
- 🌵 **Dryline Index:** convergence & moisture gradient  
- 🧠 **XAI Explainability:** attribution maps, importance vectors  
- 🛡️ **FAIR+CARE Filtering:** sovereignty-aware hazard boundaries  
- 🗂️ **STAC-XAI Hazard Metadata**  
- 📜 **PROV-O Lineage**

This model underpins **hail**, **tornado**, and **supercell composite** hazards.

---

## 🌪️⚙️⛈️ **Severe Storms Pipeline Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[🌡️ CAPE And Instability Fields] --> D[📏 Normalize Inputs]
    B[📉 CIN / Capping Strength] --> D
    C[🌬️ Deep Layer Shear] --> D
    E[🌀 Low Level Jet Strength] --> D
    F[📈 Lapse Rates] --> D
    D --> G[⚡ Deterministic Severe Storms Calculation]
    G --> H[💡 XAI Attribution Layer]
    H --> I[🗂️ STAC XAI Metadata Packaging]
    I --> J[📊 Severe Storms Hazard Outputs]
```

---

## 🌡️📉🌬️ **Inputs Required**

### 1️⃣ 🌡️ Instability  
- CAPE (surface/elevated)  
- LFC/EL levels  
- Theta-e ridge index  

### 2️⃣ 📉 CIN / Cap Strength  
- Forecast initiation windows  
- Dryline suppression fields  

### 3️⃣ 🌬️ Shear  
- Bulk shear  
- Deep-layer shear  
- Storm-relative winds  

### 4️⃣ 🌀 LLJ  
- 850mb / 925mb wind maxima  
- Nocturnal inflow  

### 5️⃣ 📈 Lapse Rates  
- 700–500mb lapse  
- 0–3 km lapse  
- Used for hail/tornado cross-compatibility  

### 6️⃣ 🌵 Dryline Parameters  
- Dewpoint gradient  
- Surface convergence  
- Moisture discontinuity  

---

## ⚡🧮⛈️ **Hazard Formula (ASCII-Safe)**

```
SevereStormsIndex =
    w1 * cape_norm
  + w2 * shear_norm
  + w3 * llj_norm
  + w4 * lapse_norm
  + w5 * (1 - cin_norm)
  + w6 * dryline_norm
```

All weights MUST be deterministic, version-pinned, and reproducible.

---

## 📦⚡📊 **Outputs**

Model MUST generate:

- `severe_storms_grid.tif`  
- `severe_storms_metadata.json`  
- `severe_storms_summary.json`  
- Optional CAM overlays (XAI)  
- STAC-XAI Item  
- Deterministic seed metadata  
- Full PROV lineage  
- CARE metadata block  

---

## 💡🧠⛈️ **XAI Integration**

XAI MUST provide:

- CAPE contribution  
- CIN inhibition role  
- Shear influence  
- LLJ enhancement effect  
- Lapse rate impact  
- Dryline convergence signal  
- Watershed/storm-environment CAM layers  
- Deterministic seed + STAC-XAI asset links  

Example:

```json
{
  "xai": {
    "importance": {
      "cape": 0.31,
      "shear": 0.27,
      "llj": 0.18,
      "lapse_rates": 0.13,
      "cin": 0.08,
      "dryline": 0.03
    },
    "seed": 42
  }
}
```

---

## 🛡️⚖️🌪️ **CARE + Sovereignty Enforcement**

Severe Storms hazard MUST:

- Mask hyperlocal storm-initiation hotspots  
- Generalize supercell tracks near sovereignty-protected lands  
- Remove high-risk indices from culturally sensitive regions  

CARE block example:

```json
{
  "care": {
    "masking": "h3-hazard-generalized",
    "scope": "public-generalized",
    "notes": ["Severe storm hotspots generalized within sovereignty-protected regions"]
  }
}
```

---

## 🔒⚙️🧪 **Determinism Requirements**

- No stochastic convective triggering  
- No random updraft predictors  
- Seed-lock for all calculations  
- Stable floating-point order  
- Deterministic shear/lapse/CAPE processing  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST confirm:

- CRS + units present  
- Deterministic hazard fields  
- Correct XAI metadata  
- STAC-XAI compliance  
- PROV lineage complete  
- CARE block present  
- Telemetry data linked  
- No missing drivers  

Failure → ❌ merge blocked.

---

## 🕰️📜 **Version History**

| Version  | Date       | Notes                                           |
|----------|------------|-------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Severe Storms Model (MAX MODE)          |

---

<div align="center">

### 🔗 Footer  
[🌪️ Back to Hazards Pipeline](./README.md) ·  
[⚡ Hazard Models](./) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

