<div align="center">

# ✅ Kansas Frontier Matrix — WCAG 2.1 AA Checklist  
`docs/design/reviews/accessibility/templates/wcag_checklist.md`

**Purpose:** Provide a reproducible verification matrix for auditing all UI components and features in the KFM system against **WCAG 2.1 AA** success criteria.  
This checklist ensures every interface meets *perceivable, operable, understandable,* and *robust* standards required by the **Master Coder Protocol (MCP)**.

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#wcag-sections)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧭 How to Use
1. Copy this file into the relevant review folder (e.g., `docs/design/reviews/accessibility/`).
2. Mark each criterion as ✅ Pass / ❌ Fail / ⚙️ Needs Review / N/A.
3. Include evidence links (screenshots, code refs, Lighthouse report).
4. Commit alongside the component or feature being reviewed.

---

## 🧩 Legend
| Symbol | Meaning |
|---------|----------|
| ✅ | Pass (compliant) |
| ❌ | Fail (non-compliant) |
| ⚙️ | Needs Review / Retest |
| N/A | Not applicable to this component |

---

## 1️⃣ Perceivable

| # | WCAG 2.1 Ref | Requirement | Result | Notes / Evidence |
|---|---------------|--------------|---------|------------------|
| 1.1.1 | Non-text Content | All images/icons have alt text or `aria-label`. | | |
| 1.2.2 | Captions (Prerecorded) | Video/audio provide synchronized captions. | | |
| 1.3.1 | Info & Relationships | Headings, lists, tables use semantic HTML. | | |
| 1.3.2 | Meaningful Sequence | Reading order preserved in DOM. | | |
| 1.4.1 | Use of Color | Color not sole means of conveying information. | | |
| 1.4.3 | Contrast (Minimum) | Text contrast ≥ 4.5 : 1 (AA). | | |
| 1.4.11 | Non-Text Contrast | UI components ≥ 3 : 1 contrast. | | |
| 1.4.12 | Text Spacing | Text spacing adjustable w/out loss. | | |

---

## 2️⃣ Operable

| # | WCAG 2.1 Ref | Requirement | Result | Notes / Evidence |
|---|---------------|--------------|---------|------------------|
| 2.1.1 | Keyboard | All functionality keyboard accessible. | | |
| 2.1.2 | No Keyboard Trap | User can exit any region by keyboard. | | |
| 2.1.4 | Character Key Shortcuts | Remappable or disableable. | | |
| 2.2.1 | Timing Adjustable | Time limits adjustable / extendable. | | |
| 2.3.1 | Seizures & Flashes | No flashing > 3 times/sec. | | |
| 2.4.1 | Bypass Blocks | Skip links to main content exist. | | |
| 2.4.3 | Focus Order | Logical order matches visual order. | | |
| 2.4.4 | Link Purpose (In Context) | Link text describes destination. | | |
| 2.4.7 | Focus Visible | Focus indicator clearly visible. | | |

---

## 3️⃣ Understandable

| # | WCAG 2.1 Ref | Requirement | Result | Notes / Evidence |
|---|---------------|--------------|---------|------------------|
| 3.1.1 | Language of Page | `<html lang>` correctly defined. | | |
| 3.2.3 | Consistent Navigation | Repeated components appear in same order. | | |
| 3.2.4 | Consistent Identification | Icons/controls consistent across pages. | | |
| 3.3.1 | Error Identification | Input errors clearly indicated. | | |
| 3.3.2 | Labels or Instructions | Inputs include visible labels. | | |
| 3.3.3 | Error Suggestions | Helpful text shown to correct issues. | | |

---

## 4️⃣ Robust

| # | WCAG 2.1 Ref | Requirement | Result | Notes / Evidence |
|---|---------------|--------------|---------|------------------|
| 4.1.1 | Parsing | Valid HTML; no duplicate IDs. | | |
| 4.1.2 | Name, Role, Value | Accessible Name API exposes semantics. | | |
| 4.1.3 | Status Messages | Announced via `aria-live` / role="status". | | |
| 4.1.4 | Orientation (2.1) | Content not locked to one orientation. | | |
| 4.1.5 | Reflow (2.1) | Layout supports 320 px width (min). | | |

---

## 5️⃣ Additional KFM Requirements (MCP Extension)

| # | Area | Requirement | Result | Notes |
|----|------|--------------|---------|-------|
| KFM-A1 | Design Tokens | Uses `--kfm-color-*`, `--kfm-font-*`. | | |
| KFM-A2 | Theme Modes | Works in light/dark themes. | | |
| KFM-A3 | Timeline Interaction | Canvas events keyboard accessible. | | |
| KFM-A4 | MapLibre Controls | ARIA roles & focus order verified. | | |
| KFM-A5 | AI Assistant | Live responses announced politely. | | |

---

## 📊 Summary Scores

| Category | Pass (%) | Notes |
|-----------|-----------|-------|
| Perceivable | | |
| Operable | | |
| Understandable | | |
| Robust | | |
| **Overall Compliance** | | |

---

## 🧾 Metadata

```yaml
review_id: "wcag_checklist_{{ component }}_{{ version }}"
component: "{{ component_name }}"
version: "{{ version }}"
reviewed_by:
  - "@accessibility-team"
  - "@design-lead"
commit: "{{ GIT_COMMIT }}"
date: "{{ ISO8601_DATE }}"
wcag_level: "AA"
result: "pass | fail | partial"
tools:
  - "Axe Core v4.10"
  - "Lighthouse v12"
  - "Pa11y v7"
  - "NVDA 2023.3"


⸻

🪪 License

Released under Creative Commons CC-BY 4.0
© 2025 Kansas Frontier Matrix Design Collective

⸻



