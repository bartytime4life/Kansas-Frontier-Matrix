---
title: "📈 Kansas Frontier Matrix — Accessible Charts & Data Visualization Patterns (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/charts.md"
version: "v10.0.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / FAIR+CARE Accessibility Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-patterns-charts-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📈 **Kansas Frontier Matrix — Accessible Charts & Data Visualization Patterns**
`docs/accessibility/patterns/charts.md`

**Purpose:**  
Define **WCAG 2.1 AA**, **WAI-ARIA 1.2**, and **FAIR+CARE**-aligned patterns for building **accessible, ethical, and reproducible** charts in KFM (MapLibre/D3/Recharts/Cesium contexts). Covers structure, keyboarding, summaries, color, motion safety, and consent provenance.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../README.md)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../standards/faircare.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-success)](../../../releases/v10.0.0/manifest.zip)

</div>

---

## 📘 Overview

KFM visualizations must be **perceivable, operable, understandable, and robust**—and **ethically contextualized**.  
Every chart requires:
1) **Semantic container & labels**, 2) **Keyboard navigation**, 3) **Textual/data table alternative**, 4) **Color-agnostic encoding**, 5) **Motion & interaction safety**, 6) **Provenance/consent metadata**.

---

## 🗂️ Directory Context

```
docs/accessibility/patterns/
├── README.md
├── alerts.md
├── buttons.md
├── charts.md                 # ← This file
├── dialogs.md
├── forms.md
├── map-controls.md
└── navigation.md
```

---

## ♿ A11y Requirements Checklist (must-have)

| Requirement | Implementation | WCAG/ARIA |
|---|---|---|
| **Semantic Region** | Wrap chart in `role="figure"` + `aria-labelledby` + `aria-describedby`. | 1.3.1 / 1.3.2 / ARIA |
| **Keyboard Access** | Tab to chart, arrow keys move focus across data points; `Esc` exits focus mode. | 2.1.1 / 2.1.2 |
| **Data Table Alt** | Provide adjacent table (or downloadable CSV) of values/summary. | 1.1.1 / 1.4.1 |
| **Color Independence** | Never rely on color alone; use shapes, patterns, markers, and labels. | 1.4.1 |
| **Contrast** | Axes, labels, legends ≥ 4.5:1; focus rings ≥ 3:1. | 1.4.3 / 2.4.7 |
| **Live Announce** | Use `aria-live="polite"` for dynamic value readouts (e.g., tooltip summaries). | 4.1.3 |
| **Motion Safety** | Honor `prefers-reduced-motion`; avoid >3Hz flashing. | 2.3.1 / 2.3.3 |
| **Provenance/Consent** | Show source, license, and CARE consent badge. | FAIR+CARE |

---

## 🧩 Structural Pattern (SVG/D3/Recharts)

```html
<section
  role="figure"
  aria-labelledby="chart-title"
  aria-describedby="chart-summary"
>
  <h3 id="chart-title">Kansas Rainfall by Decade (1900–2025)</h3>

  <!-- SVG chart -->
  <svg role="img" aria-label="Bar chart showing average rainfall by decade">
    <!-- Use <title> for short title and <desc> for long descriptions -->
    <title>Kansas Rainfall by Decade</title>
    <desc>Average annual rainfall increased from 19.4 inches in the 1930s dust era to 25.8 inches in the 2010s.</desc>

    <!-- Bars, each focusable for keyboard traversal -->
    <g role="list">
      <rect role="listitem" tabindex="0" aria-label="1930s: 19.4 inches" ... />
      <rect role="listitem" tabindex="0" aria-label="1940s: 20.7 inches" ... />
      <!-- … -->
    </g>
  </svg>

  <p id="chart-summary">
    Trend: moderate increase in average rainfall since the 1930s. Source: NOAA NCEI (CC-BY 4.0). FAIR+CARE Certified ✅
  </p>

  <!-- Data table alternative -->
  <table aria-label="Table of rainfall by decade">
    <caption>Average annual rainfall</caption>
    <thead><tr><th>Decade</th><th>Inches</th></tr></thead>
    <tbody>
      <tr><td>1930s</td><td>19.4</td></tr>
      <tr><td>1940s</td><td>20.7</td></tr>
      <!-- … -->
    </tbody>
  </table>
</section>
```

**Notes**
- Prefer native focusable elements (`tabindex="0"`) for data points, or use a single **focus ring** with roving index.
- Summaries must state **trend, range, outliers, confidence/uncertainty**.

---

## 🎛️ Keyboard Interaction Model

| Key | Action |
|---|---|
| **Tab / Shift+Tab** | Enter/leave chart interactive region; cycle controls. |
| **Left/Right (or Up/Down)** | Move focus among data points/series. |
| **Enter/Space** | Toggle selection; pin value to summary region. |
| **Esc** | Exit chart interaction or close pinned tooltip. |
| **Ctrl+Plus/Minus** | Optional zoom if supported; announce zoom level. |

Use roving tabindex for performance: single `tabindex="0"` on active item, `-1` on others.

---

## 🎨 Color, Shape & Contrast

- Use **color-blind–safe palettes** (e.g., Okabe–Ito).  
- Provide **shape encodings** (circle, square, triangle) for series distinction.  
- Ensure **legend swatches** include patterns (stripes, dots) if multiple series.  
- Maintain **≥ 4.5:1 contrast** for text/lines; **≥ 3:1** for non-text UI glyphs.

**Design tokens:** `color.data.primary`, `color.data.secondary`, `color.text.primary`, `focus.outline.color`.

---

## 🧠 Ethical Visualization (FAIR+CARE)

| Guideline | Implementation |
|---|---|
| **Collective Benefit** | Visuals clarify—not persuade. Include limits/uncertainty. |
| **Authority to Control** | Cultural datasets show consent tags; hide restricted series. |
| **Responsibility** | Avoid cherry-picked axes; show baselines and units. |
| **Ethics** | Remove stigmatizing labels; use neutral language in summaries. |

Add **provenance chips**: Source • License • Consent (e.g., “IDGB Controlled Access ⚠️”).

---

## 🔊 Live Region & Tooltip Patterns

```tsx
<div id="chart-live" role="status" aria-live="polite" className="sr-only"></div>

function announce(point) {
  document.getElementById('chart-live').textContent =
    `${point.decade}: ${point.value} inches`;
}
```

- For tooltips: render a visible box with **static text** that mirrors the live-region message.  
- Avoid constant announcer spam: **debounce** updates on pointer move.

---

## 🌀 Motion & Animation Safety

- Disable transitions when `prefers-reduced-motion: reduce`.  
- Keep default transitions **≤ 200ms**; avoid flashing/flicker.  
- Do not auto-rotate or auto-advance charts.  
- Provide a “Pause Animations” toggle if any real-time visual updates occur.

---

## 🧪 Testing Matrix

| Test | Tool | Target |
|---|---|---|
| Axe/Lighthouse | `accessibility_scan.yml` | Roles, names, color contrast |
| Jest-axe Storybook | `storybook-a11y.yml` | Component-level charts |
| Keyboard E2E | Cypress/Playwright | Focus order, arrow nav, Esc |
| Colorblind Sim | CI visual compare | Palette independence |
| Motion Scan | Visual tests | `prefers-reduced-motion` respected |

---

## 🧾 Example Recharts Wrapper (TSX)

```tsx
<Figure role="figure" aria-labelledby="chart-title" aria-describedby="chart-summary">
  <h3 id="chart-title">County Precipitation Anomalies (2000–2025)</h3>

  <ResponsiveContainer width="100%" height={320}>
    <LineChart data={data} aria-label="Line chart of precipitation anomalies">
      {/* Accessible titles/descriptions via <title>/<desc> on the <svg> root are auto-added */}
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="year" />
      <YAxis label={{ value: "mm", angle: -90, position: "insideLeft" }} />
      <Line
        dataKey="anomaly"
        stroke="var(--color-data-primary)"
        dot={{ r: 3, tabIndex: 0, 'aria-label': (d: any) => `${d.year}: ${d.anomaly} mm` }}
        isAnimationActive={window.matchMedia('(prefers-reduced-motion: reduce)').matches ? false : true}
      />
      <Legend />
      <Tooltip content={({ active, payload }) =>
        active && payload?.length ? <div role="note">{payload[0].value} mm</div> : null
      } />
    </LineChart>
  </ResponsiveContainer>

  <p id="chart-summary">Anomalies vary within ±45 mm; 2011 drought outlier at −62 mm. Source: NOAA NCEI (CC-BY 4.0). FAIR+CARE Certified ✅</p>
</Figure>
```

---

## 📊 Quality Metrics

| Metric | Target | Verified By |
|---|---|---|
| **WCAG 2.1 AA** | 100% | CI + Manual |
| **Keyboard Operability** | 100% of charts navigable | E2E Tests |
| **Contrast Compliance** | 100% | Token Linter |
| **Color Independence** | 100% (patterns/markers present) | Visual Diff |
| **Motion Safety** | 100% `prefers-reduced-motion` | CI Visual |
| **FAIR+CARE Tone** | ≥ 95% | Ethics Review |

---

## ⚙️ CI/CD Validation

| Workflow | Purpose | Artifact |
|---|---|---|
| `accessibility_scan.yml` | Axe/Lighthouse chart a11y checks. | `reports/self-validation/web/a11y_summary.json` |
| `storybook-a11y.yml` | Component snapshots & jest-axe. | `reports/ui/a11y_component_audits.json` |
| `design-tokens-validate.yml` | Contrast & token usage. | `reports/ui/design-token-lint.json` |
| `faircare-visual-audit.yml` | Tone, context, consent checks. | `reports/faircare-visual-validation.json` |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v10.0.0 | 2025-11-10 | FAIR+CARE Accessibility Council | Initial accessible chart patterns covering structure, keyboarding, summaries, color/contrast, motion, and FAIR+CARE provenance. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Part of the **Accessibility Pattern Library** · Master Coder Protocol v6.3 · FAIR+CARE Certified  
[⬅ Back to Patterns Index](README.md) · [Navigation →](navigation.md)

</div>