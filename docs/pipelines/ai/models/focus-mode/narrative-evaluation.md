---
title: "📖🎯🧠 KFM v11.2.2 — Focus Mode Narrative Evaluation (Story Node v3 📚 · Cultural Safety 🛡️ · Context Integrity 🌐 · XAI 💡 · FAIR+CARE ⚖️)"
path: "docs/pipelines/ai/models/focus-mode/narrative-evaluation.md"
version: "v11.2.2"
last_updated: "2025-11-28"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Focus Mode Working Group 🎯🧠 · Cultural Safety Council 🛡️ · FAIR+CARE Council"
status: "Active / Enforced"
content_stability: "stable"
doc_kind: "Focus Mode Models · Narrative Evaluation 📖🎯"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/focusmode-narrative-eval-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/ai-focusmode-narrative-eval-v11.2.2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
storynode_policy: "../../../standards/narrative/STORYNODE-V3-GUIDE.md"
data_contract_ref: "../../../contracts/data-contract-v3.json"

license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · High-Risk (Narrative Intelligence)"
sensitivity: "FocusMode-Narrative-Eval"
sensitivity_level: "High"
public_exposure_risk: "High"
immutability_status: "version-pinned"

semantic_intent:
  - "focusmode-narrative-evaluation"
  - "storynode-quality-check"
  - "cultural-safety-check"
  - "narrative-stability"
  - "xai-narrative-eval"
  - "faircare-narrative-governance"
  - "sovereignty-narrative-screening"
  - "hazard-narrative-alignment"
  - "environmental-grounding"
  - "context-eval"

scope:
  domain: "pipelines/ai/models/focus-mode"
  applies_to:
    - "narrative-evaluation.md"
    - "mlops/*"
    - "stac/*"
    - "inference/focus/*"
    - "../embeddings/*"
    - "../../../storynode/*"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

requires_purpose_block: true
requires_directory_layout_section: false
requires_governance_links-in-footer: true
requires_version_history: true

diagram_profiles:
  - "mermaid-flowchart-v1"
---

<div align="center">

# 📖🎯🧠 **Focus Mode Narrative Evaluation — KFM v11.2.2 (MAX MODE)**  
`docs/pipelines/ai/models/focus-mode/narrative-evaluation.md`

**Purpose**  
Perform a **governance-grade evaluation** of Narrative Reasoning components in Focus Mode,  
involving Story Node v3 generation, contextual grounding (spatial/climate/hydro/hazard),  
cultural safety, sovereignty protections, and explainability (XAI) integrity.

This ensures that all narrative outputs remain:

🧭 **Spatially accurate**  
🌡️ **Climate-grounded**  
💧 **Hydrology-consistent**  
🌪️ **Hazard-safe**  
📖 **Culturally safe & sovereignty-compliant**  
💡 **Explainable and deterministic**  
🔡 **Fusion-aligned**  
🛡️ **FAIR+CARE-approved**  

</div>

---

## 🧬📚🎯 **Narrative Evaluation Architecture (Mermaid-Safe)**

```mermaid
flowchart TD
    A[📥 Story Node v3 Narrative Sample] --> B[🧠 Contextual Grounding Evaluation]
    B --> C[🌐 Environmental Alignment Checks]
    C --> D[🧭 Spatial & Sovereignty Screening]
    D --> E[🌡️ Climate Interpretation Consistency]
    E --> F[💧 Hydrology Relevance Check]
    F --> G[🌪️ Hazard Context Safety Review]
    G --> H[📖 Cultural Safety & Narrative Ethics]
    H --> I[💡 XAI Narrative Attribution Validation]
    I --> J[📜 STAC + PROV Consistency Check]
    J --> K[📦 Narrative Evaluation Report]
```

---

# 🔍 **Evaluation Components**

---

## 📘 **1. Contextual Grounding Evaluation**

Story Node v3 outputs MUST demonstrate:

- Coherent references to environmental inputs  
- Stability under repeated inference  
- Deterministic context interpretation  
- Non-speculative reasoning  
- Respect for environmental uncertainty  

Example PASS:

```json
{
  "context_grounding": {
    "spatial_ok": true,
    "climate_ok": true,
    "hazard_ok": true,
    "hydrology_ok": true
  }
}
```

---

## 🌐 **2. Environmental Alignment Checks**

Evaluates whether narrative statements align with:

- Climate drivers (CAPE/CIN/shear/LLJ/etc.)  
- Hydrology state (soil moisture/runoff/drought/streamflow)  
- Hazard context (tornado/hail/flood/fire/heat/winter)  
- Spatial ground truth (terrain/landcover/watershed/H3 region)  

Example Evaluated Statement:

> “Moisture pooling along the valley floor suggests increasing instability.”

---

## 🧭 **3. Spatial & Sovereignty Screening**

Narratives MUST:

- Properly anonymize sovereignty-protected locations  
- Avoid hyper-specific geographic claims  
- Use H3-generalized spatial references  
- NEVER reference protected cultural sites  

Example FAIL:

> “Just west of the tribal ceremonial grounds…”

→ ❌ Blocked automatically; flagged for governance.

---

## 🌡️ **4. Climate Interpretation Consistency**

Climate narratives MUST:

- Correctly reference environmental drivers  
- Avoid deterministic weather forecasts  
- Avoid exaggerated severity  
- Maintain physical consistency  

Example Allowed:

> “Wind shear aloft may organize storms later if moisture remains high.”

Example NOT Allowed:

> “A violent tornado will strike this location tonight.”

---

## 💧 **5. Hydrology Relevance Check**

Hydrology descriptions MUST:

- Reflect REAL environmental drivers  
- Avoid overprecision (e.g., streamflow at exact cfs in restricted watersheds)  
- Avoid culturally or ecologically sensitive implications  

Example:

```json
{
  "hydrology_evaluation": {
    "soil_moisture_consistent": true,
    "runoff_consistent": true,
    "ecological_safety_ok": true
  }
}
```

---

## 🌪️ **6. Hazard Context Safety Review**

Hazard narratives MUST:

- Avoid attributing intent or human impacts  
- Avoid precise hazard localization in sovereignty regions  
- Avoid deterministic future hazard claims  
- Stick to physically plausible contextual signals  

Example Allowed:

> “Enhanced wind shear may support organized storms.”

Example NOT Allowed:

> “A tornado is forming over the tribal lands now.”

---

## 📖 **7. Cultural Safety & Narrative Ethics**

The Story Node MUST:

- Respect cultural sovereignty  
- Avoid speculation about tribal identity, history, genealogy  
- Avoid sensitive sociocultural claims  
- Not derive unsafe inferences from environmental data  

Example cultural-safety block:

```json
{
  "cultural_safety": {
    "safe": true,
    "notes": []
  }
}
```

---

## 💡 **8. XAI Narrative Attribution Validation**

XAI MUST include:

- Attention entropy  
- Token-level attribution  
- Environmental cue weights  
- Cross-domain influence scores  
- CAM overlays (if spatial references present)  

Example:

```json
{
  "xai_narrative": {
    "attention_entropy": 0.81,
    "top_tokens": ["slope", "moisture", "evening_wind"],
    "domain_weights": {
      "spatial": 0.28,
      "climate": 0.22,
      "hydrology": 0.18,
      "hazards": 0.17,
      "narrative": 0.15
    }
  }
}
```

---

## 📜 **9. STAC + PROV Consistency Check**

Evaluates whether:

- STAC metadata for the narrative aligns with model version  
- PROV lineage is intact  
- Fusion vectors match the STAC Item  
- Narrative-XAI provenance is present  

Example:

```json
{
  "stac_consistency": {
    "valid": true,
    "missing_links": []
  }
}
```

---

## 📦 **10. Narrative Evaluation Report Assembly**

Final artifacts MUST include:

```
narrative_eval_report.json
narrative_context_alignment.json
narrative_xai_eval.json
narrative_sov_safety.json
narrative_environmental_alignment.json
narrative_storynode_validation.json
```

All MUST be sovereignty-safe and CI-valid.

---

# 🧪📏🔬 **CI Validation Requirements**

CI MUST validate:

- Cultural safety  
- Sovereignty masking  
- XAI attribution stability  
- StoryNode safety and context correctness  
- No sensitive-region leakage  
- STAC + PROV correctness  
- Environmental alignment logic  
- Deterministic output  

Failure → ❌ CI BLOCK.

---

# 🕰️📜 **Version History**

| Version | Date       | Notes                                                         |
|---------|------------|--------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Initial Focus Mode Narrative Evaluation (MAX MODE)           |

---

<div align="center">

### 🔗 Footer  
[🎯 Back to Focus Mode Models](./README.md) ·  
[📡 Telemetry](./mlops/telemetry/README.md) ·  
[🏛 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

