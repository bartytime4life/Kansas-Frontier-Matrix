---
title: "🧮 Kansas Frontier Matrix — Data Domain Icons (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/data/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../../releases/v9.5.0/web-icons-data.meta.json"
validation_reports:
  - "../../../../reports/self-validation/web-icons-data-validation.json"
  - "../../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧮 Kansas Frontier Matrix — **Data Domain Icons**
`web/public/icons/data/README.md`

**Purpose:** Documents all domain-specific icons representing data types (climate, hazards, treaties, hydrology, archaeology, and cultural datasets) in the Kansas Frontier Matrix interface. Establishes design governance, FAIR+CARE metadata compliance, and accessibility standards for data-driven iconography.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../../docs/standards/governance/LEDGER.md)
[![Accessibility · WCAG 2.2 AA](https://img.shields.io/badge/Accessibility-WCAG%202.2%20AA-blueviolet)](https://www.w3.org/WAI/WCAG22/)

</div>

---

## 📁 Directory Layout

```
web/public/icons/data/
├── icon-data-climate.svg          # Climate dataset representation
├── icon-data-hazards.svg          # Natural hazard dataset
├── icon-data-treaties.svg         # Treaty and legal boundary dataset
├── icon-data-hydrology.svg        # Rivers, watersheds, and aquifer data
├── icon-data-archaeology.svg      # Archaeological dataset
├── icon-data-culture.svg          # Cultural or heritage dataset
├── icon-data-landuse.svg          # Land use and cover change data
├── icon-data-geology.svg          # Geological survey or formation data
├── legacy/                        # Archived/retired data icons
└── README.md                      # This file
```

---

## 🎨 Design Standards

| Property | Specification | Description |
|-----------|----------------|-------------|
| **Format** | SVG preferred | Vector format ensures scalability and light file size. |
| **Grid Size** | 24×24 px | Adheres to design grid for uniform UI integration. |
| **Stroke Width** | 1.5 px | Consistent with all KFM interface icons. |
| **Color Tokens** | `/web/public/assets/tokens.json` | Use semantic palette (`dataset-*`, `neutral-*`, `hazard-*`, etc.). |
| **Theme Variants** | `-light` / `-dark` | Both variants required for theme accessibility. |
| **Naming Convention** | `icon-data-{domain}.svg` | Example: `icon-data-hydrology.svg`, `icon-data-treaties.svg`. |

---

## 🧩 Implementation & Usage

1. **React Integration**
   ```js
   import { IconDataHydrology } from "@/components/icons/data";
   ```
   Example:
   ```jsx
   <div className="dataset-icon">
     <IconDataHydrology size={24} aria-label="Hydrology Dataset" />
     <span>Hydrology Data</span>
   </div>
   ```

2. **Accessibility Guidelines**
   - Include `aria-label` and `title` attributes for all icons.  
   - Maintain at least a **4.5:1** contrast ratio for all color variants.  
   - Use shape and labeling redundantly (never color-only indicators).  
   - Validate against WCAG 2.2 AA using CI workflow.  

3. **Metadata & Governance**
   - Each icon requires metadata (`web-icons-data.meta.json`).  
   - Metadata must include `license`, `creator`, `checksum`, `themes`, and `provenance`.  
   - Deprecated icons moved to `/legacy/` for preservation.  
   - All icons validated by `.github/workflows/icon-validate.yml`.  

---

## ⚙️ CI/CD Validation Workflow

**Workflow:** `.github/workflows/icon-validate.yml`

**Automated Tasks**
- SVG linting and optimization via SVGO  
- Metadata verification (`schemas/ui/icons.schema.json`)  
- FAIR+CARE compliance evaluation  
- SHA-256 checksum validation  
- WCAG 2.2 AA accessibility check  

Reports generated in:
- `reports/self-validation/web-icons-data-validation.json`  
- `reports/audit/web-icons-faircare.json`

---

## 🧾 Example Metadata Entry

```json
{
  "id": "icon-data-hazards",
  "title": "Hazard Dataset Icon",
  "category": "data",
  "version": "3.0.0",
  "creator": "KFM Design Systems",
  "license": "MIT",
  "checksum": "sha256-87d9a31e94f2aaf3a7d47b6125f2f3eeed9b4a...",
  "themes": ["light", "dark"],
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "provenance": "Designed for natural hazard dataset layer in v9.5.0; includes FAIR+CARE metadata integration and improved accessibility."
}
```

---

## 📊 Telemetry & FAIR+CARE Metrics

All results are logged in `releases/v9.5.0/focus-telemetry.json` and visualized in the Governance Ledger.

**Key Metrics:**
- ✅ Metadata completeness rate  
- 🧾 License and provenance validation success  
- ♿ Accessibility audit score  
- 🔐 Checksum verification percentage  
- 📊 FAIR+CARE compliance index  

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Added metadata governance and accessibility schema for dataset icons | Design Systems Team |
| v9.3.2 | 2025-10-20 | Introduced FAIR+CARE auditing and automated checksum validation | Governance Council |
| v9.0.0 | 2025-09-25 | Created data icon directory for domain-based datasets | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Icons that Represent Knowledge · Metadata that Defines Integrity.”*

</div>

