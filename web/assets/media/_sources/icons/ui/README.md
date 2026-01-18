# 🧩 UI Icons (Source Assets)

![Format](https://img.shields.io/badge/format-SVG-blue?logo=svg&logoColor=white)
![Scope](https://img.shields.io/badge/scope-KFM%20Web%20UI-0ea5e9)
![A11y](https://img.shields.io/badge/a11y-required-22c55e)

**Path:** `web/assets/media/_sources/icons/ui/`  
**Purpose:** Source-of-truth **UI** icon SVGs used across the Kansas Frontier Matrix (KFM) web app (maps, panels, toolbars, story UI, etc.). 🗺️✨

> [!NOTE]
> This folder is for **UI icons** (buttons, controls, panels).  
> **Map markers/symbols** should live in a dedicated markers/symbols folder (not here) to keep UI language clean and consistent. 🎯

---

## 🧠 Why this folder exists

KFM’s UI is **evidence-first** and **provenance-forward**—we want icons that help users navigate layers, timelines, citations, and “inspect the source” affordances without visual clutter. ✅

In short: icons are part of the trust experience. 🔎🧾

---

## 🗂️ Folder layout

```text
📦 web/
└── 🗂️ assets/
    └── 🗂️ media/
        └── 🗂️ _sources/
            └── 🗂️ icons/
                └── 🗂️ ui/
                    ├── 📄 README.md   👈 you are here
                    ├── 🖼️ layer-add.svg
                    ├── 🖼️ timeline.svg
                    ├── 🖼️ search.svg
                    └── 🖼️ …
```

> [!IMPORTANT]
> `_sources/` is the **authoring** home.  
> If your build system generates **optimized** icons/sprites elsewhere, do **not** hand-edit the generated output. Edit here. 🧰

---

## ✅ Quick rules (TL;DR)

- **SVG only** (no PNG for UI icons) 🧬
- **24×24 viewBox** by default (`viewBox="0 0 24 24"`) 📐
- Use **`currentColor`** for stroke/fill (no hard-coded colors) 🎨➡️🧠
- Keep shapes **simple** (avoid complex masks/filters) ✂️
- Name icons in **kebab-case** (`layer-add.svg`, `info-circle.svg`) 🏷️
- Icons must be **legible at 16–20px** (common toolbar sizes) 👀

---

## 📐 Icon spec

| Property | Standard | Notes |
|---|---:|---|
| Canvas | 24×24 | Scale via CSS (don’t export multiple sizes) |
| `viewBox` | `0 0 24 24` | Required |
| Stroke width | `2` (recommended) | Prefer consistent stroke across set |
| Stroke caps/joins | `round` / `round` | Cleaner at small sizes |
| Color | `currentColor` | Inherit from parent CSS |
| Padding | ~2px safe area | Avoid touching edges |

> [!TIP]
> If you need a filled icon, prefer `fill="currentColor"` **without** baked-in palette values.

---

## 🧩 Recommended SVG templates

### Outline icon template ✍️
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path
    d="M12 5v14M5 12h14"
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
</svg>
```

### Filled icon template 🟦
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <path d="M12 2l10 20H2L12 2z" fill="currentColor" />
</svg>
```

---

## 🏷️ Naming conventions

### ✅ Do
- `layer-add.svg`
- `layer-remove.svg`
- `timeline-play.svg`
- `timeline-pause.svg`
- `source.svg` / `citation.svg` (for provenance UI)
- `warning.svg` / `info.svg` (for advisory messaging)

### ❌ Don’t
- `LayerAdd.svg` (no PascalCase)
- `layer_add.svg` (no snake_case)
- `add-layer-final-FINAL.svg` (no chaos 😅)
- `icon1.svg` (no meaning)

> [!NOTE]
> Prefer `noun-verb` for actions (`layer-add`) and `noun-noun` for concepts (`data-catalog`).

---

## 🧼 SVG hygiene checklist

Before committing an icon, make sure:

- [ ] Has `xmlns` and `viewBox`
- [ ] No embedded raster images (`<image ...>`)
- [ ] No hard-coded color values (`#fff`, `rgb(...)`) — use `currentColor`
- [ ] No editor metadata (Sketch/Figma junk) 🧹
- [ ] Minimal paths (merge shapes where reasonable)
- [ ] No unnecessary `<defs>` unless required
- [ ] Looks good at **16px** and **24px**

---

## ⚛️ Usage patterns (React/HTML)

### Option A: Inline SVG (best for theming) 🎨
```jsx
<button className="IconButton" aria-label="Add layer">
  {/* Inline SVG inherits `currentColor` */}
  <svg viewBox="0 0 24 24" role="img" aria-hidden="true">
    <path d="M12 5v14M5 12h14" fill="none" stroke="currentColor" strokeWidth="2" />
  </svg>
</button>
```

### Option B: SVG sprite `<use>` (best for reuse) 🧷
```html
<svg class="icon icon-layer-add" aria-hidden="true">
  <use xlink:href="#icon-layer-add"></use>
</svg>
```

> [!TIP]
> Sprites can reduce duplication; inline icons make dynamic styling easier. Choose based on your bundler + caching strategy. ⚖️

---

## ♿ Accessibility rules

Icons can be **decorative** or **meaningful**:

### Decorative icon ✅
- Use `aria-hidden="true"` and no accessible name.

### Meaningful icon ✅
- Ensure the control has an accessible name (`aria-label`, visible text, or `<title>` in SVG).

> [!IMPORTANT]
> Never rely on color alone to communicate meaning. Pair icons with text/tooltips where ambiguity is possible. 🧑‍🦯

---

## 🧑‍🔧 Adding a new icon (workflow)

1. **Design** on a 24×24 grid (consistent stroke + padding) 📐
2. **Export** as SVG (outline/fill using `currentColor`) 🎨
3. **Clean** the SVG (remove metadata, collapse groups) 🧼
4. **Name** it with kebab-case and a stable semantic name 🏷️
5. **Check** it at 16px/20px/24px 👀
6. **Use** it in the UI component library (button, menu item, map control) 🧩

---

## 🧭 Suggested UI icon taxonomy (helps keep things consistent)

- 🗺️ **Map & navigation:** `pan`, `zoom-in`, `zoom-out`, `locate`, `compass`
- 🧱 **Layers & styling:** `layer`, `layer-add`, `opacity`, `legend`
- 🕒 **Time:** `timeline`, `play`, `pause`, `step-forward`, `step-back`
- 🔎 **Discovery:** `search`, `filter`, `sort`, `tag`
- 🧾 **Provenance & evidence:** `source`, `citation`, `link`, `audit`
- 🤖 **AI (advisory):** `spark`, `insight`, `confidence-low`, `confidence-high`
- ⚠️ **Status & messaging:** `info`, `warning`, `error`, `success`
- 📦 **Data actions:** `download`, `upload`, `export`, `copy`

---

## 🧯 Troubleshooting

**Icon looks blurry at 16px**  
➡️ Simplify geometry, ensure consistent stroke width, avoid tiny details, and re-check alignment.

**Icon won’t theme correctly**  
➡️ Remove hard-coded fills/strokes and replace with `currentColor`.

**Icon feels ambiguous**  
➡️ Add a tooltip + consider a more concrete metaphor. KFM values clarity over cleverness. 🧠✅

---

## 🔗 Related docs

- `web/` (frontend app)
- `web/assets/` (static assets)
- `docs/MASTER_GUIDE_v13.md` (system invariants & directory canon)
- `docs/reports/story_nodes/` (narrative UI content)

🧭 Keep icons boringly consistent — the map, evidence, and stories are the stars. ⭐
