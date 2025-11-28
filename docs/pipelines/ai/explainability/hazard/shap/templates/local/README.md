---
title: "⚡🟥🧪🧬 KFM v11.2.2 — Hazard SHAP Local Template Suite (Event-Level Drivers · JSON-LD · Narrative Codes)"
path: "docs/pipelines/ai/explainability/hazard/shap/templates/local/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Set (Hazard SHAP Local)"

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
sensitivity: "Explainability-Templates-Hazard-Local"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-local-shap-templates"
  - "event-driver-xai-templates"
  - "semantic-driver-taxonomy"
  - "xai-jsonld-templates"
  - "prov-xai-templates"
  - "story-node-hazard"
  - "focus-mode-hazard"

scope:
  domain: "explainability/hazard/shap/templates/local"
  applies_to:
    - "hazard-local-shap-template"
    - "hazard-event-driver-template"
    - "xai-shap-local-jsonld-template"
    - "driver-codes-local-template"
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

# ⚡🟥🧪🧬 **Hazard SHAP — Local Template Suite**  
`docs/pipelines/ai/explainability/hazard/shap/templates/local/README.md`

**Purpose:**  
Provide the **template suite** for all **local/event-level hazard SHAP explainability** artifacts — defining the required JSON, Markdown, and JSON-LD structures for:

- Per-event SHAP vectors  
- Local hazard driver summaries  
- Local semantic driver taxonomy  
- Local JSON-LD explainability bundles  
- STAC-XAI + PROV-O integration  
- CARE + sovereignty + H3 masking placeholders  

These templates guarantee **deterministic, reproducible, FAIR+CARE-compliant hazard explainability** across tornado, hail, wind, wildfire, flood, and multi-hazard models.

</div>

---

## 📘 Template Overview

This directory defines the **governed scaffolding** for all local hazard explainability components:

- 🔍 **Local SHAP Vectors** (raw per-event drivers)  
- 🧩 **Driver Summaries** (Markdown templates for human-readable explanations)  
- 📄 **JSON-LD Local Evidence** (semantic representation for reasoning)  
- 🧭 **Narrative Driver Codes** (Story Node & Focus Mode mappings)  
- 🔐 **CARE + H3 masking templates**  
- 🧾 **PROV-O lineage stubs**  
- 🗄️ **STAC-XAI placeholder fields**  

All templates enforce correct key ordering, metadata presence, and semantic safety.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/templates/local/
    ├── 📄 README.md                                # This file
    │
    ├── 📄 shap-local-template.json                 # Canonical local SHAP vector structure
    ├── 📄 shap-local-summary-template.md           # Human-read summary template
    │
    └── 📁 jsonld/                                  # JSON-LD semantic templates
        ├── 📄 xai-shap-local-template.jsonld       # Local event-level XAI bundle
        └── 📄 hazard-driver-codes-local.jsonld     # Narrative-safe driver taxonomy template

---

## 🔍 Template Definitions

### 1. 🟥 `shap-local-template.json` — Local SHAP Vector Template

Defines the deterministic structure for:

- Feature names  
- SHAP magnitude values  
- Contribution direction (pos/neg)  
- Hazard domain  
- CARE/H3 masking placeholders  
- `model_version` field  
- Traceability metadata fields to support PROV-O  
- STAC input references  

Keys must remain in stable order to support deterministic hashing.

---

### 2. 🧾 `shap-local-summary-template.md` — Event-Level Summary Template

Contains placeholders for:

- Event context (time, location — masked/generalized)  
- Top SHAP drivers ranked  
- Hazard-domain interpretation guidance  
- CARE + sovereignty disclaimers  
- Narrative-safe vocabulary  
- Links to JSON-LD bundle & provenance chain  

Used by:

- Story Node editors  
- Hazard governance audit reviews  
- CI-based narrative safety tests  

---

### 3. 🟩 JSON-LD Templates (`/jsonld/`)

#### **`xai-shap-local-template.jsonld`**
Defines the semantic JSON-LD model for local hazard explainability:

Required sections:

- `@context` (KFM-XAI + PROV-O)  
- `xai:event_id`  
- `xai:hazard_domain`  
- `xai:drivers`  
- `xai:spatial_context` (H3-generalized)  
- CARE metadata placeholders  
- PROV lineage placeholders  
- STAC-XAI fields:
  - `kfm:explainability:local`
  - `kfm:model_version`
  - `kfm:input_items`
  - `checksum:multihash`  

#### **`hazard-driver-codes-local.jsonld`**
Defines the narrative-safe taxonomy for local hazard drivers:

Each entry includes placeholders for:

- `xai:driver_code`  
- `xai:description` (CARE-safe)  
- `xai:linked_features`  
- `xai:hazard_domain` (tornado|wind|hail|wildfire|flood|multi)  
- `xai:story_node_roles`  
- `xai:focus_mode_tags`  
- CARE annotations  
- Provenance mapping  

These ensure consistent semantic representation across all hazard narratives and Focus Mode windows.

---

## 📡 STAC-XAI Template Rules

Generated artifacts must contain:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata if spatial context is present  
- Links to JSON-LD driver taxonomy templates  

Templates include placeholder fields in the correct order and schema.

---

## 🧾 PROV-O Template Requirements

Local hazard XAI templates must include:

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional: `prov:wasDerivedFrom` (local → narrative mapping)  

---

## 🔐 FAIR+CARE Template Rules

All templates contain:

- CARE scope fields (`care:scope`, `care:notes`)  
- Sovereignty flags  
- H3 spatial generalization placeholders  
- Narrative-safe vocabulary guidelines  
- Explicit bans on sensitive, culturally inappropriate, or speculative language  

---

## 🧪 Template CI Requirements

CI MUST validate:

- JSON Schema compliance  
- CARE masking fields present  
- Sovereignty placeholders present  
- STAC-XAI fields present  
- PROV-O lineage structure  
- Deterministic key ordering  
- Narrative safety lexical checks  

Failing tests = **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                       |
|----------|------------|-----------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard SHAP Local Template Suite (aligned with global suite & XAI)  |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard SHAP Templates](../README.md) · [⚡ Hazard XAI Root](../../../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

