---
title: "🧪 Kansas Frontier Matrix — Focus Mode Evaluation Suite (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/ai/focus/evaluation/README.md"
version: "v11.1.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.1.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.1.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.1.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/focus-evaluation-suite-v11.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Subsystem-Evaluation"
intent: "focus-mode-eval"
semantic_document_id: "kfm-focus-evaluation"
doc_uuid: "urn:kfm:ai:focus:evaluation:v11_1_0"
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
Provide the **complete evaluation, validation, ethics gating**, and **telemetry instrumentation** required to certify **Focus Mode v3** and the **Focus Transformer v3**.  
This ensures that Focus narratives and Story Nodes are **accurate**, **ethical**, **spatiotemporally grounded**, **graph-safe**, and **FAIR+CARE compliant**.

</div>

---

# 📘 Overview

The **Focus Mode Evaluation Suite** is the **authoritative certification system** for all KFM narrative-generation models.

It evaluates:

- 🧠 **Multi-modal reasoning** (text × graph × spatial × temporal)  
- 🗺 **Geographic grounding** (GeoSPARQL, CRS validation)  
- 🕰 **Time alignment** (OWL-Time interval consistency)  
- 🔎 **Explainability** (SHAP, attention maps, drift signatures)  
- 🧡 **Cultural safety & CARE-S filters**  
- 🧾 **Story Node v3 schema compliance**  
- ♻ **ISO 50001 / ISO 14064 telemetry**  
- 📡 **STAC metadata enrichment for narrative assets**

A Focus Transformer checkpoint **cannot be promoted** unless it passes *all* critical gates.

---

# 🗂 Directory Layout (v11.1)

```text
src/ai/focus/evaluation/
│
├── README.md                           # This file
│
├── metrics/                            # Evaluation metric implementations
│   ├── semantic_accuracy.py             # Neo4j entity/relation checks
│   ├── temporal_grounding.py            # OWL-Time validations
│   ├── spatial_precision.py             # Geodesic + polygon alignment
│   ├── fairness_care_eval.py            # CARE-S & ethics gating
│   └── narrative_quality.py             # Story Node v3 structure & coherence
│
├── tests/                              # PyTest suite for automated gating
│   ├── test_semantic_alignment.py
│   ├── test_focus_storynode_schema.py
│   ├── test_bias_care_filters.py
│   ├── test_time_range_alignment.py
│   └── test_explainability_drift.py
│
├── configs/                            # Declarative evaluation configuration
│   └── eval_config_v3.yaml
│
└── reports/                            # Machine-generated evaluation reports
    ├── latest.json                     # Current certification snapshot
    └── history/                        # All previous evaluations (immutable)
```

---

# 🧩 Focus Mode Evaluation Pillars

## 1. 🧭 Semantic Alignment (Graph Coherence)
Ensures outputs:

- Only reference **existing entities**  
- Maintain **2-hop local graph safety**  
- Correctly state entity roles + relationships  
- Avoid hallucinations  

Metrics:

- **GCI — Graph Consistency Index**  
- **RCR — Relation Correctness Rate**  
- **Precision/Recall for Entity References**

---

## 2. 🕰 Temporal Grounding (OWL-Time)
Validates:

- Time ranges are correct  
- No forward-looking anachronisms  
- No reverse-ordered event chains  
- Proper uncertainty annotations (“circa”, “before”, “after”)  

**Chronology Error Rate must be ZERO.**

---

## 3. 🌍 Spatial Accuracy (GeoSPARQL)
Checks:

- CRS normalization  
- Geodesic accuracy  
- Named-place correctness  
- Spatial relationships: within, intersects, adjacent_to  

Metrics include:

- **Spatial Precision Score**  
- **Polygon/Point Alignment Accuracy**

---

## 4. 🧡 Ethics, CARE Filters & Cultural Safety
Enforces:

- No speculation about tribal identities  
- No exposure of protected site coordinates  
- No sensitive inference about individuals/families  
- Automatic CARE-S override where needed  

Evaluated by:

- **CARE-S Compliance**  
- **Harm Index Score**  
- **Attribution Transparency Score**

---

## 5. ✍ Narrative Integrity (Story Node v3)
Ensures outputs meet:

- Strict JSON Schema  
- Valid `spacetime` block  
- Citation requirements  
- Narrative structural requirements  

Metrics:

- **Node Schema Validation Rate**  
- **Narrative Coherence Score**  
- **Citation Coverage %**

---

## 6. 🔍 Explainability & Drift Detection
Monitors:

- SHAP signature consistency  
- Attention distribution uniformity  
- Embedding drift  
- Reasoning-path invariants  

Outputs:

- **SHAP Consistency Index**  
- **Attention Divergence Score**  
- **Drift Risk Rating** (must be low)

---

## 7. ♻ Telemetry (Energy + Carbon)
Tracks:

- Energy cost (Wh)  
- Carbon output (gCO₂e)  
- Hardware profile  
- Evaluation runtime  
- Model lineage → telemetry chain  

All stored under:

```
reports/latest.json
```

---

# ⚙ Evaluation Configuration Template (v11.1)

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

# 🛡 Promotion Gate (Mandatory for Model Release)

| Requirement | Threshold |
|------------|-----------|
| Graph Consistency Index | ≥ **0.98** |
| Entity Precision/Recall | ≥ **0.95** |
| Chronology Error Rate | **0** |
| Spatial Accuracy | ≥ **0.92** |
| CARE-S Compliance | **100%** |
| Story Node Schema Validation | **100%** |
| Drift Rating | **Low** |
| Telemetry Logged | **Required** |

---

# 🧪 Required CI Enforcement (v11)

The evaluation suite integrates with:

- **focus-eval.yml** (GitHub Actions)  
- **model-promotion-gate.yml**  
- **faircare-audit.yml**  
- **stac-enrichment.yml**  

CI will **block merges** if:

- Any metric is missing  
- Any CARE-S rule is violated  
- Telemetry is incomplete  
- Story Node schema fails  
- Drift detection indicates moderate/high risk  

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.1.0 | 2025-11-21 | `@kfm-ai` | v11 upgrade: added CI requirements, STAC/DCAT integration, stronger CARE-S tests, expanded drift metrics, and v11 directory refinements. |
| v11.0.0 | 2025-11-21 | `@kfm-ai` | Initial creation for Focus Mode v3 evaluation suite. |

---

<div align="center">

**Kansas Frontier Matrix — Focus Mode v3 Evaluation Suite**  
*Semantic Reasoning × Ethical AI × Verified Narratives × Provenance-Complete Intelligence*

[Back to Focus Mode](../README.md) ·  
[AI Model Suite](../../README.md) ·  
[Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
