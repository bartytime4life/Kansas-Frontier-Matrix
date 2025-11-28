---
title: "⚡🟩🧪🧬 KFM v11.2.2 — Hazard Integrated Gradients (IG) Local Template Suite (Event Drivers · JSON-LD · Taxonomy)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/local/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Template Set (Hazard IG Local)"

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
sensitivity: "Explainability-Hazard-IG-Local-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ig-local-templates"
  - "event-driver-xai-templates"
  - "local-ig-taxonomy"
  - "xai-local-jsonld"
  - "prov-xai-templates"
  - "stac-xai-templates"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "care-governance"
  - "h3-masking"

scope:
  domain: "explainability/hazard/integrated-gradients/templates/local"
  applies_to:
    - "ig-local-template.json"
    - "ig-local-summary-template.md"
    - "xai-ig-local-template.jsonld"
    - "hazard-ig-driver-codes-local-template.jsonld"
    - "semantic-driver-taxonomy"
    - "care-governance"
    - "h3-masking"
    - "prov-xai"
    - "stac-xai"
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

# ⚡🟩🧪🧬 **Hazard Integrated Gradients — Local Template Suite**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/local/README.md`

**Purpose:**  
Provide the **authoritative template suite** for generating **local/event-level IG explainability artifacts** for hazard models — including raw IG vectors, human-readable summaries, semantic JSON-LD evidence bundles, narrative-safe driver codes, and governance-required metadata.

These templates ensure that IG explainability for tornado, hail, wind, flood, wildfire, and multi-hazard models is:  
**deterministic**, **FAIR+CARE aligned**, **masking-compliant**, **STAC v11–compatible**, and **ready for Story Node v3 and Focus Mode v3 reasoning**.

</div>

---

## 📘 Overview

Local Integrated Gradients (IG) explainability reveals **why a hazard model predicted a specific outcome for a specific event**, based solely on gradients from a deep-learning model.

This template directory defines:

- JSON structure for **per-event IG driver values**  
- JSON-LD structure for **semantic hazard-driver evidence**  
- Taxonomy structure linking **raw IG features → narrative hazard drivers**  
- CARE + sovereignty metadata placeholders  
- STAC-XAI + PROV-O placeholder structures  
- Deterministic ordering and reproducibility requirements  

Hazard domains supported:

- 🌀 Tornado  
- 🌩️ Hail  
- 💨 Severe wind / gust / LLJ  
- 🔥 Wildfire  
- 🌧️ Flood / Flash-Flood  
- ⚡ Hybrid multi-hazard models  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/local/
    ├── 📄 README.md                                  # This file
    │
    ├── 📄 ig-local-template.json                     # Canonical local IG gradient template
    ├── 📄 ig-local-summary-template.md               # Governance-safe narrative summary template
    │
    └── 📁 jsonld/                                     # Semantic IG Local JSON-LD templates
        ├── 📄 xai-ig-local-template.jsonld           # Local IG semantic evidence template
        └── 📄 hazard-ig-driver-codes-local-template.jsonld # Local hazard-driver taxonomy template

---

## 🔍 Template Categories

### 1. 🟥 `ig-local-template.json` — Local IG Raw Vector Template

Defines required fields and ordering:

- Feature gradients (`importance`, `direction`)  
- Hazard-domain labels  
- Event identifiers  
- CARE-masking placeholders  
- Sovereignty annotations  
- `model_version` and `pipeline_version`  
- Deterministic field ordering  
- No sensitive location information  

Used by CI to validate correctness of raw IG output before semantic conversion.

---

### 2. 🧾 `ig-local-summary-template.md` — Narrative Summary Template

Human-readable summary scaffolding:

- Hazard event title (abstracted, non-location specific)  
- Top IG drivers (token placeholders)  
- Domain interactions (CAPES × shear, VPD × fuels, etc.)  
- CARE + sovereignty disclaimers  
- Advisory for Story Node editors  
- Fields referencing the JSON-LD bundle  

Only narrative-safe language permitted.

---

### 3. 🟩 JSON-LD Templates (`/jsonld/`)

#### **`xai-ig-local-template.jsonld`**
Defines the structure for actual semantic IG local JSON-LD bundles.

Required template fields:

- `@context`  
  - KFM-XAI ontology  
  - PROV-O ontology  

- `xai:event_id`  
- `xai:hazard_domain`  
- `xai:drivers` array with:
  - `xai:driver_code`  
  - `xai:importance`  
  - `xai:linked_features`  
  - `xai:uncertainty` (optional placeholder)  

- Spatial masking  
  - `xai:spatial_context`  
  - `xai:h3_regions`  
  - `xai:region_summary`  

- CARE metadata  
  - `care:scope`  
  - `care:notes`  

- Sovereignty  
  - `sovereignty:flags`  

- STAC-XAI fields  
  - `kfm:explainability:method = "integrated-gradients"`  
  - `kfm:explainability:local`  
  - `kfm:model_version`  
  - `kfm:input_items`  
  - `checksum:multihash`  

- PROV-O lineage  
  - `prov:wasGeneratedBy`  
  - `prov:used`  
  - `prov:generatedAtTime`  
  - `prov:Agent`

#### **`hazard-ig-driver-codes-local-template.jsonld`**
Defines hazard “semantic driver” categories for IG local explanations.

Required template fields:

- `xai:driver_code`  
- `xai:description` (CARE-safe)  
- `xai:hazard_domain`  
- `xai:linked_features`  
- `xai:story_node_roles`  
- `xai:focus_mode_tags`  
- `care:annotations`  
- `sovereignty:*`  
- `prov:wasDerivedFrom` → link to local evidence template  

Ensures semantically stable, narrative-safe, governance-aligned driver codes.

---

## 📡 STAC-XAI Template Requirements

Generated IG local JSON-LD **must** include:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS/vertical datum (if spatial)  
- CARE & sovereignty metadata  
- PROV-O lineage  

Templates enforce field presence and correct ordering for CI.

---

## 🧾 PROV-O Template Requirements

Templates require:

- `prov:wasGeneratedBy` (IG inference pipeline)  
- `prov:used` (STAC hazard + climate datasets)  
- `prov:Agent`  
- `prov:generatedAtTime`  
- Optional:
  - `prov:wasDerivedFrom` (link local IG → global IG or taxonomy)

---

## 🔐 FAIR+CARE & Sovereignty Template Rules

All templates **must** include:

- H3 spatial abstraction  
- CARE-scope placeholders  
- Sovereignty protection placeholders  
- Governance-safe vocabulary  
- Prohibitions on sensitive locations & speculation  
- Explicit Data Contract v3 alignment  

---

## 🧪 Template CI Requirements

CI validation includes:

- JSON-LD schema validation  
- STAC-XAI compliance  
- CARE & sovereignty placeholder presence  
- H3 masking placeholder checks  
- Deterministic ordering tests  
- Narrative-safety lexical scan  
- PROV-O consistency  

Failing any test → **merge blocked**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                         |
|--------|------------|-------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard IG Local Template Suite (aligned with Global IG + SHAP suites) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard IG Templates](../README.md)  
[⚡ Hazard XAI Root](../../README.md)  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

