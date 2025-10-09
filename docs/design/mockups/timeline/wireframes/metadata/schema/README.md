<div align="center">

# 🧩 Kansas Frontier Matrix — Timeline Wireframe Metadata Schema  
`docs/design/mockups/timeline/wireframes/metadata/schema/`

**Purpose:** Define and validate JSON Schemas for **timeline wireframe metadata**  
to ensure design integrity, provenance, accessibility, and temporal interoperability across the KFM stack.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory defines the **authoritative JSON Schemas** for  
`docs/design/mockups/timeline/wireframes/metadata/`.  

These schemas enforce:
- 📊 **Structural consistency** for all timeline wireframe metadata records  
- 🧾 **Provenance integrity** — Figma source, Git commit, checksum linkage  
- ♿ **Accessibility compliance** — contrast ratios and alt text validation  
- ⌛ **Temporal semantics** — zoom and granularity rules aligned with OWL-Time  
- 🔗 **Interoperability** — with STAC, map, and panel metadata schemas  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/timeline/wireframes/metadata/schema/
├── README.md                        # This documentation file
├── timeline_wireframe.schema.json   # Single-record schema definition
└── index.schema.json                # Schema for aggregated metadata index
````

---

## 📘 `timeline_wireframe.schema.json`

**Purpose:** Define the schema for an individual wireframe metadata record describing one layout variant
(`default`, `condensed`, `mobile`, or `overlay_map`).

### 🧩 Schema Outline

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Timeline Wireframe Metadata Schema",
  "type": "object",
  "required": ["id", "title", "variant", "thumbnail", "provenance", "accessibility"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier (kebab-case)."
    },
    "title": { "type": "string", "description": "Human-readable name for the wireframe." },
    "variant": {
      "type": "string",
      "enum": ["default", "condensed", "mobile", "overlay_map"],
      "description": "Design variation represented by the export."
    },
    "thumbnail": {
      "type": "string",
      "description": "Path to exported image (e.g., ../exports/timeline_default.png)."
    },
    "description": { "type": "string", "description": "Brief description of layout and intent." },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Tags such as ['timeline','map_sync','overlay']."
    },
    "zoom_behavior": {
      "type": "string",
      "enum": ["discrete_ticks", "continuous_scale", "hybrid"],
      "description": "Timeline zoom model."
    },
    "time_granularity": {
      "type": "string",
      "enum": ["year", "decade", "century", "mixed"],
      "description": "Primary time granularity visualized."
    },
    "linked_components": {
      "type": "array",
      "items": { "type": "string" },
      "description": "React components tied to this design (e.g. TimelineCanvas.tsx)."
    },
    "source_figma": { "type": "string", "description": "URL/path to Figma file or frame." },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License covering this design artifact."
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum for verifying export integrity."
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string" },
        "created_with": { "type": "string" },
        "commit": { "type": "string" }
      },
      "description": "Record of design lineage and reproducibility."
    },
    "accessibility": {
      "type": "object",
      "required": ["contrast_ratio", "alt_text"],
      "properties": {
        "contrast_ratio": {
          "type": "number",
          "minimum": 4.5,
          "description": "Measured contrast ratio (WCAG 2.1 AA)."
        },
        "alt_text": {
          "type": "string",
          "description": "Descriptive text for assistive technologies."
        }
      },
      "description": "Accessibility audit metadata."
    }
  }
}
```

---

## 📗 `index.schema.json`

**Purpose:** Validate the aggregate metadata index file `timeline_wireframes_metadata.json`
for bulk QA and automation.

### 🧩 Schema Outline

```json
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
```

---

## 🧮 Validation Workflow

All schema validations are automated in CI/CD through
`jsonschema.yml` and `stac-validate.yml`.

### ✅ Automated Checks

* JSON Schema compliance for each record
* SHA-256 checksum verification
* File path existence for `../exports/*.png`
* Accessibility attributes (`contrast_ratio`, `alt_text`) required
* Optional cross-validation with STAC temporal metadata

### 🧰 Manual Validation

```bash
python -m jsonschema -i ../timeline_wireframes_metadata.json schema/timeline_wireframe.schema.json
```

---

## 🧠 Integration Notes

| Target                 | Purpose                                     | Linkage                                         |
| ---------------------- | ------------------------------------------- | ----------------------------------------------- |
| **Figma**              | Source of truth for wireframe layouts       | `timeline_wireframes_v1.fig`                    |
| **Web UI (React)**     | Implementation of timeline components       | `web/src/components/timeline/*`                 |
| **Docs Portal**        | Auto-generated previews & indexes           | `docs/design/mockups/timeline/*`                |
| **Temporal Semantics** | OWL-Time alignment for intervals & instants | [W3C OWL-Time](https://www.w3.org/TR/owl-time/) |
| **STAC Integration**   | Temporal fields filtered by timeline UI     | `data/stac/*`                                   |

---

## 🧾 Provenance & Compliance

| Attribute          | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| **Generated By**   | `scripts/generate_schema_docs.py`                                         |
| **Validated In**   | CI pipelines: `jsonschema.yml`, `stac-validate.yml`                       |
| **Schema Draft**   | [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema) |
| **License**        | [CC-BY 4.0](../../../../../../../LICENSE)                                 |
| **MCP Compliance** | Documented → Validated → Published                                        |

---

## 📚 Related References

* [Timeline Wireframe Metadata](../README.md)
* [Timeline Wireframe Exports](../../exports/README.md)
* [Panels Wireframe Metadata Schema](../../../panels/wireframes/metadata/schema/README.md)
* [Map Wireframe Metadata Schema](../../../map/wireframes/metadata/schema/README.md)
* [Kansas Frontier Matrix Web UI Architecture](../../../../../../../architecture/web_ui_architecture_review.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Time · Terrain · History · Knowledge Graphs**

</div>
