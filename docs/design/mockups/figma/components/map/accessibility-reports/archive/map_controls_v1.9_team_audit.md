---
id: map_controls_v1.9_team_audit
title: Map Controls Component (v1.9) — Archived Accessibility Audit
author: accessibility.team
date: 2025-09-25
archived_on: 2025-10-08
archived_by: accessibility.team
status: archived
replaced_by: ../../../../accessibility-reports/map_controls_v2.0_team_audit.md
source_figma: https://www.figma.com/file/KFM_MAP_COMPONENTS/Library?node-id=350%3A400
plugin_used:
  - Able v2.3
  - Stark v4.1
criteria:
  - 1.4.3 Contrast (Minimum)
  - 2.1.1 Keyboard Navigation
  - 2.4.7 Focus Visible
  - 4.1.2 Name, Role, Value
  - 2.3.3 Animation from Interactions
result: fail
issues_found: 3
license: CC-BY-4.0
review_log: ../../../../../../../../../reviews/2025-09-25_map_controls_v1.9.md
linked_export: ../../../exports/archive/map_controls_v1.9.png
linked_metadata: ../../../metadata/archive/map_controls_v1.9.yml
related_docs:
  - ../../../../../../../../ui-guidelines.md
  - ../../../../../../../../style-guide.md
  - ../../../../../../../../interaction-patterns.md
---

# ♿ Archived Accessibility Audit — Map Controls (v1.9)

**Component:** Map Controls Cluster (Zoom · Compass · Reset · Layer Toggle)  
**Audit Date:** September 25, 2025  
**Reviewed by:** Accessibility Team (`accessibility.team`)  
**Status:** ❌ Fail — Superseded by Map Controls v2.0  

---

## 🎯 Context

The Map Controls v1.9 component introduced consolidated navigation controls for the **KFM interactive map**.  
During accessibility testing, it was found to have several **WCAG 2.1 AA** compliance issues related to color contrast, focus visibility, and ARIA role completeness.  
These issues were corrected in version 2.0, which became the first MCP-certified accessible release.

---

## 🧩 WCAG 2.1 Evaluation Results

| WCAG Ref | Criterion | Result | Notes |
|:--|:--|:--|:--|
| **1.4.3** | Contrast (Minimum) | ❌ Fail | Zoom button contrast 3.8 : 1; below minimum threshold. |
| **2.1.1** | Keyboard Navigation | ⚠️ Partial | Compass rotation skipped in tab order; buttons lacked logical sequence. |
| **2.4.7** | Focus Visible | ❌ Fail | Focus ring indistinguishable from background in dark mode. |
| **4.1.2** | Name, Role, Value | ⚠️ Partial | Missing `aria-pressed` states for toggle buttons. |
| **2.3.3** | Animation from Interactions | ✅ Pass | Button hover animation < 150 ms; compliant with reduced-motion. |

---

## 🧠 Summary of Findings

- ❌ **Contrast:** Control background and icons failed 1.4.3 minimum contrast ratio.  
- ❌ **Focus Visibility:** Focus indicators not perceivable in dark map mode.  
- ⚠️ **Keyboard Navigation:** Focus jumped inconsistently between grouped elements.  
- ⚠️ **ARIA Roles:** Some interactive toggles lacked explicit `aria-pressed` and `aria-label` attributes.  
- ✅ **Motion Safety:** Hover and interaction transitions met reduced-motion criteria.  

---

## 📊 Accessibility Metrics

| Metric | v1.9 Result | WCAG Target | v2.0 Result | Status |
|:--|:--|:--|:--|:--|
| Button Contrast | 3.8 : 1 | ≥ 4.5 : 1 | 4.9 : 1 | ✅ Fixed |
| Focus Ring Visibility | 2.3 : 1 | ≥ 3 : 1 | 3.5 : 1 | ✅ Fixed |
| Keyboard Navigation Coverage | 80 % | 100 % | 100 % | ✅ Fixed |
| ARIA Role Accuracy | Partial | Complete | 100 % | ✅ Fixed |
| Animation Duration | 150 ms | ≤ 200 ms | 150 ms | 🟢 Stable |

---

## 🧩 Developer Notes

- Introduced new contrast tokens (`--map-control-bg`, `--map-control-fg`) for color accessibility.  
- Replaced focus styles with high-contrast outline token `--focus-outline-accent`.  
- Standardized tab order: `[Zoom In] → [Zoom Out] → [Compass] → [Reset] → [Layer Toggle]`.  
- Added semantic ARIA roles and states for button elements.  
- Verified compliance using Able, Stark, Axe, and manual keyboard tests.  

---

## 🔗 Provenance Links

| Type | Path |
|:--|:--|
| **Replacement Audit** | [`../../../../accessibility-reports/map_controls_v2.0_team_audit.md`](../../../../accessibility-reports/map_controls_v2.0_team_audit.md) |
| **Metadata File** | [`../../../metadata/archive/map_controls_v1.9.yml`](../../../metadata/archive/map_controls_v1.9.yml) |
| **Design Export** | [`../../../exports/archive/map_controls_v1.9.png`](../../../exports/archive/map_controls_v1.9.png) |
| **Review Log** | [`../../../../../../../../../reviews/2025-09-25_map_controls_v1.9.md`](../../../../../../../../../reviews/2025-09-25_map_controls_v1.9.md) |
| **Figma Source** | [View in Figma →](https://www.figma.com/file/KFM_MAP_COMPONENTS/Library?node-id=350%3A400) |

---

## ♿ Regression Comparison (v1.9 → v2.0)

| Issue | v1.9 Result | v2.0 Result | Status |
|:--|:--|:--|:--|
| Contrast Ratio | ❌ 3.8 : 1 | ✅ 4.9 : 1 | ✅ Fixed |
| Focus Visibility | ❌ Invisible | ✅ Accent Outline (3.5 : 1) | ✅ Fixed |
| Keyboard Navigation | ⚠️ Incomplete | ✅ Sequential | ✅ Fixed |
| ARIA Labeling | ⚠️ Partial | ✅ Full | ✅ Fixed |
| Animation Timing | ✅ Pass | ✅ Pass | 🟢 Stable |

---

## 🧩 Reviewer Sign-Off

| Role | Reviewer | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-25 | ❌ Fail |
| UI Engineer | L. Daniels | 2025-09-25 | ⚠️ Requires Revision |
| Design Reviewer | A. Barta | 2025-09-25 | ✅ Approved for Redesign v2.0 |

---

## 🧾 Archive Notes

- **Deprecation Reason:** Insufficient focus contrast, incomplete keyboard traversal, missing ARIA attributes.  
- **Resolution:** v2.0 addressed all accessibility issues and passed WCAG 2.1 AA testing.  
- **Retention:** Permanently archived under MCP Accessibility Registry for regression tracking.  

---

> **License:** CC-BY-4.0  
> **Status:** Archived — Superseded by Map Controls v2.0  
> **Retention:** Permanent (Immutable MCP Provenance Record)

---

<div align="center">

### ♿ “Controls guide movement — accessibility ensures everyone can navigate.”  
**— Kansas Frontier Matrix Accessibility & Design Council**

</div>
