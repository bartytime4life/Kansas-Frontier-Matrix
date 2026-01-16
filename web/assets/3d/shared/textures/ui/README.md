---
doc_uuid: 612878a6-d4b9-4dfe-ac2c-a32a6432b959
semantic_document_id: kfm:web:assets:3d:shared:textures:ui:readme
doc_kind: readme
doc_version: KFM-MDP-v11.2.6
created: 2026-01-15
updated: 2026-01-15
title: "🧩 UI Textures (Shared)"
description: "Shared, GPU-ready 2D textures used by 3D UI/HUD overlays across KFM WebGL/Cesium experiences."
path: web/assets/3d/shared/textures/ui/README.md
status: draft
visibility: public
sensitivity: public
license: SEE-ROOT-LICENSE
owners:
  - KFM Core Maintainers
tags:
  - kfm
  - web
  - 3d
  - textures
  - ui
  - hud
  - webgl
  - cesium
---

# 🧩 UI Textures (Shared)

![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-2ea44f?style=flat-square)
![Assets](https://img.shields.io/badge/asset-3D%20texture-blue?style=flat-square)
![Scope](https://img.shields.io/badge/scope-shared%20UI-orange?style=flat-square)

This folder contains **2D textures intended for use as UI elements inside 3D experiences** (HUD overlays, reticles, pins, billboards-as-UI, cursor decals, compass rings, UI masks, etc.). These assets are shared across KFM’s 3D viewers (e.g., WebGL/Three.js scenes and/or Cesium overlays).

> [!IMPORTANT]
> **This is a “GPU texture” folder.** If an image is only used in standard HTML/CSS UI, it likely belongs in a **non-3D web UI assets** location (not here). Keep this folder focused on textures that are uploaded to the renderer as textures.

---

## 📁 Directory map

```text
web/assets/3d/shared/textures/
├─ atlases/        🧱 Packed atlases (UI + world textures when applicable)
├─ decals/         🩹 World decals (dirt, scratches, stamps, etc.)
├─ jpg/            🟨 JPEG textures (generally no alpha)
├─ materials/      🧪 PBR maps (albedo/normal/roughness/metallic/AO)
├─ png/            🧊 PNG textures (often with alpha)
├─ terrain/        🗻 Terrain textures (tiles, masks, splats)
└─ ui/             🧩 YOU ARE HERE (HUD/UI textures for 3D experiences)
```

---

## ✅ What belongs here

**Examples (typical):**
- 🎯 **HUD**: crosshairs, selection rings, action icons used in-canvas
- 🧭 **Navigation UI**: compass rings, scale indicators used *inside the 3D renderer*
- 📍 **Markers**: pin sprites, hover glows, selection outlines (when rendered in WebGL/Cesium)
- 🪟 **In-scene UI panels**: nine-slice frames, masks, gradients used as textures
- 🖱️ **Cursors** (only if rendered in-canvas for pointer lock / custom 3D cursor)

---

## 🚫 What does *not* belong here

- 🗺️ MapLibre **sprites/glyphs** or 2D map UI assets (those belong under the maps asset tree)
- 🧩 General site icons/logos used only in HTML/CSS
- 🧱 Texture atlases that are shared beyond UI concerns → prefer `../atlases/`
- 📷 Photographic textures used for materials → prefer `../jpg/` or `../materials/`

> [!TIP]
> If an asset is used by both HTML UI *and* 3D UI, prefer a single canonical copy and reference it from both contexts via build tooling or manifests—**don’t duplicate**.

---

## 🧱 Recommended formats

### PNG (default for UI)
- ✅ Best for sharp edges, text-like shapes, transparency
- ✅ Works well for icons, masks, and overlays
- ✅ Use **true alpha** (avoid matte halos)

### WebP/AVIF (optional, only when safe)
- ✅ Great for large UI backgrounds/gradients **if** visual fidelity remains acceptable
- ⚠️ Validate alpha + color correctness across target browsers
- ⚠️ Avoid for tiny crisp icons unless thoroughly QA’d

---

## 🏷️ Naming conventions

Keep names deterministic and grep-friendly.

**Pattern (recommended):**
```
ui__<group>__<name>__<state>@<scale>x.<ext>
```

**Examples:**
- `ui__hud__crosshair__default@2x.png`
- `ui__markers__pin__hover@1x.png`
- `ui__nav__compass-ring__default@2x.png`
- `ui__panels__frame-9slice__default@1x.png`

**Rules:**
- ✅ lowercase + kebab-case in tokens
- ✅ `@1x/@2x/@3x` for DPI variants
- ✅ keep “state” explicit: `default | hover | active | disabled | selected`
- ❌ no spaces, no “final2”, no “new-new”, no unversioned ambiguity

---

## 🎨 Color + gamma rules

- UI textures are typically authored in **sRGB**.
- If the renderer distinguishes color-space (recommended), UI textures should be sampled as **sRGB** and blended correctly with alpha.
- For masks/lookup textures (data textures), use **linear** and document it in metadata.

> [!IMPORTANT]
> When you see “washed out” or “too dark” UI in WebGL, it’s often a **color-space mismatch** (sRGB vs linear). Treat UI textures as color assets unless they are explicitly “data textures.”

---

## 🧊 Size + mipmaps

- Prefer power-of-two (64/128/256/512) when:
  - you need mipmaps, or
  - the texture is reused heavily, or
  - the UI sprite is scaled/zoomed in 3D.
- For pixel-perfect overlays that are never minified, non-power-of-two can be acceptable.

**Guideline (icons):**
- `@1x`: 32–64 px baseline
- `@2x`: 64–128 px baseline
- `@3x`: 96–192 px baseline

---

## 🧰 Authoring + optimization pipeline

```mermaid
flowchart LR
  A[🎨 Authoring (Figma/PS/SVG)] --> B[🧾 Export PNG @1x/@2x]
  B --> C[🧹 Optimize (lossless)]
  C --> D[📦 Place in ui/]
  D --> E[🧭 Register in manifest (if used)]
  E --> F[🕹️ Runtime load -> GPU texture]
```

### Recommended optimizers
- **Lossless PNG**: `oxipng` / `pngcrush`
- **Careful lossy (icons only if validated)**: `pngquant` (watch halos + gradients)

> [!NOTE]
> Optimization is required for repo hygiene and load performance—**but never at the expense of edge quality** on icons and thin strokes.

---

## 📜 Attribution + licensing (non-negotiable)

If a UI texture is **third-party** or derived from third-party work:
- Include a clear attribution trail and license evidence.
- Prefer a per-asset sidecar, for example:
  - `ui__hud__crosshair__default@2x.license.md`
  - `ui__hud__crosshair__default@2x.prov.json` (optional provenance detail)

Minimum required fields in the license note:
- Source URL (or original package)
- Author/organization (if known)
- License type + link
- Modifications (if any)
- Allowed uses / restrictions

---

## ✅ QA checklist

| Check | Why it matters |
|------:|----------------|
| Alpha edges are clean (no halos) | UI looks crisp on any background |
| DPI variants exist where needed | Avoids blurry UI on high-DPI screens |
| File size optimized | Faster loads + smaller bundles |
| Naming matches convention | Predictable imports + easier grep |
| sRGB/linear intent documented | Prevents gamma bugs in WebGL |
| License note present (if not original) | Keeps repo shippable + auditable |

---

## 🔗 Related docs (nearby)

- `../atlases/README.md` 🧱 (packed UI sheets, if used)
- `../png/README.md` 🧊 (general PNG rules)
- `../materials/README.md` 🧪 (PBR textures; not UI)

---

## 🧭 Quick “do / don’t”

✅ **DO**
- keep UI sprites small + sharp
- use PNG for alpha UI
- document anything that’s “data-texture” (mask/LUT)
- keep third-party licensing next to the asset

❌ **DON’T**
- duplicate icons across folders
- store MapLibre sprites/glyphs here
- commit huge unoptimized PNGs
- mix “world decals” into UI (use `../decals/`)
