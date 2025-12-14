---
title: "🧷 KFM — Validation Metrics Templates (Registry · Thresholds · Units · Rollup Shapes)"
path: "docs/analyses/remote-sensing/validation/methods/metrics/templates/README.md"

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

intent: "remote-sensing-validation-metrics-templates"
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

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:metrics:templates:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-metrics-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/metrics/templates/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

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
---

<div align="center">

# 🧷 **KFM — Validation Metrics Templates**
`docs/analyses/remote-sensing/validation/methods/metrics/templates/README.md`

**Purpose**  
Provide governed templates to keep **metric definitions, threshold policies, and rollup payloads** consistent across
remote-sensing validation in KFM. These templates support deterministic computation and governance-safe reporting.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Metrics Templates" src="https://img.shields.io/badge/Validation-Metrics%20Templates-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This folder is reserved for **templates** that standardize how metrics are:

- registered (names, units, directionality),
- aggregated (support counts, levels),
- thresholded (warn/fail semantics),
- rolled up for per-run / daily / release reporting.

These templates are designed to:

- reduce drift across algorithm families,
- keep outputs machine-validated and audit-ready,
- ensure deterministic gate behavior,
- prevent governance leakage (no sensitive coordinate-level detail).

Metric meaning and rules live in:

- `../README.md`

Algorithm definitions live in:

- `../../algorithms/README.md`

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/metrics/
└── 📁 templates/                                               — Templates and examples (this directory)
    ├── 📄 README.md                                            — This index
    ├── 🧾 metric_registry.template.json                         — Recommended: metric ids, names, units, directionality
    ├── 🧾 metric_record.template.json                           — Recommended: a single metric record shape
    ├── 🧾 thresholds_policy.template.json                       — Recommended: thresholds + gate semantics (warn/fail)
    ├── 🧾 aggregation_rules.template.json                       — Optional: allowed aggregation levels + support rules
    ├── 🧾 reason_codes.template.json                            — Optional: shared reason codes for metric-level gating
    ├── 🧾 example_registry.minimal.json                         — Optional: tiny “golden” registry example
    ├── 🧾 example_thresholds.minimal.json                       — Optional: tiny “golden” thresholds example
    └── 🧾 example_rollup.minimal.json                           — Optional: tiny “golden” rollup example
~~~

> Filenames above are recommended conventions. Add only what is used by CI validators and report writers, and keep examples small.

---

## 🧾 Template inventory (recommended)

### 1) Metric registry template

The registry template SHOULD define each metric as a stable record:

- `metric_id` (stable identifier)
- `name` (short machine name, e.g., `rmse`)
- `family` (radiometry/classification/geometry/temporal/drift)
- `unit` (explicit)
- `direction` (`lower_is_better` / `higher_is_better` / `target_is_best`)
- `aggregation_levels_allowed` (tile/region/release, etc.)
- optional domain notes and constraints

Skeleton (illustrative only):

~~~json
{
  "registry_version": "v1",
  "metrics": [
    {
      "metric_id": "kfm:metric:radiometry:rmse:v1",
      "name": "rmse",
      "family": "radiometry",
      "unit": "reflectance",
      "direction": "lower_is_better",
      "aggregation_levels_allowed": ["tile", "region", "dataset_window", "release"],
      "notes": "RMSE computed on eligible pixels after mask policy."
    }
  ]
}
~~~

### 2) Metric record template

The metric record template SHOULD be embeddable inside algorithm outputs and reports.

Skeleton (illustrative only):

~~~json
{
  "metric_id": "kfm:metric:<family>:<name>:v1",
  "name": "<name>",
  "family": "<family>",
  "unit": "<unit>",
  "direction": "lower_is_better|higher_is_better|target_is_best",
  "level": "tile|region|dataset_window|release",
  "value": 0.0,
  "support": {
    "n_px": null,
    "n_items": null,
    "n_classes": null
  },
  "method": {
    "mask_policy_hash": "<sha256>",
    "sampling": "full|tiles|stratified|random",
    "seed": 1337,
    "quantile_method": null,
    "bin_edges_ref": null
  }
}
~~~

### 3) Thresholds policy template

Threshold policy templates MUST be deterministic and explainable:

- fixed operators,
- clear severities (`warn` vs `fail`),
- explicit fail-closed posture where required.

Skeleton (illustrative only):

~~~json
{
  "policy_version": "v1",
  "gate_mode": "fail_closed",
  "thresholds": [
    {
      "threshold_id": "kfm:threshold:radiometry:rmse:max:v1",
      "metric_id": "kfm:metric:radiometry:rmse:v1",
      "operator": "<=",
      "value": 0.05,
      "severity": "fail"
    },
    {
      "threshold_id": "kfm:threshold:temporal:coverage:pct:min:v1",
      "metric_id": "kfm:metric:temporal:coverage_pct:v1",
      "operator": ">=",
      "value": 0.98,
      "severity": "warn"
    }
  ]
}
~~~

### 4) Aggregation rules template (optional)

Use when multiple teams produce metrics and aggregation must be uniform:

- required support fields per family
- how to aggregate (mean, weighted mean, median, p95)
- stable ordering and tie behavior

Skeleton (illustrative only):

~~~json
{
  "aggregation_rules_version": "v1",
  "defaults": {
    "ordering": "stable",
    "tie_breaking": "lexicographic"
  },
  "families": {
    "radiometry": {
      "tile_to_region": "weighted_mean_by_support.n_px"
    },
    "classification": {
      "tile_to_region": "micro_average_by_support.n_items"
    }
  }
}
~~~

### 5) Reason codes template (optional)

Use when metric evaluation produces cross-family reason codes:

- missing reference/baseline
- low support
- invalid units
- governance redaction applied

Keep reason codes small and normalized.

---

## 🎯 Determinism requirements for templates

Templates MUST support deterministic evaluation:

- `metrics[]` arrays MUST have stable ordering (lexicographic by `metric_id` recommended).
- `thresholds[]` arrays MUST have stable ordering (lexicographic by `threshold_id` recommended).
- Metric directionality MUST be explicit (never implied by name).
- Any quantile or histogram settings MUST be pinned:
  - quantile method specified
  - bin edges referenced (not computed ad hoc per run)
- Sampling MUST be explicit when used:
  - seed recorded
  - sample frame hash recorded (or referenced)

If a metric cannot be computed (missing reference, missing support):

- fail-closed or warn-open behavior MUST be dictated by policy and recorded.

---

## 🛡️ FAIR+CARE and sovereignty posture

Templates and examples in this folder MUST remain safe for in-repo publication:

- no raw coordinates,
- no site-level identifiers that expose restricted collections,
- no signed URLs, secrets, or internal endpoints,
- no “worst offending tiles” enumerations.

If policy requires redaction:

- enforce `care_gate_status = redact|deny` at the algorithm output layer,
- keep templates generic and aggregated,
- require steward review for restricted diagnostics outside public artifacts.

---

## 🧪 CI/CD usage (recommended)

These templates support CI by enabling:

- schema validation (when schemas are defined under governed `schemas/`),
- golden payload regression tests (examples remain stable),
- deterministic gate checks:
  - same inputs/config → same thresholds → same outcomes.

Recommended checks:

- registry validation: all `metric_id` unique, units valid, direction valid
- thresholds validation: all referenced `metric_id` exist, operators allowed, severities valid
- ordering checks: stable ordering (optional but recommended)

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed metrics templates index; defined registry, metric record, thresholds policy, optional aggregation rules, determinism rules, and governance-safe template posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Metrics Templates" src="https://img.shields.io/badge/Validation-Metrics%20Templates-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Metrics](../README.md) ·
[⬅ Methods](../../README.md) ·
[🧾 Reports](../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

