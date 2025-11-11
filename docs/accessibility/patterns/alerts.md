---
title: "🚨 Kansas Frontier Matrix — Accessible Alerts & Live Regions (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/alerts.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / FAIR+CARE Accessibility Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-patterns-alerts-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🚨 **Kansas Frontier Matrix — Accessible Alerts & Live Regions**
`docs/accessibility/patterns/alerts.md`

**Purpose:**  
Define inclusive, non-intrusive patterns for **status**, **alert**, and **toast** messaging using **ARIA live regions** in the KFM platform. These patterns guarantee compliance with **WCAG 2.1 AA**, protect against motion/sound overload, and align with **FAIR+CARE** ethical communication.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

Alerts and status messages provide **immediate, accessible feedback** (success, info, warning, error) without breaking user flow.  
This pattern standardizes:
- **ARIA roles** and **live region** usage (`role="alert"`, `aria-live`, `role="status"`)  
- **Keyboard focus** and **escape** handling  
- **Motion and sound constraints** for sensory safety  
- **FAIR+CARE tone** for respectful, non-coercive messaging

---

## 🗂️ Directory Context

```
docs/accessibility/patterns/
├── README.md
├── buttons.md
├── charts.md
├── dialogs.md
├── forms.md
├── map-controls.md
├── navigation.md
└── alerts.md                # ← This file
```

---

## 🧩 Alert Types & ARIA Roles

| Type | Purpose | ARIA / Live Region | Keyboard | Example Use |
|---|---|---|---|---|
| **Status (Polite)** | Non-urgent updates that shouldn’t interrupt. | `role="status"` or `aria-live="polite"` | No focus shift | “Saved draft.” |
| **Alert (Assertive)** | Urgent messages requiring attention. | `role="alert"` or `aria-live="assertive"` | Move focus **only** if blocking | “Form error—Title is required.” |
| **Toast (Polite)** | Temporary, dismissible notification. | `aria-live="polite"` + close button | `Esc` closes; focus stays | “Dataset added to collection.” |
| **Progress** | Long-running process indication. | `role="status"` + `aria-busy="true"` | No focus shift | “Uploading… 65%” |

> ⚠️ Use **assertive** sparingly. Overuse causes screen-reader noise and cognitive load (WCAG 2.2, 3.2).

---

## ♿ Accessibility Requirements

| Requirement | Rule | Standard |
|---|---|---|
| **Announceability** | Use `role="status"` (polite) or `role="alert"` (assertive). Avoid duplicating announcements. | WCAG 4.1.3 |
| **Dismissal** | Toasts include close button; `Esc` dismisses. | WCAG 2.1.1 / 2.1.2 |
| **Focus Management** | Do **not** steal focus for non-blocking alerts. For blocking errors, return focus to the **first invalid field**. | WCAG 3.3.x |
| **Color Independence** | Do not rely on color alone to signal severity; include icon + text. | WCAG 1.4.1 |
| **Contrast** | Text and icon contrast ≥ 4.5:1; focus ring ≥ 3:1. | WCAG 1.4.3 / 2.4.7 |
| **Motion/Sound** | Respect `prefers-reduced-motion`; no auto-sounds. | WCAG 2.3.3 |

---

## 🎨 Design Tokens (A11y-first)

| Token | Value | Use |
|---|---|---|
| `color.alert.success.bg` | `#E8F5E9` | Success background |
| `color.alert.info.bg` | `#E3F2FD` | Info background |
| `color.alert.warning.bg` | `#FFF8E1` | Warning background |
| `color.alert.error.bg` | `#FFEBEE` | Error background |
| `color.alert.text` | `#1A1A1A` | Message text |
| `focus.outline.color` | `#FFB300` | Dismiss button focus ring |

Tokens validated via `design-tokens-validate.yml` to ensure WCAG contrast.

---

## 🧾 Patterns & Code Examples

### 1) **Polite Status Message (Non-blocking)**

```tsx
<div role="status" aria-live="polite" className="sr-only" id="save-status"></div>

<script>
// Example update
document.getElementById('save-status').textContent = 'Draft saved';
</script>
```

- Invisible to sighted users, announced to screen readers.
- Do not shift focus.

---

### 2) **Assertive Error Alert (Form Validation)**

```tsx
<div
  role="alert"
  aria-live="assertive"
  className="bg-[#FFEBEE] border border-[#C62828] text-[#1A1A1A] rounded p-3 mt-2"
  id="form-errors"
>
  <p className="font-semibold">Please fix 1 error</p>
  <ul className="list-disc ml-5">
    <li><a href="#title" className="underline">Title is required</a></li>
  </ul>
</div>

// Return focus example (on submit fail)
const firstInvalid = document.querySelector('[aria-invalid="true"]');
if (firstInvalid) firstInvalid.focus();
```

- Announces immediately; provides actionable link to the first invalid control.
- Do not spam multiple assertive alerts.

---

### 3) **Accessible Toast (Dismissible, Polite)**

```tsx
<div
  className="fixed bottom-4 right-4 bg-white border border-neutral-200 rounded shadow-lg p-3"
  role="region" aria-label="Notification"
>
  <p aria-live="polite">Dataset added to your collection.</p>
  <button
    className="ml-2 btn-icon"
    aria-label="Dismiss notification"
    onclick="closeToast()"
  >✕</button>
</div>
```

- Keyboard dismiss via button and `Esc`.
- Keep on-screen ≥ 5s; do **not** auto-dismiss if it contains critical info.

---

### 4) **Progress / Busy State**

```tsx
<div role="status" aria-live="polite" aria-busy="true" id="upload-status">
  Uploading… 65%
</div>
```

- Avoid infinite spinners without text; always include a textual state.

---

## 🧠 FAIR+CARE Ethical Tone

| Principle | Alert Copy Guidance |
|---|---|
| **Collective Benefit** | Emphasize help and clarity (“Please review the fields below”). |
| **Authority to Control** | Never coerce; provide clear, optional actions. |
| **Responsibility** | Be concise, specific, and calm—no alarmist language. |
| **Ethics** | Avoid stigmatizing phrasing (e.g., “invalid person”). Reference **data**, not **people**. |

Example rewrite:  
- ❌ “You failed to provide a name.”  
- ✅ “Name is required—please enter your name to continue.”

---

## 🔍 Testing Checklist (Excerpt)

- Live region announces once (no duplicate updates).  
- `Esc` closes any toast; focus remains stable.  
- Contrast ≥ 4.5:1 for text and icons; ≥ 3:1 for focus ring.  
- Error alerts link to the **first** invalid field and set focus there.  
- No motion or audio auto-play; `prefers-reduced-motion` respected.  

See also: `docs/accessibility/checklists/focus-navigation.md`.

---

## ⚙️ CI/CD Validation

| Workflow | Purpose | Artifact |
|---|---|---|
| `accessibility_scan.yml` | Axe/Lighthouse checks for ARIA roles and live regions. | `reports/self-validation/web/a11y_summary.json` |
| `storybook-a11y.yml` | Component snapshot tests (toast, alert, status). | `reports/ui/a11y_component_audits.json` |
| `design-tokens-validate.yml` | Contrast validation for alert colors. | `reports/ui/design-token-lint.json` |
| `faircare-visual-audit.yml` | Tone and ethics validation of alert copy. | `reports/faircare-visual-validation.json` |

---

## 📊 Quality Metrics

| Metric | Target | Verified By |
|---|---|---|
| **WCAG 2.1 AA Compliance** | 100% | CI + Manual Audit |
| **Duplicate Announcements** | 0 | Automated Tests |
| **Contrast Pass Rate** | 100% | Token Linter |
| **Motion Safety** | 100% | Accessibility Council |
| **FAIR+CARE Tone Compliance** | ≥ 95% | Ethics Review |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | FAIR+CARE Accessibility Council | Introduced standardized alert and live-region patterns with WCAG/ARIA requirements, motion safety rules, and FAIR+CARE tone guidance. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Part of the **Accessibility Pattern Library** · Master Coder Protocol v6.3 · FAIR+CARE Certified  
[⬅ Back to Patterns Index](README.md) · [Dialogs →](dialogs.md)

</div>