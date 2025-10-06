<div align="center">

# 🧩 Kansas Frontier Matrix — Panel Thumbnail Metadata Schema  
`docs/design/mockups/panels/thumbnails/metadata/schema/`

**Purpose:** Define and enforce **validation schemas** for panel thumbnail metadata  
used in Kansas Frontier Matrix (KFM) documentation, mockups, and UI component design.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines **JSON Schema documents** for validating metadata files describing  
**panel thumbnails** stored in `docs/design/mockups/panels/thumbnails/metadata/`.  

These schemas ensure:
- 📊 **Consistency** across design metadata files  
- ♿ **Accessibility compliance** through required contrast/alt-text attributes  
- 🧩 **Interoperability** with related schemas (wireframes, map thumbnails, STAC assets)  
- 🔗 **Provenance tracking** for source design and Figma file lineage  
- 🧾 **MCP reproducibility** — each design record traceable through commits and checksums  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/panels/thumbnails/metadata/schema/
├── README.md                     # This documentation file
├── panel_thumbnail.schema.json   # Schema for individual panel thumbnail metadata
└── index.schema.json             # Schema for aggregate metadata index


⸻

📘 panel_thumbnail.schema.json

Description

This schema defines the structure for a single thumbnail metadata record,
describing a design thumbnail for one KFM panel component (e.g., Detail, AI Assistant, Filter, Search).

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Panel Thumbnail Metadata Schema",
  "type": "object",
  "required": ["id", "title", "panel_type", "thumbnail", "license", "provenance"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the panel thumbnail (kebab-case)"
    },
    "title": { "type": "string", "description": "Human-readable title of the design asset" },
    "panel_type": {
      "type": "string",
      "enum": ["detail", "ai_assistant", "filter", "search", "mobile_stack"],
      "description": "Specifies which panel type the thumbnail represents"
    },
    "variant": {
      "type": "string",
      "enum": ["desktop_default", "mobile", "tablet"],
      "description": "Responsive layout variant represented by the thumbnail"
    },
    "thumbnail": {
      "type": "string",
      "description": "Relative path to the thumbnail image file"
    },
    "description": {
      "type": "string",
      "description": "Brief textual description of the panel design"
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Categorical or thematic tags"
    },
    "source_figma": {
      "type": "string",
      "description": "Link or reference to the originating Figma file"
    },
    "linked_wireframe": {
      "type": "string",
      "description": "Path to the corresponding wireframe export image"
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License governing use of this thumbnail asset"
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum for asset integrity verification"
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string", "description": "Source Figma or export file" },
        "created_with": { "type": "string", "description": "Tool or script used for generation" },
        "commit": { "type": "string", "description": "Git commit reference" }
      }
    },
    "accessibility": {
      "type": "object",
      "required": ["contrast_ratio", "alt_text"],
      "properties": {
        "contrast_ratio": {
          "type": "number",
          "minimum": 4.5,
          "description": "Minimum contrast ratio validated (WCAG 2.1 AA)"
        },
        "alt_text": {
          "type": "string",
          "description": "Descriptive alternative text for screen readers"
        }
      },
      "description": "Accessibility audit data for the thumbnail asset"
    }
  }
}


⸻

📗 index.schema.json

Description

Defines the structure of the aggregate metadata index file (panel_thumbnails_metadata.json)
used to catalog all panel thumbnails for automated discovery and validation.

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Panel Thumbnails Metadata Index",
  "type": "object",
  "required": ["version", "updated", "thumbnails"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "thumbnails": {
      "type": "array",
      "items": { "$ref": "./panel_thumbnail.schema.json" }
    }
  }
}


⸻

🧮 Validation Workflow

Panel thumbnail metadata files are automatically validated through the CI/CD pipelines:
	•	Schema Validation: Confirms structure compliance (panel_thumbnail.schema.json)
	•	Checksum Verification: Ensures all files’ SHA-256 hashes match declared checksums
	•	Path Validation: Confirms referenced files exist in exports directory
	•	Accessibility Audit: Enforces contrast ≥ 4.5:1 and alt text presence

Manual validation command:

python -m jsonschema -i panel_thumbnails_metadata.json schema/panel_thumbnail.schema.json


⸻

♿ Accessibility Compliance

Each thumbnail metadata entry must include:
	•	contrast_ratio (≥ 4.5 for text contrast)
	•	alt_text (succinct yet descriptive of panel purpose)
	•	Optional theme tags for UI/UX semantic grouping

Accessibility metadata ensures Kansas Frontier Matrix remains usable for all contributors
and compliant with WCAG 2.1 AA standards.

⸻

🧾 Provenance & Integrity
	•	Generated From: panel_wireframes_v1.fig (Figma source)
	•	Export Process: scripts/generate_thumbnails.py
	•	Validated By: GitHub Actions (jsonschema.yml and stac-validate.yml)
	•	Checksums: Stored in panel_thumbnails_metadata.json
	•	MCP Compliance: Documentation → Validation → Versioning → Publication

⸻

📚 Related References
	•	Panel Thumbnails Metadata
	•	Panel Wireframe Metadata Schema
	•	Map Thumbnail Metadata Schema
	•	Kansas Frontier Matrix Web UI Architecture
	•	Design System Accessibility Standards

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Time · Terrain · History · Knowledge Graphs

</div>
```
