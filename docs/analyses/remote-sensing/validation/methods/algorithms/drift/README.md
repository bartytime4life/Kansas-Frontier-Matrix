---
title: "📉 KFM — Drift Validation Algorithms (Run→Run · Release→Release · Threshold Gates)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/drift/README.md"

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

intent: "remote-sensing-validation-algorithms-drift"
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

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:drift:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-algorithms-drift"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/drift/README.md"
immutability_status: "version-pinned"

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

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 📉 **KFM — Drift Validation Algorithms**
`docs/analyses/remote-sensing/validation/methods/algorithms/drift/README.md`

**Purpose**  
Define drift-detection algorithms used in KFM remote-sensing validation to detect **unintended changes**
between **runs** and between **releases**, and to enforce **promotion gates** with deterministic, governance-safe outputs.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Drift-blue" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

“Drift” in this context means: **meaningful change** in outputs or metadata beyond expected variance, including:

- structural drift (schema/assets changed),
- volume drift (tile/item/asset counts change),
- spatial/temporal drift (coverage windows change),
- distribution drift (pixel-value distributions shift),
- metric drift (validation metrics shift),
- provenance drift (lineage changes unexpectedly).

Drift checks are designed to:

- support **per-run** QA (is this run anomalous?),
- support **daily** rollups (is there a trend?),
- support **release promotion** (is this SemVer bump justified?).

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/     — Algorithm docs
└── 📁 drift/                                                     — Drift validation (this directory)
    ├── 📄 README.md                                              — This reference
    └── 📁 templates/                                             — Optional: drift payload templates/schemas
~~~

---

## 🧩 Drift taxonomy (what we measure)

### 1) Structural drift (catalog/schema/asset shape)

Examples:

- STAC Item properties changed (new/removed required keys),
- assets added/removed/renamed,
- projection/CRS changes,
- nodata conventions changed,
- class-map changes (for classification products).

### 2) Volume drift (counts and cardinality)

Examples:

- tile count shifts beyond expected range,
- missing asset rate increases,
- per-day item count changes unexpectedly.

### 3) Spatial and temporal drift (coverage changes)

Examples:

- bbox or coarse H3 coverage differs from baseline,
- time range (start/end) differs from expected cadence.

### 4) Distribution drift (continuous values)

Examples:

- reflectance/temperature/index histograms shift,
- quantiles shift (p50/p90),
- divergence metrics exceed thresholds.

### 5) Metric drift (validation outputs)

Examples:

- MAE/RMSE rises beyond thresholds,
- macro-F1 or IoU drops beyond thresholds.

### 6) Provenance drift (lineage anomalies)

Examples:

- the generating `prov:Activity` differs unexpectedly,
- input entities differ from policy-defined sources,
- missing required provenance links.

---

## 🧭 Baseline selection (deterministic)

Drift requires a baseline to compare against. Supported baseline modes:

- **run→run**: compare current run against the immediately prior successful run
- **release→release**: compare new release against the previous release tag
- **pinned baseline**: compare against a policy-pinned baseline id (recommended for high-stakes products)

Baseline selection MUST be deterministic:

- baseline id resolved via stable ordering (by `ended_utc` then `run_id`, or by SemVer)
- if baseline cannot be resolved, fail closed (see reason codes) unless policy allows `warn`

Recommended baseline identifiers:

- `run_id`: `urn:kfm:run:...`
- `release_version`: `vMAJOR.MINOR.PATCH`
- catalog anchors: STAC Item/Collection `id` and `version`

---

## 🧪 Determinism requirements (non-negotiable)

Drift computation MUST be reproducible:

- stable enumeration and sorting:
  - sort item ids, asset keys, tile ids, timestamps
- fixed bin edges for histograms (if used)
- fixed quantile definitions and interpolation method
- stable rounding rules (if rounding is used, document it)
- when sampling is required:
  - fixed seed recorded in outputs
  - sample frame deterministic (sorted tile list, deterministic pixel indexing)
  - stratification rules explicit and recorded

---

## 🧮 Recommended metrics (by drift type)

### Structural drift metrics

- `assets_added`, `assets_removed`, `assets_renamed` (counts and key lists when safe)
- `required_property_missing_count`
- `schema_version_changed` (boolean)
- `crs_changed` (boolean)
- `nodata_policy_changed` (boolean)
- `class_map_hash_changed` (boolean; for classification)

### Volume drift metrics

- `items_count_delta` and `%`
- `tiles_count_delta` and `%`
- `assets_missing_rate_delta` and `%`

### Spatial/temporal drift metrics

- `time_start_delta_s`, `time_end_delta_s`
- `coverage_area_delta_pct` (generalized; do not expose sensitive shapes)
- `coarse_h3_cells_delta` (counts only when governed)

### Distribution drift metrics (continuous values)

Use only when policy allows and inputs are non-sensitive:

- quantile deltas:
  - `p10_delta`, `p50_delta`, `p90_delta`
- histogram divergence (fixed bins):
  - `psi` (population stability index) or `kl_divergence` (policy-configurable)
- robust measures:
  - `median_abs_shift`, `mad_delta`

### Metric drift (validation metric changes)

- `rmse_delta`, `mae_delta`
- `macro_f1_delta`, `iou_positive_delta`
- `pass_rate_delta` across checks

### Provenance drift metrics

- `inputs_changed_count` (ids only)
- `missing_prov_links_count`
- `activity_type_changed` (boolean)

---

## 🚦 Threshold gates and outcomes (policy-driven)

Thresholds MUST be configurable per product family and may vary by release stage.

Recommended outcomes:

- `pass`: within thresholds
- `warn`: non-critical drift or low-confidence (e.g., low support)
- `fail`: critical drift threshold breached (promotion blocked)

### Reason codes (normalized)

| Reason code | Typical trigger | Default severity |
|---|---|---|
| `BASELINE_NOT_FOUND` | No baseline run/release resolvable | fail |
| `STRUCTURE_BREAKING_CHANGE` | Required keys/assets removed or renamed | fail |
| `CRS_CHANGED` | CRS differs from baseline | fail |
| `COUNT_DELTA_EXCEEDS_THRESHOLD` | Items/tiles/assets change beyond allowed % | warn/fail |
| `DISTRIBUTION_DRIFT_EXCEEDS_THRESHOLD` | PSI/KL/quantile drift beyond allowed | warn/fail |
| `METRIC_REGRESSION` | RMSE up or F1/IoU down beyond allowed | fail |
| `PROVENANCE_INCOMPLETE` | Missing required PROV links | fail |
| `CARE_REDACTION_APPLIED` | Report had to redact details | warn |
| `SOVEREIGNTY_GATE_RESTRICTED` | Restricted/unknown governance posture | warn/fail (policy) |

Fail-closed rule:

- if governance posture is unknown or restricted and drift computation would reveal sensitive details, emit an outcome of `warn` or `fail` per policy and set `care_gate_status` accordingly.

---

## 📦 Standard output artifact (recommended)

Drift algorithms SHOULD emit a small, stable artifact suitable for rollups:

- `drift.delta.json` (per-run and per-release)

Recommended shape (truncated):

~~~json
{
  "algorithm_id": "kfm:rs:validate:drift:delta:v1",
  "run_id": "urn:kfm:run:<current>",
  "baseline": {
    "mode": "run|release|pinned",
    "run_id": "urn:kfm:run:<baseline>",
    "release_version": "vMAJOR.MINOR.PATCH"
  },
  "dataset_id": "urn:kfm:dataset:<...>",
  "scope": {
    "time_start_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "time_end_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "spatial_scope": "kansas|region:<...>|h3:r<...>"
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
      "tiles_delta_pct": 0.0
    },
    "structure": {
      "assets_added": 0,
      "assets_removed": 0,
      "schema_version_changed": false
    },
    "distributions": {
      "psi": null,
      "p50_delta": null
    },
    "metrics": {
      "rmse_delta": null,
      "macro_f1_delta": null
    }
  },
  "thresholds": {
    "items_delta_pct_max": 0.0,
    "psi_max": null
  },
  "outcome": "pass|warn|fail",
  "reason_codes": [],
  "refs": {
    "stac_items": [],
    "dcat_datasets": [],
    "prov_bundles": []
  },
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ"
}
~~~

Notes:

- keep values aggregated and safe
- do not embed full diffs of sensitive geometry or pixels
- if listing asset keys, ensure it is policy-safe for the product class

---

## 🗺️ High-level drift flow

~~~mermaid
flowchart TD
  A["Select baseline (run or release)"] --> B["Enumerate artifacts deterministically"]
  B --> C["Compute deltas (counts, structure, metrics, distributions)"]
  C --> D["Evaluate thresholds (policy)"]
  D --> E["Emit drift.delta.json (small, stable)"]
  E --> F["Roll up into per-run, daily, and release reports"]
  E --> G["Link to STAC/DCAT/PROV references"]
~~~

---

## 🔗 Report integration (where drift shows up)

Drift outputs are consumed by:

- Per-run bundles:
  - `docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/drift.delta.json`
- Daily rollups:
  - `docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/metrics.json`
- Release rollups:
  - `docs/analyses/remote-sensing/validation/reports/releases/v<semver>/drift.delta.json`

Keep the drift artifact small and use references for heavy or restricted detail.

---

## 🛡️ FAIR+CARE and sovereignty posture

Drift checks MUST not leak sensitive information:

- avoid “worst tile” or “best tile” lists when governance labels restrict
- prefer region-level or coarse H3 reporting
- never include raw coordinates, site identifiers, or access instructions
- if drift requires restricted detail to diagnose, emit `outcome = warn|fail` and require steward review via governed channels

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed drift validation algorithms reference; defined drift taxonomy, deterministic baseline selection, thresholds/reason codes, and standard drift artifact shape. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Drift-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Algorithms](../README.md) ·
[🧾 Reports](../../../reports/README.md) ·
[🧾 Per‑Run Bundles](../../../reports/per-run/README.md) ·
[📅 Daily Reports](../../../reports/daily/README.md) ·
[🏷️ Release Reports](../../../reports/releases/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

