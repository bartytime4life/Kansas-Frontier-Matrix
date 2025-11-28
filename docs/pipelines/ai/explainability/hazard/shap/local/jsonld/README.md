---
title: "⚡🟥📄 KFM v11.2.2 — Hazard SHAP Local JSON-LD Explainability (Event Drivers · Semantic Mapping · PROV-O)"
path: "docs/pipelines/ai/explainability/hazard/shap/local/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (Hazard SHAP Local JSON-LD)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/hazard-explainability-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-explainability-hazard-v11.2.2.json"
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
sensitivity: "Explainability-Hazard-Local-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-shap-local-jsonld"
  - "event-hazard-drivers"
  - "per-prediction-attribution"
  - "semantic-driver-mapping"
  - "story-node-hazard"
  - "focus-mode-hazard"
  - "prov-xai"
  - "stac-xai"

scope:
  domain: "explainability/hazard/shap/local/jsonld"
  applies_to:
    - "local-hazard-driver-jsonld"
    - "local-driver-codes-jsonld"
    - "care-governance"
    - "prov-xai"
    - "stac-xai"
    - "h3-masking"
    - "narrative-driver-mapping"

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

# ⚡🟥📄 **Hazard SHAP — Local JSON-LD Explainability**  
`docs/pipelines/ai/explainability/hazard/shap/local/jsonld/README.md`

**Purpose:**  
Provide the **JSON-LD semantic explainability layer** for **event-level hazard SHAP** drivers.  
These bundles power:

- ⚡ Hazard Story Node v3  
- 🧭 Focus Mode v3 local hazard reasoning  
- 🗺️ Hazard spatial overlays  
- 🏛 Governance + audit dashboards  
- 🔍 Deterministic traceability of hazard-model behavior

</div>

---

## 📘 Overview

Local SHAP JSON-LD for hazards expresses:

- Per-event feature-importance vectors  
- Local hazard-driver semantics (tornado, hail, flood, wildfire, wind, multi-hazard)  
- CARE-masked spatial & semantic context  
- PROV-O lineage  
- STAC v11 XAI metadata  
- Narrative-ready driver mappings  

Events covered include:

- Tornadic rotation / SRH / EHI / shear-driven signals  
- Severe storm growth (CAPE, lapse rates)  
- Hail microphysics & hail-growth environments  
- Wildfire ignition/spread drivers (fuel dryness, VPD, wind alignment)  
- Flood/flash-flood conditions (soil saturation, precip intensity, runoff index)  

All JSON-LD MUST be deterministic, schema-validated, and sovereignty-compliant.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/shap/local/jsonld/
    ├── 📄 README.md                                # This file
    │
    ├── 📄 xai-shap-local.jsonld                    # Event-level semantic explainability bundle
    └── 📄 xai-shap-local-driver-codes.jsonld       # Narrative-safe hazard driver taxonomy

---

## 🔍 JSON-LD Bundle Specifications

### 1. 🟥 `xai-shap-local.jsonld` — Local Hazard Driver Evidence  
Required fields:

- `@context` — KFM-XAI + PROV-O  
- `xai:event_id` — event or inference identifier  
- `xai:hazard_type` — tornado | hail | wind | wildfire | flood | multi-hazard  
- `xai:drivers` — local driver contribution list:
  - feature name  
  - contribution magnitude  
  - direction (positive/negative influence)  
  - uncertainty (optional)  
- `xai:spatial_context` — **H3-generalized** location abstraction  
- `care:scope` — CARE category + region restrictions  
- `prov:*` — lineage (model, data, agent, timestamp)  
- `kfm:model_version`  
- `kfm:input_items` — STAC Items used in inference  
- `checksum:multihash`  

Used for:

- Story Node v3 hazard narratives  
- Focus Mode v3 local reasoning  
- Explainability dashboards  

---

### 2. 🟩 `xai-shap-local-driver-codes.jsonld` — Narrative Hazard Driver Codes  
Maps raw SHAP features → **semantic hazard drivers** and narrative roles.

Must include:

- `xai:driver_code` — canonical hazard-driver taxonomy  
- `xai:description` — CARE-filtered, narrative-safe  
- `xai:linked_features` — features behind the driver  
- `xai:hazard_domain` — tornado|hail|wildfire|wind|flood|multi  
- `xai:focus_mode_tags`  
- `xai:story_node_roles` (primary driver, secondary driver)  
- `xai:care_annotations`  
- `prov:wasDerivedFrom` → `xai-shap-local.jsonld`  

Examples:

- `TORNADO_SIGNAL_LOCAL`  
- `HAIL_GROWTH_ENV_LOCAL`  
- `WIND_GUST_DRIVERS_LOCAL`  
- `FLASHFLOOD_SOIL_SATURATION_LOCAL`  
- `WILDFIRE_FUEL_DRYNESS_LOCAL`  

---

## 📡 STAC Integration Requirements

Each JSON-LD hazard local bundle MUST include:

- `kfm:explainability:method = "shap"`  
- `kfm:explainability:local`  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata if spatial context provided  
- CARE & sovereignty metadata  
- PROV-O lineage fields  

---

## 🧾 PROV-O Lineage Requirements

Every hazard SHAP local JSON-LD asset MUST provide:

- `prov:wasGeneratedBy` — hazard model pipeline  
- `prov:used` — STAC hazard + climate datasets  
- `prov:generatedAtTime`  
- `prov:Agent` — model + pipeline identity  
- Optional:
  - `prov:wasDerivedFrom` — local→global→narrative chain  

These lineage structures are required for:

- Governance dashboards  
- Story Node v3 provenance  
- Focus Mode hazard backtracking  

---

## 🔐 FAIR+CARE Requirements

Hazard SHAP JSON-LD MUST:

- Apply **H3 generalization** for location  
- Mask/remove culturally sensitive hazard-relevant contexts  
- Include sovereignty metadata  
- Respect Data Contract v3 + hazard-focused CARE constraints  
- Avoid speculative causal hazard claims  
- Use narrative-safe, governance-reviewed driver terms  

---

## 🧪 Testing Requirements

CI MUST validate:

- JSON-LD schema validity  
- STAC-XAI extension correctness  
- Deterministic regeneration  
- CARE & sovereignty masking  
- Driver taxonomy linkage  
- PROV-O lineage completeness  
- Hazard-driver drift stability  

Any failure automatically blocks merge.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                  |
|----------|------------|------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard SHAP Local JSON-LD explainability spec aligned with suite |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard SHAP Local](../README.md) · [⚡ Hazard XAI Root](../../../README.md) · [🏛 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

