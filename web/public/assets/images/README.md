<div align="center">

# 🖼️ Kansas Frontier Matrix — **Public Images**  
`web/public/assets/images/`

**Static Illustrations · Backgrounds · Thumbnails**

[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-blue)](../../../../docs/design/)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../../docs/design/reviews/accessibility/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Public Images (web/public/assets/images/)"
version: "v1.5.0"
last_updated: "2025-10-14"
owners: ["@kfm-design", "@kfm-web"]
tags: ["images","backgrounds","illustrations","branding","accessibility","mcp"]
license: "MIT"
semantic_alignment:
  - WCAG 2.1 AA
  - W3C Web Image Formats (PNG/JPG/WebP)
  - MCP-DL v6.2 (Design Provenance)
---
````

---

## 🧭 Overview

The `web/public/assets/images/` directory houses **raster-based images and illustrations** that power the Kansas Frontier Matrix (KFM) web experience.
These assets form the **visual storytelling layer** of the platform — from **hero backgrounds and header banners**, to **placeholders**, **historical imagery**, and **component thumbnails** in documentation and UI previews.

All files here are served **statically from the CDN** (not bundled by Vite), and optimized for performance, accessibility, and reproducibility.
Every image’s source, license, and checksum are tracked under the **Master Coder Protocol (MCP)** for design provenance and archival integrity.

> **Design Intent:** Every image captures Kansas’s light, land, and legacy — turning open imagery into open history.

---

## 🧱 Directory Structure

```text
web/public/assets/images/
├── placeholder.jpg          # Generic fallback image
├── header-bg.jpg            # Header and landing banner background
├── prairie-sunrise.jpg      # Thematic hero image for branding
├── kansas-river-aerial.webp # Hydrology section background (optimized)
├── topo-overlay.png         # Historic topographic overlay (semi-transparent)
├── timeline-bg.jpg          # Background texture for the timeline panel
├── thumbnails/              # Component thumbnails for docs and previews
│   ├── timeline-thumb.png
│   ├── mapview-thumb.png
│   └── aiassistant-thumb.png
└── README.md                # This documentation file
```

---

## 🧩 Asset Categories

| Category          | Description                                    | Format     | Example Use         |
| :---------------- | :--------------------------------------------- | :--------- | :------------------ |
| **Backgrounds**   | Full-width banners and hero sections           | JPG / WEBP | Home, About, Modals |
| **Placeholders**  | Fallback images when no data visuals exist     | JPG        | DetailPanel, Cards  |
| **Illustrations** | Scenic/abstract imagery tied to Kansas history | JPG / PNG  | Landing Pages       |
| **Overlays**      | Transparent PNGs layered over maps/timelines   | PNG        | MapView overlays    |
| **Thumbnails**    | Documentation and AI-generated previews        | PNG        | Docs / Storybook    |

---

## 🎨 Design & Theming Guidelines

All images conform to the **KFM Design System** principles:

* **Aspect Ratio:** Prefer 16:9 or 21:9 for hero banners
* **Resolution:** ≥1920px width (desktop) · ≥1280px (tablet)
* **Compression:** JPEG ≈ 85%, WebP ≈ 80%, PNG lossless
* **Color Tokens:**

  * Accent → `#00b3b3`
  * Background Dark → `#0b1020`
  * Background Light → `#ffffff`
* **Dynamic Theming:** Swap light/dark variants with CSS media queries

Example:

```css
body {
  background-image: url("/assets/images/header-bg.jpg");
}
@media (prefers-color-scheme: dark) {
  body {
    background-image: url("/assets/images/header-bg-dark.jpg");
  }
}
```

---

## 🧮 Optimization Pipeline

All images are processed in CI for **compression**, **conversion**, and **integrity verification**.

| Tool            | Function                                           |
| :-------------- | :------------------------------------------------- |
| **Sharp**       | Resize & convert to JPEG/WebP                      |
| **MozJPEG**     | Optimize JPEGs for high-quality progressive output |
| **pngquant**    | Compress transparent PNGs (80–95% quality)         |
| **cwebp**       | Generate modern WebP alternatives                  |
| **ImageMagick** | Validate resolution, DPI, and EXIF metadata        |
| **SHA256**      | Generate integrity checksums for cache validation  |

Each processed image includes metadata such as original source, author, license, and checksum in `/meta/`.

---

## ♿ Accessibility Standards

* **Alt Text:** Every image includes clear `alt` text describing its content or function.
* **Decorative Imagery:** Use `alt=""` or `role="presentation"` for non-informational backgrounds.
* **No Text-in-Image:** All text rendered via HTML/CSS to support localization and screen readers.
* **Contrast:** Maintain ≥ 4.5:1 ratio between overlays and background visuals.
* **Compliance:** All visuals validated against WCAG 2.1 AA.

Accessibility checks are executed in CI with **axe-core** and **Lighthouse** reports.

---

## 🧾 Provenance & Licensing

| Asset                      | Source                    | License       | Purpose           |
| :------------------------- | :------------------------ | :------------ | :---------------- |
| `placeholder.jpg`          | Custom KFM Design         | MIT           | Fallback asset    |
| `prairie-sunrise.jpg`      | Unsplash (Public Domain)  | CC0           | Hero background   |
| `kansas-river-aerial.webp` | USGS Public Archive       | Public Domain | Hydrology visual  |
| `topo-overlay.png`         | USGS 1894 Topo Collection | Public Domain | Map overlay       |
| `timeline-bg.jpg`          | Custom KFM Gradient       | MIT           | Timeline backdrop |

**Metadata Example:**

```json
{
  "id": "prairie-sunrise",
  "source": "Unsplash / John Doe",
  "license": "CC0",
  "tags": ["kansas", "sunrise", "prairie"],
  "checksum": "sha256:e4b9f1..."
}
```

---

## 🧩 Usage in Components

| Component        | Image                 | Purpose                              |
| :--------------- | :-------------------- | :----------------------------------- |
| **Header**       | `header-bg.jpg`       | Hero banner background               |
| **MapView**      | `topo-overlay.png`    | Historic base overlay                |
| **TimelineView** | `timeline-bg.jpg`     | Panel gradient background            |
| **DetailPanel**  | `placeholder.jpg`     | Default image for missing visuals    |
| **Docs/About**   | `prairie-sunrise.jpg` | Scenic illustration for storytelling |

---

## 🧪 Validation & Integrity

CI performs automated checks to ensure:

* File structure & naming consistency
* Resolution within defined bounds (min 1080p)
* No embedded EXIF or geolocation metadata
* Correct MIME type and file headers
* Matching SHA256 hashes between versions
* Metadata JSON schema conformance

All results are published in the CI/CD build report for transparent verification.

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                   |
| :------------------ | :----------------------------------------------- |
| Documentation-first | Each image tracked in metadata registry          |
| Provenance          | Source, author, and license logged in meta files |
| Reproducibility     | Deterministic image optimization pipeline        |
| Accessibility       | WCAG 2.1 AA compliance verified in CI            |
| Open Standards      | PNG, JPEG, WebP formats; JSON metadata schema    |
| Auditability        | Hash-based validation + CI image integrity logs  |

---

## 🔗 Related Documentation

* **Public Assets Overview** — `web/public/README.md`
* **Public Icons** — `web/public/assets/icons/README.md`
* **Design Mockups** — `docs/design/mockups/`
* **Accessibility Reviews** — `docs/design/reviews/accessibility/`

---

## 📜 License

All **custom Kansas Frontier Matrix images** are released under the **MIT License**,
and third-party materials are used under their respective **Public Domain** or **CC0** licenses.

© 2025 Kansas Frontier Matrix — created under **MCP-DL v6.2** for **accessible**, **traceable**, and **archivally sound** visual storytelling.

> *“Every image is a window into Kansas — the frontier’s light, land, and legacy rendered in pixels.”*

```
```
