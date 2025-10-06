<div align="center">

# 🧩 Kansas Frontier Matrix — Map Thumbnail Metadata Schema  
`docs/design/mockups/map/thumbnails/metadata/schema/`

**Purpose:** JSON Schemas defining the **structure and validation rules** for map thumbnail metadata files  
used in both **documentation** and the **web interface** of the Kansas Frontier Matrix (KFM).

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../..)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../../../.github/workflows/stac-validate.yml)  
[![JSON Schema](https://img.shields.io/badge/Schema-JSON%20Validated-orange)](https://json-schema.org)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines **validation schemas** for all **map thumbnail metadata** used throughout  
KFM’s documentation and UI design layers. Each thumbnail metadata JSON file must conform  
to these schemas to ensure interoperability with the KFM **STAC catalog**, **frontend layer configuration**,  
and **AI/ML data provenance pipeline**.

The schemas support:

- 🧩 Validation of thumbnail metadata files (`*.json`) in `docs/design/mockups/map/thumbnails/metadata/`  
- 🔗 Integration with STAC assets (`data/stac/items/*.json`) via linked identifiers  
- 🔍 Consistent fields across design and data layers (title, source, license, spatial/temporal extents)  
- 🧾 Provenance and reproducibility metadata (checksum, creation date, source attribution)  
- ♿ Accessibility and design-standard metadata (contrast rating, visual theme, thumbnail alt text)

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/thumbnails/metadata/schema/
├── README.md                 # This documentation file
├── thumbnail.schema.json     # Schema for individual thumbnail metadata
└── index.schema.json         # Schema for the aggregated thumbnail index


⸻

📘 thumbnail.schema.json

Description

Defines a single thumbnail metadata record (e.g., ks_topo_1894.json).
Each file describes a preview image for one geospatial or historical layer and its linkage to data sources.

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Map Thumbnail Metadata",
  "type": "object",
  "required": ["id", "title", "thumbnail", "source_stac", "license", "provenance"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the thumbnail (matches STAC item ID)"
    },
    "title": { "type": "string", "description": "Human-readable title" },
    "thumbnail": { "type": "string", "description": "Relative path to PNG or JPG file" },
    "description": { "type": "string", "description": "Short description of the map layer" },
    "source_stac": {
      "type": "string",
      "description": "Path to linked STAC item (e.g., data/stac/items/ks_topo_1894.json)"
    },
    "spatial_extent": {
      "type": "array",
      "minItems": 4,
      "maxItems": 4,
      "items": { "type": "number" },
      "description": "Bounding box [W, S, E, N] in WGS84 coordinates"
    },
    "temporal_extent": {
      "type": "object",
      "properties": {
        "start": { "type": "string", "format": "date" },
        "end": { "type": "string", "format": "date" }
      },
      "required": ["start"]
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Design theme or map layer categories"
    },
    "color_key": {
      "type": "array",
      "items": { "type": "string", "pattern": "^#([A-Fa-f0-9]{6})$" },
      "description": "Array of color hex codes representing dominant colors"
    },
    "license": { "type": "string", "description": "License of the thumbnail asset" },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum for image integrity verification"
    },
    "provenance": {
      "type": "object",
      "properties": {
        "derived_from": { "type": "string" },
        "created_with": { "type": "string" },
        "commit": { "type": "string" }
      },
      "required": ["derived_from"]
    },
    "accessibility": {
      "type": "object",
      "properties": {
        "contrast_ratio": { "type": "number", "minimum": 4.5 },
        "alt_text": { "type": "string" }
      }
    }
  }
}


⸻

📗 index.schema.json

Description

Defines the aggregate metadata structure for all map thumbnails (e.g., thumbnails_metadata.json).
This index enables bulk validation, search, and catalog integration.

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Map Thumbnails Metadata Index",
  "type": "object",
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "thumbnails": {
      "type": "array",
      "items": { "$ref": "./thumbnail.schema.json" }
    }
  },
  "required": ["version", "thumbnails"]
}


⸻

🧮 Validation Workflow

These schemas are validated automatically in GitHub Actions via the
stac-validate.yml workflow:
	•	Validates all JSON files under metadata/ against thumbnail.schema.json
	•	Confirms all referenced STAC assets exist
	•	Cross-verifies SHA-256 checksums
	•	Publishes validation report to GitHub Actions summary

Manual Validation Example:

python -m jsonschema -i ks_topo_1894.json schema/thumbnail.schema.json


⸻

🧾 Related References
	•	Map Thumbnails Metadata
	•	STAC Catalog
	•	Kansas Frontier Matrix Architecture
	•	Data Format Standards

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Time · Terrain · History · Knowledge Graphs

</div>
```
