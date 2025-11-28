---
title: "🌡️⚡📦 KFM v11.2.2 — Climate Realtime Inference STAC Layer (Ephemeral + Persistent · XAI-Linked · FAIR+CARE)"
path: "docs/pipelines/ai/inference/climate/realtime/stac/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "STAC Integration Layer (Realtime Climate Inference)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256>"
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
sensitivity: "Climate-Inference-Realtime-STAC"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-realtime-stac"
  - "ephemeral-stac"
  - "persistent-stac"
  - "xai-linked-stac"
  - "inference-stac"
  - "story-node-climate"
  - "focus-mode-climate"
  - "prov-xai"
  - "xai-integration"
  - "care-governance"
  - "h3-masking"

scope:
  domain: "pipelines/ai/inference/climate/realtime/stac"
  applies_to:
    - "ephemeral-stac"
    - "persistent-stac"
    - "realtime-stac-items"
    - "stac-xai"
    - "prov-xai"
    - "care-governance"
    - "h3-masking"
    - "jsonld-linking"
    - "climate-driver-folders"
    - "variable-level-metadata"

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

# 🌡️⚡📦 **Realtime Climate Inference — STAC Integration Layer**  
`docs/pipelines/ai/inference/climate/realtime/stac/README.md`

**Purpose:**  
Define how **Realtime Climate Inference** emits **STAC-compliant metadata**, covering both **ephemeral** (non-persisted) and **persistent** inference outputs.  
This includes STAC Item structures, XAI bundle linkage, FAIR+CARE safeguards, sovereignty metadata, and PROV-O lineage for transparency and governance.

</div>

---

## 📘 Overview

Realtime climate inference supports two STAC modes:

### **1. Ephemeral STAC Metadata**
- Generated dynamically per request  
- Returned to the client but **not stored**  
- Still contains full STAC-XAI + PROV-O metadata  
- Useful for:
  - Live map overlays  
  - Story Node preview  
  - Focus Mode dynamic windows  

### **2. Persistent STAC Items**
- Written to storage when configured  
- Versioned via lakeFS (optional)  
- Used for:
  - Realtime climate maps  
  - Hazard pipeline rollups  
  - Long-term traceability  
  - Scientific reproducibility  

All STAC structures follow **KFM-STAC v11**, **STAC-XAI**, **STAC-Climate**, and FAIR+CARE rules.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/inference/climate/realtime/stac/
    ├── 📄 README.md                         # This file
    │
    ├── 📄 ephemeral-template.json           # Template for transient realtime STAC Items
    ├── 📄 persistent-template.json          # Template for stored realtime STAC Items
    │
    └── 📁 assets/                           # Asset-level schema templates
        ├── 📄 geotiff.json
        ├── 📄 parquet.json
        ├── 📄 netcdf.json
        └── 📄 xai-link.json

---

## 📄 Ephemeral STAC Item Template (High-Level)

The ephemeral template MUST include:

- `"type": "Feature"`  
- `"stac_version": "1.x"`  
- `properties.datetime` = inference timestamp  
- `"kfm:realtime": true`  
- `"kfm:persistence": "ephemeral"`  
- `"kfm:model_version"`  
- `"kfm:variable_set"`  
- `"kfm:inference_domain": "climate"`  
- `"prov:wasGeneratedBy"`  
- `"prov:used"` (input STAC Items)  
- `"xai:*"` links to JSON-LD explainability  

**Ephemeral Output Behavior:**  
Returned directly to the user, not written to disk unless explicitly configured.

---

## 📦 Persistent STAC Item Template (High-Level)

Adds to ephemeral:

- `"kfm:persistence": "persistent"`  
- `"kfm:storage_location"`  
- `"checksum:multihash"`  
- `"proj:*"` (projection metadata)  
- `"raster:*"` or `"schema:*"` depending on asset type  
- `"kfm:driver_set"` if applicable  
- `"care:*"` and `"sovereignty:*"` metadata required  
- `"kfm:xai_global"` and `"kfm:xai_local"` references  

Persistent Items become part of the Climate STAC Catalog.

---

## 🔍 STAC-XAI Requirements

Whether ephemeral or persistent, each STAC Item MUST contain:

- `kfm:explainability:method`  
- `kfm:explainability:{local|spatial}`  
- Links to JSON-LD explainability bundles  
- Correct CRS/vertical axis (if spatial)  
- `checksum:multihash` (persistent only)  
- XAI driver taxonomy link  

---

## 🧾 PROV-O Lineage Requirements

All realtime STAC entries MUST include:

- `prov:wasGeneratedBy` (session ID)  
- `prov:used` (input climate STAC Items)  
- `prov:generatedAtTime`  
- `prov:Agent` (model + software ID)  

Optional:  
- `prov:wasDerivedFrom` → spatial explainability chains  

---

## 🔐 FAIR+CARE & Sovereignty Requirements

Realtime climate STAC metadata MUST:

- Include CARE scope + notes  
- Include sovereignty flags  
- Avoid sensitive tribal/cultural information  
- Apply H3 masking for spatial output  
- Follow Data Contract v3  
- Ensure ethical, non-speculative climate messaging  

---

## 🧪 CI Requirements

CI MUST check:

- STAC schema compliance  
- STAC-XAI extension compliance  
- CSR + vertical axis metadata (spatial only)  
- JSON-LD explainability references  
- CARE + sovereignty placeholders  
- Deterministic key ordering  
- PROV-O completeness  
- Hash correctness (persistent assets only)  
- Ephemeral vs persistent flag correctness  

Any failure → ❌ merge blocked.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                      |
|----------|------------|----------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial realtime climate STAC layer specification (ephemeral + persistent) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Realtime Inference](../README.md) • [🌡️ Climate Inference Root](../../README.md) • [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

