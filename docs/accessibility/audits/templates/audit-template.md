---
title: "🧾 Kansas Frontier Matrix — Manual Accessibility Audit Template (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/audits/templates/audit-template.md"
version: "v10.4.0"
last_updated: "2025-11-17"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/a11y-audit-template-v2.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Template"
intent: "manual-a11y-audit"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 🧾 **Kansas Frontier Matrix — Manual Accessibility Audit Template**  
`docs/accessibility/audits/templates/audit-template.md`

**Purpose:**  
Provide the **official, MCP-compliant manual audit form** for evaluating interface, narrative, and documentation accessibility across the Kansas Frontier Matrix (KFM).  
Ensures full alignment with **WCAG 2.1 AA**, **WAI-ARIA 1.2**, **FAIR+CARE**, and **ISO 9241-210**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../standards/faircare.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../releases/v10.4.0/manifest.zip)

</div>

---

## 📋 Audit Metadata

| Field | Description | Example |
|---|---|---|
| **Audit ID** | Unique identifier | `A11Y-2025-Q2-001` |
| **Date** | Execution date | `2025-06-15` |
| **Auditor(s)** | Names + roles | `J. Barta / FAIR+CARE Council` |
| **Scope** | Page(s) or component(s) | `FocusPanel`, `MapView`, `TimelineView` |
| **Tools** | Tools used | `Lighthouse 11.2`, `axe-core 4.8`, `NVDA 2025.1` |
| **Environment** | Browser, OS, device | `Firefox 125 / Windows 11 / Desktop` |
| **Build Reference** | Commit SHA or manifest | `<latest-commit-hash>` |

---

## 🧭 Audit Overview

Provide a short summary of what was tested and why.

_Example:_  
> This audit focused on Focus Mode v2 and MapView navigation. Tested keyboard paths, ARIA labels, contrast, and screen reader output using NVDA. Build: commit `<latest-commit-hash>`.

---

## ♿ WCAG 2.1 AA Checklist Results

| Criterion | Description | Status | Notes |
|---|---|---|---|
| 1.1.1 Non-text Content | All images/icons include alt text or ARIA labels | ✅ | Passed; all icons labeled |
| 1.4.3 Contrast Minimum | ≥4.5:1 text/UI contrast | ⚠️ | Primary button contrast 4.3:1 |
| 2.1.1 Keyboard | All functionality operable from keyboard | ✅ | Tab order validated |
| 2.4.7 Focus Visible | Focus indicator clearly visible | ✅ | ≥3:1 contrast ring |
| 3.1.5 Reading Level | ≤ Grade 8 reading level | ⚠️ | Focus narratives slightly above target |
| 4.1.2 Name, Role, Value | Accessible names + roles provided | ✅ | All ARIA values present |

---

## 💬 User Experience Findings

**Keyboard Navigation:**  
Describe any issues with tab order, ESC, Enter, etc.  
> Example: Dialog closes with ESC but trap occurs in nested focusable items.

**Screen Reader Output:**  
Describe landmark recognition, labeling clarity, verbosity.  
> Example: Timeline tooltip announced twice due to aria-live duplication.

**Motion / Reduced Motion:**  
> All UI honors `prefers-reduced-motion`. No unexpected flashes.

**Map & Timeline Accessibility:**  
> MapLibre panning fully keyboard-compatible; timeline axes missing `aria-describedby`.

---

## ⚖️ FAIR+CARE Ethical Review

| CARE Principle | Pass | Notes |
|---|---|---|
| **Collective Benefit** | ✅ | Accessibility fixes benefit broad users |
| **Authority to Control** | ✅ | Consent dialogs accessible and neutral |
| **Responsibility** | ⚠️ | Missing alt text on Indigenous landscape image |
| **Ethics** | ✅ | Narrative avoids harmful or biased phrasing |

---

## 🧩 Issues Summary

| ID | Severity | Issue Description | Component | Action Required |
|---|---|---|---|---|
| #001 | High | Fails WCAG 1.4.3 contrast | FocusPanel | Update primary button token |
| #002 | Medium | Tooltip double-announced | TimelineView | Fix aria-live region |
| #003 | Low | Chart missing aria-describedby | Timeline | Add description IDs |

---

## 🧠 Recommendations & Action Items

- Raise `color.button.primary.bg` contrast to ≥4.5:1  
- Add `aria-describedby` to timeline charts  
- Re-run readability checks on Focus Mode narratives  
- Retest after contrast + ARIA updates  

---

## 📊 Summary Metrics

| Metric | Result | Target | Status |
|---|---|---|---|
| **WCAG Compliance Score** | 97.2% | ≥ 95% | ✅ |
| **FAIR+CARE Review** | PASS | PASS | ✅ |
| **Critical Issues** | 0 | ≤ 0 | ✅ |
| **Readability Index** | 8.3 | ≤ 8 | ⚠️ |
| **Contrast Compliance** | 96% | 100% | ⚠️ |

---

## 🕰️ Audit Sign-off

**Reviewed By:** FAIR+CARE Accessibility Council  
**Date:** 2025-06-18  
**Next Review:** Q3 2025  
**Certification:** **FAIR+CARE Verified — WCAG 2.1 AA Compliant**

---

## 🧾 Appendix — Supporting Artifacts

Attach relevant JSON, screenshots, or exported CI outputs.

~~~text
Attached:
- reports/self-validation/web/a11y_summary.json
- reports/ui/button_focus_tests.json
~~~

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[⬅ Back to Template Index](README.md) • [WCAG Checklist →](checklist-wcag2.1aa.md)

</div>