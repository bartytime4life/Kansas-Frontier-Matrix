<div align="center">

# ✅ Kansas Frontier Matrix — Tabular Validation Workspace  
`data/work/staging/tabular/validation/`

**“Trust, verify, and document every dataset.”**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧭 Purpose

The `validation/` layer provides **data-quality assurance checkpoints** between *normalized CSVs*
(`../normalized/`) and finalized outputs (`../../processed/`).  
It captures:

- JSON-Schema and CSVW conformance reports  
- Field-type and unit checks  
- Null and range anomaly detection  
- SHA-256 checksum generation and diff logs  
- MCP-compliant provenance metadata (commit, timestamp, inputs/outputs)

Every report here functions as an **evidence trail** for reproducibility audits and CI validation.

---

## 🧩 Workflow Integration

```mermaid
flowchart TD
  A["data/work/staging/tabular/normalized/*.csv"] --> B["Schema Validator\n(JSON-Schema, CSVW)"]
  B --> C["Reports\n(validation/*.json)"]
  B --> D["Checksums\n(checksums/*.sha256)"]
  C --> E["data/work/staging/tabular/joins/"]
  D --> E
  E --> F["data/processed/\nvalidated CSVs → STAC Items"]
%% END OF MERMAID
````

**Automation:**
Triggered automatically during `make tabular-validate` or as part of `make data`.
Each validation stage logs results to a timestamped JSON file and appends summaries to `summary.log`.

---

## 📁 Directory Layout

```bash
data/work/staging/tabular/validation/
├── README.md                 # This file
├── schemas/                  # JSON-Schema definitions per dataset
├── reports/                  # Validation reports (JSON)
├── checksums/                # SHA-256 manifests
├── summary.log               # Aggregated ETL validation log
└── tmp/                      # Temporary working files (ignored by Git)
```

---

## ⚙️ Usage

```bash
# Validate all normalized CSVs
make tabular-validate

# Re-run schema checks for a specific dataset
python scripts/validate_csv.py --schema schemas/ks_climate.schema.json --input ../normalized/ks_climate.csv

# Regenerate checksum manifest
make checksums
```

Outputs:

* `reports/<dataset>_validation.json` — field-level QA results
* `checksums/<dataset>.sha256` — integrity hash
* `summary.log` — aggregated run summary

---

## 🧾 Standards

| Standard           | Purpose                                |
| ------------------ | -------------------------------------- |
| **CSVW**           | Column metadata & datatypes            |
| **JSON-Schema**    | Field-level validation                 |
| **STAC**           | Connects QA results to catalog entries |
| **DCAT**           | Dataset metadata harmonization         |
| **MCP Provenance** | Commit-based traceability              |

---

## 🔍 Provenance & Integrity

Each dataset validated here receives a provenance block appended to its metadata:

```json
{
  "validated_at": "2025-10-09T00:00:00Z",
  "validated_by": "scripts/validate_csv.py",
  "etl_commit": "{{ GIT_COMMIT }}",
  "checksums": "checksums/<dataset>.sha256",
  "validation_report": "reports/<dataset>_validation.json",
  "status": "passed"
}
```

---

## 🧠 Related Documentation

* [Tabular Staging Overview](../README.md)
* [ETL SOP](../../../../../docs/sop.md)
* [Architecture Overview](../../../../../docs/architecture.md)
* [STAC Catalog](../../../../stac/catalog.json)

---

## 🪪 License

Validation scripts and reports are distributed under **CC-BY-4.0**.
Reusers must credit *Kansas Frontier Matrix* when redistributing validation results.
