<!--
📍 Location: web/src/assets/images/README.md
🧭 Scope: Image assets shipped with the React web UI (NOT the data lake / GIS rasters)
-->

# 🖼️ `web/src/assets/images` — Image Asset Guide

![Provenance First](https://img.shields.io/badge/provenance-evidence--first-2ea44f)
![Web Performance](https://img.shields.io/badge/web-performance--minded-blue)
![Accessibility](https://img.shields.io/badge/a11y-alt--text%20%26%20contrast-important)
![GIS UI](https://img.shields.io/badge/maps-MapLibre%20%2B%20Cesium-informational)

This folder is the **UI image library** for the Kansas Frontier Matrix (KFM) web app.  
Use it for **icons, illustrations, UI imagery, story panels, and small map UI sprites** that ship with the frontend bundle.

> [!IMPORTANT]
> **Big geospatial assets do not belong here.**  
> Cloud-Optimized GeoTIFFs, PMTiles, tilesets, PDFs, etc. should live in the **data lake / object storage** and be served via the governed API/CDN, not committed into the web bundle. 🗃️🌐

---

## 📚 Table of Contents
- [✅ What belongs here](#-what-belongs-here)
- [🚫 What does NOT belong here](#-what-does-not-belong-here)
- [🗂️ Recommended folder layout](#️-recommended-folder-layout)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🧩 Formats guide](#-formats-guide)
- [⚡ Optimization rules](#-optimization-rules)
- [🧾 Provenance + licensing](#-provenance--licensing)
- [🧑‍💻 Using images in React](#-using-images-in-react)
- [🗺️ Map UI icons](#️-map-ui-icons)
- [♿ Accessibility rules](#-accessibility-rules)
- [✅ Contribution checklist](#-contribution-checklist)
- [🔗 References](#-references)

---

## ✅ What belongs here
Typical UI-safe assets:

- 🏷️ **Branding**: logos, wordmarks, lockups (prefer SVG)
- 🧭 **UI icons**: buttons, controls, menu icons (prefer SVG)
- 🧩 **Illustrations**: onboarding, empty states, banners (SVG or optimized raster)
- 📖 **Story/scene images**: narrative panels used in the web UI (optimized WebP/PNG)
- 🗺️ **Map UI**: pins, markers, legend symbols, layer icons (small + crisp)

---

## 🚫 What does NOT belong here
Keep the frontend bundle lean. Don’t commit:

- 🛰️ Large raster imagery (e.g., satellite scenes, aerial mosaics)
- 🧱 Tilesets / PMTiles / MBTiles / large sprite sheets
- 📦 Huge photos “just in case”
- 🧾 PDFs / scanned documents meant for citation (serve these via backend/object storage)
- 🔒 Anything with unclear or incompatible licensing

> [!TIP]
> If the asset is “data” (something we cite / audit / swap independently), it belongs in the **pipeline + storage** layers—not in the UI repo.

---

## 🗂️ Recommended folder layout

Use folders to keep imports predictable and reviews fast:

```text
📁 web/src/assets/images/
├─ 📁 branding/                 # logos, wordmarks, favicons (SVG preferred)
├─ 📁 icons/                    # UI icons (SVG, monochrome where possible)
│  ├─ 📁 ui/                    # buttons, nav, controls
│  └─ 📁 map/                   # pins, markers, legends (MapLibre/Cesium)
├─ 📁 illustrations/            # onboarding, empty states
├─ 📁 story/                    # narrative panels / story mode imagery
├─ 📁 placeholders/             # skeletons, fallbacks, “no image” tiles
└─ 🧾 images.manifest.yml        # REQUIRED for non-original assets
```

> [!NOTE]
> If you add a new category (e.g., `partners/`), add it intentionally and document it here.

---

## 🏷️ Naming conventions

### ✅ Do
- Use **kebab-case**: `dust-bowl-hero.webp`
- Prefix by domain when helpful: `map-pin-railroad.svg`, `ui-btn-close.svg`
- Include size suffix *only* when multiple sizes exist: `legend-128.png`, `legend-256.png`
- Use `@2x` / `@3x` only for raster assets that truly need it: `marker@2x.png`

### 🚫 Don’t
- No spaces: `my icon final.png` ❌
- No “final-final-v3.png” ❌
- No ambiguous names: `image1.png` ❌

---

## 🧩 Formats guide

| Format | Best for | Avoid when | Notes |
|---|---|---|---|
| **SVG** ✅ | icons, logos, line art | photo-like imagery | Prefer `fill="currentColor"` for theming 🎨 |
| **WebP** ✅ | photos, story panels | legacy-only environments | Great size/quality tradeoff ⚡ |
| **PNG** | transparency, crisp UI bitmaps | large photos | Use when SVG can’t work (e.g., complex raster UI) |
| **JPG/JPEG** | photos (fallback) | transparency | Use only if WebP isn’t viable |
| **GIF** ⚠️ | tiny simple animations | everything else | Prefer modern alternatives (video/Lottie) |

---

## ⚡ Optimization rules

### 🎯 Target budgets (guidelines)
- **Icons (SVG):** ideally **< 5–10 KB**
- **UI illustrations:** **< 150 KB** (SVG preferred)
- **Story panels:** **< 300–600 KB** depending on usage
- **Anything > 1 MB:** pause and reconsider ❗

### 🧼 SVG hygiene
- Remove editor metadata
- Prefer paths that render cleanly at **16–24px** (icons)
- Keep strokes consistent (don’t mix 1px + 2.5px randomly)

### 🗜️ Raster hygiene
- Crop to the smallest useful bounds
- Don’t bake text into images unless it’s part of an illustration (text should remain selectable & localizable)
- Export at the **actual display size** (avoid “4K just because”)

> [!WARNING]
> Over-sized images quietly tax **LCP**, **bundle size**, and **mobile users**. Optimize early. 📉📱

---

## 🧾 Provenance + licensing

KFM is evidence-first (“the map behind the map”). That applies to UI assets too. ✅  
If an image is **not fully original**, it must be trackable.

### ✅ Required: `images.manifest.yml`
Add an entry for:
- stock photos
- icons from libraries
- partner logos
- any third-party illustrations
- screenshots of external content

Example:

```yaml
# images.manifest.yml
assets:
  - id: "story-dust-bowl-hero"
    file: "story/dust-bowl-hero.webp"
    type: "photo"
    source:
      title: "Example Archive Item Title"
      url: "https://example.org/item/123"
    license:
      spdx: "CC-BY-4.0"
      attribution: "Author Name / Archive"
    notes: "Used on Story Mode intro panel"
```

> [!IMPORTANT]
> If we can’t identify the **source + license**, we **don’t ship it**. 🛑

---

## 🧑‍💻 Using images in React

### Import as a module (recommended)
This lets the bundler hash and optimize delivery:

```tsx
import hero from "@/assets/images/story/dust-bowl-hero.webp";

export function StoryHero() {
  return <img src={hero} alt="Dust storm over western Kansas farmland" loading="lazy" />;
}
```

### Use `<picture>` for responsive sources (recommended for large visuals)
```tsx
import heroWebp from "@/assets/images/story/dust-bowl-hero.webp";
import heroJpg from "@/assets/images/story/dust-bowl-hero.jpg";

export function StoryHero() {
  return (
    <picture>
      <source srcSet={heroWebp} type="image/webp" />
      <img src={heroJpg} alt="Dust storm over western Kansas farmland" loading="lazy" />
    </picture>
  );
}
```

---

## 🗺️ Map UI icons

KFM’s web UI includes 2D/3D mapping (e.g., MapLibre + Cesium). Map icons have special constraints:

### Rules of thumb
- Prefer **SVG** for legend/layer icons used in UI panels
- For in-map markers that require raster sprites:
  - provide **1x and 2x** versions when needed
  - keep edges crisp (avoid blurs)
  - test against multiple basemaps (light/dark/satellite) 🌗🛰️

### Visual consistency checklist
- ✅ consistent silhouette style (rounded vs sharp)
- ✅ consistent anchor point (pin tip hits the exact location)
- ✅ readable at small zoom levels
- ✅ does not rely on color alone to convey meaning

---

## ♿ Accessibility rules

- Every meaningful `<img>` must have **useful `alt` text**
- Decorative-only images should use empty alt: `alt=""`
- Avoid embedding critical text inside images (hurts screen readers + localization)
- Ensure adequate contrast if imagery is used as a UI background

> [!TIP]
> If the image conveys data, ask: “Can this be a semantic UI element instead?” (icons + labels often beat a bitmap)

---

## ✅ Contribution checklist

Before committing new images:

- [ ] File placed in the correct subfolder 🗂️
- [ ] Name follows kebab-case 🏷️
- [ ] Format is appropriate (SVG/WebP first) 🧩
- [ ] Optimized size (no accidental megabytes) ⚡
- [ ] **`images.manifest.yml` updated** if non-original 🧾
- [ ] Accessibility considered (alt text strategy) ♿
- [ ] Map icons tested at real sizes (if applicable) 🗺️

---

## 🔗 References

These project references informed the standards in this README:

- **KFM system principles (provenance, governed “truth path,” API-first assets):**  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- **Web image formats + compression + graphics considerations:**  [oai_citation:1‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- **HTML/CSS media usage patterns (images, backgrounds, responsive structure):**  [oai_citation:2‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- **Web/Node ecosystem context (serving, modular frontend/backend concerns):**  [oai_citation:3‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
- **Additional project material:**  [oai_citation:4‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)  