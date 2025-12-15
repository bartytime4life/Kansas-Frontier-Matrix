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

# 🌡️ **KFM — AI Drift Monitoring**
`tools/ai/drift/README.md`

**Purpose**  
Define the **drift monitoring subsystem** used by KFM AI governance:  
how drift is detected, scored, thresholded, and escalated—so models remain reliable as data and conditions change over time.

</div>

---

## 📘 Overview

### What drift monitoring is (in KFM terms)

In KFM, **drift monitoring** is the governed process of detecting when:

- **input data distributions** change (data drift),
- **model outputs** change (prediction drift),
- or **model performance** degrades (concept drift),

in ways that may invalidate a model’s previous certification status.

KFM treats drift as a first-class governance signal: drift does not automatically mean “bad model,” but it **does** mean “conditions changed,” and the system must respond in a traceable, policy-safe way.

### Why drift matters for a Kansas-scale system

KFM integrates multi-domain data with strong temporal components:

- climate and hydrology cycles,
- land cover and vegetation shifts,
- remote sensing sensor changes,
- archival/document ingestion changes,
- UI-driven behavior changes (query patterns and retrieval distributions).

These changes can silently cause model behavior to shift. Drift monitoring ensures KFM remains:

- **reliable** (avoid stale or misleading outputs),
- **auditable** (drift evidence stored in governed artifacts),
- **safe** (fail-closed for missing policy metadata, no sensitive leaks),
- **reproducible** (config-driven thresholds and versioned baselines).

### Drift types (normative definitions)

- **Data drift**: distributional change in model inputs (features, covariates, embeddings).
- **Prediction drift**: change in distribution of model outputs (scores, classes, ranks, text-length proxies).
- **Concept drift**: change in the relationship between inputs and targets (performance changes), often detected via evaluation sets.

### Core invariants (normative)

1. Drift monitoring MUST be **config-driven** (thresholds and actions are not hard-coded).
2. Drift reports MUST be **safe** (no secrets, no PII, no protected-site coordinates).
3. Drift monitoring MUST be **version-aware**:
   - model identity (ID + version/hash),
   - dataset identity (ID + version),
   - baseline selection identity (training distribution or last certified release).
4. Drift must **fail closed** when governance metadata is missing or ambiguous.

---

## 🗂️ Directory Layout

This directory sits under `tools/ai/`:

~~~text
📁 tools/
└── 🧠 ai/
    ├── 🌡️ drift_monitor.py              # Runner (often lives at tools/ai root)
    ├── 📁 configs/                      # Threshold profiles (see tools/ai/configs/README.md)
    └── 📁 drift/
        └── 📄 README.md                 # This file
~~~

Canonical (intended) drift subsystem layout:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 drift/
        ├── 📄 README.md                            # This file
        │
        ├── 📁 detectors/                           # Drift detector implementations (pluggable)
        │   ├── 🧾 psi.json                          # PSI-based detector config (optional)
        │   ├── 🧾 ks.json                           # KS-test detector config (optional)
        │   └── 🧾 js_divergence.json                # JS/KL divergence detector config (optional)
        │
        ├── 📁 metrics/                             # Metric calculators (numeric/categorical/embeddings)
        ├── 📁 windows/                             # Windowing logic (time slices, releases, cohorts)
        ├── 📁 baselines/                           # Baseline selection helpers (training, last release)
        ├── 📁 reporters/                           # Report builders and schema validators
        └── 📁 docs/                                # Optional drift notes (publishable and policy-safe)
~~~

Directory rules (normative):

- Implementations MAY be organized differently, but the **interfaces must remain stable**:
  - detectors compute metrics,
  - windows define comparisons,
  - reporters produce schema-valid drift reports,
  - baselines are explicit and versioned.
- Do not store run payloads here. Store drift run artifacts under:
  - `mcp/experiments/<run-id>/...` (preferred),
  - or `mcp/runs/<run-id>/...` if the project uses that structure.

---

## 🧭 Context

### Where drift monitoring runs

Drift monitoring is invoked from:

- CI workflows (validation gates),
- scheduled/continuous pipelines (batch drift checks),
- release packaging (release-to-release drift comparisons),
- operator audits (manual checks during review).

The drift subsystem is designed to work offline and deterministically—no hidden network requirements.

### Baseline selection (normative)

Every drift comparison MUST specify a baseline, chosen from one of:

- **training baseline**: distribution from the training/evaluation dataset version used to certify the model,
- **release baseline**: distribution captured at a certified release packet (e.g., last known “good”),
- **rolling baseline**: a stable trailing window (only allowed for monitoring; not recommended for certification decisions).

The baseline must be recorded in the drift report with:

- baseline type,
- dataset ID/version and slice definition,
- baseline artifact reference (where stored),
- baseline checksum/hash when available.

### Windowing strategies

Common window types:

- **Trailing windows**: last 7d / 30d / 90d relative to “now” for operational monitoring.
- **Fixed intervals**: specific date ranges (e.g., seasonal comparisons).
- **Release-to-release**: compare distributions between certified releases (recommended for governance).

Window definitions must be explicit and recorded.

---

## 🗺️ Diagrams

### Drift monitoring decision flow

~~~mermaid
flowchart TD
  A["Select model + dataset slice<br/>(ID + version)"] --> B["Select baseline<br/>(training | last release | explicit window)"]
  B --> C["Compute drift metrics<br/>(per feature/output)"]
  C --> D["Aggregate drift score<br/>(config-driven)"]
  D --> E["Compare to thresholds<br/>(PASS/WARN/FAIL)"]
  E -->|PASS| F["Record report + telemetry<br/>(no action)"]
  E -->|WARN| G["Escalate / monitor<br/>(review or increased cadence)"]
  E -->|FAIL| H["Block certification or quarantine<br/>(recalibrate/retrain/retire)"]
  F --> I["Bind to provenance + registry"]
  G --> I
  H --> I
~~~

Accessibility note: flow from selection → metrics → thresholds → actions → provenance binding.

---

## 🧠 Story Node & Focus Mode Integration

### Why drift monitoring applies to narrative systems

Focus Mode and Story Node generation can drift due to:

- retrieval distribution changes (what content is retrieved),
- embedding space drift (updated corpora or tokenization),
- model updates (weights/config),
- data updates (new documents, new records, changed catalog entries).

When narrative systems drift, the risk is:

- inconsistent narratives for similar targets,
- degraded factual grounding or citations,
- unintended topic skew.

### Recommended “drift-aware behavior” for Focus Mode

If drift status is:

- **PASS**: proceed normally.
- **WARN**: proceed with caution; attach a governance note internally and increase monitoring.
- **FAIL**: fail closed for production narrative generation OR degrade to retrieval-only behavior, depending on governance policy for the domain.

Drift gating decisions must be recorded as part of the run artifacts and (when applicable) referenced in the model registry.

---

## 🧪 Validation & CI/CD

### Determinism rules (normative)

Drift tooling MUST:

- accept thresholds and windowing via config files (see `tools/ai/configs/`)
- record the config path and config hash in outputs
- pin random seeds if sampling is used
- emit stable JSON artifacts that can be revalidated

### Minimal run outputs (contract)

Each drift run SHOULD produce:

- `report.json` (machine-readable drift report)
- `telemetry.json` (energy/carbon + runtime + summary drift score)
- optional `summary.md` (human-readable; policy-safe; never required for CI)

### Fail-closed conditions (normative)

A drift run MUST return FAIL if:

- model identity is missing or ambiguous,
- dataset identity/version is missing,
- baseline is not specified or not reproducible,
- thresholds are missing or invalid,
- report schema validation fails.

### Suggested checks wired into CI

- JSON schema validation for `report.json`
- config schema validation
- “no secrets / no PII” scanning on outputs intended for repo storage
- deterministic output shape checks (stable keys)

---

## 📦 Data & Metadata

### Drift report structure (recommended)

A drift report is a governed artifact with at least:

- `run_id`
- `status` (`PASS` | `WARN` | `FAIL`)
- model identity:
  - `model_id`, `model_version` (or `model_hash`)
- dataset identity:
  - `dataset_id`, `dataset_version` (or STAC/DCAT refs)
- baseline identity:
  - type, slice definition, reference, checksum
- window identity:
  - slice definition
- metrics:
  - per-feature metrics
  - aggregate drift score
- actions:
  - recommended or enforced actions

Example (illustrative):

~~~json
{
  "run_id": "2025-12-15_focus_drift",
  "status": "WARN",
  "model": {
    "model_id": "focus_mode_v3_narrative",
    "model_version": "11.2.6"
  },
  "dataset": {
    "dataset_id": "dcat:kfm:dataset:docs-corpus:v11",
    "dataset_version": "v11"
  },
  "baseline": {
    "type": "release",
    "ref": "releases/v11.2.2/focus-baseline.json",
    "sha256": "<sha256>",
    "slice": {
      "time": "2025-10-01/2025-11-01",
      "notes": "last certified baseline window"
    }
  },
  "window": {
    "time": "2025-11-15/2025-12-15",
    "notes": "monitoring window"
  },
  "metrics": {
    "aggregate_drift_score": 0.31,
    "by_feature": [
      {
        "feature": "embedding_norm",
        "metric": "psi",
        "value": 0.22,
        "threshold_warn": "<set-by-governance>",
        "threshold_fail": "<set-by-governance>"
      }
    ]
  },
  "actions": ["require_review_if_production"],
  "telemetry_ref": "mcp/experiments/2025-12-15_focus_drift/telemetry.json"
}
~~~

### Telemetry requirements

Drift runs SHOULD emit:

- `runtime_ms`
- `energy_wh`
- `carbon_gco2e`
- `drift_score` (aggregate)
- counts (features checked, features drifted, detectors used)

Telemetry must be schema-valid per `telemetry_schema`, `energy_schema`, and `carbon_schema`.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

If drift checks are performed on **spatial model outputs** (classified rasters, segmentation masks, tiles):

- drift comparisons SHOULD reference STAC Items/Collections used to source:
  - baseline outputs,
  - current outputs,
  - derived evaluation products.

STAC links should be stored as references (IDs/paths), not embedded payloads.

### DCAT

If a drift event causes a dataset to be flagged or reissued:

- DCAT-aligned dataset metadata should record:
  - the drift event reference,
  - the corrective action (retrain/recalibrate),
  - the new version.

### PROV-O

Each drift run should be representable as:

- a `prov:Activity` (drift check)
- using Entities:
  - model artifact (Entity),
  - baseline slice artifacts (Entity),
  - window slice artifacts (Entity)
- generating Entities:
  - drift report (Entity),
  - telemetry record (Entity)
- with attributed Agents (CI runner, maintainer role, governance role).

Goal: drift is not a “note”; it is a traceable lineage event.

---

## 🧱 Architecture

### Detector design (pluggable and task-aware)

Drift detectors should be selected based on feature type:

- numeric features:
  - PSI, KS-test, Wasserstein distance, distribution divergence
- categorical features:
  - chi-square-like distribution comparison, JS divergence on category frequencies
- embeddings:
  - aggregate statistics (mean/variance norms), centroid shifts, safe divergence measures on binned projections
- text outputs (generative systems):
  - length distribution drift, citation-rate drift, “evidence density” drift (safe aggregate measures)

Detectors must be safe-by-default: compute on aggregates, not raw protected content.

### Severity mapping (PASS/WARN/FAIL)

Severity must be config-driven:

- metric thresholds define WARN/FAIL,
- aggregation rules define how multiple metrics roll up,
- action policy defines what to do per status and per environment.

Recommended action policy:

- PASS: record
- WARN: record + escalate (review or increased cadence)
- FAIL: record + block promotion / quarantine dependent pipelines

### “Drift without labels”

In many production settings, labels are delayed or unavailable. KFM supports drift monitoring without labels via:

- input distribution drift,
- output distribution drift,
- proxy quality signals (policy-approved, safe aggregates).

Concept drift checks should run when evaluation labels are available.

---

## ⚖ FAIR+CARE & Governance

### Policy constraints (normative)

Drift monitoring must comply with:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

This implies:

- No protected-site coordinates in drift reports.
- No PII in drift reports.
- No secrets in drift reports.
- Drift reports must be written in a way that supports long-term auditability without exposing restricted data.

### Publication rule

Only **policy-safe** drift summaries may be published in `docs/reports/`.  
Full drift artifacts belong in `mcp/experiments/` and should be access-controlled by repo governance practices.

### Training prohibition

Drift reports are governance artifacts and MUST NOT be used as AI training data (`ai_training_allowed: false`).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created drift subsystem README: definitions, baseline/windowing rules, report/telemetry contracts, CI fail-closed rules, and provenance alignment for KFM AI governance. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🌡️ Drift Monitoring · Governed for Integrity

[⬅️ Back to AI Tools](../README.md) · [⚙️ Config Profiles](../configs/README.md) · [🛡 Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>