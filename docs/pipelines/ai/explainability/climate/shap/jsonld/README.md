---
title: "🌡️🟥📄 KFM v11.2.2 — Climate SHAP JSON-LD Explainability (Global · Local · Narrative Drivers)"
path: "docs/pipelines/ai/explainability/climate/shap/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Component (JSON-LD Root)"

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
sensitivity: "Explainability-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "shap-jsonld"
  - "global-driver-evidence"
  - "local-driver-evidence"
  - "semantic-driver-maps"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/climate/shap/jsonld"
  applies_to:
    - "xai-shap-global-jsonld"
    - "xai-shap-local-jsonld"
    - "xai-shap-driver-codes"
    - "semantic-taxonomy"
    - "stac-xai"
    - "prov-xai"
    - "care-governance"
    - "h3-masking"
    - "narrative-ready-xai"

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

# 🌡️🟥📄 **Climate SHAP JSON-LD Explainability**  
`docs/pipelines/ai/explainability/climate/shap/jsonld/README.md`

**Purpose:**  
Define the **root JSON-LD explainability layer** for Climate SHAP, governing the structure, semantics, provenance, CARE filtering, and STAC-linkage of global, local, and narrative-ready SHAP drivers used by:

- 🌡️ Climate AI explainability dashboards  
- 🧭 Focus Mode v3 reasoning  
- 📘 Story Node v3 narrative generation  
- 🏛 Governance + FAIR+CARE oversight pipelines  

</div>

---

## 📘 Overview

This directory standardizes:

- Global SHAP JSON-LD bundles (`xai-shap-global.jsonld`)  
- Local SHAP JSON-LD bundles (`xai-shap-local.jsonld`)  
- Narrative-friendly semantic driver code bundles (`xai-shap-driver-codes.jsonld`)  

These assets:

- Transform SHAP feature importance into **machine-readable semantic structures**  
- Apply **FAIR+CARE controls** and **H3-masking**  
- Provide **PROV-O lineage** and STAC v11 integration  
- Feed **Focus Mode v3** + **Story Node v3**  
- Enable full explainability traceability across KFM

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/shap/jsonld/
    ├── 📄 README.md                                # This file
    │
    ├── 📄 xai-shap-global.jsonld                   # Global climate driver bundle
    ├── 📄 xai-shap-local.jsonld                    # Local (per-event) driver bundle
    └── 📄 xai-shap-driver-codes.jsonld             # XAI → Narrative driver mapping

---

## 🔍 Bundle Specifications

### 1. 🟥 Global SHAP JSON-LD (`xai-shap-global.jsonld`)
Represents global climate model behavior:

- Ranked climate drivers  
- Aggregated SHAP global vectors  
- Spatial/temporal abstractions  
- CARE-scope metadata  
- H3-masked location references  
- `prov:*` lineage fields  
- Ties to STAC input datasets  
- `kfm:explainability:global` fields  

Used for:

- Global climate narratives  
- Long-range reasoning windows in Focus Mode v3  
- Drift monitoring  

---

### 2. 🧪 Local SHAP JSON-LD (`xai-shap-local.jsonld`)
Represents event-level or per-inference climate drivers:

- Local SHAP vectors  
- Per-prediction driver semantics  
- Local spatial abstractions  
- CARE masking  
- Full PROV-O lineage  
- `kfm:explainability:local` STAC fields  

Used by:

- Story Node v3 “event representation”  
- Focus Mode v3 local overlays  

---

### 3. 🟩 Driver Codes (`xai-shap-driver-codes.jsonld`)
Provides semantic, governed driver definitions:

- Canonical **climate driver taxonomy**  
- Narrative-safe descriptions  
- CARE-filtered public versions  
- Mappings from raw SHAP → driver codes  
- Story Node v3 semantic roles  
- Focus Mode reasoning categories  
- `prov:wasDerivedFrom` links to global/local bundles  

---

## 📡 STAC Integration Requirements

Each JSON-LD file MUST define:

- `kfm:explainability:method = "shap"`  
- One of:
  - `kfm:explainability:global`  
  - `kfm:explainability:local`  
  - `kfm:explainability:drivers`  
- `kfm:model_version`  
- `kfm:input_items` (array of STAC Item IDs)  
- CRS metadata (if spatial)  
- Multihash checksums  
- CARE metadata  
- PROV-O references  

---

## 🧾 PROV-O Lineage Requirements

Each SHAP JSON-LD bundle must include:

- `prov:wasGeneratedBy` (model + pipeline)  
- `prov:used` (input STAC datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (pipeline + model identity)  
- Optional: `prov:wasDerivedFrom` (model → explainability → narrative)  

---

## 🔐 FAIR+CARE Requirements

All SHAP JSON-LD must:

- Apply **H3 generalization** for sensitive spatial info  
- Remove or abstract culturally sensitive driver connections  
- Include sovereignty indicators  
- Respect CARE restrictions & Data-Contract v3  
- Avoid speculative climate interpretation not grounded in evidence  

---

## 🧪 Testing Requirements

CI must validate:

- JSON-LD schema compliance  
- STAC-XAI field correctness  
- Deterministic regeneration  
- CARE mask alignment  
- PROV-O correctness  
- Driver drift stability  
- Sovereignty rule enforcement  

PRs failing tests → **blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                               |
|----------|------------|---------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate SHAP JSON-LD explainability layer aligned with suite |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate SHAP](../README.md) · [🌡️ Climate XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

