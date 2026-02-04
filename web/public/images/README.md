# 🖼️ `web/public/images` — Public Image Assets

![Assets](https://img.shields.io/badge/assets-images-blue)
![Performance](https://img.shields.io/badge/perf-optimized-success)
![Accessibility](https://img.shields.io/badge/a11y-alt%20text%20%26%20captions-important)
![Provenance](https://img.shields.io/badge/provenance-required-informational)

> **What lives here?** Static images that are served **as-is** by the web app (public assets).  
> **What doesn’t?** Large geospatial rasters/tiles/data artifacts (those belong in the data/tile pipeline, not `public/`). 🧭

---

## 🔎 Quick links

- ⬆️ Up one level: [`../`](../)
- ⬆️ Up to `web/`: [`../../`](../../)

---

## ✅ Golden Rules

### 1) “No Source, No Asset” 🧾
If an image is not **originally created by us**, it must have **provenance + licensing** documented (see **Provenance & Licensing** below).  
This mirrors KFM’s evidence-first philosophy: assets shown to users must remain **traceable** (the “map behind the map”). 🗺️

### 2) Optimize before commit ⚡
If it’s bigger than it needs to be, it slows everything down:
- slower page load
- slower map UI
- higher bandwidth for mobile users

### 3) Accessibility isn’t optional ♿
Every meaningful image needs correct **alt text** and/or a **caption** (when it adds context).

### 4) Keep `public/` clean 🧹
Everything under `public/` is an “asset” the browser can request directly. That’s powerful… and easy to bloat. Treat this folder as production-critical.  
(Background: public assets are delivered to the browser as part of the app’s static surface.) [oai_citation:0‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

---

## 🧱 Recommended folder layout

> If your folder already differs, don’t panic—this is the **target** structure we should converge toward.

```text
web/
└─ public/
   └─ images/
      ├─ branding/        # logos, wordmarks, brand marks 🏷️
      ├─ icons/           # UI icons (prefer SVG) ✳️
      ├─ ui/              # UI illustrations, empty states, onboarding 🧩
      ├─ maps/            # map UI assets: legend images, swatches, overlays 🗺️
      ├─ sprites/         # sprite sheets (e.g., MapLibre sprite.png + sprite.json) 🧵
      ├─ screenshots/     # docs-only screenshots (prefer docs/images if possible) 📸
      └─ _meta/           # optional central attributions & licenses 📚
```

---

## 🧭 How to reference images in the app

Because these files live under `public/`, they should generally be reachable by URL path:

### HTML
```html
<img src="/images/branding/kfm-logo.svg" alt="Kansas Frontier Matrix logo">
```

### React (typical)
```tsx
export function BrandMark() {
  return (
    <img
      src="/images/branding/kfm-logo.svg"
      alt="Kansas Frontier Matrix logo"
      width={160}
      height={160}
      loading="lazy"
      decoding="async"
    />
  );
}
```

> ✅ Prefer explicit `width`/`height` to reduce layout shift (CLS).  
> ✅ Use `loading="lazy"` for below-the-fold images.  
> ✅ Use `decoding="async"` when reasonable.

---

## 🖼️ Formats: what to use (and when)

| Format | Best for | Avoid when | Notes |
|---|---|---|---|
| **SVG** ✨ | icons, logos, simple illustrations | photos, heavy gradients/filters | Keep SVGs clean: no embedded raster blobs, avoid unnecessary `<metadata>` |
| **PNG** 🧊 | transparency + pixel-perfect UI | photos (usually) | Use for crisp UI assets or when SVG isn’t viable |
| **WebP** 📦 | photos, screenshots, rich raster images | tiny icons | Great size/quality tradeoff; consider multiple sizes |
| **AVIF** 🏎️ | photos (best compression) | if tooling/support is a hassle | Optional “next step” if pipeline supports |
| **GIF** 🧨 | only tiny simple loops | almost everything else | Prefer MP4/WebM for animation (not typically stored here) |

---

## 📏 Naming conventions (keep it boring = keep it scalable)

### ✅ Do
- `kebab-case`
- include semantic meaning
- include variant tokens when needed: `-dark`, `-light`, `-mono`, `@2x`

Examples:
- `branding/kfm-logo.svg`
- `branding/kfm-wordmark-dark.svg`
- `icons/layer-toggle.svg`
- `maps/legend-drought-index.webp`
- `sprites/maplibre-sprite.png` + `maplibre-sprite@2x.png` + `maplibre-sprite.json`

### ❌ Don’t
- `IMG_1920.png`
- `final_final_REAL.png`
- spaces, mixed casing, or mystery abbreviations

---

## ⚡ Performance budgets (practical rules)

These are “red flags,” not rigid laws:

- **Icons (SVG):** keep as small as possible (often < 10 KB)
- **UI PNGs:** aim for < 100 KB
- **Photos / screenshots (WebP):** aim for < 300–600 KB depending on dimensions
- **Anything > 1 MB:** stop and ask “should this be a tile, not an image?” 🧠

### Caching 🔁
Static assets should be served with **strong caching** (e.g., far-future cache headers) so repeat visits are fast. [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

> Tip: If you must change an asset frequently, consider versioned filenames like `kfm-logo.v2.svg`.

---

## 🧰 Optimization playbook (recommended tools)

> Use whatever tools fit your workflow; these are reliable defaults.

### SVG
- Run SVGO:
```bash
npx svgo -f web/public/images --recursive
```

### PNG
- Strip metadata + optimize:
```bash
oxipng -o 4 -strip all web/public/images/**/*.png
```

### WebP
- Convert (example):
```bash
cwebp -q 82 input.png -o output.webp
```

### Strip EXIF / hidden metadata 🔒
- Especially important for photos and screenshots:
```bash
exiftool -all= -overwrite_original path/to/image.jpg
```

---

## ♿ Accessibility checklist

### Alt text rules
- **Informational image:** describe the meaning, not the pixels.
- **Decorative image:** use empty alt (`alt=""`) so screen readers skip it.
- **Complex diagrams/maps:** provide a short alt + a longer text explanation nearby (or link).

### Captions for context
When an image benefits from explanation, use semantic figure/caption patterns in docs/pages:
```html
<figure>
  <img src="/images/maps/legend-drought-index.webp" alt="Legend for drought index">
  <figcaption>Drought Index legend used in the 1930–1939 timeline view.</figcaption>
</figure>
```

---

## 🧾 Provenance & Licensing (MANDATORY for external assets)

KFM’s platform values traceability and governance—assets should follow the same discipline. ✅  
If you add an image from an outside source (archives, stock, agencies, community submissions), include a matching metadata file:

### ✅ Convention
For an asset:
- `maps/legend-drought-index.webp`

Add:
- `maps/legend-drought-index.meta.json`

### ✅ Minimal schema (example)
```json
{
  "title": "Drought Index legend",
  "description": "Legend image used in the web UI for drought index layer.",
  "created_by": "KFM Team",
  "created_at": "2026-02-04",
  "source": {
    "type": "internal",
    "name": "KFM",
    "url": null
  },
  "license": {
    "spdx": "MIT",
    "attribution": "Kansas Frontier Matrix contributors"
  },
  "modifications": [
    "exported",
    "optimized",
    "metadata stripped"
  ],
  "related": {
    "dataset_ids": ["ks_drought_index_1930s"],
    "story_ids": ["dust-bowl-overview"]
  }
}
```

### ✅ For third-party assets
Use:
- `source.url` (where you got it)
- `source.accessed_at`
- `license.spdx` (or a clear license string)
- `license.attribution` (exact wording required)

> If we don’t have license clarity, **don’t ship it**. 🚫

---

## 🗺️ Map UI specifics (MapLibre / Cesium)

KFM’s front-end map experience may include **MapLibre (2D)** and **Cesium (3D)**, which can require special asset handling (sprites, icons, etc.). [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### MapLibre sprites 🧵
If we use a MapLibre style that references `sprite`, keep the sprite assets together:

- `sprites/<name>.png`
- `sprites/<name>@2x.png`
- `sprites/<name>.json`

> Tip: keep sprite filenames stable—styles often reference them directly.

### Cesium UI icons 🌍
Cesium overlays and UI often benefit from:
- crisp SVG icons
- transparent PNG markers
- small textures (only when needed)

---

## 🔁 PR checklist (copy/paste)

- [ ] Asset is in the right folder (`branding/`, `icons/`, `maps/`, etc.)
- [ ] Filename follows conventions (`kebab-case`, meaningful, stable)
- [ ] Optimized (SVG/PNG/WebP) and metadata removed if needed
- [ ] Accessible usage planned (alt/caption or decorative)
- [ ] **If external:** added `*.meta.json` with source + license
- [ ] Verified in-browser (no broken paths, looks correct on dark/light backgrounds)
- [ ] Size budget makes sense (especially for map UI)

---

## 📚 References & project grounding

<details>
<summary>Why these rules exist (project sources)</summary>

- KFM system emphasizes evidence-first / provenance-first behavior and governed interfaces (informing our “No Source, No Asset” rule).  [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Web design guidance on choosing correct image formats + compression and avoiding misuse informs our format/optimization rules.  [oai_citation:4‡professional-web-design-techniques-and-templates.pdf](sediment://file_000000000acc71f8b2e5128c030179fc)  
- HTML/CSS semantics (including figure/caption patterns and separation of structure vs presentation) informs our accessibility + markup guidance.  [oai_citation:5‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  

Additional supporting excerpts:
- Public folder assets are part of what the browser downloads/uses to display the app. [oai_citation:6‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)
- KFM web stack includes 2D MapLibre + 3D Cesium, which impacts how we store sprites/icons. [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Static asset caching guidance (e.g., far-future cache headers) supports performance rules. [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

</details>

---

<p align="right"><a href="#-webpublicimages--public-image-assets">⬆️ Back to top</a></p>