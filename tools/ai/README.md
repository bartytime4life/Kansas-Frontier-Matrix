---
title: "🧠 Kansas Frontier Matrix — AI & Machine Learning Tools (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tools/ai/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_guid: "urn:kfm:doc:tools-ai-readme-v11.0.0"
doc_kind: "Architecture"
intent: "tools-ai-platform"
role: "ai-governance-registry"
category: "AI · ML · Explainability · Governance · FAIR+CARE"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/tools-ai-governance-v4.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_data_flag: false
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "tools/ai/README.md@v9.5.0"
  - "tools/ai/README.md@v9.6.0"
  - "tools/ai/README.md@v9.7.0"
  - "tools/ai/README.md@v10.0.0"
  - "tools/ai/README.md@v10.2.2"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalDuration"
  prov_o: "prov:Activity"
  geosparql: "N/A"

json_schema_ref: "../../../schemas/json/tools-ai-readme-v11.json"
shape_schema_ref: "../../../schemas/shacl/tools-ai-readme-v11.shape.ttl"

event_source_id: "ledger:tools/ai/README.md"
immutability_status: "mutable-plan"
doc_uuid: "urn:kfm:doc:tools-ai-readme-v11.0.0"
semantic_document_id: "kfm-doc-tools-ai"

ai_training_allowed: false
ai_training_guidance: "AI audit and governance logs MUST NOT be used as training data."
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: true

machine_readable: true
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
Define the **FAIR+CARE-certified AI & ML governance toolkit** for the Kansas Frontier Matrix (KFM) — covering explainability, bias detection, drift monitoring, sustainability metrics, and provenance binding for all AI/ML workloads:

- Focus Mode v3
- Story Node v3 generation
- Climate & hydrology models
- Remote-sensing models
- Time-series forecasters

All tools comply with:

- **MCP-DL v6.3** (documentation-first)
- **KFM-MDP v11.0** (markdown + metadata protocol)
- **FAIR+CARE** (ethics & sovereignty)
- **KFM-OP v11.0** (ontology alignment)
- **Diamond⁹ Ω / Crown∞Ω** reliability and governance standards

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](#)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-AI%20Governed-gold)](#)
[![AI Explainability](https://img.shields.io/badge/AI-Explainable%20%26%20Ethical-blueviolet)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📘 1. Overview

The **AI Tools Framework** under `tools/ai/` governs:

- Explainable AI (XAI) — SHAP, LIME, IG, attention maps, evidence bundles
- Fairness & bias audits — statistical parity, equalized odds, subgroup metrics
- Drift monitoring — distributional & conceptual drift for models and data
- Sustainability telemetrics — energy & carbon metrics for AI workloads
- Governance & provenance — JSON-LD exports, ledger integration, model registry

These tools are invoked by:

- CI/CD workflows (`tools/ci/*`)
- Autonomous pipelines (`src/pipelines/ai/*`)
- Governance workflows (`tools/governance/*`)
- Operators via CLI (`tools/cli/*`)

No AI pipeline can be certified for production use unless **AI Tools** audits pass and are recorded in the governance ledger.

---

## 🗂️ 2. Directory Layout (KFM-MDP v11 · Box-Safe)

~~~~text
tools/
└── ai/
    ├── README.md                 # This file
    │
    ├── focus_audit.py            # Explainability and transparency validator for Focus Mode AI
    ├── bias_check.py             # Fairness & bias analysis (classification/regression)
    ├── drift_monitor.py          # Data & concept drift detection and retrain/alert hooks
    │
    ├── ai_model_registry.json    # Active model registry: versions, hashes, datasets, licenses, CARE labels
    └── metadata.json             # JSON-LD config: audit thresholds, CARE profiles, telemetry config
~~~~

Each file must be:

- Deterministic and idempotent
- Safe to run in CI, staging, and offline audit environments
- Configurable via `metadata.json` and data contracts

---

## 🧬 3. AI Governance Workflow (v11)

~~~~mermaid
flowchart TD
    A["KFM AI/ML Models\n(Focus · ETL · Forecast · RS)"]
      --> B["bias_check.py\nBias & Fairness Validation"]
    B --> C["focus_audit.py\nExplainability (SHAP · LIME · IG)"]
    C --> D["drift_monitor.py\nData & Concept Drift Detection"]
    D --> E["Mitigation Hooks\n(retrain · reweight · thresholds)"]
    E --> F["FAIR+CARE Certification\nEthics · A11y · Sovereignty Gates"]
    F --> G["Governance & Telemetry\nJSON-LD → Ledgers · Telemetry · Model Registry"]
~~~~

---

## ⚙️ 4. Stage Responsibilities

### 4.1 Bias Detection (`bias_check.py`)

- Computes fairness metrics such as:
  - Statistical Parity Difference
  - Disparate Impact
  - Equalized Odds & Equal Opportunity
- Supports multiple group definitions and intersectional analysis
- Outputs:
  - Bias scores per model & dataset
  - Group-wise metrics
  - Threshold-based PASS/FAIL signals

### 4.2 Explainability (`focus_audit.py`)

- Generates XAI artifacts for:

  - Focus Mode v3 models
  - Remote-sensing models (e.g., U-Nets)
  - Tabular forecasters (e.g., hydrology time-series)

- Supports:

  - SHAP global & local importance
  - LIME local explanations
  - Integrated Gradients for deep networks
  - Attention maps (if applicable)

- Writes:

  - JSON evidence bundles for each model/entity pair
  - Links to AI model cards and provenance manifests

### 4.3 Drift Monitoring (`drift_monitor.py`)

- Tracks:

  - **Data drift** — PSI, KL/JS divergence, KS tests
  - **Prediction drift** — shift in output distributions over time
  - **Feature drift** — shifting patterns in core features

- Supports triggers:

  - Retrain suggestions to `src/pipelines/ai/*`
  - Threshold-based alerts to governance and reliability platforms

---

## 📦 5. AI Model Registry (`ai_model_registry.json`)

The registry is the **source of truth** for models under AI governance:

- Model ID, version, architecture, hyperparameters
- Primary datasets used (STAC/DCAT references)
- Licensing & CARE classification
- Model card references
- Latest audit hashes and timestamps
- Sustainability metrics (training energy, carbon)
- Deployment status & environment tags

Registry entries must be updated only via governed flows (CI or CLI) and may not be mutated manually.

---

## 🧾 6. Example AI Governance Record (v11)

~~~~json
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "id": "ai_tools_registry_v11.0.0",
  "models_registered": [
    "focus_mode_v3_climate_v11",
    "hydrology_lstm_v8"
  ],
  "bias_audits_completed": 36,
  "drift_events_detected": 2,
  "last_drift_event": "2025-11-18T19:12:03Z",
  "fairstatus": "certified",
  "ai_explainability_score": 0.997,
  "checksum_verified": true,
  "governance_registered": true,
  "telemetry_logged": true,
  "energy_wh": 7.4,
  "carbon_gco2e": 8.2,
  "validator": "@kfm-ai-governance",
  "created": "2025-11-24T00:00:00Z",
  "governance_ref": "docs/reports/audit/ai_src_ledger.json"
}
~~~~

---

## 🧠 7. FAIR+CARE Governance Matrix (AI Tools)

| Principle             | Implementation                                                       | Oversight          |
|-----------------------|----------------------------------------------------------------------|--------------------|
| **Findable**          | Model registry & audit logs indexed with IDs + JSON-LD contexts.    | @kfm-data          |
| **Accessible**        | MIT-licensed tools, open JSON/Markdown reports.                     | @kfm-accessibility |
| **Interoperable**     | JSON-LD, DCAT 3.0, STAC links, SPDX, PROV-O graph compatibility.    | @kfm-architecture  |
| **Reusable**          | Modular XAI components, pinned environments, reproducible configs.  | @kfm-design        |
| **Collective Benefit**| Supports transparent, sustainable, and equitable environmental AI.  | @faircare-council  |
| **Authority to Control** | Council controls certification, usage approvals, and revocations.| @kfm-governance    |
| **Responsibility**    | Owners ensure bias/drift logs & model card integrity.               | @kfm-security      |
| **Ethics**            | Sensitive use-cases flagged; story & Focus outputs constrained.     | @kfm-ethics        |

---

## 🌱 8. Sustainability & Telemetry Integration

The AI Tools must emit, per audit or run:

- `ai_energy_wh`
- `ai_carbon_gco2e`
- `ai_runtime_ms`
- `ai_bias_score`
- `ai_explainability_score`
- `ai_drift_score`
- `ai_audit_status` (PASS/FAIL/WARN)

These metrics integrate into:

- `releases/v11.0.0/focus-telemetry.json`
- `docs/reports/telemetry/ai/*.json`

Alignment to:

- **ISO 14064** (carbon accounting)
- **ISO 50001** (energy management)
- **RE100** (renewables commitments, where applicable)

---

## ⚖️ 9. Retention & Provenance Policy

| Artifact           | Retention | Notes                                  |
|--------------------|-----------|----------------------------------------|
| Bias Reports       | 365 days  | Required for re-certification          |
| Drift Logs         | 180 days  | Rolling window for retraining decisions|
| Explainability Packs | 365 days| Linked to model card & release         |
| Registry Snapshots | Permanent | Immutable for future audits            |
| Governance Records | Permanent | Append-only, never pruned              |

Cleanup is handled by CI workflows (`ai_cleanup.yml`) that:

- Rotate raw logs  
- Retain canonical evidence bundles and registry snapshots  

---

## 🧪 10. Local Dev & CI Usage

Example usage patterns:

~~~~text
# Local venv setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-tools-ai.txt

# Run bias audit locally
python tools/ai/bias_check.py \
  --config configs/ai/focus_v3_bias.yml \
  --out docs/reports/audit/focus_v3_bias_report.json

# Run explainability audit
python tools/ai/focus_audit.py \
  --model-id focus_mode_v3_climate_v11 \
  --dataset-id climate_streams_v4 \
  --out docs/reports/audit/focus_v3_explainability.json

# Run drift monitor
python tools/ai/drift_monitor.py \
  --window 90d \
  --source data/processed/hydrology/ \
  --out docs/reports/audit/hydro_drift_summary.json
~~~~

CI workflows call these via:

- `ai_governance_sync.yml`
- `ai_validation.yml`
- `ai_telemetry.yml`

---

## 🕰️ 11. Version History

| Version | Date       | Summary                                                                                     |
|--------:|------------|---------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-24 | Full KFM-MDP v11 upgrade; telemetry v4; OP v11; integrated with tools/ci and tools/governance; unbroken fences. |
| v10.2.2 | 2025-11-12 | JSON-LD exports; expanded drift metrics; energy/CO₂ logging; standardized evidence packs.   |
| v10.0.0 | 2025-11-10 | Telemetry schema v2; extended FAIR+CARE explainability fields; registry hardening.         |
| v9.7.0  | 2025-11-05 | Added sustainability telemetry + improved explainability scoring.                           |
| v9.6.0  | 2025-11-03 | Unified explainability metrics and governance sync.                                         |
| v9.5.0  | 2025-11-02 | Introduced bias detection + drift management for production models.                         |

---

<div align="center">

**Kansas Frontier Matrix — AI & ML Tools (v11)**  
*Transparent Intelligence × Ethical Automation × Provenance-Verified Models*  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Tools Index](../README.md) · [Tools Platform Architecture](../ARCHITECTURE.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>