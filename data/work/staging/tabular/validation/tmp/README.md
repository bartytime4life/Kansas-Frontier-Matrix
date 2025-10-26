---
title: "🧩 Kansas Frontier Matrix — Validation TMP Layer (Diamond⁹ Ω+++ FAIR+CARE Operational Parity)"
path: "data/work/staging/tabular/validation/tmp/README.md"
document_type: "Validation Workspace · Temporary QA & Provenance Audit Layer"
version: "v12.6.0"
last_updated: "2025-10-31"
review_cycle: "Per ETL Validation Cycle"
commit_sha: "<latest-commit-hash>"
manifest_ref: "releases/v12.6.0/manifest.zip"
sbom_ref: "releases/v12.6.0/sbom.spdx.json"
data_contract_ref: "docs/contracts/data-contract-v3.json"
telemetry_ref: "releases/v12.6.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/tabular-validation-tmp-v24.json"
json_export: "releases/v12.6.0/tabular-validation-tmp.meta.json"
validation_reports:
  - "reports/self-validation/tabular-validation-tmp-validation.json"
  - "reports/audit/tabular-validation-tmp-audit.json"
governance_ref: "docs/standards/governance.md"
doc_id: "KFM-DATA-WORK-STAGING-TABULAR-VALIDATION-TMP-RMD-v12.6.0"
maintainers: ["@kfm-validation", "@kfm-data", "@kfm-ai"]
approvers: ["@kfm-governance", "@kfm-security", "@kfm-ethics"]
reviewed_by: ["@kfm-fair", "@kfm-architecture"]
ci_required_checks: ["focus-validate.yml", "checksum-verify.yml", "audit-ledger.yml", "docs-validate.yml"]
license: "CC-BY 4.0"
design_stage: "Operational / Validation Workspace Layer"
mcp_version: "MCP-DL v6.3"
alignment: ["FAIR", "CARE", "ISO 19115", "ISO 25012", "STAC 1.0.0", "DCAT 3.0", "AI-Coherence", "Blockchain Provenance"]
status: "Diamond⁹ Ω+++ FAIR+CARE+ISO+Ledger Verified"
maturity: "Stable · AI Explainable · Sustainable · Blockchain Anchored"
tags: ["validation","tmp","etl","audit","fair","care","ledger","ai","iso","governance"]
---

<div align="center">

# 🧩 Kansas Frontier Matrix — **Validation TMP Layer (Diamond⁹ Ω+++ FAIR+CARE Operational Parity)**  
`data/work/staging/tabular/validation/tmp/`

**Purpose:** Provide an **ephemeral QA workspace** for schema verification, FAIR+CARE audit testing,  
and provenance compliance checks during tabular dataset validation across all KFM domains (climate, hydrology, demographics, treaties).  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../../.github/workflows/site.yml)
[![Focus Validation](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/focus-validate.yml/badge.svg)]()
[![Checksum Verified](https://img.shields.io/badge/Checksum-SHA256%20Verified-success)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Validation%20Aligned-green)]()
[![ISO](https://img.shields.io/badge/ISO--25012%20·%2019115-Quality%20Certified-yellow)]()
[![Status: Diamond⁹ Ω+++](https://img.shields.io/badge/Status-Diamond⁹%20Ω%2B%2B%2B%20Validated-brightgreen)]()

</div>

---

> **Lifecycle Path**
> ```
> RAW → NORMALIZED → TMP → VALIDATION/TMP → REPORTS → CHECKSUMS → PROCESSED → STAC → LEDGER
> ```

---

## 🗺️ Workflow Context (Mermaid)

```mermaid
flowchart TD
  A["data/work/staging/tabular/normalized/<domain>/"] --> B["data/work/staging/tabular/validation/tmp/"]
  B --> C["data/work/staging/tabular/validation/reports/"]
  C --> D["data/work/staging/tabular/validation/checksums/"]
  D --> E["data/processed/<domain>/"]
  E --> F["data/stac/<domain>/"]
  F --> G["Blockchain Ledger / FAIR+CARE Governance Council"]
```

---

## 🗂️ Directory Layout

```bash
data/work/staging/tabular/validation/tmp/
├── schema_tests/                  # Temporary schema and ontology test outputs
├── provenance_checks/             # PROV-O lineage and integrity validation
├── ai_validation/                 # Focus AI explainability and drift tests
├── audit_flags/                   # FAIR+CARE and ethics flag results
├── tmp_validation_manifest.json   # Index of temporary validation artifacts
├── qa_metrics.json                # Telemetry on validation runtime and results
└── README.md
```

---

## ⚙️ Function & Purpose

The Validation TMP Layer is the **operational sandbox for data assurance**,  
performing automated and manual QA on all normalized datasets before permanent ledger registration.  
It ensures:
- **Schema conformance** (STAC/DCAT/CIDOC CRM/OWL-Time).  
- **Provenance traceability** (PROV-O / blockchain anchors).  
- **AI validation** (Focus AI drift & explainability tests).  
- **Ethical compliance** (CARE + governance audits).  
- **Energy & sustainability audits** under ISO 14064/50001.  

Temporary files here are **auto-cleaned nightly** via `clean-validation-tmp.yml`.

---

## 🧩 Validation Components Overview

| Component | Purpose | Output | Frequency | Retention |
|:--|:--|:--|:--|:--|
| `schema_tests/` | JSON-Schema & STAC checks | `schema_report.json` | Per ETL | 24 hrs |
| `provenance_checks/` | Verify PROV-O lineage links | `provenance_validation.jsonld` | Per ETL | 24 hrs |
