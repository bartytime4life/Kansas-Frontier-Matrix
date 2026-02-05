<!--
📁 web/src/assets/map/icons/ui/
🎯 Purpose: SVG icons used for **Map UI controls** (buttons, toggles, panels) in the KFM web frontend.
-->

# 🧭 Map UI Icons (SVG)

![Format](https://img.shields.io/badge/format-SVG-blue?logo=svg&logoColor=white)
![Scope](https://img.shields.io/badge/scope-map%20UI-informational)
![Theming](https://img.shields.io/badge/theming-currentColor-success)

> [!NOTE]
> These icons are part of the **map “UI chrome”**: they should be quiet, consistent, and themeable so the map + data stay the star ⭐

---

## 📍 What lives here (and what *doesn’t*)

✅ **Belongs in this folder**
- Map UI controls: zoom, locate, rotate, reset view 🧭
- Panels & tools: layers, legend, search, filters, measure 🧰
- Timeline controls: play/pause, step, scrub indicator ⏱️
- UX “helpers”: info/help, citations/provenance, close/back ✨

🚫 **Does NOT belong in this folder**
- Feature markers / pins / POI symbols 📌 → *(use a markers folder / sprite system)*
- Layer symbology icons that render **on the map** 🗺️ → *(use map style sprites or layer-symbol assets)*
- Brand logos / external trademarks ™️ → *(keep separate and license-aware)*

---

## 🗺️ Where these icons typically show up

- **Corner controls**: zoom in/out, locate-me, reset bearing (avoid covering key map content)
- **Layer picker**: toggle layers (e.g., “Radar”, “Temperature”, “Wind”, “History Layers”) 🧩
- **Legend**: open/close legend + scale indicators 🎛️
- **Timeline overlay**: play/pause + slider interactions (tick marks, step forward/back) ⏳
- **Provenance UI**: “source / citation / evidence” affordances 🔎

> [!TIP]
> If an icon sits on top of the map, treat it like map furniture 🪑: keep it compact, high-contrast, and predictable.

---

## 🏷️ Naming conventions

**Goals:** easy to search, predictable imports, no guesswork.

### ✅ Rules
- **kebab-case** only: `layers.svg`, `zoom-in.svg`
- Prefer **verbs** for actions: `play.svg`, `pause.svg`, `close.svg`
- Prefer **nouns** for panels/tools: `legend.svg`, `layers.svg`, `measure.svg`
- Use **prefixes** for families: `timeline-play.svg`, `timeline-pause.svg`
- Use **variants** only when necessary: `*-outline.svg`, `*-solid.svg`

### Examples
| Type | ✅ Good | 🚫 Avoid |
|---|---|---|
| Action | `zoom-in.svg` | `ZoomIn.svg` |
| Panel | `layers.svg` | `layerControl.svg` |
| Timeline | `timeline-play.svg` | `playTimeline.svg` |
| Variant | `info-outline.svg` | `info_v2_final.svg` |

---

## 🎨 Design spec (make icons feel like one set)

### 📐 Sizing & grid
- Standard: **24×24** icon grid (`viewBox="0 0 24 24"`)
- Keep shapes aligned to a clean grid to avoid blur on small UI

### 🎛️ Style consistency
Pick **one** icon style for the map UI and stick to it:
- **Outline** is recommended for map chrome (less visually “heavy” than filled icons)

Suggested defaults:
- `stroke-width="2"`
- `stroke-linecap="round"`
- `stroke-linejoin="round"`

### 🌈 Theming (required)
- Use `currentColor` so icons inherit from CSS/theme
- Avoid hard-coded colors inside SVG unless there’s a *strict* semantic need (rare)

---

## 🧩 SVG authoring rules (do this every time)

### ✅ Do
- Use a single `<svg>` root with:
  - `viewBox="0 0 24 24"`
  - `xmlns="http://www.w3.org/2000/svg"`
- Prefer paths with `stroke="currentColor"` and/or `fill="currentColor"`
- Keep SVGs small & clean (no editor metadata)

### 🚫 Don’t
- Don’t bake in `width`/`height` unless a renderer requires it
- Don’t embed raster images (`<image ...>`)
- Don’t include text elements for labels (use UI text + accessibility instead)
- Don’t use unlicensed icon sources 🙅‍♂️

---

## 🧱 SVG template (copy/paste starter)

```xml
<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path
    d="M12 5v14M5 12h14"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
</svg>
```

---

## ♿ Accessibility (non-negotiable)

### Decorative icon inside a button
- Button must have an accessible name (`aria-label` or visible text)
- Icon should be hidden from screen readers

```tsx
<button aria-label="Open layers" className="MapControl">
  <LayersIcon aria-hidden="true" focusable="false" />
</button>
```

### Meaningful standalone icon
If the icon itself conveys meaning (rare for UI chrome), use `role="img"` + label:

```tsx
<WarningIcon role="img" aria-label="Warning" />
```

---

## 🧰 Using icons in React

> [!IMPORTANT]
> Your import syntax depends on the bundler setup (SVGR / Vite / CRA). Use the pattern already present in the codebase.

### Common patterns

```tsx
// Vite + SVGR (common)
import LayersIcon from "@/assets/map/icons/ui/layers.svg?react";

// CRA-style SVGR (also common)
import { ReactComponent as LayersIcon } from "@/assets/map/icons/ui/layers.svg";
```

---

## 🧪 Optimization (keep the repo fast)

- Run SVG optimization (ex: `svgo`) before committing
- Avoid redundant `<g>` wrappers, transforms, and hidden layers

<details>
  <summary>🛠️ Suggested SVGO command (example)</summary>

```bash
# example only — use the repo’s existing tooling if present
npx svgo --folder web/src/assets/map/icons/ui --recursive
```

</details>

---

## 🧾 Licensing & provenance (KFM standard)

Because KFM is **evidence-first**, icon assets should also be provenance-aware:

- If an icon is **authored in-house** ✅: no special note needed
- If an icon is **adapted from a library** 🧩:
  - record **source**, **license**, **author**, and **modifications**
  - keep attribution close to the asset set (here, or a sibling `ATTRIBUTION.md`)

<details>
  <summary>🧷 Example provenance entry (recommended pattern)</summary>

```yaml
# icons-ui.provenance.yml (suggested)
- file: layers.svg
  source: "In-house"
  license: "Project-owned"
  notes: "Original KFM icon set"

- file: locate.svg
  source: "External library name"
  license: "MIT"
  author: "Author/Org"
  modified: true
  notes: "Simplified outline + converted to currentColor"
```

</details>

---

## ✅ Add-a-new-icon checklist

- [ ] Named in **kebab-case**
- [ ] `viewBox="0 0 24 24"`
- [ ] Uses `currentColor` (themeable)
- [ ] Matches stroke weight + style of the set
- [ ] Optimized (SVGO or repo-equivalent)
- [ ] Accessible usage planned (button label, aria rules)
- [ ] Provenance recorded if sourced externally 🧾

---

## 🔁 Quick decision guide

- **Need a UI button icon?** → ✅ Put it here
- **Need an on-map symbol/marker?** → 📌 Not here
- **Need a dataset/layer identity icon?** → 🗂️ Probably a `layers/` or `legend/` asset area
- **Need a one-off icon for a story node?** → 📚 Consider story-node assets instead

---

## 🧭 Suggested baseline set (nice-to-have)

If the folder is empty or growing, these are common map-UI essentials:
- `zoom-in.svg`, `zoom-out.svg`
- `locate.svg`
- `layers.svg`, `legend.svg`
- `search.svg`, `filter.svg`
- `timeline-play.svg`, `timeline-pause.svg`, `timeline-step-forward.svg`, `timeline-step-back.svg`
- `info.svg`, `citation.svg`, `close.svg`

✨ Keep it small. Reuse before adding new files.
