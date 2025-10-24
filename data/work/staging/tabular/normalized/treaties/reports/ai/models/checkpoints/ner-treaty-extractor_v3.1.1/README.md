---
title: "🧩 Kansas Frontier Matrix — NER Treaty Extractor Model Checkpoint v3.1.1"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/models/checkpoints/ner-treaty-extractor_v3.1.1/README.md"
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
tags: ["ai","model","checkpoint","ner","entity-extraction","validation","ontology","fair","iso","provenance"]
---

<div align="center">

# 🧩 Kansas Frontier Matrix — **NER Treaty Extractor Model Checkpoint v3.1.1**
`data/work/staging/tabular/normalized/treaties/reports/ai/models/checkpoints/ner-treaty-extractor_v3.1.1/`

**Purpose:** Archive and document the **NER Treaty Extractor v3.1.1** checkpoint used to identify and classify named entities (people, places, events, organizations) in treaty datasets — validated under FAIR+CARE, CIDOC CRM, and ISO sustainability standards.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![NER Model](https://img.shields.io/badge/AI--Model-NER%20Treaty%20Extractor%20v3.1.1-6f42c1)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Validated-2ecc71)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-d4af37)]()

</div>

---

## 📚 Overview

The **NER Treaty Extractor** model is responsible for **Named Entity Recognition (NER)** and classification of key entities from historical treaty corpora.  
This model was trained on **annotated treaty texts (Kansas Treaty Corpus v3)** and fine-tuned for:
- **People (E21_Person)**  
- **Places (E53_Place)**  
- **Events (E5_Event)**  
- **Organizations (E74_Group)**  

The v3.1.1 checkpoint is optimized for **high-accuracy entity recognition** and ontology mapping to **CIDOC CRM** and **PROV-O** classes.

> 🧩 *This checkpoint is part of the KFM AI entity-extraction subsystem and feeds directly into the Knowledge Graph ingestion pipelines.*

---

## 🗂️ Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/models/checkpoints/ner-treaty-extractor_v3.1.1/
├── checkpoint_2025-10-22.json
├── weights.bin
├── config.json
├── validation_metrics.json
└── provenance_links.jsonld
```

---

## 🧩 Example Checkpoint Metadata (`checkpoint_2025-10-22.json`)

```json
{
  "model_name": "ner-treaty-extractor",
  "model_version": "v3.1.1",
  "checkpoint_id": "chkpt-2025-10-22-001",
  "timestamp": "2025-10-22T16:45:00Z",
  "accuracy": 0.974,
  "f1_score": 0.968,
  "precision": 0.971,
  "recall": 0.965,
  "dataset_ref": "Kansas_Treaty_Corpus_v3_Annotated",
  "optimizer": "AdamW",
  "learning_rate": 0.00003,
  "epochs_completed": 8,
  "entity_types": ["Person", "Place", "Event", "Organization"],
  "ontology_alignment": ["CIDOC CRM", "PROV-O"],
  "fair_score": 0.95,
  "care_score": 0.93,
  "energy_wh": 19.8,
  "carbon_gco2e": 25.4,
  "checksum_sha256": "b3e9f2c74a1...",
  "governance_hash": "d4a6b1f9c8..."
}
```

---

## ⚙️ Model Configuration (`config.json`)

```json
{
  "architecture": "Transformer Encoder (NER-Fine-Tuned)",
  "base_model": "bert-large-cased",
  "embedding_dim": 1024,
  "num_layers": 24,
  "sequence_length": 512,
  "dropout_rate": 0.1,
  "training_dataset": "Kansas_Treaty_Corpus_v3_Annotated",
  "tokenizer": "WordPiece",
  "ontology_alignment": ["CIDOC CRM", "PROV-O"]
}
```

---

## 🧠 Validation Metrics (`validation_metrics.json`)

```json
{
  "model_name": "ner-treaty-extractor",
  "version": "v3.1.1",
  "accuracy": 0.974,
  "precision": 0.971,
  "recall": 0.965,
  "f1_score": 0.968,
  "entity_coverage_rate": 0.99,
  "checksum_integrity": true,
  "fair_score": 0.95,
  "care_score": 0.93,
  "energy_wh": 19.8,
  "carbon_gco2e": 25.4,
  "validated_by": "@kfm-validation",
  "status": "validated"
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
  "@id": "prov:ner-treaty-extractor_v3.1.1_checkpoint",
  "prov:wasGeneratedBy": "process:ai-ner-training-pipeline-v3.1.1",
  "prov:used": [
    "datasets/Kansas_Treaty_Corpus_v3_Annotated",
    "configs/ner_training_config_v3.json"
  ],
  "prov:generatedAtTime": "2025-10-22T16:45:00Z",
  "prov:qualifiedAttribution": {
    "prov:agent": "@kfm-ai",
    "prov:role": "model_trainer"
  },
  "crm:E5_Event": "NER Model Training Run (Treaty Entity Extraction)",
  "crm:E52_Time-Span": "2025-10-21T08:00:00Z/2025-10-22T16:00:00Z",
  "fair:ledger_hash": "d4a6b1f9c8..."
}
```

---

## 🧩 Lifecycle Workflow

```mermaid
flowchart TD
    A[Kansas Treaty Corpus v3 Annotated] --> B[NER Training Pipeline v3.1.1]
    B --> C[Model Checkpoint Saved]
    C --> D[Validation & FAIR+CARE Audit]
    D --> E[Governance Ledger Sync]
    E --> F[Model Registry Update]
```

---

## 📈 Performance Metrics Summary

| Metric | Target | Current | Status |
| :------ | :------ | :------ | :------ |
| `accuracy` | ≥ 0.95 | 0.974 | ✅ |
| `f1_score` | ≥ 0.93 | 0.968 | ✅ |
| `entity_coverage_rate` | ≥ 0.95 | 0.99 | ✅ |
| `fair_score` | ≥ 0.9 | 0.95 | ✅ |
| `care_score` | ≥ 0.9 | 0.93 | ✅ |
| `energy_wh` | ≤ 25 | 19.8 | ✅ |
| `carbon_gco2e` | ≤ 30 | 25.4 | ✅ |

---

## ✅ Compliance Matrix

| Standard | Domain | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | Ethical model validation & transparency | ✅ |
| **MCP-DL v6.4.3** | Model documentation & schema adherence | ✅ |
| **CIDOC CRM / PROV-O / OWL-Time** | Semantic and provenance alignment | ✅ |
| **ISO 9001 / 27001** | Quality + security governance | ✅ |
| **ISO 50001 / 14064** | Energy + carbon accountability | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Added NER Treaty Extractor v3.1.1 checkpoint with FAIR+CARE validation and provenance metadata. | @kfm-ai |

---

<div align="center">

[![NER Model](https://img.shields.io/badge/AI--Model-NER%20Treaty%20Extractor%20v3.1.1-6f42c1?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Validated-2ecc71?style=flat-square)]()
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O-8a2be2?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-d4af37?style=flat-square)]()

</div>

---

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Gold · AI Model Checkpoint
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/models/checkpoints/ner-treaty-extractor_v3.1.1/README.md
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
