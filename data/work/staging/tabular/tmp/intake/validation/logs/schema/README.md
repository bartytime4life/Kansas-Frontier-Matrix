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

## 🧭 Table of Contents

- [Overview](#-overview)
- [Directory Layout](#-directory-layout)
- [Workflow · Schema Validation Process](#-workflow--schema-validation-process)
- [Runbook · Commands](#-runbook--commands)
- [Inputs & Contracts](#-inputs--contracts)
- [Validation Components](#-validation-components)
- [Governance Rules](#-governance-rules)
- [Provenance & FAIR Metadata](#-provenance--fair-metadata)
- [Quality Gates & Acceptance Criteria](#-quality-gates--acceptance-criteria)
- [CI/CD Integration](#-cicd-integration)
- [Logging, Telemetry & Retention](#-logging-telemetry--retention)
- [Security & PII](#-security--pii)
- [Troubleshooting](#-troubleshooting)
- [Related Docs](#-related-docs)
- [Version History](#-version-history)
- [Footer & Badges](#-footer--badges)

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
    A[Incoming Tabular Dataset (.csv / .json)] --> B[Schema Discovery & Metadata Inference]
    B --> C[STAC / DCAT Crosswalk Generation]
    C --> D[JSON Schema Validation Engine]
    D --> E[FAIR Compliance Audit (FAIR-CARE Framework)]
    E --> F[AI Schema Anomaly Detection (LLM/Regex Hybrid)]
    F --> G[Validation Reports + Checksums]
    G --> H[Governance Ledger Registration + Schema Provenance Log]
````

---

## 🧪 Runbook · Commands

> All commands run from the repo root (monorepo). These align with standard KFM Make targets.

* **Validate current intake batch**

  ```bash
  make tabular-validate
  ```
* **Generate STAC/DCAT crosswalk + validate**

  ```bash
  make stac-validate dcat-validate
  ```
* **Run FAIR+CARE scoring**

  ```bash
  make faircare
  ```
* **AI anomaly sweep (schema semantics)**

  ```bash
  make ai-schema-audit
  ```
* **Roll-up & checksums**

  ```bash
  make schema-logs
  ```

*Outputs are written to this directory’s `reports/`, `history/`, and `checksums/`.*

---

## 📜 Inputs & Contracts

**Required inputs (per dataset):**

* **Data file**: `.csv` or `.json` with header row / keys.
* **Sidecar metadata**: `.meta.yaml` or `.meta.json` (types, units, temporal coverage, spatial CRS if applicable).
* **Contract**: Conforms to `docs/contracts/data-contract-v3.json` (referenced in front-matter).
* **Spatial/Temporal**: ≥1 of:

  * Temporal column(s): `date`, `datetime`, `year`, `time_start/time_end`
  * Spatial column(s): `lat/lon` or `geometry` (WKT/GeoJSON) or administrative keys with a known join

**Crosswalk expectations:**

* STAC **Item/Collection** fields hydrated for tabular assets (asset roles, `type`, `description`, `created`, `updated`, `datetime` or `start_datetime`/`end_datetime`).
* DCAT JSON-LD nodes for dataset & distribution (download URL, media type, license, spatial/temporal coverage).

---

## 🧠 Validation Components

|               Stage | Tool / Standard                    | Output                           | Description                                                         |
| ------------------: | ---------------------------------- | -------------------------------- | ------------------------------------------------------------------- |
| 1. Schema Discovery | `frictionless`, `pandas-profiling` | `schema-detect.json`             | Infers structure & types; detects missing headers & mixed types.    |
|      2. JSON Schema | `jsonschema` (tabular-v13)         | `tabular-schema-validation.json` | Enforces field types, enums, formats, nullability, required fields. |
|             3. STAC | `stac-validator` + KFM crosswalk   | `stac-validation.json`           | Validates STAC 1.0 Item/Collection for tabular assets.              |
|             4. DCAT | JSON-LD + SHACL rules              | `dcat-validation.json`           | Checks dataset/distribution nodes for DCAT 3.0 semantics.           |
|        5. FAIR+CARE | FAIR scoring module                | `faircare-summary.json`          | Computes F, A, I, R and CARE context; flags gaps.                   |
|         6. AI Audit | `ai_tabular_audit.py`              | `ai-schema-anomalies.json`       | Detects semantic drifts, undocumented columns, unit mismatches.     |
|        7. Integrity | `sha256sum`                        | `validation_checksums.sha256`    | Hashes for **all** reports; immutability check.                     |

---

## 🧷 Governance Rules

* **Must-pass** stages: JSON Schema, STAC, DCAT, Integrity.
* **FAIR+CARE**: Minimum score threshold defined below; exceptions require `@kfm-schema-council` sign-off.
* **Sidecar metadata** mandatory; files without sidecars are **rejected**.
* **PII** strictly forbidden; any detected PII halts pipeline and opens a security incident.
* **Quarterly** review: Schema version bump, DCAT/STAC rule updates, FAIR thresholds, anomaly ruleset refresh.

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

> **Note:** The STAC collection is the public index for intake assets; DCAT feed is generated nightly by CI.

---

## ✅ Quality Gates & Acceptance Criteria

| Gate                  | Threshold                        | Source                           |
| --------------------- | -------------------------------- | -------------------------------- |
| JSON Schema pass rate | **100%**                         | `tabular-schema-validation.json` |
| STAC validity         | **No errors** (warnings allowed) | `stac-validation.json`           |
| DCAT validity         | **No errors**                    | `dcat-validation.json`           |
| FAIR score            | **≥ 0.95**                       | `faircare-summary.json`          |
| AI audit              | **0 critical** anomalies         | `ai-schema-anomalies.json`       |
| Checksums             | **Verified**                     | `validation_checksums.sha256`    |

**Promotion rule:** Only datasets meeting all gates are eligible for move to `data/work/staging/tabular/normalized/`.

---

## 🛠 CI/CD Integration

* **PR Gate**: Running in `validate-schema.yml` on every PR touching `data/work/staging/tabular/tmp/intake/**`.
* **Nightly**: Re-run validations on changed sources; publish STAC/DCAT and FAIR dashboards.
* **Artifacts**: All reports uploaded as CI artifacts + committed to this directory on merge.
* **Badges**: “Build & Validate · Passing” shows the last default-branch status.

---

## 📡 Logging, Telemetry & Retention

* **Logs**: `history/*.log` retained **indefinitely** (text, small footprint).
* **Reports**: Retain last **8 quarters**; older archived to `releases/v*/validation/`.
* **Metrics**: FAIR score, pass rates, anomaly counts emitted to `telemetry_schema` and aggregated in `releases/v9.0.0/focus-telemetry.json`.

---

## 🔐 Security & PII

* Classification: **Public (Open Data)**; **no PII** permitted.
* PII detection hooks in AI audit (regex + model); any hit = **hard fail** and security ticket.
* Only whitelisted MIME types: `text/csv`, `application/json`.
* License must be machine-readable; license conflicts block promotion.

---

## 🧯 Troubleshooting

* **“Unknown field”** in schema: Add to sidecar metadata or map to known alias; re-run `make tabular-validate`.
* **STAC time errors**: Ensure `datetime` or `start/end_datetime` present and ISO-8601.
* **FAIR score < threshold**: Fill missing `license`, `description`, `keywords`, `spatial/temporal` coverage.
* **AI anomaly ‘units mismatch’**: Normalize units in sidecar and/or transform step; document conversion.
* **Checksum mismatch**: Rebuild reports; confirm no manual edits to `reports/*.json`.

---

## 🔗 Related Docs

* **Data Contract** — `docs/contracts/data-contract-v3.json`
* **Repo Focus / Architecture** — `docs/architecture/repo-focus.md`
* **Monorepo & Data Layout** — `docs/architecture/file-data-architecture.md`
* **STAC Catalog (Intake)** — `data/stac/tabular/intake/collection.json`
* **TMP Intake Overview** — `data/work/staging/tabular/tmp/intake/README.md`
* **Validation (TMP root)** — `data/work/staging/tabular/tmp/intake/validation/README.md`

---

## 🗂 Version History

| Version | Date       | Description                                                                 | Commit                 |
| ------: | ---------- | --------------------------------------------------------------------------- | ---------------------- |
|  v9.0.1 | 2025-10-26 | Expanded runbook, CI, security, acceptance criteria, related links & badges | `<latest-commit-hash>` |
|  v9.0.0 | 2025-10-26 | Initial schema validation record for TMP intake data                        | `<latest-commit-hash>` |
|  v8.9.0 | 2025-07-12 | Added AI anomaly detection for schema validation                            | `b21aefc`              |
|  v8.8.0 | 2025-04-09 | Integrated FAIR+CARE compliance scoring                                     | `d61a72b`              |

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

