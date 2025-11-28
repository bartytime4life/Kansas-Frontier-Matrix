---
title: "⚡🟥🧬📈 KFM v11.2.2 — Hazard SHAP Global Templates (Feature Importance · System Drivers · JSON-LD)"
path: "docs/pipelines/ai/explainability/hazard/shap/templates/global/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Set (Hazard SHAP Global)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
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
sensitivity: "Explainability-Templates-Hazard-Global"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-global-template"
  - "hazard-driver-taxonomy"
  - "hazard-global-shap"
  - "jsonld-xai-template"
  - "prov-xai-template"
  - "story-node-hazard"
  - "focus-mode-hazard"

scope:
  domain: "explainability/hazard/shap/templates/global"
  applies_to:
    - "global-shap-vector-template"
    - "global-hazard-summary-template"
    - "xai-shap-global-jsonld-template"
    - "hazard-driver-codes-template"
    - "care-governance"
    - "h3-masking"
    - "narrative-driver-templates"
    - "stac-xai"
    - "prov-xai"

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

# ⚡🟥🧬📈 **Hazard SHAP — Global Templates**  
`docs/pipelines/ai/explainability/hazard/shap/templates/global/README.md`

**Purpose:**  
Provide the canonical **template set** for generating **global SHAP hazard explainability artifacts**, including:

- System-wide hazard driver vectors  
- Global narrative summaries  
- JSON-LD semantic evidence bundles  
- Global hazard-driver taxonomy mappings  
- STAC v11 XAI-compliant fields  
- PROV-O lineage templates  
- FAIR+CARE + sovereignty placeholders  

These templates guarantee **deterministic, reproducible, governance-aligned** global hazard explainability across **tornado**, **wind/gust**, **hail**, **flood/flash-flood**, **wildfire**, and **multi-hazard** models.

</div>

---

## 📘 Overview

This directory defines all **template scaffolds** needed to generate global hazard SHAP outputs, ensuring:

- Deterministic ordering of feature importance  
- Stable variable naming conventions  
- Governance-safe narrative vocabulary  
- Correct JSON-LD @context usage  
- Full FAIR+CARE compliance  
- Sovereignty-safe spatial abstraction via H3  
- STAC + PROV-O correctness  

The templates here feed:

- Global hazard explainability DAGs  
- Story Node v3 global hazard narratives  
- Focus Mode v3 global hazard reasoning  
- CI explainability validation pipelines  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/templates/global/
    ├── 📄 README.md                                  # This file
    │
    ├── 📄 shap-global-template.json                  # Canonical SHAP global vector structure
    ├── 📄 shap-global-summary-template.md            # Human-readable summary template
    │
    └── 📁 jsonld/                                    # JSON-LD semantic templates
        ├── 📄 xai-shap-global-template.jsonld        # Full semantic global XAI bundle
        └── 📄 hazard-driver-codes-template.jsonld    # Narrative driver taxonomy template

---

## 🔍 Template Specification

### 1. 🟥 `shap-global-template.json`
Defines canonical structure & key ordering for global SHAP vectors:

- `driver_name`  
- `importance` (normalized floats)  
- `direction` optional (if SHAP decomposition used)  
- `hazard_domain`  
- `model_version`  
- `care_scope` placeholder  
- `provenance` keys  

Ensures stable hashing for CI drift detection.

---

### 2. 🧾 `shap-global-summary-template.md`
Markdown summary template including:

- Hazard-domain description  
- Top drivers (placeholder tokens)  
- Seasonal patterns (optional template slots)  
- Terrain × climate × hazard interaction notes  
- CARE + sovereignty notes  
- Governance disclaimers  
- Template-safe narrative tone (no speculation)  

Used by Story Node editors & governance reviewers.

---

### 3. 🟩 JSON-LD Templates (`/jsonld/`)

#### **`xai-shap-global-template.jsonld`**
Defines semantic structure for global hazard explainability:

- `@context` (KFM-XAI + PROV-O)  
- `xai:drivers` list  
- `xai:importance` ranking  
- `xai:hazard_domain`  
- `xai:spatial_context` (H3 abstraction)  
- `care:scope` placeholder fields  
- `prov:*` lineage (required)  
- STAC fields (`kfm:model_version`, `kfm:input_items`, `checksum:multihash`)  

#### **`hazard-driver-codes-template.jsonld`**
Defines **canonical hazard driver taxonomy**, mapping raw SHAP features → narrative-safe categories:

Examples of template entries:

- `TORNADO_SIGNAL`  
- `SEVERE_STORM_ENV`  
- `HAIL_UPDRAFT`  
- `FLOOD_SOIL_SATURATION`  
- `WILDFIRE_FUELS_DRYNESS`  

Each driver includes:

- `xai:driver_code`  
- `xai:description` (CARE-safe)  
- `xai:linked_features` placeholder  
- `xai:story_node_roles`  
- `xai:focus_mode_tags`  
- `prov:wasDerivedFrom` template node  

---

## 📡 STAC Integration Template

Every global SHAP artifact generated from these templates must include:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:global`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata (if spatial)  
- CARE & sovereignty fields  
- PROV-O lineage  

---

## 🧾 PROV-O Template Requirements

Template structure enforces:

- `prov:wasGeneratedBy` — hazard model pipeline  
- `prov:used` — STAC hazard + climate datasets  
- `prov:generatedAtTime`  
- `prov:Agent` — model identity/version  
- `prov:wasDerivedFrom` placeholders for global→narrative mapping  

---

## 🔐 FAIR+CARE Template Rules

All templates must:

- Contain H3-generalization placeholders  
- Provide CARE scope + sovereignty fields  
- Exclude culturally sensitive terms  
- Provide abstracted hazard-driver descriptions  
- Avoid speculative or anthropogenic claims  
- Conform to Data Contract v3 hazard rules  

---

## 🧪 Template CI Requirements

Each template MUST pass:

- JSON Schema validation  
- Narrative-safety lexical scan  
- CARE/H3 masking rule checks  
- STAC-XAI extension lint  
- PROV-O structure lint  
- Deterministic hash reproducibility checks  

Failure = **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                |
|----------|------------|----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard SHAP Global Template Suite (aligned with full XAI)    |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard SHAP Templates](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

