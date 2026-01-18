# 🗺️ Map Legend Templates (`_templates`)

![status](https://img.shields.io/badge/status-template%20library-blue)
![format](https://img.shields.io/badge/format-SVG%20%2B%20JSON-informational)
![provenance](https://img.shields.io/badge/provenance-first-success)
![a11y](https://img.shields.io/badge/a11y-WCAG%20AA-brightgreen)

> [!IMPORTANT]
> In **KFM**, a legend is *user-facing evidence*. If someone can’t interpret a layer without guessing, we’ve failed the platform’s **trust + transparency** goals.

---

## 📌 What lives here?

This folder contains **reusable legend templates** for the KFM web map UI (React + MapLibre; optionally Cesium in 3D views).  
Templates are meant to be **copied** and then customized into a per-layer legend asset.

### Suggested folder relationship 🧭

```text
web/assets/media/maps/legends/
├── 📁 _templates/                       # ✅ you are here (starter kits)
│   ├── 📄 README.md
│   ├── 📁 categorical/
│   ├── 📁 continuous/
│   ├── 📁 diverging/
│   ├── 📁 graduated-symbol/
│   └── 📁 bivariate/
└── 📁 <layer_slug>/                     # 🎯 final legends live here (recommended pattern)
    ├── 🖼️ legend.svg
    ├── 🧾 legend.manifest.json
    └── 🖼️ preview.png
```

> [!TIP]
> Keep templates **generic**. Anything layer-specific (dataset names, years, class breaks) belongs in the *copied* legend folder for that layer.

---

## ⚡ Quick Start (make a new layer legend)

1) **Pick a template** (categorical / continuous / graduated-symbol / bivariate).  
2) **Copy it** into a new layer folder: `web/assets/media/maps/legends/<layer_slug>/`  
3) Update:
   - `legend.svg` (layout + symbols)
   - `legend.manifest.json` (metadata + provenance pointers)
   - `preview.png` (optional but recommended)
4) Wire it into the layer config / registry so the UI knows which legend to display.

---

## 🧩 Template Types

| Template | Best for | What the legend must show |
|---|---|---|
| 🧱 **Categorical** | Land cover, admin classes, feature types | Swatch + label per category |
| 🌈 **Continuous (sequential)** | Elevation, precipitation, density | Gradient + numeric ticks + **units** |
| 🔥 **Diverging** | Change maps, anomalies | Two-sided scale + midpoint meaning (e.g., 0) |
| 🔘 **Graduated symbol** | Counts at points (events, stations) | Size key + representative values (or class breaks) |
| 🟦🟥 **Bivariate** | Two variables combined | 2D legend matrix + axis labels + units |
| 🕰️ **Time-aware add-on** | Temporal layers | “Time shown” label + interpretation hints |

---

## 🎨 Cartographic Rules of Thumb (KFM defaults)

> [!NOTE]
> Legends should be **self-explanatory**, readable at typical UI sizes, and not dominate the map.

### Layout & readability ✅
- Put **symbols on the left** and **labels on the right** (fast scanning).
- Avoid legends that become “mini-data catalogs.” If it’s too long:
  - group items (headers),  
  - or split into sections,  
  - or use an interactive legend UI (collapse/expand).
- Prefer a subtle container (border / background) so the legend is clearly bounded.

### Units & methods are not optional 🧪
If a legend communicates **numbers**, it must include:
- **units** (e.g., `mm`, `°C`, `%`, `people / km²`)
- **classification method** if applicable (quantiles, natural breaks, equal interval, custom thresholds)
- **time shown** for time-sliced renders (year/month/date)

### Classified vs unclassified (graduated symbols) 🔘
- **Classified**: one symbol size per class (easier matching, less detail)
- **Unclassified**: symbol scales per value (more detail, harder matching; use representative sizes)

---

## ♿ Accessibility & Inclusivity (non-negotiable)

### Color & contrast 🌈
- Use **colorblind-friendly palettes** by default.
- Don’t rely on color alone:
  - add patterns / outlines, or  
  - distinct shapes when categories matter.
- Ensure readable contrast for:
  - legend text
  - swatches against legend background
  - legend container against map content

### Responsive sizing 📱🖥️
Design legends to remain legible in:
- side-panel layout (desktop)
- bottom-sheet layout (mobile/tablet)
- reduced map viewport (split panels, story mode, etc.)

---

## 🧾 Provenance & Attribution (KFM-style)

KFM is **provenance-first** and **evidence-first**. A legend should make it easy to trace:
- what the layer means
- where its symbology came from
- what units and thresholds are used
- what dataset + license governs use

**Rule:** if the UI shows a legend, the user should be able to discover the dataset source/license via the layer info panel and/or legend metadata.

### `legend.manifest.json` (recommended contract)

> If this contract doesn’t exist yet in code, treat this as the spec we’re converging on (and add a schema under `schemas/ui/` when ready).

```json
{
  "$schema": "../../../schemas/ui/legend-template.schema.json",
  "id": "landcover_categorical_v1",
  "title": "Land Cover (Categorical)",
  "legendType": "categorical",
  "version": "1.0.0",

  "render": {
    "svg": "./legend.svg",
    "preview": "./preview.png"
  },

  "units": null,
  "classification": null,

  "items": [
    { "label": "Cropland", "swatch": { "type": "fill", "color": "#E6D08A" } },
    { "label": "Grassland", "swatch": { "type": "fill", "color": "#9AC27A" } }
  ],

  "provenance": {
    "datasetRefs": [
      "dcat://datasets/kansas_landcover_2020",
      "stac://collections/kansas_landcover"
    ],
    "styleRefs": [
      "maplibre-style://styles/landcover.json"
    ],
    "license": "CC-BY-4.0",
    "attribution": "Kansas Land Cover Program"
  },

  "a11y": {
    "contrastTarget": "WCAG-AA",
    "patternFallback": true
  }
}
```

### Provenance checklist 🧠
- [ ] Legend labels match the **actual style** in MapLibre (no drift).
- [ ] Units are correct and shown consistently.
- [ ] Thresholds/class breaks are documented when used.
- [ ] License + attribution are present (directly or via dataset reference).
- [ ] If the layer is time-sliced: legend indicates **time shown**.

---

## 🧰 SVG authoring guidelines

### Do ✅
- Use a `viewBox` so legends scale cleanly.
- Keep text as text (don’t outline fonts unless absolutely necessary).
- Prefer simple shapes; avoid overly complex paths.
- Keep a consistent padding grid (8px rhythm works well for UI).

### Don’t ❌
- Don’t embed huge raster images inside SVG.
- Don’t hardcode legend colors that disagree with the actual layer style.
- Don’t include sensitive details in legend text if the underlying data is restricted.

---

## 🧪 QA / “Definition of Done” for a legend

- [ ] **Correctness**: colors/symbols match the rendered layer.
- [ ] **Interpretability**: a new user can explain what the layer means using the legend alone.
- [ ] **Units + methods**: present where numeric values are shown.
- [ ] **Accessible**: color isn’t the only channel; text is readable.
- [ ] **Provenance**: dataset/style refs present (or linkable through UI).
- [ ] **Preview**: `preview.png` updated (recommended).
- [ ] **Size**: works in the smallest intended UI placement.

---

## 🔁 When should we *not* use a custom legend?

Use **auto-generated** legends when:
- the MapLibre style JSON already includes stable categorical stops / ramp metadata
- the legend can be derived without ambiguity

Use **custom legends** when:
- the layer needs extra explanation (methods, caveats, time windows)
- the legend includes multi-part elements (matrix legends, nested categories, symbol+stroke combos)
- governance requires explicit attribution or uncertainty notes at the legend level

---

## 📚 Related docs (inside the repo)

- `docs/MASTER_GUIDE_v13.md` — pipeline + evidence-first rules
- `docs/standards/` — STAC/DCAT/PROV profiles and governance
- `schemas/ui/` — UI contracts (recommended home for legend schema)
- `web/` — UI implementation (legend panel / layer controls)

---

## 🙋 FAQ

### “Where should citations live — in the legend or the layer panel?”
Prefer **layer panel** as the canonical place, but the legend’s manifest must include enough metadata to *link back* to provenance.

### “How do we keep legends from drifting from styles?”
Treat legend specs as **contracts**:
- a manifest that references the style source
- plus validation or review gates in PRs

### “What about sensitive datasets?”
No output artifact (including legends) should be **less restricted than its inputs**. If a layer is restricted, ensure the legend does not expose sensitive thresholds, categories, or locations.
