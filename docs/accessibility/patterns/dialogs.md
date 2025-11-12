---
title: "💬 Kansas Frontier Matrix — Accessible Dialogs & Modals (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/dialogs.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-dialogs-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💬 **Kansas Frontier Matrix — Accessible Dialogs & Modals**
`docs/accessibility/patterns/dialogs.md`

**Purpose:**  
Standardize **accessible dialog and modal interaction patterns** for all KFM interfaces — ensuring consistent keyboard handling, focus management, ARIA semantics, and inclusive tone across system prompts, consent dialogs, and narrative overlays.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Dialogs are used to convey critical information, capture user input, or confirm consent.  
This document defines FAIR+CARE-aligned modal behaviors — ensuring every interaction is **accessible**, **ethical**, and **reversible**.

**Dialog Types**
- Standard modal dialog  
- Alert / confirmation dialog  
- Non-blocking drawer / side modal  
- Multi-step or nested modal sequence  

---

## 🧩 Accessibility Principles

| Principle | Description | WCAG / Standard |
|------------|--------------|-----------------|
| **Focus Containment** | Focus remains within the modal until dismissed. | WCAG 2.4.3 |
| **Return Focus** | Focus restored to invoking control on close. | WAI-ARIA 1.2 |
| **Keyboard Shortcuts** | `Esc` closes modal; `Tab` / `Shift+Tab` cycle focus. | WCAG 2.1.1 |
| **ARIA Roles** | Use `role="dialog"` or `role="alertdialog"`. | WAI-ARIA 1.2 |
| **Labels** | `aria-labelledby` for title, `aria-describedby` for content. | WCAG 2.4.6 |
| **Motion Sensitivity** | Honor `prefers-reduced-motion` for transitions. | WCAG 2.3.3 |
| **Cultural Consent** | Modals collecting sensitive data must display FAIR+CARE consent context. | FAIR+CARE |

---

## 🧭 Example Implementation

```html
<div
  id="consent-dialog"
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-description"
  class="kfm-modal"
>
  <h2 id="dialog-title">Data Usage Consent</h2>
  <p id="dialog-description">
    By continuing, you consent to data processing under FAIR+CARE principles.
  </p>
  <button id="accept-consent">Agree</button>
  <button id="decline-consent">Decline</button>
</div>
```

**Behavioral Rules**
- Focus is trapped within `.kfm-modal` when open.  
- Pressing `Esc` closes the modal and returns focus to the triggering button.  
- Non-essential modals use `role="dialog"`; urgent confirmations use `role="alertdialog"`.  
- Use `aria-hidden="true"` on background elements while dialog is active.

---

## ⚙️ Keyboard & ARIA Matrix

| Key | Action | Description |
|-----|---------|-------------|
| `Tab` / `Shift+Tab` | Navigate interactive elements | Wrap focus inside modal |
| `Esc` | Close dialog | Restore focus to opener |
| `Enter` / `Space` | Confirm primary action | Executes associated function |
| `aria-modal` | Lock background interaction | Boolean `true` |
| `aria-labelledby` | Reference dialog title | Required for screen readers |
| `aria-describedby` | Reference supporting text | Strongly recommended |

---

## 🎨 Design Tokens

| Token | Usage | Example |
|--------|--------|---------|
| `a11y.focus.color` | Focus outline for dialog buttons | `#FFD54F` |
| `dialog.backdrop.opacity` | Background overlay opacity | `0.75` |
| `dialog.transition.speed` | Animation speed | `0.25s` |
| `dialog.zIndex` | Stack priority | `1100` |

---

## ⚖️ FAIR+CARE Alignment

| Principle | Implementation |
|------------|----------------|
| **Collective Benefit** | Consent dialogs educate users about ethical data handling. |
| **Authority to Control** | Data modals provide explicit opt-in/opt-out. |
| **Responsibility** | Modals include accessible audit trails for decision logs. |
| **Ethics** | Content reviewed for tone neutrality and emotional safety. |

---

## 🧪 Validation Workflow

| Tool | Function | Output |
|------|-----------|--------|
| **axe-core** | Dialog role/label validation | `reports/self-validation/web/a11y_dialogs.json` |
| **Lighthouse** | Accessibility and focus loop test | `reports/ui/lighthouse_dialogs.json` |
| **jest-axe** | React component test coverage | `reports/ui/jest_axe_dialogs.json` |
| **Manual Review** | NVDA/VoiceOver cycle tests | FAIR+CARE Council signoff |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Established accessible modal patterns with FAIR+CARE consent integration and ARIA updates. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Patterns Index](README.md) · [Next → Forms](forms.md)

</div>
