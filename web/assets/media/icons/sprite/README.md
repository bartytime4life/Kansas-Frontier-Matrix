# 🧩 Icon Sprite (UI + Map) — `web/assets/media/icons/sprite/`

![type](https://img.shields.io/badge/type-assets-blue)
![format](https://img.shields.io/badge/format-SVG%20Sprite-success)
![focus](https://img.shields.io/badge/focus-performance%20%26%20accessibility-purple)

A single, cacheable **SVG sprite** powering consistent icons across the KFM web UI — from buttons + panels to map layers/markers.  
This directory is intentionally “boring”: **generated artifacts in one place, used everywhere** ✅

---

## 🗂️ What’s in this folder?

```text
📦 web/
└─ 🖼️ assets/
   └─ 🎞️ media/
      └─ 🧿 icons/
         └─ 🧩 sprite/
            ├─ 🧾 README.md              ← you are here
            ├─ 🧵 sprite.svg             ← SVG symbols (primary)
            ├─ 🧾 sprite.manifest.json   ← optional: name → metadata
            ├─ 🖼️ sprite.png             ← optional fallback (legacy/exports)
            └─ 🗺️ preview.html           ← optional dev preview page
```

> **Rule of thumb:** if it’s an output from a generator/build step, it belongs here.  
> If it’s a *source icon* you draw/edit, it likely belongs in a sibling “source” directory (e.g. `../src/`, `../raw/`, `../svg/`).

---

## ✅ Why a sprite?

- 🚀 **Performance**: one request (or inlined) instead of hundreds of icon files  
- 🧠 **Consistency**: shared sizing, stroke weight, and visual language  
- 🎨 **Theming**: icons can use `currentColor` and adapt to dark/light/UI states  
- 🧾 **Provenance-friendly**: one manifest can track licensing + attribution per icon (aligned with KFM’s “traceable sources” mindset)

---

## ⚡ Quick usage

### 1) HTML / Vanilla

```html
<!-- Decorative icon -->
<svg class="Icon" aria-hidden="true" focusable="false">
  <use href="/assets/media/icons/sprite/sprite.svg#search" />
</svg>

<!-- Informative icon -->
<svg class="Icon" role="img" aria-label="Download">
  <use href="/assets/media/icons/sprite/sprite.svg#download" />
</svg>
```

✅ Recommended CSS:

```css
.Icon {
  width: 1em;
  height: 1em;
  display: inline-block;
  vertical-align: -0.125em;
  fill: currentColor;
  stroke: currentColor;
}
```

> 💡 If you run into older browser edge cases, you can also try `xlink:href`:
> ```html
> <use href="...#download" xlink:href="...#download" />
> ```

---

### 2) React / TS-friendly pattern

```tsx
type IconProps = {
  name: string;
  title?: string; // if provided: becomes "informative" icon
  className?: string;
};

const SPRITE_URL = "/assets/media/icons/sprite/sprite.svg";

export function Icon({ name, title, className }: IconProps) {
  const href = `${SPRITE_URL}#${name}`;
  const decorative = !title;

  return (
    <svg
      className={className ?? "Icon"}
      aria-hidden={decorative ? "true" : undefined}
      role={decorative ? undefined : "img"}
    >
      {title ? <title>{title}</title> : null}
      <use href={href} />
    </svg>
  );
}
```

---

## 🧭 Naming conventions (IDs)

Keep IDs:
- **short**
- **kebab-case**
- **semantic** (what it *means*, not how it looks)

Examples:
- `search`, `download`, `settings`
- `map-pin`, `layer-raster`, `layer-vector`
- `warning`, `info`, `success`

🚫 Avoid:
- `blue-circle`, `icon1`, `thingy`

> ✨ Tip: If you anticipate collisions, namespace lightly:  
> `ui-search`, `map-pin`, `data-table`, etc.

---

## 🎨 Design rules (so the set looks like one family)

### Geometry & style
- 📐 Use a consistent `viewBox` across the set (common: `0 0 24 24`)
- 🧵 Prefer `stroke` icons with a consistent stroke width (common: `2`)
- 🔁 Match line caps/joins (rounded is friendlier; choose once and stick to it)
- 🧩 Keep shapes aligned to the pixel grid *where it matters* (crisper small sizes)
- 🧼 Remove stray transforms, invisible layers, and unnecessary groups

### Color & theming
- ✅ Prefer `currentColor` (or no explicit fill/stroke) so the UI can theme via CSS
- 🚫 Don’t hard-code colors (unless the icon is intentionally “status-colored” and documented)

### Accessibility defaults
- Decorative icons: `aria-hidden="true"` ✅
- Informative icons: add `aria-label` or `<title>` ✅

---

## 🧾 Provenance, licensing, and attribution

KFM treats metadata as a first-class citizen. Icons should follow the same spirit:

- ✅ Use original icons, or icons with a compatible license
- ✅ Track attribution per icon (recommended via a manifest)

**Suggested manifest shape** (`sprite.manifest.json`):

```json
{
  "search": {
    "category": "ui",
    "source": "internal",
    "license": "Proprietary",
    "notes": "KFM icon family v1"
  },
  "map-pin": {
    "category": "map",
    "source": "internal",
    "license": "Proprietary"
  }
}
```

> If you import third-party icons, add enough info that a future contributor can audit it without guesswork.

---

## 🔧 Updating / regenerating the sprite

This folder should generally be **generated**, not hand-edited.

Typical workflow:
1. ➕ Add or update source SVG(s) in the project’s icon *source* directory
2. 🧪 Optimize (SVGO or equivalent)
3. 🏗️ Rebuild sprite (project script / build step)
4. 👀 Verify in a preview page (optional)
5. ✅ Commit updated `sprite.svg` (and manifest, if used)

> 🔍 Look for an existing script in `package.json` (commonly named something like `icons:sprite`, `sprite:build`, or `build:icons`).

---

## 🧯 Troubleshooting

**Icon not showing?**
- ✅ Confirm the symbol ID exists inside `sprite.svg` (`#your-id`)
- ✅ Check the path to the sprite file (dev server base path vs production path)
- ✅ Hard refresh (sprites are *heavily cached* on purpose)
- ✅ Confirm CSS isn’t setting `fill: none` (common gotcha)

**Icon is blurry / inconsistent at 16px**
- ✅ Verify stroke width + alignment
- ✅ Test at common sizes: `16, 18, 20, 24, 32`

---

## 🧪 Minimal checklist for new icons

- [ ] Uses the standard `viewBox`
- [ ] Uses `currentColor` (or no explicit colors)
- [ ] Matches stroke width and cap/join style
- [ ] Cleaned/optimized SVG (no junk metadata)
- [ ] Named with clear, kebab-case ID
- [ ] Added/updated provenance in manifest (if applicable)

---

## 📌 Notes for map usage

Map icons often appear:
- very small (12–18px)
- on top of imagery
- in clusters

So:
- ✅ keep silhouettes simple
- ✅ avoid fine internal detail
- ✅ test in both light + dark basemaps

---

## 🔗 Related (within the repo)

- 🧭 UI components that render icons (search for `#` + icon IDs)
- 🎛️ Any theme tokens that set icon color (`currentColor` depends on surrounding CSS)
- 🗺️ Map marker layer styling (icons should be readable against basemaps)

---

*Last updated: keep this README aligned with how the sprite is actually generated and consumed in KFM.* ✨
