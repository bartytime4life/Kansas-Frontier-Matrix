---
title: "🧭 KFM AI Anomaly Schema — Out-of-Distribution (OOD) Detection Dashboard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/ood/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / FAIR+CARE Council & Autonomous Validators"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/ai/anomaly/ood-dashboard-schema-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "AI-Anomaly-Schema"
intent: "ai-anomaly-ood-schema"
semantic_document_id: "kfm-ai-anomaly-ood-schema"
doc_uuid: "urn:kfm:schemas:ai:anomaly:ood-dashboard:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "High-Risk (strict CARE-S enforcement)"
immutability_status: "version-pinned"
---

<div align="center">

# 🧭 **KFM AI Anomaly Schema — Out-of-Distribution (OOD) Detection Dashboard**  
`docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/ood/README.md`

**Purpose:**  
Define the **official schema** for all **OOD Anomaly Dashboards** in the Kansas Frontier Matrix.  
This schema governs how **novel inputs**, **semantic unknowns**, **spatiotemporal outliers**, **Focus Mode v3 OOD narratives**, and **zero-shot failure modes** must be logged, validated, governed, and surfaced in dashboards.

</div>

---

# 📘 Overview

OOD anomalies are among the **highest-risk signals** in the KFM AI stack.

This schema standardizes:

- Distribution-shift detection  
- Semantic-OOD signals  
- Spatiotemporal out-of-range detection  
- Zero-shot hallucination tracking  
- Focus Mode v3 narrative-OOD analysis  
- Raster/vector/graph embedding OOD divergence  
- Hardware/compute OOD correlations  
- CARE-S cultural-risk OOD red flags  
- Telemetry-linked OOD events  
- STAC/DCAT metadata generation for OOD anomaly datasets  
- PROV-O lineage chains for reproducibility  

All dashboards using OOD analysis **must** conform to this schema.

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/ood/
│
├── README.md                                       # This file — schema documentation
│
├── ood-dashboard-schema-v11.json                   # JSON Schema definition
│
├── examples/                                       # Canonical OOD anomaly event payloads
│   ├── ood_distribution_example.json
│   ├── ood_semantic_example.json
│   └── ood_spatiotemporal_example.json
│
└── validators/                                     # CI validation utilities
    ├── validate_ood_schema.py
    └── run_all_validations.sh
```

---

# 🧩 Schema Requirements (v11)

The **OOD Anomaly Dashboard** JSON MUST define the following blocks:

---

## 1. 🧠 Model & Run Identification
- `kfm_version`  
- `model_id`  
- `checkpoint_id`  
- `run_id`  
- `timestamp` (ISO 8601)  

---

## 2. 🧭 OOD Dimensions
Each OOD report must specify which OOD domains triggered anomalies:

- `distribution_shift`  
- `semantic_ood`  
- `spatiotemporal_ood`  
- `narrative_ood` (for Focus Mode v3 / Story Nodes)  
- `explainability_ood`  
- `embedding_ood`  
- `zero_shot_failure`  
- `energy_compute_ood`  

At least **one** domain is required.

---

## 3. 📈 Distribution Shift Metrics
Includes:

- `distribution_divergence_score`  
- `novel_cluster_density`  
- `probability_mass_outside_training`  

---

## 4. 🧬 Semantic OOD Metrics
Tracks:

- `semantic_out_of_domain_index`  
- `novel_concept_activation_rate`  
- `topic_shift_score`  
- `domain_boundary_violation_score`  

---

## 5. 🛰 Spatiotemporal OOD Metrics
Aligned with OWL-Time + GeoSPARQL:

- `spatiotemporal_integrity_score`  
- `location_out_of_bounds` (boolean)  
- `temporal_out_of_bounds` (boolean)  
- `spatial_outlier_distance_km`  
- `year_outlier_distance`  

---

## 6. 📚 Narrative OOD Metrics (Focus Mode v3)
For narrative-generating models:

- `narrative_ood_instability`  
- `hallucinated_entities_count`  
- `unsupported_geographic_claims`  
- `unsupported_temporal_claims`  
- `narrative_zero_shot_anomalies`  

---

## 7. 🔍 Explainability OOD
Uses:

- `explainability_surprise_index`  
- `shap_feature_emergence_rate`  
- `attention_head_outlier_score`  

---

## 8. 🧡 CARE-S Cultural Safety (Required)
Mandatory block:

- `care_flags[]` — triggered cultural-risk signals  
- `care_violation` — **true = automatic promotion block**  
- `cultural_sensitivity_score`  
- `narrative_harm_risk`  
- `notes_for_reviewers`  

Any CARE-S violation MUST block evaluation and promotion.

---

## 9. ♻ Sustainability & Telemetry (ISO Compliance)
Optional but strongly encouraged:

- `energy_wh`  
- `carbon_gco2e`  
- `compute_spike_pct`  
- `telemetry_ref` (URN reference to compute/energy blob)

---

## 10. 🧬 PROV-O Provenance (Required)
Includes:

- `prov.agent`  
- `prov.activity`  
- `prov.used[]`  
- `prov.generated[]`  

Ensures complete reproducibility and traceability.

---

## 11. 🛡 Governance Block
- `reviewer_role`  
- `promotion_block`  
- `override_allowed`  
- `override_rationale`  

---

# 🛠 Example OOD Anomaly Payload (Simplified)

```json
{
  "kfm_version": "11.0.0",
  "model_id": "urn:kfm:model:focus_transformer_v3",
  "checkpoint_id": "ft3_ckpt_0045",
  "run_id": "urn:kfm:run:ood:2025-11-21T19:10:00Z",
  "timestamp": "2025-11-21T19:10:44Z",
  "ood": {
    "distribution_divergence_score": 0.28,
    "semantic_out_of_domain_index": 0.17,
    "spatiotemporal_integrity_score": 0.88,
    "temporal_out_of_bounds": true,
    "spatial_outlier_distance_km": 412.3,
    "narrative_ood_instability": 0.21,
    "explainability_surprise_index": 0.14
  },
  "care": {
    "care_flags": ["heritage_speculation_risk"],
    "care_violation": true,
    "cultural_sensitivity_score": 0.73,
    "narrative_harm_risk": 0.42
  },
  "telemetry_ref": "urn:kfm:telemetry:compute:run:ood:2025-11-21T19:10:00Z",
  "prov": {
    "agent": "urn:kfm:agent:automated-ood-evaluator",
    "activity": "urn:kfm:activity:ood_eval_pipeline_v3",
    "used": [
      "urn:kfm:data:evaluation:focus_eval_set_v11",
      "urn:kfm:model:focus_transformer_v3:ft3_ckpt_0045"
    ],
    "generated": [
      "urn:kfm:report:ood:ft3_ckpt_0045:2025-11-21T19:10:44Z"
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

AI OOD anomaly dashboard payloads must pass:

- JSON Schema check (`ood-dashboard-schema-v11.json`)  
- CARE-S cultural-risk validation  
- FAIR metadata completeness  
- PROV-O integrity  
- STAC/DCAT mapping validation  
- Telemetry cross-checks (compute/energy/carbon)  
- SBOM/manifest lineage checks  

Enforced by GitHub Actions:

- `ai-anomaly-ood-schema-validate.yml`  
- `ai-ood-dashboard-lint.yml`  
- `faircare-ood-review-gate.yml`  
- `stac-validate-anomaly-datasets.yml`

Failures **block**:

- Model promotion  
- Dashboard publishing  
- Story Node auto-publishing  

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-governance` | Initial creation of OOD anomaly dashboard schema documentation for KFM v11. |

---

<div align="center">

**Kansas Frontier Matrix — OOD Anomaly Schema**  
*Boundary Awareness · Safety · Provenance-Complete Intelligence*

[Back to AI Anomaly Schemas](../README.md) ·  
[FAIR+CARE Dashboard Template](../../../templates/faircare/README.md) ·  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
