<div align="center">

# 🧾 Kansas Frontier Matrix — Panel Thumbnails Metadata  
`docs/design/mockups/panels/thumbnails/metadata/`

**Purpose:** Define, validate, and link metadata for all **panel thumbnails** used in the  
Kansas Frontier Matrix (KFM) design and documentation system — ensuring visual assets are  
traceable, accessible, and properly linked to their wireframe sources.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory stores **metadata records** describing the **panel thumbnails** located in  
`docs/design/mockups/panels/thumbnails/`.  

Each metadata entry provides:
- 🎨 Descriptive and semantic information (title, panel type, design variant)  
- 🧩 Provenance (derived from Figma exports and design tools)  
- ♿ Accessibility attributes (contrast ratio, alt text)  
- 🔗 Cross-references to related design and documentation files  
- 🧾 Checksums for reproducibility and validation in CI pipelines  

These metadata files are part of the KFM **Design Documentation Knowledge Graph**, linking visual assets to code, documentation, and historical data contexts.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/panels/thumbnails/metadata/
├── README.md                            # This file
├── panel_thumbnails_metadata.json       # Index of all panel thumbnail records
└── schema/                              # JSON Schemas for validation
    ├── panel_thumbnail.schema.json
    └── index.schema.json


⸻

🧱 Metadata Schema

Each record conforms to the Panel Thumbnail Schema (schema/panel_thumbnail.schema.json)
which defines the standard fields required for accessibility, licensing, and provenance.

Example Record

{
  "id": "panel_filter_layer_thumb",
  "title": "Layer/Filter Panel Thumbnail",
  "thumbnail": "../panel_filter_layer_thumb.png",
  "description": "Thumbnail preview of the Layer/Filter Controls panel for managing map overlays and dataset visibility.",
  "panel_type": "filter",
  "variant": "desktop_default",
  "theme": ["layers", "filters", "map_ui"],
  "creator": "KFM UX/UI Design Team",
  "license": "CC-BY-4.0",
  "source_figma": "figma/panel_wireframes_v1.fig",
  "checksum": "sha256-3a9b78cdefeabc4567d22ef1094aa99d...",
  "provenance": {
    "derived_from": "../wireframes/exports/filter_layer_panel.png",
    "created_with": "scripts/generate_thumbnails.py",
    "commit": "{{ GIT_COMMIT }}"
  },
  "accessibility": {
    "contrast_ratio": 4.7,
    "alt_text": "Filter layer control panel showing toggles and opacity sliders for map layers."
  }
}


⸻

🧩 Field Reference

Field	Type	Description
id	string	Unique thumbnail ID (kebab-case).
title	string	Human-readable name.
thumbnail	string	Relative path to the image file.
description	string	Short summary of panel purpose.
panel_type	string	Panel category (e.g. detail, ai_assistant, filter, search).
variant	string	Design variant (desktop_default, mobile, etc.).
theme	array	Thematic or functional tags (e.g. map_ui, contextual, data_entry).
creator	string	Author or design team.
license	string	Asset license (CC-BY-4.0 by default).
checksum	string	SHA-256 hash for verification.
source_figma	string	Path/URL to Figma file.
provenance	object	Source, commit reference, and creation tool.
accessibility	object	WCAG 2.1 AA compliance metrics (contrast ratio, alt text).


⸻

🧮 Validation Workflow

All thumbnail metadata is automatically validated through CI/CD pipelines (stac-validate.yml, jsonschema.yml).

Validation Checks Include:
	•	Schema compliance (panel_thumbnail.schema.json)
	•	Cross-references with actual image exports
	•	SHA-256 checksum verification
	•	License and attribution presence
	•	Accessibility compliance (contrast_ratio ≥ 4.5)

Manual Validation Example:

python -m jsonschema -i panel_thumbnails_metadata.json schema/panel_thumbnail.schema.json


⸻

♿ Accessibility Requirements

Each metadata entry must include an accessibility section documenting:
	•	Contrast Ratio — verified against WCAG 2.1 AA standard
	•	Alt Text — concise yet descriptive narrative of panel layout and purpose
	•	Color Palette Review — background/foreground pairing verified in both light and dark themes

Accessibility metadata ensures documentation and mockups are usable by all contributors and readers.

⸻

🧾 Provenance & Integrity
	•	Generated From: panel_wireframes_v1.fig (Figma)
	•	Processed By: scripts/generate_thumbnails.py
	•	Checksum Storage: SHA-256 sidecars for each thumbnail file
	•	Validated In: CI pipelines with stac-validate.yml and jsonschema.yml
	•	MCP Compliance: Documented → Built → Validated → Versioned

⸻

📚 Related References
	•	Panel Thumbnails (Main)
	•	Panel Wireframes
	•	Panel Wireframe Exports
	•	Map Thumbnails Metadata
	•	Kansas Frontier Matrix Web UI Architecture

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Time · Terrain · History · Knowledge Graphs

</div>
```
