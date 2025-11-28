---
title: "🌡️🤖📄 KFM v11.2.2 — Climate Batch Inference JSON-LD Explainability Layer (SHAP · IG · CAM · Spatial Attribution · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/batch/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Semantic Explainability Layer (JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Climate-Inference-Explainability"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-batch-jsonld"
  - "climate-driver-semantics"
  - "xai-climate-local"
  - "xai-climate-global"
  - "xai-spatial-climate"
  - "shap-ig-cams-jsonld"
  - "prov-xai"
  - "stac-xai"
  - "story-node-climate"
  - "focus-mode-climate"
  - "care-governance"
  - "h3-masking"

scope:
  domain: "pipelines/ai/inference/climate/batch/jsonld"
  applies_to:
    - "xai-climate-local.jsonld"
    - "xai-climate-global.jsonld"
    - "xai-climate-spatial.jsonld"
    - "climate-driver-taxonomy.jsonld"
    - "story-node-integration"
    - "prov-xai"
    - "stac-xai"
    - "care-governance"
    - "h3-generalization"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️🤖📄 **Climate Batch Inference — JSON-LD Explainability Layer**  
`docs/pipelines/ai/inference/climate/batch/jsonld/README.md`

**Purpose:**  
Provide the **canonical JSON-LD explainability schema** for Climate Batch Inference, unifying:

- SHAP (local/global)  
- Integrated Gradients (local/global)  
- CAMs (raster/tile spatial attribution)  
- Derived Climate Driver semantics  
- FAIR+CARE metadata  
- STAC-XAI and PROV-O lineage  

This JSON-LD layer ensures that all climate inference products are **machine-interpretable**, **governance-safe**, **sovereignty-aware**, and **Story Node v3 / Focus Mode v3 ready**.

</div>

---

## 📘 Overview

Climate batch inference produces multiple explainability modes:

- **Local attribution** (event-level)  
- **Global attribution** (system-level)  
- **Spatial attribution** (maps/tiles)  
- **Semantic driver mappings** (taxonomy)  

These JSON-LD files unify those modes into a **single semantic framework**, enabling:

- Cross-model reasoning  
- Hazard-linked climate logic  
- Narrative generation (Story Node v3)  
- Contextual filtering (Focus Mode v3)  
- Full lineage inspection  

All JSON-LD outputs MUST follow:

- KFM-XAI ontology  
- PROV-O lineage  
- STAC-XAI contract  
- FAIR+CARE + sovereignty protections  
- H3-generalization for sensitive regions  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/batch/jsonld/
    ├── 📄 README.md                                 # This file
    │
    ├── 📄 xai-climate-local.jsonld                  # Local (event-level) explainability
    ├── 📄 xai-climate-global.jsonld                 # Global climate driver explainability
    ├── 📄 xai-climate-spatial.jsonld                # Spatial explainability bundle (optional)
    │
    └── 📄 climate-driver-taxonomy.jsonld            # Narrative-safe semantic driver mapping

---

## 🔍 Component Specifications

### 1. 🟥 `xai-climate-local.jsonld` — Local Explainability
Required fields:

- `@context` — KFM-XAI + PROV-O  
- `xai:drivers`  
- `xai:importance` (SHAP/IG)  
- `xai:hazard_links` (if relevant)  
- `xai:spatial_context` (H3 generalized)  
- CARE + sovereignty metadata  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- `prov:*` lineage  

Used for:  
Story Node local narratives, Focus Mode per-event explanations.

---

### 2. 🟦 `xai-climate-global.jsonld` — Global Climate Driver Explainability  
Semantic system-wide climate attribution:

- Global driver ranking  
- Climate-domain metadata  
- Hazard-linked climate attributes (if applicable)  
- CARE + sovereignty metadata  
- STAC-XAI global fields  
- PROV-O lineage  
- Deterministic driver ordering  

Used for:  
Climate summaries, large-scale driver modeling, governance review.

---

### 3. 🟩 `xai-climate-spatial.jsonld` — Spatial Attribution (Optional)

Defines spatial explainability metadata for:

- CAMs raster/tile maps  
- IG gradient spatial fields  
- Spatial SHAP distributions  

Required:

- Generalized H3 geometry  
- Spatial driver summary  
- CARE + sovereignty annotations  
- STAC-XAI spatial fields  
- PROV lineage  
- Integrity metadata  

---

### 4. 🧩 `climate-driver-taxonomy.jsonld` — Semantic Driver Mapping
Defines the narrative-safe climate driver categories:

- Driver codes (`CLIMATE_CAPE`, `CLIMATE_INVERSION`, etc.)  
- CARE-safe description  
- Hazard relevance  
- Climate variable linkages  
- Focus Mode tags  
- Story Node roles  
- Sovereignty & CARE notes  
- PROV `wasDerivedFrom` anchors  

Used for unified reasoning across climate + hazard models.

---

## 📡 STAC-XAI Compliance Rules

Each JSON-LD file MUST include:

- `kfm:explainability:method`  
- one of:  
  - `kfm:explainability:local`  
  - `kfm:explainability:global`  
  - `kfm:explainability:spatial`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CARE & sovereignty metadata  
- CRS metadata (if spatial)  
- Proper JSON-LD linkage in STAC Items  

---

## 🧾 PROV-O Lineage Requirements

Each JSON-LD artifact MUST include:

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional: `prov:wasDerivedFrom` (XAI chaining)  

This ensures complete inference traceability.

---

## 🔐 FAIR+CARE & Sovereignty Requirements

All JSON-LD outputs MUST:

- Include CARE scope + notes  
- Include sovereignty flags  
- Avoid sensitive cultural/tribal inference  
- Mask spatial details via H3  
- Use narrative-safe vocabulary  
- Comply with Data Contract v3  
- Avoid speculative climate claims  

---

## 🧪 CI Validation Rules

CI MUST validate:

- JSON-LD structure via KFM-XAI schema  
- Required PROV fields  
- Required STAC-XAI fields  
- CARE + sovereignty metadata presence  
- H3-generalization if spatial  
- Deterministic key ordering  
- Hash stability  
- Narrative-safety lexical lint  

Failures → ❌ merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                  |
|----------|------------|------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Batch Inference JSON-LD Explainability Specification   |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate STAC](../stac/README.md) · [🌡️ Climate Inference Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

