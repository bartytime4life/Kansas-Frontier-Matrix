---
title: "🌪️📈🤖 KFM v11.2.2 — Climate Driver Models (Hazard Forcing · Derived Metrics · XAI-Ready)"
path: "docs/pipelines/ai/inference/climate/models/drivers/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Model Subcategory · Climate Drivers"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256-checksum>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/climate-drivers-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-climate-drivers-v11.2.2.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../contracts/data-contract-v3.json"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-Driver-Models"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-drivers"
  - "hazard-forcing"
  - "meteorological-derivatives"
  - "storm-environment-metrics"
  - "thermodynamic-profiles"
  - "xai-ready-driver-models"
  - "seed-locked-deterministic"

scope:
  domain: "pipelines/ai/inference/climate/models/drivers"
  applies_to:
    - "cape-driver.md"
    - "cin-driver.md"
    - "llj-driver.md"
    - "shear-driver.md"
    - "instability-pack.md"
    - "storm-environment-drivers"
    - "derived-meteorological-indices"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_purpose_block: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌪️📈🤖 **Climate Driver Models — KFM v11.2.2**  
`docs/pipelines/ai/inference/climate/models/drivers/README.md`

**Purpose**  
Define the models that compute **derived meteorological driver fields** powering hazard prediction, dynamic narratives, and statewide climate intelligence layers.

</div>

---

## 📘 Overview

Driver models transform **primary fields** (temperature, dewpoint, wind, pressure, HRRR/ERA5 grids, downscaled fields) into **derived hazard-relevant metrics**, such as:

- CAPE (Convective Available Potential Energy)  
- CIN (Convective Inhibition)  
- SRH (Storm Relative Helicity)  
- LLJ (Low-Level Jet magnitude + depth)  
- Lapse rates (surface–3km, 700–500mb)  
- Moisture transport vectors  
- Dewpoint depressions  
- Fire-weather driver indices  
- Multi-driver instability composites  

Drivers feed:

- Hazard chains (fire, hail, severe convection)  
- AI inference stacks  
- Real-time climate tiles  
- Story Node v3 climatic context  
- Focus Mode v3 dynamic overlays  
- STAC-XAI v11 driver metadata  

All driver models MUST be:

- Deterministic (seed-locked)  
- XAI-compatible (SHAP/IG/CAM)  
- FAIR+CARE + sovereignty aligned  
- CRS + vertical-axis explicit  
- STAC-XAI v11 compliant  
- Fully reproducible with PROV-O lineage  

---

## 🗂️ Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/models/drivers/
        📄 README.md                 # This file
        📄 cape-driver.md            # CAPE model card
        📄 cin-driver.md             # CIN model card
        📄 llj-driver.md             # Low-Level Jet driver card
        📄 shear-driver.md           # Shear / SRH model card
        📄 instability-pack.md       # Multi-driver pack (instability suite)

---

## 🧩 Driver Model Categories

### ⚡ Thermodynamic Drivers  
- CAPE  
- CIN  
- LFC/LCL estimates  
- Moist static energy  

### 🌪️ Kinematic Drivers  
- Shear vectors  
- SRH (0–1km, 0–3km)  
- LLJ magnitude + height  

### 🔥 Fire-Weather Drivers  
- Vapor pressure deficit (VPD)  
- Dewpoint depression  
- Mixing height approximations  

### 🧮 Instability Packs  
Composite multi-driver products for:

- Severe storm instability  
- Dryline prediction  
- Fire-weather risk  
- Tornado-favorability layers  

---

## 🧬 Driver Pipeline Flow

```mermaid
flowchart TD
    A[Downscaled Climate Fields] --> B[Driver Model Loader]
    B --> C[Seed-Locked Derived Computation]
    C --> D[XAI Attribution (SHAP/IG/CAM)]
    D --> E[STAC-XAI Driver Metadata]
    E --> F[Telemetry + PROV-O Lineage]
```
<!-- mermaid-end -->

---

## 🎛 Model Requirements

Each driver model MUST specify:

- Derivation formula & metadata  
- Inputs (downscaled fields, HRRR/ERA5 fields)  
- Normalization/preprocessing  
- CRS + vertical formulation  
- Deterministic seed-lock config  
- Metrics: RMSE, MAE, corr, bias vs radiosonde truth (if applicable)  
- XAI compatibility (SHAP/IG/CAM)  
- Sustainability telemetry (Wh, gCO₂e)  
- FAIR+CARE + sovereignty review  
- Full STAC-XAI v11 asset definitions  
- PROV-O lineage chain  

---

## 🧪 CI Validation Requirements

CI MUST check:

- Model-card schema  
- Deterministic reproduction (test vector)  
- FAIR+CARE compliance  
- Sovereignty-safe configuration  
- CRS + vertical metadata presence  
- XAI-required fields  
- STAC-XAI v11 structure  
- PROV-O lineage correctness  

CI failure → 🚫 merge blocked.

---

## 🕰 Version History

| Version | Date       | Notes                                  |
| ------- | ---------- | -------------------------------------- |
| v11.2.2 | 2025-11-28 | Initial driver model documentation.    |

---

<div align="center">

### 🔗 Footer

[⬅ Back to Climate Models](../README.md) ·  
[🌡️ Climate Pipeline Root](../../README.md) ·  
[🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

