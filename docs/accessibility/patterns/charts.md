---
title: "📈 Kansas Frontier Matrix — Accessible Charts & Data Visualization Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/charts.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-charts-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "accessible-charts"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM Accessibility Council · FAIR+CARE Council"
risk_category: "Medium"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/charts.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E29 Design or Procedure"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-charts.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-charts-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-charts-v10.4.1"
semantic_document_id: "kfm-doc-a11y-charts"
event_source_id: "ledger:docs/accessibility/patterns/charts.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "removing uncertainty or provenance"
  - "misrepresenting scales (e.g., truncated axes without callout)"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Charts & Data Visualization Accessibility"
jurisdiction: "Kansas / United States"
role: "a11y-pattern-charts"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded on next charts pattern update"
---

<div align="center">

# 📈 **Kansas Frontier Matrix — Accessible Charts & Data Visualization Patterns**  
`docs/accessibility/patterns/charts.md`

**Purpose:**  
Define **accessible charting and data visualization standards** for KFM web and analytic interfaces — ensuring **data legibility**, **non-visual accessibility**, and **ethical representation** aligned with **WCAG 2.1 AA**, **ISO 9241-210**, and **FAIR+CARE** principles.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Charts in Kansas Frontier Matrix (KFM) communicate **temporal**, **environmental**, **economic**, and **cultural** trends using libraries such as **Recharts**, **D3.js**, and map-linked overlays.

This pattern ensures:

- Charts are **perceivable** to users with different visual and cognitive profiles.  
- All visual encodings have **textual and structural equivalents**.  
- Visualizations remain **ethically framed**, exposing uncertainty and provenance.  

Supported chart types include:

- Line, bar, and area charts  
- Pie and donut charts (used sparingly, with clear labels)  
- Time-series timelines and focus sliders  
- Map-linked geostatistical overlays and choropleths  
- 3D charts and volumetric renderings (with text + tabular support)  

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
└── patterns/
    ├── charts.md                 # This file
    ├── color-contrast.md
    ├── data-visualization-controls.md
    └── tables.md
```

---

## 🧩 Accessibility Standards

| Principle              | Description                                                        | WCAG / Standard   |
|------------------------|--------------------------------------------------------------------|-------------------|
| Text Alternatives      | Every chart provides textual summary and/or data table.           | WCAG 1.1.1        |
| Color Independence     | Categories never conveyed by color alone.                         | WCAG 1.4.1        |
| Keyboard Navigation    | Interactive charts respond to `Tab`, `Arrow`, and `Enter` keys.   | WCAG 2.1.1        |
| Screen Reader Support  | Use ARIA (`role="img"`, `aria-label`, `aria-describedby`).        | WAI-ARIA 1.2      |
| Motion Sensitivity     | Animated charts obey `prefers-reduced-motion`.                    | WCAG 2.3.3        |
| Ethical Framing        | Visuals reviewed for neutral, non-stigmatizing representation.    | FAIR+CARE Ethics  |

---

## 🧭 Example Implementation (Chart + Data Table)

```html
<figure role="group" aria-labelledby="chart-title" aria-describedby="chart-description">
  <div
    role="img"
    aria-label="Precipitation trends for Kansas from 1980 to 2020, in inches"
  >
    <canvas id="precip-chart"></canvas>
  </div>

  <figcaption id="chart-title">
    Precipitation Trends (1980–2020)
  </figcaption>

  <p id="chart-description">
    Chart displays annual precipitation values derived from NOAA datasets.
    Accessible data table is provided below.
  </p>
</figure>

<table>
  <caption>Annual Precipitation Data (inches)</caption>
  <thead>
    <tr><th scope="col">Year</th><th scope="col">Precipitation</th></tr>
  </thead>
  <tbody>
    <tr><td>1980</td><td>23.4</td></tr>
    <tr><td>1990</td><td>27.1</td></tr>
    <tr><td>2020</td><td>30.5</td></tr>
  </tbody>
</table>
```

**Implementation Notes**

- Always pair the chart with **caption + description** and (ideally) a **data table**.  
- When data volumes are large, provide summary tables plus CSV/JSON downloads.  
- The `<figure>` wrapper enables screen readers to understand chart as a unit.

---

## 🎨 Design Tokens for Charts

| Token                    | Purpose                                   | Example        |
|--------------------------|-------------------------------------------|----------------|
| `chart.focus.color`      | Focus outline for chart elements          | `#FFD54F`      |
| `chart.axis.label.color` | Axis label color                          | `#212121`      |
| `chart.tooltip.bg`       | Tooltip background                        | `#333333E6`    |
| `chart.tooltip.text`     | Tooltip text color                        | `#FAFAFA`      |
| `chart.transition.speed` | Animation duration                        | `0.3s`         |

**Default Series Palette** (Okabe–Ito colorblind-safe set):

```json
["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
```

---

## ⚙️ Keyboard Interaction Matrix

| Key / Behavior   | Description                                            |
|------------------|--------------------------------------------------------|
| `Tab`            | Focus next series, legend entry, or control.          |
| `Shift+Tab`      | Focus previous interactive element.                   |
| `Arrow Keys`     | Move between points in the focused series.            |
| `Enter`          | Activate tooltip or detailed view for data point.     |
| `Esc`            | Close tooltip or exit chart focus back to container.  |

**ARIA Recommendation**

- Chart container: `role="img"` + `aria-label` (short summary).  
- Provide extended description (if needed) via `aria-describedby` or a linked text page.

---

## 🧾 FAIR+CARE Visualization Ethics

| Category       | Guideline                                                                 |
|----------------|---------------------------------------------------------------------------|
| Representation | Avoid truncated axes without clear labels/callouts.                      |
| Consent        | Cultural or sensitive data must include consent tags and warnings.       |
| Tone           | Frame results neutrally; avoid stigmatizing language.                    |
| Attribution    | Show provenance (origin, license, date, processing).                     |

Example ethical metadata:

```html
<div
  data-origin="NOAA"
  data-fair-consent="approved"
  data-ethics-reviewed="true"
></div>
```

---

## 🧪 Testing & Validation

| Tool           | Validation Type                          | Output                                      |
|----------------|-------------------------------------------|---------------------------------------------|
| **axe-core**   | Chart regions, ARIA roles, focus paths    | `a11y_charts.json`                          |
| **Lighthouse** | Contrast, motion, keyboard accessibility  | `lighthouse_charts.json`                    |
| **jest-axe**   | Component-level chart semantics           | `a11y_chart_components.json`                |
| Manual QA      | NVDA / VoiceOver chart navigation review  | FAIR+CARE Council audit log                 |

Validation checks must verify:

- Non-color encodings for categories.  
- Presence of text alternatives and summaries.  
- Adherence to motion constraints and preferences.

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                            |
|---------------------|-----------------------------------------------------------|
| Collective Benefit  | Charts support public understanding of complex datasets. |
| Authority to Control| Custodians choose what and how sensitive data is charted.|
| Responsibility      | Each chart linked to FAIR metadata + source dataset.     |
| Ethics              | Prevents misleading or biased visualization practices.   |

---

## 🕰️ Version History

| Version | Date       | Author              | Summary                                                                                   |
|--------:|------------|---------------------|-------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Upgraded to KFM-MDP v10.4.3; added extended YAML metadata, CI references, and ethics rules. |
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Initial accessible chart visualization standard with colorblind-safe palette and ARIA pattern. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Built under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Map Controls](map-controls.md) · [Back to A11y Patterns Index](README.md)

</div>