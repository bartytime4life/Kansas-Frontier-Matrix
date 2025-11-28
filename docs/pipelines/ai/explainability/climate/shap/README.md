---
title: "🌡️🟥 KFM v11.2.2 — Climate SHAP Explainability (Global · Local · Narrative Drivers)"
path: "docs/pipelines/ai/explainability/climate/shap/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Component"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
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
  - "climate-xai"
  - "shap-global"
  - "shap-local"
  - "narrative-drivers"
  - "jsonld-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/shap"
  applies_to:
    - "climate-shap-global"
    - "climate-shap-local"
    - "xai-to-narrative"
    - "jsonld-shap"
    - "stac-xai"
    - "care-governance"

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

# 🌡️🟥 **Climate SHAP Explainability**  
`docs/pipelines/ai/explainability/climate/shap/README.md`

**Purpose:**  
Define the **SHAP explainability subsystem** for climate models in KFM v11.2.2, generating FAIR+CARE-aligned **global**, **local**, and **narrative-ready** SHAP drivers for:

- Downscaling  
- Bias correction  
- Seasonal/annual forecasting  
- Climate anomaly detection  
- Climate–hydrology–terrain fusion models  

Outputs produced here feed:

- STAC v11 explainability assets  
- Story Node v3 narratives  
- Focus Mode v3 semantic reasoning  
- Governance, audit, and transparency layers  

</div>

---

## 📘 Overview

Climate SHAP explainability pipelines produce:

- **Global SHAP driver vectors** — ranked feature importance  
- **Local SHAP explanations** — per-prediction attribution  
- **Narrative-ready driver summaries** — for Story Node v3 & Focus Mode v3  
- **JSON-LD-encoded explainability bundles**  
- **STAC v11-compliant explainability assets**  
- **CARE-safe masked outputs**  

All SHAP outputs must be:

- Deterministic  
- Version-pinned  
- Machine-extractable  
- FAIR+CARE aligned  
- PROV-linked  
- Geospatially masked using H3 where required  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/shap/
    ├── 📄 README.md                        # This file
    │
    ├── 📁 global/                          # Global SHAP vectors
    │   ├── 📄 global.json                  # Global feature importance
    │   └── 📄 summary.md                   # Human-readable summary of global drivers
    │
    ├── 📁 local/                           # Local (per-prediction) SHAP outputs
    │   ├── 📄 local.json                   # Local contribution vectors
    │   └── 📄 samples.json                 # Selected local examples
    │
    └── 📁 jsonld/                          # JSON-LD explainability bundles
        ├── 📄 xai-global.jsonld            # Global explainability bundle
        ├── 📄 xai-local.jsonld             # Local explainability bundle
        └── 📄 xai-driver-summary.jsonld    # Narrative-ready driver summary

---

## 🔍 Component Specification

### 1. 🟥 Global SHAP Attribution

Used for:

- Climate downscaling  
- Forecasting  
- Bias correction  
- Anomaly detection  

Outputs MUST include:

- Ranked feature list  
- Contribution magnitudes  
- JSON-LD global attribution  
- Model version metadata  
- Dataset lineage entries  
- CARE masking where needed  

---

### 2. 🟦 Local SHAP Attribution

Local attribution MUST include:

- Per-sample feature impacts  
- Contribution vectors  
- Uncertainty indicators  
- CARE masking of sensitive context  
- PROV lineage (input → driver → output)  

Used in:

- Story Node event narratives  
- Focus Mode explanation context windows  
- Human-accessible debug surfaces  

---

### 3. 🧭 SHAP → Narrative Conversion

Narrative drivers MUST:

- Be derived strictly from SHAP global/local outputs  
- Undergo FAIR+CARE filtering  
- Avoid speculation  
- Provide geotemporal context (if applicable)  
- Produce structured JSON-LD story fragments  

Story Node v3 uses SHAP drivers as:

- **Evidence blocks**  
- “Why this climate outcome occurred” explanations  
- Model behavior insights  

---

## 📡 STAC Integration Requirements

SHAP assets MUST produce:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:global` (hash + URI)  
- `kfm:explainability:local` (hash + URI)  
- CRS & spatial extent (if applicable)  
- Model version metadata  
- Multihash checksums  
- Provenance links  

---

## 🧾 PROV-O Lineage Requirements

Each SHAP product MUST include:

- `prov:wasGeneratedBy` (model + pipeline version)  
- `prov:used` (input STAC datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (training or inference identity)  

---

## 🔐 FAIR+CARE Requirements

Climate SHAP pipelines MUST:

- Mask culturally sensitive areas via H3  
- Avoid generating drivers tied to cultural/tribal identity  
- Record CARE scope metadata  
- Respect sovereignty and data licensing  
- Avoid speculative or non-evidence-based statements  

---

## 🧪 Testing Requirements

Tests MUST validate:

- Deterministic SHAP output  
- JSON-LD validity  
- STAC compatibility  
- CARE governance filters  
- Drift detection baselines (SHAP requires stability)  
- Model-version correctness  

CI failures → **blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                    |
|----------|------------|--------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate SHAP explainability spec, aligned with XAI templates     |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate Explainability](../README.md) · [🧠 AI Pipeline Layer](../../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

