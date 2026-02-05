# 🎨 Branding Assets — Kansas Frontier Matrix (KFM)

![Branding](https://img.shields.io/badge/Assets-Branding-2b6cb0)
![SVG-first](https://img.shields.io/badge/Preferred-SVG%20First-0ea5e9)
![A11y](https://img.shields.io/badge/Standard-Accessible%20by%20Default-22c55e)
![Governed](https://img.shields.io/badge/Approach-Provenance%20%2B%20Governance-8b5cf6)

> [!NOTE]
> This folder is the **single source of truth** for KFM brand visuals used in the web UI: logos, wordmarks, marks, social previews, and app icons.

---

## 🧭 Quick Links

- ⬅️ Project root: `../../../../../README.md`
- 🕸️ Web app root: `../../../../`  
- 🧩 If you’re looking for UI icons (buttons, menus, etc.), this is **not** that folder ✅

---

## ✅ What belongs in `branding/`

**Put these here:**
- 🪪 **Logo / mark / wordmark** (prefer `*.svg` as source-of-truth)
- 🌗 **Theme variants** (light/dark, mono)
- 📱 **App icons** (PWA icons, favicons, etc.)
- 🧵 **Social/OG images** (OpenGraph, Twitter/X cards, share previews)
- 📰 **Press kit exports** (only if intentionally published)

**Keep these out:**
- 🧰 Generic UI icons (belongs in a `icons/` or `ui/` asset path)
- 🗺️ Map tiles, basemaps, legends, symbology sets (belongs in mapping/cartography assets)
- 🧪 Test snapshots (belongs in test folders)
- 🗃️ Random “working files” (PSDs, AI files) unless explicitly required & documented

---

## 🗂️ Recommended structure (if/when this folder grows)

```text
web/src/assets/images/branding/
├─ README.md
├─ manifest.branding.json        # 🧾 catalog of brand assets (recommended)
├─ logos/
│  ├─ kfm-logo.svg
│  ├─ kfm-logo-dark.svg
│  └─ kfm-logo-mono.svg
├─ wordmarks/
│  ├─ kfm-wordmark.svg
│  └─ kfm-wordmark-stacked.svg
├─ marks/
│  ├─ kfm-mark.svg               # favicon-ish mark
│  └─ kfm-mark-mono.svg
├─ app-icons/
│  ├─ icon-192.png
│  ├─ icon-512.png
│  └─ maskable-512.png
└─ social/
   ├─ og-default.png
   └─ og-dark.png
```

> [!TIP]
> Even if you don’t add subfolders yet, **start with the naming conventions** below so scaling later is painless.

---

## 🏷️ Naming conventions

### 🎯 File naming rules
Use **lowercase**, **kebab-case**, and include **variant suffixes**:

- `kfm-logo.svg` (default / primary)
- `kfm-logo-dark.svg` (optimized for dark backgrounds)
- `kfm-logo-light.svg` (optimized for light backgrounds)
- `kfm-logo-mono.svg` (single-color)
- `kfm-wordmark-stacked.svg` (layout variant)
- `kfm-mark.svg` (icon/mark only)

### 🌈 Color + theme variants
Use suffixes that describe **usage**, not implementation:
- ✅ `-dark`, `-light`, `-mono`, `-inverted`
- ❌ `-blue`, `-red` (colors change; meaning should not)

---

## 🌗 Theme & color handling (KFM-style)

> [!IMPORTANT]
> KFM theming should be easy to swap globally. Avoid “hard-coding” brand colors everywhere.
> If the web UI uses design tokens/CSS variables, branding should play nicely with that.

### Preferred SVG patterns
- **Vector-first**: keep the “source of truth” in `*.svg`
- If the mark must follow theme colors:
  - prefer `fill="currentColor"` (so CSS can control it)
  - or export **two explicit variants** (`-light`, `-dark`) if needed for fidelity

### Avoid
- embedding huge raster textures inside SVG
- exporting 15 slightly different “almost-the-same” logos 🙃

---

## ♿ Accessibility requirements (non-negotiable)

### Alt text rules
- Informational brand images: include meaningful `alt`
- Purely decorative: use `alt=""` (or use CSS backgrounds where appropriate)

### Layout stability
- When using raster images (PNG/JPG), provide **intrinsic sizing** (`width`/`height`) or CSS sizing to prevent layout shift.

> [!TIP]
> If an image contains no meaningful content beyond decoration, prefer CSS background usage instead of `<img>`.

---

## 🧰 Formats & when to use them

| Format | Use it for | Notes |
|---|---|---|
| `SVG` ✅ | Logos, wordmarks, marks | Best for crisp scaling & theme flexibility |
| `PNG` ✅ | Icons with transparency, UI-ish brand patterns | Great for transparency / low color counts |
| `JPG` ✅ | Photographic social images | Smaller files for photos; no transparency |
| `GIF` ⚠️ | Rare: tiny animations | Use sparingly; consider modern alternatives when possible |

---

## 🧪 Optimization checklist (before committing)

### SVG
- ✅ Remove editor metadata (Sketch/Illustrator junk)
- ✅ Run an optimizer (e.g., `svgo`) if available in tooling
- ✅ Keep paths tidy; avoid hidden layers

### PNG/JPG
- ✅ Compress (don’t overcompress)
- ✅ Keep file sizes small for the web
- ✅ Export at the smallest size that still looks sharp

> [!WARNING]
> Overcompression can make logos look “crunchy” and reduce trust. Branding must be crisp.

---

## 🧾 Provenance & governance (KFM mindset)

Branding is still an artifact. Treat it like one:

### Add a simple manifest (recommended)
Create/update `manifest.branding.json` (or similar) with:
- `name`, `type` (logo/wordmark/icon/social)
- `variants` (light/dark/mono)
- `intended_use` (header, footer, favicon, social preview)
- `source` (who created it / where it came from)
- `license` / `usage_rights` (especially if external)
- `checksum` (optional, but great for traceability)

### Don’t commit questionable assets
- third-party logos without permission
- stock imagery without the license recorded
- “borrowed” icons from random sites 😬

---

## 🧩 Usage examples

### React (typical)
```tsx
import kfmLogo from "@/assets/images/branding/logos/kfm-logo.svg";

export function BrandLockup() {
  return (
    <img
      src={kfmLogo}
      alt="Kansas Frontier Matrix"
      width={160}
      height={40}
      loading="eager"
      decoding="async"
    />
  );
}
```

### CSS background (decorative)
```css
.hero {
  background-image: url("./social/og-default.png");
  background-size: cover;
  background-position: center;
}
```

> [!NOTE]
> If you use CSS backgrounds for meaningful content, make sure the information exists elsewhere in accessible text.

---

## 🔁 How to add / update branding assets

1. 🧠 Decide the “source of truth” asset (usually SVG)
2. 🏷️ Name it using the conventions above
3. 🌗 Export required variants (light/dark/mono) if needed
4. 🧰 Optimize the file(s)
5. ♿ Validate accessibility usage (alt, sizing, contrast context)
6. 🧾 Update the manifest (if present)
7. 🧪 Verify in the UI (header, footer, auth screens, share previews)

---

## 🧷 Asset catalog (fill this in as we grow)

| Asset | Variants | Primary usage | Notes |
|---|---|---|---|
| `kfm-logo.svg` | `dark`, `mono` | Header / nav | SVG source-of-truth |
| `kfm-mark.svg` | `mono` | Favicon/app icon base | Keep simple shapes |
| `og-default.png` | `dark` | Social preview | 1200×630 typical |

---

## 📌 House rules (tl;dr)

- ✅ SVG first
- ✅ Theme-friendly (tokens/variables/variants)
- ✅ Accessible by default
- ✅ Optimized + tidy
- ✅ Provenance recorded

🧭 If it can’t be explained, reused, and traced… it doesn’t belong here. ✅
