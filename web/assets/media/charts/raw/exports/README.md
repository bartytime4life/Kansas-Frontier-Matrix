# 📊 Chart Exports (Raw) — `web/assets/media/charts/raw/exports/`

![scope](https://img.shields.io/badge/scope-web-blue)
![asset-type](https://img.shields.io/badge/type-charts%20%26%20viz-6f42c1)
![preferred-format](https://img.shields.io/badge/prefer-SVG-important)
![kfm-principle](https://img.shields.io/badge/principle-provenance--first-success)

> [!IMPORTANT]
> This folder is the **source-of-truth for chart *exports*** (static chart images) used by the KFM web experience.  
> Keep files **stable, attributable, and traceable** — every chart should be explainable and reproducible.

---

## 🧭 Where you are

```text
📁 web/
  📁 assets/
    📁 media/
      📁 charts/
        📁 raw/
          📁 exports/
            📄 README.md   👈 you are here
```

---

## ✅ What belongs here

Put **raw exported chart assets** here (before any optimization/derivation steps):

- 🧾 **SVG** exports (`.svg`) — preferred for most charts
- 🖼️ **PNG** exports (`.png`) — acceptable for raster/heatmaps or when SVG becomes too heavy
- 🧷 **Sidecar provenance metadata** (`.meta.json`) — **required** for every chart asset
- 📝 Optional: a tiny `.source.txt` or `.source.md` pointer to the generating notebook/script/design file

---

## 🚫 What does NOT belong here

- 🧱 Build artifacts (hashed filenames, `dist/`, bundler outputs)
- 🧪 One-off screenshots without provenance
- 🧨 Massive binaries (if it’s huge, it probably belongs in `data/` with proper versioning)
- 🔒 Proprietary assets without explicit license/attribution clearance

---

## 🧬 Provenance-first rule (required) ✨

Every chart export must ship with a **sidecar metadata file** so the UI (and humans) can trace:

- **What data** was used (dataset ID / catalog reference)
- **How** it was produced (pipeline/notebook/script + parameters)
- **When** it was generated
- **Who/what** to attribute (license + sources)
- **How to describe it accessibly** (alt text)

### 📌 Sidecar naming

For an export named:

- `rainfall_timeseries__flint-hills--v1.svg`

Add:

- `rainfall_timeseries__flint-hills--v1.meta.json`

If you export multiple formats, **reuse the same** `.meta.json` for the set.

---

## 🏷️ Naming conventions (keep filenames stable)

**Goal:** stable URLs + predictable imports.

### Recommended pattern

```text
<chart_slug>--v<major>[.<minor>].<ext>
```

Examples:
- `rainfall_timeseries__flint-hills--v1.svg`
- `rainfall_timeseries__flint-hills--v1.png`
- `soil_moisture_boxplot__ks-statewide--v2.1.svg`

### Slug guidelines ✅
- use **kebab-case** (or `snake_case`) consistently
- keep it **short but specific**
- prefer **semantic meaning** over “today’s date”
- bump version when the chart’s meaning/layout changes in a breaking way

> [!TIP]
> If a chart is referenced by Story Nodes or UI code, **don’t rename it**—create a new version.

---

## 📦 Recommended export formats & settings

### 🥇 SVG (preferred)
- Keep `viewBox` intact (responsiveness ✅)
- Avoid embedded base64 rasters unless necessary
- Keep text as text when possible (better a11y), but ensure fonts are compatible with the web app

### 🥈 PNG (fallback)
- Use when:
  - the chart is effectively a raster (dense heatmaps)
  - SVG becomes too large / slow to render
- Export at **2×** for retina when reasonable (but watch file size)

---

## ♿ Accessibility checklist (don’t skip)

For every chart:
- [ ] Provide **meaningful alt text** in the `.meta.json`
- [ ] Avoid “color-only” encoding (use patterns/labels where possible)
- [ ] Ensure legibility at small sizes (mobile-first)

---

## 🧾 `.meta.json` template (copy/paste)

> [!NOTE]
> This is intentionally lightweight and “UI-friendly”. We can evolve this into a stricter schema later.

```json
{
  "chart_id": "urn:kfm:chart:<domain>:<slug>:v1",
  "title": "Human-readable chart title",
  "description": "What this chart shows and why it exists.",
  "tags": ["kfm", "chart", "timeseries"],

  "data_inputs": [
    {
      "dataset_id": "urn:kfm:dataset:<domain>:<name>:<version>",
      "catalog_ref": "data/stac/items/<item>.json",
      "notes": "Any important filtering/aggregation notes."
    }
  ],

  "generation": {
    "method": "notebook|script|design-tool",
    "source_ref": "mcp/experiments/<...>.ipynb OR src/pipelines/<...>.py",
    "parameters": {
      "region": "Flint Hills",
      "time_start": "1890-01-01",
      "time_end": "2020-12-31",
      "aggregation": "monthly_mean"
    },
    "generated_at": "YYYY-MM-DD",
    "commit_hint": "optional git sha"
  },

  "provenance": {
    "prov_bundle_ref": "data/prov/<run_id>.json",
    "notes": "How to reproduce this chart."
  },

  "license": {
    "chart_asset_license": "CC-BY-4.0",
    "source_data_licenses": ["CC-BY-4.0", "ODC-BY-1.0"],
    "attribution": [
      { "name": "Source Org", "url": "https://example.org", "license": "CC-BY-4.0" }
    ]
  },

  "accessibility": {
    "alt": "Concise description of the chart for screen readers.",
    "long_desc": "Optional longer explanation for evidence panels or docs.",
    "colorblind_safe": true
  }
}
```

---

## 🔌 Using these exports in the web UI

### Option A — import (bundler-friendly)
```tsx
// Example (adjust path aliasing to match the app build)
import chartUrl from "./rainfall_timeseries__flint-hills--v1.svg";

export function ChartExample() {
  return (
    <img
      src={chartUrl}
      alt="Rainfall over time in the Flint Hills."
      loading="lazy"
    />
  );
}
```

### Option B — reference by relative URL
```html
<img
  src="/assets/media/charts/raw/exports/rainfall_timeseries__flint-hills--v1.svg"
  alt="Rainfall over time in the Flint Hills."
  loading="lazy"
/>
```

> [!TIP]
> If you’re wiring this into Story Nodes, keep filenames stable and treat version bumps as *content releases* 📦

---

## 🧰 Optimization (recommended, but keep raw exports pristine)

Raw exports can be optimized in a derived step (do **not** destroy the source-of-truth export):

- ✂️ SVG: run through an SVG optimizer (e.g., SVGO)
- 🧽 PNG: run lossless compression (e.g., oxipng/pngquant with caution)

> [!IMPORTANT]
> If you add an “optimized” sibling directory later, treat **this folder as the input** and the optimized folder as a build artifact.

---

## ✅ PR / review checklist

Before merging chart assets:
- [ ] File names follow the convention and are stable
- [ ] `.meta.json` exists and is complete (data + method + attribution + alt text)
- [ ] Chart is readable on mobile widths
- [ ] No sensitive data is accidentally exposed in labels/tooltips
- [ ] File sizes are reasonable (SVG not megabytes, PNG not absurd)

---

## 🧩 Quick examples

```text
📄 rainfall_timeseries__flint-hills--v1.svg
📄 rainfall_timeseries__flint-hills--v1.png
📄 rainfall_timeseries__flint-hills--v1.meta.json
📄 rainfall_timeseries__flint-hills--v1.source.txt   (optional)
```

---

## 🧠 Philosophy (why we’re strict here)

KFM treats visuals as *evidence-bearing artifacts* — charts are not decoration; they are part of the system’s auditable story.  
A chart without provenance is just a picture. A chart with provenance is a reusable scientific object 🔍📚
