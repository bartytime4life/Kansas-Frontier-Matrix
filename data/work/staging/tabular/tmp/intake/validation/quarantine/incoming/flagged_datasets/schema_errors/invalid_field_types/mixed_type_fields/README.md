---
title: "🧩 Kansas Frontier Matrix — Mixed-Type Fields (Invalid Field Type Subclass · Diamond⁹ Ω / Crown∞Ω Certified)"
path: "data/work/staging/tabular/tmp/intake/validation/quarantine/incoming/flagged_datasets/schema_errors/invalid_field_types/mixed_type_fields/README.md"
version: "v9.0.0"
last_updated: "2025-10-26"
status: "Active · FAIR+CARE+MCP-DL v6.3 Aligned"
review_cycle: "Continuous / Automated Validation"
commit_sha: "<latest-commit-hash>"
manifest_ref: "releases/v9.0.0/manifest.zip"
telemetry_ref: "releases/v9.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/mixed-type-fields-v13.json"
json_export: "releases/v9.0.0/mixed-type-fields.meta.json"
linked_reports:
  - "reports/audit/mixed_type_fields_audit.json"
  - "reports/fair/mixed_type_fields_summary.json"
  - "governance/tabular_mixed_type_fields_ledger.jsonld"
---

<div align="center">

# 🧩 Kansas Frontier Matrix — **Mixed-Type Fields**  
`data/work/staging/tabular/tmp/intake/validation/quarantine/incoming/flagged_datasets/schema_errors/invalid_field_types/mixed_type_fields/`

### *“When a field tells too many stories, validation brings order to the narrative.”*

**Purpose:**  
This directory contains datasets where **individual columns contain multiple data types** (e.g., a mix of strings, numbers, booleans, or dates).  
Such inconsistencies disrupt schema validation, AI reasoning, and knowledge graph integration within the Kansas Frontier Matrix (KFM).

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../../../../../../../../docs/architecture/repo-focus.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../../../../../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-orange)]()  
[![AI Detection](https://img.shields.io/badge/AI--Detection-Operational%20✓-teal)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR-CARE-blueviolet)]()

</div>

---

## 🧭 Overview

The **Mixed-Type Fields Subdirectory** isolates datasets that violate type uniformity within single columns.  
This problem is particularly common when tabular data originates from OCR, user-entered spreadsheets, or inconsistent ETL transformations.  
Common issues include:
- Numeric and text values in the same field (`"25"`, `"unknown"`, `"NULL"`)  
- Boolean and integer mixing (`true`, `0`, `1`, `"false"`)  
- Temporal and text mixing (`"2025-10-26"`, `"October 26"`)  
- Heterogeneous categorical encodings (`"A"`, `1`, `"missing"`)  

Such inconsistencies lead to schema conflicts, AI model confusion, and loss of data integrity during graph ingestion.

---

## 🗂️ Directory Layout

```text
data/work/staging/tabular/tmp/intake/validation/quarantine/incoming/flagged_datasets/schema_errors/invalid_field_types/mixed_type_fields/
├── mixed_type_manifest.json           # Master manifest of mixed-type field anomalies
├── ai_mixed_type_diagnostics.json     # AI-generated field type distribution & reasoning
├── remediation_plan.json              # Curator & AI suggestions for normalization
├── examples/                          # CSV/JSON snippets illustrating mixed-type issues
│   ├── ks_census_1880_example.csv
│   ├── ks_property_1890_example.json
│   └── ks_taxrolls_1900_example.csv
├── curator_notes.log                  # Manual curator notes and resolution tracking
└── README.md                          # This document
````

---

## 🔁 Detection Workflow

```mermaid
flowchart TD
    A["Schema Validator: Field Type Uniformity Check"] --> B{"Multiple Data Types Detected?"}
    B -- "Yes ❌" --> C["Move Dataset → mixed_type_fields/"]
    C --> D["AI Type Profiler (Statistical + LLM Classification)"]
    D --> E["Generate Manifest → mixed_type_manifest.json"]
    E --> F["AI Suggests Field Normalization Plan"]
    F --> G["Curator Review + Data Correction"]
    G --> H{"Schema Revalidated Successfully?"}
    H -- "Yes ✅" --> I["Return to Intake Layer"]
    H -- "No 🚫" --> J["Retain for Governance Audit"]
```

---

## 🧩 Manifest Schema

Each record in `mixed_type_manifest.json` provides contextual metadata for the field-level anomaly:

| Field                    | Description                                | Example                                                                                              |
| ------------------------ | ------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `dataset_id`             | Dataset name                               | `ks_census_1880`                                                                                     |
| `column_name`            | Mixed-type field                           | `population_density`                                                                                 |
| `detected_types`         | Data types present in the column           | `["integer", "string", "null"]`                                                                      |
| `dominant_type`          | Most frequent valid data type              | `"integer"`                                                                                          |
| `inconsistent_ratio`     | Percent of records violating dominant type | `0.12`                                                                                               |
| `ai_explanation`         | LLM commentary on anomaly                  | `"Column 'population_density' includes both numeric and textual values such as 'unknown' or 'N/A'."` |
| `remediation_suggestion` | Recommended fix                            | `"Replace non-numeric text with null or convert entire column to string type."`                      |
| `timestamp`              | Detection time (UTC)                       | `2025-10-26T15:06:48Z`                                                                               |

---

## 🤖 AI Type Profiler

| AI Module              | Function                                               | Output                                    |
| ---------------------- | ------------------------------------------------------ | ----------------------------------------- |
| **Type Classifier**    | Detects non-uniform data types within columns          | `mixed_type_manifest.json`                |
| **Value Analyzer**     | Identifies typical outliers and non-conforming entries | `ai_mixed_type_diagnostics.json`          |
| **Normalizer Planner** | Suggests coercion or conversion rules per field        | `remediation_plan.json`                   |
| **Semantic Evaluator** | Links mixed-type issues to schema-level semantics      | `tabular_mixed_type_fields_ledger.jsonld` |

> 🧠 *AI modules are fully explainable under MCP-DL principles, providing reasoning trails and reproducible detection steps.*

---

## ⚙️ Curator Workflow

Curators must:

1. Review each field flagged in `mixed_type_manifest.json`.
2. Assess the AI’s remediation recommendations.
3. Apply conversions (type coercion, replacement, or null standardization).
4. Record remediation details in `curator_notes.log`.
5. Execute revalidation:

   ```bash
   make revalidate-flagged
   ```
6. Confirm schema conformance and governance ledger update.

---

## 📈 Example Anomaly Patterns

| Category              | Invalid Examples               | Corrected Output                 |
| --------------------- | ------------------------------ | -------------------------------- |
| **Numeric + Text**    | `"45"`, `"unknown"`, `"NULL"`  | `45`, `null`, `null`             |
| **Boolean + Integer** | `true`, `0`, `1`, `"false"`    | `true`, `false`, `true`, `false` |
| **Date + Text**       | `"2025-10-26"`, `"October 26"` | `"2025-10-26"`                   |
| **Categorical Mix**   | `"A"`, `1`, `"missing"`        | `"A"`, `"1"`, `"missing"`        |

---

## 🧾 Compliance Matrix

| Standard                 | Scope                               | Validator       |
| ------------------------ | ----------------------------------- | --------------- |
| **JSON Schema Draft-07** | Field type validation and coercion  | `jsonschema`    |
| **FAIR+CARE**            | Ethical and documentation alignment | `fair-audit`    |
| **CIDOC CRM / PROV-O**   | Provenance traceability             | `graph-lint`    |
| **MCP-DL v6.3**          | Documentation-first reproducibility | `docs-validate` |
| **STAC / DCAT 3.0**      | Metadata interoperability           | `stac-validate` |

---

## 🪶 Version History

| Version | Date       | Author              | Notes                                                                                         |
| ------- | ---------- | ------------------- | --------------------------------------------------------------------------------------------- |
| v9.0.0  | 2025-10-26 | `@kfm-architecture` | Initial creation of Mixed-Type Fields documentation under Diamond⁹ Ω / Crown∞Ω certification. |

---

<div align="center">

### 🜂 Kansas Frontier Matrix — *Uniformity · Integrity · Provenance*

**“When columns speak many dialects, schema validation ensures a common tongue.”**

[![Build & Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/validate.yml?label=Build+%26+Validate)]()
[![AI Detection](https://img.shields.io/badge/AI%20Type%20Profiler-Active%20✓-teal)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-blueviolet)]()
[![Integrity Verification](https://img.shields.io/badge/Integrity-Verified-lightgrey)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR-CARE-green)]()

<br><br> <a href="#-kansas-frontier-matrix--mixed-type-fields-invalid-field-type-subclass--diamond⁹-Ω--crown∞Ω-certified">⬆ Back to Top</a>

</div>
