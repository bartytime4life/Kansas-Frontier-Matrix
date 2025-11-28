---
title: "🌡️🟩📈 KFM v11.2.2 — Climate Integrated Gradients: Global Attribution"
path: "docs/pipelines/ai/explainability/climate/integrated-gradients/global/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Global IG)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/climate-explainability-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-explainability-climate-v11.2.2.json"
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
sensitivity: "Explainability"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-xai-global-ig"
  - "gradient-attribution"
  - "deep-model-xai"
  - "global-driver-maps"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/integrated-gradients/global"
  applies_to:
    - "global-ig"
    - "aggregate-gradient-attribution"
    - "xai-jsonld"
    - "xai-stac"
    - "faircare-governance"
    - "prov-xai"
    - "h3-masking"

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

# 🌡️🟩📈 **Climate Integrated Gradients — Global Attribution**  
`docs/pipelines/ai/explainability/climate/integrated-gradients/global/README.md`

**Purpose:**  
Define the **global Integrated Gradients (IG)** explainability outputs for climate deep-learning models, representing global feature influence, aggregate gradient attribution, spatial abstractions, and JSON-LD/STAC-ready global driver evidence used in **Story Node v3**, **Focus Mode v3**, and climate governance workflows.

</div>

---

## 📘 Overview

Global Integrated Gradients (IG) attribution aggregates gradient-based explanations across **many samples, timesteps, or spatial regions**, producing a **model-wide understanding** of:

- What climate variables drive predictions  
- How terrain, hydrology, land cover, atmosphere, and climate interact  
- Which spatial patterns matter most across Kansas  
- What features dominate long-term climate behavior  

Global IG → **global climate driver vectors** → **STAC v11 XAI** → **Story Node v3** reasoning.

Outputs must be:

- Deterministic  
- Reproducible  
- JSON-LD structured  
- CARE-masked  
- CRS-correct  
- Provenance-linked  
- Compatible with all XAI template schemas  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/integrated-gradients/global/
    ├── 📄 README.md                     # This file
    │
    ├── 📄 ig-global.json                # Raw aggregated IG driver values
    ├── 📄 summary.md                    # Human-readable global driver summary
    │
    └── 📁 jsonld/                       # JSON-LD explainability bundles
        ├── 📄 xai-ig-global.jsonld      # Semantic global XAI bundle
        └── 📄 xai-ig-driver-codes.jsonld# Narrative-ready driver mapping

---

## 🔍 Component Specification

### 1. 🟥 `ig-global.json`
Raw aggregated IG values across:

- Many spatial locations  
- Multiple climate timesteps  
- Full training/validation sets  

Must include:

- Normalized driver magnitudes  
- Feature relevance rank  
- Model version metadata  
- CRS metadata (if spatial)  
- CARE masking indicators (for spatial drivers)  

---

### 2. 🧾 `summary.md`
Human-readable global attribution summary including:

- Ranked global climate drivers  
- Interaction explanations (e.g., terrain × temperature)  
- Climate-domain semantic notes  
- CARE + sovereignty notes  
- Data sources & STAC links  
- Drift-monitoring notes (e.g., “driver inversion change”)  

Used by:

- Governance reviewers  
- Story Node editorial tooling  
- Explainability dashboards  

---

### 3. 🟩 JSON-LD Bundles (in `/jsonld`)
These files capture:

#### **`xai-ig-global.jsonld`**
- Global climate driver evidence  
- PROV-O metadata (`prov:*`)  
- Model version  
- Inputs: STAC Items  
- CARE scope  
- Sovereignty flags  
- Semantic driver codes  

#### **`xai-ig-driver-codes.jsonld`**
Maps IG global drivers → narrative-safe driver categories:

- Climate variable semantic class  
- Aggregated spatial/temporal influences  
- CARE-filtered narrative versions  
- Story Node v3 alignment  

---

## 📡 STAC Integration Requirements

Global IG outputs MUST include:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:global`  
- Model version  
- Input STAC `kfm:input_items`  
- CRS + geometry (if spatial)  
- Multihash checksums  
- Provenance links (`prov:*`)  

---

## 🧾 PROV-O Lineage Requirements

Every global IG asset must include:

- `prov:wasGeneratedBy` (training/inference run)  
- `prov:used` (input climate STAC datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity + version)  
- `prov:wasDerivedFrom` (model → IG → Story Node path)  

---

## 🔐 FAIR+CARE Requirements

Global IG outputs MUST:

- Use H3 generalization for CARE-restricted locations  
- Avoid climate-driver interpretations tied to cultural identity  
- Respect sovereignty constraints  
- Remove sensitive terrain correlations where applicable  
- Include CARE scope metadata  

---

## 🧪 Testing Requirements

CI must validate:

- Deterministic global IG outputs  
- JSON-LD schema conformance  
- PROV-O lineage  
- STAC XAI extension fields  
- CRS/vertical metadata  
- CARE masking correctness  
- Driver-ranking drift tests  

Failures → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                        |
|----------|------------|------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Global IG explainability layer; aligned with full Climate XAI suite  |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Integrated Gradients](../README.md) · [🌡️ Climate XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

