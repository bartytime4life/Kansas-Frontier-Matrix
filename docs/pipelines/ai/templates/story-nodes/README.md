---
title: "📖 KFM v11.2.2 — Story Node v3 Template Suite (Narrative JSON-LD · Evidence Fusion · FAIR+CARE · STAC/PROV-O)"
path: "docs/pipelines/ai/templates/story-nodes/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Biannual · FAIR+CARE Council · Narrative Oversight Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Template Specification"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/story-node-templates-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/story-node-templates-v11.2.2.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
data_contract_ref: "../../../../contracts/data-contract-v3.json"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity: "Narrative-AI"
sensitivity_level: "Medium"
public_exposure_risk: "Moderate"
immutability_status: "version-pinned"

semantic_intent:
  - "story-node"
  - "narrative-ai"
  - "jsonld-templates"
  - "evidence-fusion"
  - "provenance"
  - "faircare-governance"
  - "focus-mode-integration"

scope:
  domain: "ai-story-node-templates"
  applies_to:
    - "story-node-jsonld"
    - "narrative-windows"
    - "evidence-chains"
    - "focus-mode-v3"
    - "xai-to-narrative"
    - "provenance-jsonld"
    - "care-governance"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 📖 **KFM v11.2.2 — Story Node v3 Template Suite**  
`docs/pipelines/ai/templates/story-nodes/README.md`

**Purpose:**  
Define the **canonical templates** for Story Node v3: narrative JSON-LD, evidence chains, XAI-to-narrative mappings, provenance blocks, temporal/spatial grounding, and CARE-safe narrative constraints used across the entire KFM AI system.  
These templates ensure deterministic, auditable, FAIR+CARE-aligned narrative generation across **Focus Mode v3**, **AI inference**, **STAC outputs**, and **graph reasoning**.

</div>

---

## 📘 Overview

Story Nodes v3 are **structured narrative units** describing:

- A person, place, event, feature, layer, hazard, trend, or dataset  
- Grounded contextual information (spatial, temporal, semantic)  
- Provenance of statements (full evidence trace)  
- CARE-compliant masked content  
- Links to STAC Items, Neo4j entities, and raw data sources  
- Narrative windows for Focus Mode v3  

Story Nodes are **JSON-LD**, ontology-aligned objects designed for:

- Machine reasoning  
- Human reading  
- Dataset interoperability  
- Narrative rendering in the UI (MapLibre, Cesium, Timeline)  

---

## 🗂 Directory Layout (v11.2.2)

    docs/pipelines/ai/templates/story-nodes/
    ├── 📄 README.md                                      # This file
    │
    ├── 📁 jsonld/                                        # Core templates
    │   ├── 📄 story-node-template.jsonld                 # Canonical v3 Story Node structure
    │   ├── 📄 narrative-window-template.jsonld           # Narrative slice/segment template
    │   ├── 📄 evidence-chain-template.jsonld             # PROV-O aligned evidence mapping
    │   └── 📄 spatial-mask-template.jsonld               # H3 generalization + CARE masking
    │
    ├── 📁 mapping/                                      # XAI → narrative rules
    │   ├── 📄 xai-to-narrative-template.md               # How to narrativize XAI drivers
    │   ├── 📄 driver-explanation-template.jsonld         # Structured driver explanation
    │   └── 📄 relevance-ranking-template.jsonld          # Evidence/relevance ordering
    │
    ├── 📁 stac/                                         # STAC-linked narrative templates
    │   ├── 📄 stac-narrative-item-template.json          # Story Node as STAC Item
    │   └── 📄 stac-narrative-asset-template.json         # Narrative assets (JSON-LD, text)
    │
    └── 📁 mlops/                                        # Governance, audits, and drift control
        ├── 📄 narrative-governance-template.md           # Rules for narrative generation
        ├── 📄 fairness-care-audit-template.md           # CARE safety auditing
        └── 📄 story-node-drift-monitoring-template.json  # Narrative drift detection

---

## 🧬 Story Node v3 Components

### 1. 🏷 Identity Block
- `story_node:id`  
- `story_node:entity` (Neo4j ID + CIDOC-CRM type)  
- `story_node:type` (place, person, event, hydrology-feature, climate-feature, etc.)  
- `story_node:version`  
- `story_node:confidence`  

### 2. 🌍 Spatial Context
- GeoJSON or abstracted geometry  
- H3 generalized geometry for sensitive sites  
- Spatial provenance (`prov:used`)  

### 3. 🕰 Temporal Context
- OWL-Time `ProperInterval`  
- Start/end timestamps  
- Time uncertainty band  

### 4. 🧠 Narrative Body
- Deterministic text generation  
- CARE-compliant abstraction  
- Data-grounded statements only  
- No speculation, hallucination, or identity inference  

### 5. 🔗 Evidence Chain (JSON-LD)
- `prov:used` → upstream STAC Items  
- `prov:wasGeneratedBy` → AI inference process  
- `prov:wasDerivedFrom` → raw data sources  
- XAI drivers → provenance bundle  

### 6. 🎨 Explainability → Narrative Mapping
- XAI factors (SHAP/IG/CAMs) mapped to:
  - Narrative sentences  
  - Feature explanations  
  - Relevance rankings  

### 7. 🧱 Governance Block
- CARE scope  
- Masking rules  
- Sovereignty declarations  
- Required disclaimers  
- Model version + pipeline contract version  

---

## 📡 STAC Integration Requirements (KFM-STAC v11)

Story Nodes published as STAC Items must include:

- `kfm:story_node:id`  
- `kfm:story_node:entity`  
- `kfm:story_node:version`  
- `kfm:story_node:evidence`  
- `kfm:story_node:confidence`  
- CRS / bounding geometry (if present)  
- `prov:*` lineage refs  
- `care:*` fields  
- Multihash checksums for narrative assets  

---

## 🔐 FAIR+CARE Requirements

Story Node templates ENFORCE:

- Masking for tribal/Indigenous knowledge  
- H3 abstraction for sensitive spatial features  
- No speculation on cultural identity or sacred sites  
- Transparent provenance for every statement  
- Ethical narrative construction  
- Explicit CARE scope fields  

Violations → **CI + governance block**.

---

## 🧪 Testing Requirements

Story Node templates must pass:

- JSON-LD schema validation  
- STAC narrative item validation  
- CARE masking tests  
- XAI-to-narrative mapping tests  
- Drift detection  
- Narrative reproducibility tests  
- FAIR+CARE audit scripts  

---

## 🕰 Version History

| Version  | Date       | Notes                                                                     |
|----------|------------|---------------------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Full uplift; added narrative-window/evidence-chain/H3 mask templates      |
| v11.0.0  | 2025-11-15 | Initial Story Node v3 template suite                                      |

---

<div align="center">

### 🔗 Footer  
[⬅ AI Template Index](../README.md) · [🧬 Model Card Templates](../model-cards/README.md) · [🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

