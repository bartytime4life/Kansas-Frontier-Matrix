---
title: "📜 Kansas Frontier Matrix — Data Contracts & Metadata Schema Specification"
path: "docs/standards/data-contracts.md"
version: "v9.7.0"
last_updated: "2025-11-05"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.7.0/sbom.spdx.json"
manifest_ref: "../../releases/v9.7.0/manifest.zip"
telemetry_ref: "../../releases/v9.7.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-data-contracts-v1.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 📜 **Kansas Frontier Matrix — Data Contracts & Metadata Schema Specification**
`docs/standards/data-contracts.md`

**Purpose:** Define the structure, fields, and validation rules for dataset metadata used throughout the Kansas Frontier Matrix (KFM).  
Data contracts ensure that all datasets — historical, geospatial, textual, and AI-generated — follow the same reproducible and FAIR+CARE-aligned schema.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](faircare.md)
[![Status: Standardized](https://img.shields.io/badge/Status-Active-success)]()

</div>

---

## 📘 Overview

**Data Contracts** in the Kansas Frontier Matrix serve as formal agreements describing the **schema**, **validation rules**, and **ethical governance requirements** for all datasets ingested into the repository.  
They ensure that data remains:
- **Machine-readable**
- **Traceable**
- **Ethically governed**
- **Reproducible**

Each contract functions as a structured JSON or YAML schema validated by the automated FAIR+CARE pipeline (`faircare-validate.yml`) and STAC/DCAT compatibility workflows.

---

## 🗂️ Directory & Schema Integration

```
docs/standards/
├── data-contracts.md                 # This document (schema and rules)
├── faircare.md                       # FAIR+CARE validation framework
├── markdown_rules.md                 # Documentation format standards
└── governance/ROOT-GOVERNANCE.md     # Ethical governance charter
```

**Schema Sources:**
- STAC 1.0.0 (SpatioTemporal Asset Catalog)
- DCAT 3.0 (W3C Data Catalog Vocabulary)
- CIDOC CRM (Cultural heritage ontology)
- OWL-Time (Temporal ontology)
- GeoJSON / ISO 19115 (Geospatial metadata)

---

## 🧱 Core Metadata Fields

| Field | Type | Description | Required | Example |
|--------|------|-------------|-----------|----------|
| `id` | String | Unique identifier (UUID or human-readable). | ✅ | `"noaa_storms_1950_2025"` |
| `title` | String | Descriptive dataset name. | ✅ | `"NOAA Storm Events Archive (1950–2025)"` |
| `description` | String | Summary of dataset contents, scope, and source. | ✅ | `"Contains recorded severe weather events across Kansas."` |
| `type` | String | Dataset category (`raster`, `vector`, `tabular`, `text`). | ✅ | `"raster"` |
| `spatial` | Array[Number] | Bounding box `[west, south, east, north]` in WGS84. | ✅ | `[-102.05, 37.0, -94.6, 40.0]` |
| `temporal` | Object | Time range of dataset validity. | ✅ | `{"start":"1950-01-01","end":"2025-12-31"}` |
| `license` | String | SPDX-compatible license name or identifier. | ✅ | `"CC-BY-4.0"` |
| `provenance` | String | Source or origin (URL, archive, or institution). | ✅ | `"https://www.ncdc.noaa.gov/stormevents/"` |
| `checksum` | String | SHA-256 checksum or pointer for DVC/LFS verification. | ✅ | `"sha256-4a0f...ae3d"` |
| `keywords` | Array[String] | Keywords for search and indexing. | ⚙️ | `["weather","climate","noaa","kansas"]` |
| `doi` | String | DOI or persistent identifier (if applicable). | ⚙️ | `"10.5065/D6R78D7V"` |
| `lineage` | String | Data transformation or processing history. | ⚙️ | `"Derived from NOAA NCEI raw archives (processed v3.1)." `|
| `format` | String | Primary file format or encoding. | ⚙️ | `"GeoTIFF"` |
| `care` | Object | Optional CARE ethics metadata (see below). | ⚙️ | `{ "statement": "Approved by Tribal Data Council, 2025" }` |
| `updated` | String | ISO timestamp for last modification. | ✅ | `"2025-11-05T00:00:00Z"` |

---

## ⚖️ CARE Metadata (Ethical Data Layer)

The `care` field ensures datasets comply with cultural and community data governance.

| CARE Field | Type | Description | Example |
|-------------|------|-------------|----------|
| `statement` | String | Describes ethical handling, permissions, or approvals. | `"Dataset reviewed and cleared for open publication by FAIR+CARE Council."` |
| `reviewer` | String | Reviewer or entity responsible for CARE oversight. | `"KFM FAIR+CARE Council"` |
| `date_reviewed` | String | Date of review completion. | `"2025-10-28"` |
| `status` | Enum | `approved`, `revision`, or `restricted`. | `"approved"` |
| `notes` | String | Additional context or ethical guidance. | `"Contains no personally identifiable or culturally restricted data."` |

---

## 🧩 Extended Metadata Fields

| Field | Description | Relation |
|--------|-------------|-----------|
| `stac_extensions` | Array of URLs linking to STAC extensions used. | STAC 1.0.0 |
| `dcat:theme` | Thematic category for DCAT compliance. | DCAT 3.0 |
| `geo:geometry` | GeoJSON geometry object for spatial reference. | GeoJSON |
| `time:hasBeginning` / `time:hasEnd` | Temporal ontology mapping. | OWL-Time |
| `prov:wasGeneratedBy` | Link to provenance activity (ETL process). | PROV-O |
| `prov:used` | Reference to input datasets. | PROV-O |
| `schema:creator` | Dataset creator metadata. | Schema.org |
| `schema:distribution` | Link to data access endpoints or download URLs. | DCAT 3.0 |
| `schema:license` | Human-readable license summary. | Schema.org |

---

## 🧠 Example Data Contract (JSON Schema)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://schemas.kfm.dev/data-contract.schema.json",
  "title": "Kansas Frontier Matrix Data Contract",
  "description": "Metadata schema for datasets in the Kansas Frontier Matrix.",
  "type": "object",
  "required": ["id", "title", "description", "type", "spatial", "temporal", "license", "provenance", "checksum"],
  "properties": {
    "id": { "type": "string" },
    "title": { "type": "string" },
    "description": { "type": "string" },
    "type": { "type": "string" },
    "spatial": { "type": "array", "items": { "type": "number" }, "minItems": 4 },
    "temporal": {
      "type": "object",
      "required": ["start"],
      "properties": {
        "start": { "type": "string", "format": "date-time" },
        "end": { "type": "string", "format": "date-time" }
      }
    },
    "license": { "type": "string" },
    "provenance": { "type": "string" },
    "checksum": { "type": "string" },
    "keywords": { "type": "array", "items": { "type": "string" } },
    "care": {
      "type": "object",
      "properties": {
        "statement": { "type": "string" },
        "reviewer": { "type": "string" },
        "date_reviewed": { "type": "string", "format": "date" },
        "status": { "type": "string", "enum": ["approved","revision","restricted"] },
        "notes": { "type": "string" }
      }
    },
    "updated": { "type": "string", "format": "date-time" }
  }
}
```

---

## 🧮 Validation Workflow

| Workflow | Function | Output |
|-----------|-----------|---------|
| `faircare-validate.yml` | Enforces schema completeness and CARE ethics compliance. | `reports/fair/faircare_results.ndjson` |
| `stac-validate.yml` | Checks STAC/DCAT structural compatibility. | `reports/self-validation/stac/_summary.json` |
| `docs-lint.yml` | Validates documentation completeness and YAML front-matter. | `reports/self-validation/docs/lint_summary.json` |
| `telemetry-export.yml` | Publishes validation results to dashboard. | `releases/v9.7.0/focus-telemetry.json` |

---

## 🧾 Governance Integration

Data contracts are reviewed quarterly by the FAIR+CARE Council and documented in:

- `reports/audit/governance-ledger.json`
- `reports/audit/release-manifest-log.json`
- `docs/reports/telemetry/governance_scorecard.json`

**Example Governance Ledger Entry:**
```json
{
  "event": "data_contract_review",
  "dataset_id": "noaa_storms_1950_2025",
  "status": "approved",
  "reviewer": "FAIR+CARE Council",
  "timestamp": "2025-11-05T19:15:00Z",
  "telemetry_ref": "releases/v9.7.0/focus-telemetry.json"
}
```

---

## ⚖️ FAIR+CARE Compliance Mapping

| Principle | Data Contract Requirement |
|------------|---------------------------|
| **Findable** | Unique dataset `id`, `title`, and discoverable metadata. |
| **Accessible** | Licensed under open terms (CC-BY 4.0 or Public Domain). |
| **Interoperable** | Metadata conforms to STAC, DCAT, and schema.org. |
| **Reusable** | Provenance, lineage, and checksum integrity recorded. |
| **CARE** | Contains `care` block for cultural or community data governance. |

---

## 🧩 Data Contract Evolution

All changes to this schema must:
1. Be versioned under semantic versioning (e.g. v1.0.0 → v1.1.0).  
2. Include changelog entries in `reports/audit/release-manifest-log.json`.  
3. Pass automated schema validation prior to merge.  
4. Receive governance council approval if changes affect CARE data fields.

**Schema Change Workflow:**
- Propose change → Governance review → Approval → Merge → Telemetry update

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v9.7.0 | 2025-11-05 | A. Barta | Defined universal KFM data contract schema with FAIR+CARE integration. |
| v9.5.0 | 2025-10-20 | A. Barta | Added CARE metadata and governance linkage. |
| v9.3.0 | 2025-08-12 | KFM Core Team | Improved STAC/DCAT compatibility mapping. |
| v9.0.0 | 2025-06-01 | KFM Core Team | Established data contract and schema validation baseline. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Compliant with **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Standards Index](README.md) · [Root Governance Charter](governance/ROOT-GOVERNANCE.md)

</div>
