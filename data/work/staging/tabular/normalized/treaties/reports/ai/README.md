---
title: "🤖 Kansas Frontier Matrix — Treaty Reports AI Module"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Continuous / Autonomous"
status: "Active · FAIR+CARE+ISO Compliant"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-ai", "@kfm-data", "@kfm-treaties"]
approvers: ["@kfm-architecture", "@kfm-ethics"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - STAC / DCAT
  - CIDOC CRM / PROV-O / OWL-Time
  - ISO 50001 / 14064 / 27001
tags: ["ai","treaties","reports","nlp","summarization","ner","provenance","cidoc","owl-time","semantic-validation"]
---

<div align="center">

# 🤖 Kansas Frontier Matrix — **AI-Generated Treaty Reports**
`data/work/staging/tabular/normalized/treaties/reports/ai/README.md`

**Purpose:** Document the AI-assisted report generation pipeline for **normalized treaty datasets**, providing automated summaries, entity linking, semantic validation, and focus-mode integration.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![AI Pipeline](https://img.shields.io/badge/AI-Pipeline%20Validated-6f42c1)]()
[![License](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-green)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71)]()

</div>

---

## 📚 Overview

This module generates **AI-enriched analytical reports** derived from **normalized treaty data** located in  
`data/work/staging/tabular/normalized/treaties/`.  
Outputs provide entity-level insights, structured summaries, and semantic annotations aligned with the **CIDOC CRM** ontology and **OWL-Time** temporal logic.

**Primary goals**
- Generate reproducible summaries of treaties and associated entities.
- Apply Named Entity Recognition (NER) and contextual linking to the knowledge graph.
- Produce markdown and JSON reports that integrate with the Focus Mode UI.
- Preserve full provenance and validation metadata in `reports/self-validation/*.json`.

---

## 🧠 AI Submodules

| Submodule | Function | Output Format | Status |
| :--------- | :-------- | :------------- | :------ |
| `summarizer.py` | Large-context treaty summarization (LLM-based) | `.md`, `.json` | ✅ Active |
| `ner_extractor.py` | Named Entity Recognition (people, places, events) | `.csv`, `.json` | ✅ Active |
| `provenance_builder.py` | PROV-O compatible provenance graph | `.jsonld` | ⚙ In Development |
| `semantic_validator.py` | Checks OWL-Time and CIDOC mappings | `.log`, `.json` | ✅ Stable |
| `focus_indexer.py` | Generates Focus Mode indices (entity-to-report map) | `.json` | ✅ Active |

---

## 🧩 Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/ai/
├── outputs/                  # Generated AI reports (.md, .json)
├── logs/                     # Process logs and validation summaries
├── prompts/                  # Reusable AI prompt templates
├── models/                   # Configs for transformer/LLM backends
├── provenance/               # JSON-LD provenance metadata
└── validation/               # AI validation reports
```

---

## 🧬 Workflow Summary

```mermaid
flowchart TD
    A[data/work/staging/tabular/normalized/treaties/*.csv] --> B[AI Inference Engine]
    B --> C[NER Extraction · spaCy / Transformers]
    B --> D[Summarization · LLM Pipeline]
    C --> E[Semantic Linking (Neo4j CIDOC Graph)]
    D --> F[Report Composer (Markdown + JSON)]
    E --> F
    F --> G[Validation & Provenance Records]
    G --> H[data/work/staging/tabular/normalized/treaties/reports/ai/outputs/]
```

---

## ⚙️ Configuration Parameters

| Parameter | Description | Default |
| :--------- | :------------ | :-------- |
| `MODEL_NAME` | Transformer or LLM model used for summaries | `gpt-5-treaty-sum` |
| `MAX_TOKENS` | Max output tokens per document | `4096` |
| `NER_MODEL` | spaCy model for entity extraction | `en_core_web_trf` |
| `GRAPH_ENDPOINT` | Neo4j instance for CIDOC linking | `bolt://localhost:7687` |
| `VALIDATION_MODE` | Enable/disable semantic validation | `True` |

---

## 🔐 Data Integrity & Provenance

- All generated reports reference their **source treaty record** via  
  `:Fact -[:DERIVED_FROM]-> :Source`.
- JSON-LD provenance conforms to **PROV-O** and **CIDOC CRM**.  
- Validation logs in `validation/` must pass with **0 critical errors**.  
- Each run produces SHA-256 checksums and timestamps in `logs/manifest.json`.

---

## 🧪 Testing & Validation

| Test Type | Description | Tool |
| :--------- | :------------ | :---- |
| Unit | AI submodule integrity | pytest |
| Semantic | CIDOC/OWL-Time graph compliance | cypher-lint |
| Provenance | JSON-LD validation | pyshacl |
| Focus Mode | Response schema tests | schemathesis |
| Performance | Token efficiency + runtime | custom metrics script |

---

## 📈 Output Formats

| Format | Description | Consumer |
| :------ | :----------- | :-------- |
| `.md` | Human-readable AI report | GitHub / Docs |
| `.json` | Structured AI output | API / Focus Mode |
| `.jsonld` | Provenance data | Neo4j / FAIR ledger |
| `.log` | Validation log | CI/CD pipeline |

---

## ✅ Compliance Matrix

| Standard | Area | Status |
| :-------- | :----- | :------ |
| **FAIR / CARE** | Data ethics + openness | ✅ Compliant |
| **MCP-DL v6.4.3** | Documentation standard | ✅ Validated |
| **CIDOC CRM / OWL-Time** | Semantic model | ✅ Verified |
| **PROV-O** | Provenance structure | ✅ Linked |
| **ISO 27001** | Security baseline | ✅ Passed |
| **ISO 50001 / 14064** | Energy & carbon metrics | ✅ Logged |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Initial AI treaty reporting module added to staging workflows. | @kfm-ai |

---

<div align="center">

[![AI Module](https://img.shields.io/badge/AI--Module-Treaty%20Reports-6f42c1?style=flat-square)]()
[![Semantic Graph](https://img.shields.io/badge/Semantics-CIDOC%20CRM%20%7C%20OWL--Time-229954?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Validated-2ecc71?style=flat-square)]()
[![Security](https://img.shields.io/badge/Security-SHA256%20Verified-008b8b?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · AI Integration
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/README.md
MCP-CERTIFIED: true
AI-MODULE: true
FAIR-CARE-COMPLIANT: true
PROVENANCE-LINKED: true
SEMANTIC-VALIDATED: true
SUSTAINABILITY-LOGGED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->