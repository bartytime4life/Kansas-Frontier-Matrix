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

## 🧭 Overview

`web/public/assets/images/` contains **raster imagery** for the KFM web client—hero/section backgrounds, illustrations, placeholders, and **component thumbnails** used across docs and UI previews.  
Files are served **statically** (not bundled by Vite) and are governed by **MCP-DL v6.2** for **provenance, accessibility, and reproducibility**.

> *Design intent:* every image supports legible storytelling—never obscuring content, always respecting contrast, motion, and user preferences.

---

## 🧱 Directory Structure

```text
web/public/assets/images/
├── placeholder.jpg               # Generic fallback image
├── header-bg.jpg                 # Landing/header banner (light)
├── header-bg-dark.jpg            # Dark theme variant
├── prairie-sunrise.jpg           # Scenic hero image for docs/branding
├── kansas-river-aerial.webp      # Hydrology section background (optimized)
├── topo-overlay.png              # Semi-transparent topo texture
├── timeline-bg.jpg               # Timeline panel background texture
├── thumbnails/                   # Component thumbnails for docs/previews
│   ├── timeline-thumb.png
│   ├── mapview-thumb.png
│   └── aiassistant-thumb.png
└── README.md                     # This document
```

---

## 🧩 Asset Categories

| Category          | Description                                       | Preferred Formats | Example Use                     |
| :---------------- | :------------------------------------------------ | :---------------- | :------------------------------ |
| **Backgrounds**   | Full-bleed hero/section imagery                   | JPG / WEBP        | Home, About, section headers    |
| **Placeholders**  | Generic fallbacks for missing visuals             | JPG               | DetailPanel, cards, empty state |
| **Illustrations** | Scenic/abstract visuals tied to Kansas themes     | JPG / PNG         | Landing pages, docs             |
| **Overlays**      | Semi-transparent textures layered under UI        | PNG               | Map/Timeline décor              |
| **Thumbnails**    | Small UI previews in docs/Storybook               | PNG               | Docs, changelogs, PR templates  |

---

## 🎨 Design & Theming Guidelines

- **Aspect Ratio:** Prefer **16:9** or **21:9** for hero banners; use focal cropping for mobile.  
- **Resolution:** ≥ **1920px** (desktop), ≥ **1280px** (tablet), provide **@2x** when practical.  
- **Compression Baselines:** JPEG ≈ **85%**, WebP ≈ **80%**, PNG **lossless**.  
- **Color Tokens:** adhere to Design System variables (examples below).

```css
/* Themed backgrounds */
body { background-image: url("/assets/images/header-bg.jpg"); }
@media (prefers-color-scheme: dark) {
  body { background-image: url("/assets/images/header-bg-dark.jpg"); }
}

/* Overlay safety: ensure readable content on top */
.hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(0deg, rgba(0,0,0,.35), rgba(0,0,0,.0));
}
```

---

## 🧮 Optimization Pipeline (CI)

| Tool        | Purpose                                           |
| :---------- | :------------------------------------------------ |
| **Sharp**   | Resize, format conversion (JPG/WEBP), @2x emits   |
| **MozJPEG** | Progressive JPEG optimization (~85 quality)       |
| **pngquant**| Transparent PNG compression (80–95% quality)      |
| **cwebp**   | Modern WebP output (lossy/lossless as needed)     |
| **Magick**  | Validate resolution, DPI, strip EXIF/geo          |
| **SHA-256** | Per-file checksums for cache/integrity            |

Artifacts include **before/after sizes** and checksum manifests.

---

## ♿ Accessibility Standards

- **Alt text** on informative images; decorative backgrounds use `alt=""` or CSS only.  
- **No text-in-image** for UI copy—render via HTML/CSS for localization and AT.  
- **Contrast safety:** ensure overlays and content meet **≥ 4.5:1**.  
- **Reduced motion:** avoid parallax/video backgrounds; respect `prefers-reduced-motion`.  
- **Zoom/HiDPI:** images remain legible at **200%** zoom and on Retina displays.

CI runs **axe-core** + **Lighthouse** accessibility checks.

---

## 🧾 Provenance & Licensing

| Asset                      | Source                     | License       | Purpose                |
| :------------------------- | :------------------------- | :------------ | :--------------------- |
| `placeholder.jpg`          | KFM Design                 | MIT           | Generic fallback       |
| `prairie-sunrise.jpg`      | Unsplash (Public Domain)   | CC0           | Hero/Docs illustration |
| `kansas-river-aerial.webp` | USGS Public Archive        | Public Domain | Hydrology background   |
| `topo-overlay.png`         | USGS Historic Maps         | Public Domain | Subtle topo texture    |
| `timeline-bg.jpg`          | KFM Gradient               | MIT           | Timeline panel backdrop|

**Per-asset metadata** (origin, author, license, checksum) stored in `/assets/meta/*.json`.

---

## 🧩 Usage in Components

| Component        | Image                 | Purpose                         |
| :--------------- | :-------------------- | :------------------------------ |
| **Header**       | `header-bg.jpg`       | Hero background                 |
| **MapView**      | `topo-overlay.png`    | Historic texture overlay        |
| **TimelineView** | `timeline-bg.jpg`     | Panel backdrop                  |
| **DetailPanel**  | `placeholder.jpg`     | Default/empty states            |
| **Docs/About**   | `prairie-sunrise.jpg` | Scenic storytelling image       |

---

## 🧪 Validation & Integrity

CI verifies:

- Naming/placement against this README schema  
- Resolution bounds (min 1280w; hero ≥ 1920w)  
- Correct MIME/type headers; EXIF/geolocation stripped  
- **SHA-256** hashes and metadata JSON validity  
- Presence of light/dark variants where required

Reports published to `ci/reports/images/`.

---

## 🧠 MCP Compliance Checklist

| Principle           | Implementation                                   |
| :------------------ | :----------------------------------------------- |
| Documentation-first | Asset families and rules captured in this README |
| Provenance          | `/assets/meta/*.json` with source/license/hash   |
| Reproducibility     | Deterministic CI pipeline & checksums            |
| Accessibility       | WCAG 2.1 AA validation in CI                     |
| Open Standards      | PNG · JPEG · WebP; JSON metadata schema          |
| Auditability        | Size diffs, hashes, and reports retained in CI   |

---

## 🔗 Related Documentation

- **Public Assets Overview** — `web/public/README.md`  
- **Public Icons** — `web/public/assets/icons/README.md`  
- **Design System** — `docs/design/README.md`  
- **Accessibility Reviews** — `docs/design/reviews/accessibility/`

---

## 🧾 Versioning & Metadata

| Field | Value |
| :---- | :---- |
| **Version** | `v1.6.0` |
| **Codename** | *Storytelling Images & Provenance Upgrade* |
| **Last Updated** | 2025-10-17 |
| **Maintainers** | @kfm-design · @kfm-web |
| **License** | MIT (custom) · CC0/Public Domain (third-party as noted) |
| **Alignment** | WCAG 2.1 AA · W3C Web Image Formats · MCP-DL v6.2 |
| **Maturity** | Stable / Production |

---

## 📜 License

Custom Kansas Frontier Matrix images are **MIT**; third-party sources retain **CC0/Public Domain** per metadata.  
© 2025 Kansas Frontier Matrix — **MCP-DL v6.2** compliant for **accessible**, **traceable**, and **archivally sound** visuals.
