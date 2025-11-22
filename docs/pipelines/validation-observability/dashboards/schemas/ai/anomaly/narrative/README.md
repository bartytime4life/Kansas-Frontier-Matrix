---
title: "📚 KFM AI Anomaly Schema — Narrative Integrity & Story Drift Dashboard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/narrative/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/ai/anomaly/narrative-dashboard-schema-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "AI-Anomaly-Schema"
intent: "ai-anomaly-narrative-schema"
semantic_document_id: "kfm-ai-anomaly-narrative-schema"
doc_uuid: "urn:kfm:schemas:ai:anomaly:narrative-dashboard:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Mixed-Risk (requires governance review)"
immutability_status: "version-pinned"
---

<div align="center">

# 📚 **KFM AI Anomaly Schema — Narrative Integrity & Story Drift Dashboard**  
`docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/narrative/README.md`

**Purpose:**  
Define the **canonical schema** and structural rules for all **Narrative Anomaly Dashboards** within the Kansas Frontier Matrix.  
This schema governs how **hallucinations**, **contradictions**, **unsafe cultural narratives**, **timeline/story drift**, and **Focus Mode v3 Story Node anomalies** are represented, validated, and surfaced across KFM observability dashboards.

</div>

---

# 📘 Overview

The **Narrative Anomaly Schema** standardizes reporting for reasoning and story-level failures in:

- Focus Mode v3 summaries  
- Story Node v3 generation  
- LLM-based explanations  
- Multi-modal narrative synthesis (text × map × timeline × graph)

Narrative anomalies include:

- Factual hallucinations  
- Contradictions and self-inconsistencies  
- Temporal/spatial storytelling errors  
- Epistemic overconfidence or unjustified speculation  
- CARE-S cultural/heritage violations  
- Provenance-breaking claims (not supported by data)  

This schema ensures that every narrative anomaly is:

- **FAIR+CARE-compliant**  
- **Provenance-rich (PROV-O)**  
- **Linked to sustainability telemetry**  
- **Aligned with Story Node v3 and STAC/DCAT metadata**

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/narrative/
│
├── README.md                                        # This file — schema documentation
│
├── narrative-dashboard-schema-v11.json              # JSON Schema definition
│
├── examples/                                        # Canonical narrative anomaly payloads
│   ├── hallucination_example.json
│   ├── contradiction_storynode_example.json
│   └── unsafe_cultural_narrative_example.json
│
└── validators/                                      # Schema-validation utilities
    ├── validate_narrative_schema.py
    └── run_all_validations.sh
```

---

# 🧩 Schema Requirements (v11)

The **Narrative Anomaly Dashboard** JSON MUST include the following blocks.

---

## 1. 🧠 Model & Run Identification

Required top-level fields:

- `kfm_version`  
- `model_id` (e.g., Focus Transformer v3 URN)  
- `checkpoint_id`  
- `run_id`  
- `timestamp` (ISO 8601)  

---

## 2. 📖 Narrative Context

Describes which narrative outputs are being evaluated:

- `narrative_type` — e.g. `"focus_summary"`, `"story_node_v3"`, `"llm_explanation"`  
- `entity_scope` — list of entity IDs the narrative is about (persons, places, events)  
- `storynode_ids` — affected Story Node URNs (if any)  
- `sample_count` — number of narrative samples assessed  

---

## 3. 🧩 Hallucination & Factuality Metrics

Captures fact-grounding quality:

- `hallucination_rate` — proportion of unsupported statements  
- `unsupported_claims_count`  
- `factuality_score` (0.0–1.0; 1.0 = fully supported)  
- `graph_alignment_score` — agreement with Neo4j knowledge graph  

---

## 4. ⚠ Contradiction & Consistency Metrics

Tracks:

- `internal_contradiction_score` — contradictions within a single narrative  
- `cross_story_conflict_score` — conflicting statements across narratives/Story Nodes  
- `chronology_conflict_score` — time-related contradictions  
- `spatial_conflict_score` — geospatial contradictions  

---

## 5. 🕰 Narrative Chronology & Spatiotemporal Grounding

Aligns with OWL-Time + GeoSPARQL:

- `temporal_grounding_score`  
- `spatial_grounding_score`  
- `timeline_integrity_score` — adherence to correct event ordering  
- `spatiotemporal_anomaly_flags[]` — e.g., `"time_impossible"`, `"location_out_of_bounds"`  

---

## 6. 🧠 Epistemic & Uncertainty Metrics

Measures:

- `epistemic_stability_score` — consistency of confidence & hedging  
- `overconfidence_index` — unsupported high-confidence claims  
- `hedging_adequacy_score` — proper signaling of uncertainty  

---

## 7. 🧡 CARE-S & Cultural Narrative Safety

Mandatory ethics block:

- `care_flags[]` — list of triggered CARE-S conditions (e.g. `"heritage_speculation"`)  
- `care_violation` — boolean (true if any violation)  
- `cultural_sensitivity_score` — 0.0–1.0  
- `narrative_harm_risk` — 0.0–1.0 risk index  
- `notes_for_reviewers` — optional explanation for human review  

**Any `care_violation: true` must lead to `promotion_block: true`.**

---

## 8. ✍ Story Node v3 Integrity (if applicable)

For Story Node outputs:

- `storynode_schema_valid` — boolean  
- `missing_spacetime_block` — boolean  
- `citation_coverage_pct` — fraction of sentences with provenance  
- `node_narrative_coherence` — 0.0–1.0  

---

## 9. ♻ Sustainability & Telemetry (Optional but Recommended)

Tracks:

- `energy_wh`  
- `carbon_gco2e`  
- `telemetry_ref` — URN to compute/energy telemetry  
- `runtime_s` — evaluation runtime  

---

## 10. 🧬 Provenance (PROV-O)

Required block:

- `prov.agent` — evaluator process or user  
- `prov.activity` — pipeline / dashboard run  
- `prov.used[]` — datasets, Story Nodes, or graphs used  
- `prov.generated[]` — anomaly reports / derived artifacts  

---

## 11. 🛡 Governance Block

All narrative anomaly dashboards must include:

- `governance.reviewer_role`  
- `governance.promotion_block`  
- `governance.override_allowed`  
- `governance.override_rationale` (if any override occurs)  

---

# 🛠 Example Narrative Anomaly Payload (Simplified)

```json
{
  "kfm_version": "11.0.0",
  "model_id": "urn:kfm:model:focus_transformer_v3",
  "checkpoint_id": "ft3_ckpt_0042",
  "run_id": "urn:kfm:run:narrative_eval:2025-11-21T18:30:00Z",
  "timestamp": "2025-11-21T18:30:22Z",
  "narrative_type": "focus_summary",
  "entity_scope": [
    "urn:kfm:entity:event:medicine_lodge_treaty_1867"
  ],
  "sample_count": 128,
  "hallucination_metrics": {
    "hallucination_rate": 0.09,
    "unsupported_claims_count": 17,
    "factuality_score": 0.86,
    "graph_alignment_score": 0.90
  },
  "consistency_metrics": {
    "internal_contradiction_score": 0.07,
    "cross_story_conflict_score": 0.05,
    "chronology_conflict_score": 0.02,
    "spatial_conflict_score": 0.03
  },
  "grounding_metrics": {
    "temporal_grounding_score": 0.93,
    "spatial_grounding_score": 0.91,
    "timeline_integrity_score": 0.92,
    "spatiotemporal_anomaly_flags": []
  },
  "epistemic_metrics": {
    "epistemic_stability_score": 0.89,
    "overconfidence_index": 0.08,
    "hedging_adequacy_score": 0.84
  },
  "storynode_metrics": {
    "storynode_schema_valid": true,
    "missing_spacetime_block": false,
    "citation_coverage_pct": 0.88,
    "node_narrative_coherence": 0.90
  },
  "care": {
    "care_flags": [],
    "care_violation": false,
    "cultural_sensitivity_score": 0.65,
    "narrative_harm_risk": 0.12,
    "notes_for_reviewers": "No explicit tribal-history speculation detected."
  },
  "telemetry_ref": "urn:kfm:telemetry:compute:run:narrative_eval:2025-11-21T18:30:00Z",
  "prov": {
    "agent": "urn:kfm:agent:automated-narrative-evaluator",
    "activity": "urn:kfm:activity:narrative_eval_pipeline_v3",
    "used": [
      "urn:kfm:data:evaluation:narrative_eval_set_v11",
      "urn:kfm:model:focus_transformer_v3:ft3_ckpt_0042"
    ],
    "generated": [
      "urn:kfm:report:narrative_anomaly:ft3_ckpt_0042:2025-11-21T18:30:22Z"
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

All narrative anomaly payloads must pass:

- JSON Schema validation (`narrative-dashboard-schema-v11.json`)  
- CARE-S compliance checks  
- FAIR metadata completeness checks  
- PROV-O integrity checks  
- Telemetry reference validation  
- STAC/DCAT mapping integrity (if used to describe anomaly datasets)  

GitHub Actions enforcing this:

- `ai-anomaly-narrative-schema-validate.yml`  
- `ai-narrative-anomaly-dashboard-lint.yml`  
- `faircare-narrative-review-gate.yml`  
- `stac-validate-anomaly-datasets.yml`

Any validation failure **blocks**:

- Model promotion  
- Story Node v3 auto-publishing  
- Dashboard deployment

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-governance` | Initial creation of narrative anomaly dashboard schema documentation for KFM v11. |

---

<div align="center">

**Kansas Frontier Matrix — Narrative Anomaly Schema**  
*Story Integrity · Historical Safety · Provenance-Complete Narratives*

[Back to AI Anomaly Schemas](../README.md) ·  
[FAIR+CARE Dashboard Template](../../../templates/faircare/README.md) ·  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
