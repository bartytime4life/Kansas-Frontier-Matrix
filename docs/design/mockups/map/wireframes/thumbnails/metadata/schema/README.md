<div align="center">

# 🧩 Kansas Frontier Matrix — Map Wireframe Thumbnail Metadata Schema  
`docs/design/mockups/map/wireframes/thumbnails/metadata/schema/`

**Purpose:** JSON Schemas defining the **validation and data structure** for all *map wireframe thumbnail metadata*  
files used within Kansas Frontier Matrix documentation and design systems.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![Schema Validated](https://img.shields.io/badge/JSON--Schema-validated-orange)](https://json-schema.org)  
[![STAC Integration](https://img.shields.io/badge/STAC-linked-blue)](../../../../../../../../data/stac/catalog.json)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines the **JSON Schemas** that govern metadata validation for all  
**map wireframe thumbnail assets** stored under  
`docs/design/mockups/map/wireframes/thumbnails/metadata/`.

Each schema supports automatic **data integrity, interoperability, and reproducibility**  
across the Kansas Frontier Matrix’s documentation system, STAC geospatial catalog, and web UI.  

The schema structure extends the base [Map Thumbnail Metadata Schema](../../../../../map/thumbnails/metadata/schema/README.md)  
to include **UI/UX-specific fields** such as Figma source links, layout variant identifiers, and  
accessibility audit attributes.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/wireframes/thumbnails/metadata/schema/
├── README.md                        # This file
├── wireframe_thumbnail.schema.json  # Schema for individual wireframe thumbnail metadata
└── index.schema.json                # Schema for the aggregated metadata index


⸻

📘 wireframe_thumbnail.schema.json

Description

Defines a single map wireframe thumbnail metadata record, describing one design variant of the
KFM Map Viewer layout (e.g., “timeline overlay,” “mobile compact view,” etc.).

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Map Wireframe Thumbnail Metadata",
  "type": "object",
  "required": ["id", "title", "thumbnail", "variant", "provenance"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the wireframe thumbnail"
    },
    "title": { "type": "string", "description": "Human-readable title" },
    "variant": {
      "type": "string",
      "enum": ["desktop_default", "mobile", "timeline_overlay", "darkmode"],
      "description": "Wireframe variant type"
    },
    "thumbnail": { "type": "string", "description": "Path to PNG/JPG preview file" },
    "description": { "type": "string", "description": "Short description of design intent" },
    "source_figma": {
      "type": "string",
      "description": "Figma file reference or URL to the wireframe source design"
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Design theme tags (e.g. ['timeline', 'overlay', 'UI'])"
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License of the image or derived work"
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum for thumbnail verification"
    },
    "accessibility": {
      "type": "object",
      "properties": {
        "contrast_ratio": { "type": "number", "minimum": 4.5 },
        "alt_text": { "type": "string" }
      },
      "description": "Accessibility attributes following WCAG 2.1 AA"
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string", "description": "Path to source file (Figma or export)" },
        "created_with": { "type": "string", "description": "Tool or script used to generate thumbnail" },
        "commit": { "type": "string", "description": "Git commit reference" }
      }
    }
  }
}


⸻

📗 index.schema.json

Description

Defines an aggregated index of all wireframe thumbnail metadata records, used for
documentation indexing and validation automation.

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Map Wireframe Thumbnails Metadata Index",
  "type": "object",
  "required": ["version", "thumbnails"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "thumbnails": {
      "type": "array",
      "items": { "$ref": "./wireframe_thumbnail.schema.json" }
    }
  }
}


⸻

🧮 Validation Workflow

Validation occurs through GitHub Actions CI (stac-validate.yml and jsonschema.yml):
	•	✅ Schema validation for all JSON files under metadata/
	•	✅ Reference checking against image paths and Figma sources
	•	✅ Checksum verification (sha256-* values)
	•	✅ Metadata completeness (no missing required fields)
	•	✅ Provenance and accessibility validation

Manual Validation Example:

python -m jsonschema -i wireframe_thumbnails_metadata.json schema/wireframe_thumbnail.schema.json


⸻

🧩 Integration with KFM Systems

Component	Purpose	Linked Standard
STAC Catalog (data/stac/catalog.json)	Links design thumbnails to their geospatial dataset layers	STAC 1.0.0
Web UI (React + MapLibreGL)	Displays design previews for documentation and map viewer	WCAG 2.1 AA
Figma Exports	Provides the design source and layout intent	Figma Design System
CI/CD Workflows	Automates schema validation and checksum verification	MCP / JSON Schema


⸻

🧾 Related References
	•	Map Wireframe Thumbnails Metadata
	•	Map Thumbnails Metadata Schema
	•	Kansas Frontier Matrix Web UI Architecture
	•	Data Format Standards

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Time · Terrain · History · Knowledge Graphs

</div>
```
