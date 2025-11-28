---
title: "⚡🛰️📄🧬 KFM v11.2.2 — Hazard CAMs JSON-LD Template Suite (Semantic CAM Drivers · STAC-XAI · PROV-O · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/cams/templates/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Specification (Hazard CAM JSON-LD Templates)"

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
sensitivity: "Explainability-Hazard-CAM-JSONLD-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-cams-jsonld-template-suite"
  - "xai-cams-global-jsonld-template"
  - "cam-driver-taxonomy-template"
  - "spatial-cam-xai-schema"
  - "story-node-hazard-template"
  - "focus-mode-hazard-template"
  - "prov-xai-template"
  - "stac-xai-template"
  - "h3-generalization-template"
  - "faircare-governance-template"

scope:
  domain: "explainability/hazard/cams/templates/jsonld"
  applies_to:
    - "xai-cams-global-template.jsonld"
    - "cams-driver-taxonomy.jsonld"
    - "semantic-driver-taxonomy"
    - "story-node-integration"
    - "prov-xai"
    - "stac-xai"
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

# ⚡🛰️📄🧬 **Hazard CAMs — JSON-LD Template Suite**  
`docs/pipelines/ai/explainability/hazard/cams/templates/jsonld/README.md`

**Purpose:**  
Define the **canonical JSON-LD templates** for Hazard CAM (Class Activation Map) explainability, including:

- Semantic evidence bundles for raster + tile CAMs  
- Narrative-safe hazard-driver taxonomies  
- H3-generalized spatial attribution contexts  
- STAC-XAI compliance scaffolding  
- PROV-O lineage placeholders  
- FAIR+CARE & sovereignty governance anchors  

These templates guarantee **deterministic, governance-safe, semantically aligned CAM explainability** across tornado, hail, wind, wildfire, flood, and multi-hazard models.

</div>

---

## 📘 Overview

JSON-LD is the **semantic layer** of Hazard CAM explainability, allowing:

- Machine-readable hazard-driver semantics  
- Story Node v3 narrative extraction  
- Focus Mode v3 spatial reasoning  
- Cross-model hazard-driver unification  
- Ethical & sovereign-compliant hazard communication  
- STAC & PROV lineage traceability  

This suite provides the templates that pipelines must use to produce:

- `xai-cams-global.jsonld` (global CAM XAI)  
- `cams-driver-taxonomy.jsonld` (semantic hazard driver codes)

All templates enforce deterministic schemas, CARE-appropriate language, and H3 spatial masking.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/cams/templates/jsonld/
    ├── 📄 README.md                              # This file
    │
    ├── 📄 xai-cams-global-template.jsonld        # Template for global CAM JSON-LD evidence
    └── 📄 cams-driver-taxonomy.jsonld            # Template for semantic hazard-driver mapping

---

## 🟥 Template Specification — `xai-cams-global-template.jsonld`

Defines the JSON-LD structure for global CAM semantic explainability.

### Required sections:

**1. Contexts**
- `@context` — KFM-XAI vocabulary  
- PROV-O lineage vocabulary  

**2. Hazard Domain**
- `xai:hazard_domain` (`tornado | hail | wind | wildfire | flood | multi`)  

**3. Drivers Block**
`xai:drivers` array containing:
- `xai:driver_code`  
- `xai:description` (CARE-safe placeholder)  
- `xai:importance`  
- `xai:linked_features`  

**4. Spatial Context (Generalized)**
- `xai:spatial_context`  
  - `xai:h3_regions` — placeholder for generalized H3 sets  
  - `xai:region_summary` — abstract regional descriptions  

**5. CARE & Sovereignty Metadata**
- `care:scope`  
- `care:notes`  
- `sovereignty:flags`  

**6. STAC-XAI Required Fields**
- `kfm:explainability:method = "cams"`  
- `kfm:explainability:global`  
- `kfm:model_version`  
- `kfm:input_items` (STAC Item IDs)  
- `checksum:multihash`  

**7. PROV-O Lineage**
- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:generatedAtTime`  
- `prov:Agent`  

This template enforces deterministic ordering, schema, and governance rules.

---

## 🟩 Template Specification — `cams-driver-taxonomy.jsonld`

Defines narrative-safe semantic hazard driver codes.

### Required fields per driver:

- `xai:driver_code`  
  - e.g., `TORNADO_SUPERCELL_STRUCTURE_CAM`  

- `xai:description`  
  - CARE-safe, governed description placeholder  

- `xai:hazard_domain`  

- `xai:linked_features`  
  - Tile or raster CAM attribution sources  

- `xai:story_node_roles`  
  - `primary_driver | secondary_driver | contextual_driver`  

- `xai:focus_mode_tags`  

- `care:annotations`  

- `sovereignty:*`  

- `prov:wasDerivedFrom`  
  - Reference template linking to `xai-cams-global-template.jsonld`  

- `checksum:multihash`  

Templates ensure semantic consistency across hazard domains and stable driver naming across releases.

---

## 📡 STAC-XAI Template Requirements

Generated CAM JSON-LD must include:

- `kfm:explainability:method = "cams"`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata if spatial  
- CARE + sovereignty fields  
- PROV lineage  

Templates define placement & ordering.

---

## 🔐 FAIR+CARE & Sovereignty Enforcement

Hazard CAM JSON-LD templates embed placeholders for:

- H3 masking  
- CARE scope & mitigation metadata  
- Sovereignty flags  
- Cultural-safety filters  
- Data Contract v3 compliance  
- Non-speculative hazard language  
- No sensitive geographic identifiers  

All generated content must pass governance validation.

---

## 🧪 Template CI Enforcement

CI must confirm:

- JSON-LD schema validity  
- STAC-XAI compliance  
- PROV-O structure completeness  
- CARE + sovereignty placeholders present  
- H3 mask placeholders present  
- Deterministic key ordering  
- Narrative-safety lexical filtering  
- Hash-stability reproducibility  

Failure → ❌ PR blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                |
|----------|------------|----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard CAM JSON-LD Template Suite (raster + tiles + global) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard CAM Templates](../README.md)  
[🛰️ Hazard XAI Root](../../../../README.md)  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

