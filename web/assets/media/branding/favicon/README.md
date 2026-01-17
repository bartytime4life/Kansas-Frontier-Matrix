# 🌾 Kansas Frontier Matrix (KFM) — Favicon Kit 🧩

![KFM](https://img.shields.io/badge/KFM-branding-0b7285)
![Web UI](https://img.shields.io/badge/web-assets-1f6feb)
![Provenance--first](https://img.shields.io/badge/principle-provenance--first-2ea043)

Welcome to `web/assets/media/branding/favicon/` — the **single source folder** for the Web UI’s favicon + app-icon outputs.

KFM’s UI aims to be *auditable* and *transparent* — this folder follows the same spirit: **keep a clear “source of truth”**, generate exports deterministically, and document exactly what belongs here. 🧾✨

---

## 🧭 What belongs in this folder?

This folder should contain:

- ✅ **A source-of-truth vector** (recommended): `kfm-favicon.source.svg`
- ✅ **Generated browser icons** (PNG + ICO)
- ✅ **PWA / install assets** (`site.webmanifest`, Android sizes, Apple touch icon)
- ✅ (Optional) **Safari pinned-tab** vector

> **Rule of thumb:** edit the **source SVG**, regenerate the exports, commit everything together.

---

## 📦 Folder layout (expected contract)

```text
web/
└─ assets/
   └─ media/
      └─ branding/
         └─ favicon/
            ├─ README.md
            ├─ kfm-favicon.source.svg          # ✅ source-of-truth (recommended)
            ├─ favicon.ico                     # ✅ multi-size ICO (16/32/48...)
            ├─ favicon-16x16.png               # ✅ legacy + UI tabs
            ├─ favicon-32x32.png               # ✅ modern browsers
            ├─ apple-touch-icon.png            # ✅ iOS home screen
            ├─ android-chrome-192x192.png      # ✅ PWA
            ├─ android-chrome-512x512.png      # ✅ PWA
            ├─ site.webmanifest                # ✅ PWA metadata
            ├─ safari-pinned-tab.svg           # ➕ optional (monochrome)
            └─ browserconfig.xml               # ➕ optional (Windows tiles)
```

If your current folder differs, that’s OK — but try to converge on this contract so every environment (dev/preview/prod) behaves consistently. 🔁

---

## 🎯 Design intent (micro-brand rules)

Favicons are tiny — the “brand” must survive at **16×16** without becoming noise.

### ✅ Do
- Use a **single, bold silhouette** (think: Kansas outline, pin, grid/matrix mark)
- Keep **strong contrast**
- Prefer **flat shapes** over thin strokes
- Keep details within a **safe margin** (avoid edge clipping)

### ❌ Don’t
- Don’t use text/letters as the primary mark (usually unreadable at 16×16)
- Don’t rely on gradients for meaning
- Don’t add small internal linework that disappears when downscaled

---

## 📐 Export specs (recommended)

| File | Size | Purpose |
|------|------|---------|
| `favicon.ico` | multi-size (16/32/48…) | Legacy + automatic browser pickup |
| `favicon-16x16.png` | 16×16 | Tabs, old UI, fallbacks |
| `favicon-32x32.png` | 32×32 | Modern browsers |
| `apple-touch-icon.png` | 180×180 | iOS home screen |
| `android-chrome-192x192.png` | 192×192 | PWA icon |
| `android-chrome-512x512.png` | 512×512 | PWA icon (high-res) |
| `site.webmanifest` | — | PWA install metadata |
| `safari-pinned-tab.svg` | vector | Safari pinned tabs (monochrome) |
| `browserconfig.xml` | — | Windows tiles (optional) |

> If you only keep one “master” artboard: make it **square** (1:1), ideally designed at **512×512**.

---

## 🔗 Wiring it up (HTML `<head>` snippet)

Paths here assume `web/assets/` is served at `/assets/`.
Adjust if your asset pipeline rewrites paths.

```html
<!-- Standard -->
<link rel="icon" type="image/png" sizes="32x32" href="/assets/media/branding/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/media/branding/favicon/favicon-16x16.png">
<link rel="shortcut icon" href="/assets/media/branding/favicon/favicon.ico">

<!-- iOS -->
<link rel="apple-touch-icon" href="/assets/media/branding/favicon/apple-touch-icon.png">

<!-- PWA -->
<link rel="manifest" href="/assets/media/branding/favicon/site.webmanifest">
<meta name="theme-color" content="#0b7285">
```

---

## 🛠️ Regenerating icons

This repo doesn’t assume one specific toolchain in this folder (yet). Pick the tool that fits your workflow, **but keep outputs deterministic**.

### ✅ Recommended workflow
1. Edit `kfm-favicon.source.svg` (or your equivalent source file)
2. Export the PNG sizes listed above
3. Build `favicon.ico` containing multiple sizes (at least 16 + 32)
4. Validate in browsers (see checklist below)
5. Commit **source + outputs** in the same PR

<details>
  <summary>🧪 Determinism tips (keep diffs clean)</summary>

- Export PNGs with consistent settings (no random metadata)
- Prefer “Export for Web” / “Optimize” to reduce file size
- If your tool adds timestamps, consider stripping metadata during export
- Keep the source SVG artboard size fixed (avoid accidental resizes)

</details>

---

## 🧪 Testing checklist (favicons are cached aggressively 😅)

Browsers often **cache favicons stubbornly**. When testing a change:

- ✅ Hard refresh
- ✅ Try a private/incognito window
- ✅ Clear site data/cache
- ✅ Verify on at least one Chromium browser + Firefox + Safari (if possible)
- ✅ Confirm the correct icon appears in:
  - tab
  - bookmarks
  - PWA install prompt (if used)
  - iOS home-screen (if used)

> Pro tip: if caching is a recurring pain, consider **renaming** outputs (or adding a cache-busting query string via your build pipeline).

---

## ✅ PR checklist (for favicon changes)

- [ ] Source-of-truth file updated (`*.source.svg` or equivalent)
- [ ] All required outputs regenerated (PNG + ICO + manifest if applicable)
- [ ] No extra “random” exports left behind (clean folder)
- [ ] Verified rendering at 16×16 and 32×32
- [ ] Confirmed browser caching behavior (incognito test)

---

## 🧾 Licensing & attribution

Only commit favicon assets that KFM has the right to ship:
- Use original artwork or properly licensed components
- Avoid copying marks from third parties unless explicitly allowed
- If derived from an external source, document it in the PR description (and ideally in a `SOURCES.md` nearby)

---

## 🔁 Rebrands / forks (Frontier Matrix family)

KFM is designed to be adaptable and forkable (e.g., other regions adopting the “Frontier Matrix” concept). 🌎  
If you’re cloning the project for another state/region, **this folder is your first stop** for swapping the UI identity:

- Replace the source favicon SVG
- Regenerate exports
- Update any `theme-color` or manifest metadata

---

💡 If you add automation later, consider a repo-level script (e.g. `scripts/generate-favicons.*`) and wire it into CI so every build can verify the favicon contract automatically.
