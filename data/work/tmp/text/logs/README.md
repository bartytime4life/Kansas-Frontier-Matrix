<div align="center">

# 🧾 Kansas Frontier Matrix — Text ETL Logs  
`data/work/tmp/text/logs/`

**Mission:** Maintain **transparent, traceable, and reproducible logs** for all text-processing stages —  
including OCR extraction, NLP entity recognition, summarization, and quality validation —  
across the Kansas Frontier Matrix (KFM) pipeline ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/text/logs/` directory is the **temporary logging workspace**  
for all **text ETL and NLP operations** within the Kansas Frontier Matrix.  

Each log entry contributes to **MCP-aligned transparency**, ensuring every step —  
from OCR extraction to NLP model inference — is recorded, traceable, and reproducible.

**Captured operations include:**
- 📰 **OCR extraction** from historical scans or documents  
- 🧠 **NLP processes** (tokenization, summarization, entity extraction)  
- 🧩 **Checksum & validation reports** for text schema compliance  
- 🧾 **QA/QC event logs** tracking content normalization and errors  

Logs are **ephemeral** but crucial for debugging, auditability, and QA reviews.  
They are regenerated automatically during ETL runs and purged upon pipeline completion.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/text/logs/
├── README.md
├── text_etl_debug.log
├── ocr_processing_report.log
├── nlp_entity_extraction.log
├── summarization_audit.log
└── text_checksum_audit.log
````

> **Note:** Log files are temporary, overwritten per run, and follow domain-based naming conventions
> (`ocr_`, `nlp_`, `summarization_`, `checksum_`, etc.) for clarity and traceability.

---

## ⚙️ Logging Framework

KFM pipelines use a modular logging system built with **Python’s `logging` library**
and extended handlers to write **human-readable and machine-parsable logs**.

**Configuration Example (YAML):**

```yaml
version: 1
formatters:
  default:
    format: "%(asctime)s — %(levelname)s — %(message)s"
handlers:
  file:
    class: logging.FileHandler
    filename: data/work/tmp/text/logs/text_etl_debug.log
    formatter: default
root:
  level: INFO
  handlers: [file]
```

Logs are emitted automatically from `src/pipelines/text/text_pipeline.py`
and linked to ETL run metadata (pipeline ID, timestamp, dataset, runtime).

---

## 🧾 Log Types & Purposes

| Log Type                        | Description                                                                           |
| :------------------------------ | :------------------------------------------------------------------------------------ |
| **`*_etl_debug.log`**           | Captures end-to-end ETL process flow, including file I/O and transformation sequence. |
| **`*_ocr_processing.log`**      | Details OCR operations, including error corrections and page confidence.              |
| **`*_entity_extraction.log`**   | Lists extracted entities (people, places, events) with model confidence scores.       |
| **`*_summarization_audit.log`** | Records summarization input-output pairs for AI explainability and QA.                |
| **`*_checksum_audit.log`**      | Contains hash validation, file comparison results, and schema test outcomes.          |

All logs use **UTF-8 plain text**, ensuring cross-platform accessibility and archiving compatibility.

---

## 🧩 Log Lifecycle

**Makefile Target:**

```bash
make text
```

**Python Invocation:**

```bash
python src/pipelines/text/text_pipeline.py --log data/work/tmp/text/logs/text_etl_debug.log
```

**Lifecycle Steps:**

1. Log file initialized with timestamp and pipeline metadata.
2. Each OCR/NLP stage appends structured log entries.
3. Errors or anomalies flagged with `WARNING` or `ERROR` levels.
4. Logs analyzed post-run for QA or during automated tests.
5. Old logs purged during cleanup cycles (`make clean-logs`).

---

## 🧹 Cleanup Policy

**Automatic Purge:**
Logs are removed at the start of every new ETL run or scheduled cleanup job.

**Makefile target:**

```bash
make clean-logs
```

**Manual Command:**

```bash
rm -rf data/work/tmp/text/logs/*
```

> Logs should not be preserved beyond active QA or validation sessions.
> Permanent metadata and audit trails are instead stored under `data/processed/metadata/text/`.

---

## 🧰 Integration with CI/CD and ETL Pipelines

| Linked Component                      | Purpose                                                   |
| :------------------------------------ | :-------------------------------------------------------- |
| `src/pipelines/text/text_pipeline.py` | Generates and manages log files for ETL/NLP runs.         |
| `.github/workflows/stac-validate.yml` | Consumes logs for validation and error context.           |
| `data/work/tmp/text/`                 | Parent workspace for transient text processing artifacts. |
| `data/processed/text/`                | Stores final cleaned text datasets.                       |
| `data/checksums/text/`                | Contains hash-based integrity validation records.         |
| `data/processed/metadata/text/`       | Maintains persistent STAC metadata for provenance.        |

---

## 🔒 Security & Privacy Considerations

| Category             | Policy                                                                  |
| :------------------- | :---------------------------------------------------------------------- |
| **Sensitive Data**   | Logs must exclude personal information or sensitive text fragments.     |
| **Access Control**   | Logs are local-only and excluded from repository commits.               |
| **Retention Period** | Logs persist only through the current pipeline cycle.                   |
| **Anonymization**    | Named entities (if logged) should use anonymized or hashed identifiers. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                          |
| :---------------------- | :---------------------------------------------------------------------- |
| **Documentation-first** | This README documents purpose, policies, and reproducibility of logs.   |
| **Reproducibility**     | Logs deterministically capture ETL/NLP actions and outcomes.            |
| **Open Standards**      | Logs written as UTF-8 text using standard logging schemas.              |
| **Provenance**          | Each log links transformations to pipeline steps and metadata.          |
| **Auditability**        | Provides clear traceability and transparency across all NLP operations. |

---

## 📎 Related Directories

| Path                            | Description                                           |
| :------------------------------ | :---------------------------------------------------- |
| `data/work/tmp/text/`           | Temporary sandbox for text ETL and NLP intermediates. |
| `data/processed/text/`          | Final structured text datasets and summaries.         |
| `data/checksums/text/`          | SHA-256 checksum manifests ensuring reproducibility.  |
| `data/processed/metadata/text/` | STAC-compliant metadata for text assets.              |

---

## 📅 Version History

| Version | Date       | Summary                                                                      |
| :------ | :--------- | :--------------------------------------------------------------------------- |
| v1.0.0  | 2025-10-04 | Initial documentation for text ETL and NLP logs.                             |
| v1.1.0  | 2025-10-09 | Added schema compliance notes and STAC integration references.               |
| v1.2.0  | 2025-10-10 | Upgraded YAML logging config, added privacy policy and lifecycle automation. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Word Accounted For. Every Step Logged.”*
📍 [`data/work/tmp/text/logs/`](.) · Temporary ETL & NLP logging workspace for text pipelines and audit transparency.

</div>
```
