---
id: timeline_marker_v1.4_team_audit
title: Timeline Marker (v1.4) — Archived Accessibility Audit
author: accessibility.team
date: 2025-09-28
archived_on: 2025-10-07
archived_by: accessibility.team
status: archived
replaced_by: ../../timeline_marker_v1.5_team_audit.md
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
**Reviewed by:** Accessibility Team (`accessibility.team`)  
**Status:** ❌ Fail — Superseded by Timeline Marker v1.5  

---

## 🎯 Context

Timeline Marker v1.4 was designed to visually represent significant historical events  
along the timeline component, synchronized with map overlays.  
During testing, accessibility issues were found in **focus indicators**, **ARIA roles**,  
and **hover contrast states**, prompting a redesign in version 1.5.  
This document remains part of the MCP Accessibility Archive for historical traceability.

---

## 🧩 WCAG 2.1 Evaluation Results

| WCAG Ref | Criterion | Result | Notes |
|:--|:--|:--|:--|
| **1.4.3** | Contrast (Minimum) | ⚠️ Partial | Hover state contrast 4.1 : 1, below 4.5 : 1. |
| **2.1.1** | Keyboard Navigation | ✅ Pass | Markers fully reachable with `Tab` and `Enter`. |
| **2.4.7** | Focus Visible | ❌ Fail | Focus outline insufficiently visible on bright backgrounds. |
| **4.1.2** | Name, Role, Value | ⚠️ Partial | Missing ARIA roles on grouped markers; tooltip text not labeled. |

---

## 🧠 Summary of Findings

- ❌ **Focus Visibility:** The focus ring used an inactive accent tone, failing minimum 3:1 contrast.  
- ⚠️ **Contrast Deficiency:** Hover and selection colors did not meet text contrast ratio for light mode.  
- ⚠️ **ARIA Role Accuracy:** Tooltip and marker group elements lacked semantic roles and `aria-label` attributes.  
- ✅ **Keyboard Operability:** Interaction through keyboard input passed functional testing.  

---

## 📊 Accessibility Metrics

| Metric | v1.4 Result | WCAG Target | v1.5 Result | Status |
|:--|:--|:--|:--|:--|
| Hover Contrast | 4.1 : 1 | ≥ 4.5 : 1 | 4.9 : 1 | ✅ Fixed |
| Focus Ring Contrast | 2.6 : 1 | ≥ 3 : 1 | 3.5 : 1 | ✅ Fixed |
| ARIA Label Coverage | Partial | 100 % | 100 % | ✅ Fixed |
| Keyboard Navigation | 100 % | 100 % | 100 % | 🟢 Stable |

---

## 🧩 Developer Notes

- Introduced stronger focus outline via `--focus-outline-accent` token (used globally in v1.5).  
- Adjusted hover/active states using improved accent color tokens for consistent visibility.  
- Added ARIA roles (`button`) and `aria-describedby` for tooltip accessibility.  
- Improved keyboard traversal and focus restoration to timeline root after marker deselection.  
- Tooltips now follow reduced-motion guidelines using 150 ms fade transitions.  

---

## 🔗 Provenance Links

| Type | Path |
|:--|:--|
| **Replacement Audit** | [`../../timeline_marker_v1.5_team_audit.md`](../../timeline_marker_v1.5_team_audit.md) |
| **Metadata File** | [`../../../metadata/archive/timeline_marker_v1.4.yml`](../../../metadata/archive/timeline_marker_v1.4.yml) |
| **Design Export** | [`../../../exports/archive/timeline_marker_v1.4.png`](../../../exports/archive/timeline_marker_v1.4.png) |
| **Review Log** | [`../../../../../../../../../reviews/2025-09-28_timeline_marker_v1.4.md`](../../../../../../../../../reviews/2025-09-28_timeline_marker_v1.4.md) |
| **Figma Source** | [View in Figma →](https://www.figma.com/file/KFM_TIMELINE_DOCS/Component-Library?node-id=400%3A320) |

---

## ♿ Regression Comparison (v1.4 → v1.5)

| Issue | v1.4 Result | v1.5 Result | Status |
|:--|:--|:--|:--|
| Focus Outline Visibility | ❌ Poor (Inactive Accent) | ✅ Accent Outline (3.5 : 1) | ✅ Fixed |
| Hover Contrast | ⚠️ 4.1 : 1 | ✅ 4.9 : 1 | ✅ Fixed |
| ARIA Role Coverage | ⚠️ Partial | ✅ Complete | ✅ Fixed |
| Keyboard Access | ✅ Pass | ✅ Pass | 🟢 Stable |
| Tooltip Motion | ⚠️ Missing Preference Handling | ✅ Honors `prefers-reduced-motion` | ✅ Fixed |

---

## 🧩 Reviewer Sign-Off

| Role | Reviewer | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-28 | ❌ Fail |
| UI Engineer | L. Daniels | 2025-09-28 | ⚠️ Requires Redesign |
| Design Reviewer | A. Barta | 2025-09-28 | ✅ Approved for Iteration v1.5 |

---

## 🧾 Archive Notes

- **Deprecation Reason:** Failed focus and hover contrast compliance; incomplete ARIA role labeling.  
- **Resolution:** Fixed in v1.5 with enhanced contrast tokens, visible focus ring, and semantic roles.  
- **Retention:** Permanently preserved under MCP Accessibility Registry for regression tracking.  

---

> **License:** CC-BY-4.0  
> **Status:** Archived — Superseded by Timeline Marker v1.5  
> **Retention:** Permanent (Immutable MCP Provenance Record)

---

<div align="center">

### ♿ “Design doesn’t evolve in silence —  
each audit is a conversation between inclusion and intent.”  
**— Kansas Frontier Matrix Accessibility & Design Governance Council**

</div>
