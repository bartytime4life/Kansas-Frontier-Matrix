---
title: "⚡🛰️🧬 KFM v11.2.2 — Hazard CAMs Template Suite (Rasters · Tiles · JSON-LD · Taxonomy)"
path: "docs/pipelines/ai/explainability/hazard/cams/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · Hazard Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Explainability Template Suite (Hazard CAMs)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha>"
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
sensitivity: "Explainability-Hazard-CAM-Templates"
sensitivity_level: "Low"
public_exposure_risk: "Low"
immutability_status: "version-pinned"

semantic_intent:
  - "hazard-cams-template-suite"
  - "cams-raster-template"
  - "cams-tile-template"
  - "cams-jsonld-template"
  - "hazard-cams-driver-taxonomy"
  - "prov-xai-template"
  - "stac-xai-template"
  - "story-node-hazard-template"
  - "focus-mode-hazard-template"
  - "faircare-governance-template"

scope:
  domain: "explainability/hazard/cams/templates"
  applies_to:
    - "cams-raster-template.json"
    - "cams-tile-template.json"
    - "xai-cams-global-template.jsonld"
    - "cams-driver-taxonomy.jsonld"
    - "faircare-governance"
    - "h3-masking"
    - "prov-xai"
    - "stac-xai"
    - "semantic-driver-taxonomy"
    - "narrative-driver-templates"

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

# ⚡🛰️🧬 **Hazard CAMs — Template Suite**  
`docs/pipelines/ai/explainability/hazard/cams/templates/README.md`

**Purpose:**  
Provide the **governed, deterministic template suite** for all Hazard CAM explainability components, covering:

- Raster CAMs (COG/GeoTIFF)  
- Tile CAMs (GeoParquet)  
- Semantic JSON-LD evidence bundles  
- CAM driver taxonomies (narrative-safe)  
- FAIR+CARE + sovereignty placeholders  
- PROV-O lineage structures  
- STAC-XAI metadata templates  
- Story Node v3 & Focus Mode v3 integration scaffolds  

These templates ensure **uniform, reproducible, governance-aligned CAM explainability** across all hazard models.

</div>

---

## 📘 Overview

Hazard CAM explainability captures the **spatial regions** that deep-learning hazard models use when making predictions.  
The template suite defines **the exact structures** that all CAM-related explainability artifacts must follow.

This suite provides:

- Schema templates for raster CAM explainability  
- Schema templates for tile CAM explainability  
- JSON-LD templates linking CAMs → semantic hazard drivers  
- Narrative-safe driver-taxonomy templates  
- FAIR+CARE masking scaffolding  
- STAC-XAI and PROV-O template modules  
- Deterministic ordering rules for CI reproducibility  

This is the root reference for all CAM pipeline outputs.

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/explainability/hazard/cams/templates/
    ├── 📄 README.md                                   # This file
    │
    ├── 📁 rasters/                                    # Templates for raster CAM explainability
    │   ├── 📄 cams-raster-template.json
    │   ├── 📄 cams-raster-driver-taxonomy.jsonld
    │   └── 📄 README.md
    │
    ├── 📁 tiles/                                      # Templates for tile CAM explainability
    │   ├── 📄 cams-tile-template.json
    │   ├── 📄 cams-tile-driver-taxonomy.jsonld
    │   └── 📄 README.md
    │
    └── 📁 jsonld/                                     # Top-level semantic CAM templates
        ├── 📄 xai-cams-global-template.jsonld
        └── 📄 cams-driver-taxonomy.jsonld

---

## 🔍 Template Categories

### 1. 🟧 Raster CAM Templates (`rasters/`)
Includes:

- `cams-raster-template.json` — COG/GeoTIFF field template  
- `cams-raster-driver-taxonomy.jsonld` — semantic raster-driver codes  
- RUN constraints:
  - CRS + vertical datum fields  
  - Pixel-value structure  
  - CARE + sovereignty placeholders  
  - H3-based generalization  
  - PROV lineage  
  - STAC-XAI asset fields  

### 2. 🟩 Tile CAM Templates (`tiles/`)
Includes:

- `cams-tile-template.json` — GeoParquet tile schema  
- `cams-tile-driver-taxonomy.jsonld` — semantic tile-driver codes  
- Rules for:
  - Tile grid indexing  
  - Partitioning  
  - CARE/H3 masking  
  - Deterministic tile sorting  
  - STAC-XAI metadata  
  - PROV-O lineage  

### 3. 🟦 JSON-LD Global CAM Templates (`jsonld/`)
Includes:

- `xai-cams-global-template.jsonld` — full semantic CAM evidence bundle  
- `cams-driver-taxonomy.jsonld` — unified hazard CAM driver taxonomy  

These drive:

- Story Node v3 hazard narratives  
- Focus Mode v3 spatial overlays  
- High-level hazard reasoning workflows  

---

## 📡 STAC-XAI Template Requirements

Generated CAM artifacts **must include**:

- `kfm:explainability:method = "cams"`  
- Proper subtype (`raster`, `tiles`, or `global`)  
- `kfm:model_version`  
- `kfm:input_items`  
- `checksum:multihash`  
- CRS metadata  
- CARE + sovereignty fields  
- JSON-LD links (for spatial explainability)  
- PROV-O lineage  

Templates here define field placement + deterministic ordering.

---

## 🧾 PROV-O Template Requirements

Templates enforce:

- `prov:wasGeneratedBy` (CAM inference pipeline)  
- `prov:used` (hazard + climate STAC datasets)  
- `prov:generatedAtTime`  
- `prov:Agent` (model identity)  
- Optional:
  - `prov:wasDerivedFrom` (CAM ↔ IG/SHAP relationships)  

These ensure explainability lineage is fully traceable.

---

## 🔐 FAIR+CARE & Sovereignty Enforcement

All CAM templates MUST include:

- H3 generalization placeholders  
- CARE scope & annotation placeholders  
- Sovereignty flags + guidance  
- No sensitive geographic details  
- No speculative hazard language  
- Data Contract v3 compliance  
- Culturally safe terminology  

Downstream content is rejected without these safeguards.

---

## 🧪 Template CI Enforcement

CI MUST validate:

- JSON / JSON-LD schema correctness  
- Deterministic key ordering  
- STAC-XAI compliance  
- PROV-O completeness  
- CARE + sovereignty placeholder presence  
- H3 generalization scaffolding  
- Narrative-safety lexical rules  
- Hash stability  

Any failure → **PR blocked**.

---

## 🕰 Version History

| Version  | Date       | Notes                                                                           |
|----------|------------|---------------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Initial Hazard CAM Template Suite (raster + tiles + JSON-LD + taxonomy)         |

---

<div align="center">

### 🔗 Footer  
[⬅ Back to Hazard CAMs](../README.md)  
[⚡ Hazard XAI Root](../../README.md)  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

