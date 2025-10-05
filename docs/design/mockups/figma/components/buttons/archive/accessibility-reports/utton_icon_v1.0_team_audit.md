---
id: button_icon_v1.0_team_audit
title: Icon Button (v1.0) — Archived Accessibility Audit
author: accessibility.team
date: 2025-09-18
archived_on: 2025-10-06
archived_by: design.board
status: archived
replaced_by: ../../../metadata/button_icon_v1.1.yml
source_figma: https://www.figma.com/file/MNOPQ23456/KFM-Component-Library?node-id=320%3A410
plugin_used:
  - Able v2.3
  - Stark v4.0
criteria:
  - 1.1.1 Non-text Content
  - 1.4.3 Contrast (Minimum)
  - 2.4.7 Focus Visible
  - 2.5.5 Target Size (Enhanced)
  - 4.1.2 Name, Role, Value
result: fail
issues_found: 4
license: CC-BY-4.0
review_log: ../../../../../../../reviews/2025-09-18_button_icon_v1.0.md
linked_export: ../../../exports/archive/button_icon_v1.0.svg
linked_metadata: ../../../metadata/archive/button_icon_v1.0.yml
related_docs:
  - ../../../../../../ui-guidelines.md
  - ../../../../../../style-guide.md
  - ../../../../../../interaction-patterns.md
---

# ♿ Archived Accessibility Audit — Icon Button (v1.0)

**Component:** Icon-Only Button (v1.0)  
**Audit Date:** September 18 2025  
**Reviewed by:** Accessibility Team (`accessibility.team`)  
**Status:** Deprecated (Replaced by v1.1)

---

## 🎯 Context

Version 1.0 introduced the first icon-only control in the Frontier Matrix interface  
(e.g., *close*, *settings*, *info* icons).  
While visually minimal, it failed several accessibility checkpoints —  
notably missing **ARIA labeling**, **focus visibility**, and **adequate target area**.  
These issues were fully remediated in **v1.1**.

---

## 🧩 WCAG 2.1 Evaluation Results

| WCAG Ref | Criterion | Result | Notes |
|:--|:--|:--|:--|
| **1.1.1** | Non-text Content | ❌ Fail | Icon lacked descriptive `aria-label`. |
| **1.4.3** | Contrast (Minimum) | ✅ Pass | Foreground icon #2c2c2c on #f9f9f9 = 5.2 : 1. |
| **2.4.7** | Focus Visible | ❌ Fail | No visible outline on focus. |
| **2.5.5** | Target Size (Enhanced) | ⚠️ Partial | 36 × 36 px < recommended 44 × 44 px. |
| **4.1.2** | Name, Role, Value | ❌ Fail | Lacked accessible name and role. |

---

## 🧮 Summary of Findings

- **Labeling Issue:** Missing `aria-label` prevented screen-reader identification.  
- **Focus Visibility:** No keyboard outline; users couldn’t detect active focus.  
- **Touch Target:** Hit area too small on touch devices.  
- **Contrast:** Met standards; unchanged in later versions.  

---

## 📊 Accessibility Metrics

| Metric | v1.0 | WCAG Target | v1.1 | Status |
|:--|:--|:--|:--|:--|
| Contrast Ratio | 5.2 : 1 | ≥ 4.5 : 1 | 5.2 : 1 | 🟢 Stable |
| Focus Indicator | None | Required | Accent Outline 2 px | ✅ Fixed |
| ARIA Label Present | No | Yes | Yes (`aria-label="Close"`) | ✅ Fixed |
| Target Size | 36 × 36 px | ≥ 44 × 44 px | 44 × 44 px | ✅ Fixed |
| Keyboard Nav | Partial | Full | Full | ✅ Improved |

---

## 🧠 Developer Notes

- Added `aria-label` to all icon buttons in v1.1.  
- Introduced shared focus-ring token (`--focus-outline-accent`).  
- Increased clickable area using padding + hit-zone expansion.  
- Verified all icons register correct role = `button`.  

---

## 🔗 Provenance Links

| Type | Path |
|:--|:--|
| **Replacement Metadata** | [`../../../metadata/button_icon_v1.1.yml`](../../../metadata/button_icon_v1.1.yml) |
| **Design Export** | [`../../../exports/archive/button_icon_v1.0.svg`](../../../exports/archive/button_icon_v1.0.svg) |
| **Review Log** | [`../../../../../../../reviews/2025-09-18_button_icon_v1.0.md`](../../../../../../../reviews/2025-09-18_button_icon_v1.0.md) |
| **Figma Source** | [View in Figma →](https://www.figma.com/file/MNOPQ23456/KFM-Component-Library?node-id=320%3A410) |

---

## ♿ Regression Tracking

| Category | v1.0 | v1.1 | Status |
|:--|:--|:--|:--|
| ARIA Label | Missing | Added | ✅ Fixed |
| Focus Outline | None | Accent 2 px ring | ✅ Fixed |
| Target Size | 36 × 36 px | 44 × 44 px | ✅ Fixed |
| Keyboard Access | Partial | Full | ✅ Fixed |
| Contrast | Pass | Pass | 🟢 Stable |

---

## 🧩 Reviewer Sign-Off

| Role | Name | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-18 | ❌ Fail |
| UI Engineer | L. Daniels | 2025-09-18 | ⚠️ Needs Revision |
| Design Reviewer | A. Barta | 2025-09-18 | ✅ Approved for Redesign |

---

## 🧾 Archive Notes

- Archived on **October 6, 2025** after v1.1 passed full WCAG 2.1 AA validation.  
- This report serves as a baseline for ARIA and focus improvement tracking.  
- Permanently retained under MCP archival policy.  

---

> **License:** CC-BY-4.0  
> **Status:** Archived for provenance and accessibility comparison with v1.1.  

---

<div align="center">

### ♿ “Small icons carry big responsibilities —  
clarity and focus make them speak for everyone.”  
**— Kansas Frontier Matrix Accessibility Review Board**

</div>
