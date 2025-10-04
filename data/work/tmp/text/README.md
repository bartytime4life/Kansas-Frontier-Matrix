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

These temporary files include:
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

> **Note:** Example files listed above are representative;
> actual contents depend on current ETL or NLP preprocessing tasks.

---

## ⚙️ Usage Guidelines

| Policy                    | Description                                                           |
| :------------------------ | :-------------------------------------------------------------------- |
| **Ephemeral Storage**     | Files are transient and automatically cleared.                        |
| **Regenerable Artifacts** | All text artifacts are reproducible via ETL/NLP scripts.              |
| **CI/CD Exclusion**       | This directory is ignored in automated builds except for diagnostics. |
| **Open Formats**          | Use open formats (TXT, JSON, JSONL, CSV) only.                        |
| **Data Sensitivity**      | Do not store personally identifiable or restricted content here.      |

---

## ⚙️ Typical Use Cases

| Task                         | Example                                                              |
| :--------------------------- | :------------------------------------------------------------------- |
| **OCR Testing**              | Generate partial OCR output from scanned newspaper PDFs.             |
| **Entity Extraction**        | Store temporary JSONL exports of NER results before graph ingestion. |
| **Text Cleaning Validation** | Preview normalization and tokenization results.                      |
| **Summarization QA**         | Validate AI-generated summaries for historical archives.             |
| **Checksum Verification**    | Validate processed text files against existing SHA-256 records.      |

---

## 🧹 Cleanup Policy

This directory is **automatically cleared** during cleanup operations or at the start of new ETL runs.

**Makefile target:**

```bash
make clean-tmp
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/text/*
```

Permanent and validated datasets are stored under:

* `data/processed/text/` — Final cleaned and structured text datasets
* `data/checksums/text/` — SHA-256 integrity validation files
* `data/processed/metadata/text/` — STAC-compliant metadata and documentation

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                        |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | README defines structure, policy, and reproducibility.                |
| **Reproducibility**     | All text files can be regenerated deterministically.                  |
| **Open Standards**      | UTF-8 plain text, JSON, and JSONL formats ensure interoperability.    |
| **Provenance**          | Temporary data correspond to logged ETL and NLP stages.               |
| **Auditability**        | Logs and intermediate files maintain traceable lineage until cleanup. |

---

## 📎 Related Directories

| Path                            | Description                                                     |
| :------------------------------ | :-------------------------------------------------------------- |
| `data/processed/text/`          | Final cleaned text datasets (OCR, transcripts, and summaries).  |
| `data/checksums/text/`          | SHA-256 hashes ensuring text data integrity.                    |
| `data/processed/metadata/text/` | Metadata and STAC entries for text datasets.                    |
| `data/work/tmp/`                | Root temporary workspace for all ETL and validation subdomains. |

---

## 📅 Version History

| Version | Date       | Summary                                                               |
| :------ | :--------- | :-------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial text temporary workspace documentation (ETL and NLP sandbox). |

---

<div align="center">

**Kansas Frontier Matrix** — *“Where Words Become Data — and Every Byte Is Accounted For.”*
📍 [`data/work/tmp/text/`](.) · Temporary workspace for text ETL, NLP, and QA validation.

</div>
