---
title: "⚡🟥🧩 KFM v11.2.2 — Hazard SHAP Driver Taxonomy Template Suite (Semantic Codes · Narrative Safety · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/shap/templates/taxonomy/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Specification (Hazard SHAP Driver Taxonomy)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

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
sensitivity: "Explainability-Hazard-Taxonomy"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-driver-taxonomy"
  - "semantic-driver-definitions"
  - "hazard-shap-taxonomy-templates"
  - "faircare-driver-mapping"
  - "story-node-hazard-templates"
  - "focus-mode-hazard-templates"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/hazard/shap/templates/taxonomy"
  applies_to:
    - "hazard-driver-taxonomy.json"
    - "driver-code-template.jsonld"
    - "driver-taxonomy-notes.md"
    - "semantic-driver-mapping"
    - "care-governance"
    - "h3-masking"
    - "prov-xai"
    - "stac-xai"
    - "narrative-driver-templates"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# ⚡🟥🧩 **Hazard SHAP Driver Taxonomy Template Suite**  
`docs/pipelines/ai/explainability/hazard/shap/templates/taxonomy/README.md`

**Purpose:**  
Provide the **canonical, governance-enforced template suite** for defining **hazard-driver semantic taxonomies** used in SHAP explainability (global + local), including:

- Narrative-safe hazard driver codes  
- CARE- and sovereignty-compliant descriptions  
- Feature → driver semantic mapping scaffolds  
- JSON-LD ontology templates  
- Story Node v3 + Focus Mode v3 integration templates  
- Deterministic, machine-parseable schemas  

This suite ensures that **all hazard SHAP explainability outputs** (global, local, tile-based, raster-based) use **consistent, stable driver semantics**.

</div>

---

## 📘 Overview

The Hazard Driver Taxonomy defines **semantic driver categories** representing the real meaning behind SHAP features.

Drivers cover:

- 🌀 Tornado / rotation / shear  
- 💨 Wind / gust / LLJ  
- 🌩️ Hail / severe convection  
- 🔥 Wildfire fuels / VPD / spread  
- 🌧️ Flood / flash-flood / soil saturation  
- ⚡ Multi-hazard fused drivers  

The taxonomy serves three critical functions:

1. **Normalize raw SHAP features → human-understandable semantic drivers**  
2. **Provide governance-safe descriptions for Story Node v3**  
3. **Drive Focus Mode v3 hazard reasoning overlays**  

All taxonomy entries are subject to:

- FAIR+CARE  
- Sovereignty restrictions  
- H3-based location generalization  
- Deterministic output structure  
- PROV-O lineage requirements  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/templates/taxonomy/
    ├── 📄 README.md                            # This file
    │
    ├── 📄 hazard-driver-taxonomy.json          # Canonical machine-readable taxonomy template
    ├── 📄 driver-code-template.jsonld          # JSON-LD driver semantics template
    └── 📄 driver-taxonomy-notes.md             # Notes & governance guidance for taxonomy authors

---

## 🔍 Template Specifications

### 1. 🟥 `hazard-driver-taxonomy.json`
A fully deterministic JSON template defining:

- `driver_code` — canonical code (e.g., `TORNADO_SIGNAL`, `FLOOD_SATURATION`)  
- `hazard_domain` — tornado|wind|hail|wildfire|flood|multi  
- `description` — CARE-safe narrative description (placeholder)  
- `linked_features` — raw SHAP features connected to the driver  
- `story_node_roles` — how the driver appears in narratives  
- `focus_mode_tags` — categories for Focus Mode explanations  
- `care_annotations` — sensitivity flags  
- `sovereignty_annotations` — required for protected geographic context  
- `provenance_stub` — PROV-O placeholders  
- `metadata_version` — semantic version pinning  

All fields must appear in templated order for CI determinism.

---

### 2. 🟩 `driver-code-template.jsonld`
Defines the JSON-LD version of the hazard driver taxonomy.

Required structural fields:

- `@context` (KFM-XAI + PROV-O)  
- `xai:driver_code`  
- `xai:description` (CARE-safe placeholder)  
- `xai:hazard_domain`  
- `xai:linked_features`  
- `xai:story_node_roles`  
- `xai:focus_mode_tags`  
- `care:scope` & `care:notes`  
- `sovereignty:*` flags  
- `prov:wasDerivedFrom` template link to SHAP evidence bundles  
- `checksum:multihash` placeholder  

Used to:

- Generate Story Node driver descriptions  
- Populate Focus Mode reasoning labels  
- Ensure XAI semantic stability  

---

### 3. 🧾 `driver-taxonomy-notes.md`
Provides governance and authoring guidance:

- CARE-compliant writing rules  
- Terms that cannot be used (no cultural/tribal identity references)  
- How to abstract sensitive hazard contexts  
- How to express hazard drivers with domain accuracy  
- Best practices for STAC/XAI alignment  
- Explanation of H3 masking in taxonomy definitions  
- The rule that **drivers describe evidence**, never speculation  

This file is a human-facing policy companion to the machine templates.

---

## 📡 STAC-XAI Template Requirements

Taxonomy-driven explainability outputs generated downstream MUST include:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:drivers` or propagation into global/local bundles  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CARE + sovereignty fields  
- PROV-O lineage linkage  

The taxonomy templates define how these fields appear and validate within CI.

---

## 🧾 PROV-O Template Requirements

Every generated driver-code mapping MUST support:

- `prov:wasGeneratedBy`  
- `prov:used` (model & STAC Items)  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional:  
  - `prov:wasDerivedFrom` (global/local → taxonomy mapping)

This allows Story Node v3 and Focus Mode v3 to express **why** a driver exists.

---

## 🔐 FAIR+CARE Template Rules

Every taxonomy template must include placeholders ensuring:

- CARE scope inclusion  
- Sovereignty compliance  
- Masking (especially wildfire & flood-sensitive areas)  
- Cultural neutrality  
- No speculation  
- H3 region abstraction guidance  
- Data Contract v3 alignment  

Driver semantics must always be **data-grounded**.

---

## 🧪 Template CI Rules

CI validates:

- JSON / JSON-LD schema correctness  
- Deterministic field ordering  
- Presence of CARE & sovereignty placeholders  
- PROV-O structure  
- STAC-XAI fields  
- Narrative safety linter  
- Stable hashing (no nondeterministic generation)  

Any failure → ❌ **merge blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                               |
|----------|------------|---------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard SHAP Driver Taxonomy Template Suite (KFM v11.2.2)    |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard SHAP Templates](../README.md)  
[⚡ Hazard XAI Root](../../../../README.md)  
[🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

