# 🗺️ Map Legend Assets (KFM)

![MapLibre](https://img.shields.io/badge/MapLibre-GL%20JS-informational)
![React](https://img.shields.io/badge/Frontend-React%20%2B%20TS-blue)
![Assets](https://img.shields.io/badge/Assets-SVG%20%7C%20PNG%20%7C%20JSON-lightgrey)
![A11y](https://img.shields.io/badge/A11y-Labelled%20%26%20Contrast--aware-success)
![Governance](https://img.shields.io/badge/Governance-Provenance%20%26%20Licensing-critical)

> [!NOTE]
> This folder is the **canonical home** for map legend assets used by the **KFM web UI** 🧭.  
> Keep legends consistent with **layer symbology** so users can trust what they see.

---

## 🎯 Purpose

The Kansas Frontier Matrix (KFM) map experience is built around **interactive layers** (vector/raster tiles and GeoJSON overlays) and a **layer control / legend** that helps users interpret symbols, colors, and ramps. This directory stores the **static legend assets** (icons + swatches + ramps) that the UI can render reliably across environments.

✅ Goals:
- **Consistency**: legend matches the map style (no “blue river” legend for a green river layer)
- **Clarity**: fast “at-a-glance” interpretation
- **Maintainability**: predictable naming + folder layout
- **Governance-ready**: licensing + provenance tracked for imported/derived assets

---

## 🧩 What belongs in this folder

Typical legend building blocks:

- 🧷 **Icons** (point features): towns, forts, events, markers
- ➖ **Line samples** (line features): trails, railroads, rivers, boundaries
- 🟫 **Fill samples** (polygon features): counties, reservations, land cover
- 🌈 **Ramps** (continuous values): heatmaps, elevation, drought severity
- 🧾 **Manifests** (optional): JSON/TS configs that map `layerId → legend items`

> [!TIP]
> Prefer generating simple swatches (solid colors, line dashes) in code **when possible**.  
> Use this folder for **icons**, **pattern fills**, and **curated ramps** that benefit from explicit assets.

---

## 📁 Suggested folder layout

You can organize legends by **domain** (recommended) and/or **geometry**:

```text
web/src/assets/map/legend/
├── README.md
├── 📁 _shared/                # shared primitives (optional)
│   ├── 🧩 patterns/            # SVG patterns (hatch, dots, etc.)
│   └── 🎨 ramps/               # reusable gradient ramps
├── 📁 hydrology/
│   ├── 🧷 icons/
│   ├── 🎨 ramps/
│   └── 🧾 legend.json          # optional manifest for this domain
├── 📁 transportation/
├── 📁 boundaries/
└── 📁 historical/
```

> [!IMPORTANT]
> If you add manifests (like `legend.json`), keep them **small, human-readable**, and versioned.

---

## 🏷️ Naming conventions

### Files ✅
- Use `kebab-case` (no spaces):  
  `historic-trails.svg`, `railroad--dash.svg`, `county-fill--hatch.svg`
- Keep names **semantic** (what it represents) not visual (how it looks):
  - ✅ `fort.svg`
  - ❌ `brown-icon-2.svg`

### Variants 🎭
If you need theme variants:
- `icon.svg` (default)
- `icon--dark.svg` (dark UI backgrounds)
- `icon--hc.svg` (high contrast)

If you need resolution variants (PNG):
- `icon.png` (1x)
- `icon@2x.png` (retina)

---

## 🖼️ Format rules

### SVG (preferred) ✅
- Use a consistent `viewBox` (recommend `0 0 24 24` or `0 0 32 32`)
- Avoid baked-in backgrounds unless required
- Use simple paths (optimize / minify if possible)
- Prefer `stroke="currentColor"` / `fill="currentColor"` when the UI needs to recolor icons

### PNG (fallback) 🧯
- Only when SVG is not viable (complex raster textures, legacy assets)
- Include `@2x` if used in UI controls

---

## 🧠 Legend design rules (mapcraft)

Your legend is part of the map’s “reading interface” 🧭:

- **Match the map**: show the same symbol *shape, weight, and dash style*
- **Group logically**: by theme (hydrology, transport, boundaries) or by “story”
- **Order intentionally**: most important / common items first
- **Avoid clutter**: if a layer has 25 classes, show a ramp + key breakpoints instead of every class

### Classified vs unclassified symbols 📏
For graduated symbols (sizes vary by value), decide:
- **Classified**: fewer sizes, easier matching
- **Unclassified**: more detail, harder matching

Use whichever serves the story and task best.

---

## ♿ Accessibility checklist

Legend UI must work for everyone:

- Don’t rely on **color alone** (use patterns, shapes, labels)
- Ensure readable label text (short, clear, no jargon)
- Keep adequate contrast for both light/dark UI
- Provide alt/aria labels when legend includes only icons

> [!TIP]
> If two layers share similar colors, differentiate by **dash style**, **pattern fills**, or **icon shape**.

---

## 🔒 Provenance & licensing (non-negotiable)

If an asset is:
- imported from an external icon set,
- derived from a map source,
- generated from proprietary design tools,

…then its **license and provenance must be recorded**.

Recommended approach:
- Add an `ATTRIBUTION.md` in the domain folder, or
- Add a `meta.json` per asset (source, author, license, modifications)

Example `meta.json` (optional):
```json
{
  "name": "historic-trails.svg",
  "source": "internal",
  "license": "Project-owned",
  "notes": "Matches MapLibre style layer `historic_trails`"
}
```

---

## ➕ Adding a new legend item

1) Identify the **map layer id** (or domain) the legend item supports  
2) Decide the legend type:
   - 🧷 icon (point)
   - ➖ stroke sample (line)
   - 🟫 fill/pattern (polygon)
   - 🌈 ramp (continuous)
3) Create/export the asset into the correct folder  
4) If using a manifest, register it (label, layerId, icon path)  
5) Verify visually in the UI:
   - legend matches map
   - legible at small sizes
   - works in dark mode (if applicable)

---

## ✅ QA / PR checklist

Before merging:
- [ ] File names are `kebab-case`
- [ ] SVGs have clean viewBox + no hidden huge canvas
- [ ] Legend looks correct at 100% and 125% browser zoom
- [ ] Contrast is acceptable on light and dark backgrounds
- [ ] License/provenance recorded for non-original assets
- [ ] Legend labels are short, consistent, and human-readable

---

## 🔗 Related docs (repo)

- 📘 `docs/MASTER_GUIDE_v13.md` (canonical structure / governance)
- 🏗️ `docs/architecture/system_overview.md` (system + UI architecture)
- 🧾 `docs/standards/` (house standards: contracts, provenance, etc.)

> [!NOTE]
> If these links move, update them here — the legend folder README is meant to be a stable entry point for map UI contributors. 🚀
