---
title: "🌡️🗺️📄 KFM v11.2.2 — Climate Spatial Attribution JSON-LD Explainability (Raster + Tile Evidence · Semantic Drivers)"
path: "docs/pipelines/ai/explainability/climate/spatial-attribution/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Component (Spatial JSON-LD Root)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/climate-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-climate-v11.2.2.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

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
sensitivity: "Explainability-Spatial-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "spatial-xai-jsonld"
  - "climate-driver-maps"
  - "semantic-driver-surfaces"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"
  - "care-governance"

scope:
  domain: "explainability/climate/spatial-attribution/jsonld"
  applies_to:
    - "spatial-raster-jsonld"
    - "spatial-tile-jsonld"
    - "driver-codes"
    - "semantic-driver-model"
    - "prov-lineage"
    - "stac-xai"
    - "care-governance"
    - "h3-masking"

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

# 🌡️🗺️📄 **Climate Spatial Attribution — Root JSON-LD Explainability Layer**  
`docs/pipelines/ai/explainability/climate/spatial-attribution/jsonld/README.md`

**Purpose:**  
Define the **semantic JSON-LD layer** for **spatial attribution explainability**, unifying raster- and tile-based XAI into FAIR+CARE-aligned, STAC-compatible, PROV-linked structures powering:

- 🌡️ Climate Story Node v3  
- 🧭 Focus Mode v3 spatial reasoning  
- 🗺️ High-resolution map overlays  
- 🏛 Governance & lineage audits  

</div>

---

## 📘 Overview

This directory governs **semantic explainability bundles** describing:

- Spatial attribution rasters (GeoTIFF/COG)  
- Tile-based attribution layers (GeoParquet)  
- Spatial driver semantics (aggregated or tile-specific)  
- CARE-filtered spatial abstractions  
- H3-generalized geographic references  
- Complete PROV-O lineage  
- STAC v11 XAI metadata fields  
- Narrative-ready driver groupings  

These JSON-LD artifacts serve as the **semantic bridge** from raw XAI → knowledge graph → narrative layers.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/spatial-attribution/jsonld/
    ├── 📄 README.md                               # This file
    │
    ├── 📄 xai-spatial-raster.jsonld               # Semantic bundle for raster attribution
    ├── 📄 xai-spatial-tiles.jsonld                # Semantic bundle for tile attribution
    └── 📄 xai-spatial-driver-codes.jsonld         # Unified driver taxonomy for spatial XAI

---

## 🔍 JSON-LD Bundle Specifications

### 1. 🟥 Raster JSON-LD (`xai-spatial-raster.jsonld`)
Represents:

- Pixel-based attribution summaries  
- Spatial driver intensities  
- H3-masked spatial context  
- Model version metadata  
- CRS & geometry  
- `prov:*` lineage  
- STAC fields (`kfm:explainability:*`, `checksum:multihash`)  

Used for:

- Raster → narrative integration  
- Focus Mode v3 map overlays  
- Global spatial evidence chains  

---

### 2. 🟦 Tile JSON-LD (`xai-spatial-tiles.jsonld`)
Represents:

- Tile-wise driver summaries  
- Tile index, CRS, bounds  
- Semantic driver interpretation  
- CARE masking flags  
- STAC reference fields  
- Provenance linking to tiles + model  

Used for:

- Tile-based spatial reasoning  
- Progressive map zoom layers  
- Distributed XAI analysis at scale  

---

### 3. 🟩 Spatial Driver Codes (`xai-spatial-driver-codes.jsonld`)
Unified taxonomy mapping spatial patterns → semantic climate drivers:

- `xai:driver_code` taxonomy  
- Narrative-safe descriptions  
- Driver roles for Story Node v3  
- Focus Mode v3 relevance categories  
- CARE annotations  
- Provenance links  

This ensures **consistent semantic interpretation** of spatial XAI across:

- Raster explainability  
- Tile explainability  
- Story Nodes  
- Focus Mode  

---

## 📡 STAC Integration Requirements

All JSON-LD files MUST expose:

- `kfm:explainability:method`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- `proj:*` (if spatial)  
- CARE masking metadata  
- PROV-O lineage references  
- Links to raster or GeoParquet tile assets  

---

## 🧾 PROV-O Lineage Requirements

Each JSON-LD explanation MUST include:

- `prov:wasGeneratedBy` (model + XAI pipeline)  
- `prov:used` (STAC climate layers)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity)  
- Optional: `prov:wasDerivedFrom` (model → spatial-XAI → narrative chain)  

These enable:

- Governance audits  
- Story Node provenance  
- Focus Mode debugging  
- Cross-pipeline lineage queries  

---

## 🔐 FAIR+CARE Requirements

Spatial JSON-LD MUST:

- Use **H3 generalization** for sensitive areas  
- Remove culturally sensitive spatial correlations  
- Include sovereignty metadata  
- Follow CARE principles for spatial abstraction  
- Avoid speculative or culturally sensitive inferences  

---

## 🧪 Testing Requirements

CI must validate:

- JSON-LD schema correctness  
- STAC-XAI compliance  
- CARE masking correctness  
- H3-generalization enforcement  
- CRS/vertical-datum fields (if applicable)  
- Deterministic regeneration tests  
- Cross-layer consistency (raster vs tile)  
- PROV-O lineage completeness  

Failures → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Spatial Attribution JSON-LD explainability specification |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Spatial Attribution](../README.md) · [🌡️ Climate XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

