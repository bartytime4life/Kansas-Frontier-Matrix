<div align="center">

# 📜 Kansas Frontier Matrix — Temporary Text Workspace  
`data/work/tmp/text/`

**Mission:** Provide a **short-term sandbox** for intermediate and experimental text artifacts —  
including OCR fragments, NLP outputs, tokenized corpora, and transcript previews —  
supporting ETL, validation, and AI-assisted analysis across the **Kansas Frontier Matrix (KFM)** ecosystem.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

The `data/work/tmp/text/` directory functions as a **temporary workspace** for managing  
intermediate textual outputs generated during KFM’s ETL and NLP pipelines.  
It allows for **debugging, quality assurance, and exploratory processing**  
without committing transient or experimental files to the repository.

**Typical artifacts include:**
- 📰 OCR-extracted raw text fragments from scanned archives  
- 🧠 Tokenized corpora and embeddings used for ML/NLP model input  
- 🧩 Named Entity Recognition (NER) or summarization JSONL exports  
- 💬 Intermediate cleaned transcripts or historical text samples  

All contents are **ephemeral**, **excluded from version control**, and **reproducible**  
through deterministic text-processing workflows (`make text`).

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

> **Note:** Example files shown above are placeholders only — actual files
> vary depending on active ETL or NLP processes.

---

## ⚙️ Usage & Governance

| Policy                         | Description                                                                |
| :----------------------------- | :------------------------------------------------------------------------- |
| **Ephemeral Storage**          | Files are temporary and subject to automatic or manual cleanup.            |
| **Regenerable Artifacts**      | Every text artifact must be reproducible via ETL or NLP pipeline.          |
| **CI/CD Exclusion**            | Ignored in validation jobs unless explicitly referenced for testing.       |
| **Open Standards**             | Only use open, non-proprietary formats (UTF-8 TXT, JSON, JSONL, CSV).      |
| **Sensitive Data Prohibition** | Do **not** store personal, restricted, or confidential content here.       |
| **Naming Convention**          | Prefix with processing stage and date (e.g., `ocr_2025-10-10_sample.txt`). |

---

## 🧩 Typical Use Cases

| Task                     | Example                                                      |
| :----------------------- | :----------------------------------------------------------- |
| **OCR Testing**          | Generate and inspect partial OCR text from historical scans. |
| **Entity Extraction**    | Export NER results (`.jsonl`) for quality validation.        |
| **Text Cleaning QA**     | Test tokenization and normalization scripts before commit.   |
| **Summarization Review** | Compare model-generated summaries to original source text.   |
| **Embedding Validation** | Verify vector representations before database ingestion.     |

---

## 🧹 Cleanup Policy

Temporary files in this directory are **cleared automatically** during
scheduled maintenance or prior to new pipeline runs.

**Makefile Target**

```bash
make clean-tmp
```

**Manual Command**

```bash
rm -rf data/work/tmp/text/*
```

**Persistence Policy:**

* Logs older than **7 days** may be deleted automatically.
* All intermediate text data is reproducible from final inputs in `data/processed/text/`.

---

## 🧰 Integration with ETL, NLP & CI/CD

| Component                             | Function                                                     |
| :------------------------------------ | :----------------------------------------------------------- |
| `src/pipelines/text_pipeline.py`      | Writes and cleans up intermediate text artifacts.            |
| `.github/workflows/stac-validate.yml` | May reference this workspace for debug logs.                 |
| `data/work/logs/`                     | Stores extended ETL and NLP runtime logs.                    |
| `data/processed/text/`                | Receives validated, cleaned, and permanent text datasets.    |
| `data/checksums/text/`                | Contains SHA-256 hashes verifying final dataset integrity.   |
| `data/stac/text/`                     | STAC catalog integrates text dataset lineage and provenance. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                                 |
| :---------------------- | :----------------------------------------------------------------------------- |
| **Documentation-first** | README details directory policy, scope, and reproducibility rules.             |
| **Reproducibility**     | Temporary artifacts are deterministically regenerable from source ETL scripts. |
| **Open Standards**      | UTF-8, JSON, JSONL, CSV ensure full interoperability and transparency.         |
| **Provenance**          | Each temporary file aligns with logged ETL/NLP operations for traceability.    |
| **Auditability**        | Logs and intermediate text allow inspection prior to deletion.                 |

---

## 🧩 Best Practices

1. **Prefix by Domain:** Use clear prefixes (`ocr_`, `nlp_`, `summary_`) for organization.
2. **Limit Size:** Avoid exceeding 100 MB per temporary file to preserve storage efficiency.
3. **Always Clean Up:** Invoke `make clean-tmp` at the end of debug sessions.
4. **Log Everything:** Write pipeline operations to `logs/text_etl_debug.log`.
5. **Never Commit:** Confirm `.gitignore` exclusions prevent text fragments from entering version control.

---

## 📎 Related Directories

| Path                            | Description                                               |
| :------------------------------ | :-------------------------------------------------------- |
| `data/processed/text/`          | Final structured and validated text datasets.             |
| `data/checksums/text/`          | SHA-256 integrity files for text layers.                  |
| `data/processed/metadata/text/` | STAC metadata entries for text datasets.                  |
| `data/work/tmp/`                | Parent directory for all transient ETL and QA subdomains. |

---

## 📅 Version History

| Version    | Date       | Summary                                                                  |
| :--------- | :--------- | :----------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial documentation for text ETL and NLP scratch space.                |
| **v1.1.0** | 2025-10-10 | Added best practices, STAC lineage integration, and auto-cleanup policy. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Where Words Become Data — and Every Byte Is Accounted For.”*
📍 [`data/work/tmp/text/`](.) · Temporary workspace for text ETL, NLP experimentation, and QA validation.

</div>
```
