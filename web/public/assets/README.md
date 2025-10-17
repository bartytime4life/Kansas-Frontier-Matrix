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

## 🧭 Overview

`web/public/assets/` holds the **visual/brand foundations** of KFM—**logos**, **icons**, **images**, and **static map overlays**—served directly by the CDN (not bundled).  
Assets follow the **KFM Design System** and **MCP-DL v6.2** for provenance, accessibility, and reproducibility.

> *Each asset is a fragment of Kansas’s visual story—coherent through shared tokens and semantics.*

---

## 🧱 Directory Structure

```text
web/public/assets/
├── logo.svg
├── logo-dark.svg
├── favicon-32x32.png
├── icons/
│   ├── map-marker.svg
│   ├── timeline.svg
│   ├── ai-bot.svg
│   ├── filter.svg
│   └── info.svg
├── images/
│   ├── placeholder.jpg
│   ├── header-bg.jpg
│   └── prairie-sunrise.jpg
├── maps/
│   ├── topo_1894_overlay.png
│   ├── treaty_boundaries_outline.svg
│   └── hydrology_network_light.svg
└── README.md
```

---

## 🎨 Design System Integration

Tokens (from `web/src/styles/variables.scss` / `web/config/themes.json`) guide color/shape/contrast:

| Token                | Example                        | Purpose                               |
| :------------------- | :----------------------------- | :------------------------------------ |
| `--kfm-color-accent` | `#00b3b3`                      | Primary accent                        |
| `--kfm-color-bg`     | `#0b1020` (dark) / `#ffffff`   | Backgrounds                           |
| `--kfm-radius`       | `12px`                          | Corner radii for badges/buttons/icons |
| `--kfm-shadow`       | `0 2px 8px rgba(0,0,0,.15)`     | Elevation                             |

**Adaptive SVG example**

```svg
<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <circle cx="32" cy="32" r="30" fill="var(--kfm-color-accent)" />
</svg>
```

---

## 🧩 Asset Provenance

| Asset                           | Source                         | License       | Purpose                          |
| :------------------------------ | :----------------------------- | :------------ | :------------------------------- |
| `logo.svg`                      | KFM Design (Figma export)      | MIT           | Primary brand mark               |
| `map-marker.svg`                | KFM Icon Set                   | MIT           | Map markers                      |
| `ai-bot.svg`                    | Derived (RemixIcon)            | MIT           | AI Assistant avatar              |
| `placeholder.jpg`               | Unsplash                       | CC0           | Empty state                      |
| `topo_1894_overlay.png`         | USGS Archive                   | Public Domain | Historic topo overlay            |
| `treaty_boundaries_outline.svg` | Digitized by KFM               | CC-BY 4.0     | Treaty boundary reference        |

> Each file has metadata in `/assets/meta/` (origin, author, license, checksum, revision date).

---

## 🗺️ Usage in Components

| Component        | Asset                                                     | Use Case                              |
| :--------------- | :-------------------------------------------------------- | :------------------------------------ |
| Header           | `logo.svg`, `logo-dark.svg`                               | Branding                              |
| MapView          | `icons/map-marker.svg`, `maps/topo_1894_overlay.png`      | Markers & raster overlay              |
| TimelineView     | `icons/timeline.svg`                                      | Toolbar/legend icon                   |
| AIAssistant      | `icons/ai-bot.svg`                                        | Assistant avatar/badge                |
| Modals/Sidebar   | `icons/info.svg`, `icons/filter.svg`                      | Controls & help                       |
| Public Branding  | `favicon-32x32.png`, `apple-touch-icon.png` (in `/public`) | Browser/PWA assets                     |

---

## 📦 Optimization Pipeline (CI)

| Step               | Tool            | Notes                                                |
| :----------------- | :-------------- | :--------------------------------------------------- |
| PNG compression    | `pngquant`      | 80–95% quality, palette optimized                    |
| JPEG optimization  | `mozjpeg`       | Quality ~85, progressive                             |
| SVG minification   | `svgo` (multipass) | Removes metadata/paths; keeps `<metadata>` license |
| Hashing            | `sha256sum`     | Integrity checksums per asset                        |
| CDN deploy         | Pages / R2      | Long-cache immutable, Brotli + gzip variants         |

**CI logs** include before/after sizes and checksum tables.

---

## ♿ Accessibility & Compliance

- **Alt text** for informative images; decorative icons use `role="presentation"`.  
- **ARIA** labels where icons represent actions (`aria-label="Filter"`).  
- **Contrast** validated ≥ **4.5:1** in light/dark.  
- **Scalability** via vector-first approach; fallbacks for older UAs.  
- **Licensing** embedded in SVG `<metadata>` where allowed.

---

## 🧾 Provenance & Integrity

| Artifact   | Description                                                  |
| :--------- | :----------------------------------------------------------- |
| Inputs     | Figma exports, STAC overlays, open-source icon sets          |
| Outputs    | Optimized static assets under version control                |
| Dependencies | Node.js, Sharp, SVGO, build scripts                       |
| Integrity  | SHA-256 checksums verified during CI/CD                      |

---

## 🧠 MCP Compliance Checklist

| Principle           | Implementation                                        |
| :------------------ | :---------------------------------------------------- |
| Documentation-first | Asset families documented with examples               |
| Provenance          | `/assets/meta/*.json` records for each file           |
| Accessibility       | WCAG 2.1 AA tokens & alt/ARIA patterns                |
| Reproducibility     | Deterministic CI optimization + hashing               |
| Open Standards      | SVG · PNG · JPEG · Public Domain/CC licensing         |

---

## 🔗 Related Documentation

- **Web Public** — `web/public/README.md`  
- **Web Config** — `web/config/README.md`  
- **Design System** — `docs/design/README.md`  
- **Accessibility Reviews** — `docs/design/reviews/accessibility/`

---

## 🧾 Versioning & Metadata

| Field | Value |
| :---- | :---- |
| **Version** | `v1.6.0` |
| **Codename** | *Design Tokens & Provenance Upgrade* |
| **Last Updated** | 2025-10-17 |
| **Maintainers** | @kfm-design · @kfm-web |
| **License** | MIT (custom assets) · CC/PD for third-party as noted |
| **Alignment** | WCAG 2.1 AA · W3C SVG/Web Graphics · MCP-DL v6.2 |
| **Maturity** | Stable / Production |

---

## 📜 License

Custom KFM assets: **MIT**. Third-party resources: retain their **original licenses** (CC-BY, CC0, Public Domain).  
© 2025 Kansas Frontier Matrix — produced under **MCP-DL v6.2** for **traceable provenance**, **inclusive design**, and **archival quality**.
