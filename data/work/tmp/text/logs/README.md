<div align="center">

# 🧾 Kansas Frontier Matrix — Text ETL Logs  
`data/work/tmp/text/logs/`

**Mission:** Store **temporary ETL and NLP process logs** generated during text extraction, cleaning, entity recognition,  
and QA/QC workflows — enabling transparency and traceability throughout the Kansas Frontier Matrix (KFM)  
text and document processing pipelines.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/badge/container-scan-informational)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/text/logs/` directory temporarily stores **pipeline logs**  
created during ETL and natural language processing (NLP) operations.  

These logs document:
- OCR extraction, cleaning, and normalization steps  
- NLP processes such as tokenization, summarization, and entity extraction  
- Validation reports for text quality and schema conformity  
- Metadata and checksum verification events  

Logs are **ephemeral** — automatically generated and deleted during ETL runs —  
but ensure full transparency in the transformation of textual data from raw source to structured output.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/text/logs/
├── README.md
├── text_etl_debug.log
├── ocr_processing_report.log
├── nlp_entity_extraction.log
└── text_checksum_audit.log
````

> **Note:** Log filenames and content vary by active ETL task or NLP stage.
> Logs are overwritten or regenerated with each run for reproducibility.

---

## ⚙️ Logging Guidelines

| Log Type                      | Purpose                                                                                 |
| :---------------------------- | :-------------------------------------------------------------------------------------- |
| **`*_etl_debug.log`**         | Captures high-level ETL process details including file I/O and transformation sequence. |
| **`*_processing_report.log`** | Summarizes OCR, text normalization, and cleaning steps.                                 |
| **`*_entity_extraction.log`** | Lists identified entities (people, places, events) and their confidence levels.         |
| **`*_checksum_audit.log`**    | Records validation results from hash verification and schema tests.                     |

All logs use **UTF-8 plain-text format** for portability and open review across systems.

---

## ⚙️ Log Management Workflow

Logs are generated automatically by KFM’s text ETL pipeline.

**Makefile target:**

```bash
make text
```

**Python command:**

```bash
python src/pipelines/text/text_pipeline.py --log data/work/tmp/text/logs/text_etl_debug.log
```

**Lifecycle:**

1. Pipeline initializes → log file created or overwritten.
2. Each OCR, NLP, or checksum step appends output and diagnostics.
3. Logs are inspected for debugging or QA validation.
4. Logs are purged automatically during cleanup or rebuild.

---

## 🧹 Cleanup Policy

This directory is cleaned automatically during maintenance or at the start of new ETL runs.

**Makefile target:**

```bash
make clean-logs
```

**Manual cleanup:**

```bash
rm -rf data/work/tmp/text/logs/*
```

Permanent files and validated metadata reside in:

* `data/processed/text/` — Final structured text datasets
* `data/checksums/text/` — Integrity hashes for reproducibility
* `data/processed/metadata/text/` — STAC metadata for text and document assets

---

## 🧩 Integration with Pipelines

| Linked Component                      | Function                                               |
| :------------------------------------ | :----------------------------------------------------- |
| `src/pipelines/text/text_pipeline.py` | Generates ETL and NLP logs during pipeline execution.  |
| `.github/workflows/stac-validate.yml` | Uses logs for checksum and schema diagnostics.         |
| `data/work/tmp/text/`                 | Parent temporary workspace for text ETL intermediates. |
| `data/processed/text/`                | Final cleaned and validated text outputs.              |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                      |
| :---------------------- | :------------------------------------------------------------------ |
| **Documentation-first** | README defines logging structure, lifecycle, and cleanup.           |
| **Reproducibility**     | Logs capture deterministic ETL and NLP steps for traceability.      |
| **Open Standards**      | Logs stored as UTF-8 text files; fully platform-agnostic.           |
| **Provenance**          | Each log traces the lineage of text transformations and metadata.   |
| **Auditability**        | Logs provide transparent records for debugging, QA, and validation. |

---

## 📎 Related Directories

| Path                            | Description                                         |
| :------------------------------ | :-------------------------------------------------- |
| `data/work/tmp/text/`           | Temporary workspace for text ETL and NLP files.     |
| `data/processed/text/`          | Final processed text and transcript datasets.       |
| `data/checksums/text/`          | Integrity validation for text data reproducibility. |
| `data/processed/metadata/text/` | Metadata and STAC catalog for text assets.          |

---

## 📅 Version History

| Version | Date       | Summary                                                 |
| :------ | :--------- | :------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial creation of text ETL and NLP log documentation. |
| v1.0.1  | 2025-10-09 | Added YAML metadata, JSON-LD schema, and MCP badges.    |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Word Accounted For. Every Step Logged.”*
📍 [`data/work/tmp/text/logs/`](.) · Temporary ETL & NLP logging workspace for textual datasets.

</div>
