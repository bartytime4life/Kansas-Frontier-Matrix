---
title: "🎨 Kansas Frontier Matrix — Accessible Color & Contrast Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/color-contrast.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-color-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Accessible Color & Contrast Standards**
`docs/accessibility/patterns/color-contrast.md`

**Purpose:**  
Define and enforce **color contrast, visual hierarchy, and palette usage standards** across all KFM interfaces — ensuring compliance with **WCAG 2.1 AA**, **ISO 9241-210**, and **FAIR+CARE inclusive design principles**.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Color and contrast are key accessibility factors in the Kansas Frontier Matrix interface — influencing **legibility**, **perception**, and **cognitive clarity**.  
These standards govern **UI themes**, **data visualizations**, and **map overlays**, ensuring that no user is excluded due to color-based communication barriers.

---

## 🧩 Core Principles

| Principle | Description | WCAG / ISO Reference |
|------------|--------------|----------------------|
| **Contrast Ratio** | Text vs. background ≥ 4.5 : 1 (3 : 1 for large text). | WCAG 1.4.3 |
| **Non-Color Cues** | Never use color alone to convey meaning. | WCAG 1.4.1 |
| **Palette Consistency** | Use standardized design tokens for brand and data. | ISO 9241-210 |
| **Dark Mode Parity** | Maintain equivalent contrast in dark and light themes. | WCAG 1.4.11 |
| **Cultural Sensitivity** | Palette choices vetted for cross-cultural neutrality. | FAIR+CARE Ethics |

---

## 🎨 Tokenized Palette

| Token | Purpose | Value (Hex) | Contrast Ratio vs BG (White `#FFFFFF`) |
|--------|----------|--------------|--------------------------------------|
| `color.primary` | Primary action / highlight | `#0053A0` | 8.5 : 1 |
| `color.secondary` | Secondary buttons / links | `#1565C0` | 6.7 : 1 |
| `color.accent` | Alerts / interactive hover | `#FFD54F` | 5.1 : 1 |
| `color.background` | Main page background | `#FAFAFA` | — |
| `color.text.primary` | Main text | `#212121` | 15.2 : 1 |
| `color.text.muted` | Secondary text | `#616161` | 7.4 : 1 |
| `color.error` | Error text / border | `#D32F2F` | 6.9 : 1 |
| `color.success` | Confirmation states | `#388E3C` | 6.1 : 1 |

---

## ⚙️ Accessibility Validation Workflow

| Tool | Validation Type | Output |
|-------|------------------|--------|
| **axe-core** | Automated contrast checks on DOM | `reports/self-validation/web/a11y_color.json` |
| **Lighthouse CI** | Audit of contrast ratios and color usage | `reports/ui/lighthouse_color.json` |
| **jest-axe** | React component contrast unit tests | `reports/ui/a11y_color_components.json` |
| **Color Contrast Analyzer (CCA)** | Manual spot-checking in UI screens | Council QA logs |

---

## 🧭 Data Visualization Guidelines

| Guideline | Description |
|------------|-------------|
| **Color-Blind Safety** | Use color-blind-safe palettes (e.g., Okabe-Ito set). |
| **Texture Alternatives** | Combine pattern fills and line styles with colors. |
| **Map Overlays** | Apply transparency < 60 % to preserve basemap context. |
| **Legend Labels** | Always include textual labels and icons for color zones. |

Example Palette (Okabe-Ito Reference):

```json
{
  "blue": "#0072B2",
  "orange": "#E69F00",
  "sky": "#56B4E9",
  "green": "#009E73",
  "yellow": "#F0E442",
  "pink": "#CC79A7",
  "grey": "#999999"
}
```

---

## 🧾 FAIR+CARE Alignment

| Principle | Implementation |
|------------|----------------|
| **Findable** | Tokens stored in central design schema (`web/src/theme/tokens.json`). |
| **Accessible** | Palette audited via automated contrast validation. |
| **Interoperable** | Applied across MapLibre, Recharts, Cesium visualizations. |
| **Reusable** | Shared in KFM Design System via NPM package. |
| **Ethics** | Colors reviewed for cultural and symbolic neutrality. |

---

## 🧪 Code Example (React)

```jsx
<Button
  style={{
    backgroundColor: "var(--color-primary)",
    color: "var(--color-text-primary)",
    outlineColor: "var(--a11y-focus-color)"
  }}
>
  Submit Data
</Button>
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Established color and contrast token standards, data-viz palette, and WCAG validation workflow. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Patterns Index](README.md) · [Next → Accessibility Index](../README.md)

</div>
