---
title: "🔬 KFM v11.2.2 — Explainability (XAI) Template Suite (SHAP · IG · CAMs · Provenance · FAIR+CARE)"
path: "docs/pipelines/ai/templates/explainability/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Reliability Engineering"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Template Specification"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-xai-templates-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-xai-templates-v11.2.2.json"
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
sensitivity: "Explainability-Artifacts"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "xai"
  - "explainability"
  - "interpretability"
  - "provenance"
  - "jsonld-xai"
  - "story-node-features"
  - "focus-mode-features"

scope:
  domain: "ai-templates-explainability"
  applies_to:
    - "shap"
    - "lime"
    - "integrated-gradients"
    - "cams"
    - "saliency"
    - "xai-jsonld"
    - "xai-stac"
    - "story-node-xai"
    - "focus-mode-xai"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🔬 **KFM v11.2.2 — Explainability Template Suite**  
`docs/pipelines/ai/templates/explainability/README.md`

**Purpose:**  
Provide the canonical **Explainability (XAI) template suite** for all AI/ML pipelines in the Kansas Frontier Matrix—ensuring standardized SHAP, IG, CAMs, saliency, attribution graphs, and provenance-safe JSON-LD structures.  
These templates power **Story Node v3**, **Focus Mode v3**, **STAC v11 explainability blocks**, and **audit-ready AI reasoning**.

</div>

---

## 📘 Overview

This directory contains **standardized templates** for expressing model explainability across all AI domains:

- Climate XAI (SHAP/IG/CAMs)  
- Hydrology XAI (terrain drivers, runoff factors)  
- Hazard XAI (wind shear, dryness index, supercell probability drivers)  
- NLP XAI (attention maps, token importances)  
- Embedding XAI (semantic factor projections)  
- Focus Mode v3 XAI (evidence fusion, narrative justification maps)

These templates ensure:

- Deterministic, comparable explainability  
- FAIR+CARE governance compliance  
- JSON-LD machine readability  
- STAC v11 compatibility  
- Provenance linkage with **PROV-O**  
- Masking for sensitive/Indigenous context  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/templates/explainability/
    ├── 📄 README.md                                 # This file
    │
    ├── 📁 jsonld/                                   # JSON-LD explainability schemas
    │   ├── 📄 xai-global-template.jsonld            # Global SHAP-style vector template
    │   ├── 📄 xai-local-template.jsonld             # Local (per-instance) explanation
    │   └── 📄 xai-evidence-chain-template.jsonld    # Evidence fusion (Focus Mode v3)
    │
    ├── 📁 visual/                                   # Visual explanation templates
    │   ├── 📄 cams-saliency-template.md             # CAMs/saliency map documentation
    │   ├── 📄 ig-gradient-template.md               # Integrated Gradients mapping rules
    │   └── 📄 attribution-overlay-template.md       # Map overlays (spatial explanations)
    │
    ├── 📁 stac/                                     # STAC explainability templates
    │   ├── 📄 stac-xai-fields-template.json         # STAC v11 explainability extensions
    │   └── 📄 stac-xai-asset-template.json          # Explainability asset templates
    │
    └── 📁 story-nodes/                              # Story Node v3 narrative XAI templates
        ├── 📄 story-node-xai-template.jsonld        # XAI → narrative structure
        └── 📄 narrative-driver-template.md          # Explainability → narrative text bridge

---

## 🧬 Explainability Components (v11.2.2)

### 1. 🟥 SHAP Templates
- Feature impact vectors  
- Global feature ranking  
- Local contributions  
- CARE masking for protected attributes  

### 2. 🟦 LIME Templates
- Surrogate feature explanations  
- Optional for NLP + hybrid models  

### 3. 🟩 Integrated Gradients Templates
- Gradient-based attribution  
- Required for deep learning (terrain, DEM, climate)  

### 4. 🟨 CAMs & Saliency Templates
- Visual heatmaps for spatial models  
- Required for remote-sensing + geospatial CNNs  
- H3 masking rules enforced  

### 5. 🟪 Evidence Fusion Templates (Focus Mode v3)
- Cross-domain driver fusion  
- Confidence + relevance scores  
- JSON-LD evidence blocks for narrative pipelines  

---

## 📡 STAC Integration Requirements

XAI templates MUST support:

- `kfm:explainability:method`  
- `kfm:explainability:drivers`  
- `kfm:explainability:saliency`  
- `kfm:explainability:local`  
- `kfm:explainability:global`  
- `kfm:input_items` (upstream STAC IDs)  
- Multihash asset checksums  
- Bounding geometry (if spatial)  
- CRS/vertical metadata  

---

## 🔐 FAIR+CARE Requirements

All XAI outputs generated via these templates MUST:

- Mask sensitive/Indigenous locations using **H3 generalization**  
- Abstract culturally sensitive concepts  
- Avoid speculative narrative extension  
- Provide provenance (`prov:*`) for each assertion  
- Include CARE scope + usage notes  

Templates failing CARE governance → **CI blocked**.

---

## 🧪 Testing Requirements

Explainability templates must pass:

- JSON-LD schema validation  
- STAC extension validation tests  
- CARE masking tests  
- Deterministic XAI rendering tests  
- Evidence fusion consistency tests  
- Story Node v3 schema integration tests  

---

## 🕰 Version History

| Version  | Date       | Notes                                                              |
|----------|------------|--------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full v11.2.2 uplift; new XAI JSON-LD suite; emoji tree added      |
| v11.0.0  | 2025-11-15 | Initial XAI template suite introduction                           |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to AI Template Index](../README.md) · [🧠 AI Model Templates](../model-cards/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

