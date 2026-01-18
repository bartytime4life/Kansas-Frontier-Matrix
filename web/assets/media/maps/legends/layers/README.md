# 🗺️ Layer Legends (Web UI)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-0B7285?style=for-the-badge)
![Path](https://img.shields.io/badge/path-web%2Fassets%2Fmedia%2Fmaps%2Flegends%2Flayers-495057?style=for-the-badge)
![Assets](https://img.shields.io/badge/assets-SVG%20%7C%20PNG%20%7C%20JSON-6C757D?style=for-the-badge)

> [!NOTE]
> This folder is the **canonical home for map-layer legend assets** used by the KFM web app.
> If a layer is visible in the UI, it should have a legend here (or an explicit “no legend” contract).

---

## 🎯 Purpose

Legends are UI “translation layers” that turn map symbology into human-readable meaning.

This directory supports:
- **Readable legends** (clarity + consistent typography)
- **Accessible legends** (high-contrast friendly, screen-reader friendly)
- **Provenance-friendly legends** (no “mystery layers”: legends should point back to a dataset ID / catalog entry)

---

## 🧭 Quick Navigation

- [📁 Folder contract](#-folder-contract)
- [🧾 `legend.json` contract](#-legendjson-contract)
- [🎨 Legend types](#-legend-types)
- [♿ Accessibility rules](#-accessibility-rules)
- [🧠 Provenance & attribution](#-provenance--attribution)
- [➕ Add a new layer legend](#-add-a-new-layer-legend)
- [✅ QA checklist](#-qa-checklist)

---

## 📁 Folder Contract

### ✅ Required per-layer structure

Each layer gets its own folder named after the **layer ID** (prefer matching your dataset/catalog ID).

```text
web/assets/media/maps/legends/layers/
├── README.md
└── <layer_id>/
    ├── legend.json           # required (machine-readable legend contract)
    └── legend.svg            # required (preferred visual legend asset)
```

### ➕ Optional (recommended) files

```text
<layer_id>/
├── legend.dark.svg           # if the UI supports dark backgrounds
├── legend.png                # fallback for environments that don’t render SVG well
├── legend@2x.png             # retina fallback
├── preview.png               # tiny card image / layer picker thumbnail
└── icons/
    ├── <symbol>.svg          # icon library for point/line symbols (optional)
    └── ...
```

> [!TIP]
> Prefer **SVG** for crisp scaling. Use PNG as a fallback when you need pixel-perfect raster textures.

---

## 🧾 `legend.json` Contract

### Why a JSON legend?

Because the UI often needs to:
- Render a legend responsively (mobile vs desktop)
- Announce legend content to assistive tech (ARIA / screen readers)
- Validate that every layer shown to users has a predictable “meaning contract”
- Cross-link to dataset provenance / licensing in the catalog

### Minimal example (categorical)

```json
{
  "legend_version": "1.0.0",
  "layer_id": "usda_crops_2020",
  "title": "Crop Types",
  "subtitle": "Kansas (2020)",
  "kind": "categorical",
  "items": [
    { "label": "Corn", "fill": "#F2C94C" },
    { "label": "Wheat", "fill": "#F2994A" },
    { "label": "Soybeans", "fill": "#27AE60" }
  ],
  "dataset_ref": {
    "dataset_id": "usda_crops_2020"
  }
}
```

### Minimal example (continuous ramp)

```json
{
  "legend_version": "1.0.0",
  "layer_id": "ndvi_timeseries",
  "title": "Vegetation Index (NDVI)",
  "kind": "ramp",
  "units": "NDVI",
  "ramp": {
    "min": 0.0,
    "max": 1.0,
    "stops": [
      { "value": 0.0, "color": "#F2F2F2", "label": "Low" },
      { "value": 0.5, "color": "#A6D96A", "label": "Moderate" },
      { "value": 1.0, "color": "#1A9850", "label": "High" }
    ]
  },
  "dataset_ref": {
    "dataset_id": "ndvi_timeseries"
  }
}
```

---

### Field reference

| Field | Type | Required | Example | Notes |
|---|---:|:---:|---|---|
| `legend_version` | string | ✅ | `"1.0.0"` | Treat as a **contract** (version if you change meaning/shape). |
| `layer_id` | string | ✅ | `"usgs_historic_topo_1894"` | Should match layer registry / map style config. |
| `title` | string | ✅ | `"USGS Historical Topo"` | Human-facing label. Keep short. |
| `subtitle` | string | ⛔ | `"Ellsworth County (1894)"` | Optional context (time, region, method). |
| `kind` | enum | ✅ | `"categorical"` | See [Legend types](#-legend-types). |
| `units` | string\|null | ⛔ | `"m"`, `"°C"` | Only when meaningful. |
| `items` | array | ⚠️ | `[{...}]` | Required for categorical/classes. |
| `ramp` | object | ⚠️ | `{min,max,stops}` | Required for ramps/continuous legends. |
| `dataset_ref` | object | ✅ | `{ "dataset_id": "..." }` | Connects legend → catalog/provenance. |
| `notes` | string | ⛔ | `"Derived from …"` | Short methodology note. Avoid essays here. |
| `ui` | object | ⛔ | `{ "orientation": "vertical" }` | Optional rendering hints (keep minimal). |

---

### Legend `items[]` reference

Use `items` for discrete keys (categories, classes, symbol sets).

| Item field | Type | When | Example | Notes |
|---|---:|---|---|---|
| `label` | string | always | `"Railroad"` | Visible in legend + announced via screen readers. |
| `fill` | hex string | polygons / swatches | `"#2D9CDB"` | Fill color. |
| `stroke` | hex string | outlines / lines | `"#1B1B1B"` | Stroke color. |
| `strokeWidth` | number | when needed | `2` | Use integers where possible. |
| `dash` | number[] | dashed lines | `[2, 2]` | Matches map style dash array concept. |
| `shape` | enum | point symbols | `"circle"` | If no icon is provided. |
| `icon` | string | point symbols | `"icons/camp.svg"` | Relative path under the layer folder. |
| `value` | number\|string | categorical/classed | `"A"` or `10` | Optional; useful for machine sorting. |
| `range` | [number, number] | classes | `[0, 25]` | Prefer inclusive ranges in UI labels. |

---

## 🎨 Legend Types

Supported `kind` values (recommended set):

- `categorical` 🧩  
  Discrete categories (land cover classes, treaty types, feature types)

- `classes` 📊  
  Binned numeric ranges (population density classes, drought severity bins)

- `ramp` 🌈  
  Continuous ramp (NDVI, temperature anomalies, elevation shading)

- `line` ➖  
  Line symbology focus (roads by class, boundary types)

- `symbol` 📍  
  Point/marker legend (sites, events, facilities)

> [!IMPORTANT]
> If your map layer is **time-enabled** (timeline slider / time scrubbing), keep the legend’s meaning stable and put time context in `subtitle` (or a UI-rendered label next to the legend).

---

## 🗺️ How the UI typically uses this

```mermaid
flowchart LR
  A[Layer Registry / Map Style] -->|layer_id| B[Legend Loader]
  B --> C[legend.json]
  B --> D[legend.svg/png]
  C --> E[Legend Renderer]
  D --> E
  E --> F[Legend Panel (UI)]
  C --> G[dataset_ref.dataset_id]
  G --> H[Catalog / Data Contract]
  H --> F
```

---

## ♿ Accessibility Rules

### Visual accessibility
- ✅ Provide **high contrast** options (either separate `legend.dark.svg` or styles that work on both light/dark).
- ✅ Use **intuitive colors** when conventional (water=blue, vegetation=green), *unless the dataset demands otherwise*.
- ✅ Avoid using **color alone** to encode meaning when you can add:
  - patterns / hatching
  - line dashes
  - icon shapes
  - labeled ranges

### Screen-reader accessibility
- `legend.json` is the canonical source for:
  - legend item labels
  - ordering
  - optional notes / units
- Every icon should be paired with a label (never “icon-only meaning”).

> [!TIP]
> Assume the legend is read aloud: labels should be short, concrete, and unambiguous.

---

## 🧠 Provenance & Attribution

KFM is **contract-first** and **provenance-first**:
- Anything user-facing should be traceable back to an identified dataset.
- Legends should never “invent meaning” that the dataset can’t support.

Practical rules for this folder:
1. **Every legend must declare `dataset_ref.dataset_id`.**
2. **Do not embed long citations in `legend.json`.**  
   Instead, the UI should fetch attribution/license from the dataset catalog (STAC/DCAT/PROV boundary artifacts).
3. If a layer is **experimental**, either:
   - place it behind an “Experimental” toggle in the UI, **or**
   - store it outside user-facing catalogs until it’s governed/validated

> [!WARNING]
> “Mystery layers” (unsourced, ad-hoc, or unverifiable datasets) should not ship with polished legends. Legends imply trust.

---

## ➕ Add a New Layer Legend

### 1) Pick an ID
- Use lowercase with underscores (recommended): `snake_case`
- Prefer matching the dataset/catalog ID: `my_dataset_2024`

### 2) Create the folder
```text
web/assets/media/maps/legends/layers/<layer_id>/
```

### 3) Add `legend.json`
- Start from the minimal examples above
- Ensure `layer_id` matches folder name

### 4) Add `legend.svg`
Design tips:
- Keep width reasonable (e.g., 320–480px) so it fits in a sidebar
- Use readable font sizes (don’t assume zoom)
- Avoid tiny swatches; aim for “glanceable”

### 5) Verify in the UI
- Toggle the layer on/off
- Confirm legend matches **exact layer symbology** (colors, dashes, categories)
- Check dark mode / high contrast (if applicable)

---

## ✅ QA Checklist

### Contract sanity ✅
- [ ] Folder name == `legend.json.layer_id`
- [ ] `legend.json.legend_version` is present
- [ ] `dataset_ref.dataset_id` is present
- [ ] Legend content matches the layer’s actual styling

### Visual QA 👀
- [ ] Legible on mobile widths
- [ ] Works on light and dark backgrounds (or has variants)
- [ ] No “color-only” meaning where confusion is likely

### Accessibility ♿
- [ ] Every symbol has a text label
- [ ] Ordering makes sense (e.g., low → high; most important → least important)

### Provenance 🔍
- [ ] Legend does not contradict dataset metadata
- [ ] If a method note is needed, `notes` is short and factual

---

## 🧰 Troubleshooting

<details>
  <summary><strong>My legend doesn’t show in the UI</strong></summary>

- Confirm the layer registry references the correct `layer_id`
- Confirm `legend.json` exists at:
  `web/assets/media/maps/legends/layers/<layer_id>/legend.json`
- If your build pipeline fingerprints assets, make sure the new files are included

</details>

<details>
  <summary><strong>The colors don’t match the map</strong></summary>

- Update either the map style or the legend, but never leave them drifting
- If the layer is driven by a style expression (ramp), prefer `kind: "ramp"` and declare explicit stops

</details>

---

## 📚 Related (project-wide) docs

These are commonly relevant when adding new layers/legends:
- `/docs/MASTER_GUIDE_v13.md` (pipeline + governance)
- `/docs/standards/` (STAC/DCAT/PROV profiles, markdown work protocol)
- `/data/catalog/` (dataset metadata as source of truth for attribution/license)

> [!NOTE]
> This README is intentionally **implementation-agnostic**: it documents the asset/contract conventions so the UI can evolve without breaking legend meaning.
