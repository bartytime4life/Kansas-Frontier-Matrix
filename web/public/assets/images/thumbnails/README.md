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

## 🧭 Overview

`web/public/assets/images/thumbnails/` contains **UI preview images** auto-generated from live KFM builds and design mockups.  
They serve as **visual anchors** across component READMEs, docs, and design reviews—helping readers instantly identify interfaces.

Each thumbnail adheres to **MCP-DL v6.2** reproducibility and documentation standards:

- ✅ Fixed aspect ratio (16:9)  
- ✅ Accessible captions/alt text  
- ✅ Optimized file size (<150 KB)  
- ✅ Traceable JSON metadata and SHA-256 checksum  

> *Thumbnails make documentation navigable, visual, and version-traceable.*

---

## 🧱 Directory Structure

```text
web/public/assets/images/thumbnails/
├── timeline-thumb.png        # TimelineView component preview
├── mapview-thumb.png         # MapView with historical overlays
├── aiassistant-thumb.png     # AI Assistant chat snapshot
├── layercontrols-thumb.png   # Sidebar + STAC legend controls
└── README.md
```

---

## 🧩 Thumbnail Specifications

| Attribute          | Value / Constraint                             |
| :----------------- | :--------------------------------------------- |
| **Aspect Ratio**   | 16:9 preferred (4:3 fallback)                  |
| **Dimensions**     | 640×360 px (desktop) · 320×180 px (mobile)     |
| **Format**         | PNG (lossless) / WebP (quality 90)             |
| **Color Space**    | sRGB (no embedded ICC profiles)                |
| **File Size**      | ≤ 150 KB                                       |
| **Naming Pattern** | `{component-name}-thumb.{ext}`                 |

---

## 🎨 Origin & Integration

| Thumbnail              | Origin                                        | Usage                                    |
| :--------------------- | :-------------------------------------------- | :--------------------------------------- |
| `timeline-thumb.png`   | Screenshot of **TimelineView** mock data      | Architecture + component README          |
| `mapview-thumb.png`    | Live MapLibre render of Kansas map overlays   | MapView docs + site index                |
| `aiassistant-thumb.png`| Conversation with citations & highlights      | AI Assistant docs                        |
| `layercontrols-thumb.png`| STAC layer UI + legend panel               | LayerControls documentation              |

**Markdown inclusion example:**
```markdown
![TimelineView Thumbnail](../../../../../web/public/assets/images/thumbnails/timeline-thumb.png "TimelineView – Temporal Navigation Interface")
```

---

## 🧮 CI Thumbnail Workflow

| Step        | Tool / Action            | Description                                 |
| :-----------| :------------------------| :------------------------------------------ |
| **Capture** | Puppeteer / Playwright   | Auto-screenshots Storybook or live builds   |
| **Resize**  | Sharp                    | Constrain to 16:9 ratio and target sizes    |
| **Compress**| pngquant / cwebp         | Optimize without perceptible loss           |
| **Verify**  | ImageMagick              | Check color mode, dimensions, headers       |
| **Checksum**| SHA-256                  | Produce integrity hash for each image       |

Each file gains a companion `/meta/*.json` metadata record storing source, component, and build info.

---

## ♿ Accessibility Standards

- **Alt Text:** succinct, descriptive (e.g., `"Timeline panel with 1850–1900 events"`).  
- **Decorative Images:** `alt=""` / `role="presentation"` if purely ornamental.  
- **Contrast:** Verified ≥ 4.5 : 1 for any embedded UI.  
- **Scalability:** Retina-ready; responsive display 1×–3× DPI.  
- **Keyboard Context:** Focusable when used in interactive galleries.  

Accessibility testing automated in CI via **axe-core** + **Lighthouse**.

---

## 🧾 Metadata Example

```json
{
  "id": "mapview-thumb",
  "component": "MapView",
  "source": "Auto-screenshot from Storybook",
  "build_hash": "commit:4c5e92b",
  "generated_at": "2025-10-17T14:32:00Z",
  "checksum": "sha256:edc0b1f...",
  "license": "MIT"
}
```

> Metadata binds each image to a component, build, and checksum for complete traceability.

---

## 🧪 Validation & Reporting

CI ensures:
- Dimensions & ratio compliance  
- Max size < 150 KB  
- Valid MIME type (image/png | image/webp)  
- Presence of JSON metadata + matching checksum  
- a11y metadata (alt text present)  

Validation logs stored in `ci/reports/thumbnails/`.

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                         |
| :------------------ | :---------------------------------------------------- |
| Documentation-first | Embedded thumbnails in component READMEs              |
| Reproducibility     | CI auto-generation tied to component build hash       |
| Provenance          | JSON metadata includes component, author, checksum    |
| Accessibility       | WCAG 2.1 AA tested automatically                      |
| Open Standards      | PNG / WebP formats + semantic alt text                |
| Auditability        | Checksum manifests & CI reports archived              |

---

## 🔗 Related Documentation

- **Public Images** — `web/public/assets/images/README.md`  
- **Components Index** — `web/src/components/README.md`  
- **Design Mockups** — `docs/design/mockups/previews/`  
- **Accessibility Reviews** — `docs/design/reviews/accessibility/`

---

## 🧾 Versioning & Metadata

| Field | Value |
| :---- | :---- |
| **Version** | `v1.1.0` |
| **Codename** | *CI-Generated Documentation Preview Upgrade* |
| **Last Updated** | 2025-10-17 |
| **Maintainers** | @kfm-design · @kfm-docs |
| **License** | MIT (custom) |
| **Alignment** | WCAG 2.1 AA · PNG/WebP · MCP-DL v6.2 |
| **Maturity** | Stable / Production |

---

## 📜 License

All thumbnails © 2025 Kansas Frontier Matrix, released under **MIT License**.  
Generated and maintained under **MCP-DL v6.2** for reproducible, accessible documentation assets.

> *“A thumbnail is a window into the interface — a visual handshake between design and documentation.”*
