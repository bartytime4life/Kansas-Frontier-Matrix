---
title: "🔢 Kansas Frontier Matrix — Numeric Booleans (Boolean Inconsistency Subclass · Diamond⁹ Ω / Crown∞Ω Certified)"
path: "data/work/staging/tabular/tmp/intake/validation/quarantine/incoming/flagged_datasets/schema_errors/invalid_field_types/boolean_inconsistencies/numeric_booleans/README.md"
version: "v9.0.0"
last_updated: "2025-10-26"
status: "Active · FAIR+CARE+MCP-DL v6.3 Aligned"
review_cycle: "Continuous / Automated"
commit_sha: "<latest-commit-hash>"
manifest_ref: "releases/v9.0.0/manifest.zip"
telemetry_ref: "releases/v9.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/numeric-booleans-v13.json"
json_export: "releases/v9.0.0/numeric-booleans.meta.json"
linked_reports:
  - "reports/audit/numeric_booleans_audit.json"
  - "reports/fair/numeric_booleans_summary.json"
  - "governance/tabular_numeric_booleans_ledger.jsonld"
---

<div align="center">

# 🔢 Kansas Frontier Matrix — **Numeric Booleans**  
`data/work/staging/tabular/tmp/intake/validation/quarantine/incoming/flagged_datasets/schema_errors/invalid_field_types/boolean_inconsistencies/numeric_booleans/`

### *“Numbers pretending to be truth can only fool validation once.”*

**Purpose:**  
This directory stores datasets where boolean (true/false) fields were improperly encoded as numeric values (`1`, `0`, `-1`, etc.).  
Such inconsistencies violate JSON Schema definitions and lead to misinterpretation during AI, analytics, and provenance mapping.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../../../../../../../../../../../docs/architecture/repo-focus.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../../../../../../../../../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-orange)]()  
[![AI Detection](https://img.shields.io/badge/AI--Detection-Enabled-teal)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR-CARE-blueviolet)]()

</div>

---

## 🧭 Overview

The **Numeric Booleans Subdirectory** contains datasets automatically quarantined for using numerical substitutes for boolean values.  
Common invalid representations include:
- `1` and `0` instead of `true` / `false`
- `-1` as an undefined boolean placeholder  
- Fields declared as numeric type instead of boolean  
- Mixtures of numeric and literal boolean values in the same column  

The KFM AI validator and schema engine detect such violations, flag them, and automatically store affected datasets here for review.

---

## 🗂️ Directory Layout

```text
data/work/staging/tabular/tmp/intake/validation/quarantine/incoming/flagged_datasets/schema_errors/invalid_field_types/boolean_inconsistencies/numeric_booleans/
├── numeric_boolean_manifest.json        # Master record of numeric-boolean anomalies
├── ai_numeric_boolean_analysis.json     # AI-generated reasoning & confidence metrics
├── remediation_plan.json                # Suggested conversion mappings
├── examples/                            # CSV/JSON snippets illustrating numeric boolean misuse
│   ├── ks_property_1885_example.csv
│   ├── ks_census_1870_example.json
│   └── ks_agriculture_1890_example.csv
├── curator_notes.log                    # Curator comments and corrections
└── README.md                            # This document
````

---

## 🔁 Detection Workflow

```mermaid
flowchart TD
    A["Schema Validation: Boolean Field Check"] --> B{"Contains Numeric Value?"}
    B -- "Yes" --> C["Move Dataset → numeric_booleans/"]
    C --> D["AI Numeric Boolean Analyzer (LLM + Heuristic Rules)"]
    D --> E["Generate numeric_boolean_manifest.json"]
    E --> F["Curator Review + Correction (Mapping or Re-encoding)"]
    F --> G{"Validated Successfully?"}
    G -- "Yes ✅" --> H["Promote to Intake Layer"]
    G -- "No 🚫" --> I["Retain for Governance Audit"]
```

---

## 🧩 Manifest Schema

Each numeric boolean anomaly is registered in `numeric_boolean_manifest.json`:

| Field                    | Description                              | Example                                                                               |
| ------------------------ | ---------------------------------------- | ------------------------------------------------------------------------------------- |
| `dataset_id`             | Dataset identifier                       | `ks_agriculture_1890`                                                                 |
| `column_name`            | Column containing invalid boolean values | `has_irrigation`                                                                      |
| `invalid_values`         | List of invalid boolean encodings        | `[1, 0, -1]`                                                                          |
| `expected_values`        | Schema-compliant boolean literals        | `["true", "false"]`                                                                   |
| `ai_commentary`          | AI summary of the issue                  | `"Boolean field 'has_irrigation' uses numeric encoding instead of boolean literals."` |
| `remediation_suggestion` | Suggested fix                            | `"Convert values 1→true, 0→false"`                                                    |
| `ai_confidence`          | Confidence in classification             | `0.984`                                                                               |
| `timestamp`              | Detection time in UTC                    | `2025-10-26T14:52:18Z`                                                                |

---

## 🤖 AI Reasoning Engine

| AI Module                       | Function                                                        | Output                             |
| ------------------------------- | --------------------------------------------------------------- | ---------------------------------- |
| **AI Numeric Boolean Detector** | Identifies boolean columns containing numeric encodings.        | `numeric_boolean_manifest.json`    |
| **Pattern Profiler**            | Detects usage patterns (1/0, -1/1, 0/99, etc.) across datasets. | `ai_numeric_boolean_analysis.json` |
| **Auto-Remediator**             | Suggests explicit conversion logic and mapping expressions.     | `remediation_plan.json`            |
| **Confidence Engine**           | Assigns confidence levels for automated suggestions.            | `ai_numeric_boolean_analysis.json` |

> 🧠 *All AI-generated insights include confidence values, rationale, and provenance linkage to ensure transparency.*

---

## ⚙️ Curator Actions

Curators should:

1. Review detected numeric boolean anomalies and AI explanations.
2. Apply suggested mappings or manually adjust data type conversions.
3. Record all updates in `curator_notes.log`.
4. Execute:

   ```bash
   make revalidate-flagged
   ```
5. Ensure corrected datasets are promoted to the validated intake directory.

---

## 🧾 Compliance Matrix

| Standard                 | Scope                                   | Validator       |
| ------------------------ | --------------------------------------- | --------------- |
| **JSON Schema Draft-07** | Type and enum validation                | `jsonschema`    |
| **FAIR+CARE**            | Ethical and transparent data handling   | `fair-audit`    |
| **CIDOC CRM / PROV-O**   | Provenance and process tracking         | `graph-lint`    |
| **MCP-DL v6.3**          | Documentation-driven reproducibility    | `docs-validate` |
| **ISO 19115 / 19157**    | Metadata lineage and quality management | `geojson-lint`  |

---

## 🪶 Version History

| Version | Date       | Author              | Notes                                                                                        |
| ------- | ---------- | ------------------- | -------------------------------------------------------------------------------------------- |
| v9.0.0  | 2025-10-26 | `@kfm-architecture` | Initial creation of Numeric Booleans documentation under Diamond⁹ Ω / Crown∞Ω certification. |

---

<div align="center">

### 🜂 Kansas Frontier Matrix — *Logic · Integrity · Transparency*

**“1 and 0 are not truth — only clear documentation makes them real.”**

[![Build & Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/validate.yml?label=Build+%26+Validate)]()
[![AI Analyzer](https://img.shields.io/badge/AI%20Analyzer-Operational%20✓-teal)]()
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger%20Linked-blueviolet)]()
[![Integrity Check](https://img.shields.io/badge/Integrity-Verified-lightgrey)]()
[![FAIR+CARE](https://img.shields.io/badge/FAIR-CARE-green)]()

<br><br> <a href="#-kansas-frontier-matrix--numeric-booleans-boolean-inconsistency-subclass--diamond⁹-Ω--crown∞Ω-certified">⬆ Back to Top</a>

</div>
