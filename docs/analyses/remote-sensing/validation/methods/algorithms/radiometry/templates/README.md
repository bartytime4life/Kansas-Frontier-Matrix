---
title: "🧷 KFM — Radiometry Validation Templates (Error Metrics · Drift · Threshold Gates)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/radiometry/templates/README.md"

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

intent: "remote-sensing-validation-templates-radiometry"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:radiometry:templates:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-radiometry-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/radiometry/templates/README.md"
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

# 🧷 **KFM — Radiometry Validation Templates**
`docs/analyses/remote-sensing/validation/methods/algorithms/radiometry/templates/README.md`

**Purpose**  
Provide governed templates for **radiometry validation outputs** (continuous fields), including
error metrics, distribution drift summaries, thresholds, and normalized reason codes—kept **small, deterministic, and governance-safe**.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Radiometry" src="https://img.shields.io/badge/Validation-Radiometry-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This folder is reserved for **templates** used by radiometry validation:

- a stable metrics payload shape for continuous-field validation,
- threshold configuration templates for policy gates,
- normalized reason-code and severity mappings,
- optional “golden payload” examples for CI regression tests.

Templates keep outputs consistent across:

- per-run bundles: `docs/analyses/remote-sensing/validation/reports/per-run/`
- daily rollups: `docs/analyses/remote-sensing/validation/reports/daily/`
- release rollups: `docs/analyses/remote-sensing/validation/reports/releases/`

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/radiometry/
└── 📁 templates/                                         — Templates and examples (this directory)
    ├── 📄 README.md                                      — This index
    ├── 🧾 radiometry_metrics.template.json               — Recommended: metrics payload template (bands + errors)
    ├── 🧾 radiometry_thresholds.template.json            — Recommended: thresholds + gate configuration
    ├── 🧾 radiometry_reason_codes.template.json          — Recommended: normalized reason codes + severity mapping
    ├── 🧾 example_radiometry.pass.json                   — Optional: “golden” pass example (small)
    ├── 🧾 example_radiometry.warn.json                   — Optional: “golden” warn example (small)
    └── 🧾 example_radiometry.fail.json                   — Optional: “golden” fail example (small)
~~~

> The files listed above are recommended conventions for this folder. Add only what is used in production, and keep example payloads small.

---

## 🧾 Template inventory (recommended)

### 1) Metrics payload template

The metrics template SHOULD:

- align with the standard algorithm output envelope,
- report per-band summaries (not tile-level offender lists),
- include deterministic distribution summaries (fixed quantiles; fixed bins when using PSI/KL),
- include masking policy metadata (nodata/cloud/QA rules) as references or hashes (not as large embedded configs).

Skeleton (illustrative only):

~~~json
{
  "algorithm_id": "kfm:rs:validate:radiometry:error_metrics:v1",
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
      "mask_policy_hash": "<sha256>",
      "reference_mode": "none|run|release|trusted",
      "bands": [
        {
          "name": "B04",
          "unit": "reflectance|scaled_reflectance|kelvin|celsius|index",
          "support_px": 0,
          "bias": 0.0,
          "mae": 0.0,
          "rmse": 0.0,
          "median_abs_error": 0.0,
          "mad_residual": 0.0,
          "p10_delta": null,
          "p50_delta": null,
          "p90_delta": null,
          "out_of_range_pct": 0.0,
          "psi": null,
          "kl_divergence": null
        }
      ]
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

- critical vs non-critical thresholds,
- per-band thresholds and allowed ranges,
- deterministic behavior for missing metrics (fail closed vs warn),
- fixed quantile and histogram settings when distribution drift checks are enabled.

Skeleton (illustrative only):

~~~json
{
  "policy_version": "v1",
  "gate_mode": "fail_closed",
  "quantiles": {
    "method": "linear",
    "ps": [0.1, 0.5, 0.9]
  },
  "histograms": {
    "enabled": true,
    "metric": "psi",
    "bin_edges_policy": "pinned",
    "bin_edges_ref": "bins:v1"
  },
  "thresholds": {
    "abs_bias_max": 0.0,
    "mae_max": 0.0,
    "rmse_max": 0.0,
    "out_of_range_pct_max": 0.0,
    "psi_max": null,
    "p50_abs_delta_max": null
  },
  "per_band_thresholds": [
    {
      "band": "B04",
      "unit": "reflectance",
      "expected_range": [0.0, 1.0],
      "abs_bias_max": 0.02,
      "rmse_max": 0.05,
      "critical": true
    }
  ]
}
~~~

### 3) Reason codes and severity mapping template

A reason-code template SHOULD map codes to deterministic severities and optional remediation hints.

Skeleton (illustrative only):

~~~json
{
  "reason_codes": [
    {"code": "REFERENCE_MISSING", "severity": "fail", "hint": "Reference required but not resolvable; check baseline selection or trusted reference availability."},
    {"code": "LOW_SUPPORT", "severity": "warn", "hint": "Too few eligible pixels after masking; verify mask policy and sampling scope."},
    {"code": "UNITS_UNKNOWN", "severity": "fail", "hint": "Unit metadata missing/ambiguous; emit explicit units in STAC properties and pipeline outputs."},
    {"code": "RANGE_VIOLATION", "severity": "fail", "hint": "Out-of-range values exceed policy; confirm scaling, nodata handling, and unit conversions."},
    {"code": "BIAS_EXCEEDS_THRESHOLD", "severity": "fail", "hint": "Systematic bias beyond policy; investigate calibration or processing changes."},
    {"code": "RMSE_EXCEEDS_THRESHOLD", "severity": "warn", "hint": "RMSE beyond policy; check regression, masking, and baseline alignment."},
    {"code": "DISTRIBUTION_DRIFT_EXCEEDS_THRESHOLD", "severity": "warn", "hint": "Distribution shift beyond policy; confirm upstream product changes or pipeline parameters."},
    {"code": "MASK_POLICY_INCONSISTENT", "severity": "warn", "hint": "Mask/nodata policy changed unexpectedly; verify version pinning and metadata emission."},
    {"code": "CARE_REDACTION_APPLIED", "severity": "warn", "hint": "Details withheld under FAIR+CARE policy."}
  ]
}
~~~

---

## 🎯 Determinism requirements for templates

Templates MUST support deterministic computation and reporting:

- stable enumeration:
  - item ids sorted
  - band names sorted by a stable band order
- explicit numeric behavior:
  - quantile method pinned (and recorded)
  - histogram bin edges pinned (do not auto-fit bins per run)
- deterministic masking:
  - mask/nodata policy must be explicitly referenced (hash or config ref)
- deterministic `outcome` and `reason_codes`:
  - reason codes sorted lexicographically
  - severity derived deterministically from policy and mapping
- deterministic sampling metadata (if sampling is used):
  - `seed` and `sample_frame_hash` present and stable

---

## 🛡️ FAIR+CARE and sovereignty posture

Templates and example payloads in this folder MUST be safe to publish in-repo:

- no raw coordinates, site identifiers, or “how to locate” guidance,
- no internal endpoints, tokens, or signed URLs,
- no tile-level offender listings that could expose sensitive areas,
- spatial scope MUST be generalized (`kansas`, region, or coarse H3).

If deeper diagnosis requires restricted detail:

- set `care_gate_status = redact|deny`,
- emit only aggregated band-level metrics and reason codes,
- require steward review via governed channels.

---

## 🧪 CI/CD usage (recommended)

Templates support CI by enabling:

- JSON validation (if schemas exist under governed `schemas/`),
- golden payload regression tests:
  - pass/warn/fail examples remain stable,
- policy determinism tests:
  - same inputs/config → same `reason_codes` ordering and `outcome`.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed radiometry templates index; defined metrics payload template, thresholds template, reason-code mapping, determinism rules, and governance-safe example posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Radiometry" src="https://img.shields.io/badge/Validation-Radiometry-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Radiometry Algorithms](../README.md) ·
[🧮 Algorithms Index](../../README.md) ·
[🧾 Reports](../../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

