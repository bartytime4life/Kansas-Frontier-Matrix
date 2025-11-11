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

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

Buttons are among the most fundamental interaction elements in the **Kansas Frontier Matrix (KFM)** web application.  
They serve as triggers for navigation, state toggles, and data submission in **Focus Mode**, **Map Controls**, and **Governance Dashboards**.  
This guide defines inclusive button design rules, focusing on **keyboard operability**, **visual affordance**, **semantic clarity**, and **ethical tone**.

**Button Types Covered**
- Primary, secondary, and ghost buttons  
- Icon-only and composite buttons  
- Toggle buttons and segmented toggles  
- Disclosure and menu trigger buttons  

---

## 🧩 Accessibility Foundations

| Principle | Description | WCAG/Standard |
|---|---|---|
| **Keyboard Operable** | All buttons reachable by `Tab`, activatable with `Enter` or `Space`. | WCAG 2.1.1 |
| **Visible Focus** | Strong focus ring (≥3:1 contrast) appears when focused. | WCAG 2.4.7 |
| **Semantic Role** | Always `<button>` or `role="button"` if non-native element used. | WAI-ARIA 1.2 |
| **Descriptive Label** | Use clear text or `aria-label` for icon-only buttons. | WCAG 2.4.6 |
| **Color Independence** | Never rely solely on color to convey state. | WCAG 1.4.1 |
| **Reduced Motion** | Animated buttons honor `prefers-reduced-motion`. | WCAG 2.3.3 |
| **Inclusive Tone** | Button text avoids bias (“whitelist/blacklist”) or culturally harmful phrases. | FAIR+CARE Ethics |

---

## 🧭 Semantic Structure

```html
<button type="button" class="btn-primary">
  Save Changes
</button>

<!-- Toggle button -->
<button type="button" aria-pressed="false" class="btn-toggle">
  <span aria-hidden="true">🌞</span> Light Mode
</button>

<!-- Icon-only example -->
<button type="button" aria-label="Open navigation menu" class="btn-icon">
  <svg role="img" aria-hidden="true">...</svg>
</button>
```

**Implementation Rules**
- Always prefer the native `<button>` element over `<div>` or `<span>`.  
- If using custom elements, include `role="button"` and `tabindex="0"`.  
- Use `aria-pressed` for toggle buttons to indicate state.  
- Include visible text whenever possible for clarity and translation support.  

---

## 🎨 Design Tokens

| Token | Description | Value | Standard |
|---|---|---|---|
| `color.button.primary.bg` | Background color for primary button | `#0053A0` | WCAG 1.4.3 |
| `color.button.primary.text` | Text color | `#FFFFFF` | WCAG 1.4.3 |
| `focus.outline.width` | Focus outline width | `3px` | ISO 9241-210 |
| `focus.outline.color` | Outline color for focused state | `#FFD54F` | FAIR+CARE token |
| `motion.prefersReduced` | Disable hover scale for low-motion users | Boolean | WCAG 2.3 |
| `aria.label` | Default labeling convention | Contextual | WAI-ARIA 1.2 |

See also: [`../../design/tokens/accessibility-tokens.md`](../../design/tokens/accessibility-tokens.md)

---

## 🧠 Behavior Matrix

| Interaction | Expected Behavior | ARIA / Notes |
|---|---|---|
| `Tab` / `Shift+Tab` | Moves between focusable elements. | Maintain natural DOM order. |
| `Enter` / `Space` | Activates button action. | Triggers `click()` event. |
| `Esc` | Cancels or closes active dialogs. | Return focus to invoking button. |
| `aria-pressed` | Reflects toggle state (`true` or `false`). | Required for toggle buttons. |
| `aria-expanded` | Indicates visibility of linked content (dropdowns). | Optional; use when expanding UI. |
| `aria-controls` | References controlled region (e.g., menu, modal). | Example: `aria-controls="menu1"` |

---

## 🧾 Ethical & Inclusive Content Rules

| Area | Guideline |
|---|---|
| **Language** | Avoid exclusionary or idiomatic phrases (“crazy fast”, “whitelist”). Use neutral, descriptive text. |
| **Cultural Sensitivity** | Icons, emojis, and symbols must be context-checked (no cultural appropriation). |
| **Consent & Data Buttons** | For consent or personal data actions, include provenance explanation (`aria-describedby="data-policy"`). |
| **Emergency / Safety** | Use clear, calm language for alerts (“Check connection” vs. “Failure!”). |
| **Multilingual Support** | Buttons must support translation strings with `lang` attributes. |

---

## 🔁 Testing & Validation

| Tool | Scope | Output |
|---|---|---|
| axe-core | Static accessibility validation | `reports/self-validation/web/a11y_buttons.json` |
| Cypress | Keyboard operability & focus tests | `reports/ui/button_focus_tests.json` |
| Lighthouse | Color contrast and ARIA checks | `reports/ui/lighthouse_a11y.json` |
| Manual QA | Screen reader audit (NVDA/VoiceOver) | Council logs |

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|---|---|
| **Collective Benefit** | Button sets tested with multiple assistive technologies. |
| **Authority to Control** | User-triggered actions never auto-submit data without explicit consent. |
| **Responsibility** | Interaction logs monitored for accessibility regressions. |
| **Ethics** | Tone, color, and iconography validated through inclusive design review. |

---

## 🧩 Example: Focus Mode Toggle Button

```html
<button
  type="button"
  class="btn-focus"
  aria-pressed="false"
  aria-label="Enable Focus Mode"
  data-tracking="focus-toggle"
>
  <span class="icon">🧠</span>
  <span class="label">Focus Mode</span>
</button>
```

**Accessibility Notes**
- Uses `aria-pressed` to reflect toggle state in Focus Mode.  
- Includes emoji as decorative (`role="presentation"` if non-essential).  
- Provides visible label and tooltip for clarity.  
- Focus ring color and width derived from A11y design tokens.

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Created standardized accessible button patterns with ARIA specs, ethical tone guidance, and CI validation. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Part of the **Accessibility Pattern Library** · Master Coder Protocol v6.3 · FAIR+CARE Certified  
[⬅ Back to Patterns Index](README.md) · [Dialogs →](dialogs.md)

</div>
