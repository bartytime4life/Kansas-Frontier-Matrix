---
title: "✅ Kansas Frontier Matrix — Treaty Reports Validation Module"
path: "data/work/staging/tabular/normalized/treaties/reports/validation/README.md"
version: "v1.0.0"
last_updated: "2025-10-24"
review_cycle: "Continuous / Pre-Deployment"
status: "Active · FAIR+CARE+ISO Validated"
mcp_version: "MCP-DL v6.4.3"
maintainers: ["@kfm-data", "@kfm-validation", "@kfm-treaties"]
approvers: ["@kfm-architecture", "@kfm-governance", "@kfm-ethics"]
license: ["MIT (code)", "CC-BY 4.0 (data/docs)"]
alignment:
  - FAIR / CARE
  - STAC / DCAT
  - CIDOC CRM / OWL-Time / PROV-O
  - ISO 19115 / 9001 / 27001
tags: ["validation","treaties","reports","schema","semantic","quality","audit","fair","cidoc","owl-time","stac"]
---

<div align="center">

# ✅ Kansas Frontier Matrix — **Treaty Reports Validation Module**
`data/work/staging/tabular/normalized/treaties/reports/validation/README.md`

**Purpose:** Perform full **schema, semantic, and provenance validation** of treaty reports before archival and governance ledger registration.  
This module ensures that all reports adhere to **FAIR+CARE**, **ISO**, and **CIDOC CRM** data integrity standards.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)]()
[![Validation](https://img.shields.io/badge/Validation-Schema%20%2B%20Semantic-6f42c1)]()
[![License](https://img.shields.io/badge/License-MIT%20%7C%20CC--BY%204.0-green)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Validated-2ecc71)]()
[![ISO Certified](https://img.shields.io/badge/ISO-9001%20%7C%201915%20%7C%202701-229954)]()

</div>

---

## 📚 Overview

The **Treaty Reports Validation Module** is the critical checkpoint between AI-generated output (`reports/ai/`) and archival inclusion (`reports/archive/`).  
It validates every report, metadata file, and provenance record for **completeness**, **semantic integrity**, and **standard compliance**.

Validation ensures:
- Data consistency across all treaty datasets.  
- STAC/DCAT schema conformance.  
- Proper CIDOC CRM and OWL-Time mappings.  
- Provenance traceability (PROV-O).  
- FAIR+CARE and ISO documentation compliance.

---

## 🧩 Directory Layout

```
data/work/staging/tabular/normalized/treaties/reports/validation/
├── logs/                        # Validation execution logs
├── reports/                     # Validation result outputs per file
├── schemas/                     # JSON / SHACL validation schemas
├── provenance/                  # Provenance validation results
├── stac/                        # STAC/DCAT validation outputs
└── summary/                     # Aggregated validation summary and scorecards
```

---

## 🧠 Validation Workflow

```mermaid
flowchart TD
    A[AI Treaty Reports] --> B[Schema Validation (STAC/DCAT)]
    B --> C[Semantic Validation (CIDOC CRM / OWL-Time)]
    C --> D[Provenance Validation (PROV-O)]
    D --> E[Quality Scoring + FAIR Metrics]
    E --> F[Validation Report + Summary Output]
    F --> G[data/work/staging/tabular/normalized/treaties/reports/archive/]
```

---

## 🧪 Validation Types

| Validation Type | Description | Tool | Output | Status |
| :---------------- | :------------ | :------ | :--------- | :-------- |
| **Schema** | Checks JSON, CSV, and STAC/DCAT structure | `jsonschema-cli` | `schema_validation.json` | ✅ Active |
| **Semantic** | Verifies ontology alignment (CIDOC, OWL-Time) | `pyshacl` | `semantic_validation.json` | ✅ Active |
| **Provenance** | Ensures proper PROV-O linkages | `rdflib` | `provenance_validation.jsonld` | ✅ Active |
| **Checksum** | Confirms SHA-256 consistency | `sha256sum` | `checksum.log` | ✅ Active |
| **A11y** | Tests accessibility of generated Markdown | `md-lint` | `a11y_validation.json` | ⚙ Planned |

---

## 📋 Validation Schema Definitions

| Schema File | Scope | Description |
| :------------- | :-------- | :------------- |
| `treaty_report.schema.json` | Markdown/JSON reports | Structural integrity of generated outputs |
| `treaty_metadata.schema.json` | STAC/DCAT | Field conformity and required metadata |
| `treaty_provenance.shacl` | Provenance | Ontological linkage (PROV-O compliance) |
| `validation_summary.schema.json` | Summary report | Aggregated pass/fail results |
| `checksum_manifest.schema.json` | Integrity | Cryptographic verification format |

---

## 📈 Metrics and Thresholds

| Metric | Target | Description |
| :------ | :------ | :------------- |
| `schema_pass_rate` | ≥ 99% | Successful schema validations |
| `semantic_alignment_score` | ≥ 95% | CIDOC/OWL-Time compliance |
| `provenance_completeness` | 100% | Provenance chains linked |
| `checksum_integrity` | 100% | File verification |
| `fair_validation_score` | ≥ 90 | FAIR principles compliance |
| `a11y_score` | ≥ 95 | Accessibility validation |

---

## 🔐 Validation Rules

- Each treaty report must include:
  - Valid STAC/DCAT JSON metadata.  
  - CIDOC CRM entity mappings (Person, Place, Event).  
  - OWL-Time temporal structure.  
  - Provenance linkage via `wasDerivedFrom` and `generatedAtTime`.  
  - A checksum entry in `checksums/treaty_checksums.json`.  
- Validation fails if any metadata fields are missing or undefined.  
- All results are logged to `reports/*.json` and integrated with CI/CD.

---

## ⚙️ Configuration Parameters

| Parameter | Description | Default |
| :--------- | :------------ | :--------- |
| `VALIDATION_MODE` | `strict` or `relaxed` validation schema enforcement | `strict` |
| `OUTPUT_FORMAT` | Output format for reports (`json`, `md`, `html`) | `json` |
| `MAX_ERRORS` | Maximum allowed non-critical warnings | `10` |
| `ENABLE_A11Y` | Toggle accessibility validation | `true` |
| `REPORT_SUMMARY` | Generate summary file | `true` |

---

## 🧩 Governance Integration

| System | Integration Type | Artifact |
| :------- | :---------------- | :---------- |
| FAIR Ledger | Telemetry and validation metrics | `fair_validation.json` |
| Governance Ledger | Immutable validation log | `validation_manifest.json` |
| Ethics Ledger | Checks for bias in AI reports | `ethics_validation.json` |
| Archive Module | Receives validated outputs | `validation_summary.json` |

---

## 🧾 Validation Summary Output (Example)

```json
{
  "run_id": "VAL-2025-10-24-001",
  "timestamp": "2025-10-24T11:45:00Z",
  "total_files": 142,
  "schema_pass_rate": 99.3,
  "semantic_alignment_score": 96.8,
  "provenance_completeness": 1.0,
  "checksum_integrity": 1.0,
  "fair_validation_score": 92.4,
  "a11y_score": 97,
  "overall_status": "pass"
}
```

---

## ✅ Compliance Matrix

| Standard | Domain | Compliance |
| :-------- | :-------- | :----------- |
| **FAIR+CARE** | Ethical data governance | ✅ |
| **MCP-DL v6.4.3** | Documentation alignment | ✅ |
| **STAC/DCAT 3.0** | Metadata structure | ✅ |
| **CIDOC CRM / OWL-Time** | Semantic model | ✅ |
| **PROV-O** | Provenance ontology | ✅ |
| **ISO 19115 / 9001 / 27001** | Data quality + security | ✅ |

---

## 🗓️ Version History

| Version | Date | Changes | Author |
| :------ | :---- | :-------- | :------ |
| v1.0.0 | 2025-10-24 | Created initial validation module documentation for treaty reporting workflow. | @kfm-data |

---

<div align="center">

[![Validation](https://img.shields.io/badge/Validation-Schema%20%26%20Semantic-6f42c1?style=flat-square)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-Compliant-2ecc71?style=flat-square)]()
[![ISO Standards](https://img.shields.io/badge/ISO-9001%20%7C%201915%20%7C%202701-229954?style=flat-square)]()
[![STAC/DCAT](https://img.shields.io/badge/Metadata-STAC%20%7C%20DCAT-8a2be2?style=flat-square)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Immutable%20Linked-d4af37?style=flat-square)]()

</div>

<!-- MCP-FOOTER-BEGIN
MCP-VERSION: v6.4.3
MCP-TIER: Silver · Validation
DOC-PATH: data/work/staging/tabular/normalized/treaties/reports/validation/README.md
MCP-CERTIFIED: true
FAIR-CARE-COMPLIANT: true
STAC-COMPLIANT: true
SEMANTIC-VALIDATED: true
PROVENANCE-LINKED: true
ISO-ALIGNED: true
VALIDATION-MODULE: true
GOVERNANCE-LEDGER-LINKED: true
GENERATED-BY: KFM-Automation/DocsBot
LAST-VALIDATED: 2025-10-24
MCP-FOOTER-END -->