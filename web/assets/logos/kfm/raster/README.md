# 🟦 KFM Raster Logos (PNG)

![Format](https://img.shields.io/badge/format-PNG-informational)
![Scope](https://img.shields.io/badge/scope-KFM%20brand%20assets-blue)
![Rule](https://img.shields.io/badge/prefer-SVG%20when%20possible-success)

📍 **Path:** `web/assets/logos/kfm/raster/`  
🧭 **Purpose:** Pixel-based exports of the **Kansas Frontier Matrix (KFM)** logo for fixed-size / compatibility scenarios (favicons, OpenGraph, emails, PDFs, etc.).

---

## 🧠 Quick rules (read this first)

- ✅ **Use SVG (vector) by default** for in-app UI (crisp at any size, smallest payload).
- ✅ **Use these PNGs** when you need a *known pixel size* or *broad compatibility*:
  - Favicons / app icons
  - Social preview cards (Open Graph / Twitter)
  - Email signatures
  - Docs/PDF exports, presentations, “print-ish” outputs
- ❌ Don’t “hand-edit” raster exports (no mystery Photoshop tweaks). If it’s wrong, fix the **source** and re-export.

> **KFM standard vibe:** no mystery artifacts, no black boxes — assets should be reproducible, traceable, and consistent. 🧾✨

---

## 🗂️ Folder context (expected layout)

```text
🌐 web/
└── 🧰 assets/
    └── 🪪 logos/
        └── 🟦 kfm/
            ├── 🧩 raster/   ← you are here
            └── 🧬 vector/   (source-of-truth; SVG/AI/etc.)
```

---

## 🧱 Naming convention (contract)

Use **kebab-case**, keep names stable, and encode meaning in the filename.

### ✅ Recommended pattern

```text
kfm-<lockup>-<style>-<size>.png
kfm-<lockup>-<style>-<size>@2x.png    (optional retina)
```

### 🔤 Allowed values

**`<lockup>`** (what it is)
- `mark` (icon only)
- `wordmark` (text only)
- `lockup-horizontal` (icon + text horizontal)
- `lockup-stacked` (icon + text stacked)

**`<style>`** (how it renders)
- `color` (full-color brand)
- `mono-black` (one-color dark)
- `mono-white` (one-color light / inverted)

**`<size>`** (pixels)
- Use the **longest edge** in px: `16`, `32`, `48`, `64`, `128`, `256`, `512`, `1024`

### 🧪 Examples

- `kfm-mark-color-32.png`
- `kfm-mark-mono-white-128.png`
- `kfm-lockup-horizontal-color-512.png`
- `kfm-wordmark-mono-black-256@2x.png`

---

## 📐 Export specs (quality bar)

### 🎯 Visual requirements
- **Transparent background** (alpha) unless a *specific* background variant is required.
- **Consistent safe-area padding** (avoid cropping/bleeding).
- **No blur**: export from vector at exact integer pixel sizes.
- **No “halo” artifacts**: validate on both light + dark backgrounds.

### 🎨 Color requirements
- Export in **sRGB** (web-safe).
- Avoid CMYK or untagged color profiles for web assets.
- If you must ship both light/dark variants, do it explicitly via `mono-black` / `mono-white`.

### 🗜️ Performance requirements
- Optimize PNGs (lossless) before committing.
- Keep small assets (≤ 256px) especially tight (icons add up fast).

---

## 🧰 How to use (web UI)

### ✅ HTML (with `srcset`)
```html
<img
  src="/assets/logos/kfm/raster/kfm-mark-color-64.png"
  srcset="
    /assets/logos/kfm/raster/kfm-mark-color-64.png 1x,
    /assets/logos/kfm/raster/kfm-mark-color-64@2x.png 2x
  "
  width="64"
  height="64"
  alt="Kansas Frontier Matrix (KFM) logo"
/>
```

### ✅ CSS background (when you need it)
```css
.kfmMark {
  width: 32px;
  height: 32px;
  background: url("/assets/logos/kfm/raster/kfm-mark-color-32.png") center/contain no-repeat;
}
```

### ✅ React / bundlers (import example)
```js
import kfmMark32 from "./kfm-mark-color-32.png";

export function BrandMark() {
  return <img src={kfmMark32} width={32} height={32} alt="KFM" />;
}
```

---

## 🔁 Regenerating raster exports (source ➜ PNG)

**Source-of-truth should live in `../vector/`.** When updating the logo:

1. ✏️ Update the vector master (SVG/AI/whatever the repo uses)
2. 🖨️ Export the full size matrix (see below)
3. 🗜️ Optimize PNGs
4. 🧾 Update manifest + README (this file)
5. ✅ Verify in light/dark UI + small sizes (16–64px)

### 🧪 Suggested size matrix
- **Marks (icons):** 16, 32, 48, 64, 128, 256  
- **Lockups / wordmarks:** 128, 256, 512, 1024

### 🛠️ Example export commands (choose your tool)

#### Option A: Inkscape CLI (common + deterministic)
```bash
# example: export 512px wide PNG from SVG
inkscape ../vector/kfm-mark.svg \
  --export-type=png \
  --export-width=512 \
  --export-filename=kfm-mark-color-512.png
```

#### Option B: Node-based pipeline (recommended for teams)
Create a tiny script using `sharp` (or similar) so exports are:
- deterministic
- reviewable
- repeatable in CI

---

## 🧾 Provenance + governance (yes, even for logos)

KFM is built around **traceability + reproducibility** — that mindset applies here too.

### ✅ Recommended: add a tiny manifest
Add `manifest.json` (or `manifest.yml`) in this folder to document:
- vector source file path
- export tool + command
- sizes/variants exported
- license/trademark note

Example:
```json
{
  "brand": "KFM",
  "source": "../vector/kfm-logo.svg",
  "exports": [
    { "file": "kfm-mark-color-32.png", "px": 32, "bg": "transparent" },
    { "file": "kfm-mark-color-64.png", "px": 64, "bg": "transparent" }
  ]
}
```

### 🛡️ Licensing / trademark
- Treat these as **brand assets**.
- Don’t mix third‑party logos into this folder.
- If any font or external element is introduced in the source, **document the license** alongside it.

---

## ✅ PR checklist (for any change in this folder)

- [ ] Updated vector source (or confirmed unchanged)
- [ ] Exported correct sizes + variants
- [ ] PNGs optimized (lossless)
- [ ] Checked on light + dark backgrounds
- [ ] Checked at 16/32/64px for clarity
- [ ] Updated `manifest.*` (if present)
- [ ] Updated this `README.md`

---

## 🔗 Related

- `web/` → frontend UI
- `web/assets/` → static assets
- `web/assets/logos/kfm/vector/` → source-of-truth (preferred)
- `docs/` → governed documentation + standards

🧠 If you’re unsure whether raster is needed, default to **SVG** and only add PNG when there’s a real constraint.