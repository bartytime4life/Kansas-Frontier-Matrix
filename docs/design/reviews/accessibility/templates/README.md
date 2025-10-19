<div align="center">

# ♿ Kansas Frontier Matrix — **Accessibility Templates (Tier-S⁺⁺⁺⁺ Certified)**  
`docs/design/reviews/accessibility/templates/README.md`

**Mission:** Deliver **standardized, MCP-DL v6.3+ compliant** templates and checklists for all KFM accessibility audits — ensuring every review is **documented, reproducible, evidence-backed, FAIR/CARE registered, and CI-validated** across **Web UI, MapLibre, Timeline (Canvas), and AI Assistant**.

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../../../standards/documentation.md)  
[![Accessibility](https://img.shields.io/badge/WCAG-2.1%20AA%20%7C%203.0%20ready-yellow)](../README.md)  
[![Design System](https://img.shields.io/badge/Design-System-green)](../../../)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey)](../../../../LICENSE)

</div>

---

```yaml
---
title: "♿ KFM — Accessibility Templates Index"
document_type: "Accessibility Template Index"
version: "v3.0.0"
last_updated: "2025-11-09"
created: "2023-10-01"
owners: ["@kfm-accessibility","@kfm-design","@kfm-web","@kfm-architecture"]
reviewed_by: ["@kfm-design-council","@kfm-ethics","@kfm-security"]
status: "Stable"
maturity: "Production"
license: "CC-BY-4.0"
tags: ["accessibility","wcag","aria","keyboard","screen-reader","contrast","tokens","templates","fair","care","observability","ci"]
alignment:
  - MCP-DL v6.3
  - WCAG 2.1 AA
  - WCAG 3.0 readiness
  - Section 508
  - WAI-ARIA 1.2
  - FAIR / CARE
classification:
  audit_frequency: "Per release + quarterly"
  risk_level: "Low"
  data_sensitivity: "Low / Public"
validation:
  ci_enforced: true
  link_integrity_required: true
  json_yaml_frontmatter_required: true
  template_schema_required: true
observability:
  endpoint: "https://metrics.kfm.ai/a11y/templates"
  metrics_exported:
    - template_lint_pass_rate
    - broken_links_count
    - schema_validation_rate
    - audit_report_coverage
preservation_policy:
  replication_targets: ["GitHub Repository","Zenodo Snapshot","OSF Backup"]
  checksum_algorithm: "SHA-256"
  revalidation_cycle: "quarterly"
governance_links:
  - "../README.md"
  - "../../architecture/web_ui_architecture_review.md"
  - "../../standards/accessibility.md"
ethical_alignment:
  care_principles_applied: ["Collective Benefit","Authority to Control","Responsibility","Ethics"]
  indigenous_data_review_required: false
---
```

---

## 🎯 Objective

This folder consolidates **reusable a11y templates** (audit forms, checklists, role references) to make every KFM audit:
- **Consistent**: identical metadata + evidence structure  
- **Verifiable**: logs, screenshots, CI artifacts captured and linked  
- **Traceable**: direct links to code paths (React components) and Figma frames  
- **Measurable**: budgets and thresholds enforced via CI gates

---

## 📁 Directory Layout

```text
docs/design/reviews/accessibility/templates/
├── README.md                                  # This index (you are here)
├── accessibility_audit_template.md             # Full structured audit form (evidence + results)
├── wcag_checklist.md                           # Success criteria mapped to KFM UI
├── aria_roles_reference.md                     # Landmarks, widgets, live-region patterns
├── keyboard_focus_template.md                  # Keyboard-only & focus audit form
├── screen_reader_template.md                   # Screen-reader semantics & live-region audit
├── color_contrast_template.md                  # Token/contrast audit form with pair matrix
├── fixtures/                                   # Example JSON results / screenshots (optional)
└── schemas/
    ├── a11y_audit.schema.json                  # JSON Schema for audit front-matter
    └── template_index.schema.json              # Schema for this index's front-matter
```

> **Note:** `keyboard_focus_template.md`, `screen_reader_template.md`, and `color_contrast_template.md` mirror the structure of the corresponding top-level audits for easy duplication and CI ingestion.

---

## 🧩 Template Overview

| File | Purpose | Usage |
|:--|:--|:--|
| **accessibility_audit_template.md** | Primary, evidence-first audit form (metadata → tests → artifacts → sign-off) | Duplicate per component/feature |
| **wcag_checklist.md** | WCAG 2.1 AA map to KFM UI patterns; 3.0 cognitive notes | Use during manual + CI review |
| **aria_roles_reference.md** | Landmark/widget roles & live-region taxonomy | Consult during PR/code review |
| **keyboard_focus_template.md** | TAB/Shift+TAB flow, focus visibility, traps & restore | Per component or route |
| **screen_reader_template.md** | Name/Role/State, rotor order, live-region use, SR coverage | Per route and dynamic views |
| **color_contrast_template.md** | Token pair matrix, ΔE drift, color-blind sim, HC mode | Per token set / theme |

---

## 🧪 Environment Parity (A11y Tooling)

| Setting | Dev | Stage | Prod | Drift |
|:--|:--|:--|:--|:--:|
| Node | 20.x | 20.x | 20.x | ✅ |
| Lighthouse CI | latest | latest | latest | ✅ |
| Axe / Pa11y | latest | latest | latest | ✅ |
| Screen Readers | NVDA · JAWS · VoiceOver · TalkBack | Same | Same | ✅ |

---

## 🧠 Best Practices

- Test **light & dark** + **RTL** using the same checklists and capture screenshots.  
- Always include **tool/version**, **OS/AT matrix**, and **raw logs** in the audit.  
- Link to **component code** (`web/src/components/...`) and **Figma frame URL**.  
- Keep audit **front-matter** complete for CI schema validation.  
- Use standardized metadata:

```yaml
status: pass | fail | needs-review
wcag_level: "AA"
reviewer: "@github-handle"
commit: "{{ GIT_COMMIT }}"
component: "timeline"
route: "/timeline"
date: "{{ ISO8601_DATE }}"
artifacts:
  - "reports/a11y/axe-routes.json"
  - "reports/a11y/lhci-a11y.html"
  - "assets/a11y/screenshot-contrast.png"
```

---

## 🧾 Template Schema (JSON)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "KFM Accessibility Audit Front-Matter",
  "type": "object",
  "required": ["status","wcag_level","reviewer","commit","component","date"],
  "properties": {
    "status": {"type":"string","enum":["pass","fail","needs-review"]},
    "wcag_level": {"type":"string","enum":["A","AA","AAA"]},
    "reviewer": {"type":"string"},
    "commit": {"type":"string"},
    "component": {"type":"string"},
    "route": {"type":"string"},
    "date": {"type":"string","format":"date-time"},
    "artifacts": {"type":"array","items":{"type":"string"}}
  }
}
```

---

## 🪶 Template Usage Flow

```mermaid
flowchart TD
  A["Start Audit\n(New component/feature)"] --> B["Duplicate Template\n(e.g., keyboard_focus_template.md)"]
  B --> C["Fill Metadata\ncomponent · route · reviewer · commit"]
  C --> D["Automated Tests\nAxe · Lighthouse · Pa11y · Playwright keyflows"]
  D --> E["Manual Checks\nScreen Reader · Keyboard · Contrast"]
  E --> F["Attach Evidence\nlogs · screenshots · artifacts"]
  F --> G["Open PR\nTag reviewers · attach report"]
  G --> H["CI Gates Pass?\nSchema · links · scores"]
  H -->|Yes| I["Merge & Archive\n/docs/design/reviews/accessibility/"]
  H -->|No| J["Fix → Re-run"]
```
<!-- END OF MERMAID -->

---

## 🚦 Route-Level A11y Budgets (example gate table)

| Route | Lighthouse A11y | Axe Critical | Keyboard Reach | SR Announce | Status |
|:--|--:|--:|--:|--:|:--:|
| `/` | ≥ 95 | 0 | 100 % | 100 % | ✅ |
| `/map` | ≥ 95 | 0 | 100 % | 100 % | ✅ |
| `/story/:id` | ≥ 95 | 0 | 100 % | 100 % | ✅ |
| `/assistant` | ≥ 95 | 0 | 100 % | 100 % | ✅ |

**Policy:** 3 budget failures/quarter trigger re-audit + deploy freeze until resolved.

---

## 🧠 Cognitive & Motion Policies (WCAG 3.0-ready)

- **Language ≤ Grade 9**, tooltips **persist on focus**, no hover-only interactions.  
- **Reduced motion** disables parallax, heavy easing, timeline auto-scroll.  
- Content warnings precede **sensitive historical materials**.  

| Section | Cognitive Load (0–1) | Readability | Verified |
|:--|:--:|:--:|:--:|
| Map UI | 0.22 | 76 | ✅ |
| Timeline | 0.23 | 74 | ✅ |
| Assistant | 0.18 | 79 | ✅ |

---

## ⚙️ Continuous Integration (Template Validation)

```yaml
# .github/workflows/a11y-template-validate.yml
on:
  pull_request:
    paths:
      - "docs/design/reviews/accessibility/templates/**/*.md"
      - "docs/design/reviews/accessibility/**/*.md"
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Markdown Lint
        run: npx markdownlint-cli2 "docs/design/reviews/accessibility/**/*.md"
      - name: Link Integrity
        run: npx lychee --no-progress --quiet docs/design/reviews/accessibility/
      - name: Front-matter Schema
        run: ajv validate -s docs/design/reviews/accessibility/templates/schemas/a11y_audit.schema.json -d "docs/design/reviews/accessibility/**/*.md"
      - name: Print Summary
        run: echo "A11y templates validated."
```

---

## 🧪 Example Front-Matter (drop-in for any audit)

```yaml
---
review_id: "a11y_map_controls_v2.0.0"
component: "map_controls"
route: "/map"
status: "needs-review"
wcag_level: "AA"
reviewer: "@kfm-accessibility"
date: "2025-11-09T00:00:00Z"
commit: "{{ GIT_COMMIT }}"
artifacts:
  - "reports/a11y/axe-routes.json"
  - "reports/a11y/keyboard-flow.html"
  - "assets/a11y/screenshot-legend-focus.png"
---
```

---

## 🧩 Example Snippets (ready-to-paste into audits)

### Keyboard/Focus pass criteria
```yaml
keyboard_focus_budgets:
  reachability_percent: 100
  focus_traps: 0
  visible_focus_min_contrast: "3:1"
```

### Screen-reader live regions
```yaml
live_region_policy:
  status: "polite"
  alert: "assertive"
  streaming: "buffered → summarize"
```

### Contrast thresholds
```yaml
contrast_thresholds:
  text: 4.5
  large_text: 3.0
  non_text: 3.0
  delta_e_max: 1.0
```

---

## 📈 Observability Dashboard (Docs Metrics)

**Grafana:** `https://metrics.kfm.ai/a11y/templates`  
Tracked: template lint pass rate · link failures · schema conformance · audit coverage  
Retention: 180 days → `/data/digests/a11y/templates_metrics.json`

---

## 🧾 Provenance & Compliance

| Field | Description |
|:--|:--|
| **Frameworks Tested** | React 18 · MapLibre GL · HTML5 Canvas |
| **Standards** | WCAG 2.1 AA · Section 508 · WAI-ARIA 1.2 |
| **Automation** | Axe Core · Pa11y CI · Lighthouse · Playwright |
| **Version Control** | Every audit includes `commit`, `reviewer`, `route`, `date`, and **artifacts** |
| **Audit Cadence** | Required per major UI release or regression |

---

## 🔄 Re-Audit Policy

```yaml
re_audit_policy:
  validity_period: "6 months"
  triggers:
    - "New route or UI feature"
    - "Token/theme/RTL changes"
    - "WCAG / ARIA update"
  archive_on_expire: true
```

---

## 🧾 Governance Ledger

| Date | Reviewer | Area | Outcome | SHA-256 |
|:--|:--|:--|:--|:--|
| 2025-11-09 | @kfm-accessibility | Templates & schemas | ✅ | `sha256:81a…` |
| 2025-11-09 | @kfm-design | A11y tokens & examples | ✅ | `sha256:2bf…` |
| 2025-11-09 | @kfm-security | CI & link integrity | ✅ | `sha256:5dc…` |

---

## 📅 Version History

| Version | Date | Author | Summary | Type |
|:--|:--|:--|:--|:--|
| **v3.0.0** | 2025-11-09 | @kfm-accessibility | Tier-S⁺⁺⁺⁺: Added schemas, usage flow, route budgets, observability, re-audit policy, governance ledger, expanded template set. | Major |
| **v2.0.0** | 2024-08-21 | @kfm-accessibility | CI validation (markdownlint + pa11y), standardized metadata, initial templates set. | Major |
| **v1.0.0** | 2023-10-01 | Founding Team | Initial accessibility templates index. | Major |

---

<div align="center">

### 🧭 Kansas Frontier Matrix — Reproducible Accessibility Framework  
**Standardized · Auditable · Inclusive · Observable**

<!-- MCP-CERTIFIED: TIER S⁺⁺⁺⁺ -->
<!-- VERIFIED-STANDARDS: [MCP-DL v6.3, WCAG 2.1 AA, WCAG 3.0 readiness, Section 508, WAI-ARIA 1.2, FAIR/CARE] -->
<!-- VALIDATION-HASH: sha256:a11y-templates-index-v3-0-0-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -->

</div>
