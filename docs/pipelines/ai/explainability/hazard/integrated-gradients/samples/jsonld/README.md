---
title: "⚡🟩📄 KFM v11.2.2 — Hazard Integrated Gradients Local JSON-LD Templates (Event Drivers · Semantic Evidence · PROV-O)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/samples/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Specification (Hazard IG Local JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../../../../schemas/telemetry/carbon-v2.json"

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
sensitivity: "Explainability-Hazard-Local-IG-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ig-local-jsonld-templates"
  - "gradient-attribution-hazard"
  - "event-driver-taxonomy"
  - "semantic-driver-mapping"
  - "story-node-hazard-templates"
  - "focus-mode-hazard-templates"
  - "prov-xai-templates"
  - "stac-xai-templates"
  - "care-governance"

scope:
  domain: "explainability/hazard/integrated-gradients/samples/jsonld"
  applies_to:
    - "xai-ig-local-template.jsonld"
    - "hazard-ig-driver-codes-local-template.jsonld"
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
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# ⚡🟩📄 **Hazard Integrated Gradients — Local JSON-LD Template Suite**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/samples/jsonld/README.md`

**Purpose:**  
Define the **canonical template suite** for **event-level Hazard Integrated Gradients (IG) JSON-LD explainability**, including semantic evidence bundles, driver-code mappings, CARE + sovereignty placeholders, PROV-O lineage skeletons, and STAC-XAI metadata fields that all downstream hazard IG outputs must implement.

These templates ensure deterministic, FAIR+CARE-governed, narrative-safe IG explainability across tornado, hail, wind, flood, wildfire, and multi-hazard models.

</div>

---

## 📘 Overview

This directory contains the **template definitions** for generating:

1. **`xai-ig-local.jsonld`**  
   Semantic IG evidence bundle for a single hazard event.

2. **`hazard-ig-driver-codes-local-template.jsonld`**  
   Template for narrative-safe driver taxonomy used in Story Node v3 & Focus Mode v3.

These templates enforce:

- JSON-LD structural consistency  
- KFM-XAI ontology alignment  
- PROV-O lineage presence  
- CARE & sovereignty compliance  
- Correct STAC XAI metadata  
- H3 generalized spatial masking  
- Deterministic ordering for CI reproducibility

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/integrated-gradients/samples/jsonld/
    ├── 📄 README.md                                      # This file
    │
    ├── 📄 xai-ig-local-template.jsonld                   # Template for local IG semantic evidence
    └── 📄 hazard-ig-driver-codes-local-template.jsonld   # Template for driver-code taxonomy (local IG)

---

## 🔍 Template Specifications

### 1. 🟥 `xai-ig-local-template.jsonld`  
The canonical event-level IG JSON-LD structure.

#### Required Template Fields

**Contexts**

- `@context`  
  - KFM-XAI context  
  - PROV-O context  

**Event Metadata**

- `xai:event_id`  
- `xai:hazard_domain` (`tornado|hail|wind|wildfire|flood|multi`)  
- `xai:timestamp` (optional placeholder)

**Drivers Block**

- `xai:drivers` (array)
  - `xai:driver_code` (references driver-code taxonomy)  
  - `xai:importance` (IG magnitude; numeric placeholder)  
  - `xai:linked_features`  
  - `xai:uncertainty` (optional)  

**Spatial Context**

- `xai:spatial_context`  
  - `xai:h3_regions` (generalized)  
  - `xai:region_summary`  

**CARE & Sovereignty Metadata**

- `care:scope`  
- `care:notes`  
- `sovereignty:flags`  

**STAC XAI Required Fields**

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items` (array of STAC Item IDs)  
- `checksum:multihash`  

**PROV-O Lineage**

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:generatedAtTime`  
- `prov:Agent`  

These placeholders ensure downstream generated content is machine-valid and governance-safe.

---

### 2. 🟩 `hazard-ig-driver-codes-local-template.jsonld`  
Defines how raw IG outputs map to **semantic hazard driver codes**.

#### Required Template Fields

- `xai:driver_code`  
  - e.g., `TORNADO_SIGNAL_IG_LOCAL`, `FLASHFLOOD_SATURATION_IG_LOCAL`

- `xai:description`  
  - CARE-safe, sovereignty-compliant description (placeholder)

- `xai:hazard_domain`  
  - Same domain codes as above

- `xai:linked_features`  
  - Placeholder list of contributing raw IG features

- `xai:story_node_roles`  
  - e.g., `primary_driver`, `secondary_driver`, `contextual_driver`

- `xai:focus_mode_tags`  
  - tags used in Focus Mode reasoning UI

- `care:annotations`
  - placeholders for CARE audit notes

- `sovereignty:*`  
  - explicit placeholders for Indigenous-sovereignty-sensitive context

- `prov:wasDerivedFrom`  
  - template mapping to IG local semantic evidence

This ensures hazard IG local drivers remain consistent, safe, semantic, and interpretable across all hazard reasoning surfaces.

---

## 📡 STAC-XAI Template Requirements

All generated JSON-LD must satisfy:

- `kfm:explainability:method`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS / vertical metadata if spatial  
- CARE + sovereignty metadata  
- PROV lineage minimum set  

The template ensures these fields exist in correct order and structure.

---

## 🧾 PROV-O Template Requirements

Template structures enforce:

- `prov:wasGeneratedBy` → hazard IG inference run  
- `prov:used` → hazard/climate STAC datasets  
- `prov:generatedAtTime` → ISO time placeholder  
- `prov:Agent` → model + pipeline identity  

Optional lineage relationships:

- `prov:wasDerivedFrom` → linking between local IG → global IG → driver taxonomy

---

## 🔐 FAIR+CARE Template Rules

Templates embed placeholders for:

- CARE scope & CARE notes  
- Sovereignty flags  
- H3 spatial masking  
- Masked region summaries  
- Non-speculative, governance-reviewed narrative-safe text  

Downstream content must obey:

- Data Contract v3  
- Indigenous sovereignty protocols  
- Heritage-sensitivity masking  
- Hazard ethics constraints  

---

## 🧪 Template CI Requirements

All template edits MUST pass:

- JSON-LD schema validation  
- STAC-XAI linter  
- PROV-O structural validation  
- CARE + sovereignty placeholder checks  
- H3-mask inclusion tests  
- Deterministic key ordering tests  
- Narrative-safety lexical checks  

Any failure → **PR rejected**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                             |
|----------|------------|-----------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard IG Local JSON-LD template suite (aligned with XAI global + local) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard IG Local Templates](../README.md) · [⚡ Hazard XAI Root](../../../../README.md) · [🏛 Governance](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

