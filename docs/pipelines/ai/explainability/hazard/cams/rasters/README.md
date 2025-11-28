---
title: "⚡🛰️🗺️ KFM v11.2.2 — Hazard CAMs Raster Explainability (COG/GeoTIFF · Spatial Attribution · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/cams/rasters/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Hazard CAM Rasters)"

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
sensitivity: "Explainability-Hazard-CAM-Raster"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-cams-rasters"
  - "spatial-attribution"
  - "cog-explainability"
  - "pixel-influence-maps"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "prov-xai"
  - "stac-xai"
  - "care-governance"

scope:
  domain: "explainability/hazard/cams/rasters"
  applies_to:
    - "hazard-cam-geotiff"
    - "hazard-cam-cog"
    - "xai-cams-raster-jsonld"
    - "care-governance"
    - "h3-generalization"
    - "prov-xai"
    - "stac-xai"

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

# ⚡🛰️🗺️ **Hazard CAMs — Raster Explainability (COG / GeoTIFF)**  
`docs/pipelines/ai/explainability/hazard/cams/rasters/README.md`

**Purpose:**  
Define the **COG/GeoTIFF raster layer** for Hazard CAM (Class Activation Map) explainability, providing pixel-level hazard-driver evidence for tornado, hail, severe wind, convection, wildfire, flood, and multi-hazard deep-learning models.  
Raster CAMs support:

- 🧭 **Focus Mode v3 spatial overlays**  
- 📘 **Story Node v3 hazard evidence extracts**  
- 🗺️ **MapLibre/Cesium interactive visualization**  
- 🏛 **FAIR+CARE governance and sovereignty reviews**  
- 🔗 **STAC v11 + PROV-O explainability lineage**  

</div>

---

## 📘 Overview

Hazard CAM rasters represent **pixel-accurate spatial attributions** from deep CNN/Transformer hazard models.

These maps encode **where** the model “looked” to form a prediction.

Examples:

- Tornado models → rotation signatures, updraft/mesocyclone regions  
- Hail models → updraft core, reflectivity clusters  
- Wind/gust models → boundary-layer shear zones  
- Flood models → pooling / runoff / DEM-derived risk zones  
- Wildfire models → fuel dryness + wind-alignment corridors  

Raster CAMs are FAIR+CARE screened and spatially H3-generalized where necessary.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/cams/rasters/
    ├── 📄 README.md                      # This file
    │
    ├── 🗺️ <hazard_cam>.tif               # Core CAM raster (COG/GeoTIFF)
    ├── 📄 metadata.json                  # Raster metadata (CRS, bounds, checksums, CARE)
    │
    └── 📁 jsonld/                        # JSON-LD semantic bundles
        ├── 📄 xai-cams-raster.jsonld     # Semantic CAM raster evidence
        └── 📄 cams-raster-driver-codes.jsonld # CAM driver taxonomy (narrative-safe)

---

## 🧱 Raster Explainability Components

### 1. 🗺️ CAM Raster (`*.tif`)
The primary explainability asset.

**Required characteristics:**

- Cloud-Optimized GeoTIFF (COG)  
- Float32 or UInt16 attribution magnitudes  
- Pixel values normalized (0 → 1)  
- Single-band or multi-band (hazard-dependent)  
- CRS defined (`proj:epsg`)  
- Vertical axis defined if relevant  
- Deterministic tiling & window metadata  
- CARE/H3 masking applied  
- Multihash checksum stored in STAC metadata  

Used by: visualization layers, dashboards, Story Node v3.

---

### 2. 📄 `metadata.json`
Machine-readable metadata:

- CRS + vertical datum  
- Bounds + resolution  
- Pixel data-type  
- Attribution method = `"cams"`  
- Hazard domain label  
- CARE scope & sovereignty notes  
- `checksum:multihash`  
- Raster lineage references  

---

### 3. 🟩 JSON-LD Semantic Explainability (`/jsonld`)
These are **required** to make raster CAM explainability usable by Story Node v3 and Focus Mode v3.

#### **`xai-cams-raster.jsonld`**  
Semantic representation of raster evidence:

- `@context` (KFM-XAI + PROV-O)  
- `xai:hazard_domain`  
- `xai:drivers` (semantic CAM drivers)  
- `xai:spatial_context` with generalized H3 geometry  
- CARE scope  
- STAC fields (`kfm:model_version`, `kfm:input_items`, `checksum:multihash`)  
- PROV lineage  

#### **`cams-raster-driver-codes.jsonld`**  
Narrative-safe driver taxonomy:

- CAM → semantic hazard-driver mapping  
- CARE & sovereignty compliance  
- Story Node v3 roles  
- Focus Mode v3 tagging  
- PROV linkage to raster assets  

---

## 📡 STAC-XAI Integration Requirements

Raster CAMs MUST include:

- `kfm:explainability:method = "cams"`  
- `kfm:explainability:raster`  
- `kfm:model_version`  
- `kfm:input_items` (hazard/climate STAC Items)  
- `checksum:multihash`  
- Raster-specific metadata: spatial extent, CRS, pixel stats  
- CARE + sovereignty metadata  
- Links to JSON-LD bundles  

---

## 🧾 PROV-O Lineage Requirements

Raster CAMs must declare:

- `prov:wasGeneratedBy` (hazard CAM pipeline)  
- `prov:used` (model + input STAC Items)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity + inference engine)  
- Optional: CAM → IG/SHAP links for multimodal XAI  

---

## 🔐 FAIR+CARE & Sovereignty Requirements

Hazard CAMs must:

- Apply H3 masking for sensitive regions  
- Include sovereignty flags & CARE scope reason  
- Avoid explicit display of sensitive landforms  
- Respect Data Contract v3 governing hazard data  
- Avoid speculative causal interpretation  

This is mandatory for deep hazard XAI maps.

---

## 🧪 Testing Requirements

CI validation MUST verify:

- COG structural compliance  
- CRS/vertical-datum correctness  
- Deterministic pixel-level attribution (given seed)  
- JSON-LD schema correctness  
- STAC-XAI extension compliance  
- CARE + sovereignty masks present  
- PROV-O lineage complete  
- Multihash checksum valid  
- Raster-driver taxonomy completeness  

Failures block merges.

---

## 🕰 Version History

| Version | Date       | Notes                                                                        |
|--------|------------|-------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard CAM Raster explainability specification (aligned with XAI v11) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard CAMs](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

