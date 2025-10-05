---
id: timeline_marker_v1.4_team_audit
title: Timeline Marker (v1.4) — Archived Accessibility Audit
author: accessibility.team
date: 2025-09-28
archived_on: 2025-10-07
archived_by: accessibility.team
status: archived
replaced_by: ../../../../accessibility-reports/timeline_marker_v1.5_team_audit.md
source_figma: https://www.figma.com/file/KFM_TIMELINE_DOCS/Component-Library?node-id=400%3A320
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
review_log: ../../../../../../../../../reviews/2025-09-28_timeline_marker_v1.4.md
linked_export: ../../../exports/archive/timeline_marker_v1.4.png
linked_metadata: ../../../metadata/archive/timeline_marker_v1.4.yml
related_docs:
  - ../../../../../../../../ui-guidelines.md
  - ../../../../../../../../style-guide.md
  - ../../../../../../../../interaction-patterns.md
---

# ♿ Archived Accessibility Audit — Timeline Marker (v1.4)

**Component:** Timeline Marker (v1.4)  
**Audit Date:** September 28, 2025  
**Reviewed by:** Accessibility & Design Board (`accessibility.team`)  
**Status:** ❌ Fail — Superseded by Timeline Marker v1.5  

---

## 🎯 Context

Timeline Marker v1.4 served as the first version of interactive historical event indicators  
within the KFM Timeline System. While functional, it failed several **WCAG 2.1 AA** accessibility  
criteria related to focus visibility, contrast, and ARIA labeling. These issues were corrected in  
v1.5 to meet MCP accessibility standards.

---

## 🧩 WCAG 2.1 Evaluation Results

| WCAG Ref | Criterion | Result | Notes |
|:--|:--|:--|:--|
| **1.4.3** | Contrast (Minimum) | ⚠️ Partial | Marker hover contrast 4.1 : 1 (below threshold). |
| **2.1.1** | Keyboard Navigation | ✅ Pass | Fully operable with Tab and Enter. |
| **2.4.7** | Focus Visible | ❌ Fail | Focus outline faint and inconsistent in dark theme. |
| **4.1.2** | Name, Role, Value | ⚠️ Partial | Tooltip missing `aria-label` and semantic roles. |

---

## 🧠 Summary of Findings

- ❌ **Focus Visibility:** Weak focus outline color; failed 3:1 minimum ratio in both themes.  
- ⚠️ **Contrast Issue:** Hover state failed 4.5:1 text/background contrast requirement.  
- ⚠️ **ARIA Roles:** Tooltip lacked accessible name; marker lacked role="button".  
- ✅ **Keyboard Navigation:** Operational but needed enhanced focus cues.

---

## 📊 Accessibility Metrics

| Metric | v1.4 Result | WCAG Target | v1.5 Result | Status |
|:--|:--|:--|:--|:--|
| Hover Contrast | 4.1 : 1 | ≥ 4.5 : 1 | 4.9 : 1 | ✅ Fixed |
| Focus Outline Contrast | 2.5 : 1 | ≥ 3 : 1 | 3.5 : 1 | ✅ Fixed |
| ARIA Role Coverage | Partial | Full | Full | ✅ Fixed |
| Keyboard Accessibility | Pass | Pass | Pass | 🟢 Stable |

---

## 🧩 Developer Notes

- Introduced focus outline token (`--focus-outline-accent`) for clarity and visibility.  
- Reworked color tokens for hover and selected marker states to exceed contrast thresholds.  
- Added ARIA role `"button"` and `aria-describedby` to improve screen reader support.  
- Adjusted tooltip timing to ensure motion compliance under `prefers-reduced-motion`.  
- Updated tab order and event synchronization with timeline playback logic.  

---

## 🔗 Provenance Links

| Type | Path |
|:--|:--|
| **Replacement Audit** | [`../../../../accessibility-reports/timeline_marker_v1.5_team_audit.md`](../../../../accessibility-reports/timeline_marker_v1.5_team_audit.md) |
| **Metadata File** | [`../../../metadata/archive/timeline_marker_v1.4.yml`](../../../metadata/archive/timeline_marker_v1.4.yml) |
| **Design Export** | [`../../../exports/archive/timeline_marker_v1.4.png`](../../../exports/archive/timeline_marker_v1.4.png) |
| **Review Log** | [`../../../../../../../../../reviews/2025-09-28_timeline_marker_v1.4.md`](../../../../../../../../../reviews/2025-09-28_timeline_marker_v1.4.md) |
| **Figma Source** | [View in Figma →](https://www.figma.com/file/KFM_TIMELINE_DOCS/Component-Library?node-id=400%3A320) |

---

## ♿ Regression Comparison (v1.4 → v1.5)

| Issue | v1.4 Result | v1.5 Result | Status |
|:--|:--|:--|:--|
| Hover Contrast | ⚠️ 4.1 : 1 | ✅ 4.9 : 1 | ✅ Fixed |
| Focus Outline | ❌ Faint | ✅ Visible 3.5 : 1 | ✅ Fixed |
| ARIA Labeling | ⚠️ Missing | ✅ Implemented | ✅ Fixed |
| Keyboard Access | ✅ Pass | ✅ Pass | 🟢 Stable |
| Motion Preference | ⚠️ Not Defined | ✅ Respects `prefers-reduced-motion` | ✅ Fixed |

---

## 🧩 Reviewer Sign-Off

| Role | Reviewer | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-28 | ❌ Fail |
| UI Engineer | L. Daniels | 2025-09-28 | ⚠️ Needs Revision |
| Design Reviewer | A. Barta | 2025-09-28 | ✅ Logged for Redesign v1.5 |

---

## 🧾 Archive Notes

- **Deprecation Reason:** Failed contrast and ARIA role validation.  
- **Resolution:** Fixed in v1.5 with new tokens, semantic roles, and improved contrast.  
- **Retention:** Permanently archived under MCP Accessibility Record for audit continuity.  

---

> **License:** CC-BY-4.0  
> **Status:** Archived — Superseded by Timeline Marker v1.5  
> **Retention:** Permanent (Immutable MCP Provenance Record)

---

<div align="center">

### ♿ “Accessibility refines attention to detail —  
each marker tells a clearer story when everyone can see it.”  
**— Kansas Frontier Matrix Accessibility & Design Council**

</div>
