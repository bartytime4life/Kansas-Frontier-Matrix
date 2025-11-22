---
title: "🧪 Kansas Frontier Matrix — Focus Mode Evaluation Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/ai/focus/evaluation/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/focus-evaluation-suite-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Subsystem-Evaluation"
intent: "focus-mode-eval"
semantic_document_id: "kfm-focus-evaluation"
doc_uuid: "urn:kfm:ai:focus:evaluation:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Low-Risk / Public"
immutability_status: "version-pinned"
---

<div align="center">

# 🧪 **Kansas Frontier Matrix — Focus Mode Evaluation Suite**  
`src/ai/focus/evaluation/README.md`

**Purpose:**  
Define the full evaluation, validation, bias-testing, safety-gating, and telemetry instrumentation used to certify **Focus Mode v3** and the **Focus Transformer** models.  
This suite measures *semantic accuracy*, *spatiotemporal grounding*, *narrative ethics*, *CARE safety*, *model drift*, *carbon/energy budgets*, and *Story Node v3 compliance*.

</div>

---

# 📘 Overview

The **Focus Mode Evaluation Suite** provides a unified testing harness for:

- **Focus Transformer v3** (multi-modal: text + timeline + geography + graph)
- **Story Node generation & narrative linking**
- **Semantic entity alignment** with the Neo4j knowledge graph
- **Temporal grounding** (OWL-Time)
- **Spatial grounding** (GeoSPARQL)
- **Narrative ethics & cultural safety** (FAIR+CARE)
- **AI explainability** (SHAP, LIME, attention audit)
- **Telemetry emissions** (ISO 50001 energy, ISO 14064 carbon)

All evaluations must pass before a Focus Transformer checkpoint can be promoted or deployed.

---

# 🗂 Directory Layout

```text
src/ai/focus/evaluation/
│
├── README.md                           # This file — documentation for the evaluation suite
│
├── metrics/                            # Metric definitions, calculators, scoring schemas
│   ├── semantic_accuracy.py
│   ├── temporal_grounding.py
│   ├── spatial_precision.py
│   ├── fairness_care_eval.py
│   └── narrative_quality.py
│
├── tests/                              # Automated tests
│   ├── test_semantic_alignment.py
│   ├── test_focus_storynode_schema.py
│   ├── test_bias_care_filters.py
│   ├── test_time_range_alignment.py
│   └── test_explainability_drift.py
│
├── configs/                            # Evaluation configuration templates
│   └── eval_config_v3.yaml
│
└── reports/                            # Auto-generated evaluation outputs
    ├── latest.json
    └── history/
```

---

# 🧩 Focus Mode Evaluation Pillars

## 1. 🧭 Semantic Alignment (Knowledge Graph Coherence)
Ensures that Focus summaries and Story Nodes:

- Correctly reference Neo4j entities  
- Avoid hallucinated people, places, or events  
- Maintain 2-hop graph coherence  
- Match canonical entity labels, dates, and relations  

Scored via:

- ❇ Graph Consistency Index (GCI)  
- ❇ Entity Precision/Recall  
- ❇ Relation Correctness Rate (RCR)  

---

## 2. 🕰 Temporal Grounding (OWL-Time Compliance)
Tests ensure generated narratives:

- Obey historical time bounds  
- Correctly express eras, ranges, and uncertainties  
- Respect event chronologies  
- Do not imply future knowledge about past entities  

Metrics:

- ❇ Time Consistency Score  
- ❇ Chronology Error Rate (must be zero for promotion)  

---

## 3. 🌍 Spatial Accuracy (GeoSPARQL)
Evaluates:

- Spatial footprint correctness  
- Place-to-entity relationships  
- Relative spatial reasoning (e.g., “west of”, “within watershed”)  
- Polygon/point alignment  

Metrics:

- ❇ Spatial Precision Score  
- ❇ Geodesic Reasoning Accuracy  

---

## 4. 🧡 Ethics, CARE Filters & Cultural Safety
Ensures narratives:

- Do **not** infer sensitive tribal histories  
- Mask restricted sites  
- Avoid speculation about heritage or identities  
- Provide transparency for uncertainties  

Safety Tests:

- ❇ CARE-S Compliance  
- ❇ Harm-Score (must pass threshold)  
- ❇ Cultural Attribution Accuracy  

---

## 5. ✍ Narrative Integrity (Story Node v3)
Ensures generated Story Nodes:

- Match strict JSON schema  
- Contain valid `spacetime` geometry + time ranges  
- Provide citations for all factual claims  
- Conform to narrative section rules  

Metrics:

- ❇ Node Schema Validation Rate  
- ❇ Narrative Coherence Score  
- ❇ Citation Coverage %

---

## 6. 🔍 Explainability & Drift Detection
Evaluates:

- SHAP signature stability  
- Textual + spatial attention maps  
- Drift of embeddings or model weights  
- Change in reasoning path quality  

Outputs:

- ❇ SHAP Consistency Index  
- ❇ Attention Divergence Score  
- ❇ Drift Risk Rating  

---

## 7. ♻ Telemetry (Energy/Carbon)
Every evaluation run emits:

- Energy consumed (Wh)  
- Carbon emissions (gCO₂e)  
- Hardware profile  
- Evaluation time  
- Model version → telemetry lineage  

All metrics stored in:

```
src/ai/focus/evaluation/reports/latest.json
```

---

# ⚙ Evaluation Configuration Template

```yaml
evaluation:
  model_checkpoint: "../../../models/focus_transformer_v3/checkpoints/ft3.ckpt"
  dataset: "../../../data/processed/focus_eval_set.json"
  strict_mode: true

metrics:
  semantic_alignment: true
  spatial_precision: true
  temporal_grounding: true
  narrative_integrity: true
  fairness_care: true
  explainability: true
  telemetry: true

telemetry:
  write_reports: true
  output_path: "../reports/latest.json"
  iso_50001: true
  iso_14064: true

governance:
  reviewer: "@faircare-council"
  require_human_approval: true
  governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
```

---

# 🛠 Promotion Gate (v11)

A Focus Transformer checkpoint can **ONLY** be promoted if:

| Requirement | Threshold |
|------------|-----------|
| Graph Consistency Index | ≥ 0.98 |
| Entity Precision/Recall | ≥ 0.95 |
| Time Error Rate | 0 |
| Spatial Accuracy | ≥ 0.92 |
| CARE-S Compliance | 100% |
| Story Node Schema Valid | 100% |
| Drift Risk Rating | Low |
| Telemetry Logged | Required |

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-ai` | Initial v11-compliant evaluation suite README creation; added CARE safety tests, Story Node v3 checks, drift evaluation, and telemetry integration. |

---

<div align="center">

**Kansas Frontier Matrix — Focus Mode v3 Evaluation Suite**  
*Semantic Reasoning × Ethical AI × Verified Narratives*

[Back to Focus Mode](../README.md) ·  
[AI Model Suite](../../README.md) ·  
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

