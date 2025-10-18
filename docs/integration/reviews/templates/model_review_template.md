<div align="center">

# 🤖 Kansas Frontier Matrix — **Model Integration Review Template**  
`docs/integration/reviews/templates/model_review_template.md`

**Purpose:** Standardize **AI/ML model reviews** across the Kansas Frontier Matrix (KFM) to ensure that  
every model (NER, summarization, embeddings, classifiers, geospatial inference, etc.) meets **MCP-DL v6.3**  
requirements for **reproducibility, provenance, security, ethics, and interoperability** with KFM’s graph and UI.

[![Docs-Validate](https://img.shields.io/badge/docs-validated-brightgreen?logo=github)](../../../../../.github/workflows/docs-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../../../.github/workflows/policy-check.yml)
[![Security · Trivy](https://img.shields.io/badge/Security-Trivy-blue)](../../../../../.github/workflows/trivy.yml)
[![Aligned · CIDOC · OWL-Time · PROV-O](https://img.shields.io/badge/Aligned-CIDOC%20CRM%20%7C%20OWL--Time%20%7C%20PROV--O-green)](../../../metadata-standards.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

```yaml
---
title: "Model Integration Review Template"
document_type: "Review Template · AI/ML"
version: "v1.0.0"
last_updated: "2025-10-18"
created: "2025-10-04"
owners: ["@kfm-ai","@kfm-ontology","@kfm-review-board","@kfm-security"]
status: "Stable"
maturity: "Production"
scope: "Docs/Integration/Reviews/Templates"
tags: ["review","model","ai","ml","ethics","reproducibility","security","provenance"]
license: "CC-BY 4.0"
audit_framework: "MCP-DL v6.3"
related_docs:
  - "docs/model_card.md"
  - "docs/architecture/ai-system.md"
  - "docs/integration/reviews/checklist.md"
---
````

---

## 🧭 Overview

This template is completed during **model reviews** to verify that an AI/ML component is:

* **Reproducible** (seeded, versioned, deterministic where applicable)
* **Provenanced** (inputs, scripts, parameters, environment captured)
* **Ethical & Secure** (bias evaluated; licensing & PII policies honored; supply chain checked)
* **Interoperable** with KFM’s **Neo4j knowledge graph**, **STAC/DCAT metadata**, and **web frontend** (Focus Mode, timeline, map)

> After completion, commit the filled review under
> `docs/integration/reviews/logs/YYYY-MM-DD_<model_name>.md` and update `audit-index.json`.

---

## 🧱 Model Information

| Field                   | Description                                           | Example                                                         |
| :---------------------- | :---------------------------------------------------- | :-------------------------------------------------------------- |
| **Model Name**          | Canonical model identifier                            | `frontier_ner_v3`                                               |
| **Task / Modality**     | NER / Summarization / Embeddings / Classifier / Other | `NER (spaCy + transformer)`                                     |
| **Location (path/URI)** | Where artifact is stored                              | `models/frontier_ner_v3/` or `s3://kfm-models/frontier_ner_v3/` |
| **Artifact Hash**       | SHA-256 of model file                                 | `ab12…ef90`                                                     |
| **Version**             | SemVer                                                | `3.1.0`                                                         |
| **Reviewer(s)**         | Assigned reviewers                                    | `@kfm-ai`, `@kfm-ontology`                                      |
| **Date**                | ISO 8601                                              | `2025-10-18`                                                    |

---

## 📦 Training & Data Provenance

| Check                         | Description                                                          | Status |
| :---------------------------- | :------------------------------------------------------------------- | :----- |
| [ ] **Datasets Listed**       | All training/eval datasets enumerated with versions and URLs.        |        |
| [ ] **Licenses**              | Dataset licenses compatible; terms recorded (PD/CC-BY/CC0/CC BY-SA). |        |
| [ ] **Data Lineage**          | PROV-O narrative: source → preprocess → split → train.               |        |
| [ ] **Preprocessing Scripts** | Versioned under `src/` with pinned dependencies.                     |        |
| [ ] **PII/Sensitive Data**    | None used OR explicit approval & redaction policy applied.           |        |
| [ ] **Consent/Restrictions**  | Oral-history or restricted data follows ethics SOP.                  |        |
| [ ] **Data Statements**       | Dataset cards or documentation linked.                               |        |

---

## ⚙️ Training Configuration & Environment

| Check                       | Description                                                         | Status |
| :-------------------------- | :------------------------------------------------------------------ | :----- |
| [ ] **Code Version**        | Git commit SHA for training code recorded.                          |        |
| [ ] **Environment**         | OS, CUDA/CPU, framework versions documented.                        |        |
| [ ] **Dependencies**        | Locked `requirements.txt`/`environment.yml` or `package-lock.json`. |        |
| [ ] **Seeds / Determinism** | Random seeds fixed; any nondeterminism noted.                       |        |
| [ ] **Hyperparameters**     | Learning rate, epochs, batch size, etc. logged (YAML/JSON).         |        |
| [ ] **Compute Budget**      | GPUs/CPUs, hours used; carbon notes (optional).                     |        |
| [ ] **Repro Script**        | `make train` or `tools/train_model.py` reproduces results.          |        |

---

## 📊 Metrics & Evaluation

| Check                            | Description                                                       | Status |
| :------------------------------- | :---------------------------------------------------------------- | :----- |
| [ ] **Task-appropriate Metrics** | NER: P/R/F1; Summarization: ROUGE/BLEU; Embeddings: Recall@K/STS. |        |
| [ ] **Baseline Comparison**      | Gains vs. prior KFM model or public baseline reported.            |        |
| [ ] **Confidence Intervals**     | CI or variance across 3+ runs (if applicable).                    |        |
| [ ] **Holdout & Leakage**        | Proper separation; no train/test contamination.                   |        |
| [ ] **Error Analysis**           | Common failure modes described with examples.                     |        |
| [ ] **Regression Tests**         | Guardrails to prevent metric regressions in CI.                   |        |

---

## ⚖️ Bias, Fairness, & Ethics

| Check                        | Description                                                       | Status |
| :--------------------------- | :---------------------------------------------------------------- | :----- |
| [ ] **Bias Audit**           | Evaluate outputs across subgroups (e.g., tribal names, toponyms). |        |
| [ ] **Cultural Sensitivity** | Respect for Indigenous contexts; language reviewed.               |        |
| [ ] **Risk Assessment**      | Document risks (hallucination, misattribution) + mitigations.     |        |
| [ ] **Human-in-the-loop**    | Confirm critical outputs require curator oversight when needed.   |        |
| [ ] **Disclosure**           | Model Card captures limitations & appropriate-use guidance.       |        |

---

## 🔍 Explainability & Observability

| Check                     | Description                                                  | Status |
| :------------------------ | :----------------------------------------------------------- | :----- |
| [ ] **Explainability**    | SHAP/LIME or task-appropriate explanation, where applicable. |        |
| [ ] **Logging**           | Inference logs include model version, latency, confidence.   |        |
| [ ] **Tracing**           | Requests correlated with reviewable artifacts (ids, hashes). |        |
| [ ] **Confidence Output** | Provide score bands; UI uses H/M/L visual cues.              |        |

---

## 🧠 Interoperability (Graph · Timeline · Focus Mode)

| Check                    | Description                                                       | Status |
| :----------------------- | :---------------------------------------------------------------- | :----- |
| [ ] **Graph Hooks**      | Output schema aligns with Neo4j ingestion (entities & relations). |        |
| [ ] **CIDOC/OWL-Time**   | Entity/time mappings recorded for extracted objects.              |        |
| [ ] **STAC/DCAT Links**  | Predictions reference dataset IDs and assets where relevant.      |        |
| [ ] **Focus Mode Ready** | Results index into Focus Mode (entity IDs, cross-links).          |        |
| [ ] **Vector Index**     | Embedding models register with Neo4j Vector Index if applicable.  |        |

---

## 🔐 Security & Supply Chain

| Check                         | Description                                              | Status |
| :---------------------------- | :------------------------------------------------------- | :----- |
| [ ] **Model Hash**            | SHA-256 recorded; artifact immutably stored.             |        |
| [ ] **Software Scans**        | CodeQL + Trivy pass; SBOM generated (no critical vulns). |        |
| [ ] **Policy-as-Code**        | OPA/Conftest rules pass (`make policy-check`).           |        |
| [ ] **Actions Pinned**        | CI actions pinned by tag/SHA; containers pinned.         |        |
| [ ] **License Compatibility** | Model + deps compatible with repo license.               |        |

---

## 🚀 Deployment & Runtime

| Check                      | Description                                               | Status |
| :------------------------- | :-------------------------------------------------------- | :----- |
| [ ] **Inference API**      | Endpoint contract documented (request/response schemas).  |        |
| [ ] **Throughput/Latency** | Meets SLOs under expected load.                           |        |
| [ ] **Resource Use**       | CPU/GPU/memory footprints captured; autoscaling guidance. |        |
| [ ] **Fallbacks**          | Safe degradations when model absent or low-confidence.    |        |
| [ ] **Cache/Cold Start**   | Warmup routines; cache invalidation policy.               |        |
| [ ] **Monitoring**         | Metrics & alerts integrated (errors, latency, drift).     |        |

---

## 🧩 Documentation Synchronization

| Check                     | Description                                          | Status |
| :------------------------ | :--------------------------------------------------- | :----- |
| [ ] **Model Card**        | `docs/model_card.md` created/updated for this model. |        |
| [ ] **Architecture Link** | Referenced in `docs/architecture/ai-system.md`.      |        |
| [ ] **Integration Docs**  | Linked from `docs/integration/*` where used.         |        |
| [ ] **Version History**   | Changelog updated; SemVer incremented.               |        |

---

## 🧮 Reviewer Summary

| Field                     | Notes                                                    |
| :------------------------ | :------------------------------------------------------- |
| **Findings**              |                                                          |
| **Actions Required**      |                                                          |
| **Follow-up Tasks**       |                                                          |
| **Dependencies Affected** |                                                          |
| **Decision**              | ☐ Approved  ☐ Conditional Approval  ☐ Revisions Required |

---

## 🗃 YAML Review Record (Append to Audit Log)

```yaml
model: frontier_ner_v3
review_type: model
reviewers: ["@kfm-ai","@kfm-ontology"]
status: approved
validation:
  metrics:
    f1: 0.91
    precision: 0.92
    recall: 0.90
  bias_audit: documented
  security: clean
  reproducibility: deterministic
artifacts:
  location: "models/frontier_ner_v3/"
  sha256: "ab12...ef90"
notes: "NER improvements on tribal/placename extraction; Focus Mode hooks validated."
timestamp: 2025-10-18T15:05:00Z
```

---

## 🔗 References

* [`docs/model_card.md`](../../../../model_card.md) — Model Card template & guidance
* [`docs/architecture/ai-system.md`](../../../../architecture/ai-system.md) — AI/ML system overview
* [`docs/integration/reviews/checklist.md`](../checklist.md) — Integration Board master checklist
* [`docs/standards/metadata.md`](../../../standards/metadata.md) — STAC/DCAT/PROV schema fields
* [`docs/standards/markdown_rules.md`](../../../standards/markdown_rules.md) — KFM Markdown & governance rules

---

<div align="center">

### 🤖 “Models write stories from data — reviews ensure those stories are faithful.”

**Kansas Frontier Matrix Review Council · MCP-DL v6.3**

</div>
