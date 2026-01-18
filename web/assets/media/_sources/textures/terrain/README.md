# 🏔️ Terrain Texture Sources (Authoring Library)

![scope](https://img.shields.io/badge/scope-terrain_textures-2ea44f)
![status](https://img.shields.io/badge/status-source_only-informational)
![provenance](https://img.shields.io/badge/provenance-required-blue)
![license](https://img.shields.io/badge/license-required-orange)

> 📌 **This folder is for _source / authoring-quality_ terrain textures** (lossless or near-lossless, high-res, editable).
>
> ✅ Use these to **generate optimized runtime textures** (WebP/KTX2/PNG atlases, etc.) that ship to the browser.  
> ❌ Do **not** import directly from `_sources/` in production UI code.

---

## 🧭 Why this exists (KFM fit)

KFM’s web UI supports 2D/3D mapping (MapLibre + optional Cesium terrain/globe). Terrain materials and “detail” surfaces (dirt/grass/rock/sand, hillshade-like overlays, etc.) need a **clean, traceable asset pipeline**.

KFM’s core rule of thumb applies here too:

- 🧾 **No “mystery layers”**: anything visible should be traceable to sources & processing.
- ⚖️ **Licensing is first-class**: every texture set needs clear usage rights and attribution.
- 🧬 **Provenance-first**: if a texture represents *evidence* (derived from DEM/imagery), treat it like a dataset artifact, not “just a graphic”.

---

## 🗂️ Directory layout

Recommended structure per texture set (keep it boring + repeatable 😄):

```text
web/assets/media/_sources/textures/terrain/
├── README.md
└── <set_slug>/
    ├── meta/
    │   ├── texture.contract.json      # required ✅ (license + provenance)
    │   ├── texture.prov.json          # optional 🧬 (deeper lineage)
    │   └── LICENSE.txt                # required ✅ (or link to canonical license)
    ├── src/                           # source maps (authoring quality)
    │   ├── <set_slug>__albedo.png
    │   ├── <set_slug>__normal.png
    │   ├── <set_slug>__roughness.png
    │   ├── <set_slug>__height.tif     # optional (prefer 16-bit)
    │   └── <set_slug>__ao.png         # optional
    └── previews/
        ├── preview.jpg                # optional but recommended 📸
        └── preview.md                 # optional notes (scale, tiling tips)
```

> 💡 If your repo already uses a different convention, **don’t fight it**—adapt the README to match reality.  
> But keep the **metadata + license** requirement unchanged.

---

## 🧱 Texture set definition

A **terrain texture set** is a folder containing one material surface (or one “theme”) and its maps.

### ✅ Required maps (baseline PBR)

| Map | Suffix | Color space | Notes |
|---|---|---:|---|
| Base color | `__albedo` | sRGB | No baked shadows / lighting |
| Normal | `__normal` | Linear | Prefer OpenGL (+Y) unless noted |
| Roughness | `__roughness` | Linear | “Roughness” (not “gloss”) |

### 🧩 Optional maps (use when you need them)

| Map | Suffix | Recommended | Notes |
|---|---|---:|---|
| Height / displacement | `__height` | 16-bit TIFF/PNG | Avoid banding; document units |
| Ambient occlusion | `__ao` | 8-bit ok | Only if you’re sure it won’t double-darken |
| Splat / weight map | `__weights` | 8-bit ok | RGBA = blend weights (document channels!) |

---

## 🎨 Authoring rules (quality guardrails)

### Tiling & seams 🧵
- Must tile cleanly in both axes (unless explicitly “non-tiling”).
- No obvious repeating landmarks (logos, text, unique objects).
- Avoid hard edges that create “grid” artifacts at distance.

### Resolution & aspect 📐
- Prefer power-of-two (1024 / 2048 / 4096).
- Keep maps in a set at the same resolution (unless justified in metadata).

### Color management 🌈
- `albedo` = **sRGB**
- `normal`, `roughness`, `ao`, `height`, `weights` = **linear**
- If any map uses unusual encoding (e.g., packed channels), **document it**.

### Normal map convention 🧭
- Default expectation: **OpenGL normal maps** (Y+ / “green up”).
- If you provide DirectX (Y-), **call it out** in `texture.contract.json`.

---

## 🏷️ Naming conventions

**Folder name:** `kebab-case` only  
**File name:** `<set_slug>__<map>.<ext>`

Examples:
- `flint-hills-limestone/flint-hills-limestone__albedo.png`
- `prairie-dirt/prairie-dirt__normal.png`

> ✅ Stable names = stable URLs + stable cache keys.

---

## 🧾 Provenance & licensing (non-negotiable)

Each set **must** include:

- `meta/texture.contract.json` ✅  
- `meta/LICENSE.txt` ✅ (or a pointer to canonical license text)

Minimum required fields (keep it simple, but complete):

```json
{
  "id": "terrain.flint-hills-limestone.v1",
  "title": "Flint Hills Limestone (Tiling PBR Set)",
  "description": "Tiling limestone surface for Kansas Flint Hills terrain material blending.",
  "license": "CC-BY-4.0",
  "attribution": {
    "author": "Name / Org",
    "required_credit_line": "Author Name — CC BY 4.0"
  },
  "sources": [
    {
      "type": "photogrammetry|procedural|scan|derived",
      "source_url": "https://example.com/source",
      "retrieved": "2026-01-18"
    }
  ],
  "technical": {
    "normal_convention": "opengl",
    "tileable": true,
    "recommended_world_scale_m": 2.0,
    "maps": {
      "albedo": "src/flint-hills-limestone__albedo.png",
      "normal": "src/flint-hills-limestone__normal.png",
      "roughness": "src/flint-hills-limestone__roughness.png"
    }
  }
}
```

### Evidence vs. decorative textures 🔍
Use this quick test:

- **Decorative material** (grass/dirt/rock used purely for shading)  
  ✅ store here with license + attribution  
  ➕ provenance is still required, but can be minimal

- **Evidence texture** (derived from DEM, historic map raster, satellite imagery, hillshade, etc.)  
  ✅ store here for authoring  
  ✅ **also** register the artifact in KFM’s catalogs (STAC/DCAT/PROV) per the project standards  
  ✅ treat processing steps as reproducible (config + logs)

---

## 🛠️ Optimization targets (runtime-friendly)

This folder intentionally stores “heavy” sources. Runtime should prefer:

- GPU-compressed textures (e.g., **KTX2/Basis**) for 3D
- Web-friendly fallbacks (WebP/PNG) when needed
- Mipmaps + sane max resolution (avoid shipping 8K unless justified)

> 🎯 Goal: keep the 3D terrain view crisp **without** punishing network + mobile GPUs.

---

## ✅ Contribution checklist (PR-ready)

- [ ] New set folder uses `kebab-case` slug
- [ ] Includes `meta/texture.contract.json`
- [ ] Includes `meta/LICENSE.txt` (or explicit license pointer)
- [ ] Albedo has **no baked lighting**
- [ ] Normal map convention documented
- [ ] Files are tileable (if marked tileable)
- [ ] `previews/preview.jpg` added (recommended)
- [ ] If evidence-derived: linked/registered with the appropriate KFM metadata standards

---

## 🔗 Related KFM docs (start here)

- 📘 `docs/MASTER_GUIDE_v13.md` — contracts, pipeline ordering, provenance-first
- 🧱 `docs/standards/` — STAC/DCAT/PROV profiles (governed)
- ⚖️ `docs/governance/` — ethics, sovereignty, review gates
- 🌍 KFM technical documentation (architecture + UI stack)

---

## 🧩 FAQ

<details>
  <summary><strong>Why store textures under <code>_sources/</code>?</strong> 🤔</summary>

Because source assets are typically **too large / too raw** for direct web delivery.  
Keeping them separate prevents accidental imports and clarifies what must be optimized before shipping.
</details>

<details>
  <summary><strong>Can we include “non-commercial” licensed textures?</strong> ⚖️</summary>

Prefer permissive licenses. If you *must* include restricted assets, isolate them clearly, document limits,
and ensure they don’t ship in public builds unless policy explicitly allows it.
</details>

<details>
  <summary><strong>Where should generated/optimized textures live?</strong> 📦</summary>

Wherever the frontend build expects them (often **outside** of `_sources/`).  
If no convention exists yet, create one and document it here so future contributors don’t guess.
</details>

---

🧠 _KFM principle reminder:_ if it shows up in the UI, it should be explainable, attributable, and traceable.
