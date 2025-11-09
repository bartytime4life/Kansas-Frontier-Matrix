---
title: "📐 Kansas Frontier Matrix — Data Schema Definitions & Validation Framework"
path: "docs/guides/data/schemas/README.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.0.0/manifest.zip"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-schemas-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Data Schema Definitions & Validation Framework**
`docs/guides/data/schemas/README.md`

**Purpose:**  
Provide a comprehensive reference for **data schemas**, **validation rules**, and **metadata contracts** that govern all datasets within the Kansas Frontier Matrix (KFM).  
These schemas ensure interoperability across ETL workflows, FAIR+CARE audits, and catalog integration (STAC/DCAT/CIDOC CRM).

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Data_Schema-orange)](../../../../../docs/standards/README.md)
[![Status](https://img.shields.io/badge/Status-Validated-brightgreen)](../../../../../releases/)
</div>

---

## 📘 Overview

This directory contains JSON Schema and YAML specifications defining **data structure, metadata fields, and governance validation** for all KFM datasets.  
It underpins the **data-contract-v3.json** used across ETL pipelines, ensuring every record, raster, and feature meets both technical and ethical standards.

---

## 🗂️ Directory Layout

```plaintext
docs/guides/data/schemas/
├── README.md                                # This documentation
├── tabular-schema.json                      # Schema for tabular (CSV/Parquet) data
├── vector-schema.json                       # Schema for vector (GeoJSON/GeoParquet) data
├── raster-schema.json                       # Schema for raster (GeoTIFF/COG) data
├── metadata-schema.json                     # STAC/DCAT metadata field schema
├── faircare-schema.json                     # FAIR+CARE metadata contract
└── governance-schema.json                   # Provenance and ledger metadata schema
```

---

## ⚙️ Schema Overview

| Schema | Purpose | Key Fields |
|---------|----------|------------|
| **tabular-schema.json** | Defines field types, units, and naming conventions for CSV/Parquet data | `field_name`, `type`, `unit`, `description` |
| **vector-schema.json** | Ensures topology validity and CRS consistency for GeoJSON/GeoParquet | `geometry`, `crs`, `properties` |
| **raster-schema.json** | Validates raster band metadata, resolution, and NoData handling | `band_count`, `resolution`, `nodata_value` |
| **metadata-schema.json** | Standardizes STAC/DCAT field naming and licensing | `id`, `title`, `description`, `license`, `provenance` |
| **faircare-schema.json** | Embeds ethical governance fields and consent metadata | `collective_benefit`, `authority_to_control`, `responsibility`, `ethics` |
| **governance-schema.json** | Defines ledger and provenance metadata for all data pipelines | `sha256`, `auditor`, `timestamp`, `faircare_status` |

---

## 🧩 Example: Vector Schema (Simplified)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Vector Dataset Schema",
  "type": "object",
  "required": ["id", "geometry", "properties", "crs"],
  "properties": {
    "id": { "type": "string" },
    "geometry": {
      "type": "object",
      "properties": {
        "type": { "enum": ["Point", "LineString", "Polygon", "MultiPolygon"] },
        "coordinates": { "type": "array" }
      }
    },
    "crs": { "type": "string", "pattern": "EPSG:[0-9]+" },
    "properties": {
      "type": "object",
      "properties": {
        "source_dataset": { "type": "string" },
        "year": { "type": "integer" },
        "license": { "type": "string" }
      }
    }
  }
}
```

---

## 🧮 FAIR+CARE Schema Example

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "FAIR+CARE Metadata Schema",
  "type": "object",
  "required": ["collective_benefit", "authority_to_control", "responsibility", "ethics"],
  "properties": {
    "collective_benefit": { "type": "string", "enum": ["Pass", "Fail"] },
    "authority_to_control": { "type": "string" },
    "responsibility": { "type": "string" },
    "ethics": { "type": "string" }
  }
}
```

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation | Schema Location |
|------------|----------------|-----------------|
| **Findable** | UUIDs and IDs enforced across schemas | `metadata-schema.json` |
| **Accessible** | Human- and machine-readable JSON Schema | `docs/guides/data/schemas/` |
| **Interoperable** | Aligned with STAC/DCAT 3.0 and OGC standards | `metadata-schema.json` |
| **Reusable** | Self-describing fields with type and unit metadata | `tabular-schema.json` |
| **Collective Benefit** | FAIR+CARE fields embedded in every dataset | `faircare-schema.json` |
| **Authority to Control** | Governance schema defines consent and oversight | `governance-schema.json` |
| **Responsibility** | Validation workflows ensure energy and ethics tracking | CI/CD validators |
| **Ethics** | Data masking rules integrated in FAIR+CARE schema | CARE policies |

---

## ⚙️ CI/CD Validation Integration

| Workflow | Function | Output |
|-----------|-----------|--------|
| `schema-validate.yml` | Validate all dataset schemas against contracts | `reports/data/schema-validation.json` |
| `faircare-validate.yml` | Verify FAIR+CARE metadata compliance | `reports/faircare/schema-audit.json` |
| `ledger-sync.yml` | Append schema hashes to governance ledger | `docs/standards/governance/LEDGER/data-schema-ledger.json` |

---

## 🧾 Example Schema Validation Report

```json
{
  "schema_id": "vector-schema-v10",
  "validation_status": "Pass",
  "datasets_tested": 58,
  "issues_found": 0,
  "faircare_compliance": "Pass",
  "timestamp": "2025-11-09T12:00:00Z"
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.0.0 | 2025-11-09 | Core Team | Established unified schema validation structure for all KFM data models |
| v9.7.0 | 2025-11-03 | A. Barta | Added FAIR+CARE schema enforcement for vector and metadata validation |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Data Guides](../README.md) · [Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

