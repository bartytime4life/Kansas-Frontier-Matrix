---
title: "🔍 KFM v11.2.2 — AI Explainability Pipelines (XAI · SHAP · Attribution · Provenance · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability Engineering"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Pipeline Layer"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/ai-explainability-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/ai-explainability-v11.2.2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

care_label: "Public · Medium-Risk"
fair_category: "F1-A1-I1-R1"
sensitivity: "AI-Derived Signals"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"

semantic_intent:
  - "explainability"
  - "xai"
  - "interpretability"
  - "provenance"
  - "ai-audits"

scope:
  domain: "ai-explainability"
  applies_to:
    - "shap"
    - "lime"
    - "integrated-gradients"
    - "saliency"
    - "xai-stac-metadata"
    - "story-node-xai"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🔍 **KFM v11.2.2 — AI Explainability Pipelines**  
`docs/pipelines/ai/explainability/README.md`

**Purpose:**  
Define the **explainability (XAI) layer** for all AI/ML models in the Kansas Frontier Matrix, including SHAP, LIME, saliency maps, Integrated Gradients, and domain-specific interpretability.  
These pipelines ensure **traceable, auditable, FAIR+CARE-compliant explanations**, embedded directly into **STAC Items**, **Story Nodes**, and **Focus Mode v3** narratives.

</div>

---

## 📘 Overview

All predictive and generative AI in the KFM ecosystem MUST produce **explainability artifacts** that:

- Reveal why a model predicted what it predicted  
- Support **FAIR+CARE oversight**  
- Enable **scientific validation**  
- Drive **Story Node v3** narrative attribution  
- Prevent misuse of AI (e.g., invisible or unjustified inference steps)  

XAI outputs are stored as:

- **STAC Item fields** (`kfm:explainability:*`)  
- **JSON-LD explainability graphs**  
- **Story Node linked evidence**  
- **OpenTelemetry spans** with attribution metadata  

Explainability is not optional — it is a **governed guarantee** of KFM v11.2.2.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/
    ├── 📄 README.md                              # This file
    │
    ├── 📁 climate/                               # Climate AI explainability
    │   ├── 📄 shap-example.json
    │   └── 📄 feature-attribution.md
    │
    ├── 📁 hydrology/                             # Hydrology AI explainability
    │   ├── 📄 integrated-gradients.json
    │   └── 📄 saliency-map.png
    │
    ├── 📁 hazard/                                # Wildfire / severe weather XAI
    │   ├── 📄 shap-factors.json
    │   └── 📄 interpretability-rules.md
    │
    └── 📁 templates/                             # Generic explainability templates
        ├── 📄 xai-metadata-template.jsonld
        └── 📄 model-explainability-sop.md

---

## 🧩 Explainability Components (v11.2.2)

### 1. 🟥 SHAP (Tree, Deep, Kernel)
- Global feature importance  
- Local explanation vectors  
- Mandatory for:
  - Climate forecasts  
  - Hydrology predictions  
  - Hazard/wildfire probability models  

### 2. 🟦 LIME
- Surrogate model explanation  
- Useful for NLP entity extraction or text-based predictions  
- Recommended for ambiguous or multi-class pipelines  

### 3. 🟩 Integrated Gradients
- Gradient-based interpretability for deep models  
- Required for:
  - DEM-based neural models  
  - Landform or hydrology CNNs  
  - Any model dependent on elevation rasters  

### 4. 🟨 Saliency Maps & CAMs
- Visual relevance maps for spatial ML  
- Used for remote-sensing models and geospatial classifiers  

### 5. 🟪 KFM-XAI Narrative Mapping
- Maps explanations into:
  - Story Node narrative fields  
  - Focus Mode context windows  
  - KFM ontology terms (CIDOC-CRM aligned)  
- Sources are always data-grounded, never speculative  

---

## 📡 STAC Integration (KFM-STAC v11)

Every AI output that becomes a STAC Item MUST include:

- `kfm:explainability:method`  
- `kfm:explainability:drivers`  
- `kfm:explainability:saliency` (if geospatial/imagery)  
- `kfm:explainability:local_factors` (JSON-LD)  
- `kfm:explainability:global_factors`  

All XAI artifacts are stored:

- As sidecar JSON / JSON-LD  
- Inside Story Node derivations  
- As lineage-supporting OpenLineage facets  

---

## 🧭 Story Node & Focus Mode Integration

### Story Nodes (v3)

XAI outputs enrich Story Nodes by:

- Highlighting which features influenced the interpretation  
- Recording the model’s confidence intervals  
- Embedding masked / abstracted spatial explanations  
- Allowing reviewers to trace:
  - **data → model → explanation → narrative**

### Focus Mode (v3)

- Each Focus summary can cite XAI fields  
- All explanations undergo CARE masking  
- Explanations affecting Indigenous or heritage-related features **MUST** use:
  - H3 generalization  
  - Conceptual (non-locational) abstractions  

---

## 🧮 Testing Requirements

Explainability outputs MUST pass:

- XAI schema validation  
- Explainability–provenance consistency checks  
- Drift testing (feature attribution must remain stable across releases)  
- Sensitivity testing for CARE masking  
- Reproducibility checks (given same seed + model)

PRs failing any requirement → **blocked**.

---

## 🪜 Operational Requirements

- All XAI pipelines must emit OTel spans annotated with:
  - `xai.method`
  - `xai.version`
  - `xai.quality_score`
  - `xai.input_features`
- All feature mappings must be deterministic  
- All exported explanations must include version fingerprints of:
  - Model  
  - Training dataset  
  - Feature schema  

---

## 🕰 Version History

| Version  | Date       | Notes                                                       |
|----------|------------|-------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | First v11.2.2-compliant explainability layer spec           |
| v11.0.0  | 2025-11-20 | Initial introduction of explainability requirements in v11  |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Pipelines](../README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md) · [🔐 FAIR+CARE](../../../standards/faircare/FAIRCARE-GUIDE.md)

</div>
