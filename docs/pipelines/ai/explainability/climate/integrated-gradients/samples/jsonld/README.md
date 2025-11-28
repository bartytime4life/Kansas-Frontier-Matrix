---
title: "🌡️🟩📄 KFM v11.2.2 — Climate Integrated Gradients: Local JSON-LD Explainability Bundles"
path: "docs/pipelines/ai/explainability/climate/integrated-gradients/samples/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Local IG JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-explainability-climate-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../../../contracts/data-contract-v3.json"

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
  - "local-ig-jsonld"
  - "climate-xai"
  - "sample-level-attribution"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/climate/integrated-gradients/samples/jsonld"
  applies_to:
    - "xai-ig-local-jsonld"
    - "xai-ig-local-driver-codes-jsonld"
    - "stac-xai"
    - "prov-xai"
    - "faircare-governance"
    - "h3-masking"

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

# 🌡️🟩📄 **Climate Local Integrated Gradients — JSON-LD Bundles**  
`docs/pipelines/ai/explainability/climate/integrated-gradients/samples/jsonld/README.md`

**Purpose:**  
Define the **local/sample-level Integrated Gradients (IG) JSON-LD explainability bundles** for climate models — encoding per-event gradient attribution, sample metadata, CARE-masked spatial context, and narrative-ready driver mappings used by **Story Node v3**, **Focus Mode v3**, and governance systems.

</div>

---

## 📘 Overview

This directory contains the **JSON-LD serialization** of local IG explainability:

- Per-sample gradient attribution (what drove this prediction?)  
- Local climate variable drivers (e.g., temperature, precip, wind, terrain)  
- CARE-masked spatial & semantic context  
- STAC-linked input datasets  
- PROV-O lineage for each explanation  
- Narrative-ready driver codes for Story Node v3 & Focus Mode v3  

These bundles are:

- Deterministic (same inputs → same JSON-LD)  
- Fully schema-validated  
- FAIR+CARE-governed  
- Integrated into STAC v11 & KFM-XAI extensions  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/integrated-gradients/samples/jsonld/
    ├── 📄 README.md                               # This file
    │
    ├── 📄 xai-ig-local.jsonld                     # Local IG JSON-LD evidence bundle
    └── 📄 xai-ig-local-driver-codes.jsonld        # Narrative-ready driver-code mapping

---

## 🔍 Bundle Specifications

### 1. 🟦 `xai-ig-local.jsonld` — Local IG Evidence

Represents **one or more sample-level IG explanations**:

- `@context` — KFM XAI and PROV-O vocabularies  
- `xai:sample_id` — unique sample identifier  
- `xai:drivers` — list of driver objects:
  - Feature name / climate variable  
  - Local IG importance  
  - Confidence / robustness indicators  
- `xai:spatial_context` (optional):
  - H3 generalized geometry or region label  
  - CRS info if needed  
- `prov:used` — input STAC Items (climate datasets)  
- `prov:wasGeneratedBy` — model + inference pipeline  
- `prov:generatedAtTime` — ISO 8601 timestamp  
- `care:scope` — CARE context + sensitivity level  

Used by:

- Story Node v3 event narratives  
- Focus Mode v3 “local reasoning windows”  
- XAI dashboards & audits  

---

### 2. 🟩 `xai-ig-local-driver-codes.jsonld` — Driver Mapping

Maps *raw* IG drivers → **semantic driver codes**, containing:

- `xai:driver_code` — canonical code (e.g., `TEMP_MAX`, `PRECIP_EXTREME`)  
- `xai:description` — narrative-safe description  
- `xai:linked_features` — underlying model features  
- `xai:care_annotations` — notes on CARE relevance/masking  
- `xai:story_node_roles` — how drivers may appear in narratives  

Used to:

- Translate technical IG values into **human-readable Story Node phrases**  
- Provide Focus Mode with more compact reasoning labels  
- Support FAIR+CARE review of narrative exposure  

---

## 📡 STAC Integration Requirements

Local IG JSON-LD assets MUST be referenced by their parent STAC Items using:

- `kfm:explainability:method = "integrated-gradients"`  
- `kfm:explainability:local` → URI + checksum to `xai-ig-local.jsonld`  
- Optional:
  - `kfm:explainability:driver_codes` → URI to `xai-ig-local-driver-codes.jsonld`  

Also required:

- `kfm:model_version`  
- `kfm:input_items` (array of STAC IDs)  
- `checksum:multihash` for JSON-LD assets  

---

## 🧾 PROV-O Lineage Requirements

Each bundle MUST satisfy:

- `prov:wasGeneratedBy` — climate model inference run  
- `prov:used` — climate STAC datasets (Collections/Items)  
- `prov:Agent` — model + pipeline identity  
- `prov:generatedAtTime` — explanation generation time  

These documents are ingested into:

- KFM lineage graph  
- Governance dashboards  
- Story Node provenance graphs  

---

## 🔐 FAIR+CARE Requirements

Local IG JSON-LD MUST:

- Use **H3 generalization** for any spatial references tied to sensitive areas  
- Mask or abstract climate drivers that reveal protected knowledge  
- Include `care:scope` and sovereignty indicators  
- Avoid speculative cause–effect claims in descriptions  
- Obey dataset-level governance from `data_contract_ref`  

---

## 🧪 Testing Requirements

CI tests for this directory MUST:

- Validate JSON-LD structure against XAI & PROV-O schemas  
- Check for presence of required KFM XAI fields (`kfm:explainability:*`)  
- Validate STAC extension compatibility for references  
- Assert deterministic generation across runs (hash stability)  
- Validate `care:*` + sovereignty fields for presence & correctness  

Any failing test → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                |
|----------|------------|----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Local IG JSON-LD explainability spec                 |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Local IG Samples](../README.md) · [🌡️ Climate XAI Root](../../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

