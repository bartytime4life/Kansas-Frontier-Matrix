---
title: "🧾 Kansas Frontier Matrix — Tabular Intake Logs Directory (Diamond⁹ Ω / Crown∞Ω Certified)"
path: "data/work/staging/tabular/tmp/intake/logs/README.md"
version: "v9.0.1"
last_updated: "2025-10-26"
status: "Active · FAIR+CARE+MCP-DL v6.3 Aligned"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
parent_ref: "data/work/staging/tabular/tmp/intake/README.md"
manifest_ref: "releases/v9.0.1/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v9.0.1/focus-telemetry.json"
audit_ledger_ref: "governance/tabular_intake_ledger.jsonld"
---

<div align="center">

# 🧾 Kansas Frontier Matrix — **Intake Logs Directory**  
`data/work/staging/tabular/tmp/intake/logs/`

### *“Every dataset leaves a trace; every trace tells the story of integrity.”*

**Purpose:**  
The **Logs Directory** is the canonical record of all automated and manual operations executed during **Tabular Intake TMP** processing.  
It provides timestamped, structured JSONL logs for ETL events, schema validation, AI checks, checksum generation, and curator reviews.  

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../docs/architecture/repo-focus.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-orange)]()
[![Integrity](https://img.shields.io/badge/Integrity-SHA--256-lightgrey)]()
[![AI Pipeline](https://img.shields.io/badge/AI--Logs-Enabled-teal)]()

</div>

---

## 🧭 Overview

This directory maintains **structured operational logs** that capture every action, anomaly, and audit message generated during intake and validation.  
Each log entry is machine-readable, human-auditable, and **linked to the dataset’s provenance ledger entry** for traceability.  

Logs follow the **MCP-DL structured logging standard (v6.3)** and are used in dashboards, telemetry, and validation history.

---

## 📁 Directory Layout

```plaintext
data/work/staging/tabular/tmp/intake/logs/
├── etl/                         # ETL process logs (fetch, transform, load)
├── validation/                  # Schema and checksum validation logs
├── ai/                          # AI inference and anomaly detection logs
├── faircare/                    # FAIR+CARE ethical audit logs
├── review/                      # Human curator review records
└── README.md                    # This document
````

---

## 🧱 Log Structure

Each log file is in **JSON Lines (.jsonl)** format for efficient append-only writing and parsing.
Each line represents one atomic event in the intake lifecycle.

**Schema (shared log model):**

```json
{
  "timestamp": "2025-10-26T13:45:21Z",
  "dataset": "ks_hydro_1874",
  "stage": "validation",
  "level": "INFO",
  "component": "stac-validator",
  "message": "STAC validation completed successfully.",
  "duration_ms": 2543,
  "checksum": "4c4925bbf65b9e1a5f8e7f0b67d7b5e9a8a8a2c1c7f7a0f0...",
  "ai_confidence": 0.97,
  "status": "passed",
  "run_id": "etl-2025-10-26-1345Z",
  "trace_id": "a12c98fa-274e-4e8d-b91d-02eebc0e26f2"
}
```

---

## ⚙️ Log Categories

| Folder          | Description                                                                                              | File Pattern             |
| --------------- | -------------------------------------------------------------------------------------------------------- | ------------------------ |
| **etl/**        | Logs for ETL processes (source fetch, transform, load). Includes errors, retries, and runtime durations. | `etl-*.jsonl`            |
| **validation/** | Schema validation and checksum operations. Includes STAC/DCAT conformity and hash mismatches.            | `validate-*.jsonl`       |
| **ai/**         | AI processing, entity recognition, and anomaly detection logs.                                           | `ai-intake-*.jsonl`      |
| **faircare/**   | FAIR+CARE ethical compliance checks (licensing, accessibility, metadata completeness).                   | `faircare-audit-*.jsonl` |
| **review/**     | Manual curation logs. Contains reviewer notes and approval timestamps.                                   | `review-*.log`           |

---

## 🧩 Log Lifecycle & Retention

1. **Creation:**
   Logs are generated automatically during each pipeline stage by `src/pipelines/tabular_intake.py`.

2. **Aggregation:**
   After each run, individual logs are merged into a consolidated file per dataset (e.g. `ks_hydro_1874.full.log.jsonl`).

3. **Archival:**
   Logs older than 6 months are compressed and moved to:
   `data/work/staging/tabular/tmp/intake/archive/logs/`

4. **Linkage:**
   The most recent log hash is registered under the dataset’s provenance record in the **Audit Ledger**.

---

## 🧪 Example Logs

**ETL Log (`etl/etl-ks_hydro_1874.jsonl`):**

```json
{"timestamp":"2025-10-26T13:42:11Z","dataset":"ks_hydro_1874","level":"INFO","component":"fetch","message":"Fetched 3 records from external source.","status":"ok"}
{"timestamp":"2025-10-26T13:42:12Z","dataset":"ks_hydro_1874","level":"INFO","component":"transform","message":"Converted date fields to ISO-8601.","status":"ok"}
{"timestamp":"2025-10-26T13:42:14Z","dataset":"ks_hydro_1874","level":"INFO","component":"load","message":"Data moved to intake/validation stage.","status":"ok"}
```

**AI Log (`ai/ai-intake-ks_hydro_1874.jsonl`):**

```json
{"timestamp":"2025-10-26T13:44:09Z","dataset":"ks_hydro_1874","stage":"ai","component":"anomaly_detector","message":"1 medium outlier detected","ai_confidence":0.92,"status":"warning"}
{"timestamp":"2025-10-26T13:44:15Z","dataset":"ks_hydro_1874","stage":"ai","component":"summarizer","message":"Generated summary report ai_summaries/tabular-intake.summary.json","status":"ok"}
```

**Review Log (`review/review-ks_hydro_1874.log`):**

```
[2025-10-26T13:50:42Z] Curator: @kfm-curation
Dataset: ks_hydro_1874
Decision: ACCEPTED
Notes: AI anomalies reviewed; data conforms to schema.
```

---

## 🧮 Log Commands

```bash
# Tail live logs for active intake run
make tail-intake-logs

# Consolidate and hash all logs
make archive-logs

# Filter warnings and errors
grep -E '"status":"(warning|error)"' logs/**/*.jsonl

# Validate log schema
make validate-logs
```

> 🧩 *All logs conform to `schemas/logging/tabular-intake-log-v2.json`.*

---

## 🧾 Governance Integration

Each consolidated log’s SHA-256 digest is stored in the **Audit Ledger** (`governance/tabular_intake_ledger.jsonld`):

```json
{
  "dataset": "ks_hydro_1874",
  "log_ref": "logs/ks_hydro_1874.full.log.jsonl",
  "log_hash": "7a5f4d9138c9a6a8a8e3b5e8a89a4c1e7d2b8c0f9a6e4d7f...",
  "linked_to": "reports/audit/ai_tabular_ledger.json",
  "status": "validated"
}
```

---

## ☑️ Logging Policy

| Policy Area     | Rule                                    |
| --------------- | --------------------------------------- |
| **Format**      | JSON Lines (UTF-8)                      |
| **Rotation**    | 1 file per dataset per run              |
| **Retention**   | 6 months (auto-archive)                 |
| **Encryption**  | SHA-256 hash registered for integrity   |
| **Redaction**   | PII scrubbed before archival            |
| **Access**      | Read-only via automated dashboard       |
| **Audit Trail** | All actions logged in Governance Ledger |

---

## 🪶 Version History

| Version    | Date       | Author              | Notes                                                                                 |
| ---------- | ---------- | ------------------- | ------------------------------------------------------------------------------------- |
| **v9.0.1** | 2025-10-26 | `@kfm-architecture` | Initial release — defines structured JSONL format, retention, and ledger integration. |

---

<div align="center">

### 🜂 Kansas Frontier Matrix — *Traceability · Auditability · Trust*

**“If it’s not logged, it never happened.”**

[![Build & Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/validate.yml?label=Build+%26+Validate)]()
[![Audit Logs](https://img.shields.io/badge/Logs-Validated-success)]()
[![AI Engine](https://img.shields.io/badge/AI--Logging-Active-teal)]()
[![Pre-Commit](https://img.shields.io/badge/Pre--Commit-Passed-success)]()

[⬆ Back to Top](#-kansas-frontier-matrix--intake-logs-directory)

</div>
```
