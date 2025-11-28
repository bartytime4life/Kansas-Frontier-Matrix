---
title: "⚡🟥📄 KFM v11.2.2 — Hazard SHAP Global JSON-LD Templates (Semantic Drivers · STAC-XAI · PROV-O)"
path: "docs/pipelines/ai/explainability/hazard/shap/templates/global/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Specification (Hazard SHAP Global JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Explainability-Templates-Hazard-Global-JSONLD"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-shap-global-jsonld-templates"
  - "hazard-driver-taxonomy-templates"
  - "semantic-driver-mapping"
  - "prov-xai-templates"
  - "stac-xai-templates"
  - "story-node-hazard-templates"
  - "focus-mode-hazard-templates"

scope:
  domain: "explainability/hazard/shap/templates/global/jsonld"
  applies_to:
    - "xai-shap-global-jsonld-template"
    - "hazard-driver-codes-jsonld-template"
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

# ⚡🟥📄 **Hazard SHAP Global JSON-LD Template Suite**  
`docs/pipelines/ai/explainability/hazard/shap/templates/global/jsonld/README.md`

**Purpose:**  
Specify the **canonical JSON-LD templates** for **global hazard SHAP explainability**, including system-wide hazard driver semantics, narrative-safe driver codes, STAC-XAI integration fields, PROV-O lineage scaffolding, and FAIR+CARE placeholders used by **Story Node v3** and **Focus Mode v3**.

</div>

---

## 📘 Overview

This directory defines the JSON-LD “blueprints” for:

- `xai-shap-global.jsonld` — global hazard-driver evidence  
- `xai-hazard-driver-codes.jsonld` — semantic, narrative-safe hazard driver taxonomy  

Templates here ensure that every generated global SHAP JSON-LD bundle is:

- Deterministic & schema-valid  
- FAIR+CARE and sovereignty aligned  
- STAC v11 + KFM-XAI extension compliant  
- PROV-O traceable  
- Ready for direct consumption by Story Nodes and Focus Mode  

The templates **do not** contain real data — they define the **structure** and **required fields** to be filled by pipelines.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/templates/global/jsonld/
    ├── 📄 README.md                                  # This file
    │
    ├── 📄 xai-shap-global-template.jsonld            # Template for global hazard-driver bundle
    └── 📄 hazard-driver-codes-template.jsonld        # Template for hazard driver taxonomy codes

---

## 🟥 `xai-shap-global-template.jsonld` — Global Evidence Template

This template defines the JSON-LD structure for the actual `xai-shap-global.jsonld` artifact.

Required structural elements:

- `@context`
  - KFM-XAI vocabulary  
  - PROV-O vocabulary  

- **Global Drivers Block**  
  - `xai:drivers` — array of driver objects:
    - `xai:driver_id` (or code ref)  
    - `xai:importance` (normalized SHAP magnitude)  
    - `xai:hazard_domain` (tornado | hail | wind | flood | wildfire | multi)  
    - `xai:description` (optional placeholder, final content must be CARE-safe)  

- **Spatial Context (Optional / Masked)**  
  - `xai:spatial_context`:
    - `xai:h3_regions` (placeholder for generalized H3 indexes)  
    - `xai:region_summary` (abstract region labels)  

- **Model & Data Metadata**  
  - `kfm:model_version`  
  - `kfm:input_items` (array of STAC Item IDs)  
  - `checksum:multihash`  

- **CARE & Sovereignty Metadata**  
  - `care:scope` (template field)  
  - `care:notes`  
  - `sovereignty:flags`  

- **PROV-O Lineage**  
  - `prov:wasGeneratedBy`  
  - `prov:used`  
  - `prov:generatedAtTime`  
  - `prov:Agent`  

This template guarantees that every global hazard SHAP JSON-LD file shares a **consistent, machine-checkable structure**.

---

## 🟩 `hazard-driver-codes-template.jsonld` — Driver Taxonomy Template

This template defines the taxonomy JSON-LD for mapping raw SHAP features → semantic hazard drivers.

Each driver entry includes placeholders for:

- `xai:driver_code`  
  - e.g., `TORNADO_SIGNAL`, `SEVERE_STORM_ENV`, `FLOOD_SOIL_SATURATION`  

- `xai:description`  
  - Narrative-safe explanation (final content must be CARE-reviewed)  

- `xai:hazard_domain`  
  - e.g., `tornado`, `hail`, `wind`, `wildfire`, `flood`, `multi`  

- `xai:linked_features`  
  - Placeholder for raw SHAP feature names contributing to this driver  

- `xai:story_node_roles`  
  - e.g., `primary_driver`, `secondary_driver`, `contextual_driver`  

- `xai:focus_mode_tags`  
  - e.g., `map-overlay`, `timeline-annotation`, `alert-driver`  

- `care:annotations`  
  - Fields describing CARE implications and masking rules  

- `prov:wasDerivedFrom`  
  - Structural link back to the global driver bundle (template placeholder)

This taxonomy template ensures:

- Consistent naming  
- SAFE vocabulary for public narratives  
- Governance-enforced semantics  

---

## 📡 STAC-XAI Template Fields

Global hazard SHAP JSON-LD generated from these templates MUST be compatible with STAC by including:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:global` (URI to the JSON-LD artifact)  
- `kfm:model_version`  
- `kfm:input_items` (STAC Item IDs)  
- `checksum:multihash`  
- CRS metadata when spatial context is present  

Templates include placeholder positions for all these fields.

---

## 🧾 PROV-O Template Requirements

Both templates MUST provide structure for:

- `prov:wasGeneratedBy` — hazard model pipeline  
- `prov:used` — STAC hazard + climate datasets  
- `prov:generatedAtTime` — ISO timestamp  
- `prov:Agent` — model + pipeline identity  

Optional structure for:

- `prov:wasDerivedFrom` — link from SHAP outputs to model + underlying data  

---

## 🔐 FAIR+CARE & Sovereignty Template Rules

Templates include placeholders for:

- CARE scope (`care:scope`)  
- CARE notes, including categories like `Public`, `Restricted-Community`, etc.  
- Sovereignty flags for Indigenous or protected context  
- H3-based spatial abstraction fields  

They explicitly **exclude**:

- Any speculative language  
- Any direct references to specific communities or sacred sites  

All narrative text inserted at runtime must pass **governance review**.

---

## 🧪 Template CI & Validation

Before changes are accepted, CI MUST:

- Validate JSON-LD structure against KFM-XAI + PROV-O schemas  
- Validate presence of STAC XAI fields where indicated  
- Run FAIR+CARE lint rules (e.g., banned phrases, missing CARE fields)  
- Ensure deterministic key ordering where specified  
- Confirm that sovereignty fields are present and non-empty where required  

Template edits that break these rules → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                           |
|----------|------------|---------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard SHAP Global JSON-LD template suite aligned with KFM XAI v11.2.2 |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard SHAP Global Templates](../README.md) · [⚡ Hazard XAI Root](../../../../README.md) · [🏛 Governance](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

