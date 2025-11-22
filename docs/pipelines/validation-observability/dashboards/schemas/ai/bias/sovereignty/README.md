---
title: "🪶 KFM AI Bias Schema — Indigenous Data Sovereignty & Cultural Authority Dashboard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/dashboards/schemas/ai/bias/sovereignty/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly / FAIR+CARE Council & Tribal Sovereignty Board"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/ai/bias/sovereignty-dashboard-schema-v11.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "AI-Bias-Schema"
intent: "ai-bias-sovereignty-schema"
semantic_document_id: "kfm-ai-bias-sovereignty-schema"
doc_uuid: "urn:kfm:schemas:ai:bias:sovereignty-dashboard:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Highest-Risk (CARE-S Sovereignty Enforcement)"
immutability_status: "version-pinned"
---

<div align="center">

# 🪶 **KFM AI Bias Schema — Indigenous Data Sovereignty & Cultural Authority Dashboard**  
`docs/pipelines/validation-observability/dashboards/schemas/ai/bias/sovereignty/README.md`

**Purpose:**  
Define the **official schema** used for **Sovereignty-Aligned Bias Dashboards**, governing detection of:  
- Indigenous data misuse  
- Cultural authority violations  
- Unauthorized inference about tribal heritage, identity, or history  
- Misrepresentation of sovereign nations  
- Land/territory misattribution  
- CARE-S (Sovereignty) high-risk cultural harms  
- AI reasoning or narratives that exceed documented tribal sources  
- FAIR+CARE sovereignty policy breaches  

This is the highest-risk category in KFM ethics governance.

</div>

---

# 📘 Overview

The **Sovereignty Bias Schema** applies to all AI outputs affecting:

- Indigenous nations  
- Tribal historical presence  
- Treaty references  
- Land attribution  
- Cultural knowledge  
- Story Nodes connected to tribal entities  
- Focus Mode v3 narratives referencing Indigenous topics  
- Any geospatial or temporal mapping involving Native nations  

AI systems must not:

- Invent or speculate about tribal identities  
- Attribute motives/actions without documented sources  
- Misstate treaty boundaries  
- Imply lineage or cultural connections  
- Expose sensitive archaeological or cultural sites  
- Override tribal authority to define their own history  

This schema enforces **CARE-S**: *Collective Benefit, Authority to Control, Responsibility, Ethics (Sovereignty)*.

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/dashboards/schemas/ai/bias/sovereignty/
│
├── README.md                                          # This file — schema documentation
│
├── sovereignty-dashboard-schema-v11.json              # JSON Schema definition
│
├── examples/                                          # Canonical sovereignty-bias payloads
│   ├── tribal_misattribution_example.json
│   ├── treaty_boundary_misstatement.json
│   └── cultural_authority_violation.json
│
└── validators/                                        # CI validation tooling
    ├── validate_sovereignty_schema.py
    └── run_all_validations.sh
```

---

# 🧩 Schema Requirements (v11)

The **Sovereignty Bias Dashboard JSON** MUST include:

---

## 1. 🧠 Model & Run Identification
- `kfm_version`  
- `model_id`  
- `checkpoint_id`  
- `run_id`  
- `timestamp`  

---

## 2. 🪶 Tribal / Cultural Context
Required fields:

- `tribal_entities[]` — URNs of affected nations  
- `sovereignty_scope` — `"nation" | "community" | "heritage" | "territory" | "treaty"`  
- `storynode_ids[]` — Story Nodes involved  
- `narrative_type` — `"focus_summary" | "story_node_v3" | "explanation"`  
- `sample_count`  

---

## 3. ⚠ Sovereignty Violation Metrics (High-Risk)
Track violations of tribal authority or cultural misrepresentation:

- `sovereignty_violation_score` (0.0–1.0)  
- `unauthorized_heritage_claims`  
- `misattributed_tribal_identity_count`  
- `territory_misattribution_score`  
- `treaty_misstatement_count`  
- `cultural_knowledge_unverified_count`  
- `forbidden_site_references` (masked by CARE-S)  

**Any non-zero violation triggers promotion block.**

---

## 4. 🧭 Spatiotemporal Sovereignty Integrity
Spatial + temporal grounding must match documented tribal history:

- `spatial_sovereignty_conflict_score`  
- `temporal_sovereignty_conflict_score`  
- `historical_presence_mismatch`  
- `territorial_boundary_conflict[]`  

Aligned with:

- GeoSPARQL  
- OWL-Time  
- Treaty metadata  

---

## 5. 🎙 Narrative & Semantic Bias (Tribal Context)
Required narrative-level metrics:

- `narrative_bias_score`  
- `cultural_authority_misrepresentation`  
- `harm_amplification_risk`  
- `erasure_bias_score`  
- `exoticization_or_stereotype_score`  
- `semantic_drift_sovereignty_index`  

---

## 6. 🧡 CARE-S Cultural Safety Block (Mandatory)
A sovereign-level ethics block:

- `care_flags[]`  
- `care_violation` — **must be TRUE if ANY sovereignty risk exists**  
- `sovereignty_risk_index` (0.0–1.0)  
- `cultural_sensitivity_score`  
- `notes_for_reviewers`  

CARE-S sovereign-level flags include:

- `"unauthorized-cultural-claim"`  
- `"heritage-speculation"`  
- `"misattributed-identity"`  
- `"protected-site-leakage"`  
- `"treaty-boundary-error"`  
- `"sovereign-authority-violation"`

---

## 7. 🧬 PROV-O Provenance (Required)
Required fields:

- `prov.agent`  
- `prov.activity`  
- `prov.used[]` (datasets/models used)  
- `prov.generated[]` (sovereignty-bias reports)  

Ensures reproducibility for governance review.

---

## 8. ♻ Telemetry & Sustainability (Optional)
For correlation with hardware drift:

- `energy_wh`  
- `carbon_gco2e`  
- `telemetry_ref` — URN pointing to compute/energy blob  

---

## 9. 🛡 Governance Metadata (Required)
- `reviewer_role` (must include tribal governance reviewers when applicable)  
- `promotion_block`  
- `override_allowed`  
- `override_rationale`  

**CARE-S sovereignty violations cannot be automatically overridden. Only Tribal Sovereignty Board may intervene.**

---

# 🛠 Example Sovereignty Bias Payload (Simplified)

```json
{
  "kfm_version": "11.0.0",
  "model_id": "urn:kfm:model:focus_transformer_v3",
  "checkpoint_id": "ft3_ckpt_0052",
  "run_id": "urn:kfm:run:sovereignty_eval:2025-11-21T20:25:00Z",
  "timestamp": "2025-11-21T20:25:41Z",
  "tribal_entities": ["urn:kfm:tribe:kaw_nation"],
  "sovereignty_scope": "heritage",
  "narrative_type": "focus_summary",
  "sample_count": 32,
  "sovereignty_metrics": {
    "sovereignty_violation_score": 0.22,
    "unauthorized_heritage_claims": 3,
    "misattributed_tribal_identity_count": 1,
    "territory_misattribution_score": 0.14,
    "treaty_misstatement_count": 0,
    "forbidden_site_references": 1
  },
  "spatiotemporal_sovereignty": {
    "spatial_sovereignty_conflict_score": 0.19,
    "temporal_sovereignty_conflict_score": 0.11
  },
  "narrative_bias": {
    "narrative_bias_score": 0.17,
    "cultural_authority_misrepresentation": 0.22
  },
  "care": {
    "care_flags": [
      "unauthorized-cultural-claim",
      "misattributed-identity"
    ],
    "care_violation": true,
    "sovereignty_risk_index": 0.33,
    "cultural_sensitivity_score": 0.71
  },
  "telemetry_ref": "urn:kfm:telemetry:compute:run:sovereignty_bias:2025-11-21T20:25:00Z",
  "prov": {
    "agent": "urn:kfm:agent:sovereignty-evaluator",
    "activity": "urn:kfm:activity:sovereignty_eval_pipeline_v3",
    "used": [
      "urn:kfm:data:evaluation:narrative_eval_set_v11",
      "urn:kfm:model:focus_transformer_v3:ft3_ckpt_0052"
    ],
    "generated": [
      "urn:kfm:report:sovereignty_bias:ft3_ckpt_0052:2025-11-21T20:25:41Z"
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

Payloads MUST pass:

- JSON Schema validation (`sovereignty-dashboard-schema-v11.json`)  
- CARE-S Sovereignty rule enforcement  
- FAIR metadata validation  
- PROV-O lineage integrity  
- Telemetry linkage validation  
- STAC/DCAT metadata correctness  
- SBOM integrity (model/dataset chain)  

CI workflows include:

- `ai-bias-sovereignty-schema-validate.yml`  
- `faircare-sovereignty-review-gate.yml`  
- `ai-sovereignty-dashboard-lint.yml`  
- `stac-validate-anomaly-datasets.yml`  

Any violation: **promotion BLOCK**.

---

# 🕰 Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-governance` | Initial creation of Sovereignty Bias Schema documentation for KFM v11. |

---

<div align="center">

**Kansas Frontier Matrix — Sovereignty Bias Schema**  
*Indigenous Data Sovereignty · Cultural Authority · Provenance-Complete AI Governance*

[Back to Bias Schemas](../README.md) ·  
[FAIR+CARE Dashboard Template](../../../templates/faircare/README.md) ·  
[Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
