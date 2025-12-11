---
title: "🤖 Kansas Frontier Matrix — AI Explainability & Bias Audit Workflow (`ai-explainability.yml`)"
path: "docs/workflows/ai-explainability.yml.md"

version: "v11.2.6"
last_updated: "2025-12-10"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & AI Governance WG"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "releases/v11.2.6/signature.sig"
attestation_ref: "releases/v11.2.6/slsa-attestation.json"
sbom_ref: "releases/v11.2.6/sbom.spdx.json"
manifest_ref: "releases/v11.2.6/manifest.zip"
telemetry_ref: "releases/v11.2.6/ai-explainability-telemetry.json"
telemetry_schema: "schemas/telemetry/ai-explainability-workflow-v11.2.6.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "ci-cd-workflows"
  applies_to:
    - ".github/workflows/ai-explainability.yml"
    - "src/models/**"
    - "configs/models/**"
    - "tools/ai/**"
    - "mcp/experiments/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Model telemetry; low-risk when aggregated"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by AI Explainability Workflow v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/workflows/ai-explainability.yml.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:ai-explainability-yml:v11.2.6"
semantic_document_id: "kfm-workflow-ai-explainability-yml-v11.2.6"
event_source_id: "ledger:kfm:doc:workflows:ai-explainability-yml:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "3d-context-render"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"
  - "secret-scan"
  - "pii-scan"

ci_integration:
  workflow: ".github/workflows/ai-explainability.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

fencing_profile: "outer-backticks-inner-tildes-v1"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🤖 **Kansas Frontier Matrix — AI Explainability & Bias Audit Workflow (`ai-explainability.yml`)**  
`docs/workflows/ai-explainability.yml.md`

**Purpose**  
Define the **governed CI/CD workflow** that runs AI explainability, fairness, and drift audits for KFM models.  
This workflow turns every model change into a **documented, reproducible, and PROV-traceable** explainability report,  
feeding the Neo4j knowledge graph, STAC/DCAT catalogs, and FAIR+CARE governance dashboards.

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/AI-Explainability_%26_Bias_Audit-orange" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance_Aligned-gold" />
<img src="https://img.shields.io/badge/CI%2FCD-GitHub_Actions-success" />

</div>

---

## 📘 Overview

### 1. Workflow Intent

The `ai-explainability.yml` GitHub Actions workflow:

- Runs **explainability and bias audits** whenever models, training configs, or model cards change.  
- Produces **versioned, deterministic** artifacts (SHAP/feature attributions, fairness metrics, drift checks).  
- Emits **telemetry** (duration, energy, carbon, governance guardrails) into `ai-explainability-telemetry.json`.  
- Writes **lineage-ready metadata** so results can be ingested into:
  - Neo4j (`:ModelVersion`, `:ExplainabilityRun`, `:Dataset` nodes + relationships),  
  - STAC/DCAT catalogs (explainability reports as datasets/items),  
  - FAIR+CARE dashboards and Story Nodes.

This document is the **canonical plan** for that workflow under KFM‑MDP v11.2.6 and MCP‑DL v6.3.  

### 2. Triggers (Conceptual)

The workflow is expected to trigger on:

- `push` / `pull_request` touching:
  - `src/models/**`  
  - `configs/models/**`  
  - `mcp/model_cards/**`  
- `workflow_dispatch` (manual) for ad‑hoc audits/backfills.  

Exact trigger patterns live in `.github/workflows/ai-explainability.yml` and MUST stay in sync with this spec.

### 3. Responsibilities

`ai-explainability.yml` is responsible for:

- **Reproducible audits**  
  - Config‑driven (`configs/models/<model>.yaml`), with fixed seeds, logged dataset snapshots, and explicit thresholds.
- **Governed outputs**  
  - Metrics mapped into FAIR+CARE governance views and model cards.  
- **Provenance & cataloging**  
  - Every run emits PROV‑compliant lineage and DCAT/STAC metadata fragments.  
- **Sustainability**  
  - Energy and carbon metrics captured per run using `energy_schema` and `carbon_schema`.

---

## 🗂️ Directory Layout

~~~text
📁 .github/
└── 📁 workflows/
    📄 ai-explainability.yml                 — GitHub Actions workflow (explainability & bias audit)

📁 docs/
└── 📁 workflows/
    📄 README.md                            — CI/CD & Governance Workflows index
    📄 ai-explainability.yml.md             — ← This governed workflow specification

📁 src/
└── 📁 models/
    📁 <model_family>/                      — E.g., focus_transformer, parcel_risk
        📄 train.py                         — Training entrypoint (consumed by ai-train.yml)
        📄 explainability.py                — Shared explainability routines (SHAP, slices, etc.)

📁 configs/
└── 📁 models/
    📄 <model_name>.yaml                    — Model config (paths, seeds, explainability settings)

📁 tools/
└── 📁 ai/
    📄 run_explainability_audit.py          — CLI used by workflow
    🧾 explainability_schema.json           — Validation schema for audit outputs

📁 mcp/
└── 📁 experiments/
    📄 <timestamp>_AI-EXPL-<id>.md          — Human-readable experiment logs (linked from CI)

📁 data/
└── 📁 processed/
    📁 models/
        📁 <model_name>/
            🧾 model_metadata.json          — Model version manifest
            🧾 explainability_report.json   — Global/local attributions & slices
            🧾 fairness_metrics.json        — Group & parity metrics
            🧾 drift_report.json            — Data & prediction drift
            🧾 explainability_manifest.json — Index & provenance for this run

📁 releases/
└── 📁 v11.2.6/
    🧾 ai-explainability-telemetry.json     — Aggregated explainability workflow telemetry
    🧾 sbom.spdx.json                       — SBOM for explainability tooling
    🧾 manifest.zip                         — Release manifest (configs, versions, checksums)
~~~

---

## 🧭 Context

### 1. Relation to Other Workflows

- **Upstream**
  - `ai-train.yml` produces governed model artifacts and base metrics.  
- **Peers**
  - `faircare-validate.yml` — dataset + documentation FAIR+CARE gate.  
  - `docs-lint.yml` — structural and governance linting for Markdown.  
- **Downstream**
  - Telemetry and reports:
    - Populate Neo4j as `:ExplainabilityRun`, `:ModelVersion`, and `:Dataset` nodes/relations.  
    - Feed governance dashboards, Story Nodes, and Focus Mode.

### 2. MCP & Reproducibility

Following MCP 2.0 and KFM‑MDP v11.2.6:

- **Config‑driven**  
  - No hard‑coded thresholds; all key parameters (sample sizes, slices, guardrails) live in `configs/models/*.yaml`.  
- **Deterministic**  
  - Seeds pinned and logged; rerunning with the same config+data reproduces results within numerical tolerance.  
- **Documented**  
  - Each run logs an experiment entry in `mcp/experiments/*AI-EXPL-*.md` and can be traced via PROV/telemetry IDs.

---

## 🗺️ Diagrams

### 1. High-Level Explainability & Bias Audit Flow

~~~mermaid
flowchart LR
    A["Code / Config / Model Card Change"] --> B["ai-explainability.yml Triggered"]
    B --> C["Checkout · Setup Python · Resolve MODEL_ID"]
    C --> D["Run Explainability & Fairness Audit CLI"]
    D --> E["Validate Outputs (JSON Schema)"]
    E --> F["Upload Artifacts · Emit Telemetry"]
    F --> G["Update Graph · STAC/DCAT Catalogs"]
    G --> H["Post Status & Links to PR / Dashboards"]
~~~

### 2. Run Lifecycle Timeline

~~~mermaid
timeline
    title AI Explainability Workflow – Run Lifecycle
    section CI Events
      T0 : Trigger : Push/PR or manual dispatch
      T1 : Environment Ready : Python + deps cached
      T2 : Audit Running : Explainability + fairness + drift scripts
      T3 : Reports Validated : JSON schema checks
      T4 : Telemetry Emitted : ai-explainability-telemetry.json updated
      T5 : Governance Updated : Neo4j + catalogs patched
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Nodes

Each explainability run can become a Story Node, for example:

- `urn:kfm:story-node:ai:explainability:<model_id>:<run_id>`

Story Node content may include:

- Key influential features (global and per slice).  
- Fairness status (parity metrics, worst‑affected groups).  
- Notable drift signals and recommended follow‑up checks.  
- Links to:
  - Model card in `mcp/model_cards/`.  
  - Explainability and fairness JSON reports.  
  - Telemetry & experiment logs.

### 2. Focus Mode Behavior

When a user focuses on a model or report:

**Focus Mode MAY:**

- Summarize explainability findings and fairness status across multiple runs.  
- Visualize trends over time (e.g., drift of specific metrics).  
- Link to experiment logs, telemetry, and governance notes.

**Focus Mode MUST NOT:**

- Alter or interpolate metrics.  
- Infer governance decisions not present in recorded reports.  
- Remove or soften FAIR+CARE warnings.

---

## 🧪 Validation & CI/CD

### 1. Quality Gates

The workflow MUST fail if:

- Any explainability/fairness/drift JSON fails schema validation.  
- Fairness guardrails defined in config are violated (e.g., parity gap beyond thresholds) with no explicit override.  
- Drift detection scripts fail or indicate unacceptable drift as per config rules.  
- Telemetry emission or provenance export fails.

### 2. Conceptual Workflow YAML

~~~yaml
name: "AI Explainability & Bias Audit (Governed)"

on:
  push:
    paths:
      - "src/models/**"
      - "configs/models/**"
      - "mcp/model_cards/**"
  pull_request:
    paths:
      - "src/models/**"
      - "configs/models/**"
      - "mcp/model_cards/**"
  workflow_dispatch:
    inputs:
      model_id:
        description: "Model identifier (e.g. ks_property_tax_v3)"
        required: true
        type: string

permissions:
  contents: read
  id-token: write

concurrency:
  group: ai-explainability-${{ github.ref }}-${{ inputs.model_id || 'auto' }}
  cancel-in-progress: true

jobs:
  explainability-audit:
    runs-on: ubuntu-22.04
    env:
      MODEL_ID: ${{ inputs.model_id }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Cache deps
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-explain-${{ hashFiles('requirements*.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-explain-

      - name: Install deps
        run: |
          pip install -r requirements.txt -r requirements-explainability.txt

      - name: Resolve config
        id: resolve
        run: |
          python tools/ai/resolve_config.py \
            --model "${MODEL_ID}" \
            --out ".github/workflows/.resolved_ai_explainability.json"

      - name: Run explainability & fairness audit
        run: |
          python tools/ai/run_explainability_audit.py \
            --config "$(jq -r '.config_path' .github/workflows/.resolved_ai_explainability.json)" \
            --run-id  "${{ github.run_id }}-${MODEL_ID}"

      - name: Validate outputs (JSON Schema)
        run: |
          python tools/ai/validate_explainability_outputs.py \
            --schema tools/ai/explainability_schema.json \
            --model "${MODEL_ID}"

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: ai-explainability-${{ env.MODEL_ID }}-${{ github.run_id }}
          path: |
            data/processed/models/${{ env.MODEL_ID }}/explainability_report.json
            data/processed/models/${{ env.MODEL_ID }}/fairness_metrics.json
            data/processed/models/${{ env.MODEL_ID }}/drift_report.json
            data/processed/models/${{ env.MODEL_ID }}/explainability_manifest.json

      - name: Emit telemetry
        run: |
          python tools/ai/emit_explainability_telemetry.py \
            --model "${MODEL_ID}" \
            --manifest "data/processed/models/${MODEL_ID}/explainability_manifest.json" \
            --out "telemetry_ai_expl_${MODEL_ID}.json"

      - name: Merge telemetry → unified log
        run: |
          python scripts/merge_telemetry.py \
            --in  "telemetry_ai_expl_${MODEL_ID}.json" \
            --dest "releases/v11.2.6/ai-explainability-telemetry.json"
~~~

---

## 📦 Data & Metadata

### 1. Core Output Files (per MODEL_ID + RUN_ID)

Under `data/processed/models/<model_name>/`:

- `explainability_report.json`  
  - Global feature importance, local explanations, slice analyses.  
- `fairness_metrics.json`  
  - Per‑group metrics and parity metrics, with pass/fail flags.  
- `drift_report.json`  
  - Data and prediction drift against a reference baseline.  
- `explainability_manifest.json`  
  - Index + provenance:
    - `model_id`, `model_version`, `dataset_id`, `dataset_version`  
    - `run_id`, timestamps, seeds, git commit  
    - Paths/URIs to other outputs  
    - DCAT/PROV‑friendly summary fields.

### 2. JSON Schema Expectations

`tools/ai/explainability_schema.json` SHOULD validate:

- Required top‑level keys:

  - `run_id`, `model_id`, `dataset_id`  
  - `metrics.fairness`, `metrics.performance`, `metrics.drift`  
  - `explanations.global`, `explanations.local`

- Value ranges and shapes:
  - Scores in `[0, 1]` where applicable.  
  - Arrays of consistent length for slices and groups.  
  - Required provenance fields (`git_commit`, `config_path`, `seeds`) present and non‑empty.

### 3. Telemetry Records

Each run contributes a record to `releases/v11.2.6/ai-explainability-telemetry.json`, e.g.:

~~~json
{
  "workflow": "ai-explainability",
  "run_id": "ai-expl_2025-12-10T18-22-00Z_model-ks-property-tax_v3",
  "model_id": "ks-property-tax_v3",
  "workflow_duration_sec": 420,
  "faircare_score": 0.96,
  "guardrails_passed": true,
  "energy_wh": 7.4,
  "carbon_gco2e": 0.0041,
  "timestamp": "2025-12-10T18:22:15Z"
}
~~~

Schema details are governed by `telemetry_schema`.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. PROV‑O

Treat each explainability run as a PROV Activity:

- **Entities**
  - `ex:ModelVersion_{id}` (`prov:Entity`)  
  - `ex:DatasetVersion_{id}` (`prov:Entity`)  
  - `ex:ExplainabilityReport_{run_id}` (`prov:Entity`)
- **Activity**
  - `ex:ExplainabilityRun_{run_id}` (`prov:Activity`)
- **Agents**
  - `ex:KFM_CI_Bot` (`prov:SoftwareAgent`)  
  - `ex:ModelOwnerTeam` (`prov:Organization`)

Key relations:

- `ex:ExplainabilityRun_{run_id} prov:used ex:ModelVersion_{id}`  
- `ex:ExplainabilityRun_{run_id} prov:used ex:DatasetVersion_{id}`  
- `ex:ExplainabilityReport_{run_id} prov:wasGeneratedBy ex:ExplainabilityRun_{run_id}`  
- `ex:ExplainabilityReport_{run_id} prov:wasAttributedTo ex:ModelOwnerTeam`

### 2. DCAT

Model explainability outputs can be modeled as DCAT datasets:

- `dcat:Dataset`
  - `dct:title`: "Explainability & Bias Audit for ${MODEL_ID} (${RUN_ID})"  
  - `dct:description`: human‑readable summary of the audit.  
  - `dct:identifier`: `${MODEL_ID}-${RUN_ID}`.  
  - `dct:issued`: audit completion time.  
- `dcat:Distribution`
  - JSON artifacts (`explainability_report.json`, `fairness_metrics.json`, `drift_report.json`)  
  - Media type `application/json` and checksums for integrity.

### 3. STAC

For geo‑aware models:

- Use a `kfm-ai-explainability` STAC Collection.  
- Per‑run STAC Item:

  - `id`: `${MODEL_ID}-${RUN_ID}`  
  - `properties.datetime`: run completion time.  
  - `assets`:
    - `explainability-report` → `explainability_report.json`  
    - `fairness-metrics` → `fairness_metrics.json`  
    - `drift-report` → `drift_report.json`  

`geometry` / `bbox` MAY reflect the model’s spatial AOI (e.g., Kansas extent) or be `null` for non‑spatial models.

---

## 🧱 Architecture

### 1. Module Boundaries

- **Workflow orchestration**  
  - `.github/workflows/ai-explainability.yml`
- **Audit logic**  
  - `tools/ai/run_explainability_audit.py` (config‑driven CLI)  
  - `src/models/**/explainability.py` (model‑specific logic)  
- **Schemas & configs**  
  - `tools/ai/explainability_schema.json`  
  - `configs/models/*.yaml`
- **Outputs & telemetry**  
  - `data/processed/models/<model>/` for JSON results  
  - `releases/v11.2.6/ai-explainability-telemetry.json` for telemetry aggregation

### 2. Determinism & Config

- Seeds for all randomness (NumPy, PyTorch, etc.) pulled from config and logged.  
- Guardrail thresholds (fairness, drift, coverage) defined in config and referenced in reports.  
- No hidden parameters; any change to behavior must be visible in git via config or code change.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR

| Aspect      | Implementation                                                                 |
|-------------|-------------------------------------------------------------------------------|
| Findable    | Stable IDs (`MODEL_ID`, `RUN_ID`), predictable paths, catalog registration   |
| Accessible  | Governed artifacts exposed via CI and storage with documented policies       |
| Interoperable | JSON Schema + DCAT + STAC + PROV mappings                                 |
| Reusable    | CC‑BY licensing, explicit provenance, versioned configs and metrics           |

### 2. CARE

- **Collective Benefit**  
  - Bias & fairness telemetry supports community accountability for deployed models.  
- **Authority to Control**  
  - Sensitive attributes, groups, and reporting rules come from governance configs and FAIR+CARE policy.  
- **Responsibility**  
  - Workflow fails on guardrail breaches, forcing remediation or explicit override.  
- **Ethics**  
  - Explainability artifacts must support human review; no opaque “trust me” metrics.

### 3. Governance Hooks

- For high‑risk model families, `ai-explainability.yml` is a **required PR check**.  
- Telemetry can be cross‑referenced with `faircare-validate.yml` and `ai-train.yml` to build an end‑to‑end governance picture.  
- Quarterly reviews (per front‑matter `review_cycle`) update:
  - Metric definitions,  
  - Thresholds,  
  - Drift strategies,  
  - Explainability coverage requirements.

---

## 🕰️ Version History

| Version    | Date       | Summary                                                                                                      |
|-----------:|------------|--------------------------------------------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-10 | Updated to align with KFM‑MDP v11.2.6 (outer‑backticks/inner‑tildes fencing, emoji directory layout, telemetry v11.2.6 paths, secret/PII test profiles, and strengthened provenance fields). |
| v11.2.4   | 2025-12-06 | Initial governed specification of `ai-explainability.yml`; aligned with KFM‑MDP v11.2.4 and CI/CD + provenance standards. |

---

<div align="center">

🤖 **Kansas Frontier Matrix — AI Explainability & Bias Audit Workflow (`ai-explainability.yml`)**  
Deterministic Audits · FAIR+CARE Governance · Explainable Intelligence for Kansas Frontier Matrix  

[⬅ Back to Workflows Index](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
