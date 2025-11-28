---
title: "🌡️🟨📄 KFM v11.2.2 — Climate CAMs JSON-LD Explainability Bundles (Global · Local · Pixel-Driver Evidence)"
path: "docs/pipelines/ai/explainability/climate/cams/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-version-hash>"
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
sensitivity: "Explainability-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-cams-jsonld"
  - "jsonld-xai"
  - "pixel-driver-evidence"
  - "spatial-xai"
  - "global-xai"
  - "local-xai"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/cams/jsonld"
  applies_to:
    - "jsonld-global"
    - "jsonld-local"
    - "jsonld-spatial"
    - "stac-xai"
    - "prov-xai"
    - "h3-masking"
    - "care-governance"
    - "semantic-driver-extraction"

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

# 🌡️🟨📄 **Climate CAMs JSON-LD Explainability Bundles**  
`docs/pipelines/ai/explainability/climate/cams/jsonld/README.md`

**Purpose:**  
Define the **JSON-LD explainability bundle formats** produced by Climate CAMs & Saliency explainability pipelines — capturing global, local, and spatial pixel-driver evidence in a **FAIR+CARE-aligned**, **STAC-compatible**, **PROV-linked**, and **narrative-ready** format for KFM v11.2.2.

</div>

---

## 📘 Overview

This layer expresses CAMs/saliency explainability as **machine-readable semantic bundles**:

- Global climate driver evidence  
- Local driver evidence for single predictions  
- Pixel-to-feature explanation chains  
- Spatial driver abstractions  
- Masking metadata (H3 generalization)  
- Full provenance (training → inference → XAI)  
- STAC `kfm:explainability:*` fields  
- Story Node v3 & Focus Mode v3 integration  

JSON-LD bundles generated here serve as the foundation for:

- Climate Story Nodes (narrative explanations)  
- Focus Mode climate windows (spatial driver overlays)  
- AI governance & audit review  
- Explainability dashboards  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/cams/jsonld/
    ├── 📄 README.md                            # This file
    │
    ├── 📄 xai-cam-global.jsonld                # Global pixel-driver JSON-LD bundle
    ├── 📄 xai-cam-local.jsonld                 # Local (per-event) driver bundle
    └── 📄 xai-cam-driver-summary.jsonld        # Narrative-ready driver summary (global/local fusion)

---

## 🔍 JSON-LD Explainability Components

### 1. 🟥 Global CAM JSON-LD (`xai-cam-global.jsonld`)
Represents **system-wide pixel-driver relationships**:

- Aggregated CAM activation patterns  
- Ranked climate variables  
- Spatial relevance summaries  
- Model-version lineage  
- STAC input dataset provenance  
- CARE masking flags  

Used by:

- Story Node v3 (global drivers)  
- Focus Mode v3 overview layers  
- Climate reasoning dashboards  

---

### 2. 🟦 Local CAM JSON-LD (`xai-cam-local.jsonld`)
Represents **per-prediction CAM evidence**:

- Local heatmap-derived pixel drivers  
- Climate variable contributions  
- Localized spatial influence  
- Per-event metadata (timestep, area)  
- CARE masking of sensitive regions  
- PROV-O lineage  

Used by:

- Story Node v3 local-event explanations  
- Focus Mode v3 “local reasoning windows”  

---

### 3. 🟩 Narrative Driver Summary (`xai-cam-driver-summary.jsonld`)

A synthesized, narrative-safe driver summary combining:

- Global CAM insights  
- Local CAM insights  
- Spatial abstraction  
- CARE & sovereignty filtering  
- Semantic driver codes  
- XAI-to-narrative alignment rules  

Used directly by:

- Story Node v3 (climate evidence blocks)  
- Focus Mode v3 summary overlays  

---

## 📡 STAC Integration Requirements

Each JSON-LD asset MUST include:

- `kfm:explainability:method = "cams"`  
- `kfm:explainability:global` or `local` or `spatial`  
- Asset URI + `checksum:multihash`  
- CRS metadata (if spatial)  
- Model version metadata  
- Input STAC IDs (`kfm:input_items`)  
- Link to raster/PNG CAM assets  
- CARE masking metadata  

---

## 🧾 PROV-O Lineage Requirements

All bundles MUST include:

- `prov:wasGeneratedBy` (pipeline + model)  
- `prov:used` (input datasets)  
- `prov:generatedAtTime`  
- `prov:Agent`  
- `prov:wasDerivedFrom` (model → CAM → narrative)  

Used by governance + lineage dashboards.

---

## 🔐 FAIR+CARE Requirements

CAM JSON-LD output MUST:

- Mask sensitive geography (H3)  
- Remove/abstract culturally sensitive terrain correlations  
- Carry CARE scope and sovereignty declarations  
- Avoid speculative climate interpretations  
- Use only evidence from the model outputs  
- Avoid revealing real-world restricted landform patterns  

---

## 🧪 Testing Requirements

Bundles must pass:

- JSON-LD schema validation  
- STAC-XAI field validation  
- PROV-O structural validation  
- CARE governance tests  
- Deterministic regeneration tests  
- Pixel-driver integrity checks  
- Linkage tests to CAM raster/PNG assets  

CI failures halt pipeline promotion.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                   |
|----------|------------|-------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate CAMs JSON-LD layer; aligned with XAI Templates & CAMs  |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate CAMs](../README.md) · [🗺️ CAM Maps](../maps/README.md) · [📊 CAM Drivers](../drivers/README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

