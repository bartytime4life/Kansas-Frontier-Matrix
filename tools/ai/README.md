---
title: "🧠 Kansas Frontier Matrix — AI & Machine Learning Tools (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/ai/README.md"

version: "v11.2.6"
last_updated: "2025-12-15"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"

doc_uuid: "urn:kfm:doc:tools-ai-readme-v11.2.6"
doc_guid: "urn:kfm:doc:tools-ai-readme-v11.2.6"
semantic_document_id: "kfm-doc-tools-ai"
doc_kind: "Architecture"
intent: "tools-ai-platform"
role: "ai-governance-registry"
category: "AI · ML · Explainability · Governance · FAIR+CARE"
immutability_status: "mutable-plan"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "tools/ai/README.md@v11.2.2"
  - "tools/ai/README.md@v11.0.0"
  - "tools/ai/README.md@v10.2.2"
  - "tools/ai/README.md@v10.0.0"
  - "tools/ai/README.md@v9.7.0"
  - "tools/ai/README.md@v9.6.0"
  - "tools/ai/README.md@v9.5.0"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalDuration"
  prov_o: "prov:Activity"
  geosparql: "N/A"

json_schema_ref: "../../schemas/json/tools-ai-readme-v11.json"
shape_schema_ref: "../../schemas/shacl/tools-ai-readme-v11.shape.ttl"

event_source_id: "ledger:tools/ai/README.md"

ai_training_allowed: false
ai_training_guidance: "AI audit and governance logs MUST NOT be used as training data."
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: true

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
lifecycle_stage: "operational"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — AI & Machine Learning Tools (v11)**
`tools/ai/README.md`

**Purpose**  
Define the **FAIR+CARE-governed AI & ML tooling surface** for the Kansas Frontier Matrix (KFM):  
explainability, bias audits, drift monitoring, sustainability telemetry, and provenance binding for all AI/ML workloads across the platform.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)]() ·
[![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM--MDP-v11.2.6-purple)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-AI%20Governed-gold)]() ·
[![AI Explainability](https://img.shields.io/badge/AI-Explainable%20%26%20Audited-blueviolet)]() ·
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

### 1) What `tools/ai/` is

`tools/ai/` is the **governance and audit toolkit** for AI/ML across KFM.

It exists to ensure AI outputs used anywhere in the KFM pipeline are:

- **Explainable** (evidence bundles and explanation artifacts exist and are version-correct)
- **Fairness-audited** (bias checks are current and thresholded)
- **Drift-monitored** (data/output/concept drift is tracked and acted on)
- **Sustainability-aware** (energy/carbon telemetry is captured)
- **Provenance-bound** (inputs → activity → outputs traceable and release-linkable)
- **Governance-safe** (FAIR+CARE + sovereignty constraints are enforced)

### 2) What it governs (scope)

These tools govern **any workload** that:

- produces **predictions, labels, rankings, embeddings, segmentations**, or **generated narrative**;
- influences user-visible outputs (map layers, Story Nodes, Focus Mode results);
- writes derived artifacts that can be promoted to `data/processed/` or packaged into `releases/`.

Examples (non-exhaustive):

- Focus Mode summary/ranking/generation models
- Story Node generation and enrichment pipelines
- Remote sensing classification/segmentation models
- Time-series forecasting models (hydrology/climate)
- Retrieval, clustering, and embedding models used for search and discovery

### 3) Operating rule (normative)

No AI pipeline may be treated as **certifiable for production use** unless:

- required audits are executed (bias + explainability, and drift where applicable),
- audit outputs are stored in the governed run locations,
- the model registry references the current audits,
- governance policy constraints are applied (including sovereignty rules).

### 4) Repo hygiene expectation

- **Training and inference code** typically belongs in `src/` (pipelines/services) or domain-specific modules.
- **Audit tooling** belongs in `tools/ai/`.
- **Run payloads** belong in `mcp/experiments/` (or `mcp/runs/` if used).
- **Certified data products** belong in `data/processed/` and are cataloged via STAC/DCAT.
- **Published summaries** belong in `docs/reports/` only after appropriate review.

---

## 🗂️ Directory Layout

This section is deliberately presented as **one complete contiguous block**.

Notes:

- The `tools/` top-level structure is **repo-canonical** (do not split it across multiple trees).
- The `tools/ai/` subtree includes:
  - files explicitly referenced by this README (registry + metadata),
  - the commonly expected audit runners (`bias_check.py`, `focus_audit.py`, `drift_monitor.py`) from prior versions,
  - and the planned modular subdirectories used to scale the suite.

If any of these do not exist in the repository yet, treat them as **required alignment work** before next certification (create them or update this tree to match reality).

~~~text
📁 tools/
├── 🧠 ai/                                       # AI/ML evaluation + governance tooling (this suite)
│   ├── 📄 README.md                             # This file (architecture + registry specification)
│   ├── 🧾 ai_model_registry.json                # Governed model registry (IDs/versions/refs)
│   ├── 🧾 metadata.json                         # Suite metadata + default profiles + thresholds
│   │
│   ├── 🧪 focus_audit.py                        # Explainability & transparency validator (Focus Mode / Story Nodes)
│   ├── ⚖️ bias_check.py                         # Fairness & bias analysis runner (classification/regression)
│   ├── 🌡️ drift_monitor.py                      # Data/output/concept drift detection + alert hooks
│   │
│   ├── 📁 configs/                              # Threshold profiles + governance presets (JSON/YAML)
│   ├── 📁 fairness/                             # Bias & fairness metric implementations + helpers
│   ├── 📁 explainability/                       # XAI methods + evidence bundle generators
│   ├── 📁 drift/                                # Drift statistics + windowing logic
│   ├── 📁 telemetry/                            # Energy/carbon capture + exports
│   ├── 📁 provenance/                           # PROV/JSON-LD emitters + binding helpers
│   └── 📁 registry/                             # Registry validators + update helpers
│
├── 🧪 ci/                                       # CI helper scripts/tools
├── ⌨️ cli/                                       # Repo CLI utilities
├── 🏛️ governance/                                # Governance automation (ledger syncing, compliance checks)
├── 📡 telemetry/                                # Telemetry aggregation + reporting tools
├── ✅ validation/                                # Validators (STAC/DCAT/schemas, etc.)
│
├── 📄 ARCHITECTURE.md                           # Tools subsystem architecture notes
└── 📄 README.md                                 # Overview of tools/ (purpose + navigation)
~~~

Directory layout rules (normative):

- This tree MUST remain **one** contiguous `~~~text` block (no split trees).
- New `tools/*` top-level directories MUST be added here.
- New canonical `tools/ai/*` directories/files MUST be added here.
- Do not list secrets, keys, credentials, or protected-site pathing patterns.

---

## 🧭 Context

### How `tools/ai/` fits KFM’s pipeline

KFM’s platform flow is:

> ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes / Focus Mode

`tools/ai/` provides the **AI governance gate** used by:

- CI/CD workflows (lint + audit + validation)
- automated pipelines (ETL/AI orchestration)
- operator tooling (CLI-driven audits for review and certification)

### Where audit artifacts should land

This README standardizes the following destinations:

- **Audit payloads** (reports, evidence bundles, drift windows, telemetry):
  - `mcp/experiments/<run-id>/...` (preferred)
  - `mcp/runs/<run-id>/...` (if used by the project)
- **Model cards**:
  - `mcp/model_cards/<model-id>.md`
- **Published safe summaries**:
  - `docs/reports/ai/...` (only if policy allows; no PII, no secrets, no restricted locations)
- **Certified model-derived datasets** (if AI output becomes data product):
  - `data/processed/...` and indexed via `data/stac/...`

### Invocation sources

AI governance tools are typically invoked by:

- `.github/workflows/*` (CI gates)
- `src/pipelines/ai/**` (automated pipelines)
- `tools/cli/**` (operator tooling)
- `tools/governance/**` (governance automation and ledger sync)

Exact workflow filenames are repo-dependent; this README defines **contracts**, not specific workflow names.

---

## 🗺️ Diagrams

### AI governance workflow (v11 conceptual)

~~~mermaid
flowchart TD
    A["KFM AI/ML Workloads<br/>(Focus · ETL · Forecast · Remote Sensing)"]
      --> B["⚖️ bias_check<br/>Bias & Fairness Validation"]
    B --> C["🧪 focus_audit<br/>Explainability (XAI evidence bundles)"]
    C --> D["🌡️ drift_monitor<br/>Data/Output/Concept Drift Detection"]
    D --> E["Mitigation Hooks<br/>(retrain · reweight · recalibrate · thresholds)"]
    E --> F["FAIR+CARE Certification Gate<br/>(Ethics · Sovereignty · Safety)"]
    F --> G["🏛 Governance + 📡 Telemetry<br/>Registry · Ledgers · Energy/Carbon"]
~~~

Accessibility note: the diagram flows from workloads → audits → drift → mitigation → certification → governance & telemetry.

---

## 🧠 Story Node & Focus Mode Integration

### Tooling obligations for narrative systems

If a model is used in **Focus Mode** or **Story Node generation**, then:

- explainability evidence MUST be available (`ai_outputs_require_explainability: true`)
- bias/fairness audits MUST be current (`ai_outputs_require_bias_audit: true`)
- drift monitoring MUST be enabled when inputs vary over time (recommended; required for long-running production systems)

### Evidence bundle requirements (normative)

Evidence bundles MUST:

- reference inputs via **IDs and hashes**, not raw sensitive content
- include model identity (ID + version/hash)
- include dataset identity (ID + version) and slice definition (time window, region, filter)
- include method/version for explainability approach used
- include a policy summary (what redactions or constraints were applied)

### Focus Mode “fail-closed” behavior (recommended)

If a Focus Mode model lacks:

- a current bias audit, or
- a current explainability audit,

the system SHOULD either:

- block the output (strict mode), or
- degrade to retrieval-only behavior with a governance warning (constrained mode),

depending on policy for the domain.

---

## 🧪 Validation & CI/CD

### Determinism rules (normative)

AI governance tools MUST:

- be config-driven (thresholds/parameters live in `tools/ai/configs/` or referenced config paths)
- record tool version, config hash, and environment metadata
- pin seeds when randomness is unavoidable
- emit stable, schema-valid JSON

### Expected outputs per audit (minimum contract)

Each audit SHOULD produce:

- `report.json` with:
  - `status`: `PASS` | `WARN` | `FAIL`
  - `run_id`
  - `model_id`, `model_version` (or hash)
  - `dataset_id`, `dataset_version` (or STAC/DCAT pointers)
  - metrics + threshold comparisons
  - pointers to evidence artifacts
- `telemetry.json` with:
  - `runtime_ms`
  - `energy_wh`
  - `carbon_gco2e`
  - audit summary scores (`bias_score`, `explainability_score`, `drift_score`)

### Failure handling (normative)

- `FAIL` MUST block certification/promotion.
- `WARN` MUST trigger either:
  - a governance review workflow, or
  - explicit documented acceptance (only if policy allows).
- Any attempt to bypass audits is a governance violation and must be logged.

### Example CLI patterns (illustrative)

Actual filenames/flags may differ; the **interface contract** below is the recommended standard:

~~~bash
# Bias / fairness audit
python tools/ai/bias_check.py \
  --model-id focus_mode_v3_narrative \
  --model-version 11.2.6 \
  --dataset-id dcat:kfm:dataset:docs-corpus:v11 \
  --config tools/ai/configs/fairness_thresholds.default.json \
  --run-id 2025-12-15_focus_bias_audit \
  --out mcp/experiments/2025-12-15_focus_bias_audit/

# Explainability audit (evidence bundle)
python tools/ai/focus_audit.py \
  --model-id focus_mode_v3_narrative \
  --model-version 11.2.6 \
  --dataset-id dcat:kfm:dataset:docs-corpus:v11 \
  --config tools/ai/configs/explainability_thresholds.json \
  --run-id 2025-12-15_focus_xai_audit \
  --out mcp/experiments/2025-12-15_focus_xai_audit/

# Drift monitoring (windowed)
python tools/ai/drift_monitor.py \
  --model-id focus_mode_v3_narrative \
  --model-version 11.2.6 \
  --dataset-id dcat:kfm:dataset:docs-corpus:v11 \
  --window 90d \
  --config tools/ai/configs/drift_thresholds.json \
  --run-id 2025-12-15_focus_drift \
  --out mcp/experiments/2025-12-15_focus_drift/
~~~

---

## 📦 Data & Metadata

### AI Model Registry (`ai_model_registry.json`)

The model registry is the **authoritative listing** of AI/ML models governed by KFM.

A registry entry SHOULD include:

- **Identity**
  - `model_id` (stable identifier)
  - `version` (semantic version) and/or `hash` (content hash)
  - `task_type` (`classification` | `regression` | `segmentation` | `generation` | `retrieval`)
  - `owner` / steward (team or role handle; no personal emails in public docs)

- **Data dependencies**
  - `datasets.train[]` and `datasets.eval[]` with STAC/DCAT identifiers
  - dataset versions and slices (time windows, regions, filters)

- **Governance labels**
  - `care_label`
  - `sensitivity`
  - `intended_use`
  - `prohibited_use` (when necessary for domain safety)

- **Audit references (required for certification)**
  - `bias_audit_ref`
  - `explainability_audit_ref`
  - `drift_report_ref` (required for long-running systems; recommended otherwise)

- **Sustainability**
  - `energy_training_wh`, `carbon_training_gco2e` (if captured)
  - `energy_eval_wh`, `carbon_eval_gco2e` (if captured)

- **Deployment**
  - `deployment_status` (`experimental` | `internal` | `production` | `retired`)
  - `release_eligibility` flags (explicitly encoded)

### Example registry entry (illustrative)

~~~json
{
  "model_id": "focus_mode_v3_narrative",
  "version": "11.2.6",
  "task_type": "generation",
  "deployment_status": "internal",
  "care_label": "Public · Low-Risk",
  "sensitivity": "General",
  "datasets": {
    "train": ["dcat:kfm:dataset:docs-corpus:v11"],
    "eval": ["dcat:kfm:dataset:docs-corpus:v11"]
  },
  "model_card_ref": "mcp/model_cards/focus_mode_v3_narrative.md",
  "bias_audit_ref": "mcp/experiments/2025-12-15_focus_bias_audit/report.json",
  "explainability_audit_ref": "mcp/experiments/2025-12-15_focus_xai_audit/evidence_bundle.json",
  "drift_report_ref": "mcp/experiments/2025-12-15_focus_drift/report.json",
  "telemetry_ref": "mcp/experiments/2025-12-15_focus_bias_audit/telemetry.json"
}
~~~

### Example AI governance record (JSON-LD style, illustrative)

~~~json
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "id": "urn:kfm:ai:audit:2025-12-15_focus_bias_audit",
  "model_id": "focus_mode_v3_narrative",
  "model_version": "11.2.6",
  "dataset_id": "dcat:kfm:dataset:docs-corpus:v11",
  "audit_type": "bias_check",
  "status": "PASS",
  "bias_score": 0.99,
  "checksum_verified": true,
  "telemetry": {
    "energy_wh": 7.4,
    "carbon_gco2e": 8.2,
    "runtime_ms": 128400
  },
  "governance_ref": "ledger:kfm:ai:audit:2025-12-15_focus_bias_audit",
  "created": "2025-12-15T00:00:00Z"
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (asset-level)

When AI produces spatial assets that become data products:

- store outputs under `data/work/` → promote to `data/processed/` when certified
- register them as STAC assets under `data/stac/` (collections/items)
- link STAC assets back to audit artifacts (via IDs/refs, not raw embeddings or sensitive examples)

### DCAT (dataset-level)

When AI produces a dataset-like deliverable (e.g., statewide classifications, time-series products):

- publish DCAT-aligned dataset metadata
- include distributions and licensing
- include update cadence and coverage
- include governance labels and redaction rules

### PROV-O (lineage)

Each audit run SHOULD be representable as:

- `prov:Activity` (audit run)
- using `prov:Entity` inputs (model artifact, dataset slice)
- generating `prov:Entity` outputs (report, evidence bundle, telemetry)
- attributed to appropriate `prov:Agent` (CI, maintainer role, governance board)

The goal: **no orphan outputs**—audit artifacts are traceable to model + data + decision.

---

## 🧱 Architecture

### Stage responsibilities

This section restores and expands the “missing” operational detail from prior versions.

#### Bias detection (`bias_check.py`)

Responsibilities:

- Compute fairness metrics appropriate to the task type.
- Support subgroup and (where policy allows) intersectional analysis.
- Compare metrics to configured thresholds and emit PASS/WARN/FAIL.

Recommended metric families:

- **Classification**
  - subgroup error rates (FPR/FNR deltas)
  - parity gap metrics (where labels and groups are available)
  - calibration deltas (reliability by subgroup)

- **Regression**
  - residual distribution deltas by subgroup
  - MAE/RMSE deltas by subgroup
  - tail-risk checks (high-error frequency by subgroup)

- **Ranking / retrieval**
  - exposure parity (where an exposure model exists)
  - outcome parity or quality parity by subgroup

Outputs:

- `report.json` with summary + per-group breakdown
- (optional) `plots/` folder for publishable charts (ensure policy-safe)
- `telemetry.json`

Normative safety:

- do not log raw sensitive values
- store only derived statistics and hashed references to slices

#### Explainability (`focus_audit.py`)

Responsibilities:

- Generate or validate explainability artifacts appropriate to model type.
- Verify that explanations correspond to the **exact** model version and dataset slice.
- Emit an **evidence bundle** suitable for long-term governance storage.

Supported approaches (method choice depends on model type):

- tabular models: global/local feature importance, partial dependence (where appropriate)
- deep learning: integrated gradients, saliency maps, attention visualization (when meaningful)
- retrieval/embedding: nearest-neighbor evidence sets, attribution summaries, retrieval provenance

Outputs:

- `evidence_bundle.json` (or `report.json` + `evidence/` assets)
- coverage/quality metrics (`explainability_score`)
- `telemetry.json`

Normative safety:

- evidence bundles must not contain raw PII or protected-site coordinates
- prefer example IDs and hashed references

#### Drift monitoring (`drift_monitor.py`)

Responsibilities:

- Detect drift across time windows or release versions for:
  - input distributions (data drift)
  - output distributions (prediction drift)
  - performance measures (concept drift)

Common drift measures (implementation-specific):

- population stability index (PSI)
- distribution divergence metrics (KL/JS) on safe-to-log aggregates
- KS test for numeric feature shifts
- embedding drift summaries (aggregate statistics only)

Outputs:

- `report.json` with per-feature and aggregate drift scores
- recommended actions:
  - `monitor`, `recalibrate`, `retrain`, `retire`
- `telemetry.json`

Normative governance rule:

- “severe drift” must:
  - be recorded in governance ledgers,
  - trigger review or block dependent promotions (policy-dependent).

### Sustainability & telemetry integration

For each AI audit run, tools SHOULD emit:

- `energy_wh` — estimated energy for audit/eval run
- `carbon_gco2e` — estimated carbon footprint
- `runtime_ms` — runtime
- summary scores:
  - `bias_score`
  - `explainability_score`
  - `drift_score`

These artifacts are forwarded to the governed telemetry bundle and/or experiment run bundles:

~~~text
mcp/experiments/<run-id>/telemetry.json
releases/<version>/focus-telemetry.json
docs/reports/telemetry/ai/*.json  (only if explicitly published and policy-safe)
~~~

### Retention & provenance policy (default guidance)

Retention is governed and may vary by domain. Default guidance:

| Artifact type              | Default retention | Notes |
|---------------------------|------------------:|------|
| Bias reports              | 365 days          | Supports re-certification and trend analysis |
| Drift logs                | 180 days          | Rolling horizon for retraining decisions |
| Explainability bundles    | 365 days          | Linked from model cards and governance |
| Registry snapshots        | Permanent         | Required for long-term audits |
| Governance ledger entries | Permanent         | Append-only; traceability-critical |

If sovereignty policy requires stricter handling, follow `sovereignty_policy`.

### Security & privacy constraints (normative)

AI tools MUST:

- avoid logging raw input data (especially PII or sensitive imagery)
- log only:
  - derived statistics
  - IDs and hashed references
  - metadata safe for long-term storage
- fail closed when encountering:
  - missing governance metadata
  - ambiguous sensitivity labels
  - unrecognized data classification

---

## ⚖ FAIR+CARE & Governance

### Governance matrix (AI tools)

| Principle                | Implementation (tools/ai/)                                                                 | Oversight |
|-------------------------|----------------------------------------------------------------------------------------------|----------|
| **Findable**             | Stable model IDs; registry + audit artifacts referenced via persistent run IDs               | FAIR+CARE Council |
| **Accessible**           | Human-readable summaries + machine-readable JSON artifacts (policy-safe publication)        | Governance + A11y |
| **Interoperable**        | JSON/JSON-LD outputs, STAC/DCAT references, PROV-ready lineage shapes                         | Architecture Board |
| **Reusable**             | Versioned configs, deterministic runs, pinned model/dataset references                        | Maintainers |
| **Collective Benefit**   | Explicit “intended use” and “prohibited use” guidance for models where needed                | FAIR+CARE Council |
| **Authority to Control** | Sovereignty policy + governance charter constrain what is produced and what can be published | Governance |
| **Responsibility**       | PASS/WARN/FAIL artifacts link decisions to actors (CI/pipelines/roles)                        | Security + Governance |
| **Ethics**               | Bias, explainability, drift, and redaction rules block unsafe promotion                       | FAIR+CARE Council |

### AI training prohibition (normative)

Audit logs and governance outputs MUST NOT be used as training data (`ai_training_allowed: false`).  
When packaging artifacts for research, exclude governance logs unless explicitly approved.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Restored and expanded missing operational content (stage responsibilities, telemetry, retention, security constraints, examples); kept `🗂️ Directory Layout` as a single contiguous block near the top; normalized relative paths; aligned headings and fencing to KFM-MDP v11.2.6. |
| v11.2.2     | 2025-11-27 | Baseline v11.2.2 AI tools README; defined bias/explainability/drift roles; governance + telemetry anchors. |
| v11.0.0     | 2025-11-24 | Initial v11 tool suite framing; telemetry and governance integration. |
| v10.2.2     | 2025-11-12 | JSON-LD exports; extended drift metrics; energy/CO₂ logging; standardized explainability bundles. |
| v10.0.0     | 2025-11-10 | Telemetry schema v2; FAIR+CARE explainability fields; registry hardening. |
| v9.7.0      | 2025-11-05 | Added sustainability telemetry and improved explainability scoring. |
| v9.6.0      | 2025-11-03 | Unified explainability metrics and governance sync. |
| v9.5.0      | 2025-11-02 | Introduced bias detection and drift management for production models. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
🧠 AI & ML Tools v11.2.6 · FAIR+CARE Governed · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω

[⬅️ Back to Tools Index](../README.md) · [🧱 Tools Architecture](../ARCHITECTURE.md) · [🛡 Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>