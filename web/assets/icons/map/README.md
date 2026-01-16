<!-- Path: web/assets/icons/map/README.md -->

# 🗺️ Map Icons (KFM)

![Format](https://img.shields.io/badge/format-SVG%20%2B%20sprite-blue)
![Rendering](https://img.shields.io/badge/render-MapLibre%20%7C%20WebGL-success)
![A11y](https://img.shields.io/badge/a11y-alt%20text%20%2B%20contrast-important)
![Governance](https://img.shields.io/badge/KFM-provenance--first-purple)
![Style](https://img.shields.io/badge/symbology-consistent%20%26%20legible-orange)

Map symbology is not “decoration” — it’s part of the *data contract* between the map and the reader. This folder contains **map-facing icons** (markers + legend glyphs + layer symbols) used by the KFM web UI.

> [!NOTE]
> These icons should help **novices understand quickly** while still being **precise enough for experts**—the UI must remain readable on desktop and mobile, and under real-world viewing conditions (movement, glare, zooming, etc.).

---

## 📌 What belongs here

✅ **Yes (map icons):**
- POI markers (town, fort, school, clinic, depot, courthouse, etc.)
- Layer glyphs used in the **Layer List / Legend**
- “Data type” icons (raster, vector, points/lines/polygons, time-series, simulation, ML prediction)
- Sensitivity / governance markers *as they appear on the map* (e.g., generalized location, restricted view)

❌ **No (UI chrome icons):**
- Buttons, menus, nav icons, generic UI controls  
  → those belong in the general UI icon set (outside `icons/map/`)

---

## 🧭 How map icons are used in KFM

KFM’s UX patterns commonly include:
- **Layer List** (toggleable layers with legend symbols)
- **Legend** (map symbology reference)
- **Search results & feature popups** (quick scanning)
- **Timeline slider / Story Focus Mode** (event markers over time)

Map icons must support these flows by being:
- **semantically consistent** (same meaning everywhere)
- **visually consistent** (same style + stroke weight + grid)
- **performance-safe** (fast on low-end devices)
- **governance-safe** (never leaking sensitive info through symbology)

---

## 🗂️ Recommended folder layout

> If this folder is currently “flat” (just a pile of SVGs), this is the target structure as we formalize the pipeline.

```text
web/assets/icons/map/
├─ 📄 README.md
├─ 🎨 svg/                # editable source icons (preferred)
│  ├─ 🎨🧷 poi-school.svg
│  ├─ 🎨🧷 poi-hospital.svg
│  ├─ 🎨🧷 hazard-flood.svg
│  └─ ➕ …
├─ 🤖 sprite/             # build outputs (generated; do not hand-edit)
│  ├─ 🖼️🧷 kfm-map-sprite@1x.png
│  ├─ 🖼️✨🧷 kfm-map-sprite@2x.png
│  └─ 🧾🧷 kfm-map-sprite.json
└─ 🧾 meta/               # icon provenance + license + tags
   ├─ 🧾 poi-school.meta.json
   ├─ 🧾 poi-hospital.meta.json
   └─ ➕ …
```

---

## 🏷️ Naming conventions

### File names
Use **kebab-case** and a **semantic prefix**:

- `poi-*` → points of interest  
- `infra-*` → infrastructure (rail, road, telegraph, pipelines, dams)  
- `hazard-*` → hazards (tornado, flood, wildfire)  
- `boundary-*` → borders, treaties, reservations, counties  
- `env-*` → environment (soil, water, air quality)  
- `event-*` → historical event markers  
- `dataset-*` → dataset type icons (raster/vector/graph/time-series)  
- `model-*` → modeling / simulation outputs  
- `ml-*` → ML prediction layers (classification/regression/uncertainty)

Examples:
- `poi-courthouse.svg`
- `infra-rail.svg`
- `event-battle.svg`
- `dataset-raster.svg`
- `ml-uncertainty.svg`

### Icon IDs (for map style + config)
The **icon ID** should match the filename **without extension**:
- `poi-hospital.svg` → `poi-hospital`

Keep icon IDs **stable**. Renaming an icon is a breaking change for:
- map styles (`icon-image`)
- legends (layer registry)
- story nodes / UI references

---

## 🎨 Visual style guide

### Grid + sizing
- Design on a **24×24** grid by default (common for web + map sprites).
- Use an SVG `viewBox="0 0 24 24"` (or `32 32` if you have a strong reason).
- Avoid ultra-thin details; icons must remain legible at **12–18px** in legends.

### Stroke + fill
- Prefer **simple silhouettes** or **simple strokes** (no micro-text).
- Use consistent stroke weight across the set.
- Avoid gradients unless the pipeline explicitly supports them (gradients often break sprite/SDF workflows).

### Figure-ground clarity
Map icons must survive:
- dark basemaps vs light basemaps
- hover/selection states
- partially transparent overlays  
Design for strong figure-ground separation and meaningful shapes.

> [!TIP]
> If two icons can be confused at 16px, they are the *same icon* in practice. Simplify.

---

## 🧠 Cartographic principles (symbology that “reads” right)

Map symbols work because users learn “codes”:
- resemblance (looks like the thing)
- convention (users already recognize it)
- difference (distinctiveness)
- standardization (consistency across the map)

When choosing/adding icons, ensure:
- the symbol-to-concept relationship is meaningful  
- symbol choices reflect the data and the map’s goal  
- the design matches viewing conditions (mobile, zoom, motion)  
- color is used as information, not decoration

---

## ♿ Accessibility & ethics

### Accessibility requirements
- Provide meaningful **alt text** wherever icons are rendered in the UI (legend, layer list, cards).
- Do not rely on **color alone** to convey meaning (use shape + label).
- Ensure adequate contrast against typical map backgrounds.

### Ethics / governance alignment
KFM is evidence-first and provenance-first. That spirit applies to UI symbols too:
- Avoid stereotypes or culturally loaded imagery unless reviewed.
- For sensitive or sovereign data, prefer icons that communicate **restriction** or **generalization** without revealing details.
- If an icon implies certainty (✅), only use it for layers that truly are “confirmed”; use uncertainty icons for modeled/predicted layers.

---

## ⚡ Performance rules (don’t make the map slow)

### SVG hygiene (required)
- Minimize paths
- Remove editor metadata
- Remove unnecessary groups and transforms
- Avoid huge coordinate ranges; keep the viewBox tight and clean

### Sprite-first mindset
For map rendering at scale, icons are typically most efficient when:
- compiled into a **sprite sheet**
- referenced by ID (`icon-image`)
- cached by the browser

If you see repeated `<svg>` DOM nodes in dense layers, you’re probably leaving performance on the table.

---

## 🧾 Metadata & provenance for each icon

Every non-trivial icon should have a sidecar metadata file:

`meta/<icon-id>.meta.json`

### Suggested schema (minimal)
```json
{
  "id": "poi-hospital",
  "title": "Hospital / Clinic",
  "category": "poi",
  "tags": ["health", "medical", "services"],
  "license": "CC0-1.0",
  "attribution": "",
  "source": {
    "name": "Internal",
    "url": ""
  },
  "created": "2026-01-14",
  "modified": "2026-01-14",
  "notes": "Used for public health facility points on the map."
}
```

> [!IMPORTANT]
> If the icon is derived from an external library, **license + attribution must be explicit** in the metadata.

---

## 🧩 Integration patterns

### 1) MapLibre / style sprites (most common)
You reference an icon by ID in your style:

```json
{
  "id": "poi-hospitals",
  "type": "symbol",
  "source": "kfm",
  "layout": {
    "icon-image": "poi-hospital",
    "icon-size": 1,
    "icon-allow-overlap": true
  }
}
```

### 2) Legend / Layer List
Your layer registry (or UI config) should map a layer to an icon:

```json
{
  "layerId": "poi-hospitals",
  "title": "Hospitals & Clinics",
  "legend": [
    { "label": "Hospital / Clinic", "icon": "poi-hospital" }
  ]
}
```

### 3) WebGL / Cesium billboards (if enabled)
- Prefer a sprite-based or atlas-based approach (GPU-friendly).
- Avoid huge PNGs; keep icons small and cacheable.
- If icons are color-themable, consider an SDF workflow (if supported).

---

## ✅ Adding a new map icon (Definition of Done)

- [ ] Icon exists as SVG in `svg/` (24×24 viewBox preferred)
- [ ] Icon name follows prefix conventions (`poi-*`, `hazard-*`, etc.)
- [ ] Icon has `meta/<id>.meta.json` with license + attribution (if needed)
- [ ] Icon is included in sprite build outputs (if sprites are used)
- [ ] Icon is referenced via config (layer registry / legend mapping) — **not hard-coded**
- [ ] Icon is legible at 16px and 12px
- [ ] Icon does not create governance risk (no sensitive inference)

---

## 🧪 QA checklist (quick)

**Looks right**
- [ ] Crisp at 1× and 2×
- [ ] No clipping
- [ ] Reads correctly on light + dark basemap

**Behaves right**
- [ ] Marker anchors correctly (tip is where the point is)
- [ ] Hover/selected states don’t distort meaning

**Stays governable**
- [ ] Metadata exists + license is clean
- [ ] Semantic naming is stable

---

## 📚 Related project references (design + engineering)

These project resources informed the standards in this folder:

### 🗺️ Cartography / GIS
- *Making Maps: A Visual Guide to Map Design for GIS*
- *Mobile Mapping: Space, Cartography and the Digital*
- *Archaeological 3D GIS*

### 🌐 Web UI / Graphics
- *Responsive Web Design with HTML5 and CSS3*
- *WebGL Programming Guide: Interactive 3D Graphics*

### 🧬 Modeling / Evidence / Uncertainty
- *Scientific Modeling and Simulation (NASA-grade guide)*
- *Understanding Statistics & Experimental Design*
- *Think Bayes (Bayesian stats in Python)*

### 🧱 Data systems / Performance / Governance
- *KFM Master Guide / Pipeline & Governance docs*
- *Data Spaces*
- *Database Performance at Scale*
- *Scalable Data Management for Future Hardware*

---

## 🧾 License note

This folder may contain a mix of:
- original KFM icons
- derived icons from external libraries

**Do not assume** everything is CC0. Check each icon’s `meta/*.meta.json` and follow attribution requirements.

---

💡 If something here feels unclear: the goal is simple — **icons are part of the map’s truthfulness**. Keep them consistent, legible, fast, and provenance-aware.
