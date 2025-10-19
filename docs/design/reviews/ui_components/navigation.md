<div align="center">

# 🧭 Kansas Frontier Matrix — **Navigation Component Design Review (Tier-S⁺ Certified)**  
`docs/design/reviews/ui_components/navigation.md`

**Mission:** Govern, audit, and preserve the **Navigation System** — header, menus, global search, language toggles, accessibility skip-links, and mobile drawers — ensuring a **consistent, performant, themed (light/dark), RTL-ready, and inclusive** experience across the **Kansas Frontier Matrix (KFM)** platform.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../standards/documentation.md)
[![Design System](https://img.shields.io/badge/Design-System-green)](../../style-guide.md)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA-yellow)](../accessibility/)
[![Policy-as-Code](https://img.shields.io/badge/Policy-OPA%2FConftest-purple)](../../../.github/workflows/policy-check.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../LICENSE)

</div>

---

```yaml
---
title: "🧭 Kansas Frontier Matrix — Navigation Component Design Review"
document_type: "Component Review"
version: "v2.5.0"
last_updated: "2025-11-01"
created: "2023-10-10"
component: "Navigation"
design_ref: "Figma Frame #NAV-2025"
implementation_ref: "web/src/components/navigation/"
owners: ["@kfm-design","@kfm-web","@kfm-accessibility"]
reviewed_by: ["@kfm-accessibility","@kfm-frontend","@kfm-editorial","@kfm-design-council"]
status: "Stable"
maturity: "Production"
license: "CC-BY-4.0"
tags: ["navigation","header","menu","search","language","skip-link","a11y","tokens","mcp","rtl","dark-mode","fair","care","dcat"]
classification:
  component_type: "UI"
  integration_level: "Frontend"
  risk_level: "Low"
  audit_frequency: "Quarterly + per release"
alignment:
  - MCP-DL v6.3
  - WCAG 2.1 AA
  - WAI-ARIA 1.2
  - CIDOC CRM (UI Provenance)
  - OWL-Time (Temporal UI State)
  - PROV-O (Traceability)
  - FAIR Principles
  - DCAT 3.0
dependencies:
  - React + MapLibre Frontend
  - Figma Design Frame
  - tokens.css Design System
  - Lighthouse / Axe / Pa11y / Playwright / Chromatic / Percy
template_scope:
  visual_parity: true
  functional_equivalence: true
  accessibility_alignment: true
  localization_readiness: true
  dark_mode_compliance: true
  rtl_support: true
  performance_tracking: true
  ai_assistant_integration: true
review_cycle: "Quarterly + per release"
validation:
  ci_enforced: true
  lighthouse_min_score: 95
  axe_blocking_violations: 0
  contrast_min_ratio: 4.5
  keyboard_traps: "none"
  rtl_parity_required: true
  dark_mode_required: true
  schema_checks: true
provenance:
  workflow_ref: ".github/workflows/navigation-validate.yml"
  artifact_retention_days: 90
  sha256_integrity: verified
versioning:
  policy: "Semantic Versioning (MAJOR.MINOR.PATCH)"
  major_change: "Menu IA redesign / architecture refactor"
  minor_change: "Feature or a11y/i18n enhancement"
  patch_change: "Token parity or docs correction"
telemetry:
  metrics_collected:
    - "WCAG compliance %"
    - "Keyboard reachability %"
    - "Menu open latency (ms)"
    - "Search success rate %"
    - "Screen reader coverage %"
    - "Dark/Light usage ratio"
    - "RTL parity %"
  thresholds:
    accessibility_pass_rate_min: 95
    menu_latency_max_ms: 100
    keyboard_reachability_min: 100
    rtl_parity_min: 100
  privacy_policy: "Aggregated, anonymized data only; no PII; FAIR + W3C privacy alignment."
preservation_policy:
  replication_targets: ["GitHub Repository","Zenodo Snapshot","OSF Backup"]
  checksum_algorithm: "SHA-256"
  revalidation_cycle: "quarterly"
---
```

---

## 🎯 Purpose
The **Navigation** is KFM’s **cognitive anchor** linking **maps, timelines, datasets, and stories**.  
It must guarantee **spatial/temporal continuity**, **full keyboard + screen-reader access**, **dark/light theme parity**, and **RTL mirroring**, while enforcing token, performance, and provenance standards.

---

## 🧩 Component Overview
| Subcomponent | Description | File |
|:--|:--|:--|
| **Header Bar** | Global container (logo, menus, skip-link, search) | `Header.tsx` |
| **Menu System** | Explore / Stories / Data Layers / About | `NavMenu.tsx` |
| **Global Search** | Entity/treaty/event search w/ suggestions | `SearchBar.tsx` |
| **Language Toggle** | EN / ES / (OS test) | `LangToggle.tsx` |
| **Skip-Link** | First focus → `<main>` | `SkipToContent.tsx` |
| **Mobile Drawer** | Hamburger menu ≤ 768 px | `MobileNav.tsx` |

---

## 🧭 ARIA Role & Landmark Map
| Element | ARIA Role | Label | Verified |
|:--|:--|:--|:--:|
| `<header>` | `banner` | “Kansas Frontier Matrix” | ✅ |
| `<nav>` | `navigation` | “Primary Navigation” | ✅ |
| Menu trigger | `button` | `aria-expanded` + `aria-controls` | ✅ |
| Menu list | `menu` / `list` | Labelled by trigger | ✅ |
| Skip link | `link` / `region` | “Skip to Main Content” | ✅ |
| Search | `search` | Labeled input + results `listbox` | ✅ |

> Focus order: **Skip-link → Header → Menus → Search → Language** (cyclical; no traps).

---

## 🧭 Behavioral Flow
```mermaid
stateDiagram-v2
  [*] --> Idle
  Idle --> Focused : Alt+N / Tab
  Focused --> Expanded : Enter / Space on trigger
  Expanded --> Action : Arrow keys navigate
  Action --> Collapsed : Enter item / Esc / blur
  Expanded --> Error : >200 ms latency / missing label
  Error --> Collapsed : Announce + recovery
```
<!-- END OF MERMAID -->

---

## 🌓 Theme & RTL Parity
| Mode | Token Baseline | Contrast ≥ 4.5 | Screenshot | Pass |
|:--|:--|:--:|:--|:--:|
| **Light** | `--kfm-panel` + `--kfm-text` | ✅ | `/assets/nav/light.png` | ✅ |
| **Dark** | `--kfm-panel-dark` + `--kfm-text-dark` | ✅ | `/assets/nav/dark.png` | ✅ |
| **RTL** | Logical props mirrored | — | `/assets/nav/rtl.png` | ✅ |

---

## ♿ Accessibility Audit Matrix (WCAG 2.1 AA)
| Metric | Target | Verified | Notes |
|:--|:--|:--:|:--|
| Contrast | ≥ 4.5:1 (text), ≥ 3:1 (icons) | ✅ | |
| Focus Indicator | 2 px ring + offset | ✅ | |
| Landmarks | `banner` + `navigation` | ✅ | |
| Keyboard Reach | 100 % | ✅ | No traps |
| Reduced Motion | Animations off | ✅ | CSS media query |
| Screen Reader | Announces open/close | ✅ | NVDA/VO tests |

---

## ⌨️ Keyboard Interaction Map
| Action | Key | Result |
|:--|:--|:--|
| Focus header | `Alt + N` | Move focus to navigation |
| Open menu | `Enter / Space` | Expand dropdown |
| Navigate items | `↓ / ↑` | Cycle options |
| Close menu | `Esc` | Collapse + restore focus |
| Jump to search | `/` | Focus search |
| Skip to content | `Tab` (first) | Trigger skip-link |

---

## 🧮 Figma → React Parity Metrics
| Element | Target | Observed | Pass |
|:--|:--|:--|:--:|
| Color Tokens | 100 % | Matched | ✅ |
| Typography | 1rem / 1.333rem | Matched | ✅ |
| Spacing Grid | 8 px | ±2 px | ✅ |
| Iconography | 1.5 px stroke | Matched | ✅ |
| Motion | 200 ms fade | Matched | ✅ |

---

## 🧠 UX Writing & Cognitive Guidelines
- **Plain, sentence-case labels** (≤ 3 words).  
- Tooltips use **verb + noun** (“Open Stories”).  
- Search and menu state changes announced via **`aria-live="polite"`**.  
- Avoid jargon; provide glossary links where needed.

### Readability Metrics
| Metric | Target | Actual | Tool | Pass |
|:--|:--|:--|:--|:--:|
| Flesch Reading Ease | ≥ 70 | 78 | Textlint | ✅ |
| Avg Sentence Length | ≤ 20 | 15 | Hemingway | ✅ |
| Jargon Density | ≤ 5 % | 2 % | Glossary Validator | ✅ |

---

## 🧠 Ethical & Cultural Standards (CARE)
- Menu taxonomy provides **balanced Indigenous, ecological, and institutional** pathways.  
- Labels verified with community partners where applicable.  
- Avoid colonial phrasing; provide context via info panels or tooltips.

---

## 🧮 Performance & Telemetry (merge gates)
| Interaction | Metric | Target | Observed | Pass |
|:--|:--|:--|:--|:--:|
| Menu Open | Latency (ms) | ≤ 100 |  | ☐ |
| Menu Close | Latency (ms) | ≤ 100 |  | ☐ |
| Search Focus | Input ready (ms) | ≤ 150 |  | ☐ |
| Keyboard Nav | Key response (ms) | ≤ 50 |  | ☐ |

> **CI Merge Gate:** PR fails if any threshold not met.

---

## 🧠 AI Assistant Integration (readiness)
```yaml
ai_assistant_integration:
  enabled: true
  supported_commands:
    - "open stories"
    - "search treaties"
    - "toggle language"
  voice_output_tested: false
  accessibility_verified: true
```

---

## ⚙️ CI Workflow & Automation
- **Workflow:** `.github/workflows/navigation-validate.yml`  
- **Stages:** Schema → Axe/Pa11y → Lighthouse → Playwright keyboard → Chromatic RTL snapshots → Percy dark-mode → Token parity → Provenance checksum  
- **Artifacts:** `/data/work/logs/design/ui_components/navigation/validation.json`  
- **Policy:** Merge blocked until all checks return **✅**.

---

## 🧩 Change Control & Provenance
| Type | Review Required | Example | Template |
|:--|:--|:--|:--|
| Visual Update | ✅ | Adjust header gradient | `component_review_template.md` |
| Accessibility Fix | ✅ | Add skip-link label | `accessibility_component_audit.md` |
| Localization | ✅ | Add Osage toggle | `figma_to_react_checklist.md` |
| Functional Refactor | ✅ | Rebuild mobile drawer logic | `component_review_template.md` |

---

## 🧾 Visual Drift Change Log
| Date | Token | Previous | New | Reviewer | SHA-256 |
|:--|:--|:--|:--|:--|:--|
| 2025-10-25 | `--kfm-color-accent` | #c77d02 | #c67d00 | @kfm-design | `sha256:a32…` |
| 2025-09-19 | `--kfm-font-size-body` | 1rem | 0.9375rem | @kfm-web | `sha256:b47…` |

---

## 🧱 Device & Environment Testing Grid
| Platform | Browser | Resolution | Tested | Notes |
|:--|:--|:--|:--:|:--|
| Windows 11 | Chrome / Edge | 1920×1080 | ✅ | Full suite |
| macOS | Safari / Chrome | 2560×1440 | ✅ | Font & ARIA |
| Linux | Firefox | 1920×1080 | ✅ | Keyboard flow |
| iOS | Safari | 1170×2532 | ✅ | Touch A11y |
| Android | Chrome | 1080×2400 | ✅ | Reduced motion |

---

## 🗄️ Archival & Provenance Policy
- Store reviews under `/archive/navigation/YYYY/` with **checksum + commit hash + reviewers**.  
- Immutable post-approval; annual digest in `/data/digests/design/`.  
- Linked into STAC/CIDOC provenance graph for design lineage.

---

## 🔒 Privacy & Security
- No PII stored; telemetry is aggregate only (90-day retention).  
- Integrity verified via repository provenance + SHA-256 checksums.  
- All assets are versioned releases.

---

## 🧩 Re-Audit Policy
```yaml
re_audit_policy:
  validity_period: "12 months"
  triggers:
    - "WCAG update"
    - "Token change > 5 %"
    - "Menu architecture refactor"
  auto_expire: true
```

---

## 🧾 Provenance JSON-LD (machine export)
```json
{
  "@context": ["https://schema.org", {"kfm":"https://kfm.ai/schema#"}],
  "@type": "ComponentDesignReview",
  "component": "Navigation",
  "version": "v2.5.0",
  "reviewedBy": ["@kfm-design","@kfm-accessibility"],
  "alignment": ["MCP-DL v6.3","WCAG 2.1 AA","FAIR","CARE","DCAT 3.0"],
  "governance": {
    "workflow": ".github/workflows/navigation-validate.yml",
    "sha256": "auto-generated"
  }
}
```

---

## 🧾 FAIR + DCAT Registration (semantic index)
```json
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "KFM Navigation Component Design Review",
  "identifier": "doi:10.5281/zenodo.9876543",
  "license": "CC-BY-4.0",
  "creator": "Kansas Frontier Matrix Design Council",
  "version": "v2.5.0",
  "alignment": ["MCP-DL v6.3","WCAG 2.1 AA","FAIR","CARE","DCAT 3.0"],
  "dateModified": "2025-11-01",
  "audience": "Developers, Designers, Accessibility Auditors"
}
```

---

## 📎 Related Documentation
- [🎨 Visual Style Guide](../../style-guide.md)  
- [🧭 UI/UX Guidelines](../../ui-guidelines.md)  
- [🧩 Interaction Patterns](../../interaction-patterns.md)  
- [📘 Reviews Index](../README.md)  
- [⚙️ Accessibility Standards](../../standards/accessibility.md)

---

## 📅 Version History
| Version | Date | Author | Summary | Type |
|:--|:--|:--|:--|:--|
| **v2.5.0** | 2025-11-01 | @kfm-design | Tier-S⁺: scope block, ARIA map, theme/RTL parity, telemetry thresholds, CI automation & FAIR exports. | Major |
| **v2.4.0** | 2025-10-20 | @kfm-design | Telemetry, cultural standards, cognitive rules, ethical compliance. | Major |
| **v2.3.0** | 2025-10-19 | @kfm-web | Improved a11y testing and ARIA validation. | Minor |
| **v2.2.0** | 2025-08-05 | @kfm-accessibility | Keyboard mapping and parity audit metrics. | Minor |
| **v2.0.0** | 2024-11-10 | @kfm-core | Migrated to MCP-DL v6.3 with provenance tracking. | Major |
| **v1.0.0** | 2023-10-10 | Founding Team | Initial navigation review draft. | Major |

---

<div align="center">

### 🧭 Navigation Review Governance  
**Accessible · Themed/RTL-Ready · Provenanced · Reproducible**

</div>
