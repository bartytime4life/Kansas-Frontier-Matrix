---
title: "🧮 Kansas Frontier Matrix — Accessible Data Visualization Controls and Analytical UI Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/data-visualization-controls.md"
version: "v10.0.0"
last_updated: "2025-11-11"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-data-visualization-controls-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧮 **Kansas Frontier Matrix — Accessible Data Visualization Controls and Analytical UI Standards**
`docs/accessibility/patterns/data-visualization-controls.md`

**Purpose:**  
Define accessibility and inclusivity standards for **interactive data visualizations**, **filter controls**, and **analytical dashboards** used throughout KFM’s hydrology, archaeology, and governance modules — ensuring **keyboard operability**, **assistive clarity**, and **ethical interpretability** under **FAIR+CARE** governance.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Analytical dashboards and visualizations form the **core interpretive environment** for the Kansas Frontier Matrix — combining hydrological, climatic, and cultural datasets into layered, ethical narratives.  
This pattern establishes **ARIA structure**, **interaction behavior**, and **data ethics metadata** for charts, filters, legends, and focus tools.

---

## 🧩 Accessibility Requirements

| Category | Description | WCAG / Standard |
|-----------|--------------|-----------------|
| **Keyboard Access** | All filters, sliders, and buttons navigable via Tab / Arrow keys. | WCAG 2.1.1 |
| **Focus Visibility** | Focus ring ≥ 3px and high-contrast (≥ 3:1). | WCAG 2.4.7 |
| **ARIA Descriptions** | Use `aria-describedby` to define data context and provenance. | WAI-ARIA 1.2 |
| **Data Context Announcements** | Chart updates use `aria-live="polite"` region. | WCAG 4.1.3 |
| **Tooltip Alternatives** | Tooltips mirrored in off-screen text regions for screen readers. | WCAG 1.1.1 |
| **Color Independence** | Never rely solely on color to encode categories. | WCAG 1.4.1 |

---

## 🧭 Example Implementation (Dashboard Filter Panel)

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

  <button type="button" aria-label="Apply Filters">Apply Filters</button>
</section>

<div id="chart-container" role="img" aria-label="Discharge levels by decade" aria-live="polite">
  <canvas></canvas>
</div>
```

**Implementation Notes**
- Filter fields grouped by `<fieldset>` and `<legend>` improve structural navigation.  
- Chart container uses `role="img"` + descriptive `aria-label`.  
- Dynamic updates announced through polite live region.  
- Ensure visual focus indicators around filter controls.  

---

## 🎨 Design Tokens for Data Visual Components

| Token | Description | Example Value |
|--------|--------------|----------------|
| `data.focus.color` | Focus highlight for chart points | `#FFD54F` |
| `data.legend.text.color` | Legend label color | `#212121` |
| `data.tooltip.bg` | Tooltip background color | `#263238` |
| `data.tooltip.text` | Tooltip text color | `#FAFAFA` |
| `data.filter.bg` | Filter panel background | `#ECEFF1` |
| `data.chart.palette` | Colorblind-safe series colors | Okabe-Ito palette |

---

## ⚙️ Keyboard & Interaction Matrix

| Key | Function | Description |
|------|-----------|-------------|
| `Tab` | Cycle through filters, sliders, and chart focusable points | Sequential, skip hidden layers |
| `Arrow Keys` | Adjust range sliders or navigate data series | Supports incremental data review |
| `Enter` | Apply filter or toggle dataset visibility | Executes live region update |
| `Esc` | Clear active focus or close expanded legends | Returns focus to primary region |
| `Shift+Enter` | Export current dataset or chart view | Triggers accessible download dialog |

---

## 🧾 FAIR+CARE Data Ethics Metadata

| Field | Description | Example |
|--------|--------------|----------|
| `data-origin` | Data source / custodian | “USGS Hydrology Division” |
| `data-license` | Reuse and attribution license | “CC-BY 4.0” |
| `data-ethics-reviewed` | Council ethical review status | `true` |
| `data-sensitivity` | Cultural or environmental sensitivity flag | `low` |
| `data-consent` | Public consent for display | `true` |

**Embedded Metadata Example:**
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

| Tool | Scope | Output |
|-------|--------|--------|
| **axe-core** | UI filter and chart ARIA validation | `reports/self-validation/web/a11y_data_viz.json` |
| **Lighthouse CI** | Performance & accessibility scoring | `reports/ui/lighthouse_data_viz.json` |
| **jest-axe** | React chart component testing | `reports/ui/a11y_data_components.json` |
| **Manual QA** | Screen reader navigation through chart & filters | FAIR+CARE audit logs |

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|------------|----------------|
| **Collective Benefit** | Analytical tools provide transparent insights across communities. |
| **Authority to Control** | Data layers toggleable based on custodial consent. |
| **Responsibility** | Every chart includes FAIR+CARE metadata for reuse tracking. |
| **Ethics** | Visualization tone reviewed to prevent misleading or extractive representations. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-11 | FAIR+CARE Council | Established accessible standards for analytical dashboards, data filters, and chart controls; integrated FAIR+CARE metadata schema and CI testing. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Index](README.md)

</div>
