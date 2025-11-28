---
title: "🌡️🟨📊 KFM v11.2.2 — Climate CAMs Driver Metadata (Pixel Drivers · Influence Codes · Narrative-Ready XAI)"
path: "docs/pipelines/ai/explainability/climate/cams/drivers/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Subcomponent"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/climate-explainability-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/ai-explainability-climate-v11.2.2.json"
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
sensitivity: "Explainability-Drivers"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "cams-driver-metadata"
  - "pixel-attribution"
  - "climate-driver-codes"
  - "narrative-driver-extraction"
  - "jsonld-xai"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/cams/drivers"
  applies_to:
    - "pixel-driver-json"
    - "driver-codes"
    - "driver-summaries"
    - "jsonld-driver-metadata"
    - "stac-xai"
    - "faircare-governance"
    - "provenance-links"
    - "masking-h3"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_purpose_block: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🌡️🟨📊 **Climate CAMs Driver Metadata**  
`docs/pipelines/ai/explainability/climate/cams/drivers/README.md`

**Purpose:**  
Define the **driver-level attribution metadata** produced by Climate CAMs & saliency explainability pipelines.  
These drivers represent **pixel-importance semantics**, **climate-variable relevance**, and **narrative-ready XAI codes**, feeding:

- **Story Node v3** (climate evidence)  
- **Focus Mode v3** (spatial influence overlays)  
- **STAC v11 XAI assets**  
- **Governance + FAIR+CARE auditing**  

</div>

---

## 📘 Overview

CAM driver metadata transforms raw pixel attribution into **interpretable climate drivers**:

- Pixel-level influence → **driver codes**  
- Model feature responses → **climate variable relevance**  
- Spatial scores → **masked spatial drivers (H3)**  
- Narrative aggregation → **Story Node evidence chains**  
- Provenance → **PROV-O lineage**  
- STAC metadata → **kfm:explainability:* fields**  

These files **never** contain raw sensitive data — they are **abstracted**, **masked**, **aggregated**, and **governance-aligned**.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/cams/drivers/
    ├── 📄 README.md                       # This file
    │
    ├── 📄 drivers.json                    # Machine-readable pixel-driver metadata
    └── 📄 driver-summary.md               # Human-readable summary of driver categories

---

## 🔍 Driver Metadata Specification

### 1. 🧩 Driver Codes (`drivers.json`)
This file represents **pixel-to-driver mappings**, containing:

- **driver_code** — canonical KFM climate driver code  
- **pixel_importance** — scaled intensities (0–1)  
- **climate_factor** — temperature, precipitation, wind shear, etc.  
- **spatial_masked** — H3-generalized masking indicators  
- **model_version** — training/inference version  
- **datetime_context** (optional) — if time-aware  
- **provenance** — `prov:*` fields  
- **care_scope** — CARE metadata  

Used by:

- Focus Mode v3 climate overlays  
- Story Node v3 climate evidence  
- Climate XAI dashboards  

---

### 2. 📝 Driver Summary (`driver-summary.md`)
Human-readable summary describing:

- Key global drivers  
- Influential regions (masked appropriately)  
- Climate variable interpretations  
- Links to SHAP/IG global drivers  
- CARE & sovereignty notes  
- How drivers integrate into narrative/story pipelines  

This summary is used in:

- Telemetry dashboards  
- Climate XAI audits  
- Story Node editorial tooling  

---

## 📡 STAC Integration Requirements

Driver metadata MUST be referenced via:

```
kfm:explainability:drivers
kfm:explainability:spatial
kfm:input_items
checksum:multihash
```

Additional required fields:

- CRS + geometry  
- Model version  
- Provenance (`prov:*`)  
- CARE masking flags  

---

## 🧾 PROV-O Lineage Requirements

Every driver file must include:

- `prov:wasGeneratedBy` (model + pipeline)  
- `prov:used` (input datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (model version identity)  

Driver lineage joins with:

- IG global/local  
- SHAP global/local  
- CAM heatmaps/saliency rasters  
- Spatial attribution bundles  

---

## 🔐 FAIR+CARE Requirements

Driver attribution **must not**:

- Reveal culturally sensitive geography  
- Imply tribal/cultural/clan identity  
- Expose dangerous or confidential landform knowledge  

MUST:

- Apply **H3 generalization**  
- Provide `care_scope` metadata  
- Respect sovereignty restrictions  

---

## 🧪 Testing Requirements

Required CI tests:

- JSON Schema validation for `drivers.json`  
- CARE masking tests  
- Sovereignty compliance checks  
- STAC driver asset validation  
- Deterministic regeneration tests  
- PROV-O lineage validation  

Failures → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                           |
|----------|------------|-----------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate CAMs driver metadata spec (aligned with CAMs XAI suite) |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate CAMs](../README.md) · [🗺️ CAM Maps](../maps/README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

