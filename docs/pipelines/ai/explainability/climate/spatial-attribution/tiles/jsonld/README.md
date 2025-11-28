---
title: "🌡️🗺️📄 KFM v11.2.2 — Climate Spatial Attribution Tiles: JSON-LD Explainability Bundles"
path: "docs/pipelines/ai/explainability/climate/spatial-attribution/tiles/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Spatial Tiles JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-explainability-climate-v11.2.2.json"
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
sensitivity: "Explainability-Spatial-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "spatial-tiles-jsonld"
  - "semantic-driver-tiles"
  - "geojsonld-xai"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"
  - "care-governance"

scope:
  domain: "explainability/climate/spatial-attribution/tiles/jsonld"
  applies_to:
    - "xai-spatial-tiles-jsonld"
    - "xai-tile-driver-codes-jsonld"
    - "prov-xai"
    - "stac-xai"
    - "h3-masking"
    - "care-governance"
    - "semantic-driver-model"

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

# 🌡️🗺️📄 **Climate Spatial Attribution — Tile-Based JSON-LD Explainability**  
`docs/pipelines/ai/explainability/climate/spatial-attribution/tiles/jsonld/README.md`

**Purpose:**  
Define the **JSON-LD explainability bundles** for **tile-based climate attribution** — transforming GeoParquet driver tiles into narrative-ready, FAIR+CARE-governed semantic structures for:
- Story Node v3  
- Focus Mode v3  
- STAC v11 explainability assets  
- Governance & transparency dashboards  

</div>

---

## 📘 Overview

Tile-level JSON-LD bundles describe:

- Climate driver semantics per tile  
- Spatially aggregated influence patterns  
- Representations safe for FAIR+CARE scope  
- H3-masked abstractions of sensitive geography  
- PROV-O lineage for auditability  
- STAC-XAI field compatibility  
- Semantic driver mapping for narrative generation  

These JSON-LD documents unify **tile-based climate model outputs** → **semantic interpretation** → **narrative & reasoning layers**.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/spatial-attribution/tiles/jsonld/
    ├── 📄 README.md                               # This file
    │
    ├── 📄 xai-spatial-tiles.jsonld                # Semantic tile-level XAI evidence
    └── 📄 xai-tile-driver-codes.jsonld            # Narrative-safe driver mapping

---

## 🔍 JSON-LD Bundle Specifications

### 1. 🟥 `xai-spatial-tiles.jsonld`  
Semantic explainability for GeoParquet attribution tiles:

- `@context` (KFM-XAI + PROV-O vocabularies)  
- `xai:tile_index` — tile identifier (z/x/y or grid index)  
- `xai:drivers` — tile-level climate driver list  
- `xai:spatial_extent` — generalized extent (H3-masked)  
- `xai:driver_intensity` — summary of attribution magnitudes  
- `xai:care_scope` — CARE classification & masking rules  
- `prov:*` — provenance chain  
- STAC references:
  - `kfm:input_items`  
  - `kfm:model_version`  
  - tile checksums (`checksum:multihash`)  

Used by:

- Focus Mode v3 tile overlays  
- Story Node v3 spatial evidence modules  
- Climate XAI dashboards  

---

### 2. 🟩 `xai-tile-driver-codes.jsonld`  
Maps tile-level model outputs → narrative-safe semantic drivers.

Contains:

- `xai:driver_code` — canonical climate driver categories  
- `xai:description` — CARE-filtered definitions  
- `xai:linked_features` — underlying model features  
- `xai:story_node_roles` — narrative usage categories  
- `xai:focus_mode_tags` — mapping for interactive reasoning  
- `prov:wasDerivedFrom` — relational link to `xai-spatial-tiles.jsonld`  

Used by:

- Climate Story Node v3  
- Focus Mode reasoning layers  
- Governance semantic reviews  

---

## 📡 STAC Integration Requirements

Tile JSON-LD outputs MUST provide:

- `kfm:explainability:method = "spatial-attribution-tiles"`  
- `kfm:explainability:spatial` metadata  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata (if spatial)  
- CARE flags & sovereignty metadata  
- PROV linkage  
- References to GeoParquet driver tiles  

---

## 🧾 PROV-O Lineage Requirements

Each JSON-LD tile bundle must include:

- `prov:wasGeneratedBy` (tile-XAI pipeline run)  
- `prov:used` (STAC climate layers, DEMs, forcing-data)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity + executor)  
- Optional: `prov:wasDerivedFrom` (model → tile → narrative lineage chain)  

These relationships allow validation in:

- Governance dashboards  
- Lineage editors  
- Story Node provenance graphs  

---

## 🔐 FAIR+CARE Requirements

Tile-level XAI JSON-LD MUST:

- Apply **H3 generalization** to all spatial elements involving sensitivity  
- Obey sovereignty & community-level constraints  
- Mask/remove drivers tied to sensitive landforms  
- Include `care:scope` & CARE rationale  
- Avoid speculative climate interpretations  

---

## 🧪 Testing Requirements

CI tests MUST validate:

- JSON-LD schema compliance  
- STAC XAI extension compliance  
- Deterministic regeneration  
- CARE & sovereignty masks  
- PROV-O lineage traceability  
- Tile-driver consistency with GeoParquet source data  

Any failure → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                      |
|----------|------------|----------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Tile-based JSON-LD explainability specification            |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Tile XAI](../README.md) · [🌡️ Climate XAI Root](../../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

<

