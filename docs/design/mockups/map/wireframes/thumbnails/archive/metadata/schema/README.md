<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Wireframe Thumbnail Archive Metadata Schema  
`docs/design/mockups/map/wireframes/thumbnails/archive/metadata/schema/`

**Purpose:** Define the **JSON Schema** validation structure for archived **map wireframe thumbnail metadata**,  
ensuring integrity, accessibility, and provenance preservation across all Kansas Frontier Matrix (KFM) design iterations.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../../..)  
[![Schema Validation](https://img.shields.io/badge/JSON--Schema-Validated-orange)](https://json-schema.org)  
[![Archive Verified](https://img.shields.io/badge/Archive-Integrity-blue)](../../../../../../../../../.github/workflows/stac-validate.yml)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines the **JSON Schema specifications** for validating metadata associated with  
**archived map wireframe thumbnails** under  
`docs/design/mockups/map/wireframes/thumbnails/archive/metadata/`.

Schemas here preserve:
- 🧩 **Data structure integrity** across legacy design records.  
- 🧾 **Provenance linkage** between archived Figma exports and their Git commits.  
- ♿ **Accessibility metrics** (contrast, alt text) retained for audit history.  
- 🔒 **Checksum validation** ensuring reproducibility and version lock.  
- 🧱 **Schema inheritance** from active Map Thumbnail Metadata Schema for interoperability.  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/wireframes/thumbnails/archive/metadata/schema/
├── README.md                           # This documentation file
├── archive_thumbnail.schema.json        # Schema for individual archived thumbnail records
└── index.schema.json                    # Schema for aggregated metadata index
````

---

## 📘 `archive_thumbnail.schema.json`

**Purpose:** Defines the JSON Schema for a single archived thumbnail metadata record
documenting deprecated or prototype wireframes of the Kansas Frontier Matrix (KFM) Map Interface.

### 🧩 Schema Outline

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Archived Map Wireframe Thumbnail Metadata Schema",
  "type": "object",
  "required": ["id", "title", "file", "variant", "status", "provenance"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the archived thumbnail record."
    },
    "title": { "type": "string", "description": "Human-readable name of the archived wireframe." },
    "file": { "type": "string", "description": "Path to archived PNG/JPG thumbnail file." },
    "description": { "type": "string", "description": "Brief description of concept or layout intent." },
    "variant": {
      "type": "string",
      "enum": ["concept_v0", "darkmode_concept", "mobile_prototype", "superseded"],
      "description": "Design version or variant identifier."
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Theme or design context tags (e.g. ['map','ui','prototype'])."
    },
    "status": {
      "type": "string",
      "enum": ["archived", "deprecated", "superseded"],
      "description": "Indicates archival state of the asset."
    },
    "archived_on": {
      "type": "string",
      "format": "date",
      "description": "Date the file was archived (ISO 8601)."
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License governing reuse of the archived image."
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum ensuring file immutability."
    },
    "source_figma": {
      "type": "string",
      "description": "Reference to Figma file or version from which the archive originated."
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string", "description": "Path or URL to original Figma source file." },
        "created_with": { "type": "string", "description": "Tool or script used to export/archive." },
        "commit": { "type": "string", "description": "Git commit hash for traceability." }
      },
      "description": "Metadata capturing origin, lineage, and creation process."
    },
    "accessibility": {
      "type": "object",
      "properties": {
        "contrast_ratio": { "type": "number", "minimum": 4.5 },
        "alt_text": { "type": "string" }
      },
      "description": "Accessibility metrics for archived thumbnails (WCAG 2.1 AA)."
    }
  }
}
```

---

## 📗 `index.schema.json`

**Purpose:** Defines the structure for the **aggregated index** of archived thumbnail metadata,
supporting validation of collections and automated documentation generation.

### 🧩 Schema Outline

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Archived Map Wireframe Thumbnails Metadata Index",
  "type": "object",
  "required": ["version", "updated", "archives"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "archives": {
      "type": "array",
      "items": { "$ref": "./archive_thumbnail.schema.json" }
    }
  }
}
```

---

## 🧮 Validation Workflow

Validation is managed through **GitHub Actions CI/CD**, guaranteeing schema consistency, accessibility, and provenance accuracy.

| Step  | Action                        | Validation Target                 |
| ----- | ----------------------------- | --------------------------------- |
| **1** | Schema Validation             | `archive_thumbnail.schema.json`   |
| **2** | File Existence Verification   | Archived images in `../`          |
| **3** | SHA-256 Checksum Verification | Metadata integrity check          |
| **4** | Accessibility Audit           | Alt text and contrast validation  |
| **5** | Provenance Validation         | Figma → Commit linkage validation |

### 🧰 Manual Validation Example

```bash
python -m jsonschema -i archive_thumbnails_metadata.json schema/archive_thumbnail.schema.json
```

---

## ♿ Accessibility & Historical Integrity

Even archived assets must maintain accessibility and traceability parity with current design assets.

| Metric               | Standard           | Description                                      |
| -------------------- | ------------------ | ------------------------------------------------ |
| **Contrast Ratio**   | ≥ 4.5 : 1          | Verified during export QA.                       |
| **Alt Text**         | Required           | Ensures meaningful description for archival use. |
| **Archival Tagging** | `status: archived` | Denotes deprecated or superseded design.         |

Accessibility data ensures historical assets remain inclusive and verifiable within the documentation ecosystem.

---

## 🧾 Provenance & MCP Compliance

| Attribute           | Description                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| **Generated By**    | `scripts/archive_thumbnail_schema_docs.py`                                |
| **Validated In CI** | `stac-validate.yml`, `jsonschema.yml`                                     |
| **Schema Draft**    | [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema) |
| **License**         | [CC-BY 4.0](../../../../../../../../../LICENSE)                           |
| **MCP Stage**       | Documented → Validated → Archived → Published                             |

---

## 📚 Related References

* [🗺 Map Wireframe Thumbnail Archive Metadata](../README.md)
* [🧩 Map Wireframe Thumbnail Metadata Schema](../../schema/README.md)
* [🧱 Kansas Frontier Matrix Web UI Architecture](../../../../../../../../../architecture/web_ui_architecture_review.md)
* [🌐 STAC Catalog](../../../../../../../../../data/stac/catalog.json)
* [♿ Accessibility Design Standards](../../../../../../../../design/reviews/accessibility/README.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Archival Validation · Provenance Tracking · Accessibility Preservation**

</div>
