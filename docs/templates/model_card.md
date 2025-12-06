---
title: "🤖 Kansas Frontier Matrix — AI/ML Model Card Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/model_card.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.4/signature.sig"
attestation_ref: "releases/v11.2.4/slsa-attestation.json"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/docs-modelcard-template-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-modelcard-template-v11.2.4.json"
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
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "experiment-templates"
  applies_to:
    - "docs/templates/model_card.md"
    - "src/ai/models/*/model_card.md"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by AI/ML Model Card Template v12"

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
  - "docs/templates/model_card.md@v10.2.2"
  - "docs/templates/model_card.md@v10.0.0"
  - "docs/templates/model_card.md@v9.7.0"
  - "docs/templates/model_card.md@v9.5.0"
  - "docs/templates/model_card.md@v9.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-model-card-template-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-model-card-template-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:templates:model-card:v11.2.4"
semantic_document_id: "kfm-model-card-template-v11.2.4"
event_source_id: "ledger:kfm:doc:templates:model-card:v11.2.4"
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
  workflow: ".github/workflows/docs-lint.yml"
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

# 🤖 **Kansas Frontier Matrix — AI/ML Model Card Template**  
`docs/templates/model_card.md`

**Purpose**  
Standardize how KFM documents AI/ML models for **reproducibility, explainability, and FAIR+CARE governance**.  
Every model card is machine-validated in CI and registered to the **Governance Ledger** with checksum lineage and telemetry.  
The template is compatible with **STAC 1.x**, **DCAT 3.0**, and **PROV-O** so cards can be indexed in catalogs and ingested into the KFM knowledge graph.

<img src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img src="https://img.shields.io/badge/Status-Template-lightgrey" />

</div>

---

## 📘 Overview

A **Model Card** describes the model’s **purpose, data, architecture, performance, risks, and ethics**.

All KFM models (e.g., Focus Mode inference, entity extraction, summarization) **must** include a `model_card.md` derived from this template and:

- Pass **`docs-lint.yml`** (front-matter, headings, links, Mermaid guardrails).  
- Pass **`faircare-validate.yml`** (ethics, CARE tags, PII/sensitivity checks).  
- Contribute to **`telemetry-export.yml`** (build, energy/carbon, governance metrics).  
- Align with **KFM-MDP v11.2.4** and the KFM-STAC / KFM-DCAT / KFM-PROV profiles for catalog + graph ingestion.

**Canonical storage pattern (per model):**

~~~text
src/ai/models/<model_name>/
└── 📄 model_card.md        — Model card for this model (filled from this template)
~~~

---

## 🗂️ Directory Layout

Use this layout (or a close variant) for each governed AI/ML model. Emojis and comments describe each node.

~~~text
📁 KansasFrontierMatrix/
├── 📁 docs/                                          # All documentation for KFM
│   └── 📁 templates/                                # Reusable documentation templates
│       📄 README.md                                 # 📄 Index of all templates and usage rules
│       📄 experiment.md                             # 🧪 Experiment / analysis documentation template
│       📄 model_card.md                             # 🤖 AI/ML model card template (this file)
│       📄 sop.md                                    # 🧾 Standard Operating Procedure template
├── 📁 src/                                           # Source code for pipelines, services, and models
│   └── 📁 ai/
│       └── 📁 models/                                # 🤖 Per-model directories (one per governed model)
│           📁 <model_name>/                          # e.g., focus_transformer_v2_1
│           ├── 📄 model_card.md                      # 🤖 Instantiated model card for <model_name>
│           ├── 📄 train.py                           # 🧠 Training entrypoint for the model
│           ├── 📄 eval.py                            # 📊 Evaluation entrypoint for the model
│           ├── 📁 config/                            # ⚙️ Config files for training/eval (YAML/JSON)
│           └── 📁 artifacts/                         # 📦 Checkpoints, logs, metrics, exports
├── 📁 releases/                                      # 📦 Versioned releases + telemetry
│   📁 v11.2.4/
│   ├── 📄 sbom.spdx.json                             # 🧬 SBOM for builds in this release
│   ├── 📄 manifest.zip                               # 📑 Manifests (checksums, asset lists)
│   └── 📄 focus-telemetry.json                       # 📈 Unified telemetry ledger (all workflows)
├── 📁 reports/
│   └── 📁 ai/                                        # 📊 Model training & evaluation reports
│       📁 <model_name>/                              # Reports for this specific model
│       ├── 📄 metrics.json                           # 📊 Metrics from eval runs (test/val)
│       ├── 📄 drift.json                             # 📉 Drift detection outputs (if applicable)
│       └── 📄 explainability.json                    # 🔍 Explainability outputs (SHAP/LIME/etc.)
└── 📁 .github/
    └── 📁 workflows/                                 # ⚙️ CI/CD definitions
        📄 ai-train.yml                               # 🚀 Governed AI training workflow
        📄 ai-explainability.yml                      # 🔍 Explainability & bias audit workflow
        📄 docs-lint.yml                              # 📏 Markdown + doc validation
~~~

When instantiating this template:

- Ensure `path` in the YAML front-matter matches the actual card location.  
- Keep emojis + comments in directory trees consistent with KFM-MDP’s layout profile.

---

## 🧭 Context

### 1. When to Use This Template

Use this template whenever you:

- Train or adopt a **governed AI/ML model** that will run in any KFM environment (ETL, Focus Mode, web, batch, etc.).  
- Need **reproducibility and governance** for model behavior and lifecycle.  
- Intend for the model to be referenced by **Story Nodes, Focus Mode**, and **STAC/DCAT catalogs**.

Typical model categories:

- **NLP models**: summarization, NER, relation extraction, embedding retrievers.  
- **Geospatial models**: raster classification, change detection, hazard scoring.  
- **Time-series models**: climate, hydrology, telemetry forecasting.  
- **Vision models**: map/imagery annotation, symbol detection for old maps.  

### 2. Section Map for Instantiated Cards

Concrete model cards created from this template should map content as:

- **Model Overview** → Identity, version, authors, license, path.  
- **Intended Use** → Tasks, domains, supported/unsupported contexts.  
- **Architecture** → Base model, layers, dependencies.  
- **Training Data & Methodology** → Datasets, preprocessing, training config.  
- **Evaluation Metrics** → Test results, OOD behavior.  
- **Explainability, Safety & Bias** → Tools, known issues, mitigations.  
- **Deployment & Integration** → Where/how the model runs in KFM.  
- **Reproducibility Checklist** → What’s required to re-run training/eval.  
- **FAIR+CARE & Governance** → Ethics summary and Council decisions.  

---

## 🗺️ Diagrams

Model cards may include **one optional Mermaid diagram per section** for architecture or flow (per KFM-MDP rules).

Example architecture diagram (adapt per model):

~~~mermaid
flowchart TD
    A["Input Text / Metadata"] --> B["Tokenizer / Feature Builder"]
    B --> C["Transformer Encoder/Decoder"]
    C --> D["Task Heads (NER / Summary / Scoring)"]
    D --> E["Outputs (Entities / Text / Scores / Embeddings)"]
~~~

Rules:

- At most **one Mermaid** diagram per section.  
- Always explain the diagram in the surrounding text.  

---

## 🧠 Story Node & Focus Mode Integration

Model cards are a primary source for **Story Nodes** and **Focus Mode**:

- Story Nodes may reference a model via an ID like `urn:kfm:model:<model_name>@vX.Y.Z`.  
- Focus Mode surfaces model cards when explaining why a model behaved in a particular way.  
- Cards should explicitly include stable identifiers (model name, version, `semantic_document_id` where applicable).

When writing a concrete model card:

- Use **clear, segmented paragraphs** so Focus Mode can extract coherent answers per H3 block.  
- Avoid ambiguous pronouns; refer to the model explicitly (e.g. `Focus Transformer v2.1` instead of “it”).  
- Put **short recap lists** at the end of complex sections (e.g., biases, mitigations).

Focus Mode:

- ✅ **MAY** summarize sections, highlight metrics, and link to STAC/DCAT/graph records.  
- ❌ **MUST NOT** fabricate model capabilities or governance approvals not present in the card.

---

## 🧪 Validation & CI/CD

Concrete model cards must integrate with KFM CI/CD:

- **`docs-lint.yml`** validates:
  - YAML front-matter structure + required keys.  
  - Heading order and emoji usage (H2 from KFM-MDP registry).  
  - Mermaid and link guardrails.

- **`faircare-validate.yml`** checks:
  - Presence of a **FAIR+CARE summary**.  
  - Sensitive-use disclosures and CARE tags.  
  - Evidence paths to governance reports.

- **`ai-train.yml` & `ai-explainability.yml`**:
  - Training/eval runs must emit metrics JSON + explainability reports that the model card references.  
  - Bias and drift checks feed into the card’s “Explainability, Safety & Bias” section.

- **`telemetry-export.yml`**:
  - Aggregates runtime + metrics into `focus-telemetry.json`, enabling trend visualization for each model.

Concrete cards should link to:

~~~text
reports/ai/<model_name>/metrics.json
reports/ai/<model_name>/drift.json
reports/ai/<model_name>/explainability.json
releases/v11.2.4/focus-telemetry.json
reports/faircare/faircare_summary.json
reports/audit/ai_models.json
~~~

---

## 📦 Data & Metadata

### 1. Required Front-Matter for Instantiated Model Cards

Every model card **MUST** start with a YAML block derived from this pattern (edit for the actual model):

~~~yaml
---
title: "🤖 [Model Name]"
path: "src/ai/models/[model_name]/model_card.md"
version: "vX.Y.Z"
last_updated: "YYYY-MM-DD"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<commit-hash>"

sbom_ref: "releases/vX.Y.Z/sbom.spdx.json"
manifest_ref: "releases/vX.Y.Z/manifest.zip"
telemetry_ref: "releases/vX.Y.Z/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/models/[model_name]-telemetry-vX.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---
~~~

Additional recommended fields:

- `model_id`: short ID (e.g. `focus_transformer_v2_1`).  
- `domain`: e.g. `"nlp"` / `"geospatial"` / `"vision"` / `"timeseries"`.  
- `status`: `"Experimental"`, `"Staging"`, or `"Production"`.  

### 2. Model Overview Section (Template)

In the concrete card:

~~~markdown
### 🧩 Model Overview

| Field              | Description                                      |
|--------------------|--------------------------------------------------|
| **Model Name**     | Human-readable name + short ID.                  |
| **Version**        | SemVer (e.g., `v1.0.0`).                         |
| **Author(s)**      | Names + affiliations/contact.                    |
| **Date Created**   | ISO 8601 (`YYYY-MM-DD`).                         |
| **License**        | Compatible license for code/weights.            |
| **Repository Path**| e.g., `src/ai/models/focus_transformer_v2_1/`.   |

Short narrative paragraph summarizing the model and its role in KFM.
~~~

### 3. Configuration & Hyperparameters

Concrete card should include:

~~~markdown
### ⚙ Configuration & Hyperparameters

| Parameter        | Description           | Value/Example             |
|------------------|-----------------------|---------------------------|
| `epochs`         | Training iterations   | `20`                      |
| `learning_rate`  | Optimizer step        | `5e-4`                    |
| `batch_size`     | Samples per batch     | `32`                      |
| `max_seq_len`    | Max tokens per input  | `1024`                    |
| `temporal_range` | If time-based input   | `1950–2025`               |
| `ocr_model`      | If OCR front-end used | `tesseract-5.3.2`         |

Reference manifests:

`data/checksums/manifest.json`  
`data/sources/*_source_metadata.json`
~~~

---

## 🧱 Architecture

Concrete cards should include:

### 🎯 Intended Use

~~~markdown
### 🎯 Intended Use

| Aspect            | Details |
|-------------------|---------|
| **Primary Task(s)** | e.g., NER, summarization, retrieval. |
| **Intended Domain** | e.g., historic Kansas texts, climate reports. |
| **Intended Users**  | Researchers, devs, curators, educators. |
| **Not Intended For**| High-stakes or prohibited domains without explicit governance approval. |
~~~

List **explicit non-intended uses** to satisfy FAIR+CARE expectations.

### 🧠 Model Architecture

~~~markdown
### 🧠 Model Architecture

| Component             | Description |
|-----------------------|-------------|
| **Base Architecture** | Encoder-only, encoder–decoder, LLM, etc. |
| **Backbone / Checkpoint** | e.g., `bert-base-uncased`, `llama-3-8b`. |
| **Inputs**            | Text, metadata (time, location, CARE tags). |
| **Outputs**           | Entities, summaries, scores, embeddings. |
| **Parameter Count**   | Approximate parameter count. |
| **Frameworks**        | PyTorch / TF versions. |
| **Dependencies**      | Major libs, external services (e.g., vector DB). |
~~~

If helpful, include the architecture Mermaid diagram from the earlier section.

### 🔬 Training Data & Methodology

~~~markdown
### 🔬 Training Data & Methodology

| Field               | Description |
|---------------------|-------------|
| **Training Dataset(s)** | Sources, DOIs/URLs, licenses. |
| **Preprocessing**        | Cleaning, OCR normalization, tokenization, filters. |
| **Sampling Strategy**    | Random/stratified/balanced; rationale. |
| **Hyperparameters**      | Summary + see configs in `config/`. |
| **Hardware/Env**         | GPU model, CPU, RAM, Docker image digest, seeds. |

Example training command:

~~~bash
python src/ai/models/<model_name>/train.py \
  --config configs/ai/<model_name>.yaml \
  --epochs 15 \
  --learning-rate 3e-5 \
  --seed 42
~~~
~~~

### 📊 Evaluation Metrics

~~~markdown
### 📊 Evaluation Metrics

| Metric         | Description                     | Value (example) |
|----------------|---------------------------------|-----------------|
| Accuracy       | Overall correctness             | 0.94            |
| Precision      | Positive predictive value       | 0.92            |
| Recall         | Sensitivity / coverage          | 0.95            |
| F1 Score       | Harmonic mean of P/R            | 0.935           |
| Task-Specific  | e.g., ROUGE-L / BLEU / NDCG@10 | 0.78            |

Document:
- Evaluation datasets + splits (ID, URL, license).
- Any OOD or robustness tests (e.g., noisy OCR, domain shift).
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

Concrete model cards should briefly describe how the model’s artifacts appear in catalogs:

- **STAC**: If model checkpoints or inference products are exposed as STAC Items, note:
  - Collection ID, Item IDs, and `assets` pointing to weights/configs.  
- **DCAT**: If the model is cataloged as a `dcat:Dataset` or `dcat:DataService`, specify:
  - Service endpoint (for hosted APIs) and distribution URLs for model artifacts.  
- **PROV-O**: Model training and evaluation should be captured as:
  - `prov:Activity` (train/eval runs), `prov:Entity` (model weights, metrics), `prov:Agent` (author, CI).  

Example DCAT/PROV note in the card:

> Training run `TRAIN-2025-01-15-fv2.1` is represented as a `prov:Activity` linked to the resulting  
> model weights (`prov:Entity`) and this model card (`prov:Entity`). The dataset is cataloged as  
> `dcat:Dataset` `urn:kfm:dataset:model:focus_transformer_v2_1` with distributions for weights,  
> configs, and this documentation.

---

## ⚖ FAIR+CARE & Governance

Each instantiated model card **must** contain a FAIR+CARE summary:

~~~markdown
### ⚖ FAIR+CARE Summary

- **Findable:** How the model is registered (IDs, catalogs, graph nodes).
- **Accessible:** License, access controls, API endpoints.
- **Interoperable:** Alignment with KFM schemas, STAC/DCAT/PROV.
- **Reusable:** How to safely reuse; SBOM + manifest availability.

- **CARE – Collective Benefit:** Who benefits; how the model supports communities.
- **CARE – Authority to Control:** How CARE tags, sovereignty policies, and governance rules are enforced.
- **CARE – Responsibility & Ethics:** Known risks, mitigations, and monitoring commitments.
~~~

Also include:

- Governance decision summary (`Approved` / `Pending` / `Changes Required`).  
- Links to FAIR+CARE reports and audit ledgers (`reports/faircare/*`, `reports/audit/*`).  

---

## 🕰️ Version History

Update this table as the template evolves; concrete model cards should maintain their own history.

| Version   | Date       | Author        | Summary                                                                                 |
|----------:|------------|---------------|-----------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-docs`   | Aligned with KFM-MDP v11.2.4; added full front-matter, emoji-rich directory layout, and STAC/DCAT/PROV integration notes. |
| v10.2.2   | 2025-11-12 | `@kfm-docs`   | Tied to telemetry v2; clarified governance & reproducibility gates.                     |
| v10.0.0   | 2025-11-10 | `@kfm-docs`   | Introduced telemetry schema v2; tightened safety/bias documentation requirements.      |
| v9.7.0    | 2025-11-05 | `@kfm-docs`   | Standardized model card structure for governance and reproducibility.                  |
| v9.5.0    | 2025-10-20 | `@kfm-docs`   | Added FAIR+CARE & explainability sections.                                             |
| v9.0.0    | 2025-06-01 | `@kfm-core`   | Initial AI/ML model card template for KFM.                                             |

---

<div align="center">

🤖 **Kansas Frontier Matrix — AI/ML Model Card Template (v11.2.4)**  
Reproducible Models · FAIR+CARE Governance · Catalog & Graph Ready  

[⬅ Back to Templates Index](README.md) ·  
[📘 Markdown Protocol (KFM-MDP v11.2.4)](../standards/kfm_markdown_protocol_v11.2.4.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
