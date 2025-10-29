---
title: "🌐 Kansas Frontier Matrix — Web Public Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/README.md"
version: "v9.3.2"
last_updated: "2025-10-28"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../../releases/v9.3.2/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🌐 Kansas Frontier Matrix — **Web Public Assets**
`web/public/README.md`

**Purpose:** Provides documentation for the public-facing static assets used by the Kansas Frontier Matrix web application.  
Ensures all assets meet accessibility, licensing, and FAIR+CARE governance standards and are deployed under transparent open-source compliance.

[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../docs/standards/faircare-validation.md)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-blue)](https://www.w3.org/WAI/WCAG21/quickref/)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

The `web/public/` directory contains all **publicly accessible static files** served directly by the KFM web app during runtime and deployment.  
These assets support **frontend rendering**, **branding**, **metadata configuration**, and **Progressive Web App (PWA)** functionality.  
Every file here is included in the production build output and must comply with **FAIR+CARE** accessibility and governance standards.

**Key Features:**
- Public entry points for the web interface (`index.html`, `manifest.webmanifest`)  
- Metadata files for SEO and accessibility compliance  
- Icons, favicons, and open-license images  
- Attribution pages for external datasets and graphics  
- Legal and ethical disclaimers required by FAIR+CARE Council

---

## 🗂️ Directory Layout

```plaintext
web/public/
├── README.md                  # Documentation for all public assets
│
├── index.html                 # Main HTML entry point rendered by Vite
├── favicon.ico                # Application favicon (open license)
├── manifest.webmanifest       # PWA manifest for browser and mobile metadata
├── robots.txt                 # Search engine and crawler directives
├── sitemap.xml                # Sitemap for SEO and archival crawlers
│
├── icons/                     # Application and OS icon set
│   ├── icon-192.png
│   ├── icon-512.png
│   └── apple-touch-icon.png
│
├── images/                    # Static images (logos, banners, illustrations)
│   ├── kfm_logo.svg
│   ├── kansas_frontier_banner.webp
│   ├── open_data_badge.png
│   └── faircare_logo.svg
│
└── meta/                      # Metadata and configuration
    ├── license.txt
    ├── attribution.md
    └── open_graph.json
```

---

## ⚙️ Asset Governance

Every file within this directory must declare or reference:
1. **License:** All visual assets and metadata files must be open-licensed (MIT, CC-BY 4.0, or Public Domain).  
2. **Attribution:** Visuals or icons sourced from external repositories must be cited in `meta/attribution.md`.  
3. **Provenance:** The creation or modification history of each asset is recorded in the MCP Git log.  
4. **Accessibility:** Images must include alternative text and conform to WCAG 2.1 AA standards.  
5. **Ethics:** Content displayed in the public interface must meet FAIR+CARE ethical use criteria.

---

## 🧠 FAIR+CARE Compliance

| Principle | Implementation |
|------------|----------------|
| **Findable** | Metadata, sitemap, and robots directives improve discovery. |
| **Accessible** | WCAG 2.1 AA accessibility and PWA compatibility. |
| **Interoperable** | Open formats (`.svg`, `.webp`, `.json`, `.md`) used for all files. |
| **Reusable** | Clearly licensed, attributed, and reproducible assets. |
| **Collective Benefit** | Open educational and civic data for Kansas history and science. |
| **Authority to Control** | Proper attribution and licensing retained for all assets. |
| **Responsibility** | Content verified for ethical representation and inclusivity. |
| **Ethics** | Logos and banners reviewed to ensure cultural sensitivity and inclusivity. |

---

## 🧩 Accessibility & SEO Standards

To guarantee universal access and machine readability, all public files adhere to:
- **WCAG 2.1 AA Accessibility Guidelines**  
- **HTML5 Validation** for semantic tags  
- **WAI-ARIA** roles and attributes  
- **SEO Best Practices**, including metadata and Open Graph tags  

Accessibility validation occurs automatically in the build process (`npm run lint:a11y`).

---

## 🧱 Progressive Web App (PWA) Manifest

The `manifest.webmanifest` defines KFM’s identity for browsers and devices:

```json
{
  "name": "Kansas Frontier Matrix",
  "short_name": "KFM",
  "description": "An open, interactive atlas of Kansas—linking history, science, and AI insights.",
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

> 🧭 **Note:** The PWA manifest ensures consistent branding, accessibility, and offline readiness, with all icons validated against open-source license metadata.

---

## 🧾 Licensing & Attribution

- All assets are licensed under **MIT (code)** or **CC-BY 4.0 (data/media)**.  
- Attribution for reused graphics or datasets is listed in `meta/attribution.md`.  
- Ethical approval for imagery depicting historical or Indigenous material is logged in `reports/audit/ui_ethics_review.json`.  

---

## 🧩 Governance Integration

**Related Workflows:**
- `.github/workflows/site.yml` — Builds and deploys the public-facing site.  
- `.github/workflows/faircare-validate.yml` — Validates licensing, accessibility, and attribution metadata.  
- `.github/workflows/governance-ledger.yml` — Registers new or modified assets in provenance logs.

Artifacts generated:
- `reports/ui-accessibility.json` — Accessibility validation report  
- `reports/audit/ui_license_check.json` — License validation record  
- `releases/v9.3.2/manifest.zip` — Includes checksum of all public assets  

---

## 🧾 Version History

| Version | Date       | Author             | Summary |
|----------|------------|--------------------|----------|
| v9.3.2   | 2025-10-28 | @kfm-ui-lab        | Initial documentation of public asset governance and FAIR+CARE compliance. |
| v9.3.1   | 2025-10-27 | @bartytime4life    | Added attribution, accessibility, and license tracking schema. |
| v9.3.0   | 2025-10-26 | @kfm-architecture  | Established public directory and PWA manifest integration. |

---

<div align="center">

**Kansas Frontier Matrix** · *Open Design × Accessibility × Ethical Transparency*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../../docs/) • [⚖️ Governance Ledger](../../docs/standards/governance/)

</div>