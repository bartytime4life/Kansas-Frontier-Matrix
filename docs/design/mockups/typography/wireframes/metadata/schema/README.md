<div align="center">

# 🔤 Kansas Frontier Matrix — Typography Wireframe Metadata Schema  
`docs/design/mockups/typography/wireframes/metadata/schema/`

**Purpose:** Define and validate JSON Schemas for **Typography Wireframe Metadata**, ensuring **reproducibility**,  
**accessibility**, and **traceability** across KFM’s typography design documentation and codebase.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![Schema Validation](https://img.shields.io/badge/JSON--Schema-Draft%202020--12-orange)](https://json-schema.org)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines the **JSON Schema specifications** for metadata files stored under  
`docs/design/mockups/typography/wireframes/metadata/`.

Schemas are used to:

- ✅ Enforce **structural consistency** in typography wireframe metadata  
- ♿ Ensure **accessibility compliance** (WCAG 2.1 AA)  
- 🧩 Maintain **traceability** to Figma, CSS tokens, and commit SHAs  
- 🧮 Automate validation in **CI/CD pipelines**  
- 🔗 Enable **interoperability** with related schemas (Panels, Map, Timeline)

---

## 🗂️ Directory Layout

```text
docs/design/mockups/typography/wireframes/metadata/schema/
├── README.md                           # This documentation file
├── typography_wireframe.schema.json    # Schema for a single wireframe record
└── index.schema.json                   # Schema for the aggregate index (list of records)
````

---

## 📘 `typography_wireframe.schema.json` (Single Record)

**Description:** Structure of one typography wireframe metadata record — documenting the visual characteristics,
token mappings, and accessibility details of a specific design export (e.g., headings, body text, code blocks).

### Schema (copy/paste)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Typography Wireframe Metadata Schema",
  "type": "object",
  "required": [
    "id",
    "title",
    "category",
    "thumbnail",
    "license",
    "provenance",
    "accessibility"
  ],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the wireframe asset (kebab/snake-case)."
    },
    "title": {
      "type": "string",
      "description": "Human-readable name of the wireframe layout."
    },
    "category": {
      "type": "string",
      "enum": ["headings", "paragraphs", "code", "responsive"],
      "description": "Typography category represented by the wireframe."
    },
    "thumbnail": {
      "type": "string",
      "description": "Relative path to exported image (e.g., ../exports/heading_hierarchy.png)."
    },
    "description": {
      "type": "string",
      "description": "Brief summary describing the purpose and content of the wireframe."
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Tags for thematic context (e.g., typography, readability)."
    },
    "tokens_reference": {
      "type": "object",
      "properties": {
        "font_family": { "type": "string", "description": "CSS token for font family (e.g., --kfm-font-display)." },
        "font_size": { "type": "string", "description": "CSS token for font size (e.g., --kfm-font-size-base)." },
        "line_height": { "type": "string", "description": "CSS token for line height (e.g., --kfm-line-height-base)." },
        "color_token": { "type": "string", "description": "CSS token for text color (e.g., --kfm-color-fg)." }
      },
      "additionalProperties": false,
      "description": "Mappings to design tokens ensuring parity between design and implementation."
    },
    "source_figma": {
      "type": "string",
      "description": "Path or URL to the source Figma file or frame."
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License for the design asset (default CC-BY-4.0)."
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 hash (prefixed with 'sha256-') verifying file integrity."
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": {
          "type": "string",
          "description": "Source Figma reference (file/frame) or export path."
        },
        "created_with": {
          "type": "string",
          "description": "Tool/process used for the export (e.g., 'Figma Export')."
        },
        "commit": {
          "type": "string",
          "description": "Git commit SHA linking this record to version control."
        }
      },
      "additionalProperties": false,
      "description": "Provenance tracking for documentation integrity."
    },
    "accessibility": {
      "type": "object",
      "required": ["contrast_ratio", "alt_text"],
      "properties": {
        "contrast_ratio": {
          "type": "number",
          "minimum": 4.5,
          "description": "Measured contrast ratio (WCAG 2.1 AA minimum ≥ 4.5)."
        },
        "alt_text": {
          "type": "string",
          "minLength": 5,
          "description": "Descriptive alternative text for screen readers."
        },
        "color_safe": {
          "type": "boolean",
          "description": "Whether the palette passes color-blind tests (recommended)."
        }
      },
      "additionalProperties": false,
      "description": "Accessibility metadata for compliance verification."
    }
  },
  "additionalProperties": false
}
```

---

## 📗 `index.schema.json` (Aggregate Index)

**Description:** Structure of the aggregate index file `typography_wireframes_metadata.json`
containing multiple metadata entries.

### Schema (copy/paste)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Typography Wireframes Metadata Index",
  "type": "object",
  "required": ["version", "updated", "wireframes"],
  "properties": {
    "version": {
      "type": "string",
      "pattern": "^\\d+\\.\\d+\\.\\d+$",
      "description": "Semantic version of the index (e.g., 1.0.0)."
    },
    "updated": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp of the last update."
    },
    "wireframes": {
      "type": "array",
      "items": { "$ref": "./typography_wireframe.schema.json" },
      "minItems": 1,
      "description": "List of wireframe metadata records."
    }
  },
  "additionalProperties": false
}
```

---

## ♿ Accessibility Requirements

Typography wireframe metadata **must** provide these validated fields:

| Field                          | Requirement     | Description                             |
| ------------------------------ | --------------- | --------------------------------------- |
| `accessibility.contrast_ratio` | ≥ 4.5           | Meets WCAG 2.1 AA for text contrast     |
| `accessibility.alt_text`       | Required        | Describes the export for screen readers |
| `accessibility.color_safe`     | Recommended     | Palette tested for color-blind safety   |
| `tokens_reference.*`           | Required tokens | Map to existing `--kfm-*` CSS variables |

---

## 🧮 Validation Workflow

All metadata is validated automatically via CI using JSON Schema + checksum checks.

### Automated Checks

* ✅ Validate structure against `typography_wireframe.schema.json`
* ✅ Verify image paths exist under `../exports/`
* ✅ Confirm SHA-256 checksums (sidecars or listed values)
* ✅ Enforce `contrast_ratio` ≥ 4.5 and presence of `alt_text`
* ✅ Cross-check `tokens_reference` against `tokens.css`

### Manual Validation Example

```bash
python -m jsonschema \
  -i ../typography_wireframes_metadata.json \
  schema/index.schema.json
```

---

## ⚙️ Continuous Integration (Schema & Integrity)

```yaml
# .github/workflows/typography_schema_validate.yml
on:
  pull_request:
    paths:
      - "docs/design/mockups/typography/wireframes/metadata/**/*.json"
      - "web/src/styles/tokens.css"
jobs:
  schema-validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate index schema
        run: |
          python -m jsonschema \
            -i docs/design/mockups/typography/wireframes/metadata/typography_wireframes_metadata.json \
            docs/design/mockups/typography/wireframes/metadata/schema/index.schema.json
      - name: Validate each record
        run: |
          jq -c '.wireframes[]' docs/design/mockups/typography/wireframes/metadata/typography_wireframes_metadata.json \
          | while read -r rec; do
              printf '%s' "$rec" > /tmp/rec.json
              python -m jsonschema -i /tmp/rec.json \
                docs/design/mockups/typography/wireframes/metadata/schema/typography_wireframe.schema.json
            done
      - name: Verify checksums (if sidecars present)
        run: |
          find docs/design/mockups/typography/wireframes/exports -name "*.sha256" -print0 | \
          xargs -0 -I{} sh -c 'shasum -a 256 -c "{}"'
```

---

## 🧾 Provenance & Integrity

| Field               | Description                                    |
| ------------------- | ---------------------------------------------- |
| **Design Source**   | `typography_wireframes_v1.fig` (Figma master)  |
| **Generated By**    | `scripts/generate_wireframe_metadata.py`       |
| **Validated In**    | GitHub Actions CI (JSON Schema + checksum)     |
| **Checksum Policy** | SHA-256 values recorded per export             |
| **License**         | CC-BY-4.0                                      |
| **MCP Compliance**  | Documented → Validated → Versioned → Published |

---

## 📚 Related References

* **Typography Wireframe Metadata** (`../README.md`)
* **Typography Wireframe Exports** (`../exports/`)
* **Thumbnails Metadata Schema** (`../../thumbnails/metadata/schema/`)
* **Panels Wireframe Metadata Schema** (parallel structure)
* **Design Tokens** (`web/src/styles/tokens.css`)
* **Web UI Architecture Review** (`../../../../../reviews/architecture/web_ui_architecture_review.md`)

---

<div align="center">

### 🔤 Kansas Frontier Matrix — Documentation-First Design

**Readable · Accessible · Traceable · Reproducible**

</div>
