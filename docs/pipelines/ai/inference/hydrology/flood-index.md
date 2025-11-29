---
title: "🌊⚠️📈💧 KFM v11.2.2 — Flood Index Model (Runoff 🌧️ · Streamflow 🌊 · Soil Moisture 🪴 · Slope 🗺️ · Deterministic ⚙️ · XAI 💡 · FAIR+CARE 🛡️)"
path: "docs/pipelines/ai/inference/hydrology/flood-index.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology Working Group 💧 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Hydrology · Model Component · Flood Index ⚠️🌊"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
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
sensitivity: "Hydrology-Flood-Index"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "flood-index"
  - "runoff-surges"
  - "flash-flooding"
  - "soil-moisture-saturation"
  - "streamflow-rise"
  - "watershed-hazards"
  - "faircare-governance"
  - "stac-xai"
  - "prov-lineage"
  - "deterministic-hydrology"
  - "xai-hydrology"

scope:
  domain: "pipelines/ai/inference/hydrology"
  applies_to:
    - "flood-index.md"
    - "runoff-driver.md"
    - "soil-moisture-driver.md"
    - "streamflow-driver.md"
    - "drought-index.md"
    - "xai-hydrology.md"
    - "telemetry/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌊⚠️📈💧 **Flood Index Model (FFI/FPI) — Hydrology AI**  
`docs/pipelines/ai/inference/hydrology/flood-index.md`

**Purpose**  
Define the deterministic, XAI-ready, sovereignty-aware **Flood Index model** for the KFM Hydrology  
Inference System.  
Integrates **runoff surges**, **soil moisture saturation**, **streamflow rise rates**, **terrain slope**,  
and **precipitation bursts**, producing watershed-scale flood hazard indicators for:  
- Realtime hazard monitoring ⚠️  
- Flash-flood risk analytics 🌊  
- Story Node v3 hydrology narratives 📖  
- Focus Mode v3 watershed overlays 🧠  

All outputs MUST follow **FAIR+CARE**, **PROV-O**, **STAC-XAI**, and **KFM-PDC v11** requirements.

</div>

---

## 🌧️🌊📈 **Overview — The Flood Index Concept**

Flood Index (FI) provides a composite hazard score by blending:

- 🌧️ **Rainfall intensity** (rate, duration, burstiness)  
- 💦 **Soil moisture saturation** (absolute + anomaly)  
- 🌊 **Streamflow magnitude & rise rate**  
- 🗺️ **DEM terrain slope & flow direction**  
- 🌪️ **Runoff surges** (RRHI)  
- 🌫️ **Antecedent wetness** (short/long window)  

The result: a deterministic, interpretable, multi-factor watershed hazard indicator.

---

## 🗂️📁🌧️ **File Placement (Hydrology Model Layout)**

```
docs/pipelines/ai/inference/hydrology/
    📄 flood-index.md               # ← This file
    📄 runoff-driver.md
    📄 soil-moisture-driver.md
    📄 streamflow-driver.md
    📄 drought-index.md
    📄 xai-hydrology.md
    📁 telemetry/
```

---

## 🧬🌧️🌀 **Flood Index Pipeline Architecture**

```mermaid
flowchart TD
    A[🌧️ Precip Intensity & Accumulations] --> D[📏 Normalization]
    B[💦 Soil Moisture Saturation] --> D
    C[🌊 Streamflow Rise Rate] --> D
    E[🗺️ Slope & Terrain Routing] --> D
    D --> F[⚡ Deterministic Composite Calculation]
    F --> G[💡 XAI Attribution]
    G --> H[🗂️ STAC XAI Metadata Assembly]
    H --> I[📊 Flood Index Outputs]
```

---

## 🌡️📊⚙️ **Model Inputs**

### 1️⃣ 🌧️ **Precipitation Inputs**
- Intensity (mm/hr)  
- Burst index  
- Rolling-window accumulations  

### 2️⃣ 💦 **Soil Moisture Inputs**
- Multi-layer soil moisture  
- Anomaly from climatology  
- Saturation index  

### 3️⃣ 🌊 **Streamflow Inputs**
- Discharge magnitude  
- Rise rate (ΔQ/Δt)  
- Routing metadata  

### 4️⃣ 🗺️ **Terrain Inputs**
- Slope  
- Flow direction  
- TWI (topographic wetness index)  

Each MUST include:  
- CRS (`EPSG:4326`)  
- Units  
- Temporal metadata (ISO 8601)  

---

## ⚡🧮📉 **Flood Index Formula (ASCII-Safe)**

Composite hazard calculation:

```
FI =
    w1 * runoff_norm
  + w2 * soil_sat_norm
  + w3 * streamflow_rise_norm
  + w4 * slope_norm
  + w5 * precip_burst_norm
```

Where:

- `w1…w5` are deterministic weights (seed-locked)  
- All `_norm` values are standardized per watershed  

Runoff normalization:

```
runoff_norm = (runoff - mean_runoff) / std_runoff
```

Streamflow rise rate:

```
rise_norm = (ΔQ/Δt) / rise_scale
```

---

## 📦🗂️🌊 **Outputs**

Flood Index model MUST produce:

- `flood_index_grid.tif` (COG)  
- `flood_index_metadata.json`  
- `flood_index_summary.json`  
- STAC Item with FI metadata  
- Deterministic seeds  
- PROV-O lineage  
- CARE metadata  

---

## 💡🧠📈 **XAI Integration for Flood Index**

XAI MUST reveal:

- Contribution of precip intensity  
- Slope influence on hazard distribution  
- Soil moisture impact weight  
- Runoff/streamflow interplay  
- Deterministic attribution maps  
- Feature importance tables  
- STAC-XAI linking  

XAI artifacts include:

- CAM overlays  
- Hydrology variable contribution bars  
- Watershed hotspot maps  

---

## 🛡️⚖️🧭 **CARE + Sovereignty Enforcement**

Flood Index MUST NOT reveal hyperlocal hazards inside protected tribal or ecological basins.

Thus:

- Apply **H3 watershed generalization**  
- Reduce spatial precision of FI maxima  
- Attach sovereignty-safe metadata:

```json
{
  "care": {
    "masking": "h3-watershed-generalized",
    "scope": "public-generalized",
    "notes": ["Flood Index generalized within sovereignty-protected watersheds"]
  }
}
```

---

## 🔒⚙️🧪 **Determinism Requirements**

Flood Index MUST follow:

- Fixed seed operations  
- Deterministic normalization  
- No random ensemble simulations  
- Reproducible floating-point operations  
- Deterministic watershed boundaries  

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST validate:

- CRS + units  
- Deterministic FI output  
- XAI metadata  
- STAC-XAI compliance  
- PROV lineage completeness  
- CARE block present  
- No missing drivers  
- All watershed boundaries respected  
- Energy + carbon telemetry present  

Failure → ❌ merge blocked.

---

## 🕰️📜 **Version History**

| Version  | Date       | Notes                                           |
|----------|------------|-------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Flood Index documentation (MAX MODE)    |

---

<div align="center">

### 🔗 Footer  
[💧 Back to Hydrology Pipeline](./README.md) ·  
[🌊 Hydrology Models](./) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

