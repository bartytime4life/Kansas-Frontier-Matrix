---
title: "🧩 KFM AI Anomaly Schema — Reasoning Pathology & Logical Drift Dashboard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/reasoning/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/ai/anomaly/reasoning-dashboard-schema-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "AI-Anomaly-Schema"
intent: "ai-anomaly-reasoning-schema"
semantic_document_id: "kfm-ai-anomaly-reasoning-schema"
doc_uuid: "urn:kfm:schemas:ai:anomaly:reasoning-dashboard:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Mixed-Risk (requires governance adjudication)"
immutability_status: "version-pinned"
---

<div align="center">

# 🧩 **KFM AI Anomaly Schema — Reasoning Pathology & Logical Drift Dashboard**  
`docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/reasoning/README.md`

**Purpose:**  
Define the **canonical JSON schema** and structural rules for all **Reasoning Anomaly Dashboards** within the Kansas Frontier Matrix v11.  
This schema governs how **reasoning failures**, **logical drift**, **contradictions**, **causal-path anomalies**, and **unsafe Focus Mode v3 reasoning** must be represented, validated, and surfaced across KFM observability dashboards.

</div>

---

# 📘 Overview

The **Reasoning Anomaly Schema** standardizes reporting for **reasoning-layer** failures in:

- Focus Mode v3 multi-hop reasoning  
- Story Node v3 causal narratives  
- LLM-based explanations and justifications  
- Multi-modal reasoning over text × map × timeline × graph  

Reasoning anomalies include:

- Broken or missing inference steps  
- Internal and cross-narrative contradictions  
- Causal graph drift and mis-ordered dependencies  
- Temporal/spatial logical errors  
- Overconfident, unsupported causal claims  
- Speculative or harmful cultural reasoning (CARE-S)  
- Violations of provenance-constrained facts  

This schema ensures every reasoning anomaly is:

- **FAIR+CARE compliant**  
- **Provenance-complete (PROV-O)**  
- **Linked to compute/energy/carbon telemetry**  
- **Aligned with Story Node v3 and STAC/DCAT metadata**

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/reasoning/
│
├── README.md                                        # This file — schema documentation
│
├── reasoning-dashboard-schema-v11.json              # JSON Schema definition
│
├── examples/                                        # Canonical reasoning anomaly payloads
│   ├── reasoning_chain_break_example.json
│   ├── contradiction_reasoning_example.json
│   └── causal_drift_reasoning_example.json
│
└── validators/                                      # Schema-validation utilities
    ├── validate_reasoning_schema.py
    └── run_all_validations.sh
```

---

# 🧩 Schema Requirements (v11)

The **Reasoning Anomaly Dashboard** JSON MUST include the following blocks.

---

## 1. 🧠 Model & Run Identification

Required top-level fields:

- `kfm_version`  
- `model_id` (e.g., `urn:kfm:model:focus_transformer_v3`)  
- `checkpoint_id`  
- `run_id`  
- `timestamp` (ISO 8601)  

---

## 2. 📖 Reasoning Context

Describes what reasoning artifacts are being evaluated:

- `reasoning_type` — e.g. `"focus_mode_chain"`, `"story_node_v3_causal"`, `"llm_explanation"`  
- `entity_scope` — list of entity URNs involved (persons, places, events)  
- `storynode_ids` — affected Story Node URNs (if any)  
- `sample_count` — number of reasoning samples/chains analyzed  

---

## 3. 🔗 Reasoning Chain Integrity Metrics

Captures structural quality of inference chains:

- `reasoning_chain_stability_index` (0.0–1.0)  
- `missing_step_count` — number of required but absent intermediate steps  
- `unsupported_jump_count` — leaps unsupported by graph/data  
- `chain_length_distribution` — summary statistics (min/mean/max)  

---

## 4. ⚠ Contradiction & Consistency Metrics

Tracks contradictions such as:

- `contradiction_burden_score` — overall contradiction load  
- `spatial_contradiction_score` — mutually exclusive spatial claims  
- `temporal_contradiction_score` — mutually exclusive time claims  
- `logical_conflict_score` — non-spatiotemporal logical conflicts  

---

## 5. 🧬 Causal Drift & Graph Deformation

Aligned with causal graphs and Neo4j relationships:

- `causal_drift_index` — deviation from reference causal graph  
- `parent_child_role_swap_count`  
- `spurious_causal_link_count`  
- `missing_required_causal_link_count`  

---

## 6. 🧠 Epistemic Stability & Uncertainty

Measures how well the model tracks uncertainty:

- `epistemic_stability_score` (0.0–1.0)  
- `overconfidence_index` — unsupported high-confidence reasoning  
- `hedging_adequacy_score` — appropriate use of hedging language  

---

## 7. 🧬 Graph Reasoning Coherence

Checks multi-hop reasoning over the knowledge graph:

- `graph_reasoning_coherence` (0.0–1.0)  
- `two_hop_coherence_score`  
- `three_hop_coherence_score`  
- `graph_safe_transition_violations`  

---

## 8. 🧡 CARE-S & Cultural Reasoning Safety

Mandatory ethics block:

- `care_flags[]` — list of triggered CARE-S conditions (e.g., `"heritage_speculation"`, `"cultural_causal_claim"`)  
- `care_violation` — boolean (`true` requires promotion_block)  
- `cultural_sensitivity_score` — 0.0–1.0  
- `reasoning_harm_risk` — 0.0–1.0 risk index  
- `notes_for_reviewers` — optional governance note  

**Any `care_violation: true` must cause `promotion_block: true`.**

---

## 9. ✍ Story Node v3 Integration (If Applicable)

For reasoning anomalies involving Story Nodes:

- `storynode_schema_valid` — boolean  
- `storynode_causal_block_valid` — boolean  
- `storynode_citation_coverage_pct` — fraction of steps with explicit provenance  
- `storynode_reasoning_coherence` — 0.0–1.0  

---

## 10. ♻ Sustainability & Telemetry (Optional but Recommended)

Tracks:

- `energy_wh`  
- `carbon_gco2e`  
- `telemetry_ref` — URN to compute/energy telemetry  
- `runtime_s` — evaluation runtime  

---

## 11. 🧬 Provenance (PROV-O)

Required block:

- `prov.agent` — evaluator agent URN  
- `prov.activity` — evaluation pipeline/activity URN  
- `prov.used[]` — datasets, models, or Story Nodes used  
- `prov.generated[]` — anomaly report URNs, derived artifacts  

---

## 12. 🛡 Governance Block

All reasoning anomaly dashboards must include:

- `governance.reviewer_role`  
- `governance.promotion_block`  
- `governance.override_allowed`  
- `governance.override_rationale` (if an override occurs)  

---

# 🛠 Example Reasoning Anomaly Payload (Simplified)

```json
{
  "kfm_version": "11.0.0",
  "model_id": "urn:kfm:model:focus_transformer_v3",
  "checkpoint_id": "ft3_ckpt_0047",
  "run_id": "urn:kfm:run:reasoning_eval:2025-11-21T20:05:00Z",
  "timestamp": "2025-11-21T20:05:33Z",
  "reasoning_type": "focus_mode_chain",
  "entity_scope": [
    "urn:kfm:entity:event:medicine_lodge_treaty_1867"
  ],
  "sample_count": 96,
  "reasoning_chain_metrics": {
    "reasoning_chain_stability_index": 0.89,
    "missing_step_count": 5,
    "unsupported_jump_count": 3
  },
  "contradiction_metrics": {
    "contradiction_burden_score": 0.11,
    "spatial_contradiction_score": 0.04,
    "temporal_contradiction_score": 0.05,
    "logical_conflict_score": 0.07
  },
  "causal_metrics": {
    "causal_drift_index": 0.13,
    "parent_child_role_swap_count": 2,
    "spurious_causal_link_count": 4,
    "missing_required_causal_link_count": 3
  },
  "epistemic_metrics": {
    "epistemic_stability_score": 0.86,
    "overconfidence_index": 0.10,
    "hedging_adequacy_score": 0.80
  },
  "graph_reasoning_metrics": {
    "graph_reasoning_coherence": 0.91,
    "two_hop_coherence_score": 0.93,
    "three_hop_coherence_score": 0.90,
    "graph_safe_transition_violations": 2
  },
  "storynode_metrics": {
    "storynode_schema_valid": true,
    "storynode_causal_block_valid": true,
    "storynode_citation_coverage_pct": 0.84,
    "storynode_reasoning_coherence": 0.89
  },
  "care": {
    "care_flags": ["heritage_speculation_risk"],
    "care_violation": true,
    "cultural_sensitivity_score": 0.72,
    "reasoning_harm_risk": 0.39,
    "notes_for_reviewers": "Generated causal claims about tribal decisions that are not explicitly supported by documented sources."
  },
  "telemetry_ref": "urn:kfm:telemetry:compute:run:reasoning_eval:2025-11-21T20:05:00Z",
  "prov": {
    "agent": "urn:kfm:agent:automated-reasoning-evaluator",
    "activity": "urn:kfm:activity:reasoning_eval_pipeline_v3",
    "used": [
      "urn:kfm:data:evaluation:reasoning_eval_set_v11",
      "urn:kfm:model:focus_transformer_v3:ft3_ckpt_0047"
    ],
    "generated": [
      "urn:kfm:report:reasoning_anomaly:ft3_ckpt_0047:2025-11-21T20:05:33Z"
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

# 🧪 Validation & CI Requirements

All reasoning anomaly payloads must pass:

- JSON Schema validation (`reasoning-dashboard-schema-v11.json`)  
- CARE-S cultural-safety enforcement  
- FAIR metadata completeness  
- PROV-O structural integrity  
- Telemetry reference checks (compute/energy/carbon)  
- STAC/DCAT mapping integrity for any attached anomaly datasets  

GitHub Actions enforcing this:

- `ai-anomaly-reasoning-schema-validate.yml`  
- `ai-reasoning-anomaly-dashboard-lint.yml`  
- `faircare-reasoning-review-gate.yml`  
- `stac-validate-anomaly-datasets.yml`

Any validation failure **blocks**:

- Model promotion  
- Story Node v3 auto-publishing  
- Dashboard publishing  

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-governance` | Initial creation of reasoning anomaly dashboard schema documentation for KFM v11. |

---

<div align="center">

**Kansas Frontier Matrix — Reasoning Anomaly Schema**  
*Logical Integrity · Ethical Reasoning · Provenance-Complete Intelligence*

[Back to AI Anomaly Schemas](../README.md) ·  
[FAIR+CARE Dashboard Template](../../../templates/faircare/README.md) ·  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
