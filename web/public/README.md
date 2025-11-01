---
title: "🌐 Kansas Frontier Matrix — Web Public Assets (Tier-Ω+∞ Certified)"
path: "web/public/README.md"
version: "v2.1.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v2.1.1/sbom.spdx.json"
manifest_ref: "../../releases/v2.1.1/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
owners: ["@kfm-web","@kfm-design","@kfm-accessibility","@kfm-docs"]
maturity: "Production"
status: "Stable"
tags: ["public-assets","web","pwa","seo","accessibility","fair","care","governance"]
alignment:
  - MCP-DL v6.4.3
  - FAIR / CARE
  - WCAG 2.1 AA / HTML5
  - PWA / SEO / Open Graph
  - ISO 9241-210 Human-Centered Design
preservation_policy:
  retention: "public assets permanent · accessibility audits 5 years"
  checksum_algorithm: "SHA-256"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Public Assets (v2.1.1 · Tier-Ω+∞ Certified)**  
`web/public/README.md`

**Mission:** Document and govern all **public-facing static assets** used by the Kansas Frontier Matrix web application —  
ensuring open licensing, accessibility, and FAIR+CARE-aligned ethical governance for all published web resources.

[![📦 Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![♿ Accessibility](https://img.shields.io/badge/WCAG%202.1%20AA-Validated-brightgreen)](../../docs/standards/accessibility.md)
[![🌍 FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../docs/standards/faircare-validation.md)
[![📄 License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![📘 Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue?logo=markdown)](../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

The `web/public/` directory contains all **publicly accessible static files** served by the KFM web app.  
These include metadata, icons, banners, manifest files, SEO metadata, and legal/ethical notices.

Every file here is part of the **production deployment** and must:
- Be open-licensed and attributed properly.  
- Pass FAIR+CARE governance and accessibility audits.  
- Comply with **WCAG 2.1 AA** and **PWA** standards.  
- Support long-term reproducibility and discoverability under **MCP-DL governance**.

---

## 🗂️ Directory Layout

```bash
web/public/
├── README.md                     # This file — documentation for all public assets
│
├── index.html                    # Main entry point rendered by Vite
├── favicon.ico                   # Open-licensed favicon
├── manifest.webmanifest           # PWA manifest defining KFM’s identity
├── robots.txt                    # Crawler directives (ethical web indexing)
├── sitemap.xml                   # Sitemap for SEO and archival tools
│
├── icons/                        # App & OS icon set
│   ├── icon-192.png
│   ├── icon-512.png
│   └── apple-touch-icon.png
│
├── images/                       # Public images, logos, and banners
│   ├── kfm_logo.svg
│   ├── kansas_frontier_banner.webp
│   ├── faircare_logo.svg
│   └── open_data_badge.png
│
└── meta/                         # Metadata and legal information
    ├── license.txt
    ├── attribution.md
    └── open_graph.json
```

---

## ⚙️ Asset Governance

Every file must include:
1. **License** — Declared in file header or `meta/license.txt` (MIT, CC-BY 4.0, or Public Domain).  
2. **Attribution** — Documented in `meta/attribution.md` for all reused assets.  
3. **Provenance** — Changes tracked via Git history and governance ledger.  
4. **Accessibility** — Alt text, captions, and semantics verified in CI.  
5. **Ethics** — Images and media must pass FAIR+CARE cultural sensitivity review.

---

## 🧠 FAIR + CARE Integration

| Principle | Implementation | Validation |
|:--|:--|:--|
| **Findable** | SEO metadata (`sitemap.xml`, `open_graph.json`). | `policy-check.yml` |
| **Accessible** | WCAG 2.1 AA and PWA compatibility. | `design-validate.yml` |
| **Interoperable** | Open file formats (.svg, .json, .webp). | `ui-validate.yml` |
| **Reusable** | CC-BY 4.0 licensing and clear attribution. | `faircare-validate.yml` |
| **Collective Benefit (CARE)** | Ethical open data and educational media. | `governance-ledger.yml` |

---

## ♿ Accessibility & SEO Standards

To ensure global accessibility:
- **WCAG 2.1 AA** compliance verified for alt text, colors, and contrast.  
- **HTML5 Validation** required for all pages.  
- **WAI-ARIA Roles** included in `index.html`.  
- **SEO Metadata** managed via `sitemap.xml` and `open_graph.json`.  

Accessibility scans run in CI via `npm run lint:a11y` → `reports/ui-accessibility.json`.

---

## 🧱 Progressive Web App (PWA) Manifest

Defines KFM identity across browsers and devices.

```json
{
  "name": "Kansas Frontier Matrix",
  "short_name": "KFM",
  "description": "An open, interactive atlas of Kansas linking history, science, and AI insights.",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#f9fafb",
  "theme_color": "#1e40af",
  "icons": [
    { "src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

---

## 🧾 Licensing & Attribution

- All assets: **MIT (code)**, **CC-BY 4.0 (media/docs)**.  
- Attribution: listed in `meta/attribution.md`.  
- Historical/Indigenous imagery reviewed by FAIR+CARE Ethics Council.  
- Audit results: `reports/audit/ui_ethics_review.json`.

---

## 🧩 Governance Integration

| Workflow | Function | Output |
|:--|:--|:--|
| `site.yml` | Builds and deploys frontend site. | `dist/` + release assets |
| `faircare-validate.yml` | Validates licensing, accessibility, and attribution. | `reports/fair/data_care_assessment.json` |
| `governance-ledger.yml` | Logs public assets checksums to ledger. | `data/reports/audit/data_provenance_ledger.json` |

Artifacts produced:
- `reports/ui-accessibility.json` — Accessibility validation  
- `reports/audit/ui_license_check.json` — License/attribution report  
- `releases/v2.1.1/manifest.zip` — Asset checksum manifest  

---

## 🕰 Version History

| Version | Date | Author | Summary |
|:--|:--|:--|:--|
| **v2.1.1** | 2025-11-16 | @kfm-web | Updated to Tier-Ω+∞; added FAIR+CARE governance and PWA validation schema. |
| v9.3.2 | 2025-10-28 | @kfm-ui-lab | Documented public asset FAIR+CARE compliance. |
| v9.3.1 | 2025-10-27 | @bartytime4life | Added attribution, accessibility, and license validation schema. |
| v9.3.0 | 2025-10-26 | @kfm-architecture | Created PWA manifest and public metadata integration. |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*“Public by Design — Ethical by Default.”*  
📍 `web/public/README.md` — FAIR+CARE-aligned public assets documentation for the Kansas Frontier Matrix.

</div>
