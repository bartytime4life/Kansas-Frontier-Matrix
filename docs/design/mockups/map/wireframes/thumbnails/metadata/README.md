<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Wireframe Thumbnail Metadata  
`docs/design/mockups/map/wireframes/thumbnails/metadata/`

**Purpose:** Define, validate, and document structured metadata for all **map wireframe thumbnails**  
used across Kansas Frontier Matrix (KFM) documentation, web mockups, and UI layer previews.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../..)  
[![STAC Validate](https://img.shields.io/badge/STAC-validate-blue)](../../../../../../../.github/workflows/stac-validate.yml)  
[![JSON Schema](https://img.shields.io/badge/Schema-JSON%20Validated-orange)](https://json-schema.org)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory stores **metadata records** describing every map wireframe thumbnail located under  
`docs/design/mockups/map/wireframes/thumbnails/`.  

Each record documents:
- 🧩 **Design purpose & layout variation** (desktop, mobile, overlay, dark mode).  
- 🧾 **Provenance** (Figma frame, export script, and Git commit).  
- 🗺️ **Spatial linkage** (optional STAC or layer metadata reference).  
- ♿ **Accessibility audit** (contrast, alt text).  
- 🔒 **Checksum verification** for reproducibility.  

Together, these metadata files ensure every visual artifact within the design system is **traceable, versioned, and machine-readable** — following Master Coder Protocol (MCP) documentation-first principles.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/wireframes/thumbnails/metadata/
├── README.md                             # This documentation file
├── wireframe_thumbnails_metadata.json    # Aggregated metadata index
└── schema/                               # Validation schemas
    ├── wireframe_thumbnail.schema.json
    └── index.schema.json
````

---

## 🧱 Metadata Structure

Each entry represents a single thumbnail asset, referencing its Figma origin, visual theme, and accessibility metrics.

### Example Record

```json
{
  "id": "map_wireframe_timeline_overlay",
  "title": "Map + Timeline Overlay Wireframe",
  "thumbnail": "../map_timeline_overlay_thumb.png",
  "description": "Wireframe showing synchronized timeline overlay and map layout for the KFM web UI.",
  "variant": "timeline_overlay",
  "spatial_extent": [-102.0, 37.0, -94.6, 40.0],
  "theme": ["ui", "timeline", "overlay"],
  "creator": "KFM UX/UI Design Team",
  "license": "CC-BY-4.0",
  "source_figma": "figma/map_wireframes_v1.fig",
  "checksum": "sha256-abc123def456...",
  "provenance": {
    "derived_from": "docs/design/mockups/map/wireframes/map_wireframes_v1.fig",
    "created_with": "scripts/generate_thumbnails.py",
    "commit": "{{ GIT_COMMIT }}"
  },
  "accessibility": {
    "contrast_ratio": 4.8,
    "alt_text": "Preview of map with timeline overlay showing 1850–1950 range."
  }
}
```

---

## 🧩 Field Reference

| Field              | Type   | Description                                                              |
| ------------------ | ------ | ------------------------------------------------------------------------ |
| **id**             | string | Unique identifier for the thumbnail (kebab-case).                        |
| **title**          | string | Human-readable title for the wireframe preview.                          |
| **thumbnail**      | string | Relative path to the image asset.                                        |
| **description**    | string | Concise overview of layout and context.                                  |
| **variant**        | string | Design category (e.g., `desktop_default`, `mobile`, `timeline_overlay`). |
| **spatial_extent** | array  | Optional [west, south, east, north] bounding box for map context.        |
| **theme**          | array  | Descriptive tags linking to UI or data domain.                           |
| **creator**        | string | Author or team attribution.                                              |
| **license**        | string | Usage license (`CC-BY-4.0` by default).                                  |
| **source_figma**   | string | Source design file (Figma frame or URL).                                 |
| **checksum**       | string | SHA-256 checksum verifying image integrity.                              |
| **provenance**     | object | Metadata capturing lineage (derived_from, created_with, commit).         |
| **accessibility**  | object | Accessibility data including contrast ratio and alt text.                |

---

## 🧮 Validation Workflow

All metadata is validated through the **GitHub Actions CI/CD pipelines** (`stac-validate.yml` + `jsonschema.yml`)
to guarantee structural integrity, accessibility compliance, and reproducibility.

| Validation Step          | Description                                                |
| ------------------------ | ---------------------------------------------------------- |
| **Schema Validation**    | Ensures conformity with `wireframe_thumbnail.schema.json`. |
| **File Existence Check** | Verifies all referenced thumbnails exist in `../`.         |
| **Checksum Validation**  | Confirms SHA-256 checksums match source images.            |
| **Accessibility Audit**  | Requires contrast ≥ 4.5 and alt text per WCAG 2.1 AA.      |
| **STAC Cross-Linking**   | Validates connections to STAC Items (if declared).         |

### 🧰 Manual Validation Example

```bash
python -m jsonschema -i wireframe_thumbnails_metadata.json schema/wireframe_thumbnail.schema.json
```

---

## ♿ Accessibility & Visual Standards

Each thumbnail record must include **accessibility metadata** validated in both **light** and **dark modes**.

| Accessibility Metric | Requirement | Description                               |
| -------------------- | ----------- | ----------------------------------------- |
| **Contrast Ratio**   | ≥ 4.5 : 1   | Measured for text overlays and icons.     |
| **Alt Text**         | Required    | Descriptive for screen reader support.    |
| **Color Mode Check** | Dual        | Tested against both documentation themes. |

Accessibility tests are automated in CI and manually reviewed by the design QA team.

---

## 🧾 Provenance & Integrity

| Attribute           | Description                                                |
| ------------------- | ---------------------------------------------------------- |
| **Generated By**    | `scripts/generate_thumbnails.py`                           |
| **Derived From**    | `docs/design/mockups/map/wireframes/map_wireframes_v1.fig` |
| **Checksums**       | SHA-256 sidecar files generated and stored in `metadata/`  |
| **Reviewed By**     | KFM Design QA (Pull Request process)                       |
| **Validated In CI** | `stac-validate.yml`, `jsonschema.yml`                      |
| **License**         | [CC-BY 4.0](../../../../../../../LICENSE)                  |
| **MCP Compliance**  | Documented → Built → Validated → Versioned                 |

---

## 🧠 Integration Notes

| Integration Target       | Description                                                     | Reference                                    |
| ------------------------ | --------------------------------------------------------------- | -------------------------------------------- |
| **Design Documentation** | Used in README previews throughout `/docs/design/mockups/map/`. | `thumbnails_index.json`                      |
| **Web UI (React)**       | Used as fallback static previews in Layer Browser.              | `web/src/components/layers/LayerPreview.tsx` |
| **Automation Script**    | Automatically updated by thumbnail generation script.           | `scripts/generate_thumbnails.py`             |
| **Accessibility QA**     | Validated for WCAG 2.1 AA compliance.                           | CI pipeline reports                          |

---

## 📚 Related References

* [🗺 Map Wireframes (Main)](../../README.md)
* [🧩 Map Wireframe Thumbnails](../README.md)
* [🧱 Kansas Frontier Matrix Web UI Architecture](../../../../../../../architecture/web_ui_architecture_review.md)
* [🌐 STAC Catalog](../../../../../../../data/stac/catalog.json)
* [♿ Accessibility Design Standards](../../../../../../design/reviews/accessibility/README.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Spatial Clarity · Accessibility Integrity · Provenance Transparency**

</div>
