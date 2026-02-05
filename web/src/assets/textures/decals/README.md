# 🏷️ Decal Textures (Web UI)

![assets](https://img.shields.io/badge/assets-decals-2ea44f?style=for-the-badge)
![scope](https://img.shields.io/badge/scope-web%2Fsrc%2Fassets-1f6feb?style=for-the-badge)
![goal](https://img.shields.io/badge/goal-fast%20%2B%20clear%20%2B%20traceable-8b5cf6?style=for-the-badge)

Small, transparent “stickers” (textures) used across the **KFM React map UI** for **2D icons (MapLibre)** and **3D markers/overlays (Cesium)**. Keep them lightweight, consistent, and provenance-safe. 🧭🗺️✨

> [!NOTE]
> This folder is for **runtime-ready** assets only (the files that ship in the web bundle).  
> Keep heavyweight authoring files (PSD/AI/large SVG working docs) **out of `web/src/`** to avoid accidental bundling.

---

<details>
  <summary><strong>📚 Table of Contents</strong></summary>

- [What belongs here](#-what-belongs-here)
- [Folder contract](#-folder-contract)
- [Naming conventions](#-naming-conventions)
- [Formats and sizing](#-formats-and-sizing)
- [Metadata and provenance](#-metadata-and-provenance)
- [Optimization rules](#-optimization-rules)
- [Usage examples](#-usage-examples)
  - [MapLibre (2D)](#maplibre-2d)
  - [Cesium (3d)](#cesium-3d)
  - [Vite-friendly URL pattern](#vite-friendly-url-pattern)
- [QA checklist](#-qa-checklist)
- [Governance and licensing](#-governance-and-licensing)
- [Related docs](#-related-docs)

</details>

---

## ✅ What belongs here

**Decals in this directory should be:**

- 🧩 **Small**: icons, badges, stamps, simple textures/pattern marks  
- 🧼 **Clean**: crisp edges, predictable padding, transparent background when needed  
- 🚀 **Fast**: optimized and right-sized for typical on-screen usage  
- 🧾 **Traceable**: source + license + creator documented (see [Metadata and provenance](#-metadata-and-provenance))

**Examples of use-cases**
- 📍 POI / site markers (wells, towns, forts, archives, etc.)
- 🧠 Focus Mode visual cues (citation markers, evidence flags, “story node” stamps)
- 🛰️ 3D billboards / pins in globe mode
- 🧵 Subtle texture accents used for qualitative layers (when appropriate)

---

## 📦 Folder contract

**This folder is treated like a mini “asset API”:** consistent filenames + predictable metadata.  
If you add an asset, it must be usable without guesswork.

Recommended structure (you can adapt if the repo already has a convention):

```text
📁 web/src/assets/textures/decals/
├── 📄 README.md
├── 📁 symbols/                 # simple icons/badges (often monochrome)
├── 📁 poi/                     # point-of-interest decals
├── 📁 hazards/                 # warning/alert decals
├── 📁 patterns/                # subtle textures (use sparingly)
└── 📁 _meta/                   # optional: centralized metadata/attribution
```

> [!TIP]
> If your decals are used as **MapLibre SDF icons**, consider a dedicated `symbols/sdf/` subfolder to keep constraints obvious.

---

## 🧾 Naming conventions

**Goals:** readable in code, searchable in Git, stable for caching.

### ✅ Filename pattern (recommended)
```text
kfm-<category>-<slug>[-<variant>][@2x].<ext>
```

**Rules**
- ✅ lowercase, kebab-case
- ✅ ASCII only
- ✅ no spaces
- ✅ keep slugs semantic (what it *is*, not where it’s currently used)

**Examples**
- `kfm-poi-historic-marker.png`
- `kfm-symbol-kansas-star.png`
- `kfm-hazards-flood-warning@2x.png`
- `kfm-pattern-hatch-light.png`

---

## 🖼️ Formats and sizing

### Preferred formats
- **PNG** ✅ for transparency + sharp edges (most decals)
- **WebP** ✅ only if you *need* it and your usage path supports it (modern browsers do; still validate your loaders)
- **JPG** ❌ usually not ideal for decals (no alpha; compression artifacts on edges)

### Sizing guidelines
- 🎯 Design for **actual usage size** first (typically 16–64px on screen).
- 🧠 Provide **one “base” size**, and only add `@2x` if you truly need retina crispness.
- 🧊 Keep the artwork inside a consistent “safe area” (padding) so anchors are predictable.

**Texture dimension guidance (WebGL-friendly)**
- Prefer **power-of-two** dimensions when possible (128, 256, 512) for predictable mipmapping behavior.
- Don’t ship a 2048px decal unless it’s genuinely required.

---

## 🧬 Metadata and provenance

KFM is an evidence-first system — even UI assets should be **auditable** when they convey meaning. 🔍

### ✅ “No source, no asset” rule
If a decal is **not original work** by the project **and** has no clear license/source → it doesn’t get merged.

### Sidecar metadata (recommended)
For each decal, add a sidecar file:

```text
kfm-poi-historic-marker.png
kfm-poi-historic-marker.meta.json
```

Example `*.meta.json`:

```json
{
  "id": "kfm-poi-historic-marker",
  "title": "Historic Marker",
  "category": "poi",
  "tags": ["history", "marker", "plaque"],
  "intendedUse": ["maplibre-icon", "cesium-billboard"],
  "source": {
    "type": "original",
    "creator": "KFM Team",
    "license": "CC-BY-4.0",
    "attribution": "Kansas Frontier Matrix"
  },
  "design": {
    "recommendedPx": [24, 32, 48],
    "safePaddingPct": 12,
    "sdfCompatible": false
  },
  "created": "2026-02-05",
  "notes": "Use for historic-site POIs in both 2D and 3D."
}
```

> [!IMPORTANT]
> Keep metadata **short and practical**. The goal is provenance + intent, not a novel.

---

## ⚡ Optimization rules

Decals are “small” by design — but they add up fast when you have many layers and views.

### ✅ Do
- ✅ Export at the smallest acceptable resolution
- ✅ Compress **every** PNG/WebP before committing
- ✅ Remove stray alpha pixels / halos
- ✅ Keep edges crisp (avoid heavy blur unless it’s intentional)

### ❌ Don’t
- ❌ Commit uncompressed “export defaults”
- ❌ Use photographic formats for icon-like decals
- ❌ Use visually noisy textures that overpower data layers
- ❌ Pick textures that imply the wrong meaning (texture ≠ decoration)

> [!TIP]
> Subtle texture can communicate *qualitative* differences — but it can also become visual noise. Use sparingly.

---

## 🧪 Usage examples

### MapLibre (2D)

```ts
// Example: add a decal as a MapLibre image for use in a symbol layer
import type { Map as MapLibreMap } from "maplibre-gl";
import decalUrl from "./poi/kfm-poi-historic-marker.png";

export async function registerDecals(map: MapLibreMap) {
  if (map.hasImage("kfm-poi-historic-marker")) return;

  const img = await loadHtmlImage(decalUrl);
  map.addImage("kfm-poi-historic-marker", img, {
    // Use sdf: true ONLY for monochrome SDF icons you plan to tint via style
    sdf: false,
    pixelRatio: 2
  });
}

function loadHtmlImage(src: string): Promise<HTMLImageElement> {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}
```

### Cesium (3D)

```ts
// Example: use a decal as a Cesium billboard
import decalUrl from "./poi/kfm-poi-historic-marker.png";

viewer.entities.add({
  position: Cesium.Cartesian3.fromDegrees(lon, lat),
  billboard: {
    image: decalUrl,
    width: 32,
    height: 32,
    verticalOrigin: Cesium.VerticalOrigin.BOTTOM
  }
});
```

### Vite-friendly URL pattern

If you prefer URL generation (instead of bundler `default` imports):

```ts
const decalUrl = new URL("./poi/kfm-poi-historic-marker.png", import.meta.url).href;
```

---

## 🔎 QA checklist

Before merging a new decal, confirm:

- [ ] ✅ Correct folder + filename (kebab-case; category matches usage)
- [ ] ✅ Transparency works (no checkerboard baked-in)
- [ ] ✅ Edge quality is clean (no halos on dark/light basemaps)
- [ ] ✅ Final dimensions are reasonable (no “oops 2000px” exports)
- [ ] ✅ File is compressed
- [ ] ✅ Sidecar metadata exists (or entry in `_meta/`), including **license/source**
- [ ] ✅ Tested in both:
  - [ ] 🗺️ 2D MapLibre view (at real size)
  - [ ] 🌍 3D Cesium view (billboard readability / anchoring)
- [ ] ✅ If it’s a texture/pattern: it’s not visually noisy and doesn’t imply misleading semantics

---

## 🛡️ Governance and licensing

- 🧾 Every third-party decal must have **clear license + attribution**
- 🔒 Respect data sovereignty and sensitivity: **do not** introduce iconography that could reveal restricted locations or culturally sensitive material without review
- 🧠 If a decal implies meaning (warning, classification, “evidence stamp”), treat it as part of the system’s trust surface

> [!WARNING]
> “Unknown source” assets are not allowed. If we can’t explain where it came from, we can’t defend why it’s in the system.

---

## 🔗 Related docs

- 📘 KFM Master Guide (pipeline + evidence-first conventions): `../../../../../docs/MASTER_GUIDE_v13.md`
- 🧭 System architecture & UI context: `../../../../../docs/architecture/`
- 🧩 Story Nodes (governed narrative assets): `../../../../../docs/reports/story_nodes/`
- 🛡️ Governance / ethics: `../../../../../docs/governance/`

---

<details>
  <summary><strong>🧠 Maintainer note</strong></summary>

If we end up with lots of decals, consider adding a small “gallery” dev route or Storybook page that:
- auto-loads all decals,
- shows them on light/dark basemaps,
- displays file size and dimensions,
- links to `.meta.json` provenance.

This keeps the asset library healthy as it grows. 🌱

</details>
