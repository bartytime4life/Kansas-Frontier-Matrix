---
title: "🧬 Kansas Frontier Matrix — AI Treaty Models Registry"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/models/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Quarterly / Continuous"
status: "Active · FAIR+CARE+ISO Certified"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-ai", "@kfm-architecture", "@kfm-data"]
approvers: ["@kfm-governance", "@kfm-security", "@kfm-ethics"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - STAC / DCAT
  - CIDOC CRM / PROV-O / OWL-Time
  - ISO 9001 / ISO 27001 / ISO 50001 / ISO 14064
tags: ["ai","models","nlp","transformers","treaties","summarization","ner","fair","iso","provenance","mcp-dl"]
---

<div align="center">

# 🧬 Kansas Frontier Matrix — **AI Treaty Models Registry**  
`data/work/staging/tabular/normalized/treaties/reports/ai/models/README.md`

**Purpose:** Maintain version-controlled documentation and configuration for all **AI models** used in generating and validating treaty reports within the Kansas Frontier Matrix (KFM) system.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![AI Model Registry](https://img.shields.io/badge/AI-Model%20Registry-6f42c1)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Validated-2ecc71)]()
[![License](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-green)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954)]()

</div>

---

## 📚 Overview

This directory defines and tracks the **AI model configurations, parameters, and metadata** used for:
- Treaty summarization and semantic enrichment  
- Entity extraction and named-entity resolution (NER)  
- Provenance linking and metadata inference  
- Validation scoring and FAIR compliance metrics  

Each model used in the pipeline must be:
- **Versioned and reproducible**  
- **Documented with model card metadata**  
- **Linked to its provenance, checksum, and audit record**

> 🧠 *All model configurations stored here must comply with FAIR principles, CIDOC CRM ontology, and MCP-DL metadata standards.*

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/models/
├── registry/                     # Model metadata and configuration files
│   ├── gpt-5-treaty-sum.json
│   ├── treaty-ner-transformer.json
│   ├── semantic-linker.yaml
│   └── validator-bot.yaml
├── checkpoints/                  # Saved model checkpoints or hashes
│   ├── gpt-5-treaty-sum.ckpt
│   ├── ner_transformer_v2.ckpt
│   └── README.md
├── provenance/                   # Model provenance and lineage JSON-LD
│   ├── gpt-5-treaty-sum_prov.jsonld
│   └── transformer_ner_prov.jsonld
├── metrics/                      # Model evaluation and accuracy logs
│   └── treaty_ai_eval_2025-10.json
└── validation/                   # Model compliance and audit logs
    └── ai_model_validation.json
```

---

## 🧩 Model Registry Fields

| Field | Type | Description |
| :------ | :------ | :------------ |
| `model_id` | string | Unique identifier for model (namespace format) |
| `version` | string | Semantic version number (SemVer) |
| `architecture` | string | Base model architecture (e.g., Transformer, LLM, spaCy) |
| `task` | string | Primary model purpose (e.g., summarization, NER, validation) |
| `parameters` | object | Tunable hyperparameters and configuration |
| `training_data` | string | Source or dataset lineage |
| `checksum_sha256` | string | Integrity hash of the model |
| `provenance_ref` | string | Path to JSON-LD provenance file |
| `energy_wh_per_run` | float | Average energy cost per inference |
| `carbon_gco2e_per_run` | float | Carbon equivalent |
| `fa_ir_compliance_score` | number | FAIR compliance metric (0–1 scale) |

---

## 🧠 Example Model Metadata

```json
{
  "model_id": "gpt-5-treaty-sum",
  "version": "v2.3.1",
  "architecture": "Transformer (Large Context)",
  "task": "treaty_summarization",
  "parameters": {
    "max_tokens": 4096,
    "temperature": 0.2,
    "top_p": 0.9
  },
  "training_data": "normalized treaty datasets (1850–1920), public legal corpora",
  "checksum_sha256": "9d8c4b...8e7fa2",
  "provenance_ref": "provenance/gpt-5-treaty-sum_prov.jsonld",
  "energy_wh_per_run": 24.6,
  "carbon_gco2e_per_run": 28.9,
  "fair_compliance_score": 0.98
}
```

---

## 🧪 Model Validation Process

| Step | Validation Area | Tool | Output | Status |
| :---- | :--------------- | :------ | :--------- | :------ |
| 1 | Model Card Schema Validation | `jsonschema-cli` | `model_card_validation.json` | ✅ Active |
| 2 | Provenance JSON-LD Validation | `pyshacl` | `provenance_audit.json` | ✅ Active |
| 3 | Reproducibility Checksum | `sha256sum` | `checksums.json` | ✅ Active |
| 4 | FAIR+CARE Compliance Check | `fair-checker` | `fair_validation.json` | ✅ Active |
| 5 | Sustainability Metrics | `energy-metrics` | `ai_energy_audit.json` | ⚙ Planned |

---

## 📈 Evaluation Metrics

| Metric | Target | Description |
| :------ | :------ | :------------ |
| `accuracy` | ≥ 95% | Model predictive accuracy on validation data |
| `semantic_precision` | ≥ 92% | Entity and event detection correctness |
| `provenance_linking` | 100% | CIDOC/PROV-O linkage validation |
| `a11y_compliance` | ≥ 95 | Accessibility score for output reports |
| `carbon_gco2e_per_run` | ≤ 30 | Energy/carbon sustainability target |

---

## 🔐 Provenance Integration

Each model must have a **JSON-LD provenance file** stored under `/provenance/`  
conforming to **PROV-O** and **CIDOC CRM**. Required fields include:

- `wasGeneratedBy` → model training pipeline  
- `used` → datasets, training parameters  
- `qualifiedAttribution` → organization/author  
- `wasDerivedFrom` → prior model or checkpoint  

Provenance is linked to FAIR and Governance Ledgers automatically via the CI pipeline `model-provenance-validate.yml`.

---

## 🧾 Model Audit & Governance

| Audit Type | Frequency | Description | Output |
| :----------- | :------------ | :-------------- | :--------- |
| FAIR Audit | Quarterly | FAIR + CARE compliance verification | `fair_audit.json` |
| Energy Audit | Monthly | Energy & sustainability metrics | `energy_audit.json` |
| Bias Audit | Semi-Annual | Bias and representational fairness | `ethics_bias_audit.json` |
| Reproducibility Audit | Continuous | SHA-256 checksum + metadata parity | `reproducibility_report.json` |

---

## ✅ Compliance Matrix

| Standard | Domain | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | AI model documentation & ethics | ✅ |
| **MCP-DL v6.4.3** | Documentation alignment | ✅ |
| **CIDOC CRM / PROV-O** | Provenance & entity linkage | ✅ |
| **ISO 9001** | Quality assurance | ✅ |
| **ISO 27001** | Security & configuration | ✅ |
| **ISO 50001 / 14064** | Energy & carbon | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Created initial AI models registry for treaty reporting pipeline. | @kfm-ai |

---

<div align="center">

[![AI Models](https://img.shields.io/badge/AI--Models-Registered%20%26%20Versioned-6f42c1?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Immutable%20Linked-d4af37?style=flat-square)]()
[![Provenance Linked](https://img.shields.io/badge/Provenance-PROV--O%20%7C%20CIDOC-8a2be2?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · AI Models
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/models/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
ISO-ALIGNED: true
PROVENANCE-LINKED: true
MODEL-VALIDATED: true
SEMANTIC-ALIGNED: true
GOVERNANCE-LEDGER-LINKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->