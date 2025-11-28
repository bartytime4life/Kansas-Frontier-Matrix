---
title: "🧬🔍 KFM v11.2.2 — Explainability Template Suite (SHAP · IG · CAMs · Spatial Attribution · JSON-LD)"
path: "docs/pipelines/ai/explainability/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Reliability Engineering"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Template Suite"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/ai-explainability-templates-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/ai-explainability-templates-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Explainability-Templates"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "explainability-templates"
  - "xai-metadata"
  - "jsonld-xai"
  - "spatial-xai"
  - "shap"
  - "integrated-gradients"
  - "cams"
  - "saliency"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "ai-explainability-templates"
  applies_to:
    - "xai-jsonld"
    - "xai-tiff"
    - "xai-geojson"
    - "xai-stac"
    - "story-node-xai"
    - "focus-mode-xai"
    - "faircare-governance"
    - "energy/carbon telemetry"

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

# 🧬🔍 **KFM v11.2.2 — Explainability Template Suite**  
`docs/pipelines/ai/explainability/templates/README.md`

**Purpose:**  
Provide the **canonical template suite** for all explainability (XAI) outputs in KFM, including SHAP, IG, CAMs, spatial attribution, JSON-LD driver bundles, STAC-ready explainability assets, and narrative-ready XAI structures used in **Story Node v3** and **Focus Mode v3**.

</div>

---

## 📘 Overview

This directory defines the **governed patterns** for explainability across **all AI model families**:

- Climate  
- Hydrology  
- Hazard  
- Embeddings  
- Focus Mode v3 reasoning  
- Multi-domain fusion models  

Templates here ensure:

- Deterministic, reproducible XAI outputs  
- JSON-LD machine readability  
- Provenance alignment (PROV-O + OpenLineage)  
- STAC v11 compatibility  
- FAIR+CARE masking & sovereignty compliance  
- Seamless input to Story Node v3 + Focus Mode v3  

Explainability templates covered:

- **SHAP global + local attribution**  
- **Integrated Gradients (IG)**  
- **CAMs / saliency maps**  
- **Spatial attribution rasters / tiles**  
- **XAI JSON-LD bundles**  
- **Narrative driver summaries**  
- **XAI → Story Node mapping templates**

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/templates/
    ├── 📄 README.md                              # This file
    │
    ├── 📁 shap/                                  # SHAP templates
    │   ├── 📄 shap-global-template.json
    │   ├── 📄 shap-local-template.json
    │   └── 📄 shap-driver-summary-template.md
    │
    ├── 📁 integrated-gradients/                  # IG templates
    │   ├── 📄 ig-global-template.json
    │   └── 📄 ig-local-template.json
    │
    ├── 📁 cams/                                  # CAM/saliency templates
    │   ├── 📄 cam-overlay-template.md
    │   └── 📄 cam-driver-template.json
    │
    ├── 📁 spatial-attribution/                   # TIFF/COG-based spatial XAI templates
    │   ├── 📄 raster-template.tif
    │   └── 📄 spatial-driver-template.json
    │
    └── 📁 jsonld/                                # JSON-LD, STAC, narrative templates
        ├── 📄 xai-global-template.jsonld
        ├── 📄 xai-local-template.jsonld
        ├── 📄 xai-spatial-template.jsonld
        ├── 📄 xai-driver-summary-template.jsonld
        └── 📄 stac-xai-fields-template.json

---

## 🔍 Template Categories

### 1. 🟥 SHAP Templates
Used for:

- Global driver ranking  
- Local prediction explanations  
- Multi-domain feature comparison  
- Narrative driver extraction  

Outputs MUST support:

- JSON-LD  
- STAC explainability fields  
- CARE masking  

---

### 2. 🟦 Integrated Gradients Templates
Required for deep models:

- Climate downscaling  
- Hydrology fusion  
- Hazard CNNs  

Outputs include:

- IG heatmaps  
- Gradient explanations  
- Deterministic JSON structures  

---

### 3. 🟨 CAM / Saliency Templates
Used for:

- Spatial CNNs  
- Radar-based hazard models  
- Terrain-sensitive models  

Outputs MUST:

- Support TIFF/COG raster export  
- Integrate with H3 masking rules  
- Provide interpretable pixel drivers  

---

### 4. 🟪 Spatial Attribution Templates
For gridded outputs:

- Flood probability  
- Downscaled climate tiles  
- Wildfire spread maps  
- Soil moisture anomalies  

Template outputs include:

- Raster attribution  
- GeoParquet attribution tiles  
- STAC driver metadata  

---

### 5. 🧭 JSON-LD XAI Bundles
Define the **canonical JSON-LD explainability model**:

- Global drivers  
- Local drivers  
- Spatial/tile-level attribution  
- CARE scope & masking metadata  
- PROV links  
- Narrative driver codes  

Consumed by:

- Story Node v3  
- Focus Mode v3  
- Governance dashboards  

---

## 📡 STAC Integration (KFM-STAC v11)

All templates specify how to generate:

- `kfm:explainability:*` fields  
- STAC XAI sidecar JSON  
- Multihash checksums  
- CRS / geometry metadata  
- Model version fields  
- Provenance links  

---

## 🧾 PROV-O Lineage Requirements

Explainability templates MUST support:

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:generatedAtTime`  
- `prov:Agent`  

Outputs feed:

- Lineage dashboards  
- Traceability audits  
- Focus Mode narrative linking  

---

## 🔐 FAIR+CARE Requirements

Explainability templates MUST:

- Mask culturally sensitive areas  
- Use H3 generalization for restricted locations  
- Remove/abstract sensitive drivers  
- Include CARE scope metadata  
- Enforce sovereignty rules from source datasets  

---

## 🧪 Testing Requirements

Templates are validated using:

- JSON-LD schema loads  
- STAC extension validation  
- TIFF raster integrity checks  
- CARE masking unit tests  
- Determinism tests for template-generated content  

PRs modifying any template MUST pass full CI validation.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                    |
|----------|------------|--------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Explainability Template Suite with full STAC/JSON-LD structure   |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Explainability Index](../README.md) · [🧬 XAI Templates (Master)](../../templates/explainability/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

