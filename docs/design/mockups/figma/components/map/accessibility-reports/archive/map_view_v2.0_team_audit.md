---
id: map_view_v2.0_team_audit
title: Map View Component (v2.0) — Archived Accessibility Audit
author: accessibility.team
date: 2025-09-20
archived_on: 2025-10-08
archived_by: accessibility.team
status: archived
replaced_by: ../../../../accessibility-reports/map_view_v2.1_team_audit.md
source_figma: https://www.figma.com/file/KFM_MAP_COMPONENTS/Library?node-id=300%3A420
plugin_used:
  - Able v2.3
  - Stark v4.1
criteria:
  - 1.4.3 Contrast (Minimum)
  - 2.1.1 Keyboard Navigation
  - 2.4.7 Focus Visible
  - 2.3.3 Animation from Interactions
  - 4.1.2 Name, Role, Value
result: fail
issues_found: 3
license: CC-BY-4.0
review_log: ../../../../../../../../../reviews/2025-09-20_map_view_v2.0.md
linked_export: ../../../exports/archive/map_view_v2.0.png
linked_metadata: ../../../metadata/archive/map_view_v2.0.yml
related_docs:
  - ../../../../../../../../ui-guidelines.md
  - ../../../../../../../../style-guide.md
  - ../../../../../../../../interaction-patterns.md
---

# ♿ Archived Accessibility Audit — Map View (v2.0)

**Component:** Interactive Map Viewport  
**Audit Date:** September 20, 2025  
**Reviewed by:** Accessibility Team (`accessibility.team`)  
**Status:** ❌ Fail — Superseded by Map View v2.1  

---

## 🎯 Context

The *Map View (v2.0)* component provided the primary interactive viewport for the **Kansas Frontier Matrix (KFM)** system,  
rendering geospatial layers, historical overlays, and timeline-synchronized data.  

Accessibility evaluation identified several critical issues related to **contrast**, **focus visibility**, and **keyboard panning support**.  
These shortcomings were remediated in version **v2.1**, achieving full WCAG 2.1 AA compliance and MCP accessibility certification.

---

## 🧩 WCAG 2.1 Evaluation Results

| WCAG Ref | Criterion | Result | Notes |
|:--|:--|:--|:--|
| **1.4.3** | Contrast (Minimum) | ⚠️ Partial | Vector overlays 4.1 : 1, below 4.5 : 1 threshold. |
| **2.1.1** | Keyboard Navigation | ⚠️ Partial | Arrow key panning intermittent; keyboard zoom inconsistent. |
| **2.4.7** | Focus Visible | ❌ Fail | Focus ring faint in dark mode; contrast < 3 : 1. |
| **2.3.3** | Animation from Interactions | ✅ Pass | Transition animations < 200 ms, motion preferences respected. |
| **4.1.2** | Name, Role, Value | ⚠️ Partial | Missing `aria-label` for dynamic map layers and tooltips. |

---

## 🧠 Summary of Findings

- ⚠️ **Contrast Deficiency:** Base map tiles and overlay boundaries insufficient under certain color themes.  
- ❌ **Focus Ring Visibility:** Focus outlines not easily perceivable against dynamic background tiles.  
- ⚠️ **Keyboard Navigation:** Arrow panning and `+`/`-` zoom operations inconsistent in some browsers.  
- ⚠️ **ARIA Labeling:** Map not fully described to assistive technologies.  
- ✅ **Motion Preference Compliance:** Camera transitions respect user reduced-motion settings.  

---

## 📊 Accessibility Metrics

| Metric | v2.0 Result | WCAG Target | v2.1 Result | Status |
|:--|:--|:--|:--|:--|
| Contrast Ratio | 4.1 : 1 | ≥ 4.5 : 1 | 5.1 : 1 | ✅ Fixed |
| Focus Outline Contrast | 2.5 : 1 | ≥ 3 : 1 | 3.2 : 1 | ✅ Fixed |
| Keyboard Navigation Coverage | 85 % | 100 % | 100 % | ✅ Fixed |
| ARIA Label Accuracy | Partial | Complete | 100 % | ✅ Fixed |
| Motion Compliance | Pass | Pass | Pass | 🟢 Stable |

---

## 🧩 Developer Notes

- Improved contrast by updating color tokens (`--map-base-fg`, `--overlay-line-accent`).  
- Added keyboard handlers for continuous panning using arrow keys and smooth zoom with `+`/`-`.  
- Implemented `role="application"` and `aria-label="Interactive Map Viewport"` for accessibility.  
- Unified focus ring color across basemap and overlay layers using `--focus-outline-accent`.  
- Conducted testing with NVDA, VoiceOver, and Axe accessibility plugin.  

---

## 🔗 Provenance Links

| Type | Path |
|:--|:--|
| **Replacement Audit** | [`../../../../accessibility-reports/map_view_v2.1_team_audit.md`](../../../../accessibility-reports/map_view_v2.1_team_audit.md) |
| **Metadata File** | [`../../../metadata/archive/map_view_v2.0.yml`](../../../metadata/archive/map_view_v2.0.yml) |
| **Design Export** | [`../../../exports/archive/map_view_v2.0.png`](../../../exports/archive/map_view_v2.0.png) |
| **Review Log** | [`../../../../../../../../../reviews/2025-09-20_map_view_v2.0.md`](../../../../../../../../../reviews/2025-09-20_map_view_v2.0.md) |
| **Figma Source** | [View in Figma →](https://www.figma.com/file/KFM_MAP_COMPONENTS/Library?node-id=300%3A420) |

---

## ♿ Regression Comparison (v2.0 → v2.1)

| Issue | v2.0 Result | v2.1 Result | Status |
|:--|:--|:--|:--|
| Map Overlay Contrast | ⚠️ 4.1 : 1 | ✅ 5.1 : 1 | ✅ Fixed |
| Focus Visibility | ❌ Faint | ✅ Accent Ring Visible | ✅ Fixed |
| Keyboard Panning | ⚠️ Partial | ✅ Full Support | ✅ Fixed |
| ARIA Labeling | ⚠️ Missing | ✅ Added | ✅ Fixed |
| Reduced Motion | ✅ Pass | ✅ Pass | 🟢 Stable |

---

## 🧩 Reviewer Sign-Off

| Role | Reviewer | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-20 | ❌ Fail |
| UI Engineer | L. Daniels | 2025-09-20 | ⚠️ Requires Revision |
| Design Reviewer | A. Barta | 2025-09-20 | ✅ Logged for Correction in v2.1 |

---

## 🧾 Archive Notes

- **Deprecation Reason:** Map focus and overlay contrast issues underperformed against WCAG 2.1 AA metrics.  
- **Resolution:** Version 2.1 introduced refined color tokens, ARIA roles, and keyboard improvements.  
- **Retention:** Permanently archived under MCP Accessibility Registry for traceability and comparison.  

---

> **License:** CC-BY-4.0  
> **Status:** Archived — Superseded by Map View v2.1  
> **Retention:** Permanent (Immutable MCP Provenance Record)

---

<div align="center">

### ♿ “Accessibility gives maps their compass —  
it ensures everyone can find their way.”  
**— Kansas Frontier Matrix Accessibility & Design Governance Council**

</div>
