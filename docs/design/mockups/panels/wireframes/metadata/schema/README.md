<div align="center">

# 🧩 Kansas Frontier Matrix — Panel Wireframe Metadata Schema  
`docs/design/mockups/panels/wireframes/metadata/schema/`

**Purpose:** Define the **JSON Schema** structure for validating wireframe metadata  
describing Kansas Frontier Matrix (KFM) **UI panel components** — ensuring consistency,  
traceability, accessibility, and reproducibility between documentation, design, and implementation.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines **validation schemas** for metadata files stored in  
`docs/design/mockups/panels/wireframes/metadata/`.  

These JSON Schemas ensure:
- 📊 **Consistent structure** across all wireframe metadata records  
- 🔗 **Linked provenance** to Figma design sources and Git commits  
- ♿ **Accessibility validation** for alt text and color contrast ratios  
- 🧩 **Interoperability** with related schemas (Map, Timeline, AI Assistant)  
- 🧱 **Reproducibility** following MCP pipeline standards (`Document → Validate → Publish`)  

The schema extends common KFM metadata fields with **panel-specific properties**:
- `panel_type` (e.g., detail, ai_assistant, filter, search, mobile_stack)  
- `ui_variant` (e.g., desktop_default, mobile, tablet)  
- `interaction_model` (scroll, tabbed, collapsible)  
- `linked_component` (React component path)  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/panels/wireframes/metadata/schema/
├── README.md                       # This documentation file
├── panel_wireframe.schema.json     # Schema for individual metadata entries
└── index.schema.json               # Schema for aggregated metadata index
````

---

## 📘 `panel_wireframe.schema.json`

**Purpose:** Define the JSON Schema for validating a single wireframe record —
enforcing structural consistency, accessibility fields, and provenance tracking.

### 🧩 Schema Outline

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Panel Wireframe Metadata Schema",
  "type": "object",
  "required": ["id", "title", "panel_type", "thumbnail", "provenance"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the panel wireframe."
    },
    "title": { "type": "string", "description": "Readable name for the wireframe design." },
    "panel_type": {
      "type": "string",
      "enum": ["detail", "ai_assistant", "filter", "search", "mobile_stack"],
      "description": "Defines the panel’s function and UI behavior."
    },
    "ui_variant": {
      "type": "string",
      "enum": ["desktop_default", "mobile", "tablet", "timeline_overlay"],
      "description": "Responsive layout or display variation."
    },
    "thumbnail": {
      "type": "string",
      "description": "Relative path to the exported PNG/JPG thumbnail image."
    },
    "description": {
      "type": "string",
      "description": "Short summary of panel intent and context."
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Tags denoting color scheme, function, or design theme."
    },
    "linked_component": {
      "type": "string",
      "description": "Path to React component (e.g., web/src/components/panels/DetailPanel.tsx)."
    },
    "source_figma": {
      "type": "string",
      "description": "Reference to original Figma file or frame ID."
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License for reuse of the wireframe asset."
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 hash used to verify export integrity."
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string", "description": "Figma source file or export name." },
        "created_with": { "type": "string", "description": "Tool or script used to generate export." },
        "commit": { "type": "string", "description": "Git commit ID linking version." }
      },
      "description": "Reproducibility and design lineage metadata."
    },
    "accessibility": {
      "type": "object",
      "required": ["contrast_ratio", "alt_text"],
      "properties": {
        "contrast_ratio": {
          "type": "number",
          "minimum": 4.5,
          "description": "Verified contrast ratio per WCAG 2.1 AA."
        },
        "alt_text": {
          "type": "string",
          "description": "Descriptive text for assistive technologies."
        }
      },
      "description": "Accessibility audit and validation data."
    }
  }
}
```

---

## 📗 `index.schema.json`

**Purpose:** Validate the aggregated index file `panel_wireframes_metadata.json` —
used for batch validation, automated ingestion, and documentation rendering.

### 🧩 Schema Outline

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Panel Wireframes Metadata Index",
  "type": "object",
  "required": ["version", "updated", "panels"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "panels": {
      "type": "array",
      "items": { "$ref": "./panel_wireframe.schema.json" }
    }
  }
}
```

---

## 🧮 Validation Workflow

Validation is performed automatically in CI/CD pipelines for consistency, provenance, and accessibility compliance.

| Step  | Process                       | Validation Target                           |
| ----- | ----------------------------- | ------------------------------------------- |
| **1** | JSON Schema validation        | `panel_wireframe.schema.json`               |
| **2** | Metadata integrity check      | `panel_wireframes_metadata.json`            |
| **3** | File existence verification   | `../exports/*.png`                          |
| **4** | SHA-256 checksum verification | Exported image hashes                       |
| **5** | Accessibility audit           | Contrast ≥ 4.5 : 1 and descriptive alt text |

### 🧰 Manual Validation Example

```bash
python -m jsonschema -i ../panel_wireframes_metadata.json schema/panel_wireframe.schema.json
```

---

## 🧠 Design Integration

| Target             | Purpose                                  | Linked Resource                |
| ------------------ | ---------------------------------------- | ------------------------------ |
| **Figma**          | Primary design source                    | `panel_wireframes_v1.fig`      |
| **Web UI (React)** | Panel component linkage                  | `web/src/components/panels/*`  |
| **Documentation**  | Auto-included metadata in panel READMEs  | `docs/design/mockups/panels/*` |
| **CI/CD**          | Schema and checksum validation workflows | `.github/workflows/*`          |

---

## 🧾 Provenance & MCP Compliance

| Attribute        | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| **Generated By** | `scripts/generate_panel_schema_docs.py`                                   |
| **Validated In** | CI Workflows: `jsonschema.yml`, `stac-validate.yml`                       |
| **Schema Draft** | [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema) |
| **License**      | [CC-BY 4.0](../../../../../../../LICENSE)                                 |
| **MCP Stage**    | Documented → Validated → Published                                        |

---

## 📚 Related References

* [Panels Wireframe Metadata](../README.md)
* [Panel Wireframe Exports](../../exports/README.md)
* [Map Wireframe Metadata Schema](../../../map/wireframes/metadata/schema/README.md)
* [Kansas Frontier Matrix Web UI Architecture](../../../../../../../architecture/web_ui_architecture_review.md)
* [Accessibility Standards](../../../../../design/reviews/accessibility/README.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Structure · Accessibility · Provenance · Reproducibility**

</div>
