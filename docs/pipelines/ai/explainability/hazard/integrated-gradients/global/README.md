---
title: "⚡🟩📈 KFM v11.2.2 — Hazard Integrated Gradients: Global Explainability (Deep Hazard Drivers · Gradient Attribution)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/global/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Hazard IG Global)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

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
sensitivity: "Explainability-Hazard-Global-IG"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ig-global"
  - "gradient-attribution-hazard"
  - "deep-hazard-model-explainability"
  - "global-driver-analysis"
  - "prov-xai"
  - "stac-xai"
  - "story-node-hazard"
  - "focus-mode-hazard"

scope:
  domain: "explainability/hazard/integrated-gradients/global"
  applies_to:
    - "hazard-ig-global-attribution"
    - "hazard-ig-global-jsonld"
    - "hazard-driver-codes"
    - "care-governance"
    - "h3-masking"
    - "prov-xai"
    - "stac-xai"
    - "narrative-driver-mapping"

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

# ⚡🟩📈 **Hazard Integrated Gradients — Global Explainability**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/global/README.md`

**Purpose:**  
Define the global Integrated Gradients (IG) explainability layer for deep hazard models (tornado, hail, wind, flood, wildfire, multi-hazard), producing **system-wide gradient attribution**, **semantic driver bundles**, **FAIR+CARE-governed JSON-LD**, and **PROV-linked STAC v11 XAI assets** for Story Node v3 and Focus Mode v3.

</div>

---

## 📘 Overview

Global IG attribution reveals **which environmental, meteorological, hydrological, and terrain-related features** drive hazard model behavior across Kansas.

Applicable hazard domains:

- 🌀 Tornado — SRH, EHI, shear, rotation  
- 💨 Wind/Gust — LLJ alignment, pressure gradients  
- 🌩️ Hail/Severe — lapse rates, updraft proxies, CAPE  
- 🌧️ Flood/Flash-Flood — soil saturation, runoff, precip intensity  
- 🔥 Wildfire — VPD, fuel dryness, wind alignment  
- ⚡ Multi-hazard fusion — joint interactions across domains  

IG is essential for deep-learning models where SHAP cannot capture spatiotemporal gradients.

Outputs include:

- Global IG driver vectors  
- Gradient-based feature importance  
- Semantic hazard-driver interpretations  
- JSON-LD evidence bundles  
- CARE-safe spatial abstractions  
- PROV-O lineage  
- STAC-XAI metadata  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/integrated-gradients/global/
    ├── 📄 README.md                         # This file
    │
    ├── 📄 ig-global.json                    # Raw aggregated IG results (gradient magnitudes)
    ├── 📄 summary.md                        # Narrative-safe global driver explanation
    │
    └── 📁 jsonld/                           # JSON-LD global explainability bundles
        ├── 📄 xai-ig-global.jsonld          # Semantic IG global driver bundle
        └── 📄 xai-hazard-ig-driver-codes.jsonld # Narrative-safe hazard driver taxonomy

---

## 🔍 Component Definitions

### 1. 🟥 `ig-global.json` — Raw IG Global Attribution
Must include:

- Normalized IG magnitudes for all hazard-relevant features  
- Ranked driver order  
- Hazard-domain labels  
- H3-masked spatial abstractions (if any spatial encoding exists)  
- Model + pipeline version metadata  
- Checksums for deterministic tracking  

Used for:

- Deep hazard model inspection  
- Governance & drift monitoring  
- Downstream narrative driver extraction  

---

### 2. 🧾 `summary.md` — Human-Readable Hazard Driver Explanation  
Contains governance-safe analysis describing:

- Which hazard drivers dominate  
- Cross-domain interactions (e.g., CAPE × shear, VPD × fuels)  
- Seasonal/meteorological context  
- CARE & sovereignty considerations  
- Model lineage + STAC dataset references  

Used by:

- Hazard experts  
- Story Node editors  
- Focus Mode content validation  
- Governance review panels  

---

### 3. 🟩 JSON-LD Bundles (`/jsonld/`)

#### **`xai-ig-global.jsonld`**
Semantic representation of global hazard IG attribution:

- `xai:drivers` — global list of hazard drivers  
- `xai:importance` — normalized gradients  
- `xai:hazard_domain` — tornado|wind|hail|wildfire|flood|multi  
- `xai:spatial_context` — H3-generalized  
- CARE scope metadata  
- PROV-O lineage  
- STAC-XAI references (`kfm:model_version`, `kfm:input_items`)  
- Integrity via `checksum:multihash`  

#### **`xai-hazard-ig-driver-codes.jsonld`**
Narrative-safe taxonomy mapping raw IG drivers → semantic hazard interpetation:

Driver codes include templates such as:

- `TORNADO_SIGNAL_IG`  
- `SEVERE_CONVECTION_IG`  
- `WILDFIRE_DRYNESS_IG`  
- `FLASHFLOOD_SATURATION_IG`  
- `EXTREME_WIND_SHEAR_IG`  

Fields include:

- Description (CARE-safe)  
- Linked features  
- Story Node semantic roles  
- Focus Mode tags  
- CARE & sovereignty annotations  
- PROV linkage  

---

## 📡 STAC Integration Requirements

Global IG hazard explainability must include:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:global`  
- `kfm:model_version`  
- `kfm:input_items` (STAC IDs of model inputs)  
- `checksum:multihash`  
- CRS/vertical metadata (if spatial)  
- CARE + sovereignty metadata  
- PROV linkage  

---

## 🧾 PROV-O Lineage Requirements

Each global IG output MUST include:

- `prov:wasGeneratedBy` — hazard inference pipeline  
- `prov:used` — STAC hazard/climate datasets  
- `prov:generatedAtTime`  
- `prov:Agent` — model + executor identity  
- Optional: `prov:wasDerivedFrom` for IG ↔ SHAP ↔ narrative alignment  

---

## 🔐 FAIR+CARE Requirements

Hazard IG outputs MUST:

- Use **H3 generalization** for any spatial references  
- Mask or abstract culturally sensitive hazard geography  
- Include CARE scope & sovereignty metadata  
- Avoid speculation regarding hazard causality  
- Respect Data Contract v3 and vertical-axis rules  
- Use governance-audited terminology only  

---

## 🧪 Testing Requirements

CI MUST enforce:

- Deterministic IG global outputs  
- JSON-LD schema + KFM-XAI validation  
- STAC-XAI extension compliance  
- CARE + sovereignty rule enforcement  
- CRS/vertical metadata correctness  
- Global-driver drift detection  
- PROV-O lineage completeness  

Failure → **merge blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                              |
|----------|------------|--------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard IG Global explainability spec aligned with suite    |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard IG](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

