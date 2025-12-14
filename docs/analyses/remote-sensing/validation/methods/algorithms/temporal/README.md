---
title: "⏱️ KFM — Temporal Validation Algorithms (Cadence · Freshness · Coverage · Time Semantics)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/temporal/README.md"

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

intent: "remote-sensing-validation-algorithms-temporal"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:temporal:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-algorithms-temporal"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/temporal/README.md"
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

# ⏱️ **KFM — Temporal Validation Algorithms**
`docs/analyses/remote-sensing/validation/methods/algorithms/temporal/README.md`

**Purpose**  
Governed metric set and deterministic computation rules for validating **time semantics** of remote-sensing outputs in KFM:
cadence correctness, temporal coverage/completeness, freshness/lag, and time-range integrity.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Temporal-blue" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Temporal validation ensures that every derived artifact is **time-correct** and operationally reliable:

- timestamps are present and unambiguous,
- time ranges are valid (`start <= end`),
- coverage matches the expected cadence (daily, 5‑day composite, seasonal, etc.),
- missing intervals and duplicates are detected deterministically,
- freshness/lag SLOs can be computed and audited,
- release promotion can be gated on temporal integrity (and SemVer alignment where applicable).

This is required for:

- per-run validation bundles,
- daily rollups and freshness dashboards,
- release promotion reports and drift checks.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/     — Algorithm docs
└── 📁 temporal/                                                  — Temporal validation (this directory)
    ├── 📄 README.md                                              — This reference
    └── 📁 templates/                                             — Optional: payload templates/schemas
~~~

---

## 🧾 Inputs (conceptual)

Temporal validation operates on **time-bearing artifacts**, typically:

- STAC Items:
  - `datetime` (instant products) OR
  - `start_datetime` / `end_datetime` (interval products)
- optional run metadata:
  - `run_started_utc`, `run_ended_utc`, `exported_at`
- optional pipeline policy:
  - expected cadence, tolerance windows, and freshness targets
- optional baseline:
  - prior run or prior release (for drift-style temporal comparisons)

Minimum required metadata per item:

- stable `id`
- one of:
  - `datetime`, or
  - (`start_datetime` and `end_datetime`)
- dataset cadence policy reference (how often we expect items/assets to be produced)

---

## ✅ Core checks (recommended)

### 1) Timestamp presence and parseability

Validate that each item has required temporal fields:

- `datetime` OR (`start_datetime` and `end_datetime`)
- ISO8601 parseable
- UTC-normalized in output metrics (do not silently assume local time)

Metrics:

- `datetime_missing_count`
- `datetime_unparseable_count`
- `timezone_ambiguous_count`

### 2) Time-range integrity (interval products)

For interval products:

- `start_datetime <= end_datetime`
- duration within policy range (e.g., daily composites not spanning weeks unless intended)

Metrics:

- `start_end_invalid_count`
- `duration_out_of_policy_count`

### 3) Monotonicity and duplicates (sequence integrity)

Given a deterministic ordering of items (by `datetime` then `id`):

- detect non-monotonic time ordering (for sequences that must be monotonic by design)
- detect duplicate timestamps when disallowed (same `datetime` + same scope)

Metrics:

- `non_monotonic_count`
- `duplicate_timestamp_count`

### 4) Cadence correctness (expected interval matching)

Cadence types (examples):

- hourly, daily, weekly, monthly
- N‑day composites (e.g., 5‑day)
- event-driven (no fixed cadence; separate policy)

Checks:

- compute observed deltas between consecutive timestamps
- compare to expected cadence within allowed tolerance
- record jitter distribution (p50/p95)

Metrics:

- `cadence_expected` (policy string)
- `cadence_mismatch_count`
- `jitter_s_p50`, `jitter_s_p95`

### 5) Completeness and missing intervals (coverage)

For a defined scope window `[T0, T1)` and an expected cadence:

- compute expected time steps
- count present time steps
- detect gaps longer than `gap_max_steps` or `gap_max_duration`

Metrics:

- `coverage_expected_steps`
- `coverage_present_steps`
- `coverage_pct`
- `gap_count`
- `max_gap_steps`
- `max_gap_duration_s`

### 6) Freshness and lag (ops-facing, governed)

Given `now_utc` at validation time:

- `freshness_lag_s = now_utc - newest_item_time_utc`
- evaluate against policy target(s) (domain-specific)

Metrics:

- `freshness_lag_s_p50`, `freshness_lag_s_p95`
- `freshness_slo_breach` (boolean or count)

> Freshness checks MUST be computed from explicit timestamps and must not infer “latest” without enumerating all eligible artifacts deterministically.

---

## 🧪 Determinism requirements (non-negotiable)

Temporal validation MUST be reproducible:

- stable enumeration and ordering:
  - items sorted by `(effective_datetime_utc ASC, id ASC)`
- explicit field precedence:
  - if both `datetime` and start/end exist, policy must decide which is authoritative
- fixed tolerance parameters pinned in config:
  - cadence expected and tolerance
  - gap thresholds (max steps/duration)
  - duration bounds for interval products
  - freshness SLO targets and measurement window
- fixed rounding behavior:
  - if rounding timestamps to bins is used (e.g., hourly bins), the binning must be explicit and recorded
- baseline selection deterministic when used:
  - previous run resolved by stable ordering rules
  - previous release resolved by SemVer or governed ledger order

Fail-closed posture:

- missing required time fields or unparseable timestamps MUST trigger `fail` when required by contract.

---

## 🚦 Thresholds and gate outcomes (policy-driven)

Temporal thresholds are product-family and stage dependent.

Common policy gates:

- `datetime_missing_count_max = 0` (critical)
- `datetime_unparseable_count_max = 0` (critical)
- `start_end_invalid_count_max = 0` (critical)
- `coverage_pct_min` (warn/fail depending on product)
- `max_gap_steps_max` or `max_gap_duration_s_max`
- `freshness_lag_s_p95_max` (SLO gate; can be warn/fail)
- `duplicate_timestamp_count_max` (critical for deterministic series)

Outcome:

- `pass`: within thresholds
- `warn`: non-critical breach, low-confidence scope, or policy redaction applied
- `fail`: critical breach (promotion blocked)

---

## 🧾 Normalized reason codes (recommended)

| Reason code | Typical trigger | Default severity |
|---|---|---|
| `DATETIME_MISSING` | Required `datetime` or start/end fields absent | fail |
| `DATETIME_UNPARSEABLE` | ISO8601 parse failure | fail |
| `TIMEZONE_AMBIGUOUS` | Timestamp lacks timezone or mixed tz policies | fail |
| `START_END_INVALID` | `start_datetime > end_datetime` | fail |
| `DURATION_OUT_OF_POLICY` | Interval duration outside allowed range | warn/fail |
| `CADENCE_MISMATCH` | Observed deltas outside tolerance | warn/fail |
| `TEMPORAL_GAP_EXCESS` | Gaps exceed policy thresholds | warn/fail |
| `DUPLICATE_TIMESTAMPS` | Duplicate timestamp collisions | fail |
| `NON_MONOTONIC_TIMES` | Non-monotonic time ordering where disallowed | warn/fail |
| `FRESHNESS_SLO_BREACH` | Freshness lag exceeds target | warn/fail |
| `BASELINE_NOT_FOUND` | Baseline required but not resolvable | fail |
| `CARE_REDACTION_APPLIED` | Details withheld under policy | warn |
| `SOVEREIGNTY_GATE_RESTRICTED` | Restricted/unknown governance posture | warn/fail (policy) |

---

## 📦 Standard output shape (recommended)

Temporal validation SHOULD emit a small, stable artifact suitable for rollups:

- per-run: `metrics.temporal.json` (or embedded in run metrics)
- release: `drift.temporal.delta.json` (optional; aggregated)

Example (truncated):

~~~json
{
  "algorithm_id": "kfm:rs:validate:temporal:integrity:v1",
  "run_id": "urn:kfm:run:<...>",
  "dataset_id": "urn:kfm:dataset:<...>",
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
      "datetime_missing_count": 0,
      "datetime_unparseable_count": 0,
      "start_end_invalid_count": 0,
      "duplicate_timestamp_count": 0,
      "non_monotonic_count": 0,
      "cadence_expected": "daily",
      "cadence_mismatch_count": 0,
      "coverage_expected_steps": 0,
      "coverage_present_steps": 0,
      "coverage_pct": 1.0,
      "gap_count": 0,
      "max_gap_steps": 0,
      "max_gap_duration_s": 0,
      "freshness_lag_s_p95": null
    },
    "thresholds": {
      "datetime_missing_count_max": 0,
      "datetime_unparseable_count_max": 0,
      "start_end_invalid_count_max": 0,
      "coverage_pct_min": 0.98,
      "max_gap_steps_max": 1,
      "freshness_lag_s_p95_max": null
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

- keep temporal reporting aggregated and safe
- avoid enumerating “missing timestamps” lists in public artifacts unless policy allows (use references instead)

---

## 🗺️ High-level temporal validation flow

~~~mermaid
flowchart TD
  A["Enumerate Items (deterministic ordering)"] --> B["Extract effective_datetime_utc (policy precedence)"]
  B --> C["Check presence + parseability + timezone rules"]
  B --> D["Check interval integrity (start/end, duration)"]
  B --> E["Compute cadence deltas + jitter"]
  B --> F["Compute completeness (expected vs present steps)"]
  B --> G["Compute freshness lag (ops-facing)"]
  C --> H["Evaluate thresholds (policy)"]
  D --> H
  E --> H
  F --> H
  G --> H
  H --> I["Emit small metrics artifact + refs to STAC/DCAT/PROV"]
~~~

---

## 🛡️ FAIR+CARE and sovereignty posture

Temporal metrics are generally low-risk, but reporting can become sensitive when:

- tied to restricted collections or culturally sensitive datasets,
- combined with small AOIs or “where/when” patterns.

Rules:

- in repo-facing outputs, keep spatial scope generalized (`kansas`, region, or coarse H3)
- do not include identifiers that reveal restricted collection membership unless governance allows
- if policy requires redaction:
  - set `care_gate_status = redact|deny`
  - emit only aggregated metrics and reason codes
  - require steward review for deeper diagnosis through governed channels

---

## 🔗 Report integration

Temporal validation feeds:

- per-run bundles: `docs/analyses/remote-sensing/validation/reports/per-run/`
- daily rollups: `docs/analyses/remote-sensing/validation/reports/daily/`
- release rollups: `docs/analyses/remote-sensing/validation/reports/releases/`

Temporal validation is also a natural input to:

- operations freshness dashboards,
- SLO alerting (freshness and cadence breaches),
- release SemVer justification (planned cadence changes should be documented).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed temporal validation algorithms reference; defined timestamp integrity, cadence/coverage/freshness metrics, determinism rules, normalized reason codes, and governance-safe output shape. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Temporal-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Algorithms](../README.md) ·
[🧾 Reports](../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

