---
title: "📜🎯🌐 KFM v11.2.2 — Focus Mode STAC Provenance Catalog (PROV-O 🧬 · Context Lineage 📖 · Fusion 🔡 · FAIR+CARE 🛡️ · Sovereignty ⚖️)"
path: "docs/pipelines/ai/models/focus-mode/stac/provenance/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Focus Mode Working Group 🎯🧠 · FAIR+CARE Council 🛡️"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Focus Mode STAC · Provenance Catalog 📜🎯"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/focusmode-stac-provenance.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/ai-focusmode-stac-provenance-v11.2.2.json"
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
sensitivity: "FocusMode-STAC-Provenance"
sensitivity_level: "High"
public_exposure_risk: "High"
immutability_status: "version-pinned"

semantic_intent:
  - "focusmode-provenance"
  - "context-ai-lineage"
  - "fusion-vector-lineage"
  - "storynode-lineage"
  - "hazard-context-lineage"
  - "climate-hydro-context-lineage"
  - "xai-lineage"
  - "faircare-governance"
  - "sovereignty-protection"
  - "stac-lineage"

scope:
  domain: "pipelines/ai/models/focus-mode/stac/provenance"
  applies_to:
    - "README.md"
    - "prov_focusmodel_*.json"
    - "../items/*"
    - "../model-cards/*"
    - "../collections/*"
    - "../telemetry/*"
    - "../../mlops/*"
    - "../../../inference/focus/*"
    - "../../../models/embeddings/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_directory_layout_section: true
requires_purpose_block: true
requires_governance_links-in-footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 📜🎯🌐 **Focus Mode STAC Provenance Catalog — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/focus-mode/stac/provenance/README.md`

**Purpose**  
Document and govern the **PROV-O lineage system** for all Focus Mode contextual intelligence models:  
🧭 Geo-awareness · 🌡️ Climate reasoning · 💧 Hydrology context · 🌪️ Hazard logic ·  
📖 Story Node v3 · 🔡 Fusion vectors · 💡 XAI explainability · 📡 Telemetry · 🛡️ FAIR+CARE · ⚖️ Sovereignty.

This catalog ensures *full traceability*, *determinism*, *auditability*, and *sovereignty-safe lineage modeling*.

</div>

---

## 🗂️📁📜 **Directory Layout (MAX MODE)**

```
docs/pipelines/ai/models/focus-mode/stac/provenance/
    📄 README.md
    📄 prov_focusmodel_v11.2.2.json
    📄 prov_focusmodel_v11.2.1.json
    📄 prov_focusmodel_template.json
```

---

## 🧬📜🎯 **Provenance Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[📦 Focus Mode STAC Item] --> B[📜 PROV O Activity Block]
    B --> C[🧬 Upstream Inputs Spatial Climate Hydro Hazard Narrative]
    C --> D[⚙️ Transformations Training Preprocessing Masking Fusion]
    D --> E[📄 Outputs Weights StoryNode Fusion XAI Telemetry]
    E --> F[🛡️ CARE And Sovereignty Metadata]
    F --> G[🌐 Final STAC Item With Provenance]
```

---

# 🔍 **Required PROV-O Blocks**

---

## 1️⃣ **prov:wasGeneratedBy**

Records the Focus Mode training activity:

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:training:focusmode_v11_2_2"
  }
}
```

---

## 2️⃣ **prov:used**

MUST enumerate *all* upstream dependencies:

```json
{
  "prov": {
    "used": [
      "urn:kfm:data:terrain_item",
      "urn:kfm:data:climate_item",
      "urn:kfm:data:hydrology_item",
      "urn:kfm:data:hazard_item",
      "urn:kfm:data:narrative_item",
      "urn:kfm:model:embeddings_spatial_v11_2_2",
      "urn:kfm:model:embeddings_fusion_v11_2_2",
      "urn:kfm:preprocess:sovereignty_mask_v3",
      "urn:kfm:xai:template_focus_v11_2"
    ]
  }
}
```

---

## 3️⃣ **prov:wasAssociatedWith**

Indicates which service/agent produced the model:

```json
{
  "prov": {
    "agent": "urn:kfm:service:focus-training-engine"
  }
}
```

---

## 4️⃣ **Deterministic Seed Metadata**

Included inside STAC `"properties.model:seed"`.

---

# 🔍 **XAI Provenance Requirements**

Focus Mode MUST produce XAI-specific provenance:

```json
{
  "xai:prov": {
    "wasGeneratedBy": "urn:kfm:activity:xai:focusmode_v11_2_2",
    "used": [
      "focus_model.pt",
      "fusion_weights.json",
      "context_router.pt"
    ],
    "agent": "urn:kfm:service:focus-xai-engine"
  }
}
```

This ensures attribution → model weights → fusion logic are traceable.

---

# 🔍 **Telemetry Provenance Requirements**

All telemetry bundles MUST include:

```json
{
  "prov": {
    "wasGeneratedBy": "urn:kfm:activity:telemetry:focus_inference_v11_2_2",
    "used": [
      "focusmodel_v11_2_2.json",
      "embedding_fusion_v11_2_2.json"
    ],
    "agent": "urn:kfm:service:focus-telemetry-engine"
  }
}
```

Covers OTel spans, XAI drift, sustainability metrics, and geography/hazard context relevance.

---

# 🛡️⚖️ **FAIR+CARE & Sovereignty Provenance Requirements**

Focus Mode provenance MUST document:

- Sovereignty-driven masking  
- Cultural-safety transformations  
- Hazard-overlocalization suppression  
- Narrative content filtering  
- Spatial H3 generalization  
- Care policy inheritance  

Required block:

```json
{
  "care": {
    "masking": "h3-focus-generalized",
    "scope": "public-generalized",
    "notes": ["Sovereignty protections applied in training and STAC assembly"]
  }
}
```

---

# 📦📜🧾 **Provenance Templates**

Template JSON files MUST be provided for:

- Geo-awareness  
- Climate logic  
- Hydrology logic  
- Hazard context  
- Story Node v3  
- Fusion layer  
- Telemetry events  
- XAI provenance  

---

# 🧪📏🔬 **CI Validation Requirements**

CI MUST verify:

- PROV-O schema correctness  
- Deterministic ordering of `"prov:used"`  
- Sovereignty masking metadata  
- CARE metadata correctness  
- STAC → model-card → XAI → PROV linkage  
- No sensitive-region leakage  
- Telemetry-provenance correctness  
- Reproducible provenance across runs  

Failure → ❌ CI BLOCK.

---

# 🕰️📜 **Version History**

| Version | Date       | Notes                                                   |
|---------|------------|---------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Focus Mode STAC Provenance Catalog (MAX MODE)   |

---

<div align="center">

### 🔗 Footer  
[🌐 Back to Focus Mode STAC Root](../README.md) ·  
[📦 STAC Items](../items/README.md) ·  
[🏛 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

