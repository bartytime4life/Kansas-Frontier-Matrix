---
title: "🧩 Kansas Frontier Matrix — STAC Schema Validation Logs"
path: "data/work/staging/tabular/tmp/intake/validation/logs/schema/README.md"
version: "v9.0.1"
last_updated: "2025-10-26"
review_cycle: "Quarterly / Autonomous"
owners: ["@kfm-data", "@kfm-schema-council"]
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v9.0.0/sbom.spdx.json"
manifest_ref: "releases/v9.0.0/manifest.zip"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v9.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/staging-tabular-schema-v13.json"
json_export: "releases/v9.0.0/schema-validation.meta.json"
stac_collection_ref: "data/stac/tabular/intake/collection.json"
validation_reports:
  - "reports/schema-validation/tabular-schema-validation.json"
  - "reports/audit/tabular-schema-audit.json"
  - "reports/fair/faircare-summary.json"
security_classification: "Public (Open Data) · PII: None"
license: "MIT"
---

<div align="center">

# 🧩 Kansas Frontier Matrix — **STAC Schema Validation Logs**  
`data/work/staging/tabular/tmp/intake/validation/logs/schema/README.md`

**Purpose:** Canonical log and operating guide for **schema-level validation** of tabular intake datasets, enforcing **STAC 1.0**, **DCAT 3.0**, **JSON Schema**, and **MCP-DL v6.3** across all CSV/JSON assets before normalization and graph ingestion.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../docs/architecture/repo-focus.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../../LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-orange)]()
[![Validation: STAC + DCAT](https://img.shields.io/badge/Validation-STAC%20%7C%20DCAT-lightblue)]()

</div>

---

<details>
<summary><b>📚 Table of Contents (click to expand)</b></summary>

- [📘 Overview](#-overview)
- [🧾 Directory Layout](#-directory-layout)
- [⚙️ Workflow · Schema Validation Process](#️-workflow--schema-validation-process)
- [🧪 Runbook · Commands](#-runbook--commands)
- [📜 Inputs & Contracts](#-inputs--contracts)
- [🧠 Validation Components](#-validation-components)
- [🧷 Governance Rules](#-governance-rules)
- [🧾 Provenance & FAIR Metadata](#-provenance--fair-metadata)
- [✅ Quality Gates & Acceptance Criteria](#-quality-gates--acceptance-criteria)
- [🛠 CI/CD Integration](#-cicd-integration)
- [📡 Logging, Telemetry & Retention](#-logging-telemetry--retention)
- [🔐 Security & PII](#-security--pii)
- [🧯 Troubleshooting](#-troubleshooting)
- [🔗 Related Docs](#-related-docs)
- [🗂 Version History](#-version-history)
- [🏁 Footer & Badges](#-footer--badges)

</details>

---

## 📘 Overview

This area is the **single source of truth** for all **schema validations** on tabular intake data before promotion to `normalized/`.  
It includes machine-generated **JSON reports**, human-readable summaries, **checksums**, and a **governance history** to guarantee **reproducibility** and **provenance** under MCP.

---

## 🧾 Directory Layout

```

data/work/staging/tabular/tmp/intake/validation/logs/schema/
├─ README.md
├─ reports/
│  ├─ tabular-schema-validation.json         # JSON Schema pass/fail details
│  ├─ stac-validation.json                   # STAC validator output (item/collection)
│  ├─ dcat-validation.json                   # DCAT JSON-LD checks
│  ├─ faircare-summary.json                  # FAIR+CARE scoring
│  ├─ ai-schema-anomalies.json               # AI/LLM anomaly findings
│  └─ tabular-schema-audit.json              # Governance/audit narrative
├─ checksums/
│  └─ validation_checksums.sha256            # Hashes of all artifacts in this run
└─ history/
├─ 2025-10-26_schema-validation.log       # Time-stamped run logs
└─ 2025-07-12_schema-validation.log

````

> **Tip:** Every new run appends to `history/` and regenerates `checksums/validation_checksums.sha256`.

---

## ⚙️ Workflow · Schema Validation Process

```mermaid
flowchart TD
    A["Incoming Tabular Dataset (CSV or JSON)"] --> B["Schema Discovery & Metadata Inference"]
    B --> C["STAC / DCAT Crosswalk Generation"]
    C --> D["JSON Schema Validation Engine"]
    D --> E["FAIR Compliance Audit (FAIR+CARE Framework)"]
    E --> F["AI Schema Anomaly Detection (LLM + Regex Hybrid)"]
    F --> G["Validation Reports + Checksums"]
    G --> H["Governance Ledger Registration + Schema Provenance Log"]
````

---

## 🧪 Runbook · Commands

> All commands run from the repo root (monorepo). These align with standard KFM Make targets.

```bash
# Validate current intake batch
make tabular-validate

# Generate STAC/DCAT crosswalk + validate
make stac-validate dcat-validate

# Run FAIR+CARE scoring
make faircare

# AI anomaly sweep (schema semantics)
make ai-schema-audit

# Roll-up & checksums
make schema-logs
```

Outputs are written to this directory’s `reports/`, `history/`, and `checksums/`.

---

## 📜 Inputs & Contracts

* **Data file:** `.csv` or `.json` with header row / keys.
* **Metadata sidecar:** `.meta.yaml` or `.meta.json` describing field types, units, spatial/temporal coverage.
* **Contract:** Must conform to `docs/contracts/data-contract-v3.json`.
* **Spatial or temporal attributes:** At least one of:

  * `datetime` or `start_datetime` / `end_datetime`
  * Spatial geometry (`lat/lon`, `geometry`, or `place_id`)

Crosswalks must generate **STAC Item** and **DCAT Dataset** entries referencing these fields.

---

## 🧠 Validation Components

|                Stage | Tool / Standard                    | Output                           | Description                                                         |
| -------------------: | ---------------------------------- | -------------------------------- | ------------------------------------------------------------------- |
| 1️⃣ Schema Discovery | `frictionless`, `pandas-profiling` | `schema-detect.json`             | Infers structure & types; detects missing headers & mixed types.    |
|      2️⃣ JSON Schema | `jsonschema` (tabular-v13)         | `tabular-schema-validation.json` | Enforces field types, enums, formats, nullability, required fields. |
|             3️⃣ STAC | `stac-validator` + KFM crosswalk   | `stac-validation.json`           | Validates STAC 1.0 Item/Collection for tabular assets.              |
|             4️⃣ DCAT | JSON-LD + SHACL rules              | `dcat-validation.json`           | Checks dataset/distribution nodes for DCAT 3.0 semantics.           |
|        5️⃣ FAIR+CARE | FAIR scoring module                | `faircare-summary.json`          | Computes FAIR & CARE metrics; flags gaps.                           |
|         6️⃣ AI Audit | `ai_tabular_audit.py`              | `ai-schema-anomalies.json`       | Detects semantic drifts, undocumented columns, unit mismatches.     |
|        7️⃣ Integrity | `sha256sum`                        | `validation_checksums.sha256`    | Hashes for **all** reports; immutability check.                     |

---

## 🧷 Governance Rules

* **Mandatory Pass:** JSON Schema, STAC, DCAT, and Integrity.
* **FAIR+CARE Threshold:** ≥ 0.95 or exception approved by `@kfm-schema-council`.
* **Sidecar metadata:** Required for all datasets; missing sidecar = rejection.
* **PII:** Forbidden. Detection triggers automatic pipeline halt.
* **Quarterly Reviews:** Schema version updates, FAIR rule changes, anomaly tuning.

---

## 🧾 Provenance & FAIR Metadata

```yaml
validation_id: "tabular-schema-validation-2025-10-26"
validated_by: "@kfm-data"
schema_ref: "schemas/tabular-v13.json"
stac_ref: "data/stac/tabular/intake/collection.json"
data_contract_ref: "docs/contracts/data-contract-v3.json"
provenance:
  toolchain: ["frictionless>=5.15", "jsonschema>=4.21", "stac-validator>=3.0"]
  commit: "<latest-commit-hash>"
  date: "2025-10-26"
license: "MIT"
```

---

## ✅ Quality Gates & Acceptance Criteria

| Gate                  | Target                      | Source                           |
| --------------------- | --------------------------- | -------------------------------- |
| JSON Schema pass rate | **100%**                    | `tabular-schema-validation.json` |
| STAC validity         | **No errors** (warnings ok) | `stac-validation.json`           |
| DCAT validity         | **No errors**               | `dcat-validation.json`           |
| FAIR+CARE score       | **≥ 0.95**                  | `faircare-summary.json`          |
| AI audit              | **0 critical** anomalies    | `ai-schema-anomalies.json`       |
| Checksums             | **Verified**                | `validation_checksums.sha256`    |

---

## 🛠 CI/CD Integration

* **PR Gate:** Executes `validate-schema.yml` for any modified intake dataset.
* **Nightly Jobs:** Re-run full schema validations, regenerate FAIR dashboards.
* **Artifacts:** Logs, metrics, and JSONs uploaded to CI artifacts.
* **Badges:** Validation status reflected in repo shields.

---

## 📡 Logging, Telemetry & Retention

* **Retention:** 8 quarters for reports, indefinite for logs.
* **Telemetry:** Schema, FAIR score, anomalies emitted to telemetry JSON.
* **Metrics Dashboard:** Generated via `focus-telemetry.json` and visualized in Focus Mode analytics.

---

## 🔐 Security & PII

* **Classification:** Public (Open Data) · **PII:** None permitted.
* **AI Scans:** All tabular data scanned for PII signatures pre-ingest.
* **Encryption:** Not required for this dataset class.

---

## 🧯 Troubleshooting

| Issue                       | Resolution                                                          |
| --------------------------- | ------------------------------------------------------------------- |
| Unknown field               | Update sidecar metadata & re-run validation.                        |
| STAC time errors            | Ensure ISO-8601 dates & valid intervals.                            |
| FAIR score < threshold      | Add missing metadata: license, keywords, spatial/temporal coverage. |
| AI anomaly “units mismatch” | Normalize units or fix schema enum; rerun `make ai-schema-audit`.   |
| Checksum mismatch           | Recompute `sha256` & ensure no manual JSON edits.                   |

---

## 🔗 Related Docs

* `docs/contracts/data-contract-v3.json`
* `docs/architecture/repo-focus.md`
* `docs/architecture/file-data-architecture.md`
* `data/stac/tabular/intake/collection.json`
* `data/work/staging/tabular/tmp/intake/README.md`
* `data/work/staging/tabular/tmp/intake/validation/README.md`

---

## 🗂 Version History

| Version | Date       | Description                                                    | Commit                 |
| ------: | ---------- | -------------------------------------------------------------- | ---------------------- |
|  v9.0.1 | 2025-10-26 | Added dropdown TOC, emojis, enhanced CI/CD and troubleshooting | `<latest-commit-hash>` |
|  v9.0.0 | 2025-10-26 | Initial schema validation record for TMP intake data           | `<latest-commit-hash>` |
|  v8.9.0 | 2025-07-12 | Added AI anomaly detection for schema validation               | `b21aefc`              |
|  v8.8.0 | 2025-04-09 | Integrated FAIR+CARE compliance scoring                        | `d61a72b`              |

---

<div align="center">

**Kansas Frontier Matrix — Tabular Intake Schema Validation Logs**
*“Reproducibility through transparency. Every schema. Every time.”*
🧭 [Return to TMP Intake Validation Overview](../../../../README.md)

[![Build & Validate](https://img.shields.io/badge/Build%20%26%20Validate-Passing-brightgreen)]()
[![FAIR Compliance](https://img.shields.io/badge/FAIR%20Compliance-0.97-green)]()
[![Schema Validator](https://img.shields.io/badge/Schema%20Validator-STAC%20%7C%20DCAT-blue)]()
[![AI Audit](https://img.shields.io/badge/AI%20Schema%20Audit-Enabled-purple)]()
[![Data Integrity](https://img.shields.io/badge/Checksums-Verified-lightgrey)]()

</div>
```
