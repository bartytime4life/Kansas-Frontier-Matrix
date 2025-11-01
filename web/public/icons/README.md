---
title: "🎨 Kansas Frontier Matrix — Web Public Icons (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/README.md"
version: "v9.3.2"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.3.2/sbom.spdx.json"
manifest_ref: "../../releases/v9.3.2/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🎨 Kansas Frontier Matrix — **Web Public Icons**
`web/public/icons/README.md`

**Purpose:** Documents the structure, usage, and governance of icon assets used in the Kansas Frontier Matrix web application’s public interface. Ensures visual consistency, accessibility compliance, and open-license transparency across all UI components.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Accessibility: WCAG 2.1 AA](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-blueviolet)](https://www.w3.org/WAI/WCAG21/)

</div>

---

## 📁 Directory Layout

```
web/public/icons/
├── app/                 # Application-level icons (menu, dashboard, timeline)
├── data/                # Dataset or domain-specific icons (climate, hazards, treaties)
├── system/              # System, settings, and governance icons
├── social/              # External links, community, collaboration icons
├── flags/               # Flags and regional markers (SVGs, PNGs)
├── badges/              # FAIR, MCP, and Diamond⁹ certification marks
├── legacy/              # Deprecated icons (retained for versioning)
└── README.md            # This file
```

---

## 🧩 Icon Specifications

| Property | Standard | Description |
|-----------|-----------|-------------|
| **Format** | SVG (preferred), PNG fallback | All icons should be vector-based (SVG) for scalability and accessibility. |
| **Size** | 24×24 px baseline | Aligns with Material Design grid and Figma design tokens. |
| **Color Palette** | Derived from `/web/public/assets/tokens.json` | Matches official KFM design tokens ensuring color accessibility. |
| **Theme Support** | Light / Dark mode variants | Use suffixes `-light` and `-dark` for theme-adaptive icons. |
| **License** | CC-BY 4.0 / MIT / Public Domain | Must be explicitly documented in `icons-license.json`. |

---

## 🧭 Usage Guidelines

1. **Component Mapping:**  
   Each icon maps to a React component in `web/src/components/icons/`.  
   Example:  
   ```js
   import { IconClimate } from "@/components/icons";
   ```

2. **Accessibility:**  
   - Include `aria-label` or `title` attributes for screen readers.  
   - Avoid color-only differentiation; use shape or contrast variants.

3. **Versioning:**  
   Icons follow semantic versioning aligned with UI releases.  
   Example: `climate-v2.svg` supersedes `climate.svg` (v1) but both remain archived in `legacy/`.

4. **Governance & FAIR Compliance:**  
   - Each icon must include metadata in `/web/public/icons/icons-meta.json` specifying `creator`, `license`, `source_url`, and `checksum`.  
   - Changes trigger automatic verification in CI (`icon-validate.yml`).

---

## 🛠️ CI/CD Validation

The `.github/workflows/icon-validate.yml` workflow performs:
- SVG linting and optimization via SVGO  
- License and metadata validation  
- SHA-256 checksum comparison  
- Accessibility checks (contrast, ARIA compliance)

All passes are logged in `reports/self-validation/icons-validation.json`.

---

## 🧱 Example Metadata Entry

```json
{
  "id": "icon-climate",
  "title": "Climate Dataset Icon",
  "creator": "KFM Design System",
  "license": "CC-BY 4.0",
  "version": "2.0.1",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "checksum": "sha256-abc123...",
  "themes": ["light", "dark"]
}
```

---

## 🧾 Governance & Versioning

| Version | Date | Change Summary | Maintainer |
|----------|------|----------------|-------------|
| v9.3.2 | 2025-11-01 | Initial documentation of web/public/icons structure and metadata rules | Design Systems Team |
| v9.2.0 | 2025-10-15 | Introduced FAIR+CARE audit for media assets | Governance Council |
| v9.0.0 | 2025-09-30 | Established unified icon directory structure | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix** · *Design Systems Directorate*  
“Clarity through Design — Provenance through Form.”

</div>
