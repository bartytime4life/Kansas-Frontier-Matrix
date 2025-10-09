<div align="center">

# 🕰️ Kansas Frontier Matrix — Timeline Thumbnails  
`docs/design/mockups/timeline/thumbnails/`

**Purpose:** Provide and manage **thumbnail previews** of the timeline design states  
(default, condensed, mobile, overlay) used in documentation, mockups, and automated gallery  
displays for the Kansas Frontier Matrix (KFM).

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory stores **thumbnail image assets** derived from exported timeline wireframes  
(`../wireframes/exports/`). These smaller previews are optimized for quick display within documentation,  
metadata indexes, and automated UI galleries in the KFM design catalog.

Each thumbnail visually represents a **timeline variant** —  
**Default**, **Condensed**, **Mobile**, or **Map Overlay** — ensuring consistent visual language and accessibility compliance.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/timeline/thumbnails/
├── README.md                              # This file
├── timeline_default_thumb.png              # Default desktop timeline layout
├── timeline_condensed_thumb.png            # Condensed timeline for dense datasets
├── timeline_mobile_thumb.png               # Mobile-optimized vertical timeline
├── timeline_overlay_map_thumb.png          # Overlay version with map integration
└── metadata/                               # JSON metadata for thumbnails
    └── timeline_thumbnails_metadata.json
````

---

## 🧱 Thumbnail Standards

| Property              | Standard                       | Description                              |
| --------------------- | ------------------------------ | ---------------------------------------- |
| **Format**            | PNG (preferred)                | Transparent or neutral background        |
| **Resolution**        | 1280×720 px                    | Optimized for web and documentation      |
| **Aspect Ratio**      | 16 : 9                         | Consistent visual proportions            |
| **DPI**               | 144                            | Retina-quality rendering                 |
| **Color Space**       | sRGB                           | Web-consistent color fidelity            |
| **Background**        | `#F5F5F5`                      | Consistent light-neutral background      |
| **Naming Convention** | `timeline_{variant}_thumb.png` | Lowercase, underscores only              |
| **Accessibility**     | ≥ 4.5 : 1 contrast             | WCAG 2.1 AA-compliant text and icons     |
| **Metadata**          | JSON index in `metadata/`      | Machine-readable registry for validation |

---

## 🧩 Example Metadata Record

Each thumbnail is documented within
`metadata/timeline_thumbnails_metadata.json`, capturing accessibility, provenance, and integrity attributes.

```json
{
  "id": "timeline_overlay_map_thumb",
  "title": "Timeline + Map Overlay Thumbnail",
  "file": "timeline_overlay_map_thumb.png",
  "description": "Thumbnail preview showing synchronized timeline overlay above map viewer in Kansas Frontier Matrix.",
  "variant": "overlay_map",
  "theme": ["timeline", "map_sync", "overlay"],
  "creator": "KFM UX/UI Design Team",
  "license": "CC-BY-4.0",
  "checksum": "sha256-df43f6b89ea9ad24e2a3b51b8bc9f8b2...",
  "provenance": {
    "derived_from": "../wireframes/exports/timeline_overlay_map.png",
    "created_with": "scripts/generate_thumbnails.py",
    "commit": "{{ GIT_COMMIT }}"
  },
  "accessibility": {
    "contrast_ratio": 4.7,
    "alt_text": "Timeline overlay above map with labeled intervals and play controls."
  }
}
```

---

## 🧮 Validation Workflow

Thumbnail metadata and assets are continuously validated in CI/CD
(`jsonschema.yml` + `stac-validate.yml`) to ensure reproducibility and integrity.

### ✅ Automated Checks

* Schema compliance (`timeline_thumbnail.schema.json`)
* File existence verification (`*.png`)
* SHA-256 checksum validation
* Provenance & license completeness
* Accessibility compliance (contrast ≥ 4.5 : 1 and descriptive alt text)

### 🧰 Manual Validation Example

```bash
python -m jsonschema -i metadata/timeline_thumbnails_metadata.json schema/timeline_thumbnail.schema.json
```

---

## ♿ Accessibility Review

All thumbnails must meet WCAG 2.1 AA standards, documented in metadata.

| Requirement             | Standard                    | Verification                   |
| ----------------------- | --------------------------- | ------------------------------ |
| **Contrast Ratio**      | ≥ 4.5 : 1                   | Verified via Figma or QA audit |
| **Alt Text**            | Required                    | Recorded in metadata JSON      |
| **Color Safety**        | No hue-only differentiation | Manual review                  |
| **Theme Compatibility** | Light & dark documentation  | Dual-preview verification      |

Accessibility audits ensure thumbnails remain legible across color modes and responsive layouts.

---

## 🧾 Provenance & Integrity

| Attribute             | Description                                              |
| --------------------- | -------------------------------------------------------- |
| **Design Source**     | `timeline_wireframes_v1.fig` (Figma master)              |
| **Generated By**      | `scripts/generate_thumbnails.py`                         |
| **Checksum Tracking** | Recorded in `metadata/timeline_thumbnails_metadata.json` |
| **Validated In CI**   | `jsonschema.yml`, `stac-validate.yml`                    |
| **License**           | [CC-BY 4.0](../../../../../../LICENSE)                   |
| **MCP Compliance**    | Documented → Validated → Versioned → Published           |

---

## 🧠 Usage in Documentation

These thumbnails appear throughout the KFM documentation suite and the MCP portal gallery
as lightweight visual cues for timeline design states.

| Preview                                             | Description                                 |
| --------------------------------------------------- | ------------------------------------------- |
| ![Default Timeline](timeline_default_thumb.png)     | Standard desktop timeline layout            |
| ![Overlay Timeline](timeline_overlay_map_thumb.png) | Overlay timeline with spatial-temporal sync |

They are referenced in both **README previews** and **metadata-linked auto-indexes** for faster navigation.

---

## 📚 Related References

* [Timeline Wireframes (Main)](../wireframes/README.md)
* [Timeline Wireframe Metadata](../wireframes/metadata/README.md)
* [Panels Thumbnails](../../panels/thumbnails/README.md)
* [Map Thumbnails Metadata](../../map/thumbnails/metadata/README.md)
* [Kansas Frontier Matrix Web UI Architecture](../../../../../../architecture/web_ui_architecture_review.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Time · Terrain · History · Knowledge Graphs**

</div>
