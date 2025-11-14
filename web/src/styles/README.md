---
title: "🎨 Kansas Frontier Matrix — Web Styles & Design System (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/styles/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-styles-v2.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Web Styles & Design System**  
`web/src/styles/README.md`

**Purpose:**  
Define the **FAIR+CARE-aligned design tokens, accessibility standards, theming architecture, and global CSS framework** for the KFM Web Platform.  
The v10.3 design layer ensures deterministic styling, A11y compliance, sustainability metrics, and provenance-aware UX under **MCP-DL v6.3**.

[![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)]()  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()  
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)]()

</div>

---

## 📘 Overview

The **Styles system** governs:

- Design tokens (color, spacing, typography, motion, elevation)  
- High-level theming (light, dark, high-contrast)  
- Global styles + Tailwind integration  
- Layout primitives & utility classes  
- A11y tokens (focus rings, contrast, motion preferences)  
- Governance-aware UI patterns (CARE masking, provenance styling)  
- Sustainability metrics for render cost  

All styles must adhere to:

- **WCAG 2.1 AA**,  
- **FAIR+CARE ethical UI rules**,  
- **MCP-DL v6.3 documentation and contract enforcement**,  
- And CI/CD validation via **Lighthouse**, **axe-core**, **CSS lint**, and **token schema guards**.

---

## 🗂️ Directory Layout (v10.3.1)

~~~~~text
web/src/styles/
├── README.md                # This file
├── globals.css              # Resets, base variables, root-level rules
├── tokens.css               # Full design token registry (color, space, type, elevation)
├── themes.css               # Light / dark / high-contrast variants
├── animations.css           # Motion-safe animations & reduced-motion rules
├── utilities.css            # Shared utility classes & A11y helpers
└── metadata.json            # Governance + accessibility metadata for the design system
~~~~~

---

## 🧩 Design System Workflow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Design Tokens<br/>(color · spacing · type · motion)"]
    --> B["Themes<br/>(light · dark · high-contrast)"]
  B --> C["Global Styles<br/>(CSS vars + Tailwind config)"]
  C --> D["UI Components<br/>(MapView · Timeline · FocusPanel)"]
  D --> E["Telemetry + A11y Validation<br/>(axe/Lighthouse)"]
~~~~~

**Pipeline Notes:**

1. **Tokens** define fundamental, stable visual primitives.  
2. **Themes** apply tokens across accessible palettes.  
3. **Global Styles** expose tokens to Tailwind + React.  
4. **Components** rely exclusively on tokenized classes.  
5. **A11y + Telemetry** ensure measurable, reproducible, ethical UX.

---

## ♿ Accessibility Standards (WCAG 2.1 AA)

The design system enforces:

- Contrast ≥ **4.5:1** for text, ≥ **3:1** for large text  
- **Keyboard-visible** focus rings using tokenized focus styles  
- **Skip links**, structural/ARIA landmarks, screen-reader targets  
- Motion control via:
  - `prefers-reduced-motion: reduce`
  - ethical animation durations  
- **High-contrast** theme baseline  
- **RTL support** (mirrored spacing, directional tokens)

All accessibility tokens defined in:

```
docs/design/tokens/accessibility-tokens.md
```

---

## 🎨 Design Token Registry

| Token Group | Examples | Purpose |
|-------------|----------|----------|
| **Color** | `--kfm-color-primary`, `--kfm-surface`, `--kfm-border-strong` | A11y-compliant palettes |
| **Spacing** | `--kfm-space-1..12` | Temporal + spatial rhythm |
| **Typography** | `--kfm-font-size-100..900`, `--kfm-font-sans` | Legibility + clarity |
| **Elevation** | `--kfm-shadow-1..5` | High-contrast, no motion excess |
| **Motion** | `--kfm-duration-fast..slow` | Reduced-motion friendly |
| **Radius** | `--kfm-radius-sm..2xl` | Card/corner shape standards |

Tokens are validated by token-schema CI and **must remain stable** for UI determinism.

---

## 🧪 Style Contracts & Validation

| Contract | Enforcement | Artifact |
|---------|-------------|----------|
| Token Schema | Token linter + CSS schema guards | `docs/reports/self-validation/styles/token_schema.json` |
| Theme Contract | Visual regression tests + contrast checks | `docs/reports/self-validation/styles/theme_regression.json` |
| A11y Contract | axe-core + Lighthouse CI | `docs/reports/self-validation/web/a11y_summary.json` |
| Build Weight | CI budget (<150 KB CSS) | `docs/reports/telemetry/build_metrics.json` |

All style changes require updated metadata in:

```
web/src/styles/metadata.json
```

---

## 🌱 Sustainability Metrics

| Metric | Target | Verified By |
|--------|--------|-------------|
| Render Energy / View | ≤ 0.6 Wh | Telemetry export |
| CSS Payload Size | ≤ 150 KB | Build metrics |
| Lighthouse A11y Score | ≥ 95 | CI accessibility scans |
| Token Reuse Rate | ≥ 90% | CSS bundle analysis |

Telemetry written to:

```
../../../releases/v10.3.0/focus-telemetry.json
```

---

## 🧾 Example Style System Metadata Record (v10.3.1)

~~~~~json
{
  "id": "web_styles_v10.3.1",
  "themes": ["light", "dark", "high-contrast"],
  "wcag": "2.1 AA",
  "contrast_min_ratio": 4.5,
  "render_energy_wh": 0.58,
  "checksum_verified": true,
  "timestamp": "2025-11-13T18:30:00Z",
  "telemetry_ref": "releases/v10.3.0/focus-telemetry.json",
  "governance_ref": "docs/reports/audit/web-governance-ledger.json"
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | Web Design Team | Upgraded from v9.7.0 → v10.3; fully tokenized; added sustainability + governance bindings. |
| v9.7.0 | 2025-11-05 | KFM Core Team | Prior design token system with early governance integration. |

---

<div align="center">

**Kansas Frontier Matrix — Web Styles System**  
Accessible × Ethical × Sustainable × Deterministic  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Web Source](../README.md) · [Architecture](../ARCHITECTURE.md)

</div>
