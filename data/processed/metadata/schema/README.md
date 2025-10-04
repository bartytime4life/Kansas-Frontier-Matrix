<div align="center">

# 🧩 Kansas-Frontier-Matrix — Processed Metadata Schemas (`data/processed/metadata/schema/`)

**Mission:** Define and maintain the **schema standards** that govern all processed dataset metadata  
across the Kansas Frontier Matrix — ensuring consistency, validation, and compliance with  
**STAC 1.0** and the **Master Coder Protocol (MCP)** for transparent, reproducible science.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Schema Files](#schema-files)
- [Validation Process](#validation-process)
- [Schema Compliance Rules](#schema-compliance-rules)
- [Extending the Schema](#extending-the-schema)
- [References](#references)

---

## 🧠 Overview

This directory houses the **metadata schema definitions** used to validate all processed dataset  
metadata (`data/processed/metadata/`). Each schema enforces required fields, typing rules,  
and controlled vocabularies to maintain a consistent and auditable metadata framework.

Schemas are aligned with:
- **STAC 1.0.0** — SpatioTemporal Asset Catalog standard for geospatial data.  
- **MCP Provenance Model** — scientific reproducibility and documentation-first requirements.  
- **JSON Schema Draft 2020-12** — for machine validation and schema evolution tracking.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── metadata/
        └── schema/
            ├── processed_item.schema.json      # Core metadata schema for processed datasets
            ├── stac_item.schema.json           # Reference schema for STAC 1.0 item compliance
            ├── validation_rules.json           # Supplemental MCP-specific validation rules
            ├── examples/
            │   ├── valid_metadata_example.json
            │   └── invalid_metadata_example.json
            └── README.md
````

Each JSON Schema file is version-controlled and used by automated validation workflows
to test all metadata files prior to publication or CI/CD deployment.

---

## 🧩 Schema Files

### `processed_item.schema.json`

Defines the **core MCP metadata schema** for all processed datasets.
It extends the STAC 1.0.0 `Item` model with additional MCP-specific fields for provenance, software, and lineage.

**Key Sections:**

* `properties.id` — Unique dataset identifier.
* `properties.mcp_provenance` — Required SHA-256 checksum reference.
* `properties.processing:software` — Description of processing tools and versions.
* `properties.derived_from` — Explicit lineage reference to parent datasets.
* `properties.license` — License key (`"CC-BY 4.0"`, `"MIT"`, etc.).
* `properties.spatial_extent` and `properties.temporal_extent` — bounding box and date range.

### `stac_item.schema.json`

Provides the **STAC 1.0.0 baseline schema**, ensuring all metadata remain
interoperable with external catalog services and mapping APIs.

Used to cross-check:

* STAC-required fields (`id`, `stac_version`, `type`, `assets`, `properties`).
* STAC optional extensions (e.g., EO, SAR, Scientific extensions).
* Asset metadata fields and roles.

### `validation_rules.json`

Contains supplemental **MCP-specific constraints** not expressible in JSON Schema alone.
These include:

* Regex patterns for dataset IDs (`^[a-z0-9_]+$`).
* File-extension consistency checks (e.g., `.tif`, `.geojson`, `.csv`).
* Required linkage between metadata `id` and file path.
* Hash verification logic ensuring `.sha256` existence.
* Conditional validation for temporal coverage fields.

---

## ⚙️ Validation Process

Validation is automated through the repository’s CI/CD pipelines and local Makefile targets.
When a contributor adds or modifies metadata, the schema validation is triggered automatically.

### Run locally

```bash
# Validate all processed metadata
make validate-metadata

# Validate a specific metadata file
python tools/validate_json.py data/processed/metadata/terrain/dem_1m_ks_filled.json
```

### Automated CI

The GitHub Action `.github/workflows/stac-validate.yml` performs:

1. JSON Schema validation (`processed_item.schema.json`)
2. STAC compliance validation (`stac_item.schema.json`)
3. Provenance and checksum matching (`validation_rules.json`)

Results are summarized in `validation_report.json`.

---

## 🧾 Schema Compliance Rules

| Rule Type                 | Description                                                            | Enforced By                  |
| ------------------------- | ---------------------------------------------------------------------- | ---------------------------- |
| **Required Fields**       | `id`, `title`, `datetime`, `mcp_provenance`, `derived_from`, `license` | `processed_item.schema.json` |
| **Checksum Integrity**    | SHA-256 hash must match dataset `.sha256` file                         | `validation_rules.json`      |
| **Cross-Link Validation** | Each dataset must have valid STAC item linkage                         | `stac_item.schema.json`      |
| **License Check**         | Must use approved open licenses (CC-BY 4.0, MIT, PDDL, etc.)           | `validation_rules.json`      |
| **Naming Conventions**    | IDs lowercase snake_case; filenames match dataset IDs                  | `validation_rules.json`      |
| **Date Consistency**      | `datetime` within `temporal_extent`                                    | MCP Validator                |
| **Provenance Chain**      | Each `derived_from` dataset must exist                                 | MCP Validator                |

Violations trigger validation failure, halting the CI/CD pipeline until resolved.

---

## 🧩 Extending the Schema

To introduce new schema elements or domain-specific extensions:

1. Duplicate and version the current schema (e.g., `processed_item.schema.v2.json`).
2. Add new field definitions under `properties`.
3. Update `$id` and `$schema` URIs for version traceability.
4. Document all new fields in `docs/standards/schema_changes.md`.
5. Validate example metadata in `examples/` before production rollout.

Schemas should remain **backward-compatible** with prior MCP releases whenever possible.

---

## 📖 References

* **STAC Specification 1.0.0:** [https://stacspec.org](https://stacspec.org)
* **JSON Schema Draft 2020-12:** [https://json-schema.org](https://json-schema.org)
* **ISO 19115 Metadata Standard:** [https://www.iso.org/standard/53798.html](https://www.iso.org/standard/53798.html)
* **MCP Documentation:** [`docs/standards/`](../../../../docs/standards/)
* **OGC FAIR Data Principles:** [https://www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)

---

<div align="center">

*“Schemas are the grammar of data — defining how Kansas’s digital landscapes remain coherent, validated, and enduring.”*

</div>
```

