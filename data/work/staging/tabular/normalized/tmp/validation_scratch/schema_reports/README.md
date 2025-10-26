---
title: "📑 Kansas Frontier Matrix — TMP Validation Scratch: Schema Reports & STAC/DCAT Compliance Logs"
path: "data/work/staging/tabular/normalized/tmp/validation_scratch/schema_reports/README.md"
document_type: "Validation Reports · Schema Compliance and QA Output"
version: "v2.0.0"
last_updated: "2025-10-25"
review_cycle: "Continuous / Nightly STAC Validation"
commit_sha: "<latest-commit-hash>"
sbom_ref: "releases/v2.0.0/sbom.spdx.json"
manifest_ref: "releases/v2.0.0/manifest.zip"
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
owners: ["@kfm-validation", "@kfm-data-engineering"]
approvers: ["@kfm-qa", "@kfm-governance"]
status: "Active · FAIR+CARE+ISO Aligned"
maturity: "Stable"
mcp_version: "MCP-DL v6.3"
tags: ["Validation", "STAC", "DCAT", "Schema", "FAIR", "Provenance", "CIDOC CRM", "Quality Assurance"]
---

<div align="center">

# 📑 Kansas Frontier Matrix — **TMP Validation Scratch: Schema Reports & STAC/DCAT Compliance Logs**  
`data/work/staging/tabular/normalized/tmp/validation_scratch/schema_reports/README.md`

**Purpose:** Host auto-generated **schema validation outputs** for tabular and geospatial data temporarily staged in the **TMP Validation Scratch workspace**.  
These reports document all **schema compliance checks, error logs, and STAC/DCAT metadata verification results** across ETL workflows under the **Kansas Frontier Matrix (KFM)**.  

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../../../../../../docs/architecture/repo-focus.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Verified-lightblue)]()
[![ISO 19115](https://img.shields.io/badge/ISO--19115-Metadata-orange)]()
[![STAC 1.0](https://img.shields.io/badge/STAC--1.0-Compliant-green)]()
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

</div>

---

## 🗂️ Directory Layout

```plaintext
schema_reports/
├── stac_validation_reports/        # STAC 1.0 validation reports (per dataset)
│   ├── KS_TREATY_1867_03_MEDICINE_LODGE_report.json
│   ├── KS_TREATY_1853_01_KAW_TREATY_report.json
│   └── ...
├── dcat_validation_reports/        # DCAT 3.0 validation output for dataset catalog
│   ├── treaties_dataset_validation.json
│   └── ai_summary_dcat_validation.json
├── schema_error_logs/              # Human-readable log of validation errors/warnings
│   ├── errors_2025-10-25.log
│   └── summary_validation_failures.csv
├── qa_summary.json                 # Combined QA metrics for schema validations
├── validation_manifest.json        # Index of all validation outputs in this subdirectory
└── README.md                       # ← You are here
```

---

## 🧭 Overview

The **Schema Reports** directory forms the **analytical core** of TMP validation testing.  
Every dataset or document passing through the `tmp/validation_scratch/` workspace must undergo **schema validation** against the project’s canonical definitions:

- **STAC 1.0** for spatiotemporal asset metadata.  
- **DCAT 3.0** for dataset-level cataloging and FAIR discoverability.  
- **MCP-DL Data Schema v6.3** for tabular and provenance metadata validation.  
- **CIDOC CRM / OWL-Time ontology conformance** for entity-event relationships.

Reports stored here enable the governance and QA teams to **track data maturity**, **detect structural anomalies**, and **verify reproducibility** before promotion to the normalized repository.

---

## ⚙️ Validation Workflow

```mermaid
flowchart TD
    A[ETL Normalization Output] --> B[Schema Validator Engine]
    B --> C[STAC Validation Module]
    B --> D[DCAT Compliance Module]
    C --> E[Schema Reports (stac_validation_reports/)]
    D --> F[Schema Reports (dcat_validation_reports/)]
    E & F --> G[qa_summary.json + validation_manifest.json]
    G --> H[Governance Review + Ledger Registration]
```
%% END OF MERMAID %%

---

## 🧩 Report Specifications

### 1️⃣ STAC Validation Report Example

**File:** `stac_validation_reports/KS_TREATY_1867_03_MEDICINE_LODGE_report.json`

```json
{
  "dataset_id": "KS_TREATY_1867_03_MEDICINE_LODGE",
  "stac_version": "1.0.0",
  "validation_date": "2025-10-25T14:55:00Z",
  "validator": "stac-validator@v3.4",
  "checks_run": [
    "schema.json",
    "extensions/datetime.json",
    "extensions/provenance.json"
  ],
  "validation_results": {
    "passed": true,
    "errors": [],
    "warnings": ["Missing optional field 'providers'."]
  },
  "checksum_verification": "sha256:8892bcd9eab6d9914f8774a91a65c633a7a3b40b3de7...",
  "reviewer": "@kfm-validation"
}
```

---

### 2️⃣ DCAT Validation Report Example

**File:** `dcat_validation_reports/treaties_dataset_validation.json`

```json
{
  "@context": "https://www.w3.org/ns/dcat3#",
  "dataset_title": "Kansas Frontier Matrix – Treaty Metadata (Normalized)",
  "validation_engine": "dcat-validator@v1.5",
  "validation_timestamp": "2025-10-25T15:00:00Z",
  "ruleset": [
    "dcat:Dataset must include dct:identifier",
    "dcat:distribution must include mediaType"
  ],
  "results": {
    "passed": false,
    "errors": [
      "Missing 'dct:identifier' in 1 record.",
      "Invalid 'byteSize' type in distribution 2."
    ],
    "warnings": []
  },
  "corrective_action": "Re-run ETL transformation with DCAT schema patch (v3.0.1).",
  "reviewed_by": "@kfm-data-engineering"
}
```

---

### 3️⃣ Schema Error Log Example

**File:** `schema_error_logs/errors_2025-10-25.log`

```text
[2025-10-25 15:03:22] WARNING: Missing STAC 'keywords' field in treaty_1853_01_kaw.geojson.
[2025-10-25 15:03:23] ERROR: Invalid 'geometry' field type; expected Polygon, found MultiPolygon.
[2025-10-25 15:03:26] INFO: CIDOC CRM alignment check — passed for treaty_1867_03_medicine_lodge.json.
```

---

## 📈 QA Summary (Aggregate Metrics)

**File:** `qa_summary.json`

```json
{
  "report_date": "2025-10-25T15:10:00Z",
  "stac_validations": 84,
  "dcat_validations": 12,
  "stac_pass_rate": 0.976,
  "dcat_pass_rate": 0.917,
  "average_runtime_seconds": 3.4,
  "critical_failures": 1,
  "non_critical_warnings": 4,
  "validator_version": "v6.3",
  "generated_by": "@kfm-validation"
}
```

---

## 🔒 Governance and Audit Integration

Schema reports automatically link to:
- `/governance/ledger/validation/YYYY/MM/schema_audit.jsonld`
- `/data/work/staging/tabular/normalized/treaties/reports/validation/reports/`
- `/data/work/staging/tabular/normalized/treaties/reports/telemetry/metrics/`

Governance integration includes:
- **PROV-O linked audit trail** connecting validator → dataset → reviewer.  
- **SHA-256 checksum verification** for every report.  
- **Digital signing by Ethics and QA Council** during monthly audits.

### Example Governance Ledger Entry

```json
{
  "@context": "https://www.w3.org/ns/prov#",
  "@id": "urn:kfm:validation:schema:2025-10-25T15:00Z",
  "prov:wasGeneratedBy": "stac_validate.py",
  "prov:wasAttributedTo": "@kfm-validation",
  "prov:generatedAtTime": "2025-10-25T15:00:00Z",
  "prov:value": "STAC/DCAT compliance report batch validated.",
  "prov:wasAssociatedWith": "@kfm-governance"
}
```

---

## 🧾 FAIR+CARE Alignment Summary

| Principle | Implementation | Reference |
|------------|----------------|------------|
| **Findable** | Validation artifacts indexed in `validation_manifest.json`. | schema_reports/ |
| **Accessible** | JSON outputs accessible to internal CI/CD and governance dashboards. | qa_summary.json |
| **Interoperable** | Uses STAC 1.0 and DCAT 3.0 schemas for metadata exchange. | stac_validation_reports/, dcat_validation_reports/ |
| **Reusable** | Maintains open standard formats for reuse in external pipelines. | schema_error_logs/ |
| **CARE — Authority to Control** | QA audit logs reviewed by Indigenous data representatives. | governance ledger |

---

## 🧾 Version History

| Version | Date | Author | Reviewer | Notes |
|----------|------|---------|-----------|--------|
| v2.0.0 | 2025-10-25 | @kfm-validation | @kfm-governance | Introduced schema validation manifest, QA metrics, and STAC/DCAT examples. |
| v1.1.0 | 2025-10-24 | @kfm-data-engineering | @kfm-validation | Added CIDOC CRM ontology checks and STAC v1.0 extensions. |
| v1.0.0 | 2025-10-23 | @kfm-data-engineering | — | Initial schema validation report documentation. |

---

<div align="center">

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-lightblue)]()
[![STAC 1.0](https://img.shields.io/badge/STAC--1.0-Validated-green)]()
[![ISO 25012](https://img.shields.io/badge/ISO--25012-Data%20Quality%20Model-orange)]()
[![Governance Ledger](https://img.shields.io/badge/Ledger-Traceable-yellow)]()

</div>

