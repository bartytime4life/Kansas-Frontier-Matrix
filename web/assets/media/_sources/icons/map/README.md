# 🗺️ Map Icons — Source Library (`_sources`)

![Scope](https://img.shields.io/badge/scope-map_UI-1f6feb)
![Format](https://img.shields.io/badge/format-SVG--first-2ea44f)
![Rule](https://img.shields.io/badge/rule-provenance--required-f85149)
![Location](https://img.shields.io/badge/path-web%2Fassets%2Fmedia%2F__sources%2Ficons%2Fmap-6f42c1)

> **According to a document from January 18, 2026**, the KFM web frontend includes static assets (like icons) and a map-driven UI (layer lists/catalogs, legends, timeline controls, etc.).  
> This folder contains the **editable icon sources** used to support those map experiences. ✅

---

## ✨ What this folder is

This directory is the **source-of-truth icon library** for **map-related UI** in KFM:

- 🧭 Map controls (zoom, locate, measure, draw, etc.)
- 🗂️ Layer & dataset affordances (raster/vector/3D/time-enabled, etc.)
- 🧩 Legends + symbology helpers
- 🧪 Status/utility icons specific to map workflows (loading layers, errors, “new”, “verified”, etc.)

**Goal:** keep the icon set **consistent, themeable, accessible, and provenance-traceable**.

---

## 📁 Suggested layout

> If your repo already has a different structure, keep that—this is a recommended convention for clarity.

```text
📁 web/assets/media/_sources/icons/map/
├─ 📄 README.md
├─ 📁 svg/                 # ✅ preferred: editable vectors
├─ 📁 png/                 # ⚠️ rare: only when raster is unavoidable
├─ 📁 meta/                # 🧾 provenance + licensing + notes (1 file per icon)
└─ 📁 _drafts/             # 🧪 WIP icons not yet used by UI
```

---

## 🏷️ Naming conventions

**Rules**
- ✅ `kebab-case` only (`layer-raster.svg`)
- ✅ keep names **semantic**, not visual (`search.svg` not `magnifier.svg`)
- ✅ avoid app-specific coupling unless truly map-only (`map-timeline.svg` is ok here)
- ✅ include variants as suffixes

**Recommended prefixes**
| Prefix | Use for | Examples |
|---|---|---|
| `layer-` | layer/dataset types | `layer-raster.svg`, `layer-vector.svg`, `layer-3d.svg` |
| `geom-` | geometry types | `geom-point.svg`, `geom-line.svg`, `geom-polygon.svg` |
| `control-` | map controls | `control-zoom-in.svg`, `control-locate.svg` |
| `tool-` | tool modes | `tool-measure.svg`, `tool-draw.svg` |
| `status-` | UI state | `status-loading.svg`, `status-warning.svg` |
| `legend-` | legend helpers | `legend-gradient.svg`, `legend-categorized.svg` |
| `poi-` | POI markers | `poi-school.svg`, `poi-hospital.svg` |

**Variant suffixes**
- `-outline`, `-solid`, `-filled`
- `-sm`, `-md`, `-lg` *(only if a single scalable SVG can’t cover it)*

---

## 🧩 SVG standards (the “quality bar”)

### ✅ Required
- **Single artboard** per icon
- Set a consistent base grid (recommended: **24×24**)
- `viewBox` present (icons must scale cleanly)
- Use themeable paint:
  - `fill="currentColor"` and/or `stroke="currentColor"`
- Prefer **simple paths** over complex filters/masks
- No embedded fonts, no external images, no editor metadata

### 🎯 Recommended
- Keep stroke widths consistent across the set (e.g., 1.5–2)
- Align strokes to pixel grid (crisper at small sizes)
- Keep icons readable at **16px** and **20px** (common UI sizes)

### 🚫 Avoid
- Hard-coded hex colors (unless truly multi-color and explicitly documented)
- Random `id="clip0_1234"` collisions when inlined (sanitize or remove IDs)
- Multiple delivery styles within the same UI area (sprite vs inline vs data-uri) unless there’s a good reason

---

## 🧾 Provenance & licensing (non-negotiable)

KFM is **contract-first + provenance-first**: anything visible in the UI should be traceable—**icons included**.

### ✅ For every icon used by the app, add a `meta/<icon-name>.json`

Example: `meta/layer-raster.json`
```json
{
  "id": "layer-raster",
  "title": "Raster layer",
  "category": "layer",
  "tags": ["map", "layer", "raster"],
  "source": {
    "type": "original | derived | third-party",
    "author": "Name or Org",
    "reference": "Figma link / repo path / external URL",
    "notes": "What changed vs source"
  },
  "license": {
    "spdx": "MIT | Apache-2.0 | CC0-1.0 | CC-BY-4.0 | Proprietary",
    "attribution": "Required attribution text if any"
  }
}
```

### 🧠 Why this matters
- Keeps the UI shippable (no “mystery icons”)
- Enables attribution/credits generation
- Prevents license surprises late in the game

---

## 🔁 Workflow: add or update an icon

### 1) Add/edit the source
- Put the icon in `svg/`
- Keep it aligned with the set (grid, stroke, style)

### 2) Add provenance metadata
- Create/update `meta/<icon-name>.json`

### 3) Optimize consistently (recommended)
Automate the boring parts to reduce human error:
- SVG optimization (e.g., SVGO)
- Optional sprite generation / import registry generation

> If your build pipeline doesn’t exist yet, consider adding a single command that:
> 1) validates metadata, 2) optimizes SVG, 3) writes runtime outputs.

### 4) Wire it into the UI
- Add to the icon registry (if your frontend uses one)
- Verify in:
  - 🗂️ layer list/catalog
  - 🧩 legend panels
  - ⏳ timeline controls (if relevant)
  - ♿ keyboard navigation + screen reader behavior

---

## 🧑‍💻 Usage patterns

> Your exact import style depends on the frontend toolchain. Pick **one** pattern and keep it consistent.

### Option A: Inline SVG component (best for theming)
```tsx
// example (tooling may vary)
import LayerRasterIcon from "@/assets/media/icons/map/layer-raster.svg";

export function LayerTypeChip() {
  return (
    <span className="chip">
      <img src={LayerRasterIcon} alt="" aria-hidden="true" />
      Raster
    </span>
  );
}
```

### Option B: Sprite / symbol usage (best for many icons)
```html
<svg aria-hidden="true" focusable="false">
  <use href="#icon-layer-raster"></use>
</svg>
```

### Accessibility note ♿
- Decorative icons: `alt=""` + `aria-hidden="true"`
- Meaningful icons: provide an accessible name (`aria-label`, or visible text)

---

## ✅ Review checklist (PR-ready)

- [ ] Icon file name follows conventions
- [ ] SVG has `viewBox` and scales cleanly
- [ ] Uses `currentColor` (or documented exceptions)
- [ ] No stray fills/strokes/filters
- [ ] Metadata file exists + includes license/provenance
- [ ] Icon looks correct at 16/20/24 px
- [ ] Works on light + dark themes
- [ ] Verified in relevant map UI surfaces

---

## 📚 External symbol sets (optional starting points)

If you need a jumpstart, there are multiple established map icon libraries. **Only import if license-compatible** and still record provenance + attribution in `meta/`.

- Mapbox “Maki”
- OSM SVG icon sets
- OSGeo symbol collections
- CC0 / public-domain map icon bundles

---

## 🧯 FAQ

### “Why are these in `_sources`?”
Because these should remain **editable** and **auditable**. Runtime assets can be optimized/generated from here so the repo keeps:
- clean diffs
- consistent outputs
- fewer one-off edits

### “Can I drop random icons in here?”
Not if they’re used by the UI. Add provenance + license metadata first. 🧾✅

---

## 🧭 Owner notes
- Keep icons boring and consistent. The map is the star. ⭐
- Prefer clarity over cleverness (especially for legends and layer types).
- When in doubt: create a small icon spec PR and align on style before bulk import.
