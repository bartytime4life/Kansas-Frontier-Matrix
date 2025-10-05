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

**Component:** Map Controls Cluster (Zoom, Compass, Reset, Layer Toggle)  
**Audit Date:** September 25, 2025  
**Reviewed by:** Accessibility Team (`accessibility.team`)  
**Status:** ❌ Fail — Superseded by Map Controls v2.0  

---

## 🎯 Context

The *Map Controls (v1.9)* introduced a unified navigation cluster for the KFM interactive map interface.  
While visually functional, it failed several **WCAG 2.1 AA** requirements, including color contrast,  
keyboard focus order, and ARIA role compliance.  
These issues were corrected in version 2.0, which achieved full MCP accessibility certification.

---

## 🧩 WCAG 2.1 Evaluation Results

| WCAG Ref | Criterion | Result | Notes |
|:--|:--|:--|:--|
| **1.4.3** | Contrast (Minimum) | ❌ Fail | Zoom button contrast 3.8 : 1 under dark theme (below 4.5 : 1). |
| **2.1.1** | Keyboard Navigation | ⚠️ Partial | Compass rotation skipped via `Tab`; buttons lacked logical order. |
| **2.4.7** | Focus Visible | ❌ Fail | Focus outlines faint and hard to perceive. |
| **4.1.2** | Name, Role, Value | ⚠️ Partial | Missing `aria-pressed` states for toggle buttons. |
| **2.3.3** | Animation from Interactions | ✅ Pass | Hover animation ≤ 150 ms; honors reduced-motion setting. |

---

## 🧠 Summary of Findings

- ❌ **Contrast:** Button contrast below WCAG 1.4.3 threshold; inaccessible on dark basemaps.  
- ❌ **Focus Visibility:** No visible focus state in several components.  
- ⚠️ **Keyboard Navigation:** Inconsistent tab traversal between buttons.  
- ⚠️ **ARIA Compliance:** Lacked descriptive roles and state attributes.  
- ✅ **Motion Safety:** All animations passed reduced-motion checks.  

---

## 📊 Accessibility Metrics

| Metric | v1.9 Result | WCAG Target | v2.0 Result | Status |
|:--|:--|:--|:--|:--|
| Button Contrast | 3.8 : 1 | ≥ 4.5 : 1 | 4.9 : 1 | ✅ Fixed |
| Focus Ring Visibility | 2.3 : 1 | ≥ 3 : 1 | 3.5 : 1 | ✅ Fixed |
| Keyboard Navigation | Partial | Full | Full | ✅ Fixed |
| ARIA Role Accuracy | Partial | Complete | Complete | ✅ Fixed |
| Animation Duration | 150 ms | ≤ 200 ms | 150 ms | 🟢 Stable |

---

## 🧩 Developer Notes

- Updated color tokens (`--map-control-bg`, `--map-control-fg`) for higher contrast.  
- Implemented a visible focus outline using `--focus-outline-accent`.  
- Standardized tab order: `[Zoom In] → [Zoom Out] → [Compass] → [Reset] → [Layer Toggle]`.  
- Added semantic ARIA attributes (`aria-pressed`, `aria-label`) to all toggle buttons.  
- Verified accessibility using Able, Stark, Axe, and NVDA screen reader.  

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
| Button Contrast | ❌ 3.8 : 1 | ✅ 4.9 : 1 | ✅ Fixed |
| Focus Visibility | ❌ Faint | ✅ Accent Outline Added | ✅ Fixed |
| Keyboard Navigation | ⚠️ Partial | ✅ Sequential | ✅ Fixed |
| ARIA Roles | ⚠️ Incomplete | ✅ Full | ✅ Fixed |
| Animation | ✅ Pass | ✅ Pass | 🟢 Stable |

---

## 🧩 Reviewer Sign-Off

| Role | Reviewer | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-25 | ❌ Fail |
| UI Engineer | L. Daniels | 2025-09-25 | ⚠️ Requires Revision |
| Design Reviewer | A. Barta | 2025-09-25 | ✅ Logged for Update in v2.0 |

---

## 🧾 Archive Notes

- **Deprecation Reason:** Failed WCAG 2.1 AA contrast and focus visibility standards.  
- **Resolution:** v2.0 fixed all issues via updated color tokens, visible outlines, and improved ARIA labeling.  
- **Retention:** Permanently archived under MCP Accessibility Registry for regression verification.  

---

> **License:** CC-BY-4.0  
> **Status:** Archived — Superseded by Map Controls v2.0  
> **Retention:** Permanent (Immutable MCP Provenance Record)

---

<div align="center">

### ♿ “Accessibility keeps navigation meaningful —  
controls should guide all users equally.”  
**— Kansas Frontier Matrix Accessibility & Design Council**

</div>
