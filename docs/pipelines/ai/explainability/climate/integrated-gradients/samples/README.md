---
title: "🌡️🟩🧪 KFM v11.2.2 — Climate Integrated Gradients: Local / Sample-Level Attribution"
path: "docs/pipelines/ai/explainability/climate/integrated-gradients/samples/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Local IG)"

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
sensitivity: "Explainability-Local"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "local-ig"
  - "ig-samples"
  - "gradient-attribution"
  - "deep-model-xai"
  - "local-driver-analysis"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/integrated-gradients/samples"
  applies_to:
    - "ig-local"
    - "sample-level-attribution"
    - "ig-jsonld"
    - "ig-raster"
    - "story-node-xai"
    - "stac-xai"
    - "care-governance"
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

# 🌡️🟩🧪 **Climate Integrated Gradients — Sample-Level Attribution**  
`docs/pipelines/ai/explainability/climate/integrated-gradients/samples/README.md`

**Purpose:**  
Define the **sample-level Integrated Gradients (IG) explainability outputs** for climate models — producing highly localized gradient attributions, pixel/feature driver vectors, masked spatial evidence, and JSON-LD outputs used in **Story Node v3** and **Focus Mode v3** climate reasoning.

</div>

---

## 📘 Overview

Local/sample IG attribution provides:

- Per-inference gradient heatmaps  
- Per-pixel influence explanations  
- Specific variable contributions (temperature, precip, wind, terrain, etc.)  
- Time-step or location-specific climate reasoning  
- CARE-masked spatial patterns  
- Fully PROV-linked and STAC-compliant JSON-LD bundles  

These outputs help answer:

- *“Why did the model predict this climate outcome at this place/time?”*  
- *“Which variables mattered most locally?”*  
- *“What spatial patterns influenced this specific event?”*

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/integrated-gradients/samples/
    ├── 📄 README.md                               # This file
    │
    ├── 📄 ig-samples.json                         # Local IG vectors / maps
    ├── 📄 sample-metadata.json                    # Metadata (CRS, bounds, model-version, CARE)
    │
    └── 📁 jsonld/                                 # JSON-LD explainability bundles
        ├── 📄 xai-ig-local.jsonld                 # Local IG JSON-LD evidence
        └── 📄 xai-ig-local-driver-codes.jsonld    # Narrative-ready driver mapping

---

## 🔍 Local IG Explainability Components

### 1. 🟦 `ig-samples.json`
Contains localized gradient attributions:

- Pixel/feature influences  
- Per-sample magnitudes  
- Multi-modal driver signals  
- Time-step attribution (if applicable)  
- H3 masking for sensitive geography  
- Deterministic numerical arrays  

---

### 2. 🧾 `sample-metadata.json`
Contains supporting metadata:

- CRS + geometry  
- Vertical datum (if applicable)  
- Model version  
- Pipeline version  
- CARE scope & sovereignty notes  
- Input STAC IDs  
- Traceability for governance audits  

---

### 3. 🟩 JSON-LD Bundles (in `/jsonld`)

#### **`xai-ig-local.jsonld`**
Semantic IG explanation for a **single event**:

- Local driver contributions  
- Location + time context  
- Climate variable semantics  
- Provenance (`prov:*`)  
- CARE-masked descriptions  

#### **`xai-ig-local-driver-codes.jsonld`**
Narrative-friendly mapping:

- Top local drivers → semantic driver categories  
- Notes for Story Node v3  
- Focus Mode v3 reasoning integration  

---

## 📡 STAC Integration Requirements

Local IG attribution MUST include:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:local`  
- Model version + checksum  
- CRS + bounds (if spatial)  
- STAC input list (`kfm:input_items`)  
- Provenance references (`prov:*`)  

---

## 🧾 PROV-O Lineage Requirements

Each local IG artifact must include:

- `prov:wasGeneratedBy` (model + inference pipeline)  
- `prov:used` (STAC climate datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (pipeline identity)  
- Optional: `prov:wasDerivedFrom` (model → IG → narrative)

---

## 🔐 FAIR+CARE Requirements

Local IG outputs MUST:

- Mask sensitive geography (H3-based spatial abstraction)  
- Remove culturally sensitive terrain correlations  
- Include CARE scope metadata  
- Respect sovereignty policies  
- Avoid speculative causal explanations  

---

## 🧪 Testing Requirements

Local IG pipelines MUST pass:

- Determinism tests (identical inputs → identical IG maps)  
- JSON-LD schema validation  
- STAC extension validation  
- CRS + vertical axis validation  
- CARE masking and sovereignty rule tests  
- Drift baseline tests for IG stability  

---

## 🕰 Version History

| Version  | Date       | Notes                                                          |
|----------|------------|----------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Local IG explainability layer                  |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Integrated Gradients](../README.md) · [🌡️ Climate XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

