# 🧩 Icons — `web/assets/media/icons/`

![KFM](https://img.shields.io/badge/KFM-web%20ui-blue)
![Icons](https://img.shields.io/badge/icons-SVG%20preferred-informational)
![Naming](https://img.shields.io/badge/naming-lower_case_with_underscores-5865F2)
![A11y](https://img.shields.io/badge/a11y-required-success)

This folder is the **single source of truth** for icon assets used across the Kansas Frontier Matrix **web front-end** (map viewer, catalog UI, story nodes, etc.). 🗺️✨  
Icons are part of the “trust UI”: they should help users navigate layers, timelines, citations, and provenance without friction.

---

<details>
  <summary><b>📚 Table of Contents</b></summary>

- [🧭 What lives here](#-what-lives-here)
- [🗂️ Folder layout](#️-folder-layout)
- [✅ Supported formats](#-supported-formats)
- [🏷️ Naming rules](#️-naming-rules)
- [🎨 SVG design rules](#-svg-design-rules)
- [🧱 Sprite workflow](#-sprite-workflow)
- [♿ Accessibility rules](#-accessibility-rules)
- [🧾 Licensing & attribution](#-licensing--attribution)
- [🧪 QA checklist](#-qa-checklist)
- [➕ Adding a new icon](#-adding-a-new-icon)
- [🧯 Troubleshooting](#-troubleshooting)

</details>

---

## 🧭 What lives here

KFM’s web UI includes common controls like:

- 🧱 **Layer list / data catalog** (toggle datasets, adjust settings)
- 🔎 **Search**
- 🏷️ **Legends**
- 🕰️ **Timeline slider**
- 🧾 **Popups / side panels** (details + context)

Icons in this directory should map cleanly to those UI concepts (and keep the interface readable at small sizes).

---

## 🗂️ Folder layout

Recommended structure (adjust as the system grows, but keep it predictable):

```text
web/assets/media/icons/
├─ 📄 README.md                 # 📘 Icon rules: naming, sizes, stroke/filled variants, accessibility, licensing
├─ 🎛️ ui/                       # Buttons/menus/generic UI glyphs (shared across app surfaces)
├─ 🗺️ map/                      # Map controls: layers, basemap, 2D/3D, measure, locate, etc.
├─ 📍 markers/                  # POI markers/pins (often referenced by map styles or legend blocks)
├─ 🚦 status/                   # Status icons: loading/success/warning/error/uncertainty/AI
├─ 🏷️ logos/                    # KFM + partner marks (tightly governed; avoid mixing with generic icons)
├─ 📦 third_party/              # Imported vendor icon sets (each pack w/ license + attribution kept alongside)
└─ 🧩 sprite/                   # Optional SVG sprite sheets for bundling/caching (<symbol> + <use> pattern)
```

> 💡 Tip: If an icon is **domain-specific** (e.g., 🌾 agriculture, 🌊 water, 🌪️ hazards), consider a dedicated subfolder (e.g., `domains/water/`) *only after* the set is large enough to justify it.

---

## ✅ Supported formats

| Format | Use it for | Notes |
|---|---|---|
| **`.svg`** ✅ | Almost everything | Crisp at any zoom level, styleable with CSS |
| **`.png`** ⚠️ | Rare cases | Only when raster is required (complex multi-color marker art, legacy constraints) |

**Default rule:** if it can be SVG, it **should** be SVG.

---

## 🏷️ Naming rules

Keep names **stable**, **searchable**, and **boring** (boring is good 😄).

### ✅ Do
- `lower_case_with_underscores`
- Prefix by category if helpful:
  - `ui_search.svg`
  - `map_layers.svg`
  - `status_warning.svg`
  - `marker_weather_station.svg`

### ❌ Don’t
- Spaces, camelCase, random abbreviations
- `final_final_v2.svg` (we use git for history)

---

## 🎨 SVG design rules

### Grid + sizing
- Design to a consistent grid (commonly **24×24** or **16×16**).
- Always include a valid `viewBox` (don’t rely on width/height alone).

### Color + theming
- Prefer theme-driven icons:
  - `stroke="currentColor"` for outline icons
  - `fill="currentColor"` for filled icons
- Avoid hard-coded colors unless the icon is intentionally “semantic color” (rare).

Example (outline icon):

```svg
<svg viewBox="0 0 24 24" aria-hidden="true">
  <path d="M4 12h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>
```

### Keep SVGs clean
- Remove editor metadata, hidden layers, and unused `<defs>`.
- Avoid embedding raster images inside SVGs.
- Prefer simple paths over excessive groups.

---

## 🧱 Sprite workflow

If we want fewer network requests and fast reuse, we can use an **SVG sprite** (symbols + `<use>`).  
This is especially useful for UI icons used in many places.

### `sprite/sprite.svg` (example)

```svg
<svg xmlns="http://www.w3.org/2000/svg">
  <symbol id="ui_search" viewBox="0 0 24 24">
    <path d="M21 21l-4.3-4.3" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
    <circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2"/>
  </symbol>
</svg>
```

### Using the sprite (HTML)

```html
<svg class="icon" aria-hidden="true">
  <use href="/assets/media/icons/sprite/sprite.svg#ui_search"></use>
</svg>
```

### Using the sprite (React-ish)

```jsx
export function Icon({ name, title }) {
  const href = `/assets/media/icons/sprite/sprite.svg#${name}`;
  const labelled = Boolean(title);

  return (
    <svg className="icon" role={labelled ? "img" : "presentation"} aria-hidden={labelled ? undefined : true}>
      {labelled ? <title>{title}</title> : null}
      <use href={href} />
    </svg>
  );
}
```

> 🧠 Rule of thumb:  
> - **Sprite** for small, repeated UI icons  
> - **Standalone SVG** for larger illustrations, special markers, or assets that rarely appear

---

## ♿ Accessibility rules

Icons are either **decorative** or **meaningful**. Treat them differently:

### Decorative icons ✅
- Must be ignored by screen readers:
  - `aria-hidden="true"`
  - OR `role="presentation"`

### Meaningful icons ✅
- Must have an accessible name:
  - `<title>` inside the SVG **or**
  - `aria-label="…"` on the control using the icon

Also:
- Don’t rely on icon-only meaning when a text label is feasible.
- Ensure **touch targets** are large enough even if the glyph is small.

---

## 🧾 Licensing & attribution

If an icon came from somewhere else (library, vendor, designer pack), it **must** be tracked.

### Third-party icon rules
Store third-party icons under:

```text
web/assets/media/icons/third_party/<library_or_source>/
├─ LICENSE
├─ SOURCE.md        # where it came from + link + version + notes
└─ *.svg
```

**SOURCE.md** should include:
- Source name + link
- License type
- Any modifications you made (color, shape, simplification)
- Date added (optional but helpful)

---

## 🧪 QA checklist

Before committing an icon, verify:

- [ ] ✅ Filename matches conventions (`lower_case_with_underscores`)
- [ ] ✅ SVG has `viewBox`
- [ ] ✅ Uses `currentColor` (unless explicitly not desired)
- [ ] ✅ Looks good at **16px / 20px / 24px**
- [ ] ✅ No unnecessary metadata / hidden layers
- [ ] ✅ Accessibility: decorative vs meaningful handled correctly
- [ ] ✅ Licensing tracked if not original work

---

## ➕ Adding a new icon

1. 🧠 Decide category: `ui/`, `map/`, `markers/`, etc.
2. 🏷️ Name it using `lower_case_with_underscores`
3. 🎨 Export as SVG with clean paths + correct `viewBox`
4. 🧼 Clean/optimize (SVGO or equivalent)  
5. 🧱 If it’s a common UI icon, consider adding it to the sprite
6. 🧾 If third-party: add `LICENSE` + `SOURCE.md`
7. ✅ Run through the QA checklist above

---

## 🧯 Troubleshooting

### “My icon isn’t inheriting CSS color”
- Ensure it uses `fill="currentColor"` and/or `stroke="currentColor"`.
- Remove hard-coded `fill="#000"` from exported paths.

### “It looks blurry”
- Verify the `viewBox` matches the design grid.
- Ensure strokes align to pixel boundaries at typical sizes (e.g., 16/24).

### “Sprite icons don’t show up”
- Confirm the `<use href="...#symbol_id">` path is correct.
- Ensure the sprite is served by the same origin (or CORS allows it).

---

🧡 **Design goal:** Icons should feel consistent, readable, and trustworthy—supporting KFM’s “inspectable data” experience without adding clutter.
