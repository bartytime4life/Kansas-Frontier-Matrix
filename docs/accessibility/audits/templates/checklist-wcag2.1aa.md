---
title: "✅ Kansas Frontier Matrix — WCAG 2.1 AA Accessibility Checklist (Diamond⁹ Ω / Crown∞ Ω Ultimate Certified)"
path: "docs/accessibility/audits/templates/checklist-wcag2.1aa.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Continuous / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/a11y-wcag-checklist-v2.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Template"
intent: "wcag-manual-checklist"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# ✅ **Kansas Frontier Matrix — WCAG 2.1 AA Accessibility Checklist**  
`docs/accessibility/audits/templates/checklist-wcag2.1aa.md`

**Purpose:**  
Provide the authoritative **WCAG 2.1 AA manual test checklist** for the **Kansas Frontier Matrix (KFM)** project.  
Used by the A11y Council and CI/CD pipelines to verify conformance of **web UI**, **AI narratives**, and **documentation**.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📘 Overview

This checklist maps directly to **WCAG 2.1 AA Success Criteria** (plus KFM ethical extensions).  
For each criterion, auditors must record:

- ✅ **Pass** – criterion satisfied  
- ⚠️ **Needs Review** – possible issue, requires follow-up  
- ❌ **Fail** – does not meet WCAG / KFM standards  

Scope:

- Web interfaces (MapLibre, Cesium, Timeline UI)  
- Focus Mode & Story Node narratives (text, controls)  
- Documentation and PDF exports  

Results are referenced from quarterly reports in `docs/accessibility/audits/`.

---

## 🗂️ Structure

| Section # | WCAG Principle | Covered Criteria (AA Level) | Audit Reference |
|---|---|---|---|
| 1 | Perceivable | 1.1.1 → 1.4.13 | Visual / Alt-text review |
| 2 | Operable | 2.1.1 → 2.5.3 | Keyboard / Timing / Input tests |
| 3 | Understandable | 3.1.1 → 3.3.4 | Language / Predictability / Errors |
| 4 | Robust | 4.1.1 → 4.1.3 | ARIA / Name-Role-Value / Status messages |
| 5 | FAIR+CARE Ethical Extensions | C1 → C4 | Cultural & AI Narrative checks |

---

## ♿ Section 1 · Perceivable

> **Principle:** Information and user interface components must be presentable to users in ways they can perceive.

| ID | Criterion | Status | Notes |
|---|---|---|---|
| 1.1.1 | Non-text Content — All images/icons/maps have `alt`, `aria-label`, or title. |  |  |
| 1.2.1 | Audio-only / Video-only content has text alternative. |  |  |
| 1.2.5 | Captions / transcripts provided for multimedia. |  |  |
| 1.3.1 | Info & Relationships conveyed via structure (headings, lists, landmarks) not just visual styling. |  |  |
| 1.3.2 | Significant content follows a meaningful reading / focus order. |  |  |
| 1.4.1 | Use of Color is not the only means to convey information. |  |  |
| 1.4.3 | Contrast (Minimum) — Text/UI components meet ≥ 4.5:1 (3:1 for large text). |  |  |
| 1.4.4 | Resize Text — Up to 200% without loss of content or functionality. |  |  |
| 1.4.10 | Reflow — Content reflows correctly at 320px wide without horizontal scroll. |  |  |
| 1.4.13 | Content on Hover or Focus is dismissible, hoverable, and persistent. |  |  |

---

## ⌨️ Section 2 · Operable

> **Principle:** User interface components and navigation must be operable.

| ID | Criterion | Status | Notes |
|---|---|---|---|
| 2.1.1 | Keyboard — All functionality available from keyboard alone (Tab, Shift+Tab, Enter, Space, Esc). |  |  |
| 2.1.2 | No Keyboard Trap — Focus can always move away using keyboard. |  |  |
| 2.2.1 | Timing Adjustable — Users can extend or turn off time limits. |  |  |
| 2.2.2 | Pause, Stop, Hide — Users can pause or stop moving/auto-updating content. |  |  |
| 2.3.1 | Three Flashes or Below — No content flashes more than 3 times per second. |  |  |
| 2.4.3 | Focus Order — Logical, consistent, and predictable focus sequence. |  |  |
| 2.4.6 | Headings and Labels — Descriptive and meaningful. |  |  |
| 2.4.7 | Focus Visible — Clear visible focus indicator with sufficient contrast. |  |  |
| 2.5.1 | Pointer Gestures — Complex gestures have single-point alternatives. |  |  |
| 2.5.3 | Label in Name — Visible label text is included in accessible name (for voice control). |  |  |

---

## 🧠 Section 3 · Understandable

> **Principle:** Information and the operation of the user interface must be understandable.

| ID | Criterion | Status | Notes |
|---|---|---|---|
| 3.1.1 | Language of Page — Primary document `lang` attribute set correctly. |  |  |
| 3.1.5 | Reading Level — Focus Mode & Story Node narratives target ≤ Grade 8 reading level. |  |  |
| 3.2.1 | On Focus — Components do not cause unexpected context changes. |  |  |
| 3.2.3 | Consistent Navigation — Navigation order and positioning are consistent. |  |  |
| 3.3.1 | Error Identification — Errors are clearly indicated and associated with fields. |  |  |
| 3.3.3 | Error Suggestion / Prevention — Help provided to correct errors, critical actions confirmed. |  |  |
| 3.3.4 | Help — Contextual help and instructions are available where needed. |  |  |

---

## 🧩 Section 4 · Robust

> **Principle:** Content must be robust enough to be interpreted reliably by a wide variety of user agents, including assistive technologies.

| ID | Criterion | Status | Notes |
|---|---|---|---|
| 4.1.1 | Parsing — Valid HTML; no duplicate IDs that affect accessibility. |  |  |
| 4.1.2 | Name, Role, Value — All components expose programmatic name, role, and state. |  |  |
| 4.1.3 | Status Messages — Communicated via `aria-live` or equivalent without shifting focus. |  |  |

---

## ⚖️ Section 5 · FAIR+CARE Ethical Extensions

> **Principle:** Extend accessibility with ethical and cultural safeguards for AI-driven content.

| ID | Criterion | Status | Notes |
|---|---|---|---|
| C1 | Collective Benefit — Accessibility improvements demonstrably benefit end users (e.g., reduced error rates, increased completion). |  |  |
| C2 | Authority to Control — Indigenous and cultural data respect consent flags and visibility constraints. |  |  |
| C3 | Responsibility — Logged accessibility issues have owners, due dates, and regression checks. |  |  |
| C4 | Ethics — AI narratives and visuals avoid harmful stereotypes, exploitative framing, or erasure. |  |  |

---

## 🧾 Completion Summary (Example)

| Metric | Result | Target | Status |
|---|---|---|---|
| WCAG Pass Rate | 97.5% | ≥ 95% | ✅ |
| Critical Issues | 0 | ≤ 0 | ✅ |
| Contrast Compliance | 96% | 100% | ⚠️ |
| FAIR+CARE Review | PASS | PASS | ✅ |

---

## 🧠 Usage Instructions

1. **Clone this template** into a new file (e.g., `docs/accessibility/audits/2025-Q2_wcag_checklist.md`).  
2. For each row, set **Status** to ✅ / ⚠️ / ❌ and capture concise **Notes**.  
3. Link any supporting screenshots or CI artifacts in the Notes column.  
4. Reference the checklist from the quarterly audit report (`docs/accessibility/audits/YYYY-QX_a11y_report.json`).  
5. Update `faircare-report.md` if ethical criteria (Section 5) show regressions or improvements.  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.4.0 | 2025-11-17 | A11y & FAIR+CARE Council | Upgraded for KFM-MDP v10.4; added telemetry schema v2; hardened against box-breaking by avoiding nested backtick fences |
| v10.0.0 | 2025-11-10 | A11y & FAIR+CARE Council | Initial WCAG 2.1 AA checklist with FAIR+CARE extensions |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Part of the Accessibility Audit Template Suite · Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified  
[⬅ Back to Templates Index](README.md) • [Ethics Review Template →](ethics-review-template.md)

</div>