<div align="center">

# 🖼️ Kansas Frontier Matrix — **Public Assets**  
`web/public/assets/`

**Logos · Icons · Images · Maps**

[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![Design System](https://img.shields.io/badge/Design-System-blue)](../../../docs/design/)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../docs/design/reviews/accessibility/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Public Assets (web/public/assets/)"
version: "v1.5.0"
last_updated: "2025-10-14"
owners: ["@kfm-design", "@kfm-web"]
tags: ["assets","design","icons","maps","images","branding","mcp"]
license: "MIT"
semantic_alignment:
  - WCAG 2.1 AA
  - W3C SVG & Web Graphics
  - MCP-DL v6.2 (Design Provenance)
---
````

---

## 🧭 Overview

The `web/public/assets/` directory contains the **visual and brand foundations** of the Kansas Frontier Matrix (KFM) web experience — including **logos**, **icons**, **images**, and **map overlays** used throughout the interactive interface.

All files in this directory are **served statically** from the CDN or `/build/assets/` output and are **not bundled** by Vite.
They adhere to the **Kansas Frontier Matrix Design System** and the **Master Coder Protocol (MCP)** standards for provenance, accessibility, and reproducibility.

> **Design Philosophy:** Each asset represents a piece of Kansas’s visual identity — unified through shared color tokens, geometry, and historical relevance.

---

## 🧱 Directory Structure

```text
web/public/assets/
├── logo.svg                # Primary KFM logo (vector, light theme)
├── logo-dark.svg           # Dark mode variant
├── favicon-32x32.png       # Browser favicon
├── icons/                  # UI icons for map, timeline, AI, etc.
│   ├── map-marker.svg
│   ├── timeline.svg
│   ├── ai-bot.svg
│   ├── filter.svg
│   └── info.svg
├── images/                 # Static images and placeholder media
│   ├── placeholder.jpg
│   ├── header-bg.jpg
│   └── prairie-sunrise.jpg
├── maps/                   # Historical overlays, static maps, STAC-derived assets
│   ├── topo_1894_overlay.png
│   ├── treaty_boundaries_outline.svg
│   └── hydrology_network_light.svg
└── README.md               # This documentation file
```

---

## 🎨 Design System Integration

All assets conform to **KFM Design Tokens** (defined in `web/config/themes.json` and `docs/design/mockups/`).

| Token                 | Example                      | Purpose                                              |
| :-------------------- | :--------------------------- | :--------------------------------------------------- |
| `--kfm-color-accent`  | `#00b3b3`                    | Primary turquoise accent across branding             |
| `--kfm-color-bg-dark` | `#0b1020`                    | Background color for dark mode                       |
| `--kfm-radius`        | `1rem`                       | Consistent corner radius for icons and UI components |
| `--kfm-shadow`        | `0 2px 8px rgba(0,0,0,0.15)` | Drop shadow for elevation consistency                |

**SVGs** should utilize CSS variables for color and adapt dynamically to light/dark themes:

```svg
<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <circle cx="32" cy="32" r="30" fill="var(--kfm-color-accent)" />
</svg>
```

---

## 🧩 Asset Provenance

| Asset                           | Source                       | License       | Purpose                            |
| :------------------------------ | :--------------------------- | :------------ | :--------------------------------- |
| `logo.svg`                      | Custom design (Figma export) | MIT           | Primary logo                       |
| `map-marker.svg`                | Custom KFM icon set          | MIT           | Used in MapView markers            |
| `ai-bot.svg`                    | Derived from RemixIcon       | MIT           | AI Assistant avatar                |
| `placeholder.jpg`               | Unsplash (public domain)     | CC0           | Placeholder image for empty states |
| `topo_1894_overlay.png`         | USGS Public Archive          | Public Domain | Historic map overlay               |
| `treaty_boundaries_outline.svg` | Digitized by KFM Team        | CC-BY 4.0     | Treaty boundary layer              |

> Every asset has an accompanying metadata record stored in `/assets/meta/`
> containing its origin, author, license, checksum, and last revision date.

---

## 🗺️ Usage in Components

| Component           | Asset                                                  | Description                           |
| :------------------ | :----------------------------------------------------- | :------------------------------------ |
| **Header**          | `logo.svg`, `logo-dark.svg`                            | Branding in the top navigation        |
| **MapView**         | `/icons/map-marker.svg`, `/maps/topo_1894_overlay.png` | Interactive markers & overlays        |
| **TimelineView**    | `/icons/timeline.svg`                                  | Toolbar and legend iconography        |
| **AIAssistant**     | `/icons/ai-bot.svg`                                    | Assistant avatar and logo badge       |
| **Modals**          | `/icons/info.svg`, `/icons/filter.svg`                 | UI controls and accessibility symbols |
| **Public Branding** | `favicon-32x32.png`, `apple-touch-icon.png`            | Browser + PWA branding assets         |

---

## 📦 Asset Optimization Pipeline

All raster and vector assets are optimized via the **CI/CD pipeline**:

| Process           | Tool                       | Description                                      |
| :---------------- | :------------------------- | :----------------------------------------------- |
| PNG Compression   | `pngquant`                 | Adaptive palette compression (80–95% quality)    |
| JPEG Optimization | `mozjpeg`                  | Reduces file size while preserving quality (85%) |
| SVG Minification  | `svgo --multipass`         | Removes metadata, comments, and redundant paths  |
| Hashing           | `sha256sum`                | Generates per-asset integrity checks             |
| CDN Deployment    | `gh-pages / Cloudflare R2` | Caches and serves optimized static assets        |

> Optimization results are logged in CI with before/after size metrics and validation reports.

---

## ♿ Accessibility & Compliance

* **Alt Text:** Informative images include descriptive `alt` attributes; decorative icons use `role="presentation"`.
* **ARIA Labels:** Applied to interactive graphics (`aria-label="Map marker icon"`).
* **Color Contrast:** All design assets validated for ≥ 4.5:1 contrast ratio in both light/dark themes.
* **Scalability:** SVGs ensure crisp rendering on high DPI/Retina displays.
* **Fallbacks:** PNG or ICO fallbacks provided for browsers lacking SVG support.

Accessibility validations are automatically performed in CI using **axe-core** and **Lighthouse**.

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                                     |
| :--------------- | :-------------------------------------------------------------- |
| **Inputs**       | Design mockups, Figma exports, STAC overlays, open-source icons |
| **Outputs**      | Optimized, licensed static assets for deployment                |
| **Dependencies** | Sharp, SVGO, TailwindCSS, Node.js build scripts                 |
| **Integrity**    | SHA256 checksums verified during CI/CD deployment               |

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                                 |
| :------------------ | :------------------------------------------------------------- |
| Documentation-first | Each asset family documented and versioned                     |
| Provenance          | Metadata (.json) tracking origin, license, and author          |
| Accessibility       | WCAG 2.1 AA compliant design and icons                         |
| Reproducibility     | CI optimization pipeline with deterministic hashing            |
| Design Consistency  | Tokens + theme variables applied globally                      |
| Open Standards      | SVG 1.1 · PNG 1.2 · JPEG 2000 · Public Domain Data Integration |

---

## 🔗 Related Documentation

* **Web Public README** — `web/public/README.md`
* **Web Configuration** — `web/config/README.md`
* **Design Mockups** — `docs/design/mockups/`
* **Accessibility Guidelines** — `docs/design/reviews/accessibility/`

---

## 📜 License

All **custom Kansas Frontier Matrix assets** are distributed under the **MIT License**,
while third-party resources retain their respective open licenses (CC-BY, CC0, or Public Domain).

© 2025 Kansas Frontier Matrix — created under **MCP-DL v6.2** for **traceable provenance**, **inclusive design**, and **archival quality**.

> *“Every pixel and vector tells a story — these assets visualize Kansas’s living digital frontier.”*

```
```
