<!--
KFM 📦 Canonical Asset README
Path: web/assets/maps/legends/ramps/README.md
Purpose: Define + govern shared color ramps used by map legends & styling
-->

# 🎨 Map Legend Ramps (Color Ramps / Palettes)

![KFM](https://img.shields.io/badge/KFM-maps%20%26%20legends-2ea44f?style=flat-square)
![status](https://img.shields.io/badge/status-canonical%20asset-blue?style=flat-square)
![a11y](https://img.shields.io/badge/a11y-color%E2%80%91blind%20aware-6f42c1?style=flat-square)
![provenance](https://img.shields.io/badge/provenance-required-orange?style=flat-square)

> **One place** for **shared color ramps** used by KFM legends and map styling.  
> Ramps are **not just aesthetics** — they shape interpretation. This folder keeps them consistent, accessible, and provenance-aware 🧭

---

## 🧱 What belongs here

✅ **This folder is for:**
- **Reusable color ramps** (sequential / diverging / categorical / cyclic)
- **Ramp metadata** (source, license, rationale, accessibility notes)
- Optional **preview artifacts** (SVG/PNG) or a **manifest/index**

🚫 **This folder is NOT for:**
- Dataset-specific **class breaks**, **min/max domains**, or **units**
- “Legend text” that is unique per dataset/layer
- Layer ordering / style logic (that belongs in the layer/style config)

> [!NOTE]
> KFM’s UI updates legends and color scales based on what’s currently shown.  
> That’s why ramps here should be **data-agnostic** (colors + meaning), while domain/breaks live with the layer.

---

## 🗂️ Recommended layout

Even if the current repo shape differs, this is the “north star” structure 🌟:

```text
📁 web/assets/maps/legends/ramps/
├─ 📄 README.md
├─ 📄 manifest.json              # optional: index of ramps (IDs, paths, tags)
├─ 📁 sequential/                # low → high (monotone data)
│  ├─ viridis-9.json
│  ├─ batlow-9.json
│  └─ blues-7.json
├─ 📁 diverging/                 # low → mid → high (anomaly / +/-)
│  ├─ balance-11.json
│  └─ rdBu-11.json
├─ 📁 categorical/               # discrete classes (no interpolation)
│  ├─ set3-12.json
│  └─ tableau-10.json
├─ 📁 cyclic/                    # wraps around (aspect, phase, seasons)
│  └─ phase-12.json
└─ 📁 _previews/                 # optional: legend swatches / gradient bars
   ├─ viridis-9.svg
   └─ balance-11.svg
```

---

## 🧾 Ramp contract (JSON)

Ramps should be **small, predictable, and machine-usable** 🤖✅

### ✅ Minimal shape (recommended)

```json
{
  "id": "sequential/viridis-9",
  "kind": "sequential",
  "colors": ["#440154", "#482878", "#3E4989", "#31688E", "#26828E", "#1F9E89", "#35B779", "#6DCD59", "#FDE725"],
  "meta": {
    "title": "Viridis (9-step)",
    "notes": ["Perceptually uniform", "Good default for continuous magnitude"]
  },
  "provenance": {
    "source": "Matplotlib colormap family (Viridis)",
    "license": "See upstream license",
    "attribution": "If required by upstream"
  },
  "a11y": {
    "colorBlindNotes": "Generally safe for common color-vision deficiencies",
    "avoidOnDarkBasemap": false
  }
}
```

### 🔧 Optional fields (use when helpful)

```json
{
  "stops": [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0],
  "tags": ["elevation", "density", "continuous"],
  "recommendedFor": ["choropleth", "heatmap", "raster"],
  "avoidFor": ["categorical"],
  "noData": { "color": "rgba(0,0,0,0)", "label": "No data" },
  "reverseId": "sequential/viridis-9-rev"
}
```

> [!TIP]
> Prefer **hex** (`#RRGGBB`) or **8-digit hex** (`#RRGGBBAA`) for portability.  
> If you must use `rgba(...)`, do it consistently and document why.

---

## 🧠 Choosing the right ramp

A ramp must match the **data meaning** — not personal preference 🎯

| Kind | Use when… | Examples | Common traps ⚠️ |
|---|---|---|---|
| **Sequential** | values go **low → high** (no natural center) | elevation, rainfall, density | reversing meaning (“dark = less”) without explicit reason |
| **Diverging** | values deviate around a **neutral midpoint** | anomaly vs baseline, +/- change | midpoint not actually meaningful (e.g., not 0 / median) |
| **Categorical** | discrete **named classes** | land use, political boundaries, tribes/nations | interpolating categories (never blend class colors) |
| **Cyclic** | data wraps (end connects to start) | aspect (0–360°), seasons, phases | using sequential ramps that “break” at wrap point |

---

## 🚫 Avoid misleading ramps (seriously 😅)

Some color ramps **invent boundaries** where none exist. In remote sensing and cartography, the classic offender is the “rainbow” ramp 🌈⚠️

**Guideline:** default to **perceptually uniform** ramps for continuous data, and use diverging ramps only when you have a real semantic center.

> [!WARNING]
> If a ramp makes subtle changes look like sharp edges, it can mislead readers into “seeing patterns” that are just color artifacts.

---

## 🗺️ Legend conventions we follow

These are practical cartography rules that keep KFM maps readable and trustworthy 🧭

- **High values at the top** of the legend (when vertical) ⬆️  
- In most contexts, users interpret **darker = more** (unless clearly labeled otherwise) 🎚️  
- If you classify into bins, show **discrete swatches** (don’t imply continuity) 🧱  
- Avoid **pure black** as the highest class if it conflicts with boundary/label colors 🖤  
- Keep **No Data** visually distinct from “low value” (often transparent or neutral gray) 🕳️

> [!NOTE]
> Legends should always include **units** and **what the colors represent** — but that belongs with the layer/dataset config, not the ramp itself.

---

## ♿ Accessibility checklist (a11y)

KFM is designed to be usable across devices and audiences — ramps must support that 🌍

### ✅ For every ramp, confirm:

- [ ] **Color-blind awareness**: avoid red/green-only distinctions where possible  
- [ ] **Contrast**: legend labels remain readable on both light & dark UI themes  
- [ ] **Ordering**: low→high progression is visually intuitive  
- [ ] **No Data** is not confused with “0”  
- [ ] **Small-screen legibility**: ramp still works when compressed (mobile legend) 📱  
- [ ] **Print/screenshot friendliness**: doesn’t fall apart when desaturated 🖨️

---

## 🧩 Using ramps in the UI

### 🎛️ 1) CSS gradient for legend bars

```css
/* Example: create a legend gradient bar */
.legendRamp {
  background: linear-gradient(
    to right,
    #440154,
    #482878,
    #3E4989,
    #31688E,
    #26828E,
    #1F9E89,
    #35B779,
    #6DCD59,
    #FDE725
  );
}
```

### 🗺️ 2) MapLibre style expression (vector styling)

```ts
// Pseudocode: convert ramp colors into an interpolate expression
// NOTE: domain & breaks come from the layer config or computed stats.

const colors = ramp.colors;          // ["#...", "#..."]
const min = layerDomain.min;         // e.g. 0
const max = layerDomain.max;         // e.g. 1000

const stops = colors.map((c, i) => {
  const t = i / (colors.length - 1);
  const value = min + t * (max - min);
  return [value, c] as const;
});

const fillColorExpr = [
  "interpolate",
  ["linear"],
  ["coalesce", ["get", "value"], min], // handle missing
  ...stops.flat()
];

// paint: { "fill-color": fillColorExpr }
```

### 🌐 3) Cesium materials (high-level idea)

- Use the ramp to build a **color table / gradient texture** for raster materials  
- Keep alpha (opacity) controlled by layer settings, not baked into ramp colors

> [!TIP]
> If you need opacity, prefer applying it in the layer style (`opacity`) so the **same ramp** works across basemap contexts.

---

## ➕ Adding a new ramp (Definition of Done ✅)

**Do this every time** so we don’t end up with “pretty but untraceable” ramps.

### 1) Create the ramp file
- [ ] Choose `kind` correctly (sequential/diverging/categorical/cyclic)
- [ ] Use **kebab-case** naming (`batlow-9.json`)
- [ ] Provide `id` that matches the path (`sequential/batlow-9`)
- [ ] Add `meta.title` and at least one rationale note
- [ ] Add `provenance.source` + `provenance.license` (or “unknown” + TODO)

### 2) Make it discoverable
- [ ] Add it to `manifest.json` (if used)
- [ ] (Optional) Add a preview swatch/gradient in `_previews/`

### 3) Don’t break existing maps
- [ ] **Never change** an existing ramp’s color order in-place  
  - Instead: add a new ramp ID (e.g., `viridis-9-v2`) and migrate consumers intentionally.

> [!WARNING]
> Changing an existing ramp silently changes map meaning. That’s a provenance problem, not a styling preference.

---

## 🔐 Provenance & licensing

KFM is built on transparency and reproducibility. That includes visuals.

**Minimum provenance fields**:
- **Source** (where the ramp comes from)
- **License** (compatibility matters in open-source)
- **Attribution** (if required)

If the ramp was adapted (tweaked endpoints, clipped range, etc.), document:
- what changed
- why
- who/when (git blame is fine, but notes help reviewers)

---

## 📚 Project references (why these rules exist)

These practices align with KFM’s broader goals:
- **Legends + units + correct interpretation** are part of the UI/UX expectations for KFM maps.
- **Colorblind-friendly palettes** and consistent symbology are explicitly called out as map-design needs.
- **Different ramps can produce different interpretations**, so ramp selection is a correctness issue.
- Cartographic legend conventions (“darker = more”, discrete vs continuous legends) reduce misreadings.

---

## 🧾 Quick FAQ

<details>
  <summary><strong>Why not store min/max in the ramp file?</strong></summary>

Because min/max are properties of **a dataset and a time slice**, not the ramp itself.  
KFM layers can change over time, and the UI may compute stats dynamically. Keep the ramp reusable; keep domain logic with the layer.

</details>

<details>
  <summary><strong>Can I reverse a ramp?</strong></summary>

Yes — but prefer adding a separate ramp asset (e.g., `*-rev`) so it’s explicit and trackable.  
Reversals can change meaning (especially where “dark = more” is expected).

</details>

<details>
  <summary><strong>How many colors should a ramp have?</strong></summary>

- UI legends: **5–11** is usually readable
- Continuous rasters: you may derive a higher-resolution ramp at runtime/build-time  
  (don’t commit 256-step ramps unless you truly need them)

</details>