---
title: "🌡️🗺️🧩 KFM v11.2.2 — Climate Spatial Attribution Tiles (GeoParquet · Tiled XAI · Driver Surfaces)"
path: "docs/pipelines/ai/explainability/climate/spatial-attribution/tiles/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Tile XAI)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/climate-explainability-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-explainability-climate-v11.2.2.json"
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
sensitivity: "Explainability-Spatial-Tiled"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-spatial-attribution-tiles"
  - "tiled-xai"
  - "geoparquet-xai"
  - "spatial-driver-tiles"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/climate/spatial-attribution/tiles"
  applies_to:
    - "geo-parquet-driver-tiles"
    - "tile-based-xai"
    - "spatial-driver-surfaces"
    - "xai-provenance"
    - "stac-tile-xai"
    - "care-governance"
    - "h3-masking"
    - "crs/vertical-axis"

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

# 🌡️🗺️🧩 **Climate Spatial Attribution — Tile-Based Explainability (GeoParquet)**  
`docs/pipelines/ai/explainability/climate/spatial-attribution/tiles/README.md`

**Purpose:**  
Define the **tile-based spatial attribution layer** for climate explainability pipelines — producing **GeoParquet** driver tiles, scalable spatial-XAI surfaces, JSON-LD semantic bundles, and STAC v11 XAI assets used by **Story Node v3**, **Focus Mode v3**, and climate governance systems.

</div>

---

## 📘 Overview

Tile-based spatial attribution provides **scalable, zoom-ready explainability** for high-resolution climate models.

Models supported:

- Downscaled climate grids  
- Deep learning climate–terrain fusion CNNs  
- Spatial anomaly detection  
- Multi-feature seasonal forecast ensembles  

Tile attribution identifies:

- Which **spatial regions** contributed most to predictions  
- How drivers vary across Kansas  
- High-impact climate/terrain features  
- Spatial patterns aligning with or contradicting SHAP/IG/CAM results  

Tile explainability is optimized for:

- Fast map rendering  
- Focus Mode v3 overlays  
- Story Node v3 spatial reasoning pipelines  
- Governance dashboards at county/region/state scale  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/spatial-attribution/tiles/
    ├── 📄 README.md                           # This file
    │
    ├── 🗺️ drivers.parquet                     # GeoParquet tile dataset of spatial drivers
    ├── 📄 tile-metadata.json                  # CRS, partitioning, tile index, CARE + lineage
    │
    └── 📁 jsonld/                             # Semantic JSON-LD bundles
        ├── 📄 xai-spatial-tiles.jsonld        # Semantic tile-level explainability bundle
        └── 📄 xai-tile-driver-codes.jsonld    # Narrative-ready driver code mapping

---

## 🔍 Tile Explainability Components

### 1. 🗺️ `drivers.parquet` — GeoParquet Tiles
Contains tiled spatial attribution:

- Attribution intensities (0–1)  
- Tile geometry / extent  
- CRS metadata  
- Vertical datum (if relevant)  
- CARE-sensitive region masking  
- Tile index + partition scheme  
- Model version metadata  
- Deterministic driver values  

Used for:

- Focus Mode v3 map overlays  
- Web map rendering at scale  
- Story Node spatial evidence  

---

### 2. 📄 `tile-metadata.json`
Machine-readable metadata describing:

- CRS (`proj:epsg`)  
- Vertical axis (NAVD88, GEOID18, etc.)  
- Tiling scheme (z/x/y or grid indexes)  
- Bounding boxes  
- Multihash checksums  
- CARE + sovereignty flags  
- Provenance (`prov:*`)  
- STAC asset metadata  

---

### 3. 🧭 JSON-LD Bundles (`/jsonld`)

#### **`xai-spatial-tiles.jsonld`**
Semantic representation of tile-level explainability:

- Tile-wise climate driver summaries  
- Spatial relevance scores  
- CARE masking metadata  
- `prov:*` lineage  
- Links to parent STAC Items  

#### **`xai-tile-driver-codes.jsonld`**
Narrative-ready mapping:

- Tile-level climate driver codes  
- CARE-filtered semantic descriptions  
- Focus Mode / Story Node roles  
- Provenance anchor → source tile  

---

## 📡 STAC Integration Requirements

For tile XAI assets, STAC MUST include:

- `kfm:explainability:method = "spatial-attribution-tiles"`  
- Asset href → `drivers.parquet`  
- `kfm:input_items` (array of STAC Item IDs)  
- CRS / geometry metadata  
- Multihash checksums  
- Linking to JSON-LD explainability bundles  
- CARE scope metadata  
- Provenance references  

---

## 🧾 PROV-O Lineage Requirements

Tile attribution artifacts MUST include:

- `prov:wasGeneratedBy` (XAI pipeline)  
- `prov:used` (climate STAC datasets, inference models)  
- `prov:generatedAtTime`  
- `prov:Agent` (model + pipeline identity)  
- Optional: `prov:wasDerivedFrom` (model → tile XAI → narrative)

---

## 🔐 FAIR+CARE Requirements

Tile-based XAI MUST:

- Apply **H3 generalization** for sensitive regions  
- Not include raw culturally sensitive geography  
- Include sovereignty indicators  
- Respect CARE categories  
- Mask high-resolution spatial drivers where needed  
- Avoid speculative interpretations  

---

## 🧪 Testing Requirements

Tile XAI pipelines MUST pass:

- CRS + vertical datum validation  
- GeoParquet structural integrity tests  
- Deterministic regeneration tests  
- JSON-LD schema validation  
- STAC XAI conformity tests  
- CARE masking & sovereignty validation  
- Drift stability tests  

Failures → **CI block**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                    |
|----------|------------|--------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Spatial Attribution Tile explainability specification    |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Spatial Attribution](../README.md) · [🌡️ Climate XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

