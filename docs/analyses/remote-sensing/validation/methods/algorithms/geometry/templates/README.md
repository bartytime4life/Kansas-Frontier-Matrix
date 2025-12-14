---
title: "🧷 KFM — Geometry Validation Templates (Integrity Metrics · Thresholds · Reason Codes)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/geometry/templates/README.md"

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

intent: "remote-sensing-validation-templates-geometry"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:geometry:templates:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-geometry-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/geometry/templates/README.md"
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

# 🧷 **KFM — Geometry Validation Templates**
`docs/analyses/remote-sensing/validation/methods/algorithms/geometry/templates/README.md`

**Purpose**  
Provide governed templates for **geometry validation outputs** (CRS/footprint/tiling/grid integrity),
threshold configuration, and normalized reason codes so reporting remains **consistent, deterministic, and governance-safe**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Geometry-blue" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This folder is reserved for **templates** used by geometry validation:

- machine-readable templates for geometry integrity metrics artifacts,
- threshold configuration templates for policy gates,
- normalized reason-code and severity mappings,
- optional “golden payload” examples for CI regression tests.

Templates help keep geometry validation outputs consistent across:

- per-run bundles: `docs/analyses/remote-sensing/validation/reports/per-run/`
- daily rollups: `docs/analyses/remote-sensing/validation/reports/daily/`
- release rollups: `docs/analyses/remote-sensing/validation/reports/releases/`

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/geometry/
└── 📁 templates/                                         — Templates and examples (this directory)
    ├── 📄 README.md                                      — This index
    ├── 🧾 geometry_metrics.template.json                 — Recommended: metrics payload template (integrity checks)
    ├── 🧾 geometry_thresholds.template.json              — Recommended: thresholds + gate configuration
    ├── 🧾 geometry_reason_codes.template.json            — Recommended: normalized reason codes + severity mapping
    ├── 🧾 example_geometry.pass.json                     — Optional: “golden” pass example (small)
    ├── 🧾 example_geometry.warn.json                     — Optional: “golden” warn example (small)
    └── 🧾 example_geometry.fail.json                     — Optional: “golden” fail example (small)
~~~

> The files listed above are recommended conventions for this folder. Add only what you actually use, and keep all payloads small.

---

## 🧾 Template inventory (recommended)

### 1) Geometry metrics payload template

A metrics template SHOULD:

- align with the standard algorithm output envelope,
- include aggregated integrity metrics only,
- avoid embedding sensitive coordinates or offender lists.

Skeleton (illustrative only):

~~~json
{
  "algorithm_id": "kfm:rs:validate:geometry:integrity:v1",
  "run_id": "urn:kfm:run:<run_id>",
  "dataset_id": "urn:kfm:dataset:<dataset_id>",
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
  "results": {
    "metrics": {
      "items_checked": 0,
      "crs_missing_count": 0,
      "crs_mismatch_count": 0,
      "invalid_geometry_count": 0,
      "empty_geometry_count": 0,
      "bbox_invalid_count": 0,
      "bbox_out_of_bounds_count": 0,
      "tile_overlap_rate_pct": null,
      "tile_gap_rate_pct": null,
      "duplicate_tile_count": null,
      "transform_missing_count": null,
      "gsd_observed_median_m": null,
      "gsd_drift_pct_p50": null
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

A threshold config template SHOULD define:

- which checks are critical (fail) vs non-critical (warn),
- numeric tolerances for overlap/gap/resolution drift,
- deterministic handling when metrics are missing (fail closed vs warn).

Skeleton (illustrative only):

~~~json
{
  "policy_version": "v1",
  "gate_mode": "fail_closed",
  "thresholds": {
    "crs_missing_count_max": 0,
    "crs_mismatch_count_max": 0,
    "invalid_geometry_count_max": 0,
    "bbox_invalid_count_max": 0,
    "bbox_out_of_bounds_count_max": 0,
    "tile_overlap_rate_pct_max": 2.0,
    "tile_gap_rate_pct_max": 2.0,
    "gsd_drift_pct_p50_max": 1.0,
    "transform_missing_count_max": 0
  },
  "severity_overrides": {
    "tile_overlap_rate_pct_max": "warn",
    "tile_gap_rate_pct_max": "warn"
  }
}
~~~

### 3) Reason codes and severity mapping template

A reason-code template SHOULD map codes to deterministic severities and optional remediation hints.

Skeleton (illustrative only):

~~~json
{
  "reason_codes": [
    {"code": "CRS_MISSING", "severity": "fail", "hint": "CRS required but missing; ensure projection metadata is emitted."},
    {"code": "CRS_MISMATCH", "severity": "fail", "hint": "CRS differs from policy; check reprojection step and item metadata."},
    {"code": "FOOTPRINT_INVALID", "severity": "fail", "hint": "Invalid geometry; validate polygon winding and self-intersections."},
    {"code": "BBOX_INVALID", "severity": "fail", "hint": "Malformed bbox; ensure min<=max for each axis and correct axis order."},
    {"code": "TILE_OVERLAP_EXCESS", "severity": "warn", "hint": "Overlap above policy; verify tiling scheme and edge buffers."},
    {"code": "TILE_GAP_EXCESS", "severity": "warn", "hint": "Gaps above policy; check tile enumeration and coverage rules."},
    {"code": "RESOLUTION_DRIFT", "severity": "warn", "hint": "GSD drift; ensure correct resampling method and metadata output."},
    {"code": "CARE_REDACTION_APPLIED", "severity": "warn", "hint": "Details withheld under FAIR+CARE policy."}
  ]
}
~~~

---

## 🎯 Determinism requirements for templates

Templates MUST support deterministic computation and reporting:

- stable enumeration: item ids and asset keys sorted
- explicit tolerances pinned (no implicit defaults)
- deterministic `outcome` and `reason_codes`:
  - codes sorted lexicographically
  - severity derived deterministically from policy and mapping
- deterministic sampling metadata when used:
  - include `seed` and `sample_frame_hash`

---

## 🛡️ FAIR+CARE and sovereignty posture

Templates and examples MUST be safe to publish in-repo:

- no raw coordinates or “how to locate” guidance
- no internal endpoints, tokens, or signed URLs
- no tile-level offender listings that might reveal sensitive locations
- spatial scope MUST be generalized (`kansas`, region, or coarse H3)

If a run requires restricted detail for diagnosis:

- set `care_gate_status = redact|deny`
- emit only aggregated metrics and reason codes
- require steward review via governed channels for deeper diagnostics

---

## 🧪 CI/CD usage (recommended)

Templates support CI by enabling:

- schema validation of emitted metrics (if schemas exist in governed `schemas/`)
- golden payload regression tests:
  - pass/warn/fail example payloads remain stable
- policy determinism tests:
  - same inputs/config → same `reason_codes` ordering and `outcome`

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed geometry templates index; defined metrics payload template, thresholds template, reason-code mapping, determinism rules, and governance-safe example posture. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Geometry-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Geometry Algorithms](../README.md) ·
[🧮 Algorithms Index](../../README.md) ·
[🧾 Reports](../../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

