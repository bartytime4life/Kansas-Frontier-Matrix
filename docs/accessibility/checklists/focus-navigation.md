---
title: "🎯 Kansas Frontier Matrix — Focus & Keyboard Navigation Accessibility Checklist (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/checklists/focus-navigation.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-focus-nav-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Checklist"
intent: "focus-keyboard-validation"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "New document generated for navigation a11y validation suite"
previous_version_hash: null
ontology_alignment:
  schema_org: "Checklist"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-checklist-focus.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-checklist-focus-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-focus-navigation-checklist-v10.4.1"
semantic_document_id: "kfm-doc-a11y-focus-navigation-checklist"
event_source_id: "ledger:docs/accessibility/checklists/focus-navigation.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Accessibility · Keyboard Navigation · Focus Management"
jurisdiction: "Kansas / United States"
role: "a11y-checklist-focus-navigation"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded by future versions"
---

<div align="center">

# 🎯 **Kansas Frontier Matrix — Focus & Keyboard Navigation Accessibility Checklist**  
`docs/accessibility/checklists/focus-navigation.md`

**Purpose:**  
Mandatory checklist validating **keyboard navigation**, **focus order**, **focus visibility**, and **assistive device compatibility** across the Kansas Frontier Matrix (KFM).  
This is required for all UI components, maps, charts, Story Nodes, Focus Mode, dashboards, archives, and scientific interfaces under **WCAG 2.1 AA**, **WAI-ARIA 1.2**, and **FAIR+CARE ethics**.

![A11y](https://img.shields.io/badge/WCAG-2.1_AA-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Keyboard](https://img.shields.io/badge/Keyboard-Navigation-success)

</div>

---

## 📘 Overview

Keyboard and focus navigation form the **core accessibility layer** of the Kansas Frontier Matrix.  
This checklist ensures:

- Predictable, logical, and reversible navigation  
- Clear focus states using KFM design tokens  
- ARIA semantics for components, dialogs, maps, and dashboards  
- Ethical, non-coercive interaction  
- Telemetry-backed validation of focus visibility and behavior  

This applies to *every* KFM interface: web, mobile, 3D, scientific dashboards, archival viewers, forms, and command components.

---

## ✅ Section 1 — Global Focus Requirements

### ✔️ Required
- [ ] One and only one focus outline at any time.
- [ ] Focus ring has ≥ **3:1 contrast ratio** and uses `a11y.focus.color`.
- [ ] No focus suppression (`outline: none;`) without replacement.
- [ ] Focus order matches DOM order and reading logic.
- [ ] Focus never jumps unexpectedly or resets.
- [ ] Keyboard trap tests passed on every component.
- [ ] Each page includes a **skip-to-content** link (`tabindex="0"`).
- [ ] No forced focus shifts except:
  - Dialog open/close  
  - Menu or disclosure activation  
  - Explicit user intent  

### ⚠️ Forbidden
- [ ] Hidden focusable elements (`tabindex="0"` on invisibles).
- [ ] Keyboard-only users blocked by mouse-dependent components.
- [ ] Auto-focusing inputs on load (violates cognitive accessibility).

---

## ✅ Section 2 — Navigation Structure

### ✔️ Required
- [ ] Navigation landmarks use `<header>`, `<nav>`, `<main>`, `<footer>`.
- [ ] Each `<nav>` has an **ARIA label** (`aria-label="Primary Navigation"`).
- [ ] `aria-current="page"` applied on active links.
- [ ] Breadcrumbs use semantic lists (`<ol>`) + accessible labels.

### WAYFINDING
- [ ] Wayfinding indicators (arrows, breadcrumbs, timeline markers) must have text equivalents.
- [ ] Navigation hierarchy tested via **linear screen reader navigation**.

---

## ✅ Section 3 — Buttons, Toggles, Forms

- [ ] Every button is a real `<button>` or has `role="button"` + `tabindex="0"`.
- [ ] Toggle buttons implement `aria-pressed="true|false"`.
- [ ] Form fields include labels or `aria-label`.
- [ ] Validation errors described via `aria-describedby`.

---

## ✅ Section 4 — Focus Mode & Story Nodes

### FOCUS MODE
- [ ] Entering/exiting Focus Mode moves focus to consistent anchor.
- [ ] AI suggestions **never steal focus**.
- [ ] All controls reachable via tabbing in < 20 keypresses.

### STORY NODES
- [ ] Time-based node navigation via Arrow Keys + Enter.
- [ ] 3D Story Node transitions preserve focus and do not shift camera.

---

## ✅ Section 5 — Data Visualizations (Charts, Maps, Dashboards)

### CHARTS
- [ ] Chart data points focusable via Arrow Keys.
- [ ] Tooltips accessible through keyboard activation.
- [ ] Provide an accessible data table alternative.

### MAPS (MapLibre / Cesium)
- [ ] Map canvas has `role="application"` + ARIA descriptors.
- [ ] Focusable map controls (`Zoom in`, `Zoom out`, layer toggles).
- [ ] Keyboard panning available (Arrow Keys) with polite announcements.
- [ ] No autofocus when map initializes.

---

## ✅ Section 6 — Dialogs & Modals

- [ ] Opening modal moves focus to first focusable element.
- [ ] Closing modal returns focus to opener.
- [ ] Focus trapped inside modal until closed.
- [ ] Modal labelled via `aria-labelledby` + `aria-describedby`.

---

## ✅ Section 7 — Lists, Tables, Panels

- [ ] Tables use `<th scope="col|row">`.
- [ ] Expandable panels use `aria-expanded` + `aria-controls`.
- [ ] Tabs implement full ARIA Tablist pattern:
  - `role="tablist"`  
  - `role="tab"`  
  - `role="tabpanel"`  
  - Arrow key navigation  

---

## 🧪 Validation & CI Integration

| Workflow                      | Scope                                     | Output |
|------------------------------|-------------------------------------------|---------|
| `focus-scan.yml`             | Automated focus traversal detection       | `reports/self-validation/web/a11y_focus_nav.json` |
| `accessibility_scan.yml`     | axe-core WCAG tests                       | `reports/self-validation/web/a11y_summary.json` |
| `storybook-a11y.yml`         | Component-level focus snapshots           | `reports/ui/a11y_components_focus.json` |
| `faircare-language.yml`      | Ethical tone + consent cues               | `reports/faircare/focus_nav_ethics.json` |
| `telemetry_focus.yml`        | Tracks real user focus visibility metrics | `reports/self-validation/web/focus_telemetry.json` |

All merges **blocked** if any focus-navigation rule fails.

---

## 🧠 References

- WCAG 2.1 — 2.1.1 Keyboard, 2.4.x Focus Patterns  
- WAI-ARIA 1.2 Authoring Practices  
- FAIR+CARE Council Ethics Review  
- KFM Interaction Design Tokens (`web/src/theme/tokens.json`)  
- Patterns: Navigation, Buttons, Dialogs, Map Controls, Charts  

---

## 🕰️ Version History

| Version | Date       | Author            | Summary |
|--------:|------------|-------------------|---------|
| v10.4.1 | 2025-11-16 | KFM A11y Council  | Initial comprehensive focus-navigation checklist aligned with MDP v10.4.3. |

---

<div align="center">

© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3  
**FAIR+CARE Certified · Focus-Safe Design Verified**

[⬅ Back to Accessibility Checklists](README.md)

</div>