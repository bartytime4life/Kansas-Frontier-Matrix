<div align="center">

# 🧩 Kansas Frontier Matrix — Panel Wireframe Metadata Schema  
`docs/design/mockups/panels/wireframes/metadata/schema/`

**Purpose:** Define the **JSON Schema** structure for validating wireframe metadata  
used to describe Kansas Frontier Matrix (KFM) **UI panel components** — ensuring consistency,  
traceability, and reproducibility across documentation, design, and implementation.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-validated-orange)](https://json-schema.org)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines **validation schemas** for metadata files under  
`docs/design/mockups/panels/wireframes/metadata/`.  
These JSON Schemas ensure all exported panel wireframe metadata (`*.json`) follows a unified structure,  
linking designs to their provenance, accessibility audits, and Figma source files.

The schema extends the **Map Wireframe Metadata Schema** with panel-specific fields like:
- `panel_type` (e.g., detail, ai_assistant, filter, search)  
- `ui_variant` (desktop_default, mobile, tablet, etc.)  
- `interaction_model` (scroll, tabbed, collapsible)  
- `linked_component` (React component path)  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/panels/wireframes/metadata/schema/
├── README.md                       # This file
├── panel_wireframe.schema.json     # Schema for individual wireframe metadata
└── index.schema.json               # Schema for aggregated metadata index


⸻

📘 panel_wireframe.schema.json

Description

Defines the structure for a single panel wireframe record, validating metadata properties
for exported panel images and ensuring consistent linkage between design artifacts and code components.

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Panel Wireframe Metadata Schema",
  "type": "object",
  "required": ["id", "title", "panel_type", "thumbnail", "provenance"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the panel wireframe"
    },
    "title": { "type": "string", "description": "Readable name for the wireframe design" },
    "panel_type": {
      "type": "string",
      "enum": ["detail", "ai_assistant", "filter", "search", "mobile_stack"],
      "description": "Panel category (defines UI behavior and content type)"
    },
    "ui_variant": {
      "type": "string",
      "enum": ["desktop_default", "mobile", "tablet", "timeline_overlay"],
      "description": "Responsive layout variant represented by this design"
    },
    "thumbnail": {
      "type": "string",
      "description": "Relative path to exported PNG/JPG thumbnail image"
    },
    "description": {
      "type": "string",
      "description": "Summary of panel purpose and design intent"
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Visual and contextual theme tags"
    },
    "linked_component": {
      "type": "string",
      "description": "React component name or path (e.g., web/src/components/panels/DetailPanel.tsx)"
    },
    "source_figma": {
      "type": "string",
      "description": "Path or URL to original Figma file or frame ID"
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License for the design asset"
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum for image validation"
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string", "description": "Figma source file or image export" },
        "created_with": { "type": "string", "description": "Tool or process used for generation" },
        "commit": { "type": "string", "description": "Git commit reference" }
      }
    },
    "accessibility": {
      "type": "object",
      "properties": {
        "contrast_ratio": { "type": "number", "minimum": 4.5 },
        "alt_text": { "type": "string" }
      },
      "description": "Accessibility metadata for UI contrast and screen-reader descriptions"
    }
  }
}


⸻

📗 index.schema.json

Description

Defines the metadata index structure for panel_wireframes_metadata.json,
enabling bulk validation and automation across multiple panel entries.

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Panel Wireframes Metadata Index",
  "type": "object",
  "required": ["version", "panels"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "panels": {
      "type": "array",
      "items": { "$ref": "./panel_wireframe.schema.json" }
    }
  }
}


⸻

🧮 Validation Workflow

All panel wireframe metadata undergoes validation in CI/CD workflows:
	•	🧾 Schema validation via jsonschema.yml and stac-validate.yml
	•	✅ Required fields (id, title, type, provenance, accessibility)
	•	🔗 Reference validation (image paths, Figma files)
	•	🔒 Checksum verification (sha256-* pattern)
	•	♿ Accessibility compliance (contrast ≥ 4.5)

Manual Validation Example:

python -m jsonschema -i ../panel_wireframes_metadata.json schema/panel_wireframe.schema.json


⸻

🧠 Design Integration

Integration Target	Description	Linked Spec
Figma	Source of truth for UI layouts	panel_wireframes_v1.fig
Web UI (React)	References validated metadata for panel rendering	/web/src/components/panels/*
Documentation	Pulls metadata for automated inclusion in Markdown READMEs	docs/design/mockups/panels/*
CI/CD	Automated schema validation, checksum checks, and accessibility audits	.github/workflows/*


⸻

📚 Related References
	•	Panels Wireframe Metadata
	•	Panel Wireframe Exports
	•	Map Wireframe Metadata Schema
	•	Kansas Frontier Matrix Web UI Architecture
	•	Accessibility Standards

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Time · Terrain · History · Knowledge Graphs

</div>
```
