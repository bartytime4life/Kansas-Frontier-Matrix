---
title: "🎯 KFM AI Anomaly Schema — Bias & Fairness Dashboard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/bias/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/ai/anomaly/bias-dashboard-schema-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "AI-Anomaly-Schema"
intent: "ai-anomaly-bias-schema"
semantic_document_id: "kfm-ai-anomaly-bias-schema"
doc_uuid: "urn:kfm:schemas:ai:anomaly:bias-dashboard:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Mixed-Risk (ethics-review-required)"
immutability_status: "version-pinned"
---

<div align="center">

# 🎯 **KFM AI Anomaly Schema — Bias & Fairness Dashboard**  
`docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/bias/README.md`

**Purpose:**  
Define the **canonical JSON schema** and usage rules for **AI Bias & Fairness Anomaly Dashboards** in the Kansas Frontier Matrix v11.  
This schema governs how **bias metrics**, **fairness anomalies**, **CARE-S violations**, and **telemetry-linked bias events** are represented, validated, and surfaced across all KFM observability dashboards.

</div>

---

# 📘 Overview

The **AI Anomaly Bias Schema** standardizes how KFM records and visualizes:

- Bias anomalies in **ML/LLM/Focus Mode v3**  
- Group-level fairness metrics (e.g., parity, TPR/FPR gaps)  
- Demographic drift and representation imbalance  
- CARE-S cultural safety violations and warnings  
- Telemetry overlays (compute, energy, carbon) associated with biased behavior  
- Provenance and governance metadata for auditability  

This schema is consumed by:

- Bias/Drift dashboards under **Validation & Observability**  
- **FAIR+CARE Governance Dashboards** (templates/faircare)  
- Model Promotion Gate workflows  
- Sustainability and ethics-ledger tooling  

All dashboards referencing AI bias anomalies MUST adhere to this schema.

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/dashboards/schemas/ai/anomaly/bias/
│
├── README.md                                   # This file — schema documentation
│
├── ai-anomaly-bias-schema-v11.json             # JSON Schema (formal definition)
│
├── examples/                                   # Canonical bias anomaly examples
│   ├── bias_alert_simple.json
│   ├── bias_alert_multi_group.json
│   └── bias_with_care_violation.json
│
└── validators/                                 # Schema validation utilities
    ├── validate_ai_anomaly_bias_schema.py
    └── run_all_validations.sh
```

---

# 🧩 Schema Requirements (v11)

The **AI Anomaly Bias Dashboard** JSON must include:

## 1. 🧠 Model & Run Identification

- `kfm_version` (e.g., `"11.0.0"`)  
- `model_id` (URI / URN)  
- `checkpoint_id`  
- `run_id` (unique URN for the evaluation/anomaly run)  
- `timestamp` (ISO 8601)  

## 2. 👥 Group & Attribute Definition

- `protected_attributes`: list of attributes under analysis (e.g., `"gender"`, `"region"`, `"language"`)  
- `groups`: array of groups with:

  - `group_id` (e.g., `"gender:female"`)  
  - `population_share`  
  - `sample_size`  

## 3. ⚖ Bias & Fairness Metrics

Per group and globally:

- `selection_rate`  
- `true_positive_rate`, `false_positive_rate`  
- `precision`, `recall`, `f1`  
- `disparate_impact` (relative rate vs reference group)  
- `equal_opportunity_gap`  
- `demographic_parity_gap`  

Raised into:

- `bias_severity_index` (0.0–1.0, dashboard primary signal)  
- `fairness_confidence` (confidence in metrics)  

## 4. 🧡 CARE-S & Ethics Signals

- `care_flags`: array of CARE-S conditions triggered  
- `care_violation`: boolean  
- `cultural_sensitivity_score` (0.0–1.0; higher → more sensitive)  
- `narrative_risk_score` (for Focus Mode outputs)  
- `notes_for_reviewers`  

## 5. ♻ Telemetry & Sustainability

Optional but recommended:

- `telemetry_ref`: link to compute/energy telemetry blob  
- `energy_wh`, `carbon_gco2e` (optional summary fields)  

## 6. 🧬 Provenance & Governance

- `prov`: PROV-O structure containing:

  - `agent` (who/what executed the evaluation)  
  - `activity` (evaluation pipeline identifier)  
  - `used` (datasets/models involved)  
  - `generated` (anomaly report URNs)  

- `governance`:

  - `reviewer_role`  
  - `promotion_block` (boolean)  
  - `override_allowed` (boolean)  
  - `override_rationale` (if any)  

---

# 🛠 Example Bias Anomaly Payload (Simplified)

```json
{
  "kfm_version": "11.0.0",
  "model_id": "urn:kfm:model:focus_transformer_v3",
  "checkpoint_id": "ft3_ckpt_0042",
  "run_id": "urn:kfm:run:eval:bias:2025-11-21T18:12:00Z",
  "timestamp": "2025-11-21T18:12:45Z",
  "protected_attributes": ["region"],
  "groups": [
    {
      "group_id": "region:urban",
      "population_share": 0.60,
      "sample_size": 1200,
      "selection_rate": 0.44,
      "true_positive_rate": 0.82,
      "false_positive_rate": 0.11
    },
    {
      "group_id": "region:rural",
      "population_share": 0.40,
      "sample_size": 800,
      "selection_rate": 0.23,
      "true_positive_rate": 0.63,
      "false_positive_rate": 0.18
    }
  ],
  "metrics": {
    "disparate_impact": 0.52,
    "equal_opportunity_gap": 0.19,
    "demographic_parity_gap": 0.21,
    "bias_severity_index": 0.27,
    "fairness_confidence": 0.93
  },
  "care": {
    "care_flags": ["collective-benefit-risk", "authority-to-control-risk"],
    "care_violation": true,
    "cultural_sensitivity_score": 0.78,
    "narrative_risk_score": 0.31,
    "notes_for_reviewers": "Urban/rural split suggests systematic under-selection in rural treaty narratives."
  },
  "telemetry_ref": "urn:kfm:telemetry:compute:run:eval:bias:2025-11-21T18:12:00Z",
  "prov": {
    "agent": "urn:kfm:agent:automated-bias-evaluator",
    "activity": "urn:kfm:activity:bias_eval_pipeline_v3",
    "used": [
      "urn:kfm:data:evaluation:focus_eval_set_v11",
      "urn:kfm:model:focus_transformer_v3:ft3_ckpt_0042"
    ],
    "generated": [
      "urn:kfm:report:bias:ft3_ckpt_0042:2025-11-21T18:12:45Z"
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

Every AI anomaly bias dashboard payload MUST:

- Validate against `ai-anomaly-bias-schema-v11.json`  
- Provide all **required fields** above (no omissions)  
- Include at least one `protected_attributes` entry  
- Register all non-zero disparity metrics when bias is present  
- Annotate CARE-S flags for any sensitive or cultural aspects  
- Include `prov` and `governance` sections  

GitHub Actions workflows:

- `ai-anomaly-bias-schema-validate.yml`  
- `ai-anomaly-bias-dashboard-lint.yml`  
- `faircare-bias-review-gate.yml`  

Any failing validation **blocks**:

- Dashboard updates  
- Model promotion pipelines depending on these reports  

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-governance` | Initial creation of AI bias anomaly dashboard schema documentation for KFM v11. |

---

<div align="center">

**Kansas Frontier Matrix — AI Bias Anomaly Schema**  
*Fairness · Cultural Safety · Provenance-Complete Governance*

[Back to AI Anomaly Schemas](../README.md) ·  
[FAIR+CARE Dashboard Template](../../../templates/faircare/README.md) ·  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
