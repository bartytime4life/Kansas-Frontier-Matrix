---
id: button_primary_v2.0_team_audit
title: Primary Button (v2.0) — Archived Accessibility Audit
author: accessibility.team
date: 2025-09-20
archived_on: 2025-10-06
archived_by: design.board
status: archived
replaced_by: ../../../metadata/button_primary_v2.1.yml
source_figma: https://www.figma.com/file/ABCDE12345/KFM-Component-Library?node-id=98%3A150
plugin_used:
  - Able v2.3
  - Stark v4.1
criteria:
  - 1.4.3 Contrast (Minimum)
  - 2.4.7 Focus Visible
  - 2.1.1 Keyboard Accessibility
  - 2.3.3 Animation from Interactions
result: fail
issues_found: 3
license: CC-BY-4.0
review_log: ../../../../../../../reviews/2025-09-20_button_primary_v2.0.md
linked_export: ../../../exports/archive/button_primary_v2.0.png
linked_metadata: ../../../metadata/archive/button_primary_v2.0.yml
related_docs:
  - ../../../../../../ui-guidelines.md
  - ../../../../../../style-guide.md
  - ../../../../../../interaction-patterns.md
---

# ♿ Archived Accessibility Audit — Primary Button (v2.0)

**Design Component:** Primary Button (v2.0)  
**Audit Date:** September 20, 2025  
**Audit Team:** Accessibility & Design Review Board (`accessibility.team`)  
**Status:** Deprecated (Replaced by v2.1)  

---

## 🎯 Context

This audit documents the accessibility evaluation for *Primary Button v2.0*,  
conducted before its redesign in version 2.1. The audit identified several  
WCAG 2.1 AA compliance issues related to **contrast**, **focus visibility**,  
and **hover color consistency**.

All issues noted here were resolved in **v2.1**, which introduced stronger  
contrast ratios, visible focus outlines, and consistent reduced-motion behavior.

---

## 🧩 WCAG Evaluation Results

| WCAG Ref | Check | Result | Notes |
|:--|:--|:--|:--|
| **1.4.3** | Contrast (Text) | ❌ Fail | White-on-accent ratio = 4.2 : 1 (below 4.5 : 1). |
| **2.4.7** | Focus Visible | ❌ Fail | Focus ring not visible in default light theme. |
| **2.1.1** | Keyboard Accessibility | ✅ Pass | Fully tab-navigable, including disabled states. |
| **2.3.3** | Animation from Interactions | ✅ Pass | Hover/focus animations ≤ 150 ms (compliant). |

---

## 🧮 Summary of Findings

- **Contrast Issues:**  
  The accent orange (#c77d02) did not meet text contrast requirements.  
  Updated in v2.1 to a darker hue (#a96a00) for improved 5.1 : 1 ratio.

- **Focus Ring Visibility:**  
  Focus outlines were not rendered in light theme.  
  Fixed in v2.1 with `outline: 2px solid var(--color-accent-alt)`.

- **Keyboard Navigation:**  
  Verified working with `Tab` and `Shift+Tab`; no traps detected.  

- **Motion Settings:**  
  Transitions reduced to 150 ms, honoring `prefers-reduced-motion`.  

---

## 📊 Accessibility Metrics

| Metric | v2.0 Result | WCAG Target | v2.1 Result | Status |
|:--|:--|:--|:--|:--|
| Text Contrast | 4.2 : 1 | ≥ 4.5 : 1 | 5.1 : 1 | ✅ Fixed |
| Focus Outline Visibility | None | Required | Visible (Accent Ring) | ✅ Fixed |
| Keyboard Access | Full | Full | Full | 🟢 Unchanged |
| Reduced Motion | Partial | Required | Full | 🟢 Improved |

---

## 🧠 Developer Notes

- The focus state in v2.0 used an inset shadow rather than outline,  
  which failed to meet minimum visibility contrast on light backgrounds.  
- All hover and active states used the same accent token,  
  resulting in insufficient distinction during interaction.  
- Color tokens were updated in v2.1 within `/docs/design/style-guide.md`.  

---

## 🔗 Provenance Links

| Type | Location |
|:--|:--|
| **Replacement Metadata** | [`../../../metadata/button_primary_v2.1.yml`](../../../metadata/button_primary_v2.1.yml) |
| **Design Export** | [`../../../exports/archive/button_primary_v2.0.png`](../../../exports/archive/button_primary_v2.0.png) |
| **Figma Source** | [View on Figma →](https://www.figma.com/file/ABCDE12345/KFM-Component-Library?node-id=98%3A150) |
| **Review Log** | [`../../../../../../../reviews/2025-09-20_button_primary_v2.0.md`](../../../../../../../reviews/2025-09-20_button_primary_v2.0.md) |
| **UI Guidelines** | [`../../../../../../ui-guidelines.md`](../../../../../../ui-guidelines.md) |

---

## ♿ Regression Tracking

| Category | v2.0 | v2.1 | Status |
|:--|:--|:--|:--|
| Text Contrast | 4.2 : 1 | 5.1 : 1 | ✅ Fixed |
| Focus Ring | None | Accent Border | ✅ Fixed |
| Hover State Contrast | 3.7 : 1 | 4.8 : 1 | ✅ Fixed |
| Keyboard Navigation | Working | Working | 🟢 Stable |
| Reduced Motion | Partial | Full | 🟢 Improved |

---

## 🧩 Reviewer Sign-Off

| Role | Name | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-20 | ❌ Fail |
| UI Engineer | L. Daniels | 2025-09-20 | ⚠️ Needs Revision |
| Design Reviewer | A. Barta | 2025-09-20 | ✅ Approved for redesign |

---

## 🧾 Archive Notes

- Archived on **October 6, 2025** upon successful validation of **v2.1**.  
- This report provides historical context for accessibility iteration improvements.  
- Stored permanently under MCP archival retention policy.  

---

> **License:** CC-BY-4.0  
> **Status:** Archived for provenance and accessibility regression comparison.  

---

<div align="center">

### ♿ “Accessibility is iteration —  
each fix illuminates the next frontier of inclusion.”  
**— Kansas Frontier Matrix Accessibility Board**

</div>
