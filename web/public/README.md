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

```yaml
---
title: "KFM • Web Public Assets (web/public/)"
version: "v1.4.0"
last_updated: "2025-10-14"
owners: ["@kfm-web", "@kfm-design"]
tags: ["assets","pwa","html","icons","manifest","seo","mcp"]
license: "MIT"
semantic_alignment:
  - WCAG 2.1 AA
  - W3C HTML5
  - W3C Web Manifest
  - Search Engine Indexing (robots + sitemap)
---
````

---

## 🧭 Overview

The `web/public/` directory contains **static, unprocessed assets** served directly by the Kansas Frontier Matrix (KFM) web application.
This includes the **HTML entry point**, **favicons**, **logos**, **PWA manifest**, and **SEO metadata** such as `robots.txt` and `sitemap.xml`.

These files form the **public interface of the web client**, copied verbatim into the build output (`/build/`).
Under **MCP-DL v6.2**, every asset within this directory is **documented, licensed, and traceable**, ensuring transparent provenance and reproducible deployments.

---

## 🧱 Directory Structure

```text
web/public/
├── index.html             # HTML entry point (Vite injects compiled React assets)
├── favicon.ico            # Browser tab icon
├── apple-touch-icon.png   # iOS home screen icon
├── manifest.webmanifest   # Progressive Web App (PWA) metadata
├── robots.txt             # Search engine directives
├── sitemap.xml            # SEO sitemap for route indexing
├── assets/                # Static logos, icons, and imagery
│   ├── logo.svg
│   ├── logo-dark.svg
│   ├── placeholder.jpg
│   └── icons/
│       ├── map-marker.svg
│       ├── timeline-icon.svg
│       └── ai-icon.svg
└── README.md              # This documentation file
```

---

## 🏠 index.html

The HTML root document of the KFM web application.
Vite injects all built assets (`main.js`, `style.css`, etc.) at build time.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Kansas Frontier Matrix — Explore Kansas history through time and terrain." />
    <meta property="og:title" content="Kansas Frontier Matrix" />
    <meta property="og:description" content="An interactive spatiotemporal knowledge map of Kansas history." />
    <meta property="og:type" content="website" />
    <link rel="icon" href="/favicon.ico" />
    <title>Kansas Frontier Matrix</title>
  </head>
  <body>
    <noscript>Please enable JavaScript to use Kansas Frontier Matrix.</noscript>
    <div id="root"></div>
  </body>
</html>
```

> The document is **semantically structured**, ensuring accessibility and search engine compatibility.

---

## 📱 manifest.webmanifest

Defines Progressive Web App (PWA) properties to enable installable web behavior.

```json
{
  "name": "Kansas Frontier Matrix",
  "short_name": "FrontierMatrix",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0b1020",
  "theme_color": "#00b3b3",
  "icons": [
    { "src": "/assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

This file inherits its theme configuration from `web/config/themes.json` during the CI build pipeline.

---

## 🤖 robots.txt

Specifies which resources are indexable by web crawlers.

```txt
User-agent: *
Allow: /
Sitemap: https://frontiermatrix.org/sitemap.xml
```

> Maintained automatically in CI via the documentation build workflow.

---

## 🗺️ sitemap.xml

Defines the canonical route list for search engine indexing.
Generated dynamically during build to reflect all public pages.

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://frontiermatrix.org/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://frontiermatrix.org/docs/</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

---

## 🎨 assets/

The `/assets/` directory holds static design artifacts — logos, icons, and imagery aligned with the official **Design System** (`docs/design/`).

| Asset               | Purpose                           | License   |
| :------------------ | :-------------------------------- | :-------- |
| `logo.svg`          | Default light-mode logo           | CC-BY 4.0 |
| `logo-dark.svg`     | Dark theme version                | CC-BY 4.0 |
| `map-marker.svg`    | Map icons for interactive markers | MIT       |
| `timeline-icon.svg` | Timeline navigation icon          | MIT       |
| `ai-icon.svg`       | AI Assistant badge                | MIT       |

All files include license metadata within their SVG headers.

---

## 🧩 Integration With Build System

* **Vite Injection:** `index.html` is processed by Vite and populated with asset references at build.
* **Static Copy:** `manifest.webmanifest`, `robots.txt`, and all icons are copied directly to `/build/`.
* **Environment Variables:** `.env` variables like `VITE_APP_TITLE` influence page titles and meta tags.
* **Checksums:** CI computes SHA-256 checksums for static assets to ensure version integrity.
* **Compression:** Assets are compressed and cached for long-term delivery (gzip + Brotli).

---

## ♿ Accessibility & SEO Compliance

| Concern                   | Implementation                                                     |
| :------------------------ | :----------------------------------------------------------------- |
| **Semantic HTML**         | Proper heading hierarchy and language attributes (`lang="en"`)     |
| **Contrast & Visibility** | Icons and logos tested for ≥ 4.5:1 color contrast ratio            |
| **Alt Text**              | Every image includes descriptive `alt` or `<title>` attributes     |
| **Metadata**              | Open Graph + Twitter Card tags provide structured preview data     |
| **Indexing**              | robots.txt and sitemap.xml updated automatically via CI            |
| **Keyboard Focus**        | Skip links and focus outlines enabled in `index.html` and base CSS |

---

## 🧾 Provenance & Integrity

| Artifact         | Description                                                                      |
| :--------------- | :------------------------------------------------------------------------------- |
| **Inputs**       | Branding assets, sitemap generator, manifest configuration, theme tokens         |
| **Outputs**      | Public build directory (`/build/`) deployed to GitHub Pages / CDN                |
| **Dependencies** | Vite, Node.js, TailwindCSS, favicon generator                                    |
| **Integrity**    | CI validates checksums, licenses, and metadata completeness per MCP-DL standards |

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                         |
| :------------------ | :----------------------------------------------------- |
| Documentation-first | All public assets documented and licensed              |
| Provenance          | SHA256 asset checksums logged in CI                    |
| Accessibility       | WCAG 2.1 AA-compliant static layout                    |
| Reproducibility     | Versioned public directory in Git                      |
| Open Standards      | HTML5, Web Manifest, XML Sitemap, robots.txt           |
| Traceability        | Design files link to `docs/design/mockups/` references |

---

## 🔗 Related Documentation

* **Web Configuration** — `web/config/README.md`
* **Web UI Architecture** — `web/ARCHITECTURE.md`
* **Design System Overview** — `docs/design/README.md`
* **Accessibility Reviews** — `docs/design/reviews/accessibility/`

---

## 📜 License

All public files are distributed under the **MIT License** unless otherwise noted.
© 2025 Kansas Frontier Matrix — built and released under **MCP-DL v6.2** for transparency, accessibility, and open digital heritage design.

> *“Public assets are the façade of the frontier — the first sight of Kansas’s digital landscape.”*

```
```
