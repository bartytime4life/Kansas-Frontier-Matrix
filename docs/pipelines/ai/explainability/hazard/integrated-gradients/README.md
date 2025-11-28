---
title: "⚡🟩 KFM v11.2.2 — Hazard Integrated Gradients (IG) Explainability (Deep Hazard Models · Gradient Attribution · PROV)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Component (Hazard IG)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
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
sensitivity: "Explainability-Hazard-IG"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-integrated-gradients"
  - "deep-hazard-models"
  - "gradient-attribution"
  - "hazard-driver-analysis"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/hazard/integrated-gradients"
  applies_to:
    - "hazard-ig-global"
    - "hazard-ig-local"
    - "hazard-ig-jsonld"
    - "hazard-driver-codes"
    - "care-governance"
    - "h3-masking"
    - "prov-xai"
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

# ⚡🟩 **Hazard Integrated Gradients (IG) Explainability**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/README.md`

**Purpose:**  
Define the **Integrated Gradients (IG) explainability subsystem** for **deep hazard models**, generating deterministic gradient-based global & local hazard drivers, spatial evidence maps, and FAIR+CARE-aligned JSON-LD explainability used by:

- ⚡ Story Node v3 (hazard narratives)  
- 🧭 Focus Mode v3 (hazard reasoning windows)  
- 🗺️ Hazard visualization & audit dashboards  
- 🏛 Governance & sovereignty review operations

</div>

---

## 📘 Overview

Hazard IG explainability provides gradient-based insight into **deep-learning hazard models**, identifying which features contributed most to predictions.

Applicable to:

- 🌀 **Tornado / Rotation / Shear IG**  
- 💨 **Wind / Gust / LLJ IG**  
- 🌩️ **Hail / Severe Convection IG**  
- 🌧️ **Flood / Flash-Flood IG**  
- 🔥 **Wildfire Fuels / VPD / Spread IG**  
- ⚡ **Multi-Hazard IG Fusion Models**  

IG is essential when SHAP is insufficient for **deep spatial/temporal feature interactions**.

Outputs include:

- Global gradient attribution  
- Local sample-level gradient maps  
- Spatial IG rasters & tiles (if applicable)  
- Narrative-ready driver summaries  
- JSON-LD semantic evidence bundles  
- PROV-O lineage  
- STAC-XAI metadata  

Always subject to sovereignty & CARE enforcement.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/integrated-gradients/
    ├── 📄 README.md                       # This file
    │
    ├── 📁 global/                         # Global IG driver attribution
    │   ├── 📄 ig-global.json
    │   ├── 📄 summary.md
    │   └── 📁 jsonld/
    │       ├── 📄 xai-ig-global.jsonld
    │       └── 📄 xai-hazard-ig-driver-codes.jsonld
    │
    ├── 📁 samples/                        # Local/sample-level IG attribution
    │   ├── 📄 ig-samples.json
    │   ├── 📄 sample-metadata.json
    │   └── 📁 jsonld/
    │       ├── 📄 xai-ig-local.jsonld
    │       └── 📄 xai-hazard-ig-local-driver-codes.jsonld
    │
    └── 📁 templates/                      # IG templates (JSON, JSON-LD, summaries)
        ├── 📄 ig-global-template.json
        ├── 📄 ig-local-template.json
        ├── 📄 hazard-ig-driver-taxonomy.json
        ├── 📄 xai-ig-global-template.jsonld
        └── 📄 xai-ig-local-template.jsonld

---

## 🔍 Explainability Components

### 1. 🟥 Global IG Attribution (`global/`)
Captures system-level behavior:

- Aggregated gradient magnitudes  
- Feature/domain interactions (e.g., CAPE × shear, VPD × fuel dryness)  
- Seasonal / situational hazard relevance  
- CARE-filtered spatial abstractions  
- JSON-LD global evidence bundles  
- STAC-XAI metadata  
- PROV lineage  

---

### 2. 🟦 Local IG Attribution (`samples/`)
Event-level gradient explanations:

- Per-sample IG maps  
- Local hazard drivers (wind, hail, flood, wildfire, tornado)  
- H3-masked spatial explanation  
- JSON-LD local evidence  
- Outcome & uncertainty metadata  
- PROV linking to model & STAC inputs  

Used by:

- Story Node v3 event narratives  
- Focus Mode local reasoning surfaces  

---

### 3. 🟩 Templates (`templates/`)
Defines deterministic structures for:

- JSON global IG vector templates  
- JSON local IG vector templates  
- Semantic JSON-LD templates  
- Narrative hazard-driver taxonomy templates  
- Governance-safe summaries  

Everything is version-pinned and CI-validated.

---

## 📡 STAC Integration Requirements

All IG assets MUST include:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:{global|local|spatial}`  
- `kfm:model_version`  
- `kfm:input_items`  
- Checksums (`checksum:multihash`)  
- CRS metadata (if spatial)  
- CARE + sovereignty metadata  
- PROV references  

---

## 🧾 PROV-O Lineage Requirements

Every global/local IG output MUST provide:

- `prov:wasGeneratedBy` (hazard-model inference pipeline)  
- `prov:used` (STAC hazard + climate datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity)  
- Optional lineage from:
  - SHAP ↔ IG comparisons  
  - IG → Story Node driver mapping  

---

## 🔐 FAIR+CARE Requirements

Hazard IG outputs MUST:

- Use H3 abstraction for any spatial references  
- Mask/remove sensitive patterns (e.g., wildfire-risk near restricted areas)  
- Include sovereignty metadata  
- Include CARE scope fields  
- Avoid speculation about cause-and-effect beyond model evidence  
- Comply with **Data Contract v3**  

---

## 🧪 Testing Requirements

Hazard IG pipelines MUST pass:

- Deterministic comparison tests  
- JSON-LD schema validation  
- STAC-XAI extension compliance  
- CARE + sovereignty masking tests  
- CRS/vertical metadata validation  
- Drift stability tests (IG sensitivity baseline)  
- PROV-O lineage validation  

Fails → **merge blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                            |
|----------|------------|------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard Integrated Gradients explainability specification |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard XAI](../README.md) · [🧠 AI Pipeline Layer](../../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

