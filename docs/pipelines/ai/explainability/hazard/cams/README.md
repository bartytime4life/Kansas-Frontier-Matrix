---
title: "⚡🛰️ KFM v11.2.2 — Hazard CAMs Explainability (Class Activation Maps · Deep Hazard Vision Models · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/cams/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Component (Hazard CAMs)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
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
sensitivity: "Explainability-Hazard-CAMs"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-cams"
  - "class-activation-mapping"
  - "deep-hazard-vision-models"
  - "spatial-driver-attribution"
  - "prov-xai"
  - "stac-xai"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "faircare-governance"
  - "h3-masking"

scope:
  domain: "explainability/hazard/cams"
  applies_to:
    - "cams-raster-xai"
    - "cams-tile-xai"
    - "cams-jsonld"
    - "hazard-driver-taxonomy"
    - "prov-xai"
    - "stac-xai"
    - "care-governance"
    - "h3-masking"
    - "spatial-attribution"

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

# ⚡🛰️ **Hazard Class Activation Maps (CAMs) — Explainability Subsystem**  
`docs/pipelines/ai/explainability/hazard/cams/README.md`

**Purpose:**  
Define KFM’s **hazard CAMs explainability layer**, providing **spatial attribution maps** for deep hazard-vision models (tornado, hail, severe convection, wind, wildfire, flood).  
CAM outputs support **Story Node v3**, **Focus Mode v3**, and hazard-governance transparency with **FAIR+CARE** safeguards, **H3-based masking**, **STAC-XAI v11** metadata, and **PROV-O** lineage.

</div>

---

## 📘 Overview

Class Activation Maps (CAMs) identify **which spatial regions** in an input tensor contributed most to a hazard model’s prediction.

Hazard CAMs are used when:

- Hazard models employ CNNs, hybrid CNN-transformer architectures, or spatiotemporal encoders  
- Spatial relevance is essential (tornado supercell structure, hail core shape, VPD/wildfire fuel alignment, floodwater pooling)  
- SHAP/IG alone cannot convey spatial contributions  

CAMs produce high-resolution, H3-generalized evidence suitable for:

- 🌩️ Hazard model debugging  
- 🧭 Focus Mode spatial reasoning windows  
- 📄 Story Node v3 spatial evidence blocks  
- 🗺️ MapLibre/Cesium overlays  

CAMs integrate with:

- STAC-XAI extension  
- PROV-O lineage  
- FAIR+CARE governance and sovereignty constraints  
- XAI JSON-LD semantic bundles  

---

## ⚡ Hazard Domains Supported

- 🌀 **Tornado CAMs** – rotation signatures, shear asymmetry, RFD/FFD structures  
- 🌩️ **Hail CAMs** – updraft cores, reflectivity structures, lapse-rate pockets  
- 💨 **Wind/Gust CAMs** – LLJ influence, downburst signatures, boundary interactions  
- 🌧️ **Flood CAMs** – DEM pooling zones, saturated soils, runoff corridors  
- 🔥 **Wildfire CAMs** – fuel dryness, wind alignment corridors, ignition likelihood zones  
- ⚡ **Multi-hazard CAMs** – joint driver fusion for compound hazard models  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/cams/
    ├── 📄 README.md                       # This file
    │
    ├── 📁 rasters/                        # CAMs as COG/GeoTIFF attribution rasters
    │   ├── 📄 README.md
    │   └── 🗺️ <hazard_cam>.tif
    │
    ├── 📁 tiles/                          # CAMs as GeoParquet tile attribution sets
    │   ├── 📄 README.md
    │   └── 🗂️ drivers.parquet
    │
    ├── 📁 jsonld/                         # Semantic XAI bundles for CAMs
    │   ├── 📄 README.md
    │   ├── 📄 xai-cams-global.jsonld
    │   └── 📄 xai-cams-driver-codes.jsonld
    │
    └── 📁 templates/                      # Template suite for CAM structures
        ├── 📄 cams-raster-template.json
        ├── 📄 cams-tile-template.json
        ├── 📄 xai-cams-global-template.jsonld
        └── 📄 cams-driver-taxonomy.jsonld

---

## 🛰️ CAM Explainability Outputs

### 1. Raster CAMs (COG/GeoTIFF)
- High-resolution pixel-level attribution  
- CRS & vertical metadata  
- Multiband support for multi-hazard channels  
- CARE+sovereignty masking  
- STAC XAI asset fields  
- Spatial H3 generalization when required  

### 2. Tile CAMs (GeoParquet)
- Scalable tile-based attribution  
- Ideal for map overlays  
- Partitioned by hazard, grid, or zoom-level  
- CARE-masked region summaries  
- Compatibility with MapLibre/TMS backends  

### 3. JSON-LD CAM Bundles
Semantic evidence for reasoning engines:

- `xai:drivers` per hazard domain  
- `xai:spatial_context` with generalized H3 indices  
- CARE scope, sovereignty flags  
- PROV-O lineage  
- STAC-XAI metadata  
- Deterministic ordering for CI  

### 4. Narrative Driver Codes (Taxonomy)
Link spatial CAM patterns → hazard narrative drivers (e.g.):

- `TORNADO_SUPERCELL_STRUCTURE_CAM`  
- `HAIL_UPDRAFT_CORE_CAM`  
- `FLASHFLOOD_POOLING_ZONE_CAM`  
- `WILDFIRE_WIND_ALIGNMENT_CAM`  

Used by Story Node v3 & Focus Mode v3.

---

## 📡 STAC-XAI Requirements

All CAM outputs MUST include:

- `kfm:explainability:method = "cams"`  
- `kfm:explainability:{spatial|raster|tiles}`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata if spatial  
- CARE + sovereignty metadata  
- PROV-O lineage references  

---

## 🧾 PROV-O Lineage Requirements

Each hazard CAM artifact MUST contain:

- `prov:wasGeneratedBy` — CAM inference pipeline  
- `prov:used` — STAC hazard/climate inputs  
- `prov:generatedAtTime`  
- `prov:Agent`  
- (Optional) `prov:wasDerivedFrom` linking CAM → IG/SHAP for multimodal reasoning  

---

## 🔐 FAIR+CARE & Sovereignty Requirements

CAM explainability MUST:

- Apply **H3 spatial generalization** for sensitive geographies  
- Mask or abstract culturally sensitive hazard-related terrain  
- Include sovereign rights metadata  
- Avoid speculative hazard interpretation  
- Use governance-safe driver labels  
- Follow Data Contract v3  

---

## 🧪 Testing Requirements

CI MUST validate:

- CAM raster integrity & deterministic tiling  
- JSON-LD schema correctness  
- STAC-XAI field compliance  
- CRS/vertical metadata correctness  
- CARE + sovereignty masking  
- Driver-taxonomy completeness  
- PROV-O lineage  
- Hash stability  

Failures → **PR blocked**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                     |
|---------|------------|---------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard CAMs explainability spec aligned with IG + SHAP frameworks |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard Explainability](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

