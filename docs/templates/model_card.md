---
title: "🤖 Kansas Frontier Matrix — AI/ML Model Card Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/templates/model_card.md"
version: "v10.2.2"
last_updated: "2025-11-12"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-modelcard-template-v2.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🤖 **Kansas Frontier Matrix — AI/ML Model Card Template**  
`docs/templates/model_card.md`

**Purpose:**  
Standardize how KFM documents AI/ML models for **reproducibility, explainability, and FAIR+CARE governance**.  
Every model card is machine-validated in CI and registered to the **Governance Ledger** with checksum lineage and telemetry.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../standards/faircare.md)
[![Status: Template](https://img.shields.io/badge/Status-Template-lightgrey)]()

</div>

---

## 📘 Overview

A **Model Card** describes the model’s **purpose, data, architecture, performance, risks, and ethics**.

All KFM models (e.g., Focus Mode inference, entity extraction, summarization) **must** include a `model_card.md` derived from this template and:

- Pass **`docs-lint.yml`** (front-matter, headings, links, Mermaid guardrails).  
- Pass **`faircare-validate.yml`** (ethics, CARE tags, PII/sensitivity checks).  
- Contribute to **`telemetry-export.yml`** (build, energy/carbon, governance metrics).  
- Align with **KFM Markdown Protocol v11.2.4**, STAC/DCAT cataloging, and PROV-O lineage modeling.

**Storage pattern (for actual model cards):**

~~~text
src/ai/models/<model_name>/
├── model_card.md          # ← Fill from this template
├── train.py
├── eval.py
└── artifacts/             # Checkpoints, configs, logs
~~~

---

## 🗂️ Directory Layout

Use this layout (or a close variant) for each governed model:

~~~text
src/ai/models/
├── focus_transformer_v2_1/
│   ├── model_card.md
│   ├── train.py
│   ├── eval.py
│   ├── config/
│   │   └── focus_v2_1.yaml
│   └── artifacts/
│       ├── checkpoints/
│       ├── logs/
│       └── reports/
└── <other_model>/
    ├── model_card.md
    └── ...
~~~

Model cards may also be mirrored into release artifacts:

~~~text
releases/models/<model_name>/
├── MODEL_CARD.md          # Generated or copied from src/ai/models/...
├── signature.sig
├── certificate.pem
└── metrics.json
~~~

---

## 🧭 Context

Model cards in KFM are:

- **Documentation artifacts** in `docs/` and `src/ai/models/**`.  
- **Catalog records** for DCAT/STAC: each model is a dataset/asset with clear provenance.  
- **Graph nodes** in Neo4j: linked to datasets, workflows, Story Nodes, and governance decisions.  
- **Focus Mode sources**: surfaced as authoritative context when users inspect model behavior.

They are tightly integrated with:

- CI workflows: `ai-train.yml`, `ai-explainability.yml`, `docs-lint.yml`, `faircare-validate.yml`, `telemetry-export.yml`.  
- STAC/DCAT catalogs describing models, training data, and evaluation datasets.  
- PROV-O provenance graphs (Entities = models/artifacts; Activities = training/eval; Agents = people/services).

---

## 🧱 Architecture

### 🧩 Model Overview (Fill Per Model)

| Field              | Description                                     |
|--------------------|-------------------------------------------------|
| **Model Name**     | Human-readable name + short ID                  |
| **Version**        | SemVer (e.g., `v1.0.0`)                         |
| **Author(s)**      | Names + affiliations/contact                    |
| **Date Created**   | ISO 8601 (`YYYY-MM-DD`)                         |
| **License**        | MIT/Apache-2.0/CC-BY-4.0 (match repo policy)    |
| **Repository Path**| e.g., `src/ai/models/focus_transformer_v2_1/`   |

**Example (replace with real content):**  
> *Focus Transformer v2.1* — contextual summarizer and entity linker for Focus Mode.  
> Optimized for Kansas historical documents, ecological/hazards narratives, and geospatial context.

---

### 🎯 Intended Use

| Aspect              | Details |
|---------------------|---------|
| **Primary Task(s)** | e.g., NER, summarization, embedding search, risk scoring |
| **Intended Domain** | Historical texts, geospatial docs, environmental/hazards reports |
| **Intended Users**  | Researchers, developers, curators, educators, policy analysts |
| **Not Intended For**| Autonomous high-stakes decision-making, law enforcement, medical triage, or culturally sensitive data use without explicit Council approval |

> Clearly list **non-approved** use-cases to satisfy FAIR+CARE governance.

---

### 🧠 Model Architecture

| Component          | Description                                             |
|--------------------|---------------------------------------------------------|
| **Base Architecture** | e.g., Encoder-only, Encoder-Decoder, LLM             |
| **Backbone / Checkpoint** | e.g., `bert-base-uncased`, `longformer-base-4096` |
| **Inputs**         | Text, optional metadata (time, location, CARE tags)     |
| **Outputs**        | Entities, summaries, scores, embeddings, etc.           |
| **Parameter Count**| Total parameters; approximate model size                |
| **Frameworks**     | PyTorch/TF/spaCy versions                              |
| **Dependencies**   | Major libs, external services, embeddings               |

**Optional Architecture Diagram**

~~~mermaid
flowchart TD
    A["Input Text / Metadata"] --> B["Tokenizer / Feature Builder"]
    B --> C["Transformer Encoder/Decoder"]
    C --> D["Task Heads (NER / Summary / Scoring)"]
    D --> E["Outputs (Entities / Text / Scores / Embeddings)"]
~~~

---

## 📦 Data & Metadata

### 🧪 Training Data & Methodology

Describe data and training pipeline with enough detail for reproduction.

| Field                  | Description                                   |
|------------------------|-----------------------------------------------|
| **Training Dataset(s)**| Source names, DOIs/URLs, licenses             |
| **Preprocessing**      | Cleaning, OCR normalization, tokenization     |
| **Sampling Strategy**  | Random/stratified/balanced; rationale         |
| **Hyperparameters**    | LR, batch size, epochs, optimizer, regularization |
| **Hardware/Env**       | GPU model, CPU, RAM, Docker image digest, seeds |

**Example command**

~~~bash
python src/ai/models/focus_transformer_v2_1/train.py \
  --config configs/ai/focus_v2_1.yaml \
  --epochs 15 \
  --learning-rate 3e-5 \
  --seed 42
~~~

---

### ⚙ Configuration & Hyperparameters

Use this table to ensure reproducibility.

| Parameter         | Description          | Value                        |
|-------------------|----------------------|------------------------------|
| `epochs`          | Training iterations  | 20                           |
| `learning_rate`   | Optimizer step       | 5e-4                         |
| `batch_size`      | Samples per batch    | 32                           |
| `max_seq_len`     | Max tokens per input | 1024                         |
| `bbox` (if spatial)| Spatial extent      | `[-102.05, 37.00, -94.60, 40.00]` |
| `temporal_range`  | Years or dates       | `1950–2025`                  |
| `ocr_model`       | Versioned OCR engine | `tesseract-5.3.2`            |

Reference supporting manifests:

~~~text
data/checksums/manifest.json
data/sources/*_source_metadata.json
~~~

---

### 📁 Outputs & Storage

| Artifact         | Location                                | Format              |
|------------------|-----------------------------------------|---------------------|
| Checkpoints      | `releases/models/<model>/checkpoints/` | framework-specific  |
| Metrics          | `reports/ai/<model>/metrics.json`       | JSON                |
| Drift Report     | `reports/ai/<model>/drift.json`         | JSON                |
| Explainability   | `reports/ai/<model>/explainability.json`| JSON                |
| Model Card       | `releases/models/<model>/MODEL_CARD.md`| Markdown            |
| Telemetry        | `releases/v10.2.0/focus-telemetry.json`| JSON (ledger)       |

---

## 🧪 Validation & CI/CD

### 📊 Evaluation Metrics

Summarize evaluation metrics and datasets.

| Metric         | Description                     | Value (example) |
|----------------|---------------------------------|-----------------|
| Accuracy       | Overall correctness             | 0.94            |
| Precision      | Positive predictive value       | 0.92            |
| Recall         | Sensitivity / coverage          | 0.95            |
| F1 Score       | Harmonic mean                   | 0.935           |
| Task-Specific  | e.g., ROUGE-L for summaries     | 0.78            |

> Specify **evaluation dataset(s)**, splits, and any **held-out** or OOD sets used.

---

### 🔍 Explainability, Safety & Bias

| Category           | Notes                                       |
|--------------------|---------------------------------------------|
| **Explainability Tools** | SHAP, LIME, Integrated Gradients, attention inspection |
| **Feature Importance**   | Key features (tokens, fields) that drive predictions   |
| **Bias Detection**       | Groups/segments evaluated; disparity metrics          |
| **Mitigation Steps**     | Reweighting, augmentation, thresholding, human review |
| **Known Limitations**    | Failures (e.g., low-contrast scans, dialect variation)|
| **Safety**               | Guardrails (rate limits, max output length, filters)  |

**Example Insight**  
> Entity recall drops for tribal names in OCR-degraded sources; mitigation added via targeted augmentation and manual annotation of tribal name lexicons.

---

### 🔁 Reproducibility Checklist

Tick all boxes before merging a model card:

- [ ] Dataset(s) documented with licenses and access links  
- [ ] Hyperparameters and seeds recorded  
- [ ] Training and evaluation scripts available  
- [ ] SBOM (`sbom.spdx.json`) and manifest (`manifest.zip`) generated  
- [ ] FAIR+CARE audit run and logged  
- [ ] Model registered in `ai_models` ledger  

**Example commands**

~~~bash
make train-model  MODEL=focus_transformer_v2_1
make eval-model   MODEL=focus_transformer_v2_1
make package-model MODEL=focus_transformer_v2_1
~~~

---

### 🧪 CI / QA Integration

All model cards must pass:

| Workflow                 | Purpose                                           |
|--------------------------|---------------------------------------------------|
| `docs-lint.yml`          | YAML, headers, links, Mermaid guardrails         |
| `faircare-validate.yml`  | Ethics + governance                               |
| `stac-validate.yml`      | If model outputs STAC metadata or depends on it  |
| `ai-train.yml`           | Training, eval, SBOM, SLSA, telemetry             |
| `ai-explainability.yml`  | Explainability, bias, drift audits                |
| `telemetry-export.yml`   | Logs sustainability & reproducibility metrics     |

---

## 🌐 STAC, DCAT & PROV Alignment

Model cards participate in KFM’s metadata stack:

- **DCAT**  
  - Treat each model as a `dcat:Dataset` with:  
    - `dct:title` = model name  
    - `dct:description` = high-level summary  
    - `dct:creator` / `dct:publisher` = authors/organizations  
    - `dcat:distribution` = checkpoint files, containers, API endpoints.  

- **STAC**  
  - Optionally represent models as Items in a “models” Collection:  
    - `id` = model identifier  
    - `properties.datetime` = release date  
    - `assets` = model weights, configs, MODEL_CARD, metrics, SBOM.  

- **PROV-O**  
  - Model card entity: `prov:Entity`  
  - Training/eval activities: `prov:Activity` with `prov:used` (datasets) and `prov:wasGeneratedBy` (artifacts).  
  - People/services: `prov:Agent` via `prov:wasAssociatedWith` and `prov:wasAttributedTo`.

These mappings allow model cards to be indexed, queried, and traced alongside datasets and workflows.

---

## ⚖ FAIR+CARE & Governance

Summarize ethics and governance outcomes for each model.

| Principle    | Implementation Example                                   |
|--------------|-----------------------------------------------------------|
| **Findable** | Model version + metadata in DCAT/STAC; optional DOI/ARK   |
| **Accessible** | Model card + code under open licenses; clear usage docs |
| **Interoperable** | Output semantics align with KFM schemas (graph, STAC)|
| **Reusable** | Checkpoints, config, SBOM, and manifest provide full lineage |
| **CARE**     | CARE tags respected; sensitive domains blocked; community review documented |

Attach relevant governance files (paths may vary per model):

~~~text
reports/fair/faircare_summary.json
reports/audit/ai_models.json
reports/audit/github-workflows-ledger.json
~~~

**Governance Notes (to fill per model)**

- **Council Reviewers:** Names / teams  
- **Decision:** ☑ Approved / ☐ Pending / ☒ Changes Required  
- **Key Concerns:** Bias, domain limitations, misuse risks  
- **Follow-ups:** Monitoring plans, retraining schedule, sunset criteria  

---

## 🕰️ Version History

| Version  | Date       | Author       | Summary                                                                 |
|----------|------------|-------------|-------------------------------------------------------------------------|
| v10.2.2  | 2025-11-12 | A. Barta    | Aligned refs to v10.2.0; integrated with telemetry v2; clarified governance & reproducibility gates. |
| v10.0.0  | 2025-11-10 | A. Barta    | Telemetry schema v2; tightened safety/bias documentation requirements. |
| v9.7.0   | 2025-11-05 | A. Barta    | Standardized model card for governance and reproducibility.            |
| v9.5.0   | 2025-10-20 | A. Barta    | Added FAIR+CARE & explainability sections.                             |
| v9.0.0   | 2025-06-01 | KFM Core Team | Initial template creation.                                           |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · **Diamond⁹ Ω / Crown∞Ω** Ultimate Certified  

[Back to Template Index](README.md) · [Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
