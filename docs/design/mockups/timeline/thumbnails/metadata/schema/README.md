<div align="center">

# 🕰️ Kansas Frontier Matrix — Timeline Thumbnail Metadata Schema  
`docs/design/mockups/timeline/thumbnails/metadata/schema/`

**Purpose:** Define JSON Schemas to validate **timeline thumbnail metadata** records, ensuring design assets  
follow KFM’s documentation-first, accessible, and reproducible metadata standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains the **authoritative JSON Schemas** that define and validate all  
timeline thumbnail metadata records stored in `docs/design/mockups/timeline/thumbnails/metadata/`.

Schemas ensure:
- ✅ Structural and semantic consistency across metadata files  
- 🔗 Provenance linkage to Figma and export assets  
- ♿ Accessibility compliance via WCAG 2.1 AA checks  
- 🔒 Integrity through checksum validation  
- 📚 Alignment with **Master Coder Protocol (MCP)** principles for reproducibility  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/timeline/thumbnails/metadata/schema/
├── README.md                        # This documentation file
├── timeline_thumbnail.schema.json   # Schema for individual timeline thumbnail metadata
└── index.schema.json                # Schema for the aggregate index


⸻

📘 timeline_thumbnail.schema.json

Description

Defines the structure for a single timeline thumbnail metadata record, describing
a preview image representing a KFM timeline design state (default, condensed, mobile, overlay_map).

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Timeline Thumbnail Metadata Schema",
  "type": "object",
  "required": ["id", "title", "variant", "thumbnail", "license", "provenance", "accessibility"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the thumbnail asset"
    },
    "title": {
      "type": "string",
      "description": "Human-readable title of the timeline thumbnail"
    },
    "variant": {
      "type": "string",
      "enum": ["default", "condensed", "mobile", "overlay_map"],
      "description": "Timeline design variation represented by this thumbnail"
    },
    "thumbnail": {
      "type": "string",
      "description": "Path to the PNG or JPG thumbnail image"
    },
    "description": {
      "type": "string",
      "description": "Brief textual description of the thumbnail and its context"
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Keywords or design tags describing the timeline context"
    },
    "source_figma": {
      "type": "string",
      "description": "Path or URL to the Figma source design file"
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License governing the design asset"
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum for image file integrity verification"
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string", "description": "Figma export or pipeline source" },
        "created_with": { "type": "string", "description": "Tool or script used to generate thumbnail" },
        "commit": { "type": "string", "description": "Git commit reference for traceability" }
      },
      "description": "Object recording lineage and reproducibility details"
    },
    "accessibility": {
      "type": "object",
      "required": ["contrast_ratio", "alt_text"],
      "properties": {
        "contrast_ratio": {
          "type": "number",
          "minimum": 4.5,
          "description": "Minimum verified color contrast ratio (WCAG 2.1 AA)"
        },
        "alt_text": {
          "type": "string",
          "description": "Descriptive alternative text for the thumbnail"
        }
      },
      "description": "Accessibility audit data ensuring visual and descriptive compliance"
    }
  }
}


⸻

📗 index.schema.json

Description

Defines the aggregate index schema for timeline_thumbnails_metadata.json,
which compiles all thumbnail metadata entries into a unified dataset for validation and discovery.

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Timeline Thumbnails Metadata Index",
  "type": "object",
  "required": ["version", "updated", "thumbnails"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "thumbnails": {
      "type": "array",
      "items": { "$ref": "./timeline_thumbnail.schema.json" }
    }
  }
}


⸻

🧮 Validation Workflow

All timeline thumbnail metadata files are validated during CI/CD pipelines (jsonschema.yml, stac-validate.yml).

Automated Checks
	•	✅ Schema validation (JSON Schema Draft 2020-12)
	•	✅ File existence and image path checks
	•	✅ SHA-256 checksum verification
	•	✅ Accessibility compliance (contrast_ratio ≥ 4.5, alt_text present)
	•	✅ License and provenance completeness

Manual Validation Example:

python -m jsonschema -i timeline_thumbnails_metadata.json schema/timeline_thumbnail.schema.json


⸻

♿ Accessibility Enforcement

Field	Requirement	Description
contrast_ratio	≥ 4.5	Ensures text and elements meet WCAG 2.1 AA visibility requirements
alt_text	Required	Provides meaningful screen-reader descriptions
color_safe	Recommended	Design reviewed for color-blind friendliness

All accessibility data is reviewed by the design QA team before commit approval.

⸻

🧾 Provenance & Reproducibility
	•	Source File: timeline_wireframes_v1.fig
	•	Generated By: scripts/generate_thumbnails.py
	•	Validated In: GitHub Actions (jsonschema.yml, stac-validate.yml)
	•	Checksum Storage: SHA-256 per asset, recorded in metadata index
	•	MCP Compliance: Documented → Validated → Versioned → Published

⸻

📚 Related References
	•	Timeline Thumbnails Metadata
	•	Timeline Wireframe Metadata Schema
	•	Panels Thumbnails Metadata Schema
	•	Map Thumbnails Metadata Schema
	•	Kansas Frontier Matrix Web UI Architecture

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Time · Terrain · History · Knowledge Graphs

</div>
```
