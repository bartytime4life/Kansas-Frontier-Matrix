# 🧩 Icon Assets (Web UI)

![Icons](https://img.shields.io/badge/icons-SVG%20preferred-brightgreen)
![Accessibility](https://img.shields.io/badge/a11y-ARIA%20friendly-blue)
![Theming](https://img.shields.io/badge/theming-currentColor%20ready-6f42c1)

> 📍 **Location:** `web/src/assets/images/icons/`  
> 🗺️ Used across the **KFM** React UI (map controls, layer toggles, timeline, Focus Mode, provenance/citation UI).

---

## ✅ TL;DR Rules (please follow)

- **SVG-first** for icons (crisp at any zoom).
- **kebab-case** filenames (lowercase, hyphens).
- Default **icon grid:** `24×24` with `viewBox="0 0 24 24"`.
- Use **`currentColor`** (or CSS-driven color) so icons theme automatically.
- **No embedded text** (text should be real UI text, not baked into SVG).
- Treat SVG like code: **no scripts, no external references**.

---

## 🗂️ Folder Map

```text
web/
└─ src/
   └─ assets/
      └─ images/
         └─ icons/
            ├─ README.md        👈 you are here
            ├─ (optional) sprites/    🧵 Map sprite outputs (if used)
            ├─ (optional) brands/     🏷️ logos (only if licensed)
            └─ *.svg / *.png
```

> 💡 Keep this folder **icon-only**. Large illustrations, photos, and map rasters belong elsewhere.

---

## 🏷️ Naming Convention

Use **kebab-case** + (optional) a lightweight prefix to keep things searchable.

### Recommended
- `ui-close.svg`
- `ui-search.svg`
- `map-layer.svg`
- `map-pin.svg`
- `data-download.svg`
- `data-citation.svg`
- `ai-focus.svg`

### Avoid
- `CloseIcon.svg` (PascalCase)
- `icon_close_final_FINAL.svg` (😵)
- `close (1).svg` (spaces / duplicates)

---

## 🎛️ Formats: What to Use (and When)

### ✅ SVG (preferred)
Use for:
- Buttons, menus, toolbars
- Map controls (zoom, layers, legend)
- Status icons (loading, warning, success)
- “Cite / Source / Provenance” UI indicators

**SVG requirements**
- Keep a clean `viewBox`
- Remove fixed `width`/`height` unless truly needed
- Prefer `fill="currentColor"` and/or `stroke="currentColor"`
- Avoid inline styles when possible (CSS should theme)

### 🟦 PNG (only when SVG is not practical)
Use for:
- Complex **raster** iconography that *must* be pixel-based
- Cesium billboards / map markers that depend on raster textures
- Sprite sheets (generated)

**PNG requirements**
- Keep it small
- Prefer transparent backgrounds when needed
- Provide `@2x` versions if the UI needs crisp retina assets

### 🚫 Not in this folder
- Photos (JPG/WebP) 📸
- Large illustrations 🖼️
- Map tiles, basemaps, raster layers 🗺️

---

## 🎨 Visual Consistency Guidelines

To keep the UI “quiet” and readable:

- **Grid:** 24×24 (default), 16×16 (dense UI), 32×32 (hero/empty states)
- **Stroke width:** pick one standard (commonly 1.5–2) and keep it consistent
- **Caps/joins:** round/round tends to read well at small sizes
- **Padding:** don’t let strokes touch the edge of the viewBox
- **Optical alignment > mathematical alignment** (especially for arrows/chevrons)

---

## ⚛️ Using Icons in React

> Pick **one** pattern and stay consistent across the codebase.

### Option A (Preferred): SVG as a React Component (SVGR-style)
This gives you easy sizing, theming, and accessibility.

```tsx
// Example (path/alias may differ in this repo)
import { ReactComponent as LayersIcon } from "@/assets/images/icons/map-layer.svg";

export function LayerToggleButton() {
  return (
    <button type="button" className="btn">
      <LayersIcon aria-hidden="true" focusable="false" />
      <span className="sr-only">Layers</span>
    </button>
  );
}
```

**Why this is good**
- CSS can control color (`currentColor`)
- You can size with `width/height` or CSS
- Great for dark mode + theme switching

### Option B: Use as an `<img>` (fallback)
Use this if the bundler doesn’t support SVG-to-component transforms.

```tsx
import layersIconUrl from "@/assets/images/icons/map-layer.svg";

export function LayerToggleButton() {
  return <img src={layersIconUrl} alt="Layers" width={24} height={24} />;
}
```

> ⚠️ If you use `<img>`, you lose some fine-grained theming unless you maintain multiple colored variants.

---

## ♿ Accessibility Rules

### Decorative icons (most UI chrome)
- Use `aria-hidden="true"` and no label
- Provide real text for screen readers via `sr-only` spans if needed

```tsx
<CloseIcon aria-hidden="true" />
<span className="sr-only">Close</span>
```

### Meaningful icons (convey unique info)
If the icon alone conveys meaning (status, warning, provenance marker), give it an accessible label:

```tsx
<WarningIcon role="img" aria-label="Warning" />
```

---

## 🧾 Provenance & Licensing (KFM-style)

KFM is evidence-first—UI assets should be traceable too.

**If an icon is not created in-house**, record:
- Source (site/library)
- License (MIT/Apache/CC/etc.)
- Author/attribution requirements
- Date added + who added it
- Any modifications

✅ Recommended approach:
- Add a lightweight `icons.manifest.json` (or `.md`) next to this README.

Example (optional):
```json
{
  "ui-search.svg": {
    "source": "in-house",
    "license": "proprietary",
    "notes": "Matches KFM UI stroke set v1"
  },
  "data-citation.svg": {
    "source": "external",
    "license": "MIT",
    "attribution": "Required in docs/ATTRIBUTIONS.md"
  }
}
```

---

## ➕ Add a New Icon Checklist

1. ✏️ **Design** on a 24×24 grid (or match existing set size).
2. 📤 **Export** as plain SVG (no editor metadata if possible).
3. 🧼 **Optimize** (SVGO or equivalent).
4. 🎛️ **Theme-proof** it (`currentColor`, no hard-coded fills unless intentional).
5. ♿ **A11y check** (decorative vs meaningful).
6. 🧾 **Provenance**: update `icons.manifest.json` (recommended).
7. 🔍 **Visual QA**: test at 16/20/24px and in dark mode.

---

## 🛠️ Suggested Tooling

- **SVGO** for SVG optimization  
  Example:
  ```bash
  npx svgo web/src/assets/images/icons --recursive
  ```

- **Lint rule idea** (optional): fail CI if SVG contains:
  - `<script>`
  - `onload=`
  - external `href` references
  - `<foreignObject>`

---

## 🧨 Common Gotchas

- ❌ Losing `viewBox` during export → icon won’t scale correctly.
- ❌ Hard-coding `fill="#000"` → icon breaks in dark mode.
- ❌ Inconsistent stroke width → UI looks “off” even if users can’t explain why.
- ❌ Over-detailed icons → muddy at 16px.

---

## 🔗 Related Docs (in-repo)

- `docs/architecture/` 📐 (system overview, UI/AI integration)
- `docs/ui/` 🎨 (if/when we add a design system + icon spec)
- `web/README.md` ⚙️ (frontend setup & build)

---

🧭 **Goal:** Icons should support KFM’s “trustworthy interface” vibe—clear, consistent, accessible, and provenance-aware.
