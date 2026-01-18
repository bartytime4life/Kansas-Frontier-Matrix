# 🎛️ UI Texture Sources  
`web/assets/media/_sources/textures/ui/`

<p align="center">
  <img alt="KFM" src="https://img.shields.io/badge/KFM-UI_Textures-0b7285?style=for-the-badge" />
  <img alt="Provenance Required" src="https://img.shields.io/badge/Provenance-Required-2ea44f?style=for-the-badge" />
  <img alt="License Documented" src="https://img.shields.io/badge/License-Documented-orange?style=for-the-badge" />
</p>

> 🧠 **What this folder is:** The **source-of-truth** artwork for KFM’s web UI textures (icons, controls, sprites, subtle patterns, etc.).  
> 🚀 **What it’s not:** The final runtime-optimized assets (those should live in a separate, “built” location).

---

## 🗂️ Folder map

```text
📁 web/
  📁 assets/
    📁 media/
      📁 _sources/
        📁 textures/
          📁 ui/   👈 you are here (editable / authoring files)
      📁 textures/
        📁 ui/     ✅ expected runtime-ready exports (optimized)
```

---

## 🧭 Contents

- [🚦 Non‑negotiables](#-nonnegotiables)
- [🧩 What belongs here](#-what-belongs-here)
- [🧾 Provenance + licensing](#-provenance--licensing)
- [🏷️ Naming conventions](#️-naming-conventions)
- [🖼️ Format + export guidelines](#️-format--export-guidelines)
- [📦 Sprites + atlases](#-sprites--atlases)
- [📱 Responsive delivery tips](#-responsive-delivery-tips)
- [♿ Accessibility notes](#-accessibility-notes)
- [✅ Contribution checklist](#-contribution-checklist)
- [🧪 QA expectations](#-qa-expectations)
- [🔧 Suggested tooling](#-suggested-tooling)
- [🔗 References](#-references)

---

## 🚦 Nonnegotiables

> [!IMPORTANT]
> **Provenance-first applies to UI assets too.**  
> If it appears in the UI, we must be able to answer: **Where did it come from? What license? What edits were applied?**

**Rules:**
- ✅ Only add assets you can **license + attribute** properly.
- ✅ Prefer **open / permissive** sources (CC0, MIT, etc.) and **document it**.
- ❌ No “mystery icons” (random downloads with unknown license).
- ❌ No vendor-locked or proprietary packs unless explicitly approved and documented.

---

## 🧩 What belongs here

Typical categories (add subfolders if helpful):

- 🖱️ **controls/** — buttons, toggles, slider tracks/handles, UI chrome
- 🧭 **navigation/** — chevrons, back/forward, zoom, compass
- 🧷 **markers/** — map pins, selection rings, highlights
- 🧾 **badges/** — small UI labels, tags, status pills
- 🧵 **patterns/** — subtle repeating textures (grain, paper, topo-lite patterns)
- 🧰 **icons/** — monochrome or token-driven UI icons (prefer SVG)

> [!NOTE]
> Keep “scratch” iterations **out of git** (or place in a clearly ignored folder like `_scratch/`).

---

## 🧾 Provenance + licensing

**Every new UI texture should ship with a small “asset contract” sidecar** so we can audit provenance, licensing, and transformations.

### ✅ Sidecar file convention (recommended)

For an asset named:
- `icons/layer-toggle.svg`

Create:
- `icons/layer-toggle.asset.json`

<details>
<summary><strong>📦 Minimal asset contract template (copy/paste)</strong></summary>

```json
{
  "id": "ui.icons.layer-toggle",
  "type": "ui-texture",
  "status": "source",
  "source": {
    "origin": "in-house | external",
    "upstream_name": "Name of pack / author (if external)",
    "upstream_url": "https://...",
    "license": "CC0-1.0 | MIT | CC-BY-4.0 | ...",
    "license_url": "https://...",
    "attribution": "How to credit (if required)"
  },
  "created": "YYYY-MM-DD",
  "modified": "YYYY-MM-DD",
  "derivations": [
    {
      "action": "edit | recolor | simplify | trace | combine",
      "notes": "Short description of what changed"
    }
  ],
  "exports": [
    {
      "path": "../../../textures/ui/icons/layer-toggle.svg",
      "purpose": "runtime",
      "optimized": true
    }
  ],
  "notes": "Any extra context (optional)"
}
```

</details>

### 🧷 Attribution in UI
If attribution is required (e.g., CC-BY), add it somewhere that ships with the UI:
- an **About / Credits** page
- a **Credits** modal
- a **NOTICE** file in the repo (preferred for centralized tracking)

---

## 🏷️ Naming conventions

Keep names predictable and grep-friendly:

- ✅ **kebab-case**, lowercase
- ✅ start with a **category prefix** (icon/control/marker/pattern)
- ✅ include **intent**, not “looks like”

Examples:
- `icons/icon-layer-toggle.svg`
- `controls/control-slider-handle@2x.png`
- `markers/marker-selected-ring.webp`
- `patterns/pattern-paper-grain.png`

> [!TIP]
> If multiple scales exist, use `@2x`, `@3x` suffixes for raster assets.

---

## 🖼️ Format + export guidelines

### 🧷 SVG (preferred for icons)
- ✅ Use for UI icons whenever possible (crisp at any scale).
- ✅ Keep shapes simple, avoid hidden layers.
- ✅ If using strokes, ensure they scale intentionally (or expand strokes).
- ✅ Remove metadata bloat (optimize before commit).

**Security note:** never commit SVG with scripts or external references.

### 🧱 PNG (lossless raster)
Use when you need:
- pixel-perfect UI bitmaps
- transparency and crisp edges
- repeatable patterns

Guidelines:
- ✅ Keep dimensions tight (crop to content)
- ✅ Keep alpha clean (no accidental halos)
- ✅ Prefer `@2x` exports for retina displays

### 🌿 WebP (runtime)
WebP is excellent for **runtime** delivery, but keep authoring sources simple.

Recommended approach:
- Author in **SVG/PNG**
- Export **WebP** (and keep a PNG fallback if needed)

---

## 📦 Sprites + atlases

If the UI uses many small icons:
- ✅ consider a **sprite sheet** (fewer requests)
- ✅ keep an index/manifest that maps names → coordinates (if applicable)

> [!NOTE]
> If you introduce a sprite workflow, document it here (how to build, how to reference, how to update).

---

## 📱 Responsive delivery tips

If you ship both WebP + a fallback, use `<picture>`:

```html
<picture>
  <source type="image/webp" srcset="/assets/media/textures/ui/controls/control-slider-handle.webp">
  <img src="/assets/media/textures/ui/controls/control-slider-handle.png" alt="Slider handle">
</picture>
```

---

## ♿ Accessibility notes

- ✅ Icons used as controls must have **text alternatives** (aria-label / visible label).
- ✅ Don’t encode meaning using color alone (use shape + label where needed).
- ✅ Keep icon semantics consistent (same icon = same action everywhere).

---

## ✅ Contribution checklist

When adding/modifying a UI texture:

1. 🧩 Put the **editable source** here (`_sources/textures/ui/...`)
2. 🧾 Add/Update the **`.asset.json`** sidecar (license + provenance)
3. 🖼️ Export runtime-optimized asset(s) to the expected runtime folder (`../textures/ui/...`)
4. 🧪 Sanity-check:
   - file size
   - transparency edges
   - crispness at 1x / 2x
5. 🧭 Ensure the UI reference uses the right asset (and has alt/labels)

---

## 🧪 QA expectations

Typical checks (manual or CI):
- ✅ no missing `.asset.json` for newly added assets
- ✅ no oversized textures (performance budget)
- ✅ file naming conventions
- ✅ no unlicensed / unattributed external art
- ✅ no unsafe SVG content (scripts/external refs)

---

## 🔧 Suggested tooling

Use what fits your stack—these are common options:

- 🧼 **SVGO** for SVG optimization
- 🗜️ **pngquant / oxipng** for PNG optimization
- 🌿 **cwebp** for WebP exports
- 🧪 **image diff** tools (for regression checks on export pipelines)

> [!TIP]
> Automate export/optimization steps where possible to reduce human error and keep outputs consistent.

---

## 🔗 References

- 📘 `docs/MASTER_GUIDE_v13.md` (contracts, governance, canonical pipeline)
- 📗 KFM technical documentation (UI + asset structure, provenance-first philosophy)
- 📙 Responsive image delivery patterns (`<picture>`, WebP + fallback)

---
