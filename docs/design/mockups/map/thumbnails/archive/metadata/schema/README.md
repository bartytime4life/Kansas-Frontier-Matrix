<div align="center">

# 🧩 Kansas Frontier Matrix — Archived Map Thumbnail Metadata Schema  
`docs/design/mockups/map/thumbnails/archive/metadata/schema/`

**Standardized · Validated · Machine-Readable Provenance**

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../../..)  
[![Schema Validation](https://img.shields.io/badge/JSON--Schema-Validated-orange)](https://json-schema.org)  
[![Archive Integrity](https://img.shields.io/badge/Archive-Integrity-blue)](../../../../../../../../../.github/workflows/stac-validate.yml)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines the **JSON Schema specifications** used to validate  
archived map thumbnail metadata stored under  
`docs/design/mockups/map/thumbnails/archive/metadata/`.

Each schema ensures archived thumbnail metadata remains **consistent**,  
**machine-readable**, and **semantically interoperable** across the  
Kansas Frontier Matrix (KFM) documentation and STAC catalog systems.

Schemas align with **JSON Schema Draft-2020-12**, **DCAT**, **STAC 1.0.0**, and **CIDOC-CRM** principles to maintain  
high-fidelity documentation integrity, temporal traceability, and interoperability between  
design assets, knowledge graphs, and spatial datasets.

---

## 🗂️ Directory Structure

```text
docs/design/mockups/map/thumbnails/archive/metadata/schema/
├── README.md                          # This documentation file
└── map_thumbnail_metadata.schema.json # JSON Schema validator for archived map thumbnails
````

---

## 📘 `map_thumbnail_metadata.schema.json`

**Purpose:** Define validation structure for archived map thumbnail metadata records,
documenting each thumbnail’s lineage, authorship, and archival rationale.

### 🧩 Schema Outline (JSON Schema Draft-2020-12)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Archived Map Thumbnail Metadata Schema",
  "description": "Validation structure for archived map thumbnail metadata within the Kansas Frontier Matrix ecosystem.",
  "type": "object",
  "required": ["id", "title", "author", "created", "archived", "license"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier including version suffix (e.g., _v1)."
    },
    "title": { "type": "string", "description": "Title with map topic and version." },
    "author": { "type": "string", "description": "Design team or author." },
    "created": { "type": "string", "format": "date", "description": "Date created (ISO-8601)." },
    "archived": { "type": "string", "format": "date", "description": "Date archived or superseded." },
    "superseded_by": { "type": "string", "description": "Path or identifier of the replacing thumbnail." },
    "reason": { "type": "string", "description": "Reason for archival (e.g., updated color scale, accessibility fix)." },
    "source": { "type": "string", "description": "Relative path to original thumbnail or design file." },
    "related": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Linked documents or related design components."
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Keywords for search and classification."
    },
    "status": {
      "type": "string",
      "enum": ["archived", "deprecated"],
      "description": "Asset archival state."
    },
    "license": {
      "type": "string",
      "description": "License type (default CC-BY-4.0)."
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum for integrity verification."
    },
    "provenance": {
      "type": "object",
      "properties": {
        "derived_from": { "type": "string", "description": "Source file or dataset reference." },
        "created_with": { "type": "string", "description": "Tool or process used (e.g., Figma Export)." },
        "commit": { "type": "string", "description": "Git commit reference for traceability." }
      },
      "required": ["derived_from"],
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

---

## 🧮 Validation Workflow

| Step                    | Description                                           | Tool / Workflow                                                     |
| ----------------------- | ----------------------------------------------------- | ------------------------------------------------------------------- |
| **1. Create / Update**  | Add or modify metadata under `/metadata/`.            | Manual or automation script                                         |
| **2. Validate Schema**  | Check metadata files against schema.                  | `jsonschema -i file.json schema/map_thumbnail_metadata.schema.json` |
| **3. CI Automation**    | Auto-validation during GitHub Actions.                | `.github/workflows/stac-validate.yml`                               |
| **4. Integrity Checks** | Validate SHA-256 checksum and file paths.             | STAC validator                                                      |
| **5. Provenance Trace** | Ensure linkage to `derived_from` and `superseded_by`. | Knowledge graph ingestion                                           |

### Manual Validation Example

```bash
python -m jsonschema -i metadata/20251009_map-treaty-boundaries-thumb_v1.json \
  schema/map_thumbnail_metadata.schema.json
```

---

## 🧩 Standards Alignment

| Standard                           | Description                                   | Relevance                                     |
| ---------------------------------- | --------------------------------------------- | --------------------------------------------- |
| **JSON Schema Draft-2020-12**      | Base structural validation and format typing. | Ensures metadata interoperability.            |
| **DCAT (Data Catalog Vocabulary)** | Dataset-level metadata for catalog indexing.  | Integrates with KFM catalog exports.          |
| **STAC 1.0.0**                     | Spatial/temporal asset metadata framework.    | Connects design imagery to datasets.          |
| **CIDOC-CRM**                      | Cultural heritage and provenance modeling.    | Provides semantic linkage for design lineage. |
| **OWL-Time**                       | Time interval ontology.                       | Enables precise temporal querying.            |

---

## 🧠 Schema Extension Guidelines

When extending schema functionality (e.g., adding `reviewed_by`, `accessibility`, or `linked_issue`):

1️⃣ Copy the existing schema to a new file:
`map_thumbnail_metadata_v2.schema.json`

2️⃣ Update `$id`, `title`, and `description` to reflect the version.
3️⃣ Add or modify property definitions.
4️⃣ Update CI references (`stac-validate.yml`, docs links).
5️⃣ Validate existing metadata to ensure backward compatibility.

---

## 🧩 Integration with KFM Systems

Validated metadata is indexed into KFM’s **knowledge graph** and **STAC catalog**.
Schema fields map to persistent semantic and spatial properties.

| Metadata Field  | Knowledge Graph (Neo4j / RDF) | STAC Equivalent           |
| --------------- | ----------------------------- | ------------------------- |
| `id`            | `identifier`                  | `id`                      |
| `title`         | `name`                        | `title`                   |
| `created`       | `created`                     | `properties.datetime`     |
| `archived`      | `endDate`                     | `properties.end_datetime` |
| `superseded_by` | `replacedBy`                  | `links.replaced_by`       |
| `source`        | `derivedFrom`                 | `assets.source.href`      |
| `license`       | `license`                     | `license`                 |

This semantic alignment ensures that every archived asset is queryable, comparable,
and retraceable through time within the broader KFM knowledge infrastructure.

---

## ⚖️ License

All schemas and metadata specifications are released under
**Creative Commons Attribution 4.0 International (CC-BY-4.0)**.

**© 2025 Kansas Frontier Matrix Design Team**
Attribution required for reuse, modification, or redistribution.
Commercial use permitted with credit.

---

## 🗓️ Change Log

| Date           | Description                                                                    |
| -------------- | ------------------------------------------------------------------------------ |
| **2025-10-14** | Initial version — schema structure and validation workflow established.        |
| **2025-10-15** | Added standards alignment and schema extension guide.                          |
| **2025-10-16** | Integrated knowledge graph / STAC mapping section for provenance traceability. |

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Validation · Provenance · Accessibility · Reproducibility**

</div>
```
