---
title: "🌡️⚡🧠📄 KFM v11.2.2 — Climate Realtime XAI Layer (SHAP · IG · CAM · Spatial Attribution · JSON-LD · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/realtime/xai/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Realtime Explainability Layer"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/climate-inference-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-climate-inference-v11.2.2.json"
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
sensitivity: "Climate-Inference-Realtime-XAI"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-realtime-xai"
  - "shap-realtime"
  - "ig-realtime"
  - "cams-realtime"
  - "spatial-attribution-realtime"
  - "jsonld-xai"
  - "prov-xai"
  - "stac-xai"
  - "story-node-climate"
  - "focus-mode-climate"
  - "care-governance"
  - "h3-masking"

scope:
  domain: "pipelines/ai/inference/climate/realtime/xai"
  applies_to:
    - "shap"
    - "integrated-gradients"
    - "cams"
    - "spatial-attribution"
    - "jsonld-generation"
    - "prov-xai"
    - "stac-xai"
    - " CARE-governance"
    - "sovereignty-protection"
    - "focus-mode"
    - "story-node-integration"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 🌡️⚡🧠📄 **Realtime Climate XAI Layer — KFM v11.2.2**  
`docs/pipelines/ai/inference/climate/realtime/xai/README.md`

**Purpose:**  
Provide the **realtime explainability subsystem** for Climate AI Inference, supporting **SHAP**, **Integrated Gradients**, **CAMs**, and **Spatial Attribution**, producing **JSON-LD explainability bundles**, **STAC-XAI metadata**, and **PROV-O lineage** for live climate predictions in KFM.

</div>

---

## 📘 Overview

The Climate Realtime XAI module provides **on-demand**, **low-latency**, and **deterministic** explainability for:

- 🌡️ Downscaled climate variables  
- 💧 Climate anomaly / drift detections  
- 💨 Hazard-linked climate drivers  
- ❄️ Snowpack / freeze-thaw predictions  
- 🔮 Any AI-generated climate inference  

Realtime XAI supports:

- **Focus Mode v3** (map-aware climate reasoning)  
- **Story Node v3** (narrative-ready semantic evidence)  
- **Governance dashboards** (FAIR+CARE compliance)  
- **Realtime API responses** (REST, WebSocket, gRPC)

Compute intensity varies — handlers may throttle or queue XAI requests.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/realtime/xai/
    ├── 📄 README.md                     # This file
    │
    ├── 📄 shap.py                       # SHAP local explainability
    ├── 📄 ig.py                         # Integrated Gradients local explainability
    ├── 📄 cams.py                       # CAM spatial attribution
    └── 📄 spatial.py                    # Realtime spatial-attribution mini-rasters/tiles

---

## 🤖 XAI Methods Supported

### 1. 🔍 SHAP Local (Event-Level Attribution)
- Per-query attribution  
- Feature-importance vectors  
- Deterministic under seed lock  
- JSON-LD semantic driver mapping  
- CARE-protected output  

### 2. 🧬 Integrated Gradients (IG Local)
- Gradient-based explainability  
- Suitable for deeper climate inference models  
- Produces semantic driver lists  
- Supports H3-masked spatial metadata  

### 3. 🛰️ CAMs (Class Activation Maps)
- Spatial relevance for CNN/Transformer climate models  
- Optional COG/GeoParquet mini-tile outputs  
- Downsampled for realtime constraints  
- Always H3-generalized  

### 4. 🗺️ Spatial Attribution (Raster/Tile Micro-Surfaces)
- Lightweight spatial surfaces  
- Useful for Focus Mode v3 contextual visualizations  
- Optional multiscale tiles  
- Full governance enforcement  

All of the above support:

- JSON-LD export  
- XAI driver taxonomy  
- STAC-XAI compliance  
- PROV-O lineage  
- CARE & sovereignty metadata  

---

## 🧬 JSON-LD Outputs (Realtime)

Each explainability call (SHAP, IG, CAM, Spatial) must emit:

- **JSON-LD bundle** with:
  - `@context` (KFM-XAI + PROV-O)  
  - `xai:drivers`  
  - `xai:hazard_links` (if used for hazard drivers)  
  - `xai:spatial_context` (H3 generalized)  
  - `care:*` metadata  
  - `sovereignty:*` flags  
  - `kfm:model_version`  
  - `kfm:input_items`  
  - `checksum:multihash`  
  - `prov:*` lineage  

---

## 🧭 Realtime XAI Flow (GitHub-Safe Mermaid)

```mermaid
flowchart TD
    A[Inference Output] --> B[Select XAI Method]
    B --> C[Compute SHAP IG CAM or Spatial]
    C --> D[Generate JSON-LD Bundle]
    D --> E[Apply CARE and Sovereignty Filters]
    E --> F[Return to Handler]
    F --> G[Emit PROV + Telemetry]
```

---

## 🔐 FAIR+CARE & Sovereignty Requirements

Realtime XAI MUST:

- Apply H3 spatial masking  
- Avoid sensitive geographic inference  
- Provide CARE scope + notes  
- Include sovereignty flags  
- Follow Data Contract v3  
- Ensure all climate narratives remain non-speculative  

---

## 📡 STAC-XAI Requirements

If realtime outputs are persisted:

- Must embed `kfm:explainability:{local|spatial}`  
- Must include JSON-LD linkage fields  
- Must include CRS + vertical axis metadata  
- Must register in STAC Collection if configured  

---

## 🧪 CI Requirements

Realtime XAI code MUST pass:

- Deterministic attribution test  
- JSON-LD schema validation  
- STAC-XAI metadata validation  
- CARE + sovereignty lint checks  
- CRS + vertical validation (if spatial)  
- PROV lineage completeness  
- Performance thresholds (latency under configured limit)

---

## 🕰 Version History

| Version  | Date       | Notes                                                           |
|----------|------------|-----------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial realtime XAI specification (SHAP, IG, CAM, Spatial)     |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Realtime Inference](../README.md) • [🌡️ Climate Inference Root](../../README.md) • [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

