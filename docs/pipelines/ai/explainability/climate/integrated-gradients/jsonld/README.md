---
title: "🌡️🟩📄 KFM v11.2.2 — Climate Integrated Gradients JSON-LD Explainability Bundles (Global · Local · Spatial Drivers)"
path: "docs/pipelines/ai/explainability/climate/integrated-gradients/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Subcomponent (JSON-LD)"

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
sensitivity: "Explainability-JSONLD"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "integrated-gradients-jsonld"
  - "climate-xai"
  - "global-driver-bundles"
  - "local-driver-bundles"
  - "spatial-driver-bundles"
  - "prov-xai"
  - "stac-xai"
  - "story-node-xai"
  - "focus-mode-xai"

scope:
  domain: "explainability/climate/integrated-gradients/jsonld"
  applies_to:
    - "xai-ig-global-jsonld"
    - "xai-ig-local-jsonld"
    - "xai-ig-spatial-jsonld"
    - "story-node-xai"
    - "focus-mode-xai"
    - "stac-xai"
    - "prov-xai"
    - "care-governance"
    - "h3-masking"

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

# 🌡️🟩📄 **Climate Integrated Gradients — JSON-LD Explainability Bundles**  
`docs/pipelines/ai/explainability/climate/integrated-gradients/jsonld/README.md`

**Purpose:**  
Define the **JSON-LD explainability bundle formats** for Climate Integrated Gradients (IG) — including **global**, **local**, and **spatial** gradient-driven climate drivers — providing deterministic, FAIR+CARE-aligned, PROV-linked, STAC-ready explainability artifacts for KFM v11.2.2.

</div>

---

## 📘 Overview

Integrated Gradients (IG) JSON-LD bundles formalize gradient-based climate explainability into:

- **Global driver evidence** (system-level climate drivers)  
- **Local driver evidence** (per-event gradient attribution)  
- **Spatial driver abstractions** (if applicable)  
- **FAIR+CARE-filtered semantic structures**  
- **PROV-O lineage chains**  
- **STAC v11 XAI metadata**  
- **Story Node v3 & Focus Mode v3 reasoning inputs**

These files form the **semantic layer** bridging deep-model IG outputs → narrative reasoning → governance transparency.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/integrated-gradients/jsonld/
    ├── 📄 README.md                         # This file
    │
    ├── 📄 xai-ig-global.jsonld              # Global IG JSON-LD evidence bundle
    ├── 📄 xai-ig-local.jsonld               # Local IG JSON-LD evidence bundle
    └── 📄 xai-ig-spatial.jsonld             # Optional: spatial attribution driver bundle

---

## 🔍 JSON-LD Bundle Specifications

### 1. 🟥 Global JSON-LD (`xai-ig-global.jsonld`)
Represents **model-wide climate drivers**:

- Aggregated IG attributions  
- Ranked climate variables (temperature, precip, winds, humidity, terrain interactions)  
- Spatially aggregated relevance scores  
- CARE-masked summaries  
- Model + inference version metadata  
- `prov:*` lineage fields  
- `kfm:explainability:global` STAC linkage  

Used by:

- Story Node v3 climate narrative blocks  
- Focus Mode v3 “global reasoning” overlays  

---

### 2. 🟦 Local JSON-LD (`xai-ig-local.jsonld`)
Represents **per-sample climate drivers**:

- Local gradient contributions  
- Pixel/feature-level relevance  
- Spatial or temporal context (H3-masked)  
- Input STAC dataset references  
- CARE scope + sovereignty flags  
- `kfm:explainability:local` fields  

Used by:

- Event-level Story Node narratives  
- Focus Mode v3 “local context windows”

---

### 3. 🟩 Spatial JSON-LD (`xai-ig-spatial.jsonld`)
Optional but recommended for spatial IG pipelines:

- Tile/raster-derived gradient attribution  
- Spatial driver abstractions (H3 generalized)  
- Links to raster/COG attribution assets  
- Spatial CRS metadata  
- CARE-safe transformations  
- `kfm:explainability:spatial` STAC XAI fields  

Used by:

- Map overlays in Focus Mode v3  
- Spatial evidence chains in Story Node v3  

---

## 📡 STAC Integration Requirements

All IG JSON-LD outputs MUST include:

- `kfm:explainability:method = "integrated-gradients"`  
- One of:
  - `kfm:explainability:global`  
  - `kfm:explainability:local`  
  - `kfm:explainability:spatial`  
- `kfm:model_version`  
- `kfm:input_items` (array of STAC Item IDs)  
- `checksum:multihash`  
- CRS/geometry if spatial  
- PROV-O references  

---

## 🧾 PROV-O Lineage Requirements

Each JSON-LD IG bundle MUST contain:

- `prov:wasGeneratedBy` (model + pipeline)  
- `prov:used` (climate STAC datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (model + inference identity)  
- Optional: `prov:wasDerivedFrom` (model → IG → narrative)  

Lineage is surfaced in:

- Focus Mode timelines  
- Story Node “evidence blocks”  
- Governance review panels  

---

## 🔐 FAIR+CARE Requirements

Climate IG JSON-LD must:

- Use **H3 generalization** for any spatial location  
- Remove culturally sensitive correlations  
- Include CARE scope + sovereignty flags  
- Avoid speculative reasoning  
- Follow Data-Contract v3 + Vertical-Axis v11  

---

## 🧪 Testing Requirements

Required CI tests:

- JSON-LD schema validation  
- STAC XAI extension validation  
- Deterministic regeneration tests  
- PROV-O consistency checks  
- CARE masking tests  
- Sovereignty compliance  
- Driver ranking drift tests (IG stability)

PRs failing any → ❌ **blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate IG JSON-LD explainability spec, aligned with XAI suite |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Integrated Gradients](../README.md) · [🌡️ Climate XAI Root](../../README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

