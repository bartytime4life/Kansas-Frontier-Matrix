---
title: "🌡️🟨 KFM v11.2.2 — Climate CAMs & Saliency Explainability (Heatmaps · Pixel Drivers · Spatial Attribution)"
path: "docs/pipelines/ai/explainability/climate/cams/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Component"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
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
sensitivity: "Explainability"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-cams"
  - "saliency-maps"
  - "cnn-explainability"
  - "pixel-drivers"
  - "spatial-xai"
  - "jsonld-xai"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/cams"
  applies_to:
    - "cams-global"
    - "cams-local"
    - "cams-spatial"
    - "cams-jsonld"
    - "care-governance"
    - "stac-xai"

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

# 🌡️🟨 **Climate CAMs & Saliency Explainability**  
`docs/pipelines/ai/explainability/climate/cams/README.md`

**Purpose:**  
Define the **Class Activation Maps (CAMs)** and **saliency-map explainability system** used for deep-learning climate models in KFM v11.2.2.  
Outputs include pixel-level importance maps, spatial attribution rasters, JSON-LD explainability bundles, and narrative-ready driver summaries used in **Story Node v3** and **Focus Mode v3**.

</div>

---

## 📘 Overview

Climate CAMs / saliency pipelines generate detailed spatial explainability for:

- Downscaling CNNs  
- Climate–terrain–hydrology fusion models  
- Radar/imagery-driven prediction models  
- Spatial anomaly detection networks  

Outputs MUST be:

- Deterministic  
- FAIR+CARE-safe  
- CRS-correct  
- Masked via H3 for sensitive locations  
- Properly attributed via PROV-O  
- Packaged into STAC v11 explainability assets  
- Narrative-compatible for Focus Mode & Story Node v3  

This directory defines the pipeline structure for:

- **CAM heatmaps**  
- **Saliency overlays**  
- **Pixel-level driver maps**  
- **TIFF/COG spatial XAI rasters**  
- **JSON-LD XAI bundles**  
- **Narrative driver summaries**  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/cams/
    ├── 📄 README.md                               # This file
    │
    ├── 📁 maps/                                   # CAM/saliency heatmaps
    │   ├── 📄 cam-maps.md
    │   ├── 📄 cam-global.png
    │   └── 📄 cam-local.png
    │
    ├── 📁 drivers/                                # Pixel-driver metadata & summaries
    │   ├── 📄 saliency-driver.json
    │   └── 📄 driver-summary.md
    │
    └── 📁 jsonld/                                 # JSON-LD explainability bundles
        ├── 📄 xai-cam-global.jsonld
        ├── 📄 xai-cam-local.jsonld
        └── 📄 xai-cam-driver-summary.jsonld

---

## 🔍 Explainability Components

### 1. 🟨 CAM Heatmaps
Used for:

- Spatial CNNs  
- Terrain-aware downscaling  
- Climate-radar fusion models  

Outputs include:

- Activation heatmaps  
- Feature-importance visual overlays  
- CARE-masked abstractions  
- TIFF/PNG derivative assets  

---

### 2. 🟥 Saliency Maps
Used for:

- Patch/region-level climate predictions  
- Extreme-event spatial anomaly detection  

Outputs MUST provide:

- Pixel-level gradients  
- Explanation confidence  
- Driver relevance encoding (JSON-LD)  
- Spatial masking where required  

---

### 3. 🧭 Driver & Pixel Attribution Metadata

CAMs → Driver summaries must include:

- Driver code / concept  
- Climate variable associations  
- Spatial relevance intervals  
- CARE-scope indicators  
- Provenance (model version, dataset list)  

---

### 4. 🧠 Narrative Conversion (Story Node v3)

CAMs → narrative drivers MUST:

- Be strictly data-grounded  
- Provide interpretable regional climate context  
- Include masked summaries for protected regions  
- Present climate trends when supported by model evidence  

**Story Node v3** uses these as:

- Evidence blocks  
- “Why this pattern” explanations  
- Spatial driver tags  

---

## 📡 STAC Integration Requirements

Every CAM/saliency explanation MUST include:

- `kfm:explainability:method = "cams"`  
- `kfm:explainability:spatial`  
- Asset checksums (`checksum:multihash`)  
- CRS metadata  
- Bounding geometry  
- Model version  
- JSON-LD explainability bundle references  

Outputs MUST follow **KFM-STAC v11**.

---

## 🧾 PROV-O Lineage Requirements

CAM outputs must include:

- `prov:wasGeneratedBy` (model + pipeline)  
- `prov:used` (STAC input datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity)  

These lineage bundles feed:

- Lineage dashboards  
- Climate narrative generation  
- Focus Mode v3 contextual overlays  

---

## 🔐 FAIR+CARE Requirements

CAM pipelines MUST:

- Mask sensitive locations (H3 generalization)  
- Avoid revealing privileged environmental/cultural geography  
- Include CARE-scope + sovereignty metadata  
- Obey dataset licensing and community protections  

---

## 🧪 Testing Requirements

CAM explainability pipelines MUST pass:

- Deterministic output tests  
- Raster-integrity tests  
- JSON-LD validation  
- STAC XAI asset validation  
- CRS + vertical metadata validation  
- CARE masking tests  
- Drift baselines (CAM stability across versions)  

PRs failing any → **blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                            |
|----------|------------|------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate CAMs explainability layer                        |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate Explainability](../README.md) · [🧠 AI Pipeline Layer](../../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

