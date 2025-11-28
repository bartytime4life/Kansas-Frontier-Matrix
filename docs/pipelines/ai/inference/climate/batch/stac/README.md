---
title: "🌡️📦 KFM v11.2.2 — Climate AI Batch Inference STAC Outputs (Deterministic · XAI-Aligned · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/batch/stac/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "STAC Integration Layer (Climate Batch Inference)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
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
sensitivity: "Climate-Inference-Batch-STAC"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "stac-climate-batch"
  - "climate-inference-metadata"
  - "downscaling-stac"
  - "bias-correction-stac"
  - "climate-driver-stac"
  - "xai-ready-stac"
  - "stac-xai"
  - "prov-xai"
  - "faircare-governance"
  - "focus-mode-climate"
  - "story-node-climate"

scope:
  domain: "pipelines/ai/inference/climate/batch/stac"
  applies_to:
    - "stac-item-generation"
    - "stac-collection-metadata"
    - "climate-driver-stac-items"
    - "bias-corrected-stac-items"
    - "downscaled-stac-items"
    - "xai-linked-assets"
    - "telemetry-and-lineage"
    - "faircare-maskable-properties"

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

# 🌡️📦 **STAC Layer — Climate Batch AI Inference**  
`docs/pipelines/ai/inference/climate/batch/stac/README.md`

**Purpose:**  
Define how **Climate Batch AI Inference** publishes **STAC Collections**, **STAC Items**, and **XAI-linked assets**, ensuring:

- Deterministic metadata  
- FAIR+CARE compliance  
- Sovereignty-safe masking  
- PROV-O lineage  
- Full compatibility with **STAC v11**, **STAC-XAI**, **STAC-Climate**, and KFM’s AI explainability framework.

</div>

---

## 📘 Overview

Every Climate Batch inference run produces **structured, immutable STAC outputs** that encode:

- Downscaled climate surfaces  
- Bias-corrected datasets  
- Climate driver derivatives (CAPE, CIN, SRH, lapse rates, LLJ metrics, soil moisture, etc.)  
- Seasonal/long-range anomaly indicators  
- Explainability bundles (SHAP / IG / CAMs / spatial attribution)  
- CARE + Sovereignty metadata  
- Full PROV lineage

These STAC items are consumed directly by:

- MapLibre + Cesium  
- Climate driver AI pipelines  
- Hazard AI pipelines  
- Story Node v3 + Focus Mode v3  
- KFM governance dashboards  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/batch/stac/
    ├── 📄 README.md                          # This file
    │
    ├── 📄 collection.json                     # STAC Collection for all batch inference outputs
    ├── 📁 items/                              # Individual STAC Items per inference batch
    │   ├── 📄 <timestamp>-downscaled.json
    │   ├── 📄 <timestamp>-bias-corrected.json
    │   ├── 📄 <timestamp>-drivers.json
    │   └── 📄 <timestamp>-anomalies.json
    │
    └── 📁 assets/                             # Asset metadata templates
        ├── 📄 geotiff-template.json
        ├── 📄 parquet-template.json
        ├── 📄 netcdf-template.json
        └── 📄 xai-linkage.json

---

## 🔍 STAC Collection Requirements

Each Climate Batch Collection MUST include:

- `id = "kfm-climate-inference-batch-v11"`  
- STAC extensions:
  - `"projection"`
  - `"raster"`
  - `"checksum"`
  - `"scientific"`
  - `"xai"` (KFM-XAI extension)
  - `"kfm:climate"` (domain extension)
- CRS + vertical metadata (projection extension)  
- Temporal extent (inference run time)  
- Provenance metadata:  
  - `kfm:inference_model_version`  
  - `kfm:software_stack`  
  - `prov:wasGeneratedBy`  

---

## 🔍 STAC Item Requirements

Each STAC Item MUST include:

### Core
- `type = "Feature"`  
- `stac_version = "1.x"`  
- `stac_extensions` including `"xai"`, `"projection"`, `"raster"`  
- `bbox`, `proj:bbox`, `proj:shape`, `proj:transform`  
- `datetime = <inference datetime>`

### Domain Metadata
- `kfm:domain = "climate"`  
- `kfm:inference_type = "batch"`  
- `kfm:model_version`  
- `kfm:driver_set` (if climate drivers included)

### CARE + Sovereignty
- `care:scope`  
- `care:notes`  
- `sovereignty:flags`  

### Lineage
- `prov:wasGeneratedBy`  
- `prov:used` (STAC input Items)  
- `prov:generatedAtTime`  

### XAI Linkage
- `"xai:local"` → link to JSON-LD explainability  
- `"xai:global"` → optional  
- `"xai:spatial"` → CAM/IG rasters or tiles  
- `"xai:drivers"` → climate driver semantic evidence

---

## 📦 Asset Requirements

### GeoTIFF (Raster)
- `"type": "image/tiff; application=geotiff"`  
- `"raster:bands"` definitions  
- `"proj:epsg"`  
- `checksum:multihash`

### NetCDF
- `"type": "application/netcdf"`  
- `"kfm:variable_set"`  
- Climate metadata fields  

### Parquet
- `"type": "application/x-parquet"`  
- Tabular climate drivers  
- Derived hazard-index variables  

### Explainability Links
- `"xai:href"` → JSON-LD explainability bundle  
- `"prov:wasGeneratedBy"` anchor  
- `"care:*"` required values  

---

## 📡 STAC-XAI Integration

STAC items MUST correctly reference:

- `kfm:explainability:method`  
- `kfm:explainability:{global|local|spatial}`  
- JSON-LD files under `/jsonld` directory  
- CAM/IG/SHAP/spatial attribution  
- Driver taxonomies  

This enables:

- Story Node v3 narrative assembly  
- Focus Mode v3 context-aware reasoning  
- Governance and lineage dashboards  

---

## 🔐 FAIR+CARE Requirements

All STAC Climate outputs must:

- Include sovereign rights metadata  
- Apply H3-generalization where required  
- Provide CARE scope + notes  
- Avoid sensitive cultural/tribal content  
- Follow Data Contract v3  
- Respect safe climate communications  

---

## 🧪 CI & Validation Requirements

CI MUST validate:

- Correct STAC schema  
- Projection metadata  
- Deterministic field ordering  
- Existence of XAI linkage  
- CARE + sovereignty metadata  
- Valid multihash for every asset  
- PROV lineage completeness  
- JSON-LD explainability integrity  

Failure → **CI block**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                           |
|----------|------------|-----------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial STAC layer for Climate Batch AI Inference under v11.2.2 |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Batch Inference](../README.md) · [🌡️ Climate Inference Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

