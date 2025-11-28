---
title: "⚡🟥🧪 KFM v11.2.2 — Hazard SHAP: Local Explainability (Event-Level Drivers · Per-Prediction Attribution)"
path: "docs/pipelines/ai/explainability/hazard/shap/local/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Hazard SHAP Local)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
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
sensitivity: "Explainability-Hazard-Local"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-shap-local"
  - "event-hazard-drivers"
  - "per-prediction-feature-importance"
  - "severe-weather-xai"
  - "wildfire-xai"
  - "flood-xai"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/hazard/shap/local"
  applies_to:
    - "local-hazard-shap"
    - "sample-driver-attribution"
    - "local-driver-codes"
    - "jsonld-hazard-xai"
    - "care-governance"
    - "h3-masking"
    - "prov-xai"
    - "story-node-xai"
    - "focus-mode-xai"

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

# ⚡🟥🧪 **Hazard SHAP — Local Explainability**  
`docs/pipelines/ai/explainability/hazard/shap/local/README.md`

**Purpose:**  
Provide **event-level hazard explainability** using SHAP for tornado, severe-storm, hail, wind, wildfire, and flood models.  
Outputs support **Story Node v3**, **Focus Mode v3**, and hazard-governance workflows by producing:

- Per-prediction hazard driver vectors  
- Local hazard-factor interpretations  
- CARE-masked geographic context  
- JSON-LD explainability bundles  
- STAC-XAI integration  
- PROV-linked lineage  

</div>

---

## 📘 Overview

Local SHAP hazard attribution answers:

- **“Why did the model predict this hazard intensity here and now?”**  
- **“Which environmental factors most influenced this specific event?”**  
- **“What meteorological, terrain, climate, or fuel signals mattered most?”**

Local SHAP is used for:

- Event-level hazard narratives  
- Focus Mode reasoning windows  
- Forensic hazard analysis  
- Governance & model-behavior review  
- Drift monitoring across updates  

Hazards covered:

- Tornado / rotation / shear  
- Wind & gust / LLJ  
- Hail & severe convection  
- Flood / flash-flood  
- Wildfire ignition & spread  
- Multi-hazard fusion  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/local/
    ├── 📄 README.md                            # This file
    │
    ├── 📄 local.json                            # Raw per-event SHAP vectors
    ├── 📄 samples.json                          # Optional curated local XAI examples
    │
    └── 📁 jsonld/                               # JSON-LD semantic explainability bundles
        ├── 📄 xai-shap-local.jsonld             # Local event driver evidence
        └── 📄 xai-shap-local-driver-codes.jsonld# Narrative-safe driver mapping

---

## 🔍 Local SHAP Components

### 1. 🟥 `local.json` — Per-Event SHAP Vectors  
Must include:

- Feature contributions (positive/negative)  
- Hazard variable mapping (CAPE, shear, PWAT, RH_low, NDVI, VPD, rainfall rate, etc.)  
- Normalized magnitudes  
- Driver confidence or robustness indicators  
- CARE masking indicators  
- Model version metadata  
- Input STAC Item IDs (if available)  

Used for:

- Event-level hazard reasoning  
- Drift detection  
- Narrative synthesis  

---

### 2. 🧪 `samples.json` — Curated Local Examples  
For internal testing, demos, and governance inspection:

- Multiple hazard scenarios  
- CARE-masked spatial patterns  
- Comparative driver behavior across events  

---

### 3. 🟩 JSON-LD Bundles (`/jsonld/`)

#### **`xai-shap-local.jsonld`**
Contains:

- Local driver list (`xai:drivers`)  
- H3-generalized spatial context  
- Hazard-domain labels  
- CARE scope metadata  
- PROV-O lineage  
- STAC fields:
  - `kfm:explainability:local`
  - `kfm:model_version`
  - `kfm:input_items`

Used by:

- Story Node v3 event narratives  
- Focus Mode local hazard reasoning  

#### **`xai-shap-local-driver-codes.jsonld`**
Maps **raw SHAP features → narrative-safe hazard driver codes**:

Examples:

- `TORNADO_SIGNAL_LOCAL`  
- `HAIL_GROWTH_ENV_LOCAL`  
- `WILDFIRE_DRYNESS_LOCAL`  
- `FLASHFLOOD_SOIL_SATURATION_LOCAL`  

Each entry must include:

- Driver code  
- CARE-filtered description  
- Linked SHAP features  
- Story Node role tags  
- Focus Mode reasoning tags  
- PROV linkage  

---

## 📡 STAC Integration Requirements

Local hazard SHAP must specify:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata (if spatial)  
- CARE & sovereignty metadata  
- PROV-O lineage  

---

## 🧾 PROV-O Lineage Requirements

Each explanation must include:

- `prov:wasGeneratedBy` (hazard model pipeline)  
- `prov:used` (STAC hazard/climate datasets)  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional: `prov:wasDerivedFrom` mapping raw → semantic drivers  

---

## 🔐 FAIR+CARE Requirements

Local SHAP outputs MUST:

- Use H3 generalization for geographic context  
- Mask/remove culturally sensitive hazard patterns  
- Include CARE scope + sovereignty metadata  
- Avoid speculative hazard causality  
- Respect all Data Contract v3 rules  
- Follow hazard ethics (e.g., wildfire & Indigenous stewardship zones)  

---

## 🧪 Testing Requirements

CI must validate:

- Deterministic local SHAP vectors  
- JSON-LD schema correctness  
- STAC-XAI compliance  
- CARE & sovereignty enforcement  
- CRS/vertical-axis correctness (if spatial)  
- Drift stability across model versions  
- PROV lineage completeness  

Fails → **merge blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                          |
|----------|------------|----------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard SHAP Local explainability spec aligned with suite |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard SHAP](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

