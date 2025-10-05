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
  - 4.1.2 Name, Role, Value
  - 2.3.3 Animation from Interactions
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
**Reviewed by:** Accessibility & Design Board (`accessibility.team`)  
**Status:** ❌ Fail — Superseded by Map View v2.1  

---

## 🎯 Context

The *Map View (v2.0)* served as the primary viewport for geospatial visualization  
within the Kansas Frontier Matrix, integrating basemaps, overlays, and timeline-linked layers.  
Accessibility evaluation revealed **contrast, focus, and ARIA labeling issues**, which prevented full WCAG 2.1 AA compliance.  
All identified deficiencies were addressed in **v2.1**, the first MCP-certified accessible release of the viewport.

---

## 🧩 WCAG 2.1 Evaluation Results

| WCAG Ref | Criterion | Result | Notes |
|:--|:--|:--|:--|
| **1.4.3** | Contrast (Minimum) | ⚠️ Partial | Overlay boundaries 4.1 : 1 contrast ratio (below 4.5 : 1). |
| **2.1.1** | Keyboard Navigation | ⚠️ Partial | Arrow key panning intermittently unresponsive. |
| **2.4.7** | Focus Visible | ❌ Fail | Focus outline indistinct; 2.5 : 1 contrast ratio. |
| **4.1.2** | Name, Role, Value | ⚠️ Partial | Missing ARIA region label for map viewport. |
| **2.3.3** | Animation from Interactions | ✅ Pass | Smooth transitions ≤ 200 ms; respects reduced motion settings. |

---

## 🧠 Summary of Findings

- ❌ **Focus Visibility:** Focus outlines difficult to detect against map background.  
- ⚠️ **Contrast:** Overlay lines and label text below WCAG minimum threshold.  
- ⚠️ **Keyboard Panning:** Arrow key focus sometimes lost during layer updates.  
- ⚠️ **ARIA Roles:** Missing or incomplete for map container and interactive layers.  
- ✅ **Motion Safety:** Animations met reduced-motion user preferences.  

---

## 📊 Accessibility Metrics

| Metric | v2.0 Result | WCAG Target | v2.1 Result | Status |
|:--|:--|:--|:--|:--|
| Overlay Contrast | 4.1 : 1 | ≥ 4.5 : 1 | 5.1 : 1 | ✅ Fixed |
| Focus Outline Visibility | 2.5 : 1 | ≥ 3 : 1 | 3.2 : 1 | ✅ Fixed |
| Keyboard Panning Coverage | 85 % | 100 % | 100 % | ✅ Fixed |
| ARIA Role Completeness | Partial | Complete | 100 % | ✅ Fixed |
| Animation Compliance | Pass | Pass | Pass | 🟢 Stable |

---

## 🧩 Developer Notes

- Added ARIA roles: `role="application"` and `aria-label="Interactive Map Viewport"`.  
- Introduced higher-contrast overlay colors via `--map-overlay-line` token.  
- Unified keyboard event handler for arrow keys and zoom (`+` / `-`) functions.  
- Implemented `--focus-outline-accent` token for consistent visibility.  
- Verified accessibility with Axe, Able, Stark, NVDA, and VoiceOver testing suites.  

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
| Overlay Contrast | ⚠️ 4.1 : 1 | ✅ 5.1 : 1 | ✅ Fixed |
| Focus Visibility | ❌ Poor | ✅ Accent Outline (3.2 : 1) | ✅ Fixed |
| Keyboard Navigation | ⚠️ Partial | ✅ Full Support | ✅ Fixed |
| ARIA Labeling | ⚠️ Missing | ✅ Added | ✅ Fixed |
| Motion Preferences | ✅ Pass | ✅ Pass | 🟢 Stable |

---

## 🧩 Reviewer Sign-Off

| Role | Reviewer | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-20 | ❌ Fail |
| UI Engineer | L. Daniels | 2025-09-20 | ⚠️ Revision Required |
| Design Reviewer | A. Barta | 2025-09-20 | ✅ Logged for Update in v2.1 |

---

## 🧾 Archive Notes

- **Deprecation Reason:** Failed to meet WCAG 2.1 AA criteria for focus visibility and contrast.  
- **Resolution:** Fixed in v2.1 with updated color tokens, event handlers, and ARIA enhancements.  
- **Retention:** Permanently preserved under MCP Accessibility Registry for provenance tracking.  

---

> **License:** CC-BY-4.0  
> **Status:** Archived — Superseded by Map View v2.1  
> **Retention:** Permanent (Immutable MCP Provenance Record)

---

<div align="center">

### ♿ “Maps help us find our way —  
accessibility ensures we can all get there.”  
**— Kansas Frontier Matrix Accessibility & Design Council**

</div>
