---
title: "🌈 KFM — Radiometry Validation Algorithms (Continuous Fields · Error Metrics · Distribution Drift)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/radiometry/README.md"

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

intent: "remote-sensing-validation-algorithms-radiometry"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:radiometry:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-algorithms-radiometry"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/radiometry/README.md"
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

# 🌈 **KFM — Radiometry Validation Algorithms**
`docs/analyses/remote-sensing/validation/methods/algorithms/radiometry/README.md`

**Purpose**  
Governed metric set and deterministic computation rules for validating **continuous-valued** remote-sensing outputs
in KFM (reflectance, temperature, indices, continuous masks), including robust error metrics, distribution drift checks,
and FAIR+CARE-safe reporting constraints.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Radiometry" src="https://img.shields.io/badge/Validation-Radiometry-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Radiometry validation targets **continuous fields**, including:

- surface reflectance bands (or TOA reflectance),
- thermal brightness temperature / LST products,
- vegetation/water indices (NDVI, NDWI, NBR, etc.),
- continuous probability layers (e.g., cloud probability),
- continuous biophysical estimates (where governed).

Goals:

- detect systematic bias or calibration shifts,
- catch range errors, unit mistakes, and nodata leakage,
- quantify quality against baselines or references (when available),
- enforce drift and promotion gates with deterministic, audit-ready outputs.

Radiometry validation outputs MUST remain governance-safe: avoid leaking sensitive location detail through overly granular reporting.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/     — Algorithm docs
└── 📁 radiometry/                                                — Radiometry validation (this directory)
    ├── 📄 README.md                                              — This reference
    └── 📁 templates/                                             — Optional: payload templates/schemas
~~~

---

## 🧾 Inputs (conceptual)

Radiometry validation typically compares:

- `x`: produced continuous raster(s)
- `x_ref`: reference raster(s) or baseline (optional but recommended)

Common reference options (policy-dependent):

- previous run output (run→run drift)
- previous release output (release→release drift)
- trusted upstream product or independently processed baseline
- station/point observations (requires collocation; governed separately)

Required metadata:

- band names / variable identifiers and units
- nodata / mask policy (cloud mask, QA mask, water mask, etc.)
- spatial and temporal scope (generalized where required by policy)
- sampling policy (full coverage vs deterministic sampling)
- governance posture: CARE gate and sovereignty gate

---

## ✅ Core metrics (recommended)

### 1) Error metrics (per band / variable)

For eligible pixels (after nodata/mask rules):

- **Bias** (mean error): `mean(x - x_ref)`
- **MAE**: `mean(|x - x_ref|)`
- **RMSE**: `sqrt(mean((x - x_ref)^2))`
- **Median absolute error** (robust): `median(|x - x_ref|)`
- **MAD of residuals** (robust spread): `median(|(x - x_ref) - median(x - x_ref)|)`

Determinism:

- define eligibility masking exactly (cloud/nodata/QA)
- define numeric dtype behavior and rounding (if any)
- define how NaNs are handled (exclude by default unless policy differs)

### 2) Correlation / agreement (optional; policy-driven)

When meaningful for the variable:

- Pearson correlation `r`
- Spearman correlation `ρ`
- `R²` (document definition; do not mix with correlation squared unless explicitly intended)

Use only when:

- sample support is sufficient,
- distribution is not degenerate under masks.

### 3) Quantile deltas (distribution alignment)

Compute deltas between produced and reference distributions:

- `Δp10`, `Δp50`, `Δp90` for `x - x_ref`
- optionally report absolute reference quantiles to confirm ranges (policy safe)

Quantile method MUST be fixed (interpolation definition recorded).

### 4) Range and unit sanity (always required)

Per band/variable:

- min/max observed (masked, aggregated)
- expected physical or product range checks
- percentage of values outside expected bounds

Examples (illustrative; do not treat as universal):

- reflectance typically [0, 1] (or [0, 10000] scaled) depending on product
- probabilities typically [0, 1]
- temperatures in Kelvin vs Celsius must be explicit

---

## 📉 Distribution drift checks (recommended)

These checks detect shifts even without a pixel-level reference.

### Histogram-based divergence (optional; policy-driven)

For fixed bins (must be pinned):

- **PSI** (Population Stability Index) or
- **KL divergence** (if using normalized histograms)

Rules:

- bins must be fixed by policy (not auto-binned per run)
- histogram computation must be deterministic (masking, bin edges, normalization)

### Robust shift summaries

- `median_shift` (median of x vs baseline)
- `p90_shift` (p90 delta)
- `mad_shift` (spread shift)

---

## 🧪 Determinism requirements (non-negotiable)

Radiometry validation MUST be reproducible:

- stable enumeration and ordering:
  - items sorted by `id`
  - bands sorted by stable band order
  - tile ids sorted (if tiling)
- fixed masks:
  - explicit nodata
  - explicit cloud/QA exclusion rules
- fixed sampling behavior (if sampling):
  - deterministic seed recorded
  - deterministic sample frame hash recorded (tile list + pixel indexing)
  - fixed sample sizes and stratification rules
- fixed numeric behavior:
  - explicit dtype
  - explicit quantile method
  - explicit bin edges for any histogram-based metric
- deterministic thresholds and outcomes:
  - same metrics + same policy → same `outcome` and `reason_codes` ordering

Fail-closed posture:

- missing required units, missing nodata rules, or missing policy metadata MUST cause `fail` when required by contract.

---

## 🚦 Thresholds and gate outcomes (policy-driven)

Thresholds are product-family dependent and should be pinned in governed configs.

Common policy gates:

- `mae_max`
- `rmse_max`
- `abs_bias_max`
- `out_of_range_pct_max`
- `psi_max` (if PSI used)
- `p50_abs_delta_max` (distribution shift bounds)

Outcomes:

- `pass`: within thresholds
- `warn`: non-critical threshold breach or low-confidence (e.g., low support)
- `fail`: critical threshold breached (promotion blocked)

---

## 🧾 Normalized reason codes (recommended)

| Reason code | Typical trigger | Default severity |
|---|---|---|
| `REFERENCE_MISSING` | Reference required but not provided/resolvable | fail |
| `LOW_SUPPORT` | Too few eligible pixels/samples after masking | warn/fail (policy) |
| `UNITS_UNKNOWN` | Unit metadata missing or ambiguous | fail |
| `RANGE_VIOLATION` | Out-of-range rate exceeds policy | fail |
| `BIAS_EXCEEDS_THRESHOLD` | |bias| exceeds policy | fail |
| `MAE_EXCEEDS_THRESHOLD` | MAE exceeds policy | warn/fail |
| `RMSE_EXCEEDS_THRESHOLD` | RMSE exceeds policy | warn/fail |
| `DISTRIBUTION_DRIFT_EXCEEDS_THRESHOLD` | PSI/KL/quantile drift exceeds policy | warn/fail |
| `MASK_POLICY_INCONSISTENT` | Nodata/cloud/QA rules changed unexpectedly | warn/fail |
| `BASELINE_NOT_FOUND` | Baseline required but not resolvable | fail |
| `CARE_REDACTION_APPLIED` | Details withheld under policy | warn |
| `SOVEREIGNTY_GATE_RESTRICTED` | Restricted/unknown governance posture | warn/fail (policy) |

---

## 📦 Standard output shape (recommended)

Radiometry validation SHOULD emit a small, stable artifact (suitable for rollups):

- per-run: `metrics.radiometry.json` (or embedded in run metrics)
- release: `drift.radiometry.delta.json` (optional; aggregated)

Example (truncated):

~~~json
{
  "algorithm_id": "kfm:rs:validate:radiometry:error_metrics:v1",
  "run_id": "urn:kfm:run:<...>",
  "dataset_id": "urn:kfm:dataset:<...>",
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
      "bands": [
        {
          "name": "B04",
          "unit": "reflectance",
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
          "psi": null
        }
      ]
    },
    "thresholds": {
      "abs_bias_max": 0.0,
      "mae_max": 0.0,
      "rmse_max": 0.0,
      "out_of_range_pct_max": 0.0,
      "psi_max": null
    },
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

Notes:

- keep band-level detail policy-safe; avoid tile-level offender lists
- keep spatial scope generalized in in-repo artifacts

---

## 🗺️ High-level radiometry validation flow

~~~mermaid
flowchart TD
  A["Select scope + masks (policy)"] --> B["Resolve baseline/reference (optional)"]
  B --> C["Enumerate items/bands deterministically"]
  C --> D["Compute error metrics + robust stats"]
  C --> E["Compute distribution summaries (quantiles / hist divergence)"]
  D --> F["Evaluate thresholds (policy)"]
  E --> F
  F --> G["Emit small metrics artifact + refs to STAC/DCAT/PROV"]
~~~

---

## 🛡️ FAIR+CARE and sovereignty posture

Radiometry metrics can become sensitive when:

- AOIs are small,
- reporting includes precise spatial stratification (tile-level, site-level),
- “best/worst locations” are included.

Rules:

- in repo-facing outputs, use generalized `spatial_scope` (region-level or coarse H3)
- do not include raw coordinates or “how to locate” guidance
- if policy requires redaction:
  - set `care_gate_status = redact|deny`
  - emit only aggregated metrics and reason codes
  - require steward review for deeper diagnostics through governed channels

---

## 🔗 Report integration

Radiometry validation feeds:

- per-run bundles: `docs/analyses/remote-sensing/validation/reports/per-run/`
- daily rollups: `docs/analyses/remote-sensing/validation/reports/daily/`
- release rollups: `docs/analyses/remote-sensing/validation/reports/releases/`

Prefer linking from reports to:

- STAC Items/Collections representing validated artifacts
- DCAT datasets/distributions
- PROV bundles for lineage and configuration snapshots

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed radiometry validation algorithms reference; defined continuous-field metrics, distribution drift checks, determinism rules, normalized reason codes, and governance-safe output shape. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Radiometry" src="https://img.shields.io/badge/Validation-Radiometry-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Algorithms](../README.md) ·
[🧾 Reports](../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

