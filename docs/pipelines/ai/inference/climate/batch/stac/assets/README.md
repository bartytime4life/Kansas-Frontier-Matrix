---
title: "🌡️📦📁 KFM v11.2.2 — Climate Batch Inference STAC Assets (GeoTIFF · NetCDF · Parquet · XAI Bindings · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/batch/stac/assets/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "STAC Asset Specification (Climate Batch Inference)"

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
sensitivity: "Climate-Asset-Metadata"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-stac-assets"
  - "downscaled-asset-schema"
  - "bias-correction-assets"
  - "climate-driver-assets"
  - "anomaly-assets"
  - "xai-asset-linking"
  - "prov-xai"
  - "faircare-governance"
  - "focus-mode-climate"
  - "story-node-climate"

scope:
  domain: "pipelines/ai/inference/climate/batch/stac/assets"
  applies_to:
    - "geotiff-assets"
    - "netcdf-assets"
    - "parquet-assets"
    - "xai-linked-assets"
    - "scientific-metadata"
    - "projection-metadata"
    - "checksum-metadata"
    - "care-governance"
    - "provenance"
    - "hazard-driver-links"
    - "climate-driver-links"

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

# 🌡️📦📁 **Climate Batch Inference — STAC Asset Definitions**  
`docs/pipelines/ai/inference/climate/batch/stac/assets/README.md`

**Purpose:**  
Define the **canonical STAC asset schemas** for all climate batch inference outputs, including GeoTIFF rasters, NetCDF datasets, Parquet climate driver tables, and JSON-LD explainability bundles.

These asset schemas guarantee:
- Deterministic metadata  
- FAIR+CARE compliance  
- Sovereignty-safe masking  
- XAI linkage (SHAP · IG · CAMs · spatial attribution)  
- PROV-O lineage consistency  
- STAC v11 + KFM-STAC extension alignment  
- Story Node v3 + Focus Mode v3 compatibility  

</div>

---

## 📘 Overview

This directory governs the **per-asset JSON templates** used in climate batch inference.  
Each template defines:

- MIME type  
- Raster/table metadata  
- CRS + vertical axis fields  
- Scientific metadata (STAC Scientific Extension)  
- Asset-level checksums  
- STAC-XAI linkage  
- CARE + sovereignty metadata  
- PROV-O references  

Every climate inference pipeline uses these templates when writing STAC Items.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/batch/stac/assets/
    ├── 📄 README.md                       # This file  
    │
    ├── 📄 geotiff-template.json           # Raster schema for downscaled & anomaly layers
    ├── 📄 netcdf-template.json            # NetCDF schema for climate ensembles & drivers
    ├── 📄 parquet-template.json           # Parquet schema for climate driver tables
    └── 📄 xai-linkage.json                # XAI bundle reference template

---

## 🔍 Asset Schema Specifications

### 1. 🗺️ `geotiff-template.json` — Raster Asset Schema

Required fields:

- `"type": "image/tiff; application=geotiff"`  
- `"roles": ["data"]`  
- `"proj:epsg"`  
- `"proj:bbox"`, `"proj:shape"`, `"proj:transform"`  
- `"raster:bands"` (band count, data type, no-data value)  
- `"scientific:units"` (Kelvin, mm/day, J/kg, etc.)  
- `"checksum:multihash"`  
- `"kfm:domain": "climate"`  
- `"kfm:variable"` (temperature, RH, precip, CAPE, etc.)  
- CARE + sovereignty metadata  
- Optional `"xai:*"` links  

Supports:

- Downscaled fields  
- Bias-corrected fields  
- Precipitation hazard inputs  
- Seasonal anomalies  

---

### 2. 🌐 `netcdf-template.json` — NetCDF Asset Schema

Required fields:

- `"type": "application/netcdf"`  
- `"roles": ["data"]`  
- `"scientific:units"`  
- `"scientific:variable_description"`  
- `"proj:epsg"`  
- `"checksum:multihash"`  
- `"kfm:model_version"`  
- `"kfm:variable_set"` (list of variables contained)  
- `"kfm:ensemble_member"` (optional)  
- CARE + sovereignty metadata  
- `"xai:*"` explainability fields  

Used for:

- Multi-variable climate ensembles  
- Seasonal anomaly batches  
- Low-frequency climate derivatives  

---

### 3. 📊 `parquet-template.json` — Parquet Asset Schema

Required fields:

- `"type": "application/x-parquet"`  
- `"roles": ["data"]`  
- `"schema"` (column definitions)  
- `"kfm:driver_set"` (CAPE, CIN, SRH, lapse rates, LLJ metrics, soil moisture indices)  
- `"checksum:multihash"`  
- `"proj:epsg"` (if spatial columns present)  
- CARE + sovereignty metadata  
- `"xai:drivers"` for semantic mapping  

Used for:

- Climate driver tables  
- Aggregated hazard-linked variables  
- Derived environmental predictors  

---

### 4. 🧬 `xai-linkage.json` — Explainability Bundle Linkage

Defines how STAC assets link to JSON-LD XAI bundles.

Required fields:

- `"xai:local"` (SHAP/IG local explainability)  
- `"xai:global"` (global drivers)  
- `"xai:spatial"` (CAM/IG rasters or tiles)  
- `"xai:drivers"` (semantic driver taxonomy)  
- `"prov:wasGeneratedBy"`  
- `"prov:used"`  
- CARE + sovereignty metadata  

Used to build:

- Story Node v3 reasoning blocks  
- Focus Mode explainability overlays  
- Hazard integration pipelines  

---

## 📡 STAC-XAI Integration

Asset templates must fully comply with the **KFM-XAI metadata standard**, including:

- `kfm:explainability:*` fields  
- Links to JSON-LD bundles in `jsonld/`  
- STAC Item → XAI mapping consistency  
- XAI provenance  

---

## 🔐 FAIR+CARE & Sovereignty Metadata

All asset templates MUST include placeholders for:

- CARE scope & notes  
- Sovereignty flags  
- H3 masking metadata for any spatial footprint  
- Restrictions on hazardous/sensitive geographic inferences  
- Data Contract v3 compliance  

---

## 🧪 CI Enforcement

CI MUST check:

- Schema correctness for each template  
- STAC-XAI field inclusion  
- KFM-STAC v11 compliance  
- CARE/scope placeholders  
- Sovereignty metadata presence  
- Deterministic key ordering  
- CRS + vertical axis validity  
- PROV-O linkage fields  
- Hash-stability rules  

Any violations → ❌ merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                            |
|----------|------------|------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Batch STAC Asset schema suite for KFM v11.2.2   |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate STAC](../README.md) · [🌡️ Climate Inference Root](../../README.md) · [🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

