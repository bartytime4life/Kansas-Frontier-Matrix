---
title: "⚡🟩📄🧬 KFM v11.2.2 — Hazard IG Global JSON-LD Template Suite (Semantic Drivers · STAC-XAI · PROV-O · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/global/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Specification (Hazard IG Global JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Explainability-Hazard-IG-Global-JSONLD-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ig-global-jsonld-templates"
  - "hazard-driver-taxonomy-templates"
  - "global-gradient-driver-mapping"
  - "prov-xai-templates"
  - "stac-xai-templates"
  - "story-node-hazard-templates"
  - "focus-mode-hazard-templates"
  - "care-governance"

scope:
  domain: "explainability/hazard/integrated-gradients/templates/global/jsonld"
  applies_to:
    - "xai-ig-global-template.jsonld"
    - "hazard-ig-driver-codes-template.jsonld"
    - "semantic-driver-taxonomy"
    - "stac-xai"
    - "prov-xai"
    - "care-governance"
    - "h3-masking"
    - "narrative-driver-templates"

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

# ⚡🟩📄🧬 **Hazard Integrated Gradients — Global JSON-LD Template Suite**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/global/jsonld/README.md`

**Purpose:**  
Specify the **canonical JSON-LD templates** for **global Hazard IG explainability**, including:

- System-wide gradient-based hazard drivers (`xai-ig-global.jsonld`)  
- Narrative-safe hazard driver taxonomies (`hazard-ig-driver-codes.jsonld`)  
- STAC v11 XAI metadata fields  
- PROV-O lineage skeletons  
- FAIR+CARE and sovereignty placeholders  

These templates guarantee that all global Hazard IG JSON-LD outputs are structurally identical, governance-safe, and interoperable with **Story Node v3**, **Focus Mode v3**, and KFM’s lineage/telemetry subsystems.

</div>

---

## 📘 Overview

This directory does **not** contain real explainability data.  
Instead, it defines JSON-LD **blueprints** used by:

- Hazard IG ETL/XAI pipelines  
- CI validation workflows  
- Governance review processes  

Templates here define the shape of:

1. `xai-ig-global-template.jsonld` — global IG driver evidence  
2. `hazard-ig-driver-codes-template.jsonld` — semantic hazard driver taxonomy for IG outputs  

These ensure:

- Deterministic JSON-LD shape & key ordering  
- Correct `@context` usage (KFM-XAI + PROV-O)  
- Presence of STAC-XAI fields  
- FAIR+CARE + sovereignty enforcement points  
- Reuse across multiple hazard model families  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/global/jsonld/
    ├── 📄 README.md                                  # This file
    │
    ├── 📄 xai-ig-global-template.jsonld              # Template for global IG evidence bundle
    └── 📄 hazard-ig-driver-codes-template.jsonld     # Template for IG hazard driver taxonomy

---

## 🟥 `xai-ig-global-template.jsonld` — Global Evidence Template

Defines the **JSON-LD structure** for actual `xai-ig-global.jsonld` outputs.

### Required Sections & Fields

**1. Context**

- `@context`  
  - KFM-XAI context  
  - PROV-O context  

**2. Drivers Block**

- `xai:drivers` (array of objects)  
  - `xai:driver_code` — reference into hazard IG driver taxonomy  
  - `xai:importance` — normalized IG magnitude placeholder  
  - `xai:hazard_domain` — `tornado|hail|wind|wildfire|flood|multi`  
  - `xai:description` — CARE-safe description placeholder  

**3. Spatial Context (Optional / Masked)**

- `xai:spatial_context`  
  - `xai:h3_regions` — placeholder for H3 indices (generalized)  
  - `xai:region_summary` — abstract geographic description  

**4. Model & Dataset Metadata**

- `kfm:model_version`  
- `kfm:input_items` (STAC Item IDs)  
- `checksum:multihash`  

**5. CARE & Sovereignty Metadata**

- `care:scope`  
- `care:notes`  
- `sovereignty:flags`  

**6. PROV-O Lineage**

- `prov:wasGeneratedBy` — pipeline run placeholder  
- `prov:used` — datasets placeholder  
- `prov:generatedAtTime`  
- `prov:Agent`  

Key ordering and required presence are enforced by this template.

---

## 🟩 `hazard-ig-driver-codes-template.jsonld` — IG Driver Taxonomy Template

Defines the global semantic mapping between **deep-model IG gradients** and **human-interpretable hazard drivers**.

### Required Template Fields Per Driver

- `xai:driver_code`  
  - e.g., `TORNADO_SIGNAL_IG`, `FLOOD_SATURATION_IG`  

- `xai:description`  
  - Narrative-safe explanation (placeholder content must pass CARE review)  

- `xai:hazard_domain`  
  - `tornado|hail|wind|wildfire|flood|multi`  

- `xai:linked_features`  
  - Placeholder list of underlying model features  

- `xai:story_node_roles`  
  - e.g., `primary_driver`, `secondary_driver`, `contextual_driver`  

- `xai:focus_mode_tags`  
  - Tagging for interactive reasoning (map overlay, timeline annotation, etc.)  

- `care:annotations`  
  - CARE impact + masking guidance  

- `sovereignty:*`  
  - Indigenous or protected context flags  

- `prov:wasDerivedFrom`  
  - Template linkage to IG global evidence bundle  

This taxonomy template guarantees:  

- Stable driver codes across versions  
- Clear semantics for each hazard driver  
- Governance and narrative safety support  

---

## 📡 STAC-XAI Template Requirements

ANY global IG JSON-LD bundle produced using these templates MUST:

- Set `kfm:explainability:method = "integrated-gradients"`  
- Provide `kfm:explainability:global` references in STAC Items  
- Record `kfm:model_version`  
- Record `kfm:input_items` (STAC Item IDs)  
- Include `checksum:multihash`  
- Add CRS metadata when spatial patterns exist  
- Embed CARE & sovereignty metadata  

Templates define the position and schema of these fields.

---

## 🧾 PROV-O Template Requirements

Templates enforce PROV-O structural expectations:

- `prov:wasGeneratedBy` → hazard IG inference pipeline  
- `prov:used` → STAC hazard + climate inputs  
- `prov:generatedAtTime` → timestamp  
- `prov:Agent` → model & pipeline identity  
- Optional `prov:wasDerivedFrom` → mapping from model/datasets to IG semantics  

---

## 🔐 FAIR+CARE & Sovereignty Template Rules

All templates MUST:

- Include H3-generalization fields for spatial masking  
- Provide CARE scope & notes fields  
- Provide sovereignty flags for Indigenous/heritage-relevant contexts  
- Exclude any hard-coded sensitive geography or community references  
- Use governance-neutral placeholder language  

Concrete content must be filled by pipelines and reviewed by governance.

---

## 🧪 Template CI Requirements

CI must validate template changes by:

- JSON-LD schema checking  
- STAC-XAI linting  
- PROV-O structure validation  
- CARE/scope & sovereignty placeholders presence  
- H3 mask placeholders presence  
- Deterministic key ordering checks  
- Narrative-safety lexical lint  

Any failing check → ❌ **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                                 |
|----------|------------|---------------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard IG Global JSON-LD Template Suite (aligned with SHAP, Climate IG XAI)  |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard IG Global Templates](../README.md) · [⚡ Hazard XAI Root](../../../../README.md) · [🏛 Governance](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

