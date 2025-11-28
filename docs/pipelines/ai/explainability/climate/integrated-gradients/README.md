---
title: "🌡️🟩 KFM v11.2.2 — Climate Integrated Gradients (IG) Explainability"
path: "docs/pipelines/ai/explainability/climate/integrated-gradients/README.md"
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
  - "integrated-gradients"
  - "climate-ig"
  - "deep-model-xai"
  - "gradient-attribution"
  - "narrative-xai"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/integrated-gradients"
  applies_to:
    - "ig-global"
    - "ig-local"
    - "ig-jsonld"
    - "ig-raster"
    - "story-node-xai"
    - "stac-xai"
    - "faircare-governance"

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

# 🌡️🟩 **Climate Integrated Gradients (IG) Explainability**  
`docs/pipelines/ai/explainability/climate/integrated-gradients/README.md`

**Purpose:**  
Define the **Integrated Gradients (IG)** explainability subsystem for climate models, producing FAIR+CARE-compliant gradient attribution maps, JSON-LD bundles, STAC XAI assets, and narrative-ready climate driver evidence used across **Story Node v3**, **Focus Mode v3**, and governance layers.

</div>

---

## 📘 Overview

Climate IG explainability pipelines generate structured attribution for deep-learning–based climate models, including:

- Downscaling CNNs  
- Hybrid climate–terrain–hydrology fusion networks  
- Seasonal/annual deep forecast models  
- Anomaly detection networks  
- Local event probability inference  

Outputs must be:

- Deterministic  
- JSON-LD structured  
- STAC v11 compliant  
- CARE-masked (spatial + semantic)  
- Provenance rich (PROV-O)  
- Version-pinned  

IG is used when SHAP cannot fully capture spatial/temporal deep model interactions.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/integrated-gradients/
    ├── 📄 README.md                   # This file
    │
    ├── 📁 global/                     # Global IG attribution
    │   ├── 📄 ig-global.json          # Global gradient attribution summary
    │   └── 📄 summary.md              # Human-readable summary
    │
    ├── 📁 samples/                    # Local/sample-level attribution
    │   ├── 📄 ig-samples.json         # Local IG heatmaps
    │   └── 📄 sample-metadata.json    # Provenance + context
    │
    └── 📁 jsonld/                     # JSON-LD explainability bundles
        ├── 📄 xai-ig-global.jsonld
        ├── 📄 xai-ig-local.jsonld
        └── 📄 xai-ig-driver-summary.jsonld

---

## 🔍 IG Explainability Components

### 1. 🟥 Global Integrated Gradients
Captures overall behavior of deep climate models by aggregating gradient attribution across a dataset.

Outputs include:

- Global driver intensity vectors  
- Aggregated spatial/temporal contribution maps  
- Cross-feature contribution summaries  
- JSON-LD global IG bundle  
- CARE-masked spatial abstractions  

---

### 2. 🟦 Local Integrated Gradients

For event-level and tile-level predictions:

- Local heatmaps  
- Per-sample gradient vectors  
- Explanation metadata (CRS, timestep, model version)  
- Uncertainty indicators  
- Provenance-backed local IG JSON-LD bundles  

Used in:

- Story Node v3 "local climate event" narratives  
- Focus Mode v3 local reasoning windows  

---

### 3. 🟨 IG → Narrative Driver Summaries

Rule-based and model-guided conversion of IG results into **narrative driver fragments**:

- Only strictly data-grounded reasoning allowed  
- CARE-filtered & sovereignty-respecting  
- Structured JSON-LD summaries  
- No speculation or inferred causation beyond data  

Used by:

- Story Node v3  
- Focus Mode v3’s climate evidence overlays  

---

## 📡 STAC Integration Requirements (KFM-STAC v11)

Each IG product MUST embed:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:global` (URI + checksum)  
- `kfm:explainability:local` (URI + checksum)  
- CRS & geometry metadata (if spatial)  
- Model version fields  
- Multihash checksums  
- Provenance references  

---

## 🧾 PROV-O Lineage Requirements

IG assets must produce:

- `prov:wasGeneratedBy` (pipeline + model)  
- `prov:used` (input STAC datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity + version)  

All lineage must align with KFM-OP v11.

---

## 🔐 FAIR+CARE Requirements

All climate IG outputs MUST:

- Mask sensitive geography using **H3 generalization**  
- Avoid revealing culturally sensitive terrain correlations  
- Include CARE scope metadata  
- Follow dataset sovereignty restrictions  
- Remove/abstract non-public Indigenous indicators  

---

## 🧪 Testing Requirements

IG explainability pipelines must pass:

- Determinism tests (same input → identical IG maps)  
- JSON-LD structure validation  
- STAC asset validation  
- CRS/vertical metadata verification  
- CARE masking + sovereignty logic tests  
- Drift-detection baselines (IG should be stable over model versions)  

Failures → **CI block**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                               |
|----------|------------|---------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Integrated Gradients explainability spec            |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate Explainability](../README.md) · [🧠 AI Pipeline Layer](../../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
