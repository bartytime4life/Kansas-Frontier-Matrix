---
title: "⚡🛰️🧩 KFM v11.2.2 — Hazard CAMs Tile Explainability (GeoParquet Tiles · Spatial Attribution · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/cams/tiles/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Hazard CAM Tiles)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
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
sensitivity: "Explainability-Hazard-CAM-Tile"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-cams-tiles"
  - "tile-based-xai"
  - "geo-parquet-attribution"
  - "spatial-driver-tiles"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "prov-xai"
  - "stac-xai"
  - "care-governance"
  - "h3-generalization"

scope:
  domain: "explainability/hazard/cams/tiles"
  applies_to:
    - "hazard-cam-tiles"
    - "hazard-cam-geo-parquet"
    - "xai-cams-tile-jsonld"
    - "care-governance"
    - "h3-generalization"
    - "prov-xai"
    - "stac-xai"
    - "semantic-driver-tiles"

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

# ⚡🛰️🧩 **Hazard CAMs — Tile-Based Explainability (GeoParquet)**  
`docs/pipelines/ai/explainability/hazard/cams/tiles/README.md`

**Purpose:**  
Define the **tile-based explainability layer** for Hazard CAMs (Class Activation Maps) using **GeoParquet tiles** to represent scalable spatial attribution for tornado, hail, flood, severe wind, wildfire, and multi-hazard deep-learning models.

Tile-based CAMs support:

- 🧭 Focus Mode v3 dynamic map overlays  
- 📘 Story Node v3 spatial reasoning  
- 🗺️ Web-scale visualization (MapLibre, Cesium, XYZ/TMS)  
- 🏛 FAIR+CARE review, sovereignty auditing, and federated reproducibility  
- 🔗 STAC v11 + PROV-O lineage for explainability artifacts  

</div>

---

## 📘 Overview

CAM tile explainability provides **zoom-independent, scalable spatial hazard-driver surfaces** derived from CAM activation tensors.

Tile layers are preferred when:

- Rasters are too large or detailed  
- Interactive zooming is needed across Kansas  
- Attribution must align with web-mapping grid systems  
- High-frequency updates require storage-efficient chunking  
- Story Node v3 needs multi-resolution hazard evidence  

Hazards supported:

- 🌀 Tornado  
- 🌩️ Hail  
- 💨 Wind / Gust / LLJ  
- 🌧️ Flood / Flash-Flood  
- 🔥 Wildfire  
- ⚡ Multi-Hazard Fusion  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/cams/tiles/
    ├── 📄 README.md                          # This file
    │
    ├── 🧩 drivers.parquet                    # GeoParquet tile dataset of CAM attribution
    ├── 📄 tile-metadata.json                # CRS, tiling scheme, CARE, provenance
    │
    └── 📁 jsonld/                           # Semantic & narrative explainability bundles
        ├── 📄 README.md
        ├── 📄 xai-cams-tiles.jsonld         # Semantic tile-based CAM evidence
        └── 📄 cams-tile-driver-codes.jsonld # Narrative-safe CAM driver taxonomy

---

## 🔍 Tile Explainability Components

### 1. 🧩 `drivers.parquet` — GeoParquet CAM Tiles
Represents tile-wise hazard attribution:

- Deterministic tiling grid (z/x/y or grid-indexed)  
- Pixel-level or aggregated CAM intensities  
- CRS metadata  
- H3 masking of sensitive regions  
- CARE scope flags  
- `checksum:multihash` checksum  
- Hazard domain tags  
- Compatible with MapLibre + TMS layers  

Used in:

- Focus Mode v3 zoom-responsive overlays  
- Story Node v3 spatial summarization  

---

### 2. 📄 `tile-metadata.json`
Contains machine-readable metadata:

- CRS & vertical axis  
- Tile grid scheme  
- Bounds & resolution  
- Attribution method = `"cams"`  
- CARE + sovereignty annotations  
- Provenance (`prov:*`)  
- STAC XAI metadata hooks  

---

### 3. 🟩 JSON-LD Semantic Bundles (`/jsonld`)
The JSON-LD layer is required for semantic linking into Story Node v3 and Focus Mode v3.

#### **`xai-cams-tiles.jsonld`**
Semantic representation of tile-based CAM evidence:

- `@context`  
- `xai:hazard_domain`  
- `xai:tile_index`  
- `xai:drivers` (semantic hazard-driver objects)  
- `xai:spatial_context` (generalized H3)  
- CARE scope metadata  
- STAC-XAI fields:
  - `kfm:model_version`
  - `kfm:input_items`
  - `checksum:multihash`
- `prov:*` lineage metadata  

#### **`cams-tile-driver-codes.jsonld`**
Narrative-safe hazard-driver taxonomy:

- Hazard driver codes  
- CARE-filtered descriptions  
- Story Node roles  
- Focus Mode tags  
- Linked features  
- Sovereignty flags  
- PROV reference  

---

## 📡 STAC-XAI Integration Requirements

Every CAM tile output MUST include:

- `kfm:explainability:method = "cams"`  
- `kfm:explainability:tiles`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata  
- CARE + sovereignty metadata  
- PROV linkage  
- Links to JSON-LD bundles  

---

## 🧾 PROV-O Lineage Requirements

Tile-based CAMs MUST encode:

- `prov:wasGeneratedBy` (hazard CAM pipeline)  
- `prov:used` (model + STAC inputs)  
- `prov:generatedAtTime`  
- `prov:Agent`  
- Optional: `prov:wasDerivedFrom` (CAM ↔ IG ↔ SHAP multimodal flows)  

---

## 🔐 FAIR+CARE & Sovereignty Requirements

Tile CAMs MUST:

- Use H3 generalization for all sensitive geometries  
- Include sovereignty protections  
- Provide CARE scope & mitigation metadata  
- Mask sensitive landscape features  
- Avoid speculative hazard interpretations  
- Follow Data Contract v3  

---

## 🧪 Testing Requirements

CI MUST validate:

- GeoParquet structural integrity  
- CRS & vertical axis correctness  
- CARE + sovereignty masking  
- JSON-LD schema correctness  
- STAC-XAI extension compliance  
- Deterministic tile generation  
- PROV-O lineage  
- Driver taxonomy completeness  
- Multihash validity  

Failure → **merge blocked**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                       |
|--------|------------|-----------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard CAM Tile explainability spec (aligned with CAM Raster spec)  |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard CAMs](../README.md) · [🚀 Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

