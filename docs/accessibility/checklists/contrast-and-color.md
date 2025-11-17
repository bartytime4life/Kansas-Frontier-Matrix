---
title: "🎨 Kansas Frontier Matrix — Color, Contrast & Visual Accessibility Checklist (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/checklists/contrast-and-color.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-contrast-color-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Checklist"
intent: "color-contrast-validation"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "Checklist generated for universal color & contrast compliance validation"
previous_version_hash: null
ontology_alignment:
  schema_org: "Checklist"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-checklist-contrast.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-checklist-contrast-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-contrast-color-checklist-v10.4.1"
semantic_document_id: "kfm-doc-a11y-contrast-color-checklist"
event_source_id: "ledger:docs/accessibility/checklists/contrast-and-color.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Accessibility · Contrast · Color · Vision Safety"
jurisdiction: "Kansas / United States"
role: "a11y-checklist-contrast-color"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded by future versions"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Color, Contrast & Visual Accessibility Checklist**  
`docs/accessibility/checklists/contrast-and-color.md`

**Purpose:**  
Enforce WCAG 2.1 AA color contrast, non-color redundancy, pattern-safety, and visual clarity standards across all Kansas Frontier Matrix (KFM) interfaces, ensuring **perceptual accessibility**, **data clarity**, and **ethical, culturally neutral color use** across scientific, civic, and historical UI surfaces.

![A11y](https://img.shields.io/badge/WCAG-2.1_AA-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Contrast](https://img.shields.io/badge/Contrast-Validated-brightgreen)

</div>

---

## 📘 Overview

Color is one of the highest-impact accessibility variables in the Kansas Frontier Matrix.  
This checklist ensures:

- Text and UI elements meet required contrast ratios  
- Color is never used alone to convey meaning  
- Data visualizations use pattern-safe encoding  
- Cultural & ethical rules govern palette choices  
- All colors are sourced from tokenized design systems (`tokens.json`)  

This applies to web UI, charts, mapping tools, 3D views, Focus Mode, telemetry dashboards, scientific visualizations, and archival content.

---

## 🎯 Section 1 — Text & UI Element Contrast

### ✔️ Must Pass
- [ ] **Normal text** contrast ≥ **4.5:1**
- [ ] **Large text (≥ 18px or 14px bold)** contrast ≥ **3:1**
- [ ] **Icons & strokes** meet ≥ **3:1** against background  
- [ ] **Disabled elements** maintain perceivable contrast (≥ 3:1)
- [ ] Focus outlines use `a11y.focus.color` with ≥ **3:1 contrast**

### ⚠️ Forbidden
- [ ] Thin text < 14px without strong weight  
- [ ] Transparent overlays reducing contrast below WCAG thresholds  
- [ ] Text embedded inside low-contrast gradients  

---

## 🎯 Section 2 — Color Independence (Color is Never the Only Signal)

### ✔️ Required
- [ ] All state changes include **text**, **icons**, or **patterns** (not color alone)
- [ ] Status indicators include labels:
  - “Success”, “Warning”, “Error”, “Inactive”
- [ ] Charts include:
  - Explicit legend labels  
  - Distinct patterns (stripes, dots, crosshatch)  
  - Shapes (circle, triangle, square markers)

### ⚠️ Forbidden
- [ ] Red/green–only distinctions  
- [ ] Heatmaps without textual numerical equivalents  
- [ ] Layers that change only color on hover/active

---

## 🎯 Section 3 — Design Tokens & Palette Governance

### ✔️ All UI must use KFM design tokens:
- [ ] `color.primary`, `color.secondary`, `color.accent`
- [ ] `chart.series.palette` (Okabe–Ito colorblind-safe palette)
- [ ] `map.layer.*` for geospatial overlays
- [ ] `a11y.focus.color`
- [ ] `alert.*.bg` + `alert.text.color`

### ✔️ Token validation:
- [ ] All colors stored in `/web/src/theme/tokens.json`
- [ ] No hardcoded hex values except in design token files
- [ ] Tokens validated via `color-contrast.yml`

---

## 🎯 Section 4 — Data Visualizations (Charts, Maps, Plots)

### ✔️ Charts
- [ ] Default palette = **Okabe–Ito** colorblind-safe set
- [ ] Provide **CSV or table** equivalent
- [ ] All series include:
  - [ ] Legend label  
  - [ ] Distinct pattern or marker shape  
  - [ ] ARIA `aria-label` for data context

### ✔️ Maps (MapLibre / Cesium)
- [ ] Geospatial overlays at < 60% opacity for stackability
- [ ] Sensitive overlays use non-red, non-alerting colors
- [ ] Boundaries + polygons require textured alternatives

### ✔️ Heatmaps / Choropleths
- [ ] Numeric scale appears in text  
- [ ] Color ramp uses colorblind-safe sequence  
- [ ] No green→red gradients without pattern reinforcing  

---

## 🎯 Section 5 — Cultural & Ethical Color Rules

### ✔️ Required
- [ ] Avoid culturally sensitive colors for heritage layers  
- [ ] Indigenous-related symbols or tribal overlays use approved palettes  
- [ ] Hazard colors (red, orange, purple) used only for:
  - Weather warnings  
  - Air quality  
  - Wildfire hazard  
- [ ] Avoid colonial or stigmatizing color choices for demographic maps  

### ⚠️ Forbidden
- [ ] Red shading on tribal or heritage lands  
- [ ] Colors implying ownership hierarchy or value judgment  
- [ ] Overly saturated neon tones causing cognitive overload  

---

## 🎯 Section 6 — Motion, Blend Modes & Layer Stacking

- [ ] Animated color transitions honor `prefers-reduced-motion`  
- [ ] Blend modes do not reduce contrast  
- [ ] Overlays must remain readable atop base layers  
- [ ] No flashing or pulsing color > 3 Hz  

---

## 🧪 Validation Pipelines

| Workflow | Scope | Output |
|----------|--------|--------|
| `color-contrast.yml` | Automated contrast audit across UI | `reports/ui/color-contrast.json` |
| `storybook-a11y.yml` | Component color snapshots | `reports/ui/a11y_color_components.json` |
| `accessibility_scan.yml` | Axe-core color & text violations | `reports/self-validation/web/a11y_summary.json` |
| `faircare-visual-audit.yml` | Palette ethics & cultural compliance | `reports/faircare/visual-color-ethics.json` |

All PRs *must* pass contrast + ethics validation before merge.

---

## 🧠 References

- WCAG 2.1 — 1.4.x Contrast Guidelines  
- WAI-ARIA 1.2  
- Okabe–Ito Colorblind Safe Palette  
- KFM Design Tokens (`web/src/theme/tokens.json`)  
- FAIR+CARE Ethical Visual Communication Charter  

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------------|---------|----------|
| v10.4.1 | 2025-11-16 | KFM A11y Council | Initial release, aligned with new MDP v10.4.3 and validated token governance. |

---

<div align="center">

© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3  
**FAIR+CARE Certified · Contrast-Safe Verified**

[⬅ Back to Accessibility Checklists](README.md)

</div>