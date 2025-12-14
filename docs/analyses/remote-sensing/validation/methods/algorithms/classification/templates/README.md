---
title: "🧷 KFM — Classification Validation Templates (Metrics · Thresholds · Schemas)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/classification/templates/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Templates"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "remote-sensing-validation-templates-classification"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:classification:templates:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-classification-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/classification/templates/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🧷 **KFM — Classification Validation Templates**
`docs/analyses/remote-sensing/validation/methods/algorithms/classification/templates/README.md`

**Purpose**  
Provide governed templates for **classification validation outputs** (metrics, thresholds, and report references)
so per-run, daily, and release rollups remain **consistent, deterministic, and governance-safe**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Classification-blue" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This folder is reserved for **templates** used by classification validation:

- machine-readable JSON templates for outputs (metrics envelope, per-class arrays),
- JSON templates for threshold configuration (gate rules),
- optional JSON Schemas (if/when maintained in-repo) and example “golden” payloads.

Templates help keep:

- per-run bundles (`reports/per-run/`) consistent,
- daily rollups (`reports/daily/`) stable,
- release promotion rollups (`reports/releases/`) audit-friendly.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/classification/
└── 📁 templates/                                         — Templates and example payloads (this directory)
    ├── 📄 README.md                                      — This index
    ├── 🧾 classification_metrics.template.json           — Recommended: metrics output template (envelope + per-class)
    ├── 🧾 classification_thresholds.template.json        — Recommended: threshold config template (gate rules)
    ├── 🧾 class_map.template.json                        — Recommended: class_id → name map template (versioned)
    ├── 🧾 example_payload.pass.json                      — Optional: “golden” pass example (small)
    ├── 🧾 example_payload.fail.json                      — Optional: “golden” fail example (small)
    └── 🧾 README.notes.md                                — Optional: notes on template usage (if needed)
~~~

> The files listed above are recommended conventions for this folder. Add only what you actually use, and keep all payloads small.

---

## 🧾 Template inventory (recommended)

### 1) Metrics output template

A template for the classification algorithm output SHOULD align to the parent “standard output shape” and include:

- `algorithm_id`, `run_id`, `dataset_id`
- `scope` (time and generalized spatial scope)
- `governance` (CARE + sovereignty gates)
- `results.metrics` (accuracy, macro_f1, weighted_f1, per_class array)
- `results.thresholds` (the thresholds applied)
- `results.outcome` and `results.reason_codes`
- `refs` (STAC/DCAT/PROV pointers)
- checksums (optional but recommended)

Skeleton (illustrative only):

~~~json
{
  "algorithm_id": "kfm:rs:validate:classification:confusion:v1",
  "run_id": "urn:kfm:run:<run_id>",
  "dataset_id": "urn:kfm:dataset:<dataset_id>",
  "scope": {
    "time_start_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "time_end_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "spatial_scope": "kansas|region:<...>|h3:r<...>",
    "sampling": "full|tiles|stratified|random"
  },
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {
      "events_total": 0,
      "reasons": []
    }
  },
  "results": {
    "metrics": {
      "accuracy": 0.0,
      "macro_f1": 0.0,
      "weighted_f1": 0.0,
      "per_class": [
        {
          "class_id": 0,
          "name": "background",
          "support": 0,
          "precision": 0.0,
          "recall": 0.0,
          "f1": 0.0,
          "iou": 0.0
        }
      ]
    },
    "thresholds": {},
    "outcome": "pass|fail|warn",
    "reason_codes": []
  },
  "refs": {
    "stac_items": [],
    "dcat_datasets": [],
    "prov_bundles": []
  },
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ"
}
~~~

### 2) Threshold configuration template

A threshold config template SHOULD define:

- the metric keys used for gating,
- critical vs non-critical thresholds,
- per-class minimums where needed,
- minimum support rules for rare classes,
- deterministic behavior for “missing metric” cases (fail closed vs warn).

Skeleton (illustrative only):

~~~json
{
  "policy_version": "v1",
  "gate_mode": "fail_closed",
  "min_support_per_class": 100,
  "thresholds": {
    "macro_f1_min": 0.85,
    "weighted_f1_min": 0.9,
    "accuracy_min": 0.9
  },
  "per_class_thresholds": [
    {"class_id": 1, "metric": "iou", "min": 0.9, "critical": true}
  ],
  "reason_code_map": {
    "LOW_SUPPORT_CLASS": "warn",
    "THRESHOLD_BREACH_CRITICAL": "fail",
    "THRESHOLD_BREACH_NONCRITICAL": "warn"
  }
}
~~~

### 3) Class map template

A class map template SHOULD be explicit, versioned, and hashable:

- stable class ordering (sorted by `class_id`)
- human-readable names
- optional groupings (e.g., “water-family”)
- optional remap rules (if multiple sources differ)

Skeleton (illustrative only):

~~~json
{
  "class_map_version": "v1",
  "classes": [
    {"class_id": 0, "name": "background"},
    {"class_id": 1, "name": "water"}
  ]
}
~~~

---

## 🎯 Determinism requirements for templates

Templates MUST be compatible with deterministic computation and reporting:

- stable class ordering: sorted by `class_id`
- consistent numeric precision rules (if rounding is used, document it)
- deterministic `outcome` and `reason_codes` selection (no ambiguous ties)
- stable JSON key ordering is not required by JSON, but producers SHOULD emit stable ordering when feasible

When sampling is used, templates SHOULD include:

- `seed`
- `sample_frame_hash`
- `sampling_strategy`
- `sample_counts_by_stratum`

---

## 🛡️ FAIR+CARE and sovereignty posture

Templates in this folder MUST be safe to publish in-repo:

- no raw coordinates or “how to locate” guidance
- no internal endpoints, tokens, or signed URLs
- no example payloads that embed restricted identifiers or sensitive AOI details

If examples are included, ensure they:

- use generalized `spatial_scope`
- omit tile IDs that could be sensitive under governance
- include only minimal, non-sensitive metric values

---

## 🧪 CI/CD and validation usage (recommended)

When a JSON Schema is maintained for these outputs, validate in CI (tooling varies by repo):

- validate metrics payloads against the schema,
- enforce required keys and allowed enums,
- ensure `care_gate_status` and `sovereignty_gate` are present and policy-consistent.

Store schema locations under governed `schemas/` only if/when they exist; templates should not depend on non-existent paths.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed templates index for classification validation; established recommended template set, determinism rules, and governance-safe example posture. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Classification-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Classification Algorithms](../README.md) ·
[🧮 Algorithms Index](../../README.md) ·
[🧾 Reports](../../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

