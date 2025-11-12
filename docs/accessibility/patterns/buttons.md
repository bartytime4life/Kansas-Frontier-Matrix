---
title: "🔘 Kansas Frontier Matrix — Accessible Buttons & Toggles (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/buttons.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-buttons-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🔘 **Kansas Frontier Matrix — Accessible Buttons & Toggles**
`docs/accessibility/patterns/buttons.md`

**Purpose:**  
Define keyboard, ARIA, and inclusive design patterns for **buttons, toggles, and interactive controls** in the KFM platform, ensuring compliance with **WCAG 2.1 AA**, **ISO 9241-210**, and **FAIR+CARE** ethical design principles.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Buttons are among the most fundamental interaction elements in the **Kansas Frontier Matrix (KFM)** web application.  
They serve as triggers for navigation, state toggles, and data submission across **Focus Mode**, **Map Controls**, and **Governance Dashboards**.  
This guide defines inclusive button design rules emphasizing **keyboard operability**, **semantic clarity**, **visual affordance**, and **ethical tone**.

**Button Types Covered**
- Primary, secondary, and ghost buttons  
- Icon-only and composite buttons  
- Toggle and segmented toggles  
- Disclosure and menu trigger buttons  

---

## 🧩 Accessibility Foundations

| Principle | Description | WCAG/Standard |
|------------|--------------|----------------|
| **Keyboard Operable** | Reachable via `Tab`, activatable with `Enter` or `Space`. | WCAG 2.1.1 |
| **Visible Focus** | Strong focus ring (≥3:1 contrast). | WCAG 2.4.7 |
| **Semantic Role** | Always `<button>` or `role="button"`. | WAI-ARIA 1.2 |
| **Descriptive Label** | Use text or `aria-label` for icon-only buttons. | WCAG 2.4.6 |
| **Color Independence** | Avoid using color alone for state. | WCAG 1.4.1 |
| **Reduced Motion** | Honor `prefers-reduced-motion`. | WCAG 2.3.3 |
| **Inclusive Tone** | Avoid harmful or biased phrasing. | FAIR+CARE Ethics |

---

## 🧭 Semantic Structure

```html
<!-- Primary Action -->
<button type="button" class="btn-primary">
  Save Changes
</button>

<!-- Toggle Button -->
<button type="button" aria-pressed="false" class="btn-toggle">
  <span aria-hidden="true">🌞</span> Light Mode
</button>

<!-- Icon-only Example -->
<button type="button" aria-label="Open navigation menu" class="btn-icon">
  <svg role="img" aria-hidden="true">...</svg>
</button>
```

**Implementation Rules**
- Always prefer native `<button>` over `<div>`/`<span>`.  
- Custom elements must include `role="button"` and `tabindex="0"`.  
- Toggle buttons require `aria-pressed`.  
- Provide visible labels for screen readers and translation.  

---

## 🎨 Design Tokens

| Token | Description | Example Value | Reference |
|--------|--------------|----------------|------------|
| `color.button.primary.bg` | Primary button background | `#0053A0` | WCAG 1.4.3 |
| `color.button.primary.text` | Button text color | `#FFFFFF` | WCAG 1.4.3 |
| `focus.outline.width` | Outline thickness | `3px` | ISO 9241-210 |
| `focus.outline.color` | Focus indicator color | `#FFD54F` | FAIR+CARE token |
| `motion.prefersReduced` | Motion setting for animation toggle | Boolean | WCAG 2.3 |
| `aria.label` | Default ARIA labeling rule | Contextual | WAI-ARIA 1.2 |

See [`../../design/tokens/accessibility-tokens.md`](../../design/tokens/accessibility-tokens.md).

---

## 🧠 Behavior Matrix

| Interaction | Expected Behavior | ARIA / Notes |
|--------------|------------------|---------------|
| `Tab` / `Shift+Tab` | Navigate focus sequence. | Maintain DOM order. |
| `Enter` / `Space` | Activate button. | Trigger `click()` event. |
| `Esc` | Cancel / Close context. | Return focus to invoking control. |
| `aria-pressed` | Reflect toggle state. | Boolean `true/false`. |
| `aria-expanded` | Show/Hide state for menus. | Used with disclosure buttons. |
| `aria-controls` | Link to controlled element. | `aria-controls="menu1"`. |

---

## 🧾 Ethical & Inclusive Content Rules

| Category | Guideline |
|-----------|------------|
| **Language** | Replace idioms (“crazy fast”) with neutral terms (“extremely fast”). |
| **Cultural Sensitivity** | Avoid imagery implying hierarchy, domination, or cultural misuse. |
| **Consent & Data** | Use `aria-describedby="policy-id"` for consent actions. |
| **Safety Contexts** | Use calm, factual tone (“Check connection”). |
| **Multilingual Support** | Buttons support `lang` attributes and translation strings. |

---

## 🔁 Testing & Validation

| Tool | Validation Scope | Output |
|-------|------------------|---------|
| **axe-core** | Accessibility violations, ARIA roles | `reports/self-validation/web/a11y_buttons.json` |
| **Cypress** | Keyboard focus & state transitions | `reports/ui/button_focus_tests.json` |
| **Lighthouse** | Color contrast and semantic review | `reports/ui/lighthouse_a11y.json` |
| **Manual Audit** | NVDA, VoiceOver, keyboard-only tests | FAIR+CARE logs |

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|------------|----------------|
| **Collective Benefit** | Button sets tested on multiple devices and assistive techs. |
| **Authority to Control** | Buttons never auto-submit or track without consent. |
| **Responsibility** | A11y telemetry logs button focus and interaction coverage. |
| **Ethics** | Color and language reviewed for inclusivity per release cycle. |

---

## 🧩 Focus Mode Toggle Example

```html
<button
  type="button"
  class="btn-focus"
  aria-pressed="false"
  aria-label="Enable Focus Mode"
  data-telemetry="focus-toggle"
>
  <span class="icon" aria-hidden="true">🧠</span>
  <span class="label">Focus Mode</span>
</button>
```

**Accessibility Notes**
- `aria-pressed` tracks toggle state visually and programmatically.  
- Emoji marked `aria-hidden` to avoid duplication in SR output.  
- Focus outline and background tokenized per design system.  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Upgraded button specification; integrated motion settings, tone ethics, and telemetry hooks. |

---

<div align="center">

© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3  
**FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  

[⬅ Back to Patterns Index](README.md) · [Next → Dialogs](dialogs.md)

</div>
