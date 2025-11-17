---
title: "🧮 Kansas Frontier Matrix — Accessible Data Visualization Controls and Analytical UI Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/data-visualization-controls.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-data-visualization-controls-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "accessible-data-viz-controls"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council · FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/data-visualization-controls.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E31 Document"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-data-visualization-controls.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-data-visualization-controls-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-data-visualization-controls-v10.4.1"
semantic_document_id: "kfm-doc-a11y-data-visualization-controls"
event_source_id: "ledger:docs/accessibility/patterns/data-visualization-controls.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "removal of ethics metadata"
  - "speculative interpretation of data"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Analytical UI Pattern"
jurisdiction: "Kansas / United States"
role: "a11y-pattern-data-viz-controls"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next data-viz standard update"
---

<div align="center">

# 🧮 **Kansas Frontier Matrix — Accessible Data Visualization Controls and Analytical UI Standards**  
`docs/accessibility/patterns/data-visualization-controls.md`

**Purpose:**  
Define accessibility and inclusivity standards for **interactive data visualizations**, **filter controls**, and **analytical dashboards** used across KFM — including hydrology, archaeology, governance, environmental, and treaty modules — ensuring **keyboard operability**, **assistive clarity**, and **ethical interpretability** under **FAIR+CARE** governance.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Analytical dashboards and visualizations form the **core interpretive environment** for KFM. They:

- Combine hydrological, climatic, ecological, and cultural datasets  
- Present complex relationships in charts, maps, and tables  
- Power Focus Mode narratives and decision-support workflows  

This pattern specifies:

- ARIA structure for charts, legends, and filter panels  
- Keyboard and screen-reader interaction behavior for analytical UIs  
- FAIR+CARE metadata requirements for data context and ethical framing  

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
└── patterns/
    ├── data-visualization-controls.md   # This file
    ├── environmental-dashboards.md
    ├── hydrology-water.md
    ├── tables.md
    └── ...
```

---

## 🧩 Accessibility Requirements

| Category            | Description                                                  | WCAG / Standard |
|---------------------|--------------------------------------------------------------|-----------------|
| Keyboard Access     | All filters, sliders, and buttons navigable via Tab/Arrow.  | WCAG 2.1.1      |
| Focus Visibility    | Focus ring ≥ 3px, high contrast (≥ 3:1).                    | WCAG 2.4.7      |
| ARIA Descriptions   | `aria-describedby` used to expose data context and provenance.| WAI-ARIA 1.2    |
| Data Context Announce | `aria-live="polite"` regions used for chart updates.       | WCAG 4.1.3      |
| Tooltip Alternatives| Tooltip content mirrored in accessible text regions.        | WCAG 1.1.1      |
| Color Independence  | Color never the sole encoder of categories/states.          | WCAG 1.4.1      |

---

## 🧭 Example Filter + Chart Implementation

```html
<section aria-labelledby="dashboard-title" role="region">
  <h2 id="dashboard-title">Hydrological Trends Dashboard</h2>

  <fieldset role="group" aria-label="Data Filters">
    <legend>Filter by Time Period</legend>
    <label><input type="radio" name="period" value="1950-1970" /> 1950–1970</label>
    <label><input type="radio" name="period" value="1970-1990" /> 1970–1990</label>
    <label><input type="radio" name="period" value="1990-2020" /> 1990–2020</label>
  </fieldset>

  <label for="river-select">River System</label>
  <select id="river-select" name="river">
    <option value="kansas">Kansas River</option>
    <option value="arkansas">Arkansas River</option>
    <option value="smokyhill">Smoky Hill River</option>
  </select>

  <button type="button" aria-label="Apply filters to hydrology data">Apply Filters</button>
</section>

<div
  id="chart-container"
  role="img"
  aria-label="Discharge levels by decade for selected river"
  aria-live="polite"
  aria-describedby="chart-meta"
>
  <canvas></canvas>
</div>

<p id="chart-meta">
  Data from USGS; FAIR+CARE reviewed for ethics and provenance.
</p>
```

**Implementation Notes**

- Group related filters with `<fieldset>` + `<legend>` to enhance navigation.  
- Use `role="img"` + `aria-label` for canvas charts; pair with text meta.  
- Live updates should be **polite** to avoid interrupting AT user tasks.  

---

## 🎨 Design Tokens for Analytical UI

| Token                    | Description                            | Example Value |
|--------------------------|----------------------------------------|---------------|
| `data.focus.color`       | Focus highlight on chart UI            | `#FFD54F`     |
| `data.legend.text.color` | Legend labels                          | `#212121`     |
| `data.tooltip.bg`        | Tooltip background                     | `#263238`     |
| `data.tooltip.text`      | Tooltip text                           | `#FAFAFA`     |
| `data.filter.bg`         | Filter panel surface                   | `#ECEFF1`     |
| `data.chart.palette`     | Colorblind-safe palettes (Okabe-Ito)   | N/A (palette) |

---

## ⚙️ Keyboard & Interaction Matrix

| Key                | Function                                  | Accessibility Notes                                  |
|--------------------|--------------------------------------------|------------------------------------------------------|
| `Tab`              | Cycle through filters, sliders, controls  | Skip hidden or disabled elements                     |
| `Arrow Keys`       | Adjust sliders / move between series      | Announce current value or series via `aria-live`     |
| `Enter`            | Apply filters / toggle dataset visibility | Trigger chart update and status announcement         |
| `Esc`              | Close legends/tooltips / reset focus      | Return focus to primary dashboard region             |
| `Shift+Enter`      | Trigger export of filtered data           | Opens accessible export dialog or confirms action    |

---

## 🧾 FAIR+CARE Data Ethics Metadata

| Field               | Description                                | Example                         |
|---------------------|--------------------------------------------|---------------------------------|
| `data-origin`       | Data source / custodian                    | "USGS Hydrology Division"      |
| `data-license`      | Reuse license                              | "CC-BY 4.0"                     |
| `data-ethics-reviewed` | Ethical review completion               | true                            |
| `data-sensitivity`  | Sensitivity classification                 | "low"                           |
| `data-consent`      | Public consent display flag                | true                            |

Example embedding:

```json
{
  "data-origin": "USGS Hydrology Division",
  "data-license": "CC-BY 4.0",
  "data-ethics-reviewed": true,
  "data-sensitivity": "low",
  "data-consent": true
}
```

---

## 🧪 Testing & Validation Workflows

| Tool        | Scope                                           | Output                                      |
|-------------|-------------------------------------------------|---------------------------------------------|
| **axe-core**| ARIA + interactive control semantics            | `a11y_data_viz.json`                        |
| **Lighthouse** | Focus, motion, and keyboard performance     | `lighthouse_data_viz.json`                  |
| **jest-axe** | Unit/component-level chart + filter tests     | `a11y_data_components.json`                 |
| **Manual QA** | Screen reader + keyboard navigation through analytics | FAIR+CARE audit logs                |

Validation should confirm:

- All interactive controls pass keyboard + AT checks.  
- Motion is optional, minimal, and reduced when user preference is set.  
- Tooltips and chart details have text equivalents.  

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                                    |
|---------------------|------------------------------------------------------------------------------------|
| Collective Benefit  | Visualizations highlight shared, not exploitative, insights.                      |
| Authority to Control| Custodians can govern which layers appear in dashboards.                          |
| Responsibility      | Each data series includes provenance and ethics flags shown in UI or metadata.    |
| Ethics              | Visual framing avoids exaggeration or misrepresentation of risk or disparity.     |

---

## 🕰️ Version History

| Version | Date       | Author                 | Summary                                                                                          |
|--------:|------------|------------------------|--------------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council  | Upgraded to KFM-MDP v10.4.3; added metadata, design tokens, and comprehensive interaction matrix. |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council      | Initial accessible data visualization controls and dashboard pattern.                            |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** • Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Patterns Index](../README.md)

</div>