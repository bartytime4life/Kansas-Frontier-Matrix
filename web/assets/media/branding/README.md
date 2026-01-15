---
title: "KFM Branding Assets"
status: "active"
version: "v0.1.0"
last_updated: "2026-01-15"
doc_kind: "Asset README"
path: "web/assets/media/branding/README.md"
---

# 🧭 KFM Branding Assets (Web)

![scope](https://img.shields.io/badge/scope-web%2Fassets%2Fmedia%2Fbranding-informational)
![usage](https://img.shields.io/badge/usage-web%20ui%20%2F%20maps%20%2F%20share%20cards-blue)
![principle](https://img.shields.io/badge/principle-provenance--first-success)

Welcome to the **Kansas Frontier Matrix (KFM)** branding folder 🌾🗺️  
This directory is the **single source of truth** for the project’s visual identity assets used in the web UI (React), map experiences (MapLibre/Cesium), and share/export surfaces.

> ✨ Brand idea in one sentence: **a trustworthy “living atlas” vibe** — clean, research-friendly, and transparently sourced.

---

## 🔗 Quick links

- [📦 What’s inside](#-whats-inside)
- [🧱 Folder layout](#-folder-layout)
- [🧩 Naming conventions](#-naming-conventions)
- [🖥️ How to use in the web app](#️-how-to-use-in-the-web-app)
- [🗺️ Map watermark guidance](#️-map-watermark-guidance)
- [🧪 Export + optimization](#-export--optimization)
- [♿ Accessibility](#-accessibility)
- [⚖️ Licensing + “do not imply endorsement”](#️-licensing--do-not-imply-endorsement)
- [🧰 Adding or updating assets](#-adding-or-updating-assets)

---

## 📦 What’s inside

This folder should contain (or will contain) assets like:

- 🪪 **Logos** (primary mark, wordmark, mono variants)
- 🧷 **Icons** (app icon, favicon set)
- 🧾 **Map watermark** variants (small, legible, non-intrusive)
- 🧵 **Social/share images** (OpenGraph / Twitter)
- 🧩 Optional UI glyphs tied to KFM concepts (e.g., “source”, “verified”, “advisory AI”)

---

## 🧱 Folder layout

> ✅ Keep the structure boring and predictable. Branding is infrastructure.

Recommended structure (adjust to match what actually exists — but try to keep names stable):

```text
📁 web/
  📁 assets/
    📁 media/
      📁 branding/
        📄 README.md
        📁 logo/
          🖼️ kfm-logo.svg
          🖼️ kfm-logo.png
          🖼️ kfm-wordmark.svg
          🖼️ kfm-wordmark.png
          🖼️ kfm-mark.svg
          🖼️ kfm-mark.png
          🖼️ kfm-logo-mono.svg
        📁 favicon/
          🧷 favicon.ico
          🧷 favicon-16.png
          🧷 favicon-32.png
          🧷 apple-touch-icon.png
          🧷 site.webmanifest
        📁 social/
          🖼️ og-default.png
          🖼️ og-story.png
        📁 watermark/
          🖼️ kfm-watermark.svg
          🖼️ kfm-watermark.png
        📁 source/
          🎨 kfm-logo.source.svg   (optional: “authoritative” editable source)
          📄 LICENSES.md           (optional: any asset-specific licensing notes)
```

---

## 🧩 Naming conventions

Use **kebab-case** and a consistent prefix:

- ✅ `kfm-…` prefix for project-owned marks  
- ✅ theme suffixes: `-light`, `-dark`, `-mono`  
- ✅ size suffixes for raster: `-16`, `-32`, `-64`, `-256`, etc.

Examples:

- `kfm-logo.svg`
- `kfm-logo-mono.svg`
- `kfm-mark-256.png`
- `og-default-1200x630.png`

> 💡 Tip: prefer **SVG** for logos/marks and only rasterize where necessary.

---

## 🖥️ How to use in the web app

### ✅ React (TypeScript) example

```tsx
import kfmLogoUrl from "./logo/kfm-logo.svg";

export function KfmLogo() {
  return (
    <img
      src={kfmLogoUrl}
      alt="Kansas Frontier Matrix"
      width={160}
      height={48}
      loading="eager"
    />
  );
}
```

### ✅ CSS background example

```css
.kfm-brand-mark {
  background-image: url("./logo/kfm-mark.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
}
```

> 🧠 Keep brand assets referenced via the build system when possible (so hashing/caching works automatically).

---

## 🗺️ Map watermark guidance

KFM map views are information-dense — the watermark must be **present but not intrusive** 🧩

**Placement (recommended):**
- Bottom-left or bottom-right
- Must not overlap:
  - attribution text
  - scale bar
  - time slider / playback controls
  - layer panel affordances

**Behavior (recommended):**
- Fade slightly when user is actively panning/dragging
- Increase contrast subtly on busy basemaps (use mono variant if needed)
- Keep click-target reasonable (minimum ~32px height on touch screens)

### Example overlay (framework-agnostic)

```html
<a class="kfm-watermark" href="/" aria-label="Kansas Frontier Matrix home">
  <img src="./watermark/kfm-watermark.svg" alt="Kansas Frontier Matrix" />
</a>
```

```css
.kfm-watermark {
  position: absolute;
  z-index: 5;
  bottom: 12px;
  right: 12px;
  opacity: 0.85;
  text-decoration: none;
}

.kfm-watermark img {
  height: 28px;
  width: auto;
  display: block;
}
```

---

## 🧪 Export + optimization

### Vector (SVG) ✅
- Include a proper `viewBox`
- Prefer shapes over embedded raster
- Avoid unnecessary groups and transforms
- Keep strokes consistent (especially for small marks)

### Raster (PNG) ✅
- Export at common UI sizes (at least 1x and 2x)
- Use **transparent background** unless the design requires a plate

### Optional: optimization tooling
If the repo uses Node tooling, consider:
- `svgo` for SVG optimization
- `sharp` for generating PNG variants

---

## ♿ Accessibility

Branding is part of UX. Minimum baseline:

- ✅ Always provide meaningful `alt` text (or `alt=""` for purely decorative repeats)
- ✅ Ensure sufficient contrast when the logo sits on imagery or map tiles
- ✅ Do not use color alone to communicate meaning (if the mark is used as a status indicator)

---

## ⚖️ Licensing + “do not imply endorsement”

- 🧾 **Do not** use KFM marks in a way that implies endorsement or official partnership without permission.
- 🧩 If adding any third-party marks (agencies, archives, universities), **confirm their usage terms** and document them.

> 🔍 If you’re unsure: treat it like data provenance — record the source, terms, and intended use.

---

## 🧰 Adding or updating assets

### ✅ PR checklist
- [ ] Add/edit the **source** asset (SVG preferred)
- [ ] Export required variants (mono/light/dark where needed)
- [ ] Optimize files (SVG cleanup, PNG compression)
- [ ] Update this README if filenames or structure changed
- [ ] Confirm licensing notes for any external elements

### 🧯 “Please don’t” list
- ❌ Don’t embed text in SVG that depends on a local font (unless outlined/embedded)
- ❌ Don’t upload massive PNGs “because it’s just an asset folder”
- ❌ Don’t rename canonical files without updating all references

---

## 🧭 Brand vibe cheatsheet (tiny but useful)

- **Tone:** confident, calm, research-friendly 📚
- **Visual personality:** modern atlas + transparent sourcing 🗺️
- **Default:** less decoration, more clarity ✅

---

## 🧾 Asset inventory (fill in as assets land)

| Asset | Path | Format | Used for | Notes |
|---|---|---:|---|---|
| Primary logo | `logo/kfm-logo.svg` | SVG | Header / splash | Preferred |
| Wordmark | `logo/kfm-wordmark.svg` | SVG | Footer / docs | Wide layout |
| Mark (icon) | `logo/kfm-mark.svg` | SVG | App icon / small UI | Mono variant recommended |
| Watermark | `watermark/kfm-watermark.svg` | SVG | Map UI | Keep subtle |
| OG default | `social/og-default.png` | PNG | Sharing | 1200×630 |

---

## 🧬 How this supports KFM (why branding matters here)

KFM isn’t just “a map app” — it’s a platform where users should feel they can **trust what they see**.  
Branding should reinforce that trust through consistency, legibility, and clarity.

✅ If the UI shows citations, sources, or advisory AI outputs, the visual language must help users distinguish **data** vs **interpretation** vs **generated summaries**.

---
