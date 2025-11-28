---
title: "⚡🛰️🧩 KFM v11.2.2 — Hazard CAMs Tile Template Suite (GeoParquet Tiles · Semantic Spatial Drivers · STAC-XAI · PROV-O · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/cams/templates/tiles/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Template Specification (Hazard CAM Tile Templates)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
energy_schema: "../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../schemas/telemetry/carbon-v2.json"

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
sensitivity: "Explainability-Hazard-CAM-Tile-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-cams-tile-template-suite"
  - "geo-parquet-tile-template"
  - "xai-cams-tiles-template"
  - "cam-driver-taxonomy-template"
  - "spatial-attribution-template"
  - "story-node-hazard-template"
  - "focus-mode-hazard-template"
  - "prov-xai-template"
  - "stac-xai-template"
  - "faircare-governance"
  - "h3-masking"

scope:
  domain: "explainability/hazard/cams/templates/tiles"
  applies_to:
    - "cams-tile-template.json"
    - "cams-tile-driver-taxonomy.jsonld"
    - "xai-cams-tiles-template.jsonld"
    - "semantic-driver-taxonomy"
    - "h3-generalization"
    - "prov-xai"
    - "stac-xai"
    - "care-governance"
    - "narrative-driver-templates"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# ⚡🛰️🧩 **Hazard CAMs — Tile Template Suite**  
`docs/pipelines/ai/explainability/hazard/cams/templates/tiles/README.md`

**Purpose:**  
Define the **governed, deterministic template suite** for **tile-based Hazard CAM explainability**, covering:

- GeoParquet tile structure templates  
- Semantic JSON-LD tile evidence templates  
- Narrative-safe hazard driver taxonomy templates  
- FAIR+CARE, sovereignty, and H3-generalization scaffolding  
- Full STAC-XAI and PROV-O integration  

This suite ensures tile-level CAM explainability is fully aligned across Story Node v3, Focus Mode v3, STAC v11, and KFM’s ethics + governance frameworks.

</div>

---

## 📘 Overview

Hazard CAM tiles (GeoParquet) provide **zoom-independent spatial attributions** from deep hazard models.  
This template suite defines how tile-level CAM explainability **must be structured**, ensuring:

- Deterministic schema  
- Semantic consistency across hazard domains  
- FAIR+CARE compliance  
- Sovereignty protection  
- H3-generalized spatial masking  
- Reproducibility under CI  
- Seamless Story Node + Focus Mode integration  

Supported hazard domains:

- 🌀 Tornado  
- 🌩️ Hail  
- 💨 Wind/Gust  
- 🌧️ Flood / Flash-flood  
- 🔥 Wildfire  
- ⚡ Multi-hazard fusion models  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/cams/templates/tiles/
    ├── 📄 README.md                                      # This file
    │
    ├── 📄 cams-tile-template.json                        # Canonical GeoParquet tile schema
    ├── 📄 cams-tile-driver-taxonomy.jsonld               # Hazard CAM driver taxonomy template
    │
    └── 📄 xai-cams-tiles-template.jsonld                 # JSON-LD semantic evidence bundle template

---

## 🔍 Template Specifications

### 1. 🧩 `cams-tile-template.json` — Tile Schema Template

Defines:

- Tile index scheme (z/x/y or grid index)  
- Required partition keys  
- CRS + vertical metadata  
- Tile resolution requirements  
- Tile-level driver summary placeholders  
- CARE + sovereignty placeholders  
- H3-generalization structure  
- Deterministic key ordering  
- STAC-XAI hooks  
- PROV lineage anchors  

Ensures every generated tile dataset is structurally valid.

---

### 2. 🟦 `xai-cams-tiles-template.jsonld` — Semantic Tile Evidence Template

Defines the JSON-LD structure consumed by reasoning engines.

Required fields:

- `@context` — KFM-XAI + PROV-O  
- `xai:hazard_domain`  
- `xai:tile_index`  
- `xai:tile_href`  
- `xai:drivers` list:
  - `xai:driver_code`  
  - `xai:importance`  
  - `xai:linked_features`  
  - `xai:description` (CARE-safe placeholder)  
- `xai:spatial_context`:
  - `xai:h3_regions`  
  - `xai:region_summary`  
- CARE & sovereignty metadata  
- STAC-XAI fields:
  - `kfm:explainability:method = "cams"`  
  - `kfm:explainability:tiles`  
  - `kfm:model_version`  
  - `kfm:input_items`  
  - `checksum:multihash`  
- PROV lineage:
  - `prov:wasGeneratedBy`  
  - `prov:used`  
  - `prov:generatedAtTime`  
  - `prov:Agent`  

All field positions are fixed for CI enforcement.

---

### 3. 🟩 `cams-tile-driver-taxonomy.jsonld` — Narrative-Safe Driver Taxonomy Template

Defines hazard driver semantics at the tile level.

Required fields per driver entry:

- `xai:driver_code`  
- `xai:description` (CARE-safe placeholder)  
- `xai:hazard_domain`  
- `xai:linked_features`  
- `xai:story_node_roles`  
- `xai:focus_mode_tags`  
- `care:annotations`  
- `sovereignty:*`  
- `prov:wasDerivedFrom` — link to tile evidence template  
- `checksum:multihash`  

Used by:

- Story Node v3 hazard narratives  
- Focus Mode hazard reasoning overlays  
- Hazard governance dashboards  

---

## 📡 STAC-XAI Template Requirements

Generated assets MUST include:

- `kfm:explainability:method = "cams"`  
- `kfm:explainability:tiles`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata  
- CARE + sovereignty flags  
- PROV-O lineage metadata  

Templates strictly define order + presence of these fields.

---

## 🧾 PROV-O Template Requirements

Every tile JSON-LD output MUST support:

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:Agent`  
- `prov:generatedAtTime`  
- Optional:
  - `prov:wasDerivedFrom` for linking to upstream rasters / IG / SHAP  

---

## 🔐 FAIR+CARE & Sovereignty Enforcement

All CAM tile templates embed placeholders for:

- H3 spatial abstraction  
- CARE scope + mitigation metadata  
- Sovereignty protections  
- Cultural-safety constraints  
- No explicit sensitive geography  
- No speculative hazard reasoning  
- Conformance with Data Contract v3  

---

## 🧪 Template CI Enforcement

CI tests must validate:

- JSON / JSON-LD schema validity  
- Deterministic key ordering  
- STAC-XAI compliance  
- PROV-O completeness  
- CARE + sovereignty placeholders  
- H3-mask placeholders  
- Narrative-safe lexicon scan  
- Hash consistency  

Failing any → **PR blocked**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                          |
|--------|------------|--------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard CAM Tile Template Suite (aligned with raster, IG, SHAP suites) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard CAM Templates](../README.md)  
[🛰️ Hazard XAI Root](../../../../README.md)  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

