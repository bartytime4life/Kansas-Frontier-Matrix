---
title: "⚠️ Kansas Frontier Matrix — AI Validation Error Schema Summary"
path: "data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/reports/error_schema_summary.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Continuous / Automated"
status: "Active · FAIR+CARE+ISO Tracked"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-validation", "@kfm-ai", "@kfm-data"]
approvers: ["@kfm-architecture", "@kfm-governance", "@kfm-security"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - CIDOC CRM / PROV-O / OWL-Time
  - ISO 9001 / 19115 / 27001 / 50001 / 14064
tags: ["ai","validation","errors","logs","audit","ontology","fair","cidoc","prov-o","iso","governance"]
---

<div align="center">

# ⚠️ Kansas Frontier Matrix — **AI Validation Error Schema Summary**
`data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/reports/error_schema_summary.md`

**Purpose:** Summarize **schema-related validation errors** detected during AI validation runs.  
This report provides structured visibility into recurring schema mismatches, field violations, and ontology inconsistencies under FAIR+CARE and ISO governance standards.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![Error Summary](https://img.shields.io/badge/Validation-Error%20Summary-ff4d4f)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Tracked-2ecc71)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-d4af37)]()

</div>

---

## 📚 Overview

This **Error Schema Summary** aggregates and classifies all schema-level issues identified across AI validation pipelines.  
These include:
- Invalid JSON structure or missing required fields  
- Schema mismatch against reference templates (STAC / DCAT / CIDOC CRM)  
- Semantic ontology violations (PROV-O / OWL-Time)  
- FAIR+CARE scoring anomalies  
- Energy logging discrepancies or incomplete telemetry  

> 🧩 *Each recorded error is associated with its originating validation log and tracked for trend analysis, impact assessment, and governance review.*

---

## 🗂️ Directory Context

```
data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/reports/
├── error_schema_summary.md
├── schema_error_registry.json
├── schema_error_trends.json
├── checksums.sha256
└── provenance_links.jsonld
```

---

## 🧩 Summary Metrics (as of 2025-10-24)

| Metric | Count | Change (30d) | Status |
| :------ | :------ | :------ | :------ |
| Total Validation Runs | 128 | +4.8% | ✅ |
| Schema Errors Detected | 12 | -18.0% | 🟢 |
| CIDOC Alignment Errors | 3 | -25.0% | 🟢 |
| PROV-O Reference Errors | 2 | -33.0% | 🟢 |
| FAIR/CARE Audit Deviations | 1 | Stable | ⚠️ |
| Telemetry/ISO Energy Logging Issues | 0 | -100% | ✅ |
| Ledger Sync Failures | 0 | Stable | ✅ |

---

## 🧠 Common Schema Violations

| Error Type | Frequency | Severity | Ontology / Schema | Notes |
| :----------- | :---------- | :---------- | :---------- | :---------- |
| Missing Required Fields | 5 | Moderate | JSON Schema (STAC/DCAT) | Often due to incomplete metadata ingestion. |
| Invalid Temporal Format | 3 | High | OWL-Time | Incorrect ISO 8601 date patterns detected. |
| Broken Ontology Link | 2 | High | CIDOC CRM / PROV-O | Missing `E52_Time-Span` references. |
| FAIR Metadata Incomplete | 1 | Moderate | FAIR+CARE Schema | Missing “authority_to_control” property. |
| Telemetry Field Omitted | 1 | Low | ISO 50001 | EnergyWh data not written to validation report. |

---

## 🧾 Example Error Trace (`schema_error_registry.json` excerpt)

```json
{
  "errors": [
    {
      "error_id": "SCHEMA-ERR-2025-10-24-001",
      "timestamp": "2025-10-24T17:10:00Z",
      "file": "../logs/validation_run_2025-10-24.log",
      "error_type": "Missing Required Field",
      "field": "checksum_verified",
      "schema_ref": "../schemas/validation_log.schema.json",
      "severity": "moderate",
      "status": "resolved",
      "resolved_by": "@kfm-validation",
      "resolution_timestamp": "2025-10-24T17:40:00Z"
    },
    {
      "error_id": "SCHEMA-ERR-2025-10-24-002",
      "timestamp": "2025-10-24T17:11:00Z",
      "file": "../reports/ai_validation_report_2025-10-24.json",
      "error_type": "Invalid Temporal Format",
      "field": "timestamp",
      "schema_ref": "../schemas/validation_log.schema.json",
      "severity": "high",
      "status": "open"
    }
  ]
}
```

---

## ⚙️ Workflow Diagram

```mermaid
flowchart TD
    A[AI Validation Logs] --> B[Schema Validation Engine]
    B --> C[Error Detection & Classification]
    C --> D[Ontology Audit (CIDOC CRM / PROV-O)]
    D --> E[Governance Ledger Registration]
    E --> F[Summary Report Generation]
```

---

## 🔗 Provenance JSON-LD (`provenance_links.jsonld`)

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "crm": "http://www.cidoc-crm.org/cidoc-crm/",
    "fair": "https://purl.org/fair/"
  },
  "@id": "prov:error_schema_summary_2025-10-24",
  "prov:wasGeneratedBy": "process:ai-validation-error-analysis-pipeline-v2",
  "prov:used": [
    "../schemas/validation_log.schema.json",
    "../logs/validation_run_2025-10-24.log"
  ],
  "prov:generatedAtTime": "2025-10-24T17:20:00Z",
  "prov:qualifiedAttribution": {
    "prov:agent": "@kfm-validation",
    "prov:role": "error_auditor"
  },
  "fair:ledger_hash": "f9b3c7d8e2..."
}
```

---

## ✅ Corrective Actions Summary

| Issue | Action Taken | Responsible | Date |
| :------ | :------ | :------ | :------ |
| Missing checksum field | Schema update to enforce validation checks | @kfm-validation | 2025-10-24 |
| Invalid timestamp format | Added regex validator for ISO 8601 | @kfm-ai | 2025-10-24 |
| FAIR metadata omission | FAIR+CARE template expanded | @kfm-data | 2025-10-23 |

---

## 🧩 FAIR+CARE & ISO Review Status

| Standard | Domain | Compliance | Reviewer |
| :-------- | :-------- | :----------- | :----------- |
| **FAIR+CARE** | Ethical data handling & error traceability | ✅ | @kfm-ethics |
| **CIDOC CRM / PROV-O / OWL-Time** | Semantic error mapping | ✅ | @kfm-ontology |
| **ISO 9001 / 27001** | Validation quality control | ✅ | @kfm-governance |
| **ISO 50001 / 14064** | Energy & sustainability logging | ✅ | @kfm-sustainability |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Created AI Validation Error Schema Summary with FAIR+CARE audit, ontology traceability, and corrective action registry. | @kfm-validation |

---

<div align="center">

[![Error Summary](https://img.shields.io/badge/Validation-Error%20Summary-ff4d4f?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Tracked-2ecc71?style=flat-square)]()
[![Ontology](https://img.shields.io/badge/Ontology-CIDOC%20CRM%20%7C%20PROV--O%20%7C%20OWL--Time-8a2be2?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%202701%20%7C%2050001-229954?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · AI Validation Error Schema Summary
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/ai/logs/errors/validation/reports/error_schema_summary.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
ISO-ALIGNED: true
PROVENANCE-LINKED: true
ERRORS-TRACKED: true
CORRECTIVE-ACTIONS-DOCUMENTED: true
GOVERNANCE-LEDGER-LINKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->