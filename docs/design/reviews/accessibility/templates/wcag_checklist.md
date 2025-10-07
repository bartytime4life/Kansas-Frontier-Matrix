<div align="center">

# ✅ Kansas Frontier Matrix — WCAG 2.1 AA Checklist  
`docs/design/reviews/accessibility/templates/wcag_checklist.md`

**Purpose:** Provide a reproducible verification matrix for auditing all KFM UI components and features against  
**WCAG 2.1 AA** success criteria. This checklist enforces MCP standards of **perceivable**, **operable**,  
**understandable**, and **robust** design reproducibility.

[![Accessibility](https://img.shields.io/badge/WCAG-2.1AA-yellow)](#wcag-sections)  
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey)](../../../../../LICENSE)

</div>

---

## 🧭 How to Use

1. Copy this file into the relevant review folder (e.g., `docs/design/reviews/accessibility/`).
2. Mark each criterion as ✅ Pass / ❌ Fail / ⚙️ Needs Review / N/A.
3. Link **evidence** — screenshots, code references, Lighthouse/Axe reports.
4. Commit the completed checklist with your component’s audit report.

---

## 🧩 Legend

| Symbol | Meaning |
|:-------:|----------|
| ✅ | Pass (Compliant) |
| ❌ | Fail (Non-compliant) |
| ⚙️ | Needs Review / Retest |
| N/A | Not Applicable to Component |

---

## 1️⃣ Perceivable

| # | WCAG Ref | Requirement | Result | Notes / Evidence |
|----|-----------|--------------|:------:|------------------|
| 1.1.1 | Non-text Content | All images/icons have alt text or `aria-label`. | | |
| 1.2.2 | Captions (Prerecorded) | Video/audio include synchronized captions. | | |
| 1.3.1 | Info & Relationships | Headings, lists, tables use semantic HTML. | | |
| 1.3.2 | Meaningful Sequence | Reading order follows DOM. | | |
| 1.4.1 | Use of Color | Color is not the only means of conveying meaning. | | |
| 1.4.3 | Contrast (Minimum) | Text contrast ≥ **4.5 : 1** (AA). | | |
| 1.4.11 | Non-Text Contrast | UI components ≥ **3 : 1** contrast. | | |
| 1.4.12 | Text Spacing | Spacing adjustable without layout break. | | |

---

## 2️⃣ Operable

| # | WCAG Ref | Requirement | Result | Notes / Evidence |
|----|-----------|--------------|:------:|------------------|
| 2.1.1 | Keyboard | All functionality accessible via keyboard. | | |
| 2.1.2 | No Keyboard Trap | User can tab in/out of all interactive regions. | | |
| 2.1.4 | Character Key Shortcuts | Can be remapped or disabled. | | |
| 2.2.1 | Timing Adjustable | Time limits extendable or adjustable. | | |
| 2.3.1 | Seizures & Flashes | No flashing > 3 times per second. | | |
| 2.4.1 | Bypass Blocks | Skip link to main content available. | | |
| 2.4.3 | Focus Order | Logical, matches visual flow. | | |
| 2.4.4 | Link Purpose (In Context) | Link text describes destination. | | |
| 2.4.7 | Focus Visible | Clear visual focus indicator. | | |

---

## 3️⃣ Understandable

| # | WCAG Ref | Requirement | Result | Notes / Evidence |
|----|-----------|--------------|:------:|------------------|
| 3.1.1 | Language of Page | `<html lang>` correctly declared. | | |
| 3.2.3 | Consistent Navigation | Repeated UI appears in same order. | | |
| 3.2.4 | Consistent Identification | Icons/controls consistent across pages. | | |
| 3.3.1 | Error Identification | Input errors visually + textually indicated. | | |
| 3.3.2 | Labels or Instructions | Inputs have visible labels. | | |
| 3.3.3 | Error Suggestions | Helpful text provided to correct input. | | |

---

## 4️⃣ Robust

| # | WCAG Ref | Requirement | Result | Notes / Evidence |
|----|-----------|--------------|:------:|------------------|
| 4.1.1 | Parsing | Valid HTML; unique IDs; no syntax errors. | | |
| 4.1.2 | Name, Role, Value | Accessible Name API exposes correct semantics. | | |
| 4.1.3 | Status Messages | Announced via `aria-live` or `role="status"`. | | |
| 4.1.4 | Orientation | App functions in portrait & landscape. | | |
| 4.1.5 | Reflow | Supports 320 px min width / zoom 400%. | | |

---

## 5️⃣ Additional KFM MCP Requirements

| # | Area | Requirement | Result | Notes |
|----|------|--------------|:------:|-------|
| KFM-A1 | Design Tokens | Uses `--kfm-color-*`, `--kfm-font-*` variables. | | |
| KFM-A2 | Theme Modes | Verified in light and dark themes. | | |
| KFM-A3 | Timeline Interaction | Timeline events keyboard accessible. | | |
| KFM-A4 | MapLibre Controls | All ARIA roles & focus order validated. | | |
| KFM-A5 | AI Assistant | Live responses announced via `aria-live="polite"`. | | |
| KFM-A6 | Motion & Animation | Honors `prefers-reduced-motion`. | | |

---

## 🧮 Scoring Formula (Optional)

```text
Compliance Score = (✅ / Total Criteria) × 100
AA Threshold = 90%+
AAA Threshold = 97%+
````

> MCP recommends **AA or higher** for production components and documentation linkage to CI evidence.

---

## 📊 Summary Scores

| Category               | Pass (%) | Notes |
| ---------------------- | -------- | ----- |
| Perceivable            |          |       |
| Operable               |          |       |
| Understandable         |          |       |
| Robust                 |          |       |
| **Overall Compliance** |          |       |

---

## ⚙️ Continuous Integration (WCAG Validation)

```yaml
# .github/workflows/a11y_wcag_validate.yml
on:
  pull_request:
    paths:
      - "docs/design/reviews/accessibility/templates/wcag_checklist.md"
      - "web/src/components/**"
jobs:
  wcag:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install accessibility tools
        run: npm i -g pa11y-ci axe-core-cli
      - name: Validate WCAG compliance
        run: pa11y-ci --config .pa11yci.wcag.json > wcag-report.json
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: wcag-compliance-report
          path: wcag-report.json
```

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
environment:
  os: "Windows 11"
  browser: "Chrome 130"
  viewport: "1440×900"
```

---

## 🪪 License

Released under **Creative Commons CC-BY 4.0**
© 2025 Kansas Frontier Matrix Design Collective

---

<div align="center">

### ✅ Kansas Frontier Matrix — Accessibility Compliance Framework

**Perceivable · Operable · Understandable · Robust**

</div>
