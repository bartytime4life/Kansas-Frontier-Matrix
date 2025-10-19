<div align="center">

# ✅ Kansas Frontier Matrix — **WCAG 2.1 AA Checklist (Tier-Ω+∞ Certified)**  
`docs/design/reviews/accessibility/templates/wcag_checklist.md`

**Mission:** Provide a **governance-grade, MCP-DL v6.3+ compliant** verification matrix for auditing every KFM UI component and feature against **WCAG 2.1 AA** (with **WCAG 3.0 readiness**).  
This template enforces **Perceivable · Operable · Understandable · Robust (POUR)** design — with CI gates, evidence capture, FAIR/CARE metadata, and observability.

[![WCAG 2.1 AA | 3.0 ready](https://img.shields.io/badge/WCAG-2.1%20AA%20%7C%203.0%20ready-yellow)](#wcag-sections)  
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../standards/documentation.md)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../../style-guide.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

```yaml
---
title: "KFM — WCAG 2.1 AA Checklist"
document_type: "Accessibility Checklist"
version: "v3.0.0"
last_updated: "2025-11-11"
created: "2023-10-01"
owners: ["@kfm-accessibility","@kfm-design","@kfm-web"]
reviewed_by: ["@kfm-design-council","@kfm-ethics"]
status: "Template"
maturity: "Production"
license: "CC-BY-4.0"
tags: ["wcag","checklist","aria","keyboard","screen-reader","contrast","motion","captions","gestures","i18n","ci","observability","fair","care"]
alignment:
  - MCP-DL v6.3
  - WCAG 2.1 AA
  - WCAG 3.0 readiness
  - Section 508
  - EN 301 549
  - WAI-ARIA 1.2
  - ISO 9241-171
validation:
  ci_enforced: true
  schema_required: true
  evidence_required: true
observability:
  endpoint: "https://metrics.kfm.ai/a11y/wcag"
  metrics_exported: ["wcag_pass_rate", "axe_violations", "route_a11y_score", "gai_score"]
---
```

---

## 🧭 How to Use

1. Copy this file into your feature’s review folder (e.g., `docs/design/reviews/accessibility/feature-name/`).  
2. For each criterion, select **✅ Pass / ❌ Fail / ⚙️ Needs Review / N/A** and link **evidence** (screenshots, code, reports).  
3. Commit the checklist alongside the **component audit** and **CI artifacts**.  
4. CI must pass all blocking gates before merge.

---

## 🧩 Legend

| Symbol | Meaning |
|:--:|--|
| ✅ | Pass (Compliant) |
| ❌ | Fail (Non-compliant) |
| ⚙️ | Needs Review / Retest |
| N/A | Not Applicable |

---

## 1️⃣ Perceivable

| # | WCAG Ref | Requirement | Result | Notes / Evidence |
|--:|:--|:--|:--:|:--|
| 1.1.1 | Non-text Content | Images/icons have alt text or are `aria-hidden` if decorative. |  |  |
| 1.2.2 | Captions (Prerecorded) | Synchronized captions provided for video/audio. |  |  |
| 1.2.5 | Audio Description (Prerecorded) | Audio description or transcript exists. |  |  |
| 1.3.1 | Info & Relationships | Headings, lists, tables are semantic; labels associate to inputs. |  |  |
| 1.3.2 | Meaningful Sequence | Reading order follows DOM; rotor order correct. |  |  |
| 1.3.4 | Orientation | Works in portrait and landscape. |  |  |
| 1.4.1 | Use of Color | Color not sole means to convey meaning; add label/pattern. |  |  |
| 1.4.3 | Contrast (Minimum) | Text ≥ **4.5:1** (AA). |  |  |
| 1.4.10 | Reflow | Supports 320px width and 400% zoom w/o loss. |  |  |
| 1.4.11 | Non-Text Contrast | UI components ≥ **3:1**. |  |  |
| 1.4.12 | Text Spacing | Custom spacing does not break layout. |  |  |
| 1.4.13 | Content on Hover/Focus | Dismissible, hoverable, persistent on focus. |  |  |

---

## 2️⃣ Operable

| # | WCAG Ref | Requirement | Result | Notes / Evidence |
|--:|:--|:--|:--:|:--|
| 2.1.1 | Keyboard | All functionality works via keyboard. |  |  |
| 2.1.2 | No Keyboard Trap | Tab/Shift+Tab enter/exit all regions. |  |  |
| 2.1.4 | Character Key Shortcuts | Remappable/disable when needed. |  |  |
| 2.2.1 | Timing Adjustable | Time limits extendable / paused. |  |  |
| 2.3.1 | Seizures & Flashes | No flashes > 3Hz (or below threshold). |  |  |
| 2.4.1 | Bypass Blocks | Skip-link to `<main>` visible on first Tab. |  |  |
| 2.4.3 | Focus Order | Logical and matches visual flow. |  |  |
| 2.4.4 | Link Purpose (In Context) | Link text describes destination. |  |  |
| 2.4.7 | Focus Visible | ≥ 3px outline and ≥ 3:1 contrast. |  |  |
| 2.5.1 | Pointer Gestures | Complex gestures have single-point/keyboard alternatives. |  |  |
| 2.5.5 | Target Size | Touch targets ≥ 44×44 px (advisory / EN 301 549). |  |  |

---

## 3️⃣ Understandable

| # | WCAG Ref | Requirement | Result | Notes / Evidence |
|--:|:--|:--|:--:|:--|
| 3.1.1 | Language of Page | `<html lang>` set; inline `lang` for quotes. |  |  |
| 3.2.3 | Consistent Navigation | Repeated UI order is consistent. |  |  |
| 3.2.4 | Consistent Identification | Same icon/label used for same function. |  |  |
| 3.3.1 | Error Identification | Input errors are described textually and visually. |  |  |
| 3.3.2 | Labels or Instructions | Visible labels for all inputs; programmatic association. |  |  |
| 3.3.3 | Error Suggestions | Helpful text to fix errors. |  |  |
| 3.3.7 | Accessible Authentication (Advisory) | No cognitive-only authentication. |  |  |

---

## 4️⃣ Robust

| # | WCAG Ref | Requirement | Result | Notes / Evidence |
|--:|:--|:--|:--:|:--|
| 4.1.1 | Parsing | Valid HTML; unique IDs; no ARIA misuse. |  |  |
| 4.1.2 | Name, Role, Value | Accessible Name exposes correct semantics. |  |  |
| 4.1.3 | Status Messages | Announced via `role="status"`/`aria-live`. |  |  |
| 4.1.4 | Orientation (AA ext) | App functions when orientation changes. |  |  |
| 4.1.5 | Reflow (AA ext) | 320px / 400% zoom support. |  |  |

---

## 5️⃣ KFM MCP Extended Requirements (Map · Timeline · AI · Tokens)

| ID | Area | Requirement | Result | Notes / Evidence |
|--:|:--|:--|:--:|:--|
| KFM-A1 | Design Tokens | Uses `--kfm-color-*`, `--kfm-font-*`; contrast ≥ 4.5:1. |  |  |
| KFM-A2 | Theme Modes | Verified **light/dark/HC**; RTL snapshots pass. |  |  |
| KFM-A3 | Timeline | Keyboard scrubbing; `aria-valuetext` + summary region. |  |  |
| KFM-A4 | MapLibre | Only map region uses `role="application"`; Esc exits; SR summary present. |  |  |
| KFM-A5 | AI Live Regions | Buffered `aria-live="polite"`; no token-by-token spam. |  |  |
| KFM-A6 | Motion | `prefers-reduced-motion` disables heavy easing/auto-scroll. |  |  |
| KFM-A7 | Media | Captions/transcripts required; autoplay muted only. |  |  |
| KFM-A8 | Gestures | Pointer/keyboard alternatives; hit area ≥ 44×44 px. |  |  |
| KFM-A9 | i18n | `lang`/`dir` set; pseudo-locale test; RTL focus mirrors layout. |  |  |

---

## 🧮 Scoring & Budgets

### Global Accessibility Index (GAI)
```
GAI = (AxeScore×0.4 + Lighthouse×0.4 + KeyboardCoverage×0.2)
Target: ≥ 95
```

### Route-Level Budgets (merge gates)
| Route | Lighthouse A11y | Axe Critical | Keyboard Reach | SR Announce | Status |
|:--|--:|--:|--:|--:|:--:|
| `/` | ≥ 95 | 0 | 100 % | 100 % |  |
| `/map` | ≥ 95 | 0 | 100 % | 100 % |  |
| `/story/:id` | ≥ 95 | 0 | 100 % | 100 % |  |
| `/assistant` | ≥ 95 | 0 | 100 % | 100 % |  |

> **Error Budget:** 3 budget failures/quarter → RCA + deploy freeze.

---

## 📊 Summary Scores

| Category | Pass (%) | Notes |
|:--|:--:|:--|
| Perceivable |  |  |
| Operable |  |  |
| Understandable |  |  |
| Robust |  |  |
| **GAI Score** |  |  |
| **Overall Compliance** |  |  |

---

## 🧠 Hints & Anti-Patterns

- Prefer **native elements**; add ARIA only to **custom widgets**.  
- Do **not** announce every AI token — **buffer and summarize** updates.  
- Ensure **visible focus** on all controls; never remove outlines without a strong alternative.  
- For map: **only** the map region should use `role="application"`; provide an **Esc** help hint.  
- Provide **pattern/label** redundancy for all color-encoded info.

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
      - name: Install tools
        run: npm i -g pa11y-ci axe-core-cli @lhci/cli
      - name: Start test app
        run: npm run start:test & npx wait-on http://localhost:3000
      - name: Lighthouse (a11y)
        run: lhci collect --config=./lighthouse.a11y.json && lhci assert --config=./lighthouse.a11y.json
      - name: Pa11y (wcag)
        run: pa11y-ci --config .pa11yci.wcag.json > reports/wcag-report.json
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: wcag-compliance-report
          path: reports/
```

---

## 🧾 Metadata (fill for each audit)

```yaml
review_id: "wcag_checklist_{{ component }}_{{ version }}"
component: "{{ component_name }}"
route: "{{ route }}"
version: "{{ version }}"
reviewed_by: ["@accessibility-team","@design-lead"]
commit: "{{ GIT_COMMIT }}"
date: "{{ ISO8601_DATE }}"
wcag_level: "AA"
result: "pass | fail | partial"
tools: ["Axe v4.10","Lighthouse v12","Pa11y v7","NVDA 2023.3"]
environment:
  os: "Windows 11"
  browser: "Chrome 130"
  viewport: "1440×900"
artifacts:
  - "reports/wcag-report.json"
  - "reports/lighthouse-a11y.html"
  - "assets/a11y/screenshot-keyboard.png"
```

---

## 🔄 FAIR / CARE JSON-LD (optional, for registry)

```json
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "KFM WCAG 2.1 AA Checklist",
  "license": "CC-BY-4.0",
  "version": "v3.0.0",
  "dateModified": "2025-11-11",
  "creator": "Kansas Frontier Matrix Accessibility Council",
  "alignment": ["MCP-DL v6.3","WCAG 2.1 AA","Section 508","EN 301 549","FAIR","CARE"]
}
```

---

## 📅 Version History

| Version | Date | Author | Summary | Type |
|:--|:--|:--|:--|:--|
| **v3.0.0** | 2025-11-11 | @kfm-accessibility | Tier-Ω+∞: added route budgets, GAI scoring, i18n/gestures/media checks, CI app start, FAIR JSON-LD, observability hooks. | Major |
| v2.0.0 | 2024-08-21 | @kfm-accessibility | Expanded criteria mapping and CI reporting. | Minor |
| v1.0.0 | 2023-10-01 | Founding Team | Initial WCAG checklist template. | Major |

---

<div align="center">

### ✅ Kansas Frontier Matrix — Accessibility Compliance Framework  
**Perceivable · Operable · Understandable · Robust · Observable**

<!-- MCP-CERTIFIED: TIER Ω+∞ -->
<!-- VERIFIED-STANDARDS: [MCP-DL v6.3, WCAG 2.1 AA, WCAG 3.0 readiness, Section 508, EN 301 549, WAI-ARIA 1.2, ISO 9241-171, FAIR, CARE] -->
<!-- VALIDATION-HASH: sha256:wcag-checklist-v3-0-0-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -->

</div>
