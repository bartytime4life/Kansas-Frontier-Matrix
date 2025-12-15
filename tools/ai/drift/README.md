---
title: "🌡️ Kansas Frontier Matrix — AI Drift Monitoring"
path: "tools/ai/drift/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-drift-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-drift"
event_source_id: "ledger:tools/ai/drift/README.md"
immutability_status: "mutable-plan"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

# Note: v11.2.6 documentation can legitimately reference the last certified release bundle.
# Update these to releases/v11.2.6/* once the v11.2.6 release packet exists.
sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"

telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

json_schema_ref: "../../../schemas/json/tools-ai-drift-report-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/tools-ai-drift-report-v11.shape.ttl"

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
ai_training_guidance: "Drift reports and governance audit artifacts MUST NOT be used as training data."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"

provenance_chain:
  - "tools/ai/README.md@v11.2.6"
---

<div align="center">

# 🌡️ **KFM — AI Drift Monitoring (v11)**
`tools/ai/drift/README.md`

**Purpose**  
Define the **drift monitoring subsystem** used by KFM AI governance:  
how drift is detected, scored, thresholded, and escalated—so models remain reliable as data and conditions change over time.

</div>

---

## 📘 Overview

### What drift monitoring means in KFM

In the Kansas Frontier Matrix, **drift monitoring** is the governed process of detecting when:

- **Input distributions** change (*data drift*),
- **Model outputs** change (*prediction drift*),
- and/or **Model performance** changes (*concept drift*),

in ways that can invalidate a model’s prior certification or its intended operational assumptions.

Drift is treated as a **first-class governance signal**:
- Drift does not automatically mean “bad model.”
- Drift means **conditions changed**, and KFM must respond in a traceable, policy-safe way.

### Why drift matters for Kansas-scale, multi-domain systems

KFM runs across domains with strong temporal variability and shifting instrumentation:

- Climate/hydrology seasonality and regime shifts
- Land cover change, phenology change, disturbance events
- Remote sensing sensor changes and processing changes
- Archival ingestion changes (OCR/NER model updates, new corpora)
- Retrieval distribution changes (search/index refreshes, embedding updates)
- UI-driven distribution changes (how users query, what gets retrieved)

Drift can be **silent** and cumulative. Monitoring catches it before it becomes:
- misleading narratives,
- unstable map layers,
- degraded retrieval quality,
- or governance risk (unsafe inference via small slices).

### Normative definitions

- **Data drift**: distributional change in model inputs (features, covariates, embeddings).
- **Prediction drift**: distributional change in model outputs (scores/classes/ranks/text proxies).
- **Concept drift**: change in the mapping from inputs → targets (often detected via labeled evaluation).

### Scope of this subsystem

This `tools/ai/drift/` subsystem defines:

1. **Windows** — how “baseline” and “current” slices are defined and made reproducible  
2. **Baselines** — how reference distributions are chosen, versioned, and stored  
3. **Detectors** — how drift statistics are computed (feature/output/embedding aware)  
4. **Metrics** — metric normalization, aggregation, and cross-feature scoring  
5. **Reporters** — schema-valid, policy-safe output artifacts and summaries  
6. **Escalation** — PASS/WARN/FAIL mapping and follow-on actions (review, retrain, retire)

### Core invariants (normative)

1. Drift monitoring MUST be **config-driven** (no hard-coded thresholds for production decisions).
2. Drift reports MUST be **policy-safe** (no secrets, no PII, no protected-site coordinates).
3. Drift monitoring MUST be **version-aware**:
   - model identity (ID + version/hash),
   - dataset identity (ID + version),
   - baseline identity (type + slice + checksum where feasible),
   - window identity (slice definition, timezone, semantics).
4. Drift monitoring MUST **fail closed** when governance metadata is missing or ambiguous.
5. Drift monitoring MUST be **deterministic** given the same inputs and pinned configs.

---

## 🗂️ Directory Layout

> The repository’s `tools/ai/` area is reserved for **AI evaluation and drift analysis tools**. This drift subtree is the governed internal structure for drift monitoring within that scope.

### Drift subsystem (canonical layout)

~~~text
📁 tools/
└── 🧠 ai/
    ├── 📄 README.md                              # AI & ML Tools index
    ├── 📁 configs/                               # Governed config profiles (thresholds, domains, environments)
    │   └── 📄 README.md                          # Config conventions + schemas + examples
    │
    └── 📁 drift/                                 # 🌡️ Drift monitoring subsystem (THIS)
        ├── 📄 README.md                          # Drift overview + contracts + integration (this file)
        │
        ├── 📁 baselines/                         # Reference distributions + capture + storage rules
        │   └── 📄 README.md
        │
        ├── 📁 detectors/                         # Detector implementations + safe defaults + capability matrix
        │   └── 📄 README.md
        │
        ├── 📁 metrics/                           # Metric definitions + aggregation + scoring conventions
        │   └── 📄 README.md
        │
        ├── 📁 reporters/                         # Report building + schema validation + rendering (JSON/MD)
        │   └── 📄 README.md
        │
        ├── 📁 windows/                           # Window definitions (time/release/count/event) + validators
        │   └── 📄 README.md
        │
        └── 📁 docs/                              # Drift docs (publishable, policy-safe)
            └── 📄 README.md
~~~

### Subsystem index (human navigation)

- **Baselines** → `./baselines/README.md`  
- **Detectors** → `./detectors/README.md`  
- **Metrics** → `./metrics/README.md`  
- **Reporters** → `./reporters/README.md`  
- **Windows** → `./windows/README.md`  
- **Docs** → `./docs/README.md`

### Directory rules (normative)

- This drift module MUST remain **co-located** under `tools/ai/drift/` (no scattered drift code across the repo).
- Drift **run artifacts** (reports/telemetry/manifests) MUST NOT be committed inside this directory by default.
  - Store run artifacts in governed run locations (e.g., MCP experiment logs) and reference them from summaries.
- Every directory shown above MUST contain a `README.md` that documents its contract.

---

## 🧭 Context

### Where drift monitoring fits in the KFM pipeline

Drift monitoring is cross-cutting:

- **Pipelines/ETL**: detect drift in incoming data streams and processed outputs  
- **Model governance**: detect drift relative to certified baselines  
- **Story/Narrative**: detect drift in retrieval and narrative-generation proxies  
- **Telemetry**: record drift events and their operational/energy impact

Drift monitoring is most effective when run at **known transition boundaries**, such as:

- dataset refresh,
- pipeline version bump,
- model version bump,
- release cut,
- or scheduled cadence (daily/weekly) for critical models.

### Baseline identity is mandatory

Every drift check MUST specify one baseline mode:

- **training baseline**: distribution captured from the training/eval dataset used for certification
- **release baseline**: distribution captured from the last certified release packet
- **explicit baseline**: distribution captured by an operator for a specific evaluation period
- **rolling baseline**: allowed for monitoring only; NOT recommended as the sole evidence for certification decisions

Baseline identity must be recorded in outputs as:
- baseline type,
- dataset ID/version,
- slice definition (window semantics),
- and a checksum/hash when feasible.

### Windowing is not optional

All drift results MUST be interpretable as:

- “baseline window vs current window”
- with explicit:
  - temporal bounds,
  - timezone,
  - inclusion semantics,
  - minimum sample rules.

Windowing lives in `tools/ai/drift/windows/`.

### Relationship to other AI governance modules

Drift is designed to be composable with:

- **Fairness** (`tools/ai/fairness/`): drift may trigger re-audit of subgroup metrics
- **Explainability** (`tools/ai/explainability/`): drift may trigger regeneration/validation of explainability bundles
- **Provenance** (`tools/ai/provenance/`): drift artifacts must bind to run lineage
- **Registry** (`tools/ai/registry/`): drift status may affect deployment status or certification labels
- **Telemetry** (`tools/ai/telemetry/`): drift runs must emit energy/carbon + drift summary metrics

---

## 🗺️ Diagrams

### Drift monitoring lifecycle (governed flow)

~~~mermaid
flowchart TD
  A["Select target<br/>model_id + version/hash"] --> B["Resolve dataset slice<br/>dataset_id + version"]
  B --> C["Resolve baseline<br/>training | release | explicit"]
  B --> D["Resolve window(s)<br/>baseline_window + current_window"]
  C --> E["Compute drift stats<br/>(detectors)"]
  D --> E
  E --> F["Normalize + aggregate<br/>(metrics)"]
  F --> G["Threshold mapping<br/>(config-driven)"]
  G -->|PASS| H["Record + continue"]
  G -->|WARN| I["Escalate + increase monitoring"]
  G -->|FAIL| J["Quarantine / block promotion<br/>recalibrate | retrain | retire"]
  H --> K["Emit report + telemetry<br/>(policy-safe)"]
  I --> K
  J --> K
  K --> L["Bind to provenance + registry<br/>(audit trail)"]
~~~

Accessibility note: the flow moves from model/dataset selection → baseline/window resolution → detector computation → aggregation → thresholding → action → reporting and provenance binding.

---

## 🧠 Story Node & Focus Mode Integration

### Why drift matters for narrative and retrieval systems

For Focus Mode and Story Node generation, drift can occur even without explicit labels:

- retrieval distribution shifts (what evidence is retrieved),
- embedding representation shifts,
- corpus refresh and OCR/NER changes,
- prompt template changes,
- model weights/config changes.

This can degrade:
- consistency across time,
- grounding density (citations/evidence),
- topic balance,
- and reliability of summaries.

### Drift-aware behavior (recommended policy pattern)

- **PASS**: normal operation
- **WARN**: allow operation, but:
  - increase monitoring cadence,
  - log governance-safe warning,
  - flag for review if in production
- **FAIL**: fail closed for certification-dependent outputs:
  - block promotion to production,
  - or degrade to retrieval-only mode if approved by governance for the domain

### Drift-to-governance escalation (normative)

If drift status is **FAIL** for a production-certified model, the system MUST:

- record a drift event with:
  - model identity,
  - dataset identity,
  - baseline identity,
  - window identity,
  - detector summary,
  - action taken,
- and route it to governance review pathways defined by `governance_ref`.

---

## 🧪 Validation & CI/CD

### Required validations (normative)

For any drift run that produces governed artifacts:

- **Schema validation**
  - drift report must validate against `json_schema_ref`
  - telemetry must validate against `telemetry_schema`, `energy_schema`, `carbon_schema`
- **Determinism check**
  - the report must include config references and config hash
  - the window spec must be explicit (not “now” without an anchor)
- **Safety scans**
  - no secrets
  - no PII
  - no protected-site coordinates
- **Fail-closed rules**
  - missing IDs/versions → FAIL
  - missing baseline identity → FAIL
  - missing threshold config → FAIL
  - insufficient sample size → mark “ineligible” and do not claim drift

### Output profiles (recommended)

- `report.json` (required; machine-readable)
- `summary.md` (optional; policy-safe; human-readable)
- `telemetry.json` (required when running in governed environments)
- `selection_manifest.json` (optional; lists item IDs/hashes, not raw sensitive payloads)

### Example artifact layout (recommended)

~~~text
📁 mcp/
└── 📁 experiments/
    └── 📁 2025-12-15__drift__focus_mode_v3__kfm-v11.2.6/
        ├── 🧾 report.json                        # Schema-valid drift report
        ├── 🧾 telemetry.json                     # Energy/carbon + runtime + drift summary
        ├── 🧾 selection_manifest.json            # IDs/hashes of selected items (no sensitive payload)
        ├── 📄 summary.md                         # Policy-safe narrative summary (optional)
        └── 📄 README.md                          # Run context: purpose, configs, provenance refs
~~~

---

## 📦 Data & Metadata

### Drift report contract (recommended structure)

At minimum, a drift report SHOULD capture:

- `run_id` (stable, timestamped)
- `status` (`PASS` | `WARN` | `FAIL` | `INELIGIBLE`)
- `model`:
  - `model_id`
  - `model_version` and/or `model_hash`
- `dataset`:
  - `dataset_id`
  - `dataset_version`
  - optional STAC/DCAT references
- `baseline`:
  - `type`
  - `ref` (path/URI)
  - `sha256` (if available)
  - `window` (slice definition)
- `window`:
  - current window spec (slice definition)
- `detectors_used`:
  - list of detector IDs/versions
- `metrics`:
  - per-feature drift stats
  - aggregate drift score
- `thresholds`:
  - config ref + hash
- `actions`:
  - none / monitor / review / recalibrate / retrain / retire
- `provenance`:
  - references to run logs, provenance entities, registry updates

Illustrative (policy-safe) skeleton:

~~~json
{
  "run_id": "2025-12-15__drift__example",
  "status": "WARN",
  "model": { "model_id": "<model-id>", "model_version": "<ver>", "model_hash": "<sha256>" },
  "dataset": { "dataset_id": "<dataset-id>", "dataset_version": "<ver>" },
  "baseline": {
    "type": "release",
    "ref": "releases/v11.2.2/<baseline-artifact>.json",
    "sha256": "<sha256>",
    "window": { "type": "anchored_time", "start": "<iso>", "end": "<iso>", "timezone": "UTC" }
  },
  "window": { "type": "rolling_time", "start": "<iso>", "end": "<iso>", "timezone": "UTC" },
  "detectors_used": ["psi_v1", "ks_v1"],
  "metrics": {
    "aggregate_drift_score": 0.31,
    "by_feature": [
      { "feature": "feature_1", "metric": "psi", "value": 0.22 }
    ]
  },
  "thresholds": { "config_ref": "tools/ai/configs/<profile>.json", "config_sha256": "<sha256>" },
  "actions": ["require_review_if_production"],
  "provenance": { "run_ref": "mcp/experiments/<run-id>/" }
}
~~~

### Telemetry contract (minimum)

Telemetry SHOULD include:

- `runtime_ms`
- `energy_wh`
- `carbon_gco2e`
- `status`
- `aggregate_drift_score`
- counts (features_checked, features_flagged, detectors_used_count)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC alignment (recommended)

For spatial model outputs (COGs, vector tiles, GeoJSON):

- Baseline and current selections SHOULD be representable as:
  - STAC Item IDs
  - plus the STAC search query snapshot (for replayability)

Avoid embedding full STAC Items inside drift reports; store IDs/refs.

### DCAT alignment (recommended)

Drift results that affect dataset releases SHOULD be linkable via DCAT as:

- a dataset quality note / governance record
- with references to:
  - dataset ID/version
  - drift report distribution (machine-readable artifact)

### PROV-O alignment (recommended)

Represent each drift run as a provenance activity:

- `prov:Activity` = “drift_check”
- `prov:used` = model entity, dataset entity, baseline entity, config entity
- `prov:generated` = drift report entity, telemetry entity
- `prov:wasAssociatedWith` = governance agents/CI runner roles

This supports auditability and replay.

---

## 🧱 Architecture

### Component responsibilities

- **Windows** (`windows/`)
  - resolves baseline/current slices deterministically
  - enforces minimum sample + safety constraints

- **Baselines** (`baselines/`)
  - defines how baseline distributions are captured and stored
  - establishes baseline provenance (training/release/explicit)

- **Detectors** (`detectors/`)
  - compute drift statistics appropriate to feature type:
    - numeric, categorical, geospatial proxies, embeddings, text proxies
  - MUST operate on aggregates when possible (policy safety)

- **Metrics** (`metrics/`)
  - normalize drift stats into comparable scores
  - aggregate feature-level drift into subsystem- and model-level scores
  - define weighting rules (config-driven)

- **Reporters** (`reporters/`)
  - produce schema-valid JSON reports
  - produce optional human summaries
  - validate outputs against schemas and safety checks

### Recommended detector categories (non-exhaustive)

- Numeric:
  - PSI, KS test, Wasserstein distance, JS/KL divergence on binned distributions
- Categorical:
  - JS divergence on category frequencies, chi-square style comparisons (as allowed by policy)
- Embeddings:
  - centroid shift norms, binned projection divergence, safe summary statistics
- Text outputs (for narrative systems):
  - length distribution drift, citation-rate drift, evidence-density proxies (aggregate-only)

### Status mapping (PASS/WARN/FAIL)

Status mapping MUST be defined in config profiles:

- thresholds per metric
- aggregation rule (max, weighted sum, quorum)
- per-environment action policy (dev/staging/prod)

Recommended semantics:

- PASS: no action
- WARN: escalate and monitor
- FAIL: block certification-dependent actions and route to governance review

---

## ⚖ FAIR+CARE & Governance

### Safety constraints (normative)

Drift reporting MUST NOT include:

- PII
- secrets
- protected-site coordinates
- raw sensitive imagery snippets
- raw text excerpts from restricted corpora

Drift reporting SHOULD prefer:

- aggregate statistics,
- coarse spatial binning (when relevant),
- suppression of small groups/subcohorts.

### Small-group suppression (normative)

Any drift output that could expose a small cohort MUST be suppressed or generalized:

- require minimum `n` for subgroup reporting
- avoid intersectional subgroup breakdowns unless governance-approved

### Governance escalation (normative)

A **FAIL** status for a production-certified model MUST trigger:

- an audit trail entry (report + telemetry + provenance link)
- a recommended corrective action:
  - recalibrate thresholds,
  - retrain,
  - retire,
  - or restrict usage scope (domain/env gating)

### Training prohibition

Drift artifacts are governance records and MUST NOT be used as training data (`ai_training_allowed: false`).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Drift subsystem architecture: canonical layout, definitions, baseline/windowing requirements, detector/metric/reporting contracts, CI validation and fail-closed rules, provenance and governance alignment. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🌡️ Drift Monitoring · Governed for Integrity · KFM v11

[⬅️ Back to AI Tools](../README.md) ·
[⚙️ Config Profiles](../configs/README.md) ·
[🪟 Drift Windows](./windows/README.md) ·
[🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
