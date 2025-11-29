---
title: "🌊⚠️💧 KFM v11.2.2 — Flood Risk Hazard Model (Runoff 🌧️ · Streamflow 🌊 · Soil Saturation 🪴 · Rise Rate ⚡ · XAI 💡 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/inference/hazards/flood-risk.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazards Working Group 🌪️ · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hazards · Flood Risk Model 🌊"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
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
sensitivity: "Hazards-FloodRisk"
sensitivity_level: "High"
public_exposure_risk: "High"
immutability_status: "version-pinned"

semantic_intent:
  - "flood-risk"
  - "flash-flood-hazards"
  - "runoff-surges"
  - "soil-saturation"
  - "rapid-rise-rate"
  - "watershed-routing"
  - "flow-accumulation"
  - "stac-xai"
  - "prov-lineage"
  - "care-governance"
  - "sovereignty-protection"

scope:
  domain: "pipelines/ai/inference/hazards"
  applies_to:
    - "flood-risk.md"
    - "flood-index.md"
    - "runoff-driver.md"
    - "soil-moisture-driver.md"
    - "streamflow-driver.md"
    - "hazard-composite.md"
    - "xai-hazards.md"
    - "telemetry/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_governance_links_in_footer: true
requires_directory_layout_section: false
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌊⚠️💧 **Flood Risk Hazard Model — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/inference/hazards/flood-risk.md`

**Purpose**  
Define the deterministic, FAIR+CARE-enforced, sovereignty-protected **Flood Risk Hazard Model**,  
combining **runoff 🌧️**, **soil saturation 🪴**, **streamflow rise 🌊**, **terrain routing 🗺️**,  
and **rapid water-level change ⚡** to generate watershed-scale flood & flash-flood hazard indices.  
Supports realtime hazard chains, map tiles, and Story Node v3 hydrology + weather narratives.

</div>

---

## 🌊📘⚠️ **Overview — Flood Risk in KFM**

The Flood Risk Model blends:

- 🌧️ **Rainfall intensity & burst index**  
- 💦 **Soil moisture saturation & deficits**  
- 🌊 **Streamflow discharge (Q)** + **ΔQ/Δt rise rate**  
- 🌀 **Runoff surges (RRHI)**  
- 🗺️ **Terrain routing + flow accumulation**  
- 🧭 **Watershed topology & wetness index**  
- 🌡️ **Snowmelt/temperature** (if winter conditions)  
- 🧠 **XAI interpretability** (watershed CAM overlays)  
- 🛡️ **Sovereignty-aware masking** (sensitive watersheds)  

Outputs provide:

- Flash-flood hazard levels  
- Flood Index augmentation  
- Multi-hazard composites (fire/flood, heat/flood, storm/flood)

---

## 🧬🌊⚙️ **Flood Risk Pipeline Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[🌧️ Rainfall Intensity And Accumulations] --> D[📏 Normalize Inputs]
    B[🪴 Soil Moisture Saturation] --> D
    C[🌊 Streamflow Q And Rise Rate] --> D
    E[🗺️ Terrain Routing And Flow Accumulation] --> D
    D --> F[⚡ Deterministic Flood Risk Calculation]
    F --> G[💡 XAI Hazard Attribution]
    G --> H[🗂️ STAC XAI Metadata Assembly]
    H --> I[📊 Flood Risk Outputs]
```

---

## 🌧️🪴🌊 **Inputs Required**

### 1️⃣ 🌧️ Rainfall  
- Downscaled precip  
- Burst index  
- Rolling accumulations (1h/3h/6h)

### 2️⃣ 🪴 Soil Moisture  
- Absolute + anomaly  
- Saturation index  
- Multi-layer depth support  

### 3️⃣ 🌊 Streamflow  
- Discharge (Q)  
- Rise rate (ΔQ/ΔT)  
- Baseflow state  

### 4️⃣ 🗺️ Topography  
- Slope  
- Flow direction  
- Flow accumulation  
- Watershed boundaries  

### 5️⃣ ❄️ Optional Snowmelt  
- Temperature  
- Wet-bulb  
- Melt index  

All MUST include CRS, units, timestamps, and PROV-compatible metadata.

---

## ⚡🧮🌊 **Flood Risk Formula (ASCII-Safe)**

The composite Flood Risk Index (FRI):

```
FRI =
    w1 * runoff_norm
  + w2 * saturation_norm
  + w3 * rise_rate_norm
  + w4 * flow_accum_norm
  + w5 * precip_burst_norm
```

Where:

- All weights (`w1..w5`) MUST be deterministic  
- Norm values are **watershed-normalized**  
- ΔQ/Δt MUST be seed-locked and reproducible

---

## 📦🌊📊 **Outputs**

The model MUST produce:

- `flood_risk_grid.tif`  
- `flood_risk_metadata.json`  
- `flood_risk_summary.json`  
- Optional hazard-CAM overlays  
- STAC-XAI compliant Item  
- Deterministic seed metadata  
- Complete PROV-O lineage  
- CARE metadata block  

---

## 💡🧠🌊 **XAI Integration**

Hazards XAI MUST output:

- Feature importance for runoff, saturation, rise rate, flow accum, burst index  
- CAM overlays for watershed-level flood signals  
- Seed metadata  
- STAC-XAI attribution assets  
- CARE + sovereignty filters applied to XAI masks  

Example XAI importance block:

```json
{
  "xai": {
    "importance": {
      "runoff": 0.41,
      "saturation": 0.27,
      "rise_rate": 0.18,
      "accumulation": 0.09,
      "precip_burst": 0.05
    },
    "seed": 42
  }
}
```

---

## 🛡️⚖️🌊 **CARE + Sovereignty Enforcement**

Flood risk maps MUST NOT expose hyperlocal vulnerability inside sovereignty-protected,  
culturally sensitive, or endangered ecological watersheds.

Therefore apply:

- **H3 watershed generalization**  
- Downsampling of FI maxima  
- Removal of ΔQ/Δt spikes in sensitive zones  
- Attachable CARE block:

```json
{
  "care": {
    "masking": "h3-watershed-generalized",
    "scope": "public-generalized",
    "notes": ["Flood risk hotspots generalized in sovereignty-protected basins"]
  }
}
```

---

## 🔒⚙️🧪 **Determinism Requirements**

- No stochastic routing  
- Rise-rate computed with stable ordering  
- CN/runoff dependence deterministic  
- Slope/flow accumulation deterministic  
- Seed-lock ensures stable XAI attribution  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST confirm:

- Deterministic FRI output  
- CRS + units present  
- XAI metadata complete  
- STAC-XAI validity  
- PROV completeness  
- CARE block enforced  
- Hydrology/hazard coupling correct  
- Telemetry integrations (OTel, energy, carbon)

Failures → ❌ CI BLOCKED.

---

## 🕰️📜 **Version History**

| Version  | Date       | Notes                                          |
|----------|------------|------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Flood Risk Hazard Model (MAX MODE)     |

---

<div align="center">

### 🔗 Footer  
[🌪️ Back to Hazards Pipeline](./README.md) ·  
[🌊 Hydrology Models](../hydrology/README.md) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

