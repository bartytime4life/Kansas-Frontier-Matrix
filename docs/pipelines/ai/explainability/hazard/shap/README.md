---
title: "⚡🟥 KFM v11.2.2 — Hazard SHAP Explainability (Global & Local Drivers · Tornado · Wind/Hail · Wildfire · Flood)"
path: "docs/pipelines/ai/explainability/hazard/shap/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Component (Hazard SHAP)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
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
sensitivity: "Explainability (Hazard)"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-shap"
  - "hazard-global-drivers"
  - "hazard-local-drivers"
  - "severe-weather-xai"
  - "wildfire-xai"
  - "tornado-wind-hail-xai"
  - "flood-xai"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/hazard/shap"
  applies_to:
    - "hazard-global-shap"
    - "hazard-local-shap"
    - "hazard-driver-taxonomy"
    - "jsonld-hazard-xai"
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

# ⚡🟥 **Hazard SHAP Explainability**  
`docs/pipelines/ai/explainability/hazard/shap/README.md`

**Purpose:**  
Define SHAP-based explainability for **hazard ML models** in KFM — including tornado, hail, wind, severe-weather, flood/flash-flood, and wildfire drivers — producing global & local hazard-driver vectors, FAIR+CARE-aligned JSON-LD bundles, STAC-XAI metadata, and narrative-ready hazard evidence for **Story Node v3** and **Focus Mode v3**.

</div>

---

## 📘 Overview

Hazard SHAP pipelines produce structured feature-importance explanations across:

- 🌀 **Tornado / rotation / shear models**  
- 💨 **Wind & gust prediction models**  
- 🌩️ **Hail & severe-weather classification models**  
- 🔥 **Wildfire probability / spread models**  
- 🌧️ **Flood / flash-flood ML models**  
- ⚡ **Multi-hazard fusion models**  

Hazard SHAP outputs include:

- **Global SHAP vectors** — system-wide hazard drivers  
- **Local SHAP vectors** — event-level hazard explanations  
- **Driver taxonomies** — narrative-safe hazard factors  
- **JSON-LD bundles** — machine-readable explainability  
- **STAC v11 XAI metadata** — XAI Item extensions  
- **CARE masking** — spatial & semantic protections  

All outputs must be:

- Deterministic  
- PROV-linked  
- H3 generalized  
- Story Node compliant  
- FAIR+CARE governed  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/
    ├── 📄 README.md                       # This file
    │
    ├── 📁 global/                         # Global hazard-driver vectors
    │   ├── 📄 global.json
    │   ├── 📄 summary.md
    │   └── 📁 jsonld/
    │       ├── 📄 xai-shap-global.jsonld
    │       └── 📄 xai-hazard-driver-codes.jsonld
    │
    ├── 📁 local/                          # Local (per-event) hazard explanations
    │   ├── 📄 local.json
    │   ├── 📄 samples.json
    │   └── 📁 jsonld/
    │       ├── 📄 xai-shap-local.jsonld
    │       └── 📄 xai-shap-local-driver-codes.jsonld
    │
    └── 📁 templates/                      # Hazard XAI templates (global + local + narrative)
        ├── 📄 shap-global-template.json
        ├── 📄 shap-local-template.json
        └── 📄 hazard-driver-taxonomy.json

---

## 🔍 Hazard SHAP Components

### 1. 🟥 Global Hazard SHAP Attribution  
Indicates which hazard-related variables most influence model behavior:

- Wind shear, CAPE, CIN  
- Vorticity, helicity, storm-relative winds  
- Vegetation / dryness signals (wildfire)  
- Rainfall intensity, soil moisture, runoff potential (flood)  
- Terrain interaction (valleys, ridges, canyon funnels)  

Outputs:

- `global.json` — raw SHAP vectors  
- `summary.md` — human-readable interpretation  
- `xai-shap-global.jsonld` — semantic global driver bundle  

---

### 2. 🧪 Local Hazard SHAP Attribution  
Per-event hazard explanations including:

- Local feature impacts  
- Positive/negative contributions  
- Confidence intervals  
- Per-hazard-type contextual reasoning  
- CARE/H3 masking for sensitive geographic associations  

Outputs:

- `local.json` — raw per-event SHAP vectors  
- `samples.json` — curated examples  
- `xai-shap-local.jsonld` — semantic local driver evidence  

---

### 3. 🟩 Narrative Hazard Driver Codes  
Maps SHAP features → **narrative-safe hazard drivers**, e.g.:

- `TORNADO_SIGNAL`  
- `HAIL_GROWTH_ENV`  
- `WILDFIRE_FUELS_DRYNESS`  
- `FLOOD_SOIL_SATURATION`  

Encoded in:

- `xai-hazard-driver-codes.jsonld`  
- `xai-shap-local-driver-codes.jsonld`

Used by:

- Story Node v3 hazard narratives  
- Focus Mode v3 hazard reasoning  

---

## 📡 STAC Integration Requirements

All hazard SHAP outputs MUST include:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:{global|local}`  
- `kfm:model_version`  
- `kfm:input_items`  
- Multihash checksums  
- CRS/vertical axis (if spatial)  
- CARE/H3 masking metadata  
- PROV lineage references  

---

## 🧾 PROV-O Lineage Requirements

Each artifact MUST include:

- `prov:wasGeneratedBy` (hazard model pipeline)  
- `prov:used` (STAC hazard/climate inputs)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity)  
- Optional `prov:wasDerivedFrom` (model → XAI → narrative)  

---

## 🔐 FAIR+CARE Requirements

Hazard SHAP outputs MUST:

- Use H3 generalization for sensitive spatial zones  
- Avoid revealing culturally sensitive hazard patterns  
- Obey sovereignty constraints  
- Include CARE scope metadata  
- Avoid speculative causal inferences  

---

## 🧪 Testing Requirements

CI MUST validate:

- Deterministic SHAP values  
- JSON-LD schema correctness  
- STAC-XAI extension compliance  
- CARE masking rules  
- Sovereignty + terrain masking  
- PROV-O lineage completeness  
- Hazard-driver drift stability across versions  

---

## 🕰 Version History

| Version  | Date       | Notes                                                                    |
|----------|------------|--------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard SHAP explainability layer aligned with XAI suite         |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard Explainability](../README.md) · [🧠 AI Pipeline Layer](../../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

