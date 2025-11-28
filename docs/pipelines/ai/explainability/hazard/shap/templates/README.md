---
title: "⚡🟥🧬 KFM v11.2.2 — Hazard SHAP Template Suite (Global · Local · Driver Taxonomy · JSON-LD)"
path: "docs/pipelines/ai/explainability/hazard/shap/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
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
sensitivity: "Explainability-Hazard-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-xai-templates"
  - "shap-global-template"
  - "shap-local-template"
  - "hazard-driver-taxonomy"
  - "jsonld-hazard-xai"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/hazard/shap/templates"
  applies_to:
    - "hazard-global-template"
    - "hazard-local-template"
    - "hazard-driver-taxonomy"
    - "jsonld-hazard-templates"
    - "faircare-governance"
    - "h3-masking"
    - "prov-xai"
    - "stac-xai"
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

# ⚡🟥🧬 **Hazard SHAP Template Suite**  
`docs/pipelines/ai/explainability/hazard/shap/templates/README.md`

**Purpose:**  
Provide the **governed template suite** for all hazard-related SHAP explainability outputs — including global drivers, local per-event drivers, semantic driver taxonomies, and JSON-LD explainability bundles.  
These templates ensure deterministic, FAIR+CARE-aligned, reproducible explainability across the hazard metadata ecosystem powering **Story Node v3**, **Focus Mode v3**, and KFM governance dashboards.

</div>

---

## 📘 Overview

This directory defines template scaffolding for all components of **Hazard SHAP Explainability**:

- 🌎 **Global SHAP** feature-importance template  
- 🧪 **Local SHAP** per-prediction template  
- 🧩 **Hazard Driver Taxonomy** (semantic driver codes)  
- 📄 **JSON-LD explainability bundles** (global, local, narrative)  
- 🧭 **H3-generalized spatial masking templates**  
- 📑 **STAC-XAI template fields**  
- 🔗 **PROV-O lineage templates**  

Hazards supported:

- Tornado / rotation / shear  
- Wind / gust / LLJ  
- Hail / severe convection  
- Wildfire / fuels / VPD  
- Flood / flash-flood / soil saturation  
- Multi-hazard fusion  

All templates are version-pinned, deterministic, and ready for enforcement by CI.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/templates/
    ├── 📄 README.md                                  # This file
    │
    ├── 📁 global/                                    # Global SHAP templates
    │   ├── 📄 shap-global-template.json
    │   ├── 📄 shap-global-summary-template.md
    │   └── 📄 xai-shap-global-template.jsonld
    │
    ├── 📁 local/                                     # Local (per-event) SHAP templates
    │   ├── 📄 shap-local-template.json
    │   ├── 📄 shap-event-summary-template.md
    │   └── 📄 xai-shap-local-template.jsonld
    │
    └── 📁 taxonomy/                                  # Hazard Semantic Driver Taxonomy
        ├── 📄 hazard-driver-taxonomy.json
        ├── 📄 driver-code-template.jsonld
        └── 📄 driver-taxonomy-notes.md

---

## 🔍 Template Categories

### 1. 🟥 Global SHAP Templates  
Define the required structure for:

- `global.json` SHAP vectors  
- `summary.md` global hazard interpretation  
- JSON-LD semantic evidence (`xai-shap-global.jsonld`)  

Required fields:

- Feature names  
- Normalized magnitudes  
- Hazard domain codes  
- CARE metadata  
- STAC `kfm:explainability:global` fields  
- PROV lineage anchors  

---

### 2. 🧪 Local SHAP Templates  
Define deterministic structure for:

- Per-event SHAP vectors  
- Local driver summaries  
- Local JSON-LD evidence objects  

Must include:

- H3 spatial masks  
- CARE scoping  
- `kfm:model_version`  
- `kfm:input_items`  
- Per-hazard driver taxonomy tags  

---

### 3. 🧩 Hazard Driver Taxonomy Templates  
Provide canonical, narrative-safe semantic drivers like:

- `TORNADO_SIGNAL`  
- `SEVERE_STORM_ENV`  
- `WILDFIRE_DRYNESS`  
- `FLOOD_SOIL_SATURATION`  
- `HAIL_UPDRAFT_GROWTH`  

Templates define:

- Driver code  
- Clean natural-language descriptions  
- CARE annotations  
- Story Node v3 semantic roles  
- Focus Mode v3 tags  
- PROV links  

---

### 4. 🧭 JSON-LD Template Models  
Semantic schemas for all XAI JSON-LD:

- Global bundles  
- Local bundles  
- Driver-code mappings  

Each JSON-LD template must include:

- `@context` (KFM-XAI + PROV-O)  
- CARE + sovereignty metadata  
- STAC XAI fields (`kfm:*`)  
- `checksum:multihash`  
- Provenance structure  

---

## 📡 STAC Integration Template

Templates define field requirements for:

- `kfm:explainability:{method}`  
- `kfm:model_version`  
- `kfm:input_items`  
- CRS & geometry (if spatial)  
- Driver-code references  
- JSON-LD link structure  

These are enforced by CI and lint rules.

---

## 🧾 PROV-O Template Requirements

Each template includes:

- Required `prov:wasGeneratedBy`  
- Required `prov:used` datasets  
- Required `prov:generatedAtTime`  
- Optional `prov:wasDerivedFrom` chain  
- Agent metadata for model + pipeline  

---

## 🔐 FAIR+CARE Template Requirements

All templates embed:

- H3 spatial abstraction placeholders  
- CARE scope & rationale fields  
- Sovereignty policy placeholders  
- No speculative language patterns  
- Only data-grounded semantics  

---

## 🧪 Testing Requirements (Template-Level)

Each template MUST:

- Validate under JSON Schema  
- Pass narrative-safety lexical scan  
- Pass CARE governance linter  
- Pass STAC-XAI lint  
- Pass provenance structure tests  
- Support deterministic rendering rules  

Failing any → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                       |
|----------|------------|-----------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard SHAP Template Suite aligned with global KFM explainability   |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard SHAP](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

