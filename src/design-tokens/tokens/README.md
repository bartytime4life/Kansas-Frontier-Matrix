---
title: "🎨 Kansas Frontier Matrix — Design Token Library (Foundations · Semantic · Accessibility)"
path: "src/design-tokens/tokens/README.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/src-design-tokens-tokens-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Design Token Library**
`src/design-tokens/tokens/README.md`

**Purpose:**  
Define and maintain the **core token sets** (colors, typography, spacing, motion, elevation, accessibility) that power the Kansas Frontier Matrix (KFM) visual language.  
This directory implements **FAIR+CARE-certified**, **WCAG 2.1 AA**, and **ISO 50001**-aligned standards for accessible, sustainable design systems.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../docs/README.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-A11y%20Certified-orange)](../../../docs/standards/faircare.md)
[![Status: Active](https://img.shields.io/badge/Status-Library%20Stable-success)]()

</div>

---

## 📘 Overview

The **Design Token Library** stores **machine-readable style variables** in JSON format for consistent UI rendering across web, data visualization, and AI-generated interfaces.  
These tokens are compiled into CSS, SCSS, and JS exports to ensure visual integrity, accessibility, and sustainability throughout KFM’s platform.

All tokens are **versioned**, **validated**, and **governed** under:
- `design-token-validate.yml` (schema + color contrast)
- `ui-accessibility.yml` (WCAG 2.1 AA + ARIA)
- `telemetry-export.yml` (sustainability and reuse metrics)

---

## 🗂️ Directory Layout

```plaintext
src/design-tokens/tokens/
├── README.md                 # This file — Token Library Overview
│
├── colors.json               # Core and semantic color palette
├── typography.json           # Font families, weights, and sizes
├── spacing.json              # Grid, margins, and padding scales
├── elevation.json            # Shadows, surfaces, and z-index tokens
├── motion.json               # Animation durations and easing tokens
└── accessibility.json        # Focus, contrast, ARIA, and assistive tokens
```

---

## 🧱 Foundational Tokens

### 🎨 Colors

| Token | Description | Example |
|--------|--------------|----------|
| `color.brand.primary` | KFM primary brand color | `#003366` |
| `color.brand.secondary` | Secondary highlight color | `#f2a900` |
| `color.surface.default` | Default background | `#ffffff` |
| `color.text.primary` | Main body text | `#1a1a1a` |
| `color.text.invert` | Text for dark backgrounds | `#ffffff` |

**Contrast Targets:**  
All color pairs meet WCAG 2.1 AA minimum ratio of **4.5:1** for normal text and **3:1** for large text.

---

### 🖋 Typography

| Token | Purpose | Value |
|--------|----------|--------|
| `font.family.base` | Primary sans-serif stack | `"Inter", "Helvetica", "Arial", sans-serif` |
| `font.family.serif` | Serif type for documents | `"Source Serif Pro", Georgia, serif` |
| `font.size.base` | Root text size | `16px` |
| `font.weight.medium` | Default medium weight | `500` |
| `line.height.default` | Body line height | `1.5` |

---

### 📏 Spacing & Layout

| Token | Unit | Description |
|--------|------|-------------|
| `spacing.xs` | `0.25rem` | Extra small spacing |
| `spacing.sm` | `0.5rem` | Small spacing |
| `spacing.md` | `1rem` | Medium spacing (base grid) |
| `spacing.lg` | `2rem` | Large spacing |
| `spacing.xl` | `4rem` | Extra large spacing |

All spacing tokens follow a **4-point system** for scalable layouts.

---

### 🌫 Elevation & Shadows

| Token | Depth | Value |
|--------|-------|--------|
| `shadow.sm` | Surface hover | `0 1px 2px rgba(0,0,0,0.1)` |
| `shadow.md` | Card / panel | `0 4px 6px rgba(0,0,0,0.15)` |
| `shadow.lg` | Overlay / modal | `0 8px 16px rgba(0,0,0,0.25)` |
| `z-index.modal` | Layer priority | `9999` |

---

### ⏱ Motion & Transitions

| Token | Description | Example |
|--------|--------------|----------|
| `motion.duration.short` | Default interaction timing | `150ms` |
| `motion.duration.medium` | Hover/entry animations | `300ms` |
| `motion.easing.standard` | Default easing function | `cubic-bezier(0.4, 0, 0.2, 1)` |
| `motion.easing.decelerate` | Gentle exit animation | `cubic-bezier(0, 0, 0.2, 1)` |

> ⚙️ Motion tokens follow **Reduced Motion Preferences** for accessibility; motion-heavy elements are disabled when `prefers-reduced-motion` is true.

---

### ♿ Accessibility Tokens

| Token | Description | Example |
|--------|-------------|----------|
| `focus.outline.color` | Outline for focused elements | `#1e90ff` |
| `focus.outline.width` | Outline thickness | `3px` |
| `aria.region.label` | Landmark roles | `"main"`, `"navigation"`, `"contentinfo"` |
| `contrast.min.ratio` | Minimum contrast target | `4.5:1` |

Accessibility tokens align with:
- **WCAG 2.1 AA**
- **Section 508**
- **ISO 9241-171 (Accessibility of ICT Products)**

---

## 🧮 Example JSON Token File (`colors.json`)

```json
{
  "color": {
    "brand": {
      "primary": "#003366",
      "secondary": "#f2a900"
    },
    "text": {
      "primary": "#1a1a1a",
      "secondary": "#555555",
      "invert": "#ffffff"
    },
    "background": {
      "default": "#ffffff",
      "alt": "#f9f9f9"
    },
    "status": {
      "success": "#28a745",
      "warning": "#ffcc00",
      "error": "#e63946",
      "info": "#007bff"
    }
  }
}
```

---

## ⚙️ Validation & Governance

| Workflow | Purpose | Output |
|-----------|----------|--------|
| `design-token-validate.yml` | Checks schema compliance and contrast ratios | `reports/self-validation/ui/design_tokens.json` |
| `ui-accessibility.yml` | Ensures WCAG 2.1 compliance | `reports/self-validation/ui/a11y_summary.json` |
| `telemetry-export.yml` | Publishes sustainability metrics | `releases/v10.0.0/focus-telemetry.json` |

Governance metadata stored in:
```
docs/reports/telemetry/governance_scorecard.json
```

---

## 🧠 FAIR+CARE Design Matrix

| Principle | Implementation |
|------------|----------------|
| **Findable** | Tokens indexed in manifest and governance ledger |
| **Accessible** | JSON + CSS exports publicly documented |
| **Interoperable** | Supported across React, Figma, and design tools |
| **Reusable** | Licensed under CC-BY 4.0 and version controlled |
| **CARE** | Color, motion, and typography reviewed for inclusivity |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | `@kfm-design-system` | Published v10 unified design token library — added sustainability telemetry and accessibility schema alignment. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Governed under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Design Tokens Index](../README.md) · [Accessibility Standards](../../../docs/standards/ui_accessibility.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

