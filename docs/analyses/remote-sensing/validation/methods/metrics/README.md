---
title: "📐 KFM — Remote Sensing Validation Metrics (Definitions · Aggregation · Threshold Semantics)"
path: "docs/analyses/remote-sensing/validation/methods/metrics/README.md"

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
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "remote-sensing-validation-metrics"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:metrics:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-metrics"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/metrics/README.md"
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

# 📐 **KFM — Remote Sensing Validation Metrics**
`docs/analyses/remote-sensing/validation/methods/metrics/README.md`

**Purpose**  
Canonical metric definitions and conventions for KFM remote-sensing validation:
naming, units, aggregation rules, threshold semantics, and governance-safe reporting posture.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="Validation Metrics" src="https://img.shields.io/badge/Validation-Metrics-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory defines **what metrics mean** in KFM remote-sensing QA and how they must be computed and reported so that:

- metric values are **comparable across runs and releases**,
- computations are **deterministic** and audit-ready,
- thresholds support **promotion gates** (pass/warn/fail),
- reporting remains **governance-safe** (FAIR+CARE, sovereignty policies).

Algorithm-specific docs live under:

- `../algorithms/README.md` (index)
- `../algorithms/radiometry/README.md`
- `../algorithms/classification/README.md`
- `../algorithms/geometry/README.md`
- `../algorithms/temporal/README.md`
- `../algorithms/drift/README.md`

This directory focuses on **metric semantics**, not implementations.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/
└── 📁 metrics/                                              — Metric definitions and conventions (this directory)
    ├── 📄 README.md                                         — This reference (you are here)
    └── 📁 templates/                                        — Optional: common metric registry / schema templates
~~~

> Keep this directory small and normative. Store large tables, plots, and per-run artifacts under the governed reports structure.

---

## 🧾 Metric design rules (normative)

### 1) Every metric MUST declare its unit and direction

A metric definition MUST include:

- `unit`: explicit, unambiguous (e.g., `ugm3`, `reflectance`, `kelvin`, `px`, `pct`, `ratio`)
- `direction`:
  - `higher_is_better` (e.g., F1, IoU)
  - `lower_is_better` (e.g., RMSE, MAE, bias magnitude)
  - `target_is_best` (e.g., bias target = 0)

### 2) Metrics MUST state the evaluation mask

For raster metrics, a metric MUST specify:

- nodata behavior (exclude by default),
- QA masks (cloud, water, invalid pixels),
- eligibility criteria.

Mask policy MUST be pinned and referenced (config ref or hash).

### 3) Metrics MUST specify aggregation level(s)

Allowed aggregation levels:

- `pixel` (not normally reported directly)
- `tile` / `scene` / `granule`
- `region` (recommended for public summaries)
- `dataset_window` (e.g., a daily run window)
- `release` (release-to-release comparisons)

Public-facing artifacts SHOULD prefer `region` or coarser.

### 4) Metrics MUST be stable under deterministic enumeration

If a metric involves:

- sampling,
- quantiles,
- histogram binning,
- class label ordering,

…then the definition MUST pin:

- seeds and sampling frame rules (when sampling),
- quantile method,
- bin edges,
- class label ordering.

---

## 🧩 Metric families (canonical taxonomy)

### A) Continuous-field error metrics (radiometry)

Common metrics (per band/variable):

- `bias = mean(x - x_ref)` (target = 0)
- `mae = mean(|x - x_ref|)` (lower is better)
- `rmse = sqrt(mean((x - x_ref)^2))` (lower is better)
- `median_abs_error` (robust; lower is better)
- `mad_residual` (robust spread; lower is better)
- distribution deltas: `p10_delta`, `p50_delta`, `p90_delta`
- range checks: `out_of_range_pct`

When histogram drift is used, bins MUST be pinned.

### B) Categorical metrics (classification / masks)

Common metrics (global and per class):

- confusion matrix (label order pinned)
- `precision`, `recall`, `f1`
- `iou` / `jaccard`
- macro vs micro averages (definition must be explicit)
- prevalence reporting (class frequencies) as context (not “corrected” silently)

### C) Geometry integrity metrics

Common metrics (aggregated counts/rates):

- CRS missing/mismatch counts
- invalid/empty geometry counts
- bbox validity and bounds checks
- overlap/gap rates for tiles (if tiling is part of the product)
- grid alignment / GSD drift summaries

Do not report “worst offending locations” in public artifacts.

### D) Temporal metrics

Common metrics:

- missing/unparseable timestamps
- cadence mismatch counts and jitter summaries
- coverage completeness (% expected steps)
- gap counts and max-gap duration
- freshness lag (ops-facing; SLO gate)

### E) Drift / delta metrics (release comparison)

Common metrics:

- counts changed (items/assets/tiles)
- metric deltas (aggregate only)
- threshold outcomes and reason codes

---

## 🧱 Standard metric record (recommended)

Metrics SHOULD be representable as a minimal “metric record” inside algorithm outputs.

~~~json
{
  "metric_id": "kfm:metric:<family>:<name>:v1",
  "name": "rmse",
  "family": "radiometry",
  "unit": "reflectance",
  "direction": "lower_is_better",
  "level": "region",
  "value": 0.0421,
  "support": {
    "n_px": 1234567,
    "n_items": 42
  },
  "method": {
    "mask_policy_hash": "<sha256>",
    "sampling": "full|tiles|stratified|random",
    "seed": 1337,
    "quantile_method": "linear",
    "bin_edges_ref": "bins:v1"
  }
}
~~~

Notes:

- `support` MUST be present when it affects interpretability (low support must trigger reason codes).
- `method` should prefer refs/hashes over embedding long configs.

---

## 🚦 Threshold semantics (normative)

Threshold evaluation MUST be deterministic and explainable.

### Threshold fields (recommended)

- `threshold_id` (stable identifier)
- `metric_id` (what is being thresholded)
- `operator`: `<=`, `<`, `>=`, `>`, `between_inclusive`
- `value` or `min/max`
- `severity`: `warn` or `fail`
- `gate_mode`: `fail_closed` default

Example (illustrative):

~~~json
{
  "threshold_id": "kfm:threshold:radiometry:rmse:max:v1",
  "metric_id": "kfm:metric:radiometry:rmse:v1",
  "operator": "<=",
  "value": 0.05,
  "severity": "fail",
  "gate_mode": "fail_closed"
}
~~~

### Outcomes

- `pass`: no threshold breaches
- `warn`: at least one warn breach, no fail breach
- `fail`: at least one fail breach or missing required inputs under fail-closed policy

Reason codes MUST be emitted for:

- each fail condition,
- policy-required warn conditions (e.g., low support).

---

## 🎯 Determinism checklist (metric-level)

Metric computations MUST document (or reference) the following:

- stable item ordering (by `id`, then time when relevant)
- stable band/class ordering
- numeric dtype and NaN handling rules
- pinned quantile method (if any)
- pinned histogram bins (if any)
- sampling seed and sample-frame hash (if sampling)
- stable tie-breaking for reason-code emission

---

## 🛡️ FAIR+CARE and sovereignty posture

Metrics can leak sensitive detail when they are:

- computed on very small AOIs,
- broken down to fine-grained spatial partitions,
- paired with “worst offender” location lists.

Rules:

- public artifacts MUST use generalized spatial scopes (region or coarse grid)
- never embed raw coordinates, signed URLs, secrets, or restricted identifiers
- when governance is unclear or conflicting:
  - fail closed or require review (policy-defined)
  - emit `care_gate_status` and `sovereignty_gate` in algorithm outputs

---

## 🗺️ Relationship to algorithms and reports

- Algorithms define **how** metrics are computed for a product family.
- This directory defines **what** metrics mean and how they are reported.
- Reports aggregate algorithm outputs:
  - per-run: `../../reports/per-run/`
  - daily: `../../reports/daily/`
  - releases: `../../reports/releases/`

Recommended pattern:

- keep algorithm outputs small and stable,
- store heavy artifacts outside docs and link via STAC assets and PROV refs.

---

## 🧭 High-level flow (metric lifecycle)

~~~mermaid
flowchart TD
  A["Enumerate governed scope (items/bands/classes)"] --> B["Apply mask policy (pinned)"]
  B --> C["Compute metrics deterministically"]
  C --> D["Evaluate thresholds (policy)"]
  D --> E["Emit outcome + reason codes + refs (STAC/DCAT/PROV)"]
~~~

---

## ➕ Adding a metric (governed checklist)

1. Define `metric_id`, name, family, unit, direction.
2. Specify mask policy requirements and aggregation level.
3. Specify determinism requirements (ordering, quantiles, bins, seed policy).
4. Specify thresholds and severities (or document “no gate”).
5. Ensure algorithm outputs include:
   - metric values,
   - support counts,
   - refs/hashes for configs and masks,
   - reason codes for breaches.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed metrics reference for remote-sensing validation; defined metric taxonomy, record format, threshold semantics, determinism rules, and governance-safe reporting posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Methods](../README.md) ·
[🧮 Algorithms](../algorithms/README.md) ·
[🧾 Reports](../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
