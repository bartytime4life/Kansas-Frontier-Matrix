---
title: "🌡️📦🗂️ KFM v11.2.2 — Climate Batch Inference STAC Items (Deterministic · XAI-Linked · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/batch/stac/items/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "STAC Item Specification (Climate Batch Inference)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
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
care_label: "Public · Low-Risk"
sensitivity: "Climate-Inference-STAC-Items"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-stac-item-spec"
  - "batch-inference-stac"
  - "downscaled-stac-items"
  - "bias-corrected-stac-items"
  - "driver-stac-items"
  - "anomaly-stac-items"
  - "xai-stac-binding"
  - "prov-xai"
  - "care-governance"
  - "h3-generalization"
  - "story-node-integration"
  - "focus-mode-climate"

scope:
  domain: "pipelines/ai/inference/climate/batch/stac/items"
  applies_to:
    - "stac-items"
    - "downscaled-climate-stac"
    - "bias-corrected-stac"
    - "climate-driver-items"
    - "anomaly-items"
    - "xai-linked-items"
    - "prov-items"
    - "care-governance"
    - "deterministic-stac"

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

# 🌡️📦🗂️ **STAC Items for Climate Batch AI Inference**  
`docs/pipelines/ai/inference/climate/batch/stac/items/README.md`

**Purpose:**  
Define the **canonical STAC Item structure** for all climate batch inference outputs, including:

- Downscaled climate fields  
- Bias-corrected products  
- Derived climate drivers (e.g., CAPE, CIN, SRH, lapse rates)  
- Seasonal/long-range anomaly layers  
- Explainability artifacts (SHAP, IG, CAMs, spatial attribution)  

All STAC items are deterministic, FAIR+CARE aligned, sovereignty-aware, STAC-XAI compliant, and ready for use by **Story Node v3**, **Focus Mode v3**, and downstream AI pipelines.

</div>

---

## 📘 Overview

Every inference batch generates **multiple STAC Items**, one per output family:

- **downscaled fields** (GeoTIFF / NetCDF)  
- **bias-corrected fields**  
- **climate drivers** (Parquet or TIFF)  
- **anomaly indicators**  
- **XAI bundles** (JSON-LD)  

Each Item:

- References input STAC Items  
- Encodes provenance via PROV-O  
- Includes CARE + sovereignty metadata  
- Includes XAI metadata (local/global/spatial)  
- Uses deterministic ordering  
- Adheres to KFM-STAC v11 and STAC-XAI extension  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/batch/stac/items/
    ├── 📄 README.md                         # This file
    │
    ├── 📄 <timestamp>-downscaled.json       # Downscaled grid
    ├── 📄 <timestamp>-bias-corrected.json   # Bias-corrected climate layer
    ├── 📄 <timestamp>-drivers.json          # Derived climate drivers
    ├── 📄 <timestamp>-anomalies.json        # Seasonal / long-range anomalies
    └── 📄 <timestamp>-xai.json              # Semantic explainability linkage

---

## 📦 STAC Item Requirements

### 1. Core STAC Fields (Required)
Each Item MUST specify:

- `"type": "Feature"`  
- `"stac_version": "1.x"`  
- `"stac_extensions"` including:
  - `"projection"`
  - `"raster"`
  - `"checksum"`
  - `"scientific"`
  - `"xai"`
  - `"kfm:climate"` (domain extension)
- `bbox`  
- `properties.datetime`  
- `proj:epsg`  
- `proj:bbox`, `proj:shape`, `proj:transform`  
- `checksum:multihash`  

---

### 2. KFM Domain Metadata
Each Item MUST include:

- `kfm:domain = "climate"`  
- `kfm:inference_type = "batch"`  
- `kfm:model_version`  
- `kfm:driver_set` (if present)  
- `kfm:hazard_links` (if hazard climate drivers produced)  

---

### 3. CARE + Sovereignty Metadata
All items MUST declare:

- `care:scope`  
- `care:notes`  
- `sovereignty:flags`  

Mandatory for public-facing climate data.

---

### 4. PROV-O Lineage Metadata
Each Item MUST include:

- `prov:wasGeneratedBy` — batch inference run  
- `prov:used` — input climate STAC Items  
- `prov:generatedAtTime`  
- `prov:Agent` — model + software identity  

Optional:

- `prov:wasDerivedFrom` for multimodal or chained explainability  

---

## 📡 XAI Integration (STAC-XAI)

All Items MUST link to explainability bundles:

- `"xai:local"` (for IG/SHAP local)  
- `"xai:global"` (global SHAP/IG)  
- `"xai:spatial"` (CAM/spatial-attribution rasters/tiles)  
- `"xai:drivers"` (climate-driver semantic bundles)

Bundles are located under the `/jsonld` directory of the inference output package.

---

## 🗂 Asset Requirements (Per STAC Item)

### GeoTIFF  
- `"type": "image/tiff; application=geotiff"`  
- `"raster:bands"`  
- CRS metadata  
- Multihash checksum  

### NetCDF  
- `"type": "application/netcdf"`  
- Climate variable metadata  
- Scientific extension required  

### Parquet  
- `"type": "application/x-parquet"`  
- Used for climate driver tables  

---

## 🧪 CI Enforcement

Each STAC Item MUST pass:

- JSON schema validation  
- KFM-STAC v11 compliance  
- STAC-XAI extension check  
- Deterministic ordering scan  
- CARE + sovereignty metadata validation  
- CRS + vertical axis check  
- Provenance completeness (PROV-O)  
- Multihash correctness  
- Hazard-driver linkage validation (if present)  

Failures → ❌ merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                             |
|----------|------------|-------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Batch Inference STAC Item specification           |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate STAC](../README.md) · [🌡️ Climate Inference Root](../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
