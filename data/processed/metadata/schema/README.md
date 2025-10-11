<div align="center">

# 🧩 Kansas Frontier Matrix — Processed Metadata Schemas

`data/processed/metadata/schema/`

**Mission:** Define and maintain the **schema standards** that govern all processed dataset metadata
across the Kansas Frontier Matrix — ensuring consistency, validation, and compliance with
**STAC 1.0.0**, **JSON Schema Draft 2020-12**, and the **Master Coder Protocol (MCP)** for transparent, reproducible science.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![AI Validation](https://img.shields.io/badge/AI%20Assisted-Yes-purple)](../../../../docs/ai/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../LICENSE)

</div>

---

## 🧾 Version Metadata

| Attribute         | Value                                                                              |
| ----------------- | ---------------------------------------------------------------------------------- |
| **Version**       | `v2.2.0`                                                                           |
| **Status**        | ✅ Stable                                                                           |
| **Last Updated**  | 2025-10-11                                                                         |
| **Maintainers**   | @andy-barta · @matrix-core-team                                                    |
| **Compatibility** | MCP ≥1.1 · STAC ≥1.0.0 · JSON Schema ≥2020-12                                      |
| **Linked Docs**   | [`docs/standards/schema_changes.md`](../../../../docs/standards/schema_changes.md) |

---

## 📚 Table of Contents

* [Overview](#overview)
* [Directory Layout](#directory-layout)
* [Schema Architecture (Mermaid)](#schema-architecture-mermaid)
* [Schema Files](#schema-files)
* [Validation Process](#validation-process)
* [Schema Compliance Rules](#schema-compliance-rules)
* [Extending the Schema](#extending-the-schema)
* [AI-Driven Metadata Validation](#ai-driven-metadata-validation)
* [Change Log](#changelog)
* [References](#references)

---

## 🧠 Overview

This directory houses **machine-readable JSON Schemas** used to validate all processed dataset metadata (`data/processed/metadata/`).
Each schema defines required fields, typing rules, and controlled vocabularies to maintain a unified and auditable metadata ecosystem.

Schemas integrate:

* 🛰️ **STAC 1.0.0** — standardized metadata model for spatial & temporal datasets
* 🧬 **MCP Provenance Model** — ensuring dataset lineage, software traceability, and reproducibility
* 🧩 **JSON Schema Draft 2020-12** — for formal validation and cross-system interoperability

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── metadata/
        └── schema/
            ├── processed_item.schema.json      # Core MCP metadata schema for processed datasets
            ├── stac_item.schema.json           # STAC 1.0 reference schema
            ├── validation_rules.json           # Supplemental MCP-specific validation rules
            ├── examples/
            │   ├── valid_metadata_example.json
            │   └── invalid_metadata_example.json
            └── README.md
```

Each schema file is **version-controlled** and automatically validated by CI/CD prior to data publication.

---

## 🧩 Schema Architecture (Mermaid)

```mermaid
flowchart TD
  A["Processed Dataset Metadata\n(data/processed/metadata/*.json)"] --> B["Schema Validation\n(JSON Schema + MCP Rules)"]
  B --> C["Validated STAC Item\n(data/stac/processed/*.json)"]
  C --> D["Catalog Integration\n(STAC Collections)"]
  D --> E["Knowledge Graph Node\n(Neo4j · CIDOC CRM · OWL-Time)"]
  E --> F["Web UI Layer\n(MapLibre · Timeline · API)"]
  F --> G["AI Validation Feedback\n(LLM Metadata Analyzer)"]
<!-- END OF MERMAID -->
```

This flow illustrates how schema validation feeds the **provenance chain**—from JSON metadata to the graph and web visualization layers.

---

## 🧩 Schema Files

### 🧮 `processed_item.schema.json`

Defines the **core MCP metadata structure**, extending STAC’s `Item` model with MCP-specific properties:

| Field                                | Description                                  | Requirement |
| ------------------------------------ | -------------------------------------------- | ----------- |
| `id`                                 | Unique dataset identifier                    | ✅ Required  |
| `mcp_provenance`                     | SHA-256 checksum or external provenance hash | ✅ Required  |
| `processing.software`                | Software/tool versions used in ETL           | ✅ Required  |
| `derived_from`                       | Lineage references (parent dataset IDs)      | ✅ Required  |
| `license`                            | License keyword (`CC-BY 4.0`, `MIT`)         | ✅ Required  |
| `spatial_extent` / `temporal_extent` | Dataset coverage                             | ✅ Required  |
| `quality_assurance`                  | Optional QC summary                          | ⚙️ Optional |

---

### 🌐 `stac_item.schema.json`

STAC baseline schema that guarantees **interoperability** with geospatial catalog tools.

* Enforces `stac_version`, `id`, `type`, `assets`, and `properties`
* Checks optional extensions (EO, SAR, Scientific)
* Validates asset roles and media types

---

### ⚖️ `validation_rules.json`

Supplemental MCP rule set for advanced validation:

* Regex for dataset IDs: `^[a-z0-9_]+$`
* File-extension matching for declared assets
* Cross-reference checks between metadata ID and file path
* Checksum verification (.sha256 file existence)
* Conditional temporal coverage enforcement

---

## ⚙️ Validation Process

### Local Validation

```bash
# Validate all processed metadata
make validate-metadata

# Validate one file manually
python tools/validate_json.py data/processed/metadata/terrain/dem_1m_ks_filled.json
```

### Continuous Integration

Automated through [`.github/workflows/stac-validate.yml`](../../../../.github/workflows/stac-validate.yml):

1. JSON Schema + MCP validation
2. STAC 1.0.0 compliance check
3. Provenance & checksum verification
4. Outputs: `validation_report.json` + summary badge

---

## ✅ Schema Compliance Rules

| Rule Type                 | Description                                                            | Enforced By                  |
| ------------------------- | ---------------------------------------------------------------------- | ---------------------------- |
| **Required Fields**       | `id`, `title`, `datetime`, `mcp_provenance`, `derived_from`, `license` | `processed_item.schema.json` |
| **Checksum Integrity**    | SHA-256 match with `.sha256` file                                      | `validation_rules.json`      |
| **Cross-Link Validation** | Valid STAC item linkage                                                | `stac_item.schema.json`      |
| **License Check**         | Approved open licenses only                                            | `validation_rules.json`      |
| **Naming Convention**     | lowercase `snake_case` IDs                                             | `validation_rules.json`      |
| **Date Consistency**      | `datetime` ⊆ `temporal_extent`                                         | MCP Validator                |
| **Provenance Chain**      | `derived_from` must resolve                                            | MCP Validator                |

Non-compliance halts CI/CD until corrected.

---

## 🔮 AI-Driven Metadata Validation

The **AI Metadata Validator** (LLM-powered microservice) assists schema integrity by:

* Parsing new metadata for field completeness
* Detecting semantic anomalies (e.g., mismatched bounding boxes, wrong date formats)
* Auto-generating human-readable validation reports
* Suggesting MCP-compliant corrections

Integrated in the **Matrix-AI pipeline** (`ai/metadata_validator/`), it provides
confidence scoring and MCP certification tagging (`"validated_by_ai": true`).

---

## 🧩 Extending the Schema

1. Duplicate & version (`processed_item.schema.v3.json`)
2. Increment `$id` and `$schema` URIs
3. Update field definitions with descriptions
4. Add to [`docs/standards/schema_changes.md`](../../../../docs/standards/schema_changes.md)
5. Validate against examples before production release

> 🧭 Schemas **must remain backward-compatible** with MCP 1.x lineage.

---

## 🕰️ CHANGELOG

| Version   | Date       | Author      | Summary                                                 |
| --------- | ---------- | ----------- | ------------------------------------------------------- |
| **2.2.0** | 2025-10-11 | A. Barta    | Added AI validation integration, MCP v1.1 compatibility |
| **2.1.0** | 2025-09-28 | Matrix Team | Updated STAC schema links, improved Mermaid diagram     |
| **2.0.0** | 2025-08-12 | Matrix Team | Complete schema overhaul for MCP alignment              |
| **1.0.0** | 2025-07-04 | A. Barta    | Initial schema directory setup                          |

---

## 📖 References

* 🌍 **STAC Specification 1.0.0** — [https://stacspec.org](https://stacspec.org)
* 🧱 **JSON Schema Draft 2020-12** — [https://json-schema.org](https://json-schema.org)
* 🗺️ **ISO 19115 Metadata Standard** — [https://www.iso.org/standard/53798.html](https://www.iso.org/standard/53798.html)
* 🧬 **MCP Documentation** — [`docs/standards/`](../../../../docs/standards/)
* 🧩 **FAIR Data Principles** — [https://www.go-fair.org/fair-principles/](https://www.go-fair.org/fair-principles/)

---

<div align="center">

> *“Schemas are the grammar of data — defining how Kansas’s digital landscapes remain coherent, validated, and enduring.”*
> **— Kansas Frontier Matrix, MCP Edition v2.2**

</div>
