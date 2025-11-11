---
title: "🎨 Kansas Frontier Matrix — Accessibility Design Tokens (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/tokens.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/a11y-tokens-v1.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Accessibility Design Tokens**
`docs/accessibility/tokens.md`

**Purpose:**  
Define reusable **accessibility and inclusive design tokens** used across the **Kansas Frontier Matrix (KFM)** web application and documentation — ensuring consistent, measurable compliance with **WCAG 2.1 AA**, **FAIR+CARE**, and **ISO 9241-210** design standards.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../standards/faircare.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

Accessibility design tokens are the **atomic elements** of the KFM design system.  
They ensure consistent user experience across all UI components, including **Focus Mode**, **Timeline**, **Map**, and **Governance Dashboard**.  
Tokens define **contrast ratios**, **motion preferences**, **spacing**, and **interaction states**, enabling designers and developers to build accessible interfaces programmatically.

This document complements the global token set in `docs/design/tokens/` by focusing solely on **a11y-specific properties** validated by the **FAIR+CARE Council**.

---

## 🗂️ Token Categories

```
docs/accessibility/
├── README.md
├── tokens.md                     # ← This file
├── patterns/                     # Accessible component guidelines
└── audits/                       # Reports, checklists, and ethics reviews
```

Accessibility tokens are grouped by purpose:

| Category | Description |
|---|---|
| **Color Tokens** | Guarantee legible contrast ratios and visual clarity. |
| **Typography Tokens** | Maintain readable text hierarchy across devices. |
| **Motion Tokens** | Control animation accessibility and user preferences. |
| **Focus Tokens** | Define visible outlines and state transitions. |
| **ARIA Tokens** | Standardize labeling and semantic descriptors. |
| **Ethical Tokens** | Represent inclusivity, consent, and provenance in visual design. |

---

## 🎨 Color Tokens

| Token | Example Value | Description | WCAG Ratio |
|---|---|---|---|
| `color.text.primary` | `#1A1A1A` | Default text color for high contrast themes. | 15.0:1 |
| `color.text.secondary` | `#404040` | Subdued text used for metadata and labels. | 9.0:1 |
| `color.text.inverse` | `#FFFFFF` | Text on dark backgrounds. | 12.0:1 |
| `color.bg.surface` | `#FFFFFF` | Main background surface. | N/A |
| `color.bg.alt` | `#F6F6F6` | Alternate background for alternating rows. | N/A |
| `color.button.primary.bg` | `#0053A0` | Primary action button background. | 4.6:1 |
| `color.button.primary.text` | `#FFFFFF` | Text for primary buttons. | 4.6:1 |
| `color.link.default` | `#004FC6` | Standard link color (underlined). | 5.2:1 |
| `color.link.focus` | `#FFCA28` | Highlight color for active or focused link. | 7.1:1 |
| `color.error` | `#C62828` | Error state (meets 4.5:1 contrast minimum). | 5.0:1 |

---

## 🔠 Typography Tokens

| Token | Value | Description |
|---|---|---|
| `font.base.size` | `16px` | Default base font for readability. |
| `font.scale.ratio` | `1.25` | Modular scale increment (Minor Third). |
| `font.lineheight.normal` | `1.6` | Balanced for large paragraph content. |
| `font.weight.bold` | `700` | Bold weight for headings and labels. |
| `text.spacing.letter` | `0.02em` | Minimum letter spacing for legibility. |
| `text.decoration.links` | `underline` | Reinforces visual identification. |
| `text.align.readableWidth` | `70ch` | Line length limit for long-form readability. |

---

## 💫 Motion Tokens

| Token | Value | Behavior |
|---|---|---|
| `motion.duration.short` | `100ms` | Used for small visual cues (button hover). |
| `motion.duration.medium` | `250ms` | Standard transitions (modals, overlays). |
| `motion.duration.long` | `500ms` | Large transitions (page fade). |
| `motion.easing.default` | `ease-in-out` | Smooth animation easing curve. |
| `motion.prefersReduced` | `true` (system dependent) | Disables motion for sensitive users. |

> ⚠️ **Note:** Motion tokens dynamically adapt to the `prefers-reduced-motion` media query, ensuring comfort for users with vestibular disorders.

---

## 🔲 Focus Tokens

| Token | Value | Purpose |
|---|---|---|
| `focus.outline.color` | `#FFB300` | Default yellow outline for keyboard focus. |
| `focus.outline.width` | `3px` | Standard focus ring thickness. |
| `focus.outline.offset` | `2px` | Margin between element and outline. |
| `focus.transition.duration` | `100ms` | Time for focus ring fade-in/out. |
| `focus.shadow.color` | `rgba(255,179,0,0.25)` | Glow around focused elements. |

---

## 🔖 ARIA Tokens

| Token | Description | Example |
|---|---|---|
| `aria.label.primaryNav` | Label for main site navigation. | `"Main navigation"` |
| `aria.label.focusToggle` | Describes Focus Mode activation control. | `"Enable Focus Mode"` |
| `aria.status.loading` | Announces content loading state. | `"Loading timeline data"` |
| `aria.status.ready` | Announces component readiness. | `"Timeline loaded"` |
| `aria.live.polite` | Defines polite live regions for non-critical updates. | `"map status update"` |
| `aria.live.assertive` | Defines assertive live regions for urgent messages. | `"Error loading data"` |

---

## 🧭 Ethical Tokens (FAIR+CARE Integration)

| Token | Function | Example Value | Standard |
|---|---|---|---|
| `care.provenance.chip.color` | Provenance badge color (high visibility). | `#FFCA28` | FAIR+CARE |
| `care.consent.indicator.icon` | Symbol for user-consented data. | `"🟢"` | FAIR+CARE |
| `care.ethics.alert.bg` | Background color for sensitive content warning. | `#FFF3E0` | ISO 26000 |
| `care.inclusive.iconset` | Culturally neutral icon pack flag. | `true` | CARE C3 |
| `care.altText.default` | Standardized description format. | `"Image of [subject]"` | WCAG 1.1.1 |

---

## ⚙️ Validation & CI Integration

Design tokens are validated automatically through CI workflows:

| Workflow | Purpose | Output Artifact |
|---|---|---|
| `color-contrast.yml` | Ensures color tokens meet WCAG 2.1 AA ratios. | `reports/ui/color-contrast.json` |
| `accessibility_scan.yml` | Scans focus, motion, and ARIA properties in components. | `reports/self-validation/web/a11y_summary.json` |
| `faircare-audit.yml` | Verifies ethical tokens for provenance and inclusivity. | `reports/faircare-validation.json` |
| `build-and-deploy.yml` | Bundles validated tokens into release manifest. | `releases/v10.0.0/manifest.zip` |

---

## 🧾 Example Usage (React)

```tsx
<button
  className="focus:outline focus:outline-[var(--focus-outline-color)] 
             focus:outline-offset-[var(--focus-outline-offset)] 
             focus:shadow-[var(--focus-shadow-color)]"
  aria-label="Activate Focus Mode"
>
  Enable Focus Mode
</button>
```

**CSS Variable Mapping**
```css
:root {
  --focus-outline-color: #FFB300;
  --focus-outline-offset: 2px;
  --focus-shadow-color: rgba(255,179,0,0.25);
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Established standardized accessibility tokens for color, typography, focus, motion, and ethics; integrated with CI validation and FAIR+CARE governance. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Validated by **FAIR+CARE Council**  
[⬅ Back to Accessibility Index](README.md) · [Design Tokens →](../design/tokens/accessibility-tokens.md)

</div>