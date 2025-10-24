---
title: "💾 Kansas Frontier Matrix — GPT-5 Treaty Summarization Model Checkpoint v5.2.0"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/models/checkpoints/gpt-5-treaty-sum_v5.2.0/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Continuous / Automated"
status: "Active · FAIR+CARE+ISO Validated"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-ai", "@kfm-validation", "@kfm-data"]
approvers: ["@kfm-architecture", "@kfm-governance", "@kfm-ethics"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - CIDOC CRM / PROV-O / OWL-Time
  - ISO 9001 / 27001 / 50001 / 14064
tags: ["ai","model","checkpoint","gpt-5","treaty-summarization","validation","ontology","fair","iso","provenance"]
---

<div align="center">

# 💾 Kansas Frontier Matrix — **GPT-5 Treaty Summarization Model Checkpoint v5.2.0**
`data/work/staging/tabular/normalized/treaties/reports/ai/models/checkpoints/gpt-5-treaty-sum_v5.2.0/`

**Purpose:** Record and describe the **GPT-5 Treaty Summarization Model v5.2.0** checkpoint — including its configuration, validation metrics, FAIR+CARE audit, and provenance metadata — as part of the KFM AI model lifecycle registry.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![Model Checkpoint](https://img.shields.io/badge/AI--Model-GPT--5%20Treaty%20Sum%20v5.2.0-6f42c1)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Validated-2ecc71)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-d4af37)]()

</div>

---

## 📚 Overview

This directory contains the **model checkpoint files** and supporting documents for the **GPT-5 Treaty Summarization model**, version 5.2.0.  
This checkpoint powers AI summarization workflows that convert treaty texts into semantically structured, FAIR+CARE-aligned Markdown summaries and JSON metadata.

Key characteristics:
- Fine-tuned on **Kansas Treaty Corpus v4 (1854–1871)**  
- Aligned with **CIDOC CRM**, **PROV-O**, and **OWL-Time** ontologies  
- FAIR+CARE compliance validated at 0.96 / 0.94  
- Fully traceable through governance and provenance chains  

> 🧩 *This checkpoint is a “frozen” version used for production treaty summarization pipelines.*

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/models/checkpoints/gpt-5-treaty-sum_v5.2.0/
├── checkpoint_2025-10-24.json
├── weights.bin
├── config.json
├── validation_metrics.json
├── energy_profile.json
└── provenance_links.jsonld
```

---

## 🧩 Example Checkpoint Metadata (`checkpoint_2025-10-24.json`)

```json
{
  "model_name": "gpt-5-treaty-sum",
  "model_version": "v5.2.0",
  "checkpoint_id": "chkpt-2025-10-24-001",
  "timestamp": "2025-10-24T17:10:00Z",
  "accuracy": 0.982,
  "f1_score": 0.973,
  "loss": 0.012,
  "optimizer": "AdamW",
  "learning_rate": 0.00005,
  "epochs_completed": 6,
  "dataset_ref": "Kansas_Treaty_Corpus_v4",
  "energy_wh": 21.5,
  "carbon_gco2e": 27.1,
  "fair_score": 0.96,
  "care_score": 0.94,
  "checksum_sha256": "b6f9e2a47c9...",
  "governance_hash": "c3a7f1b9d8..."
}
```

---

## ⚙️ Model Configuration (`config.json`)

```json
{
  "architecture": "Transformer Decoder",
  "hidden_layers": 48,
  "attention_heads": 64,
  "embedding_dim": 8192,
  "vocab_size": 50048,
  "sequence_length": 16384,
  "training_objective": "Summarization + Semantic Labeling",
  "tokenizer": "SentencePiece",
  "training_dataset": "Kansas_Treaty_Corpus_v4",
  "ontology_alignment": ["CIDOC CRM", "PROV-O", "OWL-Time"]
}
```

---

## 🧠 Validation Metrics (`validation_metrics.json`)

```json
{
  "model_name": "gpt-5-treaty-sum",
  "version": "v5.2.0",
  "accuracy": 0.982,
  "precision": 0.978,
  "recall": 0.971,
  "f1_score": 0.973,
  "fair_score": 0.96,
  "care_score": 0.94,
  "checksum_integrity": true,
  "energy_wh": 21.5,
  "carbon_gco2e": 27.1,
  "validation_dataset": "Kansas_Treaty_Corpus_v4",
  "validated_by": "@kfm-validation",
  "status": "validated"
}
```

---

## 🔋 Sustainability Profile (`energy_profile.json`)

```json
{
  "hardware": "NVIDIA A100 (40GB) GPU Cluster",
  "training_time_hours": 6.5,
  "avg_energy_wh_per_epoch": 3.6,
  "total_energy_wh": 21.5,
  "carbon_gco2e": 27.1,
  "renewable_energy_ratio": 1.0,
  "iso_50001_verified": true,
  "carbon_offset_certified": "ISO 14064",
  "audited_by": "@kfm-sustainability"
}
```

---

## 🔗 Provenance Record (`provenance_links.jsonld`)

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "crm": "http://www.cidoc-crm.org/cidoc-crm/",
    "fair": "https://purl.org/fair/",
    "time": "http://www.w3.org/2006/time#"
  },
  "@id": "prov:gpt-5-treaty-sum_v5.2.0_checkpoint",
  "prov:wasGeneratedBy": "process:ai-training-run-2025-10-24",
  "prov:used": [
    "datasets/Kansas_Treaty_Corpus_v4",
    "configs/training_config_v5.json"
  ],
  "prov:generatedAtTime": "2025-10-24T17:10:00Z",
  "prov:qualifiedAttribution": {
    "prov:agent": "@kfm-ai",
    "prov:role": "model_trainer"
  },
  "crm:E5_Event": "AI Model Training Run (Treaty Summarization)",
  "crm:E52_Time-Span": "2025-10-23T09:00:00Z/2025-10-24T17:00:00Z",
  "fair:ledger_hash": "c3a7f1b9d8..."
}
```

---

## 🧩 Lifecycle Workflow

```mermaid
flowchart TD
    A[Dataset: Kansas Treaty Corpus v4] --> B[Fine-Tuning Pipeline (GPT-5 v5.2.0)]
    B --> C[Checkpoint Saved]
    C --> D[Validation & FAIR+CARE Audit]
    D --> E[Governance Ledger Registration]
    E --> F[Model Registry Update]
```

---

## 📈 Performance Metrics Summary

| Metric | Target | Current | Status |
| :------ | :------ | :------ | :------ |
| `accuracy` | ≥ 0.97 | 0.982 | ✅ |
| `f1_score` | ≥ 0.95 | 0.973 | ✅ |
| `fair_score` | ≥ 0.9 | 0.96 | ✅ |
| `care_score` | ≥ 0.9 | 0.94 | ✅ |
| `energy_wh` | ≤ 25 | 21.5 | ✅ |
| `carbon_gco2e` | ≤ 30 | 27.1 | ✅ |
| `checksum_integrity` | 100% | 100% | ✅ |

---

## ✅ Compliance Matrix

| Standard | Domain | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | Ethical model documentation | ✅ |
| **MCP-DL v6.4.3** | Documentation & schema validation | ✅ |
| **CIDOC CRM / PROV-O / OWL-Time** | Ontology alignment | ✅ |
| **ISO 9001 / 27001** | Quality + security governance | ✅ |
| **ISO 50001 / 14064** | Energy + carbon sustainability | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Added GPT-5 Treaty Summarization Model Checkpoint v5.2.0 with FAIR+CARE, ontology, and sustainability validation. | @kfm-ai |

---

<div align="center">

[![Model Checkpoint](https://img.shields.io/badge/AI--Model-GPT--5%20Treaty%20Sum%20v5.2.0-6f42c1?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Validated-2ecc71?style=flat-square)]()
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O%20%7C%20OWL--Time-8a2be2?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Gold · AI Model Checkpoint
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/models/checkpoints/gpt-5-treaty-sum_v5.2.0/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
ISO-ALIGNED: true
PROVENANCE-LINKED: true
ONTOLOGY-VALIDATED: true
CHECKSUM-VERIFIED: true
GOVERNANCE-LEDGER-LINKED: true
ENERGY-AUDITED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->
