---
title: "🌡️🗺️📡 KFM v11.2.2 — Climate Spatial Attribution Rasters (COG · GeoTIFF · Pixel Influence Maps)"
path: "docs/pipelines/ai/explainability/climate/spatial-attribution/rasters/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Raster XAI)"

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
sensitivity: "Explainability-Spatial-Raster"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-spatial-attribution-rasters"
  - "raster-xai"
  - "pixel-influence-maps"
  - "cog-explainability"
  - "semantic-driver-surfaces"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/climate/spatial-attribution/rasters"
  applies_to:
    - "xai-raster-cog"
    - "xai-raster-geotiff"
    - "pixel-influence"
    - "spatial-driver-surfaces"
    - "xai-provenance"
    - "stac-xai"
    - "care-governance"
    - "h3-masking"
    - "vertical-axis-metadata"

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

# 🌡️🗺️📡 **Climate Spatial Attribution — Raster Explainability**  
`docs/pipelines/ai/explainability/climate/spatial-attribution/rasters/README.md`

**Purpose:**  
Define the **raster-based climate attribution outputs** (COG/GeoTIFF) representing pixel-level influence surfaces derived from SHAP, Integrated Gradients, CAMs, or hybrid spatial XAI pipelines in KFM v11.2.2.

These rasters feed:

- Focus Mode v3 map overlays  
- Story Node v3 spatial evidence blocks  
- STAC v11 XAI assets  
- Governance dashboards (provenance + CARE compliance)

</div>

---

## 📘 Overview

Raster spatial attribution provides **high-resolution pixel-level evidence** of what influenced a climate model’s predictions.

Used for models involving:

- Climate downscaling  
- Climate anomaly detection  
- Seasonal forecasting  
- Terrain × climate fusion  
- Spatial deep-learning (CNN-based) architectures  

Raster outputs must be:

- Deterministic and reproducible  
- Cloud-Optimized (COG) preferred  
- CRS + vertical axis aligned  
- CARE-masked (H3 where applicable)  
- Fully STAC v11 compliant  
- PROV-linked  
- JSON-LD compatible (referenced in `/jsonld` bundles)

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/spatial-attribution/rasters/
    ├── 📄 README.md                     # This file
    │
    ├── 🗺️ attribution.tif               # Primary attribution raster (GeoTIFF/COG)
    ├── 📄 metadata.json                 # Raster metadata (CRS, bounds, checksum, CARE)
    │
    └── 📁 jsonld/                       # Semantic JSON-LD explainability wrappers
        ├── 📄 xai-spatial-raster.jsonld # Links raster -> drivers -> provenance
        └── 📄 xai-raster-driver-codes.jsonld

---

## 🔍 Raster Explainability Components

### 1. 🗺️ `attribution.tif` (COG/GeoTIFF)
Contains pixel-level attribution intensities:

- Float grid (0→1) representing variable importance  
- Multi-band or single-band depending on model  
- CRS metadata (EPSG code)  
- Bounding box + resolution  
- Vertical datum (if relevant)  
- H3-masked for CARE-sensitive locations  
- Multihash checksums for integrity  

---

### 2. 📄 `metadata.json`
Machine-readable companion metadata:

- CRS (`proj:epsg`)  
- Vertical axis information (`vertical:` fields, NAVD88/GEOID)  
- Attribution method (`integrated-gradients`, `shap`, `cams`, `hybrid`)  
- CARE + sovereignty flags  
- Provenance (`prov:*`)  
- Tiling scheme / resolution  
- STAC asset metadata references  

---

### 3. 🧭 JSON-LD explainability bundles (in `/jsonld/`)
**`xai-spatial-raster.jsonld`**  
Provides semantic mapping:

- Pixel driver interpretation  
- Attribution method  
- Global/local driver relationships  
- Links to STAC items and provenance  
- CARE masking metadata  

**`xai-raster-driver-codes.jsonld`**  
Maps raster pixel patterns → narrative-safe driver codes:

- Climate driver categories  
- Spatial context summaries  
- CARE-filtered patterns  
- Story Node v3 & Focus Mode v3 alignment  

---

## 📡 STAC Integration Requirements

Raster assets MUST include:

- `kfm:explainability:method`  
- `kfm:explainability:spatial`  
- `proj:*` fields for CRS  
- `kfm:model_version`  
- `kfm:input_items` (STAC IDs)  
- `checksum:multihash`  
- CARE scope indicators  
- Links to JSON-LD sidecar files  

---

## 🧾 PROV-O Lineage Requirements

Each raster must be associated with:

- `prov:wasGeneratedBy` (XAI pipeline)  
- `prov:used` (STAC climate model inputs)  
- `prov:generatedAtTime`  
- `prov:Agent` (model + execution pipeline identity)  

These lineage elements power:

- Investigation workflows  
- Story Node provenance  
- Focus Mode reasoning backtracking  

---

## 🔐 FAIR+CARE Requirements

Raster attribution MUST:

- Apply H3 generalization for sensitive areas  
- Avoid depicting culturally sensitive terrain correlations  
- Include CARE scope + sovereignty metadata  
- Respect Data Contract v3 + Vertical Axis v11  
- Obey masking rules defined in KFM heritage standards  

Raster visual patterns must **never** encode raw locations tied to restricted data.

---

## 🧪 Testing Requirements

The raster explainability pipeline must pass:

- CRS & vertical-axis validation  
- Raster integrity (COG structure, windowing)  
- Deterministic reconstruction tests  
- JSON-LD linkage checks  
- STAC XAI extension compliance  
- CARE & sovereignty rule enforcement  
- Drift stability checks across model upgrades  

CI failures → merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Raster Spatial Attribution explainability spec for climate    |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Spatial Attribution](../README.md) · [🌡️ Climate XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

