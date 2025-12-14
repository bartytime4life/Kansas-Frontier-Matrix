---
title: "🧷 KFM — Drift Validation Templates (Delta Payloads · Thresholds · Reason Codes)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/drift/templates/README.md"

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

intent: "remote-sensing-validation-templates-drift"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:drift:templates:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-drift-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/drift/templates/README.md"
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

# 🧷 **KFM — Drift Validation Templates**
`docs/analyses/remote-sensing/validation/methods/algorithms/drift/templates/README.md`

**Purpose**  
Provide governed templates for **drift validation outputs** and **threshold configuration**
so per-run, daily, and release rollups remain **consistent, deterministic, and governance-safe**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Drift-blue" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This folder is reserved for **templates** used by drift validation:

- a stable `drift.delta.json` payload shape (small, aggregated, safe),
- policy templates for drift thresholds and gate outcomes,
- normalized reason codes and deterministic severity mapping,
- optional example “golden” payloads for CI regression tests.

Templates help keep drift reporting consistent across:

- per-run bundles: `docs/analyses/remote-sensing/validation/reports/per-run/`
- daily rollups: `docs/analyses/remote-sensing/validation/reports/daily/`
- release rollups: `docs/analyses/remote-sensing/validation/reports/releases/`

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/drift/
└── 📁 templates/                                         — Templates and example payloads (this directory)
    ├── 📄 README.md                                      — This index
    ├── 🧾 drift_delta.template.json                      — Recommended: drift delta payload template
    ├── 🧾 drift_thresholds.template.json                 — Recommended: policy thresholds + gate configuration
    ├── 🧾 drift_reason_codes.template.json               — Recommended: normalized reason codes + severity mapping
    ├── 🧾 example_drift.pass.json                        — Optional: “golden” pass example (small)
    ├── 🧾 example_drift.warn.json                        — Optional: “golden” warn example (small)
    └── 🧾 example_drift.fail.json                        — Optional: “golden” fail example (small)
~~~

> The files listed above are recommended conventions for this folder. Add only what you actually use, and keep all payloads small.

---

## 🧾 Template inventory (recommended)

### 1) Drift delta payload template

A drift delta payload template SHOULD be:

- **small** (aggregation only),
- **deterministic** (stable ordering, pinned baseline selection rules),
- **safe** (no sensitive geometry, no tile-level leakiness unless policy allows).

Skeleton (illustrative only):

~~~json
{
  "algorithm_id": "kfm:rs:validate:drift:delta:v1",
  "run_id": "urn:kfm:run:<current>",
  "dataset_id": "urn:kfm:dataset:<dataset>",
  "baseline": {
    "mode": "run|release|pinned",
    "run_id": "urn:kfm:run:<baseline>",
    "release_version": "vMAJOR.MINOR.PATCH",
    "baseline_ref": "urn:kfm:baseline:<optional>"
  },
  "scope": {
    "time_start_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "time_end_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "spatial_scope": "kansas|region:<...>|h3:r<...>",
    "sampling": "full|tiles|stratified|random",
    "seed": 1337,
    "sample_frame_hash": "<sha256>"
  },
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {
      "events_total": 0,
      "reasons": []
    }
  },
  "deltas": {
    "counts": {
      "items_delta": 0,
      "items_delta_pct": 0.0,
      "tiles_delta": 0,
      "tiles_delta_pct": 0.0,
      "assets_missing_rate_delta_pct": 0.0
    },
    "structure": {
      "schema_version_changed": false,
      "crs_changed": false,
      "nodata_policy_changed": false,
      "assets_added": 0,
      "assets_removed": 0,
      "assets_renamed": 0,
      "class_map_hash_changed": false
    },
    "distributions": {
      "psi": null,
      "kl_divergence": null,
      "p10_delta": null,
      "p50_delta": null,
      "p90_delta": null
    },
    "metrics": {
      "rmse_delta": null,
      "mae_delta": null,
      "macro_f1_delta": null,
      "iou_positive_delta": null
    },
    "provenance": {
      "inputs_changed_count": 0,
      "missing_prov_links_count": 0,
      "activity_type_changed": false
    }
  },
  "thresholds": {
    "items_delta_pct_max": 0.0,
    "tiles_delta_pct_max": 0.0,
    "assets_missing_rate_delta_pct_max": 0.0,
    "psi_max": null,
    "macro_f1_drop_max": null
  },
  "outcome": "pass|warn|fail",
  "reason_codes": [],
  "refs": {
    "stac_items": [],
    "dcat_datasets": [],
    "prov_bundles": []
  },
  "checksums": {
    "input_pack_sha256": "<sha256>",
    "output_sha256": "<sha256>"
  },
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ"
}
~~~

### 2) Threshold configuration template

A drift threshold template SHOULD define:

- baseline selection mode and fallback behavior,
- thresholds by drift type (counts, structure, distributions, metrics, provenance),
- deterministic gate evaluation rules,
- critical vs non-critical thresholds,
- allowed “expected changes” for planned releases (policy exceptions, still auditable).

Skeleton (illustrative only):

~~~json
{
  "policy_version": "v1",
  "gate_mode": "fail_closed",
  "baseline": {
    "mode": "release",
    "fallback_mode": "run",
    "require_baseline": true
  },
  "thresholds": {
    "counts": {
      "items_delta_pct_max": 2.0,
      "tiles_delta_pct_max": 2.0,
      "assets_missing_rate_delta_pct_max": 0.5
    },
    "structure": {
      "schema_version_changed": "fail",
      "crs_changed": "fail",
      "nodata_policy_changed": "warn",
      "assets_removed": "fail",
      "assets_renamed": "fail"
    },
    "distributions": {
      "psi_max": 0.2,
      "p50_abs_delta_max": null
    },
    "metrics": {
      "rmse_increase_max": null,
      "macro_f1_drop_max": 0.02,
      "iou_positive_drop_max": null
    },
    "provenance": {
      "missing_prov_links_max": 0,
      "inputs_changed_max": 0
    }
  },
  "expected_changes": [
    {
      "when": {"release_version": "vMAJOR.MINOR.PATCH"},
      "allow": ["items_delta_pct_max", "assets_added"],
      "notes": "Planned tiling expansion; non-breaking"
    }
  ]
}
~~~

### 3) Reason codes template (normalized)

A reason-code template SHOULD map reason codes to deterministic severities and optional remediation hints.

Skeleton (illustrative only):

~~~json
{
  "reason_codes": [
    {"code": "BASELINE_NOT_FOUND", "severity": "fail", "hint": "Check baseline resolution rules; ensure prior run/release exists."},
    {"code": "STRUCTURE_BREAKING_CHANGE", "severity": "fail", "hint": "Asset/property removal or rename detected; requires MAJOR bump and migration notes."},
    {"code": "CRS_CHANGED", "severity": "fail", "hint": "CRS differs from baseline; confirm intended reprojection and update SemVer."},
    {"code": "COUNT_DELTA_EXCEEDS_THRESHOLD", "severity": "warn", "hint": "Tile/item counts shifted beyond policy; investigate ingestion completeness and AOI changes."},
    {"code": "DISTRIBUTION_DRIFT_EXCEEDS_THRESHOLD", "severity": "warn", "hint": "Value distribution shift; confirm upstream product changes or processing parameter changes."},
    {"code": "METRIC_REGRESSION", "severity": "fail", "hint": "Quality regression detected; block promotion and investigate."},
    {"code": "PROVENANCE_INCOMPLETE", "severity": "fail", "hint": "Missing PROV links; re-run lineage emission and validators."},
    {"code": "CARE_REDACTION_APPLIED", "severity": "warn", "hint": "Details withheld for policy; escalate via governed channels if diagnosis requires restricted info."}
  ]
}
~~~

---

## 🎯 Determinism requirements for templates

Templates MUST support deterministic computation and reporting:

- stable baseline selection:
  - run baseline resolved by `ended_utc DESC`, tie-break by `run_id ASC`
  - release baseline resolved by SemVer ordering (or governed release ledger order)
- stable enumeration:
  - STAC Item ids sorted
  - asset keys sorted
  - tile ids sorted
- fixed histogram bins and quantile definitions (if used)
- stable `outcome` and `reason_codes` selection:
  - reason codes sorted lexicographically
  - severity derived deterministically from policy and reason-code mapping
- sampling determinism (if sampling is used):
  - record `seed`, `sample_frame_hash`, and sampling strategy

---

## 🛡️ FAIR+CARE and sovereignty posture

Templates and example payloads in this folder MUST be safe to publish in-repo:

- no raw coordinates, site identifiers, or “how to locate” guidance
- no internal endpoints, tokens, signed URLs, or private bucket paths
- no tile-level “worst/best” listings when governance labels restrict
- spatial scope MUST be generalized (`kansas`, region, or coarse H3)

If a drift diagnostic would require restricted detail:

- set `care_gate_status` to `redact` or `deny`,
- emit only aggregated deltas and reason codes,
- require steward review for deeper diagnosis via governed channels.

---

## 🧪 CI/CD alignment (recommended)

Templates support CI by enabling:

- schema validation of `drift.delta.json` (if a JSON Schema exists)
- “golden payload” regression tests:
  - pass/warn/fail example files validate and remain stable
- policy gate determinism checks:
  - identical inputs/config → identical `reason_codes` ordering and `outcome`

If/when schemas are added under `schemas/`, keep them in governed locations and reference them from the pipeline validators rather than embedding schema logic here.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed drift templates index; defined delta payload template, threshold configuration template, reason-code mapping, determinism rules, and governance-safe example posture. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Drift-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Drift Algorithms](../README.md) ·
[🧮 Algorithms Index](../../README.md) ·
[🧾 Reports](../../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

