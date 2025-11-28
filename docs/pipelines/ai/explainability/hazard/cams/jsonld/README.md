---
title: "⚡🛰️📄 KFM v11.2.2 — Hazard CAMs JSON-LD Explainability (Semantic Spatial Drivers · PROV-O · STAC-XAI · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/cams/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Component (Hazard CAM JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
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
sensitivity: "Explainability-Hazard-CAM-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-cams-jsonld"
  - "semantic-driver-mapping"
  - "spatial-cam-explainability"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "prov-xai"
  - "stac-xai"
  - "care-governance"
  - "h3-generalization"

scope:
  domain: "explainability/hazard/cams/jsonld"
  applies_to:
    - "xai-cams-global.jsonld"
    - "xai-cams-driver-codes.jsonld"
    - "semantic-driver-taxonomy"
    - "story-node-integration"
    - "prov-xai"
    - "stac-xai"
    - "care-governance"
    - "h3-generalization"
    - "spatial-driver-metadata"

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

# ⚡🛰️📄 **Hazard CAMs — JSON-LD Explainability Layer**  
`docs/pipelines/ai/explainability/hazard/cams/jsonld/README.md`

**Purpose:**  
Define the **semantic JSON-LD explainability layer** for Hazard CAM (Class Activation Map) outputs, unifying:

- Raster-based CAM evidence  
- Tile-based CAM evidence  
- Narrative-safe hazard-driver taxonomies  
- FAIR+CARE + sovereignty metadata  
- STAC-XAI explainability fields  
- PROV-O lineage  

This enables CAM explainability to seamlessly flow into **Story Node v3**, **Focus Mode v3**, and governance systems.

</div>

---

## 📘 Overview

Hazard CAM JSON-LD files provide **structured, machine-readable** representations of spatial hazard-driver evidence extracted from CAM maps.

They encode:

- Hazard driver semantics  
- Tile- or raster-level spatial context  
- Generalized (H3) geographic abstraction  
- CARE + sovereignty labels  
- Relationships to STAC Items  
- Provenance describing how CAM explainability was generated  
- Narrative-ready descriptors for use by Story Node v3

This directory governs JSON-LD **artifact specifications**, not raw CAM data.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/cams/jsonld/
    ├── 📄 README.md                          # This file
    │
    ├── 📄 xai-cams-global.jsonld             # Semantic CAM explainability bundle (global)
    └── 📄 xai-cams-driver-codes.jsonld       # Narrative-safe driver taxonomy for CAM semantics

---

## 🟥 Component: `xai-cams-global.jsonld`

This file expresses **semantic CAM evidence** from raster or tile CAMs.

### Required fields:

- `@context` — KFM-XAI + PROV-O contexts  
- `xai:hazard_domain`  
- `xai:drivers` (array, semantic hazard drivers)  
- `xai:spatial_context`  
  - `xai:h3_regions`  
  - `xai:region_summary`  
- CARE scope metadata  
- Sovereignty flags  
- STAC-XAI fields:
  - `kfm:explainability:method = "cams"`  
  - `kfm:model_version`  
  - `kfm:input_items`  
  - `checksum:multihash`  
- PROV lineage  
  - `prov:wasGeneratedBy`  
  - `prov:used`  
  - `prov:generatedAtTime`  
  - `prov:Agent`

Used for:

- Story Node v3 global hazard narratives  
- Focus Mode v3 map overlays and evidence reasoning  

---

## 🟩 Component: `xai-cams-driver-codes.jsonld`

A narrative-safe taxonomy defining CAM-derived hazard drivers.

### Each entry includes:

- `xai:driver_code`  
  - e.g., `TORNADO_SUPERCELL_STRUCTURE_CAM`  
- `xai:description` (CARE-safe)  
- `xai:hazard_domain`  
- `xai:linked_features`  
- `xai:story_node_roles`  
  - `primary_driver`, `secondary_driver`, `contextual_driver`  
- `xai:focus_mode_tags`  
- `care:annotations`  
- `sovereignty:*`  
- `prov:wasDerivedFrom`  
- `checksum:multihash`

Used by:

- Story Node v3 narrative assembly  
- Focus Mode overlay reasoning  
- Hazard governance dashboards  

---

## 📡 STAC-XAI Compliance

All CAM JSON-LD artifacts must include:

- `kfm:explainability:method = "cams"`  
- `kfm:model_version`  
- `kfm:input_items`  
- CRS/vertical metadata (if spatial)  
- `checksum:multihash`  
- CARE scope + sovereignty fields  
- Links to raster or tile CAM datasets  
- PROV lineage  

JSON-LD files are validated by CI against KFM-XAI schemas.

---

## 🔐 FAIR+CARE Requirements

All JSON-LD CAM files MUST:

- Use **H3 masking** for potentially sensitive hazard geographies  
- Include sovereignty flags  
- Provide CARE scope & mitigation notes  
- Avoid sensitive tribal/cultural references  
- Avoid speculative hazard causality  
- Follow Data Contract v3 hazard-ethics rules  
- Use narrative-safe terminology  

---

## 🧪 Testing Requirements

CAM JSON-LD must pass CI tests for:

- JSON-LD schema validity  
- STAC-XAI extension compliance  
- CARE & sovereignty placeholders  
- CRS + vertical metadata (if spatial)  
- Deterministic key ordering  
- H3 mask verification  
- PROV-O lineage completeness  
- Narrative-safety lexical lint  
- Hash stability  

Failures → merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                            |
|----------|------------|----------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard CAM JSON-LD explainability specification (aligned with CAM suite) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard CAMs](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

