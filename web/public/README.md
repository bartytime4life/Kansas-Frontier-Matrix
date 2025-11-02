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

**Mission:** Document, preserve, and ethically govern all **public-facing static assets** powering the Kansas Frontier Matrix web application.  
Ensures full compliance with FAIR+CARE, accessibility (WCAG 2.1 AA), and open licensing for every file made public.

[![📦 Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![♿ Accessibility](https://img.shields.io/badge/WCAG%202.1%20AA-Validated-brightgreen)](../../docs/standards/accessibility.md)  
[![🌍 FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../docs/standards/faircare-validation.md)  
[![📄 License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)  
[![📘 Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue?logo=markdown)](../../docs/architecture/repo-focus.md)

</div>

---

## 📚 Overview

This directory (`web/public/`) contains all static assets distributed to the public layer of the KFM platform.  
Assets here form part of the live, production-grade deployment and are covered by KFM’s **Tier-Ω+∞ Certification**, indicating long-term archival, open licensing, and verified accessibility compliance.

Core goals:
- **Accessibility:** Each file passes WCAG 2.1 AA validation.  
- **Openness:** All content is under CC-BY 4.0 or equivalent open license.  
- **Governance:** Metadata, checksums, and licenses are reviewed quarterly.  
- **Reproducibility:** All assets versioned under MCP-DL governance frameworks.  

---

## 🗂️ Directory Layout

```bash
web/public/
├── README.md                     # This file — documentation and governance reference
│
├── index.html                    # Main HTML entry for the app (includes Open Graph metadata)
├── favicon.ico                   # KFM favicon — CC-BY-licensed icon
├── manifest.webmanifest           # PWA manifest defining KFM web identity and theme
├── robots.txt                    # Ethical crawler rules for archival indexing
├── sitemap.xml                   # Sitemap ensuring SEO and scholarly discoverability
│
├── icons/                        # Icon set for devices, PWA, and OS integrations
│   ├── icon-192.png              # Web app icon (standard)
│   ├── icon-512.png              # High-resolution PWA icon
│   └── apple-touch-icon.png      # iOS-specific web clip icon
│
├── images/                       # Publicly displayed imagery and logos
│   ├── kfm_logo.svg              # Project branding logo (SVG)
│   ├── kansas_frontier_banner.webp # Homepage banner image
│   ├── faircare_logo.svg         # FAIR+CARE certification emblem
│   └── open_data_badge.png       # Open data badge for UI footer and reports
│
└── meta/                         # Metadata, licenses, and Open Graph data for web integrity
    ├── license.txt               # License summary for all assets in this directory
    ├── attribution.md            # List of all external attributions (required by CC-BY)
    └── open_graph.json           # Open Graph / SEO metadata for web embedding
```

### File Functions:
- **`index.html`** — Primary entrypoint for SPA/PWA rendering. Includes `<meta>` tags for accessibility and SEO.  
- **`manifest.webmanifest`** — PWA configuration for installable KFM web apps.  
- **`robots.txt` / `sitemap.xml`** — Ethical indexing controls and findability layer for academic crawlers.  
- **`meta/license.txt`** — Legal overview of usage permissions for public content.  
- **`meta/attribution.md`** — Credits all third-party resources, fonts, and icons with proper citation.  
- **`meta/open_graph.json`** — Provides structured social media and SEO metadata.  

---

## ⚙️ Asset Governance

Each file in this directory must comply with the following governance conditions:

1. **License Attribution** — Declared in headers or in `meta/license.txt` (MIT, CC-BY 4.0, or Public Domain).  
2. **Accessibility Metadata** — Must include alt-text, ARIA roles, or descriptive captions.  
3. **Checksum Integrity** — Verified SHA-256 hashes in every release manifest.  
4. **Ethical Media Policy** — All imagery reviewed for cultural appropriateness per FAIR+CARE.  
5. **Reproducibility Chain** — File lineage recorded via Immutable Governance Ledger.  

Quarterly FAIR+CARE validation reports are published to:
```
reports/fair/web-public-validation-summary.json
reports/audit/web-public-lineage.json
```

---

## 🧠 FAIR + CARE Implementation

| Principle | Implementation | Validation Workflow |
|------------|----------------|----------------------|
| **Findable** | Open Graph metadata (`open_graph.json`, `sitemap.xml`) | `policy-check.yml` |
| **Accessible** | WCAG 2.1 AA, semantic HTML, ARIA attributes | `design-validate.yml` |
| **Interoperable** | Open formats (.svg, .json, .webp, .txt) | `ui-validate.yml` |
| **Reusable** | Open licensing (CC-BY 4.0) and full attribution | `faircare-validate.yml` |
| **Collective Benefit (CARE)** | Ethical review and inclusive visual design | `governance-ledger.yml` |

---

## ♿ Accessibility & SEO Standards

Public assets are tested continuously for compliance with:
- **WCAG 2.1 AA accessibility guidelines**
- **HTML5 validation** using W3C validator
- **Lighthouse SEO benchmarks (≥90%)**
- **ARIA compliance for all images and interactive elements**

Reports generated automatically under:
```
reports/ui-accessibility.json
reports/seo-audit.json
```

---

## 🧱 Progressive Web App (PWA) Manifest

Defines identity and appearance across browsers and devices.

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

## 🧩 Governance & Validation Integration

| Workflow | Function | Output |
|-----------|-----------|---------|
| `site.yml` | Builds and deploys production website | `dist/` artifacts + release bundle |
| `faircare-validate.yml` | Validates accessibility, licensing, and ethical compliance | `reports/fair/data_care_assessment.json` |
| `governance-ledger.yml` | Logs file checksums and provenance | `reports/audit/data_provenance_ledger.json` |
| `security-scan.yml` | Performs SBOM and open-source dependency checks | `reports/audit/ui_sbom_audit.json` |

Artifacts produced:
- `reports/ui-accessibility.json` — Accessibility validation report  
- `reports/audit/ui_license_check.json` — License and attribution report  
- `releases/v2.1.1/manifest.zip` — File manifest with SHA-256 checksums  

---

## 🧾 Licensing & Attribution

- **Software & Scripts:** MIT License  
- **Media & Documentation:** CC-BY 4.0 License  
- **Attribution:** Listed in `meta/attribution.md`  
- **Ethical Oversight:** Indigenous imagery and cultural content reviewed under FAIR+CARE framework  
- **Audit Log:** `reports/audit/ui_ethics_review.json`

---

## 🕰 Version History

| Version | Date | Author | Notes |
|----------|------|---------|--------|
| **v2.1.1** | 2025-11-16 | @kfm-web | Updated Tier-Ω+∞; implemented PWA validation, FAIR+CARE audits, and accessibility metadata. |
| v9.3.2 | 2025-10-28 | @kfm-ui-lab | Expanded FAIR+CARE integration and public asset licensing. |
| v9.3.1 | 2025-10-27 | @bartytime4life | Added attribution metadata and UI accessibility schema. |
| v9.3.0 | 2025-10-26 | @kfm-architecture | Initial deployment manifest and metadata registry. |

---

<div align="center">

**Kansas Frontier Matrix © 2025**  
*“Public by Design — Ethical by Default.”*  
📍 `web/public/README.md` — Core FAIR+CARE-aligned documentation for the Kansas Frontier Matrix public web assets.

</div>
