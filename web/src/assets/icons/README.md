# 🧩 Icons (KFM) — `web/src/assets/icons/`

![Icons](https://img.shields.io/badge/assets-icons-111827?style=for-the-badge)
![SVG First](https://img.shields.io/badge/SVG-first-0ea5e9?style=for-the-badge)
![Themeable](https://img.shields.io/badge/theme-currentColor-22c55e?style=for-the-badge)
![A11y](https://img.shields.io/badge/a11y-required-f59e0b?style=for-the-badge)
![Provenance](https://img.shields.io/badge/provenance-first-a855f7?style=for-the-badge)

> [!NOTE]
> This folder holds **UI icons** used by the Kansas Frontier Matrix (KFM) web frontend — especially map controls, timeline/story tooling, and Focus Mode affordances. Keep icons **consistent, accessible, and traceable**.

---

## 📁 Folder scope

Typical contents:

```text
web/
└─ src/
   └─ assets/
      └─ icons/
         ├─ README.md  👈 you are here
         ├─ *.svg      ✅ preferred
         └─ *.png      ⚠️ only when SVG isn't viable
```

---

## 🎯 Design goals (why we’re picky)

### 1) Clarity at tiny sizes 🔎
Icons must read cleanly at **16px / 20px / 24px** (toolbar + sidebar + mobile).

### 2) Consistency 🧱
A user should feel like the app was designed “as one system”, not stitched together.

### 3) Theme-ready 🌗
Icons should inherit color from CSS (`currentColor`) so dark/light themes “just work”.

### 4) Accessibility-first ♿
Icon-only UI must be screen-reader friendly (aria labels, decorative hiding, etc.).

### 5) Provenance-first ⛓️
KFM is evidence-first; icons must also respect governance: **track icon sources + licenses**.

---

## ✅ Standards (do this every time)

### 🧬 Preferred format: SVG

**Use SVG by default** because it’s:
- Resolution independent (crisp at any zoom)
- Small + cacheable
- Easy to color via CSS

#### ✅ SVG rules (hard requirements)
- Use a **standard viewBox**: `viewBox="0 0 24 24"` (preferred)  
- Avoid hard-coded fills like `fill="#000"` (use `currentColor`)
- Keep paths simple (fewer nodes = faster)
- Remove editor metadata (optimize!)

**Recommended pattern (monochrome):**
```xml
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="none">
  <path d="..." stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

> [!TIP]
> If you need both “outline” and “solid” versions, keep them as **separate files** (don’t overload one SVG with multiple styles).

---

## 🏷️ Naming conventions

### ✅ File naming
Use **kebab-case** and keep names **semantic** (what it means, not what it looks like).

**Recommended prefixes (optional but helpful):**
- `ui-` → generic interface (close, menu, settings)
- `map-` → map/geo actions (layers, locate, compass, measure)
- `time-` → timeline/story controls (play, pause, rewind)
- `data-` → datasets, downloads, citations/provenance
- `ai-` → Focus Mode / assistant affordances

Examples:
- `ui-close.svg`
- `map-layers.svg`
- `time-play.svg`
- `data-citation.svg`
- `ai-spark.svg`

### ✅ Variants
Use suffixes like:
- `-solid`, `-outline`
- `-sm`, `-lg` (only if you truly need size-specific art)
- `-disabled` (rare; prefer CSS)

---

## 🧩 Using icons in React (recommended patterns)

> [!IMPORTANT]
> Pick **one import pattern** and stick to it project-wide (consistency > preference).

### Option A: SVG as React component (SVGR-style)
```tsx
import { ReactComponent as LayersIcon } from "@/assets/icons/map-layers.svg";

export function LayersButton() {
  return (
    <button type="button" aria-label="Toggle layers">
      <LayersIcon aria-hidden="true" focusable="false" />
    </button>
  );
}
```

### Option B: SVG as URL (useful for `<img>` or CSS background)
```tsx
import layersUrl from "@/assets/icons/map-layers.svg";

export function LayersButton() {
  return (
    <button type="button" aria-label="Toggle layers">
      <img src={layersUrl} alt="" />
    </button>
  );
}
```

---

## ♿ Accessibility rules (non-negotiable)

### ✅ Decorative icons
If an icon is purely decorative (most icons inside buttons), hide it from screen readers:

- If using SVG component: `aria-hidden="true"`
- If using `<img>`: `alt=""`

### ✅ Icon-only buttons
If an icon is the only visible label, the **button must provide text for assistive tech**:

- `aria-label="Open citation panel"`
- or visible text + icon

> [!TIP]
> Tooltips are helpful, but **tooltips do not replace aria-labels**.

---

## 🧾 Provenance & licensing (KFM-style)

KFM is built on traceability. Icons must respect that too.

### ✅ When adding a third‑party icon
Create an entry in your preferred tracking file:
- `web/src/assets/icons/ATTRIBUTION.md` (simple)
- or `web/src/assets/icons/icons.manifest.json` (structured)
- or both (best)

**Minimum fields to record:**
- Source (project/site)
- License (SPDX if possible)
- Link to original
- Modifications (if any)
- Date added

Example manifest snippet:
```json
{
  "file": "map-layers.svg",
  "source": "Mapbox Maki (example)",
  "license": "CC0-1.0",
  "origin_url": "https://example.com/original",
  "modified": true,
  "notes": "Stroke adjusted to 2px; converted to currentColor."
}
```

> [!WARNING]
> Never import a third-party icon set “because it’s easy” without checking the license.
> This project is governance-heavy by design.

---

## 🗺️ Map icon sets (if you need external symbols)

If you need a map/cartography-oriented icon style, prefer established sets that are:
- Designed for map use (clarity at small sizes)
- License-compatible with KFM
- Consistent across categories (POIs, land use, transport, etc.)

> [!TIP]
> If you adopt an external set, **adapt it** to KFM’s visual rules (grid, stroke, currentColor) and record provenance.

---

## ⚙️ Optimization workflow (recommended)

### ✅ Before committing a new icon
- Remove unnecessary groups and transforms
- Ensure `viewBox` is correct
- Ensure `currentColor` behavior
- Run SVG optimization (e.g., SVGO)

Example (if SVGO is available):
```bash
npx svgo --folder web/src/assets/icons
```

---

## ✅ QA checklist (copy/paste into PRs)

- [ ] Renders cleanly at **16/20/24px**
- [ ] Uses `viewBox="0 0 24 24"` (or documented exception)
- [ ] Uses `currentColor` (no hard-coded fills unless required)
- [ ] Decorative icons use `aria-hidden="true"` or `alt=""`
- [ ] Icon-only controls include `aria-label`
- [ ] Source + license recorded (ATTRIBUTION / manifest)
- [ ] SVG optimized (no editor junk)

---

## 🧭 Future upgrades (nice-to-have)
- 🧪 Add an “icons gallery” dev page (visual regression for icons)
- 🧰 Add `npm run icons:optimize` + `npm run icons:lint`
- 🗂️ Introduce subfolders (`map/`, `ui/`, `data/`, `ai/`) if the set grows large