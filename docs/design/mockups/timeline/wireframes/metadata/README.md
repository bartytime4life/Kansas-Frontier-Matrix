<div align="center">

# 🕰️ Kansas Frontier Matrix — Timeline Wireframe Metadata  
`docs/design/mockups/timeline/wireframes/metadata/`

**Purpose:** Define, validate, and link structured metadata for all **timeline wireframe exports**  
used in the Kansas Frontier Matrix (KFM) Web UI — ensuring consistent documentation,  
traceability, accessibility, and reproducibility.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../../../..)  
[![JSON Schema](https://img.shields.io/badge/Schema-Validated-orange)](https://json-schema.org)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains **metadata records** describing each exported timeline wireframe  
in `../exports/`. Each metadata entry captures the design’s **purpose**, **layout variant**,  
**accessibility metrics**, **provenance**, and **checksum integrity** — forming a reproducible record  
of how timeline UI concepts evolve across the KFM design system.

These metadata records feed into:

- 🧩 Design documentation (Markdown READMEs & gallery previews)  
- 🌐 MCP documentation index (JSON-LD + STAC integration)  
- 🧮 Continuous validation (CI/CD JSON Schema checks)  
- ♿ Accessibility audit tracking & compliance history  

---

## 🗂️ Directory Layout

```text
docs/design/mockups/timeline/wireframes/metadata/
├── README.md                         # This file
├── timeline_wireframes_metadata.json  # Index of all timeline wireframe metadata entries
└── schema/                            # JSON Schema definitions for validation
    ├── timeline_wireframe.schema.json
    └── index.schema.json
````

---

## 🧱 Metadata Structure

Each wireframe record documents what the timeline design represents,
how it was created, and its compliance attributes.
All records must validate against `schema/timeline_wireframe.schema.json`.

### 🧩 Example Record

```json
{
  "id": "timeline_overlay_map",
  "title": "Timeline + Map Overlay Layout",
  "thumbnail": "../exports/timeline_overlay_map.png",
  "description": "Wireframe showing the timeline overlaid on the map for synchronized spatial-temporal exploration.",
  "variant": "overlay_map",
  "theme": ["timeline", "map_sync", "overlay"],
  "creator": "KFM UX/UI Design Team",
  "license": "CC-BY-4.0",
  "source_figma": "figma/timeline_wireframes_v1.fig",
  "checksum": "sha256-6a2f13d7ef4c9823e9b476fc4b75d5ef...",
  "provenance": {
    "derived_from": "timeline_wireframes_v1.fig",
    "created_with": "Figma Export",
    "commit": "{{ GIT_COMMIT }}"
  },
  "accessibility": {
    "contrast_ratio": 4.8,
    "alt_text": "Overlay timeline wireframe displaying 1850–1950 period above Kansas map view."
  }
}
```

---

## 🧩 Field Reference

| Field             | Type   | Description                                                         |
| ----------------- | ------ | ------------------------------------------------------------------- |
| **id**            | string | Unique identifier (kebab-case).                                     |
| **title**         | string | Human-readable name of the wireframe.                               |
| **thumbnail**     | string | Relative path to exported image file.                               |
| **description**   | string | Concise summary of design purpose and function.                     |
| **variant**       | string | Layout type (e.g. `default`, `condensed`, `overlay_map`, `mobile`). |
| **theme**         | array  | Tags indicating design scope or use case.                           |
| **creator**       | string | Author or team responsible for the design.                          |
| **license**       | string | License identifier (default: `CC-BY-4.0`).                          |
| **source_figma**  | string | Path to original Figma design source.                               |
| **checksum**      | string | SHA-256 hash for export file integrity verification.                |
| **provenance**    | object | Metadata detailing creation, derivation, and Git commit linkage.    |
| **accessibility** | object | Accessibility attributes (contrast ratio, alt text).                |

---

## 🧮 Validation Workflow

All metadata entries are automatically validated via CI/CD pipelines
(`jsonschema.yml` and `stac-validate.yml`).

### ✅ Automated Checks

* Schema validation (`timeline_wireframe.schema.json`)
* File path verification for all exports (`../exports/*.png`)
* SHA-256 checksum verification
* Required field validation (title, description, provenance, license)
* Accessibility compliance (contrast ratio ≥ 4.5:1)

### 🧰 Manual Validation Example

```bash
python -m jsonschema -i timeline_wireframes_metadata.json schema/timeline_wireframe.schema.json
```

---

## ♿ Accessibility & Compliance

Accessibility attributes are **mandatory** for each wireframe metadata entry.

| Requirement        | Threshold                   | Validation                           |
| ------------------ | --------------------------- | ------------------------------------ |
| **Contrast Ratio** | ≥ 4.5 : 1                   | Verified in Figma export QA          |
| **Alt Text**       | Required                    | Present in metadata for every export |
| **Color Use**      | No hue-only differentiation | Manual design check                  |

Accessibility compliance is reviewed and logged during Figma QA.
Metadata captures all relevant attributes for audit transparency.

---

## 🧾 Provenance & Reproducibility

| Attribute          | Description                                      |
| ------------------ | ------------------------------------------------ |
| **Design Source**  | `timeline_wireframes_v1.fig` (Figma master file) |
| **Generated By**   | `scripts/generate_timeline_thumbnails.py`        |
| **Validated In**   | `jsonschema.yml`, `stac-validate.yml`            |
| **Checksums**      | Stored in `timeline_wireframes_metadata.json`    |
| **MCP Compliance** | Documented → Built → Validated → Versioned       |

---

## 🧭 Linked Standards

| Domain                  | Standard                                        |
| ----------------------- | ----------------------------------------------- |
| 🕰️ Temporal Semantics  | [W3C OWL-Time](https://www.w3.org/TR/owl-time/) |
| 📅 Historical Periods   | [PeriodO Gazetteer](https://perio.do)           |
| 🏺 Cultural Context     | [CIDOC CRM](https://www.cidoc-crm.org)          |
| 🗺️ Geospatial Metadata | [STAC 1.0.0](https://stacspec.org)              |

---

## 📚 Related References

* [Timeline Wireframes (Main)](../README.md)
* [Timeline Wireframe Exports](../exports/README.md)
* [Panels Wireframes](../../../panels/wireframes/README.md)
* [Map Wireframes](../../../map/wireframes/README.md)
* [Kansas Frontier Matrix Web UI Architecture](../../../../../architecture/web_ui_architecture_review.md)
* [Accessibility Standards](../../../../../design/reviews/accessibility/README.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Time · Terrain · History · Knowledge Graphs**

</div>
