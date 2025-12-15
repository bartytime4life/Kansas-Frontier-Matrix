---
title: "📚 Kansas Frontier Matrix — AI Model Registry"
path: "tools/ai/registry/README.md"

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

doc_uuid: "urn:kfm:doc:tools-ai-registry-readme:v11.2.6"
semantic_document_id: "kfm-doc-tools-ai-registry"
event_source_id: "ledger:tools/ai/registry/README.md"
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

json_schema_ref: "../../../schemas/json/ai-model-registry-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/ai-model-registry-v11.shape.ttl"

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
ai_training_guidance: "Model registry content and governance metadata MUST NOT be used as training data unless explicitly approved."

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual review"
sunset_policy: "Superseded upon next AI-tools platform update"

provenance_chain:
  - "tools/ai/README.md@v11.2.6"
---

<div align="center">

# 📚 **KFM — AI Model Registry**
`tools/ai/registry/README.md`

**Purpose**  
Define the **AI Model Registry subsystem** for KFM:  
how models are identified, versioned, audited, and approved for use—ensuring every deployed model is traceable, explainable, fairness-audited, drift-monitored (when applicable), and governance-compliant.

</div>

---

## 📘 Overview

### What the AI Model Registry is (normative)

The **AI Model Registry** is KFM’s authoritative record of:

- which models exist,
- what they are allowed to do,
- what data they depend on,
- what audits are current (bias / explainability / drift),
- whether they are eligible for production use,
- and how they connect to provenance, releases, and governance decisions.

In KFM, the model registry is a **governance contract**, not a convenience list.

If a model is not registered (or is registered but non-compliant), it MUST NOT be used for:

- production Focus Mode outputs,
- Story Node generation/enrichment,
- certification-impacting data products,
- release packaging.

### Where the canonical registry lives

The canonical registry file is expected at:

- `tools/ai/ai_model_registry.json`

This `tools/ai/registry/` directory provides:

- registry validation logic,
- update helpers,
- and documentation for how the registry is structured and governed.

### Core invariants (normative)

1. **Stable identity**  
   Every model MUST have a stable `model_id` and a version identifier (semantic version or content hash).

2. **Audit traceability**  
   Every model eligible for governed use MUST reference current audit artifacts:
   - fairness/bias audit (required)
   - explainability audit (required for narrative/user-facing systems)
   - drift report (required for long-running production systems; recommended otherwise)

3. **Dataset traceability**  
   Every model MUST reference dataset identities (DCAT/STAC IDs), not ad-hoc filenames.

4. **Policy labeling**  
   Every model MUST include governance labels: CARE label, sensitivity, intended use, and prohibited use where relevant.

5. **Fail closed**  
   Missing required registry fields MUST block certification and promotion flows.

---

## 🗂️ Directory Layout

### Position in the repo

~~~text
📁 tools/
└── 🧠 ai/
    ├── 🧾 ai_model_registry.json                # Canonical registry file (authoritative listing)
    └── 📁 registry/
        └── 📄 README.md                         # This file
~~~

Canonical (intended) registry subsystem layout:

~~~text
📁 tools/
└── 🧠 ai/
    └── 📁 registry/
        ├── 📄 README.md                            # This file
        │
        ├── 📁 validators/                           # Registry schema validation + invariant checks
        ├── 📁 updaters/                             # Governed update helpers (add/retire models)
        ├── 📁 id_minting/                           # Model ID minting conventions + helpers
        ├── 📁 policies/                             # Registry policy rules (what is required when)
        ├── 📁 reports/                              # Optional publishable summaries (policy-safe only)
        └── 📁 docs/                                 # Notes and examples (policy-safe)
~~~

Directory rules (normative):

- The registry file itself remains at `tools/ai/ai_model_registry.json`.
- This directory contains code/docs to keep the registry valid—**not** the registry itself.
- Do not store secrets, PII, or restricted location info in registry entries.

---

## 🧭 Context

### How the registry fits the KFM pipeline

The registry sits at the center of AI governance:

- Pipelines produce models and audit artifacts.
- Audit artifacts are stored in governed run locations (`mcp/experiments/...`).
- The registry links:
  - model identity,
  - dataset dependencies,
  - audit references,
  - telemetry summaries,
  - and deployment status.

Then CI and governance tooling uses the registry to decide:

- can the model run in production?
- can its outputs be promoted to `data/processed/`?
- can it be included in release packets?

### Registry as “policy switchboard”

The registry is the place where governance can encode and enforce:

- intended and prohibited uses,
- environment restrictions (e.g., internal-only),
- review requirements,
- sunset/retirement policies,
- special sovereignty constraints.

The registry is not meant to encode secrets; it encodes rules and references.

---

## 🗺️ Diagrams

### Registry-centered governance flow

~~~mermaid
flowchart TD
  A["Model created/updated<br/>(training or tuning)"] --> B["Audits executed<br/>(bias + explainability + drift)"]
  B --> C["Artifacts stored<br/>(mcp/experiments/<run-id>/...)"]
  C --> D["Registry update proposed<br/>(tools/ai/ai_model_registry.json)"]
  D --> E["Validation gates<br/>(schema + invariants + safety)"]
  E -->|PASS| F["Registry entry accepted<br/>(eligible status set)"]
  E -->|FAIL| G["Blocked<br/>(fix audits/metadata before use)"]
  F --> H["Production use allowed<br/>(per deployment_status + policy)"]
~~~

Accessibility note: flow from model creation → audits → artifacts → registry update → validation → use or block.

---

## 🧠 Story Node & Focus Mode Integration

### Why the registry matters for narrative systems

Focus Mode and Story Node generation must remain evidence-led and policy safe. The registry provides:

- which model(s) are allowed for narrative tasks,
- required audit freshness (bias + explainability),
- what corpora/datasets are approved for use,
- whether the system must degrade to retrieval-only when audits are stale.

### Recommended registry fields for narrative systems

For narrative-capable models, entries SHOULD include:

- `task_type: "generation"` or `task_type: "retrieval"`
- `grounding_requirements`:
  - minimum evidence density
  - citation requirements (if policy defines it)
- `redaction_requirements`:
  - masking/generalization rules
  - prohibited content flags
- `audit_freshness_policy`:
  - max age for bias audit and explainability audit
  - required drift cadence

---

## 🧪 Validation & CI/CD

### Registry validation (normative)

Registry validation MUST include:

- schema validation (JSON schema + shapes if enforced)
- required keys present and typed correctly
- uniqueness:
  - `model_id` unique
  - `version` unique within model_id (unless explicitly versioned by hash)
- reference checks:
  - audit references exist and are path-safe
  - model card references exist (when required)
- safety checks:
  - no secrets
  - no PII
  - no protected-site coordinates

### Fail-closed rules (normative)

Registry validation MUST FAIL if:

- a production-status model lacks required audits,
- a model references datasets without stable IDs/versions,
- a model is missing CARE/sensitivity labels,
- prohibited uses are required by policy but missing,
- references are invalid or unsafe.

### Recommended “audit freshness” checks

CI SHOULD enforce that for `deployment_status: production` models:

- bias audit reference exists and is within allowed age
- explainability audit reference exists and is within allowed age (for narrative models)
- drift report exists and is within allowed age (for long-running systems)

The age thresholds should be config-driven (see `tools/ai/configs/`).

---

## 📦 Data & Metadata

### Registry entry (recommended contract)

A registry entry SHOULD include the following groups:

#### Identity
- `model_id` (stable identifier)
- `version` (semantic) and/or `hash` (content hash)
- `name` (human-readable)
- `task_type` (`classification` | `regression` | `segmentation` | `generation` | `retrieval`)

#### Governance labels
- `care_label`
- `sensitivity`
- `intended_use`
- `prohibited_use` (when policy requires it)
- `risk_category` (low/medium/high)

#### Dependencies
- `datasets.train[]`, `datasets.eval[]` (DCAT/STAC IDs)
- `code_ref` (commit SHA or module path reference; no secrets)
- `config_profiles[]` (profiles used for audits)

#### Audits (required for eligibility)
- `bias_audit_ref`
- `explainability_audit_ref` (required for narrative/user-facing systems)
- `drift_report_ref` (required for long-running production systems)
- `last_audit_timestamp` (ISO)

#### Deployment
- `deployment_status` (`experimental` | `internal` | `production` | `retired`)
- `release_eligible` (bool)
- `sunset_policy` / `retirement_reason` (when applicable)

#### Artifacts
- `model_card_ref`
- `telemetry_ref` (summary telemetry)
- `provenance_bundle_ref`

### Example registry entry (illustrative)

~~~json
{
  "model_id": "focus_mode_v3_narrative",
  "version": "11.2.6",
  "name": "Focus Mode v3 Narrative Generator",
  "task_type": "generation",
  "deployment_status": "internal",
  "release_eligible": false,
  "care_label": "Public · Low-Risk",
  "sensitivity": "General",
  "risk_category": "Low",
  "intended_use": [
    "Generate evidence-led narrative summaries for KFM Focus Mode targets."
  ],
  "prohibited_use": [
    "Do not use for high-stakes decisions or for generating sensitive site locations."
  ],
  "datasets": {
    "train": ["dcat:kfm:dataset:docs-corpus:v11"],
    "eval": ["dcat:kfm:dataset:docs-corpus:v11"]
  },
  "config_profiles": [
    "fairness_thresholds.default@11.2.6",
    "explainability_thresholds.default@11.2.6",
    "drift_thresholds.default@11.2.6"
  ],
  "audits": {
    "bias_audit_ref": "mcp/experiments/2025-12-15_focus_bias_audit/report.json",
    "explainability_audit_ref": "mcp/experiments/2025-12-15_focus_xai_audit/evidence_bundle.json",
    "drift_report_ref": "mcp/experiments/2025-12-15_focus_drift/report.json",
    "last_audit_timestamp": "2025-12-15T00:00:00Z"
  },
  "artifacts": {
    "model_card_ref": "mcp/model_cards/focus_mode_v3_narrative.md",
    "telemetry_ref": "mcp/experiments/2025-12-15_focus_bias_audit/telemetry.json",
    "provenance_bundle_ref": "mcp/experiments/2025-12-15_focus_bias_audit/provenance_bundle.jsonld"
  }
}
~~~

### Storage and publication rules

- Registry file: `tools/ai/ai_model_registry.json`
- Audit artifacts: `mcp/experiments/<run-id>/...`
- Publishable summaries (optional): `tools/ai/registry/reports/` **only if policy-safe**

Do not publish row-level evaluation data.

---

## 🌐 STAC, DCAT & PROV Alignment

### DCAT references (datasets)

Registry must reference datasets using stable DCAT identifiers where possible:

- `dcat:kfm:dataset:<name>:<version>`

### STAC references (spatial assets)

For spatial model products, registry entries should reference:

- STAC Collection / Item IDs for:
  - training data assets (if spatial),
  - evaluation assets,
  - produced data products.

### PROV references (lineage)

Registry entries should reference provenance bundles that can be translated into:

- `prov:Activity` for audits and training/evaluation
- `prov:Entity` for model artifacts and audit outputs
- `prov:Agent` for CI runners and governance roles

This provides end-to-end lineage: model ↔ audits ↔ data ↔ releases.

---

## 🧱 Architecture

### ID minting (recommended convention)

Model IDs should be:

- stable
- human-readable
- lower_snake_case
- domain/task scoped

Recommended pattern:

~~~text
<system_or_domain>_<component>_<task>[_v<major>]
~~~

Examples:

- `focus_mode_v3_narrative`
- `hydrology_lstm_forecast_v8`
- `remote_sensing_landcover_segmentation_v2`

### Registry update process (governed)

A registry update should follow:

1. Generate or update model artifacts (training/tuning).
2. Run required audits and store results in `mcp/experiments/…`.
3. Propose registry changes:
   - add model entry or update audit refs
   - update deployment status if promotion is intended
4. Validate registry:
   - schema + invariants + safety checks
5. Approve through governance/PR review (as required by policy)

### Minimal “eligible for production” rule (normative)

To be eligible for `deployment_status: production`, a model MUST:

- have required audits present and current
- have stable dataset references
- have a model card reference
- have provenance bundle reference(s)
- be labeled with CARE and sensitivity
- pass registry validation gates

---

## ⚖ FAIR+CARE & Governance

### Policy constraints (normative)

Registry content must comply with:

- `governance_ref`
- `ethics_ref`
- `sovereignty_policy`

This means:

- do not embed sensitive location details
- do not embed PII
- encode restrictions as rules and labels, not as raw data
- include prohibited-use notes when relevant

### Training prohibition

Registry metadata is governance data and MUST NOT be used as training data unless explicitly approved (`ai_training_allowed: false` by default).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-15 | Created registry subsystem README: defined registry purpose, invariants, validation gates, recommended entry contract, provenance/audit linking, and governance-safe publication rules for KFM AI model registry management. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
📚 Model Registry · Governed for Integrity

[⬅️ Back to AI Tools](../README.md) · [⚙️ Config Profiles](../configs/README.md) · [🧾 Provenance](../provenance/README.md) · [🛡 Governance](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>