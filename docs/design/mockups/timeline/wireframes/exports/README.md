<div align="center">

# 🕰️ Kansas Frontier Matrix — Timeline Wireframe Exports  
`docs/design/mockups/timeline/wireframes/exports/`

**Purpose:** Store and version exported **wireframe images** of the Timeline module’s design variants  
for documentation, testing, and accessibility review.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../..)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../../..)  
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../../../../..)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../../LICENSE)

</div>

---

## 🧭 Overview

This directory contains **Figma-exported PNG wireframes** representing the design layouts of  
the Kansas Frontier Matrix (KFM) **Timeline interface**.  

These exports serve as **canonical visual references** for developers and designers implementing  
the Timeline components — ensuring synchronization between **map**, **timeline**, and **detail panels**  
in the KFM web application.

Each file represents a distinct **state or responsive variant** of the timeline (desktop, condensed, overlay, or mobile).  
Exports are automatically validated in CI for **integrity**, **naming**, and **accessibility compliance**.

---

## 🗂️ Directory Layout

```text
docs/design/mockups/timeline/wireframes/exports/
├── README.md                      # This file
├── timeline_default.png            # Standard desktop layout
├── timeline_condensed.png          # Compact scrollable version
├── timeline_mobile.png             # Vertical mobile timeline
└── timeline_overlay_map.png        # Overlay variant with map integration
````

---

## 🧱 Export Standards

| Property              | Standard                                      | Description                                 |
| --------------------- | --------------------------------------------- | ------------------------------------------- |
| **Format**            | PNG                                           | Transparent or neutral background preferred |
| **Resolution**        | 1920×1080 px (desktop) / 1280×720 px (mobile) | High-resolution exports                     |
| **Aspect Ratio**      | 16 : 9                                        | Consistent visual proportions               |
| **DPI**               | 144                                           | Retina-ready quality for docs and galleries |
| **Color Space**       | sRGB                                          | Web-standard rendering consistency          |
| **Background**        | `#F5F5F5` or transparent                      | Readable in light/dark modes                |
| **Naming Convention** | `timeline_{variant}.png`                      | Lowercase, underscores only                 |
| **Accessibility**     | ≥ 4.5 : 1 contrast ratio                      | WCAG 2.1 AA compliance                      |

---

## 🧩 Design Variants

| Filename                     | Layout Description                                                  | Primary Use                                             |
| ---------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------- |
| **timeline_default.png**     | Standard desktop timeline showing event bands, ticks, and controls. | Reference for main web layout implementation.           |
| **timeline_condensed.png**   | Compact horizontal timeline with reduced spacing.                   | Used for dense datasets or mid-sized screens.           |
| **timeline_mobile.png**      | Vertical, scrollable timeline for mobile (< 768 px).                | Optimized for phones and narrow viewports.              |
| **timeline_overlay_map.png** | Overlay version combining timeline and map regions.                 | Demonstrates synchronized spatial-temporal interaction. |

---

## 🧮 Validation Workflow

All exports undergo validation through CI/CD pipelines
(`jsonschema.yml` + `stac-validate.yml`).

### ✅ Automated Checks

* File presence and naming consistency
* SHA-256 checksum validation against metadata
* Metadata linkage in `../metadata/timeline_wireframes_metadata.json`
* Accessibility verification (contrast ≥ 4.5 : 1 and alt-text present)

### 🧰 Manual Checksum Example

```bash
shasum -a 256 *.png > checksums.sha256
```

---

## ♿ Accessibility Verification

Every exported wireframe must include **accessibility metadata** within its corresponding JSON entry.

| Requirement        | Standard                    | Validation                                                |
| ------------------ | --------------------------- | --------------------------------------------------------- |
| **Contrast Ratio** | ≥ 4.5 : 1                   | Measured via Figma or design QA                           |
| **Alt Text**       | Required                    | Stored in `../metadata/timeline_wireframes_metadata.json` |
| **Color Safety**   | No hue-only differentiation | Manual review per WCAG 2.1 AA                             |

Accessibility audits are reviewed in design QA and recorded in the metadata index.

---

## 🧾 Provenance & Integrity

| Attribute             | Detail                                     |
| --------------------- | ------------------------------------------ |
| **Design Source**     | `timeline_wireframes_v1.fig`               |
| **Generated By**      | KFM Design Team · Figma Export Workflow    |
| **Checksum Tracking** | SHA-256 hashes logged in metadata          |
| **Validated In CI**   | `jsonschema.yml`, `stac-validate.yml`      |
| **License**           | [CC-BY 4.0](../../../../../../LICENSE)     |
| **MCP Compliance**    | Documented → Built → Validated → Versioned |

---

## 🧠 Usage in Documentation

These exports appear in **design READMEs** and **MCP portal galleries**
as official timeline design references.

| Preview                                       | Description                          |
| --------------------------------------------- | ------------------------------------ |
| ![Timeline Default](timeline_default.png)     | Standard timeline layout (desktop)   |
| ![Timeline Overlay](timeline_overlay_map.png) | Timeline + Map overlay demonstration |

Each image is referenced in higher-level design guides and auto-indexed in the MCP design catalog.

---

## 📚 Related References

* [Timeline Wireframes (Main)](../README.md)
* [Timeline Wireframes Metadata](../metadata/README.md)
* [Panels Wireframes](../../../panels/wireframes/README.md)
* [Map Wireframes](../../../map/wireframes/README.md)
* [Kansas Frontier Matrix Web UI Architecture](../../../../../../architecture/web_ui_architecture_review.md)

---

<div align="center">

### Kansas Frontier Matrix — Documentation-First Design

**Time · Terrain · History · Knowledge Graphs**

</div>
