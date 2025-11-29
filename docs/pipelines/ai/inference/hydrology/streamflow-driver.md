---
title: "🌊📈💧 KFM v11.2.2 — Streamflow Driver Model (Routing 🌐 · Discharge 📤 · Rise Rate ⚡ · Deterministic · XAI 💡 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/inference/hydrology/streamflow-driver.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology Working Group 💧 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hydrology · Model Component · Streamflow Driver 🌊"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
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
sensitivity: "Hydrology-Streamflow"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "streamflow-driver"
  - "discharge-modeling"
  - "rise-rate"
  - "routing"
  - "watershed-flow"
  - "rrhi-feedback"
  - "runoff-coupling"
  - "faircare-governance"
  - "stac-xai"
  - "prov-lineage"
  - "xai-hydrology"

scope:
  domain: "pipelines/ai/inference/hydrology"
  applies_to:
    - "streamflow-driver.md"
    - "runoff-driver.md"
    - "soil-moisture-driver.md"
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

# 🌊📈💧 **Streamflow Driver Model**  
`docs/pipelines/ai/inference/hydrology/streamflow-driver.md`

**Purpose**  
Define the deterministic, FAIR+CARE-enforced, watershed-scale **Streamflow Driver**, which converts  
runoff + soil moisture + terrain + routing metadata into **discharge (Q)**, **rise rate**, and **flow-state  
hazard indicators**.  
Feeds the **Flood Index**, **Drought Index (SSI)**, and Story Node v3 watershed narratives.

</div>

---

## 🌊📘💧 **Overview — Streamflow in the KFM Hydrology System**

Streamflow modeling integrates:

- 🌧️ Runoff depth & RRHI  
- 🪴 Soil moisture saturation  
- 🗺️ Flow accumulation & watershed routing  
- 🧭 DEM-based flow direction  
- 🌡️ ET & baseflow parameters  
- 🧠 Optional ML-enhanced flow magnitude (deterministic)  
- 🌀 Rapid-rise early warning (ΔQ/Δt)  

Outputs include **streamflow magnitude**, **rise-rate hazard**, and **flow-stage anomaly**.

---

## 🗂️📁🌊 **Directory Placement**

```
docs/pipelines/ai/inference/hydrology/
    📄 streamflow-driver.md      # ← This file
    📄 runoff-driver.md
    📄 soil-moisture-driver.md
    📄 flood-index.md
    📄 drought-index.md
    📄 xai-hydrology.md
    📁 telemetry/
```

---

## 🧬🌊⚙️ **Streamflow Driver Pipeline Architecture**

```mermaid
flowchart TD
    A[🌧️ Runoff Depth & RRHI] --> D[📏 Normalize Inputs]
    B[🪴 Soil Moisture Saturation] --> D
    C[🗺️ Watershed Routing] --> D
    D --> E[🌊 Deterministic Discharge Calculation]
    E --> F[⚡ Flow Rise Rate (ΔQ/Δt)]
    F --> G[💡 XAI Attribution]
    G --> H[🗂️ STAC XAI Metadata Assembly]
    H --> I[📊 Streamflow Outputs]
```

---

## 🌡️🧱🔧 **Inputs Required**

### 1️⃣ 🌧️ Runoff Inputs  
- Runoff depth  
- RRHI  
- Curve Number context  

### 2️⃣ 🪴 Soil Moisture Inputs  
- Absolute soil moisture  
- Saturation index  
- Anomaly  

### 3️⃣ 🗺️ Terrain Routing  
- Flow direction  
- Accumulation  
- Slope  
- Watershed boundaries  

### 4️⃣ 🌡️ ET / Baseflow  
- PET/ET  
- Baseflow coefficient (deterministic)

All MUST include CRS, units, and ISO-8601 timestamps.

---

## 📈🧮🌊 **Core Formulas (ASCII-Safe)**

### **Discharge (Q)**  
Deterministic Manning-based routing (example form):

```
Q = A * (R^(2/3)) * sqrt(S)
```

Where:  
- `A` = contributing area  
- `R` = hydraulic radius  
- `S` = slope  

### **Rise Rate (ΔQ/Δt)**

```
rise_rate = (Q_t - Q_(t-1)) / Δt
```

---

## 📦🗂️💧 **Outputs**

Streamflow driver MUST produce:

- `streamflow_grid.tif`  
- `streamflow_rise_rate_grid.tif`  
- `streamflow_metadata.json`  
- `streamflow_summary.json`  
- STAC Item with hydrology metadata  
- Deterministic seed info  
- PROV lineage  
- CARE compliance block  

---

## 💡🧠🌊 **XAI Integration**

XAI MUST reveal:

- Influence of runoff  
- Contribution of soil moisture  
- Terrain routing sensitivity  
- Slope and DEM-derived factors  
- ΔQ/Δt attribution maps  
- Watershed hotspot visualizations  
- Deterministic seed metadata  
- STAC-XAI assets  

---

## 🛡️⚖️🧭 **CARE + Sovereignty Enforcement**

Streamflow outputs MUST:

- Apply H3 watershed generalization  
- Smooth discharge maxima in protected basins  
- Mask hyperlocal rise-rate spikes  
- Include sovereignty-safe metadata:

```json
{
  "care": {
    "masking": "h3-watershed-generalized",
    "scope": "public-generalized",
    "notes": ["Streamflow and rise-rate generalized in sovereignty-protected watersheds"]
  }
}
```

---

## 🔒⚙️🧪 **Determinism Requirements**

- No stochastic routing  
- No random hydraulic coefficients  
- Fixed DEM derivatives  
- Seed-lock full inference pipeline  
- Reproducible rise-rate calculations  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST ensure:

- CRS + units valid  
- Deterministic routing results  
- Streamflow grids + rise-rate grids present  
- XAI metadata complete  
- STAC-XAI compliance  
- PROV lineage populated  
- CARE block included  
- Telemetry files attached  
- No missing hydrology drivers  

Failure → ❌ merge blocked.

---

## 🕰️📜 **Version History**

| Version  | Date       | Notes                                         |
|----------|------------|-----------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Streamflow Driver (MAX MODE)          |

---

<div align="center">

### 🔗 Footer  
[💧 Back to Hydrology Pipeline](./README.md) ·  
[🌊 Hydrology Models](./) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

