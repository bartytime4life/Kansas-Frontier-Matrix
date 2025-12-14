---
title: "🧮 KFM — Remote Sensing Validation Algorithms (Metrics · Determinism · Governance)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Reference"
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

intent: "remote-sensing-validation-algorithms"
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

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-algorithms"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🧮 **KFM — Remote Sensing Validation Algorithms**
`docs/analyses/remote-sensing/validation/methods/algorithms/README.md`

**Purpose**  
Canonical index and conventions for **validation algorithms** used in KFM remote-sensing QA:
metric definitions, deterministic computation rules, and governance-safe reporting.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/Validation-Algorithms-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory documents the **algorithms and metrics** used to validate remote-sensing outputs in KFM.

Scope:

- deterministic metric computation (same inputs + same config → same outputs),
- governance-safe reporting (no sensitive leakage),
- a small set of reusable “algorithm families” (radiometry, classification, geometry, time-series consistency, drift),
- a standardized output shape suitable for:
  - per-run bundles,
  - daily rollups,
  - release promotion rollups.

This is documentation-first. Implementations may live elsewhere (e.g., `src/`, `tools/`, or pipeline code), but the **definitions and contracts** are governed here.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/           — Validation method docs
└── 📁 algorithms/                                           — Algorithm definitions and contracts (this directory)
    ├── 📄 README.md                                         — This index (you are here)
    ├── 📁 templates/                                        — Optional: JSON templates for outputs
    ├── 📁 radiometry/                                       — Optional: reflectance/temperature metrics
    ├── 📁 classification/                                   — Optional: confusion-matrix metrics
    ├── 📁 geometry/                                         — Optional: georegistration / footprint checks
    ├── 📁 temporal/                                         — Optional: temporal stability / continuity checks
    └── 📁 drift/                                            — Optional: release-to-release drift checks
~~~

> Subfolders are recommended for organization. Add only what you use, under governance review.

---

## 🧩 Algorithm families (recommended)

### 1) Radiometry / continuous fields

Use when validating continuous-valued rasters (reflectance, temperature, elevation-derived layers, indices).

Common metrics:

- MAE, RMSE, bias (mean error)
- correlation (Pearson/Spearman) when appropriate
- robust error (median absolute error, MAD-based) for heavy tails
- quantile errors (p50/p90 absolute error) for distribution alignment

### 2) Classification / masks

Use when validating categorical layers (land cover, water masks, cloud masks, burn scars).

Common metrics:

- confusion matrix
- precision, recall, F1
- IoU / Jaccard
- per-class metrics + macro/micro averages
- prevalence and class-imbalance notes (reported, not “corrected” silently)

### 3) Geometry / spatial integrity

Use to validate spatial correctness without leaking sensitive detail.

Common checks:

- CRS present and expected
- bounding box sanity (non-empty; within expected region bounds)
- pixel alignment / grid resolution sanity
- georegistration drift against control features (aggregated; no precise site coordinates)

### 4) Temporal consistency

Use for time-series or repeated acquisitions.

Common checks:

- missing-timestep detection
- temporal lag and expected cadence
- continuity checks (spikes, steps, discontinuities)
- seasonality-aware drift flags (domain-configurable)

### 5) Drift / release deltas

Use to compare new release vs previous release.

Common outputs:

- counts changed (tiles/assets/items)
- metric deltas (aggregate only)
- threshold outcomes (pass/fail), and “reason codes” for gate failures

---

## 🧾 Input and output contracts (governed)

### Required inputs (conceptual)

Algorithms MUST define:

- input dataset identifiers (STAC/DCAT ids where applicable),
- the evaluation scope:
  - spatial window (generalized region / coarse grid when required),
  - temporal window (UTC),
  - sampling method (tile set, stratified sample, full coverage),
- baseline/reference definition (if any),
- governance posture applied (CARE gate result, sovereignty gate result).

### Required outputs (standard shape)

Every algorithm run SHOULD emit a small machine-readable summary:

~~~json
{
  "algorithm_id": "kfm:rs:validate:<family>:<name>:v1",
  "run_id": "urn:kfm:run:<...>",
  "dataset_id": "urn:kfm:dataset:<...>",
  "scope": {
    "time_start_utc": "2025-12-14T00:00:00Z",
    "time_end_utc": "2025-12-15T00:00:00Z",
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
      "rmse": 0.0,
      "mae": 0.0
    },
    "thresholds": {
      "rmse_max": 0.0
    },
    "outcome": "pass|fail|warn",
    "reason_codes": []
  },
  "refs": {
    "stac_items": [],
    "dcat_datasets": [],
    "prov_bundles": []
  },
  "checksums": {
    "input_pack_sha256": "<sha256>",
    "output_sha256": "<sha256>"
  },
  "created_utc": "2025-12-14T00:00:00Z"
}
~~~

Notes:

- Keep outputs **small** and **stable** (aggregation and reason codes).
- If detailed tables are needed, store them as governed artifacts and reference them.

---

## 🎯 Determinism requirements (non-negotiable)

Validation algorithms MUST be reproducible:

- stable sorting before aggregation,
- fixed random seeds when sampling (and record them),
- pinned parameters and thresholds (recorded in a config snapshot),
- consistent numeric behavior (explicit dtype/rounding rules when needed),
- deterministic “reason code” selection (no ambiguous tie behavior).

### Sampling determinism (when sampling is used)

If `sampling != full`, record:

- seed,
- sample frame (how candidates were enumerated),
- sampling strategy (stratification keys, weights),
- sample count per stratum.

---

## 🛡️ FAIR+CARE and sovereignty posture

Validation can accidentally expose sensitive locations through:

- small AOIs,
- “before/after” visuals,
- precise coordinate summaries,
- rare-class examples.

Rules:

- reports and algorithm outputs MUST obey governance labels on inputs.
- where redaction is required:
  - report spatial scope at generalized levels only (region/coarse grid),
  - avoid embedding coordinates or “how to locate” details,
  - prefer aggregated metrics and counts.
- if governance status is unclear:
  - fail closed (`outcome = "warn"` or `"fail"` per policy),
  - emit `care_gate_status = "deny"` or `sovereignty_gate = "unknown"` and require review.

---

## 🧪 Validation & CI/CD alignment

Algorithm docs and outputs SHOULD support:

- per-run bundles: `docs/analyses/remote-sensing/validation/reports/per-run/`
- daily rollups: `docs/analyses/remote-sensing/validation/reports/daily/`
- release rollups: `docs/analyses/remote-sensing/validation/reports/releases/`

Recommended CI checks:

- schema validation for algorithm output JSON (when a schema is defined)
- threshold gate enforcement (pass/fail outcomes consistent with policy)
- leakage checks for restricted fields (no coordinates, no signed URLs, no secrets)

---

## ➕ Adding a new algorithm (governed checklist)

1. Assign an `algorithm_id` and family.
2. Define:
   - inputs and scope,
   - metrics and thresholds,
   - determinism rules (sorting, seed behavior, rounding),
   - governance posture (what is redacted and when).
3. Add documentation under the appropriate family folder (or extend this README).
4. Ensure outputs match the standard shape (or document an approved extension).
5. Update report writers/rollups to include the new algorithm in:
   - per-run summaries,
   - daily aggregates,
   - release promotion rollups.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed index for remote-sensing validation algorithms; defined families, determinism rules, governance posture, and standard output shape. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Methods](../README.md) ·
[📡 Validation](../../README.md) ·
[🧾 Reports](../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
