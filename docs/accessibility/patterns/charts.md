---
title: "📈 Kansas Frontier Matrix — Accessible Charts & Data Visualization Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/charts.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-charts-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📈 **Kansas Frontier Matrix — Accessible Charts & Data Visualization Patterns**
`docs/accessibility/patterns/charts.md`

**Purpose:**  
Define **accessible charting and data visualization standards** for KFM web and analytic interfaces — ensuring **data legibility**, **non-visual accessibility**, and **ethical representation** aligned with **WCAG 2.1 AA**, **ISO 9241-210**, and **FAIR+CARE** principles.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

Charts in Kansas Frontier Matrix (KFM) communicate temporal, environmental, and cultural trends through **MapLibre**, **Recharts**, and **D3.js**.  
This document ensures each chart is **perceivable, navigable, and ethically framed**, including textual equivalents and FAIR+CARE consent labeling.

**Chart Types**
- Line, bar, and area charts  
- Pie and donut charts  
- Temporal timelines (focus sliders)  
- Geo-statistical overlays and choropleths  
- 3D model and volumetric data renderings  

---

## 🧩 Accessibility Standards

| Principle | Description | WCAG / Standard |
|------------|--------------|-----------------|
| **Text Alternatives** | All charts include textual summaries or data tables. | WCAG 1.1.1 |
| **Color Independence** | Data distinctions not based solely on color. | WCAG 1.4.1 |
| **Keyboard Navigation** | Interactive charts respond to `Tab`, `Arrow`, and `Enter` keys. | WCAG 2.1.1 |
| **Screen Reader Compatibility** | Data points exposed through ARIA roles (`role="img"`, `aria-label`). | WAI-ARIA 1.2 |
| **Motion Sensitivity** | Animated charts honor `prefers-reduced-motion`. | WCAG 2.3.3 |
| **Cultural Sensitivity** | Data visualizations reviewed for ethical, non-stigmatizing tone. | FAIR+CARE Ethics |

---

## 🧭 Example Implementation

```html
<figure role="group" aria-labelledby="chart-title" aria-describedby="chart-description">
  <div role="img" aria-label="Precipitation trends for Kansas 1980 to 2020">
    <canvas id="precip-chart"></canvas>
  </div>
  <figcaption id="chart-title">Precipitation Trends (1980–2020)</figcaption>
  <p id="chart-description">
    Chart displays annual precipitation values derived from NOAA datasets.
    Accessible data table available below.
  </p>
</figure>

<table>
  <caption>Annual Precipitation Data (inches)</caption>
  <thead>
    <tr><th>Year</th><th>Precipitation</th></tr>
  </thead>
  <tbody>
    <tr><td>1980</td><td>23.4</td></tr>
    <tr><td>1990</td><td>27.1</td></tr>
    <tr><td>2020</td><td>30.5</td></tr>
  </tbody>
</table>
```

**Implementation Notes**
- Include `<figcaption>` for every chart with descriptive text.  
- Provide accessible table or CSV download alternative.  
- For dynamic charts, announce updates via `aria-live="polite"`.  
- Apply semantic region roles (`role="img"` or `role="graphics-document"`).  

---

## 🎨 Design Tokens

| Token | Purpose | Example |
|--------|----------|---------|
| `chart.focus.color` | Focus outline for chart elements | `#FFD54F` |
| `chart.series.palette` | Colorblind-safe series palette | Okabe-Ito palette |
| `chart.axis.label.color` | Axis label color | `#212121` |
| `chart.tooltip.bg` | Tooltip background | `#333333E6` |
| `chart.transition.speed` | Animation duration | `0.3s` |

Okabe-Ito Palette (default for data series):
```json
["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
```

---

## ⚙️ Keyboard Interaction Matrix

| Key | Behavior | Description |
|------|-----------|-------------|
| `Tab` | Focus next data series or legend entry | Sequential focus order |
| `Arrow Keys` | Move focus between data points | Announces value via `aria-live` |
| `Enter` | Activate tooltip or focus state | Displays detailed data |
| `Esc` | Close tooltip or exit chart focus | Returns to previous UI element |

---

## 🧾 FAIR+CARE Visualization Ethics

| Category | Guideline |
|-----------|------------|
| **Representation** | Avoid visual distortion (e.g., truncated axes). |
| **Consent** | Include consent metadata for culturally sensitive datasets. |
| **Tone** | Frame data context neutrally; avoid stigmatizing terms. |
| **Attribution** | Display data provenance and FAIR metadata sources. |

Example Ethical Metadata:
```html
<div data-origin="NOAA" data-fair-consent="approved" data-ethics-reviewed="true"></div>
```

---

## 🧪 Testing & Validation

| Tool | Validation Type | Output |
|-------|------------------|--------|
| **axe-core** | Chart role & focus checks | `reports/self-validation/web/a11y_charts.json` |
| **Lighthouse CI** | Visual contrast and color independence | `reports/ui/lighthouse_charts.json` |
| **jest-axe** | React chart component ARIA validation | `reports/ui/a11y_chart_components.json` |
| **Manual Audit** | NVDA / VoiceOver chart summaries | FAIR+CARE Council audit log |

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|------------|----------------|
| **Collective Benefit** | Charts co-designed for equitable knowledge sharing. |
| **Authority to Control** | Users can toggle sensitive datasets before display. |
| **Responsibility** | Data sources annotated with provenance & consent tags. |
| **Ethics** | Visualization text and colors reviewed for neutrality. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-10 | FAIR+CARE A11y Council | Defined accessible chart visualization standards, colorblind-safe palettes, and ethical data context patterns. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Map Controls](map-controls.md) · [Back to A11y Patterns Index](README.md)

</div>
