# 🧩 SVG Icon Sources (Map Sprite Builder)

![KFM](https://img.shields.io/badge/KFM-provenance--first-1f6feb?style=flat)
![Map](https://img.shields.io/badge/Maps-MapLibre%20Style%20Sprites-2ea44f?style=flat)
![SVG](https://img.shields.io/badge/Format-SVG-ffb13b?style=flat)
![Assets](https://img.shields.io/badge/Web-Static%20Assets-8a2be2?style=flat)

Welcome! This folder contains the **canonical, hand-edited SVG icons** that get compiled into the **sprite sheets** used by our map styles. 🗺️✨  
If you’re adding / tweaking map icons, this is your home base.

> [!IMPORTANT]
> This directory is **source-of-truth**. Generated sprite outputs (PNG/JSON) should be treated as build artifacts and **not hand-edited**. 🧯

---

## 📍 You are here

`web/assets/maps/styles/sprites/src/svg/`

**What lives here?**
- ✅ Raw `.svg` icons (single-icon-per-file)
- ✅ Icons designed to work at tiny map sizes (12–24px)
- ✅ Icons that can be bundled into sprites for fast rendering

---

## 🗂️ Expected sprite layout

We keep sprites organized like a normal build pipeline: **src ➜ build output**.

```text
🗂️ web/
  🗂️ assets/
    🗂️ maps/
      🗂️ styles/
        🗂️ sprites/
          🗂️ src/
            🗂️ svg/            👈 you are here
              📄 README.md
              🖼️ example-icon.svg
          🗂️ dist/             🏗️ generated (png/json)
            🖼️ sprite.png
            🖼️ sprite@2x.png
            🧾 sprite.json
            🧾 sprite@2x.json
```

> [!NOTE]
> Your repo may output to a different folder name than `dist/`. Use the project’s sprite build script as the source of truth. 🧭

---

## 🚀 Quick start (add a new icon)

1) **Create** a new SVG file in this folder  
2) **Follow the SVG rules** below (viewBox, grid, fills, etc.)  
3) **Run sprite generation** (see “Build / Generate Sprites”)  
4) **Use the icon name** in the map style (`icon-image`) 🧪

---

## 🏷️ Naming conventions

### ✅ File names
- Use **kebab-case**: `trailhead.svg`, `historic-site.svg`
- Be explicit and stable: `railroad-station.svg` > `station.svg`
- Avoid versioning in names: `school.svg` > `school-v2.svg`

### ✅ Namespacing (optional but recommended)
If we expect a large icon set, prefer subfolders for “namespaces”:

```text
🗂️ svg/
  🗂️ kfm/
    🖼️ courthouse.svg
    🖼️ monument.svg
  🗂️ infra/
    🖼️ dam.svg
    🖼️ bridge.svg
```

This typically maps to sprite icon IDs like:
- `kfm/courthouse`
- `infra/bridge`

> [!TIP]
> Namespacing keeps style JSON readable and reduces collisions. 🔧

---

## 🎨 SVG rules (non‑negotiable)

| Rule | Why it matters | ✅ Do | ❌ Don’t |
|---|---|---|---|
| **Must have `viewBox`** | Required for consistent scaling | `viewBox="0 0 24 24"` | Missing viewBox |
| **Use a consistent grid** | Prevents “jitter” between icons | 24×24 (recommended) | Random sizes per icon |
| **Keep coordinates pixel-friendly** | Prevents blur | mostly integers / halves | lots of long decimals |
| **No filters / raster embeds** | Sprite toolchain compatibility | simple paths | drop-shadows, bitmaps |
| **Avoid transforms** | Determinism & easier diffs | bake transforms | nested transforms |
| **Keep shapes bold enough** | Legible at 12–16px | thicker strokes / solid fills | hairline strokes |

### ✅ Recommended SVG skeleton

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-label="courthouse">
  <path d="..."/>
</svg>
```

> [!NOTE]
> `aria-label` is optional for sprites, but helpful if we ever reuse icons inline in UI. ♿

---

## 🎯 Style guidance for map legibility

Map icons are *tiny* and sit on top of complex basemaps. Keep them:
- **Simple** (avoid intricate details)
- **High-contrast** (solid silhouettes beat thin linework)
- **Consistent** (stroke weights and corner radii match across the set)
- **Semantic** (icon meaning matches layer meaning) 🧠

---

## 🧪 QA checklist (before committing)

- [ ] File name follows `kebab-case` (and namespace folder if used) 🏷️  
- [ ] `viewBox` is present and matches the agreed grid (recommended `0 0 24 24`) 📐  
- [ ] Looks good at **12px / 16px / 24px** (test in your editor) 🔍  
- [ ] No filters, masks, or embedded images 🧼  
- [ ] Paths are merged/simplified where possible (clean diffs) ✂️  
- [ ] Icon meaning is clear, not “cute” 😉  
- [ ] If it’s third‑party: provenance & license recorded (see below) 🧾  

---

## 🏗️ Build / Generate sprites

The exact command depends on our toolchain, but the workflow is always:

**SVG folder ➜ sprite PNGs ➜ sprite JSON metadata**

### Typical commands (pick the one that matches the repo)

```bash
# Option A: repo script (preferred if present)
npm run sprites

# Option B: monorepo tooling
pnpm run sprites
# or
pnpm -C web run sprites
```

### What you should see after a successful build ✅
- `sprite.png` and `sprite@2x.png` (retina)
- `sprite.json` and `sprite@2x.json` (icon layout metadata)

> [!IMPORTANT]
> Sprite builds should be **deterministic** (same inputs → same outputs). If your build output changes without SVG changes, flag it. 🧯

---

## 🧾 Provenance & licensing (no “mystery icons”)

KFM’s philosophy is **provenance-first**: nothing ships without knowing *where it came from* and *how it was made*. 🧬

If you add an icon that is not fully original:
- record the **source URL / pack name**
- record the **license**
- record **what you changed**
- record **date added** and **author**

### Suggested manifest file (recommended)
Create or update a manifest alongside the sprite system (commonly in `sprites/` or `sprites/src/`):

`icons.manifest.yml` (example)
```yaml
# 🧾 icons.manifest.yml
icons:
  - id: "kfm/courthouse"
    file: "kfm/courthouse.svg"
    source: "original"
    license: "MIT"
    author: "KFM contributors"
    notes: "Designed for 24x24 grid; bold silhouette for 12–16px map usage."
  - id: "infra/bridge"
    file: "infra/bridge.svg"
    source: "https://example.com/icon-pack"
    license: "CC-BY-4.0"
    attribution: "Example Icon Pack"
    modifications: "Simplified stroke + removed inner details"
    added: "2026-01-17"
```

> [!TIP]
> This manifest makes it easy to auto-generate attribution and keep assets audit-friendly. ✅

---

## 🧩 Using an icon in a MapLibre-style layer

Example snippet (style JSON):

```json
{
  "id": "poi-historic-sites",
  "type": "symbol",
  "source": "kfm-poi",
  "layout": {
    "icon-image": "kfm/monument",
    "icon-size": 1.0,
    "icon-allow-overlap": false
  }
}
```

---

## 🧯 Troubleshooting (common sprite failures)

<details>
  <summary>❌ Icon renders blurry</summary>

- Check for non-integer coordinates and odd transforms  
- Ensure you’re designing on the agreed grid (`24x24`)  
- Test at 12–16px; simplify thin lines  
</details>

<details>
  <summary>❌ Build tool skips / drops an icon</summary>

- Missing `viewBox`
- Unsupported SVG features (filters, masks, embedded images)
- Invalid XML (unclosed tags)
</details>

<details>
  <summary>❌ Icon name doesn’t work in the style</summary>

- Sprite name may include folder prefix (`kfm/thing`)  
- Rebuild sprites and verify the icon exists in `sprite.json`  
</details>

---

## 🔗 Related KFM docs 📚

- 📘 KFM Technical Docs (architecture + provenance-first principles)
- 🧭 KFM Markdown / Governance guide (contract-first + evidence-first docs)
- 🎨 Cartographic references (see the project’s docs library manifest)

> [!NOTE]
> If you’re designing new symbology (not just icons), check the cartography references in the docs library so styles stay consistent across layers. 🗺️✨
