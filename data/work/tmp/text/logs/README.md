<div align="center">

# 🧾 Kansas Frontier Matrix — **Text ETL Logs**  
`data/work/tmp/text/logs/`

**Mission:** Maintain **transparent, traceable, and reproducible logs** for all text-processing stages —  
including OCR extraction, NLP entity recognition, summarization, and quality validation —  
across the **Kansas Frontier Matrix (KFM)** pipeline ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Text ETL Logs (data/work/tmp/text/logs/)"
version: "v1.3.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-nlp"]
tags: ["logs","etl","nlp","ocr","summarization","validation","mcp","ci-cd"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - FAIR Principles (Transparent Experimentation)
  - UTF-8 Plain Text · JSON · JSONL Open Standards
---
```

---

## 📚 Overview

The `data/work/tmp/text/logs/` directory is the **temporary logging workspace** for **text ETL and NLP** operations in KFM.  
Every stage — from **OCR** to **tokenization**, **NER**, **summarization**, and **schema validation** — is recorded here to ensure **auditability** and **reproducibility**.

**Captured operations include:**
- 📰 **OCR extraction** from historical scans or documents  
- 🧠 **NLP pipelines** (tokenization, embeddings, NER, summarization)  
- 🧩 **Checksums & schema tests** for text layer compliance  
- 🧾 **QA/QC events** (normalization, language detection, error traces)

Logs are **ephemeral** (auto-regenerated per run) and **purged** on cleanup cycles.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/text/logs/
├── README.md
├── text_etl_debug.log          # High-level pipeline trace
├── ocr_processing_report.log   # OCR + page confidence + corrections
├── nlp_entity_extraction.log   # NER results + confidence + counts
├── summarization_audit.log     # Summaries + references (redacted indices)
└── text_checksum_audit.log     # SHA-256 + schema checks + file diffs
```

> **Note:** Files are overwritten or rotated per run; naming follows domain prefixes (`ocr_`, `nlp_`, `summary_`, `checksum_`) for clarity.

---

## ⚙️ Logging Framework

KFM uses **Python `logging`** with structured formatters and rotation for **human-readable** and **machine-parsable** records.

### 🔧 Example YAML Config

```yaml
version: 1
formatters:
  default:
    format: "%(asctime)s — %(levelname)s — %(name)s — %(message)s"
handlers:
  file_debug:
    class: logging.handlers.RotatingFileHandler
    filename: data/work/tmp/text/logs/text_etl_debug.log
    maxBytes: 1048576  # 1 MB
    backupCount: 3
    encoding: utf-8
    formatter: default
loggers:
  kfm.text:
    level: INFO
    handlers: [file_debug]
    propagate: no
root:
  level: WARNING
  handlers: [file_debug]
```

### 🐍 Minimal Python Snippet

```python
import logging, logging.config, json, time
logging.config.dictConfig(json.load(open("config/logging_text.yaml")))
log = logging.getLogger("kfm.text")

log.info("ETL start | pipeline=text | run_id=2025-10-16T12:01:02Z")
# ... OCR/NLP steps
log.warning("low_confidence_ocr | page=12 | conf=0.63 | doc=ks_daily_1897_05_14.pdf")
log.error("schema_violation | file=entities.jsonl | field=offset | reason=missing")
log.info("ETL end | duration=142.8s | status=SUCCESS")
```

---

## 🧾 Log Types & Purposes

| Log Type                        | Description                                                                                 |
| :------------------------------ | :------------------------------------------------------------------------------------------ |
| **`*_etl_debug.log`**           | End-to-end process trace: inputs, steps, timings, success/fail states.                      |
| **`*_ocr_processing*.log`**     | OCR engine, languages, page confidence, correction rules, error pages.                      |
| **`*_entity_extraction*.log`**  | Entities with counts and confidence summaries (values/anonymized where appropriate).        |
| **`*_summarization_audit*.log`**| Summary references (IDs), length, model name, temperature, quality checks.                  |
| **`*_checksum_audit*.log`**     | SHA-256 hashes, diffs against prior runs, schema validation outcomes.                       |

**Encoding:** All logs are **UTF-8** plain text and newline-terminated.

---

## 🧩 Standard Line Schema

For grep-ability and machine parsing, each log line SHOULD follow:

```text
[timestamp] [LEVEL] [component] key1=val1 key2=val2 ... message="free text"
```

**Example:**

```text
2025-10-16T12:08:13Z INFO text.ocr page=12 conf=0.63 lang="eng" message="ocr low confidence"
2025-10-16T12:09:54Z INFO text.ner doc_id="ks-1897-05-14" persons=18 places=7 events=2 message="ner pass"
```

---

## 🧪 Log Levels

| Level     | Purpose                               | Typical Events                                  |
| :-------- | :------------------------------------ | :---------------------------------------------- |
| **DEBUG** | Developer trace                       | Token ranges, span offsets, timings             |
| **INFO**  | Normal operation                      | Stage start/end, counts, summaries              |
| **WARNING** | Non-fatal anomalies                 | Low OCR conf, partial schema, retries           |
| **ERROR** | Recoverable failure                   | File not found, schema violation, bad encodings |
| **CRITICAL** | Pipeline abort                     | Corrupted inputs, fatal dependency failure      |

---

## 🔒 Security & Privacy

| Category             | Policy                                                                 |
| :------------------- | :--------------------------------------------------------------------- |
| **Sensitive Data**   | Logs **MUST NOT** include PII, secrets, or full raw content dumps.     |
| **Access Scope**     | Local-only; excluded from repo via `.gitignore`.                       |
| **Retention**        | Purged on run start or scheduled cleanup; max age default **7 days**.  |
| **Anonymization**    | Use hashed or ID-linked references for example payloads where needed.  |

---

## 🧩 Lifecycle & Commands

**Makefile Targets**

```bash
# Run text ETL + emit logs
make text

# Purge logs (rotation + cleanup)
make clean-logs
```

**Direct Invocation**

```bash
python src/pipelines/text/text_pipeline.py \
  --log data/work/tmp/text/logs/text_etl_debug.log
```

**Lifecycle**

1. Initialize log with run metadata (pipeline ID, commit SHA, env hash).  
2. Append structured entries per stage (OCR → clean → NER → summarize → validate).  
3. Flag anomalies via `WARNING`/`ERROR`.  
4. Summarize counts, duration, and status (`SUCCESS`/`FAIL`).  
5. Auto-rotate and purge per retention policy.

---

## 🧰 CI/CD & Pipeline Integration

| Linked Component                      | Purpose                                                   |
| :------------------------------------ | :-------------------------------------------------------- |
| `src/pipelines/text/text_pipeline.py` | Generates and manages log files for ETL/NLP runs.         |
| `.github/workflows/*.yml`            | Consumes logs for validation error context and reporting. |
| `data/work/tmp/text/`                 | Parent sandbox for transient text outputs.                |
| `data/processed/text/`                | Final cleaned text datasets and derived summaries.        |
| `data/checksums/text/`                | SHA-256 integrity manifests for published artifacts.      |
| `data/processed/metadata/text/`       | Persistent STAC metadata for provenance.                  |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                          |
| :---------------------- | :---------------------------------------------------------------------- |
| **Documentation-first** | README documents purpose, format, lifecycle, and retention policies.    |
| **Reproducibility**     | Logs deterministically capture ETL/NLP actions & outcomes.              |
| **Open Standards**      | UTF-8 text lines; optional JSON/JSONL adjuncts for structured outputs.  |
| **Provenance**          | Each log ties to pipeline ID, dataset IDs, and commit SHA.              |
| **Auditability**        | Clear, searchable trace enhances QA and test reproducibility.           |

---

## 📎 Related Directories

| Path                            | Description                                               |
| :------------------------------ | :-------------------------------------------------------- |
| `data/work/tmp/text/`           | Temporary sandbox for text ETL and NLP intermediates.     |
| `data/processed/text/`          | Final structured text datasets and summaries.             |
| `data/checksums/text/`          | SHA-256 checksum manifests ensuring reproducibility.      |
| `data/processed/metadata/text/` | STAC metadata for text assets and lineage.                |

---

## 📅 Version History

| Version  | Date       | Summary                                                                                |
| :------- | :--------- | :------------------------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial documentation for text ETL and NLP logs.                                       |
| **v1.1.0** | 2025-10-09 | Added schema compliance notes and STAC integration references.                         |
| **v1.3.0** | 2025-10-16 | Alignment pass: YAML front matter, standard line schema, rotation, privacy policies.   |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Word Accounted For. Every Step Logged.”*  
📍 [`data/work/tmp/text/logs/`](.) · Temporary ETL & NLP logging workspace for text pipelines and audit transparency.

</div>
