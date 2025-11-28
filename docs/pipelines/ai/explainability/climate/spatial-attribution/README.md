---
title: "🌡️🗺️ KFM v11.2.2 — Climate Spatial Attribution Explainability (Raster Drivers · Tiles · GeoParquet · COG)"
path: "docs/pipelines/ai/explainability/climate/spatial-attribution/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Component"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
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
sensitivity: "Explainability-Spatial"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-spatial-attribution"
  - "raster-xai"
  - "tile-xai"
  - "geoparquet-xai"
  - "cog-xai"
  - "spatial-drivers"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/spatial-attribution"
  applies_to:
    - "raster-attribution"
    - "tiled-attribution"
    - "spatial-jsonld"
    - "xai-stac"
    - "prov-xai"
    - "care-governance"
    - "masking-h3"

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

# 🌡️🗺️ **Climate Spatial Attribution Explainability**  
`docs/pipelines/ai/explainability/climate/spatial-attribution/README.md`

**Purpose:**  
Define the **spatial attribution explainability subsystem** for climate models — producing FAIR+CARE-aligned raster, tile, and GeoParquet/COG-based attribution maps and JSON-LD explainability bundles used in STAC v11, Story Node v3, and Focus Mode v3.

</div>

---

## 📘 Overview

Climate spatial attribution pipelines generate spatially-explicit explainability for:

- Downscaled climate layers  
- Climate anomaly detection  
- Bias-corrected spatial predictions  
- Climate–terrain fusion models  
- Climate–hydrology–terrain composite drivers  

Outputs produced here must be:

- Deterministic across runs  
- CRS-correct + vertical-datum aligned  
- H3-masked when interacting with CARE-restricted geographies  
- STAC v11-compliant  
- Machine-extractable (GeoParquet / JSON-LD)  
- Provenance-rich (PROV-O + OpenLineage)  
- Version-pinned  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/spatial-attribution/
    ├── 📄 README.md                            # This file
    │
    ├── 📁 rasters/                             # TIFF/COG raster attribution
    │   ├── 📄 attribution.tif                  # Example raster attribution
    │   └── 📄 metadata.json                    # Raster CRS + provenance
    │
    ├── 📁 tiles/                               # Tile-based (GeoParquet) attribution
    │   ├── 📄 drivers.parquet                  # Tile-wise attribution layer
    │   └── 📄 tile-metadata.json               # Tiling scheme + CRS + checksum
    │
    └── 📁 jsonld/                              # JSON-LD explainability bundles
        ├── 📄 xai-global.jsonld
        ├── 📄 xai-local.jsonld
        └── 📄 xai-spatial-drivers.jsonld

---

## 🔍 Spatial Attribution Components

### 1. 🟥 Raster-Based Attribution
Raster drivers include:

- Climate variable influence grids  
- Terrain-modulated attribution  
- Gradient-/SHAP-/CAM-derived fields  

Files must:

- Use GeoTIFF or Cloud-Optimized GeoTIFF (COG)  
- Contain CRS, bounds, resolution, vertical datum  
- Carry multihash checksums  
- Mask sensitive regions  

---

### 2. 🟦 Tile-Based (GeoParquet) Attribution
Tile-level attribution for scalable map rendering:

- Used for large statewide downscaled drivers  
- Efficient for web visualizations  
- Ideal for Focus Mode’s spatial-evidence overlays  

Each tile MUST include:

- CRS  
- Bounding geometry  
- Attribution vector  
- Provenance links  
- CARE masking flags  

---

### 3. 🟨 JSON-LD Attribution Bundles
Provide machine-readable climate driver summaries:

- Global spatial drivers  
- Local/tile-level drivers  
- Harmonized narrative-ready fields  
- Encoding for:
  - Story Node v3  
  - Focus Mode v3  
  - Governance dashboards  

---

## 📡 STAC Integration Requirements

Spatial attribution assets MUST embed:

- `kfm:explainability:method = "spatial-attribution"`  
- `kfm:explainability:spatial` (URI + checksum)  
- CRS + bounding geometry  
- Vertical datum (if applicable)  
- Model version metadata  
- Provenance references  
- Multihash checksums  
- Tiling scheme (if tiled)  

---

## 🧾 PROV-O Lineage Requirements

Each spatial attribution artifact MUST include:

- `prov:wasGeneratedBy` (model + pipeline)  
- `prov:used` (input STAC datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (pipeline + model version identity)  

Used by:

- Focus Mode v3 spatial reasoning  
- Story Node v3 spatial evidence blocks  
- Climate lineage dashboards  

---

## 🔐 FAIR+CARE Requirements

Spatial XAI MUST:

- Apply H3 masking for CARE-sensitive geographies  
- Avoid exposing culturally restricted patterns (e.g., landform correlations near heritage sites)  
- Include CARE scope metadata  
- Respect sovereignty policies & dataset licenses  
- Remove/abstract culturally sensitive spatial correlations  

---

## 🧪 Testing Requirements

Pipelines MUST pass:

- Raster/COG integrity tests  
- CRS & vertical datum checks  
- JSON-LD validation  
- STAC compliance tests  
- CARE masking rules  
- Deterministic regeneration tests  
- Drift baselines for raster/tile attribution  

Failing tests → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                      |
|----------|------------|----------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Spatial Attribution explainability layer                   |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate Explainability](../README.md) · [🧠 AI Pipeline Layer](../../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

