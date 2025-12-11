---
title: "🧠 Kansas Frontier Matrix — AI Training Workflow (`ai-train.yml`) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/workflows/ai-train.yml.md"

version: "v11.2.6"
last_updated: "2025-12-11"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.6/signature.sig"
attestation_ref: "releases/v11.2.6/slsa-attestation.json"
sbom_ref: "releases/v11.2.6/sbom.spdx.json"
manifest_ref: "releases/v11.2.6/manifest.zip"
telemetry_ref: "releases/v11.2.6/ai-train-telemetry.json"
telemetry_schema: "schemas/telemetry/ai-train-workflow-v11.2.6.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
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
    - ".github/workflows/ai-train.yml"
    - "src/ai/**"
    - "configs/ai/**"
    - "mcp/model_cards/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Model training & telemetry; low-risk when aggregated"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by AI Training Workflow v12"

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
  - "docs/workflows/ai-train.yml.md@v10.2.4"
  - "docs/workflows/ai-train.yml.md@v10.1.0"
  - "docs/workflows/ai-train.yml.md@v9.9.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:ai-train-yml:v11.2.6"
semantic_document_id: "kfm-workflow-ai-train-yml-v11.2.6"
event_source_id: "ledger:kfm:doc:workflows:ai-train-yml:v11.2.6"
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

ci_integration:
  workflow: ".github/workflows/ai-train.yml"
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

# 🧠 **Kansas Frontier Matrix — AI Training Workflow (`ai-train.yml`)**  
`docs/workflows/ai-train.yml.md`

**Purpose**  
Define the **governed GitHub Actions workflow** that trains and evaluates KFM AI models (e.g., **Focus Transformer v2.1**), enforces **FAIR+CARE** and **MCP‑DL v6.3** governance, generates **Model Cards**, computes **bias/drift/explainability** metrics, signs artifacts (SLSA/OIDC), and exports **telemetry** & **SBOM** for Diamond⁹ Ω / Crown∞Ω certification.  
The workflow is fully aligned with **KFM‑MDP v11.2.4** and the CI/CD & Governance index at `docs/workflows/README.md`.

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/AI-Train_&_Eval-governed" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance_Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Automated-brightgreen" />

</div>

---

## 📘 Overview

### 1. Workflow Intent

The `ai-train.yml` workflow is the **governed training entrypoint** in the KFM CI/CD pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

Within this chain, `ai-train.yml`:

- Orchestrates **data → model** steps for KFM models (including Focus Transformer families).  
- Enforces **reproducibility** (locked deps, deterministic seeds, versioned configs and artifacts).  
- Runs **FAIR+CARE**, PII/sensitivity checks, and data-contract validation before training.  
- Produces **evaluation, drift, and explainability** artifacts suitable for:
  - Model cards in `mcp/model_cards/`,
  - Governance and audit dashboards,
  - Story Node and Focus Mode overlays.
- Emits **telemetry** (v3-style) covering runtime, quality, fairness, energy, and carbon.

**Hard gate (normative):**

> Training **MUST FAIL** if any input asset is:
> - Flagged with `care.tag = sensitive`, OR  
> - Quarantined under `data/work/staging/**/abandonment_candidates/`  
> and no explicit governance override is present.

### 2. Triggers & Inputs (Conceptual)

The workflow triggers on:

- `push` to:
  - `src/ai/**`
  - `data/training/**`
  - `configs/ai/**`
- `workflow_dispatch` (manual) with inputs:
  - `model_id`, `dataset_ref`, `config_path`, `epochs`, `device`
- (Optional) `schedule` for nightly health checks on selected models.

The exact trigger configuration is defined in `.github/workflows/ai-train.yml` and **must remain consistent** with this spec.

### 3. Responsibilities

`ai-train.yml` is responsible for:

- Deterministic training + evaluation of governed KFM models.  
- Enforcing gates on data contracts, FAIR+CARE, PII, and sensitivity rules.  
- Producing and verifying:
  - Metrics, drift and explainability reports.
  - Model Cards.
  - SBOM, SLSA provenance, and signatures.  
- Emitting **telemetry** and **provenance** that can be ingested into:
  - Neo4j (as `:ModelVersion`, `:TrainingRun`, `:Dataset` nodes and relationships),
  - STAC/DCAT catalogs,
  - Focus Mode Story Nodes.

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── ⚙️ .github/
│   └── 📁 workflows/
│       📄 ai-train.yml                     # GitHub Actions workflow (governed AI training)
│
├── 📚 docs/
│   └── ⚙️ workflows/
│       📄 README.md                        # CI/CD & Governance Workflows index
│       📄 ai-train.yml.md                  # ← This specification
│
├── 🧠 src/
│   └── 📁 ai/
│       📄 train.py                         # Training entrypoint (used by CI)
│       📄 eval.py                          # Evaluation & metrics
│       📄 drift_check.py                   # Drift & OOD checks
│       📁 explainability/                  # Shared explainability routines
│
├── ⚙️ configs/
│   └── 🤖 ai/
│       📄 focus_v2_1.yaml                  # Example training config for Focus Transformer v2.1
│       📄 <model_name>.yaml                # Other model configs (seeds, STAC refs, hyperparams)
│
├── 🧾 mcp/
│   └── 📁 model_cards/
│       📄 FOCUS_V2_1_MODEL_CARD.md        # Generated model card (example)
│
├── 🗂️ data/
│   └── 📁 processed/
│       📁 models/
│           📁 <model_id>/
│               📄 model_metadata.json      # Model version manifest
│               📄 model_weights.bin        # Model artifacts (or storage pointer)
│               📄 metrics.json             # Eval metrics
│               📄 drift.json               # Drift/OOD report
│               📄 explainability.json      # Explainability report
│               📄 MODEL_CARD.md            # Governed model card
│               📄 signature.sig            # Cosign signature
│               📄 certificate.pem          # Sig certificate
│
└── 📦 releases/
    └── 📁 v11.2.6/
        📄 sbom.spdx.json                   # SBOM
        📄 manifest.zip                     # Release manifest
        📄 ai-train-telemetry.json          # Aggregated training telemetry
~~~

---

## 🧭 Context

### 1. Relationship to Other Workflows

- **Upstream:**
  - ETL and cataloging pipelines produce training-ready datasets and STAC/DCAT metadata.  
- **Siblings:**
  - `faircare-validate.yml` validates FAIR+CARE and governance for datasets/docs.  
  - `ai-explainability.yml` can perform **post-training explainability audits** on model versions produced here.  
- **Downstream:**
  - Results flow into:
    - Model cards in `mcp/model_cards/`,
    - Neo4j model graph,
    - Frontend features (e.g., Focus Mode on model behavior).

### 2. MCP & Reproducibility

In line with MCP 2.0:

- All training is **config-driven**:
  - `configs/ai/<model>.yaml` defines:
    - STAC/DCAT references for data.
    - Random seeds.
    - Hyperparameters.
    - Explainability/telemetry toggles.
- Seeds and dataset versions are logged in:
  - `data/processed/models/<model>/model_metadata.json`
  - Telemetry records and experiment logs.

---

## 🗺️ Diagrams

### 1. High-Level AI Training Flow

~~~mermaid
flowchart LR
    A["Data (STAC/DCAT)"] --> B["Contract + FAIR+CARE Validation"]
    B --> C["PII / Sensitive Data Gate"]
    C --> D["Train Model (Deterministic Seeds)"]
    D --> E["Evaluate · OOD · Drift"]
    E --> F["Explainability (SHAP / LIME / IG)"]
    F --> G["Model Card · SBOM · SLSA Attest"]
    G --> H["Upload Artifacts · Emit Telemetry"]
    H --> I["Graph & Catalog Update · Governance Review"]
~~~

### 2. Training Run Timeline

~~~mermaid
timeline
    title AI Training Workflow — Run Lifecycle
    section CI Events
      T0 : Commit / Workflow Dispatch : Trigger ai-train.yml
      T1 : Environment Ready : Python + deps cached
      T2 : Validation : Contracts · FAIR+CARE · PII/sensitivity
      T3 : Training : Deterministic epochs
      T4 : Evaluation : Metrics · drift · explainability
      T5 : Packaging : Model card · SBOM · SLSA · signatures
      T6 : Telemetry : ai-train-telemetry.json updated
      T7 : Governance : Graph/catalog updated and reviewed
~~~

---

## 🧠 Story Node & Focus Mode Integration

- Each training run (for a given `model_id` + `run_id`) is a candidate **Story Node**, e.g.:

  - `urn:kfm:story-node:ai:train:<model_id>:<run_id>`

- Story Node content includes:
  - A narrative summary of:
    - Dataset(s) used and constraints,
    - Key metrics and fairness status,
    - Important drift/explainability findings.  
  - Links to:
    - The model card,
    - STAC/DCAT entries,
    - Neo4j entities (`:ModelVersion`, `:TrainingRun`).

**Focus Mode** MAY:

- Surface:
  - Training history for a model (timeline of runs).  
  - Metric trends and fairness status across versions.  
- Highlight:
  - Where data contracts or governance gates failed in previous runs.

**Focus Mode MUST NOT**:

- Rewrite numerical metrics or governance decisions.  
- Infer new policy from the presence/absence of a run — it can only surface existing content.

---

## 🧪 Validation & CI/CD

### 1. Quality Gates

The workflow MUST fail if:

- Data contract validation fails (schema, allowed values, required fields).  
- FAIR+CARE or PII/sensitivity checks fail without an approved governance override.  
- Evaluation or drift scripts do not produce valid JSON conforming to schemas.  
- Telemetry or SBOM generation fails.

Training is considered **non‑governed** and MUST NOT be used in production if the workflow fails.

### 2. Workflow YAML (Conceptual Spec)

~~~yaml
name: "AI Train (Governed)"

on:
  push:
    paths:
      - "src/ai/**"
      - "data/training/**"
      - "configs/ai/**"
  workflow_dispatch:
    inputs:
      model_id:
        description: "Model identifier (e.g. focus_transformer_v2_1)"
        required: true
        type: string
      dataset_ref:
        description: "STAC / DCAT data reference"
        required: true
        type: string
      config_path:
        description: "Training config path"
        required: false
        default: "configs/ai/focus_v2_1.yaml"
        type: string
      epochs:
        description: "Number of epochs"
        required: false
        default: "3"
        type: number
      device:
        description: "Execution device"
        required: false
        default: "cuda"
        type: choice
        options: [cpu, cuda]

permissions:
  contents: read
  actions: read
  id-token: write

concurrency:
  group: ai-train-${{ github.ref }}-${{ inputs.model_id || 'focus_transformer_v2_1' }}
  cancel-in-progress: true

env:
  PYTHON_VERSION: "3.11"
  PIP_CACHE_DIR: ~/.cache/pip
  HF_HOME: ~/.cache/huggingface
  PIP_DISABLE_PIP_VERSION_CHECK: "1"

jobs:
  train:
    name: Train & Validate (${{ inputs.model_id || 'focus_transformer_v2_1' }})
    runs-on: ${{ inputs.device == 'cuda' && 'ubuntu-22.04-gpu' || 'ubuntu-22.04' }}
    timeout-minutes: 480
    env:
      MODEL_ID:    ${{ inputs.model_id }}
      DATASET_REF: ${{ inputs.dataset_ref }}
      CONFIG_PATH: ${{ inputs.config_path }}
      EPOCHS:      ${{ inputs.epochs }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Cache deps
        uses: actions/cache@v4
        with:
          path: |
            ${{ env.PIP_CACHE_DIR }}
            ${{ env.HF_HOME }}
          key: ${{ runner.os }}-pip-${{ hashFiles('pyproject.toml','poetry.lock','requirements.lock') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Install deps
        run: |
          pip install -U pip wheel
          pip install -r requirements.txt -r requirements.train.txt

      - name: Validate data contract
        run: |
          python scripts/validate_contract.py \
            --dataset "$DATASET_REF" \
            --contract docs/contracts/data-contract-v3.json \
            --out "data/work/staging/tabular/tmp/validation/contract_${MODEL_ID}.json"

      - name: FAIR+CARE audit
        run: |
          python tools/validation/faircare_validator.py \
            --dataset "$DATASET_REF" \
            --out "data/work/staging/tabular/tmp/validation/faircare_${MODEL_ID}.json"

      - name: PII / Sensitive gate
        run: |
          python scripts/scan_pii_sensitive.py \
            --dataset "$DATASET_REF" \
            --fail-on-sensitive

      - name: Train model
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          python src/ai/train.py \
            --model "$MODEL_ID" \
            --data "$DATASET_REF" \
            --config "$CONFIG_PATH" \
            --epochs "$EPOCHS" \
            --device "${{ inputs.device }}"

      - name: Evaluate (metrics + OOD + drift)
        run: |
          python src/ai/eval.py \
            --model "$MODEL_ID" \
            --data "$DATASET_REF" \
            --out "reports/ai/${MODEL_ID}/metrics.json"
          python src/ai/drift_check.py \
            --model "$MODEL_ID" \
            --baseline "releases/models/${MODEL_ID}/baseline_metrics.json" \
            --out "reports/ai/${MODEL_ID}/drift.json"

      - name: Explainability (SHAP/LIME/IG)
        run: |
          python src/ai/explainability/run_shap.py \
            --model "$MODEL_ID" \
            --data "$DATASET_REF" \
            --out "reports/ai/${MODEL_ID}/explainability.json"

      - name: Generate Model Card
        run: |
          python scripts/make_model_card.py \
            --model "$MODEL_ID" \
            --metrics "reports/ai/${MODEL_ID}/metrics.json" \
            --drift   "reports/ai/${MODEL_ID}/drift.json" \
            --explain "reports/ai/${MODEL_ID}/explainability.json" \
            --template "docs/templates/model_card.md" \
            --out "data/processed/models/${MODEL_ID}/MODEL_CARD.md"

      - name: Build SBOM (SPDX)
        uses: anchore/syft-action@v1
        with:
          args: "dir:. -o spdx-json=./releases/v11.2.6/sbom.spdx.json"

      - name: Attest Build Provenance (SLSA)
        uses: slsa-framework/slsa-github-generator/actions/attest-build-provenance@v1
        with:
          subject-path: "data/processed/models/${{ env.MODEL_ID }}/"

      - name: Install Cosign
        uses: sigstore/cosign-installer@v3

      - name: Cosign sign model card
        run: |
          cosign sign-blob --yes \
            --output-signature "data/processed/models/${MODEL_ID}/signature.sig" \
            --output-certificate "data/processed/models/${MODEL_ID}/certificate.pem" \
            "data/processed/models/${MODEL_ID}/MODEL_CARD.md"

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: ai_${{ env.MODEL_ID }}_artifacts
          path: |
            data/processed/models/${{ env.MODEL_ID }}/
            reports/ai/${{ env.MODEL_ID }}/
            data/work/staging/tabular/tmp/validation/*${{ env.MODEL_ID }}*.json

      - name: Emit telemetry
        run: |
          python scripts/emit_telemetry.py \
            --kind ai_train \
            --summary "reports/ai/${MODEL_ID}/metrics.json" \
            --drift   "reports/ai/${MODEL_ID}/drift.json" \
            --explain "reports/ai/${MODEL_ID}/explainability.json" \
            --out "telemetry_ai_${MODEL_ID}.json"

      - name: Merge telemetry → unified log
        run: |
          python scripts/merge_telemetry.py \
            --in  "telemetry_ai_${MODEL_ID}.json" \
            --dest "releases/v11.2.6/ai-train-telemetry.json"
~~~

---

## 📦 Data & Metadata

### 1. Inputs

- **Config:** `configs/ai/<model>.yaml`  
  - Model family and version.  
  - STAC/DCAT dataset references.  
  - Hyperparameters, seeds, resource limits.  
- **Data:** STAC/DCAT referenced datasets resolved via:
  - `dataset_ref` input, or  
  - Mapping in the training config.

### 2. Artifacts

Per `MODEL_ID`, the workflow MUST produce (at minimum):

- `data/processed/models/<MODEL_ID>/model_metadata.json`  
- `data/processed/models/<MODEL_ID>/metrics.json`  
- `data/processed/models/<MODEL_ID>/drift.json`  
- `data/processed/models/<MODEL_ID>/explainability.json`  
- `data/processed/models/<MODEL_ID>/MODEL_CARD.md`  
- `data/processed/models/<MODEL_ID>/signature.sig`  
- `data/processed/models/<MODEL_ID>/certificate.pem`

Release-level artifacts:

- `releases/v11.2.6/sbom.spdx.json`  
- `releases/v11.2.6/manifest.zip`  
- `releases/v11.2.6/ai-train-telemetry.json`

### 3. Telemetry Record Shape (Conceptual)

Each run contributes an entry similar to:

~~~json
{
  "workflow": "ai-train",
  "run_id": "ai-train_2025-12-06T18-00-00Z_focus-transformer-v2_1",
  "model_id": "focus_transformer_v2_1",
  "dataset_ref": "kfm:stac:collection:training:focus:v2_1",
  "workflow_duration_sec": 840,
  "train_time_min": 135.2,
  "energy_wh": 1835,
  "carbon_gco2e": 612,
  "f1_macro": 0.842,
  "faircare_bias_score": 0.05,
  "drift_flag": false,
  "explainability_stability": 0.93,
  "timestamp": "2025-12-06T18:14:06Z"
}
~~~

The exact schema is defined in `schemas/telemetry/ai-train-workflow-v11.2.6.json`.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. PROV-O

For each training run:

- **Entities**
  - `ex:ModelVersion_<MODEL_ID>_<VERSION>`  
  - `ex:DatasetVersion_<DATASET_ID>_<VERSION>`  
  - `ex:TrainingReport_<RUN_ID>` (metrics, drift, explainability, model card)  
- **Activity**
  - `ex:TrainingRun_<RUN_ID>`  
- **Agents**
  - `ex:KFM_CI_Bot` (software agent)  
  - `ex:ModelOwnerTeam` (organization)  

Key relations:

- `ex:TrainingRun_<RUN_ID> prov:used ex:DatasetVersion_<...>`  
- `ex:TrainingRun_<RUN_ID> prov:used ex:ModelConfig_<...>`  
- `ex:TrainingReport_<RUN_ID> prov:wasGeneratedBy ex:TrainingRun_<RUN_ID>`  
- `ex:TrainingRun_<RUN_ID> prov:wasAssociatedWith ex:KFM_CI_Bot`  

These mappings enable reconstruction of which dataset and config produced which model version.

### 2. DCAT

- Each train/eval bundle can be a `dcat:Dataset`:
  - `dct:title`: "Training & Evaluation for ${MODEL_ID} — ${RUN_ID}"  
  - `dct:description`: Short narrative summarizing training context and metrics.  
  - `dct:identifier`: `${MODEL_ID}-${RUN_ID}`.  
  - `dct:issued`: run completion time.  
- `dcat:Distribution` entries point to:
  - Model card,  
  - Metrics/drift/explainability JSON,  
  - SBOM,  
  - Telemetry snapshots.  

### 3. STAC

For geo-aware models:

- Represent training/validation results as STAC Items in a `kfm-ai-train` Collection:
  - `id`: `${MODEL_ID}-${RUN_ID}`  
  - `properties.datetime`: training completion.  
  - `assets`:
    - `model-card` → `MODEL_CARD.md`  
    - `metrics` → `metrics.json`  
    - `drift` → `drift.json`  
    - `explainability` → `explainability.json`  
- `geometry` / `bbox` may reflect:
  - Training coverage (e.g., Kansas bounding box), or  
  - The footprint of training data if spatially constrained.

---

## 🧱 Architecture

### 1. Module Boundaries

- `src/ai/*`:
  - Training and evaluation logic.  
  - No direct CI-specific APIs (keep reusable).  
- `tools/`:
  - Data contract validation, FAIR+CARE checks, telemetry emission utilities.  
- `.github/workflows/ai-train.yml`:
  - Orchestration only; calls stable CLIs and scripts.  
- `docs/workflows/ai-train.yml.md`:
  - This document; authoritative workflow spec.

### 2. Determinism & Config

- All randomness:
  - Seeded via values in `configs/ai/<model>.yaml`.  
  - Seeds logged in model metadata and telemetry.  
- No hidden configuration:
  - All thresholds for drift/fairness must be explicitly configurable and documented.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR

| Aspect      | Implementation                                                                 |
|-------------|--------------------------------------------------------------------------------|
| Findable    | Stable IDs (`MODEL_ID`, `RUN_ID`), catalog inclusion, path conventions         |
| Accessible  | Governed artifacts exposed through CI artifacts and/or storage with policies  |
| Interoperable | JSON Schema, DCAT 3.0, STAC, and PROV-O mappings                            |
| Reusable    | Clear licensing, versioning, and provenance; documented configs and metrics   |

### 2. CARE

- **Collective Benefit**  
  Training runs include fairness & drift checks, improving overall safety and trust.  

- **Authority to Control**  
  Sensitive attributes and groups are defined by governance documents; the workflow enforces redaction and gating.  

- **Responsibility**  
  Fail-fast behavior for PII/sensitive data or unfairness breaches; requires explicit mitigation and override.  

- **Ethics**  
  Checks must be interpretable; metrics and thresholds documented in configs and model cards.

### 3. Governance Hooks

- `ai-train.yml` is a **required check** for high-risk model families.  
- Governance bodies (FAIR+CARE Council, AI Governance WG) periodically review:
  - Metric definitions,  
  - Guardrails,  
  - Drift strategies,  
  - Telemetry trends.  

---

## 🕰️ Version History

| Version    | Date       | Author       | Summary                                                                                                     |
|-----------:|------------|-------------|-------------------------------------------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-11 | `@kfm-ai`   | Aligned to KFM v11.2.6; updated release and telemetry references to `v11.2.6`, adopted emoji directory layout, and extended footer navigation. |
| v11.2.4   | 2025-12-06 | `@kfm-ai`   | Aligned with KFM‑MDP v11.2.4; expanded front-matter, STAC/DCAT/PROV mappings, Story Node hooks, and telemetry ref to v11.2.4; no breaking semantic changes to training flow. |
| v10.2.4   | 2025-11-12 | `@kfm-ai`   | Telemetry schema v3; Focus Transformer v2.1 alignment; added PII/sensitive gate and updated SBOM/manifest refs. |
| v10.1.0   | 2025-11-10 | `@kfm-ai`   | Introduced telemetry v2, integrated IG explainability, SLSA/Cosign attestations.                            |
| v9.9.0    | 2025-11-08 | `@kfm-ai`   | Initial governed AI training workflow doc with drift/explainability and telemetry export.                   |

---

<div align="center">

🧠 **Kansas Frontier Matrix — AI Training Workflow (`ai-train.yml`) · v11.2.6**  
Deterministic Training · FAIR+CARE Governance · SLSA & SBOM · Focus-Ready Model Intelligence  

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/AI-Train%2FEval-governed" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Back to CI/CD & Governance Workflows](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[📚 Glossary](../glossary.md) ·  
[📐 Markdown Protocol (KFM-MDP v11.2.4)](../standards/kfm_markdown_protocol_v11.2.4.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md) ·  
[🤝 FAIR+CARE Guide](../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)  

  
© 2025 Kansas Frontier Matrix — CC-BY 4.0 for this document  
MCP-DL v6.3 · KFM-MDP v11.2.4 · FAIR+CARE Governance · Diamond⁹ Ω / Crown∞Ω Certified  

</div>
