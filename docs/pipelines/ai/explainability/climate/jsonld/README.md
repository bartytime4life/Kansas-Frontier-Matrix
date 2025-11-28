---
title: "🌡️📄 KFM v11.2.2 — Climate Explainability JSON-LD Bundles (Global · Local · Spatial Drivers)"
path: "docs/pipelines/ai/explainability/climate/jsonld/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Climate Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Explainability Component"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
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
  - "xai-jsonld"
  - "climate-xai"
  - "global-drivers"
  - "local-drivers"
  - "spatial-drivers"
  - "story-node-xai"
  - "focus-mode-xai"
  - "prov-xai"

scope:
  domain: "explainability/climate/jsonld"
  applies_to:
    - "jsonld-global"
    - "jsonld-local"
    - "jsonld-spatial"
    - "stac-xai"
    - "prov-xai"
    - "story-node-xai"
    - "faircare-governance"
    - "sovereignty"

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

# 🌡️📄 **Climate Explainability JSON-LD Bundles**  
`docs/pipelines/ai/explainability/climate/jsonld/README.md`

**Purpose:**  
Define the **canonical JSON-LD explainability bundles** for climate AI models — including **global**, **local**, and **spatial** attribution drivers.  
These bundles connect climate model explainability to **STAC v11**, **Story Node v3**, **Focus Mode v3**, and downstream governance systems.

</div>

---

## 📘 Overview

Climate JSON-LD XAI bundles express:

- Model-derived drivers  
- Global & local attribution signals  
- Spatial drivers (if applicable)  
- Structured explanations for narratives  
- FAIR+CARE-aligned masking information  
- Provenance (PROV-O)  
- STAC XAI asset metadata  

They serve as the **machine-readable bridge** between raw explainability computations and:

- Story Node v3  
- Focus Mode v3 reasoning  
- Lineage dashboards  
- Governance review workflows  

Each JSON-LD file must be:

- Deterministic  
- Schema-valid  
- CARE-filtered  
- Version-pinned  
- Fully traceable  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/climate/jsonld/
    ├── 📄 README.md                                  # This file
    │
    ├── 📄 xai-global.jsonld                          # Global climate driver bundle
    ├── 📄 xai-local.jsonld                           # Local (per-prediction) bundle
    └── 📄 xai-spatial-drivers.jsonld                 # Optional: spatial attribution drivers

---

## 🔍 JSON-LD Bundle Specifications

### 1. 🟥 Global JSON-LD (xai-global.jsonld)

Represents **system-level climate drivers**:

- Global SHAP vectors  
- Aggregated IG gradients  
- Global CAM summaries  
- Spatial aggregates (masked where required)  
- Feature rankings  
- Climate variable relationships  
- Version + provenance metadata  

Used by:

- Story Node v3 climate narratives  
- Focus Mode v3 climate timeline overlays  
- High-level driver dashboards  

---

### 2. 🟦 Local JSON-LD (xai-local.jsonld)

Represents **instance-level climate drivers**:

- Local SHAP vectors  
- Tile-level IG explanations  
- Local CAM highlights  
- Per-event climate driver summaries  
- CARE-masked local context  
- Fine-grained provenance  

Used for:

- Event-based Story Nodes  
- Forecast explanation panels  
- Focus Mode “local reasoning windows”  

---

### 3. 🟩 Spatial Driver JSON-LD (xai-spatial-drivers.jsonld)

For models producing **spatially explicit climate attribution**:

- Raster/tile-derived attribution summaries  
- GeoJSON-based abstractions (H3-generalized)  
- Spatial relevance codes  
- Domain semantics (terrain × climate drivers)  

Used by:

- Focus Mode map overlays  
- Story Node spatial evidence blocks  
- Climate model interpretability surfaces  

---

## 📡 STAC Integration Requirements

Each JSON-LD bundle MUST provide:

- `kfm:explainability:*` fields  
- Asset references + multihash checksums  
- CRS + geometry (if spatial)  
- Model version fields  
- Input STAC IDs (`kfm:input_items`)  
- Provenance (`prov:*`) relations  

---

## 🧾 PROV-O Lineage Requirements

Each XAI JSON-LD output must include:

- `prov:wasGeneratedBy`  
- `prov:used`  
- `prov:wasDerivedFrom`  
- `prov:generatedAtTime`  
- `prov:Agent`  

These lineage chains connect:

- Model → Explainability → Narrative → End-user reasoning  

---

## 🔐 FAIR+CARE Requirements

JSON-LD XAI outputs MUST:

- Mask culturally sensitive geography (H3 generalization)  
- Remove drivers tied to restricted/clan/tribal indicators  
- Carry CARE-scope & sovereignty metadata  
- Follow KFM’s cultural-data governance rules  
- Contain no speculative associations  

---

## 🧪 Testing Requirements

All JSON-LD explainability bundles MUST pass:

- JSON Schema validation  
- PROV-O consistency checks  
- STAC extension validation  
- CARE masking checks  
- Deterministic hashing tests  
- Narrative linkage tests (Story Node v3)  

PRs altering JSON-LD structures MUST pass full CI validation.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                |
|----------|------------|----------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Climate Explainability JSON-LD spec aligned with XAI suite  |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Climate Explainability](../README.md) · [🌡️ XAI Templates](../../templates/README.md) · [🏛 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

