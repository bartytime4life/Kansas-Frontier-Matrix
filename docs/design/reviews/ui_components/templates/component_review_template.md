<div align="center">

# 🧾 Kansas Frontier Matrix — **Component Review Template**  
`docs/design/reviews/ui_components/templates/component_review_template.md`

**Mission:** Standardize how **UI component design reviews** are created, documented, and validated within the **Kansas Frontier Matrix (KFM)** system.  
This template ensures each review is **MCP-DL v6.3**, **FAIR**, and **WCAG 2.1 AA** compliant — capturing **design provenance**, **accessibility validation**, and **governance sign-off** for every component.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../../standards/documentation.md)
[![Design Governance](https://img.shields.io/badge/Governance-Audited-green)](../../../../../docs/design/README.md)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../../accessibility/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../../LICENSE)

</div>

---

```yaml
---
title: "<🧩 Component Name> — Design Review"
document_type: "Component Review"
version: "vX.X.X"
last_updated: "YYYY-MM-DD"
created: "YYYY-MM-DD"
component: "<component_name>"
design_ref: "Figma Frame #XXXX"
implementation_ref: "web/src/components/<path>/"
owners: ["@kfm-design","@kfm-accessibility"]
reviewed_by: ["@kfm-web","@kfm-data","@kfm-ethics"]
status: "In Review"
maturity: "Pre-Release"
license: "CC-BY-4.0"
tags: ["ui","component","review","accessibility","mcp","tokens","design-system"]
alignment:
  - MCP-DL v6.3
  - WCAG 2.1 AA
  - FAIR Principles
  - CIDOC CRM
  - PROV-O
dependencies:
  - React + MapLibre
  - tokens.css Design System
  - Lighthouse / Axe / Pa11y
validation:
  axe_score: ""
  lighthouse_score: ""
  schema_verified: ""
  performance_benchmark: ""
  accessibility_verified: ""
  documentation_complete: ""
governance:
  design_council_review: "Pending"
  accessibility_review: "Pending"
  ethics_review: "Pending"
preservation_policy:
  replication_targets: ["GitHub Repository","Zenodo Snapshot"]
  checksum_algorithm: "SHA-256"
  revalidation_cycle: "quarterly"
---
```

---

## 🎯 Component Overview

| Field | Description |
|:--|:--|
| **Component Name** | Name of the UI element (e.g., Navigation Bar, Legend, Map Control). |
| **Purpose** | Short, plain-language description of the component’s mission within KFM. |
| **Owner** | Responsible person/team maintaining this component. |
| **Dependencies** | Technologies, data pipelines, or frameworks this component relies on. |
| **Design Reference** | Link to the Figma design source. |
| **Implementation Path** | Link to the actual React or Python implementation. |

---

## 🧠 Purpose & Context

Provide a **clear narrative** explaining how this component contributes to KFM’s visual, narrative, and accessibility goals.  
Focus on:
- Its role in the **map/timeline ecosystem**
- The **data or story context** it supports
- Any **AI or Focus Mode integration**

---

## 🧩 Design Provenance

| Design Source | Implementation Source | Verified | SHA-256 Checksum |
|:--|:--|:--:|:--|
| Figma Frame | React Component | ☐ | `sha256:...` |
| Mockup Screenshot | Live Preview | ☐ | `sha256:...` |
| Token Reference | CSS Variables | ☐ | `sha256:...` |

✅ **Goal:** Demonstrate reproducibility between design intent and implementation output.

---

## 🧮 Accessibility Validation Summary

| Test | Tool | Score | Pass/Fail | Notes |
|:--|:--|:--|:--|:--|
| **Color Contrast** | Pa11y | 4.8:1 | ✅ | Meets WCAG AA |
| **Keyboard Navigation** | Playwright | 100 % reachable | ✅ | All interactive elements focusable |
| **Screen Reader Output** | NVDA / VoiceOver | 100 % | ✅ | Announces all controls |
| **ARIA Roles** | Axe-core | Verified | ✅ | Proper roles present |
| **Reduced Motion Support** | Manual | Verified | ✅ | Motion off when set |

✅ **Attach screenshots or logs from automated runs.**

---

## 🧱 Design-to-Implementation Checklist

| Category | Figma Reference | Implementation Result | Verified |
|:--|:--|:--|:--:|
| **Color Tokens** | `--kfm-color-accent` | Matches React styles | ✅ |
| **Typography Scale** | H1 2.0rem / Body 1.0rem | Verified in dev tools | ✅ |
| **Spacing System** | 8px grid | Matches layout | ✅ |
| **Icons / SVGs** | Lucide / Heroicons | Matching set | ✅ |
| **Motion / Easing** | 200ms fade | Consistent | ✅ |

---

## ♿ Accessibility Review Notes

- ✅ WCAG 2.1 AA verified.  
- ☐ Keyboard traps identified/resolved.  
- ☐ Live region (ARIA) feedback functional.  
- ☐ Focus outlines visible and distinct.  
- ☐ Mobile gesture parity verified.  

> Include reference screenshots and audit file paths.

---

## 🧭 Performance Benchmarks

| Metric | Target | Actual | Tool |
|:--|:--|:--|:--|
| **Load Time** | < 200 ms |  | Lighthouse |
| **Interaction Latency** | < 100 ms |  | DevTools |
| **Memory Footprint** | < 10 MB |  | Chrome Profiler |
| **Accessibility Score** | ≥ 95 |  | Lighthouse / Axe |

✅ Include CI summary from automated tests under `/data/work/logs/`.

---

## 🧾 Provenance Metadata (JSON Example)

```json
{
  "@context": ["https://schema.org", {"kfm": "https://kfm.ai/schema#"}],
  "@type": "UIComponentReview",
  "component": "<component_name>",
  "version": "vX.X.X",
  "reviewedBy": ["@kfm-accessibility","@kfm-web"],
  "alignment": ["MCP-DL v6.3","WCAG 2.1 AA","FAIR Principles"],
  "provenance": {
    "workflow": ".github/workflows/design-template.yml",
    "sha256": "auto-generated"
  }
}
```

---

## 🧠 Cognitive & Ethical Considerations

| Category | Description | Verified |
|:--|:--|:--:|
| **Cognitive Load** | Information hierarchy follows logical order; minimal nested interactions. | ☐ |
| **Tone & Clarity** | Labels and tooltips use clear, non-technical phrasing. | ☐ |
| **Cultural Representation** | Dataset or labels avoid bias; verified by Ethics Council. | ☐ |
| **Reduced Motion Mode** | Visuals respect user preferences. | ☐ |
| **AI Integration** | If used, transparent model metadata displayed. | ☐ |

---

## 🧩 Governance Sign-Off

| Review Type | Reviewer | Date | Status | Notes |
|:--|:--|:--|:--:|:--|
| **Accessibility Review** | @kfm-accessibility |  | ☐ |  |
| **Design Validation** | @kfm-design |  | ☐ |  |
| **Ethics Review** | @kfm-ethics |  | ☐ |  |
| **Data Provenance Audit** | @kfm-data |  | ☐ |  |
| **Governance Council Sign-Off** | @kfm-design-council |  | ☐ |  |

✅ **All governance fields must be completed before merging review documentation.**

---

## 🗄️ Archival Policy

- Review results stored under `/docs/design/reviews/ui_components/archive/<component_name>/`.  
- Metadata checksums (`.sha256`) generated automatically by CI.  
- Immutable once merged and archived with Zenodo DOI snapshot.  
- Linked in governance logs at `/data/digests/design/ui_components/`.

---

## 🧩 Template Use Notes

> 🔹 Use this file as the basis for every **component-level review**.  
> 🔹 Never modify archived review versions — always bump the version number.  
> 🔹 Attach JSON-LD provenance block and WCAG results before governance approval.  
> 🔹 Maintain parity between design tokens and implementation.  

---

## 🧩 Version Control & Provenance Summary

```yaml
mcp_certification: "Tier-A+++"
review_type: "Component Design Review"
checksum: "sha256:<auto>"
validated_by: "@kfm-governance-bot"
archived_on: "<YYYY-MM-DD>"
repository_ref: "https://github.com/bartytime4life/Kansas-Frontier-Matrix/"
```

---

<div align="center">

### 🧾 Kansas Frontier Matrix — Component Review Template  
**Reproducible · Accessible · Ethical · Provenanced**

<!-- MCP-CERTIFIED: TIER=A+++ -->
<!-- VERIFIED-STANDARDS: [MCP-DL v6.3, FAIR, WCAG 2.1 AA] -->
<!-- VALIDATION-HASH: sha256:templatecomponentreviewxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -->

</div>
