<div align="center">

# 📜 Kansas Frontier Matrix — Temporary Text Workspace  
`data/work/tmp/text/`

**Mission:** Provide a **temporary workspace** for intermediate and experimental text datasets —  
including OCR outputs, transcript fragments, tokenized corpora, and NLP feature extractions —  
used during ETL, validation, and analysis in the Kansas Frontier Matrix (KFM).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/text/` directory serves as a **sandbox environment**  
for handling intermediate textual artifacts during ETL and NLP pipeline execution.  

These temporary files may include:

- OCR-processed raw text fragments (e.g., from scanned newspapers)  
- Tokenized or vectorized text data for machine learning models  
- Intermediate JSONL exports of named entities or summaries  
- Pre-cleaned transcripts and temporary embeddings  

All files are **ephemeral**, **excluded from version control**, and **safe to delete** —  
they are fully **reproducible** through deterministic ETL and NLP pipelines (`make text`).

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
````

> **Note:** Example files shown above are placeholders;
> actual contents depend on active ETL or NLP processing tasks.

---

## ⚙️ Usage Guidelines

| Policy                    | Description                                                         |
| :------------------------ | :------------------------------------------------------------------ |
| **Ephemeral Storage**     | Files here are transient and automatically purged.                  |
| **Regenerable Artifacts** | All text artifacts are reproducible via ETL or NLP scripts.         |
| **CI/CD Exclusion**       | Directory ignored by automated builds except for debug diagnostics. |
| **Open Formats**          | Use only open formats (TXT, JSON, JSONL, CSV).                      |
| **Data Sensitivity**      | Do **not** store personally identifiable or restricted content.     |

---

## ⚙️ Typical Use Cases

| Task                         | Example                                                    |
| :--------------------------- | :--------------------------------------------------------- |
| **OCR Testing**              | Generate partial OCR output from scanned PDFs.             |
| **Entity Extraction**        | Store JSONL exports of NER results before graph ingestion. |
| **Text Cleaning Validation** | Preview tokenization or normalization results.             |
| **Summarization QA**         | Validate AI-generated summaries of historical archives.    |
| **Checksum Verification**    | Compare processed text with existing SHA-256 records.      |

---

## 🧹 Cleanup Policy

This directory is **automatically cleared** during scheduled maintenance or at the start of new ETL runs.

**Makefile Target**

```bash
make clean-tmp
```

**Manual Command**

```bash
rm -rf data/work/tmp/text/*
```

Permanent and validated datasets are stored in:

* `data/processed/text/` — Final cleaned and structured text datasets
* `data/checksums/text/` — SHA-256 integrity validation files
* `data/processed/metadata/text/` — STAC-compliant metadata and documentation

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                   |
| :---------------------- | :--------------------------------------------------------------- |
| **Documentation-first** | README defines structure, policy, and reproducibility.           |
| **Reproducibility**     | All text files regenerable deterministically via ETL/NLP.        |
| **Open Standards**      | UTF-8, JSON, and JSONL ensure interoperability.                  |
| **Provenance**          | Temporary files align with logged ETL/NLP stages.                |
| **Auditability**        | Logs and intermediates maintain traceable lineage until cleanup. |

---

## 📎 Related Directories

| Path                            | Description                                                |
| :------------------------------ | :--------------------------------------------------------- |
| `data/processed/text/`          | Final cleaned text datasets (OCR, transcripts, summaries). |
| `data/checksums/text/`          | SHA-256 hashes ensuring text data integrity.               |
| `data/processed/metadata/text/` | STAC metadata entries for text datasets.                   |
| `data/work/tmp/`                | Root workspace for all ETL and validation subdomains.      |

---

## 📅 Version History

| Version    | Date       | Summary                                                                |
| :--------- | :--------- | :--------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial documentation of temporary text workspace (ETL + NLP sandbox). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Where Words Become Data — and Every Byte Is Accounted For.”*
📍 [`data/work/tmp/text/`](.) · Temporary workspace for text ETL, NLP, and QA validation.

</div>
