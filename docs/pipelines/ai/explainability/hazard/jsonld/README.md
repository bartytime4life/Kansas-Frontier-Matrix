---
title: "⚡📄🧬 KFM v11.2.2 — Hazard Explainability JSON-LD Layer (Unified Semantics · STAC-XAI · PROV-O · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Component (Unified Hazard JSON-LD Semantics)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

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
sensitivity: "Explainability-Hazard-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-jsonld"
  - "hazard-driver-semantics"
  - "global-hazard-xai"
  - "local-hazard-xai"
  - "cams-jsonld"
  - "shap-jsonld"
  - "ig-jsonld"
  - "spatial-attribution-jsonld"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "prov-xai"
  - "stac-xai"
  - "care-governance"
  - "h3-masking"

scope:
  domain: "explainability/hazard/jsonld"
  applies_to:
    - "hazard-xai-unified-jsonld"
    - "hazard-driver-taxonomy"
    - "cams-jsonld"
    - "shap-jsonld"
    - "ig-jsonld"
    - "spatial-jsonld"
    - "story-node-integration"
    - "focus-mode-metadata"
    - "prov-xai"
    - "stac-xai"
    - "care-governance"
    - "h3-maskable"
    
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

# ⚡📄🧬 **Hazard Explainability — Unified JSON-LD Layer**  
`docs/pipelines/ai/explainability/hazard/jsonld/README.md`

**Purpose:**  
Define the **unified JSON-LD explainability layer** for all hazard AI pipelines—SHAP, IG, CAMs, Spatial Attribution—providing:

- Semantic hazard-driver representations  
- H3-generalized spatial contexts  
- FAIR+CARE-governed narrative and metadata structures  
- STAC-XAI v11 compatible metadata fields  
- PROV-O lineage anchors  
- Direct interoperability with **Story Node v3** and **Focus Mode v3**

This layer harmonizes explainability outputs across tornado, hail, wind, flood, wildfire, and multi-hazard models.

</div>

---

## 📘 Overview

The **Hazard Explainability JSON-LD Layer** provides machine-readable, governance-validated explainability metadata for:

- **Local explanations** (per-event SHAP/IG/CAMs)
- **Global explanations** (system-wide SHAP/IG summaries)
- **Spatial attribution** (raster or tile CAMs/IG surfaces)
- **Hazard driver taxonomy** (narrative-safe semantics)
- **Cross-modal evidence fusion** (e.g., SHAP + IG + CAMs)

JSON-LD explainability is the **semantic sublayer** that:

- Encodes hazard driver semantics  
- Enables narrative generation (Story Node v3)  
- Supports interactive hazard reasoning (Focus Mode v3)  
- Allows governance review (FAIR+CARE + sovereignty)  
- Links explainability artifacts to STAC Items  
- Integrates with PROV-O lineage graphs  

All hazard explainability pipelines **must** produce JSON-LD that matches these specifications.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/jsonld/
    ├── 📄 README.md                                 # This file
    │
    ├── 📄 xai-hazard-global.jsonld                  # Unified global hazard semantic drivers
    ├── 📄 xai-hazard-local.jsonld                   # Unified per-event semantic hazard drivers
    ├── 📄 xai-hazard-spatial.jsonld                 # Unified spatial semantic attribution (optional)
    │
    └── 📄 hazard-driver-taxonomy.jsonld             # Narrative-safe hazard driver semantic taxonomy

---

## 🔍 JSON-LD Components

### 1. 🟥 `xai-hazard-global.jsonld`  
Semantic evidence for **global hazard drivers**, regardless of method (SHAP, IG, CAMs, fused).

Required fields:

- `@context` (KFM-XAI + PROV-O)  
- `xai:hazard_domain`  
- `xai:drivers` (global driver list)  
- CARE & sovereignty metadata  
- STAC-XAI fields  
- PROV lineage  

### 2. 🟦 `xai-hazard-local.jsonld`  
Semantic **per-event** hazard evidence:

- Driver list with importance  
- H3-generalized spatial context  
- CARE/Sovereignty fields  
- PROV lineage  
- STAC references  

Works with SHAP local & IG local outputs.

### 3. 🟩 `xai-hazard-spatial.jsonld`  
Semantic representation of **spatial hazard attribution**:

- Raster or tile source references  
- Generalized H3 spatial descriptors  
- Hazard-driver summaries  
- PROV lineage  
- STAC-XAI metadata  

### 4. 🧩 `hazard-driver-taxonomy.jsonld`  
Canonical cross-hazard driver taxonomy:

- Unified driver codes  
- Narrative-safe descriptions  
- Hazard-domain tags  
- Story Node roles  
- Focus Mode tags  
- CARE & sovereignty rules  
- PROV anchors  

This taxonomy is the **semantic backbone** for hazard explainability across the entire KFM system.

---

## 📡 STAC-XAI Compliance

All hazard JSON-LD outputs MUST include:

- `kfm:explainability:method` (`shap`, `integrated-gradients`, `cams`, `spatial-attribution`)  
- `kfm:explainability:{local|global|raster|tiles}`  
- `kfm:model_version`  
- `kfm:input_items` (STAC Item IDs used during inference)  
- `checksum:multihash`  
- CRS metadata where applicable  
- CARE + sovereignty metadata  
- PROV lineage identifiers  

---

## 🧾 PROV-O Lineage Requirements

Each JSON-LD hazard explainability document must include:

- `prov:wasGeneratedBy` (model pipeline run)  
- `prov:used` (STAC inputs)  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional `prov:wasDerivedFrom` for multi-modal explainability chains  

Supports:

- Lineage-led audits  
- Traceability  
- Story Node provenance visualization  

---

## 🔐 FAIR+CARE & Sovereignty Constraints

All hazard JSON-LD must:

- Apply **H3 spatial generalization** to sensitive regions  
- Include sovereignty flags + CARE scope notes  
- Avoid sensitive tribal/cultural representation  
- Avoid speculative hazard causality  
- Use policy-approved hazard terminology  
- Follow Data Contract v3 and hazard-ethics guidance  

---

## 🧪 CI Validation Requirements

CI MUST validate:

- JSON-LD schema correctness (KFM-XAI)  
- STAC-XAI extension fields  
- PROV-O lineage completion  
- CARE + sovereignty placeholders  
- H3 masking structures  
- Deterministic key ordering  
- Narrative-safety lexical checks  
- Checksum stability  

Any failure → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                         |
|----------|------------|-------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial unified Hazard JSON-LD explainability specification (global/local/spatial) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard Explainability](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

