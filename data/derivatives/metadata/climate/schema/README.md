<div align="center">

# 🧩 Kansas Frontier Matrix — Climate Derivative Metadata Schema  
`data/derivatives/metadata/climate/schema/`

**Purpose:** Define, validate, and document the **JSON Schema** used to describe  
all climate-related derivative metadata records within the **Kansas Frontier Matrix (KFM)** system.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../../../.github/workflows/codeql.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../docs/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory defines the **formal JSON Schema** for validating all metadata  
under `data/derivatives/metadata/climate/`.  
Schemas ensure **interoperability** between MCP documentation, **STAC 1.0.0**,  
and internal governance standards for derivative datasets.

Every climate metadata record must pass schema validation **before merge** into the repository.  
CI workflows automatically enforce these schema rules to maintain reproducibility and data integrity.

---

## 🗂️ Directory Layout

```bash
data/derivatives/metadata/climate/schema/
├── README.md                               # This document (v1.1.0)
└── climate_derivative_metadata.schema.json # Core schema definition
````

---

## 🧮 Schema Specification

| Element                | Type    | Description                                  |
| :--------------------- | :------ | :------------------------------------------- |
| `$schema`              | string  | Schema draft standard (Draft 2020-12 URI)    |
| `$id`                  | string  | Canonical URI for schema reference           |
| `title`                | string  | Schema name                                  |
| `description`          | string  | Purpose of metadata definition               |
| `type`                 | string  | Must be `"object"`                           |
| `properties`           | object  | Metadata fields and constraints              |
| `required`             | array   | Required fields for validation               |
| `additionalProperties` | boolean | Must be `false` to prevent unregistered keys |

---

## 🧠 Example Schema Stub

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kansasfrontiermatrix.org/schema/climate_derivative_metadata.schema.json",
  "title": "KFM Climate Derivative Metadata Schema",
  "description": "Standardized schema for derived climate metadata records.",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "title": { "type": "string" },
    "description": { "type": "string" },
    "provenance": { "$ref": "#/$defs/provenance" },
    "spatial_extent": { "$ref": "#/$defs/spatial_extent" },
    "temporal_extent": { "$ref": "#/$defs/temporal_extent" },
    "uncertainty": { "$ref": "#/$defs/uncertainty" },
    "stac_extensions": {
      "type": "array",
      "items": { "type": "string" }
    },
    "version": { "type": "string", "pattern": "^v?[0-9]+\\.[0-9]+\\.[0-9]+$" },
    "created": { "type": "string", "format": "date" },
    "last_updated": { "type": "string", "format": "date" }
  },
  "required": ["id", "title", "description", "provenance", "version"],
  "additionalProperties": false
}
```

---

## 🧭 Validation Workflow

```mermaid
flowchart TD
  A["Metadata JSON<br/>(data/derivatives/metadata/climate)"]
    --> B["Schema Definition<br/>(climate_derivative_metadata.schema.json)"]
  B --> C["Validation<br/>(jsonschema-cli · stac-validator)"]
  C --> D["Continuous Integration<br/>(.github/workflows/stac-validate.yml)"]
  D --> E["Validated Metadata<br/>for STAC Catalog Ingest"]
```

<!-- END OF MERMAID -->

---

## 🧰 Usage Example

| Purpose                       | Command                                                                                   | Result                       |
| :---------------------------- | :---------------------------------------------------------------------------------------- | :--------------------------- |
| Validate single metadata file | `jsonschema -i ../mean_temperature_summary.json climate_derivative_metadata.schema.json`  | Confirms JSON validity       |
| Batch validation              | `for f in ../*.json; do jsonschema -i "$f" climate_derivative_metadata.schema.json; done` | Validates all metadata files |
| STAC validation               | `stac-validator ../mean_temperature_summary.json`                                         | Confirms STAC compliance     |

---

## ⚙️ Continuous Integration (CI/CD)

The schema is validated automatically through
[`.github/workflows/stac-validate.yml`](../../../../../../.github/workflows/stac-validate.yml):

1. **Schema syntax check** (Draft 2020-12 compliance)
2. **Metadata validation** for all derivative JSON files
3. **Error aggregation** and artifact publication
4. **Workflow badges** updated automatically in project documentation

Logs are stored in `data/derivatives/metadata/climate/validation/stac-validation.log`.

---

## ✅ MCP Compliance Checklist

| MCP Principle       | Implemented | Evidence                          |
| :------------------ | :---------: | :-------------------------------- |
| Documentation-First |      ✅      | Schema documented + versioned     |
| Reproducibility     |      ✅      | CI schema validation              |
| Provenance          |      ✅      | `$id` URI and repo path           |
| Transparency        |      ✅      | Public schema + validation logs   |
| Versioning          |      ✅      | Semantic version control via tags |

---

## 🧾 Versioning & Changelog

| Version    | Date       | Author                  | Notes                                                     |
| :--------- | :--------- | :---------------------- | :-------------------------------------------------------- |
| **v1.1.0** | 2025-10-11 | KFM Data Standards Team | Added front-matter, CI integration, and MCP checklist     |
| **v1.0.0** | 2025-10-11 | KFM Data Standards Team | Initial publication of climate derivative metadata schema |

---

## 🔗 Related Documents

* [`../README.md`](../README.md) — Parent metadata registry
* [`../validation/README.md`](../validation/README.md) — Validation logs and workflow
* [`../../../../../../docs/standards/markdown_protocol.md`](../../../../../../docs/standards/markdown_protocol.md) — Markdown & MCP standards
* [`../../../../../../docs/templates/model_card.md`](../../../../../../docs/templates/model_card.md) — Climate model documentation template

---

## 🪶 License & Provenance

**License:** [CC-BY 4.0](../../../../../../LICENSE)
**Provenance:** Authored under the **Master Coder Protocol (MCP)** — documentation-first, auditable, and version-controlled.
**Maintainers:** Kansas Frontier Matrix Data Standards Team
**Last Updated:** 2025-10-11

```

---
```
