---
title: "🪴💧📉 KFM v11.2.2 — Soil Moisture Driver Model (Water Balance · Saturation Index · Deterministic · XAI 💡 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/inference/hydrology/soil-moisture-driver.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology Working Group 💧 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hydrology · Model Component · Soil Moisture Driver 🪴"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/hydrology-inference-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-hydrology-inference-v11.2.2.json"
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
care_label: "Public · Medium-Risk"
sensitivity: "Hydrology-Soil-Moisture"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "soil-moisture-driver"
  - "water-balance"
  - "root-zone-moisture"
  - "saturation-index"
  - "evapotranspiration"
  - "precip-infiltration"
  - "runoff-coupling"
  - "xai-hydrology"
  - "faircare-governance"
  - "stac-xai"
  - "prov-lineage"

scope:
  domain: "pipelines/ai/inference/hydrology"
  applies_to:
    - "soil-moisture-driver.md"
    - "runoff-driver.md"
    - "streamflow-driver.md"
    - "flood-index.md"
    - "drought-index.md"
    - "xai-hydrology.md"
    - "telemetry/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🪴💧📉 **Soil Moisture Driver Model**  
`docs/pipelines/ai/inference/hydrology/soil-moisture-driver.md`

**Purpose**  
Define the watershed-scale, deterministic, FAIR+CARE-governed **Soil Moisture Driver**, including:  
- **Absolute soil moisture** (surface & root-zone)  
- **Saturation index**  
- **Soil moisture anomaly**  
- **Water balance model integration**  
- **Hydrology XAI attribution maps**  
- **Sovereignty-safe watershed reporting**

Outputs feed the **Runoff Driver**, **Flood Index**, **Streamflow Driver**, and **Drought Index (SSI)**.

</div>

---

## 🪴📘💧 **Overview — Soil Moisture in Hydrology AI**

The Soil Moisture Driver uses:

- 🌧️ Precip intensity & accumulation  
- 🌤️ ET (evapotranspiration) & PET  
- 💦 Infiltration capacity  
- 🪨 Soil type & hydraulic conductivity  
- 🗺️ DEM terrain (slope, TWI)  
- 🌀 Runoff inputs (feedback)  
- 🌡️ Temperature + radiation forcing  
- 🧠 AI enhancements (deterministic) for infiltration & recharge  

It produces:

- Surface soil moisture  
- Root-zone soil moisture  
- Moisture anomaly  
- Saturation index  
- Slope-weighted wetness  

All outputs MUST be deterministic and seed-locked.

---

## 🗂️📁🪴 **Directory Placement (v11.2.2)**

```
docs/pipelines/ai/inference/hydrology/
    📄 soil-moisture-driver.md     # ← This file
    📄 runoff-driver.md
    📄 streamflow-driver.md
    📄 flood-index.md
    📄 drought-index.md
    📄 xai-hydrology.md
    📁 telemetry/
```

---

## 🧬💦⚙️ **Soil Moisture Pipeline Architecture**

```mermaid
flowchart TD
    A[🌧️ Precipitation] --> C[📏 Normalize Inputs]
    B[🌤️ ET / PET Fields] --> C
    C --> D[💦 Infiltration Calculation]
    D --> E[🪴 Soil Moisture Model]
    E --> F[📉 Soil Moisture Anomaly]
    F --> G[🧮 Saturation Index]
    G --> H[💡 XAI Attribution]
    H --> I[🗂️ STAC XAI Metadata Assembly]
```

---

## 🌡️🌧️💦 **Input Requirements**

### 1️⃣ 🌧️ Precipitation (P)
- Downscaled & bias-corrected  
- Hourly/daily cumulative precipitation  
- Intensities for infiltration vs runoff partitioning  

### 2️⃣ 🌤️ ET & PET
- Derived from climate fields  
- Required for water balance closure  

### 3️⃣ 🪴 Soil Type & Properties
- Hydraulic conductivity  
- Porosity  
- Field capacity & wilting point  

### 4️⃣ 🗺️ Terrain
- Slope  
- Flow direction  
- TWI  

### 5️⃣ 💧 Water-Balance Components
- Infiltration  
- Recharge  
- Baseflow coupling (optional)

All MUST include CRS, units, and temporal metadata.

---

## 🧮📉🪴 **Core Formulas (ASCII-Safe)**

### **Water Balance**
```
SM_t = SM_(t-1) + P - ET - runoff - drainage
```

### **Saturation Index**
```
Sat = SM / field_capacity
```

### **Soil Moisture Anomaly**
```
SM_anom = SM - climatology_SM
```

---

## 📦🗂️💧 **Outputs**

- `soil_moisture_grid.tif`  
- `soil_moisture_anomaly_grid.tif`  
- `saturation_index_grid.tif`  
- `soil_moisture_metadata.json`  
- `soil_moisture_summary.json`  
- STAC Item metadata (SM, anomaly, saturation)  
- PROV-O lineage  
- Deterministic seed metadata  
- CARE block  

---

## 💡🧠🪴 **XAI Integration**

Hydrology XAI MUST expose:

- Contributions: P, ET, PET, slope, soil type, infiltration  
- CAM overlays (watershed moisture sensitivity)  
- Feature-importance curves  
- Deterministic seed  
- XAI metadata embedded in STAC Items  

---

## 🛡️⚖️🧭 **CARE + Sovereignty Enforcement**

Soil moisture MUST:

- Apply watershed-scale H3 masking  
- Downsample sensitive ecological basins  
- Mask hyperlocal anomalies  
- Include sovereignty metadata:

```json
{
  "care": {
    "masking": "h3-watershed-generalized",
    "scope": "public-generalized",
    "notes": ["Soil moisture generalized in sovereignty-protected watersheds"]
  }
}
```

---

## 🔒⚙️🧪 **Determinism Rules**

- No stochastic infiltration  
- No random soil parameter perturbations  
- Seed-locked inference  
- Deterministic DEM derivatives  
- Fixed floating-point evaluation order  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST validate:

- CRS + units present  
- Deterministic water-balance calculations  
- XAI metadata complete  
- STAC-XAI validity  
- PROV lineage correct  
- CARE + sovereignty blocks included  
- Telemetry logs exist  
- Soil-property metadata included  

Failure → ❌ merge blocked.

---

## 🕰️📜 **Version History**

| Version  | Date       | Notes                                           |
|----------|------------|-------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Soil Moisture Driver (MAX MODE)        |

---

<div align="center">

### 🔗 Footer  
[💧 Back to Hydrology Pipeline](./README.md) ·  
[🌊 Hydrology Models](./) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

