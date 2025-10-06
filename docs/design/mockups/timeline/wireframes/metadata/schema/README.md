<div align="center">

# 🧩 Kansas Frontier Matrix — Timeline Wireframe Metadata Schema  
`docs/design/mockups/timeline/wireframes/metadata/schema/`

**Purpose:** Define JSON Schemas to validate **timeline wireframe metadata** used in KFM documentation and UI design, ensuring consistency, provenance, accessibility, and time-aware interoperability.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-validated-orange)](https://json-schema.org)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains the **authoritative JSON Schemas** for all metadata entries in  
`docs/design/mockups/timeline/wireframes/metadata/`.

The schemas enforce:

- 📊 **Structural consistency** across all timeline wireframe records  
- 🧾 **Provenance & integrity** (Figma source, Git commit, checksums)  
- ♿ **Accessibility** (contrast ratios, meaningful alt text)  
- ⌛ **Temporal semantics** (variant/zoom behavior aligned with OWL-Time concepts)  
- 🔗 **Interoperability** with related specs (STAC temporal fields, Map/Panel wireframe schemas)

---

## 🗂️ Directory Layout

```text
docs/design/mockups/timeline/wireframes/metadata/schema/
├── README.md                        # This file
├── timeline_wireframe.schema.json   # Schema for a single timeline wireframe record
└── index.schema.json                # Schema for the aggregated metadata index


⸻

📘 timeline_wireframe.schema.json

Description

Defines the structure of a single timeline wireframe metadata record describing one design variant
(e.g., default, condensed, mobile, overlay_map).

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Timeline Wireframe Metadata Schema",
  "type": "object",
  "required": ["id", "title", "variant", "thumbnail", "provenance", "accessibility"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier (kebab/slug)."
    },
    "title": { "type": "string", "description": "Human-readable name of the wireframe." },
    "variant": {
      "type": "string",
      "enum": ["default", "condensed", "mobile", "overlay_map"],
      "description": "Design variation represented by the export."
    },
    "thumbnail": {
      "type": "string",
      "description": "Relative path to the exported PNG/JPG (e.g., ../exports/timeline_default.png)."
    },
    "description": {
      "type": "string",
      "description": "Brief summary of the layout and intended use."
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Tags (e.g., ['timeline','map_sync','overlay'])."
    },
    "zoom_behavior": {
      "type": "string",
      "enum": ["discrete_ticks", "continuous_scale", "hybrid"],
      "description": "How the timeline zoom model is presented."
    },
    "time_granularity": {
      "type": "string",
      "enum": ["year", "decade", "century", "mixed"],
      "description": "Primary granularity emphasized in the design."
    },
    "linked_components": {
      "type": "array",
      "items": { "type": "string" },
      "description": "React components tied to this design (e.g., TimelineCanvas.tsx)."
    },
    "source_figma": {
      "type": "string",
      "description": "Path/URL to the Figma file or frame."
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License for the design export."
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum for the export image."
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string", "description": "Figma source or export path." },
        "created_with": { "type": "string", "description": "Tool/process used (e.g., Figma Export)." },
        "commit": { "type": "string", "description": "Git commit reference." }
      },
      "description": "Reproducibility and lineage details."
    },
    "accessibility": {
      "type": "object",
      "required": ["contrast_ratio", "alt_text"],
      "properties": {
        "contrast_ratio": {
          "type": "number",
          "minimum": 4.5,
          "description": "Minimum contrast ratio validated (WCAG 2.1 AA)."
        },
        "alt_text": {
          "type": "string",
          "description": "Screen-reader description of the export."
        }
      },
      "description": "Accessibility audit data."
    }
  }
}


⸻

📗 index.schema.json

Description

Specifies the aggregate metadata index for timeline wireframes, enabling bulk validation and automation.

Schema Outline

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Timeline Wireframes Metadata Index",
  "type": "object",
  "required": ["version", "updated", "wireframes"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "wireframes": {
      "type": "array",
      "items": { "$ref": "./timeline_wireframe.schema.json" }
    }
  }
}


⸻

🧮 Validation Workflow

These schemas are enforced by CI/CD (e.g., jsonschema.yml, stac-validate.yml):
	•	✅ JSON Schema compliance for each record
	•	🔒 SHA-256 checksum verification for referenced exports
	•	🖼️ Path existence checks for ../exports/*.png
	•	♿ Accessibility audit fields required (contrast_ratio, alt_text)
	•	🔗 Optional cross-checks with STAC temporal metadata (where applicable)

Manual validation:

python -m jsonschema -i ../timeline_wireframes_metadata.json schema/timeline_wireframe.schema.json


⸻

🧠 Integration Notes

Target	Purpose	Linkage
Figma	Source of truth for layouts	timeline_wireframes_v1.fig
Web UI (React)	Implementation reference for Timeline components	web/src/components/timeline/*
Docs Portals	Auto-generated previews & indexes	docs/design/mockups/timeline/*
Temporal Semantics	Alignment with OWL-Time for periods/instants	OWL-Time (W3C)
STAC	Temporal fields in data layers filtered by the UI	data/stac/*


⸻

📚 Related References
	•	Timeline Wireframe Metadata
	•	Timeline Wireframe Exports
	•	Panels Wireframe Metadata Schema
	•	Map Wireframe Metadata Schema
	•	Kansas Frontier Matrix Web UI Architecture

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Time · Terrain · History · Knowledge Graphs

</div>
```
