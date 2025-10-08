<div align="center">

# 🔤 Kansas Frontier Matrix — Typography Wireframe Metadata  
`docs/design/mockups/typography/wireframes/metadata/`

**Purpose:** Define and validate structured metadata for **typography wireframes and exports**,  
linking design artifacts to accessibility standards, Figma sources, and KFM design tokens.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../..)  
[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](../../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory holds **metadata JSON files** describing each exported typography wireframe  
stored in `../exports/`. Each record documents hierarchy, accessibility compliance, token mappings,  
and provenance — forming a reproducible dataset for the **Kansas Frontier Matrix (KFM)** Typography System.  

All records follow **Master Coder Protocol (MCP)** principles:
- Documented — clearly defined schema and purpose  
- Validated — tested by CI pipelines and schema validators  
- Versioned — tracked via commit SHA and checksum  
- Published — linked to assets and design tokens  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/typography/wireframes/metadata/
├── README.md                           # This file
├── typography_wireframes_metadata.json # Aggregate metadata index
└── schema/                             # JSON Schema definitions
    ├── typography_wireframe.schema.json
    └── index.schema.json
````

---

## 🧱 Metadata Structure

Each record defines design data about a wireframe export — including style category, CSS variable mapping,
and WCAG compliance. Metadata ensures design assets can be validated and cross-referenced with token definitions.

### 🧩 Example Record

```json
{
  "id": "typography_heading_hierarchy",
  "title": "Typography — Heading Hierarchy",
  "thumbnail": "../exports/heading_hierarchy.png",
  "description": "Wireframe demonstrating typographic hierarchy for headings H1–H6 and subheadings, using the Inter font family.",
  "category": "headings",
  "theme": ["typography", "hierarchy", "readability"],
  "creator": "KFM Design System Team",
  "license": "CC-BY-4.0",
  "source_figma": "figma/typography_wireframes_v1.fig",
  "checksum": "sha256-b2f9736ee98cde9a4317f03f96cfd2812a7bb1dfde99a1...",
  "tokens_reference": {
    "font_family": "--kfm-font-display",
    "font_weight": "--kfm-font-weight-bold",
    "line_height": "--kfm-line-height-base",
    "color_token": "--kfm-color-fg"
  },
  "provenance": {
    "derived_from": "typography_wireframes_v1.fig",
    "created_with": "Figma Export",
    "commit": "{{ GIT_COMMIT }}"
  },
  "accessibility": {
    "contrast_ratio": 4.7,
    "alt_text": "Wireframe showing heading styles H1–H6 with standardized spacing and alignment."
  }
}
```

---

## 🧾 Field Reference

| Field              | Type   | Description                            |
| ------------------ | ------ | -------------------------------------- |
| `id`               | string | Unique identifier (kebab-case).        |
| `title`            | string | Human-readable name.                   |
| `thumbnail`        | string | Path to exported PNG/JPG asset.        |
| `description`      | string | Short summary of layout purpose.       |
| `category`         | string | Classification (headings, body, code). |
| `theme`            | array  | Keywords / context tags.               |
| `creator`          | string | Author or contributor.                 |
| `license`          | string | License type (default: CC-BY-4.0).     |
| `source_figma`     | string | Source Figma file reference.           |
| `checksum`         | string | SHA-256 hash for file integrity.       |
| `tokens_reference` | object | Links design tokens to CSS variables.  |
| `provenance`       | object | Tracks lineage and commit reference.   |
| `accessibility`    | object | Includes WCAG compliance and alt text. |

---

## 🧮 Validation Workflow

All metadata files are validated automatically in CI/CD using JSON Schema and checksum verification.

### ✅ Automated Checks

* Validate against `schema/typography_wireframe.schema.json`
* Confirm all linked image files exist under `../exports/`
* Verify SHA-256 checksums for export integrity
* Ensure `accessibility` section includes `contrast_ratio` and `alt_text`
* Cross-check `tokens_reference` values exist in `tokens.css`

### 🧰 Manual Validation Example

```bash
python -m jsonschema -i typography_wireframes_metadata.json schema/typography_wireframe.schema.json
```

---

## ♿ Accessibility Requirements

Typography wireframes must conform to **WCAG 2.1 AA**:

| Requirement              | Target                           | Validation                    |
| ------------------------ | -------------------------------- | ----------------------------- |
| **Contrast Ratio**       | ≥ 4.5 : 1                        | Verified via Stark + Pa11y CI |
| **Alt Text**             | Required for all images          | Present in metadata           |
| **Readable Scale**       | Base font ≥ 16 px                | Checked in token set          |
| **Font Tokens**          | Must match `--kfm-*` variables   | Validated by schema           |
| **Screen Reader Labels** | Descriptive captions for exports | Reviewed manually             |

Accessibility reports are generated and logged in `accessibility/` review directories.

---

## ⚙️ Continuous Integration (Metadata Validation)

```yaml
# .github/workflows/typography_metadata_validate.yml
on:
  pull_request:
    paths:
      - "docs/design/mockups/typography/wireframes/metadata/**/*.json"
jobs:
  validate-typography-metadata:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate JSON Schema
        run: python -m jsonschema -i docs/design/mockups/typography/wireframes/metadata/typography_wireframes_metadata.json docs/design/mockups/typography/wireframes/metadata/schema/typography_wireframe.schema.json
      - name: Verify checksums
        run: sha256sum -c checksums.txt
```

---

## 🧾 Provenance & Integrity

| Field                 | Description                                    |
| --------------------- | ---------------------------------------------- |
| **Source Design**     | `typography_wireframes_v1.fig`                 |
| **Generated By**      | `scripts/generate_wireframe_metadata.py`       |
| **Validated In**      | GitHub Actions CI (JSON Schema + checksum)     |
| **Checksum Tracking** | Recorded per export asset                      |
| **License**           | CC-BY-4.0 (open documentation standard)        |
| **MCP Compliance**    | Documented → Validated → Versioned → Published |

---

## 📚 Related References

* [Typography Wireframes (Main)](../README.md)
* [Typography Wireframe Exports](../exports/)
* [Typography Thumbnails Metadata](../../thumbnails/metadata/)
* [Panels Wireframe Metadata](../../../panels/wireframes/metadata/)
* [Design Tokens Reference](../../../../design-tokens/)
* [Web UI Architecture Review](../../../../../reviews/architecture/web_ui_architecture_review.md)

---

<div align="center">

### 🔤 Kansas Frontier Matrix — Documentation-First Typography Metadata

**Readable · Accessible · Traceable · Reproducible**

</div>
