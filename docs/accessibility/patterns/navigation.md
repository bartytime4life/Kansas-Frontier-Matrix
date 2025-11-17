---
title: "🧭 Kansas Frontier Matrix — Accessible Navigation & Landmark Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/navigation.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-navigation-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-navigation"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council · FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/navigation.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-navigation.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-navigation-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-navigation-v10.4.1"
semantic_document_id: "kfm-doc-a11y-navigation"
event_source_id: "ledger:docs/accessibility/patterns/navigation.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public Document"
jurisdiction: "United States / Kansas"
role: "a11y-pattern-navigation"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next navigation/landmark standard update"
---

<div align="center">

# 🧭 **Kansas Frontier Matrix — Accessible Navigation & Landmark Patterns**  
`docs/accessibility/patterns/navigation.md`

**Purpose:**  
Define accessible, predictable, keyboard-navigable, and screen-reader-compatible **navigation structures and landmark regions** across all Kansas Frontier Matrix (KFM) interfaces.  
Ensures compliance with **WCAG 2.1 AA**, **WAI-ARIA 1.2**, **XAUR considerations**, and **FAIR+CARE** ethical usability principles.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Navigation is the semantic backbone of the Kansas Frontier Matrix interface — connecting maps, dashboards, Focus Mode narratives, governance portals, and data exploration tools into a coherent user journey.

This pattern governs:

- Global navigation (headers, sidebars)  
- Local navigation (tabs, breadcrumbs, sub-menus)  
- Skip links and landmark regions  
- Logical focus order and keyboard navigation  
- Ethical content hierarchy design (FAIR+CARE-aligned)  

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
├── README.md
├── testing-guide.md
├── tokens.md
└── patterns/
    ├── navigation.md                # This file
    ├── notifications.md
    ├── network-infrastructure.md
    ├── parks-conservation.md
    ├── planetarium-3d.md
    ├── pollinators-ecosystem-services.md
    ├── prairie-restoration.md
    ├── rail-transit.md
    ├── soil-health.md
    ├── space-remote-sensing.md
    ├── system-controls.md
    ├── tables.md
    ├── telemetry-streams.md
    ├── testing-validation.md
    ├── tooltips.md
    ├── transportation-mobility.md
    ├── urban-planning.md
    ├── vehicle-logistics.md
    └── wildlife-tracking.md
```

---

## 🧩 Landmark Roles

| Landmark        | HTML Element | ARIA Role / Label        | Description                                      |
|-----------------|--------------|---------------------------|--------------------------------------------------|
| Header          | `<header>`   | `role="banner"`           | Global site header                               |
| Navigation      | `<nav>`      | `role="navigation"`       | Groups sets of navigation links                  |
| Main Content    | `<main>`     | `role="main"`             | Primary content region (one per document)        |
| Complementary   | `<aside>`    | `role="complementary"`    | Related side content or filters                  |
| Footer          | `<footer>`   | `role="contentinfo"`      | Site metadata, licensing, or feedback links      |

### Required Rules

- Every page must contain **exactly one** `<main>` region.  
- Every navigation region must use **unique ARIA labels** (e.g., `aria-label="Primary Navigation"`).  
- Nested navigation elements must maintain predictable hierarchy and keyboard flow.

---

## 🧭 Example Implementation

~~~html
<a class="skip-link" href="#main-content">Skip to content</a>

<header role="banner">
  <h1>Kansas Frontier Matrix</h1>

  <nav aria-label="Primary Navigation">
    <ul>
      <li><a href="/map" aria-current="page">Map</a></li>
      <li><a href="/timeline">Timeline</a></li>
      <li><a href="/governance">Governance</a></li>
    </ul>
  </nav>
</header>

<main id="main-content" role="main" tabindex="-1">
  <h2>Focus Mode Overview</h2>
  <!-- Main content -->
</main>

<footer role="contentinfo">
  <nav aria-label="Footer Links">
    <a href="/about">About</a> | <a href="/accessibility">Accessibility</a>
  </nav>
</footer>
~~~

### Best Practices

- Skip-link must be visible on keyboard focus.  
- Maintain a logical heading hierarchy (`<h1>` → `<h2>` → `<h3>`).  
- Use `aria-current="page"` for active navigation states.  
- Do not duplicate navigation landmarks on single-page apps unless scoped.  

---

## 🎨 Design Tokens for Navigation

| Token                   | Description                         | Example Value |
|-------------------------|-------------------------------------|---------------|
| a11y.focus.color        | Focus outline for nav items         | #FFD54F       |
| nav.spacing.horizontal  | Spacing between nav items           | 1rem          |
| nav.font.weight         | Navigation font weight              | 600           |
| skiplink.bg            | Skip-link background                 | #212121       |

### Example SCSS

~~~scss
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--skiplink-bg);
  color: #fff;
  padding: 8px;
  z-index: 1000;
}
.skip-link:focus {
  top: 0;
}
~~~

---

## ⚙️ Keyboard & ARIA Interaction Matrix

| Key / Attribute       | Function                                  | Notes                                  |
|------------------------|--------------------------------------------|----------------------------------------|
| Tab                   | Moves across navigation items               | Sequential order required               |
| Enter / Space         | Activates link or toggle                   | Consistent interaction model            |
| Arrow Keys            | Navigates submenus or grouped links        | Recommended for dropdown nav           |
| Esc                   | Closes expanded submenus                   | Returns focus to parent                |
| aria-expanded         | Indicates visibility of collapsible menus  | Must update dynamically                 |
| aria-current="page"   | Marks current navigation target             | Required for active pages               |

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                                |
|---------------------|--------------------------------------------------------------------------------|
| Collective Benefit  | Landmark semantics support AT users in navigating complex KFM content.        |
| Authority to Control| Skip-link, theme, and reduced-motion settings give users autonomy.            |
| Responsibility      | Navigation analytics appear in focus telemetry for auditability.             |
| Ethics              | Language, ordering, and groupings validated to avoid cultural bias.          |

---

## 🧪 Testing & Validation Workflows

| Tool           | Scope                                 | Output File                                   |
|----------------|----------------------------------------|-----------------------------------------------|
| axe-core       | Landmark, heading, ARIA correctness    | a11y_navigation.json                          |
| Cypress        | Keyboard traversal & focus order       | navigation_focus_tests.json                   |
| Lighthouse CI  | Landmark coverage & nav performance    | lighthouse_navigation.json                    |
| Manual QA      | Screen reader (NVDA / VoiceOver) pass | FAIR+CARE Council logs                        |

Validation confirms:

- Predictable keyboard travel across all navigation components  
- Accurate roles and ARIA labels for all major regions  
- Skip-link and heading structure meet WCAG 2.1 AA  
- No inaccessible or unlabeled navigation elements  

---

## 🕰️ Version History

| Version | Date       | Author                | Summary                                                                                      |
|--------:|------------|-----------------------|----------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Upgraded to KFM-MDP v10.4.3; added extended metadata, navigation telemetry hooks, and one-box-safe formatting. |
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council| Initial navigation & landmark accessibility pattern established.                             |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Patterns Index](../README.md)

</div>