---
title: "🏜️📉💧 KFM v11.2.2 — Drought Index Model (SPI 🌡️ · SPEI 🌤️ · SSI 💦 · Deterministic · FAIR+CARE 🛡️ · XAI 💡)"
path: "docs/pipelines/ai/inference/hydrology/drought-index.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hydrology Working Group 💧 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Component · Hydrology · Drought Index (SPI/SPEI/SSI)"

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
sensitivity: "Hydrology-Drought-Index"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "drought-index"
  - "spi"
  - "spei"
  - "ssi"
  - "hydrology-drought"
  - "water-balance"
  - "precip-evap-deficit"
  - "soil-moisture-deficit"
  - "faircare-governance"
  - "stac-xai"
  - "prov-lineage"

scope:
  domain: "pipelines/ai/inference/hydrology"
  applies_to:
    - "drought-index.md"
    - "runoff-driver.md"
    - "soil-moisture-driver.md"
    - "streamflow-driver.md"
    - "flood-index.md"
    - "xai-hydrology.md"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🏜️📉💧 **Drought Index Model (SPI · SPEI · SSI)**  
`docs/pipelines/ai/inference/hydrology/drought-index.md`

**Purpose**  
Define the deterministic **drought index modeling** subsystem for KFM hydrology inference, including  
**SPI (Standardized Precipitation Index)**, **SPEI (Standardized Precipitation–Evapotranspiration Index)**,  
and **SSI (Soil Moisture Index)**.  
Outputs support drought monitoring, agricultural intelligence, hazard-chain context, and  
Story Node v3 environmental narratives — all under FAIR+CARE + sovereignty governance.

</div>

---

## 💧📘🏜️ **Overview — Drought Modeling in KFM**

The Drought Index System integrates climate + hydrology fields:

- 🌧️ Precipitation (downscaled, bias-corrected)  
- 🌤️ Evapotranspiration (PET/ET)  
- 💦 Soil moisture (absolute + anomaly)  
- 🌡️ Temperature (for SPEI energy balance)  
- 🗺️ Watershed-level flow + soil type properties  
- 🧭 Multi-timescale rolling windows (1/3/6/12/24 months)  
- 🧠 AI-enhanced drought tendency indicators  
- 🛡️ CARE + sovereignty-safe drought dissemination  

Outputs are deterministic, seed-locked, and aligned to STAC-XAI + PROV-O.

---

## 🗂️📁🏜️ **Drought Index Directory Layout (v11.2.2)**

```
docs/pipelines/ai/inference/hydrology/
    📄 drought-index.md           # ← This file (MAX EMOJI MODE)
    📄 runoff-driver.md
    📄 soil-moisture-driver.md
    📄 streamflow-driver.md
    📄 flood-index.md
    📄 xai-hydrology.md
    📁 telemetry/
```

---

## 🧬📈🌧️ **Drought Index Pipeline**

```mermaid
flowchart TD
    A[🌧️ Precipitation Series] --> C[📏 Rolling Window Aggregation]
    B[🌤️ PET/ET Series] --> C
    C --> D[📉 Compute Anomaly]
    D --> E[🏜️ SPI / SPEI Calculation]
    E --> F[💦 Optional SSI Integration]
    F --> G[🛡️ CARE & Sovereignty Filters]
    G --> H[🗂️ STAC XAI Metadata Assembly]
    H --> I[📊 Drought Index Outputs]
```

---

## 🌡️📉📊 **Model Types & Formulas**

### 1️⃣ **SPI — Standardized Precipitation Index**
Based on **precip-only** deficits:

```
SPI = (P - mean_P) / std_P
```

### 2️⃣ **SPEI — Standardized Precipitation–Evapotranspiration Index**
Water-balance driven:

```
D = P - PET
SPEI = (D - mean_D) / std_D
```

### 3️⃣ **SSI — Soil Moisture Index**
Hydrologically grounded:

```
SSI = (SM - mean_SM) / std_SM
```

Where:  
- `P` = precipitation  
- `PET` = potential evapotranspiration  
- `SM` = soil moisture  

All windows MUST be seed-locked + reproducible.

---

## 🧱🔧💧 **Input Requirements**

### 🌧️ Precipitation  
- Downscaled, bias-corrected  
- Daily/monthly granularity  

### 🌤️ ET/PET  
- Derived from temperature, humidity, solar radiation  

### 💦 Soil Moisture  
- Absolute + anomaly fields  
- Watershed-scale smoothing  

### 🗺️ Metadata  
- CRS (`EPSG:4326`)  
- Units (`mm`, `mm/day`, `mm/month`, etc.)  
- Temporal precision  

---

## 📦🗂️📉 **Outputs**

- `drought_spi_grid.tif`  
- `drought_spei_grid.tif`  
- `drought_ssi_grid.tif`  
- `drought_index_metadata.json`  
- `drought_index_summary.json`  
- STAC Items (SPI/SPEI/SSI)  
- Deterministic seeds  
- PROV-O lineage  
- CARE metadata block  

---

## 💡🧠🌍 **XAI for Drought Index**

XAI MUST include:

- Variable contributions (P, ET, SM, PET deficits)  
- Sensitivity to rolling-window width  
- CAM overlays for watershed dryness patterns  
- Deterministic attribution grids  
- Full XAI metadata in STAC Items  

---

## 🛡️⚖️🧭 **CARE + Sovereignty Enforcement**

Drought indices MUST:

- Smooth sensitive watershed regions  
- Avoid disclosing hyperlocal dryness anomalies  
- Apply H3 watershed masking  
- Include sovereignty-safe metadata:

```json
{
  "care": {
    "masking": "h3-watershed-generalized",
    "scope": "public-generalized",
    "notes": ["Drought metrics generalized in sovereignty-protected basins"]
  }
}
```

---

## 🧪🔬📏 **CI Validation Requirements**

CI MUST validate:

- Deterministic rolling-window computation  
- CRS + units correctness  
- PROV-O completeness  
- STAC-XAI metadata correctness  
- CARE block always present  
- No missing drought index variables  
- Energy + carbon telemetry included  
- Metadata schemas pass validation  

Failure → ❌ merge blocked.

---

## 🕰️📜 **Version History**

| Version  | Date       | Notes                                       |
|----------|------------|----------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial drought-model documentation (MAX MODE) |

---

<div align="center">

### 🔗 Footer  
[💧 Back to Hydrology Pipeline](./README.md) ·  
[🌊 Hydrology Drivers](./) ·  
[🏛 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

