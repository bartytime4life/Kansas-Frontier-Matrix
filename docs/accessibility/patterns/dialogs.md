---
title: "💬 Kansas Frontier Matrix — Accessible Dialogs & Modal Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/dialogs.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / FAIR+CARE Accessibility Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-patterns-dialogs-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 💬 **Kansas Frontier Matrix — Accessible Dialogs & Modal Patterns**
`docs/accessibility/patterns/dialogs.md`

**Purpose:**  
Define inclusive, accessible, and ethical dialog patterns — covering modals, confirmations, drawers, and inline overlays — for the **Kansas Frontier Matrix (KFM)**.  
Ensures compliance with **WCAG 2.1 AA**, **WAI-ARIA 1.2**, and **FAIR+CARE** communication ethics.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

Dialogs are **contextual overlays** that require user interaction — confirmation, additional input, or acknowledgement.  
Accessible dialogs in KFM:
- Use semantic roles (`role="dialog"` or `role="alertdialog"`)  
- Trap focus within the modal until dismissed  
- Include visible and programmatic titles and descriptions  
- Respect motion and assistive technology preferences  
- Maintain ethical tone under **FAIR+CARE** standards  

---

## 🗂️ Directory Context

```
docs/accessibility/patterns/
├── README.md
├── alerts.md
├── buttons.md
├── charts.md
├── dialogs.md            # ← This file
├── forms.md
├── map-controls.md
└── navigation.md
```

---

## 🧩 Dialog Types

| Type | Purpose | ARIA Role | Focus Behavior | Example |
|---|---|---|---|---|
| **Standard Modal** | Displays content that requires user interaction. | `role="dialog"` | Focus trapped inside. | Settings dialog. |
| **Alert Dialog** | Communicates urgent message requiring confirmation. | `role="alertdialog"` | Moves focus to modal immediately. | Delete confirmation. |
| **Drawer** | Slide-in panel containing contextual content. | `role="dialog"` | Focus contained until closed. | Data filter menu. |
| **Inline Dialog** | Small, anchored pop-up for inline actions. | `role="dialog"` | Focusable container with ESC to close. | Tooltip or mini-form. |

---

## ♿ Accessibility Standards

| Requirement | Description | Compliance |
|---|---|---|
| **Keyboard Navigation** | Tab/Shift+Tab cycle within modal; `Esc` closes it. | WCAG 2.1.1 / 2.1.2 |
| **Focus Trap** | Focus cannot leave dialog until dismissed. | WCAG 2.4.3 |
| **Title & Description** | Link heading via `aria-labelledby` and body via `aria-describedby`. | WCAG 1.3.1 |
| **No Background Scroll** | Prevent underlying content scroll (avoid focus loss). | ISO 9241-210 |
| **Dismissibility** | Always include a close button (`aria-label="Close dialog"`). | WCAG 2.1.1 |
| **Reduced Motion** | Respect `prefers-reduced-motion`; fade only, no slides if reduced. | WCAG 2.3.3 |

---

## 🧾 Example: Standard Modal

```tsx
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-description"
  className="fixed inset-0 flex items-center justify-center bg-black/50"
>
  <div className="bg-white rounded-lg p-6 max-w-md w-full shadow-lg focus:outline-none focus-visible:ring-4 focus-visible:ring-[#FFB300]">
    <h2 id="dialog-title" className="text-lg font-semibold text-primary">
      FAIR+CARE Data Use Policy
    </h2>
    <p id="dialog-description" className="text-sm mt-2 text-body">
      By continuing, you confirm you will handle datasets ethically and in accordance with FAIR+CARE principles.
    </p>
    <div className="mt-4 flex justify-end gap-2">
      <button className="btn-secondary" aria-label="Cancel">Cancel</button>
      <button className="btn-primary" aria-label="Agree to policy">Agree</button>
    </div>
  </div>
</div>
```

**Notes:**
- Focus automatically set to the first interactive element inside the dialog.  
- Background content hidden via `aria-hidden="true"`.  
- `Esc` key closes modal and restores focus to trigger button.

---

## ⚠️ Example: Alert Dialog (Confirmation)

```tsx
<div
  role="alertdialog"
  aria-modal="true"
  aria-labelledby="alert-title"
  aria-describedby="alert-desc"
  className="fixed inset-0 flex items-center justify-center bg-black/60"
>
  <div className="bg-white border-l-4 border-[#C62828] rounded-lg shadow-lg p-6 max-w-sm w-full">
    <h2 id="alert-title" className="text-lg font-bold text-[#C62828]">
      Confirm Data Deletion
    </h2>
    <p id="alert-desc" className="text-sm mt-2 text-body">
      This dataset contains cultural or sensitive material. Deleting it cannot be undone. Ensure tribal consent is archived before proceeding.
    </p>
    <div className="mt-4 flex justify-end gap-3">
      <button className="btn-secondary" aria-label="Cancel deletion">Cancel</button>
      <button className="btn-primary" aria-label="Confirm delete">Delete</button>
    </div>
  </div>
</div>
```

**FAIR+CARE Integration:**
- Language emphasizes **responsibility** and **consent awareness**.  
- Avoids coercive phrasing like “Are you sure you want to do this?” without context.

---

## 🧠 Ethical Tone Guidelines (FAIR+CARE)

| Principle | Dialog Design Guidance |
|---|---|
| **Collective Benefit** | Use dialogs to clarify or educate, not interrupt or manipulate. |
| **Authority to Control** | Always provide an explicit opt-out (e.g., Cancel). |
| **Responsibility** | Include ethical disclaimers for culturally sensitive actions. |
| **Ethics** | Avoid alarmist or coercive modal copy. Maintain neutrality. |

Example rewrite:  
- ❌ “Deleting will permanently erase all your work!”  
- ✅ “Deleting this dataset is permanent. Ensure you’ve archived copies before continuing.”

---

## 🎛️ Focus Management

```js
const modal = document.querySelector('[role="dialog"]');
const focusable = modal.querySelectorAll('a, button, input, textarea, select, [tabindex="0"]');
let first = focusable[0];
let last = focusable[focusable.length - 1];

modal.addEventListener('keydown', e => {
  if (e.key === 'Tab') {
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }
  if (e.key === 'Escape') modal.remove();
});
```

- Keeps focus inside modal while open.  
- `Esc` returns focus to trigger element when closed.

---

## 🔊 Screen Reader Best Practices

- **Provide clear titles** (`aria-labelledby`).  
- **Avoid empty regions** — ensure all descriptive text exists in DOM.  
- **Announce opening/closing** via polite `aria-live` region outside dialog.  
- **Set `aria-hidden="true"`** on the rest of the page while modal is open.  

---

## 🧩 Motion & Sensory Safety

| Pattern | Requirement |
|---|---|
| Animation Duration | ≤ 200ms, fades preferred over slides. |
| Flashing Elements | None above 3Hz. |
| Sound/Vibration | Disabled by default. |
| `prefers-reduced-motion` | Disable animations entirely when enabled. |

---

## ⚙️ Validation Pipelines

| Workflow | Purpose | Artifact |
|---|---|---|
| `storybook-a11y.yml` | Tests modal structure and focus trap. | `reports/ui/a11y_component_audits.json` |
| `accessibility_scan.yml` | Validates ARIA labeling and role usage. | `reports/self-validation/web/a11y_summary.json` |
| `design-tokens-validate.yml` | Ensures contrast for borders and focus rings. | `reports/ui/design-token-lint.json` |
| `faircare-visual-audit.yml` | Reviews dialog language for ethical tone. | `reports/faircare-visual-validation.json` |

---

## 📊 Quality Metrics

| Metric | Target | Verified By |
|---|---|---|
| **WCAG 2.1 AA Compliance** | 100% | Accessibility Audit |
| **Focus Trap Accuracy** | 100% | E2E Keyboard Testing |
| **Contrast Pass Rate** | 100% | Token Validation |
| **Motion Safety** | 100% | Accessibility Council |
| **FAIR+CARE Ethics Compliance** | ≥ 95% | Ethics Review |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | FAIR+CARE Accessibility Council | Introduced comprehensive accessible dialog pattern covering modals, alerts, drawers, and ethical interaction tone guidelines. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Part of the **Accessibility Pattern Library** · Master Coder Protocol v6.3 · FAIR+CARE Certified  
[⬅ Back to Patterns Index](README.md) · [Forms →](forms.md)

</div>