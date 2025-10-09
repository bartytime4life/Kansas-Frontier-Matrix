<div align="center">

# 🗺️ Kansas Frontier Matrix — Map Wireframe Thumbnail Archive Metadata  
`docs/design/mockups/map/wireframes/thumbnails/archive/metadata/`

**Purpose:** Define and validate metadata for **archived map wireframe thumbnails** preserved for documentation  
continuity, reproducibility, and design history within the Kansas Frontier Matrix (KFM) project.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![Archive Integrity](https://img.shields.io/badge/Archive-Integrity-blue)](../../../../../../../../.github/workflows/stac-validate.yml)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains the **metadata records** describing archived map wireframe thumbnails stored in  
`docs/design/mockups/map/wireframes/thumbnails/archive/`.

Each metadata file records:
- 📘 **Historical design provenance** (Figma origin, export date, author, commit ID).  
- 🧩 **Layout variant** (concept, dark mode, mobile-first, experimental).  
- ♿ **Accessibility audit results** (contrast ratio, alt text).  
- 🔒 **Checksum validation** (SHA-256).  
- 🧾 **Status** flagging the asset as “archived” for traceability.  

These records provide machine-readable continuity for the KFM’s design evolution under the **Master Coder Protocol (MCP)**.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/map/wireframes/thumbnails/archive/metadata/
├── README.md                            # This documentation file
├── archive_thumbnails_metadata.json     # Index of all archived map thumbnail metadata
└── schema/                              # JSON Schema definitions for validation
    ├── archive_thumbnail.schema.json
    └── index.schema.json
````

---

## 🧱 Metadata Structure

Archived metadata follows the same structure as active thumbnail records but adds versioning and archival status fields.
All records are validated against `schema/archive_thumbnail.schema.json`.

### Example Record

```json
{
  "id": "map_concept_v0_thumb",
  "title": "Early Concept — Map Wireframe",
  "file": "map_concept_v0_thumb.png",
  "description": "Prototype wireframe exploring the earliest KFM map layout, predating STAC integration.",
  "variant": "concept_v0",
  "theme": ["map", "ui", "prototype"],
  "creator": "KFM Design Team",
  "license": "CC-BY-4.0",
  "source_figma": "figma/map_wireframes_v0.fig",
  "checksum": "sha256-7bd9f4e72ca8a2a6a6a8d04fa7bb2ef4...",
  "status": "archived",
  "provenance": {
    "derived_from": "docs/design/mockups/map/wireframes/map_wireframes_v0.fig",
    "created_with": "Figma Export",
    "commit": "{{ GIT_COMMIT }}"
  },
  "accessibility": {
    "contrast_ratio": 4.5,
    "alt_text": "Prototype wireframe showing Kansas topographic base map with toolbar and overlay controls."
  },
  "archived_on": "2024-06-12"
}
```

---

## 🧩 Field Reference

| Field             | Type   | Description                                                       |
| ----------------- | ------ | ----------------------------------------------------------------- |
| **id**            | string | Unique identifier for the archived thumbnail (kebab-case).        |
| **title**         | string | Descriptive title of the design variant.                          |
| **file**          | string | Path to archived image asset.                                     |
| **description**   | string | Short description of concept or revision purpose.                 |
| **variant**       | string | Type of archived design (`concept_v0`, `darkmode_concept`, etc.). |
| **theme**         | array  | Tags indicating function, theme, or design context.               |
| **creator**       | string | Design author or contributing team.                               |
| **source_figma**  | string | Figma source file reference.                                      |
| **license**       | string | Usage license (`CC-BY-4.0` default).                              |
| **checksum**      | string | SHA-256 hash verifying file integrity.                            |
| **status**        | string | Archive state (`archived`, `deprecated`, or `superseded`).        |
| **provenance**    | object | Metadata describing derivation, commit, and creation tool.        |
| **accessibility** | object | Accessibility metrics and descriptive alt text.                   |
| **archived_on**   | string | Date archived (ISO 8601).                                         |

---

## 🧮 Validation Workflow

All archive metadata entries are validated through **GitHub Actions**
(`jsonschema.yml` + `stac-validate.yml`) to ensure historical reproducibility.

| Step  | Validation            | Target                                       |
| ----- | --------------------- | -------------------------------------------- |
| **1** | Schema compliance     | `schema/archive_thumbnail.schema.json`       |
| **2** | File existence        | Verify archived images exist in `../`        |
| **3** | Checksum verification | SHA-256 match to recorded metadata           |
| **4** | Accessibility audit   | Contrast ratio ≥ 4.5 : 1; alt text present   |
| **5** | Provenance lineage    | Confirms Figma source and Git commit linkage |
| **6** | Archive tagging       | Ensures `status: archived` is declared       |

### 🧰 Manual Validation Example

```bash
python -m jsonschema -i archive_thumbnails_metadata.json schema/archive_thumbnail.schema.json
```

---

## ♿ Accessibility Review

Even archived designs maintain accessibility metadata and are audited periodically for compliance.

| Metric                            | Threshold       | Description                                             |
| --------------------------------- | --------------- | ------------------------------------------------------- |
| **Contrast Ratio**                | ≥ 4.5 : 1       | Verified visually and with plugin audits.               |
| **Alt Text**                      | Required        | Provides screen-reader context for documentation reuse. |
| **Dark/Light Mode Compatibility** | Dual validation | Ensures readability in both visual themes.              |

---

## 🧾 Provenance & Preservation

| Attribute               | Description                                             |
| ----------------------- | ------------------------------------------------------- |
| **Generated By**        | `scripts/archive_thumbnails_metadata.py`                |
| **Derived From**        | `figma/map_wireframes_v0.fig`                           |
| **Validated In CI**     | `jsonschema.yml`, `stac-validate.yml`                   |
| **Checksum Tracking**   | Stored alongside `archive_thumbnails_metadata.json`     |
| **License**             | [CC-BY 4.0](../../../../../../../../LICENSE)            |
| **Preservation Policy** | Immutable record retained for historical documentation. |

Archived entries remain version-locked and included in validation pipelines
to maintain full provenance under MCP documentation standards.

---

## 📚 Related References

* [🗺 Map Wireframe Thumbnail Archive](../README.md)
* [🧩 Map Wireframe Thumbnails Metadata](../../metadata/README.md)
* [🧱 Kansas Frontier Matrix Web UI Architecture](../../../../../../../../architecture/web_ui_architecture_review.md)
* [🌐 STAC Catalog](../../../../../../../../data/stac/catalog.json)
* [♿ Accessibility Standards](../../../../../../../design/reviews/accessibility/README.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Archival Fidelity · Accessibility Continuity · Provenance Integrity**

</div>
