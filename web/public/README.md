<div align="center">

# 🌐 Kansas Frontier Matrix — **Web Public Assets**  
`web/public/`

**Static Files · HTML Entry Point · Icons · PWA Manifest**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../.github/workflows/ci.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../docs/design/reviews/accessibility/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

## 🧭 Overview

`web/public/` contains **static, unprocessed assets** served directly by the KFM Web App: the **HTML entry**, **favicons & logos**, **PWA manifest**, **robots.txt**, **sitemap.xml**, and other public files.  
Everything here is copied **verbatim** to the build output (`/build/`). Under **MCP-DL v6.2**, public assets are **documented, licensed, checksummed**, and **a11y/SEO-aligned** for reproducible releases.

---

## 🧱 Directory Structure

```text
web/public/
├── index.html               # HTML entry (Vite injects compiled assets)
├── favicon.ico
├── apple-touch-icon.png
├── manifest.webmanifest     # PWA metadata (name, icons, theme)
├── robots.txt               # Crawler directives
├── sitemap.xml              # Search engine indexing
├── security.txt             # Security contact (RFC 9116) - optional
├── assets/                  # Logos, icons, static imagery
│   ├── logo.svg
│   ├── logo-dark.svg
│   ├── placeholder.jpg
│   └── icons/
│       ├── icon-192.png
│       ├── icon-512.png
│       ├── map-marker.svg
│       ├── timeline-icon.svg
│       └── ai-icon.svg
└── README.md                # This document
```

---

## 🏠 index.html (HTML Entry)

Vite injects JS/CSS at build; keep it **semantic**, **a11y-ready**, and **SEO-complete**.

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Kansas Frontier Matrix</title>

    <!-- Description & Open Graph -->
    <meta name="description" content="Kansas Frontier Matrix — Explore Kansas history through time and terrain." />
    <meta property="og:title" content="Kansas Frontier Matrix" />
    <meta property="og:description" content="An interactive spatiotemporal knowledge map of Kansas history." />
    <meta property="og:type" content="website" />
    <meta property="og:image" content="/assets/placeholder.jpg" />
    <meta name="theme-color" content="#00b3b3" />

    <!-- PWA & Icons -->
    <link rel="manifest" href="/manifest.webmanifest" />
    <link rel="icon" href="/favicon.ico" />
    <link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180" />

    <!-- Security/Privacy hints (non-binding in static doc) -->
    <meta http-equiv="Permissions-Policy" content="geolocation=(), microphone=(), camera=()" />
    <meta http-equiv="X-Content-Type-Options" content="nosniff" />
  </head>
  <body>
    <a class="skip-link" href="#root">Skip to Content</a>
    <noscript>Please enable JavaScript to use Kansas Frontier Matrix.</noscript>
    <div id="root" role="main"></div>
  </body>
</html>
```

**Notes**

- **Skip link** improves keyboard navigation from the first paint.  
- Color/contrast for logos/icons should satisfy **WCAG 2.1 AA** on both themes.

---

## 📱 manifest.webmanifest (PWA)

```json
{
  "name": "Kansas Frontier Matrix",
  "short_name": "FrontierMatrix",
  "start_url": "/",
  "display": "standalone",
  "scope": "/",
  "background_color": "#0b1020",
  "theme_color": "#00b3b3",
  "icons": [
    { "src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable" },
    { "src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" }
  ]
}
```

> Theme colors and names can be **templated** from `web/config/themes.json` during CI.

---

## 🤖 robots.txt

```txt
User-agent: *
Allow: /
Sitemap: https://frontiermatrix.org/sitemap.xml
```

**Tip:** Use environment-specific `Sitemap:` (e.g., staging vs prod) in CI.

---

## 🗺️ sitemap.xml

`/sitemap.xml` is generated at build from the public routes.

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://frontiermatrix.org/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>https://frontiermatrix.org/docs/</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>
</urlset>
```

---

## 🔐 security.txt (optional but recommended)

Provide a **security contact** per **RFC 9116**.

```txt
Contact: mailto:security@frontiermatrix.org
Preferred-Languages: en
Policy: https://frontiermatrix.org/security
```

---

## 🎨 assets/ (Logos & Icons)

Static design artifacts aligned with the **Design System** (`docs/design/`).

| Asset               | Purpose                            | License   |
| :------------------ | :--------------------------------- | :-------- |
| `logo.svg`          | Default light-mode logo            | CC-BY 4.0 |
| `logo-dark.svg`     | Dark theme variant                 | CC-BY 4.0 |
| `icon-192.png`      | PWA icon (maskable)                | MIT       |
| `icon-512.png`      | PWA icon (maskable)                | MIT       |
| `map-marker.svg`    | Map marker glyph                   | MIT       |
| `timeline-icon.svg` | Timeline UI glyph                  | MIT       |
| `ai-icon.svg`       | AI Assistant badge                 | MIT       |

> Embed license/attribution in SVG `<metadata>` blocks where applicable.

---

## 🧩 Build & Release Integration

- **Vite Injection:** `index.html` receives hashed JS/CSS.  
- **Static Copy:** `manifest.webmanifest`, icons, and SEO files pass through unchanged.  
- **Env Templating:** `VITE_APP_TITLE`, `VITE_APP_DESCRIPTION`, and theme tokens fill meta and manifest fields.  
- **Checksums:** CI writes **SHA-256** for each asset; list stored as an artifact.  
- **Compression & Caching:** CI emits **Brotli + gzip**; sets long-lived cache headers for immutable assets.

---

## ♿ Accessibility & SEO

| Concern           | Implementation                                                                 |
| :---------------- | :------------------------------------------------------------------------------ |
| **Semantic HTML** | `lang`, `dir`, roles, skip link, `<noscript>`                                  |
| **Contrast**      | Logo/icon palettes validated ≥ **4.5:1** across themes                         |
| **Meta**          | Description + Open Graph for rich link previews                                |
| **Indexing**      | `robots.txt` + `sitemap.xml` kept current by CI                                 |
| **Keyboard**      | Skip link is focusable & visible on focus (base CSS)                           |

Example base CSS (in `web/src/styles/base.css`):

```css
.skip-link{position:absolute;left:-9999px;top:auto}
.skip-link:focus{left:1rem;top:1rem;padding:.25rem .5rem;background:#00b3b3;color:#000}
```

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                                          |
| :--------------- | :------------------------------------------------------------------- |
| **Inputs**       | Branding assets, manifest template, sitemap generator, theme tokens  |
| **Outputs**      | `/build/` public bundle (HTML, icons, manifest, robots, sitemap)     |
| **Dependencies** | Vite, Node.js, PostCSS/Tailwind, favicon/manifest tooling            |
| **Integrity**    | CI validates **licenses**, **checksums**, and **meta completeness** (MCP-DL) |

---

## 🧠 MCP Compliance Checklist

* ✅ **Documentation-first**: every public asset documented & licensed  
* ✅ **Provenance**: SHA-256 checksums stored per-release  
* ✅ **Accessibility**: WCAG 2.1 AA static surface; skip link on first paint  
* ✅ **Reproducibility**: environment-templated manifest/meta under version control  
* ✅ **Open Standards**: HTML5, Web Manifest, XML Sitemap, robots.txt

---

## 🔗 Related Documentation

* **Web Configuration** — `web/config/README.md`  
* **Web UI Architecture** — `web/ARCHITECTURE.md`  
* **Design System** — `docs/design/README.md`  
* **Accessibility Reviews** — `docs/design/reviews/accessibility/`

---

## 🧾 Versioning & Metadata

| Field | Value |
| :---- | :---- |
| **Version** | `v1.6.0` |
| **Codename** | *Public Interface & PWA Hardening* |
| **Last Updated** | 2025-10-17 |
| **Maintainers** | @kfm-web · @kfm-design |
| **License** | MIT (code) · CC-BY 4.0 (artwork/docs) |
| **Alignment** | WCAG 2.1 AA · W3C HTML5 · Web Manifest · SEO (robots+sitemap) |
| **Maturity** | Stable / Production |

---

## 📜 License

All public files are distributed under the **MIT License** unless otherwise noted.  
© 2025 Kansas Frontier Matrix — released under **MCP-DL v6.2** for transparent, accessible, and reproducible web delivery.

> *“Public assets are the façade of the frontier — the first sight of Kansas’s digital landscape.”*
