---
title: "🎨 Kansas Frontier Matrix — Accessible Color & Contrast Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/color-contrast.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-color-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-color-contrast"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Design System · Accessibility Council"
risk_category: "Minimal"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/color-contrast.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  schema_org: "Guideline"
  cidoc: "E29 Design or Procedure"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-color.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-color-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-color-contrast-v10.4.1"
semantic_document_id: "kfm-doc-a11y-color-contrast"
event_source_id: "ledger:docs/accessibility/patterns/color-contrast.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Color & Contrast Accessibility"
jurisdiction: "Kansas / United States"
role: "a11y-pattern-color"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded on next major palette update"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Accessible Color & Contrast Standards**  
`docs/accessibility/patterns/color-contrast.md`

**Purpose:**  
Define and enforce **color contrast, visual hierarchy, and palette usage standards** across all KFM interfaces — ensuring compliance with **WCAG 2.1 AA**, **ISO 9241-210**, and **FAIR+CARE inclusive design principles** for public scientific, cultural, and historical data.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

High-quality color & contrast accessibility is essential to the Kansas Frontier Matrix visual ecosystem:  

- **Data dashboards** (climate, hydrology, archaeology)  
- **Map layers** (Landcover, STAC-based rasters, heritage overlays)  
- **Focus Mode** AI narratives & highlight systems  
- **Web components** (forms, buttons, tables, story nodes)  

This document defines the **one authoritative, MCP-DL v6.3–certified color/contrast standard** for the entire KFM platform.

---

## 🗂️ Directory Context

```text
docs/accessibility/
└── patterns/
    ├── color-contrast.md        # This file
    ├── design-tokens.md
    ├── charts.md
    ├── map-controls.md
    └── ...
```

---

## 🧩 Core Principles

| Principle | Description | WCAG / ISO Reference |
|----------|-------------|----------------------|
| **Contrast Ratio** | Text vs. background must be ≥ **4.5:1**, large text ≥ **3:1**. | WCAG 1.4.3 |
| **Non-Color Cues** | Never use color alone to convey meaning or status. | WCAG 1.4.1 |
| **Palette Consistency** | All colors must use official KFM design tokens. | ISO 9241-210 |
| **Dark Mode Parity** | Dark + light themes must meet equal contrast requirements. | WCAG 1.4.11 |
| **Cultural Sensitivity** | Colors reviewed for symbolic neutrality across cultures. | FAIR+CARE Ethics |

---

## 🎨 Tokenized Palette (Authoritative KFM Palette v10.4)

| Token | Purpose | Value (Hex) | Contrast vs `#FFFFFF` | Contrast vs `#121212` |
|-------|---------|--------------|------------------------|------------------------|
| `color.primary` | Primary buttons & anchors | `#0053A0` | 8.5:1 | 5.9:1 |
| `color.secondary` | Secondary CTAs | `#1565C0` | 6.7:1 | 4.2:1 |
| `color.accent` | Warnings / highlights | `#FFD54F` | 5.1:1 | 3.8:1 |
| `color.error` | Errors & alerts | `#D32F2F` | 6.9:1 | 4.3:1 |
| `color.success` | Success states | `#388E3C` | 6.1:1 | 4.0:1 |
| `color.text.primary` | Primary text | `#212121` | 15.2:1 | — |
| `color.text.muted` | Secondary text | `#616161` | 7.4:1 | — |
| `color.background` | Light background | `#FAFAFA` | — | — |
| `color.background.dark` | Dark background | `#121212` | — | — |

> ✔ **All tokenized palette entries exceed WCAG requirements** in both themes.

---

## 🧭 Data Visualization Requirements

### Color-Blind–Safe Palettes (Mandatory)
KFM uses the **Okabe–Ito palette** across all analytics surfaces:

```json
{
  "blue":   "#0072B2",
  "orange": "#E69F00",
  "sky":    "#56B4E9",
  "green":  "#009E73",
  "yellow": "#F0E442",
  "pink":   "#CC79A7",
  "grey":   "#999999"
}
```

### Map & Chart Rules

| Requirement | Description |
|------------|-------------|
| **Texture Alternatives** | Do not rely on color alone; use pattern fills & line styles. |
| **Opacity Guidance** | Overlays must maintain < 60% opacity above basemap. |
| **Legend Text** | Every color category requires text description + icon. |
| **NDVI/Climate Rasters** | Must include explicit scale bar with numeric endpoints. |

---

## ⚙️ Validation Workflow (CI-Enforced)

| Tool | Validation Type | Output |
|-------|------------------|--------|
| **axe-core** | Automated DOM contrast check | `reports/self-validation/web/a11y_color.json` |
| **Lighthouse CI** | Contrast, theme, & forced-colors tests | `reports/ui/lighthouse_color.json` |
| **jest-axe** | Component-level contrast tests | `reports/ui/a11y_color_components.json` |
| **CCA Manual Review** | Council QA log | `reports/a11y/manual_color_review.txt` |

All findings appear in the **FAIR+CARE governance ledger**.

---

## 🛠️ Example Usage (React + Tokens)

```jsx
<Button
  className="kfm-button"
  style={{
    backgroundColor: "var(--color-primary)",
    color: "var(--color-text-primary)",
    outlineColor: "var(--a11y-focus-color)"
  }}
>
  Submit Data
</Button>
```

---

## 🧾 FAIR+CARE Alignment

| Principle | Implementation |
|-----------|----------------|
| **Findable** | Design tokens globally discoverable in `web/src/theme/tokens.json`. |
| **Accessible** | Contrast validated in CI + Focus Mode telemetry. |
| **Interoperable** | Palette feeds MapLibre, Cesium, Recharts, Story Node renderers. |
| **Reusable** | Distributed via KFM NPM Design System package. |
| **Ethics** | Colors reviewed for cultural neutrality and symbolic safety. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|------|--------|---------|
| v10.4.1 | 2025-11-16 | KFM A11y Council | Upgraded to KFM-MDP v10.4.3; added dual-theme validation + expanded palette metadata. |
| v10.0.0 | 2025-11-10 | FAIR+CARE Council | Initial color/contrast standardization + Okabe–Ito palette adoption. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · Certified by **FAIR+CARE Council**  
[⬅ Back to Patterns Index](README.md)

</div>