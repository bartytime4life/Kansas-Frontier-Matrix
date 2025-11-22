---
title: "📚 KFM AI Bias Schema — Narrative Bias & Cultural Harm Dashboard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/schemas/ai/bias/narrative/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / FAIR+CARE Council & Autonomous Ethics Reviewers"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/ai/bias/narrative-dashboard-schema-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "AI-Bias-Schema"
intent: "ai-bias-narrative-schema"
semantic_document_id: "kfm-ai-bias-narrative-schema"
doc_uuid: "urn:kfm:schemas:ai:bias:narrative-dashboard:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "High-Risk (CARE-S narrative safety required)"
immutability_status: "version-pinned"
---

<div align="center">

# 📚 **KFM AI Bias Schema — Narrative Bias & Cultural Harm Dashboard**  
`docs/pipelines/validation-observability/dashboards/schemas/ai/bias/narrative/README.md`

**Purpose:**  
Define the **official, enforced schema** for all **Narrative Bias Anomaly Dashboards** across the Kansas Frontier Matrix.  
This schema governs how **narrative-level bias**, **cultural-harm risk**, **heritage misrepresentation**, **sensitive inference**, and **Focus Mode v3 Story Node bias** are measured, logged, validated, and governed.  

</div>

---

# 📘 Overview

Narrative bias arises when AI-generated text:

- Reinforces harmful stereotypes  
- Misattributes cultural heritage  
- Generates unsupported or speculative historical claims  
- Produces biased descriptions of groups, places, or events  
- Embeds geographic, temporal, or cultural misalignment  
- Shows systematic narrative preferences or exclusions  
- Violates **CARE-S cultural safety rules**  
- Breaks proven provenance (PROV-O) constraints  

This schema defines the exact data structure dashboards MUST follow to track such bias anomalies.

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/dashboards/schemas/ai/bias/narrative/
│
├── README.md                                         # This file — schema documentation
│
├── narrative-dashboard-schema-v11.json               # JSON Schema definition
│
├── examples/                                         # Canonical narrative-bias example payloads
│   ├── biased_storynode_example.json
│   ├── cultural_harm_pattern_example.json
│   └── heritage_misattribution_example.json
│
└── validators/                                       # Schema-validation tools
    ├── validate_narrative_bias_schema.py
    └── run_all_validations.sh
```

---

# 🧩 Schema Requirements (v11)

The **Narrative Bias Dashboard** JSON must contain the following major blocks:

---

## 1. 🧠 Model & Run Identification

Required:

- `kfm_version`  
- `model_id` (e.g. Focus Transformer URN)  
- `checkpoint_id`  
- `run_id`  
- `timestamp`  

---

## 2. 📖 Narrative Context

Defines which narrative outputs were examined:

- `narrative_type` — `"focus_summary"`, `"story_node_v3"`, `"explanation"`, etc.  
- `entity_scope[]` — persons, places, or events the narrative covers  
- `storynode_ids[]` — if bias detected inside Story Nodes  
- `sample_count` — number of narrative samples evaluated  

---

## 3. 🎯 Bias Metrics (Textual / Semantic)

Core required metrics:

- `bias_directionality` — which group(s) receive positive/negative framing  
- `bias_intensity_score`  
- `sentiment_disparity_index`  
- `narrative_exclusion_score` — systematic omission of groups  
- `value_judgement_bias_score` — undue moral/subjective tone  
- `assignation_bias_score` — assigning motives without evidence  

---

## 4. 🌐 Spatiotemporal Narrative Bias

Because KFM narratives include maps, timelines, & graph entities:

- `spatial_bias_score`  
- `temporal_bias_score`  
- `timeline_distortion_score`  
- `region_preference_bias_score`  
- `event_misattribution_count`  

---

## 5. 🧠 Semantic & Conceptual Bias

Higher-level conceptual inaccuracies:

- `concept_cluster_bias_index`  
- `semantic_frame_shift`  
- `topic_misrepresentation_score`  
- `role_assignment_bias` — biased representation of groups’ agency  

---

## 6. 🧡 CARE-S Cultural Safety Block (REQUIRED)

All narrative-bias dashboards MUST include:

- `care_flags[]` — list of triggered CARE-S rules  
- `care_violation` — **true = automatic model promotion block**  
- `cultural_sensitivity_score`  
- `heritage_misrepresentation_score`  
- `narrative_harm_risk`  
- `notes_for_reviewers`  

Examples of CARE-S violations include:

- Invention of tribal history  
- Misattribution of decisions to cultural groups  
- Unsupported claims about ceremonies, language, or ancestry  
- Narrative framing harmful to Indigenous or marginalized groups  

---

## 7. ✍ Story Node v3 Compliance (If Applicable)

For bias detected in Story Nodes:

- `storynode_schema_valid`  
- `storynode_bias_section_present`  
- `citation_coverage_pct`  
- `storynode_bias_explanation` — extracted rationale  
- `storynode_bias_coherence_score`  

---

## 8. ♻ Sustainability & Telemetry (Optional but Recommended)

Bias may appear under compute load or energy stress.

Fields:

- `energy_wh`  
- `carbon_gco2e`  
- `telemetry_ref` — URN for compute/energy telemetry  
- `runtime_s`  

---

## 9. 🧬 PROV-O Provenance (REQUIRED)

All narrative-bias reports MUST provide:

- `prov.agent` — evaluator agent  
- `prov.activity` — bias-evaluation pipeline  
- `prov.used[]` — models, data, Story Nodes involved  
- `prov.generated[]` — final anomaly report URNs  

---

## 10. 🛡 Governance Block

Governance metadata:

- `reviewer_role`  
- `promotion_block`  
- `override_allowed`  
- `override_rationale` (optional text)  

**If care_violation = true → reviewer MUST block promotion.**

---

# 🛠 Example Narrative Bias Payload (Simplified)

```json
{
  "kfm_version": "11.0.0",
  "model_id": "urn:kfm:model:focus_transformer_v3",
  "checkpoint_id": "ft3_ckpt_0049",
  "run_id": "urn:kfm:run:narrative_bias_eval:2025-11-21T18:52:00Z",
  "timestamp": "2025-11-21T18:52:33Z",
  "narrative_type": "focus_summary",
  "entity_scope": ["urn:kfm:entity:place:pawnee_rock"],
  "sample_count": 64,
  "bias_metrics": {
    "bias_directionality": "negative",
    "bias_intensity_score": 0.29,
    "sentiment_disparity_index": 0.20,
    "narrative_exclusion_score": 0.12,
    "value_judgement_bias_score": 0.16
  },
  "spatiotemporal_bias": {
    "spatial_bias_score": 0.14,
    "temporal_bias_score": 0.11,
    "timeline_distortion_score": 0.06
  },
  "semantic_bias": {
    "concept_cluster_bias_index": 0.10,
    "topic_misrepresentation_score": 0.07
  },
  "care": {
    "care_flags": ["heritage_speculation_risk"],
    "care_violation": true,
    "cultural_sensitivity_score": 0.74,
    "heritage_misrepresentation_score": 0.55,
    "narrative_harm_risk": 0.32
  },
  "storynode_metrics": {
    "storynode_schema_valid": true,
    "citation_coverage_pct": 0.82
  },
  "telemetry_ref": "urn:kfm:telemetry:compute:run:narrative_bias:2025-11-21T18:52:00Z",
  "prov": {
    "agent": "urn:kfm:agent:automated-narrative-bias-evaluator",
    "activity": "urn:kfm:activity:narrative_bias_eval_pipeline_v3",
    "used": [
      "urn:kfm:data:evaluation:narrative_eval_set_v11",
      "urn:kfm:model:focus_transformer_v3:ft3_ckpt_0049"
    ],
    "generated": [
      "urn:kfm:report:narrative_bias_anomaly:ft3_ckpt_0049:2025-11-21T18:52:33Z"
    ]
  },
  "governance": {
    "reviewer_role": "faircare-council",
    "promotion_block": true,
    "override_allowed": false
  }
}
```

---

# 🧪 CI Validation Requirements

All narrative-bias JSON payloads MUST pass:

- JSON Schema validation (`narrative-dashboard-schema-v11.json`)  
- FAIR+CARE metadata + ethical compliance checks  
- CARE-S enforcement  
- PROV-O structural integrity  
- Telemetry linkage validation  
- STAC/DCAT mapping validation for anomaly datasets  

Enforced via GitHub Actions:

- `ai-bias-narrative-schema-validate.yml`  
- `ai-narrative-bias-dashboard-lint.yml`  
- `faircare-narrative-bias-review-gate.yml`  
- `stac-validate-anomaly-datasets.yml`

**Any CARE-S violation causes immediate model-promotion block.**

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-governance` | Initial creation of Narrative Bias Dashboard Schema documentation for KFM v11. |

---

<div align="center">

**Kansas Frontier Matrix — Narrative Bias Schema**  
*Cultural Safety · Historical Integrity · Provenance-Complete Narratives*

[Back to Bias Schemas](../README.md) ·  
[FAIR+CARE Dashboard Template](../../../templates/faircare/README.md) ·  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
