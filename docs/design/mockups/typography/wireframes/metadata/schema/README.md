<div align="center">

# 🔤 Kansas Frontier Matrix — Typography Wireframe Metadata Schema  
`docs/design/mockups/typography/wireframes/metadata/schema/`

**Purpose:** Define and validate JSON Schemas for **Typography Wireframe Metadata**, ensuring reproducibility,  
accessibility, and traceability across KFM’s typography design documentation and codebase.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![Schema Validation](https://img.shields.io/badge/JSON--Schema-Draft%202020--12-orange)](https://json-schema.org)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines the **JSON Schema specifications** for metadata files stored under  
`docs/design/mockups/typography/wireframes/metadata/`.

These schemas are used to:
- ✅ Enforce **structural consistency** in typography wireframe metadata  
- ♿ Ensure **accessibility compliance** (WCAG 2.1 AA standards)  
- 🧩 Maintain **traceability** across design sources (Figma, CSS tokens, commit IDs)  
- 🧮 Automate validation in **CI/CD pipelines**  
- 🔗 Enable **interoperability** with related metadata schemas (Panels, Map, Timeline)  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/typography/wireframes/metadata/schema/
├── README.md                           # This documentation file
├── typography_wireframe.schema.json    # Schema for single wireframe metadata file
└── index.schema.json                   # Schema for aggregate metadata index


⸻

📘 typography_wireframe.schema.json

Description

Defines the structure for a single typography wireframe metadata record.
Each record documents the visual and accessibility characteristics of a specific design export
(e.g., headings, body text, code blocks, responsive type layouts).

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Typography Wireframe Metadata Schema",
  "type": "object",
  "required": ["id", "title", "category", "thumbnail", "license", "provenance", "accessibility"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the wireframe asset"
    },
    "title": {
      "type": "string",
      "description": "Human-readable name of the wireframe layout"
    },
    "category": {
      "type": "string",
      "enum": ["headings", "paragraphs", "code", "responsive"],
      "description": "Specifies which typography category the wireframe represents"
    },
    "thumbnail": {
      "type": "string",
      "description": "Path to the exported image (e.g., ../exports/heading_hierarchy.png)"
    },
    "description": {
      "type": "string",
      "description": "Brief summary describing the purpose and content of the wireframe"
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Tags defining the thematic context (e.g., typography, accessibility)"
    },
    "tokens_reference": {
      "type": "object",
      "properties": {
        "font_family": { "type": "string", "description": "Linked CSS token for font family" },
        "font_size": { "type": "string", "description": "Linked CSS token for font size" },
        "line_height": { "type": "string", "description": "Linked CSS token for line height" },
        "color_token": { "type": "string", "description": "Linked CSS token for text color" }
      },
      "description": "Mappings to design tokens ensuring consistency between design and implementation"
    },
    "source_figma": {
      "type": "string",
      "description": "Path or URL to the source Figma file"
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License under which the design asset is released"
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 hash verifying file integrity"
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": {
          "type": "string",
          "description": "Source Figma frame or export path"
        },
        "created_with": {
          "type": "string",
          "description": "Tool or process used to generate export"
        },
        "commit": {
          "type": "string",
          "description": "Git commit reference linking this record to version control"
        }
      },
      "description": "Provenance tracking for documentation integrity"
    },
    "accessibility": {
      "type": "object",
      "required": ["contrast_ratio", "alt_text"],
      "properties": {
        "contrast_ratio": {
          "type": "number",
          "minimum": 4.5,
          "description": "Measured color contrast ratio (WCAG 2.1 AA minimum)"
        },
        "alt_text": {
          "type": "string",
          "description": "Descriptive alternative text for accessibility compliance"
        }
      },
      "description": "Accessibility metadata for compliance verification"
    }
  }
}


⸻

📗 index.schema.json

Description

Defines the structure for the aggregate index file
(typography_wireframes_metadata.json), which contains multiple metadata entries
for typography wireframe exports.

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Typography Wireframes Metadata Index",
  "type": "object",
  "required": ["version", "updated", "wireframes"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "wireframes": {
      "type": "array",
      "items": { "$ref": "./typography_wireframe.schema.json" }
    }
  }
}


⸻

🧮 Validation Workflow

Metadata validation occurs automatically through CI pipelines using
jsonschema.yml and stac-validate.yml.

Automated Checks Include:
	•	✅ Schema validation for all metadata records
	•	✅ SHA-256 checksum verification for exported files
	•	✅ File existence validation (../exports/*.png)
	•	✅ Accessibility compliance checks (contrast_ratio ≥ 4.5)
	•	✅ CSS token cross-verification (--kfm-font-*, --kfm-line-height-*, etc.)

Manual Validation Example:

python -m jsonschema -i ../typography_wireframes_metadata.json schema/typography_wireframe.schema.json


⸻

♿ Accessibility Requirements

Typography wireframe metadata must include the following validated fields:

Field	Requirement	Description
contrast_ratio	≥ 4.5	Minimum contrast ratio required by WCAG 2.1 AA.
alt_text	Required	Must describe visual content for screen readers.
color_safe	Recommended	Confirms palette passes color-blind testing.
tokens_reference	Required	Ensures mapping to KFM CSS design tokens.


⸻

🧾 Provenance & Integrity
	•	Design Source: typography_wireframes_v1.fig (Figma master design)
	•	Generated By: scripts/generate_wireframe_metadata.py
	•	Validated In: CI/CD (jsonschema.yml, stac-validate.yml)
	•	Checksum Verification: SHA-256 sidecars ensure immutability
	•	License: CC-BY-4.0 (open documentation standard)
	•	MCP Compliance: Documentation → Validation → Versioning → Publication

⸻

📚 Related References
	•	Typography Wireframe Metadata
	•	Typography Wireframes Exports
	•	Typography Thumbnails Metadata Schema
	•	Panels Wireframe Metadata Schema
	•	Design Token Definitions
	•	Kansas Frontier Matrix Web UI Architecture

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Readability · Accessibility · Traceability · Reproducibility

</div>
```
