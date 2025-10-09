<div align="center">

# 🧩 Kansas Frontier Matrix — Map Wireframe Thumbnail Metadata Schema  
`docs/design/mockups/map/wireframes/thumbnails/metadata/schema/`

**Purpose:** Define and validate the **JSON Schema structures** that govern map wireframe thumbnail metadata  
within the Kansas Frontier Matrix (KFM) documentation, ensuring interoperability, provenance, and reproducibility.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![Schema Validated](https://img.shields.io/badge/JSON--Schema-validated-orange)](https://json-schema.org)  
[![STAC Integration](https://img.shields.io/badge/STAC-linked-blue)](../../../../../../../../data/stac/catalog.json)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains the **authoritative JSON Schemas** for validating metadata files  
under `docs/design/mockups/map/wireframes/thumbnails/metadata/`.

These schemas ensure:
- ✅ **Structural consistency** across all thumbnail metadata entries  
- 🧾 **Traceable provenance** from Figma sources to exports  
- ♿ **Accessibility compliance** via alt-text and contrast metrics  
- 🔗 **Integration** with STAC and the web UI’s design system  
- 🔒 **Reproducibility** via checksum verification and CI workflows  

The schema extends the base [Map Thumbnail Metadata Schema](../../../../../map/thumbnails/metadata/schema/README.md)  
to include UI/UX-specific attributes such as Figma source linkage, design variants, and accessibility metadata.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/wireframes/thumbnails/metadata/schema/
├── README.md                        # This file
├── wireframe_thumbnail.schema.json  # Schema for individual thumbnail records
└── index.schema.json                # Schema for aggregated metadata index
````

---

## 📘 `wireframe_thumbnail.schema.json`

**Purpose:** Defines validation rules for a single **map wireframe thumbnail metadata record**
describing one design variant (e.g., default, mobile, timeline overlay, darkmode).

### 🧩 Schema Outline

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Map Wireframe Thumbnail Metadata Schema",
  "type": "object",
  "required": ["id", "title", "thumbnail", "variant", "provenance"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9_\\-]+$",
      "description": "Unique identifier for the thumbnail record."
    },
    "title": { "type": "string", "description": "Human-readable name of the wireframe thumbnail." },
    "variant": {
      "type": "string",
      "enum": ["desktop_default", "mobile", "timeline_overlay", "darkmode"],
      "description": "UI layout or theme variation represented by this design."
    },
    "thumbnail": { "type": "string", "description": "Path to the thumbnail image (PNG/JPG)." },
    "description": { "type": "string", "description": "Short explanation of layout or design intent." },
    "source_figma": {
      "type": "string",
      "description": "Reference or URL to original Figma frame or design file."
    },
    "theme": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Visual or thematic tags (e.g., ['timeline', 'overlay', 'UI'])."
    },
    "license": {
      "type": "string",
      "default": "CC-BY-4.0",
      "description": "License governing the thumbnail image."
    },
    "checksum": {
      "type": "string",
      "pattern": "^sha256-[A-Fa-f0-9]+$",
      "description": "SHA-256 checksum for file integrity verification."
    },
    "accessibility": {
      "type": "object",
      "properties": {
        "contrast_ratio": { "type": "number", "minimum": 4.5 },
        "alt_text": { "type": "string" }
      },
      "description": "Accessibility metadata conforming to WCAG 2.1 AA."
    },
    "provenance": {
      "type": "object",
      "required": ["derived_from"],
      "properties": {
        "derived_from": { "type": "string", "description": "Source file or Figma export reference." },
        "created_with": { "type": "string", "description": "Tool or script used to generate the asset." },
        "commit": { "type": "string", "description": "Git commit reference for version traceability." }
      },
      "description": "Metadata capturing file lineage and reproducibility context."
    }
  }
}
```

---

## 📗 `index.schema.json`

**Purpose:** Defines the structure for aggregated metadata indexes,
enabling batch validation and automation in CI/CD workflows.

### 🧩 Schema Outline

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Map Wireframe Thumbnails Metadata Index",
  "type": "object",
  "required": ["version", "updated", "thumbnails"],
  "properties": {
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "updated": { "type": "string", "format": "date-time" },
    "thumbnails": {
      "type": "array",
      "items": { "$ref": "./wireframe_thumbnail.schema.json" }
    }
  }
}
```

---

## 🧮 Validation Workflow

Validation occurs via **GitHub Actions CI/CD** pipelines (`jsonschema.yml`, `stac-validate.yml`),
ensuring metadata consistency, integrity, and accessibility compliance.

| Step  | Description                            | Validation Target                        |
| ----- | -------------------------------------- | ---------------------------------------- |
| **1** | Schema validation                      | `wireframe_thumbnail.schema.json`        |
| **2** | File existence & checksum verification | All referenced thumbnails                |
| **3** | Metadata completeness check            | Required fields populated                |
| **4** | Accessibility verification             | Contrast ≥ 4.5 : 1 and alt text present  |
| **5** | STAC cross-reference validation        | Links between thumbnails and STAC layers |

### 🧰 Manual Validation Example

```bash
python -m jsonschema -i wireframe_thumbnails_metadata.json schema/wireframe_thumbnail.schema.json
```

---

## 🧠 Integration with KFM Systems

| Component                       | Purpose                                                     | Linked Standard                             |
| ------------------------------- | ----------------------------------------------------------- | ------------------------------------------- |
| **STAC Catalog**                | Links design previews to spatial data layers.               | [STAC 1.0.0](https://stacspec.org)          |
| **Web UI (React + MapLibreGL)** | Displays wireframe thumbnails as UI mockup previews.        | WCAG 2.1 AA                                 |
| **Figma Exports**               | Provides authoritative design source and version reference. | [Figma Design System](../../../../../../..) |
| **CI/CD Workflows**             | Automates schema validation and checksum audits.            | MCP + JSON Schema Draft 2020-12             |

---

## 🧾 Provenance & MCP Compliance

| Attribute           | Description                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| **Generated By**    | `scripts/generate_thumbnail_schema_docs.py`                               |
| **Validated In CI** | `stac-validate.yml`, `jsonschema.yml`                                     |
| **Schema Draft**    | [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema) |
| **License**         | [CC-BY 4.0](../../../../../../../../LICENSE)                              |
| **MCP Stage**       | Documented → Validated → Published                                        |

---

## 📚 Related References

* [🗺 Map Wireframe Thumbnails Metadata](../README.md)
* [🧩 Map Thumbnails Metadata Schema](../../../../../map/thumbnails/metadata/schema/README.md)
* [🧱 Kansas Frontier Matrix Web UI Architecture](../../../../../../../../architecture/web_ui_architecture_review.md)
* [🌐 STAC Catalog](../../../../../../../../data/stac/catalog.json)
* [♿ Accessibility Standards](../../../../../../../design/reviews/accessibility/README.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Validation · Provenance · Accessibility · Interoperability**

</div>
