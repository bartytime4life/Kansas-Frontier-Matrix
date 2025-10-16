<div align="center">

# 📊 Kansas Frontier Matrix — **Tabular ETL Logs**  
`data/work/tmp/tabular/logs/`

**Mission:** Store **temporary log files** generated during tabular ETL, validation, and QA/QC workflows —  
ensuring full **transparency**, **traceability**, and **reproducibility** for census, agricultural, and economic datasets processed within  
the **Kansas Frontier Matrix (KFM)** system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-Validate-blue)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../../.github/workflows/codeql.yml)
[![Trivy Security](https://img.shields.io/badge/Container%20Scan-Secure-orange)](../../../../../../.github/workflows/trivy.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-green)](../../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-blue)](../../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Tabular ETL Logs (data/work/tmp/tabular/logs/)"
version: "v1.2.0"
last_updated: "2025-10-16"
owners: ["@kfm-data", "@kfm-etl"]
tags: ["tabular","etl","logs","csv","parquet","schema","checksum","mcp","stac"]
license: "CC-BY 4.0"
semantic_alignment:
  - MCP-DL v6.2 (Reproducibility & Provenance)
  - FAIR Principles (Traceable Experimental Records)
  - CSVW · JSON Schema · DCAT / STAC metadata alignment
---
```

---

## 📚 Overview

The `data/work/tmp/tabular/logs/` directory holds **transient ETL, validation, and QA/QC logs** emitted while tabular data  
(e.g., **census**, **agricultural**, **economic** tables) is loaded, cleaned, transformed, normalized, and verified.

Logs here enable:

- **Schema** & **format validation** for CSV/Parquet outputs  
- **Quality control** (type checks, unit normalization, range and integrity tests)  
- **Time-series QA** across decades (consistency, diffs, rollups)  
- **Checksum audits** and reproducibility verification  

All files are **ephemeral**, **excluded from version control**, and **regenerated** on each ETL run.

---

## 🗂️ Directory Layout

```bash
data/work/tmp/tabular/logs/
├── README.md
├── tabular_etl_debug.log
├── census_schema_validation.log
├── agriculture_cleaning_report.log
└── checksum_audit_report.log
```

> **Note:** Filenames rotate or overwrite per run and may differ depending on active ETL tasks.

---

## ⚙️ Logging Guidelines

| Log Type                    | Purpose                                                                 |
| :-------------------------- | :---------------------------------------------------------------------- |
| **`*_etl_debug.log`**       | ETL stages — load → clean → transform → export; timings & statuses.     |
| **`*_validation.log`**      | JSON Schema/CSVW checks, data types, units, and constraint evaluations. |
| **`*_cleaning_report.log`** | Missing-value strategies, normalizations, coercions, and anomaly flags. |
| **`*_checksum_audit.log`**  | SHA-256 hashes, diff-to-baseline, determinism checks, and summaries.    |

**Format:** UTF-8 plain text; single-line entries; newline-terminated; no ANSI colors.

---

## 🧾 Standard Line Schema

All tabular logs follow a **grep-friendly**, machine-parseable schema:

```text
[timestamp] [LEVEL] [component] key1=val1 key2=val2 ... message="free text"
```

**Examples**

```text
2025-10-16T09:18:02Z INFO tabular.etl stage="start" run_id="2025-10-16T09:18Z" message="tabular pipeline init"
2025-10-16T09:18:11Z INFO tabular.load src="data/raw/tabular/census_1890.csv" rows=12437 message="load complete"
2025-10-16T09:18:22Z WARNING tabular.clean column="population" action="coerce_int" bad_rows=41 message="type mismatch"
2025-10-16T09:18:36Z INFO tabular.schema file="census_1890.csv" schema="schemas/census_1890.json" result="pass"
2025-10-16T09:18:49Z INFO tabular.checksum file="census_1890_clean.csv" sha256="a7f0f3..." result="match"
2025-10-16T09:18:55Z INFO tabular.etl stage="end" status="SUCCESS" duration_s=53.0
```

**Components:** `tabular.load`, `tabular.clean`, `tabular.schema`, `tabular.stats`, `tabular.checksum`, `tabular.export`.

---

## 🔧 Minimal Logging Config (YAML)

```yaml
version: 1
formatters:
  line:
    format: "%(asctime)s %(levelname)s %(name)s %(message)s"
handlers:
  tabular_rotating:
    class: logging.handlers.RotatingFileHandler
    filename: data/work/tmp/tabular/logs/tabular_etl_debug.log
    maxBytes: 2097152   # 2 MB
    backupCount: 3
    encoding: utf-8
    formatter: line
loggers:
  kfm.tabular:
    level: INFO
    handlers: [tabular_rotating]
    propagate: no
root:
  level: WARNING
  handlers: [tabular_rotating]
```

**Python Emission (snippet)**

```python
import logging
log = logging.getLogger("kfm.tabular")
log.info('stage="start" run_id="2025-10-16T09:18Z" message="tabular pipeline init"')
```

---

## ⚙️ Log Generation Workflow

Logs are produced automatically by the **Tabular ETL pipeline** or can be invoked manually.

**Makefile**

```bash
make tabular
```

**Python CLI**

```bash
python src/pipelines/tabular/tabular_pipeline.py \
  --log data/work/tmp/tabular/logs/tabular_etl_debug.log
```

**Lifecycle**

1. **Initialize** log with run metadata (run ID, commit SHA, env hash).  
2. **Append** structured entries per stage (load → clean → validate → export).  
3. **Flag** anomalies with `WARNING`/`ERROR` (include remediation where possible).  
4. **Summarize** counts, duration, status; rotate and purge per retention policy.

---

## 🧹 Cleanup Policy

Logs are **temporary** and purged between runs to prevent accumulation.

**Automated**

```bash
make clean-logs
```

**Manual**

```bash
rm -rf data/work/tmp/tabular/logs/*
```

**Permanent Artifacts**

- `data/processed/tabular/` — validated, published tables  
- `data/checksums/tabular/` — SHA-256 manifests for reproducibility  
- `data/processed/metadata/tabular/` — STAC-compliant dataset metadata

---

## 🔒 Security & Retention

| Rule                   | Implementation                                                                 |
| :--------------------- | :------------------------------------------------------------------------------ |
| **Retention**          | Logs persist only for the active ETL cycle or CI job; default ≤ **7 days**.     |
| **Sensitive Data**     | Do **not** log PII or confidential values; log counts and metrics instead.      |
| **Access Scope**       | Local-only artifacts; never committed or uploaded to remote storage.            |
| **Content Minimization** | Record parameters and metrics; avoid dumping raw table content.               |

---

## 🧰 CI/CD & Metadata Integration

| Linked Component                            | Function                                                        |
| :------------------------------------------ | :-------------------------------------------------------------- |
| `src/pipelines/tabular/tabular_pipeline.py` | Emits ETL, schema, and checksum logs; manages rotation/purge.   |
| `.github/workflows/stac-validate.yml`       | Consumes logs for schema/DCAT checks and checksum QA.           |
| `data/work/tmp/tabular/`                    | Parent scratch for tabular intermediates under test.            |
| `data/processed/tabular/`                   | Destination for finalized, validated tabular datasets.          |
| `data/checksums/tabular/`                   | Integrity verification manifests for published outputs.          |
| `data/processed/metadata/tabular/`          | STAC Items/Collections linking tabular provenance & lineage.    |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                              |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Documentation-first** | README documents structure, lifecycle, and retention.                       |
| **Reproducibility**     | Logs deterministically mirror ETL/QA actions, parameters, and results.      |
| **Open Standards**      | UTF-8 text lines; CSVW/JSON Schema references for metadata alignment.       |
| **Provenance**          | Entries bind to run ID, commit SHA, inputs, and transformation stages.      |
| **Auditability**        | Grep-friendly format; CI consumers enable transparent QA and diagnostics.   |

---

## 📎 Related Directories

| Path                               | Description                                     |
| :--------------------------------- | :---------------------------------------------- |
| `data/work/tmp/tabular/`           | Temporary workspace for tabular ETL operations. |
| `data/processed/tabular/`          | Finalized, validated tabular datasets.          |
| `data/checksums/tabular/`          | SHA-256 validation for reproducibility.         |
| `data/processed/metadata/tabular/` | STAC metadata and dataset documentation.        |

---

## 📅 Version History

| Version | Date       | Summary                                                                 |
| :------ | :--------- | :---------------------------------------------------------------------- |
| **v1.0.0** | 2025-10-04 | Initial creation of tabular ETL log documentation.                     |
| **v1.1.0** | 2025-10-09 | Added YAML header, schema alignment, and provenance references.        |
| **v1.2.0** | 2025-10-16 | Alignment pass: line schema, rotation config, security & retention.    |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Table Has a Trail — Logged, Verified, and Reproducible.”*  
📍 [`data/work/tmp/tabular/logs/`](.) · Temporary ETL logging workspace for tabular datasets.

</div>
