<div align="center">

# 🖼️ Kansas Frontier Matrix — **Image Thumbnails**  
`web/public/assets/images/thumbnails/`

**Component Previews · Documentation Visuals · UI Snapshots**

[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-blue)](../../../../../docs/design/)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../../../docs/design/reviews/accessibility/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Image Thumbnails (web/public/assets/images/thumbnails/)"
version: "v1.0.0"
last_updated: "2025-10-14"
owners: ["@kfm-design", "@kfm-docs"]
tags: ["thumbnails","documentation","ui-previews","images","mcp"]
license: "MIT"
semantic_alignment:
  - WCAG 2.1 AA
  - W3C Web Image Formats (PNG/JPG)
  - MCP-DL v6.2 (Documentation Provenance)
---
````

---

## 🧭 Overview

The `web/public/assets/images/thumbnails/` directory contains **small-sized UI preview images**
used throughout the **Kansas Frontier Matrix documentation**, **component showcases**, and **design reviews**.
These thumbnails provide quick visual context for key components — enabling clear navigation across the documentation ecosystem.

Each image follows strict MCP-DL v6.2 documentation standards:

* ✅ Consistent aspect ratios (16:9)
* ✅ Accessible captions and alt text
* ✅ Optimized file size and compression
* ✅ Traceable provenance and checksum validation

> **Purpose:** Thumbnails make documentation more visual, approachable, and reproducible — bridging design and development clarity.

---

## 🧱 Directory Structure

```text
web/public/assets/images/thumbnails/
├── timeline-thumb.png        # Snapshot of TimelineView component
├── mapview-thumb.png         # Snapshot of MapView rendering Kansas overlays
├── aiassistant-thumb.png     # Chat interface preview for AI Assistant
├── layercontrols-thumb.png   # Example LayerControls and legend UI
└── README.md                 # This documentation file
```

---

## 🧩 Thumbnail Standards

| Attribute              | Specification                                   |
| :--------------------- | :---------------------------------------------- |
| **Aspect Ratio**       | 16:9 (preferred) or 4:3 for compact layouts     |
| **Dimensions**         | 640×360 px (desktop docs) / 320×180 px (mobile) |
| **File Format**        | PNG (lossless) or WebP (quality 90)             |
| **Color Mode**         | sRGB (no embedded profiles)                     |
| **Compression Target** | ≤ 150 KB per image                              |
| **Naming Convention**  | `{component-name}-thumb.{ext}`                  |

All thumbnails are generated directly from live KFM builds or approved mockups within the design system.

---

## 🎨 Design & Integration

| Thumbnail                 | Origin                                               | Usage                                         |
| :------------------------ | :--------------------------------------------------- | :-------------------------------------------- |
| `timeline-thumb.png`      | Screenshot of `TimelineView` rendering sample events | Docs/Architecture + Timeline component README |
| `mapview-thumb.png`       | MapLibre render showing historic map overlays        | MapView docs + homepage                       |
| `aiassistant-thumb.png`   | Chat session with citations and entity highlights    | AI Assistant documentation                    |
| `layercontrols-thumb.png` | Sidebar showing STAC-driven layers and legends       | LayerControls README                          |

Example inclusion in documentation:

```markdown
![TimelineView Thumbnail](../../../../../web/public/assets/images/thumbnails/timeline-thumb.png "TimelineView Component – temporal navigation interface")
```

---

## 🧮 Optimization Workflow

Thumbnails are generated and optimized via CI to ensure consistency and minimal size impact.

| Step     | Tool             | Function                                        |
| :------- | :--------------- | :---------------------------------------------- |
| Capture  | Puppeteer        | Auto-screenshot component previews during build |
| Resize   | Sharp            | Convert to standard 16:9 ratio                  |
| Compress | pngquant / cwebp | Optimize PNG/WebP size                          |
| Verify   | ImageMagick      | Validate dimensions and color profiles          |
| Checksum | SHA256           | Generate per-image hash for reproducibility     |

Each thumbnail includes a `.json` metadata file under `/meta/` for source tracking and version integrity.

---

## ♿ Accessibility

* **Alt Text:** Each thumbnail includes meaningful alt text describing the UI state.
* **Decorative Thumbnails:** Use `alt=""` for purely aesthetic documentation visuals.
* **Contrast Compliance:** Thumbnails must maintain 4.5:1 contrast ratio for embedded text/UI.
* **Scaling:** Responsive display at 1×–3× DPI; supports high-resolution displays.
* **Keyboard Context:** Focusable when used in interactive documentation interfaces.

Accessibility validation runs automatically using **axe-core** + **Lighthouse**.

---

## 🧾 Provenance & Metadata Example

```json
{
  "id": "timeline-thumb",
  "component": "TimelineView",
  "source": "Auto-screenshot from Storybook build",
  "generated_by": "CI pipeline (Puppeteer)",
  "created": "2025-10-14T12:00:00Z",
  "checksum": "sha256:7e2a9d9f...",
  "license": "MIT"
}
```

> Metadata files ensure each visual is traceable to the specific component state and build hash.

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                                |
| :------------------ | :------------------------------------------------------------ |
| Documentation-first | Each thumbnail embedded in docs & architecture overviews      |
| Reproducibility     | CI-generated assets tied to component build ID                |
| Provenance          | JSON metadata includes component name, author, checksum       |
| Accessibility       | WCAG 2.1 AA validated via CI                                  |
| Open Standards      | PNG/WebP formats + semantic alt text                          |
| Traceability        | Design-to-code link through MCP registry & Storybook snapshot |

---

## 🔗 Related Documentation

* **Public Images Overview** — `web/public/assets/images/README.md`
* **Component Documentation Index** — `web/src/components/README.md`
* **Design Mockups (UI Previews)** — `docs/design/mockups/previews/`
* **Accessibility Reviews** — `docs/design/reviews/accessibility/`

---

## 📜 License

All thumbnails are released under the **MIT License** and are regenerated in each major KFM release.
Third-party imagery within thumbnails (if any) is under compatible open licenses (CC0, CC-BY, or Public Domain).

© 2025 Kansas Frontier Matrix — created under **MCP-DL v6.2** for **reproducible**, **accessible**, and **traceable documentation assets**.

> *“A thumbnail is a glimpse — each captures Kansas’s evolving frontier of data, design, and discovery.”*

```
```
