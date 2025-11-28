---
title: "⚡🟩🧬 KFM v11.2.2 — Hazard Integrated Gradients (IG) Template Suite (Global · Local · JSON-LD · Driver Taxonomy)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Explainability Template Suite"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Explainability-Hazard-IG-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ig-template-suite"
  - "hazard-ig-global-template"
  - "hazard-ig-local-template"
  - "hazard-ig-driver-taxonomy"
  - "semantic-driver-mapping"
  - "stac-xai-template"
  - "prov-o-template"
  - "story-node-hazard-template"
  - "focus-mode-hazard-template"
  - "faircare-governance-template"

scope:
  domain: "explainability/hazard/integrated-gradients/templates"
  applies_to:
    - "ig-global-template"
    - "ig-local-template"
    - "hazard-ig-driver-taxonomy"
    - "xai-ig-global-jsonld-template"
    - "xai-ig-local-jsonld-template"
    - "stac-xai"
    - "prov-xai"
    - "care-governance"
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

# ⚡🟩🧬 **Hazard Integrated Gradients — Template Suite**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/README.md`

**Purpose:**  
Provide the **canonical template suite** for all Hazard-IG explainability components, including:

- Global IG templates  
- Local IG templates  
- Semantic JSON-LD templates  
- Narrative hazard driver taxonomy  
- FAIR+CARE + sovereignty placeholders  
- STAC v11 + PROV-O integration templates  

These templates ensure **deterministic, reproducible, governance-safe IG explainability** for tornado, hail, wind, flood, wildfire, and multi-hazard deep-learning models.

</div>

---

## 📘 Overview

Hazard IG explainability requires **high-fidelity gradient attribution workflows** across:

- Deep CNN/RNN transformer hazard models  
- Spatiotemporal hazard forecasting  
- Multi-hazard fusion engines  

This directory defines the **templates** used to generate:

- `ig-global.json` (raw global IG vectors)  
- `ig-samples.json` (per-event IG vectors)  
- JSON-LD global hazard XAI bundles  
- JSON-LD local hazard XAI bundles  
- Hazard IG semantic driver taxonomies  
- Governance-safe summary documents  

Every file generated downstream must conform to these templates exactly.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/integrated-gradients/templates/
    ├── 📄 README.md                                # This file
    │
    ├── 📁 global/                                   # Templates for global IG explainability
    │   ├── 📄 ig-global-template.json
    │   ├── 📄 ig-global-summary-template.md
    │   └── 📁 jsonld/
    │       ├── 📄 xai-ig-global-template.jsonld
    │       └── 📄 hazard-ig-driver-codes-template.jsonld
    │
    ├── 📁 local/                                    # Templates for local IG explainability
    │   ├── 📄 ig-local-template.json
    │   ├── 📄 ig-local-summary-template.md
    │   └── 📁 jsonld/
    │       ├── 📄 xai-ig-local-template.jsonld
    │       └── 📄 hazard-ig-driver-codes-local-template.jsonld
    │
    └── 📁 taxonomy/                                 # Hazard IG semantic driver taxonomy
        ├── 📄 hazard-ig-driver-taxonomy.json
        ├── 📄 driver-code-template.jsonld
        └── 📄 driver-taxonomy-notes.md

---

## 🔍 Template Categories

### 1. 🟥 Global IG Templates (`global/`)
Provide scaffolding for:

- Global IG vector structures  
- Aggregate gradient driver summaries  
- JSON-LD global IG evidence bundles  
- CARE-safe driver semantics  
- PROV-O lineage  
- STAC-XAI metadata fields  

Fields include placeholders for:

- `xai:drivers`  
- `xai:importance`  
- `xai:hazard_domain`  
- `xai:spatial_context` (H3 generalized)  
- `kfm:model_version`  
- `prov:*` lineage elements  

---

### 2. 🧪 Local IG Templates (`local/`)
Provide deterministic templates for per-event hazard IG explainability:

- `ig-local-template.json` — raw gradient structure  
- `ig-local-summary-template.md` — human-readable summary  
- `xai-ig-local-template.jsonld` — JSON-LD semantics  
- Local hazard driver taxonomy templates  

Include placeholders for:

- Event ID  
- Local driver gradients  
- H3-masked spatial context  
- CARE scope + sovereignty flags  
- `kfm:input_items`  
- `checksum:multihash`  

---

### 3. 🧩 Hazard IG Driver Taxonomy (`taxonomy/`)
Defines semantic mappings:

- IG gradient features → human-interpretable hazard drivers  
- Story Node v3 roles (primary, secondary, contextual)  
- Focus Mode v3 reasoning tags  
- CARE and sovereignty annotations  
- PROV linkage  
- Deterministic key ordering  

Ensures semantic consistency across all hazard reasoning systems.

---

## 📡 STAC-XAI Template Requirements

Every generated IG explainability asset must contain:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:{global|local}`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS/vertical datum metadata (if spatial)  
- CARE scope + sovereignty metadata  
- PROV lineage fields  

The template suite places placeholders for these fields in correct order and structure.

---

## 🧾 PROV-O Template Requirements

Templates enforce full PROV compatibility:

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional: `prov:wasDerivedFrom` (for IG ↔ SHAP ↔ narrative linking)

---

## 🔐 FAIR+CARE & Sovereignty Template Rules

Templates **must** contain:

- H3 spatial abstraction placeholders  
- CARE scope and annotation placeholders  
- Sovereignty flags  
- Non-speculative, governance-safe language scaffolding  
- Compliance with Data Contract v3 + hazard ethics  

They **must not** contain:

- Sensitive locations  
- Cultural/tribal identifiers  
- Unvalidated hazard causality  

---

## 🧪 Template CI Checks

CI enforces:

- JSON / JSON-LD schema correctness  
- Deterministic key ordering  
- CARE + sovereignty placeholders  
- STAC-XAI compliance  
- PROV-O structure  
- Narrative-safety lexical rules  
- Hash-stability checks  

Failure → **PR blocked**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                           |
|--------|------------|---------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard IG Template Suite (matching SHAP, Climate IG, CAMs, Spatial XAI) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard IG](../README.md)  
[⚡ Hazard XAI Root](../../README.md)  
[🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

