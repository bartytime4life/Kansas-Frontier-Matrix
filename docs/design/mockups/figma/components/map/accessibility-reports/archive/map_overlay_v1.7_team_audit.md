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

The *Map Overlay (v1.7)* introduced collapsible panels for map layers, legends, and metadata.  
Accessibility testing identified several deficiencies in contrast, focus visibility, and keyboard accessibility.  
These findings led to a comprehensive redesign in **v1.8**, which achieved full WCAG 2.1 AA compliance.

---

## 🧩 WCAG 2.1 Evaluation Results

| WCAG Ref | Criterion | Result | Notes |
|:--|:--|:--|:--|
| **1.4.3** | Contrast (Minimum) | ❌ Fail | Legend text 4.0 : 1 — below 4.5 : 1 threshold. |
| **2.1.1** | Keyboard Navigation | ⚠️ Partial | Focus order inconsistent; layer toggles skipped via `Tab`. |
| **2.4.7** | Focus Visible | ❌ Fail | No visible outline in high-contrast mode. |
| **4.1.2** | Name, Role, Value | ✅ Pass | All ARIA attributes present. |

---

## 🧠 Summary of Findings

- ❌ **Contrast Issues:** Legend labels and toggle text failed 1.4.3 color contrast minimums.  
- ❌ **Focus Visibility:** Focus outlines were either invisible or clipped.  
- ⚠️ **Keyboard Navigation:** Tab traversal inconsistent between panel sections.  
- ✅ **ARIA Semantics:** ARIA roles and labels implemented correctly.  

These issues made interactive legends and toggles difficult to perceive or operate for some users.

---

## 📊 Accessibility Metrics

| Metric | v1.7 Result | WCAG Target | v1.8 Result | Status |
|:--|:--|:--|:--|:--|
| Text Contrast | 4.0 : 1 | ≥ 4.5 : 1 | 5.0 : 1 | ✅ Fixed |
| Focus Ring Contrast | None | ≥ 3 : 1 | 3.4 : 1 | ✅ Fixed |
| Keyboard Navigation | Partial | Full | Full | ✅ Fixed |
| ARIA Label Accuracy | 100 % | 100 % | 100 % | 🟢 Stable |

---

## 🧩 Developer Notes

- Updated color tokens for legend backgrounds (`--legend-bg`, `--legend-fg`).  
- Added focus styles with accent outline tokens (`--focus-outline-accent`).  
- Implemented uniform tab order across collapsible panels.  
- Introduced `aria-expanded` state for all collapsible sections.  
- Verified compliance using Stark, Axe, and manual testing across themes.  

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
| Focus Outline Visibility | ❌ Absent | ✅ Visible Accent Outline | ✅ Fixed |
| Keyboard Navigation | ⚠️ Partial | ✅ Sequential & Consistent | ✅ Fixed |
| ARIA Semantics | ✅ Pass | ✅ Pass | 🟢 Stable |

---

## 🧩 Reviewer Sign-Off

| Role | Reviewer | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-18 | ❌ Fail |
| UI Engineer | L. Daniels | 2025-09-18 | ⚠️ Needs Revision |
| Design Reviewer | A. Barta | 2025-09-18 | ✅ Logged for Redesign in v1.8 |

---

## 🧾 Archive Notes

- **Deprecation Reason:** Failed WCAG contrast and keyboard focus requirements.  
- **Resolution:** v1.8 corrected all accessibility issues and achieved certification.  
- **Retention:** Archived permanently under MCP governance as part of KFM’s Accessibility Registry.  

---

> **License:** CC-BY-4.0  
> **Status:** Archived — Superseded by Map Overlay v1.8  
> **Retention:** Permanent (Immutable MCP Provenance Record)

---

<div align="center">

### ♿ “Accessibility is clarity —  
when legends are legible, history becomes visible.”  
**— Kansas Frontier Matrix Accessibility & Design Council**

</div>
