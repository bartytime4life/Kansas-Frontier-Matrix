---
title: "🔥🌬️🌡️ KFM v11.2.2 — Fire Weather Hazard Model (VPD 🔥 · Wind 🌬️ · RH 💧 · Fuels 🌾 · Deterministic ⚙️ · XAI 💡 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/inference/hazards/fire-weather.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazards Working Group 🌪️ · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hazards · Fire Weather Model 🔥"

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
sensitivity: "Hazards-FireWeather"
sensitivity_level: "High"
public_exposure_risk: "Medium"
immutability_status: "version-pinned"

semantic_intent:
  - "fire-weather"
  - "vpd"
  - "humidity-deficit"
  - "wind-driven-spread"
  - "fuel-dryness"
  - "hazard-driver"
  - "xai-hazards"
  - "stac-xai"
  - "prov-lineage"
  - "sovereignty-protection"
  - "deterministic-seed"

scope:
  domain: "pipelines/ai/inference/hazards"
  applies_to:
    - "fire-weather.md"
    - "hazard-composite.md"
    - "severe-storms.md"
    - "heat-risk.md"
    - "flood-risk.md"
    - "winter-weather.md"
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

# 🔥🌬️🌡️ **Fire Weather Hazard Model — KFM v11.2.2**  
`docs/pipelines/ai/inference/hazards/fire-weather.md`

**Purpose**  
Define the deterministic, FAIR+CARE-enforced, sovereignty-protected **Fire Weather Hazard Model**,  
which blends **VPD 🔥**, **Relative Humidity 💧**, **Wind Speed 🌬️**, **Fuel Dryness 🌾**,  
and **Temperature 🌡️** into a **composite fire-weather hazard index** suitable for realtime maps,  
hazard chains, and Story Node v3 narrative overlays.

</div>

---

## 🔥📘🌡️ **Overview — Fire Weather in KFM**

The Fire Weather model assesses **meteorological fire danger** by combining:

- 🌡️ Temperature-driven vapor pressure  
- 💧 Relative humidity (dryness deficits)  
- 🔥 **VPD (Vapor Pressure Deficit)**  
- 🌬️ Wind speed & gust potential  
- 🌾 Fuel dryness + soil moisture deficit  
- 🗺️ Terrain slope & aspect modifiers  
- 🧠 Optional deterministic ML refinement  
- 🛡️ CARE + sovereignty safe hazard spatialization  
- 🗂️ STAC-XAI hazard model metadata  
- 📜 PROV-O lineage for traceability  

This model powers:  
- Fire risk map tiles  
- Realtime fire-weather alerting  
- Multi-hazard composites  
- Focus Mode v3 hazard narratives  

---

## 🧬🔥⚙️ **Fire Weather Hazard Pipeline**

```mermaid
flowchart TD
    A[🌡️ Temperature Fields] --> D[📏 Normalize Inputs]
    B[💧 Relative Humidity] --> D
    C[🌬️ Wind Speed And Gusts] --> D
    E[🌾 Fuel Dryness + Soil Moisture Deficit] --> D
    D --> F[🔥 VPD And Fire Weather Index Calculation]
    F --> G[💡 XAI Attribution Layer]
    G --> H[🗂️ STAC XAI Metadata Packaging]
    H --> I[📊 Fire Weather Hazard Outputs]
```

---

## 🌡️💧🌬️ **Input Requirements**

### 1️⃣ 🌡️ Temperature  
- 2 m temp, 850 mb temp, or downscaled surface temp  
- Used for saturation vapor pressure  

### 2️⃣ 💧 Relative Humidity  
- Needed for actual vapor pressure  
- Optional dewpoint-based RH reconstruction  

### 3️⃣ 🌬️ Wind Speed & Gusts  
- 10 m wind  
- Derived gust fields  
- Critical for fire spread potential  

### 4️⃣ 🌾 Fuel Dryness  
- Derived from soil moisture deficit  
- Optional vegetation index modifiers  

### 5️⃣ 🗺️ Terrain  
- Slope  
- Aspect (south-facing slope dryness enhancement)  

All MUST include CRS, units, and ISO timestamps.

---

## 🔥🧮📈 **Core Hazard Formula (ASCII-Safe)**

### **1. Vapor Pressure Deficit (VPD)**  
```
es = 0.6108 * exp((17.27 * T) / (T + 237.3))
ea = es * (RH / 100)
VPD = es - ea
```

### **2. Fire Weather Index (FWI-like deterministic variant)**  
```
FWI = w1 * VPD_norm
    + w2 * wind_norm
    + w3 * fuel_dryness_norm
    + w4 * temp_norm
```

Weights MUST be deterministic and version-pinned.

---

## 📦📊🔥 **Outputs**

Model MUST produce:

- `fire_weather_grid.tif`  
- `fire_weather_metadata.json`  
- `fire_weather_summary.json`  
- Optional CAM-like attribution maps  
- STAC Item referencing all hazard drivers  
- Deterministic seeds  
- PROV-O lineage  
- CARE metadata block  

---

## 💡🧠🔥 **XAI Integration**

Fire-weather XAI MUST reveal:

- VPD contributions  
- Wind sensitivity  
- RH (moisture) impact  
- Fuel dryness weight  
- Terrain-driven amplification  
- CAM overlays across watersheds or fire polygons  

Example XAI excerpt:

```json
{
  "xai": {
    "importance": {
      "vpd": 0.52,
      "wind": 0.33,
      "fuel_dryness": 0.10,
      "temperature": 0.05
    },
    "seed": 42
  }
}
```

---

## 🛡️⚖️🔥 **CARE + Sovereignty Enforcement**

Fire-weather hazard maps MUST NOT expose hyperlocal hotspot patterns in sovereignty-protected regions.

Apply:

- **H3 hazard generalization**  
- Downsampling around sensitive ecological or tribal areas  
- Removal of high-risk detail where culturally sensitive  

CARE block example:

```json
{
  "care": {
    "masking": "h3-hazard-generalized",
    "scope": "public-generalized",
    "notes": ["Fire weather hotspots generalized in sovereignty-protected regions"]
  }
}
```

---

## 🔒⚙️🧪 **Determinism Requirements**

- Seed-locked operations  
- No stochastic hazard sampling  
- Deterministic wind adjustments  
- DEM slope/applications stable  
- Exact reproducibility under CI replay  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST verify:

- Deterministic FWI output  
- CRS + units present  
- XAI metadata complete  
- PROV lineage populated  
- STAC-XAI compliance  
- CARE + sovereignty block present  
- Telemetry (OTel, energy, carbon) attached  
- Weights fixed and version-pinned  

Fail → ❌ merge blocked.

---

## 🕰️📜 **Version History**

| Version  | Date       | Notes                                                |
|----------|------------|------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Fire Weather Hazard Model (MAX MODE)         |

---

<div align="center">

### 🔗 Footer  
[🌪️ Back to Hazards Pipeline](./README.md) ·  
[🔥 Fire Weather Models](./) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

