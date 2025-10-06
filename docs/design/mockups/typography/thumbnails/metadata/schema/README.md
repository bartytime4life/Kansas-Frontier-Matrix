<div align="center">

# 🔤 Kansas Frontier Matrix — Typography Thumbnail Metadata Schema  
`docs/design/mockups/typography/thumbnails/metadata/schema/`

**Purpose:** Define and validate JSON Schemas for **typography thumbnail metadata**  
ensuring visual consistency, traceability, and accessibility compliance across  
Kansas Frontier Matrix’s design system.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines **JSON Schema specifications** for metadata files under  
`docs/design/mockups/typography/thumbnails/metadata/`.

Schemas are used to validate typography-related thumbnail metadata, guaranteeing:
- 📐 **Consistent structure** across all documentation artifacts  
- ♿ **Accessibility compliance** (contrast ratios, alt text)  
- 🔍 **Traceability** via Figma, CSS token, and commit references  
- 🧩 **Integration** with other design metadata systems (Map, Panels, Timeline)  
- 🔒 **Reproducibility** in MCP workflows (document → validate → version → release)  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/typography/thumbnails/metadata/schema/
├── README.md                          # This documentation file
├── typography_thumbnail.schema.json   # Schema for individual thumbnail metadata
└── index.schema.json                  # Schema for the aggregated index


⸻

📘 typography_thumbnail.schema.json

Description

Defines the structure of an individual typography thumbnail metadata record.
Each record corresponds to a PNG/JPG preview showing part of the typography system
(e.g., type scale, headings, paragraphs, or code blocks).

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Typography Thumbnail Metadata Schema",
  "type": "object",
  "required": ["id", "title", "category", "thumbnail", "license", "provenance", "accessibility"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the thumbnail asset"
    },
    "title": {
      "type": "string",
      "description": "Readable name of the design thumbnail"
    },
    "category": {
      "type": "string",
      "enum": ["headings", "paragraphs", "code", "scale", "tokens"],
      "description": "The type of typography asset represented"
    },
    "thumbnail": {
      "type": "string",
      "description": "Relative path to the image file (e.g., ../heading_styles_thumb.png)"
    },
    "description": {
      "type": "string",
      "description": "Brief explanation of what the image represents"
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Tags or visual themes (e.g., ['typography','hierarchy','accessibility'])"
    },
    "tokens_reference": {
      "type": "object",
      "properties": {
        "font_family": { "type": "string" },
        "font_size": { "type": "string" },
        "line_height": { "type": "string" },
        "color_token": { "type": "string" }
      },
      "description": "References to CSS variables in web/src/styles/tokens.css"
    },
    "source_figma": {
      "type": "string",
      "description": "Path or URL to the Figma source file"
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License covering this design artifact"
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 hash for verifying file integrity"
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string", "description": "Figma file or export path" },
        "created_with": { "type": "string", "description": "Tool or process used" },
        "commit": { "type": "string", "description": "Git commit hash linking this version" }
      },
      "description": "Record of design lineage and reproducibility"
    },
    "accessibility": {
      "type": "object",
      "required": ["contrast_ratio", "alt_text"],
      "properties": {
        "contrast_ratio": {
          "type": "number",
          "minimum": 4.5,
          "description": "Measured contrast ratio according to WCAG 2.1 AA"
        },
        "alt_text": {
          "type": "string",
          "description": "Descriptive text for screen readers and non-visual contexts"
        }
      },
      "description": "Accessibility metadata for documentation and auditing"
    }
  }
}


⸻

📗 index.schema.json

Description

Defines the aggregate metadata index for typography thumbnail metadata files.
Used to verify completeness, timestamps, and batch consistency across assets.

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Typography Thumbnails Metadata Index",
  "type": "object",
  "required": ["version", "updated", "thumbnails"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "thumbnails": {
      "type": "array",
      "items": { "$ref": "./typography_thumbnail.schema.json" }
    }
  }
}


⸻

🧮 Validation Workflow

All JSON metadata is validated via GitHub Actions CI/CD pipelines.

Automated Checks Include:
	•	✅ Schema structure compliance (JSON Schema Draft 2020-12)
	•	✅ Checksum match for image integrity
	•	✅ File existence checks for referenced thumbnails
	•	✅ Contrast ratio ≥ 4.5 for accessibility
	•	✅ Valid tokens_reference matching defined CSS variables

Manual validation example:

python -m jsonschema -i ../typography_thumbnails_metadata.json schema/typography_thumbnail.schema.json


⸻

♿ Accessibility Compliance

Typography metadata includes strict accessibility validation fields:

Field	Requirement	Description
contrast_ratio	≥ 4.5	Ensures legible type and compliant color contrast
alt_text	Required	Describes the image content for screen readers
tokens_reference	Required	Ensures design reflects actual implemented tokens in CSS
color_safe	Recommended	Confirms palette visibility for color-blind users


⸻

🧾 Provenance & Integrity
	•	Design Source: typography_design_v1.fig (Figma)
	•	Generated By: scripts/generate_thumbnails.py
	•	Validated By: CI (jsonschema.yml, stac-validate.yml)
	•	Checksum Storage: Recorded in typography_thumbnails_metadata.json
	•	MCP Compliance: Documented → Validated → Versioned → Published

⸻

📚 Related References
	•	Typography Thumbnails Metadata
	•	Typography Thumbnails
	•	Panels Thumbnails Metadata Schema
	•	Map Thumbnails Metadata Schema
	•	Kansas Frontier Matrix Web UI Architecture
	•	KFM Design Tokens

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Readability · Accessibility · Traceability · Reproducibility

</div>
```
