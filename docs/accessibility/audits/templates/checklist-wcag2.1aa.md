---
title: "✅ Kansas Frontier Matrix — WCAG 2.1 AA Accessibility Checklist (Diamond⁹ Ω / Crown∞ Ω Ultimate Certified)"
path: "docs/accessibility/audits/templates/checklist-wcag2.1aa.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/a11y-wcag-checklist-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# ✅ **Kansas Frontier Matrix — WCAG 2.1 AA Accessibility Checklist**
`docs/accessibility/audits/templates/checklist-wcag2.1aa.md`

**Purpose:**  
Serve as the authoritative **WCAG 2.1 AA manual test checklist** for the **Kansas Frontier Matrix (KFM)** project.  
Used by the A11y Council and CI/CD pipelines to ensure each release meets minimum accessibility conformance for **web**, **AI narratives**, and **documentation**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

This checklist maps directly to **WCAG 2.1 AA Success Criteria** and KFM’s ethical extensions.  
Each criterion must be marked ✅ Pass, ⚠️ Needs Review, or ❌ Fail during audits.  
It applies to:  
- Web interfaces (MapLibre, Cesium, Timeline UI)  
- AI Focus Mode content and summary readouts  
- Documentation and PDF exports  

All results feed automatically into quarterly reports in `docs/accessibility/audits/`.

---

## 🗂️ Structure

| Section # | WCAG Principle | Covered Criteria (AA Level) | Audit Reference |
|------------|----------------|------------------------------|-----------------|
| 1 | Perceivable | 1.1.1 → 1.4.13 | Visual / Alt-text review |
| 2 | Operable | 2.1.1 → 2.5.5 | Keyboard / Timing tests |
| 3 | Understandable | 3.1.1 → 3.3.4 | Language / Error handling |
| 4 | Robust | 4.1.1 → 4.1.3 | ARIA roles / Name-Value pairs |
| 5 | FAIR+CARE Ethical Extensions | C1 → C4 | Cultural & AI Narrative checks |

---

## ♿ 1 · Perceivable (Information must be perceivable)

| ID | Criterion | Status | Notes |
|----|------------|--------|-------|
| 1.1.1 | Non-text Content — All images / icons have alt or aria-label. |  |  |
| 1.2.1 | Audio-only / Video alternative text provided. |  |  |
| 1.2.5 | Captions / transcripts for multimedia content. |  |  |
| 1.3.1 | Info and Relationships conveyed via structure, not appearance. |  |  |
| 1.3.2 | Meaningful reading / focus order. |  |  |
| 1.4.1 | Use of Color not sole means of conveying information. |  |  |
| 1.4.3 | Contrast (Minimum 4.5:1 text / 3:1 large text). |  |  |
| 1.4.4 | Resizable Text (200% without loss of content). |  |  |
| 1.4.10 | Reflow on mobile ≤ 320 px viewport. |  |  |
| 1.4.13 | Content on Hover / Focus dismissible, hoverable, persistent. |  |  |

---

## ⌨️ 2 · Operable (Interface elements usable via keyboard)

| ID | Criterion | Status | Notes |
|----|------------|--------|-------|
| 2.1.1 | Keyboard Operable (Tab, Shift+Tab, Enter, Space, Esc). |  |  |
| 2.1.2 | No Keyboard Trap / Focus escapable. |  |  |
| 2.2.1 | Timing Adjustable (no auto-timeouts). |  |  |
| 2.2.2 | Pause, Stop, Hide for animations or carousels. |  |  |
| 2.3.1 | Flashing ≤ 3 Hz (limit seizure risk). |  |  |
| 2.4.3 | Focus Order logical / predictable. |  |  |
| 2.4.6 | Descriptive Headings and Labels. |  |  |
| 2.4.7 | Focus Visible (≥ 3:1 contrast ring). |  |  |
| 2.5.1 | Pointer Gestures alternatives provided. |  |  |
| 2.5.3 | Label in Name (voice control compatibility). |  |  |

---

## 🧠 3 · Understandable (Content must be clear and predictable)

| ID | Criterion | Status | Notes |
|----|------------|--------|-------|
| 3.1.1 | Page Language defined (`lang` attribute). |  |  |
| 3.1.5 | Reading Level ≤ Grade 8 for Focus Mode narratives. |  |  |
| 3.2.1 | On Focus — No unexpected context change. |  |  |
| 3.2.3 | Consistent Navigation across pages. |  |  |
| 3.3.1 | Error Identification and Messaging clear. |  |  |
| 3.3.3 | Error Prevention for data entry / submission. |  |  |
| 3.3.4 | Help Available / Instructions present. |  |  |

---

## 🧩 4 · Robust (Compatible with assistive tech and future tools)

| ID | Criterion | Status | Notes |
|----|------------|--------|-------|
| 4.1.1 | Parsing — HTML valid, no duplicate IDs. |  |  |
| 4.1.2 | Name, Role, Value exposed via ARIA / DOM. |  |  |
| 4.1.3 | Status Messages announce via `aria-live`. |  |  |

---

## ⚖️ 5 · FAIR+CARE Ethical Extensions (for AI and Cultural Contexts)

| ID | Criterion | Status | Notes |
|----|------------|--------|-------|
| C1 | Collective Benefit — Accessibility improvements benefit all users. |  |  |
| C2 | Authority to Control — Cultural data respect consent / visibility settings. |  |  |
| C3 | Responsibility — Accessibility issues tracked and resolved each quarter. |  |  |
| C4 | Ethics — Narrative and visual tone avoid harm or bias. |  |  |

---

## 🧾 Completion Summary (Example)

| Metric | Result | Target | Status |
|--------|--------|--------|--------|
| WCAG Pass Rate | 97.5% | ≥ 95% | ✅ |
| Critical Issues | 0 | ≤ 0 | ✅ |
| Contrast Compliance | 96% | 100% | ⚠️ |
| FAIR+CARE Review | PASS | PASS | ✅ |

---

## 🧠 Usage Instructions

1. Duplicate this file for each audit cycle → `YYYY-QX_wcag_checklist.md`.  
2. Fill “Status” column with ✅ / ⚠️ / ❌.  
3. Include references to screenshots or JSON artifacts.  
4. Commit to `docs/accessibility/audits/` and link from the quarterly report.  
5. Update `faircare-report.md` if ethical criteria changed.  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|--------|----------|
| v10.0.0 | 2025-11-10 | A11y & FAIR+CARE Council | Established comprehensive WCAG 2.1 AA checklist for manual audits with FAIR+CARE ethical extensions. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Part of the Accessibility Audit Template Suite · Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified  
[⬅ Back to Templates Index](README.md) · [Ethics Review Template →](ethics-review-template.md)

</div>