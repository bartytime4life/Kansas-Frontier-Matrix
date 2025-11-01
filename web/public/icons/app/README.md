---
title: "🧭 Kansas Frontier Matrix — Application Icons (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/icons/app/README.md"
version: "v9.5.0"
last_updated: "2025-11-01"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v9.5.0/sbom.spdx.json"
manifest_ref: "../../../releases/v9.5.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v9.5.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-icons-v1.json"
json_export: "../../../releases/v9.5.0/web-icons-app.meta.json"
validation_reports:
  - "../../../reports/self-validation/web-icons-app-validation.json"
  - "../../../reports/audit/web-icons-faircare.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
---

<div align="center">

# 🧭 Kansas Frontier Matrix — **Application Icons**
`web/public/icons/app/README.md`

**Purpose:** Defines standards and metadata for all application-level icons used in the Kansas Frontier Matrix UI (navigation, dashboards, panels, modals). Ensures semantic naming, accessible design, and lifecycle traceability under FAIR+CARE compliance.

[![Docs · MCP-DL v6.4.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.4.3-blue)](../../../docs/standards/markdown_rules.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-orange)](../../../docs/standards/governance/ROOT-GOVERNANCE.md)
[![Governance Ledger](https://img.shields.io/badge/Governance-Ledger-Active-purple)](../../../docs/standards/governance/LEDGER.md)
[![Accessibility · WCAG 2.2 AA](https://img.shields.io/badge/Accessibility-WCAG%202.2%20AA-blueviolet)](https://www.w3.org/WAI/WCAG22/)

</div>

---

## 📂 Directory Layout

```
web/public/icons/app/
├── nav/             # Navigation icons (Home, Explore, Timeline, Settings)
├── panels/          # Panel or modal UI icons (Info, Close, Expand)
├── dashboard/       # Main dashboard visual icons
├── timeline/        # Timeline interaction icons (Play, Pause, Focus)
├── forms/           # Input/validation icons (Save, Edit, Confirm)
├── alerts/          # App-level alert and status icons
├── meta/            # MCP, FAIR, or Governance-related UI symbols
└── README.md        # This file
```

---

## 🎨 Design Standards

| Parameter | Requirement | Description |
|------------|-------------|-------------|
| **Format** | SVG preferred | All icons are vector-based for performance and scale; rasterized variants stored only if essential. |
| **Grid System** | 24×24 px baseline | Aligns with the design system grid and ensures pixel-perfect scaling. |
| **Stroke Width** | 1.5 px uniform | Maintains clarity in dark/light modes and ensures visual harmony. |
| **Color Tokens** | `/web/public/assets/tokens.json` | Apply `primary-500`, `neutral-600`, or contrast-compliant palette variants. |
| **Theme Modes** | Light/Dark variants required | Maintain parity for accessibility (suffix `-light` / `-dark`). |
| **Naming Convention** | `icon-{context}-{function}.svg` | e.g., `icon-nav-home.svg`, `icon-timeline-play.svg`. |

---

## 🧩 Implementation Notes

1. **Component Import Pathing**
   - All icons map to React components in `web/src/components/icons/app/`.
   ```js
   import { IconNavHome } from "@/components/icons/app";
   ```
   - Each icon component exports accessible markup with `<title>` and `aria-label`.

2. **Dynamic Theming**
   - The app auto-detects user theme (`prefers-color-scheme`) and switches between suffix variants.
   - Dark variants use lighter strokes or fills to maintain contrast ≥ 4.5:1.

3. **Usage Context**
   - App-level icons appear only in structural UI areas (navbars, modals, dashboards).
   - Data-domain icons (hazards, treaties, etc.) reside in `/web/public/icons/data/`.

---

## ⚙️ Validation & Governance

**Workflow:** `.github/workflows/icon-validate.yml`  
Applies the following validation logic at each commit:
- SVG optimization via **SVGO**  
- Metadata validation via `schemas/ui/icons.schema.json`  
- SHA-256 checksum verification  
- WCAG 2.2 AA accessibility testing  
- License consistency check  

Reports are exported to:
- `reports/self-validation/web-icons-app-validation.json`  
- `reports/audit/web-icons-faircare.json`

---

## 🧾 Example Metadata

```json
{
  "id": "icon-nav-home",
  "title": "Home Navigation Icon",
  "category": "app/nav",
  "version": "3.1.0",
  "creator": "KFM Design System",
  "license": "MIT",
  "checksum": "sha256-1a3bc9f6df89acb...",
  "themes": ["light", "dark"],
  "provenance": "Designed in Figma, exported as SVG",
  "source_url": "https://github.com/bartytime4life/Kansas-Frontier-Matrix"
}
```

---

## 🧾 Version History

| Version | Date | Summary | Maintainer |
|----------|------|----------|-------------|
| v9.5.0 | 2025-11-01 | Updated app icon metadata schema and validation hooks | Design Systems Team |
| v9.3.2 | 2025-10-20 | Added theme-parity requirements and Figma source traceability | Governance Council |
| v9.2.0 | 2025-10-10 | Implemented naming conventions for timeline and panel icons | UI/UX Maintainers |
| v9.0.0 | 2025-09-25 | Created base structure and design token alignment | Core Maintainers |

---

<div align="center">

**Kansas Frontier Matrix — Design Systems Directorate**  
*“Precision in Form · Integrity in Access · Transparency in Design.”*

</div>

