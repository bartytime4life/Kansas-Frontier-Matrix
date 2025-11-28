---
title: "⚡🛰️📄 KFM v11.2.2 — Hazard CAMs Raster JSON-LD Explainability Templates (Semantic Spatial Drivers · PROV-O · STAC-XAI · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/cams/rasters/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Specification (Hazard CAM Raster JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-hash>"
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
sensitivity: "Explainability-Hazard-CAM-Raster-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-cams-raster-jsonld-templates"
  - "semantic-spatial-attribution"
  - "pixel-level-driver-mapping"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "prov-xai"
  - "stac-xai"
  - "care-governance"
  - "h3-masking"

scope:
  domain: "explainability/hazard/cams/rasters/jsonld"
  applies_to:
    - "xai-cams-raster-template.jsonld"
    - "cams-raster-driver-codes-template.jsonld"
    - "semantic-driver-taxonomy"
    - "prov-xai"
    - "stac-xai"
    - "care-governance"
    - "h3-masking"
    - "spatial-driver-templates"

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

# ⚡🛰️📄 **Hazard CAMs — Raster JSON-LD Template Suite**  
`docs/pipelines/ai/explainability/hazard/cams/rasters/jsonld/README.md`

**Purpose:**  
Provide the **canonical template suite** for **JSON-LD semantic explainability bundles** associated with **Hazard CAM rasters** (COG/GeoTIFF).  
These templates ensure all raster-based CAM explainability is:

- Deterministic  
- FAIR+CARE aligned  
- Sovereignty-compliant  
- H3-generalized  
- STAC-XAI v11 conformant  
- PROV-linked  
- Story Node v3 & Focus Mode v3 compatible  

</div>

---

## 📘 Overview

This directory defines the JSON-LD **“schema-of-schemas”** for transforming raster CAM attribution maps into semantic, machine-readable explainability bundles.

It includes:

1. **`xai-cams-raster-template.jsonld`**  
   – Structure for the semantic raster-level CAM evidence bundle.

2. **`cams-raster-driver-codes-template.jsonld`**  
   – Narrative-safe hazard-driver taxonomy for CAM raster patterns.

All templates incorporate:

- STAC-XAI v11 extension fields  
- PROV-O lineage requirements  
- H3-generalized spatial masking fields  
- CARE + sovereignty placeholders  
- Narrative-safe semantics  
- Deterministic ordering (for CI reproducibility)  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/cams/rasters/jsonld/
    ├── 📄 README.md                                # This file
    │
    ├── 📄 xai-cams-raster-template.jsonld          # Template for raster-level CAM semantic evidence
    └── 📄 cams-raster-driver-codes-template.jsonld # Template for semantic CAM driver taxonomy

---

## 🟥 Template Specification — `xai-cams-raster-template.jsonld`

Defines the semantic JSON-LD envelope for **COG/GeoTIFF hazard CAM explainability**.

### Required structural fields

**1. Contexts**

- `@context`  
  - KFM-XAI ontology context  
  - PROV-O lineage context  

**2. Raster Metadata**

- `xai:hazard_domain` — tornado | hail | wind | wildfire | flood | multi  
- `xai:attribution_method = "cams"`  
- `xai:raster_href` — link to CAM raster (COG/GeoTIFF)  
- `xai:raster_stats` — min/max/mean placeholders  

**3. Spatial Context (Generalized)**

- `xai:spatial_context`  
  - `xai:h3_regions` — generalized H3 hexes  
  - `xai:region_summary` — high-level, non-sensitive description  

**4. Drivers Block**

`xai:drivers` (array of objects):
- `xai:driver_code`  
- `xai:importance` (optional raster summary)  
- `xai:description` (CARE-safe placeholder)  
- `xai:linked_features`  

**5. CARE & Sovereignty Metadata**

- `care:scope`  
- `care:notes`  
- `sovereignty:flags`  

**6. STAC-XAI Required Fields**

- `kfm:explainability:method = "cams"`  
- `kfm:explainability:raster`  
- `kfm:model_version`  
- `kfm:input_items` (STAC Items used for hazard inference)  
- `checksum:multihash`  

**7. PROV-O Lineage**

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional: `prov:wasDerivedFrom` (CAM ↔ IG/SHAP linkage)  

This template defines **exact field presence, names, and ordering** enforced via CI.

---

## 🟩 Template Specification — `cams-raster-driver-codes-template.jsonld`

Defines the narrative-safe taxonomy of **semantic hazard drivers** associated with CAM raster patterns.

Each driver entry MUST include:

- `xai:driver_code`  
  - e.g., `TORNADO_SUPERCELL_STRUCTURE_CAM`, `FLOOD_POOLING_ZONE_CAM`

- `xai:description`  
  - CARE-safe, governance-approved placeholder text  

- `xai:hazard_domain`  
  - Domain classification (tornado|hail|wind|wildfire|flood|multi)

- `xai:linked_features`  
  - Placeholder list for feature map channels / model inputs  

- `xai:story_node_roles`  
  - How the driver appears in Story Node v3 narrative (primary/secondary/contextual)

- `xai:focus_mode_tags`  
  - Tags used for Focus Mode semantic reasoning

- `care:annotations`  
  - Required CARE-specific masking & context guidance  

- `sovereignty:*`  
  - Explicit sovereignty compliance placeholders  

- `prov:wasDerivedFrom`  
  - Linkage to raster semantic evidence  

- `checksum:multihash`  
  - Deterministic asset checksum placeholder  

This taxonomy ensures semantic uniformity across all CAM-based hazard interpretations.

---

## 📡 STAC-XAI Compliance

Generated JSON-LD from these templates MUST include:

- `kfm:explainability:method = "cams"`  
- `kfm:explainability:raster`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS/vertical metadata if spatial  
- CARE + sovereignty metadata  
- PROV-O lineage  
- Links to raster (.tif) assets  

Templates guarantee field position + schema.

---

## 🔐 FAIR+CARE & Sovereignty Rules

All derived JSON-LD **must:**

- Use H3 spatial abstraction for sensitive geography  
- Mask culturally sensitive or restricted hazard-related areas  
- Include sovereignty flags and CARE scope notes  
- Avoid speculative or harmful language  
- Follow Data Contract v3 hazard data rules  
- Use governance-approved driver terminology ONLY  

---

## 🧪 Template CI Enforcement

CI MUST verify:

- JSON-LD schema correctness  
- STAC-XAI compatibility  
- PROV-O structure completeness  
- CARE/sovereignty placeholder presence  
- H3 generalization fields present  
- Deterministic key ordering  
- Narrative-safety lexical rules  
- Hash-stability consistency  

Failure → ❌ **PR blocked**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                             |
|---------|------------|-----------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard CAM Raster JSON-LD Template Suite (aligned with IG & SHAP XAI)     |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard CAM Raster](../README.md) · [⚡ Hazard XAI Root](../../../README.md) · [🏛 Governance](../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

