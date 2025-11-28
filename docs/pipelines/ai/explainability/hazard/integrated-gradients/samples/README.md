---
title: "⚡🟩🧪 KFM v11.2.2 — Hazard Integrated Gradients: Local / Sample-Level Explainability (Event Drivers · Gradient Maps)"
path: "docs/pipelines/ai/explainability/hazard/integrated-gradients/samples/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Hazard IG Local)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
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
sensitivity: "Explainability-Hazard-Local-IG"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-ig-local"
  - "sample-level-hazard-explainability"
  - "gradient-attribution"
  - "event-driver-analysis"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/hazard/integrated-gradients/samples"
  applies_to:
    - "ig-local"
    - "sample-level-attribution"
    - "hazard-ig-jsonld"
    - "hazard-driver-codes"
    - "care-governance"
    - "h3-masking"
    - "prov-xai"
    - "stac-xai"

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

# ⚡🟩🧪 **Hazard Integrated Gradients — Sample-Level Explainability**  
`docs/pipelines/ai/explainability/hazard/integrated-gradients/samples/README.md`

**Purpose:**  
Define the **event-level Integrated Gradients (IG)** explainability subsystem for hazard models, generating per-prediction gradient evidence, spatially masked driver maps, semantic JSON-LD bundles, and narrative-ready driver summaries powering:

- ⚡ Hazard Story Node v3  
- 🧭 Focus Mode v3 hazard reasoning  
- 🗺️ Hazard map overlays & dashboards  
- 🏛 FAIR+CARE governance workflows  

</div>

---

## 📘 Overview

Sample-level (local) IG attribution reveals:

- Why a deep hazard model predicted a tornado, hail event, wind gust, flood, or wildfire condition  
- Which meteorological / hydrologic / terrain / fuel variables contributed most  
- What spatial or vertical gradients influenced an event  
- How multi-hazard interactions appeared for the specific sample  

This directory contains:

- **Raw local IG contributions**
- **Metadata describing sample context**
- **JSON-LD semantic bundles**
- **Narrative-friendly hazard driver mappings**

All outputs MUST be:

- Deterministic  
- FAIR+CARE + sovereignty compliant  
- H3-generalized for spatial content  
- PROV-linked  
- STAC-XAI conformant  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/integrated-gradients/samples/
    ├── 📄 README.md                              # This file
    │
    ├── 📄 ig-samples.json                        # Raw per-sample IG vectors/maps
    ├── 📄 sample-metadata.json                   # CRS, vertical, hazard-domain, CARE scope
    │
    └── 📁 jsonld/                                # JSON-LD semantic bundles
        ├── 📄 xai-ig-local.jsonld                # Local IG driver evidence (semantic)
        └── 📄 xai-hazard-ig-local-driver-codes.jsonld  # Narrative-safe driver taxonomy

---

## 🔍 Local IG Explainability Components

### 1. 🟥 `ig-samples.json` — Raw Local IG Vectors  
Must include:

- Gradient magnitudes per feature  
- Directional influence (if supported by model)  
- Hazard domain (tornado|hail|wind|wildfire|flood|multi)  
- CARE-masking flags  
- Deterministic, sorted key ordering  
- Checksums for reproducibility  
- Optional spatial grid representations (masked with H3)  

---

### 2. 🧾 `sample-metadata.json`  
Contains supporting metadata:

- Spatial context (H3 generalized only)  
- Timestep & event metadata  
- Model version & pipeline version  
- CRS + vertical axis if spatial  
- CARE scope + sovereignty indicators  
- STAC input dataset references  
- Provenance markers  

Used for governance review & traceability.

---

### 3. 🟩 JSON-LD Bundles (`/jsonld/`)

#### **`xai-ig-local.jsonld`**
Semantic evidence bundle for a single hazard event:

- `@context` (KFM-XAI + PROV-O)  
- `xai:event_id`  
- `xai:hazard_domain`  
- `xai:drivers` (gradient → driver mapping)  
- `xai:spatial_context` (H3)  
- CARE scope  
- PROV lineage  
- STAC-XAI fields:
  - `kfm:model_version`
  - `kfm:input_items`
  - `checksum:multihash`

#### **`xai-hazard-ig-local-driver-codes.jsonld`**
Narrative-safe driver taxonomy for local IG:

- Driver codes (e.g., `TORNADO_SIGNAL_IG_LOCAL`)  
- CARE-filtered descriptions  
- Feature linkage  
- Story Node roles  
- Focus Mode relevance tags  
- PROV linkage  

---

## 📡 STAC-XAI Integration Requirements

Local IG hazard explainability MUST define:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items`  
- Spatial metadata (if spatial)  
- `checksum:multihash`  
- CARE + sovereignty fields  

---

## 🧾 PROV-O Lineage Requirements

Each semantic bundle MUST include:

- `prov:wasGeneratedBy` (hazard IG inference run)  
- `prov:used` (STAC hazard + climate data)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity / executor)  
- Optional narrative linkage:
  - `prov:wasDerivedFrom` → global IG bundle or SHAP bundle  

---

## 🔐 FAIR+CARE Requirements

Local IG hazard explainability MUST:

- Apply H3-based spatial generalization  
- Mask or abstract culturally sensitive hazard regions  
- Include CARE scope + sovereignty metadata  
- Avoid conjecture about cause-and-effect  
- Respect Data Contract v3 and Natural Hazard Ethics guidance  
- Use governance-approved, narrative-safe terminology  

---

## 🧪 Testing Requirements

CI MUST validate:

- Deterministic IG sample outputs  
- JSON-LD schema correctness  
- STAC-XAI extension compliance  
- CARE + sovereignty masking  
- CRS + vertical axis metadata (if spatial)  
- Drift baseline stability  
- PROV-O lineage correctness  
- Driver taxonomy completeness  

Failure → **merge blocked**.

---

## 🕰 Version History

| Version | Date       | Notes                                                                     |
|---------|------------|---------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Hazard Local IG explainability specification, matching XAI suite |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard IG](../README.md) · [⚡ Hazard XAI Root](../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

