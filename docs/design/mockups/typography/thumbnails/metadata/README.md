<div align="center">

# 🔤 Kansas Frontier Matrix — Typography Thumbnails Metadata  
`docs/design/mockups/typography/thumbnails/metadata/`

**Purpose:** Define and validate structured metadata for typography thumbnail assets  
used in the Kansas Frontier Matrix (KFM) design system, ensuring documentation reproducibility,  
visual consistency, and accessibility compliance.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains the **metadata index** describing all **typography thumbnail assets**  
from `docs/design/mockups/typography/thumbnails/`.  
Each record represents a visual preview of typographic standards (headings, paragraphs, type scale, etc.)  
and includes accessibility validation, provenance, and semantic linkage to Figma and style tokens.

These JSON files ensure:
- 📊 **Traceable provenance** for each design artifact  
- ♿ **Accessibility compliance** through WCAG 2.1 AA contrast metrics  
- 🔒 **Checksum validation** for reproducibility  
- 🧩 **Cross-linking** between typography assets and KFM’s CSS variable definitions  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/typography/thumbnails/metadata/
├── README.md                             # This file
├── typography_thumbnails_metadata.json   # Aggregated metadata for all thumbnails
└── schema/                               # Validation schemas
    ├── typography_thumbnail.schema.json
    └── index.schema.json


⸻

🧱 Metadata Structure

Each entry documents a single typography thumbnail asset used in the KFM Design System.
Metadata includes font hierarchy, design origin, contrast compliance, and provenance details.

Example Record

{
  "id": "heading_styles_thumb",
  "title": "Heading Styles Thumbnail",
  "file": "heading_styles_thumb.png",
  "description": "Thumbnail showing typography hierarchy and scale from H1 to H6.",
  "category": "headings",
  "theme": ["typography", "hierarchy", "readability"],
  "creator": "KFM Design Team",
  "license": "CC-BY-4.0",
  "source_figma": "figma/typography_design_v1.fig",
  "checksum": "sha256-9f83e38c4bd6f702a0d5e83cd65a1b2d3c909b8a27c9e8f1...",
  "provenance": {
    "derived_from": "../wireframes/typography_design_v1.fig",
    "created_with": "Figma Export",
    "commit": "{{ GIT_COMMIT }}"
  },
  "accessibility": {
    "contrast_ratio": 4.8,
    "alt_text": "Typography hierarchy preview showing Inter typefaces for H1–H6 and body text."
  },
  "tokens_reference": {
    "font_family": "--kfm-font-sans",
    "heading_scale": "--kfm-font-size-xl",
    "line_height": "--kfm-line-height-base"
  }
}


⸻

🧩 Field Reference

Field	Type	Description
id	string	Unique identifier for the thumbnail (kebab-case).
title	string	Human-readable title.
file	string	Path to the thumbnail image file.
description	string	Short summary of what the thumbnail represents.
category	string	Type of typography (e.g. headings, paragraphs, monospace).
theme	array	Design context tags (e.g. “hierarchy”, “legibility”).
creator	string	Author or design team attribution.
license	string	Asset license (default: CC-BY-4.0).
source_figma	string	Reference to the original Figma file.
checksum	string	SHA-256 hash to verify the exported file integrity.
provenance	object	Metadata about file creation, source, and Git reference.
accessibility	object	Contrast ratio and alt text for accessibility validation.
tokens_reference	object	Links to KFM CSS variable definitions controlling typography.


⸻

🧮 Validation Workflow

All metadata is validated in CI/CD pipelines (jsonschema.yml + stac-validate.yml)
to ensure completeness and compliance with documentation standards.

Validation Checks
	•	✅ Schema compliance with typography_thumbnail.schema.json
	•	✅ File existence and path validation
	•	✅ SHA-256 checksum validation
	•	✅ Accessibility compliance (contrast ≥ 4.5)
	•	✅ Token reference existence (--kfm-font-* variables verified in CSS)

Manual Validation Example:

python -m jsonschema -i typography_thumbnails_metadata.json schema/typography_thumbnail.schema.json


⸻

♿ Accessibility & Typography Guidelines

Typography thumbnails must conform to the KFM Accessibility Design Framework:
	•	Contrast ratio ≥ 4.5:1 for body text and ≥ 3:1 for headings
	•	Alt text describes the visual style hierarchy and intent
	•	Fonts verified for legibility (Inter, Roboto Mono, or equivalent open-source family)
	•	Alignment with CSS tokens (--kfm-font-size-*, --kfm-line-height-*)

Accessibility is validated during the design QA process and automated through CI.

⸻

🧾 Provenance & Integrity
	•	Design Source: typography_design_v1.fig
	•	Generated By: scripts/generate_thumbnails.py
	•	Validated In: CI pipelines (JSON Schema, checksum, and accessibility tests)
	•	Checksums: Recorded per asset for reproducibility
	•	License: CC-BY 4.0 (Attribution required for derivative works)
	•	MCP Compliance: Document → Validate → Version → Release

⸻

📚 Related References
	•	Typography Thumbnails (Main)
	•	Typography Metadata Schema
	•	Panels Thumbnails Metadata
	•	Map Thumbnails Metadata
	•	Kansas Frontier Matrix Web UI Architecture
	•	Design Token Reference

⸻


<div align="center">


Kansas Frontier Matrix — Documentation-First Design
Readability · Accessibility · Consistency · Provenance

</div>
```
