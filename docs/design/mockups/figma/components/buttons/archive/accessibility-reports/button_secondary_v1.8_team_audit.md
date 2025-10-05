---
id: button_secondary_v1.8_team_audit
title: Secondary Button (v1.8) — Archived Accessibility Audit
author: accessibility.team
date: 2025-09-25
archived_on: 2025-10-06
archived_by: design.board
status: archived
replaced_by: ../../../metadata/button_secondary_v2.0.yml
source_figma: https://www.figma.com/file/HIJKL67890/KFM-Component-Library?node-id=210%3A450
plugin_used:
  - Able v2.3
  - Stark v4.1
criteria:
  - 1.4.3 Contrast (Minimum)
  - 1.4.11 Non-Text Contrast
  - 2.4.7 Focus Visible
  - 2.1.1 Keyboard Accessibility
result: fail
issues_found: 2
license: CC-BY-4.0
review_log: ../../../../../../../reviews/2025-09-25_button_secondary_v1.8.md
linked_export: ../../../exports/archive/button_secondary_v1.8.png
linked_metadata: ../../../metadata/archive/button_secondary_v1.8.yml
related_docs:
  - ../../../../../../ui-guidelines.md
  - ../../../../../../style-guide.md
  - ../../../../../../interaction-patterns.md
---

# ♿ Archived Accessibility Audit — Secondary Button (v1.8)

**Design Component:** Secondary Button (v1.8)  
**Audit Date:** September 25, 2025  
**Reviewed by:** Accessibility Team (`accessibility.team`)  
**Status:** Deprecated (Replaced by v2.0)  

---

## 🎯 Context

The Secondary Button (v1.8) served as the default non-primary action button in the KFM design system.  
During accessibility validation, several WCAG 2.1 AA compliance issues were found related to **border contrast** and **focus visibility**.

The following audit documents these findings, which informed design corrections implemented in **version 2.0**.

---

## 🧩 WCAG Evaluation Results

| WCAG Ref | Category | Result | Notes |
|:--|:--|:--|:--|
| **1.4.3** | Contrast (Text) | ✅ Pass | Text-to-background contrast = 4.7 : 1 (acceptable). |
| **1.4.11** | Non-Text Contrast | ❌ Fail | Border contrast 2.8 : 1 (below required 3:1). |
| **2.4.7** | Focus Visible | ⚠️ Partial | Focus outline not visible in dark mode. |
| **2.1.1** | Keyboard Accessibility | ✅ Pass | Full keyboard navigation supported. |

---

## 🧮 Summary of Findings

- **Border Visibility:**  
  The light gray border (`#d9d9d9`) failed contrast standards against the white background in light mode.  
  Updated in v2.0 to a darker neutral (`#a6a6a6`), meeting **3.2 : 1** ratio.

- **Focus Visibility:**  
  Focus ring color and thickness were inconsistent across themes.  
  Fixed in v2.0 with accent color outlines and increased stroke width.

- **Keyboard Navigation:**  
  No accessibility barriers found; tab order and focus restoration passed manual review.

---

## 📊 Accessibility Metrics

| Metric | v1.8 Result | WCAG Target | v2.0 Result | Status |
|:--|:--|:--|:--|:--|
| Text Contrast | 4.7 : 1 | ≥ 4.5 : 1 | 4.8 : 1 | ✅ Pass |
| Border Contrast | 2.8 : 1 | ≥ 3.0 : 1 | 3.2 : 1 | ✅ Fixed |
| Focus Outline | Inconsistent | Visible, 2px | Standardized | ✅ Fixed |
| Keyboard Navigation | Working | Working | Working | 🟢 Stable |

---

## 🧠 Developer Notes

- Original border token (`--color-border`) was replaced by new `--color-outline` variable in v2.0.  
- Focus ring thickness increased from **1px → 2px** for higher visibility.  
- Border color adjusted to meet **non-text contrast (1.4.11)** criteria.  
- Focus and hover states now honor **prefers-reduced-motion** in animation timing.  

---

## 🔗 Provenance Links

| Type | Path |
|:--|:--|
| **Replacement Metadata** | [`../../../metadata/button_secondary_v2.0.yml`](../../../metadata/button_secondary_v2.0.yml) |
| **Design Export** | [`../../../exports/archive/button_secondary_v1.8.png`](../../../exports/archive/button_secondary_v1.8.png) |
| **Review Log** | [`../../../../../../../reviews/2025-09-25_button_secondary_v1.8.md`](../../../../../../../reviews/2025-09-25_button_secondary_v1.8.md) |
| **Figma Source** | [View in Figma →](https://www.figma.com/file/HIJKL67890/KFM-Component-Library?node-id=210%3A450) |

---

## ♿ Regression Tracking

| Accessibility Category | v1.8 | v2.0 | Status |
|:--|:--|:--|:--|
| Border Contrast | 2.8 : 1 | 3.2 : 1 | ✅ Fixed |
| Focus Ring Visibility | Inconsistent | Consistent | ✅ Fixed |
| Keyboard Navigation | Full | Full | 🟢 Stable |
| Reduced Motion | None | Supported | 🟢 Improved |

---

## 🧩 Reviewer Sign-Off

| Role | Reviewer | Date | Result |
|:--|:--|:--|:--|
| Accessibility Lead | M. Jordan | 2025-09-25 | ⚠️ Revision Required |
| UI Engineer | L. Daniels | 2025-09-25 | ✅ Approved for v2.0 redesign |
| Design Reviewer | A. Barta | 2025-09-25 | ✅ Confirmed archival compliance |

---

## 🧾 Archive Notes

- Archived on **October 6, 2025**, following implementation of **v2.0** improvements.  
- This record provides evidence of **WCAG 1.4.11 compliance evolution**.  
- Retained permanently under MCP archival policy for accessibility regression tracking.

---

> **License:** CC-BY-4.0  
> **Status:** Archived for provenance and accessibility comparison with version 2.0.

---

<div align="center">

### ♿ “Every improvement starts with an honest audit —  
accessibility evolves through iteration.”  
**— Kansas Frontier Matrix Accessibility & Design Council**

</div>
