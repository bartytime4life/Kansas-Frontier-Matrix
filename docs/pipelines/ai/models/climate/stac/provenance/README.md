---
title: "📜🌐🌡️ KFM v11.2.2 — Climate STAC Provenance Catalog (PROV-O 🧬 · Lineage Integrity 🔐 · FAIR+CARE 🛡️ · Sovereignty ⚖️)"
path: "docs/pipelines/ai/models/climate/stac/provenance/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Data Working Group 🌡️📊 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Climate STAC · Provenance Catalog 📜"

commit_sha: "<latest-commit-sha>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/climate-stac-provenance.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-climate-stac-provenance-v11.2.2.json"
energy_schema: "../../../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../../contracts/data-contract-v3.json"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · High-Risk (Lineage Metadata)"
sensitivity: "Climate-STAC-Provenance"
sensitivity_level: "High"
public_exposure_risk: "Medium"
immutability_status: "version-pinned"

semantic_intent:
  - "climate-provenance"
  - "prov-o"
  - "stac-lineage"
  - "model-lineage"
  - "deterministic-traceability"
  - "sovereignty-compliance"
  - "faircare-governance"
  - "xai-provenance"
  - "telemetry-linkage"

scope:
  domain: "pipelines/ai/models/climate/stac/provenance"
  applies_to:
    - "README.md"
    - "prov-model_v11.2.2.json"
    - "../items/*"
    - "../collections/*"
    - "../../mlops/*"
    - "../../../inference/climate/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_purpose_block: true
requires_governance_links_in_footer: true
requires_version_history: true
diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 📜🌐🌡️ **Climate STAC Provenance Catalog — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/climate/stac/provenance/README.md`

**Purpose**  
Define the **PROV-O lineage system** for Climate STAC Collections and Items.  
This governs **traceability**, **model accountability**, **training-data lineage**,  
**XAI provenance**, **MLOps audit chains**, and **sovereignty-aware metadata paths**,  
ensuring *every climate model artifact* is reconstructible, reversible, and governance-safe.

</div>

---

## 📘📜🌡️ **Overview — Why Provenance?**

Every climate model version depends on:

- Training datasets (ERA5, NARR, HRRR, NLDAS)  
- Preprocessing pipelines  
- Downscaling architectures  
- Driver models (CAPE, CIN, shear, LLJ)  
- Bias-correction workflows  
- Anomaly pipelines  
- XAI explainability artifacts  
- Sustainability telemetry  
- Sovereignty screening logic  

PROV-O lineage guarantees:

- Deterministic reconstruction of any model version  
- Governance oversight & safety reviews  
- FAIR+CARE compliance  
- Ancestry tracking for model families  
- Transparent cross-pipeline dependency modeling  
- Inputs → transformations → outputs → metadata  

---

## 🗂️📁📜 **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/climate/stac/provenance/
    📄 README.md                       # ← This file
    📄 prov-model_v11.2.2.json         # PROV-O lineage example for a model
    📄 prov-model_v11.2.1.json
    📄 prov-downscaling-template.json  # Template PROV structure for new models
    📄 prov-driver-template.json       # Template for CAPE/CIN/shear/LLJ models
    📄 prov-biascorr-template.json     # Template for bias-correction models
    📄 prov-anomaly-template.json      # Template for anomaly models
```

---

## 🧬📜🔐 **Provenance Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[📥 STAC Item] --> B[📜 PROV-O Activity Block]
    B --> C[🧬 Inputs: Training Data + Drivers + Pipelines]
    C --> D[⚙️ Transformations: Training Downscaling BiasCorr Anomaly]
    D --> E[📦 Outputs: Model Weights XAI Telemetry]
    E --> F[🛡️ CARE + Sovereignty Metadata]
    F --> G[🌐 Write STAC Item With Provenance]
```

---

## 📜🧬🌡️ **Required PROV-O Fields**

Each STAC Item MUST include:

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:training:climate_downscaler_v11_2_2",
    "used": [
      "urn:kfm:data:stac:era5_item",
      "urn:kfm:data:stac:terrain",
      "urn:kfm:model:climate_drivers_v11_2_1"
    ],
    "agent": "urn:kfm:service:climate-training-engine"
  }
}
```

Additional mandatory blocks:

### ✔ `prov:used`  
Includes all upstream sources:

- Climate drivers  
- Terrain  
- Preprocessing pipelines  
- Hydrology coupling layers  
- Bias-correction assets  
- XAI templates  

### ✔ `prov:wasGeneratedBy`  
Describes training or model-building activity.

### ✔ `prov:wasAssociatedWith`  
Climate MLOps service agent.

### ✔ Deterministic seeds  
Always included in `properties.model:seed`.

---

## 🧠💡📊 **XAI Provenance Requirements**

Every XAI output MUST have:

```json
{
  "xai:prov": {
    "wasGeneratedBy": "urn:kfm:activity:xai:climate_v11_2_2",
    "used": [
      "weights.pt",
      "normalization.json",
      "driver_inputs.json"
    ],
    "agent": "urn:kfm:service:climate-xai-engine"
  }
}
```

XAI provenance links **attribution maps → model parameters → training inputs**.

---

## 🔋🌍📡 **Telemetry Provenance Integration**

Telemetry artifacts MUST include PROV links:

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:telemetry:run",
    "used": ["model.pt", "stac_item.json"],
    "agent": "urn:kfm:service:climate-telemetry-engine"
  }
}
```

Energy & carbon metrics MUST be tied to activity IDs.

---

## 🛡️⚖️🧭 **FAIR+CARE & Sovereignty Provenance**

Provenance MUST track:

- Sovereignty-driven masking  
- CARE transformation stages  
- H3 downsampling in sensitive areas  
- Hazard suppression logic  
- Cultural-site redaction  

Example:

```json
{
  "care": {
    "masking": "h3-climate-generalized",
    "scope": "public-generalized",
    "notes": ["Sovereignty protections applied during training and STAC assembly"]
  }
}
```

---

## 📦📜🧾 **Provenance Templates Provided**

Templates MUST exist for:

- Downscaling models  
- Driver models  
- Bias correction  
- Anomaly detection  
- Climate embeddings coupling  

These templates ensure deterministic, CI-safe PROV creation.

---

## 🧪📏🔬 **CI Validation Requirements**

CI MUST verify:

- PROV-O schema validity  
- All upstream dependencies included  
- Deterministic ordering of `prov:used`  
- Sovereignty metadata present  
- CARE metadata valid  
- STAC–PROV cross-links intact  
- Activity → agent → entity chains complete  
- No sensitive-site leakage  

Failure → ❌ CI BLOCK.

---

## 🕰️📜 **Version History**

| Version | Date       | Notes                                             |
|---------|------------|---------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Climate STAC Provenance Catalog (MAX MODE) |

---

<div align="center">

### 🔗 Footer  
[🌡️ Back to Climate STAC Catalog](../README.md) ·  
[📜 STAC Items](../items/) ·  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

