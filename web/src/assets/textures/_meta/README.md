# 🎨 Textures Meta — Kansas Frontier Matrix (Web)

![Status](https://img.shields.io/badge/status-active-success)
![Scope](https://img.shields.io/badge/scope-web%20client-blue)
![Assets](https://img.shields.io/badge/assets-textures-orange)
![Governance](https://img.shields.io/badge/governance-provenance--first-purple)
![License](https://img.shields.io/badge/license-per--asset%20metadata%20required-critical)

> 🧭 **“The texture behind the texture.”**  
> This folder exists to keep every visual asset **traceable, licensed, and reproducible** — consistent with KFM’s evidence-first philosophy.

---

## 📍 Location

`web/src/assets/textures/_meta/`

---

## 🧠 Why this folder exists

Textures aren’t “just visuals” in KFM — they shape readability, trust, and historical tone (paper overlays, grain, hillshade effects, etc.).  
This `_meta/` directory is where we keep the **paper trail** 🧾:

- ✅ **Licensing & attribution** (no surprises in production)
- ✅ **Provenance** (“where did this come from?”)
- ✅ **Generation notes** (how to rebuild / improve)
- ✅ **Performance constraints** (file size + WebGL sanity)
- ✅ **Consistency rules** (naming, variants, tiling, color space)

> 🔒 **Rule of thumb:** If a texture can’t be explained, it can’t ship.

---

## 🗂️ Recommended folder layout

> This is a *guide* for how this area should stay organized over time.

```text
web/src/assets/textures/
├─ ui/                        # UI backgrounds, subtle paper/noise, panels, etc.
├─ map/                       # MapLibre patterns, overlays, masks (tileable)
├─ pbr/                        # Optional: 3D/PBR materials for Cesium/3D scenes
└─ _meta/
   ├─ README.md               # (you are here)
   ├─ textures/               # one YAML/JSON per texture ID
   │  ├─ paper-fiber.yml
   │  ├─ grain-noise.yml
   │  └─ ...
   ├─ sources/                # optional raw/source files (PSD/SVG/BLEND/etc.)
   │  ├─ paper-fiber/
   │  └─ ...
   └─ exports/                # optional: intermediate exports, bake notes, etc.
```

---

## ✅ Non‑negotiables (KFM governance for visuals)

### 1) **No license, no ship** 🔒
Every texture must have an explicit license (preferably SPDX identifier) and attribution rules.

### 2) **Provenance-first (traceable assets)** 🧾
Every texture must have a `_meta/textures/<id>.yml` entry that answers:
- Where did it come from?
- Who made it?
- What transformations were applied?
- What files are shipped?
- What is the intended usage?

### 3) **Fail closed by default** 🚫
If metadata is missing, unclear, or contradictory:
- treat the asset as **restricted**
- do **not** ship it in public builds

### 4) **Performance budgets matter** ⚡
Textures can quietly destroy load time and WebGL memory.
Ship the smallest thing that still looks good.

---

## 🏷️ Naming conventions

### Texture IDs
Use **kebab-case** IDs that describe *content*, not a temporary style:

✅ `paper-fiber`  
✅ `grain-noise`  
✅ `parchment-warm`  
❌ `orange-bg` (style may change)  
❌ `cool-v2-final-final2` (versioning belongs in git, not filenames)

### Runtime filenames
Use predictable roles:

`<id>.<role>.<ext>`

Common roles:
- `tile` — seamless tile meant to repeat
- `preview` — readable preview for docs/UI
- `thumb` — tiny thumbnail for catalogs/menus
- `mask` — alpha mask / stencil / LUT-like helper

Examples:
- `paper-fiber.tile.webp`
- `paper-fiber.preview.png`
- `paper-fiber.thumb.webp`
- `county-mask.mask.png`

### PBR naming (if you add 3D materials)
`<id>.<map>.<ext>`

Maps (suggested):
- `albedo` (base color)
- `normal`
- `roughness`
- `metallic`
- `ao` (ambient occlusion)
- `height` (optional)
- `emissive` (optional)

Example:
- `limestone-weathered.albedo.webp`
- `limestone-weathered.normal.png`

---

## 📐 Technical constraints and budgets

| Category | Use case | Recommended formats | Budget guidance |
|---|---|---|---|
| 🧩 UI textures | Panels, backgrounds, subtle paper | `webp` (preferred), `png` (if needed) | Keep most under **≤ 80 KB** |
| 🗺️ Map patterns | Repeating fills, overlays | `webp`, `png` | Prefer **≤ 40 KB** and small tiles |
| 🌍 3D / PBR | Cesium/3D materials | `webp`/`png`, (future: `ktx2`) | Keep sets tight; avoid huge 4K by default |
| 🧼 Masks/LUTs | Alpha masks, ramps | `png` | Small + lossless |

**WebGL notes (practical defaults):**
- ✅ Prefer **power-of-two** dimensions for GPU-friendly mipmaps: 256/512/1024/2048
- ✅ Keep tiles **seamless** if they’ll repeat
- ✅ Avoid embedded color profiles that bloat file size
- ✅ If it looks “banded,” consider subtle dithering/noise *within budget*

---

## 🧾 Texture metadata files

Each shipped texture should have **one metadata file**:

`web/src/assets/textures/_meta/textures/<id>.yml`

### Minimal required fields

| Field | Required | Example |
|---|---:|---|
| `id` | ✅ | `paper-fiber` |
| `title` | ✅ | `Paper Fiber (Subtle)` |
| `kind` | ✅ | `ui` / `map` / `pbr` |
| `description` | ✅ | Human readable purpose |
| `license.spdx` | ✅ | `CC0-1.0`, `MIT`, etc. |
| `license.attribution` | ✅ | Attribution string or `null` |
| `source.type` | ✅ | `created` / `public-domain` / `purchased` / `open-data` |
| `files.*.path` | ✅ | relative path to shipped file |
| `files.*.sha256` | ✅ (recommended) | integrity hash |

### Example YAML

```yaml
id: paper-fiber
title: Paper Fiber (Subtle)
kind: ui
description: >
  Subtle paper texture for panels and historical UI overlays.
  Designed to preserve text readability and reduce flat-color banding.

intended_use:
  - ui.panels
  - ui.backgrounds
  - map.story-overlays

license:
  spdx: CC0-1.0
  attribution: null
  notes: "Created in-house for KFM."

source:
  type: created
  author: "KFM Design Team"
  created_at: "2026-02-05"
  url: null

files:
  tile:
    path: ../../ui/paper-fiber.tile.webp
    size_px: [1024, 1024]
    tileable: true
    alpha: true
    color_space: sRGB
    sha256: "REPLACE_WITH_SHA256"
  preview:
    path: ../../ui/paper-fiber.preview.png
    size_px: [1200, 800]
    tileable: false
    alpha: false
    color_space: sRGB
    sha256: "REPLACE_WITH_SHA256"

quality:
  notes:
    - "Keep contrast low; background must not compete with labels."
    - "Test with light/dark UI themes."
```

> 🧠 Tip: You can compute sha256 via `sha256sum <file>` (Linux/macOS with coreutils).

---

## 🧬 Optional: A generated manifest

If the UI ever needs to show **credits** or **asset audit info**, consider generating a single runtime manifest:

`web/src/assets/textures/_meta/textures.manifest.json`

This can be generated from the YAML files to keep the UI simple.

Example shape:

```json
{
  "paper-fiber": {
    "title": "Paper Fiber (Subtle)",
    "kind": "ui",
    "license": { "spdx": "CC0-1.0", "attribution": null },
    "files": {
      "tile": "ui/paper-fiber.tile.webp",
      "preview": "ui/paper-fiber.preview.png"
    }
  }
}
```

---

## 🧩 Usage examples (Web)

> These are *patterns*, not strict requirements — adapt to your bundler (Vite/Webpack/etc.).

### CSS (background texture)
```css
.panel {
  background-image: url("../textures/ui/paper-fiber.tile.webp");
  background-repeat: repeat;
  background-size: 512px 512px;
}
```

### TypeScript (safe URL creation)
```ts
const paperFiber = new URL(
  "../assets/textures/ui/paper-fiber.tile.webp",
  import.meta.url
).href;
```

### React (import as asset)
```tsx
import paperFiber from "@/assets/textures/ui/paper-fiber.tile.webp";

export function PaperPanel() {
  return (
    <div style={{ backgroundImage: `url(${paperFiber})` }}>
      {/* content */}
    </div>
  );
}
```

### MapLibre (pattern image)
```ts
// Pseudo-pattern: load the image, then addImage + use in a fill-pattern layer
map.loadImage(paperFiber, (err, image) => {
  if (err || !image) return;

  if (!map.hasImage("paper-fiber")) {
    map.addImage("paper-fiber", image, { pixelRatio: 2 });
  }

  // Use in style: "fill-pattern": "paper-fiber"
});
```

---

## 🧪 QA checklist (before merging)

- [ ] 🧾 Metadata file exists: `_meta/textures/<id>.yml`
- [ ] 🔒 License is explicit, compatible, and attribution is correct
- [ ] 🧬 Source is documented (created/purchased/open-data/etc.)
- [ ] 🧱 File naming follows the convention (`<id>.<role>.<ext>`)
- [ ] ⚡ File sizes are within budget
- [ ] 🧩 Tileable assets are truly seamless (no visible seams)
- [ ] 🎛️ Works under both light/dark themes (if applicable)
- [ ] 🗺️ Doesn’t reduce map label readability (test with dense labels)
- [ ] 🧠 No sensitive/identifying imagery (faces, plates, private locations)

---

## 🧰 Handy tooling (optional)

- 🛠️ **ImageMagick** for resizing/format conversion (`magick`, `convert`)
- 🗜️ **Lossless compression** tools (depending on format)
- 🎨 **Design sources** (PSD/AFDESIGN/SVG/BLEND) stored under `_meta/sources/<id>/`

> If you add scripts later, keep them deterministic and document them here (inputs ➜ outputs ➜ hashes).

---

## 📜 Attribution & “credits UI” idea

If the KFM web UI ever shows texture credits (recommended):
- surface “Attribution” from metadata
- link to the source (when public)
- keep it searchable (“audit panel” style)

This aligns with KFM’s broader principle that outputs should be explainable and traceable.

---

## 🔁 Contribution flow (quick)

1) Drop new texture into the appropriate folder (`ui/`, `map/`, `pbr/`)  
2) Add `_meta/textures/<id>.yml` with license + provenance  
3) Add preview/thumb if useful  
4) Verify budgets + seams + readability  
5) Commit + PR 🎯

---

## 🧭 Design north stars (keep it “KFM”)

- 🗺️ **Legibility > decoration**
- 📚 **Historical tone without fake “antique noise” overload**
- 🔍 **Subtle textures that support evidence-first storytelling**
- ⚖️ **Always respect licensing and cultural sensitivity**

---
