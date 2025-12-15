---
title: "⚖️ Kansas Frontier Matrix — AI Fairness & Bias Auditing"
path: "tools/ai/fairness/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-fairness-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-fairness"
event_source_id: "ledger:tools/ai/fairness/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../schemas/json/tools-ai-fairness-report-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/tools-ai-fairness-report-v11.shape.ttl"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "United States · Kansas"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

ai_training_allowed: false
ai_training_guidance: "Fairness reports, subgroup metrics, and governance audit artifacts MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"

provenance_chain:
  - "tools/ai/README.md@v11.2.6"
---

<div align="center">

# ⚖️ **KFM — AI Fairness & Bias Auditing**
`tools/ai/fairness/README.md`

**Purpose**  
Define the **fairness and bias auditing subsystem** for KFM AI governance:  
how subgroup and intersectional bias is measured (when permitted), thresholded, reported, and escalated—without leaking sensitive data.

</div>

---

## 📘 Overview

### What fairness means in KFM (normative)

In KFM, **fairness** is a governed, context-aware, and task-specific property that answers:

- Do model errors or outcomes disproportionately affect groups, communities, or regions?
- Are there systematic disparities in performance or outputs across cohorts?
- Are those disparities acceptable under documented policy for the model’s *intended use*?

KFM does not treat fairness as a single metric. Fairness auditing in KFM is:

- **multi-metric** (classification, regression, ranking, generation require different checks),
- **policy-scoped** (only audit sensitive attributes when authorized and properly governed),
- **thresholded** (PASS/WARN/FAIL based on config profiles),
- **provenance-bound** (model+data+config identity recorded).

### What this subsystem governs

Fairness auditing applies to any AI workload that:

- influences user-facing outputs (Focus Mode, Story Nodes, UI layers),
- affects certification of data products,
- performs classification/regression/ranking with potential subgroup impacts,
- uses human-centered content or community-relevant data.

### Core invariants (normative)

1. Fairness audits MUST be **config-driven** (thresholds and required metrics are not hard-coded).
2. Fairness audits MUST be **version-aware** (model + dataset + config identity).
3. Fairness audits MUST be **safe**:
   - no PII,
   - no secrets,
   - no protected-site coordinates,
   - no raw record-level subgroup dumps.
4. Fairness audits MUST fail closed if:
   - required metadata is missing,
   - subgroup definitions are ambiguous,
   - policy constraints are not satisfied.

---

## 🗂️ Directory Layout

This directory sits under `tools/ai/`:

~~~text
📁 tools/
└── 🧠 ai/
    ├── ⚖️ bias_check.py                        # Fairness runner (often lives at tools/ai root)
    ├── 📁 configs/                              # Fairness threshold profiles (see configs README)
    └── 📁 fairness/
        └── 📄 README.md                         # This file
~~~

Canonical (intended) fairness subsystem layout:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 fairness/
        ├── 📄 README.md                            # This file
        │
        ├── 📁 metrics/                             # Metric calculators (task-aware)
        │   ├── 🧾 classification.json               # Classification metric registry (optional)
        │   ├── 🧾 regression.json                   # Regression metric registry (optional)
        │   └── 🧾 ranking.json                      # Ranking metric registry (optional)
        │
        ├── 📁 cohorting/                            # Cohort and subgroup builders (policy-aware)
        ├── 📁 validators/                           # Report validators (schema + safety + completeness)
        ├── 📁 scorers/                              # Score aggregation (bias_score, severity mapping)
        ├── 📁 redaction/                            # Safe summarization/redaction helpers
        └── 📁 docs/                                 # Optional publishable notes (policy-safe only)
~~~

Directory rules (normative):

- Do not store run payloads here. Store fairness run artifacts under:
  - `mcp/experiments/<run-id>/...` (preferred),
  - or `mcp/runs/<run-id>/...` if used.
- Do not store raw cohort membership lists or row-level subgroup tables in repo outputs.
- Prefer aggregates and safe cohort summaries.

---

## 🧭 Context

### Fairness auditing is policy-scoped

Fairness audits can only be performed with the attributes and subgroup definitions that are:

- explicitly permitted by governance policy,
- present in the dataset metadata/data contracts,
- safe to process and safe to summarize.

If protected attributes are not permitted or not available, KFM still supports:

- fairness auditing using **proxy cohorts** (e.g., region types, data quality tiers),
- drift-aware fairness monitoring (bias changes over time),
- uncertainty-aware reporting (explicitly marking gaps).

### Subgroup definition sources

Subgroup definitions should come from:

- data contracts (e.g., a contract defining allowable cohorting fields),
- DCAT/STAC metadata labels (e.g., “rural/urban”, “domain tier”, “coverage quality tier”),
- governance policy overlays.

Subgroups MUST NOT be invented by the tool.

### When intersectional analysis is allowed

Intersectional fairness checks (multiple attributes combined) are powerful but can increase privacy risk.

Intersectional analysis is allowed only when:

- policy permits it,
- sample sizes are sufficient to avoid leaking small groups,
- outputs are aggregated and redacted appropriately.

If group sizes are too small, the tool must:

- suppress the subgroup output,
- mark the suppression in the report,
- optionally recommend a different evaluation approach.

---

## 🗺️ Diagrams

### Fairness auditing decision flow

~~~mermaid
flowchart TD
  A["Select model + dataset slice<br/>(ID + version)"] --> B["Load fairness profile<br/>(configs)"]
  B --> C["Build cohorts<br/>(policy-permitted only)"]
  C --> D["Compute metrics<br/>(task-aware)"]
  D --> E["Aggregate bias score<br/>(config-driven)"]
  E --> F["Threshold decision<br/>(PASS/WARN/FAIL)"]
  F --> G["Emit report + telemetry<br/>(safe aggregates only)"]
  G --> H["Bind to registry + provenance<br/>(model card refs, run ids)"]
  F -->|WARN| I["Escalate to governance review"]
  F -->|FAIL| J["Block certification / quarantine"]
~~~

Accessibility note: flow from selection → profile → cohorts → metrics → decision → reporting → governance actions.

---

## 🧠 Story Node & Focus Mode Integration

### Why fairness auditing matters for narratives

Narrative systems can introduce fairness risk via:

- retrieval skew (some sources dominate),
- topic skew (some communities under/overrepresented),
- style and framing differences by location/time,
- disparities in evidence availability.

For narrative generation, fairness auditing should emphasize safe aggregate signals such as:

- distribution of sources by region/time
- coverage parity across dataset slices
- error/omission indicators by cohort (when measurable)

Fairness auditing for narratives must be careful:

- avoid auditing on protected personal attributes
- focus on policy-permitted cohorts (e.g., region types, dataset quality tiers)

---

## 🧪 Validation & CI/CD

### Determinism rules (normative)

Fairness tooling MUST:

- be config-driven (see `tools/ai/configs/README.md`)
- record config path + sha256
- record model + dataset IDs/versions
- pin seeds if sampling is used
- emit stable JSON outputs

### Minimal outputs (contract)

Each fairness audit SHOULD produce:

- `report.json` containing:
  - `status`: `PASS` | `WARN` | `FAIL`
  - model identity
  - dataset identity + slice definition
  - cohort definitions used (names/labels only; no row-level membership)
  - metrics (aggregated)
  - thresholds and comparisons
  - actions and notes
- `telemetry.json` containing:
  - runtime + energy/carbon + summary `bias_score`

### Fail-closed conditions (normative)

A fairness audit MUST FAIL if:

- model identity is missing/ambiguous,
- dataset identity/version is missing,
- cohort definitions are missing or not permitted,
- config profile invalid/missing,
- output violates safety checks (PII, secrets, protected-site coordinates),
- schema validation fails.

### Suggested CI checks

- config validation + schema validation (when available)
- “no secrets / no PII” scan on outputs intended for repo storage
- minimum cohort size enforcement (suppress small groups; report suppression)

---

## 📦 Data & Metadata

### Recommended fairness report structure

A fairness report should include:

- `run_id`
- `status`
- `model`: `model_id`, `model_version` (or hash)
- `dataset`: `dataset_id`, `dataset_version`, `slice`
- `cohorts`: list of cohort labels and summary sizes (with suppression rules)
- `metrics`: per-cohort metrics and disparity measures
- `bias_score`: aggregated score used for gating
- `thresholds`: warn/fail thresholds used
- `actions`: recommended/enforced actions
- `policy`: what was suppressed/redacted and why

Example (illustrative):

~~~json
{
  "run_id": "2025-12-15_focus_bias_audit",
  "status": "PASS",
  "model": {
    "model_id": "focus_mode_v3_narrative",
    "model_version": "11.2.6",
    "task_type": "generation"
  },
  "dataset": {
    "dataset_id": "dcat:kfm:dataset:docs-corpus:v11",
    "dataset_version": "v11",
    "slice": { "time": "2025-11-01/2025-12-01", "notes": "monthly audit slice" }
  },
  "cohorts": [
    { "cohort_id": "region_type:rural", "count": 1200 },
    { "cohort_id": "region_type:urban", "count": 980 }
  ],
  "metrics": {
    "coverage_parity_gap": 0.03,
    "evidence_density_gap": 0.05
  },
  "bias_score": 0.97,
  "thresholds": {
    "warn": { "coverage_parity_gap": "<set-by-governance>" },
    "fail": { "coverage_parity_gap": "<set-by-governance>" }
  },
  "actions": [],
  "policy": {
    "intersectional_analysis": false,
    "suppressed_small_groups": true
  }
}
~~~

### Telemetry requirements

Fairness audits SHOULD emit:

- `runtime_ms`
- `energy_wh`
- `carbon_gco2e`
- `bias_score`
- counts (cohorts evaluated, cohorts suppressed)

Telemetry must be schema-valid per the referenced telemetry schemas.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

If fairness checks are applied to spatial outputs (e.g., classification rasters by region):

- reference STAC Items/Collections for the evaluated assets
- summarize by region categories without exposing protected locations

### DCAT

If fairness outcomes affect dataset publishing or re-issuance:

- DCAT metadata should reference:
  - fairness audit report,
  - the applied thresholds profile,
  - corrective actions taken.

### PROV-O

A fairness audit run should be representable as:

- `prov:Activity` (audit)
- using Entities:
  - model artifact,
  - dataset slice,
  - config profile
- generating Entities:
  - report,
  - telemetry record
- attributed to Agents:
  - CI runner, maintainer role, governance board (as required)

Goal: bias audit outputs are first-class provenance events.

---

## 🧱 Architecture

### Metrics by task type (recommended)

**Classification**
- per-cohort FPR/FNR deltas
- error-rate deltas
- calibration deltas
- coverage parity (when applicable)

**Regression**
- per-cohort MAE/RMSE deltas
- residual distribution comparisons
- tail error frequency deltas

**Ranking/Retrieval**
- exposure parity (if exposure model exists)
- top-k coverage parity
- quality parity metrics

**Narrative generation (Focus Mode / Story Nodes)**
- evidence density parity (citations/refs per output length)
- coverage parity across policy-permitted cohorts
- omission/uncertainty parity proxies (safe aggregates)

### Severity mapping (PASS/WARN/FAIL)

- Thresholds MUST be set by governance profiles in `tools/ai/configs/`.
- Aggregation MUST be transparent and logged:
  - metric → cohort → disparity → score → status.

Default actions (recommended):

- PASS: record
- WARN: require review (or increase cadence)
- FAIL: block certification and quarantine dependent promotions

---

## ⚖ FAIR+CARE & Governance

### Policy constraints (normative)

Fairness auditing must comply with:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

This implies:

- no protected-site coordinates in reports
- no PII in reports
- no secrets
- no re-identification risk via small subgroup reporting

### Publication rule

Only policy-safe fairness summaries may be published in `docs/reports/`.  
Full fairness artifacts belong in `mcp/experiments/` and should follow access controls.

### Training prohibition

Fairness reports are governance artifacts and MUST NOT be used as training data (`ai_training_allowed: false`).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created fairness subsystem README: policy-scoped cohorting, task-aware metrics, thresholded PASS/WARN/FAIL behavior, safe reporting rules, and provenance/governance alignment for KFM AI fairness auditing. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
⚖️ Fairness & Bias Auditing · Governed for Integrity

[⬅️ Back to AI Tools](../README.md) · [⚙️ Config Profiles](../configs/README.md) · [🛡 Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>