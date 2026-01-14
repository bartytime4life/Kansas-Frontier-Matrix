# 📊 Chart Tokens (Design Tokens)
![KFM](https://img.shields.io/badge/KFM-Web%20Charts-0B5FFF?style=for-the-badge)
![Tokens](https://img.shields.io/badge/Design%20Tokens-Single%20Source%20of%20Truth-111827?style=for-the-badge)
![Provenance](https://img.shields.io/badge/Provenance-First-16A34A?style=for-the-badge)
![A11y](https://img.shields.io/badge/Accessibility-A11y-7C3AED?style=for-the-badge)
![Responsive](https://img.shields.io/badge/Responsive-UI-0EA5E9?style=for-the-badge)

> [!IMPORTANT]
> **“Tokens” in this folder = _design tokens_** (colors, typography, spacing, motion, semantics for charts).  
> They are **NOT** API keys, session cookies, auth tokens, or anything security-sensitive. 🔐

---

## 🧭 Why this folder exists

Kansas Frontier Matrix (KFM) charts are not “pretty add-ons” — they’re **evidence surfaces**: time series, summaries, distributions, comparisons, and model outputs that must remain **consistent, readable, accessible, and provenance-aware** across:

- 📍 Map popups & side panels (e.g., clicking a station opens a chart)
- 🧵 Story Nodes / narrative walkthroughs
- 🧠 Focus Mode (evidence-backed responses + citations)
- 🌗 Themes (light/dark), 🖥️ desktop, 📱 mobile

This folder is where we keep **one shared language** for chart visuals and behavior — so we don’t end up with:
- hardcoded hex values sprinkled across components
- inconsistent legends / axis styles
- charts that “look right” but mislead or hide uncertainty
- charts that break contrast rules in dark mode

---

## 📍 Location

`web/assets/charts/tokens/`

---

## 🗂️ Suggested folder structure (scaffold)

> [!NOTE]
> The exact filenames can vary — but the **separation of concerns** is the key.

```text
🌐 web/
└─ 🎛️ assets/
   └─ 📊 charts/
      └─ 🧩 tokens/
         ├─ 📘 README.md  ✅ (you are here)
         ├─ 🧾 tokens.schema.json          # JSON schema validation (contract-first)
         ├─ 🧱 primitives.tokens.json      # raw “atoms” (base colors, sizes, fonts)
         ├─ 🧠 semantic.tokens.json        # meaning-based tokens (axis, grid, series)
         ├─ 🧩 components.tokens.json      # component-level tokens (tooltip, legend, etc.)
         ├─ 🌗 themes/
         │  ├─ 🌞 light.theme.json
         │  └─ 🌚 dark.theme.json
         ├─ 🎨 palettes/
         │  ├─ 🧪 categorical.palette.json
         │  ├─ 🌡️ sequential.palette.json
         │  └─ ⚖️ diverging.palette.json
         ├─ ♿ a11y.tokens.json             # contrast targets, focus rings, patterns
         ├─ 🎞️ motion.tokens.json          # transitions, durations, easing
         └─ 🧪 tokens.testcases.json        # sample usage snapshots / regression fixtures
```

---

## 🧱 Token model (what a “token” looks like)

We treat tokens like **data contracts** — small, typed, documented, and stable.

### ✅ Minimal token shape (recommended)

```json
{
  "chart.color.axis": {
    "type": "color",
    "value": "var(--kfm-fg-muted)",
    "description": "Axis line + tick label color (non-primary).",
    "deprecated": false
  }
}
```

### Optional metadata fields (highly useful)

- `since`: version introduced
- `replaces`: older token name
- `constraints`: e.g., “must pass WCAG AA vs background”
- `examples`: “used in time series charts, histograms, tooltips…”
- `provenance`: link to the design decision (ADR / issue / doc)

---

## 🧠 Token layers (don’t skip this)

### 1) 🧱 Primitive tokens
Raw values you rarely use directly in components.

Examples:
- `color.gray.700`
- `font.size.2`
- `space.3`
- `stroke.1`

### 2) 🧠 Semantic tokens
Meaning-based names you use everywhere.

Examples:
- `chart.color.axis`
- `chart.color.grid`
- `chart.text.title`
- `chart.series.default.strokeWidth`

### 3) 🧩 Component tokens
Component-specific finishing touches.

Examples:
- `chart.tooltip.background`
- `chart.legend.itemGap`
- `chart.brush.selectionFill`

> [!TIP]
> Semantic tokens make refactors safe: you can change the theme without touching chart code.

---

## 🏷️ Naming conventions (stable + searchable)

**Rule:** tokens should read like a sentence fragment and sort cleanly.

✅ Good:
- `chart.color.axis`
- `chart.color.series.0`
- `chart.size.tick.length`
- `chart.legend.text`
- `chart.state.hover.opacity`

🚫 Avoid:
- `blueLine1`
- `axisGrey`
- `thingySpacing`

### Recommended namespace prefixes

| Namespace | Purpose |
|---|---|
| `chart.color.*` | color system for charts (axes, grid, series, status) |
| `chart.text.*` | typography and text styling |
| `chart.space.*` | padding/margins/gaps |
| `chart.size.*` | dimensions (tick length, marker size, corner radius) |
| `chart.line.*` | stroke widths, dash patterns |
| `chart.point.*` | point radius, hitbox size |
| `chart.area.*` | area fills, gradients, opacity |
| `chart.legend.*` | legend layout + typography |
| `chart.tooltip.*` | tooltip styling |
| `chart.annotation.*` | event markers, bands, labels |
| `chart.interaction.*` | hover/active/selected/brush states |
| `chart.a11y.*` | focus rings, patterns, contrast thresholds |
| `chart.motion.*` | animation + reduced motion support |

---

## 🎨 Color & palette guidance (maps + charts)

Charts and map symbology should feel like they belong to the **same visual system**.

### Qualitative vs quantitative 🧠
- **Qualitative / categorical** series → use distinct hues (category palette)
- **Quantitative / magnitude** values → use sequential ramps (light → dark)
- **Deviation around a reference** (e.g., above/below baseline) → use diverging ramps

### Classification (bins) 🎯
When converting continuous values into classes (especially for choropleth-style legends):
- Don’t “over-bin” (too many classes becomes noise)
- Don’t “under-bin” (too few hides structure)
- Prefer sane defaults and document the chosen method (equal interval, quantile, natural breaks)

> [!WARNING]
> Classification choices can dramatically change perceived patterns. Always document the method in the legend/caption when it matters.

---

## 🧾 Provenance hooks (Focus Mode compatible)

KFM’s philosophy: **the user should always be able to see “the map behind the map.”** 🗺️✨  
Charts should support that the same way maps do.

### Required UI affordances (design intention)
- 🏷️ **Caption citations** (dataset + provider + year/time span)
- 🧾 “Details” affordance to open:
  - source metadata
  - processing lineage (PROV)
  - units, transform steps, model config (if derived)
- 🧭 Tooltip text that clarifies what the datum is (not just the value)

### Token support for provenance UI
Define consistent tokens for:
- `chart.annotation.citationText`
- `chart.tooltip.metaText`
- `chart.badge.derived`
- `chart.badge.aiGenerated`
- `chart.state.redacted.*` (see below)

---

## 🧵 Timeline + events tokens (historical-first UI)

Time is a primary navigation axis in KFM (scrub years, show events like “Dust Bowl 1931–1939”).  
Charts should share a consistent token set for:

- `chart.annotation.eventMarker.*`
- `chart.annotation.eventBand.*`
- `chart.axis.time.*`
- `chart.interaction.scrubLine.*`

Bonus: keep these aligned with timeline slider tokens so the UI feels cohesive.

---

## ♿ Accessibility (A11y) requirements

### Contrast
- Axis labels, legend text, and tooltip text must maintain contrast in **both** themes.
- Don’t rely on color alone: add **shape/line style** differences.

Tokens to include:
- `chart.a11y.focusRing.color`
- `chart.a11y.focusRing.width`
- `chart.line.dash.*` (distinct patterns)
- `chart.point.shape.*` (if applicable)

### Reduced motion
Respect system settings:
- `prefers-reduced-motion: reduce`

Tokens to include:
- `chart.motion.duration.fast`
- `chart.motion.duration.slow`
- `chart.motion.easing.standard`
- `chart.motion.enabled` (boolean / mode switch)

---

## 📱 Responsive behavior (tokenized)

Charts must degrade gracefully:
- fewer ticks
- simplified legends
- stacked panels / collapsible metadata
- larger tap targets on touch devices

**Why tokens?** So responsive behavior is consistent and testable.

Tokens to include:
- `chart.breakpoint.sm`, `chart.breakpoint.md`, `chart.breakpoint.lg`
- `chart.size.tapTargetMin`
- `chart.legend.layout.mobile`
- `chart.axis.tickDensity.mobile`

---

## ⚡ Performance notes (KFM-scale data)

KFM is built to handle everything from local community layers to NASA-scale remote sensing pipelines.  
Charts must therefore be able to handle:

- large time series (downsampling / aggregation)
- streaming updates (progressive rendering)
- expensive tooltips (avoid heavy recompute on hover)

Token strategy that helps performance:
- prefer constant-time style lookup (`tokens[name]`)
- avoid per-point dynamic styling unless needed
- keep palettes finite and precomputed

---

## 🔒 Sensitive / redacted data states (Focus Mode-safe)

Sometimes we must withhold or generalize sensitive data, while clearly signaling why.

Tokens to include:
- `chart.state.redacted.fill`
- `chart.state.redacted.stroke`
- `chart.state.redacted.text`
- `chart.state.redacted.pattern`
- `chart.state.redacted.badge`

UI behavior:
- Show a small “redacted” badge + a short explanation
- Keep the rest of the chart UI functional (axes, context, metadata)

---

## 🧪 Validation & CI (contract-first)

Treat tokens like compile-time contracts ✅

Recommended gates:
1. JSON schema validation (`tokens.schema.json`)
2. type validation (`color`, `size`, `font`, etc.)
3. theme completeness (light/dark must define required semantic tokens)
4. a11y checks (contrast thresholds for text tokens)
5. snapshot / visual regression tests for core charts

---

## 🔧 How to use tokens (examples)

### ✅ CSS (custom properties)
```css
.chartAxis {
  color: var(--kfm-chart-color-axis);
  font-size: var(--kfm-chart-text-axis-size);
}
```

### ✅ TypeScript / JS (token lookup)
```ts
import tokens from "@/assets/charts/tokens/semantic.tokens.json";

const axisColor = tokens["chart.color.axis"].value;
```

### ✅ Chart library config (generic)
```ts
const theme = {
  axis: {
    stroke: tokens["chart.color.axis"].value,
    tick: { stroke: tokens["chart.color.tick"].value },
    label: { fill: tokens["chart.color.axisLabel"].value }
  },
  grid: {
    stroke: tokens["chart.color.grid"].value,
    strokeWidth: tokens["chart.line.grid.width"].value
  }
};
```

---

## ✅ Contribution checklist (PR-ready)

- [ ] Added/updated token in the correct layer (primitive vs semantic vs component)
- [ ] Token includes `type`, `value`, and `description`
- [ ] Works in 🌞 light and 🌚 dark themes
- [ ] Legend/tooltip states considered (hover/selected/disabled)
- [ ] A11y reviewed (contrast + not color-only)
- [ ] Schema + tests updated
- [ ] If renaming: added `replaces` + left an alias (deprecation path)

---

## 🧬 Design intent (one-liner)

> **Tokens make KFM charts consistent, accessible, performant, and provenance-aware — without hardcoding style decisions into chart components.**

---

## 📚 Project bookshelf (sources used by this token system)

<details>
<summary><strong>📖 KFM & governance docs</strong></summary>

- 📘 Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  
- 🧭 MARKDOWN_GUIDE_v13.md.gdoc  
- 🧩 Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf  
- 🧾 Audit of the Kansas Frontier Matrix (KFM) Repository.pdf *(if present in repo)*  
- 🧪 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx *(if present in repo)*  

</details>

<details>
<summary><strong>🗺️ Cartography, GIS, and geospatial visualization</strong></summary>

- 🗺️ making-maps-a-visual-guide-to-map-design-for-gis.pdf  
- 📱 Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf  
- 🏺 Archaeological 3D GIS_26_01_12_17_53_09.pdf  
- 🧑‍🍳 python-geospatial-analysis-cookbook.pdf  
- ☁️ Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf  

</details>

<details>
<summary><strong>📈 Stats, modeling, and “honest charts”</strong></summary>

- 🧠 Understanding Statistics & Experimental Design.pdf  
- 📉 graphical-data-analysis-with-r.pdf  
- 🧮 regression-analysis-with-python.pdf  
- 🧾 Regression analysis using Python - slides-linear-regression.pdf  
- 🎲 think-bayes-bayesian-statistics-in-python.pdf  
- 🛰️ Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf  
- 🧱 Generalized Topology Optimization for Structural Design.pdf  
- 🧩 Spectral Geometry of Graphs.pdf  

</details>

<details>
<summary><strong>🌐 Web, performance, databases, and systems</strong></summary>

- 🎨 responsive-web-design-with-html5-and-css3.pdf  
- 🧊 webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf  
- 🗃️ PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf  
- ⚡ Database Performance at Scale.pdf  
- 🧠 Scalable Data Management for Future Hardware.pdf  
- 🧬 Data Spaces.pdf  
- 🧵 concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf  
- 🖼️ compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf  

</details>

<details>
<summary><strong>🧭 Ethics, human factors, and security awareness</strong></summary>

- 🤝 Introduction to Digital Humanism.pdf  
- ⚖️ On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf  
- 🛡️ ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf  
- 🕶️ Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf  
- 🧠 Principles of Biological Autonomy - book_9780262381833.pdf  

</details>

<details>
<summary><strong>📚 Programming Books Compendiums</strong></summary>

- 📘 A programming Books.pdf  
- 📘 B-C programming Books.pdf  
- 📘 D-E programming Books.pdf  
- 📘 F-H programming Books.pdf  
- 📘 I-L programming Books.pdf  
- 📘 M-N programming Books.pdf  
- 📘 O-R programming Books.pdf  
- 📘 S-T programming Books.pdf  
- 📘 U-X programming Books.pdf  

</details>

---

🧩 **Next sibling folders (recommended):**
- `web/assets/charts/themes/` for chart-library specific themes
- `web/assets/charts/examples/` for golden reference charts (visual regression)
- `web/assets/charts/README.md` for top-level chart architecture
