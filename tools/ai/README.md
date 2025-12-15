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

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.2.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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

json_schema_ref: "../../../schemas/json/tools-ai-readme-v11.json"
shape_schema_ref: "../../../schemas/shacl/tools-ai-readme-v11.shape.ttl"

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

Applies to (non-exhaustive):

- **Focus Mode** narrative generation and summarization workloads
- **Story Node** generation and enrichment workflows
- **Remote sensing** and geospatial ML (classification/segmentation)
- **Forecasting** and time-series models (climate/hydrology)
- **Entity extraction / linking** and doc-to-graph pipelines

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)]() ·
[![KFM-MDP v11.2.6](https://img.shields.io/badge/KFM--MDP-v11.2.6-purple)]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-AI%20Governed-gold)]() ·
[![AI Explainability](https://img.shields.io/badge/AI-Explainable%20%26%20Audited-blueviolet)]() ·
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

### What this directory is

`tools/ai/` contains **governance-grade utilities** that make AI/ML behavior in KFM:

- **Auditable** (bias + explainability + drift evidence)
- **Traceable** (PROV-linked run records, versioned model/dataset identities)
- **Reproducible** (deterministic configs; pinned versions; stable IDs)
- **Sustainable** (energy/carbon estimates for training/eval/audit)
- **Policy-safe** (FAIR+CARE + sovereignty constraints are enforced by design)

This README is an **architecture + registry specification** (`doc_kind: Architecture`, `immutability_status: mutable-plan`).  
It defines the **intended** tool surface and output contracts. Individual scripts/modules may evolve as the platform updates.

### What these tools govern (scope)

These tools govern **any workload** that:

- Produces a prediction, label, ranking, embedding, classification, segmentation, or generated narrative
- Influences user-visible outputs (UI layers, Story Nodes, Focus Mode views)
- Produces derived data that may become “certified” (`data/processed/`) or versioned into `releases/`

### Non-goals

`tools/ai/` is **not** the model training “home” and is **not** a production inference service.  
It is a governance and validation surface that:

- runs in CI, controlled environments, and audit pipelines
- emits structured artifacts for ledgers/telemetry/model cards
- blocks/flags non-compliant outcomes before promotion

### Core capabilities (tool categories)

1. **Explainability / evidence bundles**
   - Local and global “why” artifacts per model and per dataset slice
   - Coverage scoring (how often explanations are available and meaningful)

2. **Bias / fairness audits**
   - Subgroup metrics and intersectional checks
   - Threshold-based PASS/WARN/FAIL gating aligned to documented risk profiles

3. **Drift monitoring**
   - Feature drift, output drift, and concept drift signals
   - Action recommendations (monitor/recalibrate/retrain/retire)

4. **Sustainability telemetry**
   - Energy and carbon estimation for audit + evaluation runs
   - Reporting aligned to `energy_schema` and `carbon_schema`

5. **Governance + provenance binding**
   - Model registry management
   - Run records linked to model cards, datasets, and release packets

---

## 🗂️ Directory Layout

### Position in the repo

`tools/ai/` is one of the governed tool suites under `tools/`:

~~~text
📁 tools/
├── 🧠 ai/                                     # AI/ML evaluation, audit, governance tooling (this README lives here)
├── 🧪 ci/                                     # CI helper scripts/tools
├── ⌨️ cli/                                     # Command-line utilities (repo-level interface layer)
├── 🏛️ governance/                              # Governance automation (ledgers/compliance)
├── 📡 telemetry/                               # Telemetry aggregation and reporting
└── ✅ validation/                              # Data/metadata validators (STAC/DCAT/schema checks)
~~~

### Canonical (intended) layout inside `tools/ai/`

This is the **recommended canonical layout** for the AI governance toolchain.  
(Some subfolders may be added over time as the suite grows; keep interfaces stable and config-driven.)

~~~text
📁 tools/
└── 🧠 ai/
    ├── 📄 README.md                            # This file (architecture + tool registry)
    │
    ├── 📁 configs/                             # Threshold profiles + governance presets (YAML/JSON)
    │   ├── 🧾 fairness_thresholds.default.json  # Default fairness thresholds by task type
    │   ├── 🧾 explainability_thresholds.json    # Explainability coverage/quality thresholds
    │   └── 🧾 drift_thresholds.json             # Drift alert thresholds
    │
    ├── 📁 fairness/                            # Bias & fairness metric implementations + runners
    ├── 📁 explainability/                      # XAI runners and evidence bundle generators
    ├── 📁 drift/                               # Drift detection implementations + runners
    ├── 📁 telemetry/                           # Energy/carbon capture, aggregation, and export
    ├── 📁 provenance/                          # PROV/JSON-LD emitters and binding helpers
    ├── 📁 registry/                            # Model registry helpers + validation rules
    │
    ├── 🧾 ai_model_registry.json                # Registry of governed models (IDs, versions, refs)
    └── 🧾 metadata.json                         # Tool suite metadata + default profiles
~~~

### Directory rules (normative)

- AI governance tools SHOULD be **deterministic** and **idempotent** where possible.
- Any new scripts MUST be callable in:
  - CI environments
  - staging validation
  - offline audit environments (no hidden network requirements)
- Tool outputs MUST be:
  - structured (JSON / JSON-LD where applicable)
  - schema-valid (see `telemetry_schema`, `energy_schema`, `carbon_schema`)
  - safe (no secrets, no PII, no protected-site coordinates)

---

## 🧭 Context

### How `tools/ai/` fits the KFM pipeline

KFM’s platform flow is:

> ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes / Focus Mode

`tools/ai/` contributes to the **governance gates** in that flow by producing:

- **Audit artifacts** (fairness, explainability, drift)
- **Telemetry artifacts** (energy/carbon + run-time metrics)
- **Provenance bindings** (run → model → dataset → release packet)

### Where outputs belong

To maintain repo hygiene and reproducibility:

- **Derived datasets** (model-ready features, predictions used as data products) belong in:
  - `data/work/` (intermediate)
  - `data/processed/` (certified outputs)
- **Run logs / audit artifacts** belong in:
  - `mcp/experiments/` or `mcp/runs/` (raw run payloads)
- **Human-readable summaries** may be mirrored into:
  - `docs/reports/` (when explicitly published and scrubbed)

Do not store large run payloads in `tools/ai/` itself.

### Terminology (quick)

- **Model**: a versioned artifact (weights + code + config + dependencies) referenced by `model_id` and version/hash.
- **Dataset**: a versioned asset or collection described via STAC/DCAT identifiers.
- **Audit**: a deterministic procedure that produces PASS/WARN/FAIL plus evidence artifacts.
- **Certification**: a governance decision based on audit outputs + policy constraints.

---

## 🗺️ Diagrams

### AI governance gate (conceptual)

This diagram shows the **intended** evaluation path for AI/ML workloads before they are promoted or released.

~~~mermaid
flowchart TD
  A["AI/ML Workload<br/>(Focus Mode · Story Nodes · RS/ML · Forecasting)"] --> B["Bias/Fairness Audit<br/>(subgroup metrics + thresholds)"]
  B --> C["Explainability Audit<br/>(evidence bundle + coverage scoring)"]
  C --> D["Drift Checks<br/>(data/output/concept drift)"]
  D --> E["Sustainability Telemetry<br/>(energy_wh + carbon_gco2e)"]
  E --> F["Governance Binding<br/>(registry + provenance + ledgers)"]
  F -->|PASS| G["Eligible for certification / promotion<br/>(work → processed → release)"]
  F -->|WARN| H["Escalate / monitor<br/>(tighten thresholds or require review)"]
  F -->|FAIL| I["Block / quarantine<br/>(retrain, recalibrate, retire)"]
~~~

Accessibility note: the diagram flows from workload → audits → telemetry → governance binding → PASS/WARN/FAIL outcomes.

---

## 🧠 Story Node & Focus Mode Integration

### What “AI-governed output” means for KFM narratives

When KFM generates or enriches narratives (Story Nodes or Focus Mode outputs), the tooling must ensure:

- **Explainability is available** (why the narrative included claims, citations, or entity links)
- **Bias audits are current** for the model and task configuration
- **Drift is monitored** for the input distributions used in generation
- **Sensitive content is constrained** by sovereignty policy and FAIR+CARE guidance

### Focus Mode requirements (normative)

If a model is used for user-facing narrative generation:

- `ai_outputs_require_explainability: true` implies the model MUST have a valid explainability audit reference.
- `ai_outputs_require_bias_audit: true` implies the model MUST have a valid bias/fairness audit reference.
- Audit references MUST be version-linked (model version + dataset version + config hash).

### “Evidence bundles” (concept)

An evidence bundle is a structured artifact that explains:

- inputs used (by ID / hashed references, never raw sensitive content)
- features/signals that drove outputs
- model version + configuration
- dataset IDs and slices (e.g., region/time window)
- relevant constraints or redactions applied

Evidence bundles must be safe to store long-term and safe to publish only when policy permits.

---

## 🧪 Validation & CI/CD

### How audits are invoked

AI tools are invoked by:

- CI workflows under `.github/workflows/` (lint + governance + validations)
- pipeline runs under `src/pipelines/` (automated ETL + model workflows)
- operators via repo CLI tools (under `tools/cli/`)

Exact workflow filenames can vary by release; the contract is: **audits MUST run before promotion**.

### Determinism rules (normative)

AI governance tools MUST:

- accept all thresholds and parameters via config files (not hard-coded)
- record run parameters, tool version, and environment info
- pin seeds when randomness is unavoidable
- output stable JSON that can be revalidated

### Expected outputs per audit

Each audit SHOULD produce:

- a top-level `status`: `PASS` | `WARN` | `FAIL`
- a `run_id` that can be traced to a pipeline run or experiment
- `model_id`, `model_version` (or hash)
- `dataset_id`, `dataset_version` (or STAC/DCAT pointers)
- metric payloads + summaries
- references to stored artifacts (explainability bundles, drift charts, etc.)
- telemetry payload for energy/carbon

### Failure handling (fail-closed)

- FAIL outcomes MUST block certification and production promotion.
- WARN outcomes MUST either:
  - trigger a review workflow (human governance), or
  - be explicitly accepted with a documented rationale (where policy allows)

---

## 📦 Data & Metadata

### Model registry (`ai_model_registry.json`)

The model registry is the **authoritative listing** of governed AI/ML models.

A registry entry SHOULD include:

- `model_id` (stable ID)
- `version` (semantic version or content hash)
- `task_type` (classification / regression / segmentation / generation / retrieval)
- `inputs` and `outputs` (high-level description)
- `datasets` (STAC/DCAT identifiers for training/eval)
- `model_card_ref` (path to a model card under `mcp/model_cards/`)
- audit references:
  - `bias_audit_ref`
  - `explainability_audit_ref`
  - `drift_report_ref`
- sustainability metrics:
  - `energy_wh` and `carbon_gco2e` (when captured)
- `deployment_status`: `experimental` | `internal` | `production` | `retired`
- `care_label` and `sensitivity` flags as appropriate

Registry updates SHOULD be performed via governed tooling (CLI + validation), not ad-hoc manual edits.

### Example (illustrative) registry entry

~~~json
{
  "model_id": "focus_mode_v3_narrative",
  "version": "11.2.6",
  "task_type": "generation",
  "deployment_status": "internal",
  "datasets": [
    "dcat:kfm:dataset:docs-corpus:v11",
    "stac:kfm:collection:kansas-basemap:v11"
  ],
  "model_card_ref": "mcp/model_cards/focus_mode_v3_narrative.md",
  "bias_audit_ref": "mcp/experiments/2025-12-15_focus_bias_audit/report.json",
  "explainability_audit_ref": "mcp/experiments/2025-12-15_focus_xai_audit/evidence_bundle.json",
  "drift_report_ref": "mcp/experiments/2025-12-15_focus_drift/report.json",
  "telemetry_ref": "mcp/experiments/2025-12-15_focus_audit/telemetry.json",
  "care_label": "Public · Low-Risk",
  "sensitivity": "General"
}
~~~

### Telemetry (energy + carbon)

All AI governance runs SHOULD emit telemetry aligned to:

- `telemetry_schema`
- `energy_schema`
- `carbon_schema`

Minimum recommended fields:

- `run_id`
- `tool` (bias / xai / drift)
- `runtime_ms`
- `energy_wh`
- `carbon_gco2e`
- compact audit scores (e.g., `bias_score`, `explainability_score`, `drift_score`)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC alignment (assets and evaluation artifacts)

When AI produces **spatial assets** (e.g., segmentation masks, tiles, classified rasters):

- Outputs SHOULD be stored under `data/work/` or `data/processed/`
- Catalog them via STAC in `data/stac/`
- Keep assets discoverable by time and region

### DCAT alignment (dataset-level records)

When AI produces **dataset-level deliverables**:

- Describe the dataset with DCAT-aligned metadata (as governed by KFM docs)
- Include licensing, steward, distributions, and update cadence
- Link back to the producing pipeline and audits

### PROV alignment (lineage)

Every AI audit run SHOULD be representable as:

- a `prov:Activity` (the audit run)
- consuming `prov:Entity` inputs (model artifact, dataset slice)
- producing `prov:Entity` outputs (audit report, evidence bundle, telemetry)
- attributed to responsible agents (CI, maintainers, governance roles)

The goal: **no orphan outputs**—everything ties back to provenance.

---

## 🧱 Architecture

### Tool contracts (recommended interfaces)

To keep the suite consistent, each audit runner SHOULD support:

Inputs (required):

- `--model-id`
- `--model-version` or `--model-hash`
- `--dataset-id`
- `--dataset-version` or `--stac-item` / `--dcat-record`
- `--config` (threshold profile)
- `--run-id`
- `--out` (output directory or report file)

Outputs (required):

- `report.json` (machine-readable)
- `telemetry.json` (energy/carbon + runtime)
- optional evidence artifacts (explainability bundles, plots)

### Bias & fairness audits (design guidance)

Bias checks should support:

- subgroup metrics (by protected attribute where relevant/available)
- intersectional checks (where policy permits and data supports)
- task-appropriate metrics:
  - classification: error rates by subgroup, parity gaps, calibration deltas
  - regression: error distributions by subgroup, residual analysis
  - ranking: exposure parity and outcome parity where applicable

Bias audits MUST NOT:

- log raw sensitive inputs
- “invent” protected attributes (only audit what is explicitly defined and authorized)

### Explainability audits (design guidance)

Explainability audits should:

- generate global + local explanations appropriate to model type
- verify artifact/version consistency:
  - explanation corresponds to the exact model version
  - explanation corresponds to the exact dataset slice / time window
- compute explainability coverage and quality scores:
  - coverage: percentage of cases with valid explanations
  - quality: stability/consistency metrics (method-dependent)

### Drift monitoring (design guidance)

Drift checks should:

- compare distributions across time windows or releases
- output per-feature drift summaries and an aggregate drift score
- recommend actions and attach thresholds used

---

## ⚖ FAIR+CARE & Governance

### Policy anchors (normative)

This tool suite MUST operate under:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

Governance constraints apply even when risk is “Low”:

- Do not output protected coordinates.
- Do not output PII.
- Do not publish raw data slices into audit logs.
- Fail closed on ambiguous classification or missing policy metadata.

### AI training prohibition for governance logs

`ai_training_allowed: false` is enforced for audit artifacts.  
Audit logs and governance ledgers MUST NOT be used as training data.

### Security & privacy constraints (normative)

AI tools MUST:

- avoid printing secrets, tokens, API keys, or credentials in logs
- avoid embedding raw inputs in reports (store hashed references and IDs instead)
- keep artifacts and summaries policy-scoped:
  - internal-only artifacts remain internal
  - public summaries must be scrubbed and reviewed if needed

### Default retention guidance (override by governance)

Retention is governed and may vary by domain. Default guidance:

| Artifact type             | Default retention | Notes |
|--------------------------|------------------:|------|
| Bias reports             | 365 days          | supports re-certification and trend analysis |
| Drift logs               | 180 days          | rolling horizon for retraining decisions |
| Explainability bundles   | 365 days          | linked from model cards and narrative governance |
| Registry snapshots       | Permanent         | required for long-term audits |
| Governance ledger entries| Permanent         | append-only, traceability-critical |

If a domain is sensitive, sovereignty policy can require **longer retention**, **shorter retention**, or **restricted access**.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Aligned to KFM-MDP v11.2.6 heading + fencing conventions; clarified repo placement and output destinations (data vs runs vs docs); expanded contracts for audit inputs/outputs; strengthened provenance and telemetry guidance; refreshed governance constraints and retention guidance; updated URNs and provenance chain. |
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

[⬅️ Back to Tools Index](../README.md) · [🧱 Tools Architecture](../ARCHITECTURE.md) · [🛡 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>