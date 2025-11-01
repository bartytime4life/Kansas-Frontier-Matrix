---
title: "🎨 Kansas Frontier Matrix — Web Public Icons (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-icons-v1.json"
json_export: "../../releases/v9.5.0/web-icons.meta.json"
validation_reports:
  - "../../reports/self-validation/web-icons-validation.json"
  - "../../reports/audit/web-icons-faircare.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🎨 Kansas Frontier Matrix — **Web Public Icons**
`web/public/icons/README.md`

**Purpose:** Defines, governs, and validates all iconography used across Kansas Frontier Matrix’s public web interface. Establishes FAIR+CARE-aligned metadata standards, licensing transparency, and accessibility compliance across design assets.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../docs/standards/governance/LEDGER.md)
[![Accessibility · WCAG 2.2 AA](https://img.shields.io/badge/Accessibility-WCAG%202.2%20AA-blueviolet)](https://www.w3.org/WAI/WCAG22/)

</div>

---

## 📁 Directory Layout

```
web/public/icons/
├── app/                 # Application icons (menus, dashboards, workflows)
├── data/                # Dataset-specific icons (climate, hazards, treaties, etc.)
├── system/              # System, telemetry, and governance icons
├── social/              # Collaboration & community icons
├── flags/               # Flags, markers, and geographic identifiers
├── badges/              # Certification, FAIR, MCP, Diamond⁹, and provenance badges
├── legacy/              # Archived/deprecated icons (for version traceability)
└── README.md            # This file
```

---

## 🧩 Icon Standards & Specifications

| Attribute | Requirement | Description |
|------------|--------------|-------------|
| **Format** | SVG preferred; PNG fallback | Vector-based for scalability and performance; raster only when required. |
| **Baseline Size** | 24 × 24 px grid | Matches KFM design token grid system and maintains consistency across UI. |
| **Color Tokens** | `/web/public/assets/tokens.json` | Reference official theme palette for accessibility compliance (contrast ≥ 4.5 : 1). |
| **Theme Variants** | `-light` / `-dark` suffix | Enables automatic mode switching via CSS/JS theme detector. |
| **Licensing** | CC-BY 4.0 / MIT / Public Domain | All licenses declared in `icons-license.json` and verified in CI. |
| **Metadata Schema** | `schemas/ui/icons.schema.json` | Defines mandatory fields (`id`, `title`, `license`, `checksum`, `theme`). |

---

## 🧭 Usage & Governance Guidelines

1. **React Component Mapping**  
   Each SVG icon maps to a React wrapper in `web/src/components/icons/`.  
   ```js
   import { IconHazard } from "@/components/icons";
   ```
   Components must accept `size`, `color`, and `ariaLabel` props for adaptive rendering.

2. **Accessibility Requirements**  
   - Provide `role="img"` and `aria-label` attributes.  
   - Use semantic naming (`icon-climate.svg`, `icon-flood.svg`).  
   - Avoid meaning-conveying color alone; ensure shape or label redundancy.

3. **Version Control**  
   - Icons adhere to semantic versioning synchronized with KFM UI releases.  
   - Archive superseded assets under `legacy/` with SHA-256 checksum for traceability.  
   - Maintain changelog entries within `icons-meta.json`.

4. **FAIR + CARE Compliance**  
   - Metadata fields: `creator`, `license`, `provenance`, `checksum`, `theme`.  
   - Auto-validated during pre-commit via `.github/workflows/icon-validate.yml`.  
   - Icons lacking verified metadata fail CI and block merge.

---

## ⚙️ CI/CD Validation Workflow

**Workflow:** `.github/workflows/icon-validate.yml`

**Automated checks**
- 🧹 SVG optimization (SVGO)  
- 🧾 Metadata validation against `schemas/ui/icons.schema.json`  
- 🔐 SHA-256 checksum verification  
- ♿ Accessibility scan (WCAG 2.2 AA contrast + ARIA labels)  
- 📜 License audit (MIT / CC-BY / Public Domain only)

Reports are exported to:
- `reports/self-validation/web-icons-validation.json`  
- `reports/audit/web-icons-faircare.json`  

---

## 🧱 Example Metadata Record

```json
{
  "id": "icon-flood",
  "title": "Flood Hazard Icon",
  "creator": "KFM Design Systems",
  "license": "CC-BY 4.0",
  "version": "3.0.0",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
  "checksum": "sha256-d3f54a29abc123ef...",
  "themes": ["light", "dark"],
  "provenance": "Derived from USGS public-domain symbology set"
}
```

---

## 🧩 Telemetry & Metrics

Each validated commit updates telemetry record `releases/v9.5.0/focus-telemetry.json` capturing:
- Number of active icons per category  
- Validation success/failure counts  
- Accessibility compliance percentage  
- FAIR+CARE compliance rating  

These metrics populate the Focus Mode dashboard and the Governance Ledger.

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Updated to MCP-DL v6.4.3; added telemetry & FAIR + CARE audit hooks | Design Systems Team |
| v9.3.2 | 2025-10-20 | Revised metadata schema & CI pipeline alignment | Governance Council |
| v9.2.0 | 2025-10-15 | Introduced FAIR + CARE audit for media assets | Governance Council |
| v9.0.0 | 2025-09-30 | Established unified icon directory & licensing rules | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Clarity through Design · Provenance through Form · Integrity through Verification.”*

</div>
