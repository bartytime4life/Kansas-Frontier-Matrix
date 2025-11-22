---
title: "⚖️ KFM AI Bias Schema — Statistical Parity & Group Fairness Dashboard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/schemas/ai/bias/parity/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / FAIR+CARE Council & Autonomous Fairness Validators"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/ai/bias/parity-dashboard-schema-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "AI-Bias-Schema"
intent: "ai-bias-parity-schema"
semantic_document_id: "kfm-ai-bias-parity-schema"
doc_uuid: "urn:kfm:schemas:ai:bias:parity-dashboard:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Moderate-Risk (requires fairness & CARE-S review)"
immutability_status: "version-pinned"
---

<div align="center">

# ⚖️ **KFM AI Bias Schema — Statistical Parity & Group Fairness Dashboard**  
`docs/pipelines/validation-observability/dashboards/schemas/ai/bias/parity/README.md`

**Purpose:**  
Define the **canonical, enforced schema** for all **Statistical Parity & Group Fairness Dashboards** within the Kansas Frontier Matrix v11.  
This schema governs how **statistical parity**, **selection-rate fairness**, **group-level disparities**, **parity-gap drift**, and **CARE-S–aligned fairness expectations** must be recorded, validated, and surfaced across the KFM Validation & Observability system.

</div>

---

# 📘 Overview

The **Statistical Parity Schema** applies to all fairness dashboards analyzing:

- Group-based model outputs  
- Selection-rate disparity  
- Parity-gap variation across time  
- Inter-group fairness comparisons  
- Distribution-balanced decisions  
- CARE-S–relevant fairness issues  
- Sustainability-linked fairness anomalies  
- Embedding-leakage fairness risks  
- Focus Mode v3 demographic narrative parity  

This schema ensures:

- **FAIR+CARE governance compliance**  
- **Reproducible, PROV-O aligned parity estimates**  
- **Cross-dashboard consistency**  
- **Soft and hard violation thresholds**  
- **STAC/DCAT-compliant fairness metadata**  
- **Machine-extractable, CI-validated structures**

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/dashboards/schemas/ai/bias/parity/
│
├── README.md                                          # This file
│
├── parity-dashboard-schema-v11.json                   # Core JSON Schema definition
│
├── examples/                                          # Canonical parity evaluation payloads
│   ├── parity_basic_example.json
│   ├── parity_protected_attribute_multi.json
│   └── fairness_parity_drift_example.json
│
└── validators/                                        # CI schema-validation tools
    ├── validate_parity_schema.py
    └── run_all_validations.sh
```

---

# 🧩 Schema Requirements (v11)

The **Parity Dashboard JSON** MUST define the following blocks:

---

## 1. 🧠 Model & Run Identification

- `kfm_version`  
- `model_id`  
- `checkpoint_id`  
- `run_id`  
- `timestamp`  

---

## 2. 🧬 Protected Attributes & Groups

Required:

- `protected_attributes[]`  
- `groups[]` with:  
  - `group_id`  
  - `sample_size`  
  - `population_share`  
  - `selection_rate`  

---

## 3. ⚖ Statistical Parity Core Metrics

- `selection_rate_parity_gap`  
- `demographic_parity_gap`  
- `tpr_parity_gap` — True Positive Rate parity  
- `fpr_parity_gap` — False Positive Rate parity  
- `predictive_parity_gap` — Precision parity across groups  
- `overall_parity_score` — normalized 0.0–1.0 score  

---

## 4. 🧮 Derived Metrics & Thresholds

Includes:

- `parity_delta_from_baseline`  
- `parity_violation_flags[]`  
- `parity_severity_index`  
- `fairness_confidence` — confidence in disparity estimation  

---

## 5. 🌐 Spatiotemporal Parity Effects (Optional but Recommended)

To align with KFM’s geospatial + temporal nature:

- `spatial_parity_distribution[]`  
- `temporal_parity_drift[]`  
- `region_based_parity_gap`  
- `timeline_parity_gap`  

---

## 6. 🧠 Embedding-Parity Indicators (Optional)

Captures fairness issues hidden in latent space:

- `embedding_sensitivity_parity`  
- `latent_feature_parity_gap`  
- `vector_magnitude_disparity`  

---

## 7. 🧡 CARE-S Cultural Safety (Required)

CARE-S–specific parity concerns:

- `care_parity_flags[]`  
- `care_violation` (boolean)  
- `cultural_sensitivity_score`  
- `heritage_equity_index`  
- `notes_for_reviewers`  

**Any `care_violation: true` → immediate promotion block.**

---

## 8. ♻ Sustainability & Telemetry (ISO 50001 / 14064)

Bias anomalies often correlate with hardware or energy drift.

Parities may depend on:

- `energy_wh`  
- `carbon_gco2e`  
- `compute_spike_pct`  
- `telemetry_ref` — URN to compute/energy blob  

---

## 9. 🧬 PROV-O Provenance (Required)

- `prov.agent`  
- `prov.activity`  
- `prov.used[]` (datasets/models)  
- `prov.generated[]` (reports, dashboards)  

---

## 10. 🛡 Governance Block

- `reviewer_role`  
- `promotion_block`  
- `override_allowed`  
- `override_rationale`  

**Parity gaps exceeding threshold → `promotion_block: true`.**

---

# 🛠 Example Parity Payload (Simplified)

```json
{
  "kfm_version": "11.0.0",
  "model_id": "urn:kfm:model:focus_transformer_v3",
  "checkpoint_id": "ft3_ckpt_0048",
  "run_id": "urn:kfm:run:parity_eval:2025-11-21T19:20:00Z",
  "timestamp": "2025-11-21T19:20:31Z",
  "protected_attributes": ["region"],
  "groups": [
    {
      "group_id": "region:urban",
      "sample_size": 950,
      "population_share": 0.60,
      "selection_rate": 0.48
    },
    {
      "group_id": "region:rural",
      "sample_size": 650,
      "population_share": 0.40,
      "selection_rate": 0.29
    }
  ],
  "parity_metrics": {
    "selection_rate_parity_gap": 0.19,
    "demographic_parity_gap": 0.17,
    "tpr_parity_gap": 0.12,
    "fpr_parity_gap": 0.08,
    "predictive_parity_gap": 0.11,
    "overall_parity_score": 0.73,
    "parity_delta_from_baseline": -0.08
  },
  "care": {
    "care_parity_flags": ["collective-benefit-risk"],
    "care_violation": true,
    "cultural_sensitivity_score": 0.62,
    "heritage_equity_index": 0.44
  },
  "telemetry_ref": "urn:kfm:telemetry:compute:run:parity_eval:2025-11-21T19:20:00Z",
  "prov": {
    "agent": "urn:kfm:agent:automated-parity-evaluator",
    "activity": "urn:kfm:activity:parity_eval_pipeline_v3",
    "used": [
      "urn:kfm:data:evaluation:bias_parity_eval_set_v11",
      "urn:kfm:model:focus_transformer_v3:ft3_ckpt_0048"
    ],
    "generated": [
      "urn:kfm:report:parity_eval:ft3_ckpt_0048:2025-11-21T19:20:31Z"
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

All parity-dashboard JSON payloads MUST pass:

- JSON Schema validation (`parity-dashboard-schema-v11.json`)  
- FAIR+CARE compliance  
- PROV-O lineage integrity  
- Telemetry linkage consistency  
- STAC/DCAT metadata if representing parity datasets  
- SBOM consistency checks  

GitHub Actions enforcing:

- `ai-bias-parity-schema-validate.yml`  
- `ai-parity-dashboard-lint.yml`  
- `faircare-parity-review-gate.yml`  
- `stac-validate-anomaly-datasets.yml`

Failures **block**:

- Model promotion  
- Dashboard deployment  
- Focus Mode v3 narrative publishing  

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-governance` | Initial creation of Statistical Parity Dashboard Schema documentation. |

---

<div align="center">

**Kansas Frontier Matrix — Statistical Parity Schema**  
*Fairness · Equity · Provenance-Complete Governance*

[Back to Bias Schemas](../README.md) ·  
[FAIR+CARE Template](../../../templates/faircare/README.md) ·  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
