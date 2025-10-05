---
id: map_overlay_v1.7_team_audit
title: Map Overlay Component (v1.7) — Archived Accessibility Audit
author: accessibility.team
date: 2025-09-18
archived_on: 2025-10-08
archived_by: accessibility.team
status: archived
replaced_by: ../../../../accessibility-reports/map_overlay_v1.8_team_audit.md
source_figma: https://www.figma.com/file/KFM_MAP_COMPONENTS/Library?node-id=480%3A520
plugin_used:
  - Able v2.3
  - Stark v4.1
criteria:
  - 1.4.3 Contrast (Minimum)
  - 2.1.1 Keyboard Navigation
  - 2.4.7 Focus Visible
  - 4.1.2 Name, Role, Value
result: fail
issues_found: 3
license: CC-BY-4.0
review_log: ../../../../../../../../../reviews/2025-09-18_map_overlay_v1.7.md
linked_export: ../../../exports/archive/map_overlay_v1.7.png
linked_metadata: ../../../metadata/archive/map_overlay_v1.7.yml
related_docs:
  - ../../../../../../../../ui-guidelines.md
  - ../../../../../../../../style-guide.md
  - ../../../../../../../../interaction-patterns.md
---

# ♿ Archived Accessibility Audit — Map Overlay (v1.7)

**Component:** Map Overlay (Legend · Layer · Metadata Panels)  
**Audit Date:** September 18, 2025  
**Reviewed by:** Accessibility Team (`accessibility.team`)  
**Status:** ❌ Fail — Superseded by Map Overlay v1.8  

---

## 🎯 Context

The *Map Overlay (v1.7)* handled map legends, layer toggles, and collapsible metadata sections.  
Accessibility evaluation identified multiple **WCAG 2.1 AA** violations — including low text contrast, poor focus visibility, and inconsistent tab traversal.  

These findings prompted the development of **v1.8**, which remediated all issues and achieved MCP certification for full accessibility compliance.

---

## 🧩 WCAG 2.1 Evaluation Results

| WCAG Ref | Criterion | Result | Notes |
|:--|:--|:--|:--|
| **1.4.3** | Contrast (Minimum) | ❌ Fail | Legend text contrast 4.0 : 1 — below 4.5 : 1 minimum. |
| **2.1.1** | Keyboard Navigation | ⚠️ Partial | Inconsistent tab focus between collapsible legend panels. |
| **2.4.7** | Focus Visible | ❌ Fail | Focus indicators not visible in light theme. |
| **4.1.2** | Name, Role, Value | ✅ Pass | ARIA roles correctly implemented for buttons and regions. |

---

## 🧠 Summary of Findings

- ❌ **Contrast Deficiency:** Legend and toggle text failed contrast ratio.  
- ❌ **Focus Visibility:** Focus rings too faint for adequate visibility.  
- ⚠️ **Keyboard Accessibility:** Layer toggles and panel headers inconsistent in focus order.  
- ✅ **ARIA Compliance:** ARIA roles and labeling accurate.  

Accessibility barriers were addressed in **v1.8** with improved color tokens, focus styling, and navigation patterns.

---

## 📊 Accessibility Metrics

| Metric | v1.7 Result | WCAG Target | v1.8 Result | Status |
|:--|:--|:--|:--|:--|
| Text Contrast | 4.0 : 1 | ≥ 4.5 : 1 | 5.0 : 1 | ✅ Fixed |
| Focus Outline Contrast | 2.2 : 1 | ≥ 3 : 1 | 3.4 : 1 | ✅ Fixed |
| Keyboard Navigation Coverage | Partial | Full | Full | ✅ Fixed |
| ARIA Role Accuracy | Complete | Complete | Complete | 🟢 Stable |

---

## 🧩 Developer Notes

- Updated contrast tokens (`--legend-bg`, `--legend-fg`) to ensure text readability in both color modes.  
- Implemented `--focus-outline-accent` for consistent focus styling across overlay elements.  
- Defined a consistent tab index order across all collapsible and interactive regions.  
- Verified compliance using **Stark**, **Able**, **Axe**, and manual keyboard testing.  
- No animation or transition-related accessibility violations found.  

---

## 🔗 Provenance Links

| Type | Path |
|:--|:--|
| **Replacement Audit** | [`../../../../accessibility-reports/map_overlay_v1.8_team_audit.md`](../../../../accessibility-reports/map_overlay_v1.8_team_audit.md) |
| **Metadata File** | [`../../../metadata/archive/map_overlay_v1.7.yml`](../../../metadata/archive/map_overlay_v1.7.yml) |
| **Design Export** | [`../../../exports/archive/map_overlay_v1.7.png`](../../../exports/archive/map_overlay_v1.7.png) |
| **Review Log** | [`../../../../../../../../../reviews/2025-09-18_map_overlay_v1.7.md`](../../../../../../../../../reviews/2025-09-18_map_overlay_v1.7.md) |
| **Figma Source** | [View in Figma →](https://www.figma.com/file/KFM_MAP_COMPONENTS/Library?node-id=480%3A520) |

---

## ♿ Regression Comparison (v1.7 → v1.8)

| Issue | v1.7 Result | v1.8 Result | Status |
|:--|:--|:--|:--|
| Legend Text Contrast | ❌ 4.0 : 1 | ✅ 5.0 : 1 | ✅ Fixed |
| Focus Indicator | ❌ Missing | ✅ Accent Outline (3.4 : 1) | ✅ Fixed |
| Keyboard Navigation | ⚠️ Partial | ✅ Sequential and Consistent | ✅ Fixed |
| ARIA Roles | ✅ Pass | ✅ Pass | 🟢 Stable |

---

## 🧩 Reviewer Sign-Off

| Role | Reviewer | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-18 | ❌ Fail |
| UI Engineer | L. Daniels | 2025-09-18 | ⚠️ Needs Revision |
| Design Reviewer | A. Barta | 2025-09-18 | ✅ Approved for Iteration in v1.8 |

---

## 🧾 Archive Notes

- **Deprecation Reason:** Failed WCAG 1.4.3 contrast and 2.4.7 focus visibility standards.  
- **Resolution:** All issues remediated in v1.8 with enhanced tokens and improved keyboard flow.  
- **Retention:** Permanently archived under MCP Accessibility Registry for regression tracking and audit continuity.  

---

> **License:** CC-BY-4.0  
> **Status:** Archived — Superseded by Map Overlay v1.8  
> **Retention:** Permanent (Immutable MCP Provenance Record)

---

<div align="center">

### ♿ “Accessibility turns data into discovery —  
every legend must be legible to every user.”  
**— Kansas Frontier Matrix Accessibility & Design Council**

</div>
