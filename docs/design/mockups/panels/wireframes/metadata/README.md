<div align="center">

# 🧾 Kansas Frontier Matrix — Panel Wireframe Metadata  
`docs/design/mockups/panels/wireframes/metadata/`

**Purpose:** Define structured metadata for **panel wireframe assets** used in the Kansas Frontier Matrix (KFM)  
Web UI and documentation system — ensuring **traceability**, **accessibility**, and **reproducibility**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory houses the **metadata index** describing all exported **panel wireframes**  
from `../exports/`. Each JSON record corresponds to one design variant (e.g., Detail Panel, AI Assistant Panel).  

All metadata follows the **Master Coder Protocol (MCP)** design documentation standards —  
ensuring every visual artifact is versioned, validated, and linked to its source (`panel_wireframes_v1.fig`).

Metadata files are:
- 🧾 **Machine-readable** (JSON format, validated via JSON Schema)  
- ♿ **Accessibility-compliant** (includes alt text & contrast ratios)  
- 🔁 **Reproducible** (includes provenance and SHA-256 checksums)  
- 🔍 **Cross-linked** to related STAC, Figma, and UI component references  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/panels/wireframes/metadata/
├── README.md                           # This file
├── panel_wireframes_metadata.json      # Aggregated metadata index
└── schema/                             # JSON Schema definitions
    ├── panel_wireframe.schema.json
    └── index.schema.json
````

---

## 🧱 Metadata Structure

Each metadata record defines the **identity**, **context**, **provenance**, and **accessibility metrics**
of a single panel wireframe export. These entries support documentation automation and CI validation.

### 🧩 Example Record

```json
{
  "id": "panel_detail_default",
  "title": "Detail Panel (Default Layout)",
  "thumbnail": "../exports/detail_panel_default.png",
  "description": "Wireframe showing the default Detail Panel layout used to display entity data.",
  "panel_type": "detail",
  "variant": "desktop_default",
  "theme": ["light", "information", "metadata"],
  "creator": "KFM Design Team",
  "license": "CC-BY-4.0",
  "source_figma": "figma/panel_wireframes_v1.fig",
  "checksum": "sha256-9ad73c45b23eaa8fcd0b98c4a54a8adf...",
  "provenance": {
    "derived_from": "panel_wireframes_v1.fig",
    "created_with": "Figma Export",
    "commit": "{{ GIT_COMMIT }}"
  },
  "accessibility": {
    "contrast_ratio": 4.8,
    "alt_text": "Detail panel with metadata tabs and linked entity preview."
  }
}
```

---

## 🧩 Field Reference

| Field             | Type   | Description                                                         |
| ----------------- | ------ | ------------------------------------------------------------------- |
| **id**            | string | Unique identifier for the wireframe (kebab-case).                   |
| **title**         | string | Human-readable title for the panel wireframe.                       |
| **thumbnail**     | string | Relative path to the exported PNG/JPG.                              |
| **description**   | string | Concise summary of the wireframe’s purpose.                         |
| **panel_type**    | string | Type of panel (`detail`, `ai_assistant`, `filter`, `search`, etc.). |
| **variant**       | string | Layout variation (`desktop_default`, `mobile`, etc.).               |
| **theme**         | array  | Design tags indicating function, color scheme, or purpose.          |
| **creator**       | string | Author or design team responsible for the asset.                    |
| **source_figma**  | string | Figma source file or frame reference.                               |
| **license**       | string | Usage license (default: `CC-BY-4.0`).                               |
| **checksum**      | string | SHA-256 hash for verifying export integrity.                        |
| **provenance**    | object | Metadata for creation lineage and version tracking.                 |
| **accessibility** | object | WCAG audit data: contrast ratio, alt text, etc.                     |

---

## 🧮 Validation Workflow

Metadata integrity is continuously validated via **GitHub Actions** (`jsonschema.yml` + `stac-validate.yml`).

### ✅ Automated Checks

* Schema compliance (`panel_wireframe.schema.json`)
* Export file existence verification (`../exports/*.png`)
* SHA-256 checksum consistency
* Required field completion and license verification
* Accessibility compliance (contrast ratio ≥ 4.5 : 1)

### 🧰 Manual Validation Example

```bash
python -m jsonschema -i panel_wireframes_metadata.json schema/panel_wireframe.schema.json
```

---

## ♿ Accessibility Metadata

Accessibility is a required field for each record and validated in CI pipelines.

| Field              | Requirement | Description                                       |
| ------------------ | ----------- | ------------------------------------------------- |
| **contrast_ratio** | ≥ 4.5 : 1   | Minimum verified text/background contrast.        |
| **alt_text**       | Required    | Descriptive caption for assistive technologies.   |
| **verified_by**    | Optional    | Reviewer, audit script, or QA process identifier. |

Accessibility compliance ensures every visual element in the design suite meets **WCAG 2.1 AA** standards.

---

## 🧾 Provenance & Integrity

| Attribute           | Description                                   |
| ------------------- | --------------------------------------------- |
| **Generated By**    | `scripts/generate_wireframe_metadata.py`      |
| **Source File**     | `panel_wireframes_v1.fig` (Figma)             |
| **Validated In CI** | `stac-validate.yml`, `jsonschema.yml`         |
| **Checksums**       | Recorded in `panel_wireframes_metadata.json`  |
| **License**         | [CC-BY 4.0](../../../../../../LICENSE)        |
| **MCP Compliance**  | Documented → Designed → Validated → Published |

---

## 🧭 Integration Notes

| Integration                 | Purpose                                | Reference                            |
| --------------------------- | -------------------------------------- | ------------------------------------ |
| **Panel Wireframe Exports** | Corresponding full-resolution images   | `../exports/`                        |
| **Metadata Schema**         | JSON Schema definitions for validation | `schema/panel_wireframe.schema.json` |
| **Figma Reference**         | Design provenance link                 | `figma/panel_wireframes_v1.fig`      |
| **Design Token Sync**       | Styling consistency across components  | `web/src/styles/tokens.css`          |

---

## 📚 Related References

* [Panels Wireframes (Main)](../README.md)
* [Panel Wireframe Exports](../exports/README.md)
* [Map Wireframes](../../../map/wireframes/README.md)
* [Kansas Frontier Matrix Web UI Architecture](../../../../../../architecture/web_ui_architecture_review.md)
* [Accessibility Design Standards](../../../../design/reviews/accessibility/README.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Context · Accessibility · Provenance · Reproducibility**

</div>
