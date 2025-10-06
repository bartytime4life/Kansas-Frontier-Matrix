<div align="center">

# 🧩 Kansas Frontier Matrix — Archived Map Thumbnail Metadata Schema  
`docs/design/mockups/map/thumbnails/archive/metadata/schema/`

**Standardized · Validated · Machine-Readable Provenance**

</div>

---

## 🧭 Overview

This directory defines the **JSON Schema specifications** used to validate  
archived map thumbnail metadata files stored in  
`docs/design/mockups/map/thumbnails/archive/metadata/`.  

Each schema ensures metadata for archived thumbnails remains **consistent, machine-readable,  
and semantically interoperable** across the Kansas Frontier Matrix (KFM) ecosystem.  

By aligning with **JSON Schema Draft-07**, **DCAT**, and **STAC** conventions, these definitions  
support reproducibility, data integrity, and integration into the broader KFM  
knowledge graph and spatiotemporal data catalog.

---

## 📁 Directory Structure

```text
docs/design/mockups/map/thumbnails/archive/metadata/schema/
├── README.md                                         # This documentation (GitHub-safe)
└── map_thumbnail_metadata.schema.json                # JSON Schema validator for archived map thumbnails

File Naming Convention:
{schema_subject}.schema.json
Example → map_thumbnail_metadata.schema.json

⸻

🧾 Example Schema — map_thumbnail_metadata.schema.json

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Archived Map Thumbnail Metadata Schema",
  "description": "Defines structure and validation rules for archived map thumbnail metadata used in the Kansas Frontier Matrix documentation system.",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for the archived map thumbnail, typically includes version suffix (e.g., _v1)."
    },
    "title": {
      "type": "string",
      "description": "Descriptive title for the thumbnail, including map topic and version."
    },
    "author": {
      "type": "string",
      "description": "Author or design team responsible for the original map thumbnail."
    },
    "created": {
      "type": "string",
      "format": "date",
      "description": "Original creation date of the thumbnail."
    },
    "archived": {
      "type": "string",
      "format": "date",
      "description": "Date this version was archived or replaced."
    },
    "superseded_by": {
      "type": "string",
      "description": "Relative path or identifier of the thumbnail that replaces this version."
    },
    "reason": {
      "type": "string",
      "description": "Explanation of why the thumbnail was archived (e.g., updated colors, layout change, accessibility improvements)."
    },
    "source": {
      "type": "string",
      "description": "Relative path to the original thumbnail file in the archive."
    },
    "related": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of related components, layers, or documents linked to this thumbnail (relative paths)."
    },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Descriptive keywords to assist with search and filtering."
    },
    "status": {
      "type": "string",
      "enum": ["archived", "deprecated"],
      "description": "Indicates the archival state of the asset."
    },
    "license": {
      "type": "string",
      "description": "License declaration for the thumbnail (default: CC-BY-4.0)."
    }
  },
  "required": ["id", "title", "author", "created", "archived", "license"],
  "additionalProperties": false
}


⸻

🧮 Validation Workflow
	1.	Create or Update Metadata
Add or edit a metadata file under:
docs/design/mockups/map/thumbnails/archive/metadata/
	2.	Validate Schema
Run schema validation manually before commit:

jsonschema -i metadata/20251009_map-treaty-boundaries-thumb_v1.json schema/map_thumbnail_metadata.schema.json


	3.	Continuous Integration (CI)
All metadata is automatically validated as part of the
KFM CI/CD pipeline (.github/workflows/stac-validate.yml or make validate-json).
	4.	Error Reporting
If validation fails, CI logs display the invalid field(s) and suggest corrections.

⸻

🧩 Standards Alignment

Standard	Description	Relevance to KFM
JSON Schema Draft-07	Schema validation and machine readability	Base validation standard
DCAT (Data Catalog Vocabulary)	Metadata interoperability for datasets	Supports catalog integration
STAC (SpatioTemporal Asset Catalog)	Geospatial and temporal metadata interoperability	Used for dataset discovery
CIDOC CRM	Cultural heritage ontology for provenance	Adds semantic depth for historical assets
OWL-Time	Temporal reasoning and date interval alignment	For structured date-based queries


⸻

🧠 Schema Extension Guidelines

To extend the schema (for example, adding fields like checksum, reviewed_by, or linked_issue):
	1.	Copy the current schema to a new version file:
map_thumbnail_metadata_v2.schema.json
	2.	Update the $id or title field with a new version tag.
	3.	Add or modify property definitions.
	4.	Update references in the CI configuration and README files.
	5.	Validate all existing metadata against the updated schema to ensure backward compatibility.

⸻

🧩 Integration with Knowledge Graph and STAC Catalog

Each validated metadata file is ingested into KFM’s knowledge graph and STAC index,
where schema-defined fields become properties on corresponding graph nodes.

Metadata Field	Graph Property	STAC Equivalent
id	identifier	id
title	name	title
created	created	properties.datetime
archived	endDate	properties.end_datetime
superseded_by	replacedBy	links.replaced_by
source	derivedFrom	assets.source.href
license	license	license


⸻

⚖️ License

All schema files and metadata specifications are released under
Creative Commons Attribution 4.0 International (CC-BY 4.0)

Credit: Kansas Frontier Matrix Design Team · 2025

Attribution required for reuse, modification, or redistribution.
Commercial use permitted with credit.

⸻

🗓️ Change Log

Date	Description
2025-10-14	Initial version — added schema structure, workflow, and integration
2025-10-15	Added standards alignment and schema extension guide