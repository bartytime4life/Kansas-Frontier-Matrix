# 🗺️ Map Icons (KFM Web UI)

![Static Assets](https://img.shields.io/badge/web-assets-✅-informational?style=for-the-badge)
![Icons](https://img.shields.io/badge/icons-map-🗺️-informational?style=for-the-badge)
![Format](https://img.shields.io/badge/prefer-SVG-0aa?style=for-the-badge)
![A11y](https://img.shields.io/badge/accessibility-expected-2ea44f?style=for-the-badge)

This folder contains **map-facing icon assets** used by the **KFM front-end** (map viewer + UI controls). Icons in here power things like:

- 🧭 Map UI controls (layers, legend, timeline, search, etc.)
- 📍 Markers / POI glyphs for rendered features
- 🧾 Story Nodes UI affordances (when a narrative step needs an icon callout)

> ✨ KFM’s UI is designed to be **responsive + accessible**, and it includes standard UI elements like a **layer catalog**, **search**, **legend**, and **timeline slider** — these icons should support those elements cleanly and consistently.  
> (See project technical documentation for the front-end folder intent and UI element overview.)  

---

## 📌 Quick rules (TL;DR)

- ✅ **Prefer SVG** for icons (sharp at any zoom + generally smaller than raster for icon-scale graphics).
- ✅ Keep icons **simple, legible, and consistent** (same stroke weight, corner radius style, and visual density).
- ✅ Use **semantic naming** (what it *means*, not what it *looks*).
- ✅ **No “mystery icons”**: if an icon is sourced externally, record **license + provenance**.
- ✅ Optimize assets before committing (SVGO / equivalent).
- ❌ Don’t commit screenshots or unlicensed icon dumps.
- ❌ Don’t embed hard-coded colors unless the icon is truly multi-color by design.

---

## 🧱 Where this sits in the repo

```text
🗂️ web/
  🧩 components/            # UI components (LayerList, Legend, Search, etc.)
  🗺️ viewers/               # Map viewer logic (MapLibre GL JS / Leaflet, etc.)
  🧰 assets/
    🖼️ media/
      🧿 icons/
        🗺️ map/             # ← you are here
          README.md
          (icons live here)
```

> `web/assets/` is the canonical home for **static assets like icons/images** used by the front-end.

---

## 🗃️ Recommended organization

If this directory grows, prefer **subfolders** over dumping everything flat:

```text
🗺️ map/
  🧭 ui/          # buttons, toggles, panels (layer, legend, time, search…)
  📍 markers/     # pins, selected/hover states, clusters
  🧩 poi/         # point-of-interest glyphs (school, fort, water, etc.)
  🧱 layers/      # dataset-type glyphs (raster, vector, timeline, heatmap…)
  🧪 status/      # loading, warning, error, info
  🧾 meta/        # helper symbols (external link, citation, provenance badge…)
  README.md
  ICON_SOURCES.yml (optional, but recommended ✅)
```

---

## 🏷️ Naming conventions

### ✅ File naming

Use **kebab-case** and keep it **semantic**.

| Category | Prefix | Example |
|---|---|---|
| UI controls | `ui-` | `ui-layers.svg`, `ui-legend.svg`, `ui-timeline.svg` |
| Markers | `marker-` | `marker-pin.svg`, `marker-selected.svg` |
| POI glyphs | `poi-` | `poi-school.svg`, `poi-fort.svg` |
| Layer types | `layer-` | `layer-raster.svg`, `layer-vector.svg` |
| Status | `status-` | `status-warning.svg`, `status-error.svg` |

### ✅ Variants

If an icon needs variants, suffix them:

- `marker-pin.svg`
- `marker-pin--selected.svg`
- `marker-pin--hover.svg`

> Keep variants minimal. Prefer styling (CSS `currentColor`, SDF/tinting, etc.) over duplicating files.

---

## 🎨 Design system rules for icons

### Grid + geometry
- 📐 Standardize on a **single viewBox** (recommend: `0 0 24 24` or `0 0 32 32`, pick one and stick to it).
- ✍️ Keep **stroke width** consistent across the icon set.
- 🧩 Snap to pixel grid when possible (especially at small sizes).

### Color + theming
- 🌗 Prefer `currentColor` so icons adapt to light/dark themes.
- 🧼 Avoid embedding hard-coded fills unless the icon is intentionally multi-color.
- ♿ Ensure contrast works at typical UI sizes.

### Accessibility
- 🏷️ Icons used as interactive controls must have:
  - Visible label **or**
  - `aria-label` / `title` when embedded as SVG
- 🧏 Don’t rely solely on color to communicate meaning (use shape + tooltip + label).

---

## 🧩 Usage patterns

### 1) Simple `<img>` usage
```html
<img
  src="/assets/media/icons/map/ui/ui-layers.svg"
  alt="Layers"
/>
```

### 2) Inline SVG (best for theming with `currentColor`)
```html
<button aria-label="Toggle layers">
  <!-- inline svg (or imported as a React component) -->
  <svg role="img" aria-hidden="true" viewBox="0 0 24 24">
    <title>Layers</title>
    <!-- paths... -->
  </svg>
</button>
```

### 3) CSS mask (great for monochrome icons)
```css
.icon {
  width: 1.25rem;
  height: 1.25rem;
  background: currentColor;
  mask: url("/assets/media/icons/map/ui/ui-legend.svg") no-repeat center / contain;
  -webkit-mask: url("/assets/media/icons/map/ui/ui-legend.svg") no-repeat center / contain;
}
```

### 4) Map rendering libraries (MapLibre GL / Leaflet)
KFM’s design notes mention MapLibre GL (or Leaflet) as the front-end mapping library option. If icons are used as **map style sprites / images**, you may need PNGs or library-specific loading.

<details>
  <summary><strong>🗺️ Example: MapLibre-style image registration (conceptual)</strong></summary>

```js
// Pseudocode: adjust to your actual viewer wrapper + bundler paths.
map.loadImage("/assets/media/icons/map/poi/poi-school.png", (err, img) => {
  if (err) throw err;
  map.addImage("poi-school", img, { sdf: true }); // sdf allows tinting in some pipelines
});
```

</details>

> 📝 When a map library requires raster sprites, keep an SVG source-of-truth and export PNG at required sizes.

---

## 🧾 Provenance & licensing (NO “mystery icons”)

KFM’s broader architecture enforces a **provenance-first** / **evidence-first** mindset: anything surfaced in UI should be traceable and governed (the same spirit applies to icon assets). That means:

- ✅ If an icon is **created in-house**, note author + date (git history is fine).
- ✅ If an icon is **derived from an external set**, record:
  - Source name + link
  - License type (and any attribution requirements)
  - What changed (if modified)

### Recommended: `ICON_SOURCES.yml`
Add a lightweight provenance register next to the assets:

```yaml
# ICON_SOURCES.yml (suggested)
icons:
  - id: ui-layers
    file: ui/ui-layers.svg
    source: "Original (KFM)"
    license: "Project-owned"
    notes: "Matches layer catalog toggle in the map UI"

  - id: poi-school
    file: poi/poi-school.svg
    source: "Derived from external icon set"
    upstream: "NAME + URL"
    license: "CC-BY-4.0 (example)"
    attribution: "Required in About/Credits"
    notes: "Simplified for 24px grid + unified stroke weight"
```

> 💡 If you later build an “icon picker” UI, this file can double as the manifest for browsing/searching icons.

---

## ➕ Add a new icon (workflow)

1) 🧠 **Pick a semantic name** (start with `ui-`, `poi-`, etc.)  
2) 🎨 **Design on the correct grid** (match existing viewBox + stroke rules)  
3) 🧼 **Optimize** (SVGO or equivalent)  
4) ♿ **Check accessibility** (legibility at 16–24px; ensure alt/labels exist where used)  
5) 🧾 **Record provenance** (update `ICON_SOURCES.yml` if applicable)  
6) 🧪 **Smoke test in the UI**:
   - Light + dark mode
   - Hover/active states
   - Zoom scaling (for marker icons)
   - Mobile sizing (touch targets)

---

## ✅ Definition of Done checklist

- [ ] Icon is placed in the correct subfolder (`ui/`, `poi/`, `markers/`, etc.)
- [ ] File name is semantic + kebab-case
- [ ] SVG has a clean `viewBox` and no junk metadata
- [ ] Uses `currentColor` when appropriate
- [ ] Optimized (no unnecessary paths/groups)
- [ ] Provenance recorded (if external/derived)
- [ ] Visible + legible at 16–24px
- [ ] Works in light/dark backgrounds
- [ ] Used controls have accessible labeling (alt/aria)

---

## 🧯 Troubleshooting

- **Icon looks blurry** → confirm it’s SVG (or PNG exported at correct scale).
- **Icon doesn’t theme** → ensure fill/stroke uses `currentColor` (or CSS variables), not hard-coded hex.
- **Icon is clipped** → fix the SVG `viewBox` and remove stray transforms.
- **Map marker won’t tint** → check whether your map pipeline supports SDF/tinting; otherwise export separate colored assets.

---

## 🔗 Related docs (project context)

- 📘 KFM front-end structure + UI elements: `web/`, `assets/`, map viewers, and standard UI controls (layer list, search, legend, timeline).
- 🧭 Repo governance / provenance guardrails: “provenance first” + “evidence-first narrative” expectations.

<!-- Project references used to shape this README (hidden so the repo stays clean):
      [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  (KFM technical documentation: web/ structure + assets/ + UI elements)
      [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  (KFM markdown guide: provenance-first + evidence-first expectations)
      [oai_citation:2‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-Heg28TVM2nReDYTQ7nPhAK)  (Responsive web design: SVG for resolution independence + optimization)
      [oai_citation:3‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  (KFM hub design: MapLibre/Leaflet UI + timeline map UI concept)
      [oai_citation:4‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)  (Mapping icon libraries list for optional upstream sets)
-->
