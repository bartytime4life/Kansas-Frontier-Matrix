<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Wireframe Thumbnail Archive  
`docs/design/mockups/map/wireframes/thumbnails/archive/`

**Purpose:** Preserve, document, and reference **legacy map wireframe thumbnails**  
from earlier Kansas Frontier Matrix (KFM) design iterations for research, validation, and provenance tracking.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../..)  
[![Archive Validated](https://img.shields.io/badge/Archive-Integrity-blue)](../../../../../../../.github/workflows/stac-validate.yml)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains **archived map wireframe thumbnails** representing earlier concept designs, experimental layouts,  
and deprecated interface versions for the **Kansas Frontier Matrix (KFM)** web UI.  

Archived thumbnails serve to:
- 🧩 Preserve **design evolution history** across MCP documentation cycles.  
- 🧾 Support **comparative validation** between design iterations.  
- 🧠 Provide a **knowledge reference** for UI/UX decisions and architectural refinements.  
- ♻️ Ensure **reproducibility and lineage** through recorded checksums and provenance metadata.  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/wireframes/thumbnails/archive/
├── README.md                          # This documentation file
├── map_concept_v0_thumb.png            # Early prototype of Map Viewer interface
├── map_darkmode_thumb.png              # Concept design for dark theme visualization
└── metadata/                           # Metadata and validation records for archived files
    └── archive_thumbnails_metadata.json
````

---

## 🧱 Archive Standards

| Property              | Standard              | Description                                        |                                    |
| --------------------- | --------------------- | -------------------------------------------------- | ---------------------------------- |
| **Format**            | PNG (preferred) / JPG | Preserves full visual fidelity of early wireframes |                                    |
| **Resolution**        | 1280×720 px           | Standardized aspect ratio (16 : 9)                 |                                    |
| **Color Space**       | sRGB                  | Consistent rendering for comparison                |                                    |
| **Naming Convention** | `map_{concept         | variant}_v{n}_thumb.png`                           | Lowercase with version identifiers |
| **Accessibility**     | ≥ 4.5 : 1 contrast    | Verified per WCAG 2.1 AA                           |                                    |
| **License**           | CC-BY-4.0             | Attribution required for reuse                     |                                    |

All archived files are immutable and maintained solely for **historical documentation** and reproducibility.

---

## 🧩 Metadata & Provenance

Each file is recorded within `metadata/archive_thumbnails_metadata.json`,
capturing its provenance, purpose, and validation state.

### Example Record

```json
{
  "id": "map_darkmode_thumb",
  "title": "Dark Mode Concept — KFM Map Wireframe",
  "file": "map_darkmode_thumb.png",
  "description": "Early dark mode concept wireframe showcasing alternative color palettes and map styling.",
  "variant": "darkmode_concept",
  "theme": ["map", "ui", "concept", "darkmode"],
  "created": "2024-06-12",
  "creator": "KFM Design Team",
  "source_figma": "figma/map_wireframes_v0.fig",
  "checksum": "sha256-b78c9f23ad7e90e5f89c63d2e99fe11f...",
  "provenance": {
    "derived_from": "docs/design/mockups/map/wireframes/map_wireframes_v0.fig",
    "created_with": "Figma Export",
    "commit": "{{ GIT_COMMIT }}"
  },
  "accessibility": {
    "contrast_ratio": 4.6,
    "alt_text": "Early dark mode concept showing Kansas map with nighttime color palette."
  },
  "status": "archived"
}
```

---

## 🧮 Validation Workflow

All archived thumbnails remain part of the validation process to ensure referential consistency across versions.

| Step  | Validation                  | Target                                      |
| ----- | --------------------------- | ------------------------------------------- |
| **1** | JSON Schema validation      | `metadata/archive_thumbnails_metadata.json` |
| **2** | File existence verification | Archived thumbnails                         |
| **3** | SHA-256 checksum match      | Image integrity confirmation                |
| **4** | Accessibility audit         | WCAG 2.1 AA standards                       |
| **5** | Provenance lineage check    | Figma → Commit → Archive linkage            |

### Manual Check

```bash
python -m jsonschema -i metadata/archive_thumbnails_metadata.json schema/wireframe_thumbnail.schema.json
```

---

## ♿ Accessibility & Compliance

Even though these assets are archived, they are subject to ongoing accessibility validation for parity with the current design system.

| Check                          | Standard  | Description                                  |
| ------------------------------ | --------- | -------------------------------------------- |
| **Contrast Ratio**             | ≥ 4.5 : 1 | Verified at export time                      |
| **Alt Text**                   | Required  | Present in metadata for every thumbnail      |
| **ARIA Compliance**            | Optional  | Recommended if used in documentation         |
| **Dark/Light Mode Visibility** | Verified  | Both color modes tested during design review |

---

## 🧾 Preservation Policy

* 🔒 **Immutable Storage:** Archived assets are version-locked and never overwritten.
* 📜 **Retrospective Tracking:** Each archived asset is mapped to its originating commit and documented in changelogs.
* 🗃 **Metadata Integrity:** Checksums and schema compliance validated semi-annually.
* 🧭 **Historical Context:** All archived files remain referenced in MCP provenance chains for continuity.

---

## 📚 Related References

* [🗺 Map Wireframe Thumbnails (Current)](../README.md)
* [🧩 Map Wireframe Thumbnail Metadata](../metadata/README.md)
* [🧱 Web UI Architecture](../../../../../../../architecture/web_ui_architecture_review.md)
* [🌐 STAC Catalog](../../../../../../../data/stac/catalog.json)
* [♿ Accessibility Standards](../../../../../../design/reviews/accessibility/README.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Archival Integrity · Accessibility · Provenance Preservation**

</div>
