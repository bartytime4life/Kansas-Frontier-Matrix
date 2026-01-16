# 🧩 Legacy Map Sprites (MapLibre / Mapbox)

![asset](https://img.shields.io/badge/asset-sprite%20pack-blue)
![status](https://img.shields.io/badge/status-legacy-orange)
![web](https://img.shields.io/badge/web-static%20front--end-brightgreen)

This folder contains **legacy sprite sheets** (PNG) + **sprite metadata** (JSON) used by the Kansas Frontier Matrix (KFM) web map viewer.

> ⚠️ **“Legacy” = stability-first.**  
> These sprites exist primarily to keep **older style JSONs** working without breaking icon references.

---

## 📦 What’s in here?

A MapLibre/Mapbox sprite pack is typically shipped as:

- 🖼️ `NAME.png` — the sprite atlas image (1×)
- 🧩 `NAME.json` — the icon index (1×)
- 🖼️ `NAME@2x.png` — the sprite atlas image (2× / high-DPI)
- 🧩 `NAME@2x.json` — the icon index (2× / high-DPI)

> 📝 The JSON maps **icon-name → atlas rectangle + pixelRatio**. The *name* is what your style references (not the file name).

---

## 🔌 How sprites are loaded (style.json)

In a MapLibre/Mapbox style, `sprite` points to the **base URL (no file extension)**:

```json
{
  "version": 8,
  "name": "KFM Style (Legacy)",
  "sprite": "./assets/maps/sprites/legacy/kfm-legacy"
}
```

MapLibre will then request:

- `kfm-legacy.json` + `kfm-legacy.png`
- `kfm-legacy@2x.json` + `kfm-legacy@2x.png` (when needed)

Icons get used by name in layer layout:

```json
{
  "id": "historic-sites",
  "type": "symbol",
  "source": "kfm",
  "layout": {
    "icon-image": "kfm-fort",
    "icon-size": 1
  }
}
```

---

## 🧭 Legacy rules (don’t break old styles)

### ✅ Do

- ✅ Keep **existing icon names stable** (backward compatibility)
- ✅ Use **kebab-case** for new names (example: `kfm-trailhead`)
- ✅ Prefer a `kfm-` prefix to avoid collisions with upstream icon packs
- ✅ Add new icons only when required to support legacy styles

### 🚫 Don’t

- ❌ Rename icons (breaks `icon-image` references)
- ❌ Delete icons that might still be referenced
- ❌ “Clean up” legacy keys unless you also update *every* referencing style/layer
- ❌ Repack/reorder sprites casually (it increases diff noise and risks subtle regressions)

---

## 🛠️ Updating / regenerating sprites

<details>
  <summary><strong>Suggested workflow (tool-agnostic)</strong> 🧰</summary>

1. **Add/modify source artwork** (SVG/PNG) following the project’s icon conventions.
2. **Regenerate** the atlas + index for:
   - 1× (`NAME.png` + `NAME.json`)
   - 2× (`NAME@2x.png` + `NAME@2x.json`)
3. **Replace** the outputs in this folder.
4. **Smoke-test** locally:
   - check icons at multiple zooms
   - check both standard and high-DPI screens
5. **Update provenance** (see licensing section) if any icon source changed.

> 💡 If the repo doesn’t yet have a deterministic sprite build command, consider adding a `Makefile`/script target so regeneration is reproducible.

</details>

<details>
  <summary><strong>Quick “where is this used?” search</strong> 🔎</summary>

From repo root, look for style references:

```bash
grep -R "\"sprite\"" -n web | head
grep -R "\"icon-image\"" -n web | head
```

(Adjust to your environment/tooling.)

</details>

---

## ✅ QA checklist (before committing)

- [ ] Crisp at **1× and 2×** (no blurry edges / no accidental scaling)
- [ ] Consistent padding (avoid icons “touching” atlas neighbors)
- [ ] Works on **light + dark** basemaps (no unintended hard-coded colors)
- [ ] Anchor/offset behavior is sane (especially if styles use `icon-anchor` / `icon-offset`)
- [ ] Naming matches conventions (`kebab-case`, preferably `kfm-` prefix)
- [ ] No accidental breaking changes to existing icon keys

---

## 🧾 Licensing & provenance (icons are “data” too)

KFM emphasizes being **explicit and careful about licensing** across the project—sprite artwork should follow the same discipline.

**When adding or modifying an icon, capture:**
- 📌 Source (URL / archive / author)
- 📜 License (CC-BY, Public Domain, custom terms, etc.)
- ✂️ Modifications (resized, recolored, simplified, etc.)
- 🧾 Any required attribution text

> ✅ Practical suggestion: maintain an **icon attribution manifest** (file name + icon key → source + license).  
> If one already exists elsewhere in the repo, keep using it. If not, consider adding one near sprite sources.

---

## 🗂️ Folder map

```text
📁 web/
  📁 assets/
    📁 maps/
      📁 sprites/
        📁 legacy/
          🧾 README.md
          🖼️  NAME.png
          🧩  NAME.json
          🖼️  NAME@2x.png
          🧩  NAME@2x.json
```

---

## 🔎 Sources & project context

- The KFM front-end viewer is described as a **static site** under `web/` using MapLibre/Leaflet (and built for GitHub Pages-style hosting). [oai_citation:0‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)
- KFM’s licensing stance: **code is MIT licensed**, while **data/content may have their own licenses** and should be handled transparently. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- KFM explicitly highlights careful license handling to avoid conflicts and enable adoption/collaboration. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)