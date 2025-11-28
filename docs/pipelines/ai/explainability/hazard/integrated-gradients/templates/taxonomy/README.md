---
title: "⚡🟩🧩🧬 KFM v11.2.2 — Hazard IG Driver Taxonomy Template Suite (Semantic Gradient Drivers · Narrative Safety · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/taxonomy/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Specification (Hazard IG Driver Taxonomy)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
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
sensitivity: "Explainability-Hazard-IG-Taxonomy"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ig-driver-taxonomy-template"
  - "gradient-driver-semantic-codes"
  - "narrative-safe-driver-codes"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "prov-xai-template"
  - "stac-xai-template"
  - "care-governance"
  - "h3-masking"

scope:
  domain: "explainability/hazard/integrated-gradients/templates/taxonomy"
  applies_to:
    - "hazard-ig-driver-taxonomy.json"
    - "driver-code-template.jsonld"
    - "driver-taxonomy-notes.md"
    - "semantic-driver-taxonomy"
    - "prov-xai"
    - "care-governance"
    - "stac-xai"
    - "h3-masking"
    - "narrative-driver-templates"

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

# ⚡🟩🧩🧬 **Hazard Integrated Gradients — Driver Taxonomy Template Suite**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/taxonomy/README.md`

**Purpose:**  
Define the **semantic driver taxonomy templates** for Hazard Integrated Gradients (IG) explainability, specifying:

- Canonical IG-based hazard driver codes  
- Narrative-safe semantic mappings  
- CARE + sovereignty placeholders  
- H3-masked spatial abstractions  
- PROV-O lineage scaffolding  
- STAC-XAI metadata requirements  
- Templates for Story Node v3 & Focus Mode v3 usage  

This suite governs how **raw IG gradient features** are transformed into **high-level, interpretable, ethically safe hazard-driver concepts**.

</div>

---

## 📘 Overview

This directory defines templates for **IG-based hazard driver semantics**, enabling:

- Stable cross-version driver codes  
- Governance-safe textual descriptions  
- Deterministic machine-friendly driver taxonomies  
- Integration into KFM’s AI explainability layer  
- Direct use in Story Node v3 narrative sections  
- Driver indexing for Focus Mode v3 hazard reasoning panels  

Hazards supported:

- 🌀 Tornado  
- 💨 Wind & gust  
- 🌩️ Hail & severe convection  
- 🔥 Wildfire  
- 🌧️ Flood & flash-flood  
- ⚡ Multi-Hazard fusion  

Each driver must be mapped from raw IG gradient features → **semantic narrative constructs**.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/taxonomy/
    ├── 📄 README.md                               # This file
    │
    ├── 📄 hazard-ig-driver-taxonomy.json          # Canonical flexible JSON taxonomy template
    ├── 📄 driver-code-template.jsonld             # JSON-LD semantic driver template
    └── 📄 driver-taxonomy-notes.md                # Authoring rules for safe taxonomy entries

---

## 🟥 Template: `hazard-ig-driver-taxonomy.json`

Defines the **canonical JSON structure** for hazard IG driver definitions.

Required fields per driver entry:

- `driver_code`  
  - e.g., `TORNADO_SIGNAL_IG`, `FLOOD_SATURATION_IG`, `WILDFIRE_DRYNESS_IG`  

- `hazard_domain`  
  - `tornado|wind|hail|wildfire|flood|multi`  

- `description`  
  - Placeholder for CARE-filtered narrative-safe definition  

- `linked_features`  
  - Placeholder array for IG features contributing to this driver  

- `story_node_roles`  
  - `primary_driver | secondary_driver | contextual_driver`  

- `focus_mode_tags`  
  - e.g., `map-overlay`, `timeline-driver`, `hazard-core-driver`  

- `care_annotations`  
- `sovereignty_annotations`  
- `provenance_stub` (to be filled via PROV-O templates)  

Template enforces **fixed key ordering** for deterministic hashing.

---

## 🟩 Template: `driver-code-template.jsonld`

Defines the JSON-LD semantic structure for IG driver codes.

Required JSON-LD fields per driver:

- `@context`  
  - KFM-XAI, PROV-O  

- `xai:driver_code`  
- `xai:description` (CARE-safe placeholder)  
- `xai:hazard_domain`  
- `xai:linked_features`  
- `xai:story_node_roles`  
- `xai:focus_mode_tags`  
- `care:annotations`  
- `sovereignty:*`  
- `prov:wasDerivedFrom` (template mapping back to global/local IG evidence)  
- `checksum:multihash` placeholder  

This template ensures that hazard IG driver codes are:

- Machine-readable  
- Semantic, interpretable  
- Governance-safe  
- Narrative-ready  
- Internally consistent across all XAI pipelines  

---

## 🧾 Template: `driver-taxonomy-notes.md`

Contains the authoritative human-facing rules for writing hazard-driver taxonomy entries:

- **CARE language guidance**  
- Prohibited terms (cultural, tribal, speculative hazard claims)  
- How to abstract sensitive geography using H3 generalization  
- Rules for defining hazard driver semantics  
- Best practices for aligning text with Story Node v3 and Focus Mode v3  
- Requirements for deterministic structuring  
- Cross-domain driver vocabulary alignment  

This ensures driver semantics remain ethical, factual, and reproducible.

---

## 📡 STAC-XAI Template Requirements

Any artifact generated from these templates MUST include:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:{global|local}` as applicable  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata (if spatial)  
- CARE + sovereignty metadata  
- PROV-O lineage  

Templates define the exact placement of these fields.

---

## 🔐 FAIR+CARE & Sovereignty Template Rules

All templates MUST embed placeholders for:

- CARE scope + notes  
- Sovereignty protection flags  
- H3-masked regional abstractions  
- Cultural-sensitivity safe wording  
- Non-speculative hazard representations  
- Strict compliance with Data Contract v3  

These templates form an ethical “guardrail” for all downstream hazard explainability.

---

## 🧪 Template CI Requirements

CI will validate that any template modification:

- Passes JSON / JSON-LD schema validation  
- Includes mandatory CARE + sovereignty placeholders  
- Includes H3-masking placeholders  
- Passes STAC-XAI + PROV-O compliance checks  
- Preserves deterministic ordering  
- Passes narrative-safety lexical lint  
- Maintains hash stability for diff-based governance  

Failures → **PR rejected**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                            |
|--------|------------|----------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard IG Driver Taxonomy Template Suite (aligned with SHAP + Climate IG) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard IG Template Suite](../README.md)  
[⚡ Hazard XAI Root](../../../../README.md)  
[🏛 Governance](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

