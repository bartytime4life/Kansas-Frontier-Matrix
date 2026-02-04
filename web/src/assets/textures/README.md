# Textures 🎨🧩

✅ Optimized • 🧾 Provenance-first • 🗺️ Map/3D friendly • ⚡ Bundle-aware

This folder contains **runtime texture assets** used by the web client—primarily for:

- **UI patterns** (subtle backgrounds, noise, paper, grid, etc.)
- **Map overlays** (hatches, stipple, heat masks, thematic fills)
- **3D materials** (albedo/baseColor, normal, roughness, etc.) for WebGL/Cesium-like pipelines

> [!IMPORTANT]
> **Evidence-first rule:** If a texture is sourced externally (open data, scans, photo libraries, etc.), it **must** ship with clear provenance + licensing metadata.  
> This matches the project’s broader “trust + traceability” ethos (“the map behind the map”).  [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 📌 Quick goals

- **Fast loads**: small files, GPU-friendly sizes, minimal overdraw
- **Consistent naming**: predictable suffixes and sizes
- **Safe usage**: no copyrighted/uncleared textures
- **Traceability**: every non-trivial asset can be audited back to its source

---

## 🧭 Recommended directory layout

> [!NOTE]
> The repo may not have all of these subfolders yet—this is the **target structure** as the library grows.

```text
web/src/assets/textures/
├─ ui/                 # UI-only patterns (tileable backgrounds, noise, paper, etc.)
├─ map/                # 2D map styling assets (hatches, masks, thematic fills)
├─ pbr/                # 3D PBR sets (baseColor/normal/roughness/metallic/ao/etc.)
├─ decals/             # Single-use non-tile textures (stamps, worn edges, labels)
├─ _meta/              # Sidecar metadata (provenance + license), one per external asset
└─ README.md           # You are here ✨
```

---

## 🧱 File formats & performance rules

### Preferred formats ✅

| Use case | Preferred | Acceptable | Avoid |
|---|---|---|---|
| UI patterns / subtle noise | **WebP** | PNG | Huge PNG/JPG |
| Map hatches (needs crisp edges) | **PNG** | WebP (if lossless) | JPEG (edge blur) |
| 3D textures (GPU + streaming) | **KTX2** (if pipeline supports) | PNG/WebP | Uncompressed TIFF |
| Normal maps | **PNG** (lossless) | KTX2 | Lossy WebP/JPEG |

> [!TIP]
> Keep textures **power-of-two** when possible: `64, 128, 256, 512, 1024, 2048`  
> Power-of-two improves mipmapping and reduces surprises in WebGL materials.

### Size budgets (practical defaults)

- **UI tileables**: `≤ 256×256` (often `64×64` or `128×128` is enough)
- **Map hatches**: `64×64` to `256×256` (tileable)
- **PBR sets**: start at `1024×1024`, only go `2048×2048` when truly justified

> [!WARNING]
> If a texture exceeds **1 MB**, it needs a reason (and usually a better compression strategy).

---

## 🏷️ Naming conventions

Use **kebab-case** and include **resolution** when it matters.

### General
- `texture-purpose_variant_size.ext`
- Examples:
  - `paper-fine_256.webp`
  - `noise-perlin_128.webp`
  - `hatch-diagonal_64.png`

### PBR suffixes (standardized)
For physically-based sets, keep a consistent base name:

```text
rock-limestone_1024_basecolor.webp
rock-limestone_1024_normal.png
rock-limestone_1024_roughness.webp
rock-limestone_1024_metallic.webp
rock-limestone_1024_ao.webp
rock-limestone_1024_height.webp
rock-limestone_1024_emissive.webp
```

> [!NOTE]
> Normal/height/roughness/metallic are frequently treated as **linear** data; baseColor is typically **sRGB**.  
> (Exact handling depends on the renderer / shader pipeline.)

---

## 🧾 Provenance & licensing (non-negotiable)

KFM’s platform design is built around **traceability and trust**. Assets should follow the same standard: each external or derived texture should have a small metadata record (sidecar) that lets us audit **where it came from**, **how it was transformed**, and **how it may be used**.  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### ✅ Sidecar metadata (recommended)

For any texture that is **not fully original** (downloaded, scanned, derived from datasets), create a JSON file in `_meta/`:

```text
_meta/
  paper-fine_256.meta.json
  hatch-diagonal_64.meta.json
  rock-limestone_1024.meta.json
```

#### Template: `*.meta.json`
```json
{
  "id": "paper-fine_256",
  "type": "texture",
  "title": "Paper Fine (Tileable)",
  "source": {
    "origin": "external",
    "author": "UNKNOWN",
    "publisher": "UNKNOWN",
    "license": "CC-BY-4.0 | CC0 | Public Domain | Proprietary (NOT ALLOWED) | ...",
    "attribution": "Required attribution text if applicable",
    "source_notes": "Where it came from and any constraints"
  },
  "processing": {
    "tools": ["image editor", "cli optimizer"],
    "steps": [
      "cropped to tileable square",
      "exported to WebP (quality=90)",
      "checked for seams"
    ]
  },
  "usage": {
    "intended": ["ui-background", "map-overlay"],
    "do_not_use_for": ["branding", "commercial-only contexts if license forbids"]
  },
  "integrity": {
    "sha256": "OPTIONAL-BUT-IDEAL",
    "created_at": "YYYY-MM-DD",
    "updated_at": "YYYY-MM-DD"
  }
}
```

> [!IMPORTANT]
> If you can’t supply a license/provenance record, **don’t add the texture**.  
> This mirrors the project’s broader “no source, no answer” governance pattern.  [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:3‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)

---

## 🧩 Using textures in code

> [!NOTE]
> Exact import behavior depends on the web tooling (Vite/Webpack/etc.). The patterns below are the common approach in React/TS projects.  [oai_citation:4‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

### 1) Importing a texture URL (React/TS)
```ts
import paperFineUrl from "./ui/paper-fine_256.webp";

// Use as <img>, CSS background, or WebGL texture source.
```

### 2) CSS background (tileable)
```css
.panel {
  background-image: url("./ui/paper-fine_256.webp");
  background-repeat: repeat;
  background-size: 256px 256px;
}
```

### 3) Map patterns (MapLibre-style approach)
If your map layer supports image patterns, you typically load an image and reference it by name.

```ts
import hatchUrl from "./map/hatch-diagonal_64.png";

// Example shape (API varies by mapping lib)
map.loadImage(hatchUrl, (err, image) => {
  if (err || !image) return;
  map.addImage("hatch-diagonal", image, { pixelRatio: 1 });

  // Then reference "hatch-diagonal" in a fill/line symbol style.
});
```

### 4) 3D / materials (WebGL/Cesium-like)
```ts
import baseColorUrl from "./pbr/rock-limestone_1024_basecolor.webp";
import normalUrl    from "./pbr/rock-limestone_1024_normal.png";

// Pseudocode: your engine will differ
material.setTexture("baseColor", baseColorUrl);
material.setTexture("normal", normalUrl);
```

---

## ✅ Texture quality checklist (PR gate)

Before committing a new texture:

- [ ] **Correct format** (WebP/PNG/KTX2 as appropriate)
- [ ] **Reasonable size** (no surprise multi-MB files)
- [ ] **Tileable** when intended (no seams / obvious repeats)
- [ ] **Named correctly** (kebab-case + resolution + suffix)
- [ ] **Metadata added** if sourced externally (`_meta/*.meta.json`)
- [ ] **License is compatible** with this repo’s distribution

> [!TIP]
> If a texture is used in multiple places, prefer a **single canonical asset** rather than slightly different duplicates.

---

## 🧠 Design note: why we’re strict about provenance

The Kansas Frontier Matrix is designed as an evidence-first geospatial knowledge platform where outputs are traceable to their sources, improving trust and accountability. That same mindset applies even to “small” assets like textures, because UI and cartographic styling can still carry licensing and interpretability risks.  [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 📚 References & alignment

- Kansas Frontier Matrix — governance, provenance, “truth path” architecture.  [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- Learn to Code HTML & CSS — practical usage of images/backgrounds and web asset conventions.  [oai_citation:7‡learn-to-code-html-and-css-develop-and-style-websites.pdf](sediment://file_00000000ed6471fdb0ecead71e051444)  
- Node.js / Web tooling context — general web project structure + runtime/bundling mindset.  [oai_citation:8‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  
- Trust & “best practices” framing (why guardrails matter in high-stakes systems).  [oai_citation:9‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)