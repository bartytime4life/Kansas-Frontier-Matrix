<div align="center">

# 🧩 Kansas Frontier Matrix — Archived Thumbnail Metadata Schema  
`docs/design/mockups/excalidraw/sketches/exports/thumbnails/archive/metadata/schema/`

**Structured · Validated · Machine-Readable**

</div>

---

## 🧭 Overview

This directory defines the **JSON Schema specifications** used to validate all archived thumbnail metadata files in  
`docs/design/mockups/excalidraw/sketches/exports/thumbnails/archive/metadata/`.

Each schema ensures that every metadata record conforms to the **Kansas Frontier Matrix (KFM)** documentation standards —  
providing consistent structure, machine readability, and compliance with **Master Coder Protocol (MCP)** principles of reproducibility and provenance.

Schemas in this folder are applied automatically during CI validation (`make validate-json` or `jsonschema` command)  
and ensure every archived thumbnail JSON entry includes required provenance, linkage, and licensing information.

---

## 📁 Directory Structure

```text
docs/design/mockups/excalidraw/sketches/exports/thumbnails/archive/metadata/schema/
├── README.md                                  # This documentation (GitHub-safe)
└── thumbnail_metadata.schema.json             # JSON Schema for archived thumbnail metadata

File Naming Convention:
Each schema file should follow:
{schema_subject}.schema.json
Example → thumbnail_metadata.schema.json

⸻

🧾 Example Schema: thumbnail_metadata.schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Archived Thumbnail Metadata Schema",
  "description": "Validation structure for archived thumbnail metadata under the Kansas Frontier Matrix.",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for the archived thumbnail asset (include version suffix)."
    },
    "title": {
      "type": "string",
      "description": "Human-readable title of the thumbnail or design concept."
    },
    "author": {
      "type": "string",
      "description": "Author or design team responsible for the asset."
    },
    "created": {
      "type": "string",
      "format": "date",
      "description": "Original creation date of the thumbnail."
    },
    "archived": {
      "type": "string",
      "format": "date",
      "description": "Date this version was archived."
    },
    "source": {
      "type": "string",
      "description": "Relative path to the original thumbnail file."
    },
    "superseded_by": {
      "type": "string",
      "description": "Relative path or identifier of the replacement thumbnail (new version)."
    },
    "reason": {
      "type": "string",
      "description": "Brief explanation for why the thumbnail was archived (e.g., replaced, deprecated, style update)."
    },
    "related": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of related metadata or design files (relative paths)."
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Keywords describing the visual asset (max 5)."
    },
    "status": {
      "type": "string",
      "enum": ["archived", "deprecated"],
      "description": "Indicates archival state."
    },
    "license": {
      "type": "string",
      "description": "License for the asset (default CC-BY-4.0)."
    }
  },
  "required": ["id", "title", "author", "created", "archived", "license"],
  "additionalProperties": false
}


⸻

🧮 Validation Workflow
	1.	Edit or add new metadata JSON under:
docs/design/mockups/excalidraw/sketches/exports/thumbnails/archive/metadata/
	2.	Validate manually using the command-line jsonschema tool:

jsonschema -i metadata/20250920_navigation-flow-thumb_v1.json schema/thumbnail_metadata.schema.json


	3.	Automated CI Validation
KFM’s CI/CD (.github/workflows/stac-validate.yml or similar) includes JSON Schema checks as part of
the make validate-json or make data pipeline to ensure compliance.

⸻

🧩 Schema Standards & Alignment

Standard	Purpose	Integration
JSON Schema Draft-07	Structure validation for metadata	Enforced in CI
ISO8601	Temporal values (created, archived)	Uniform date parsing
DCAT / STAC Inspired	Semantic consistency with geospatial & dataset metadata	Optional enrichment
MCP Provenance Model	Ensures traceability of every visual artifact	Repository-wide

Each schema is versioned in Git and backward-compatible, enabling long-term reproducibility.

⸻

🧠 Extending the Schema

To extend metadata validation (e.g., include reviewed_by or checksum),
duplicate the current schema, update the $id field, and increment the semantic version tag:

"$id": "https://kansasfrontier.org/schemas/thumbnail_metadata_v2.schema.json"

Then update dependent CI and documentation references.

⸻

⚖️ License

All schema definitions are licensed under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

⸻

🗓️ Change Log

Date	Description
2025-10-11	Initial version — added thumbnail metadata schema + validation guide
2025-10-12	Updated per KFM Markdown formatting and added schema alignment table