<div align="center">

# 📜 Kansas Frontier Matrix — **Temporary Text Workspace**  
`data/work/tmp/text/`

**Mission:** Provide a **short-term sandbox** for intermediate and experimental text artifacts —  
including OCR fragments, NLP outputs, tokenized corpora, and transcript previews —  
supporting ETL, validation, and AI-assisted analysis across the **Kansas Frontier Matrix (KFM)** ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Temporary Text Workspace (data/work/tmp/text/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-nlp"]
tags: ["text","tmp","nlp","ocr","summarization","mcp","ai","etl","validation"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - FAIR Principles (Transparent Experimentation)
  - UTF-8, JSON, JSONL Open Text Standards
---
```

---

## 📚 Overview

The `data/work/tmp/text/` directory is a **temporary NLP and text-processing workspace**,  
dedicated to **short-lived, reproducible artifacts** generated during OCR, NER,  
summarization, or model-training phases of the **Kansas Frontier Matrix** project.

It enables **debugging, quality assurance**, and **pipeline testing** without persisting  
unstable or unvalidated content into version control.

**Common temporary artifacts include:**
- 📰 OCR-extracted text fragments from historical archives.  
- 🧠 Tokenized corpora or embeddings for NLP models.  
- 🧩 Named Entity Recognition (NER) or summarization JSONL exports.  
- 💬 Intermediate cleaned transcripts or AI summaries.  

All contents are **ephemeral**, **ignored by Git**, and **reproducible**  
via deterministic Make or ETL targets (`make text`).

---

## 🗂️ Directory Layout

```bash
data/work/tmp/text/
├── README.md
├── ocr_extract_sample.txt
├── nlp_entities_preview.jsonl
├── transcript_snippet.json
└── logs/
    └── text_etl_debug.log
```

> Each file in this directory represents a transient stage of data transformation,  
> facilitating inspection and debugging prior to final ingestion into `data/processed/text/`.

---

## ⚙️ Usage & Governance

| Policy                         | Description                                                                 |
| :----------------------------- | :-------------------------------------------------------------------------- |
| **Ephemeral Storage**          | Files are temporary and subject to automatic or manual cleanup.             |
| **Reproducible Artifacts**     | Every file must be regenerable via text ETL or NLP pipeline scripts.        |
| **CI/CD Exclusion**            | Ignored in validation jobs unless explicitly referenced for testing.        |
| **Open Standards**             | Use only open, UTF-8 formats (TXT, JSON, JSONL, CSV).                      |
| **No Sensitive Data**          | Do not store restricted or personal content.                               |
| **Naming Convention**          | Prefix files with pipeline step and date (e.g., `ocr_2025-10-16_stage1.txt`). |

---

## 🧩 Typical Use Cases

| Task                     | Example Output                                               |
| :----------------------- | :----------------------------------------------------------- |
| **OCR Testing**          | Extracted text fragments for OCR quality control.            |
| **Entity Extraction**    | JSONL files containing NER tags for validation.              |
| **Text Cleaning QA**     | Tokenization and normalization results pre-publication.      |
| **Summarization Review** | Generated summaries compared against source documents.       |
| **Embedding Validation** | Intermediate vectors prior to Neo4j or ML model ingestion.   |

---

## 🧹 Cleanup Policy

Temporary files are routinely deleted before new ETL/NLP runs or at scheduled CI maintenance cycles.  
All outputs can be **recreated** from upstream workflows.

### Automated Cleanup

```bash
make clean-tmp
```

### Manual Cleanup

```bash
rm -rf data/work/tmp/text/*
```

> Logs older than **7 days** are auto-purged by CI.  
> All text data can be regenerated from inputs under `data/processed/text/`.

---

## 🧰 Integration with ETL, NLP & CI/CD

| Component                             | Function                                                     |
| :------------------------------------ | :----------------------------------------------------------- |
| `src/pipelines/text_pipeline.py`      | Writes and cleans up intermediate NLP/OCR artifacts.          |
| `.github/workflows/stac-validate.yml` | May reference this workspace for testing and validation logs. |
| `data/work/logs/`                     | Stores ETL and NLP debug traces.                              |
| `data/processed/text/`                | Hosts validated and versioned textual datasets.               |
| `data/checksums/text/`                | Maintains SHA-256 verification for final text assets.         |
| `data/stac/text/`                     | Contains metadata lineage linking text datasets to source.    |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                                 |
| :---------------------- | :----------------------------------------------------------------------------- |
| **Documentation-first** | README defines purpose, governance, and regeneration protocols.               |
| **Reproducibility**     | Every temporary artifact regenerable via ETL/NLP pipelines.                   |
| **Open Standards**      | UTF-8 TXT, JSON, JSONL, CSV maintain transparency and portability.             |
| **Provenance**          | Domain mirrors final `data/processed/text/` lineage.                          |
| **Auditability**        | Debug logs and JSONL outputs preserved until cleanup.                         |

---

## 🧩 Best Practices

1. **Prefix by Type:** Use clear prefixes (`ocr_`, `nlp_`, `summary_`) for clarity.  
2. **Limit File Size:** Keep individual files ≤ 100 MB for efficient review and cleanup.  
3. **Automate Deletion:** Use `make clean-tmp` at the end of tests.  
4. **Log Operations:** Always record in `logs/text_etl_debug.log`.  
5. **Never Commit:** Verify `.gitignore` excludes transient text fragments.  

---

## 📎 Related Directories

| Path                            | Description                                               |
| :------------------------------ | :-------------------------------------------------------- |
| `data/processed/text/`          | Final structured and validated text datasets.             |
| `data/checksums/text/`          | SHA-256 integrity manifests for text layers.              |
| `data/processed/metadata/text/` | STAC metadata entries for text datasets.                  |
| `data/work/tmp/`                | Parent workspace for all transient domain subfolders.     |

---

## 📅 Version History

| Version    | Date       | Summary                                                                  |
| :--------- | :--------- | :----------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial documentation of temporary text workspace.                       |
| **v1.1.0** | 2025-10-10 | Added CI/CD integration and best practices for NLP staging.              |
| **v1.2.0** | 2025-10-16 | Alignment with MCP-DL v6.2 — standardized YAML, governance, and format.  |

---

<div align="center">

**Kansas Frontier Matrix** — *“Where Words Become Data — and Every Byte Is Accounted For.”*  
📍 [`data/work/tmp/text/`](.) · Temporary sandbox for OCR, NLP, and AI-driven text experimentation.

</div>
