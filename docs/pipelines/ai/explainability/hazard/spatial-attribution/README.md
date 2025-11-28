---
title: "⚡🗺️ KFM v11.2.2 — Hazard Spatial Attribution Explainability (Raster & Tile Drivers · GeoParquet/COG · FAIR+CARE)"
path: "docs/pipelines/ai/explainability/hazard/spatial-attribution/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Component (Hazard Spatial Attribution)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
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
sensitivity: "Explainability-Hazard-Spatial"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-spatial-attribution"
  - "raster-xai"
  - "geo-parquet-xai"
  - "spatial-driver-surfaces"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "prov-xai"
  - "stac-xai"
  - "care-governance"
  - "h3-masking"

scope:
  domain: "explainability/hazard/spatial-attribution"
  applies_to:
    - "hazard-raster-attribution"
    - "hazard-tile-attribution"
    - "spatial-driver-jsonld"
    - "stac-xai"
    - "prov-xai"
    - "faircare-governance"
    - "h3-masking"
    - "narrative-spatial-drivers"

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

# ⚡🗺️ **Hazard Spatial Attribution Explainability**  
`docs/pipelines/ai/explainability/hazard/spatial-attribution/README.md`

**Purpose:**  
Define the **spatial attribution explainability layer** for hazard models — representing hazard driver influence as **raster surfaces (COG/GeoTIFF)** and **tile-based GeoParquet layers**, plus JSON-LD semantic bundles that are:

- FAIR+CARE aligned  
- Sovereignty-aware and H3-masked  
- STAC-XAI v11 compliant  
- PROV-O lineage linked  
- Ready for **Story Node v3** and **Focus Mode v3** hazard reasoning.

</div>

---

## 📘 Overview

Hazard spatial attribution captures **where** hazard models (shallow or deep) see the strongest signals on the landscape and atmosphere.

This layer provides:

- Spatial driver surfaces for:
  - Tornado / severe convection environments  
  - Hail / wind / gust environments  
  - Flood / flash-flood risk zones  
  - Wildfire fuels & dryness patterns  
  - Multi-hazard fused risk layers  
- Raster + tile formats for:
  - Map rendering (MapLibre, Cesium)  
  - Analytics pipelines  
  - Narrative spatial summaries  

Spatial attribution is used when:

- The model produces **gridded outputs** (risk maps, probability fields)  
- We need a stable, reproducible encoding of **hazard driver intensity** across space  
- Explainability must plug into STAC, Story Nodes, Focus Mode, and governance review  

All assets are FAIR+CARE filtered and, where necessary, **H3-generalized** to protect sensitive geographies.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/spatial-attribution/
    ├── 📄 README.md                          # This file
    │
    ├── 📁 rasters/                           # Raster-based spatial attribution (COG/GeoTIFF)
    │   ├── 📄 README.md
    │   └── 🗺️ attribution.tif               # Hazard driver raster (example)
    │
    ├── 📁 tiles/                             # Tile-based spatial attribution (GeoParquet)
    │   ├── 📄 README.md
    │   └── 🧩 drivers.parquet                # Tile-wise hazard driver surface
    │
    └── 📁 jsonld/                            # Semantic JSON-LD explainability bundles
        ├── 📄 README.md
        ├── 📄 xai-hazard-spatial-raster.jsonld  # Semantic raster-level spatial XAI (optional)
        ├── 📄 xai-hazard-spatial-tiles.jsonld   # Semantic tile-level spatial XAI
        └── 📄 xai-hazard-spatial-driver-codes.jsonld # Spatial driver taxonomy (narrative-safe)

---

## 🧱 Spatial Attribution Components

### 1. 🗺️ Raster Spatial Attribution (COG/GeoTIFF)

Represents pixel-level hazard attribution surfaces:

- Climate/terrain/hydrology-driven hazard risk  
- Pixel-level gradients derived from SHAP/IG/CAMs or hybrid pipelines  
- CRS + vertical metadata  
- Multihash checksums for integrity  
- H3 masking in metadata & downstream visualization  
- Asset registered as STAC XAI  

Used for:

- Static & interactive hazard risk maps  
- Story Node v3 spatial context  
- Focus Mode spatial overlays  

---

### 2. 🧩 Tile Spatial Attribution (GeoParquet)

Tile-wise hazard-driver surfaces:

- GeoParquet drivers per tile  
- Efficient for web-scale rendering  
- Partitioned by grid, hazard domain, or zoom level  
- H3 masking for sensitive grids  
- STAC XAI asset references  
- Deterministic tile indexing  

Used for:

- Focus Mode v3 dynamic zoom  
- Story Node v3 “regional driver” narratives  
- Scalable analytics workflows  

---

### 3. 📄 JSON-LD Semantic Bundles

Semantic explainability documents that describe:

- Global or per-region spatial hazard drivers  
- Linkages to raster or tiles  
- CARE & sovereignty metadata  
- STAC Item references  
- PROV-O lineage  

Files:

- `xai-hazard-spatial-raster.jsonld` — optional, raster-specific semantics  
- `xai-hazard-spatial-tiles.jsonld` — tile-level semantics  
- `xai-hazard-spatial-driver-codes.jsonld` — taxonomy of spatial hazard drivers  

These are consumed by:

- Story Node v3 (spatial evidence blocks)  
- Focus Mode v3 (spatial reasoning layers)  
- Governance dashboards & lineage systems  

---

## 📡 STAC-XAI Requirements

Spatial attribution assets MUST:

- Set `kfm:explainability:method` appropriately (e.g. `"spatial-attribution"`, `"spatial-attribution-tiles"`)  
- Include `kfm:model_version`  
- Include `kfm:input_items` (STAC Items used in model inference)  
- Provide `checksum:multihash`  
- Fully describe CRS + vertical datum (raster and tiles)  
- Provide CARE + sovereignty metadata fields  
- Reference associated JSON-LD semantic bundles  
- Participate in STAC XAI item/asset schemas  

---

## 🧾 PROV-O Lineage Requirements

Spatial attribution outputs MUST encode:

- `prov:wasGeneratedBy` — hazard spatial-attribution pipeline  
- `prov:used` — hazard & climate STAC datasets  
- `prov:generatedAtTime` — timestamp of attribution creation  
- `prov:Agent` — model & pipeline identity  

Optional:

- `prov:wasDerivedFrom` — link from model & training data to spatial attribution surfaces  

These lineage records feed:

- Hazard explainability audits  
- Story Node provenance graphs  
- Focus Mode reasoning tracebacks  

---

## 🔐 FAIR+CARE & Sovereignty Rules

All hazard spatial attribution must:

- Apply **H3 spatial generalization** to any sensitive regions (e.g., cultural/heritage locations)  
- Mask or coarsen representations near protected communities or sites  
- Include `care:scope` and sovereignty flags in JSON-LD  
- Use governance-vetted driver naming and descriptions  
- Avoid speculative or non-data-grounded hazard interpretations  
- Comply with **Data Contract v3** and hazard ethics guidance  

---

## 🧪 Testing & CI Requirements

CI MUST validate:

- Raster/COG structural integrity  
- GeoParquet tile schema correctness  
- CRS + vertical metadata  
- JSON-LD schema compliance  
- STAC-XAI field presence & validity  
- CARE + sovereignty metadata presence  
- H3 masking for any flagged region  
- Deterministic key ordering and multihash stability  
- PROV-O lineage completeness  

Any failure → **merge blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                              |
|----------|------------|------------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard Spatial Attribution explainability spec aligned with CAM/IG/SHAP   |

---

<div align="center">

### 🔗 Footer  

[⬅ Back to Hazard Explainability](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
