---
title: "🧷 KFM — Temporal Validation Templates (Cadence · Coverage · Freshness · Time Semantics)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/temporal/templates/README.md"

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

intent: "remote-sensing-validation-templates-temporal"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Release Managers"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:temporal:templates:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-temporal-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/temporal/templates/README.md"
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

# 🧷 **KFM — Temporal Validation Templates**
`docs/analyses/remote-sensing/validation/methods/algorithms/temporal/templates/README.md`

**Purpose**  
Provide governed templates for **temporal validation outputs** (timestamp integrity, cadence, coverage, freshness),
policy threshold configuration, and normalized reason codes—kept **small, deterministic, and governance-safe**.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Temporal" src="https://img.shields.io/badge/Validation-Temporal-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This folder is reserved for **templates** used by temporal validation:

- a stable, machine-readable metrics payload shape,
- threshold configuration templates for cadence/coverage/freshness gates,
- normalized reason-code and severity mappings,
- optional “golden payload” examples used by CI to prevent report drift.

Templates keep outputs consistent across:

- per-run bundles: `docs/analyses/remote-sensing/validation/reports/per-run/`
- daily rollups: `docs/analyses/remote-sensing/validation/reports/daily/`
- release rollups: `docs/analyses/remote-sensing/validation/reports/releases/`

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/temporal/
└── 📁 templates/                                         — Templates and examples (this directory)
    ├── 📄 README.md                                      — This index
    ├── 🧾 temporal_metrics.template.json                 — Recommended: metrics payload template (cadence/coverage/freshness)
    ├── 🧾 temporal_thresholds.template.json              — Recommended: thresholds + gate configuration
    ├── 🧾 temporal_reason_codes.template.json            — Recommended: normalized reason codes + severity mapping
    ├── 🧾 cadence_profiles.template.json                 — Optional: shared cadence profiles (daily/weekly/n-day composites)
    ├── 🧾 example_temporal.pass.json                     — Optional: “golden” pass example (small)
    ├── 🧾 example_temporal.warn.json                     — Optional: “golden” warn example (small)
    └── 🧾 example_temporal.fail.json                     — Optional: “golden” fail example (small)
~~~

> Filenames above are recommended conventions. Add only what is used by CI validators and report writers, and keep examples small.

---

## 🧾 Template inventory (recommended)

### 1) Metrics payload template

The metrics template SHOULD:

- align with the common algorithm output envelope,
- define how `effective_datetime_utc` is chosen (policy precedence),
- compute cadence and coverage from **deterministic enumeration**,
- compute freshness lag from explicit timestamps,
- avoid embedding long “missing timestamp” lists in public artifacts (use references if needed).

Skeleton (illustrative only):

~~~json
{
  "algorithm_id": "kfm:rs:validate:temporal:integrity:v1",
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
      "items_checked": 0,
      "effective_datetime_policy": "datetime|start_end_midpoint|start_datetime",
      "datetime_missing_count": 0,
      "datetime_unparseable_count": 0,
      "timezone_ambiguous_count": 0,
      "start_end_invalid_count": 0,
      "duration_out_of_policy_count": 0,
      "duplicate_timestamp_count": 0,
      "non_monotonic_count": 0,
      "cadence_expected": "daily|hourly|weekly|n_day_composite|event_driven",
      "cadence_tolerance_s": 0,
      "cadence_mismatch_count": 0,
      "jitter_s_p50": null,
      "jitter_s_p95": null,
      "coverage_expected_steps": 0,
      "coverage_present_steps": 0,
      "coverage_pct": 1.0,
      "gap_count": 0,
      "max_gap_steps": 0,
      "max_gap_duration_s": 0,
      "freshness_lag_s_p95": null,
      "freshness_slo_breach_count": 0
    },
    "thresholds": {},
    "outcome": "pass|warn|fail",
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

A thresholds template SHOULD define:

- the cadence policy and tolerance,
- coverage minimums and gap limits,
- freshness SLO limits,
- deterministic behavior for missing timestamps (fail closed vs warn).

Skeleton (illustrative only):

~~~json
{
  "policy_version": "v1",
  "gate_mode": "fail_closed",
  "effective_datetime_policy": "datetime",
  "cadence": {
    "expected": "daily",
    "step_s": 86400,
    "tolerance_s": 3600,
    "event_driven": false
  },
  "coverage": {
    "coverage_pct_min": 0.98,
    "max_gap_steps_max": 1,
    "max_gap_duration_s_max": 172800
  },
  "freshness": {
    "freshness_lag_s_p95_max": null,
    "slo_enforced": false
  },
  "thresholds": {
    "datetime_missing_count_max": 0,
    "datetime_unparseable_count_max": 0,
    "timezone_ambiguous_count_max": 0,
    "start_end_invalid_count_max": 0,
    "duplicate_timestamp_count_max": 0
  }
}
~~~

### 3) Reason codes and severity mapping template

A reason-code template SHOULD map reason codes to deterministic severities and optional remediation hints.

Skeleton (illustrative only):

~~~json
{
  "reason_codes": [
    {"code": "DATETIME_MISSING", "severity": "fail", "hint": "Emit datetime or start/end fields; do not infer timestamps."},
    {"code": "DATETIME_UNPARSEABLE", "severity": "fail", "hint": "Ensure ISO8601 timestamps; include timezone (UTC) explicitly."},
    {"code": "TIMEZONE_AMBIGUOUS", "severity": "fail", "hint": "Timestamp missing timezone or mixed timezone policies; normalize to UTC."},
    {"code": "START_END_INVALID", "severity": "fail", "hint": "Interval products require start_datetime <= end_datetime."},
    {"code": "CADENCE_MISMATCH", "severity": "warn", "hint": "Observed cadence outside tolerance; verify scheduler/publish cadence and binning rules."},
    {"code": "TEMPORAL_GAP_EXCESS", "severity": "warn", "hint": "Gaps exceed policy; verify missingness vs expected cadence and upstream availability."},
    {"code": "DUPLICATE_TIMESTAMPS", "severity": "fail", "hint": "Duplicate timestamp collisions; confirm item id construction and partitioning."},
    {"code": "FRESHNESS_SLO_BREACH", "severity": "warn", "hint": "Freshness lag exceeded SLO; inspect scheduler delays, upstream availability, and retries."},
    {"code": "CARE_REDACTION_APPLIED", "severity": "warn", "hint": "Details withheld under FAIR+CARE policy."}
  ]
}
~~~

### 4) Cadence profiles template (optional)

Use a shared cadence profile file when multiple products share definitions.

Skeleton (illustrative only):

~~~json
{
  "cadence_profiles": [
    {"name": "hourly", "step_s": 3600, "tolerance_s": 900},
    {"name": "daily", "step_s": 86400, "tolerance_s": 3600},
    {"name": "weekly", "step_s": 604800, "tolerance_s": 21600},
    {"name": "n_day_composite_5", "step_s": 432000, "tolerance_s": 43200}
  ]
}
~~~

---

## 🎯 Determinism requirements for templates

Templates MUST support deterministic temporal computation:

- stable ordering:
  - items sorted by `(effective_datetime_utc ASC, id ASC)`
- explicit `effective_datetime_utc` precedence:
  - define whether `datetime` or interval fields are authoritative
- explicit cadence policy:
  - define `step_s` and `tolerance_s` (no implicit defaults)
- explicit binning rules:
  - if rounding/bucketing timestamps is used, record the method and boundaries
- deterministic `outcome` and `reason_codes`:
  - reason codes sorted lexicographically
  - outcome derived deterministically from threshold evaluation and reason-code severity mapping
- freshness computed from explicit timestamps:
  - do not infer “latest” without enumerating eligible items deterministically

---

## 🛡️ FAIR+CARE and sovereignty posture

Temporal metrics are typically low-risk, but MUST remain governance-safe:

- do not include raw coordinates or sensitive identifiers in temporal templates or examples,
- avoid publishing full lists of missing timestamps or “where/when” drilldowns for restricted collections,
- keep `spatial_scope` generalized (`kansas`, region, or coarse H3).

If a run requires restricted detail to diagnose:

- set `care_gate_status = redact|deny`,
- emit aggregated metrics and reason codes only,
- require steward review via governed channels for deeper diagnostics.

---

## 🧪 CI/CD usage (recommended)

Templates support CI by enabling:

- JSON validation (if schemas exist under governed `schemas/`),
- golden payload regression tests (pass/warn/fail examples remain stable),
- deterministic gate checks:
  - same inputs/config → same `reason_codes` ordering and `outcome`.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed temporal templates index; defined metrics payload template, thresholds template, reason-code mapping, optional cadence profiles, determinism rules, and governance-safe example posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Temporal" src="https://img.shields.io/badge/Validation-Temporal-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Temporal Algorithms](../README.md) ·
[🧮 Algorithms Index](../../README.md) ·
[🧾 Reports](../../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

