# 📊 `web/assets/charts/` — Chart Assets & Specs

![KFM](https://img.shields.io/badge/KFM-web%2Fassets%2Fcharts-1f6feb)
![Provenance](https://img.shields.io/badge/provenance-required-2ea043)
![Accessible](https://img.shields.io/badge/a11y-ARIA%20%2B%20semantic%20HTML-8250df)
![Responsive](https://img.shields.io/badge/responsive-progressive%20enhancement-0969da)

> **Purpose:** This folder holds **static chart assets** (SVG/PNG/JPG) and **declarative chart specs** used by the KFM web UI (pop-ups, side panels, story embeds, printable exports).  
> **Not here:** React/TS code, query logic, or raw datasets.

---

## 🧭 Quick Navigation

- 📌 [Folder contract](#-folder-contract)
- 🗂️ [Suggested layout](#️-suggested-layout)
- 🧩 [Chart categories](#-chart-categories)
- 🔗 [Data contracts](#-data-contracts)
- 🧾 [Provenance rules](#-provenance-rules)
- ♿ [Accessibility + responsive rules](#-accessibility--responsive-rules)
- ⚡ [Performance & scale](#-performance--scale)
- 🖼️ [Export formats](#️-export-formats)
- ✅ [Add a new chart checklist](#-add-a-new-chart-checklist)
- 📚 [Project reference shelf](#-project-reference-shelf)

---

## 🚦 Folder Contract

### ✅ This folder is for…
- **Chart previews** for dataset catalog cards, story nodes, docs, and UI placeholders.
- **Declarative chart specs** (e.g., Vega/Vega-Lite JSON) that can be rendered in the client.
- **Chart manifests** describing:
  - what the chart shows,
  - which dataset(s) it depends on,
  - provenance + licensing,
  - default options + rendering hints.

### ❌ This folder is NOT for…
- React components, hooks, data fetching code  
  👉 those belong in `web/components/` (or `web/components/charts/`).
- Raw downloads, giant CSVs, or unprocessed rasters  
  👉 those belong under `data/` (sources/raw/processed/catalog/provenance).

---

## 🗂️ Suggested Layout

> If these subfolders don’t exist yet, create them as needed. Keep names **kebab-case** and stable.

```text
📁 web/
  📁 assets/
    📁 charts/
      📝 README.md
      📁 manifests/       # chart metadata + provenance pointers (yaml/json)
      📁 specs/           # declarative specs (vega/vega-lite/etc.)
      📁 previews/        # small previews for catalog/story/docs
      📁 exports/         # “final” static outputs used in UI
      📁 tokens/          # chart design tokens (scales, spacing, typography)
```

---

## 🧩 Chart Categories

KFM charts typically fall into these buckets:

| Category | Where it appears | Typical size | Suggested renderer |
|---|---|---:|---|
| 🪄 **Micro-charts** | Map pop-ups (sparkline, mini-bar) | tiny | SVG/Canvas |
| 📈 **Panel charts** | Dataset “Details” sidebar, dashboards | medium | Canvas (or SVG if small) |
| 🧭 **Map-coupled charts** | Linked brushing: map ↔ chart | medium/large | Canvas/WebGL |
| 🛰️ **Remote sensing charts** | Spectral curves, time series by AOI | medium | Canvas |
| 🧠 **Model/analysis charts** | Regression diagnostics, uncertainty bands | medium | Canvas/SVG |
| 🕸️ **Graph/network charts** | Knowledge-graph views, adjacency summaries | large | WebGL (optional) |

> Rule of thumb: **SVG for small + crisp**, **Canvas for medium**, **WebGL only when you truly need it**.

---

## 🔗 Data Contracts

### 1) Chart IDs are stable 📌
Every chart asset/spec should have a stable `chartId` that is:
- unique
- kebab-case
- *meaningful*
- versionable

Example:
- `weather-station-sparkline@v1`
- `county-population-trend@v2`
- `eo1-spectrum@v1`

### 2) Chart payload shape (recommended)
When your UI requests chart data from the API, prefer a **simple, explicit** payload:

```json
{
  "meta": {
    "chartId": "weather-station-sparkline@v1",
    "title": "Precipitation (last 10 years)",
    "x": { "label": "Date", "type": "time" },
    "y": { "label": "mm", "type": "number" },
    "notes": ["Values aggregated monthly."]
  },
  "series": [
    {
      "seriesId": "precip",
      "label": "Precipitation",
      "points": [
        { "x": "2016-01-01", "y": 12.4 },
        { "x": "2016-02-01", "y": 9.1 }
      ]
    }
  ],
  "provenance": {
    "datasetIds": ["noaa-station-precip@2025-10"],
    "catalogRefs": ["data/catalog/..."],
    "license": "CC-BY-4.0",
    "generatedAt": "2026-01-14T00:00:00Z",
    "query": { "stationId": "KSWICHITA001", "bucket": "month" }
  }
}
```

✅ **Why this shape works**
- UI has everything needed to label axes + units  
- chart component can stay “dumb” (render-only)
- provenance can be rendered as a “📎 Sources” drawer

---

## 🧾 Provenance Rules

### ✅ Always include…
- **Dataset IDs** (stable identifiers)
- **Catalog reference(s)** (where the dataset’s metadata lives)
- **License + attribution**
- **Generation timestamp**
- **Query parameters** (what exactly was requested / filtered)

### 🚫 Never do this in KFM UI…
- charts with *no* source (especially inside “assistive” views like Focus Mode)
- charts that can’t be traced back to cataloged/manifested data
- charts that embed sensitive locations or personal info

> ⚠️ If a chart is derived from a *sensitive* dataset, use aggregation / anonymization / fuzzing rules *before* it reaches the UI.

---

## ♿ Accessibility & Responsive Rules

### ♿ Accessibility checklist
- [ ] Title + axis labels + units are visible (or readable by screen readers)
- [ ] Don’t encode meaning by color **alone** (use shape/line-style/labels)
- [ ] Provide **high-contrast** compatibility
- [ ] Keyboard navigation works for key interactions (focusable legend, toggles)
- [ ] Tooltip content is reachable (not hover-only)

### 📱 Responsive checklist
- [ ] “Design dictates breakpoints” (don’t hardcode arbitrary breakpoints)
- [ ] Progressive enhancement (micro-chart still useful if animations are off)
- [ ] Functional parity across device tiers (not necessarily aesthetic parity)
- [ ] Tested on real devices (at least one phone + one tablet)

---

## ⚡ Performance & Scale

Charts are only “fun” when they’re fast 🏎️

### 🧮 Data-size rules of thumb
- Micro-charts: keep it **< 200 points** (downsample aggressively)
- Panel time series: **< 5k points** (bucket/aggregate)
- “Big scatter”: if you exceed this, switch to **Canvas/WebGL** or aggregate

### 🗜️ Prefer aggregation + caching
- Cache common queries (popular locations/datasets/time windows)
- Precompute “standard views” where it makes sense (daily/weekly/monthly rollups)
- Treat chart queries like a workload: repeated patterns are optimization gold

### 🎛️ Confidence / uncertainty is a first-class feature
If a chart communicates model outputs, include uncertainty bands / confidence intervals where appropriate.

---

## 🖼️ Export Formats

### ✅ Recommended formats
- **SVG** 🧾 for:
  - line charts, small multiples, icons, print-ready artifacts
- **PNG** 🧩 for:
  - rasterized charts that need transparency or exact pixel control
- **JPG** 📷 for:
  - photo-heavy content (avoid for plots unless there’s no alternative)

### 📏 DPI / sizing
- Provide `@1x` and `@2x` exports when a chart is used as an image in UI.
- Prefer “content-aware” sizing: labels shouldn’t get cut off at narrow widths.

---

## ➕ Add a New Chart Checklist

### 1) Create a manifest 🧾
Add `web/assets/charts/manifests/<chartId>.yml` containing:
- chart ID
- purpose + where it’s used
- dataset IDs + license
- pointers to catalog/provenance records
- default options + render hints

### 2) Add a preview 🖼️
Add `web/assets/charts/previews/<chartId>.png` (and optional `@2x`)

### 3) Add a spec (optional) 🧩
If you use declarative specs:
- `web/assets/charts/specs/<chartId>.json`

### 4) Wire it into UI 🔌
Reference the chartId from:
- a Story Node config
- a dataset details view
- a map popup template

### 5) Validate ✅
- [ ] provenance present
- [ ] license present
- [ ] axes labeled
- [ ] accessible defaults
- [ ] works on narrow screens

---

## 🧪 Testing Ideas

> These are patterns we recommend—add tooling as the repo matures.

- ✅ Schema validation: verify every manifest has required fields
- ✅ Visual regression: pixel-diff previews in CI for key charts
- ✅ Data contract tests: payload shape doesn’t drift across API versions
- ✅ “Focus Mode gate”: block charts without provenance from rendering

---

## 🧠 Chart Options Pattern (UI-friendly)

Borrow the “options object” pattern: keep chart behavior declarative and portable.

```js
const options = {
  title: "EO-1 spectrum",
  hAxis: { title: "Band" },
  vAxis: { title: "Reflectance" },
  legend: { position: "none" },
  pointSize: 3,
  // KFM extras 👇
  mode: "compact",          // compact | expanded
  showProvenance: true,
  allowExport: true
};
```

---

## 📚 Project Reference Shelf

This folder’s practices are guided by the project’s library across:
- 🧭 **Geospatial + cartography**
- 📊 **Statistics + regression + visualization**
- 🧠 **Machine learning + data mining**
- 🗄️ **Databases + scalable query systems**
- 🧩 **WebGL + interactive graphics**
- 🛡️ **Security + governance + ethics**

> Keep this README updated when the chart system evolves—charts are a “front door” to trust in the data. ✅